"""Validate component.toml files: python3 -m lib.check [component paths...]"""

import ast
import hashlib
import inspect
import re
import sys
import tomllib
from pathlib import Path

from . import capacitor, catalog, equations, kicad, rules, series
from . import review_status
from .component import (EVIDENCE, ROOT, _read_toml, _repo_root, ledger_state_of, load_calc, merge_variant, override_rows, pinout_hash, row_hash,
                        run_example, variants_of)
from .units import to_si

PART_FIELDS = ["value", "mpn", "manufacturer", "description", "category", "package", "datasheet_url",
               "datasheet_rev", "datasheet_date", "kicad_symbol", "kicad_footprint", "step"]
PIN_FIELDS = ["number", "name", "type", "function", "cite"]
PARAM_FIELDS = ["name", "kind", "scope", "unit", "conditions", "cite"]
PIN_TYPES = {"input", "output", "bidirectional", "tri_state", "passive", "free", "unspecified", "power_in",
             "power_out", "open_collector", "open_emitter", "no_connect"}
KINDS = {"abs_max", "rec_op", "electrical", "thermal", "mechanical"}
SCOPES = {"25C", "full", "partial", "na"}
# KiCad 10 symbol format. `pcb apply schematic` (pcb 0.4.102) rejects older symbol libraries. Upgrade with
# `kicad-cli sym upgrade --force` (docs/KICAD.md, Symbol). Footprints are not checked for this.
KICAD_SYMBOL_MIN_VERSION = 20251024


SERIES_FIELDS = ["value_param", "e_series", "series_power"]  # plus series_tol or series_tolerances; series_vlimit is optional
CAPACITOR_FIELDS = ["catalog", "tc_param", "package_default", "package_alternates"]


def check_part(part, folder, family=False):
    """[part] table: required fields, value == directory name, KiCad/STEP files exist.
    A family's shared [part] has no mpn (each variant sets its own, checked in check_variant); a series has none
    either (calc.mpn gives it, checked in check_series_part)."""
    out = []
    for f in PART_FIELDS:
        if (family or part.get("series")) and f == "mpn":
            continue
        if f not in part and f != "datasheet_url":  # datasheet_url: missing or empty is the tolerated warning below
            out.append(("ERROR", f"[part] missing field '{f}'"))
    if part.get("value", folder.name) != folder.name:
        out.append(("ERROR", f"[part] value '{part['value']}' differs from directory '{folder.name}'"))
    for f in ("kicad_symbol", "kicad_footprint"):
        if f in part and not (folder / part[f]).exists():
            out.append(("ERROR", f"{f} file not found: {part[f]}"))
    url = part.get("datasheet_url", "")
    if not url:
        out.append(("WARN", "datasheet_url empty (record the vendor URL; open item)"))
    elif not str(url).startswith(("http://", "https://")):
        out.append(("ERROR", f"datasheet_url must start with http:// or https:// (got '{url}')"))
    if part.get("datasheet_file") and not (ROOT / part["datasheet_file"]).exists():
        out.append(("WARN", f"datasheet_file not found: {part['datasheet_file']} (PDFs are not committed)"))
    step = part.get("step", "none")
    if step not in ("embedded", "none") and not (folder / step).exists():
        out.append(("ERROR", f"step file not found: {step}"))
    return out


def check_pins(pins):
    """[[pin]] entries: required fields and a known type."""
    out = []
    numbers = [str(p.get("number")) for p in pins]
    for num in sorted({n for n in numbers if numbers.count(n) > 1}):
        out.append(("ERROR", f"pin {num}: number appears more than once in [[pin]]"))
    for i, pin in enumerate(pins):
        label = f"pin {pin.get('number', f'#{i + 1}')}"
        for f in PIN_FIELDS:
            if not pin.get(f):
                out.append(("ERROR", f"{label}: missing '{f}'" + (" (cite)" if f == "cite" else "")))
        if pin.get("type") and pin["type"] not in PIN_TYPES:
            out.append(("ERROR", f"{label}: unknown type '{pin['type']}'"))
    return out


def has_field(t, field):
    """True if the TOML row gives min/typ/max (a tol_pct row gives min and max through its typ)."""
    return field in t or ("tol_pct" in t and field in ("min", "max"))


def check_tol_pct(label, t):
    """tol_pct = [lo, hi] (printed percent): needs typ, no min/max, lo <= hi."""
    if "tol_pct" not in t:
        return []
    tol = t["tol_pct"]
    if not (isinstance(tol, list) and len(tol) == 2 and all(isinstance(x, (int, float)) for x in tol)):
        return [("ERROR", f"{label}: tol_pct must be [lo, hi] numbers")]
    out = []
    if "typ" not in t or "min" in t or "max" in t:
        out.append(("ERROR", f"{label}: tol_pct needs typ and no min/max"))
    if tol[0] > tol[1]:
        out.append(("ERROR", f"{label}: tol_pct lo {tol[0]} > hi {tol[1]}"))
    return out


def check_series(label, key, t):
    """Key and symbol both ending in _<digits>: the numbers must agree (vovc_thr_10 with symbol ..._16 is a typo)."""
    k, s = re.search(r"_(\d+)$", key), re.search(r"_(\d+)$", t.get("symbol", ""))
    if k and s and int(k.group(1)) != int(s.group(1)):
        return [("ERROR", f"{label}: key suffix {int(k.group(1))} != symbol suffix {int(s.group(1))}")]
    return []


def check_param(key, t, pin_names=(), used_by_series=False):
    """One [param.key] table (used_by_series: the series check reads this row, so it needs no Zener disposition)."""
    out = []
    label = f"param {key}"
    for f in PARAM_FIELDS:
        if f not in t or (f == "cite" and not t[f]):
            out.append(("ERROR", f"{label}: missing '{f}'"))
    if t.get("kind") not in KINDS and "kind" in t:
        out.append(("ERROR", f"{label}: kind '{t['kind']}' not one of {sorted(KINDS)}"))
    if t.get("scope") not in SCOPES and "scope" in t:
        out.append(("ERROR", f"{label}: scope '{t['scope']}' not one of {sorted(SCOPES)}"))
    if key == "pinout":
        out.append(("ERROR", f"{label}: [param.pinout] is reserved for the pin table's review row; rename this row "
                             f"(for example 'pinout_note') in component.toml, calc.py INPUTS and examples"))
    out.extend(check_tol_pct(label, t) + check_series(label, key, t))
    has_number = any(f in t for f in ("min", "typ", "max"))
    if has_number == ("text" in t):  # both or neither
        out.append(("ERROR", f"{label}: needs either min/typ/max or text, not both and not neither"))
    if t.get("sym") and ("max" not in t or "min" in t):
        out.append(("ERROR", f"{label}: sym = true needs max and no min"))
    if t.get("curve") and not any(w in t.get("cite", "").lower() for w in ("fig", "graph")):
        out.append(("WARN", f"{label}: curve value but cite does not name a figure or graph"))
    out.extend(check_zen_fields(label, t, pin_names, used_by_series))
    for f in ("min_ref", "max_ref", "typ_ref"):
        if f in t and t[f] not in pin_names:
            out.append(("ERROR", f"{label}: {f} '{t[f]}' is not a [[pin]] name"))
    if "typ_ref" in t and "typ" not in t:
        out.append(("ERROR", f"{label}: typ_ref needs typ"))
    out.extend(check_order(label, t))
    return out


def check_zen_fields(label, t, pin_names, used_by_series=False):
    """check_pins / check_ambient / unchecked (docs/SPEC.md, Zener wrapper)."""
    out = []
    pins = t.get("check_pins", [])
    if pins and (t.get("unit", "").lstrip("munpkMG") != "V" or "text" in t or t.get("curve")):
        out.append(("ERROR", f"{label}: check_pins needs a numeric voltage param (not text, not curve)"))
    for pin in pins:
        if pin not in pin_names:
            out.append(("ERROR", f"{label}: check_pins '{pin}' is not a [[pin]] name"))
    if pins and not any(has_field(t, f) for f in ("min", "max")):
        out.append(("ERROR", f"{label}: check_pins needs a min or max"))
    if t.get("check_ambient") and (t.get("unit") != "degC" or not has_field(t, "min") or not has_field(t, "max") or t.get("curve")):
        out.append(("ERROR", f"{label}: check_ambient needs a degC param with min and max (not curve)"))
    if "unchecked" in t and not str(t["unchecked"]).strip():
        out.append(("ERROR", f"{label}: unchecked needs a reason"))
    if t.get("kind") in ("abs_max", "rec_op") and not (pins or t.get("check_ambient") or t.get("unchecked") or used_by_series):
        out.append(("WARN", f"{label}: {t['kind']} row has no check_pins, check_ambient or unchecked reason"))
    return out


def check_order(label, t):
    """Units known, values numeric, min <= typ <= max compared in SI."""
    try:
        v = {f: to_si(t[f], t.get("unit", ""))[0] for f in ("min", "typ", "max") if f in t}
        if not v:
            to_si(0, t.get("unit", ""))  # still validate the unit
    except ValueError as e:
        return [("ERROR", f"{label}: {e}")]
    if "tol_pct" in t:
        return []  # min/max come from typ and the percentages (check_tol_pct)
    if "min_ref" in t or "max_ref" in t or "typ_ref" in t:
        return []  # offsets from different pins (2 from -VS, -2 from +VS) cannot be ordered
    if t.get("sym") and "max" in v:
        v["min"] = -v["max"]
    if t.get("typ_pm") and "typ" in v:
        v["typ"] = 0.0
    vals = [v[f] for f in ("min", "typ", "max") if f in v]
    if vals != sorted(vals):
        return [("ERROR", f"{label}: min <= typ <= max violated ({vals} in SI)")]
    return []


def check_capacitor_part(part, pins, params, folder):
    """[part] capacitor fields, the catalog file, dielectric / parts restrictions and the temperature-characteristic and
    ambient rows every catalog dielectric needs (docs/SPEC.md, Capacitor series). Returns (messages, catalog rows)."""
    out = [("ERROR", f"[part] series needs '{f}'") for f in CAPACITOR_FIELDS if f not in part]
    if "mpn" in part:
        out.append(("ERROR", "[part] mpn must be absent for a series: the catalog value plus the package letter is the MPN"))
    if len(pins) != 2:
        out.append(("ERROR", f"a series capacitor needs exactly 2 pins, found {len(pins)}"))
    letters = [part.get("package_default")] + list(part.get("package_alternates", []))
    if any(not (isinstance(x, str) and re.fullmatch(r"[A-Z]", x)) for x in letters) or len(set(letters)) != len(letters):
        out.append(("ERROR", f"[part] package_default and package_alternates must be distinct single capital letters, got {letters}"))
    tc_param = part.get("tc_param", {})
    if not isinstance(tc_param, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in tc_param.items()):
        return out + [("ERROR", "[part] tc_param must be a table {dielectric = \"param key\"}")], []
    if "catalog" not in part:
        return out, []
    try:
        rows = capacitor.read_catalog(folder / part["catalog"])
    except ValueError as e:
        return out + [("ERROR", line) for line in str(e).splitlines()], []
    dielectrics = {r.dielectric for r in rows}
    values = {r.value for r in rows}
    if part.get("catalog_decoder") == "murata-gcm":  # re-decode every row: a hand edit of a column is an error
        for r in rows:
            out += [("ERROR", f"catalog row {r.value}: {m}") for m in catalog.catalog_row_problems(r, folder.name)]
    elif "catalog_decoder" in part:
        out.append(("ERROR", f"[part] catalog_decoder = '{part['catalog_decoder']}': only 'murata-gcm' exists"))
    by_value = {r.value: r.dielectric for r in rows}
    if not rows:
        out.append(("ERROR", "the catalog has no rows"))
    for d in sorted(dielectrics):
        if d not in tc_param:
            out.append(("ERROR", f"catalog dielectric '{d}' has no [part] tc_param entry: no temperature-characteristic row, "
                                 f"so its parts cannot be listed"))
    for d, key in tc_param.items():
        t = params.get(key)
        if t is None:
            out.append(("ERROR", f"[part] tc_param {d} = '{key}' is not a param key"))
        elif t.get("dielectric") != d:
            out.append(("ERROR", f"param {key}: the temperature-characteristic row of {d} must have dielectric = \"{d}\""))
        elif not (t.get("unit") in ("%", "ppm/degC") and "min" in t and "max" in t):
            out.append(("ERROR", f"param {key}: a temperature characteristic needs min, max and unit % or ppm/degC"))
    ambient = {d: [k for k, t in params.items() if t.get("check_ambient") and t.get("dielectric", d) == d] for d in dielectrics}
    for d, keys in sorted(ambient.items()):
        if len(keys) != 1:
            out.append(("ERROR", f"dielectric {d}: needs exactly one check_ambient row (unrestricted or dielectric = \"{d}\"), "
                                 f"found {len(keys)}"))
    for key, t in params.items():
        label = f"param {key}"
        if key in capacitor.SELECTION_KEYS:
            out.append(("ERROR", f"{label}: key is reserved for the part selection ({', '.join(capacitor.SELECTION_KEYS)})"))
        if "dielectric" in t and "parts" in t:
            out.append(("ERROR", f"{label}: a row has dielectric or parts, not both"))
        suffix = next((d for d in dielectrics if key.lower().endswith("_" + d.lower())), None)
        if suffix and "dielectric" in t and t["dielectric"] != suffix:
            out.append(("WARN", f"{label}: key ends in _{suffix.lower()} but dielectric = '{t['dielectric']}'"))
        if suffix and "parts" in t and isinstance(t["parts"], list):
            other = [x for x in t["parts"] if by_value.get(x, suffix) != suffix]
            if other:
                out.append(("WARN", f"{label}: key ends in _{suffix.lower()} but parts names {', '.join(other)} of another dielectric"))
        if "dielectric" in t and t["dielectric"] not in dielectrics:
            out.append(("ERROR", f"{label}: dielectric '{t['dielectric']}' is not in the catalog ({', '.join(sorted(dielectrics))})"))
        if "parts" in t:
            if not (isinstance(t["parts"], list) and t["parts"] and all(isinstance(x, str) for x in t["parts"])):
                out.append(("ERROR", f"{label}: parts must be a non-empty list of catalog values"))
            else:
                out += [("ERROR", f"{label}: parts names '{x}', which is not a catalog value") for x in t["parts"] if x not in values]
            if t.get("check_ambient"):
                out.append(("ERROR", f"{label}: a part-restricted row cannot have check_ambient (the wrapper checks per dielectric)"))
        if t.get("check_pins"):
            out.append(("ERROR", f"{label}: check_pins is not supported in a capacitor series (the wrapper checks the catalog rated voltage)"))
    return out, rows


def check_series_part(part, pins, params, folder):
    """[part] series fields, the rows they name, and calc.mpn over every allowed value (docs/SPEC.md, Series components)."""
    if part.get("series") != "resistor":
        return [("ERROR", f"[part] series = '{part.get('series')}': only 'resistor' and 'capacitor' are supported")]
    out = [("ERROR", f"[part] series needs '{f}'") for f in SERIES_FIELDS if f not in part]
    if "mpn" in part:
        out.append(("ERROR", "[part] mpn must be absent for a series: calc.mpn(value) is the single source"))
    if "series_pins" in part:
        sp = part["series_pins"]
        if not (isinstance(sp, list) and len(sp) == 2 and sp[0] != sp[1] and all(x in {p.get("name") for p in pins} for x in sp)):
            out.append(("ERROR", f"[part] series_pins must list two different [[pin]] names, got {sp}"))
    elif len(pins) != 2:
        out.append(("ERROR", f"a series resistor needs exactly 2 pins, found {len(pins)} (or name the two current pins in series_pins)"))
    if "series_tol" in part and "series_tolerances" in part:
        out.append(("ERROR", "[part] series_tol and series_tolerances are exclusive: tolerance options carry their own rows"))
    elif "series_tol" not in part and "series_tolerances" not in part:
        out.append(("ERROR", "[part] series needs 'series_tol' or 'series_tolerances'"))
    for f in ("value_param", "series_power", "series_vlimit", "series_tol"):
        if f in part and part[f] not in params:
            out.append(("ERROR", f"[part] {f} = '{part[f]}' is not a param key"))
    names = part.get("e_series", [])
    unknown = [n for n in names if n not in series.E_SERIES]
    if unknown or not names:
        out.append(("ERROR", f"[part] e_series must list names from {sorted(series.E_SERIES)}, got {names}"))
    mins = part.get("series_eseries_min", {})
    if not isinstance(mins, dict) or any(n not in names or isinstance(v, bool) or not isinstance(v, (int, float)) or v <= 0
                                         for n, v in mins.items()):
        out.append(("ERROR", f"[part] series_eseries_min must map names from e_series to a positive ohm value, got {mins}"))
        mins = {}
    rng = params.get(part.get("value_param"), {})
    if rng and not (rng.get("unit", "").endswith("ohm") and "min" in rng and "max" in rng):
        out.append(("ERROR", f"param {part['value_param']}: the series value range needs min, max and an ohm unit"))
    tol = params.get(part.get("series_tol"), {})
    if tol and not (tol.get("unit") in ("%", "ppm") and "min" in tol and "max" in tol):
        out.append(("ERROR", f"param {part['series_tol']}: the series tolerance needs min, max and unit %"))
    out += check_series_tables(part, params)
    if out:
        return out
    if not (folder / "calc.py").exists():
        return [("ERROR", "a series needs calc.py with mpn(value)")]
    try:
        calc = load_calc(folder / "calc.py")
    except Exception:
        return []  # check_calc reports the import failure
    if not callable(getattr(calc, "mpn", None)):
        return [("ERROR", "calc.py of a series must define mpn(value)")]

    def bounds(key):
        return tuple(to_si(params[key][f], params[key]["unit"])[0] for f in ("min", "max"))

    pair_list = series.pairs(part, bounds)
    out = []
    if part.get("series_tolerances"):
        for code, _, key in series.options(part):
            if not any(c == code for _, c in pair_list):
                out.append(("ERROR", f"[part] series_tolerances.{code}: its range '{key}' has no value inside the series range"))
    out += [("ERROR", msg) for msg in series.mpn_table(calc, pair_list)[1]]
    if part.get("series_tcr"):
        spans = [bounds(r) for _, r in series.tcr_rows(part)]
        for v in sorted({v for v, _ in pair_list}):
            n = sum(lo * (1 - 1e-9) <= v <= hi * (1 + 1e-9) for lo, hi in spans)
            if n != 1:
                out.append(("ERROR", f"[part] series_tcr: {n} TCR rows cover {v:g} ohm (need exactly 1)"))
    return out


def check_series_tables(part, params):
    """series_tolerances = {code = {tol, range}} and series_tcr = [{tcr, range}]: well-formed, rows exist with units."""
    out = []
    opts = part.get("series_tolerances", {})
    if "series_tolerances" in part and (not isinstance(opts, dict) or not opts or any(
            not isinstance(c, str) or not c.isalnum() or not isinstance(o, dict) or set(o) != {"tol", "range"}
            for c, o in opts.items())):
        return out + [("ERROR", "[part] series_tolerances must map a code (letters/digits) to { tol = <row>, range = <row> }")]
    pairs_ = [(f"series_tolerances.{c}", o["tol"], ("%", "ppm"), o["range"]) for c, o in opts.items()]
    tcrs = part.get("series_tcr", [])
    if "series_tcr" in part and (not isinstance(tcrs, list) or not tcrs or any(
            not isinstance(o, dict) or set(o) != {"tcr", "range"} for o in tcrs)):
        return out + [("ERROR", "[part] series_tcr must be a list of { tcr = <row>, range = <row> }")]
    pairs_ += [(f"series_tcr[{i}]", o["tcr"], ("ppm/degC",), o["range"]) for i, o in enumerate(tcrs)]
    for label, row, units, rrow in pairs_:
        for key in (row, rrow):
            if key not in params:
                out.append(("ERROR", f"[part] {label}: '{key}' is not a param key"))
        t, r = params.get(row, {}), params.get(rrow, {})
        if t and not (t.get("unit") in units and "min" in t and "max" in t):
            out.append(("ERROR", f"param {row}: needs min, max and unit {' or '.join(units)}"))
        if r and not (r.get("unit", "").endswith("ohm") and "min" in r and "max" in r):
            out.append(("ERROR", f"param {rrow}: a range row needs min, max and an ohm unit"))
    return out


def check_kicad(pins, part, folder):
    """TOML pins vs symbol pins (exact), and footprint pads cover every pin number."""
    out = []
    sym, fp = folder / part.get("kicad_symbol", ""), folder / part.get("kicad_footprint", "")
    if part.get("kicad_symbol") and sym.exists():
        version = kicad.symbol_format_version(sym)
        if version is None or version < KICAD_SYMBOL_MIN_VERSION:
            found = "no integer (version N) in its header" if version is None else f"format version {version}"
            out.append(("ERROR", f"{part['kicad_symbol']}: {found}; KiCad 10 format ({KICAD_SYMBOL_MIN_VERSION} or newer) "
                                 f"is required by pcb apply. Fix: kicad-cli sym upgrade --force {sym} (docs/KICAD.md, Symbol)"))
        symbol = {num: (name, typ) for num, name, typ in kicad.symbol_pins(sym)}
        toml = {str(p.get("number")): (p.get("name"), p.get("type")) for p in pins}
        for num in sorted(toml.keys() - symbol.keys()):
            out.append(("ERROR", f"pin {num}: in TOML but not in symbol"))
        for num in sorted(symbol.keys() - toml.keys()):
            out.append(("ERROR", f"pin {num}: in symbol ({symbol[num][0]}) but not in TOML"))
        for num in sorted(toml.keys() & symbol.keys()):
            if toml[num][0] != symbol[num][0]:
                out.append(("ERROR", f"pin {num}: name mismatch, TOML '{toml[num][0]}' vs symbol '{symbol[num][0]}'"))
            if toml[num][1] != symbol[num][1]:
                out.append(("ERROR", f"pin {num}: type mismatch, TOML '{toml[num][1]}' vs symbol '{symbol[num][1]}'"))
        out += finding_messages(rules.symbol_grid_findings(sym))
    if part.get("kicad_footprint") and fp.exists():
        for num in sorted({str(p.get("number")) for p in pins} - kicad.footprint_pads(fp)):
            out.append(("ERROR", f"pin {num}: no footprint pad with that number"))
        out += finding_messages(rules.courtyard_findings(fp)[0])
    return out


def finding_messages(findings):
    """Rule findings as (ERROR, '[rule] location: message') tuples; main() maps them to the allowlist."""
    return [("ERROR", rules.text(f)) for f in findings]


def check_imports(path):
    """ERROR for every import in calc.py other than math."""
    out = []
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        names = []
        if isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            names = [node.module or "."]
        out += [("ERROR", f"calc.py imports '{n}'; only math is allowed") for n in names if n.split(".")[0] != "math"]
    return out


def check_inputs(calc, params):
    """INPUTS = {function: {argument: "key" or "key.min|typ|max"}}: function, argument, key and field must exist."""
    inputs = getattr(calc, "INPUTS", None)
    if not inputs:
        return [("WARN", "calc.py has no INPUTS")]
    out = []
    for fname, args in inputs.items():
        fn = getattr(calc, fname, None)
        if not callable(fn):
            out.append(("ERROR", f"INPUTS: function '{fname}' does not exist"))
            continue
        for arg, key in args.items():
            if arg not in inspect.signature(fn).parameters:
                out.append(("ERROR", f"INPUTS: {fname} has no argument '{arg}'"))
            name, _, field = key.partition(".")
            if name not in params:
                out.append(("ERROR", f"INPUTS: {fname}.{arg} -> unknown param key '{name}'"))
            elif field and field not in ("min", "typ", "max"):
                out.append(("ERROR", f"INPUTS: {fname}.{arg} -> '{key}': field must be min, typ or max"))
            elif field and not has_field(params[name], field):
                out.append(("ERROR", f"INPUTS: {fname}.{arg} -> '{key}': the DS gives no {field}"))
            elif not field and not (has_field(params[name], "min") and has_field(params[name], "max")) and not params[name].get("sym"):
                out.append(("WARN", f"INPUTS: {fname}.{arg} -> '{key}' has no min/max range; wca cannot sweep "
                                    f"it. Name the field, e.g. '{key}.typ'"))
    return out


def check_examples(calc):
    """EXAMPLES present and reproducing within tolerance."""
    examples = getattr(calc, "EXAMPLES", None)
    if not examples:
        return [("WARN", "calc.py has no EXAMPLES")]
    out = []
    for row in examples:
        if not callable(getattr(calc, row[0], None)):
            out.append(("ERROR", f"example function '{row[0]}' does not exist"))
            continue
        try:
            got, ok = run_example(calc, row)
        except Exception as e:
            out.append(("ERROR", f"example {row[0]}{row[1]}: {type(e).__name__}: {e}"))
            continue
        if not ok:
            out.append(("ERROR", f"example {row[0]}{row[1]}: got {got:.6g}, expected {row[2]:.6g} "
                                 f"(tol {row[3]:g}) [{row[4]}]"))
    return out


def check_calc(folder, params, inputs=True):
    """calc.py present, imports only math, EXAMPLES and INPUTS valid (inputs=False: a family checks them per variant)."""
    if not (folder / "calc.py").exists():
        return [("WARN", "no calc.py")]
    out = check_imports(folder / "calc.py") + finding_messages(rules.example_comment_findings(folder / "calc.py"))
    try:
        calc = load_calc(folder / "calc.py")
    except Exception as e:
        return out + [("ERROR", f"calc.py fails to import: {e}")]
    out += finding_messages(rules.inputs_coverage_findings(calc))
    out += equations.check_folder(folder)  # equations.toml records (docs/spec/equations.md); [] when absent
    return out + check_examples(calc) + (check_inputs(calc, params) if inputs else [])


def check_component(folder, raw=False):
    """All checks for one component directory, minus findings listed in lib/known_findings.toml (raw=True keeps them,
    so main() can tell which entries went stale). Returns [(level, message), ...]."""
    out = _check_component(folder)
    if raw:
        return out
    part = f"{Path(folder).parent.name}/{Path(folder).name}"
    allowed = {(e["rule"], e["location"]) for e in rules.load_allowlist() if e["part"] == part}
    return [(lvl, msg) for lvl, msg in out if not (lvl == "ERROR" and rules.split_message(msg) in allowed)]


def abstentions(folder):
    """Rules that could not decide for this component (reported in the summary, never a failure)."""
    folder = Path(folder)
    notes = []
    for fp in sorted(folder.glob("*.kicad_mod")):
        reason = rules.courtyard_findings(fp)[1]
        if reason:
            notes.append(f"{folder.name}: courtyard-margin not checked: {reason}")
    return notes


def _ledger_rows(f):
    with open(f, "rb") as fh:
        return tomllib.load(fh).get("row", {})


REVIEW_MODES = {}  # component dir -> (mode, images matched); check_ledger fills it, main prints one mode line


REVIEW_FILES = ("review.toml", catalog.EXPORT_RECORD)  # the only committed files under review/
EXPORT_STAMP = capacitor.parse_group_stamp  # one parser for the machine and the legacy human `verified` line


def stray_review_files(folder):
    """ERROR per file under review/ that is not a committed review record (docs/spec/review.md)."""
    folder = Path(folder)
    return [("ERROR", f"review/{p.relative_to(folder / 'review')}: only review/review.toml and review/export_check.toml are "
                     f"committed (page images and generated pages live in the git-ignored .review-cache/); delete it")
            for p in sorted((folder / "review").rglob("*")) if p.is_file() and p.name not in REVIEW_FILES
            and not p.name.startswith(".")]


def check_export_record(folder):
    """review/export_check.toml (docs/spec/capacitor.md "Export check"). Always: valid TOML; the catalog hash is the committed
    catalog.csv's and the tables hash is the current decode tables' (else STALE); a group's `verified` is a machine line
    whose 12 digits are the group hash, or a legacy human stamp for that group. In every mode the export check is run
    again on the cited export (docs/datasheets/, docs/vendor/, then the committed docs/exports/ subset; a missing export
    is an error), and the export rows hash and every group hash must match the record."""
    folder = Path(folder)
    f = folder / "review" / catalog.EXPORT_RECORD
    if not f.exists():
        return []
    rerun = f"rerun python3 -m lib.catalog export-check <export> {folder}"
    try:
        with open(f, "rb") as fh:
            rec = tomllib.load(fh)
        with open(folder / "component.toml", "rb") as fh:
            part = tomllib.load(fh).get("part", {})
    except (OSError, tomllib.TOMLDecodeError) as e:
        return [("ERROR", f"review/export_check.toml or component.toml is not valid TOML ({e})")]
    out = []
    cat = folder / part.get("catalog", "catalog.csv")
    if not cat.is_file():
        out.append(("ERROR", f"review/export_check.toml: {cat.name} is missing"))
    elif rec.get("catalog", {}).get("sha256") != catalog.sha256_file(cat):
        out.append(("ERROR", f"review/export_check.toml is STALE: {cat.name} changed since the export check ({rerun})"))
    groups = rec.get("group", {})
    machine = False
    if cat.is_file():
        counts = {}
        try:
            for r in catalog.committed_rows(cat):
                counts[r["dielectric"]] = counts.get(r["dielectric"], 0) + 1
        except ValueError as e:
            out.append(("ERROR", f"review/export_check.toml: {e}"))
            counts = None
        groups_to_count = {} if counts is None else groups
        for d, g in groups_to_count.items():
            if d not in counts:
                out.append(("ERROR", f"review/export_check.toml group {d}: no row of {cat.name} has dielectric {d}"))
            elif g.get("rows") != counts[d]:
                out.append(("ERROR", f"review/export_check.toml group {d}: rows = {g.get('rows')} but {cat.name} has "
                                     f"{counts[d]} {d} rows ({rerun})"))
    for d, g in groups.items():
        v = g.get("verified")
        if v is None:
            continue
        stamp = EXPORT_STAMP(v)
        if stamp is None or (stamp["kind"] == "human" and stamp["group"] != d):
            out.append(("ERROR", f"review/export_check.toml group {d}: verified is not a human or machine export-check line "
                                 f"for group {d} (machine export-check <date> <group_sha256[:12]>; {rerun})"))
        elif stamp["kind"] == "machine":
            machine = True
            if stamp["sha12"] != str(g.get("group_sha256", ""))[:12]:
                out.append(("ERROR", f"review/export_check.toml group {d}: machine line {stamp['sha12']} is not the group's "
                                     f"group_sha256 {str(g.get('group_sha256', ''))[:12]} ({rerun})"))
    if machine:  # human lines stay valid whatever the tables hash (as lib.capacitor.current_groups)
        if rec.get("tables_sha256") != catalog.tables_sha256():
            out.append(("ERROR", f"review/export_check.toml is STALE: the decode tables of lib/catalog.py changed since the "
                                 f"export check (re-check them against the datasheet, then {rerun})"))
    name = rec.get("export", {}).get("file", "")
    root = folder.resolve().parents[2]
    found = catalog.find_exports(root, name)
    if not found:  # the comparison is re-run in every mode: the committed subset is the export CI has
        return out + [("ERROR", f"review/export_check.toml: {name or 'the cited export'} is not in docs/datasheets/, "
                                f"docs/vendor/ or docs/exports/ (commit the trimmed export: python3 -m lib.catalog "
                                f"export-subset <export>, then {rerun})")]
    for path in found:  # every copy must agree with the record (the full local export and the committed subset)
        try:
            res = catalog.export_check(folder, path)
        except ValueError as e:
            return out + [("ERROR", f"review/export_check.toml: {e}")]
        where = path.relative_to(root).as_posix() if path.is_relative_to(root) else path.name
        if res["export_rows_sha256"] != rec.get("export", {}).get("rows_sha256"):
            out.append(("ERROR", f"review/export_check.toml: the rows of {where} changed since the export check ({rerun})"))
        if res["result"] != "MATCH":
            out.append(("ERROR", f"export check is MISMATCH now ({where}): {'; '.join((res['differences'] + res['errors'])[:3])}"))
        for d, g in res["groups"].items():
            if groups.get(d, {}).get("group_sha256") != g["sha256"]:
                out.append(("ERROR", f"group {d} changed since its export check ({where}; {rerun})"))
    return out


def check_ledger(folder):
    """review/ (docs/spec/review.md). Always (ledger-only mode): valid TOML, nothing but review.toml under review/, a row per
    Param whose hash is the row's and whose stamp is its `verified`. Evidence mode (the row's PDF is in
    docs/datasheets/): its cache images (.review-cache/<Mfr>/<Value>/) exist with the ledger's SHA-256."""
    folder = Path(folder)
    f = folder / "review" / "review.toml"
    if not f.exists():
        return stray_review_files(folder)
    rerun = f"rerun python3 tools/ds_review.py {folder}"
    try:
        with open(f, "rb") as fh:
            ledger = tomllib.load(fh)
        with open(folder / "component.toml", "rb") as fh:
            comp = tomllib.load(fh)
        params = comp.get("param", {})
    except (OSError, tomllib.TOMLDecodeError) as e:
        return [("ERROR", f"review/review.toml or component.toml is not valid TOML ({e}): {rerun}")]
    out = stray_review_files(folder)
    rows, inp = ledger.get("row", {}), ledger.get("inputs", {})
    main = Path(inp.get("datasheet_file", "")).name
    # a variants.toml override: a row that matters is a full row (hash of base row + override fields, stamp = its own
    # `verified`), any other is REFERENCE (docs/spec/review.md "Variant overrides")
    over = {k: v for k, v in override_rows(folder, params).items()} if (folder / "variants.toml").is_file() else {}
    mat = review_status.matters(folder) if over else {}
    full = {**{k: (t, t) for k, t in params.items()}, **{k: v for k, v in over.items() if k in mat}}
    for key, (table, own) in full.items():
        r = rows.get(key)
        if not isinstance(r, dict) or r.get("hash") != row_hash(table):
            out.append(("ERROR", f"review/review.toml row {key} is missing or older than component.toml: {rerun}"))
        elif (r.get("stamp") or "") != (own.get("verified") or ""):
            out.append(("ERROR", f"review/review.toml row {key}: stamp differs from its verified line: {rerun}"))
        else:  # the state follows from the stamp, the row hash and the ledger's pins; never trust the written word
            P = (inp.get("sheets") or {}).get(r.get("sheet") or main, "")
            want = ledger_state_of(r["hash"], r.get("stamp") or "", r.get("stamp_hash") or "", r.get("pdf_sha256") or "", P)
            if r.get("state") != want:
                out.append(("ERROR", f"review/review.toml row {key}: state {r.get('state')!r} but the stamp and pins give "
                                     f"{want!r}: {rerun}"))
    pins, pr = comp.get("pin"), ledger.get("pinout")
    if pins:  # the pinout record (docs/spec/review-view.md "Pinout stamp"), checked like a row
        stamp = (comp.get("pinout") or {}).get("verified") or ""
        if not isinstance(pr, dict) or pr.get("hash") != pinout_hash(pins):
            out.append(("ERROR", f"review/review.toml pinout is missing or older than component.toml: {rerun}"))
        elif (pr.get("stamp") or "") != stamp:
            out.append(("ERROR", f"review/review.toml pinout: stamp differs from its verified line: {rerun}"))
        else:
            P = (inp.get("sheets") or {}).get(main, "")  # the pinout stamp binds the main PDF
            want = ledger_state_of(pr["hash"], stamp, pr.get("stamp_hash") or "", pr.get("pdf_sha256") or "", P, pinout=True)
            if pr.get("state") != want:
                out.append(("ERROR", f"review/review.toml pinout: state {pr.get('state')!r} but the stamp and pins give "
                                     f"{want!r}: {rerun}"))
    elif pr is not None:
        out.append(("ERROR", f"review/review.toml has a pinout record but component.toml has no [[pin]]: {rerun}"))
    for key, (_m, own) in over.items():
        if key not in mat and own.get("verified"):
            out.append(("ERROR", f"{key}: a reference override (the row does not matter) carries a `verified` line; remove it: "
                                 f"nothing to stamp"))
    for key in over:
        if key not in mat and (not isinstance(rows.get(key), dict) or rows[key].get("state") != "REFERENCE"):
            out.append(("ERROR", f"review/review.toml row {key}: an override of a row that does not matter must have state "
                                 f"'REFERENCE': {rerun}"))
    for key, r in rows.items():
        if key not in params and key not in over and (not isinstance(r, dict) or r.get("state") != "NOT_COVERED"):
            out.append(("ERROR", f"review/review.toml row {key}: not a Param, so its state must be 'NOT_COVERED': {rerun}"))
    root = _repo_root(folder) or ROOT
    cache = root / ".review-cache" / folder.resolve().relative_to(root / "components") if _repo_root(folder) else None
    ev = (_read_toml(cache / EVIDENCE) or {}) if cache else {}  # the local evidence record: what the PDF and the render decided

    def pdf(sheet):  # the main datasheet at its datasheet_file path, other sheets in docs/datasheets/
        return root / inp["datasheet_file"] if sheet == main and inp.get("datasheet_file") else root / "docs" / "datasheets" / sheet
    present, absent, matched = set(), set(), set()
    pages = [pg for pg in pr.get("page", []) if isinstance(pg, dict)] if isinstance(pr, dict) else []  # every cited page
    erow, epin = ev.get("row") or {}, ev.get("pinout") or {}
    epage = {(g.get("sheet", ""), g.get("pdf_page")): g for g in epin.get("page") or [] if isinstance(g, dict)}
    for key, r in list(rows.items()) + [("pinout", pg) for pg in pages]:
        # a ledger row (or pinout page) the cite placed on a PDF page has evidence images, once the PDF is local
        if not isinstance(r, dict) or not r.get("pdf_page") or r.get("state") in ("REFERENCE", "NOT_COVERED"):
            continue
        sheet = r.get("sheet") or main
        if not pdf(sheet).is_file() or cache is None:
            absent.add(sheet)
            continue
        present.add(sheet)
        pin = key == "pinout"
        e = epage.get((r.get("sheet", ""), r.get("pdf_page")), {}) if pin else erow.get(key) or {}
        if (epin.get("hash") != pr.get("hash")) if pin else (e.get("hash") != r.get("hash")):
            out.append(("ERROR", f"{cache.relative_to(root)}/{EVIDENCE} has no evidence of {key} for its current hash (PDF present): "
                                 f"{rerun}"))
            continue
        for field, sha_field in (("image", "image_sha256"), ("header_image", "header_sha256"), ("foot_image", "foot_sha256")):
            image = e.get(field, "")
            if not image:
                continue
            img = cache / image
            if not img.is_file():
                out.append(("ERROR", f"{img.relative_to(root)} missing ({key}; PDF present): {rerun} to render it"))
            elif hashlib.sha256(img.read_bytes()).hexdigest() != e.get(sha_field, ""):
                out.append(("ERROR", f"{img.relative_to(root)} sha256 differs from {EVIDENCE} ({key}): delete it and {rerun}"))
            else:
                matched.add(image)
    if not present and not absent:  # no row is placed on a page: the main PDF decides
        (present if main and pdf(main).is_file() else absent).add(main)
    REVIEW_MODES[str(folder)] = ("evidence" if present and not absent else "partial" if present else "ledger-only", len(matched))
    return out


def review_mode_line():
    """The mode check_ledger ran in, so a run without PDFs never reads as an evidence check."""
    modes = list(REVIEW_MODES.items())
    ev = [m for _, m in modes if m[0] != "ledger-only"]
    lo = [Path(d).name for d, m in modes if m[0] == "ledger-only"]
    pa = [Path(d).name for d, m in modes if m[0] == "partial"]
    out = []
    if ev:
        out.append(f"evidence mode (PDF present) in {len(ev)} part(s): {sum(m[1] for m in ev)} cache image(s) matched the "
                   f"ledger" + (f"; partial (a sheet missing): {', '.join(pa)}" if pa else ""))
    if lo:
        out.append(f"ledger-only mode (no local PDF) in {len(lo)} part(s): {', '.join(lo)}")
    return "review: " + ("; ".join(out) or "no review records")


def ledger_notes(folder):
    """Non-failing REVIEW notes for rows whose review state is STALE or PDF_CHANGED."""
    f = Path(folder) / "review" / "review.toml"
    try:
        rows = _ledger_rows(f)
    except (OSError, tomllib.TOMLDecodeError):
        return []
    return [f"{Path(folder).name}: {k} is {r['state']} (counts as unverified; rerun python3 tools/ds_review.py {folder})"
            for k, r in rows.items() if isinstance(r, dict) and r.get("state") in ("STALE", "PDF_CHANGED")]


def sheet_names(folder, root):
    """PDF names a cite of this part may name: the sheets its committed review.toml records (so CI knows them) plus the
    PDFs in root/docs/datasheets/ when that directory exists locally."""
    names = set()
    try:
        with open(Path(folder) / "review" / "review.toml", "rb") as f:
            names |= set((tomllib.load(f).get("inputs") or {}).get("sheets") or {})
    except (OSError, tomllib.TOMLDecodeError):
        pass
    d = Path(root) / "docs" / "datasheets"
    if d.is_dir():
        names |= {p.name for p in d.glob("*.pdf")}
    return names


def _check_component(folder):
    """All checks for one component directory. Returns [(level, message), ...].

    A family (variants.toml present): the shared file is checked once; each variant's merged params get the
    param and INPUTS checks, reported as 'variant <Value>: ...'.
    """
    folder = Path(folder)
    toml_file = folder / "component.toml"
    if not toml_file.exists():
        return [("ERROR", "component.toml not found")]
    try:
        with open(toml_file, "rb") as f:
            data = tomllib.load(f)
        variants = variants_of(folder)
    except tomllib.TOMLDecodeError as e:
        return [("ERROR", f"component.toml or variants.toml is not valid TOML: {e}")]
    part, pins = data.get("part", {}), data.get("pin", [])
    out = check_part(part, folder, family=bool(variants)) + check_pins(pins) + check_ledger(folder) + check_export_record(folder)
    out += finding_messages(rules.cite_findings(data, variants))
    out += finding_messages(rules.cite_sheet_findings(data, variants))
    out += finding_messages(rules.cite_unbracketed_findings(data, sheet_names(folder, ROOT), variants))
    out += finding_messages(rules.verified_findings(data, variants))
    for name in sorted({n for _, n in rules.cite_sheets(data, variants) if n.endswith('.pdf')}):
        if not (ROOT / "docs" / "datasheets" / name).exists():
            out.append(("WARN", f"datasheet_file not found: docs/datasheets/{name} (cited sheet; PDFs are not committed)"))
    names = {p.get("name") for p in pins}
    used = series.series_keys(part)
    if part.get("series") and variants:
        out.append(("ERROR", "a series component cannot be a family (variants.toml)"))
    elif part.get("series") == "capacitor":
        found, _ = check_capacitor_part(part, pins, data.get("param", {}), folder)
        out += found
    elif part.get("series"):
        out += check_series_part(part, pins, data.get("param", {}), folder)
    for key, table in data.get("param", {}).items():
        out += check_param(key, table, names, used_by_series=key in used)
    out += check_kicad(pins, part, folder)
    if not variants:
        calc_params = data.get("param", {})
        if part.get("series") == "capacitor":  # the part selection supplies these keys to INPUTS
            calc_params = {**calc_params, **{k: {"min": 0, "typ": 0, "max": 0} for k in capacitor.SELECTION_KEYS}}
        return out + check_calc(folder, calc_params)
    out += check_calc(folder, data.get("param", {}), inputs=False)
    for key, table in data.get("param", {}).items():
        for v in table.get("variants", []):
            if v not in variants:
                out.append(("ERROR", f"param {key}: variants names unknown variant '{v}'"))
    calc = load_calc(folder / "calc.py") if (folder / "calc.py").exists() else None
    for name in sorted(variants):
        merged = merge_variant(data, variants, name)
        found = [(lvl, f"variant {name}: {msg}") for lvl, msg in check_variant(merged, variants[name], names, calc)]
        out += found
    return out


def check_variant(merged, own, pin_names, calc):
    """Checks for one variant: required [part] fields, its override rows, INPUTS resolving in its merged params."""
    out = [("ERROR", f"[part] missing field '{f}'") for f in PART_FIELDS if f not in merged["part"] and f != "datasheet_url"]
    for f in ("mpn", "alternates", "temp_grade"):  # inherited values would silently be wrong for some variants
        if f not in own:
            out.append(("ERROR", f"must set its own {f} in variants.toml"))
    for key, table in own.get("param", {}).items():
        out += check_param(key, table, pin_names)
    return out + (check_inputs(calc, merged["param"]) if calc else [])


def find_components(args):
    """Directories from the command line (dir or component.toml path), else all in components/."""
    if not args:
        return sorted(p.parent for p in (ROOT / "components").glob("*/*/component.toml"))
    return [Path(a).parent if a.endswith("component.toml") else Path(a) for a in args]


TOLERATED = "datasheet_file not found"  # PDFs are git-ignored
TOLERATED_ALL = (TOLERATED, "datasheet_url empty")  # the only WARNs that do not fail the exit code


def collect(folders, root, full):
    """(findings, other messages) over all folders. findings are rules.Finding; other messages are (label, level, msg)
    for the older checks. Rule findings from check_component are tagged with the component; full adds repo-level rules."""
    findings, others, notes, reviews = [], [], [], []
    REVIEW_MODES.clear()
    for folder in folders:
        part = f"{folder.parent.name}/{folder.name}"
        for level, msg in check_component(folder, raw=True):
            parsed = rules.split_message(msg)
            if parsed and level == "ERROR":
                findings.append(rules.Finding(parsed[0], part, parsed[1], msg[rules.MESSAGE_RE.match(msg).end():]))
            else:
                others.append((part, level, msg))
        findings += rules.wiring_findings(folder, root)
        notes += abstentions(folder)
        reviews += ledger_notes(folder)
    if full:
        findings += rules.repo_findings(root) + rules.zen_lint_findings(root)
    return findings, others, notes, reviews


def main(argv=None):
    """Print problems, a summary, and return the exit code (1 on any ERROR, any WARN other than a missing datasheet
    file, a stale allowlist entry, or zero components found)."""
    args = sys.argv[1:] if argv is None else argv
    folders = find_components(args)
    findings, others, notes, reviews = collect(folders, ROOT, full=not args)
    errors = warns = tolerated = 0
    if not folders:
        print("ERROR: no components found (components/*/*/component.toml); nothing was checked")
        errors += 1
    for part, level, msg in others:
        if level == "WARN" and any(t in msg for t in TOLERATED_ALL):
            tolerated += 1
            continue
        print(f"{part}: {level}: {msg}")
        errors += level == "ERROR"
        warns += level == "WARN"
    for n in notes:
        print(f"ABSTAIN: {n}")
    for n in reviews:
        print(f"REVIEW: {n}")
    print(review_mode_line())
    abstained = len(notes)
    violations, allowed, stale = rules.apply_allowlist(findings, rules.load_allowlist())
    for f in violations:
        print(f"{f.part}: ERROR: {rules.text(f)}")
    errors += len(violations)
    if not args:  # a partial run cannot see every entry
        for e in stale:
            print(f"lib/known_findings.toml: ERROR: stale entry (matches nothing): {e['rule']} {e['part']} {e['location']}")
        errors += len(stale)
    print(f"{len(folders)} components, {errors} errors, {warns} warnings, {tolerated} tolerated (datasheets absent), "
          f"{len(allowed)} allowlisted findings, {abstained} abstained")
    return 1 if errors or warns else 0


if __name__ == "__main__":
    sys.exit(main())
