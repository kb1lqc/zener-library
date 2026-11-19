#!/usr/bin/env python3
"""Build a local-only, SHADOW datasheet review packet. Text checks are CHECK ONLY, never a source.

usage: tools/ds_review_packet.py <datasheet.pdf> <component.toml|component-dir> --out <directory> [--archive]
       tools/ds_review_packet.py --finalize <archive-directory>

The packet reads component parameter values and cites without modifying them. It renders evidence images directly
from the PDF. --archive saves a pending human-review record and those images beside the component, never the PDF.
"""
import argparse
import datetime
import hashlib
import html
import json
import math
import os
import re
import shutil
import sys
import tempfile
import tomllib
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_index as D  # noqa: E402
import table_xcheck as T  # noqa: E402


class PacketError(Exception):
    """An input or local PDF-tool failure that prevents a usable review packet."""


def load_component(path):
    path = Path(path).expanduser().resolve()
    toml_path = path / "component.toml" if path.is_dir() else path
    if not toml_path.is_file():
        raise PacketError("component.toml missing: %s" % toml_path)
    try:
        with toml_path.open("rb") as f:
            data = tomllib.load(f)
    except (OSError, tomllib.TOMLDecodeError) as e:
        raise PacketError("component.toml unreadable: %s" % e)
    params = data.get("param")
    if not isinstance(params, dict) or not params:
        raise PacketError("component.toml has no [param.*] rows")
    for key, row in params.items():
        if not isinstance(row, dict):
            raise PacketError("[param.%s] must be a table" % key)
        for field in ("min", "typ", "max"):
            value = row.get(field)
            if value is not None and (
                isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value)
            ):
                raise PacketError("[param.%s].%s must be a finite number" % (key, field))
        if "cite" in row and not isinstance(row["cite"], str):
            raise PacketError("[param.%s].cite must be a string" % key)
    return toml_path, params


def pdf_page_count(pdf):
    rc, info, err = D.run(["pdfinfo", str(pdf)])
    match = re.search(r"^Pages:\s+(\d+)", info, re.M)
    if rc or not match:
        raise PacketError("pdfinfo failed: %s" % (err.strip()[:160] or "page count unavailable"))
    return int(match.group(1))


def render_page(pdf, page, destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    base = destination.with_suffix("")
    rc, _out, err = D.run([
        "pdftoppm", "-r", "150", "-f", str(page), "-l", str(page), "-png", "-singlefile", str(pdf), str(base)
    ])
    if rc or not destination.is_file() or destination.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        raise PacketError("pdftoppm failed rendering PDF page %d: %s" % (page, err.strip()[:160]))
    return destination


def render_crop(pdf, page, bbox, destination, dpi=300):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    base = destination.with_suffix("")
    x0, y0, x1, y1 = bbox
    scale = dpi / 72.0
    px = [int(x0 * scale), int(y0 * scale), int((x1 - x0) * scale) + 1, int((y1 - y0) * scale) + 1]
    rc, _out, err = D.run([
        "pdftoppm", "-r", str(dpi), "-f", str(page), "-l", str(page),
        "-x", str(px[0]), "-y", str(px[1]), "-W", str(px[2]), "-H", str(px[3]),
        "-png", "-singlefile", str(pdf), str(base),
    ])
    if rc or not destination.is_file() or destination.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        raise PacketError("pdftoppm failed rendering the row snippet on PDF page %d: %s" % (
            page, err.strip()[:160]
        ))
    return destination


def cite_page(cite, printed_pages, page_count):
    if not cite:
        return None, None, "missing cite"
    match = re.match(r"^DS\s+(PDF\s+)?p\.(\d+)(?:\s|,|$)", cite, re.I)
    if not match:
        return None, None, "cite has no supported DS page"
    cited = int(match.group(2))
    if match.group(1):
        if 1 <= cited <= page_count:
            return cited, printed_pages.get(str(cited)), None
        return None, cited, "cited PDF page is out of range"
    candidates = [int(pdf_page) for pdf_page, printed in printed_pages.items() if printed == cited]
    if len(candidates) == 1:
        return candidates[0], cited, None
    if not candidates:
        return None, cited, "printed page could not be mapped uniquely"
    return None, cited, "printed page maps to multiple PDF pages"


def indexed_table_bboxes(index, page, cite):
    cite_text = (cite or "").lower()
    table_labels = re.findall(r"\btable\s+([\d.\-]+)", cite_text)
    hits = [
        (item, hit)
        for item in index.get("items", [])
        if item.get("kind") != "figure"
        for hit in item.get("hits", [])
        if hit.get("pdf_page") == page and hit.get("table_bbox")
    ]
    if not hits:
        return []
    exact = [
        hit["table_bbox"] for item, hit in hits
        if item.get("key", "").startswith("table:")
        and item["key"].split(":", 1)[1].lower() in table_labels
    ]
    if exact:
        return exact
    tables = [hit["table_bbox"] for item, hit in hits if item.get("kind") == "table"]
    if tables:
        return tables
    sections = [hit["table_bbox"] for item, hit in hits if item.get("kind") == "section"]
    return sections[:1]


def safe_stem(key, ordinal):
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", key).strip("._-") or "param"
    return "%04d-%s" % (ordinal, slug)


def component_values(row):
    out = {}
    for name in ("min", "typ", "max", "text", "unit", "conditions"):
        if name in row:
            out[name] = row[name]
    return out


def component_snapshot(row):
    fields = ("name", "symbol", "kind", "scope", "min", "typ", "max", "text", "unit", "conditions", "cite")
    return {name: row[name] for name in fields if name in row}


def display_values(values):
    parts = ["%s=%s" % (name, values[name]) for name in ("min", "typ", "max") if name in values]
    if "text" in values:
        parts.append("text=%s" % values["text"])
    for name in ("unit", "scope", "conditions"):
        if values.get(name) not in (None, ""):
            parts.append("%s=%s" % (name, values[name]))
    return "; ".join(parts) or "(no numeric value)"


def md_cell(value):
    return str(value).replace("|", r"\|").replace("\n", " ").replace("\r", " ")


def build_markdown(packet):
    lines = [
        "# %s: datasheet review" % md_cell(packet["component"]),
        "",
        "SHADOW; text checks only, not human verification. PDF SHA-256: `%s`." % packet["pdf_sha256"],
        "Do not redistribute the PDF or screenshots except as permitted by the vendor license.",
        "",
        "| Key | Library values | Cite / status | Datasheet snippet |",
        "|---|---|---|---|",
    ]
    for row in packet["parameters"]:
        cite_status = "%s<br>%s" % (row["status"], md_cell(row.get("cite", "")))
        if row["status"] != "AGREE_TEXT_CHECK":
            cite_status += "<br>%s" % md_cell(row["reason"])
        if row["pdf_pages"]:
            context = "context/page-%04d.png" % row["pdf_pages"][0]
            cite_status += "<br>[full page](%s)" % context
        label = {
            "row_crop": "row snippet",
            "table_crop": "table excerpt",
        }.get(row["crop_mode"], "full-page fallback")
        evidence = " ".join(
            "![%s](%s)" % (label, path.replace("\\", "/")) for path in row["image_paths"]
        ) or "No page mapped"
        lines.append("| %s | %s | %s | %s |" % (
            md_cell(row["key"]), md_cell(display_values(row["values"])), cite_status, evidence,
        ))
    return "\n".join(lines)


def build_issue_draft(packet):
    return "\n".join([
        "# Verify %s against the datasheet" % packet["component"],
        "",
        "- PDF SHA-256: `%s`" % packet["pdf_sha256"],
        "Human review has not been performed. Compare each library value and cite in `github-review.md` with its "
        "linked PDF evidence; text checks are CHECK ONLY, never a source.",
        "Do not redistribute the datasheet or screenshots except as permitted by the vendor license.",
    ])


def build_review_record(packet):
    lines = [
        "# %s: datasheet human-review record" % md_cell(packet["component"]),
        "",
        "**Review status: PENDING — no human review has been recorded.**",
        "",
        "- PDF SHA-256: `%s`" % packet["pdf_sha256"],
        "- Reviewer: [enter one-word handle]",
        "- Review date: [enter YYYY-MM-DD]",
        "- Attestation: [ ] I compared each listed library value with its cited PDF evidence.",
        "- Text-check results are aids only; `AGREE_TEXT_CHECK` does not mean verified.",
        "- Complete `coverage.md` too, then run `python3 tools/ds_review_packet.py --finalize <archive-dir>`.",
        "- Do not redistribute the PDF or screenshots except as permitted by the vendor license.",
        "",
        "| Key | Library values | Datasheet cite | PDF evidence | Human decision | Notes |",
        "|---|---|---|---|---|---|",
    ]
    for row in packet["parameters"]:
        label = {
            "row_crop": "snippet",
            "table_crop": "table excerpt",
        }.get(row["crop_mode"], "full-page fallback")
        images = " ".join(
            "![%s](%s)" % (label, path.replace("\\", "/")) for path in row["image_paths"]
        ) or "No page mapped"
        cite = "%s (PDF page%s %s)" % (
            md_cell(row.get("cite", "")),
            "" if len(row["pdf_pages"]) == 1 else "s",
            ", ".join(str(page) for page in row["pdf_pages"]) or "unmapped",
        )
        decision = "[ ] Confirmed<br>[ ] Needs correction<br>[ ] Unable to verify"
        lines.append("| %s | %s | %s | %s | %s | [add notes] |" % (
            md_cell(row["key"]), md_cell(display_values(row["values"])), cite, images, decision,
        ))
    lines.extend([
        "",
        "After visually checking the images, complete the reviewer, date, attestation, and every parameter decision. "
        "For each Confirmed row only, set `verified = \"<one-word-name> YYYY-MM-DD human page-image review\"` and "
        "`verification_type = \"human_page_image\"` inside its `[param.<key>]` table in `component.toml`. The "
        "finalize command checks these stamps and checklist fields before changing the status. This is a "
        "human-edited record, not a cryptographic signature; `lib.check` validates stamp format, not truth.",
    ])
    return "\n".join(lines) + "\n"


def build_coverage(packet):
    lines = [
        "# Datasheet coverage checklist",
        "",
        "PDF SHA-256: `%s`." % packet["pdf_sha256"],
        "Index status: `%s` — %s." % (
            packet["index_status"], md_cell(packet.get("index_reason", "") or "no index warning"),
        ),
        "- Whole-datasheet sweep: [ ] I checked every PDF page for relevant content omitted from this text index.",
        "- This checklist is a manual coverage attestation, not a claim that `ds_index` found every datasheet table.",
        "",
        "| Index item | Kind | Index result | PDF / printed pages | Coverage decision | Parameter keys or reason |",
        "|---|---|---|---|---|---|",
    ]
    for item in packet["coverage_items"]:
        disposition = "[ ] Extracted<br>[ ] Not applicable"
        detail = "keys: [enter keys] OR reason: [enter reason]"
        lines.append("| %s | %s | %s: %s | %s | %s | %s |" % (
            md_cell(item["key"]), md_cell(item["kind"]), md_cell(item["status"]),
            md_cell(item["reason"]), md_cell(item["pages"]), disposition, detail,
        ))
    return "\n".join(lines) + "\n"


def indexed_coverage_items(index):
    items = []
    for item in index.get("items", []):
        pages = []
        for hit in item.get("hits", []):
            page = "PDF p.%s" % hit.get("pdf_page", "?")
            printed = hit.get("printed_page")
            if printed is not None:
                page += " (printed p.%s)" % printed
            if page not in pages:
                pages.append(page)
        items.append({
            "key": item["key"],
            "kind": item["kind"],
            "status": item["status"],
            "reason": item["reason"],
            "pages": ", ".join(pages) or "not found by text index",
        })
    items.append({
        "key": "unindexed_or_other",
        "kind": "manual",
        "status": "manual",
        "reason": "Record relevant datasheet items not represented by the text index",
        "pages": "whole document",
    })
    return items


def markdown_cells(line):
    if not line.startswith("|") or not line.endswith("|"):
        return []
    cells, cell, escaped = [], [], False
    for char in line[1:-1]:
        if char == "|" and not escaped:
            cells.append("".join(cell).strip())
            cell = []
            continue
        cell.append(char)
        if char == "\\" and not escaped:
            escaped = True
        else:
            escaped = False
    cells.append("".join(cell).strip())
    return cells


def table_rows(text):
    return [cells for line in text.splitlines() if (cells := markdown_cells(line))]


def row_decisions(cell, labels):
    found = {}
    for label in labels:
        states = re.findall(r"\[([ xX])\]\s*" + re.escape(label), cell)
        if len(states) != 1:
            raise PacketError("decision cell must contain one checkbox for %s" % label)
        found[label] = states[0].lower() == "x"
    selected = [label for label, checked in found.items() if checked]
    if len(selected) != 1:
        raise PacketError("select exactly one decision: %s" % ", ".join(labels))
    return selected[0]


def coverage_decisions(archive_dir, manifest):
    path = Path(archive_dir) / "coverage.md"
    if not path.is_file():
        raise PacketError("coverage.md missing; regenerate the review archive")
    text = path.read_text(encoding="utf-8")
    if not re.search(r"^- Whole-datasheet sweep: \[x\]", text, re.I | re.M):
        raise PacketError("coverage checklist needs the whole-datasheet sweep attestation")
    rows = {}
    for cells in table_rows(text):
        if len(cells) != 6:
            continue
        if cells[0] in rows:
            raise PacketError("duplicate coverage item: %s" % cells[0])
        rows[cells[0]] = cells
    param_keys = {row["key"] for row in manifest.get("parameters", [])}
    decisions, covered = {}, set()
    for item in manifest.get("coverage_items", []):
        cells = rows.get(item["key"])
        if not cells:
            raise PacketError("coverage item missing: %s" % item["key"])
        decision = row_decisions(cells[4], ("Extracted", "Not applicable"))
        detail = cells[5]
        if decision == "Extracted":
            match = re.match(r"keys:\s*(.+)$", detail, re.I)
            raw_keys = match.group(1) if match else ""
            keys = [key.strip().strip("`") for key in raw_keys.split(",") if key.strip()]
            if not keys or any(key.startswith("[") or key.lower() == "or" for key in keys):
                raise PacketError("coverage item %s needs comma-separated parameter keys" % item["key"])
            unknown = sorted(set(keys) - param_keys)
            if unknown:
                raise PacketError("coverage item %s lists unknown parameter keys: %s" % (
                    item["key"], ", ".join(unknown)
                ))
            covered.update(keys)
        else:
            match = re.match(r"reason:\s*(.+)$", detail, re.I)
            reason = match.group(1).strip() if match else ""
            if not reason or reason.startswith("[") or reason.lower() == "enter reason":
                raise PacketError("coverage item %s needs a not-applicable reason" % item["key"])
            keys = []
        decisions[item["key"]] = {"decision": decision, "parameter_keys": keys,
                                  "reason": reason if decision == "Not applicable" else ""}
    missing = sorted(param_keys - covered)
    if missing:
        raise PacketError("coverage checklist does not account for parameter keys: %s" % ", ".join(missing))
    return decisions


def finalize_archive(archive_dir):
    archive_dir = Path(archive_dir).expanduser().resolve()
    manifest_path = archive_dir / "manifest.json"
    review_path = archive_dir / "datasheet-review.md"
    if not manifest_path.is_file() or not review_path.is_file():
        raise PacketError("archive must contain manifest.json and datasheet-review.md")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise PacketError("archive manifest unreadable: %s" % error)
    review_text = review_path.read_text(encoding="utf-8")
    if manifest.get("review_record", {}).get("status") != "PENDING":
        raise PacketError("archive is not pending review")

    reviewer_match = re.search(r"^- Reviewer: ([^\r\n]+)$", review_text, re.M)
    date_match = re.search(r"^- Review date: ([^\r\n]+)$", review_text, re.M)
    reviewer = reviewer_match.group(1).strip() if reviewer_match else ""
    review_date = date_match.group(1).strip() if date_match else ""
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", reviewer) or reviewer.startswith("["):
        raise PacketError("enter a one-word reviewer handle")
    try:
        datetime.date.fromisoformat(review_date)
    except ValueError:
        raise PacketError("enter a valid review date as YYYY-MM-DD")
    if not re.search(r"^- Attestation: \[x\]", review_text, re.I | re.M):
        raise PacketError("human-review attestation must be checked")

    parameter_rows = {row["key"]: row for row in manifest.get("parameters", [])}
    table = {}
    for cells in table_rows(review_text):
        if len(cells) != 6 or cells[0] not in parameter_rows:
            continue
        if cells[0] in table:
            raise PacketError("duplicate parameter decision row: %s" % cells[0])
        table[cells[0]] = cells
    if set(table) & set(parameter_rows) != set(parameter_rows):
        missing = sorted(set(parameter_rows) - set(table))
        raise PacketError("parameter decisions missing for: %s" % ", ".join(missing))
    decisions = {}
    for key in parameter_rows:
        decision = row_decisions(
            table[key][4], ("Confirmed", "Needs correction", "Unable to verify")
        )
        decisions[key] = decision

    component_dir = archive_dir.parent.parent
    component_path = component_dir / "component.toml"
    try:
        with component_path.open("rb") as component_file:
            component_data = tomllib.load(component_file)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise PacketError("component.toml unreadable: %s" % error)
    current_params = component_data.get("param", {})
    if set(current_params) != set(parameter_rows):
        raise PacketError("component parameter keys changed since packet generation; regenerate the archive")
    for key, row in parameter_rows.items():
        if row.get("component_snapshot") != component_snapshot(current_params[key]):
            raise PacketError("component values or cite changed since packet generation for %s" % key)
        stamp = current_params[key].get("verified", "")
        kind = current_params[key].get("verification_type")
        matches_review = isinstance(stamp, str) and stamp.startswith("%s %s " % (reviewer, review_date))
        if decisions[key] == "Confirmed":
            if kind != "human_page_image" or not matches_review:
                raise PacketError(
                    "%s is Confirmed but lacks this reviewer's dated human_page_image stamp in component.toml" % key
                )
        elif kind == "human_page_image":
            raise PacketError("%s has a human_page_image stamp but is not Confirmed" % key)

    coverage = coverage_decisions(archive_dir, manifest)
    revised_text = re.sub(
        r"^\*\*Review status: PENDING — no human review has been recorded\.\*\*$",
        "**Review status: HUMAN-REVIEWED by `%s` on `%s`.**" % (reviewer, review_date),
        review_text, count=1, flags=re.M,
    )
    if revised_text == review_text:
        raise PacketError("pending review status marker is missing")
    updated = dict(manifest)
    updated["human_review"] = "HUMAN_REVIEWED"
    updated["review_record"] = {
        "status": "HUMAN-REVIEWED",
        "reviewer": reviewer,
        "review_date": review_date,
        "attestation": True,
        "parameter_decisions": decisions,
        "coverage_decisions": coverage,
    }
    review_path.write_text(revised_text, encoding="utf-8")
    manifest_path.write_text(json.dumps(updated, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return updated["review_record"]


def save_archive(packet, packet_dir, component_dir):
    archive_root = Path(component_dir) / "datasheet-review"
    archive_dir = archive_root / packet["pdf_sha256"][:12]
    if archive_dir.exists():
        raise PacketError("review archive already exists: %s" % archive_dir)
    if archive_root.exists() and not archive_root.is_dir():
        raise PacketError("review archive path is not a directory: %s" % archive_root)

    image_paths = set(packet["context_images"].values())
    for row in packet["parameters"]:
        image_paths.update(row["image_paths"])
    for relative in sorted(image_paths):
        source = (Path(packet_dir) / relative).resolve()
        try:
            source.relative_to(Path(packet_dir).resolve())
        except ValueError:
            raise PacketError("generated image path escapes the packet directory")
        if not source.is_file():
            raise PacketError("review image is missing: %s" % relative)

    archive_root.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".pending-review-", dir=archive_root))
    try:
        for relative in sorted(image_paths):
            source = Path(packet_dir) / relative
            destination = staging / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        archive_manifest = dict(packet)
        archive_manifest["review_record"] = {
            "status": "PENDING",
            "reviewer": "",
            "review_date": "",
            "attestation": False,
        }
        (staging / "manifest.json").write_text(
            json.dumps(archive_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        (staging / "datasheet-review.md").write_text(build_review_record(packet), encoding="utf-8")
        (staging / "coverage.md").write_text(build_coverage(packet), encoding="utf-8")
        if archive_dir.exists():
            raise PacketError("review archive already exists: %s" % archive_dir)
        os.replace(staging, archive_dir)
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    return archive_dir


def build_packet(pdf, component, out_dir, archive=False):
    pdf = Path(pdf).expanduser().resolve()
    out_dir = Path(out_dir).expanduser().resolve()
    toml_path, params = load_component(component)
    component_dir = toml_path.parent
    if out_dir == component_dir or component_dir in out_dir.parents:
        raise PacketError("output directory must be outside the component directory")
    file_error = D.check_file(str(pdf))
    if file_error:
        raise PacketError(file_error)
    if out_dir.exists():
        if not out_dir.is_dir():
            raise PacketError("output path is not a directory")
        if any(out_dir.iterdir()):
            raise PacketError("output directory must be empty")
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf_sha256 = hashlib.sha256(pdf.read_bytes()).hexdigest()
    if archive and (component_dir / "datasheet-review" / pdf_sha256[:12]).exists():
        raise PacketError("review archive already exists: %s" % (
            component_dir / "datasheet-review" / pdf_sha256[:12]
        ))

    try:
        index, _jobs = D.build(str(pdf), str(out_dir), figures=True, crops=False)
    except OSError as e:
        raise PacketError("could not run the local PDF tools: %s" % e)
    page_count = index.get("page_count") or pdf_page_count(pdf)
    printed_pages = index.get("printed_pages", {})
    page_boxes = []
    if not index.get("reason", "").startswith("no text layer"):
        rc, xhtml, _err = D.run(["pdftotext", "-bbox-layout", str(pdf), "-"])
        if rc == 0 and "<page" in xhtml:
            page_boxes = D.parse_bbox(xhtml)
    rotations = D.page_rotations(str(pdf), page_count) if page_boxes else {}
    try:
        checks, fatal = T.check_rows(str(pdf), str(toml_path))
    except OSError as e:
        raise PacketError("could not run the local PDF tools: %s" % e)
    check_by_key = {key: (status, reason) for key, status, reason in checks}
    if fatal:
        check_by_key = {}

    evidence_specs = []
    required_pages = set()
    for ordinal, key in enumerate(sorted(params), 1):
        row = params[key]
        cite = row.get("cite", "")
        pdf_page, printed_page, cite_problem = cite_page(cite, printed_pages, page_count)
        crop_boxes = []
        crop_mode = None
        if (
            pdf_page is not None
            and len(page_boxes) == page_count
            and 1 <= pdf_page <= len(page_boxes)
            and not rotations.get(pdf_page, 0)
        ):
            page = page_boxes[pdf_page - 1]
            symbol = row.get("symbol")
            if isinstance(symbol, str) and symbol:
                row_bbox = T.locate_row_bbox(page, symbol)
                crop_boxes = [row_bbox] if row_bbox else T.locate_evidence_bboxes(page, row, cite)
            else:
                crop_boxes = T.locate_evidence_bboxes(page, row, cite)
            if crop_boxes:
                crop_mode = "row_crop"
            else:
                crop_boxes = indexed_table_bboxes(index, pdf_page, cite)
                if crop_boxes:
                    crop_mode = "table_crop"
        status, reason = check_by_key.get(key, ("UNSURE", fatal or cite_problem or "no text-layer check result"))
        if cite_problem:
            status = "UNSURE"
            reason = cite_problem + ("; " + reason if reason and reason != cite_problem else "")
        if index.get("reason", "").startswith("no text layer"):
            status = "UNSURE"
            reason = "PDF has no usable text layer; compare the page images manually"
        if pdf_page is not None:
            required_pages.add(pdf_page)
        evidence_specs.append((ordinal, key, row, cite, pdf_page, printed_page, crop_boxes, crop_mode, status, reason))

    # Unmapped parameters get the complete local page set as fallback context, without guessing a cite location.
    if any(item[4] is None for item in evidence_specs):
        required_pages.update(range(1, page_count + 1))

    context_images = {}
    for page in sorted(required_pages):
        path = render_page(pdf, page, out_dir / "context" / ("page-%04d.png" % page))
        context_images[str(page)] = path.relative_to(out_dir).as_posix()

    result_rows = []
    for ordinal, key, row, cite, pdf_page, printed_page, crop_boxes, crop_mode, status, reason in evidence_specs:
        image_paths = []
        if pdf_page is not None:
            if crop_boxes:
                for crop_index, bbox in enumerate(crop_boxes, 1):
                    suffix = "" if len(crop_boxes) == 1 else "-%d" % crop_index
                    destination = out_dir / "evidence" / (safe_stem(key, ordinal) + suffix + ".png")
                    path = render_crop(pdf, pdf_page, bbox, destination)
                    image_paths.append(path.relative_to(out_dir).as_posix())
                crop_mode = crop_mode or "row_crop"
            else:
                destination = out_dir / "evidence" / (safe_stem(key, ordinal) + ".png")
                path = render_page(pdf, pdf_page, destination)
                crop_mode = "full_page_fallback"
                image_paths.append(path.relative_to(out_dir).as_posix())
        else:
            image_paths.extend(context_images.values())
            if image_paths:
                crop_mode = "full_document_fallback"
        crop_coordinates = crop_boxes or None
        result_rows.append({
            "key": key,
            "status": {"AGREE": "AGREE_TEXT_CHECK"}.get(status, status),
            "reason": reason,
            "cite": cite,
            "values": component_values(row),
            "component_snapshot": component_snapshot(row),
            "pdf_sha256": pdf_sha256,
            "pdf_pages": [pdf_page] if pdf_page is not None else [],
            "printed_pages": [printed_page] if printed_page is not None else [],
            "crop_coordinates": crop_coordinates,
            "full_page": not crop_boxes,
            "crop_mode": crop_mode,
            "image_path": image_paths[0] if image_paths else None,
            "image_paths": image_paths,
        })

    counts = {name: 0 for name in ("AGREE_TEXT_CHECK", "DISAGREE", "UNSURE")}
    for row in result_rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    packet = {
        "tool": "ds_review_packet",
        "trust": "SHADOW",
        "version": 2,
        "component": component_dir.name,
        "pdf_sha256": pdf_sha256,
        "pdf_page_count": page_count,
        "index_status": index.get("status", "FAIL"),
        "index_reason": index.get("reason", ""),
        "human_review": "NOT_PERFORMED",
        "summary": counts,
        "parameters": result_rows,
        "coverage_items": indexed_coverage_items(index),
        "context_images": context_images,
        "limitations": [
            "Text cross-check is CHECK ONLY and cannot establish human verification.",
            "A row snippet is cropped only when table_xcheck-style parsing isolates one symbol row; otherwise a full-page fallback is used.",
            "A DISAGREE or AGREE_TEXT_CHECK requires adjudication against the page image.",
            "No claim of complete datasheet coverage is made.",
            "Do not redistribute the PDF or screenshots except as permitted by the vendor license.",
        ],
    }

    (out_dir / "manifest.json").write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (out_dir / "review.html").write_text(render_html(packet), encoding="utf-8")
    (out_dir / "github-review.md").write_text(build_markdown(packet), encoding="utf-8")
    (out_dir / "github-issue.md").write_text(build_issue_draft(packet), encoding="utf-8")
    (out_dir / "coverage.md").write_text(build_coverage(packet), encoding="utf-8")
    if archive:
        packet["archive_path"] = str(save_archive(packet, out_dir, component_dir))
    return packet


def render_html(packet):
    rows = []
    for row in packet["parameters"]:
        values = html.escape(display_values(row["values"]))
        label = {
            "row_crop": "row snippet",
            "table_crop": "table excerpt",
        }.get(row["crop_mode"], "full-page fallback")
        images = " ".join(
            '<a href="%s"><img loading="lazy" src="%s" alt="%s"><small>%s</small></a>' % (
                html.escape(path, quote=True), html.escape(path, quote=True),
                html.escape(label, quote=True), html.escape(label),
            ) for path in row["image_paths"]
        ) or "No page assigned"
        rows.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><code>%s</code></td><td>%s</td></tr>" % (
            html.escape(row["key"]), html.escape(row["status"]), html.escape(row["reason"]),
            html.escape(row.get("cite", "")), values, images,
        ))
    context = " ".join(
        '<figure><img loading="lazy" src="%s" alt="PDF page %s"><figcaption>PDF page %s</figcaption></figure>' % (
            html.escape(path, quote=True), html.escape(page), html.escape(page),
        ) for page, path in packet["context_images"].items()
    )
    return """<!doctype html>
<meta charset="utf-8">
<title>Datasheet review packet</title>
<style>
body{font:15px system-ui,sans-serif;max-width:1200px;margin:2rem auto;padding:0 1rem}
table{border-collapse:collapse;width:100%%}th,td{border:1px solid #bbb;padding:.5rem;text-align:left;vertical-align:top}
td img{max-width:420px;height:auto}figure{display:inline-block;width:28%%;vertical-align:top}figure img{width:100%%}
.warning{background:#fff3cd;padding:1rem}
</style>
<h1>Datasheet review packet</h1>
<p class="warning">SHADOW only. Human review NOT PERFORMED. Text checks are CHECK ONLY, never a source.
Do not redistribute the PDF or screenshots except as permitted by the vendor license.</p>
<p>Component: <code>%s</code><br>PDF SHA-256: <code>%s</code></p>
<h2>Component values versus datasheet evidence snippets</h2>
<table><thead><tr><th>Key</th><th>Status</th><th>Reason</th><th>Cite</th><th>Component values</th><th>Evidence</th></tr></thead>
<tbody>%s</tbody></table>
<h2>Full-page context</h2>%s
""" % (html.escape(packet["component"]), packet["pdf_sha256"], "".join(rows), context)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pdf", nargs="?", help="datasheet PDF (never copied)")
    parser.add_argument("component", nargs="?", help="component.toml or component directory (read-only)")
    parser.add_argument("--out", help="new or empty packet directory")
    parser.add_argument("--archive", action="store_true",
                        help="save a PENDING review record and evidence beside the component (no PDF copy)")
    parser.add_argument("--finalize", metavar="ARCHIVE_DIR",
                        help="mark an archive HUMAN-REVIEWED only after all review and coverage checks pass")
    args = parser.parse_args(argv)
    if args.finalize:
        if args.pdf or args.component or args.out or args.archive:
            parser.error("--finalize cannot be combined with packet-generation arguments")
        try:
            record = finalize_archive(args.finalize)
        except PacketError as e:
            print("FAIL: %s" % e, file=sys.stderr)
            return 1
        print("review record: HUMAN-REVIEWED by %s on %s" % (record["reviewer"], record["review_date"]))
        return 0
    if not args.pdf or not args.component or not args.out:
        parser.error("PDF, component and --out are required unless --finalize is used")
    try:
        packet = build_packet(args.pdf, args.component, args.out, archive=args.archive)
    except PacketError as e:
        print("FAIL: %s" % e, file=sys.stderr)
        return 1
    print("packet: %s" % Path(args.out).expanduser().resolve())
    if packet.get("archive_path"):
        print("review record: %s" % packet["archive_path"])
    print("parameters: %d; AGREE_TEXT_CHECK=%d DISAGREE=%d UNSURE=%d; human review: not performed" % (
        len(packet["parameters"]), packet["summary"]["AGREE_TEXT_CHECK"],
        packet["summary"]["DISAGREE"], packet["summary"]["UNSURE"],
    ))
    return 2 if packet["summary"]["DISAGREE"] else 0


if __name__ == "__main__":
    sys.exit(main())
