# Brief: local datasheet review packet

Run `python3 tools/ds_review_packet.py <datasheet.pdf> <component.toml-or-directory> --out <empty-directory> --archive`
to keep parameter evidence, section/table/figure coverage, and a pending review record beside the component.
Read `docs/spec/datasheet-review.md` for formats and statuses.

Interpret `AGREE_TEXT_CHECK` and `DISAGREE` as text-layer checks only. Verify each parameter against the rendered
PDF page image. `UNSURE` is intentional abstention. Never set `verified`, change component data, or describe the
packet as human-reviewed from this output alone. A human must fill reviewer/date, attestation, every parameter
decision, and every coverage disposition; add a typed `human_page_image` stamp only to Confirmed rows. Then run
`python3 tools/ds_review_packet.py --finalize <archive-directory>`. The gate refuses incomplete or stale records.
Rows get a row snippet, indexed table/section excerpt, or full-page fallback. For missing or ambiguous cites, do
not infer a page from neighboring parameters. The tool is local-only and creates draft Markdown without GitHub API
calls. Respect the vendor's redistribution terms for datasheets and screenshots.
