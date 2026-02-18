#!/usr/bin/env python3
"""Extract human-readable text content from the local www.heigl-zt.at repository.

Recommended use:
  python3 scripts/extract_heigl_repo_text.py \
    --repo /home/seb/code/www.heigl-zt.at \
    --output references/heigl-zt-corpus.md \
    --include-dir src/pages \
    --include-dir src/components \
    --include-dir src/layouts
"""

from __future__ import annotations

import argparse
import html
import re
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_EXTENSIONS = {".astro", ".md", ".mdx", ".html", ".txt"}
EXCLUDE_DIRS = {".git", "node_modules", "dist", ".astro", "coverage", "build"}


def strip_frontmatter(text: str) -> str:
    # YAML frontmatter (--- ... ---) at the top
    return re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)


def normalize_text(raw: str) -> str:
    text = strip_frontmatter(raw)

    # Remove script/style blocks
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.IGNORECASE | re.DOTALL)

    # Remove MDX/JSX import/export lines and code fences
    text = re.sub(r"^\s*(import|export)\s+.+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)

    # Remove Astro/JS template expressions and comments
    text = re.sub(r"\{[^{}]*\}", " ", text)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)

    # Convert HTML tags to spaces
    text = re.sub(r"<[^>]+>", " ", text)

    # Decode HTML entities
    text = html.unescape(text)

    # Keep markdown headings/list markers readable while removing noisy punctuation bursts
    text = re.sub(r"[\t\r\f\v]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Collapse repeated spaces
    text = re.sub(r" {2,}", " ", text)

    # Strip lines and remove empty/noise lines
    cleaned_lines: list[str] = []
    for line in text.splitlines():
        candidate = line.strip()
        if not candidate:
            continue
        # Skip pure punctuation/noise lines
        if re.fullmatch(r"[\W_]+", candidate):
            continue
        cleaned_lines.append(candidate)

    return "\n".join(cleaned_lines).strip()


def discover_files(repo_root: Path, include_dirs: list[str], extensions: set[str]) -> list[Path]:
    files: list[Path] = []

    if include_dirs:
        roots = [repo_root / p for p in include_dirs]
    else:
        roots = [repo_root]

    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue

            # Excluded directories
            if any(part in EXCLUDE_DIRS for part in path.parts):
                continue

            if path.suffix.lower() not in extensions:
                continue

            files.append(path)

    return sorted(set(files))


def build_output(repo_root: Path, files: list[Path]) -> tuple[str, int]:
    sections: list[str] = []
    kept = 0

    for path in files:
        raw = path.read_text(encoding="utf-8", errors="ignore")
        cleaned = normalize_text(raw)
        if len(cleaned) < 25:
            continue

        rel = path.relative_to(repo_root)
        sections.append(f"## {rel}\n\n{cleaned}\n")
        kept += 1

    header = [
        "# Heigl ZT Text Corpus",
        "",
        f"- Quelle (Repo): `{repo_root}`",
        f"- Generiert: {datetime.now(timezone.utc).isoformat()}",
        f"- Dateien enthalten: {kept}",
        "",
        "> Automatisch erzeugt aus dem lokalen Repository. Für Content-Analyse und Content-Entwürfe.",
        "",
    ]

    return "\n".join(header) + "\n".join(sections), kept


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract text corpus from local www.heigl-zt.at repository")
    parser.add_argument("--repo", required=True, help="Path to repository root")
    parser.add_argument(
        "--output",
        required=True,
        help="Output markdown file path (absolute or relative to current working directory)",
    )
    parser.add_argument(
        "--include-dir",
        action="append",
        default=[],
        help="Optional directory inside repo to include (repeatable). If omitted, scans full repo with exclusions.",
    )
    parser.add_argument(
        "--ext",
        action="append",
        default=[],
        help="Optional file extension to include, e.g. --ext .astro --ext .mdx",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    repo_root = Path(args.repo).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    if not repo_root.exists() or not repo_root.is_dir():
        raise SystemExit(f"Repo path not found or not a directory: {repo_root}")

    extensions = {e if e.startswith(".") else f".{e}" for e in args.ext} if args.ext else DEFAULT_EXTENSIONS

    files = discover_files(repo_root, args.include_dir, extensions)
    if not files:
        raise SystemExit("No matching files found with current filters.")

    content, kept = build_output(repo_root, files)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")

    print(f"Scanned files: {len(files)}")
    print(f"Included files: {kept}")
    print(f"Wrote: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
