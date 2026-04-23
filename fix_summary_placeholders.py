#!/usr/bin/env python3
"""Replace placeholder lesson summary HTML with real content_data summary sections.

This script updates only Summary pages that still contain the placeholder text:
"Detailed summary content for <b>... is coming soon.".
"""

from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
COURSEFILES_DIR = BASE_DIR / "ArisEdu Project Folder" / "CourseFiles"
CONTENT_DATA_DIR = BASE_DIR / "content_data"

PLACEHOLDER_MARKER = "Detailed summary content for <b>"
LESSON_FILE_RE = re.compile(r"Lesson\s*([A-Za-z0-9.]+)_Summary\.html$")
LESSON_NOTES_RE = re.compile(
    r'(<div\s+class="lesson-notes">\s*)(.*?)(\s*</div>)',
    re.DOTALL,
)


def build_replacement_notes(summary_json: dict) -> str:
    title = summary_json.get("title", "")
    sections = summary_json.get("summary_sections", [])

    lines: list[str] = [f"<h3>Key Concepts: {escape(title)}</h3>"]
    for section in sections:
        content_html = (section.get("content_html") or "").strip()
        if content_html:
            lines.append(content_html)

    return "\n".join(lines)


def main() -> None:
    updated = 0
    skipped_no_placeholder = 0
    skipped_filename_parse = 0
    skipped_missing_json = 0
    skipped_no_sections = 0
    skipped_no_lesson_notes = 0

    for html_path in COURSEFILES_DIR.rglob("*_Summary.html"):
        html_text = html_path.read_text(encoding="utf-8")
        if PLACEHOLDER_MARKER not in html_text:
            skipped_no_placeholder += 1
            continue

        match = LESSON_FILE_RE.search(html_path.name)
        if not match:
            skipped_filename_parse += 1
            continue

        lesson_number = match.group(1)
        rel_parent = html_path.relative_to(COURSEFILES_DIR).parent
        json_path = CONTENT_DATA_DIR / rel_parent / f"Lesson{lesson_number}_Summary.json"

        if not json_path.exists():
            skipped_missing_json += 1
            continue

        summary_data = json.loads(json_path.read_text(encoding="utf-8"))
        sections = summary_data.get("summary_sections", [])
        if not sections:
            skipped_no_sections += 1
            continue

        new_notes_html = build_replacement_notes(summary_data)
        replaced_text, replacements = LESSON_NOTES_RE.subn(
            lambda m: f"{m.group(1)}{new_notes_html}{m.group(3)}",
            html_text,
            count=1,
        )

        if replacements == 0:
            skipped_no_lesson_notes += 1
            continue

        html_path.write_text(replaced_text, encoding="utf-8")
        updated += 1

    print(f"updated={updated}")
    print(f"skipped_no_placeholder={skipped_no_placeholder}")
    print(f"skipped_filename_parse={skipped_filename_parse}")
    print(f"skipped_missing_json={skipped_missing_json}")
    print(f"skipped_no_sections={skipped_no_sections}")
    print(f"skipped_no_lesson_notes={skipped_no_lesson_notes}")


if __name__ == "__main__":
    main()
