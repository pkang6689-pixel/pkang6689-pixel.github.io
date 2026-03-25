#!/usr/bin/env python3
"""
Generate lesson_names.txt listing all lesson titles from content_data/.

For each Lesson*_Summary.json the script reads:
  1. The ``title`` field (preferred).
  2. Falls back to the first ``summary_sections`` entry title after stripping
     HTML markup and a leading "Key Concepts: " prefix.

Output format (one line per lesson):
  CourseName | UnitName | Lesson X.Y | Title

Usage:  python generate_lesson_names.py
Output: lesson_names.txt (overwritten in place)
"""

import json
import re
from html import unescape
from pathlib import Path

CONTENT_DATA = Path(__file__).parent / "content_data"
OUTPUT_FILE = Path(__file__).parent / "lesson_names.txt"


def strip_html(html_str: str) -> str:
    """Remove HTML tags and decode HTML entities."""
    text = re.sub(r"<[^>]+>", "", html_str)
    return unescape(text).strip()


def get_lesson_title(data: dict) -> str:
    """Return the best available title for a lesson JSON entry."""
    title = unescape(data.get("title", "")).strip()
    if title:
        return title
    # Fallback: use the first summary_sections title (strip HTML + prefix)
    for section in data.get("summary_sections", []):
        raw = strip_html(section.get("title", ""))
        if raw:
            raw = re.sub(r"^Key Concepts:\s*", "", raw)
            return raw
    return ""


def lesson_sort_key(path: Path) -> tuple:
    """Sort Lesson X.Y files numerically (handles 1.10 > 1.9)."""
    m = re.search(r"(\d+)\.(\d+)", path.name)
    return (int(m.group(1)), int(m.group(2))) if m else (999, 0)


def unit_sort_key(path: Path) -> int:
    """Sort Unit folders numerically."""
    m = re.search(r"\d+", path.name)
    return int(m.group()) if m else 999


def collect_lines() -> list[str]:
    lines: list[str] = []
    for course_dir in sorted(CONTENT_DATA.iterdir()):
        if not course_dir.is_dir():
            continue
        course_name = course_dir.name
        for unit_dir in sorted(course_dir.iterdir(), key=unit_sort_key):
            if not unit_dir.is_dir():
                continue
            unit_name = unit_dir.name
            summary_files = sorted(
                unit_dir.glob("Lesson*_Summary.json"), key=lesson_sort_key
            )
            for fpath in summary_files:
                with open(fpath, encoding="utf-8") as fh:
                    try:
                        data = json.load(fh)
                    except json.JSONDecodeError:
                        continue
                lesson_num = data.get("lesson_number", "")
                title = get_lesson_title(data)
                lines.append(
                    f"{course_name} | {unit_name} | Lesson {lesson_num} | {title}"
                )
    return lines


def main() -> None:
    lines = collect_lines()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"Written {len(lines)} lessons to {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
