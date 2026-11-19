import hashlib
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tests" / "fixtures"))
import ds_review_packet as P  # noqa: E402
import phase3b_pdf as fx  # noqa: E402


HEAD = '[part]\nvalue = "X"\nmanufacturer = "Texas Instruments"\n'


def param(key, symbol, unit, cite="DS p.2, 6.5 Electrical Characteristics, row", **values):
    fields = [
        "[param.%s]" % key,
        'name = "%s"' % key,
        'symbol = "%s"' % symbol,
        'kind = "electrical"',
        'scope = "25C"',
        'unit = "%s"' % unit,
        'conditions = ""',
    ]
    if cite is not None:
        fields.append('cite = "%s"' % cite)
    for name, value in values.items():
        fields.append("%s = %s" % (name, value))
    return "\n".join(fields) + "\n"


class TestDatasheetReviewPacket(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(self.tmp, ignore_errors=True))
        self.component_dir = self.tmp / "component"
        self.component_dir.mkdir()
        self.pdf = self.tmp / "datasheet.pdf"
        self.pdf.write_bytes(fx.build_pdf(fx.datasheet_pages()))

    def component(self, *rows):
        path = self.component_dir / "component.toml"
        path.write_text(HEAD + "".join(rows), encoding="utf-8")
        return path

    def packet(self, *rows):
        component = self.component(*rows)
        out = self.tmp / "packet"
        return P.build_packet(self.pdf, component, out), out

    def test_clean_text_match_maps_to_packet_only_status(self):
        packet, out = self.packet(param("vos", "VOS", "uV", typ="10", max="35"))
        row = packet["parameters"][0]
        self.assertEqual(row["status"], "AGREE_TEXT_CHECK")
        self.assertEqual(row["pdf_pages"], [2])
        self.assertEqual(row["printed_pages"], [2])
        self.assertEqual(row["human_review"] if "human_review" in row else packet["human_review"],
                         "NOT_PERFORMED")
        self.assertEqual(row["crop_mode"], "row_crop")
        self.assertFalse(row["full_page"])
        self.assertIsNotNone(row["crop_coordinates"])
        self.assertTrue((out / row["image_path"]).is_file())
        crop = (out / row["image_path"]).read_bytes()
        context = (out / packet["context_images"]["2"]).read_bytes()
        self.assertLess(struct.unpack(">I", crop[20:24])[0], struct.unpack(">I", context[20:24])[0])

    def test_mismatch_stays_disagree_and_not_a_source(self):
        packet, _ = self.packet(param("vos", "VOS", "uV", typ="10", max="36"))
        row = packet["parameters"][0]
        self.assertEqual(row["status"], "DISAGREE")
        self.assertIn("MAX differs", row["reason"])
        self.assertEqual(packet["human_review"], "NOT_PERFORMED")

    def test_missing_cite_is_unsure_and_uses_full_document_fallback(self):
        packet, out = self.packet(param("vos", "VOS", "uV", cite=None, typ="10", max="35"))
        row = packet["parameters"][0]
        self.assertEqual(row["status"], "UNSURE")
        self.assertEqual(row["pdf_pages"], [])
        self.assertEqual(row["crop_mode"], "full_document_fallback")
        self.assertTrue(row["image_paths"])
        self.assertTrue(all((out / path).is_file() for path in row["image_paths"]))

    def test_ambiguous_symbol_remains_unsure(self):
        packet, _ = self.packet(param("iq", "IQ", "mA", typ="1.2", max="2"))
        row = packet["parameters"][0]
        self.assertEqual(row["status"], "UNSURE")
        self.assertIn("several conditions", row["reason"])
        self.assertEqual(row["crop_mode"], "row_crop")
        self.assertTrue(row["crop_coordinates"])

    def test_unmatched_row_uses_table_excerpt(self):
        packet, _ = self.packet(param("unknown", "UNKNOWN", "V", typ="3"))
        row = packet["parameters"][0]
        self.assertEqual(row["crop_mode"], "table_crop")
        self.assertFalse(row["full_page"])
        self.assertTrue(row["crop_coordinates"])

    def test_scanned_pdf_renders_context_but_never_agrees(self):
        self.pdf.write_bytes(fx.build_pdf(fx.datasheet_pages(), scanned=(1, 2, 3, 4)))
        packet, out = self.packet(param("vos", "VOS", "uV", typ="10", max="35"))
        row = packet["parameters"][0]
        self.assertEqual(packet["index_status"], "FAIL")
        self.assertIn("no text layer", packet["index_reason"])
        self.assertEqual(row["status"], "UNSURE")
        self.assertTrue(row["image_paths"])
        self.assertTrue(all((out / path).read_bytes().startswith(b"\x89PNG") for path in row["image_paths"]))

    def test_invalid_component_and_pdf_fail_closed(self):
        bad = self.component_dir / "bad.toml"
        bad.write_text("[param\nbroken", encoding="utf-8")
        with self.assertRaisesRegex(P.PacketError, "unreadable"):
            P.build_packet(self.pdf, bad, self.tmp / "bad-packet")
        self.pdf.write_bytes(b"not a pdf")
        with self.assertRaisesRegex(P.PacketError, "truncated|not a PDF"):
            P.build_packet(self.pdf, self.component(param("vos", "VOS", "uV", typ="10")), self.tmp / "bad-pdf")

    def test_manifest_has_hash_pages_crop_and_relative_markdown_paths(self):
        source = self.component_dir / "component.toml"
        packet, out = self.packet(param("vos", "VOS", "uV", typ="10", max="35"))
        row = packet["parameters"][0]
        manifest = json.loads((out / "manifest.json").read_text())
        self.assertEqual(manifest["pdf_sha256"], hashlib.sha256(self.pdf.read_bytes()).hexdigest())
        for field in ("key", "pdf_sha256", "pdf_pages", "printed_pages", "crop_coordinates",
                      "full_page", "image_path", "crop_mode"):
            self.assertIn(field, row)
        self.assertIsNotNone(row["crop_coordinates"])
        self.assertFalse(row["full_page"])
        review = (out / "github-review.md").read_text()
        issue = (out / "github-issue.md").read_text()
        self.assertIn("![row snippet](evidence/0001-vos.png)", review)
        self.assertIn("typ=10", review)
        self.assertIn("Datasheet snippet", review)
        self.assertNotIn(str(self.tmp), review + issue)
        self.assertIn("Do not redistribute", review)
        self.assertTrue((out / "review.html").is_file())
        self.assertTrue((out / "manifest.json").is_file())
        self.assertFalse((out / "review.json").exists())
        self.assertFalse((out / "review.csv").exists())
        self.assertTrue((out / "coverage.md").is_file())
        self.assertEqual(source.read_text(), HEAD + param("vos", "VOS", "uV", typ="10", max="35"))
        self.assertFalse(list(out.rglob("*.pdf")))

    def test_archive_saves_pending_human_record_and_only_evidence_images(self):
        source = self.component(param("vos", "VOS", "uV", typ="10", max="35"))
        original = source.read_text()
        out = self.tmp / "packet"
        packet = P.build_packet(self.pdf, source, out, archive=True)
        archive = Path(packet["archive_path"])
        manifest = json.loads((archive / "manifest.json").read_text())
        record = (archive / "datasheet-review.md").read_text()

        self.assertEqual(manifest["review_record"]["status"], "PENDING")
        self.assertFalse(manifest["review_record"]["attestation"])
        self.assertIn("Review status: PENDING", record)
        self.assertIn('verification_type = "human_page_image"', record)
        self.assertIn("inside its `[param.<key>]` table in `component.toml`", record)
        self.assertIn("[ ] Confirmed", record)
        self.assertIn("typ=10", record)
        self.assertIn("![snippet](evidence/0001-vos.png)", record)
        self.assertTrue((archive / "evidence/0001-vos.png").is_file())
        self.assertTrue((archive / "context/page-0002.png").is_file())
        self.assertTrue((archive / "coverage.md").is_file())
        self.assertIn("Whole-datasheet sweep", (archive / "coverage.md").read_text())
        self.assertFalse(list(archive.rglob("*.pdf")))
        self.assertEqual(source.read_text(), original)
        self.assertTrue((out / "github-review.md").is_file())

    def test_archive_refuses_to_overwrite_a_prior_record(self):
        source = self.component(param("vos", "VOS", "uV", typ="10", max="35"))
        P.build_packet(self.pdf, source, self.tmp / "first-packet", archive=True)
        with self.assertRaisesRegex(P.PacketError, "archive already exists"):
            P.build_packet(self.pdf, source, self.tmp / "second-packet", archive=True)

    def test_finalize_requires_all_attestations_and_human_stamps(self):
        source = self.component(param("vos", "VOS", "uV", typ="10", max="35"))
        packet = P.build_packet(self.pdf, source, self.tmp / "packet", archive=True)
        archive = Path(packet["archive_path"])
        review = (archive / "datasheet-review.md").read_text()
        review = review.replace("- Reviewer: [enter one-word handle]", "- Reviewer: abrown")
        review = review.replace("- Review date: [enter YYYY-MM-DD]", "- Review date: 2026-11-19")
        review = review.replace("- Attestation: [ ]", "- Attestation: [x]")
        (archive / "datasheet-review.md").write_text(review)
        with self.assertRaisesRegex(P.PacketError, "select exactly one decision"):
            P.finalize_archive(archive)
        manifest = json.loads((archive / "manifest.json").read_text())
        self.assertEqual(manifest["review_record"]["status"], "PENDING")

    def prepare_finalize_archive(self, stamp=True, cover_parameter=True):
        source_text = param("vos", "VOS", "uV", typ="10", max="35")
        if stamp:
            source_text += (
                'verified = "abrown 2026-11-19 human page-image review"\n'
                'verification_type = "human_page_image"\n'
            )
        source = self.component(source_text)
        packet = P.build_packet(self.pdf, source, self.tmp / "packet", archive=True)
        archive = Path(packet["archive_path"])

        review_path = archive / "datasheet-review.md"
        review_lines = review_path.read_text().splitlines()
        for index, line in enumerate(review_lines):
            if line.startswith("- Reviewer:"):
                review_lines[index] = "- Reviewer: abrown"
            elif line.startswith("- Review date:"):
                review_lines[index] = "- Review date: 2026-11-19"
            elif line.startswith("- Attestation:"):
                review_lines[index] = line.replace("[ ]", "[x]", 1)
            elif line.startswith("| vos |"):
                cells = P.markdown_cells(line)
                cells[4] = "[x] Confirmed<br>[ ] Needs correction<br>[ ] Unable to verify"
                review_lines[index] = "| " + " | ".join(cells) + " |"
        review_path.write_text("\n".join(review_lines) + "\n")

        coverage_path = archive / "coverage.md"
        coverage_lines = coverage_path.read_text().splitlines()
        coverage_items = packet["coverage_items"]
        first_extractable = coverage_items[0]["key"]
        for index, line in enumerate(coverage_lines):
            if line.startswith("- Whole-datasheet sweep:"):
                coverage_lines[index] = line.replace("[ ]", "[x]", 1)
            cells = P.markdown_cells(line)
            if len(cells) == 6 and cells[0] in {item["key"] for item in coverage_items}:
                if cells[0] == first_extractable and cover_parameter:
                    cells[4] = "[x] Extracted<br>[ ] Not applicable"
                    cells[5] = "keys: vos"
                else:
                    cells[4] = "[ ] Extracted<br>[x] Not applicable"
                    cells[5] = "reason: no applicable rows in this test fixture"
                coverage_lines[index] = "| " + " | ".join(cells) + " |"
        coverage_path.write_text("\n".join(coverage_lines) + "\n")
        return archive, source, review_path

    def test_finalize_success_updates_status_only_after_valid_review(self):
        archive, _, review_path = self.prepare_finalize_archive()
        result = P.finalize_archive(archive)
        self.assertEqual(result["status"], "HUMAN-REVIEWED")
        manifest = json.loads((archive / "manifest.json").read_text())
        self.assertEqual(manifest["human_review"], "HUMAN_REVIEWED")
        self.assertEqual(manifest["review_record"]["reviewer"], "abrown")
        self.assertIn("coverage_decisions", manifest["review_record"])
        self.assertIn("HUMAN-REVIEWED by `abrown`", review_path.read_text())

    def test_finalize_rejects_uncovered_parameter(self):
        archive, _, _ = self.prepare_finalize_archive(cover_parameter=False)
        with self.assertRaisesRegex(P.PacketError, "does not account for parameter keys"):
            P.finalize_archive(archive)
        manifest = json.loads((archive / "manifest.json").read_text())
        self.assertEqual(manifest["review_record"]["status"], "PENDING")

    def test_finalize_rejects_confirmed_row_without_human_stamp(self):
        archive, _, _ = self.prepare_finalize_archive(stamp=False)
        with self.assertRaisesRegex(P.PacketError, "lacks this reviewer's dated"):
            P.finalize_archive(archive)
        manifest = json.loads((archive / "manifest.json").read_text())
        self.assertEqual(manifest["review_record"]["status"], "PENDING")

    def test_finalize_rejects_stale_component_values(self):
        archive, source, _ = self.prepare_finalize_archive()
        source.write_text(source.read_text().replace("typ = 10", "typ = 11"))
        with self.assertRaisesRegex(P.PacketError, "values or cite changed"):
            P.finalize_archive(archive)
        manifest = json.loads((archive / "manifest.json").read_text())
        self.assertEqual(manifest["review_record"]["status"], "PENDING")

    def test_output_must_be_outside_component_and_empty(self):
        component = self.component(param("vos", "VOS", "uV", typ="10"))
        with self.assertRaisesRegex(P.PacketError, "outside the component"):
            P.build_packet(self.pdf, component, self.component_dir / "packet")
        out = self.tmp / "occupied"
        out.mkdir()
        (out / "keep.txt").write_text("keep")
        with self.assertRaisesRegex(P.PacketError, "must be empty"):
            P.build_packet(self.pdf, component, out)

    def test_cli_writes_packet_and_returns_disagree_code(self):
        self.component(param("vos", "VOS", "uV", typ="10", max="36"))
        out = self.tmp / "cli-packet"
        result = subprocess.run([
            sys.executable, str(ROOT / "tools" / "ds_review_packet.py"),
            str(self.pdf), str(self.component_dir), "--out", str(out), "--archive",
        ], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("DISAGREE=1", result.stdout)
        self.assertIn("review record:", result.stdout)
        self.assertTrue((out / "github-review.md").is_file())


if __name__ == "__main__":
    unittest.main()
