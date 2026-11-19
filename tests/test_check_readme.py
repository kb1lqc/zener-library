import tempfile
import tomllib
import unittest
from pathlib import Path
from shutil import copytree

from lib import Param, load, readme
from lib.check import check_component

FIX = Path(__file__).parent / "fixtures" / "Acme"


def messages(folder):
    return [f"{lvl}: {msg}" for lvl, msg in check_component(folder)]


class TestCheck(unittest.TestCase):
    def test_good_fixture_passes(self):
        self.assertEqual(messages(FIX / "LDO1"), [])

    def test_bad_fixture_fails(self):
        text = "\n".join(messages(FIX / "BAD1"))
        self.assertIn("ERROR: param vin_abs: min <= typ <= max violated", text)
        self.assertIn("ERROR: param vref: missing 'cite'", text)
        self.assertIn("ERROR: pin 3: name mismatch, TOML 'VOUT' vs symbol 'OUT'", text)
        self.assertIn("ERROR: pin 2: type mismatch, TOML 'input' vs symbol 'power_in'", text)
        self.assertIn("ERROR: example vout", text)

    def test_missing_calc_is_warning(self):
        with tempfile.TemporaryDirectory() as d:
            copy = Path(d) / "LDO1"
            copytree(FIX / "LDO1", copy)
            (copy / "calc.py").unlink()
            self.assertEqual(messages(copy), ["WARN: no calc.py"])

    def test_unknown_unit_and_missing_pad(self):
        with tempfile.TemporaryDirectory() as d:
            copy = Path(d) / "LDO1"
            copytree(FIX / "LDO1", copy)
            toml = copy / "component.toml"
            toml.write_text(toml.read_text().replace('unit = "mV"', 'unit = "furlong"'))
            fp = copy / "LDO1.kicad_mod"
            fp.write_text(fp.read_text().replace('(pad "3"', '(pad "9"'))
            text = "\n".join(messages(copy))
            self.assertIn("unknown unit 'furlong'", text)
            self.assertIn("pin 3: no footprint pad", text)


def copy_fixture(tmp, edits=None, calc_edits=None):
    """Copy LDO1 into tmp, applying (old, new) text replacements to component.toml / calc.py."""
    copy = Path(tmp) / "LDO1"
    copytree(FIX / "LDO1", copy)
    for name, pairs in (("component.toml", edits or []), ("calc.py", calc_edits or [])):
        path = copy / name
        text = path.read_text()
        for old, new in pairs:
            assert old in text, old
            text = text.replace(old, new)
        path.write_text(text)
    return copy


class TestNewChecks(unittest.TestCase):
    def run_edit(self, edits=None, calc_edits=None):
        with tempfile.TemporaryDirectory() as d:
            return "\n".join(messages(copy_fixture(d, edits, calc_edits)))

    def test_sym_needs_max_and_no_min(self):
        text = self.run_edit([("typ = 10\nmax = 40\nsym = true", "typ = 10\nmin = -5\nmax = 40\nsym = true")])
        self.assertIn("param vos: sym = true needs max and no min", text)
        text = self.run_edit([("typ = 10\nmax = 40\nsym = true", "typ = 10\nsym = true")])
        self.assertIn("param vos: sym = true needs max and no min", text)

    def test_text_xor_numbers(self):
        self.assertIn("either min/typ/max or text", self.run_edit([('text = "Continuous"', 'text = "Continuous"\nmax = 1')]))
        self.assertIn("either min/typ/max or text", self.run_edit([('text = "Continuous"\n', "")]))

    def test_partial_scope_ok_and_bad_scope(self):
        self.assertEqual(self.run_edit(), "")  # fixture already uses scope = "partial"
        self.assertIn("scope 'sometimes'", self.run_edit([('scope = "partial"', 'scope = "sometimes"')]))

    def test_duplicate_pin_numbers(self):
        text = self.run_edit([('number = "3"', 'number = "2"')])
        self.assertIn("pin 2: number appears more than once", text)

    def test_bad_ref(self):
        self.assertIn("min_ref 'VSS' is not a [[pin]] name", self.run_edit([('min_ref = "GND"', 'min_ref = "VSS"')]))

    def test_cite_format_is_error(self):
        text = self.run_edit([("DS p.5, Electrical Characteristics, TC", "page 5, TC")])
        self.assertIn("ERROR: [cite-format] param tc: cite 'page 5, TC'", text)

    def test_datasheet_file_missing_is_warning(self):
        text = self.run_edit([('step = "none"', 'step = "none"\ndatasheet_file = "docs/datasheets/nope.pdf"')])
        self.assertIn("WARN: datasheet_file not found", text)
        self.assertNotIn("ERROR", text)

    def test_bad_import(self):
        text = self.run_edit(calc_edits=[("def vout", "import os\nfrom math import pi\n\n\ndef vout")])
        self.assertIn("ERROR: calc.py imports 'os'", text)
        self.assertNotIn("'math'", text)

    def test_missing_example_function(self):
        text = self.run_edit(calc_edits=[('("vout", {"vref"', '("nofn", {"vref"')])
        self.assertIn("ERROR: example function 'nofn' does not exist", text)

    def test_inputs_good_missing_and_bad(self):
        self.assertEqual(self.run_edit(), "")
        self.assertIn("WARN: calc.py has no INPUTS", self.run_edit(calc_edits=[('    "vout": {"vref": "vref"},\n', "")]))
        bad = self.run_edit(calc_edits=[('"vout": {"vref": "vref"}', '"nofn": {}, "vout": {"vref": "nokey", "zz": "vref"}')])
        self.assertIn("INPUTS: function 'nofn' does not exist", bad)
        self.assertIn("INPUTS: vout.vref -> unknown param key 'nokey'", bad)
        self.assertIn("INPUTS: vout has no argument 'zz'", bad)

    def test_inputs_field_syntax(self):
        self.assertEqual(self.run_edit(calc_edits=[('"vout": {"vref": "vref"}', '"vout": {"vref": "vref.max"}')]), "")
        bad = self.run_edit(calc_edits=[('"vout": {"vref": "vref"}', '"vout": {"vref": "vref.mid"}')])
        self.assertIn("field must be min, typ or max", bad)


class TestSymbolFormat(unittest.TestCase):
    """The symbol must be KiCad 10 format (version 20251024 or newer): pcb apply rejects older libraries."""
    HEADER = "(kicad_symbol_lib (version 20251024)"

    def run_header(self, new_header):
        with tempfile.TemporaryDirectory() as d:
            copy = Path(d) / "LDO1"
            copytree(FIX / "LDO1", copy)
            sym = copy / "LDO1.kicad_sym"
            text = sym.read_text()
            assert self.HEADER in text
            sym.write_text(text.replace(self.HEADER, new_header, 1))
            return messages(copy)

    def test_kicad6_symbol_is_error(self):
        out = self.run_header("(kicad_symbol_lib (version 20211014)")
        self.assertEqual(len(out), 1)
        self.assertIn("ERROR: LDO1.kicad_sym: format version 20211014; KiCad 10 format (20251024 or newer)", out[0])
        self.assertIn("kicad-cli sym upgrade --force", out[0])

    def test_kicad10_symbol_is_clean(self):
        self.assertEqual(messages(FIX / "LDO1"), [])
        self.assertEqual(self.run_header(self.HEADER), [])

    def test_missing_version_is_error(self):
        out = self.run_header("(kicad_symbol_lib")
        self.assertEqual(len(out), 1)
        self.assertIn("ERROR: LDO1.kicad_sym: no integer (version N) in its header", out[0])

    def test_footprint_is_not_checked_for_version(self):
        with tempfile.TemporaryDirectory() as d:
            copy = Path(d) / "LDO1"
            copytree(FIX / "LDO1", copy)
            fp = copy / "LDO1.kicad_mod"
            fp.write_text(fp.read_text().replace("(version 20241229)", "(version 20211014)", 1))
            self.assertEqual(messages(copy), [])


class TestExampleTolerance(unittest.TestCase):
    def test_relative_and_absolute(self):
        from lib.component import run_example
        calc = type("C", (), {"f": staticmethod(lambda x: x)})
        self.assertTrue(run_example(calc, ("f", {"x": 100.05}, 100.0, 1e-3, ""))[1])  # relative
        self.assertFalse(run_example(calc, ("f", {"x": 100.5}, 100.0, 1e-3, ""))[1])
        self.assertTrue(run_example(calc, ("f", {"x": 0.0005}, 0, 1e-3, ""))[1])  # absolute at 0
        self.assertFalse(run_example(calc, ("f", {"x": 0.005}, 0, 1e-3, ""))[1])


class TestLoad(unittest.TestCase):
    def test_load_si(self):
        part = load(str(FIX / "LDO1"))
        self.assertEqual(part.info["mpn"], "LDO1R")
        self.assertEqual(len(part.pins), 3)
        self.assertAlmostEqual(part.param("vref").max, 1.01)
        self.assertEqual(part.param("vref").unit, "V")
        self.assertEqual(part.calc.vout(1.0, 10e3, 10e3), 2.0)
        with self.assertRaises(KeyError):
            part.param("nope")


class TestLoadNew(unittest.TestCase):
    def setUp(self):
        self.part = load(str(FIX / "LDO1"))

    def test_inputs_helper(self):
        whole = self.part.inputs("vout")["vref"]
        self.assertAlmostEqual(whole.max, 1.01)
        self.assertEqual(self.part.inputs("nofn"), {})

    def test_sym(self):
        p = self.part.param("vos")
        self.assertEqual((p.min, p.typ, p.max), (-40e-6, 0.0, 40e-6))  # sym typ is centred
        self.assertAlmostEqual(p.typ_spread, 10e-6)

    def test_typ_pm(self):
        p = self.part.param("gain_err")
        self.assertEqual((p.typ, p.typ_spread, p.unit), (0.0, 0.00025, "1"))
        self.assertAlmostEqual(p.max, 0.001)

    def test_text_and_ppm(self):
        self.assertEqual(self.part.param("io_cont").text, "Continuous")
        self.assertAlmostEqual(self.part.param("tc").max, 50e-6)
        self.assertEqual(self.part.param("tc").unit, "1/degC")

    def test_resolve_floats(self):
        p = self.part.resolve("vcm", {"GND": 0.0, "IN": 15.0})
        self.assertEqual((p.min, p.max, p.min_ref), (2.0, 13.0, None))

    def test_resolve_params(self):
        gnd = Param(min=-0.1, max=0.1)
        rail = Param(min=14.0, max=16.0)
        p = self.part.resolve("vcm", {"GND": gnd, "IN": rail})
        self.assertAlmostEqual(p.min, 2.1)  # offset + rail.max
        self.assertAlmostEqual(p.max, 12.0)  # offset + rail.min

    def test_resolve_errors_and_passthrough(self):
        with self.assertRaises(ValueError) as cm:
            self.part.resolve("vcm", {"GND": 0.0})
        self.assertIn("'IN'", str(cm.exception))
        self.assertIs(self.part.resolve("vref", {}), self.part.param("vref"))

    def test_sym_load_error(self):
        from lib.component import to_param
        with self.assertRaises(ValueError):
            to_param({"sym": True, "min": 1, "unit": "V"})

    def test_verification_type_loads_into_param(self):
        from lib.component import to_param
        param = to_param({
            "unit": "V",
            "verified": "abrown 2026-11-19 human page-image review",
            "verification_type": "human_page_image",
        })
        self.assertEqual(param.verification_type, "human_page_image")


class TestReadme(unittest.TestCase):
    def test_review_badge_counts_stamps_and_links_archive(self):
        with tempfile.TemporaryDirectory() as d:
            copy = copy_fixture(d, [
                ('name = "Reference voltage"',
                 'name = "Reference voltage"\nverified = "abrown 2026-11-19 page-image review"\n'
                 'verification_type = "human_page_image"'),
            ])
            rows = tomllib.loads((copy / "component.toml").read_text())["param"]
            total = len(rows)
            text = readme.build(copy)
            self.assertIn(f"Human page-image review: 1/{total} human", text)
            self.assertIn(f"human%20review-1%2F{total}%20human-yellow", text)
            self.assertIn("cross-model audits: 0", text)
            self.assertIn("| human page-image review: abrown 2026-11-19 page-image review |", text)

            (copy / "datasheet-review").mkdir()
            self.assertIn("](datasheet-review/)", readme.build(copy))

    def test_cross_model_stamp_is_not_counted_as_human(self):
        with tempfile.TemporaryDirectory() as d:
            copy = copy_fixture(d, [
                ('name = "Reference voltage"',
                 'name = "Reference voltage"\nverified = "sonnet-audit 2026-11-18 blind cross-model page-image review"'),
            ])
            text = readme.build(copy)
            self.assertIn("Human page-image review: 0/", text)
            self.assertIn("cross-model audits: 1", text)
            self.assertIn("cross-model page-image audit:", text)

    def test_typed_review_without_stamp_is_not_counted(self):
        with tempfile.TemporaryDirectory() as d:
            copy = copy_fixture(d, [
                ('name = "Reference voltage"',
                 'name = "Reference voltage"\nverification_type = "human_page_image"'),
            ])
            text = readme.build(copy)
            self.assertIn("Human page-image review: 0/", text)
            self.assertEqual(readme.verification_label({"verification_type": "human_page_image"}), "")

    def test_new_rendering(self):
        text = readme.build(FIX / "LDO1")
        self.assertIn("| Output offset | VOS |  | \u00b110 | \u00b140 | uV |", text)  # sym
        self.assertIn("| Gain error |  | -0.1 | \u00b10.025 | 0.1 | % |", text)  # typ_pm
        self.assertIn("| Output current rating |  |  | Continuous |  | A | TA <= 70 degC |", text)  # text
        self.assertIn("| Common-mode range |  | 2 (rel. GND) |  | -2 (rel. IN) | V |", text)
        self.assertIn("Inputs:\n\n- `vref` -> `vref` (min 990 typ 1000 max 1010 mV)", text)

    def test_curve_marked(self):
        with tempfile.TemporaryDirectory() as d:
            copy = copy_fixture(d, [('unit = "ppm/degC"', 'unit = "ppm/degC"\ncurve = true')])
            self.assertIn("(curve) |", readme.build(copy))


    def test_generated_text(self):
        text = readme.build(FIX / "LDO1")
        self.assertTrue(text.startswith("<!-- GENERATED - do not edit"))
        self.assertIn("| 3 | OUT | power_out | Output | DS p.3, Pin Functions, OUT |", text)
        self.assertIn("## Parameters: abs_max", text)
        self.assertIn(
            "| Reference voltage |  | 990 | 1000 | 1010 | mV | TA = 25 degC \\| IL = 1 mA Note: Characterized | "
            "DS p.5, Electrical Characteristics, VREF |  |",
            text,
        )
        self.assertIn("### `vout`", text)
        self.assertNotIn("_hidden", text)
        self.assertIn("| vout(vref=1, r1=10000, r2=10000) | 2 | 2 | 0.001 | pass |", text)

    def test_deterministic_and_written(self):
        with tempfile.TemporaryDirectory() as d:
            copy = Path(d) / "LDO1"
            copytree(FIX / "LDO1", copy)
            readme.main([str(copy)])
            first = (copy / "README.md").read_text()
            readme.main([str(copy / "component.toml")])
            self.assertEqual(first, (copy / "README.md").read_text())


if __name__ == "__main__":
    unittest.main()
