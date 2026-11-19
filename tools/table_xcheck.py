#!/usr/bin/env python3
"""Cross-check committed component.toml rows against clean text-layer tables. A CHECK, never a source.

usage: tools/table_xcheck.py <datasheet.pdf> <component.toml>

For each [param.*] row that has a number and a `DS p.<printed page>` cite, look on that page for ONE clean table line
whose leftmost word (or word under a "Symbol" header) is the row's symbol, split its numbers into the MIN/TYP/MAX
columns found from the header row, read the unit cell, and compare with the committed min/typ/max/unit.
It prints a status per row and NEVER prints values for use in component.toml; a DISAGREE line names only the
differing column, for adjudication against the page image.

Row status:
  AGREE     one clean single-line row found; every committed min/typ/max equals the printed number in the same
            column, no extra printed numbers, and the unit string is identical after ASCII normalisation.
  DISAGREE  one clean row found, units equal, and a number differs (or the table prints a number the row lacks).
  UNSURE    anything else: merged cells, symbol not on the value line, several candidate rows, continuation lines,
            footnote markers, "+/-", "<", ">", "%", ppm, curve/sym/typ_pm/tol_pct/_ref conventions, units that do
            not compare, a printed page that is not numbered, a rotated page, or a vendor not yet in TESTED_VENDORS.
  FAIL      (whole run) missing/truncated/scanned PDF, missing or empty toml, no MIN/TYP/MAX header in the PDF.
Exit code: 1 on FAIL, 2 on any DISAGREE (and no FAIL), else 0. Summary line counts AGREE/DISAGREE/UNSURE/FAIL.
"""
import os
import re
import sys
import tomllib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_index as D  # noqa: E402

# Vendors whose datasheets were run through the golden set with zero wrong AGREE (see tools/TRUST.md).
TESTED_VENDORS = ("Texas Instruments", "Analog Devices", "STMicroelectronics", "Infineon")  # name prefixes

NUM = re.compile(r"^[-+]?(?:\d+\.?\d*|\.\d+)$")
UNIT_MAP = [("µ", "u"), ("μ", "u"), ("Ω", "ohm"), ("Ω", "ohm"), ("°C", "degC"),
            ("°", "deg")]
ODD_ROW_KEYS = ("sym", "typ_pm", "tol_pct", "curve", "min_ref", "max_ref", "typ_ref", "text")


def norm_minus(t):
    return t.replace("–", "-").replace("—", "-").replace("−", "-")


def norm_unit(u):
    u = u.strip()
    for a, b in UNIT_MAP:
        u = u.replace(a, b)
    return re.sub(r"\s+", "", u)


def find_headers(page):
    """-> list of dicts {y0, y1, cols:{min,typ,max: xmid}, unit_x or None, sym_x list}, sorted by y."""
    words = [w for ln in page["lines"] for w in ln["words"]]
    heads = []
    for w in words:
        if re.fullmatch(r"(?i)min\.?", w[4]):
            ymid = (w[1] + w[3]) / 2
            row = [v for v in words if abs((v[1] + v[3]) / 2 - ymid) < 3]
            t = [v for v in row if re.fullmatch(r"(?i)typ\.?", v[4])]
            m = [v for v in row if re.fullmatch(r"(?i)max\.?", v[4])]
            if len(t) == 1 and len(m) == 1 and w[0] < t[0][0] < m[0][0]:
                cols = {"min": (w[0] + w[2]) / 2, "typ": (t[0][0] + t[0][2]) / 2, "max": (m[0][0] + m[0][2]) / 2}
                unit = [v for v in words if re.fullmatch(r"(?i)units?", v[4]) and abs((v[1] + v[3]) / 2 - ymid) < 25
                        and v[0] > m[0][0]]
                sym = [(v[0], v[2]) for v in words if re.fullmatch(r"(?i)symbols?", v[4]) and abs((v[1] + v[3]) / 2 - ymid) < 25]
                heads.append({"y0": w[1], "y1": w[3], "cols": cols,
                              "unit_x": (unit[0][0] + unit[0][2]) / 2 if unit else None, "sym": sym})
    heads.sort(key=lambda h: h["y0"])
    out = []
    for h in heads:  # one header per cluster
        if not out or h["y0"] - out[-1]["y0"] > 4:
            out.append(h)
    return out


def y_lines(page):
    """Words grouped into y-lines: list of {ymid, y0, y1, words sorted by x}."""
    lines = D.y_rows(page["lines"])
    for ln in lines:
        ln["y0"] = min(w[1] for w in ln["words"])
        ln["y1"] = max(w[3] for w in ln["words"])
    return lines


def split_line(ln, h):
    """Words of a line -> (label words, {col: [tokens]}, unit words, between-columns words)."""
    c = h["cols"]
    sp = (c["max"] - c["min"]) / 2
    lab, cells, unit, bad = [], {"min": [], "typ": [], "max": []}, [], []
    for w in ln["words"]:
        xm = (w[0] + w[2]) / 2
        if xm < c["min"] - 0.6 * sp:
            lab.append(w)
            continue
        if xm > c["max"] + 0.6 * sp:
            unit.append(w)
            continue
        col = min(c, key=lambda k: abs(c[k] - xm))
        if abs(c[col] - xm) <= 0.6 * sp:
            cells[col].append(w)
        else:
            bad.append(w)
    return lab, cells, unit, bad


def parse_cells(cells):
    """-> ({col: float or None}, reason or None). reason set when any cell is not a plain number or blank."""
    out = {}
    for col, ws in cells.items():
        if not ws:
            out[col] = None
            continue
        if len(ws) != 1:
            return None, "cell %s holds several tokens (merged/footnote/range)" % col
        t = norm_minus(ws[0][4])
        if t in ("-",):
            out[col] = None
        elif NUM.match(t):
            out[col] = float(t)
        else:
            return None, "cell %s is not a plain number (%s)" % (col, "marker or text")
    return out, None


def row_conventions(row):
    for k in ODD_ROW_KEYS:
        if k in row:
            return "row uses convention '%s'" % k
    if row.get("scope") == "partial":
        return "partial-scope row"
    u = row.get("unit", "")
    if not u or re.search(r"[%]|ppm|\+/-|LSB|/rtHz|pp$", u):
        return "unit %r not comparable" % u
    return None


def cite_page(cite):
    m = re.match(r"^DS p\.(\d+),", cite or "")
    return int(m.group(1)) if m else None


def check_rows(pdf, toml_path):
    """-> (rows [(key, status, reason)], fatal or None)"""
    err = D.check_file(pdf)
    if err:
        return [], err
    if not os.path.isfile(toml_path):
        return [], "component.toml missing"
    try:
        with open(toml_path, "rb") as f:
            data = tomllib.load(f)
    except (tomllib.TOMLDecodeError, OSError) as e:
        return [], "component.toml unreadable: %s" % e
    params = data.get("param", {})
    if not params:
        return [], "component.toml has no [param] rows"
    vendor = data.get("part", {}).get("manufacturer", "")
    rc, xhtml, se = D.run(["pdftotext", "-bbox-layout", pdf, "-"])
    if rc != 0 or "<page" not in xhtml:
        return [], "pdftotext failed"
    pages = D.parse_bbox(xhtml)
    rc, info, _ = D.run(["pdfinfo", pdf])
    m = re.search(r"^Pages:\s+(\d+)", info, re.M)
    if rc != 0 or not m or int(m.group(1)) != len(pages):
        return [], "page count mismatch (truncated PDF?)"
    nwords = sum(len(l["words"]) for p in pages for l in p["lines"])
    if nwords < 50:
        return [], "no text layer (scanned PDF?)"
    printed, _off = D.printed_pages(pages)
    inv = {}
    for pdfp, pr in printed.items():
        inv.setdefault(pr, []).append(pdfp)
    rot = D.page_rotations(pdf, len(pages))
    heads = {i: find_headers(p) for i, p in enumerate(pages, 1)}
    if not any(heads.values()):
        return [], "no MIN/TYP/MAX table header found in the PDF (no clean text-layer table to check)"
    ylines = {}
    rows = []
    for key in sorted(params):
        row = params[key]
        if not any(k in row for k in ("min", "typ", "max")):
            rows.append((key, "UNSURE", "row has no min/typ/max number"))
            continue
        why = row_conventions(row)
        if why:
            rows.append((key, "UNSURE", why))
            continue
        if not vendor.startswith(TESTED_VENDORS):
            rows.append((key, "UNSURE", "vendor %r not in the tested set" % vendor))
            continue
        pn = cite_page(row.get("cite"))
        if pn is None or len(inv.get(pn, [])) != 1:
            rows.append((key, "UNSURE", "cite has no usable printed page number"))
            continue
        pg = inv[pn][0]
        if rot.get(pg, 0):
            rows.append((key, "UNSURE", "rotated page"))
            continue
        sym = row.get("symbol", "")
        if not sym:
            rows.append((key, "UNSURE", "row has no symbol to locate it"))
            continue
        if not heads[pg]:
            rows.append((key, "UNSURE", "no MIN/TYP/MAX header on the cited page"))
            continue
        if pg not in ylines:
            ylines[pg] = y_lines(pages[pg - 1])
        rows.append((key,) + one_row(row, sym, ylines[pg], heads[pg]))
    return rows, None


def head_for(h_list, y):
    above = [h for h in h_list if h["y1"] < y]
    return above[-1] if above else None


def sym_at(lab, start):
    """Join touching words from lab[start] (subscripts are separate touching words): 'V' + 'TMR(F)' -> 'VTMR(F)'."""
    t, x1 = "", None
    for w in lab[start:]:
        if x1 is not None and w[0] - x1 > 3:
            break
        t += norm_minus(w[4])
        x1 = w[2]
    return re.sub(r"\s+", "", t)


def line_symbol_x(lab, h):
    """x0 of the word where this line's symbol starts: the first label word, or a word under a Symbol header."""
    out = [(0, lab[0][0])]
    for i, w in enumerate(lab):
        if any(w[0] < b + 8 and w[2] > a - 8 for a, b in h["sym"]):
            out.append((i, w[0]))
    return out


def matching_rows(sym, lines, hlist):
    want = re.sub(r"\s+", "", norm_minus(sym))
    cands = []
    for i, ln in enumerate(lines):
        h = head_for(hlist, ln["ymid"])
        if h is None:
            continue
        lab, cells, unit, bad = split_line(ln, h)
        if not lab:
            continue
        if any(sym_at(lab, k) == want for k, _x in line_symbol_x(lab, h)):
            cands.append((i, ln, h))
    return cands


def locate_row_bbox(page, sym):
    """Return a conservative PDF-point crop box for one isolated symbol row, else None."""
    lines = y_lines(page)
    headers = find_headers(page)
    cands = matching_rows(sym, lines, headers)
    if len(cands) != 1:
        return None
    i, ln, h = cands[0]
    lab, cells, unit, bad = split_line(ln, h)
    values, reason = parse_cells(cells)
    if bad or reason or not any(value is not None for value in values.values()):
        return None
    pitch = (ln["y1"] - ln["y0"]) * 1.7
    sx = [x for _k, x in line_symbol_x(lab, h)]
    top = ln["y0"] - 4
    crop_words = list(ln["words"])
    if 0 <= ln["ymid"] - h["y1"] <= 55:
        top = min(top, h["y0"] - 3)
        header_y = (h["y0"] + h["y1"]) / 2
        crop_words.extend(
            word for line in page["lines"] for word in line["words"]
            if abs((word[1] + word[3]) / 2 - header_y) < 3
        )
    for j in (i - 1, i + 1):
        if 0 <= j < len(lines):
            other = lines[j]
            if abs(other["ymid"] - ln["ymid"]) <= pitch and head_for(headers, other["ymid"]) is h:
                olab, ocells, ounit, _obad = split_line(other, h)
                if olab and any(abs(olab[0][0] - x) < 6 for x in sx):
                    continue
                oval, owhy = parse_cells(ocells)
                if owhy or any(value is not None for value in (oval or {}).values()) or olab or ounit:
                    return None
    x0 = max(0.0, min(word[0] for word in crop_words) - 4)
    x1 = min(page["w"], max(word[2] for word in crop_words) + 4)
    return [x0, max(0.0, top), x1, min(page["h"], ln["y1"] + 4)]


def locate_evidence_bboxes(page, row, cite):
    """Find visual evidence regions from the cited row label, symbol, or name; never compare values."""
    lines = y_lines(page)
    headers = find_headers(page)
    symbol = re.sub(r"[^a-z0-9]", "", norm_minus(str(row.get("symbol", ""))).lower())
    stopwords = {"a", "and", "at", "for", "of", "on", "per", "pins", "row", "the", "to", "value"}
    labels = [
        set(re.findall(r"[a-z0-9]+", str(text).lower()))
        for text in (row.get("name", ""), (cite or "").rsplit(",", 1)[-1])
    ]
    labels = [{word for word in words if len(word) > 1 and word not in stopwords and not word.isdigit()}
              for words in labels]
    candidates = []
    for i, line in enumerate(lines):
        text = " ".join(word[4] for word in line["words"])
        normalized = re.sub(r"[^a-z0-9]", "", norm_minus(text).lower())
        words = set(re.findall(r"[a-z0-9]+", text.lower()))
        name_score = len(labels[0] & words) / len(labels[0]) if labels[0] else 0
        cite_score = len(labels[1] & words) / len(labels[1]) if labels[1] else 0
        symbol_match = bool(symbol and symbol in normalized)
        if symbol_match or name_score >= 0.6 or cite_score >= 0.6:
            candidates.append((i, line, int(symbol_match) * 10 + name_score * 3 + cite_score * 4))
    if not candidates:
        return []
    best = max(item[2] for item in candidates)
    matches = [item for item in candidates if item[2] >= best - 1]
    boxes = []
    for i, line, _score in matches:
        included = [line]
        for j in (i - 1, i + 1):
            if 0 <= j < len(lines) and abs(lines[j]["ymid"] - line["ymid"]) <= 24:
                included.append(lines[j])
        crop_words = [word for item in included for word in item["words"]]
        header = head_for(headers, line["ymid"])
        top = line["y0"] - 4
        if header and 0 <= line["ymid"] - header["y1"] <= 55:
            top = min(top, header["y0"] - 3)
            header_y = (header["y0"] + header["y1"]) / 2
            crop_words.extend(
                word for text_line in page["lines"] for word in text_line["words"]
                if abs((word[1] + word[3]) / 2 - header_y) < 3
            )
        box = [
            max(0.0, min(word[0] for word in crop_words) - 4),
            max(0.0, top),
            min(page["w"], max(word[2] for word in crop_words) + 4),
            min(page["h"], max(item["y1"] for item in included) + 4),
        ]
        if not any(abs(box[1] - old[1]) < 8 and abs(box[3] - old[3]) < 8 for old in boxes):
            boxes.append(box)
    return boxes


def one_row(row, sym, lines, hlist):
    cands = matching_rows(sym, lines, hlist)
    if not cands:
        return "UNSURE", "symbol not found as the first/Symbol-column word of any table line"
    if len(cands) > 1:
        return "UNSURE", "symbol found on %d table lines (several conditions/temperatures)" % len(cands)
    i, ln, h = cands[0]
    lab, cells, unit, bad = split_line(ln, h)
    if bad:
        return "UNSURE", "a word sits between columns"
    vals, why = parse_cells(cells)
    if why:
        return "UNSURE", why
    if all(v is None for v in vals.values()):
        return "UNSURE", "symbol line carries no numbers (multi-line row)"
    # continuation lines directly above/below: a neighbour that does not start with its own symbol (a word at this
    # line's symbol x) is a wrapped name/condition or a sub-row of this row
    pitch = (ln["y1"] - ln["y0"]) * 1.7
    sx = [x for _k, x in line_symbol_x(lab, h)]
    for j in (i - 1, i + 1):
        if 0 <= j < len(lines):
            o = lines[j]
            if abs(o["ymid"] - ln["ymid"]) <= pitch and head_for(hlist, o["ymid"]) is h:
                olab, ocells, ounit, obad = split_line(o, h)
                if olab and any(abs(olab[0][0] - x) < 6 for x in sx):
                    continue  # a separate row of its own
                ov, owhy = parse_cells(ocells)
                if owhy or any(v is not None for v in (ov or {}).values()) or olab or ounit:
                    return "UNSURE", "adjacent line without its own symbol (multi-line name/conditions or sub-row)"
    if not unit:
        return "UNSURE", "no unit cell on the value line"
    uw = [unit[0]]  # the unit cell: the first word right of MAX plus touching words (conditions text follows)
    for w in unit[1:]:
        if w[0] - uw[-1][2] > 4:
            break
        uw.append(w)
    pu = norm_unit("".join(w[4] for w in uw))
    cu = norm_unit(row["unit"])
    committed = {k: (float(row[k]) if k in row else None) for k in ("min", "typ", "max")}
    # presence: a committed value missing from the line may sit on a wrapped line -> UNSURE, not DISAGREE
    if any(committed[k] is not None and vals[k] is None for k in committed):
        return "UNSURE", "a committed value is not on the symbol line"
    if pu != cu:
        return "UNSURE", "printed unit differs from committed unit after normalisation"
    for k in committed:
        if committed[k] is not None and abs(committed[k] - vals[k]) > 1e-9 * max(1.0, abs(vals[k])):
            pset = sorted(v for v in vals.values() if v is not None)
            cset = sorted(v for v in committed.values() if v is not None)
            if pset == cset:
                return "UNSURE", "same numbers in different columns (sign/ordering convention)"
            return "DISAGREE", "column %s differs: table prints %s, committed %s (CHECK ONLY, adjudicate on the page image)" % (
                k.upper(), fmtnum(vals[k]), fmtnum(committed[k]))
    for k in committed:
        if committed[k] is None and vals[k] is not None:
            return "DISAGREE", "table prints a %s number %s that the committed row lacks (CHECK ONLY)" % (k.upper(), fmtnum(vals[k]))
    return "AGREE", "one clean line; min/typ/max and unit equal"


def fmtnum(x):
    return ("%.6g" % x)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2 or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv and argv[0] in ("-h", "--help") else 1
    rows, fatal = check_rows(argv[0], argv[1])
    c = {"AGREE": 0, "DISAGREE": 0, "UNSURE": 0, "FAIL": 0}
    print("# table_xcheck: CROSS-CHECK ONLY, never a source of values for component.toml")
    for key, st, why in rows:
        c[st] += 1
        print("%s: %s %s" % (key, st, why))
    if fatal:
        c["FAIL"] += 1
        print("FAIL: %s" % fatal)
    print("summary: AGREE=%d DISAGREE=%d UNSURE=%d FAIL=%d" % (c["AGREE"], c["DISAGREE"], c["UNSURE"], c["FAIL"]))
    return 1 if c["FAIL"] else (2 if c["DISAGREE"] else 0)


if __name__ == "__main__":
    sys.exit(main())
