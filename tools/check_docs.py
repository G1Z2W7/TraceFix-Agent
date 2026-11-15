"""Check repository Markdown files without third-party dependencies."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


IGNORED_DIRECTORIES = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "build",
    "dist",
    "htmlcov",
    "venv",
}

MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
REMOTE_PREFIXES = ("http://", "https://", "mailto:")


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    message: str

    def display(self, root: Path) -> str:
        relative_path = self.path.relative_to(root).as_posix()
        return f"{relative_path}:{self.line}: {self.message}"


def iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in IGNORED_DIRECTORIES for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def normalize_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif ' "' in target:
        target = target.split(' "', maxsplit=1)[0]
    elif " '" in target:
        target = target.split(" '", maxsplit=1)[0]

    target = unquote(target)
    if not target or target.startswith("#") or target.startswith(REMOTE_PREFIXES):
        return None

    return target.split("#", maxsplit=1)[0].split("?", maxsplit=1)[0]


def resolve_link(root: Path, source: Path, target: str) -> Path:
    if target.startswith("/"):
        return root / target.lstrip("/")
    return source.parent / target


def check_markdown_file(root: Path, path: Path) -> list[Finding]:
    findings: list[Finding] = []
    in_code_fence = False

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line != line.rstrip():
            findings.append(Finding(path, line_number, "trailing whitespace"))

        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_fence = not in_code_fence
            continue

        if in_code_fence:
            continue

        if "\t" in line:
            findings.append(Finding(path, line_number, "tab outside a code fence"))

        for match in MARKDOWN_LINK.finditer(line):
            target = normalize_link_target(match.group(1))
            if target is None:
                continue

            resolved = resolve_link(root, path, target)
            if not resolved.exists():
                findings.append(
                    Finding(path, line_number, f"broken local link: {match.group(1)}")
                )

    return findings


def check_repository(root: Path) -> tuple[list[Path], list[Finding]]:
    files = iter_markdown_files(root)
    findings: list[Finding] = []
    for path in files:
        findings.extend(check_markdown_file(root, path))
    return files, findings


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    files, findings = check_repository(root)

    if findings:
        for finding in findings:
            print(finding.display(root))
        print(f"Documentation checks failed with {len(findings)} finding(s).")
        return 1

    print(f"Documentation checks passed for {len(files)} Markdown file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
