"""Structural rules for `python3 -m lib.check` that need no judgement, plus the known-findings allowlist.

Every rule returns Finding(rule, part, location, message). `part` is "<Mfr>/<Value>" for a component or a
repo-relative path; (rule, part, location) is the exact-match key of an entry in lib/known_findings.toml.
A rule that cannot decide structurally abstains (returns nothing, or reports an Abstain) and never guesses.
"""

import ast
import os
import datetime
import re
import tomllib
from collections import namedtuple
from pathlib import Path

from . import kicad

Finding = namedtuple("Finding", "rule part location message")
Abstain = namedtuple("Abstain", "rule part reason")
ALLOWLIST = Path(__file__).with_name("known_findings.toml")
GRID = 2.54  # mm: symbol pins sit on a 100 mil grid (docs/KICAD.md, Symbol)
COURTYARD_MARGIN = 0.25  # mm beyond the larger of pads and body (docs/KICAD.md, Footprint)
GEOM_TOL = 0.005  # mm

# DS p.<printed page>, ... | DS PDF p.<n>, ... ; a Murata sheet may be named in parentheses after the page number.
CITE_RE = re.compile(r"^DS (?:PDF )?p\.\d+(?:-\d+)?(?: \([^()]+\))?, \S")
PCB_VERSION_RE = re.compile(r"^\d+\.\d+$")
# A cite from a document other than datasheet_file names it in brackets after the page: DS p.7 (<file>.pdf), ...
SHEET_RE = re.compile(r"^DS (?:PDF )?p\.\d+(?:-\d+)? \(([^()]+)\), ")


def text(f):
    """Message form used by lib.check: '[rule] location: message' (location contains no ': ')."""
    return f"[{f.rule}] {f.location}: {f.message}"


MESSAGE_RE = re.compile(r"^\[([a-z0-9-]+)\] (.+?): ")


def split_message(msg):
    """(rule, location) of a '[rule] location: message' string, or None for an older-style message."""
    m = MESSAGE_RE.match(msg)
    return (m.group(1), m.group(2)) if m else None


# ---------------------------------------------------------------- allowlist

def load_allowlist(path=ALLOWLIST):
    """[[finding]] entries (part, location, rule, reason, found). A missing file is an error, never an empty list."""
    with open(path, "rb") as f:
        entries = tomllib.load(f).get("finding", [])
    for e in entries:
        missing = [k for k in ("part", "location", "rule", "reason", "found") if not e.get(k)]
        if missing:
            raise ValueError(f"{path}: allowlist entry {e} is missing {missing}")
    return entries


def apply_allowlist(findings, entries):
    """(violations, allowed, stale): findings not in the list, findings matched, entries that matched nothing."""
    keys = {(e["rule"], e["part"], e["location"]): e for e in entries}
    seen, violations, allowed = set(), [], []
    for f in findings:
        k = (f.rule, f.part, f.location)
        if k in keys:
            allowed.append(f)
            seen.add(k)
        else:
            violations.append(f)
    stale = [e for k, e in keys.items() if k not in seen]
    return violations, allowed, stale


# ---------------------------------------------------------------- repo level (B)

def repo_findings(root):
    """No PDF under components/, pcb-version major.minor, [workspace] only in the root pcb.toml, component pcb.toml empty.

    The walk covers hidden and git-ignored directories. It skips .git (object store) and the top-level .pcb/, which
    holds only symlinks to the toolchain's own stdlib and download cache (not repo content; a walk does not follow
    symlinks and would see nothing there anyway)."""
    root = Path(root)
    out = []
    for dirpath, dirs, files in os.walk(root / "components"):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in files:
            if name.lower().endswith(".pdf"):
                rel = (Path(dirpath) / name).relative_to(root).as_posix()
                out.append(Finding("no-pdf", rel, "file", "PDFs live in docs/datasheets/, never under components/"))
    root_toml = root / "pcb.toml"
    if not root_toml.exists():
        out.append(Finding("pcb-version", "pcb.toml", "file", "root pcb.toml is missing"))
    else:
        try:
            ws = tomllib.loads(root_toml.read_text(encoding="utf-8")).get("workspace", {})
        except tomllib.TOMLDecodeError as e:
            ws, _ = {}, out.append(Finding("pcb-version", "pcb.toml", "file", f"not valid TOML: {e}"))
        version = ws.get("pcb-version")
        if not (isinstance(version, str) and PCB_VERSION_RE.match(version)):
            out.append(Finding("pcb-version", "pcb.toml", "pcb-version",
                               f"pcb-version = {version!r} must be major.minor only (\"0.4\"); \"0.4.95\" breaks every build"))
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d != ".git" and not (Path(dirpath) == root and d == ".pcb")]
        if "pcb.toml" in files and Path(dirpath) != root:
            path = Path(dirpath) / "pcb.toml"
            rel = path.relative_to(root).as_posix()
            data = path.read_text(encoding="utf-8")
            try:
                has_ws = "workspace" in tomllib.loads(data)
            except tomllib.TOMLDecodeError:
                has_ws = "[workspace" in data
            if has_ws:
                out.append(Finding("nested-workspace", rel, "[workspace]", "only the root pcb.toml may have [workspace]"))
            elif Path(dirpath).parent.parent == root / "components" and data.strip():
                out.append(Finding("component-pcb-toml-empty", rel, "file",
                                   "a component pcb.toml is empty (docs/spec/wrapper.md: lib.zen writes an empty file)"))
    return out


# ---------------------------------------------------------------- per component, repo context (C)

def cases_components(root):
    """Set of component dirs ('Mfr/Value') named in the first column of CASES in tests/test_zen.py, or None if unreadable."""
    path = Path(root) / "tests" / "test_zen.py"
    if not path.exists():
        return None
    for node in ast.parse(path.read_text(encoding="utf-8")).body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "CASES" for t in node.targets):
            return {r.elts[0].value for r in node.value.elts if isinstance(r, ast.Tuple) and r.elts
                    and isinstance(r.elts[0], ast.Constant)}
    return None


def wiring_findings(folder, root):
    """Harness file, a CASES row and a root README parts-table row exist for this component directory."""
    root, folder = Path(root), Path(folder)
    part = f"{folder.parent.name}/{folder.name}"
    out = []
    if not (root / "tests" / "zen" / f"{folder.name}_harness.zen").exists():
        out.append(Finding("harness-missing", part, "tests/zen", f"tests/zen/{folder.name}_harness.zen does not exist"))
    cases = cases_components(root)
    if cases is None:
        out.append(Finding("cases-row", part, "tests/test_zen.py", "CASES not found in tests/test_zen.py"))
    elif part not in cases:
        out.append(Finding("cases-row", part, "tests/test_zen.py", f"no CASES row for '{part}' in tests/test_zen.py"))
    readme = root / "README.md"
    link = f"components/{part}/README.md"
    if not readme.exists() or link not in readme.read_text(encoding="utf-8"):
        out.append(Finding("readme-row", part, "README.md", f"root README.md parts table has no row linking {link}"))
    return out


# ---------------------------------------------------------------- per component, content (D, E)

VERIFIED_RE = re.compile(r"^\S+ (\d{4}-\d{2}-\d{2}) \S.*$")
SHEET_NAME_RE = re.compile(r"^[A-Za-z0-9_.-]+\.pdf$")


def _verified_ok(text):
    m = VERIFIED_RE.match(str(text))
    if not m:
        return False
    try:
        datetime.date.fromisoformat(m[1])
    except ValueError:
        return False
    return True


def verified_findings(data, variants=None):
    """Validate reviewer stamps and explicit provenance (docs/spec/extract.md, Fields)."""
    items = [(f"param {k}", t) for k, t in data.get("param", {}).items()]
    for v, table in (variants or {}).items():
        items += [(f"variant {v} param {k}", t) for k, t in table.get("param", {}).items()]
    allowed_types = {"human_page_image", "cross_model_page_image", "manufacturer_export"}
    out = []
    for loc, row in items:
        stamp = row.get("verified")
        kind = row.get("verification_type")
        if stamp is not None and not _verified_ok(stamp):
            out.append(Finding("verified-format", "", loc,
                               f"verified '{stamp}' is not '<who> <YYYY-MM-DD> <method>'"))
        if kind is not None and (not isinstance(kind, str) or kind not in allowed_types):
            out.append(Finding("verification-type", "", loc,
                               f"verification_type '{kind}' must be one of {', '.join(sorted(allowed_types))}"))
        if kind is not None and stamp is None:
            out.append(Finding("verification-type", "", loc, "verification_type requires a verified stamp"))
    return out


def cite_sheets(data, variants=None):
    """(location, name) for every cite that names a source sheet in brackets after its page."""
    items = [(f"pin {p.get('number')}", p.get("cite")) for p in data.get("pin", [])]
    items += [(f"param {k}", t.get("cite")) for k, t in data.get("param", {}).items()]
    for v, table in (variants or {}).items():
        items += [(f"variant {v} param {k}", t.get("cite")) for k, t in table.get("param", {}).items()]
    out = []
    for loc, c in items:
        m = SHEET_RE.match(c or "")
        if m:
            out.append((loc, m[1]))
    return out


def cite_sheet_findings(data, variants=None):
    """A bracketed source in a cite must be a PDF file name (docs/spec/extract.md, Cite); existence is checked by
    lib.check like datasheet_file (a missing PDF is the tolerated warning: PDFs are not committed)."""
    return [Finding("cite-sheet", "", loc, f"source '{name}' is not a PDF file name; write 'DS p.<n> (<file>.pdf), ...'")
            for loc, name in cite_sheets(data, variants) if not SHEET_NAME_RE.match(name)]


def cite_findings(data, variants=None):
    """Every [[pin]] and [param.*] cite (and variant param cites) matches CITE_RE."""
    items = [(f"pin {p.get('number')}", p.get("cite")) for p in data.get("pin", [])]
    items += [(f"param {k}", t.get("cite")) for k, t in data.get("param", {}).items()]
    for v, table in (variants or {}).items():
        items += [(f"variant {v} param {k}", t.get("cite")) for k, t in table.get("param", {}).items()]
    return [Finding("cite-format", "", loc, f"cite '{c}' does not match 'DS p.<n>, <table>, <row>' or 'DS PDF p.<n>, <drawing>'")
            for loc, c in items if c and not CITE_RE.match(c)]


def inputs_coverage_findings(calc):
    """Every public function defined in calc.py has an INPUTS entry (docs/spec/extract.md, calc.py)."""
    inputs = getattr(calc, "INPUTS", None) or {}
    out = []
    for name, fn in sorted(vars(calc).items()):
        if (callable(fn) and getattr(fn, "__module__", None) == calc.__name__ and not name.startswith("_")
                and isinstance(fn, type(lambda: 0)) and name not in inputs):
            out.append(Finding("inputs-coverage", "", name, f"function '{name}' has no INPUTS entry"))
    return out


def example_comment_findings(path):
    """An EXAMPLES row with tolerance > 1e-3 needs a comment on one of its lines or on the line before it."""
    src = Path(path).read_text(encoding="utf-8")
    lines = src.splitlines()
    out = []
    for node in ast.parse(src).body:
        if not (isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "EXAMPLES" for t in node.targets)
                and isinstance(node.value, (ast.List, ast.Tuple))):
            continue
        for row in node.value.elts:
            if not (isinstance(row, ast.Tuple) and len(row.elts) >= 4):
                continue
            tol = row.elts[3]
            try:
                value = ast.literal_eval(tol)
            except ValueError:
                continue  # not a literal: abstain
            if not isinstance(value, (int, float)) or value <= 1e-3:
                continue
            span = lines[row.lineno - 1:row.end_lineno]
            before = lines[row.lineno - 2].strip() if row.lineno >= 2 else ""
            fn = row.elts[0].value if isinstance(row.elts[0], ast.Constant) else "?"
            if not (any("#" in ln for ln in span) or before.startswith("#")):
                out.append(Finding("example-tolerance-comment", "", f"EXAMPLES line {row.lineno} {fn}",
                                   f"tolerance {value:g} is looser than 1e-3 and the row has no comment saying why"))
    return out


# ---------------------------------------------------------------- KiCad (G)

def symbol_grid_findings(sym):
    """Every symbol pin's connection point (at x y) is on the 2.54 mm grid."""
    out = []
    for pin in kicad.find_all(kicad.read(sym), "pin"):
        if len(pin) > 2 and isinstance(pin[1], str):
            at = next((c for c in pin if isinstance(c, list) and c and c[0] == "at"), None)
            if not at or len(at) < 3:
                continue
            x, y = float(at[1]), float(at[2])
            if any(abs(round(v / GRID) * GRID - v) > GEOM_TOL for v in (x, y)):
                out.append(Finding("symbol-grid", "", f"pin {kicad._field(pin, 'number')}",
                                   f"pin at ({x:g}, {y:g}) mm is off the {GRID} mm grid"))
    return out


def _layer(node):
    return kicad._field(node, "layer")


def _xy(node, key):
    child = next(c for c in node if isinstance(c, list) and c and c[0] == key)
    return float(child[1]), float(child[2])


def _graphic_points(node):
    """Points of an fp_line / fp_rect / fp_poly / fp_circle; None when the shape is not exactly bounded (arc)."""
    kind = node[0]
    if kind in ("fp_line", "fp_rect"):
        return [_xy(node, "start"), _xy(node, "end")]
    if kind == "fp_poly":
        pts = next(c for c in node if isinstance(c, list) and c and c[0] == "pts")
        return [(float(p[1]), float(p[2])) for p in pts if isinstance(p, list) and p and p[0] == "xy"]
    if kind == "fp_circle":
        (cx, cy), (ex, ey) = _xy(node, "center"), _xy(node, "end")
        r = ((cx - ex) ** 2 + (cy - ey) ** 2) ** 0.5
        return [(cx - r, cy - r), (cx + r, cy + r)]
    return None


def _bbox(points):
    xs, ys = [p[0] for p in points], [p[1] for p in points]
    return min(xs), min(ys), max(xs), max(ys)


def _fab_rects(fab):
    """Closed axis-aligned rectangles on F.Fab as (x0, y0, x1, y1): fp_rect, a 4-corner axis-aligned fp_poly, or four
    axis-aligned fp_line segments forming one."""
    rects = []
    for n in fab:
        pts = _graphic_points(n)
        if n[0] == "fp_rect":
            rects.append(_bbox(pts))
        elif n[0] == "fp_poly":
            uniq = list(dict.fromkeys(pts))
            if len(uniq) == 4 and len({round(x, 4) for x, _ in uniq}) == 2 and len({round(y, 4) for _, y in uniq}) == 2:
                rects.append(_bbox(uniq))
    segs = [_graphic_points(n) for n in fab if n[0] == "fp_line"]
    hs = [(min(a[0], b[0]), max(a[0], b[0]), a[1]) for a, b in segs if abs(a[1] - b[1]) <= GEOM_TOL]
    vs = [(a[0], min(a[1], b[1]), max(a[1], b[1])) for a, b in segs if abs(a[0] - b[0]) <= GEOM_TOL]
    close = lambda a, b: abs(a - b) <= GEOM_TOL
    for h0 in hs:
        for h1 in hs:
            if h0[2] < h1[2] - GEOM_TOL and close(h0[0], h1[0]) and close(h0[1], h1[1]):
                x0, x1, y0, y1 = h0[0], h0[1], h0[2], h1[2]
                has = lambda x: any(close(v[0], x) and close(v[1], y0) and close(v[2], y1) for v in vs)
                if has(x0) and has(x1):
                    rects.append((x0, y0, x1, y1))
    return rects


def courtyard_findings(fp):
    """Courtyard (F.CrtYd) bounding box is at least 0.25 mm beyond the pads on every side (exact), and beyond the body
    when F.Fab holds exactly one closed axis-aligned rectangle enclosing every pad centre (the body outline; several
    rectangles, such as capacitor-plate drawings, make the outline ambiguous).

    Returns (findings, abstain reason or None). Pads always checked. The body part abstains (reason returned, pad
    findings still reported) when F.Fab has no such rectangle (a symbolic drawing, arcs, open outline). The whole
    check abstains for: no F.CrtYd, an arc on F.CrtYd, a custom or trapezoid pad, a pad rotated off a multiple of 90."""
    root = kicad.read(fp)
    graphics = [n for n in root if isinstance(n, list) and n and n[0] in ("fp_line", "fp_rect", "fp_poly", "fp_circle", "fp_arc")]
    crt = [n for n in graphics if _layer(n) == "F.CrtYd"]
    fab = [n for n in graphics if _layer(n) == "F.Fab"]
    if not crt:
        return [], "no F.CrtYd graphics"
    if any(n[0] == "fp_arc" for n in crt):
        return [], "arc on F.CrtYd"
    pads, centres = [], []
    for pad in (n for n in root if isinstance(n, list) and n and n[0] == "pad"):
        if pad[3] in ("custom", "trapezoid"):
            return [], f"{pad[3]} pad {pad[1]}"
        at, size = next(c for c in pad if isinstance(c, list) and c and c[0] == "at"), _xy(pad, "size")
        rot = float(at[3]) if len(at) > 3 else 0.0
        if rot % 90 != 0:
            return [], f"pad {pad[1]} rotated {rot:g} degrees"
        w, h = (size[1], size[0]) if rot % 180 == 90 else size
        x, y = float(at[1]), float(at[2])
        pads += [(x - w / 2, y - h / 2), (x + w / 2, y + h / 2)]
        centres.append((x, y))
    if not pads:
        return [], "no pads"
    ext = list(pads)
    abstain = None
    rects = _fab_rects(fab)
    encloses = lambda r: all(r[0] - GEOM_TOL <= x <= r[2] + GEOM_TOL and r[1] - GEOM_TOL <= y <= r[3] + GEOM_TOL for x, y in centres)
    if len(rects) == 1 and encloses(rects[0]):
        ext += [(rects[0][0], rects[0][1]), (rects[0][2], rects[0][3])]
    else:
        abstain = "body not checked: F.Fab needs exactly one closed axis-aligned rectangle, enclosing every pad centre"
    cx0, cy0, cx1, cy1 = _bbox([p for n in crt for p in _graphic_points(n)])
    bx0, by0, bx1, by1 = _bbox(ext)
    need = COURTYARD_MARGIN - GEOM_TOL
    out = []
    for side, margin in (("xmin", bx0 - cx0), ("ymin", by0 - cy0), ("xmax", cx1 - bx1), ("ymax", cy1 - by1)):
        if margin < need:
            out.append(Finding("courtyard-margin", "", side,
                               f"courtyard is {margin:.3f} mm beyond the pads/body, needs {COURTYARD_MARGIN} mm"))
    return out, abstain


# ---------------------------------------------------------------- Zener lint (F)

# `Module("../...` or `Module("./..`: a relative path that leaves the package fails.
MODULE_ESCAPE_RE = re.compile(r'Module\(\s*"(?:\.\./|\./\.\.)')
# A temperature range string with a unit on one end only ("-40 to 85°C" parses as -313.15 degC).
UNIT = r"(?:°C|degC|°F|K)"
NUM = r"[+-]?\d+(?:\.\d+)?"
RANGE_RE = re.compile(rf'"\s*({NUM})\s*({UNIT})?\s+to\s+({NUM})\s*({UNIT})?\s*"')
WRAPPER_BAD_RE = re.compile(r"sqrt\(|\*\*")


def _code(line):
    """The part of a Zener line before a # comment (a # inside a string literal is not handled; none occur)."""
    return line.split("#", 1)[0]


def zen_lint_findings(root):
    """Module() paths that escape; one-ended temperature units in harnesses; sqrt( or ** in generated wrappers."""
    root = Path(root)
    out = []
    for base, kind in ((root / "components", "wrapper"), (root / "tests" / "zen", "harness")):
        for dirpath, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if d not in (".git", ".pcb")]
            for name in sorted(files):
                if not name.endswith(".zen"):
                    continue
                path = Path(dirpath) / name
                rel = path.relative_to(root).as_posix()
                for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                    code = _code(line)
                    if MODULE_ESCAPE_RE.search(code):
                        out.append(Finding("zen-module-path", rel, f"line {n}", "Module() path leaves the package; load by URL or ./"))
                    if kind == "harness":
                        for m in RANGE_RE.finditer(code):
                            if bool(m.group(2)) != bool(m.group(4)) :
                                out.append(Finding("zen-temp-unit", rel, f"line {n}",
                                                   f"range {m.group(0).strip()} has a unit on one end only"))
                    elif WRAPPER_BAD_RE.search(code):
                        out.append(Finding("zen-no-sqrt-pow", rel, f"line {n}", "Zener has no sqrt( or **; compare squares"))
    return out
