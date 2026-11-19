# Local datasheet review

Build a local packet and archive it beside the component:

```sh
python3 tools/ds_review_packet.py <datasheet.pdf> <component.toml-or-directory> --out <new-or-empty-directory> --archive
```

Requires `pdfinfo`, `pdftotext`, and `pdftoppm`. The packet contains `review.html`, `manifest.json`,
`github-review.md`, `github-issue.md`, `coverage.md`, parameter evidence images, and full-page context images.
`--archive` saves `datasheet-review/<PDF-SHA-prefix>/` with the human review record, coverage checklist, manifest,
and referenced images. It does not copy the PDF or edit `component.toml`. Existing archives are never overwritten.
Omit `--archive` for a temporary packet only. GitHub Markdown files are drafts; the tool makes no network calls.

The saved record begins **PENDING**. A human enters a one-word reviewer handle and date, checks the attestation,
and selects a decision for every parameter after comparing its value with the cited PDF image. The coverage checklist
includes all sections and table/figure captions found by `ds_index`, a manual row for unindexed material, and a
whole-document sweep. For every inventory item, list the covered parameter keys or explain why it is not applicable.
Text-index inventory is a starting point, not guaranteed completeness.

For each **Confirmed** parameter, add both fields inside its `[param.<key>]` table:

```toml
verified = "abrown 2026-11-19 human page-image review"
verification_type = "human_page_image"
```

`verification_type` may instead be `cross_model_page_image` or `manufacturer_export`; text checks have no
verification type and are never treated as verification. Legacy stamps without a type remain usable but are
classified as untyped. `lib.check` validates the stamp/type format; it cannot establish that the review happened.
Remove or renew a human stamp if its parameter changes.

After completing both files, run:

```sh
python3 tools/ds_review_packet.py --finalize <component>/datasheet-review/<PDF-SHA-prefix>
```

Finalization refuses incomplete reviewer/date/attestation fields, unchecked parameter decisions, unresolved coverage
items, stale component values/cites, or Confirmed rows without the matching reviewer/date human stamp. On success it
sets the archive manifest and record to **HUMAN-REVIEWED**. It does not edit component data and is not a
cryptographic signature.

Printed-page citations use the `ds_index` page map; `DS PDF p.<n>` refers directly to PDF page `n`. Each parameter
gets a directly rendered evidence image: an isolated row crop when available, otherwise a table/section excerpt
from `ds_index`, otherwise a full-page fallback. Full-page context is also included. Missing or ambiguous citations
do not get an inferred page; they remain `UNSURE`. Scanned PDFs render page images but cannot produce text checks.

- `AGREE_TEXT_CHECK` maps `table_xcheck`'s `AGREE`; it only means a clean text-layer row matched the stored value
  and unit. It is not datasheet evidence or human verification.
- `DISAGREE` is a text-layer discrepancy to adjudicate against the rendered page.
- `UNSURE` is intentional abstention for missing/unmappable cites, ambiguous rows, unsupported conventions,
  scanned PDFs, or other cases the text checker cannot compare safely.

The manifest records the input PDF SHA-256, component values/cites, PDF and printed pages, crop coordinates or
full-page indicator, image paths, text-check status, and limitations. No complete datasheet coverage is claimed.
Each generated component README shows a badge counting explicitly typed human page-image reviews (gray for none,
yellow for partial, green when every parameter row is human-reviewed). The line below separates cross-model audits,
manufacturer-export stamps, and legacy/untyped stamps; text checks are excluded. Parameter tables show provenance
per row. Counts cover only component parameter rows and do not prove complete datasheet coverage or truthful review.
Exit code `1` means invalid input or local-tool failure, `2` means one or more text-check discrepancies, and `0`
means no discrepancy was detected by the text checker.
