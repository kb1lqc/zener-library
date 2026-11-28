"""Equation records, hash, state, search, index and review page (docs/spec/equations.md).

Pure functions, stdlib only (no matplotlib needed), usable from another repo: `from lib import equations`.
Nothing here writes a file except `write_stamp` (called by a person's tools/equations.py) and `write_page`.
"""

import ast
import copy
import dataclasses
import hashlib
import html
import json
import os
import re
import sys
import textwrap
import tomllib
from pathlib import Path

KINDS = ("datasheet", "derived")
STATES = ("HUMAN_VERIFIED", "STALE", "NEW", "MACHINE_ONLY", "FIX_FIRST", "UNKNOWN")
PINNED_PYTHON = (3, 12)  # ast.dump differs between minor versions, so hashes and stamps are only valid on this one
RUNNING_PYTHON = tuple(sys.version_info[:2])  # read at call time (tests replace it)
FIELDS = {"title", "kind", "latex", "symbols", "cite", "extends", "constants", "note", "reuse_search", "verified"}
SYMBOL_FIELDS = ("tex", "meaning", "unit")
CONSTANT_FIELDS = ("value", "unit", "basis")
DERIVED_CITE = "not a datasheet equation"
LOGIN = r"[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}"  # same rule as lib.component.GITHUB_LOGIN
STAMP_RE = re.compile(rf"^human:({LOGIN}) (\d{{4}}-\d{{2}}-\d{{2}}) equation-review (\S+) hash ([0-9a-f]{{12}})$")
FLAG_WORDS = ("estimate", "assumed", "read as")
FIND_LIMIT = 8
AGENT = "refused: running inside Claude Code (CLAUDECODE is set); a person must run the stamp in their own shell"


class EquationsError(Exception):
    """A file that cannot be read at all (not a per-record finding)."""


@dataclasses.dataclass
class Equation:
    id: str
    fn: str
    record: dict
    toml: Path
    py: Path
    src: str = ""          # dedented function source
    start: int = 0         # first source line (1-based, decorators included)
    hash: str = ""
    errors: list = dataclasses.field(default_factory=list)
    state: str = "FIX_FIRST"
    calls: list = dataclasses.field(default_factory=list)      # callee names defined in the same module
    warnings: list = dataclasses.field(default_factory=list)   # non-trivial numeric literals
    module: object = None  # imported calc module (EXAMPLES), only when loaded with import_module

    @property
    def ref(self):
        """`<Value>:<fn>` for the stamp command (library ids are `<Value>.<fn>`)."""
        return f"{self.id.rsplit('.', 1)[0]}:{self.fn}"


# ---------------------------------------------------------------- functions

def _functions(text):
    """{name: (node, source lines)} for the top-level functions of a module's text."""
    tree = ast.parse(text)
    lines = text.splitlines()
    out = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            start = min([node.lineno] + [d.lineno for d in node.decorator_list])
            out[node.name] = (node, start, "\n".join(lines[start - 1:node.end_lineno]))
    return out


def params_of(node):
    """Parameter names in order; `*args` and `**kwargs` are reported with their star (they cannot have symbols)."""
    a = node.args
    names = [x.arg for x in a.posonlyargs + a.args + a.kwonlyargs]
    return names + (["*" + a.vararg.arg] if a.vararg else []) + (["**" + a.kwarg.arg] if a.kwarg else [])


def version_warning():
    """One WARN line when this Python is not the pinned minor version (states are then UNKNOWN), else None."""
    if RUNNING_PYTHON == PINNED_PYTHON:
        return None
    return (f"WARN equations: running Python {RUNNING_PYTHON[0]}.{RUNNING_PYTHON[1]}, hashes are valid on "
            f"{PINNED_PYTHON[0]}.{PINNED_PYTHON[1]} only; every state shows UNKNOWN and stamping is refused")


def function_dump(src):
    """ast.dump of the dedented function without its docstring: comments, formatting and docstring do not change it."""
    node = ast.parse(textwrap.dedent(src)).body[0]
    if node.body and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[0], "value", None), ast.Constant) \
            and isinstance(node.body[0].value.value, str):
        node.body = node.body[1:]
    return ast.dump(node)


def record_hash(record, src):
    """SHA-256 hex of the record without `verified`, a newline and the function's ast.dump."""
    rec = {k: v for k, v in record.items() if k != "verified"}
    text = json.dumps(rec, sort_keys=True, separators=(",", ":")) + "\n" + function_dump(src)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def numeric_warnings(node):
    """Sorted `<literal> (line N)` for numeric literals other than integers 0 to 10 and 0.5."""
    seen = {}
    for n in ast.walk(node):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
            v = n.value
            if v == 0.5 or (float(v) == int(v) and 0 <= v <= 10):
                continue
            seen.setdefault(repr(v), n.lineno)
    return [f"{k} (line {seen[k]})" for k in sorted(seen)]


def callees(node, names):
    """Names from `names` (this module's functions) called in the body, sorted, without the function itself."""
    found = {n.func.id for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
    return sorted((found & set(names)) - {node.name})


# ---------------------------------------------------------------- record checks

def _text(v):
    return isinstance(v, str) and bool(v.strip())


def check_record(eq_id, fn, record, node, docstring=None):
    """Findings (strings; empty = pass) for one record against its function node."""
    out = []
    for k in sorted(set(record) - FIELDS):
        out.append(f"unknown field '{k}'")
    for k in ("title", "kind", "latex", "symbols", "cite"):
        if k not in record:
            out.append(f"missing field '{k}'")
    kind = record.get("kind")
    if "kind" in record and kind not in KINDS:
        out.append(f"kind must be one of {', '.join(KINDS)}")
    if "title" in record and not _text(record["title"]):
        out.append("title is empty")
    latex = record.get("latex")
    if "latex" in record:
        if not (isinstance(latex, list) and latex and all(_text(x) for x in latex)):
            out.append("latex must be a non-empty list of non-empty strings")
        elif any("$" in x for x in latex):
            out.append("latex lines must not contain '$' (display math, no delimiters)")
    cite = record.get("cite")
    if "cite" in record:
        if not _text(cite):
            out.append("cite is empty")
        elif kind == "derived" and not cite.lower().startswith(DERIVED_CITE):
            out.append(f"derived cite must start with '{DERIVED_CITE}'")
        elif kind == "datasheet" and cite.lower().startswith(DERIVED_CITE):
            out.append("datasheet cite names a datasheet page and equation, not 'not a datasheet equation'")
    if kind == "datasheet" and docstring and docstring.lstrip().startswith("Not a DS equation"):
        out.append("kind is datasheet but the docstring says 'Not a DS equation' (use kind = derived)")
    out += _check_symbols(record.get("symbols"), node)
    consts = record.get("constants")
    if consts is not None:
        if not isinstance(consts, dict):
            out.append("constants must be a table of name = { value, unit, basis }")
        else:
            for name, c in sorted(consts.items()):
                if not isinstance(c, dict) or set(c) != set(CONSTANT_FIELDS) or not _text(c.get("basis")) \
                        or not _text(c.get("unit")) or isinstance(c.get("value"), bool) \
                        or not isinstance(c.get("value"), (int, float)):
                    out.append(f"constants.{name} needs value (number), unit and basis")
    for k in ("extends", "note"):
        if k in record and not _text(record[k]):
            out.append(f"{k} is empty")
    verified = record.get("verified")
    if verified is None:
        if not _text(record.get("reuse_search")):
            out.append("new record needs reuse_search (the terms searched with tools/equations.py find, "
                       "and the ids considered or 'none found')")
    elif not isinstance(verified, str):
        out.append("verified must be a string")
    elif verified.startswith("human:"):
        m = STAMP_RE.match(verified)
        if not m:
            out.append("malformed human stamp (human:<login> <YYYY-MM-DD> equation-review <id> hash <hash12>)")
        elif m.group(3) != eq_id:
            out.append(f"stamp names '{m.group(3)}', not this equation '{eq_id}'")
    return out


def _check_symbols(symbols, node):
    if symbols is None:
        return []
    if not isinstance(symbols, dict) or not symbols:
        return ["symbols must be a table of name = { tex, meaning, unit }"]
    out = []
    params = params_of(node)
    for p in params:
        if p.startswith("*"):
            out.append(f"parameter {p} cannot be described by symbols (use named parameters)")
    names = {p for p in params if not p.startswith("*")}
    plain = {k for k in symbols if not (k == "result" or k.startswith("result."))}
    results = [k for k in symbols if k == "result" or k.startswith("result.")]
    if plain != names:
        if names - plain:
            out.append("symbols lack parameter(s): " + ", ".join(sorted(names - plain)))
        if plain - names:
            out.append("symbols name no parameter: " + ", ".join(sorted(plain - names)))
    if not results:
        out.append("symbols lack 'result' (or result.<name> per tuple element)")
    elif "result" in results and len(results) > 1:
        out.append("use either 'result' or result.<name> entries, not both")
    slip = symbols.get("result")
    slipped = isinstance(slip, dict) and any(isinstance(v, dict) for v in slip.values())
    if slipped:
        first = next(k for k, v in sorted(slip.items()) if isinstance(v, dict))
        out.append(f'symbols.result is a nested table (an unquoted result.{first}): quote the key: "result.{first}"')
    for k, s in sorted(symbols.items()):
        if k == "result" and slipped:
            continue
        if not isinstance(s, dict) or set(s) != set(SYMBOL_FIELDS) or not all(_text(s[f]) for f in SYMBOL_FIELDS):
            out.append(f"symbols.{k} needs tex, meaning and unit (all non-empty)")
    return out


# ---------------------------------------------------------------- loading and state

def read_records(toml_path):
    """{fn: record} from an equations file; {} when absent. Only an `equation` table is allowed."""
    toml_path = Path(toml_path)
    if not toml_path.exists():
        return {}
    try:
        data = tomllib.loads(toml_path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as e:
        raise EquationsError(f"{toml_path.name}: not valid TOML: {e}")
    if set(data) - {"equation"} or not isinstance(data.get("equation", {}), dict):
        raise EquationsError(f"{toml_path.name}: only [equation.<fn>] tables are allowed")
    return data.get("equation", {})


def _state(eq):
    if RUNNING_PYTHON != PINNED_PYTHON:
        return "UNKNOWN"
    if eq.errors:
        return "FIX_FIRST"
    v = eq.record.get("verified")
    if v is None:
        return "NEW"
    m = STAMP_RE.match(v)
    if not m:
        return "MACHINE_ONLY"
    return "HUMAN_VERIFIED" if m.group(4) == eq.hash[:12] else "STALE"


def load(toml_path, py_path, prefix, import_module=False):
    """Equations of one records file: [Equation] sorted by function name, with errors, hash and state computed.

    prefix: id prefix (`<Value>` gives `<Value>.<fn>`). import_module: also import py_path (for EXAMPLES); the
    default reads the source only, so a check never executes code."""
    toml_path, py_path = Path(toml_path), Path(py_path)
    records = read_records(toml_path)
    if not records:
        return []
    if not py_path.exists():
        raise EquationsError(f"{toml_path.name}: {py_path.name} not found next to it")
    text = py_path.read_text(encoding="utf-8")
    try:
        funcs = _functions(text)
    except SyntaxError as e:
        raise EquationsError(f"{py_path.name}: {e}")
    module = None
    if import_module:
        from .component import load_calc
        module = load_calc(py_path)
    out = []
    for fn in sorted(records):
        rec = records[fn]
        eq = Equation(id=f"{prefix}.{fn}", fn=fn, record=rec if isinstance(rec, dict) else {}, toml=toml_path,
                      py=py_path, module=module)
        if not isinstance(rec, dict):
            eq.errors.append("record must be a table")
        elif fn not in funcs:
            eq.errors.append(f"function '{fn}' not found in {py_path.name}")
        elif fn.startswith("_"):
            eq.errors.append("a private function (leading underscore) has no record")
        else:
            node, eq.start, raw = funcs[fn]
            eq.src = textwrap.dedent(raw)
            eq.hash = record_hash(rec, raw)
            eq.calls = callees(node, funcs)
            eq.warnings = numeric_warnings(node)
            eq.errors += check_record(eq.id, fn, rec, node, ast.get_docstring(node, clean=False))
        eq.state = _state(eq)
        out.append(eq)
    return out


def load_folder(folder, import_module=False):
    """Equations of a component directory (`equations.toml` and `calc.py`; id prefix = directory name)."""
    folder = Path(folder)
    return load(folder / "equations.toml", folder / "calc.py", folder.name, import_module)


def library_files(root):
    """Sorted component directories that hold an equations.toml, under <root>/components/<Mfr>/<Value>/."""
    return sorted(p.parent for p in Path(root).glob("components/*/*/equations.toml"))


def library_equations(root, import_module=False):
    out = []
    for d in library_files(root):
        out += load_folder(d, import_module)
    return out


def missing_records(py_path, toml_path):
    """Public top-level functions of py_path with no record (for a module where every function needs one)."""
    funcs = _functions(Path(py_path).read_text(encoding="utf-8"))
    have = read_records(toml_path)
    return sorted(f for f in funcs if not f.startswith("_") and f not in have)


def check_folder(folder):
    """[(level, message)] for lib.check: every finding of a component's records is an ERROR."""
    folder = Path(folder)
    if not (folder / "equations.toml").exists():
        return []
    try:
        eqs = load_folder(folder)
    except EquationsError as e:
        return [("ERROR", f"equations: {e}")]
    return [("ERROR", f"equations: {e.id}: {msg}") for e in eqs for msg in e.errors]


def count_line(eqs):
    """`equations: k of n checked (m FIX_FIRST)`: k = HUMAN_VERIFIED."""
    k = sum(e.state == "HUMAN_VERIFIED" for e in eqs)
    m = sum(e.state == "FIX_FIRST" for e in eqs)
    return f"equations: {k} of {len(eqs)} checked ({m} FIX_FIRST)"


# ---------------------------------------------------------------- stamp

def stamp_line(eq, who, date):
    """The `verified` value for an equation (date: datetime.date or 'YYYY-MM-DD')."""
    return f"human:{who} {date} equation-review {eq.id} hash {eq.hash[:12]}"


def stamp_refusal(eq, who, env=None):
    """Why a stamp must not be written (string) or None. env defaults to os.environ."""
    env = os.environ if env is None else env
    if env.get("CLAUDECODE"):
        return AGENT
    if not re.fullmatch(LOGIN, who or ""):
        return f"'{who}' is not one GitHub login (letters, digits, single hyphens)"
    if RUNNING_PYTHON != PINNED_PYTHON:
        return version_warning().replace("WARN equations: ", "refused: ")
    if eq.state not in ("NEW", "STALE", "MACHINE_ONLY"):
        return f"{eq.id} is {eq.state}; only NEW, STALE or MACHINE_ONLY is stamped" + (
            "" if eq.state != "FIX_FIRST" else ": " + "; ".join(eq.errors))
    return None


_HEADER = re.compile(r"^\[[A-Za-z0-9_.\"-]+\]\s*(#.*)?$")


def write_stamp(toml_path, fn, line):
    """Put `verified = "<line>"` in [equation.<fn>] (replacing an existing one), keeping every other byte."""
    toml_path = Path(toml_path)
    lines = toml_path.read_text(encoding="utf-8").split("\n")
    head = next((i for i, x in enumerate(lines) if re.fullmatch(rf"\[equation\.{re.escape(fn)}\]\s*(#.*)?", x)), None)
    if head is None:
        raise EquationsError(f"{toml_path.name}: no [equation.{fn}] table")
    end = next((i for i in range(head + 1, len(lines)) if _HEADER.match(lines[i])), len(lines))
    new = f'verified = "{line}"'
    at = next((i for i in range(head + 1, end) if re.match(r"verified\s*=", lines[i])), None)
    if at is not None:
        lines[at] = new
    else:
        at = end
        while at > head + 1 and not lines[at - 1].strip():
            at -= 1
        lines.insert(at, new)
    text = "\n".join(lines)
    if tomllib.loads(text)["equation"][fn].get("verified") != line:  # fail closed before writing
        raise EquationsError(f"{toml_path.name}: could not place the stamp for {fn}")
    toml_path.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------- find and index

def _haystack(eq):
    """[(text, weight)] searched by find: ids and titles weigh most, then symbols and meanings, then LaTeX and units."""
    r = eq.record
    sym = r.get("symbols", {}) if isinstance(r.get("symbols"), dict) else {}
    parts = [(eq.id, 3), (str(r.get("title", "")), 3)]
    for name, s in sorted(sym.items()):
        s = s if isinstance(s, dict) else {}
        parts += [(name, 2), (str(s.get("tex", "")), 2), (str(s.get("meaning", "")), 2), (str(s.get("unit", "")), 1)]
    parts += [(x, 1) for x in r.get("latex", []) if isinstance(x, str)]
    return [(t.lower(), w) for t, w in parts]


def find(terms, eqs, limit=FIND_LIMIT):
    """[(matched terms, Equation)] best first, at most `limit`. Rank: terms matched (substring, case-insensitive),
    then field weight, then id. Equations matching no term are not returned."""
    terms = [t.lower() for t in terms if t.strip()]
    scored = []
    for eq in eqs:
        hay = _haystack(eq)
        hit = [t for t in terms if any(t in text for text, _ in hay)]
        if hit:
            weight = sum(w for t in hit for text, w in hay if t in text)
            scored.append((-len(hit), -weight, eq.id, len(hit), eq))
    scored.sort(key=lambda s: s[:3])
    return [(s[3], s[4]) for s in scored[:limit]]


def find_lines(terms, eqs, limit=FIND_LIMIT):
    """Printable rows for find()."""
    n = len([t for t in terms if t.strip()])
    return [f"{hit}/{n}  {eq.id}  [{eq.record.get('kind', '?')}]  {eq.record.get('title', '')}  ({eq.state})"
            for hit, eq in find(terms, eqs, limit)] or ["no equation matches"]


def _result_unit(eq):
    sym = eq.record.get("symbols", {}) if isinstance(eq.record.get("symbols"), dict) else {}
    units = [s.get("unit", "") for k, s in sorted(sym.items()) if (k == "result" or k.startswith("result.")) and isinstance(s, dict)]
    return ", ".join(units)


def index_rows(eqs, used_by=None):
    """[dict] sorted by id: id, title, kind, unit (result), symbols, state, used_by (from the used_by {id: text} map)."""
    used_by = used_by or {}
    rows = []
    for eq in sorted(eqs, key=lambda e: e.id):
        sym = eq.record.get("symbols", {}) if isinstance(eq.record.get("symbols"), dict) else {}
        rows.append({"id": eq.id, "title": eq.record.get("title", ""), "kind": eq.record.get("kind", ""),
                     "unit": _result_unit(eq), "symbols": ", ".join(k for k in sorted(sym) if not k.startswith("result")),
                     "state": eq.state, "used_by": used_by.get(eq.id, ""), "part": eq.id.rsplit(".", 1)[0]})
    return rows


def _cell(x):
    return str(x).replace("|", "\\|").replace("\n", " ")


def index_markdown(rows):
    head = ["id", "title", "kind", "result unit", "symbols", "state", "used by"]
    keys = ["id", "title", "kind", "unit", "symbols", "state", "used_by"]
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(_cell(r[k]) for k in keys) + " |" for r in rows]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- page

def examples(eq):
    """[(inputs text, library result, expected, tolerance, cite)] from the module's EXAMPLES rows for this function."""
    rows = []
    for row in getattr(eq.module, "EXAMPLES", []) or []:
        if row[0] != eq.fn:
            continue
        try:
            got = f"{getattr(eq.module, eq.fn)(**row[1]):.9g}"
        except Exception as e:  # shown, never raised: a page must still render
            got = f"error: {type(e).__name__}: {e}"
        rows.append((", ".join(f"{k}={v:g}" if isinstance(v, (int, float)) else f"{k}={v}" for k, v in sorted(row[1].items())),
                     got, f"{row[2]:.9g}", f"{row[3]:g}", row[4]))
    return rows


def order_cards(rows):
    """rows (objects with .state, .record, .id) in page order: NEW, STALE, FIX_FIRST and UNKNOWN first, then MACHINE_ONLY,
    HUMAN_VERIFIED last; within a group `datasheet` before `derived`, then by id."""
    eqs = rows
    group = {"FIX_FIRST": 0, "STALE": 0, "NEW": 0, "UNKNOWN": 0, "MACHINE_ONLY": 1, "HUMAN_VERIFIED": 2}
    return sorted(eqs, key=lambda e: (group[e.state], e.record.get("kind") != "datasheet", e.id))


def _flagged(eq):
    note = str(eq.record.get("note", ""))
    return any(w in note.lower() for w in FLAG_WORDS)


def _symbol_rows(eq):
    sym = eq.record.get("symbols", {}) if isinstance(eq.record.get("symbols"), dict) else {}
    return [(k, s.get("tex", ""), s.get("meaning", ""), s.get("unit", "")) for k, s in sorted(sym.items()) if isinstance(s, dict)]


def _constants(eq):
    c = eq.record.get("constants")
    return sorted(c.items()) if isinstance(c, dict) else []


def status_line(rows):
    """The progress line: `<k> of <n> checked; <t> to review; <m> FIX_FIRST` (k = HUMAN_VERIFIED)."""
    eqs = rows
    k = sum(e.state == "HUMAN_VERIFIED" for e in eqs)
    todo = sum(e.state in ("NEW", "STALE", "MACHINE_ONLY") for e in eqs)
    return f"{k} of {len(eqs)} checked; {todo} to review; {sum(e.state == 'FIX_FIRST' for e in eqs)} FIX_FIRST"


LIMITS = ("A stamp is an accountability record, not proof. A tick covers the equation and its implementation, not "
          "datasheet row values, min and max boxes, the worst-case method, or assumptions.")
TICK_MEANS = ("this equation is right and cites what it says, the code implements it as written (units, signs, terms), "
              "the symbols are the right quantities.")

CSS = """:root{--bg:#fff;--fg:#1b1f24;--mut:#59636e;--line:#d0d7de;--card:#f6f8fa;--bad:#cf222e;--warn:#9a6700;--ok:#1a7f37}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--fg:#e6edf3;--mut:#9198a1;--line:#30363d;--card:#161b22;--bad:#ff7b72;--warn:#d29922;--ok:#3fb950}}
body{background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,sans-serif;max-width:60rem;margin:0 auto;padding:1rem 16px}
article,details{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:.6rem 1rem;margin:1rem 0}
h1{font-size:1.4rem}h2{font-size:1.1rem;margin:.2rem 0}.mut{color:var(--mut)}.bad{color:var(--bad)}.warn{color:var(--warn)}
.st{font-size:.8rem;border:1px solid var(--line);border-radius:4px;padding:0 .4rem;margin-left:.4rem}
table{border-collapse:collapse;width:100%;margin:.4rem 0;display:block;overflow-x:auto}td,th{border:1px solid var(--line);padding:.2rem .5rem;text-align:left;vertical-align:top}
code,pre{font:13px/1.4 ui-monospace,monospace}pre{overflow-x:auto;background:var(--bg);padding:.5rem;border:1px solid var(--line)}
.tex{white-space:pre-wrap;margin:.3rem 0}textarea{width:100%;font:13px ui-monospace,monospace}
"""

JS = """(function(){
function ls(f){try{return f()}catch(e){return null}}
var boxes=[].slice.call(document.querySelectorAll('input.tick')),out=document.getElementById('stamp-cmd'),n=document.getElementById('ticked');
function update(){var refs=boxes.filter(function(b){return b.checked}).map(function(b){return b.getAttribute('data-ref')});
out.value=refs.length?'python3 tools/equations.py stamp '+refs.join(' '):'';n.textContent=refs.length+' ticked'}
boxes.forEach(function(b){var k='eqtick:'+b.getAttribute('data-key');
b.checked=ls(function(){return localStorage.getItem(k)==='1'})===true;
b.addEventListener('change',function(){ls(function(){b.checked?localStorage.setItem(k,'1'):localStorage.removeItem(k)});update()})});
update();
})();"""


def _h(x):
    return html.escape(str(x), quote=True)


def _tex(src, display):
    """LaTeX source as readable monospace (no external script: the Markdown page carries the rendered math)."""
    return f'<pre class="tex">{_h(src)}</pre>' if display else f"<code>{_h(src)}</code>"


def card_html(row, state=None, tick=True, by_id=None):
    """HTML of one equation card. row: an Equation, or any object with the same attributes (id, fn, record, state, hash,
    errors, src, start, py, calls, warnings, module). state: shown instead of row.state when given. tick=False omits the
    tick box (a card that is reviewed elsewhere, e.g. a library equation on a blocks page). by_id: {id: Equation} used to
    show the `extends` base and the states of `calls` (default: none known)."""
    eq = row
    if state is not None and state != row.state:
        eq = copy.copy(row)
        eq.state = state
    return _card(eq, by_id or {}, tick)


def _card(eq, by_id, tick):
    r = eq.record
    bad = eq.state == "FIX_FIRST"
    parts = [f'<h2>{_h(r.get("title", eq.fn))}<span class="st">{_h(eq.state)}</span>'
             f'<span class="st">{_h(r.get("kind", "?"))}</span></h2>', f'<div class="mut"><code>{_h(eq.id)}</code> '
             f'hash <code>{_h(eq.hash[:12])}</code></div>']
    if bad:
        parts.append('<ul class="bad">' + "".join(f"<li>{_h(m)}</li>" for m in eq.errors) + "</ul>")
    parts += [_tex(x, True) for x in r.get("latex", []) if isinstance(x, str)]
    rows = _symbol_rows(eq)
    if rows:
        parts.append("<table><tr><th>symbol</th><th>name</th><th>meaning</th><th>unit</th></tr>" + "".join(
            f"<tr><td>{_tex(t, False)}</td><td><code>{_h(k)}</code></td><td>{_h(m)}</td><td>{_h(u)}</td></tr>"
            for k, t, m, u in rows) + "</table>")
    parts.append(f"<p><b>Cite:</b> {_h(r.get('cite', ''))}</p>")
    if r.get("extends"):
        base = by_id.get(r["extends"])
        parts.append(f"<p><b>Extends:</b> <code>{_h(r['extends'])}</code>" + (
            f" ({_h(base.record.get('title', ''))}, {_h(base.state)})" if base else " (not on this page)") + "</p>")
        if base:
            parts += [_tex(x, True) for x in base.record.get("latex", []) if isinstance(x, str)]
    if r.get("note"):
        parts.append(f'<p class="{"warn" if _flagged(eq) else ""}">{"&#9888; " if _flagged(eq) else ""}'
                     f"<b>Note:</b> {_h(r['note'])}</p>")
    cs = _constants(eq)
    if cs:
        parts.append("<table><tr><th>constant</th><th>value</th><th>unit</th><th>basis</th></tr>" + "".join(
            f"<tr><td><code>{_h(k)}</code></td><td>{_h(c.get('value'))}</td><td>{_h(c.get('unit'))}</td>"
            f"<td>{_h(c.get('basis'))}</td></tr>" for k, c in cs) + "</table>")
    if eq.warnings:
        parts.append(f'<p class="warn">&#9888; numeric literals in the code: {_h(", ".join(eq.warnings))}</p>')
    if eq.src:
        end = eq.start + len(eq.src.splitlines()) - 1
        numbered = "\n".join(f"{eq.start + i:>4}  {ln}" for i, ln in enumerate(eq.src.splitlines()))
        parts.append(f"<details><summary>Source <code>{_h(eq.py.name)}:{eq.start}-{end}</code></summary>"
                     f"<pre>{_h(numbered)}</pre></details>")
    ex = examples(eq) if r.get("kind") == "datasheet" else []
    if ex:
        parts.append("<p><b>Datasheet examples (EXAMPLES)</b></p><table><tr><th>inputs</th><th>library result</th>"
                     "<th>expected</th><th>tolerance</th><th>cite</th></tr>" + "".join(
                         "<tr>" + "".join(f"<td>{_h(c)}</td>" for c in row) + "</tr>" for row in ex) + "</table>")
    if eq.calls:
        parts.append("<p><b>Calls:</b> " + ", ".join(
            f"<code>{_h(c)}</code> ({_h(next((e.state for e in by_id.values() if e.fn == c and e.py == eq.py), 'no record'))})"
            for c in eq.calls) + "</p>")
    if tick and eq.state in ("NEW", "STALE", "MACHINE_ONLY"):
        parts.append(f'<label><input type="checkbox" class="tick" data-ref="{_h(eq.ref)}" '
                     f'data-key="{_h(eq.id)}|{_h(eq.hash[:12])}"> tick: {_h(TICK_MEANS)}</label>')
    return "\n".join(parts)


def page_html(eqs, title="Equations review"):
    """One self-contained HTML page (no external script; LaTeX shown as monospace source)."""
    ordered = order_cards(eqs)
    by_id = {e.id: e for e in eqs}
    body = []
    for eq in ordered:
        card = card_html(eq, by_id=by_id)
        if eq.state == "HUMAN_VERIFIED":
            body.append(f"<details><summary>{_h(eq.record.get('title', eq.fn))} <code>{_h(eq.id)}</code> "
                        f"HUMAN_VERIFIED</summary>{card}</details>")
        else:
            body.append(f"<article>{card}</article>")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{_h(title)}</title>
<style>{CSS}</style></head><body>
<h1>{_h(title)}</h1>
<p><b>{_h(status_line(eqs))}</b></p>
{('<p class="warn">' + _h(version_warning()) + '</p>') if version_warning() else ''}
<p class="mut">Out of scope: datasheet row values and boxes, the worst-case method, design assumptions. {_h(LIMITS)}</p>
<p><b>Stamp command</b> <span id="ticked" class="mut"></span><br><textarea id="stamp-cmd" rows="3" readonly></textarea></p>
{chr(10).join(body)}
<script>{JS}</script>
</body></html>
"""


def page_markdown(eqs, title="Equations review"):
    """The same content as Markdown (GitHub `$$ ... $$` math, no tick boxes)."""
    by_id = {e.id: e for e in eqs}
    out = [f"# {title}", "", f"**{status_line(eqs)}**", "", *([version_warning(), ""] if version_warning() else []), "Out of scope: datasheet row values and boxes, the "
           "worst-case method, design assumptions. " + LIMITS, ""]
    todo = [e.ref for e in order_cards(eqs) if e.state in ("NEW", "STALE")]
    if todo:
        out += ["Stamp command (after review):", "", "```", "python3 tools/equations.py stamp " + " ".join(todo), "```", ""]
    for eq in order_cards(eqs):
        r = eq.record
        out += [f"## {r.get('title', eq.fn)}", "", f"`{eq.id}` · {r.get('kind', '?')} · **{eq.state}** · hash `{eq.hash[:12]}`", ""]
        if eq.state == "FIX_FIRST":
            out += [f"- FIX FIRST: {m}" for m in eq.errors] + [""]
        for x in r.get("latex", []):
            out += ["$$", str(x), "$$", ""]
        rows = _symbol_rows(eq)
        if rows:
            out += ["| symbol | name | meaning | unit |", "|---|---|---|---|"]
            out += [f"| ${_cell(t)}$ | `{k}` | {_cell(m)} | {_cell(u)} |" for k, t, m, u in rows] + [""]
        out += [f"Cite: {r.get('cite', '')}", ""]
        if r.get("extends"):
            base = by_id.get(r["extends"])
            out += [f"Extends: `{r['extends']}`" + (f" ({base.record.get('title', '')}, {base.state})" if base else ""), ""]
            if base:
                for x in base.record.get("latex", []):
                    out += ["$$", str(x), "$$", ""]
        if r.get("note"):
            out += [("**WARNING** " if _flagged(eq) else "") + f"Note: {r['note']}", ""]
        cs = _constants(eq)
        if cs:
            out += ["| constant | value | unit | basis |", "|---|---|---|---|"]
            out += [f"| `{k}` | {c.get('value')} | {_cell(c.get('unit'))} | {_cell(c.get('basis'))} |" for k, c in cs] + [""]
        if eq.warnings:
            out += ["Numeric literals in the code: " + ", ".join(eq.warnings), ""]
        if eq.src:
            end = eq.start + len(eq.src.splitlines()) - 1
            out += [f"Source `{eq.py.name}:{eq.start}-{end}`", "", "```python", eq.src, "```", ""]
        ex = examples(eq) if r.get("kind") == "datasheet" else []
        if ex:
            out += ["Datasheet examples:", "", "| inputs | library result | expected | tolerance | cite |", "|---|---|---|---|---|"]
            out += ["| " + " | ".join(_cell(c) for c in row) + " |" for row in ex] + [""]
        if eq.calls:
            out += ["Calls: " + ", ".join(f"`{c}`" for c in eq.calls), ""]
    return "\n".join(out).rstrip("\n") + "\n"


def write_page(eqs, out_dir, name, title="Equations review"):
    """Write <out_dir>/<name>.html and <name>.md (the only files a page run writes). Returns the two paths."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    h, m = out_dir / f"{name}.html", out_dir / f"{name}.md"
    h.write_text(page_html(eqs, title), encoding="utf-8")
    m.write_text(page_markdown(eqs, title), encoding="utf-8")
    return h, m
