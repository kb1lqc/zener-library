#!/usr/bin/env python3
"""Check that every human stamp a pull request adds names the PR author (docs/spec/review.md "Runs").

Usage (repo root, CI on pull requests):
  python3 tools/check_stamps.py --author LOGIN --base REF [--head REF] [--root R]
Structural, not a text diff: lists the changed components/**/component.toml, variants.toml and equations.toml files (`git diff --name-only
--no-renames BASE...HEAD`; a rename is a delete plus an add), reads each file at HEAD and at the merge base with
`git show`, parses both with tomllib and walks every string value. A value starting with "human:" that is new or
changed versus the merge base at the same TOML key path must read `human:<LOGIN> ...` (LOGIN by GitHub login rules,
then one space; compared case-insensitively). Anything else starting with "human:" is a malformed human stamp.
Removed stamps and machine stamps are ignored. A HEAD file that is not valid UTF-8 TOML fails (closed).
Prints `file:line: human stamp names <name>, but the PR author is <login>` (or `file [<key path>]: ...` when the line
is not found) per finding, else one OK line. Exit 0 = OK, 1 = a finding or a tool error (git failed, bad TOML).
"""

import argparse
import os
import re
import subprocess
import sys
import tomllib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.component import GITHUB_LOGIN  # noqa: E402  (the stamp's name part, as lib checks it)

PATHSPECS = (":(glob)components/**/component.toml", ":(glob)components/**/variants.toml",  # override stamps live in variants.toml
             ":(glob)components/**/equations.toml")  # equation stamps (docs/spec/equations.md)
NAME_RE = re.compile(rf"human:({GITHUB_LOGIN}) ")


class ToolError(Exception):
    pass


def git(root, *args):
    r = subprocess.run(["git", "-C", str(root), *args], capture_output=True)
    if r.returncode:
        raise ToolError(f"git {' '.join(args)} failed: {r.stderr.decode(errors='replace').strip()}")
    return r.stdout


def changed_files(root, base, head):
    out = git(root, "diff", "--name-only", "--no-renames", "--no-textconv", "--no-ext-diff", "-z", f"{base}...{head}",
              "--", *PATHSPECS)
    return [p for p in out.decode().split("\0") if p]


def blob(root, rev, path):
    """File text at rev, or None when the path does not exist there."""
    r = subprocess.run(["git", "-C", str(root), "cat-file", "-e", f"{rev}:{path}"], capture_output=True)
    if r.returncode:
        return None
    return git(root, "show", f"{rev}:{path}").decode("utf-8")


def human_values(doc, path=()):
    """{key path tuple: value} for every string anywhere in a parsed TOML doc that starts with "human:"."""
    out = {}
    if isinstance(doc, dict):
        for k, v in doc.items():
            out.update(human_values(v, path + (k,)))
    elif isinstance(doc, list):
        for i, v in enumerate(doc):
            out.update(human_values(v, path + (i,)))
    elif isinstance(doc, str) and doc.startswith("human:"):
        out[path] = doc
    return out


def where(path, text, keys, value):
    n = next((i for i, ln in enumerate(text.splitlines(), 1) if value in ln), None)
    return f"{path}:{n}" if n else f"{path} [{'.'.join(map(str, keys))}]"


def findings(head_text, base_text, path, author):
    """Messages for one file; ToolError when the HEAD text is not valid TOML (fail closed)."""
    try:
        head = tomllib.loads(head_text)
    except tomllib.TOMLDecodeError as e:
        raise ToolError(f"{path}: not valid TOML at HEAD ({e})")
    try:
        base = tomllib.loads(base_text) if base_text is not None else {}
    except tomllib.TOMLDecodeError:
        base = {}  # every human value counts as new
    old = human_values(base)
    out = []
    for keys, value in sorted(human_values(head).items(), key=lambda kv: [str(k) for k in kv[0]]):
        if old.get(keys) == value:
            continue
        m = NAME_RE.match(value)
        loc = where(path, head_text, keys, value)
        if not m:
            out.append(f"{loc}: malformed human stamp ({value[:40]!r}), the PR author is {author}")
        elif m.group(1).casefold() != author.casefold():
            out.append(f"{loc}: human stamp names {m.group(1)}, but the PR author is {author}")
    return out


def check(root, base, head, author):
    msgs, n = [], 0
    mb = git(root, "merge-base", base, head).decode().strip()
    for path in changed_files(root, base, head):
        text = blob(root, head, path)
        if text is None:
            continue  # deleted at HEAD
        n += 1
        msgs += findings(text, blob(root, mb, path), path, author)
    return msgs, n


def main(argv=None):
    ap = argparse.ArgumentParser(prog="tools/check_stamps.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--author", required=True, metavar="LOGIN", help="GitHub login every added human stamp must name")
    ap.add_argument("--base", required=True, metavar="REF", help="PR base ref or SHA")
    ap.add_argument("--head", default="HEAD", metavar="REF", help="head ref or SHA (default: HEAD)")
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    help="repo root (default: this repo)")
    a = ap.parse_args(argv)
    try:
        msgs, n = check(a.root, a.base, a.head, a.author)
    except (ToolError, UnicodeDecodeError) as e:
        print(f"check_stamps: FAIL: {e}")
        return 1
    if msgs:
        print("\n".join(msgs))
        return 1
    print(f"check_stamps: OK ({n} changed component.toml/variants.toml file(s); every new human stamp names {a.author})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
