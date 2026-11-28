"""tools/check_stamps.py: new human stamps in a PR must name the PR author (structural check on real git repos)."""
import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_stamps as C  # noqa: E402

STAMP = "2026-11-20 page-image ds_review 0123456789ab row ba9876543210"
BOB, AL = f"human:bob {STAMP}", f"human:alice {STAMP}"
X = "components/Acme/X/component.toml"
BASE = '[param.a]\ncite = "DS p.1"\nvalue = 1\n'
G = ["git", "-c", "user.name=t", "-c", "user.email=t@example.com", "-c", "commit.gpgsign=false"]


class Repo(unittest.TestCase):
    def setUp(self):
        self._t = None
        self.fresh()

    def fresh(self):
        """A new empty git repo (each subcase starts clean)."""
        if self._t:
            self._t.cleanup()
        self._t = tempfile.TemporaryDirectory()
        self.r = Path(self._t.name)
        subprocess.run(G + ["init", "-q"], cwd=self.r, check=True)

    def tearDown(self):
        self._t.cleanup()

    def commit(self, files, rm=()):
        for p in rm:
            subprocess.run(G + ["rm", "-q", p], cwd=self.r, check=True)
        for p, t in files.items():
            f = self.r / p
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(t.encode())
        subprocess.run(G + ["add", "-A"], cwd=self.r, check=True)
        subprocess.run(G + ["commit", "-qm", "c", "--allow-empty"], cwd=self.r, check=True)
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.r, capture_output=True, text=True).stdout.strip()

    def run_c(self, base_files, head_files, rm=(), author="alice"):
        base = self.commit(base_files)
        self.commit(head_files, rm)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = C.main(["--root", str(self.r), "--author", author, "--base", base])
        return rc, buf.getvalue().strip()

    def flagged(self, base_files, head_files, rm=(), want="names bob"):
        rc, out = self.run_c(base_files, head_files, rm)
        self.assertEqual(rc, 1, out)
        self.assertIn(want, out)
        return out

    def test_match_mismatch_case(self):
        rc, out = self.run_c({X: BASE}, {X: BASE + f'verified = "{AL}"\n'})
        self.assertEqual(rc, 0, out)
        self.fresh()
        self.assertEqual(self.run_c({X: BASE}, {X: BASE + f'verified = "{AL}"\n'}, author="Alice")[0], 0)
        self.fresh()
        out = self.flagged({X: BASE}, {X: BASE + f'verified = "{BOB}"\n'})
        self.assertEqual(out, f"{X}:4: human stamp names bob, but the PR author is alice")

    def test_pinout_stamp_names_the_author_like_a_row_stamp(self):
        pin = lambda who: f'[pinout]\nverified = "human:{who} 2026-11-20 page-image pinout 0123456789ab pins ba9876543210"\n'  # noqa: E731
        self.flagged({X: BASE}, {X: BASE + pin("bob")})
        self.fresh()
        self.assertEqual(self.run_c({X: BASE}, {X: BASE + pin("alice")})[0], 0)
        self.fresh()
        self.flagged({X: BASE + pin("alice")}, {X: BASE + pin("bob")})  # a changed pinout stamp
        self.fresh()
        self.assertEqual(self.run_c({X: BASE + pin("bob")}, {X: BASE + pin("bob") + "# x\n"})[0], 0)  # unchanged

    def test_preexisting_and_removed_stamps_ignored(self):
        rc, out = self.run_c({X: BASE + f'verified = "{BOB}"\n'}, {X: BASE + f'verified = "{BOB}"\nnote = "x"\n'})
        self.assertEqual(rc, 0, out)
        self.fresh()
        rc, out = self.run_c({X: BASE + f'verified = "{BOB}"\n'}, {X: BASE})
        self.assertEqual(rc, 0, out)

    def test_machine_stamp_and_non_human_strings_ignored(self):
        rc, out = self.run_c({X: BASE}, {X: BASE + 'verified = "sonnet-audit 2026-11-20 x"\nnote = "a human: alice"\n'
                                         f'cite2 = """\nverified = "{BOB}"\n"""\n'})  # multi-line string: not a stamp
        self.assertEqual(rc, 0, out)

    def test_inline_tables_quoted_dotted_and_escaped_keys(self):
        for head in (BASE.replace("value = 1", f'value = 1\nx = {{ verified = "{BOB}" }}'),
                     f'param.a = {{ cite = "DS p.1", value = 1, verified = "{BOB}" }}\n',
                     f'param.b.verified = "{BOB}"\n' + BASE,  # dotted key
                     BASE + f'"verified" = "{BOB}"\n',
                     BASE + f'"\\u0076erified" = "{BOB}"\n',
                     BASE + f"verified   =   '{BOB}'\n",
                     f'[param.a]\nverified = "\\u0068uman:bob {STAMP}"\n'):
            with self.subTest(head=head):
                self.fresh()
                self.flagged({X: BASE}, {X: head})

    def test_gitattributes_cannot_hide(self):
        for attr in ("components/**/component.toml -diff\n", "components/** binary\n"):
            with self.subTest(attr=attr):
                self.fresh()
                self.flagged({X: BASE, ".gitattributes": ""}, {".gitattributes": attr, X: BASE + f'verified = "{BOB}"\n'})

    def test_rename_new_file_and_moved_stamp(self):
        z = "components/Acme/Z/component.toml"
        self.assertIn(z, self.flagged({X: BASE}, {z: BASE + f'verified = "{BOB}"\n'}, rm=[X]))
        self.fresh()
        self.flagged({X: BASE}, {"components/Acme/New/component.toml": f'[param.x]\ncite = "DS"\nverified = "{BOB}"\n'})
        self.fresh()
        out = self.flagged({X: BASE + f'verified = "{BOB}"\n[param.b]\ncite = "DS p.2"\n'},
                           {X: BASE + f'[param.b]\ncite = "DS p.2"\nverified = "{BOB}"\n'})
        self.assertIn(":6:", out)

    def test_crlf_lone_cr_tab_and_malformed(self):
        self.flagged({X: BASE}, {X: (BASE + f'verified = "{BOB}"\n').replace("\n", "\r\n")})
        self.fresh()
        rc, out = self.run_c({X: BASE}, {X: BASE.replace("value = 1\n", f'value = 1\rverified = "{BOB}"\n')})
        self.assertEqual(rc, 1, out)
        self.assertIn("not valid TOML at HEAD", out)  # fails closed
        for bad in (f"human:alice\t{STAMP}", "human:", f"human:-alice {STAMP}", "human:alice"):
            with self.subTest(bad=bad):
                self.fresh()
                self.flagged({X: BASE}, {X: BASE + f'verified = "{bad}"\n'}, want="malformed human stamp")

    def test_outside_components_and_git_errors(self):
        rc, out = self.run_c({X: BASE}, {"other/component.toml": f'verified = "{BOB}"\n'})
        self.assertEqual(rc, 0, out)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(C.main(["--root", str(self.r), "--author", "alice", "--base", "nope"]), 1)
        self.assertIn("FAIL", buf.getvalue())
        with self.assertRaises(SystemExit):
            with contextlib.redirect_stderr(io.StringIO()):
                C.main(["--author", "alice"])  # --base is required

    def test_human_values_walks_everything(self):
        doc = {"param": {"a": {"verified": BOB, "l": [{"x": AL}], "n": "human-ish"}}, "y": "human:q"}
        self.assertEqual(C.human_values(doc), {("param", "a", "verified"): BOB, ("param", "a", "l", 0, "x"): AL,
                                               ("y",): "human:q"})


class VariantsMoves(Repo):
    V = "components/Acme/X/variants.toml"

    def block(self, name, key, stamp=""):
        return f'[variant."{name}".param.{key}]\ncite = "DS p.1"\n' + (f'verified = "{stamp}"\n' if stamp else "")

    def test_a_moved_stamp_is_new_at_its_new_key_path(self):
        self.flagged({self.V: self.block("V1", "a", BOB) + self.block("V1", "b")},
                     {self.V: self.block("V1", "a") + self.block("V1", "b", BOB)})  # bob's stamp moved to b: alice is the author

    def test_a_deleted_stamp_is_ignored(self):
        rc, out = self.run_c({self.V: self.block("V1", "a", BOB)}, {self.V: self.block("V1", "a")})
        self.assertEqual(rc, 0, out)

    def test_a_renamed_variant_is_a_new_stamp(self):
        self.flagged({self.V: self.block("V1", "a", BOB)}, {self.V: self.block("V2", "a", BOB)})

    def test_equation_stamps_in_equations_toml_name_the_author(self):
        eq = "components/Acme/X/equations.toml"
        base = '[equation.f]\ntitle = "t"\n'
        stamp = lambda who: f'verified = "human:{who} 2026-11-28 equation-review X.f hash 0123456789ab"\n'  # noqa: E731
        out = self.flagged({X: BASE, eq: base}, {eq: base + stamp("bob")})
        self.assertIn(f"{eq}:3: human stamp names bob", out)
        self.fresh()
        self.assertEqual(self.run_c({X: BASE, eq: base}, {eq: base + stamp("alice")})[0], 0)
        self.fresh()
        self.flagged({eq: base + stamp("alice")}, {eq: base + stamp("bob")})  # a changed stamp
        self.fresh()
        self.assertEqual(self.run_c({eq: base + stamp("bob")}, {eq: base + stamp("bob") + "# x\n"})[0], 0)  # unchanged
        self.fresh()
        self.assertEqual(self.run_c({eq: base}, {eq: base + 'verified = "machine check"\n'})[0], 0)  # machine stamp ignored


if __name__ == "__main__":
    unittest.main()
