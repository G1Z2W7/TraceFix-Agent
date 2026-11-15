from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.check_docs import check_repository, normalize_link_target


class CheckDocsTests(unittest.TestCase):
    def test_accepts_existing_local_links_and_remote_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "guide.md").write_text("# Guide\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[Guide](guide.md)\n[Section](#section)\n"
                "[Website](https://example.com)\n",
                encoding="utf-8",
            )

            files, findings = check_repository(root)

            self.assertEqual(2, len(files))
            self.assertEqual([], findings)

    def test_reports_a_broken_local_link(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "[Missing](docs/missing.md)\n", encoding="utf-8"
            )

            _, findings = check_repository(root)

            self.assertEqual(1, len(findings))
            self.assertIn("broken local link", findings[0].message)

    def test_reports_trailing_whitespace_and_tabs_outside_code(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "bad  \n\tbad\n```text\n\tallowed\n```\n", encoding="utf-8"
            )

            _, findings = check_repository(root)
            messages = [finding.message for finding in findings]

            self.assertIn("trailing whitespace", messages)
            self.assertIn("tab outside a code fence", messages)
            self.assertEqual(2, len(findings))

    def test_normalizes_angle_brackets_and_titles(self) -> None:
        self.assertEqual("docs/a file.md", normalize_link_target("<docs/a%20file.md>"))
        self.assertEqual(
            "docs/guide.md", normalize_link_target('docs/guide.md "Guide"')
        )


if __name__ == "__main__":
    unittest.main()
