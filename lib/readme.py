"""Generate README.md per component: python3 -m lib.readme [component paths...]"""

import inspect
import sys
import tomllib
from pathlib import Path

from . import capacitor, series
from . import equations as eqlib
from .check import find_components
from . import review_status
from .review_status import checked_rows
from .component import ROOT, load, load_calc, merge_variant, restriction, run_example, variants_of
from .units import eng

HEADER = "<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->"
KINDS = ["abs_max", "rec_op", "electrical", "thermal", "mechanical"]
PARAM_HEADERS = ["Parameter", "Symbol", "Min", "Typ", "Max", "Unit", "Conditions", "Cite", "Checked"]
PART_ORDER = ["mpn", "alternates", "manufacturer", "description", "category", "package", "datasheet_url",
              "datasheet_file", "datasheet_rev", "datasheet_date", "temp_grade", "kicad_symbol",
              "kicad_footprint", "step"]
LABELS = {"mpn": "MPN", "alternates": "Alternate MPNs", "datasheet_url": "Datasheet URL",
          "datasheet_file": "Datasheet file", "datasheet_rev": "Datasheet revision",
          "datasheet_date": "Datasheet date", "temp_grade": "Temperature grade", "kicad_symbol": "Symbol file",
          "kicad_footprint": "Footprint file", "step": "3D model"}
GLOSSARY = "Terms: [glossary](../../../CONTRIBUTING.md#glossary)."
ZEN_LEGEND = "[wrapper checks](../../../docs/spec/wrapper.md#reading-the-zener-checks)"


def cell(x):
    """Markdown-safe table cell text."""
    return str(x).replace("|", "\\|").replace("\n", " ")


def md_table(headers, rows):
    """GitHub markdown table from a header list and a list of row lists."""
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    lines += ["| " + " | ".join(cell(c) for c in row) + " |" for row in rows]
    return "\n".join(lines) + "\n"


def shown(t, field):
    """A min/typ/max cell as printed: +/- for sym and typ_pm, text in the Typ column, ref pins, tol_pct as printed."""
    if field == "typ" and "text" in t:
        return t["text"]
    if "tol_pct" in t and field in ("min", "max"):
        return f"{t['tol_pct'][0 if field == 'min' else 1]:+g} %"
    if field not in t or (field == "min" and t.get("sym")):
        return ""
    value = str(t[field])
    if (field == "max" and t.get("sym")) or (field == "typ" and (t.get("typ_pm") or t.get("sym"))):
        return "\u00b1" + value
    ref = t.get(field + "_ref")
    return f"{value} (rel. {ref})" if ref else value


def param_rows(params, kind, checked=None):
    """Rows for one kind of parameter table, in TOML order. checked: {key: (login, date)} (lib.review_status)."""
    rows = []
    checked = checked or {}
    for key, t in params.items():
        if t.get("kind") != kind:
            continue
        cond = t.get("conditions", "") + (f" Variants: {', '.join(t['variants'])}." if t.get("variants") else "")
        if restriction(t):
            cond += f" Applies to: {restriction(t)}."
        cond += f" Note: {t['note']}" if t.get("note") else ""
        cite = t.get("cite", "") + (" (curve)" if t.get("curve") else "")
        rows.append([t.get("name", ""), t.get("symbol", ""), shown(t, "min"), shown(t, "typ"), shown(t, "max"),
                     t.get("unit", ""), cond.strip(), cite,
                     "checked ({}, {})".format(*checked[key]) if key in checked else ""])
    return rows


def inputs_text(args, params):
    """'Inputs:' lines for one function: arg -> param_key (printed values)."""
    lines = ""
    for arg, key in args.items():
        t = params.get(key.partition(".")[0])
        if t is None and key.partition(".")[0] in capacitor.SELECTION_KEYS:
            lines += f"- `{arg}` -> `{key}` (from the catalog part selection, `Part.select`)\n"
            continue
        if t is None:
            lines += f"- `{arg}` -> `{key}` (unknown key)\n"
            continue
        vals = " ".join(f"{f} {shown(t, f)}" for f in ("min", "typ", "max") if shown(t, f))
        lines += f"- `{arg}` -> `{key}` ({vals} {t.get('unit', '')})\n"
    return lines


def equations(calc, params):
    """Markdown for each public calc function's docstring and its INPUTS."""
    out = ""
    inputs = getattr(calc, "INPUTS", {})
    for name, fn in vars(calc).items():
        if inspect.isfunction(fn) and not name.startswith("_"):
            out += f"### `{name}`\n\n```\n{inspect.cleandoc(fn.__doc__ or '(no docstring)')}\n```\n\n"
            if name in inputs:
                out += "Inputs:\n\n" + inputs_text(inputs[name], params) + "\n"
    return out or "None.\n"


def examples(calc):
    """Markdown table of EXAMPLES rows with computed vs expected."""
    rows = []
    for row in getattr(calc, "EXAMPLES", []):
        fname, kwargs, expected, tol, cite = row
        try:
            got, ok = run_example(calc, row)
            result = "pass" if ok else "FAIL"
            got = f"{got:.6g}"
        except Exception as e:
            got, result = f"error: {e}", "FAIL"
        args = ", ".join(f"{k}={v:g}" for k, v in kwargs.items())
        rows.append([f"{fname}({args})", got, f"{expected:.6g}", f"{tol:g}", result, cite])
    if not rows:
        return "None.\n"
    return md_table(["Call", "Computed", "Expected", "Rel. tol", "Result", "Cite"], rows)


def zen_checks(params):
    """Which rows the generated Zener wrapper checks (check_pins / check_ambient) and which it leaves unchecked."""
    rows = []
    for key, t in params.items():
        if t.get("check_pins"):
            rows.append([key, t.get("name", ""), "pins " + ", ".join(t["check_pins"]), t.get("unchecked", "")])
        if t.get("check_ambient"):
            rows.append([key, t.get("name", ""), "board ambient", ""])
        if t.get("unchecked") and not t.get("check_pins"):
            rows.append([key, t.get("name", ""), "UNCHECKED", t["unchecked"]])
    if not rows:
        return "No Zener checks declared.\n"
    note = f"Generated wrapper: `{{v}}.zen` (`python3 -m lib.zen`). How each check reports: {ZEN_LEGEND}.\n\n"
    return note + md_table(["Param", "Name", "Checked against", "Not checked / reason"], rows)


def limits_line(tables):
    """'Limits of this data' text from the rows: scopes, curve and text rows, junction-only temperatures."""
    tables = list(tables)
    scopes = {}
    for t in tables:
        scopes[t.get("scope", "?")] = scopes.get(t.get("scope", "?"), 0) + 1
    text = "Rows by scope: " + ", ".join(f"{s} {n}" for s, n in sorted(scopes.items())) + " (25C rows hold only at 25 degC). "
    text += f"Curve (graph) rows: {sum(bool(t.get('curve')) for t in tables)}. "
    text += f"Text rows: {sum('text' in t for t in tables)}."
    tj = any(t.get("unit") == "degC" and t.get("kind") in ("abs_max", "rec_op")
             and ("TJ" in t.get("symbol", "").upper() or "junction" in t.get("name", "").lower()
                  or "junction" in t.get("symbol", "").lower()) for t in tables)
    if tj and not any(t.get("check_ambient") for t in tables):
        text += " Temperatures are junction (TJ): analyse with TJ = TA + P x RthJA; no ambient range is printed."
    return text + "\n"


def variants_table(part, variants):
    """Variants table: Value, MPN, alternates, temp_grade, then every other [part] key some variant overrides."""
    base = ("mpn", "alternates", "temp_grade")
    extra = sorted({k for v in variants.values() for k in v if k not in base + ("param",)})
    merged = {name: merge_variant({"part": part}, variants, name)["part"] for name in variants}
    cols = list(base) + extra
    rows = [[name] + [", ".join(m[k]) if isinstance(m.get(k), list) else m.get(k, "") for k in cols]
            for name, m in merged.items()]
    return md_table(["Value"] + cols, rows)


def param_table(rows, show_checked):
    """A parameter table; the Checked column appears only once some row of the part is checked."""
    if show_checked:
        return md_table(PARAM_HEADERS, rows)
    return md_table(PARAM_HEADERS[:-1], [r[:-1] for r in rows])


def variant_sections(variants, show_checked=False):
    """'Variant-specific parameters' tables, one per variant that has parameter overrides."""
    text = ""
    for name, v in variants.items():
        rows = [r for kind in KINDS for r in param_rows(v.get("param", {}), kind)]
        if rows:
            text += f"\n## Variant-specific parameters: {name}\n\n"
            text += param_table(rows, show_checked)
    return text


def series_section(folder):
    """'Series' section: range, E-series, MPN rule with examples, rated voltage formula and a table by decade."""
    part = load(folder)
    info, values = part.info, part.values()
    power = part.param(info["series_power"])
    vlim = part.param(info["series_vlimit"]) if "series_vlimit" in info else None
    vl_max = vlim.max if vlim else None
    pairs = part.pairs()
    options = series.options(info)
    if options:
        picks = [pairs[0], pairs[len(pairs) // 2], pairs[-1]]
        examples = ", ".join(f"{eng(v, 'ohm')} {c} -> `{part.mpn(v, c)}`" for v, c in picks)
    else:
        picks = [values[0], values[len(values) // 2], values[-1]]
        examples = ", ".join(f"{eng(v, 'ohm')} -> `{part.mpn(v)}`" for v in picks)
    decades = [v for v in (1e-3, 1e-2, 1e-1, 1, 10, 100, 1e3, 1e4, 1e5, 1e6) if v in values]
    rows = [[eng(v, "ohm"), eng(series.rated_voltage(v, power.max, vl_max), "V")] for v in decades]
    text = "\n## Series\n\n"
    text += f"- **Value range**: {eng(values[0], 'ohm')} to {eng(values[-1], 'ohm')} (`{info['value_param']}`)\n"
    text += f"- **E-series**: {', '.join(info['e_series'])} ({len(values)} values in range)"
    text += "".join(f"; {n} only from {eng(v, 'ohm')}" for n, v in info.get("series_eseries_min", {}).items()) + "\n"
    if options:
        text += "- **Tolerance options** (code, tolerance, range clipped to the series range, values; `Part.tolerance`, "
        text += "wrapper config `tolerance`):\n"
        for code, tkey, rkey in options:
            tol, n = part.param(tkey), len(part.values(code))
            vs = part.values(code)
            span = f"{eng(vs[0], 'ohm')} to {eng(vs[-1], 'ohm')}, {n} values" if vs else "no value in this series"
            text += f"  - `{code}`: +/-{tol.max * 100:g} % (`{tkey}`), {span} (`{rkey}`)\n"
    else:
        tol = part.param(info["series_tol"])
        text += f"- **Tolerance**: {tol.max * 100:g} % (`{info['series_tol']}`), used by `Part.series_value`\n"
    text += (f"- **MPN rule**: `calc.mpn(value{', tol_code' if options else ''})`; examples: {examples}\n")
    if series.tcr_rows(info):
        text += "- **TCR by value** (`Part.tcr(value)` returns the row whose range holds the value): "
        text += ", ".join(f"`{t}` for {eng(part.param(r).min, 'ohm')} to {eng(part.param(r).max, 'ohm')}"
                          for t, r in series.tcr_rows(info)) + "\n"
    if vlim:
        text += (f"- **Rated voltage**: min(sqrt(P70 x R), Vlimit), P70 = {eng(power.max, 'W')} (`{info['series_power']}`), "
                 f"Vlimit = {eng(vlim.max, 'V')} (`{info['series_vlimit']}`)\n")
    else:
        text += (f"- **Rated voltage**: sqrt(P70 x R), P70 = {eng(power.max, 'W')} (`{info['series_power']}`); the "
                 f"datasheet prints no limiting element voltage\n")
    p1, p2 = info.get("series_pins", ["P1", "P2"])
    text += (f"- **Zener wrapper**: config `value`{' and `tolerance` (a code)' if options else ''}, optional `v_across` (the module's "
             f"worst-case voltage across the part; replaces the net ranges in `rated_voltage` when set); checks `value_allowed` and "
             f"`rated_voltage` (|V({p1}) - V({p2})| <= derate x rated voltage). It uses the 70 degC power rating at every "
             f"ambient, so above 70 degC it is optimistic: use `calc.rated_power` (curve-based) for hot designs\n"
             f"- **Worst-case resistance**: `wca(calc.resistance_worst, r0=<value>, tol={"part.tolerance(<code>)" if options else "part.param('tol')"}, tcr={"part.tcr(<value>)" if series.tcr_rows(info) else "..."}, ...)` "
             f"with the plain value as r0; `Part.series_value(value)` already includes the tolerance, so do not pass it "
             f"as r0 together with tol (that counts the tolerance twice)\n\n")
    keys = f"`{info['series_power']}`" + (f", `{info['series_vlimit']}`" if vlim else "")
    text += f"Rated voltage at decade values, computed from {keys} and the formula above:\n\n"
    return text + md_table(["Resistance", "Rated voltage"], rows)


def capacitor_section(folder):
    """'Series' section of a capacitor series: catalog summary, MPN rule, selection API, wrapper and worst-case use."""
    part = load(folder)
    info, rows = part.info, part.catalog()
    letter, alts = info["package_default"], info["package_alternates"]
    example = rows[len(rows) // 2]
    table = []
    for d in part.dielectrics():
        of = [r for r in rows if r.dielectric == d]
        c = [r.c for r in of]
        table.append([d, len(of), f"{eng(min(c), 'F')} to {eng(max(c), 'F')}",
                      ", ".join(eng(v, "V") for v in sorted({r.v for r in of})),
                      ", ".join(sorted({r.tolerance for r in of})), f"`{info['tc_param'].get(d, '')}`"])
    text = "\n## Series\n\n"
    text += f"- **Catalog**: `{info['catalog']}`, {len(rows)} orderable values, one row per value with its cite (a manufacturer export, not a datasheet table)\n"
    text += (f"- **MPN rule**: catalog value + package letter; default `{letter}`, alternates {', '.join(f'`{a}`' for a in alts)} "
             f"(same part, other packaging); example: `{example.value}` -> `{example.value + letter}`\n")
    text += ("- **Selection**: `sel = part.select(capacitance, rated_voltage, dielectric, tolerance=None)` returns the MPN, "
             "`capacitance` / `rated_voltage` Params and `sel.part`, a Part holding the rows that apply (dielectric and "
             "part restrictions applied, plus `capacitance`, `tolerance`, `rated_v` and `tc`); an unlisted or ambiguous "
             "request raises ValueError\n")
    text += ("- **Zener wrapper**: configs `value`, `rated_v`, `dielectric`, optional `tolerance`; checks `part_orderable`, "
             "`rated_voltage` (|V(P1) - V(P2)| <= derate x rated voltage) and `ambient_range` (per dielectric)\n")
    text += ("- **Worst-case capacitance**: X7R (percent change): `wca(sel.part.calc.capacitance_worst_pct, "
             "**sel.part.inputs('capacitance_worst_pct'))`; C0G (ppm/degC): `wca(sel.part.calc.capacitance_worst_ppm, "
             "dt=Param(min=0, max=100), **sel.part.inputs('capacitance_worst_ppm'))` (dt required, 0 to 100 degC; below 25 degC "
             "use the printed drift rows). Both EXCLUDE DC-bias and aging loss\n\n")
    return text + md_table(["Dielectric", "Parts", "Capacitance", "Rated voltages", "Tolerances", "TC row"], table)


def build(folder):
    """README text for one component or family directory."""
    with open(folder / "component.toml", "rb") as f:
        data = tomllib.load(f)
    variants = variants_of(folder)
    part, shared = data.get("part", {}), data.get("param", {})
    checked = checked_rows(folder, local_pdf=False)  # ledger only: the README never depends on a local PDF or cache
    text = f"{HEADER}\n\n# {part.get('value', folder.name)}\n\n"
    r = review_status.review(folder, ROOT, local_pdf=False)
    text += f"{review_status.readme_line(folder.name, r)}\n\n{GLOSSARY}\n\n## Part\n\n"
    for key in PART_ORDER:
        val = part.get(key)
        if val in (None, "", []):
            continue
        if isinstance(val, list):
            val = ", ".join(val)
        if key == "datasheet_url":
            val = f"[{val}]({val})"
        text += f"- **{LABELS.get(key, key)}**: {val}\n"
    show_checked = bool(checked)
    if variants:
        text += "\n## Variants\n\nShared data below applies to every variant unless a row names its variants.\n\n"
        text += variants_table(part, variants)
    if part.get("series") == "capacitor":
        text += capacitor_section(folder)
    elif part.get("series"):
        text += series_section(folder)
    text += "\n## Pins\n\n"
    pin_rows = [[p.get(k, "") for k in ("number", "name", "type", "function", "cite")] for p in data.get("pin", [])]
    text += md_table(["Pin", "Name", "Type", "Function", "Cite"], pin_rows)
    for kind in KINDS:
        rows = param_rows(shared, kind, checked)
        if rows:
            text += f"\n## Parameters: {kind}\n\n"
            text += param_table(rows, show_checked)
    text += variant_sections(variants, show_checked)
    every = list(shared.values()) + [t for v in variants.values() for t in v.get("param", {}).values()]
    text += "\n## Limits of this data\n\n" + limits_line(every)
    lookup = {k: t for v in variants.values() for k, t in v.get("param", {}).items()} | shared  # for INPUTS text
    calc = load_calc(folder / "calc.py") if (folder / "calc.py").exists() else None
    wrapper = "<Variant>" if variants else part.get("value", folder.name)
    text += "\n## Zener checks\n\n" + zen_checks(shared).replace("{v}", wrapper)
    for name, v in variants.items():
        if v.get("param"):
            text += f"\n### Zener checks: variant {name}\n\n" + zen_checks(v["param"]).replace("{v}", name)
    text += "\n## Equations\n\n" + (equations(calc, lookup) if calc else "No calc.py.\n")
    text += "\n## Examples\n\n" + (examples(calc) if calc else "No calc.py.\n")
    return text


START, END = "<!-- review-status:start -->", "<!-- review-status:end -->"


def _parts(root):
    """[(manufacturer, value, description, review dict)] for every component directory under root (ledger only)."""
    out = []
    for toml in sorted(Path(root).glob("components/*/*/component.toml")):
        d = toml.parent
        desc = (tomllib.loads(toml.read_text(encoding="utf-8")).get("part") or {}).get("description", "")
        out.append((d.parent.name, d.name, desc, review_status.review(d, root, local_pdf=False)))
    return out


def top_table(root):
    """The README block: counts and a link, never one line per part (the list grows with the library)."""
    parts = _parts(root)
    released = sum(r["released"] for *_, r in parts)
    mfrs = len({m for m, *_ in parts})
    return (f"{len(parts)} parts from {mfrs} manufacturers, {released} released (every row that matters checked by a "
            f"person). One line per part, by manufacturer: [docs/PARTS.md](docs/PARTS.md). Is a part safe to use: "
            f"`python3 tools/status.py <Value>`.\n")


def parts_index(root):
    """docs/PARTS.md: generated, one section per manufacturer, one line per part with its review status."""
    parts = _parts(root)
    text = ("# Parts\n\nGenerated by `python3 -m lib.readme`; do not edit. Status counts the rows that matter that a "
            "person has checked ([glossary](../CONTRIBUTING.md#glossary)). Single part: `python3 tools/status.py <Value>`.\n")
    for mfr in sorted({m for m, *_ in parts}):
        rows = []
        for m, value, desc, r in parts:
            if m == mfr:
                status = "released" if r["released"] else f"{r['k']} of {r['n']}"
                rows.append([f"[{value}](../components/{m}/{value}/README.md)", desc, status])
        text += f"\n## {mfr}\n\n" + md_table(["Part", "What", "Status"], rows)
    return text


def equations_index(root):
    """docs/EQUATIONS.md: generated, one row per equation record of the library (docs/spec/equations.md). No state column: stamping
    must not force a regeneration, and the file is the same on every Python."""
    text = ("# Equations\n\nGenerated by `python3 -m lib.readme`; do not edit. One row per `equations.toml` record; the review "
            "state is computed, never listed here (`python3 tools/equations.py check`, `docs/spec/equations.md`). Find a record before writing one: `python3 tools/equations.py find <terms>`.\n\n")
    eqs = eqlib.library_equations(root)
    if not eqs:
        return text + "No equation records yet.\n"
    rows = []
    for r, eq in zip(eqlib.index_rows(eqs), sorted(eqs, key=lambda e: e.id)):
        part = f"[{r['part']}](../components/{eq.toml.parent.parent.name}/{r['part']}/README.md)"
        rows.append([f"`{r['id']}`", r["title"], r["kind"], r["unit"], r["symbols"], part])
    return text + md_table(["Id", "Title", "Kind", "Result unit", "Symbols", "Part"], rows)


TOP_FILES = ("README.md", "docs/EQUATIONS.md", "docs/PARTS.md")  # every file outside components/ that update_top writes; tools check against this


def update_top(root):
    """Rewrite the block between the review-status markers of root/README.md and write root/docs/PARTS.md; False
    when there is no README or marker."""
    f = Path(root) / "README.md"
    if not f.is_file():
        return False
    text = f.read_text(encoding="utf-8")
    if START not in text or END not in text or text.index(START) > text.index(END):
        return False
    head, rest = text.split(START, 1)
    tail = rest.split(END, 1)[1]
    f.write_text(f"{head}{START}\n{top_table(root)}{END}{tail}", encoding="utf-8")
    (Path(root) / "docs").mkdir(exist_ok=True)
    (Path(root) / "docs" / "PARTS.md").write_text(parts_index(root), encoding="utf-8")
    (Path(root) / "docs" / "EQUATIONS.md").write_text(equations_index(root), encoding="utf-8")
    return True


def main(argv=None):
    """Write README.md in each component directory, then the parts summary in the top README.md and docs/PARTS.md (components of this
    repo only)."""
    folders = find_components(sys.argv[1:] if argv is None else argv)
    for folder in folders:
        (folder / "README.md").write_text(build(folder), encoding="utf-8")
        print(f"wrote {folder / 'README.md'}")
    if any(ROOT in Path(f).resolve().parents for f in folders) and update_top(ROOT):
        print(f"wrote {ROOT / 'README.md'} (parts summary), docs/PARTS.md and docs/EQUATIONS.md")


if __name__ == "__main__":
    main()
