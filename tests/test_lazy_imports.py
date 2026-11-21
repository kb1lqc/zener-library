"""The stamp tools run before CI installs matplotlib: they must import with matplotlib blocked."""

import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# A None entry in sys.modules makes every `import matplotlib` raise ImportError.
BLOCK = "import runpy, sys; sys.modules['matplotlib'] = None; sys.argv = sys.argv[1:]; runpy.run_path(sys.argv[0], run_name='__main__')"


def run_blocked(*args):
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    return subprocess.run([sys.executable, "-c", BLOCK, *args], cwd=ROOT, env=env, capture_output=True, text=True, timeout=60)


class LazyImports(unittest.TestCase):
    def test_block_really_blocks(self):
        p = subprocess.run([sys.executable, "-c", "import sys; sys.modules['matplotlib'] = None; import matplotlib"],
                           capture_output=True, text=True, timeout=60)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("import of matplotlib halted", p.stderr)  # ModuleNotFoundError (an ImportError subclass)

    def test_check_stamps_runs_without_matplotlib(self):
        p = run_blocked("tools/check_stamps.py", "--author", "nobody", "--base", "HEAD", "--head", "HEAD")
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn("check_stamps: OK", p.stdout)
        self.assertNotIn("matplotlib", p.stderr)

    def test_stamp_help_runs_without_matplotlib(self):
        p = run_blocked("tools/stamp.py", "--help")
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn("usage:", p.stdout)

    def test_lib_component_does_not_load_report(self):
        p = subprocess.run([sys.executable, "-c", "import sys; sys.modules['matplotlib'] = None; import lib.component, lib; "
                            "assert 'lib.report' not in sys.modules; print(lib.component.GITHUB_LOGIN)"],
                           cwd=ROOT, capture_output=True, text=True, timeout=60)
        self.assertEqual(p.returncode, 0, p.stderr)

    def test_wca_is_the_function_after_any_import_order(self):
        # lib.wca is both a submodule and a function; `from lib import wca` must give the function even after the
        # submodule was imported (lib.report imports it). Fresh interpreter per order.
        for pre in ("", "import lib.report; ", "import lib.wca; ", "from lib import table; "):
            code = pre + "import lib; from lib import wca, sweep; assert callable(wca) and callable(lib.wca), type(wca)"
            p = subprocess.run([sys.executable, "-c", code], cwd=ROOT, capture_output=True, text=True, timeout=60)
            self.assertEqual(p.returncode, 0, pre + p.stderr)

    def test_package_exports_still_resolve(self):
        import lib
        for name in lib.__all__:
            self.assertTrue(callable(getattr(lib, name)) or isinstance(getattr(lib, name), type), name)
        self.assertIs(lib.load, __import__("lib.component", fromlist=["load"]).load)
        with self.assertRaises(AttributeError):
            lib.no_such_name  # noqa: B018
        from lib import Param, table, verdict, wca  # noqa: F401  (the from-import form callers use)


if __name__ == "__main__":
    unittest.main()
