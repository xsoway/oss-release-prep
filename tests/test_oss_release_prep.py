from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run_script(name: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(SCRIPTS / name), *args], text=True, capture_output=True, check=False)


class OSSReleasePrepTests(unittest.TestCase):
    def test_package_contract_passes(self) -> None:
        result = run_script("validate_skill_package.py", str(ROOT))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS: oss-release-prep package contract", result.stdout)

    def test_required_readme_files_exist(self) -> None:
        self.assertTrue((ROOT / "README.md").is_file())
        self.assertTrue((ROOT / "README.zh-CN.md").is_file())

    def test_bilingual_switch_links_cross_reference(self) -> None:
        en = (ROOT / "README.md").read_text(encoding="utf-8")
        zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        self.assertIn("README.zh-CN.md", en)
        self.assertIn("README.md", zh)

    def test_three_eval_cases_present(self) -> None:
        cases = ROOT / "evals" / "cases"
        for case in ("basic-success.yaml", "edge-incomplete-input.yaml", "edge-scope-boundary.yaml"):
            self.assertTrue((cases / case).is_file(), f"missing case {case}")


if __name__ == "__main__":
    unittest.main()