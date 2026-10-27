"""Regression tests for the validator's actual failure detection."""

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate_package.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.root = Path(self.workspace.name) / "package"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(
            ".git", "__pycache__", "evaluation-runs", "RESEARCH-NOTES.md"))

    def tearDown(self):
        self.workspace.cleanup()

    def test_current_package_passes(self):
        self.assertEqual(VALIDATOR.validate(self.root), [])

    def test_missing_skill_fails(self):
        (self.root / "skills/onboarding-design/SKILL.md").unlink()
        self.assertTrue(any("Missing:" in p for p in VALIDATOR.validate(self.root)))

    def test_broken_relative_link_fails(self):
        with (self.root / "README.md").open("a") as handle:
            handle.write("\n[Missing file](not-a-file.md)\n")
        self.assertTrue(any("Broken relative link" in p for p in VALIDATOR.validate(self.root)))

    def test_escaping_link_fails(self):
        with (self.root / "README.md").open("a") as handle:
            handle.write("\n[Outside](../outside.md)\n")
        self.assertTrue(any("escapes package" in p for p in VALIDATOR.validate(self.root)))

    def test_private_path_fails(self):
        with (self.root / "README.md").open("a") as handle:
            handle.write("\nPrivate " + "/Users/" + "fixture/private-file.md\n")
        self.assertTrue(any("Private absolute path" in p for p in VALIDATOR.validate(self.root)))

    def test_missing_invocation_fails(self):
        path = self.root / "skills/onboarding-design/agents/openai.yaml"
        path.write_text(path.read_text().replace("$onboarding-design", "the tool"))
        self.assertTrue(any("Default prompt" in p for p in VALIDATOR.validate(self.root)))


if __name__ == "__main__":
    unittest.main()
