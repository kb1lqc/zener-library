# Component library format (v0.1): index

The contract is split by role. Code, data and READMEs cite SPEC sections by the titles below; each title resolves to
the file that now holds it. Load only the file your role needs.

| SPEC section title | File |
|---|---|
| Rules that override convenience (cite, never invent, raw units, simple) | docs/spec/extract.md |
| Directory layout | docs/spec/extract.md |
| component.toml | docs/spec/extract.md |
| Fields | docs/spec/extract.md |
| Signs and ordering | docs/spec/extract.md |
| Units | docs/spec/extract.md |
| Pin types (KiCad) | docs/spec/extract.md |
| Defaults instead of questions; Check-row defaults ("Choosing check rows") | docs/spec/extract.md |
| calc.py | docs/spec/extract.md |
| Temperature and combined errors (the one recipe) | docs/spec/extract.md |
| Local datasheet review packet (SHADOW) | docs/spec/datasheet-review.md |
| Families and variants | docs/spec/family.md |
| Series of numbered rows | docs/spec/series.md |
| Series components (the value is a design input) | docs/spec/series.md |
| Capacitor series (the part is picked from a catalog) | docs/spec/capacitor.md |
| Zener wrapper (generated) | docs/spec/wrapper.md |
| Series wrapper | docs/spec/wrapper.md |
| Capacitor wrapper | docs/spec/wrapper.md |
| Tests (harness and CASES) | .claude/skills/zener-wrapper/SKILL.md, section 2 |
| Using a part (lib API); Worst-case method (`wca`) | docs/spec/lib-api.md |
| Validation; README "Limits of this data" | enforced in `lib/check.py`, `lib/readme.py` (not prose) |
| Goal; rationale; history | docs/notes/spec-rationale.md (humans only) |

KiCad file rules: docs/KICAD.md. Agent briefs: docs/briefs/. Role-to-file map: CLAUDE.md.
