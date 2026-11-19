"""Tests for lib/rules.py and the fail-closed behaviour of lib.check.main. Every rule has a failing and a passing fixture."""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from shutil import copytree
from unittest import mock

from lib import check, readme, rules
from lib.component import ROOT

FIX = Path(__file__).parent / "fixtures" / "Acme" / "LDO1"


def write(path, text=""):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def mini_repo(tmp):
    """A repo root that passes every repo-level and wiring rule for components/Acme/X."""
    root = Path(tmp)
    write(root / "pcb.toml", '[workspace]\nrepository = "x"\npcb-version = "0.4"\n')
    write(root / "components/Acme/X/component.toml")
    write(root / "components/Acme/X/pcb.toml")
    write(root / "tests/zen/X_harness.zen", 'U = Module("./X.zen")\n')
    write(root / "tests/test_zen.py", 'CASES = [\n    ("Acme/X", "nominal", [], "pass", ""),\n]\n')
    write(root / "README.md", "| Acme X | thing | [README](components/Acme/X/README.md) |\n")
    return root


def rules_of(findings):
    return sorted({f.rule for f in findings})


class TestAllowlist(unittest.TestCase):
    F = rules.Finding("cite-format", "Acme/X", "param a", "msg")

    def entry(self, **kw):
        e = {"part": "Acme/X", "location": "param a", "rule": "cite-format", "reason": "r", "found": "2026-11-17"}
        return {**e, **kw}

    def test_exact_match_is_allowed(self):
        bad, ok, stale = rules.apply_allowlist([self.F], [self.entry()])
        self.assertEqual((bad, len(ok), stale), ([], 1, []))

    def test_unlisted_violation_fails(self):
        bad, ok, stale = rules.apply_allowlist([self.F], [self.entry(location="param b")])
        self.assertEqual(bad, [self.F])
        self.assertEqual(len(stale), 1)  # and the entry that matched nothing is stale

    def test_stale_entry_is_reported(self):
        bad, ok, stale = rules.apply_allowlist([], [self.entry()])
        self.assertEqual((bad, ok, len(stale)), ([], [], 1))

    def test_entry_missing_field_is_error(self):
        with tempfile.TemporaryDirectory() as d:
            path = write(Path(d) / "k.toml", '[[finding]]\npart = "a"\nrule = "b"\n')
            with self.assertRaises(ValueError):
                rules.load_allowlist(path)

    def test_missing_file_is_error(self):
        with self.assertRaises(FileNotFoundError):
            rules.load_allowlist(Path("/nonexistent/known_findings.toml"))

    def test_committed_allowlist_loads(self):
        self.assertTrue(all(e["found"] == "2026-11-17" for e in rules.load_allowlist()))

    def test_message_roundtrip(self):
        self.assertEqual(rules.split_message(rules.text(self.F)), ("cite-format", "param a"))
        self.assertIsNone(rules.split_message("pin 3: name mismatch"))


class TestVerificationProvenance(unittest.TestCase):
    def test_explicit_types_require_a_valid_stamp(self):
        data = {"param": {"vref": {
            "verified": "abrown 2026-11-19 page-image review",
            "verification_type": "human_page_image",
        }}}
        self.assertEqual(rules.verified_findings(data), [])

    def test_rejects_unknown_or_orphaned_types(self):
        unknown = rules.verified_findings({"param": {"vref": {
            "verified": "abrown 2026-11-19 page-image review",
            "verification_type": "text_check",
        }}})
        self.assertEqual([finding.rule for finding in unknown], ["verification-type"])
        orphaned = rules.verified_findings({"param": {"vref": {
            "verification_type": "human_page_image",
        }}})
        self.assertEqual([finding.rule for finding in orphaned], ["verification-type"])

    def test_legacy_stamp_remains_accepted(self):
        self.assertEqual(rules.verified_findings({"param": {
            "vref": {"verified": "sonnet-audit 2026-11-18 cross-model page-image review"},
        }}), [])


class TestMain(unittest.TestCase):
    def run_main(self, argv, components, others=(), wiring=()):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), \
                mock.patch.object(check, "find_components", return_value=components), \
                mock.patch.object(check, "check_component", return_value=list(others)), \
                mock.patch.object(rules, "wiring_findings", return_value=list(wiring)), \
                mock.patch.object(check, "abstentions", return_value=[]):
            rc = check.main(argv)
        return rc, out.getvalue()

    def test_zero_components_fails(self):
        rc, out = self.run_main([], [])
        self.assertEqual(rc, 1)
        self.assertIn("no components found", out)

    def test_clean_component_passes(self):
        rc, out = self.run_main(["x"], [Path("components/Acme/LDO1")])
        self.assertEqual(rc, 0, out)

    def test_warning_fails_exit_code(self):
        rc, out = self.run_main(["x"], [Path("components/Acme/LDO1")], others=[("WARN", "calc.py has no INPUTS")])
        self.assertEqual(rc, 1)
        self.assertIn("1 warnings", out)

    def test_missing_datasheet_is_tolerated_and_counted(self):
        warn = ("WARN", "datasheet_file not found: docs/datasheets/a.pdf (PDFs are not committed)")
        rc, out = self.run_main(["x"], [Path("components/Acme/LDO1")], others=[warn])
        self.assertEqual(rc, 0, out)
        self.assertIn("0 warnings, 1 tolerated (datasheets absent)", out)

    def test_wiring_finding_fails(self):
        f = rules.Finding("harness-missing", "Acme/LDO1", "tests/zen", "no harness")
        rc, out = self.run_main(["x"], [Path("components/Acme/LDO1")], wiring=[f])
        self.assertEqual(rc, 1)
        self.assertIn("[harness-missing]", out)

    def test_no_other_warning_in_the_repo_today(self):
        """Every committed component passes with 0 warnings (the datasheet_file warning is the only tolerated one)."""
        for folder in check.find_components([]):
            warns = [m for lvl, m in check.check_component(folder, raw=True) if lvl == "WARN" and check.TOLERATED not in m]
            self.assertEqual(warns, [], folder.name)

    def test_real_repo_passes_with_no_stale_entries(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = check.main([])
        self.assertEqual(rc, 0, out.getvalue())
        self.assertNotIn("stale", out.getvalue())


class TestRepoRules(unittest.TestCase):
    def test_good_repo_passes(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(rules.repo_findings(mini_repo(d)), [])

    def test_pdf_under_components(self):
        with tempfile.TemporaryDirectory() as d:
            root = mini_repo(d)
            write(root / "components/Acme/X/ds.PDF", "x")
            f = rules.repo_findings(root)
            self.assertEqual([(x.rule, x.part) for x in f], [("no-pdf", "components/Acme/X/ds.PDF")])

    def test_pdf_outside_components_is_fine(self):
        with tempfile.TemporaryDirectory() as d:
            root = mini_repo(d)
            write(root / "docs/datasheets/ds.pdf", "x")
            self.assertEqual(rules.repo_findings(root), [])

    def test_pcb_version_forms(self):
        for version, ok in (("0.4", True), ("0.4.95", False), ("0", False), ("v0.4", False)):
            with tempfile.TemporaryDirectory() as d:
                root = mini_repo(d)
                write(root / "pcb.toml", f'[workspace]\npcb-version = "{version}"\n')
                self.assertEqual(rules.repo_findings(root) == [], ok, version)

    def test_pcb_version_missing_or_no_root_toml(self):
        with tempfile.TemporaryDirectory() as d:
            root = mini_repo(d)
            write(root / "pcb.toml", '[workspace]\nrepository = "x"\n')
            self.assertEqual(rules_of(rules.repo_findings(root)), ["pcb-version"])
            (root / "pcb.toml").unlink()
            self.assertEqual(rules_of(rules.repo_findings(root)), ["pcb-version"])

    def test_nested_workspace_found_in_hidden_dir(self):
        with tempfile.TemporaryDirectory() as d:
            root = mini_repo(d)
            write(root / ".hidden/sub/pcb.toml", "[workspace]\n")
            f = rules.repo_findings(root)
            self.assertEqual([(x.rule, x.part) for x in f], [("nested-workspace", ".hidden/sub/pcb.toml")])

    def test_tool_cache_and_git_are_skipped(self):
        with tempfile.TemporaryDirectory() as d:
            root = mini_repo(d)
            write(root / ".pcb/stdlib/pcb.toml", "[workspace]\n")
            write(root / ".git/x/pcb.toml", "[workspace]\n")
            self.assertEqual(rules.repo_findings(root), [])

    def test_component_pcb_toml_must_be_empty(self):
        with tempfile.TemporaryDirectory() as d:
            root = mini_repo(d)
            write(root / "components/Acme/X/pcb.toml", "[dependencies]\n")
            self.assertEqual(rules_of(rules.repo_findings(root)), ["component-pcb-toml-empty"])


class TestWiring(unittest.TestCase):
    def run_rule(self, mutate=None):
        with tempfile.TemporaryDirectory() as d:
            root = mini_repo(d)
            if mutate:
                mutate(root)
            return rules.wiring_findings(root / "components/Acme/X", root)

    def test_complete_wiring_passes(self):
        self.assertEqual(self.run_rule(), [])

    def test_missing_harness(self):
        self.assertEqual(rules_of(self.run_rule(lambda r: (r / "tests/zen/X_harness.zen").unlink())), ["harness-missing"])

    def test_missing_cases_row(self):
        f = self.run_rule(lambda r: write(r / "tests/test_zen.py", 'CASES = [\n    ("Acme/Y", "n", [], "pass", ""),\n]\n'))
        self.assertEqual(rules_of(f), ["cases-row"])

    def test_missing_cases_variable_or_file_fails_closed(self):
        self.assertEqual(rules_of(self.run_rule(lambda r: write(r / "tests/test_zen.py", "X = 1\n"))), ["cases-row"])
        self.assertEqual(rules_of(self.run_rule(lambda r: (r / "tests/test_zen.py").unlink())), ["cases-row"])

    def test_missing_readme_row(self):
        self.assertEqual(rules_of(self.run_rule(lambda r: write(r / "README.md", "| other |\n"))), ["readme-row"])
        self.assertEqual(rules_of(self.run_rule(lambda r: (r / "README.md").unlink())), ["readme-row"])


class TestCite(unittest.TestCase):
    def cites(self, *cites):
        data = {"pin": [{"number": "1", "cite": c} for c in cites]}
        return rules.cite_findings(data)

    def test_accepted_forms(self):
        self.assertEqual(self.cites("DS p.6, 7.5 Electrical Characteristics, VOSI", "DS PDF p.12, drawing PKG-1",
                                    "DS p.5-6, Table 1, row", "DS p.2 (GCM31CR71E475KA55-01A), 2. Land Dimensions, a"), [])

    def test_rejected_forms(self):
        for bad in ("page 5, TC", "DS p.5", "DS p.x, Table", "DS p.5,Table", "DS PDF 5, Table", "ds p.5, Table"):
            self.assertEqual(len(self.cites(bad)), 1, bad)

    def test_cite_sheet_must_be_a_pdf_file(self):
        good = {"param": {"a": {"cite": "DS p.7 (GCM1885C1H101GA16-01A-EN.pdf), Table A, 5C"}}}
        bad = {"param": {"a": {"cite": "DS p.7 (C0G sheet of GCM1885C1H101GA16), Table A, 5C"}}}
        self.assertEqual(rules.cite_findings(good), [])  # the bracket form is a valid cite
        self.assertEqual(rules.cite_sheet_findings(good), [])
        self.assertEqual(rules.cite_sheets(good), [("param a", "GCM1885C1H101GA16-01A-EN.pdf")])
        f = rules.cite_sheet_findings(bad)
        self.assertEqual([x.rule for x in f], ["cite-sheet"])
        trav = {"param": {"a": {"cite": "DS p.7 (../secret.pdf), Table A, 5C"}}}
        self.assertEqual([x.rule for x in rules.cite_sheet_findings(trav)], ["cite-sheet"])

    def test_variant_cites_checked(self):
        f = rules.cite_findings({}, {"V1": {"param": {"a": {"cite": "nope"}}}})
        self.assertEqual(f[0].location, "variant V1 param a")


class TestCalcRules(unittest.TestCase):
    def calc(self, body):
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        return write(Path(d.name) / "calc.py", body)

    def test_inputs_coverage(self):
        from lib.component import load_calc
        good = load_calc(self.calc("def f(x):\n    return x\n\n\ndef _h(x):\n    return x\n\n\nINPUTS = {'f': {}}\n"))
        self.assertEqual(rules.inputs_coverage_findings(good), [])
        bad = load_calc(self.calc("def f(x):\n    return x\n\n\ndef g(x):\n    return x\n\n\nINPUTS = {'f': {}}\n"))
        self.assertEqual([f.location for f in rules.inputs_coverage_findings(bad)], ["g"])

    def test_imported_functions_are_not_public_functions(self):
        from lib.component import load_calc
        calc = load_calc(self.calc("from math import sqrt\n\n\nINPUTS = {}\n"))
        self.assertEqual(rules.inputs_coverage_findings(calc), [])

    def test_loose_tolerance_needs_comment(self):
        loose = 'EXAMPLES = [\n    ("f", {"x": 1}, 2.0, 0.02, "DS p.1, t, r"),\n]\n'
        self.assertEqual(len(rules.example_comment_findings(self.calc(loose))), 1)

    def test_loose_tolerance_with_comments_passes(self):
        same = 'EXAMPLES = [\n    ("f", {"x": 1}, 2.0, 0.02, "DS p.1, t, r"),  # DS rounds to E96\n]\n'
        prev = 'EXAMPLES = [\n    # DS rounds to E96\n    ("f", {"x": 1}, 2.0, 0.02, "DS p.1, t, r"),\n]\n'
        multi = 'EXAMPLES = [\n    ("f", {"x": 1}, 2.0,\n     0.02,  # DS rounds\n     "DS p.1, t, r"),\n]\n'
        for text in (same, prev, multi):
            self.assertEqual(rules.example_comment_findings(self.calc(text)), [], text)

    def test_tight_tolerance_needs_no_comment(self):
        tight = 'EXAMPLES = [\n    ("f", {"x": 1}, 2.0, 1e-3, "DS p.1, t, r"),\n]\n'
        self.assertEqual(rules.example_comment_findings(self.calc(tight)), [])

    def test_check_component_reports_both(self):
        with tempfile.TemporaryDirectory() as d:
            copy = Path(d) / "LDO1"
            copytree(FIX, copy)
            calc = copy / "calc.py"
            calc.write_text(calc.read_text() + "\n\ndef extra(x):\n    return x\n")
            text = "\n".join(m for _, m in check.check_component(copy))
            self.assertIn("[inputs-coverage] extra:", text)


class TestKicadRules(unittest.TestCase):
    def sym(self, at):
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        text = (FIX / "LDO1.kicad_sym").read_text().replace("(at -5.08 2.54 0)", f"(at {at} 0)")
        return write(Path(d.name) / "s.kicad_sym", text)

    def test_grid_pass_and_fail(self):
        self.assertEqual(rules.symbol_grid_findings(FIX / "LDO1.kicad_sym"), [])
        self.assertEqual(rules.symbol_grid_findings(self.sym("-7.62 5.08")), [])
        f = rules.symbol_grid_findings(self.sym("-5.08 1.27"))
        self.assertEqual([x.location for x in f], ["pin 1"])
        self.assertEqual(rules.symbol_grid_findings(self.sym("-5.082 2.54")), [])  # within 0.005 mm

    def footprint(self, crt, extra=""):
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        x0, y0, x1, y1 = crt
        text = ('(footprint "F" (version 20241229)\n'
                '  (pad "1" smd rect (at -1 0) (size 1 2) (layers "F.Cu"))\n'
                '  (pad "2" smd rect (at 1 0) (size 1 2) (layers "F.Cu"))\n'
                '  (fp_rect (start -2 -1) (end 2 1) (stroke (width 0.1) (type solid)) (layer "F.Fab"))\n'
                f'  (fp_rect (start {x0} {y0}) (end {x1} {y1}) (stroke (width 0.05) (type solid)) (layer "F.CrtYd"))\n'
                f"{extra})\n")
        return write(Path(d.name) / "f.kicad_mod", text)

    def test_courtyard_pass(self):
        # pads and body span x -2..2 (pads 0.5..1.5 +- 0.5), y -1..1; courtyard exactly 0.25 beyond
        found, abstain = rules.courtyard_findings(self.footprint((-2.25, -1.25, 2.25, 1.25)))
        self.assertEqual((found, abstain), ([], None))

    def test_courtyard_tolerance(self):
        self.assertEqual(rules.courtyard_findings(self.footprint((-2.246, -1.25, 2.25, 1.25)))[0], [])

    def test_courtyard_too_tight_fails_per_side(self):
        found, _ = rules.courtyard_findings(self.footprint((-2.2, -1.25, 2.25, 1.1)))
        self.assertEqual(sorted(f.location for f in found), ["xmin", "ymax"])

    def test_courtyard_uses_single_body_rectangle(self):
        # one closed F.Fab rectangle larger than the pads in y: a courtyard hugging the pads only fails on that body
        text = self.footprint((-2.25, -1.25, 2.25, 1.25)).read_text().replace("(start -2 -1) (end 2 1)", "(start -2 -3) (end 2 3)")
        path = write(self.footprint((0, 0, 1, 1)).parent / "b.kicad_mod", text)
        found, abstain = rules.courtyard_findings(path)
        self.assertEqual((sorted(f.location for f in found), abstain), (["ymax", "ymin"], None))

    def test_murata_plate_drawing_is_not_a_body(self):
        """F.Fab holds a plate drawing (3 closed rectangles, one enclosing the pad centres) wider in y than the real body.
        The courtyard is exactly 0.25 over the pads: PASS, body abstained, pads still checked."""
        def rect(x0, y0, x1, y1):
            e = '(stroke (width 0.0254) (type solid)) (layer "F.Fab")'
            return (f'  (fp_line (start {x0} {y0}) (end {x1} {y0}) {e})\n  (fp_line (start {x1} {y0}) (end {x1} {y1}) {e})\n'
                    f'  (fp_line (start {x1} {y1}) (end {x0} {y1}) {e})\n  (fp_line (start {x0} {y1}) (end {x0} {y0}) {e})\n')
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        cy = (-1.55, -0.9, 1.55, 0.9)
        text = ('(footprint "M" (version 20241229)\n'
                '  (pad "1" smd rect (at -0.95 0) (size 0.7 1.3) (layers "F.Cu"))\n'
                '  (pad "2" smd rect (at 0.95 0) (size 0.7 1.3) (layers "F.Cu"))\n'
                + rect(-1.0795, -0.6985, -0.3429, 0.6985) + rect(0.3429, -0.6985, 1.0795, 0.6985)
                + rect(-1.0795, -0.6985, 1.0795, 0.6985)
                + '  (fp_rect (start -1.55 -0.9) (end 1.55 0.9) (stroke (width 0.05) (type solid)) (layer "F.CrtYd"))\n)\n')
        path = write(Path(d.name) / "m.kicad_mod", text)
        found, abstain = rules.courtyard_findings(path)
        self.assertEqual(found, [])
        self.assertIn("body not checked", abstain)
        tight = write(Path(d.name) / "t.kicad_mod", text.replace("(start -1.55 -0.9) (end 1.55 0.9)", "(start -1.55 -0.85) (end 1.55 0.9)"))
        self.assertEqual([f.location for f in rules.courtyard_findings(tight)[0]], ["ymin"])  # pads are still checked

    def test_courtyard_abstains(self):
        arc = '  (fp_arc (start 0 0) (mid 1 1) (end 2 0) (stroke (width 0.1) (type solid)) (layer "F.CrtYd"))\n'
        found, abstain = rules.courtyard_findings(self.footprint((-9, -9, 9, 9), arc))
        self.assertEqual(found, [])
        self.assertIn("arc", abstain)
        custom = self.footprint((-9, -9, 9, 9)).read_text().replace("smd rect (at -1 0)", "smd custom (at -1 0)")
        path = write(self.footprint((-9, -9, 9, 9)).parent / "c.kicad_mod", custom)
        self.assertIn("custom", rules.courtyard_findings(path)[1])
        rotated = custom.replace("smd custom (at -1 0)", "smd rect (at -1 0 45)")
        path = write(path.parent / "r.kicad_mod", rotated)
        self.assertIn("rotated", rules.courtyard_findings(path)[1])
        nocrt = write(path.parent / "n.kicad_mod", '(footprint "F"\n  (pad "1" smd rect (at 0 0) (size 1 1) (layers "F.Cu"))\n)\n')
        self.assertEqual(rules.courtyard_findings(nocrt), ([], "no F.CrtYd graphics"))

    def test_rotated_pad_swaps_size(self):
        text = self.footprint((-2.25, -1.25, 2.25, 1.25)).read_text().replace("(at 1 0) (size 1 2)", "(at 1 0 90) (size 1 2)")
        path = write(self.footprint((0, 0, 1, 1)).parent / "q.kicad_mod", text)
        # pad 2 becomes 2 wide, 1 tall: x extent 0..2, so the fab (x -2..2) still binds and the courtyard passes
        self.assertEqual(rules.courtyard_findings(path)[0], [])


class TestZenLint(unittest.TestCase):
    def lint(self, wrapper="", harness=""):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            write(root / "components/Acme/X/X.zen", wrapper)
            write(root / "tests/zen/X_harness.zen", harness)
            return rules.zen_lint_findings(root)

    def test_clean(self):
        self.assertEqual(self.lint('x = 1  # sqrt( in a comment\n', 'U = Module("./X.zen")\nta = "-40°C to 85°C"\nv = "0V to 5V"\n'), [])

    def test_module_escape(self):
        for path in ("../X.zen", "./../X.zen"):
            f = self.lint(harness=f'U = Module("{path}")\n')
            self.assertEqual(rules_of(f), ["zen-module-path"], path)

    def test_module_in_wrapper_also_checked(self):
        self.assertEqual(rules_of(self.lint(wrapper='U = Module("../X.zen")\n')), ["zen-module-path"])

    def test_temperature_unit_on_one_end(self):
        for rng in ("-40 to 85°C", "-40°C to 85", "0 to 70 degC"):
            f = self.lint(harness=f'ta = "{rng}"\n')
            self.assertEqual(rules_of(f), ["zen-temp-unit"], rng)

    def test_unitless_or_voltage_ranges_not_flagged(self):
        self.assertEqual(self.lint(harness='a = "1 to 2"\nb = "0V to 130mV"\n'), [])

    def test_sqrt_and_pow_in_wrapper(self):
        self.assertEqual(rules_of(self.lint(wrapper="x = sqrt(2)\n")), ["zen-no-sqrt-pow"])
        self.assertEqual(rules_of(self.lint(wrapper="x = 2 ** 3\n")), ["zen-no-sqrt-pow"])

    def test_harness_may_use_kwargs_unpacking(self):
        self.assertEqual(self.lint(harness="U(**({} if a else {'b': 1}))\n"), [])


class TestGeneratedCurrency(unittest.TestCase):
    def test_committed_readmes_equal_generator_output(self):
        folders = check.find_components([])
        self.assertTrue(folders, "no components found")
        for folder in folders:
            committed = (folder / "README.md").read_text(encoding="utf-8")
            self.assertEqual(readme.build(folder), committed, f"{folder.name}/README.md is stale: run python3 -m lib.readme")

    def test_stale_readme_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            copy = Path(d) / "LDO1"
            copytree(FIX, copy)
            (copy / "README.md").write_text(readme.build(copy), encoding="utf-8")
            self.assertEqual(readme.build(copy), (copy / "README.md").read_text(encoding="utf-8"))
            toml = copy / "component.toml"
            toml.write_text(toml.read_text().replace('unit = "mV"', 'unit = "V"', 1))
            self.assertNotEqual(readme.build(copy), (copy / "README.md").read_text(encoding="utf-8"))

    def test_root_readme_is_hand_written(self):
        """lib.readme writes only component READMEs; the root README parts table is checked by the readme-row rule."""
        self.assertTrue((ROOT / "README.md").exists())


if __name__ == "__main__":
    unittest.main()
