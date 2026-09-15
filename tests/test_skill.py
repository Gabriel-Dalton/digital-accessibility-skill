"""Checks that the skill is valid, internally consistent and cites real criteria.

Run: python tests/test_skill.py
"""
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "digital-accessibility"
SKILL_MD = SKILL_DIR / "SKILL.md"
REFERENCES = sorted((SKILL_DIR / "references").glob("*.md"))

# Every Level A and AA success criterion in WCAG 2.2. 4.1.1 is listed because
# the files mention it as removed; the test below checks that no file treats it
# as a live criterion.
WCAG_22_A_AA = {
    "1.1.1", "1.2.1", "1.2.2", "1.2.3", "1.2.4", "1.2.5",
    "1.3.1", "1.3.2", "1.3.3", "1.3.4", "1.3.5",
    "1.4.1", "1.4.2", "1.4.3", "1.4.4", "1.4.5", "1.4.10", "1.4.11", "1.4.12", "1.4.13",
    "2.1.1", "2.1.2", "2.1.4", "2.2.1", "2.2.2", "2.3.1",
    "2.4.1", "2.4.2", "2.4.3", "2.4.4", "2.4.5", "2.4.6", "2.4.7", "2.4.11",
    "2.5.1", "2.5.2", "2.5.3", "2.5.4", "2.5.7", "2.5.8",
    "3.1.1", "3.1.2", "3.2.1", "3.2.2", "3.2.3", "3.2.4", "3.2.6",
    "3.3.1", "3.3.2", "3.3.3", "3.3.4", "3.3.7", "3.3.8",
    "4.1.2", "4.1.3",
}
WCAG_22_AAA = {
    "1.2.6", "1.2.7", "1.2.8", "1.2.9", "1.3.6", "1.4.6", "1.4.7", "1.4.8", "1.4.9",
    "2.1.3", "2.2.3", "2.2.4", "2.2.5", "2.2.6", "2.3.2", "2.3.3",
    "2.4.8", "2.4.9", "2.4.10", "2.4.12", "2.4.13", "2.5.5", "2.5.6",
    "3.1.3", "3.1.4", "3.1.5", "3.1.6", "3.2.5", "3.3.6", "3.3.9",
}
REMOVED = {"4.1.1"}

CRITERION = re.compile(r"\b([1-4])\.(\d)\.(\d{1,2})\b")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def without_versions(text: str) -> str:
    """Drop version strings (v3.2.1, version: "1.0.0", 91.20.902-style numbers) that look like criteria."""
    text = re.sub(r"\bv\d+\.\d+\.\d+\b", "", text)
    text = re.sub(r"version:\s*\"[^\"]+\"", "", text)
    text = re.sub(r"\b\d+\.\d+\.\d+\.\d+\b", "", text)
    return text


class Frontmatter(unittest.TestCase):
    def test_reference_validator_passes(self):
        result = subprocess.run(
            ["uvx", "--from", "skills-ref", "agentskills", "validate", str(SKILL_DIR)],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_name_matches_directory(self):
        match = re.search(r"^name:\s*(\S+)", read(SKILL_MD), re.M)
        self.assertEqual(match.group(1), SKILL_DIR.name)

    def test_description_length(self):
        text = read(SKILL_MD)
        block = text.split("---")[1]
        desc = re.search(r"^description:\s*(.+)$", block, re.M).group(1)
        self.assertLessEqual(len(desc), 1024)
        self.assertGreater(len(desc), 50)


class Layout(unittest.TestCase):
    def test_skill_md_under_500_lines(self):
        self.assertLess(len(read(SKILL_MD).splitlines()), 500)

    def test_every_referenced_file_exists(self):
        refs = set(re.findall(r"`(references/[\w.-]+\.md)`", read(SKILL_MD)))
        self.assertTrue(refs, "SKILL.md references no files")
        for ref in refs:
            self.assertTrue((SKILL_DIR / ref).is_file(), ref)

    def test_every_reference_file_is_mentioned_in_skill_md(self):
        text = read(SKILL_MD)
        for path in REFERENCES:
            self.assertIn(f"references/{path.name}", text, path.name)

    def test_no_product_branding_in_prose(self):
        # The skill is written for any agent that reads the Agent Skills format.
        for path in [SKILL_MD, *REFERENCES, ROOT / "README.md"]:
            text = read(path)
            self.assertNotRegex(text, r"\bClaude skill\b", path.name)
            self.assertNotRegex(text, r"helps Claude", path.name)


class Criteria(unittest.TestCase):
    def cited(self, text: str):
        return {".".join(m) for m in CRITERION.findall(text)}

    def test_all_cited_criteria_are_real(self):
        known = WCAG_22_A_AA | WCAG_22_AAA | REMOVED
        for path in [SKILL_MD, *REFERENCES]:
            unknown = self.cited(without_versions(read(path))) - known
            self.assertFalse(unknown, f"{path.name}: unknown criteria {sorted(unknown)}")

    def test_checklist_covers_every_a_and_aa_criterion(self):
        text = read(SKILL_DIR / "references" / "wcag-checklist.md")
        missing = WCAG_22_A_AA - self.cited(text)
        self.assertFalse(missing, f"checklist missing {sorted(missing)}")

    def test_removed_criterion_is_flagged_as_removed(self):
        for path in [SKILL_MD, *REFERENCES]:
            for line in without_versions(read(path)).splitlines():
                if "4.1.1" in line:
                    self.assertRegex(line, r"removed|no longer|Parsing", f"{path.name}: {line}")


class Evidence(unittest.TestCase):
    def test_legal_files_carry_a_check_date(self):
        for name in ["SKILL.md", "references/legal-frameworks.md", "references/wcag-checklist.md",
                     "references/testing-guide.md"]:
            text = read(SKILL_DIR / name)
            self.assertRegex(text, r"(checked|verified|Verified) (on )?\d{4}-\d{2}-\d{2}", name)

    def test_every_legal_section_has_a_source(self):
        text = read(SKILL_DIR / "references" / "legal-frameworks.md")
        sections = re.split(r"^## ", text, flags=re.M)[1:]
        for section in sections:
            title = section.splitlines()[0]
            if title.startswith("Contents"):
                continue
            self.assertIn("https://", section, f"no source in section: {title}")

    def test_no_em_dashes(self):
        for path in [SKILL_MD, *REFERENCES, ROOT / "README.md"]:
            self.assertNotIn("—", read(path), path.name)


if __name__ == "__main__":
    sys.exit(unittest.main(verbosity=2).result.wasSuccessful() is False)
