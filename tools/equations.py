#!/usr/bin/env python3
"""Equation records of the library (docs/spec/equations.md). Thin wrapper over lib/equations.py.

Usage (repo root; `--root R` before the command, default this repo):
  python3 tools/equations.py check [<Value> ...]        findings of every equations.toml (or the named parts)
  python3 tools/equations.py find <terms...>            closest records (at most 8), run before writing an equation
  python3 tools/equations.py index [--out FILE]         id, title, kind, result unit, symbols, state (Markdown)
  python3 tools/equations.py page <Value> ... --out-dir DIR   review page DIR/equations.html + .md (writes only those)
  python3 tools/equations.py stamp [--who LOGIN] <Value>:<fn> [...]   a PERSON writes `verified` (never an agent)
Exit 0 = ok / written, 1 = findings or refused, 2 = bad usage. Output: one summary line or the first 5 failures.
stamp refuses when CLAUDECODE is set, when the Python minor version is not the pinned one (lib.equations.PINNED_PYTHON;
check and page then print one WARN line and show UNKNOWN), when a state is not NEW, STALE or MACHINE_ONLY (FIX_FIRST shows
its findings), when the login is not one word, and writes nothing unless every named equation passes (all or nothing).
"""

import argparse
import datetime
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from lib import equations as eqlib  # noqa: E402

SHOWN = 5


def find_dirs(root, values):
    """Component directories holding equations.toml: all, or those named by Value (directory name)."""
    dirs = eqlib.library_files(root)
    if not values:
        return dirs
    names = {d.name: d for d in dirs}
    missing = [v for v in values if v not in names]
    if missing:
        raise SystemExit("no equations.toml for: " + ", ".join(missing))
    return [names[v] for v in values]


def load_all(root, values=(), import_module=False):
    out = []
    for d in find_dirs(root, list(values)):
        out += eqlib.load_folder(d, import_module)
    return out


def warn_version():
    w = eqlib.version_warning()
    if w:
        print(w)


def cmd_check(args):
    warn_version()
    eqs = load_all(args.root, args.values)
    fails = [f"{e.id}: {m}" for e in eqs for m in e.errors]
    if fails:
        print(f"FAIL {eqlib.count_line(eqs)}")
        for f in fails[:SHOWN]:
            print("  " + f)
        if len(fails) > SHOWN:
            print(f"  ... {len(fails) - SHOWN} more")
        return 1
    print("PASS " + eqlib.count_line(eqs))
    return 0


def cmd_find(args):
    print("\n".join(eqlib.find_lines(args.terms, load_all(args.root))))
    return 0


def cmd_index(args):
    text = eqlib.index_markdown(eqlib.index_rows(load_all(args.root)))
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(text, end="")
    return 0


def cmd_page(args):
    warn_version()
    eqs = load_all(args.root, args.values, import_module=True)
    h, m = eqlib.write_page(eqs, args.out_dir, "equations", "Equations review: " + ", ".join(args.values or ["library"]))
    print(f"wrote {h} and {m.name} ({eqlib.status_line(eqs)})")
    return 0


def github_login():
    try:
        r = subprocess.run(["gh", "api", "user", "--jq", ".login"], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    return r.stdout.strip() if r.returncode == 0 and r.stdout.strip() else None


def cmd_stamp(args):
    if os.environ.get("CLAUDECODE"):
        print(eqlib.AGENT)
        return 1
    who = args.who or github_login()
    if not who:
        print("refused: no GitHub login: run `gh auth login`, or pass --who <github-login>")
        return 1
    day = datetime.date.today().isoformat()
    chosen, problems = [], []
    for ref in args.refs:
        value, _, fn = ref.partition(":")
        fn = fn[3:] if fn.startswith("eq.") else fn
        try:
            eqs = load_all(args.root, [value])
        except SystemExit as e:
            problems.append(str(e))
            continue
        eq = next((e for e in eqs if e.fn == fn), None)
        if eq is None:
            problems.append(f"{ref}: no such equation")
            continue
        why = eqlib.stamp_refusal(eq, who)
        problems += [f"{ref}: {why}"] if why else []
        chosen.append(eq)
    if problems:
        print("refused (nothing written):")
        for p in problems[:SHOWN]:
            print("  " + p)
        return 1
    for eq in chosen:
        eqlib.write_stamp(eq.toml, eq.fn, eqlib.stamp_line(eq, who, day))
    print(f"stamped {len(chosen)}: " + ", ".join(e.id for e in chosen))
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--root", type=Path, default=ROOT)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("check")
    s.add_argument("values", nargs="*")
    s = sub.add_parser("find")
    s.add_argument("terms", nargs="+")
    s = sub.add_parser("index")
    s.add_argument("--out")
    s = sub.add_parser("page")
    s.add_argument("values", nargs="*")
    s.add_argument("--out-dir", required=True)
    s = sub.add_parser("stamp")
    s.add_argument("--who")
    s.add_argument("refs", nargs="+")
    args = p.parse_args(argv)
    try:
        return {"check": cmd_check, "find": cmd_find, "index": cmd_index, "page": cmd_page, "stamp": cmd_stamp}[args.cmd](args)
    except eqlib.EquationsError as e:
        print(f"FAIL equations: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
