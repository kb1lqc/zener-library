# Equations: one source, reused, reviewed

Status: DRAFT 2026-11-28, library side. Implemented by `lib/equations.py` (pure functions, stdlib + matplotlib, imported
as `from lib import equations` by any repo) and `tools/equations.py`. The blocks repo (`docs/spec/equations.md` there)
adds topic and block equations, use-site cases and its own checks; the shared sections below are the same text in both.

An equation exists **once**, as a pure function with a record, in the lowest place that owns all its inputs. Every
analysis calls it; none retypes it. A person reviews each equation once, and the stamp follows it to every use. Agents
never stamp.

Out of scope: equation input review (rows and boxes: `docs/spec/review.md`), how worst case is formed (`wca`), design
assumptions. The page states this.

## Homes
Library (this repo; equations are not rows of the datasheet ledger: records live in `equations.toml`, stamps are written by `tools/equations.py stamp`, never by `tools/stamp.py`): a datasheet equation or a single-part derived relation (Ohm's law, rated power,
`resistance_worst`): function in `components/<Mfr>/<Value>/calc.py`, record in `components/<Mfr>/<Value>/equations.toml`,
stamp in that record. Equations spanning several parts live in the blocks repo (topic) or one block. Id: `<Value>.<fn>`
(`WSK2512.sense_voltage`). Renaming the function or the part directory changes the id and stales the stamp.

## Function contract
Pure function: plain floats in SI units (`docs/spec/extract.md`, "calc.py"), temperatures in degC, no globals, no I/O,
no module constants except `math`. Datasheet values, design values and assumptions arrive as arguments. Names starting
`_` are private helpers and need no record. Returns a float or a tuple. Iterative equations keep the loop inside, with
named constants listed in the record's `constants`. Non-trivial numeric literals (anything but integers 0 to 10 and 0.5)
are listed on the page as warnings, not failures. The docstring stays prose for humans and does not restate the record.

## Record `[equation.<fn>]` (file `equations.toml`, next to `calc.py`)
The file holds only `[equation.<fn>]` tables (and their subtables). It is separate from `component.toml` so that adding
or editing a record never changes the datasheet review ledger's `component_sha256`.
- `title`; `kind` = `datasheet` | `derived` (not a datasheet equation: physical relation, composition, estimate). A
  `datasheet` record whose function docstring starts `Not a DS equation` is a check failure.
- `latex`: list, display math, no `$`, one line per derivation step, units on constants (`\,\mathrm{unit}`), written from
  what the function body computes.
- `symbols`: `name = { tex, meaning, unit }` (all non-empty; `unit` may be `"1"` for a ratio). Keys must equal the
  function's parameter names plus `result` (or the quoted key `"result.<name>"` per tuple element: an unquoted `result.p` is read by TOML as a nested table under
  `result`, which is `FIX_FIRST` with the message `quote the key: "result.p"`). Machine-checked.
- `cite`: `datasheet`: page and equation, table or figure; `derived`: the prefix `not a datasheet equation`, optionally
  followed by `; <context>` (the datasheet inputs it uses), nothing else first. `extends = "<id>"` when a derived equation modifies another (the page shows both).
- `constants`: optional `name = { value, unit, basis }` for fixed named constants inside the function.
- `reuse_search`: required on a record with no `verified` (a new record): the terms searched (`tools/equations.py find`)
  and the ids considered (`"none found"` allowed with the terms). `note`: display only (the page marks it when it says
  "estimate", "assumed" or "read as"). `verified`: written only by `stamp`.
Unknown keys in a record are an error.

## Hash, stamp, state
Hash: SHA-256 of `json.dumps(record without verified, sort_keys=True, separators=(",", ":"))`, `\n`, `ast.dump` of
the dedented function **without its docstring** (comments, formatting and docstring do not stale it).
**Pinned Python:** `ast.dump` differs between minor versions, so hashes and stamps are valid on one version only, the constant
`lib.equations.PINNED_PYTHON` (3.12, as CI). On any other minor version `check` and `page` print one `WARN` line and every
state is `UNKNOWN` (never `STALE` or `HUMAN_VERIFIED`); `stamp` refuses; `lib.check` findings (version independent) still
report and verify does not fail on the version. Callees
are not hashed; the page lists `calls` with their states. Stamp:
`verified = "human:<github-login> <YYYY-MM-DD> equation-review <id> hash <hash[:12]>"`, written by
`python3 tools/equations.py stamp <Value>:<fn> [...]`, run by the person, refused when `CLAUDECODE` is set, on a
Python other than the pinned one, when the state is `FIX_FIRST`, `UNKNOWN` or an already current `HUMAN_VERIFIED` (stamped
states: `NEW`, `STALE`, `MACHINE_ONLY`), and when the login is not one word. CI: `tools/check_stamps.py` also scans
`components/**/equations.toml`; a new or changed `human:` stamp must name the PR author. The stamp is not part of
`review/review.toml` (the datasheet-row ledger); state is computed, never committed.

| State | Meaning |
|---|---|
| `HUMAN_VERIFIED` | `human:` stamp, id matches, hash12 equals the current hash |
| `STALE` | `human:` stamp, hash12 differs |
| `NEW` | no stamp, no failed check |
| `MACHINE_ONLY` | a `verified` that does not start `human:` (never a human check; may get a human stamp) |
| `FIX_FIRST` | a machine check failed (signature, symbols, fields, malformed stamp, id mismatch, missing reuse_search) |
| `UNKNOWN` | not on the pinned Python: no state can be computed |

## Machine checks (`lib.check`, `python3 tools/equations.py check`; errors fail verify)
Records parse; fields and kinds valid; function exists; symbols = parameters + result; `latex` lines non-empty and
without `$`; `cite` rule per kind; new record has `reuse_search`; stamp syntax and id. Count line:
`equations: k of n checked (m FIX_FIRST)`. The verdict does not require human stamps.

## Reuse
`python3 tools/equations.py find <terms...>` searches ids, titles, symbols, meanings, LaTeX and units over every
`equations.toml`, ranks by the number of terms matched, prints at most 8 rows. An author runs it before writing any
equation and records the terms in `reuse_search`. `python3 -m lib.readme` (run by verify) writes `docs/EQUATIONS.md`
(generated, never hand-edited, same rule as `docs/PARTS.md`): id, title, kind, result unit, symbols, part (no state: stamping never changes it).
`python3 tools/equations.py index` prints the same table without the part link.

## Review page (`python3 tools/equations.py page <Value> ... --out-dir DIR`)
One self-contained HTML plus Markdown file per page, deterministic (sorted, no timestamps). Order: `FIX_FIRST`, `STALE`
and `NEW` first; `datasheet` before `derived`; `HUMAN_VERIFIED` folded; progress count first. Card: title, id, kind,
state; rendered equation (one line per step) and symbol table; cite and the `extends` base; `constants` with basis; source
with line numbers; for `datasheet`, the part's `EXAMPLES` rows for that function (inputs, library result, the datasheet's
expected value, cite); `calls` with states; numeric-literal warnings; tick box (`localStorage` in try/catch, keyed by id and hash
so an edit clears it) for `NEW`, `STALE` and `MACHINE_ONLY` only; one copyable `stamp` command for all ticked rows. `FIX_FIRST` shows the
failed check and no tick box. The page writes nothing but its two output files. A tick means: **this equation is right
and cites what it says, the code implements it as written (units, signs, terms), the symbols are the right
quantities.**

## Math rendering
LaTeX in the record is the source and is hashed. The Markdown page carries the rendered math as GitHub `$$ ... $$` blocks.
The HTML page loads no external script or stylesheet: each equation shows as readable monospace LaTeX beside the symbol
table (its one inline script only keeps the ticks and the stamp command).

## Public API (`from lib import equations`; stable, other repos call these)
- `load(toml, py, prefix, import_module=False)`, `load_folder(dir)`, `library_equations(root)`: `[Equation]` with `errors`,
  `hash`, `state`; `read_records`, `missing_records`, `check_record`, `check_folder`, `count_line`.
- `params_of(node)` and `check_record` (signature = symbols); `record_hash(record, src)`, `function_dump(src)`.
- `stamp_line`, `stamp_refusal`, `write_stamp`; `version_warning()`, `PINNED_PYTHON`.
- `find(terms, eqs)`, `find_lines`; `index_rows(eqs, used_by)`, `index_markdown(rows)`.
- `page_html(eqs, title)`, `page_markdown(eqs, title)`, `write_page(eqs, dir, name, title)`.
- `card_html(row, state=None, tick=True, by_id=None)`: one card; `tick=False` renders it without the tick box.
- `order_cards(rows)`: page order (NEW, STALE, FIX_FIRST, UNKNOWN first; datasheet before derived; checked last).
- `status_line(rows)`: the progress line.
Names starting `_` are private.

## Limits (stated on the page)
A stamp is an accountability record, not proof. A tick covers the equation and its implementation, not datasheet row
values, min and max boxes, the worst-case method, or assumptions. Inline arithmetic that bypasses a registered equation
is invisible to this check.
