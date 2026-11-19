#!/usr/bin/env python3
"""Datasheet index from the PDF text layer: table/figure titles -> page, printed page, bounding boxes, crops.

usage: tools/ds_index.py <datasheet.pdf> --out <dir> [--figures] [--no-crops]

Writes <dir>/index.json and crops <dir>/crops/*.png (pdftoppm, DPI chosen from the glyph height, 200..400).
One job: locate titles. It never reads values. Boxes are ESTIMATES: from the title top to the next title on the
page (or the page bottom), full text width; a table can continue on the next page.

Item status (one item per expected key, plus one per "Table N" / "Figure N" / "Diagram N" caption):
  OK      the title was found exactly once, in the expected form, on a page with a printed page number, not on a
          rotated page, and is not a continued table.
  UNSURE  found more than once, a "(continued)" title, a rotated page, no printed page number, a trailing
          subtitle/page-range in the title line, or not found at all (listed under "not_found").
  FAIL    file missing/truncated/unreadable, or no text layer (scanned PDF), or zero titles matched.
Exit code 1 on any FAIL. The summary line counts OK/UNSURE/FAIL and lists expected sections not found.
"""
import argparse
import functools
import hashlib
import html
import json
import os
import re
import statistics
import subprocess
import sys

# key -> regex for the title text (after an optional "7.5" / "Table 3." prefix). Case-insensitive.
SECTIONS = [
    ("abs_max", r"(?:absolute\s+)?maximum\s+ratings"),
    ("esd", r"ESD\s+ratings"),
    ("rec_op", r"recommended\s+operating\s+conditions"),
    ("thermal", r"thermal\s+(?:information|characteristics)"),
    ("electrical", r"electrical\s+characteristics"),
    ("static_characteristics", r"static\s+characteristics"),
    ("dynamic_characteristics", r"dynamic\s+characteristics"),
    ("gate_charge", r"gate\s+charge\s+characteristics"),
    ("reverse_diode", r"reverse\s+diode"),
    ("pin_config", r"pin\s+configuration(?:\s+and\s+functions)?"),
    ("pin_functions", r"pin\s+(?:functions|descriptions?)"),
    ("ordering", r"ordering\s+information"),
    ("package_option", r"package\s+option\s+addendum"),
    ("land_pattern", r"(?:recommended\s+)?(?:land\s+pattern(?:\s+example)?|solder\s+pad(?:\s+(?:layout|pitch\s+and\s+dimensions|dimensions))?|footprint)"),
    ("package_outline", r"package\s+(?:outline|information|dimensions)|dimensions"),
    ("typical_characteristics", r"typical\s+(?:performance\s+)?characteristics"),
]
PREFIX = r"^(?:\d+(?:[.\-]\d+)*\s+)?(?:Table\s+[\d.\-]+[.:]?\s+)?"
CAPTION = [("table", re.compile(r"^Table\s+([\d.\-]+?)(?:([.:])\s*|\s+)(.*)$", re.I)),
           ("figure", re.compile(r"^Figure\s+([\d.\-]+?)(?:([.:])\s*|\s+)(.*)$", re.I)),
           ("diagram", re.compile(r"^Diagram\s+([\d.\-]+?)(?:([.:])\s*|\s+)(.*)$", re.I))]
HEADING = re.compile(r"^\d+(?:\.\d+)+\s+[A-Z][A-Za-z]|^[A-Z][A-Z0-9 /&()\-,]{8,}$")
TOC = re.compile(r"(?:\.\s*){4,}")
CONT = re.compile(r"\(\s*continued\s*\)|\(\s*cont\.?\s*\)", re.I)


def norm_dash(t):
    return t.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")


def run(cmd):
    p = subprocess.run(cmd, capture_output=True)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def check_file(path):
    if not os.path.isfile(path):
        return "file missing"
    size = os.path.getsize(path)
    if size < 100:
        return "file empty or truncated (%d bytes)" % size
    with open(path, "rb") as f:
        head = f.read(8)
        f.seek(max(0, size - 2048))
        tail = f.read()
    if not head.startswith(b"%PDF"):
        return "not a PDF (no %PDF header)"
    if b"%%EOF" not in tail:
        return "truncated PDF (no %%EOF near the end)"
    return None


def parse_bbox(xhtml):
    """-> list of pages: {w, h, lines:[{x0,y0,x1,y1,text,words:[(x0,y0,x1,y1,text)]}]}"""
    pages = []
    for pm in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', xhtml, re.S):
        page = {"w": float(pm.group(1)), "h": float(pm.group(2)), "lines": []}
        for lm in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>',
                              pm.group(3), re.S):
            words = []
            for a, b, c, d, t in re.findall(
                    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',
                    lm.group(5), re.S):
                a, b, c, d, t = float(a), float(b), float(c), float(d), html.unescape(t)
                if re.search(r"[\x00-\x1f]", t):
                    # some PDFs put control characters (e.g. \x02) where spaces belong: split, interpolate x
                    n = len(t)
                    for m in re.finditer(r"[^\x00-\x1f]+", t):
                        words.append((a + (c - a) * m.start() / n, b, a + (c - a) * m.end() / n, d, m.group(0)))
                else:
                    words.append((a, b, c, d, t))
            if not words:
                continue
            text = re.sub(r"\s+", " ", " ".join(w[4] for w in words)).strip()
            text = text.replace("–", "-").replace("—", "-").replace("−", "-")
            page["lines"].append({"x0": float(lm.group(1)), "y0": float(lm.group(2)), "x1": float(lm.group(3)),
                                   "y1": float(lm.group(4)), "text": text, "words": words})
        pages.append(page)
    return pages


def y_rows(lines):
    """Words of the given text lines regrouped into visual rows (same y within 3 pt), each sorted by x."""
    words = sorted((w for ln in lines for w in ln["words"]), key=lambda w: (w[1] + w[3]) / 2)
    rows = []
    for w in words:
        ym = (w[1] + w[3]) / 2
        if rows and abs(ym - rows[-1]["ymid"]) <= 3:
            rows[-1]["words"].append(w)
            rows[-1]["ymid"] += (ym - rows[-1]["ymid"]) / len(rows[-1]["words"])
        else:
            rows.append({"ymid": ym, "words": [w]})
    for r in rows:
        r["words"].sort(key=lambda w: w[0])
    return rows


def page_rotations(path, n):
    rc, out, _ = run(["pdfinfo", "-f", "1", "-l", str(n), path])
    rot = {}
    for m in re.finditer(r"^Page\s+(\d+)\s+rot:\s+(\d+)", out, re.M):
        rot[int(m.group(1))] = int(m.group(2))
    return rot


def printed_pages(pages):
    """Majority-vote offset (printed - pdf page) from digit tokens in the header/footer bands."""
    cands = {}
    for i, pg in enumerate(pages, 1):
        c = set()
        for ln in pg["lines"]:
            for w in ln["words"]:
                if w[1] < pg["h"] * 0.09 or w[1] > pg["h"] * 0.90:
                    m = re.match(r"^(\d{1,4})(?:/\d{1,4})?$", w[4])
                    if m:
                        c.add(int(m.group(1)))
        cands[i] = c
    votes = {}
    for i, c in cands.items():
        for v in c:
            votes[v - i] = votes.get(v - i, 0) + 1
    if not votes:
        return {}, None
    best = sorted(votes.items(), key=lambda kv: (-kv[1], abs(kv[0]), kv[0]))[0]
    if best[1] < min(3, len(pages)):
        return {}, None
    off = best[0]
    return {i: i + off for i, c in cands.items() if i + off in c}, off


def _loose(pat):
    return pat.replace(r"\s+", r"\s*")


PREFIX_LOOSE = r"^(?:\d+(?:[.\-]\d+)*\s*)?(?:Table\s*[\d.\-]+[.:]?\s*)?"
NOTES = re.compile(r"^\(\s*notes?\s+[\d, and]+\)$", re.I)


@functools.lru_cache(maxsize=None)
def classify(text):
    """-> tuple of (kind, key, suffix_kind, via) for one line; empty when it is not a known title."""
    if TOC.search(text):
        return ()
    for loose in (False, True):
        for key, pat in SECTIONS:
            if loose:
                m = re.match(PREFIX_LOOSE + "(" + _loose(pat) + ")(.*)$", text, re.I)
            else:
                m = re.match(PREFIX + "(" + pat + ")(.*)$", text, re.I)
            if not m:
                continue
            title, suffix = m.group(1), m.group(2).strip()
            if suffix == "" or NOTES.match(suffix):
                sk = "plain"
            elif CONT.fullmatch(suffix):
                sk = "continued"
            elif suffix[0] in "(:,-":
                sk = "subtitle"
            elif title.isupper() and suffix[0].isalpha():
                sk = "subtitle"  # ADI style: "ELECTRICAL CHARACTERISTICS The l denotes ..."
            else:
                continue
            if loose:
                if re.match(PREFIX + "(" + pat + ")", text, re.I):
                    continue  # the strict form matched this line before; not reached normally
                sk = "nospace"
            has_table = re.match(r"^(?:\d+(?:[.\-]\d+)*\s*)?Table\s*\d", text, re.I) is not None
            return (("section", key, sk, "table" if has_table else "heading"),)
    return ()


def caption(line):
    text = line["text"]
    if TOC.search(text):
        return None
    for kind, rx in CAPTION:
        nospace = False
        m = rx.match(text)
        if not m:
            m = re.match(r"^%s\s*([\d.\-]+?)(?:([.:])\s*|\s*)([A-Za-z].*)$" % kind, text, re.I)
            nospace = True
        if not m:
            continue
        label, punct, rest = m.group(1).rstrip(".:"), m.group(2), m.group(3).strip()
        if not rest or not label:
            return None
        if not punct:
            # "Table 2          Maximum ratings": accept only with a visible gap after the number, or no spaces at all
            ws = line["words"]
            gap = len(ws) >= 3 and ws[2][0] - ws[1][2] > 8
            if not gap and not (nospace and len(ws) == 1) and not (nospace and len(ws) <= 3):
                return None
            if not gap:
                nospace = True
        cont = bool(CONT.search(rest))
        return kind, label, CONT.sub("", rest).strip(), cont, nospace
    return None


def build(pdf, out_dir, figures, crops):
    doc = {"pdf": os.path.basename(pdf), "tool": "ds_index", "version": 1}
    err = check_file(pdf)
    if err:
        return dict(doc, status="FAIL", reason=err, complete=False, items=[], not_found=[]), []
    rc, xhtml, stderr = run(["pdftotext", "-bbox-layout", pdf, "-"])
    if rc != 0 or "<page" not in xhtml:
        return dict(doc, status="FAIL", reason="pdftotext failed: " + stderr.strip()[:120], complete=False,
                    items=[], not_found=[]), []
    with open(pdf, "rb") as f:
        doc["pdf_sha256"] = hashlib.sha256(f.read()).hexdigest()
    pages = parse_bbox(xhtml)
    rc, info, _ = run(["pdfinfo", pdf])
    m = re.search(r"^Pages:\s+(\d+)", info, re.M)
    if rc != 0 or not m or int(m.group(1)) != len(pages):
        return dict(doc, status="FAIL", reason="page count mismatch or unreadable (truncated?)", complete=False,
                    items=[], not_found=[]), []
    nwords = sum(len(l["words"]) for p in pages for l in p["lines"])
    textpages = sum(1 for p in pages if sum(len(l["words"]) for l in p["lines"]) >= 5)
    if nwords < 50 or textpages * 2 < len(pages):
        return dict(doc, status="FAIL", reason="no text layer (scanned PDF?): %d words, %d/%d pages with text" % (
            nwords, textpages, len(pages)), complete=False, items=[], not_found=[]), []
    rot = page_rotations(pdf, len(pages))
    printed, offset = printed_pages(pages)
    doc["pdf_abspath"] = os.path.abspath(pdf)
    doc["page_count"] = len(pages)
    doc["printed_page_offset"] = offset
    doc["printed_pages"] = {str(pdf_page): printed_page for pdf_page, printed_page in sorted(printed.items())}

    hits = {}  # item key -> list of hit dicts
    meta = {}

    def add(key, kind, pn, ln, sk, label, extra):
        pg = pages[pn - 1]
        hits.setdefault(key, []).append({"pdf_page": pn, "printed_page": printed.get(pn), "title": ln["text"],
                                         "title_bbox": [ln["x0"], ln["y0"], ln["x1"], ln["y1"]], "suffix": sk,
                                         "rotated": rot.get(pn, 0) != 0, "via": extra})
        meta[key] = kind

    for pn, pg in enumerate(pages, 1):
        for ln in pg["lines"]:
            for kind, key, sk, via in classify(ln["text"]):
                add(key, "section", pn, ln, sk, None, via)
            c = caption(ln)
            if c and (figures or c[0] != "figure"):
                kind, label, rest, cont, nosp = c
                add("%s:%s" % (kind, label), kind, pn, ln, "continued" if cont else ("nospace" if nosp else "plain"),
                    label, "caption")

    # merge same-page duplicates of a named section (e.g. "1 Maximum ratings" heading above "Table 2 Maximum
    # ratings"): same key, same page, all plain titles -> one hit, the lowest one (the table's own title)
    for key in list(hits):
        if meta[key] != "section":
            continue
        by_page = {}
        for h in hits[key]:
            by_page.setdefault(h["pdf_page"], []).append(h)
        merged = []
        for pn in sorted(by_page):
            hs = by_page[pn]
            if len(hs) > 1 and all(h["suffix"] == "plain" for h in hs):
                merged.append(sorted(hs, key=lambda h: h["title_bbox"][1])[-1])
            else:
                merged.extend(hs)
        hits[key] = merged

    # title boundaries per page
    bounds = {}
    for pn, pg in enumerate(pages, 1):
        b = []
        for ln in pg["lines"]:
            if classify(ln["text"]) or caption(ln) or HEADING.match(ln["text"]):
                b.append(ln["y0"])
        bounds[pn] = sorted(b)

    items = []
    crop_jobs = []
    for key in sorted(hits):
        hs = sorted(hits[key], key=lambda h: (h["pdf_page"], h["title_bbox"][1]))
        for idx, h in enumerate(hs):
            pg = pages[h["pdf_page"] - 1]
            x0 = min(l["x0"] for l in pg["lines"])
            x1 = max(l["x1"] for l in pg["lines"])
            top = h["title_bbox"][1] - 2
            below = [y for y in bounds[h["pdf_page"]] if y > h["title_bbox"][3] + 2]
            bottom_lim = pg["h"] * 0.93
            if below and below[0] < bottom_lim:
                bot, end = below[0], "next_title"
            else:
                bot, end = bottom_lim, "page_bottom"
            h["table_bbox"] = [x0, max(0.0, top), x1, bot]
            h["end"] = end
            hts = [w[3] - w[1] for l in pg["lines"] if top <= l["y0"] <= bot for w in l["words"]]
            gh = statistics.median(hts) if hts else 9.0
            h["dpi"] = int(min(400, max(200, round(30.0 / max(gh, 1.0) * 72.0 / 10.0) * 10)))
            if crops and (meta[key] != "figure"):
                name = "crops/%s_p%d%s.png" % (re.sub(r"[^A-Za-z0-9_.-]", "_", key), h["pdf_page"],
                                              "" if idx == 0 or hs[idx - 1]["pdf_page"] != h["pdf_page"] else "_%d" % idx)
                h["crop"] = name
                crop_jobs.append((h, name))
            elif crops:
                name = "crops/%s_p%d.png" % (re.sub(r"[^A-Za-z0-9_.-]", "_", key), h["pdf_page"])
                h["crop"] = name
                crop_jobs.append((h, name))
        # status
        if len(hs) > 1:
            st, why = "UNSURE", "found %d times (pages %s)" % (len(hs), ",".join(str(h["pdf_page"]) for h in hs))
        else:
            h = hs[0]
            if h["suffix"] == "continued":
                st, why = "UNSURE", "continued table title"
            elif h["suffix"] == "subtitle":
                st, why = "UNSURE", "title line carries a subtitle/qualifier"
            elif h["suffix"] == "nospace":
                st, why = "UNSURE", "text layer has no word spaces; title matched loosely"
            elif h["rotated"]:
                st, why = "UNSURE", "rotated page"
            elif h["printed_page"] is None:
                st, why = "UNSURE", "no printed page number on the page"
            else:
                st, why = "OK", "found once, printed page %d" % h["printed_page"]
        if st != "UNSURE" or len(hs) == 1:
            pass
        if any(h["suffix"] == "continued" for h in hs) and len(hs) > 1:
            why += "; continued table"
        if any(h["rotated"] for h in hs) and "rotated" not in why:
            why += "; rotated page"
        if any(h["printed_page"] is None for h in hs) and st == "UNSURE" and "no printed" not in why:
            why += "; some hits have no printed page number"
        items.append({"key": key, "kind": meta[key], "status": st, "reason": why, "hits": hs})

    expected = [k for k, _ in SECTIONS]
    not_found = [k for k in expected if k not in hits]
    for k in not_found:
        items.append({"key": k, "kind": "section", "status": "UNSURE", "reason": "title not found", "hits": []})
    items.sort(key=lambda i: i["key"])
    if not hits:
        return dict(doc, status="FAIL", reason="zero titles matched", complete=False, items=items,
                    not_found=not_found), []
    doc.update(status="OK", reason="", complete=not not_found, items=items, not_found=not_found)
    return doc, crop_jobs


def render_crops(pdf, out_dir, jobs):
    os.makedirs(os.path.join(out_dir, "crops"), exist_ok=True)
    for h, name in jobs:
        dpi = h["dpi"]
        s = dpi / 72.0
        x0, y0, x1, y1 = h["table_bbox"]
        px = [int(x0 * s), int(y0 * s), int((x1 - x0) * s) + 1, int((y1 - y0) * s) + 1]
        base = os.path.join(out_dir, name[:-4])
        rc, _, err = run(["pdftoppm", "-r", str(dpi), "-f", str(h["pdf_page"]), "-l", str(h["pdf_page"]),
                          "-x", str(px[0]), "-y", str(px[1]), "-W", str(px[2]), "-H", str(px[3]),
                          "-png", "-singlefile", pdf, base])
        if rc != 0:
            h["crop"] = None
            h["crop_error"] = err.strip()[:100]


def fmt(o):
    if isinstance(o, float):
        return round(o, 2)
    if isinstance(o, dict):
        return {k: fmt(v) for k, v in o.items()}
    if isinstance(o, list):
        return [fmt(v) for v in o]
    return o


def main(argv=None):
    ap = argparse.ArgumentParser(description="Datasheet index (titles -> page, printed page, bbox, crops) from the text layer.")
    ap.add_argument("pdf")
    ap.add_argument("--out", required=True, help="output directory (index.json + crops/)")
    ap.add_argument("--figures", action="store_true", help="also index and crop Figure/Diagram captions")
    ap.add_argument("--no-crops", action="store_true", help="index only; render no PNG crops")
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)
    doc, jobs = build(a.pdf, a.out, a.figures, not a.no_crops)
    if jobs:
        render_crops(a.pdf, a.out, jobs)
    doc = fmt(doc)
    counts = {"OK": 0, "UNSURE": 0, "FAIL": 0}
    for it in doc["items"]:
        counts[it["status"]] += 1
        print("%s: %s %s" % (it["key"], it["status"], it["reason"]))
    if doc["status"] == "FAIL":
        counts["FAIL"] += 1
        print("DOCUMENT: FAIL %s" % doc["reason"])
    doc["summary"] = {"OK": counts["OK"], "UNSURE": counts["UNSURE"], "FAIL": counts["FAIL"]}
    with open(os.path.join(a.out, "index.json"), "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=1, sort_keys=True)
        f.write("\n")
    print("summary: OK=%d UNSURE=%d FAIL=%d complete=%s not_found=[%s]" % (
        counts["OK"], counts["UNSURE"], counts["FAIL"], str(doc.get("complete", False)).lower(),
        ",".join(doc.get("not_found", []))))
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
