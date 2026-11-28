"""lib/equations.py and tools/equations.py on a temp fixture (docs/spec/equations.md). Nothing here touches the repo's
own equations.toml; stamps are written into the temp copy only."""
import datetime
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from lib import equations as E  # noqa: E402
from lib import check  # noqa: E402
from lib import readme  # noqa: E402

CALC = '''"""Fixture calc."""


def power(i, r):
    """Not a DS equation: P = I^2 R."""
    # a comment
    return i * i * r


def gain(rg):
    """G = 1 + 49.4 kohm / RG. DS p.20 Equation 1."""
    return 1 + 49.4e3 / rg


EXAMPLES = [
    ("gain", {"rg": 5.49e3}, 9.998, 1e-3, "DS p.20, Table 8-1, G = 10 row"),
]
'''

TOML = r"""[equation.power]
title = "Power in a resistor"
kind = "derived"
latex = [
  'P = I^{2}\,R',
]
cite = "not a datasheet equation; physical relation"
reuse_search = "find: power resistor current -> none found"

[equation.power.symbols]
i = { tex = 'I', meaning = "current", unit = "A" }
r = { tex = 'R', meaning = "resistance", unit = "ohm" }
result = { tex = 'P', meaning = "power", unit = "W" }

[equation.gain]
title = "Gain of the fixture amplifier"
kind = "datasheet"
latex = [
  'G = 1 + \dfrac{49.4\,\mathrm{k\Omega}}{R_G}',
]
cite = "DS p.20, Equation 1"
reuse_search = "find: gain amplifier -> none found"

[equation.gain.symbols]
rg = { tex = 'R_G', meaning = "gain resistor", unit = "ohm" }
result = { tex = 'G', meaning = "gain", unit = "V/V" }
"""

DAY = datetime.date(2026, 11, 28)


class Fixture(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.object(E, "RUNNING_PYTHON", E.PINNED_PYTHON)  # states are tested as on the pinned Python
        patcher.start()
        self.addCleanup(patcher.stop)
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.dir = self.root / "components" / "Mfr" / "Fx"
        self.dir.mkdir(parents=True)
        self.write(CALC, TOML)

    def write(self, calc=None, toml=None):
        if calc is not None:
            (self.dir / "calc.py").write_text(calc, encoding="utf-8")
        if toml is not None:
            (self.dir / "equations.toml").write_text(toml, encoding="utf-8")

    def edit(self, old, new, which="toml"):
        f = self.dir / ("equations.toml" if which == "toml" else "calc.py")
        text = f.read_text(encoding="utf-8")
        self.assertIn(old, text)
        f.write_text(text.replace(old, new, 1), encoding="utf-8")

    def eqs(self, import_module=False):
        return {e.fn: e for e in E.load_folder(self.dir, import_module)}

    def hash(self, fn="power"):
        return self.eqs()[fn].hash

    def stamp(self, fn, who="alice"):
        eq = self.eqs()[fn]
        E.write_stamp(eq.toml, fn, E.stamp_line(eq, who, DAY))


class Hash(Fixture):
    def test_loads_new_with_ids(self):
        eqs = self.eqs()
        self.assertEqual(sorted(eqs), ["gain", "power"])
        self.assertEqual(eqs["power"].id, "Fx.power")
        self.assertEqual({e.state for e in eqs.values()}, {"NEW"})
        self.assertEqual(eqs["power"].ref, "Fx:power")

    def test_hash_changes_on_equation_text_symbol_cite_and_code(self):
        base = self.hash()
        for old, new in [("P = I^{2}", "P = I^{3}"), ("meaning = \"current\"", "meaning = \"amps\""),
                         ("physical relation", "other relation"), ("title = \"Power", "title = \"Heat")]:
            self.write(CALC, TOML)
            self.edit(old, new)
            self.assertNotEqual(self.hash(), base, old)
        self.write(CALC, TOML)
        self.edit("return i * i * r", "return i * i * r * 2", "calc")
        self.assertNotEqual(self.hash(), base)

    def test_hash_unchanged_on_comment_and_formatting(self):
        base = self.hash()
        self.edit("    # a comment\n    return i * i * r", "    return (i *   i)*r  # moved comment", "calc")
        self.edit("def power(i, r):", "def power( i,r ):", "calc")
        self.assertEqual(self.hash(), base)

    def test_docstring_edit_leaves_hash_unchanged(self):
        base = self.hash()
        self.edit('"""Not a DS equation: P = I^2 R."""', '"""Rewritten prose.\n\n    More lines."""', "calc")
        self.assertEqual(self.hash(), base)
        self.edit('    """Rewritten prose.\n\n    More lines."""\n', "", "calc")  # no docstring at all
        self.assertEqual(self.hash(), base)
        self.edit("return i * i * r", "return i * i * r + 1", "calc")
        self.assertNotEqual(self.hash(), base)

    def test_other_function_edit_does_not_change_hash(self):
        base = self.hash()
        self.edit("49.4e3", "50e3", "calc")
        self.assertEqual(self.hash(), base)

    def test_verified_is_not_hashed(self):
        base = self.hash()
        self.stamp("power")
        self.assertEqual(self.hash(), base)


class Checks(Fixture):
    def test_signature_mismatch_is_fix_first(self):
        self.edit("def power(i, r):", "def power(i, r, k):", "calc")
        eq = self.eqs()["power"]
        self.assertEqual(eq.state, "FIX_FIRST")
        self.assertTrue(any("lack parameter" in m and "k" in m for m in eq.errors), eq.errors)

    def test_extra_symbol_and_missing_result(self):
        self.edit("r = { tex = 'R', meaning = \"resistance\", unit = \"ohm\" }\n",
                  "r = { tex = 'R', meaning = \"resistance\", unit = \"ohm\" }\nz = { tex = 'Z', meaning = \"z\", unit = \"1\" }\n")
        self.assertTrue(any("name no parameter" in m for m in self.eqs()["power"].errors))
        self.write(CALC, TOML)
        self.edit("result = { tex = 'P', meaning = \"power\", unit = \"W\" }\n", "")
        self.assertTrue(any("lack 'result'" in m for m in self.eqs()["power"].errors))

    def test_unquoted_tuple_key_names_the_quoting_slip(self):
        self.write(CALC.replace("return i * i * r", "return i * i * r, i * r"),
                   TOML.replace("result = { tex = 'P', meaning = \"power\", unit = \"W\" }",
                                "result.p = { tex = 'P', meaning = \"power\", unit = \"W\" }\n"
                                "result.v = { tex = 'V', meaning = \"voltage\", unit = \"V\" }"))
        eq = self.eqs()["power"]
        self.assertEqual(eq.state, "FIX_FIRST")
        self.assertTrue(any('quote the key: "result.p"' in m for m in eq.errors), eq.errors)
        self.assertFalse(any("needs tex" in m for m in eq.errors), eq.errors)

    def test_tuple_results_accept_named_elements(self):
        self.write(CALC.replace("return i * i * r", "return i * i * r, i * r"),
                   TOML.replace("result = { tex = 'P', meaning = \"power\", unit = \"W\" }",
                                "\"result.p\" = { tex = 'P', meaning = \"power\", unit = \"W\" }\n"
                                "\"result.v\" = { tex = 'V', meaning = \"voltage\", unit = \"V\" }"))
        self.assertEqual(self.eqs()["power"].errors, [])

    def test_missing_reuse_search_on_new_record_is_flagged(self):
        self.edit('reuse_search = "find: power resistor current -> none found"\n', "")
        eq = self.eqs()["power"]
        self.assertEqual(eq.state, "FIX_FIRST")
        self.assertTrue(any("reuse_search" in m for m in eq.errors))
        self.assertTrue(any("reuse_search" in m for lvl, m in check.equations.check_folder(self.dir)))

    def test_kind_and_cite_rules(self):
        self.edit('kind = "datasheet"', 'kind = "derived"')
        self.assertTrue(any("derived cite" in m for m in self.eqs()["gain"].errors))
        self.write(CALC, TOML)
        self.edit('kind = "derived"', 'kind = "datasheet"')
        errs = self.eqs()["power"].errors
        self.assertTrue(any("not a datasheet equation" in m for m in errs), errs)
        self.assertTrue(any("Not a DS equation" in m for m in errs), errs)

    def test_latex_dollar_unknown_field_and_missing_function(self):
        self.edit("'P = I^{2}\\,R'", "'$P$'")
        self.assertTrue(any("'$'" in m for m in self.eqs()["power"].errors))
        self.write(CALC, TOML)
        self.edit('cite = "DS p.20, Equation 1"', 'cite = "DS p.20, Equation 1"\nbogus = 1')
        self.assertTrue(any("unknown field 'bogus'" in m for m in self.eqs()["gain"].errors))
        self.write(CALC, TOML + "\n[equation.nope]\ntitle = 't'\n")
        self.assertTrue(any("not found" in m for m in self.eqs()["nope"].errors))

    def test_missing_records_lists_public_functions(self):
        self.write(None, TOML.split("\n[equation.gain]")[0] + "\n")
        self.assertEqual(E.missing_records(self.dir / "calc.py", self.dir / "equations.toml"), ["gain"])

    def test_numeric_literal_warning(self):
        self.assertEqual(self.eqs()["power"].warnings, [])
        self.assertEqual(self.eqs()["gain"].warnings, ["49400.0 (line 12)"])

    def test_lib_check_reports_findings_and_passes_clean(self):
        self.assertEqual(E.check_folder(self.dir), [])
        self.edit("def power(i, r):", "def power(i):", "calc")
        out = E.check_folder(self.dir)
        self.assertTrue(out and all(lvl == "ERROR" for lvl, _ in out))

    def test_real_wsk2512_records_have_no_findings(self):
        eqs = E.load_folder(ROOT / "components" / "Vishay" / "WSK2512")
        self.assertEqual(sorted(e.fn for e in eqs), ["dissipation", "rated_power", "resistance_worst", "sense_voltage"])
        self.assertEqual([(e.id, e.errors) for e in eqs if e.errors], [])


class Stamp(Fixture):
    def test_refused_under_claudecode(self):
        eq = self.eqs()["power"]
        self.assertEqual(E.stamp_refusal(eq, "alice", env={"CLAUDECODE": "1"}), E.AGENT)
        self.assertIsNone(E.stamp_refusal(eq, "alice", env={}))

    def test_cli_refused_under_claudecode_and_writes_nothing(self):
        before = (self.dir / "equations.toml").read_text(encoding="utf-8")
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "equations.py"), "--root", str(self.root), "stamp",
                            "--who", "alice", "Fx:power"], capture_output=True, text=True,
                           env={**os.environ, "CLAUDECODE": "1"})
        self.assertEqual(r.returncode, 1)
        self.assertIn("CLAUDECODE", r.stdout)
        self.assertEqual((self.dir / "equations.toml").read_text(encoding="utf-8"), before)

    def test_refused_unless_new_or_stale(self):
        self.assertIsNone(E.stamp_refusal(self.eqs()["power"], "alice", env={}))
        self.write(CALC, TOML.replace('reuse_search = "find: power', 'verified = "machine check"\nreuse_search = "find: power', 1))
        self.assertEqual(self.eqs()["power"].state, "MACHINE_ONLY")
        self.assertIsNone(E.stamp_refusal(self.eqs()["power"], "alice", env={}))  # a human may stamp it
        self.write(CALC, TOML)
        self.stamp("power")
        self.assertIn("HUMAN_VERIFIED", E.stamp_refusal(self.eqs()["power"], "alice", env={}))
        self.edit("def power(i, r):", "def power(i):", "calc")
        why = E.stamp_refusal(self.eqs()["power"], "alice", env={})
        self.assertIn("FIX_FIRST", why)
        self.assertIn("one GitHub login", E.stamp_refusal(self.eqs()["gain"], "al ice", env={}))

    def test_other_python_shows_unknown_warns_and_refuses_stamp(self):
        with mock.patch.object(E, "RUNNING_PYTHON", (3, 11)):
            self.assertIn("3.12", E.version_warning())
            eqs = self.eqs()
            self.assertEqual({e.state for e in eqs.values()}, {"UNKNOWN"})
            self.assertIn("refused", E.stamp_refusal(eqs["power"], "alice", env={}))
            self.assertEqual(E.check_folder(self.dir), [])  # findings are version independent; verify does not fail
            self.assertIn("UNKNOWN", E.page_html(list(eqs.values())))
            self.assertNotIn('class="tick"', E.page_html(list(eqs.values())))
            self.assertIn("WARN", E.page_markdown(list(eqs.values())))
        self.assertIsNone(E.version_warning())

    def test_stamp_made_on_pinned_python_is_unknown_elsewhere_not_verified(self):
        self.stamp("power")
        with mock.patch.object(E, "RUNNING_PYTHON", (3, 14)):
            self.assertEqual(self.eqs()["power"].state, "UNKNOWN")
        self.assertEqual(self.eqs()["power"].state, "HUMAN_VERIFIED")

    def test_stamp_verifies_then_stales_after_code_edit(self):
        self.stamp("power")
        eq = self.eqs()["power"]
        self.assertEqual(eq.state, "HUMAN_VERIFIED")
        self.assertEqual(eq.record["verified"], f"human:alice 2026-11-28 equation-review Fx.power hash {eq.hash[:12]}")
        self.edit("return i * i * r", "return i * i * r * 2", "calc")
        self.assertEqual(self.eqs()["power"].state, "STALE")
        self.assertEqual(E.stamp_refusal(self.eqs()["power"], "alice", env={}), None)

    def test_stale_after_record_edit_and_restamp_replaces_line(self):
        self.stamp("power")
        self.edit("physical relation", "other relation")
        self.assertEqual(self.eqs()["power"].state, "STALE")
        self.stamp("power", who="bob")
        text = (self.dir / "equations.toml").read_text(encoding="utf-8")
        self.assertEqual(text.count("verified ="), 1)
        self.assertEqual(self.eqs()["power"].state, "HUMAN_VERIFIED")
        self.assertEqual(self.eqs()["gain"].state, "NEW")  # the other record is untouched

    def test_stamp_for_other_id_and_machine_stamp(self):
        self.stamp("power")
        self.edit("equation-review Fx.power", "equation-review Fx.gain")
        eq = self.eqs()["power"]
        self.assertEqual(eq.state, "FIX_FIRST")
        self.assertTrue(any("not this equation" in m for m in eq.errors))
        self.write(CALC, TOML.replace('reuse_search = "find: power', 'verified = "machine check 2026-11-28"\nreuse_search = "find: power', 1))
        self.assertEqual(self.eqs()["power"].state, "MACHINE_ONLY")

    def test_other_bytes_kept(self):
        self.stamp("power")
        text = (self.dir / "equations.toml").read_text(encoding="utf-8")
        lines = [ln for ln in text.split("\n") if not ln.startswith("verified =")]
        self.assertEqual("\n".join(lines), TOML)


class Find(Fixture):
    def test_known_match_ranks_first(self):
        eqs = list(self.eqs().values())
        got = E.find(["power", "current"], eqs)
        self.assertEqual(got[0][1].id, "Fx.power")
        self.assertEqual(got[0][0], 2)
        self.assertEqual(E.find(["gain"], eqs)[0][1].id, "Fx.gain")
        self.assertEqual(E.find(["gain", "resistor"], eqs)[0][1].id, "Fx.gain")  # gain matches both terms
        self.assertEqual(E.find(["zzz"], eqs), [])

    def test_limit_and_lines(self):
        eqs = list(self.eqs().values()) * 6
        self.assertEqual(len(E.find(["a"], eqs)), 8)
        self.assertEqual(E.find_lines(["zzz"], eqs), ["no equation matches"])

    def test_searches_latex_unit_and_meaning(self):
        eqs = list(self.eqs().values())
        self.assertEqual(E.find(["dfrac"], eqs)[0][1].id, "Fx.gain")
        self.assertEqual(E.find(["V/V"], eqs)[0][1].id, "Fx.gain")
        self.assertEqual(E.find(["resistance"], eqs)[0][1].id, "Fx.power")

    def test_index_rows(self):
        rows = E.index_rows(list(self.eqs().values()), {"Fx.power": "BlockA"})
        self.assertEqual([r["id"] for r in rows], ["Fx.gain", "Fx.power"])
        self.assertEqual(rows[1]["unit"], "W")
        self.assertEqual(rows[1]["symbols"], "i, r")
        self.assertIn("BlockA", E.index_markdown(rows))


class Page(Fixture):
    def test_page_has_latex_and_examples(self):
        eqs = list(self.eqs(import_module=True).values())
        html, md = E.page_html(eqs, "T"), E.page_markdown(eqs, "T")
        for eq in eqs:
            for line in eq.record["latex"]:
                self.assertIn(E._h(line), html)
                self.assertIn("$$\n" + line + "\n$$", md)
        for page in (html, md):
            self.assertIn("rg=5490", page)          # the EXAMPLES inputs
            self.assertIn("9.998", page)  # the datasheet value
            self.assertIn("DS p.20, Table 8-1, G = 10 row", page)
        self.assertNotIn("<script src", html)
        self.assertNotIn("http", html)
        self.assertNotIn("katex", html.lower())
        self.assertIn("localStorage", html)
        self.assertIn("stamp-cmd", html)
        self.assertIn("python3 tools/equations.py stamp Fx:gain Fx:power", md)

    def test_derived_has_no_examples_and_fix_first_has_no_tick(self):
        self.write(CALC.replace('("gain", {"rg"', '("power", {"i": 2.0, "r": 3.0}, 12.0, 1e-9, "fixture row"), ("gain", {"rg"'))
        self.edit("def power(i, r):", "def power(i):", "calc")
        eqs = list(self.eqs(import_module=True).values())
        html = E.page_html(eqs)
        self.assertNotIn("fixture row", html)          # derived kind: no EXAMPLES
        self.assertIn("name no parameter", html)
        self.assertEqual(html.count('class="tick"'), 1)  # only gain; power is FIX_FIRST

    def test_card_without_tick_and_state_override(self):
        eqs = self.eqs(import_module=True)
        with_tick = E.card_html(eqs["gain"])
        self.assertIn('class="tick"', with_tick)
        self.assertEqual(with_tick, E.card_html(eqs["gain"], by_id={}))
        self.assertNotIn('class="tick"', E.card_html(eqs["gain"], tick=False))
        self.assertIn("HUMAN_VERIFIED", E.card_html(eqs["gain"], state="HUMAN_VERIFIED"))
        self.assertNotIn('class="tick"', E.card_html(eqs["gain"], state="HUMAN_VERIFIED"))
        self.assertEqual(eqs["gain"].state, "NEW")  # the override copies, never mutates

    def test_order_cards_and_status_line(self):
        self.stamp("gain")
        eqs = list(self.eqs().values())  # gain HUMAN_VERIFIED, power NEW
        self.assertEqual([e.fn for e in E.order_cards(eqs)], ["power", "gain"])
        self.assertEqual(E.status_line(eqs), "1 of 2 checked; 1 to review; 0 FIX_FIRST")
        self.write(CALC, TOML)
        both = list(self.eqs().values())
        self.assertEqual([e.fn for e in E.order_cards(both)], ["gain", "power"])  # datasheet before derived

    def test_page_is_deterministic_and_write_page_writes_two_files(self):
        eqs = list(self.eqs(import_module=True).values())
        h, m = E.write_page(eqs, self.root / "out", "equations")
        self.assertEqual(sorted(p.name for p in (self.root / "out").iterdir()), ["equations.html", "equations.md"])
        self.assertEqual(h.read_text(encoding="utf-8"), E.page_html(eqs, "Equations review"))
        self.assertEqual(m.read_text(encoding="utf-8"), E.page_markdown(eqs, "Equations review"))

    def test_checked_equation_is_folded_and_listed_last(self):
        self.stamp("power")
        html = E.page_html(list(self.eqs(import_module=True).values()))
        self.assertIn("HUMAN_VERIFIED</summary>", html)
        self.assertLess(html.index("Gain of the fixture"), html.index("HUMAN_VERIFIED</summary>"))
        self.assertIn("1 of 2 checked", html)



class Index(unittest.TestCase):
    def test_generated_equations_index_is_in_sync(self):
        self.assertEqual((ROOT / "docs" / "EQUATIONS.md").read_text(encoding="utf-8"), readme.equations_index(ROOT))

    def test_index_is_in_top_files_and_lists_every_record(self):
        self.assertIn("docs/EQUATIONS.md", readme.TOP_FILES)
        text = readme.equations_index(ROOT)
        for e in E.library_equations(ROOT):
            self.assertIn(f"`{e.id}`", text)
        self.assertIn("do not edit", text)
        self.assertNotIn("NEW", text)  # no state column


if __name__ == "__main__":
    unittest.main()
