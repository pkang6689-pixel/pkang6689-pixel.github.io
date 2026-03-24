#!/usr/bin/env python3
"""
Extract content from course JSON files in content_data/ and produce
plain-text files for each unit of each course.

Output structure:
  content_text/<Course>/<Unit>.txt
"""

import json
import os
import re
from html import unescape
from pathlib import Path

CONTENT_DATA = Path(__file__).parent / "content_data"
OUTPUT_DIR = Path(__file__).parent / "content_text"


def strip_html(html_str: str) -> str:
    """Remove HTML tags and decode entities."""
    text = re.sub(r"<br\s*/?>", "\n", html_str)
    text = re.sub(r"</?p[^>]*>", "\n", text)
    text = re.sub(r"<li[^>]*>", "  • ", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    # collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def format_summary(data: dict) -> str:
    lines = []
    title = data.get("title", "")
    lesson = data.get("lesson_number", "")
    lines.append(f"--- Lesson {lesson}: {title} (Summary) ---")
    for section in data.get("summary_sections", []):
        sec_title = section.get("title", "")
        if sec_title:
            lines.append(f"\n  {sec_title}")
        content = section.get("content_html", "")
        if content:
            lines.append(strip_html(content))
    return "\n".join(lines)


def format_quiz(data: dict) -> str:
    lines = []
    title = data.get("title", "")
    lesson = data.get("lesson_number", "")
    lines.append(f"\n--- Lesson {lesson}: {title} (Quiz) ---")
    for q in data.get("quiz_questions", []):
        qnum = q.get("question_number", "")
        qtext = q.get("question_text", "")
        lines.append(f"\n  Q{qnum}. {qtext}")
        for opt in q.get("options", []):
            marker = "*" if opt.get("is_correct") else " "
            lines.append(f"    [{marker}] {opt.get('text', '')}")
        explanation = q.get("explanation", "")
        if explanation:
            lines.append(f"    Explanation: {explanation}")
    return "\n".join(lines)


def format_practice(data: dict) -> str:
    lines = []
    title = data.get("title", "")
    lesson = data.get("lesson_number", "")
    lines.append(f"\n--- Lesson {lesson}: {title} (Flashcards) ---")
    for i, card in enumerate(data.get("flashcards", []), 1):
        lines.append(f"\n  {i}. Q: {card.get('question', '')}")
        lines.append(f"     A: {card.get('answer', '')}")
    return "\n".join(lines)


def collect_unit_files(unit_dir: Path) -> dict:
    """Return {lesson_number: {type: data}} sorted by lesson number."""
    lessons: dict[str, dict] = {}
    for fp in sorted(unit_dir.glob("*.json")):
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        lesson_num = data.get("lesson_number", fp.stem)
        if lesson_num not in lessons:
            lessons[lesson_num] = {}
        if "_Summary" in fp.name:
            lessons[lesson_num]["summary"] = data
        elif "_Quiz" in fp.name:
            lessons[lesson_num]["quiz"] = data
        elif "_Practice" in fp.name:
            lessons[lesson_num]["practice"] = data
    return dict(sorted(lessons.items(), key=lambda x: _lesson_sort_key(x[0])))


def _lesson_sort_key(lesson_num: str):
    """Sort lesson numbers like 1.1, 1.2, 1.10 correctly."""
    parts = lesson_num.split(".")
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return (999,)


def build_unit_text(unit_name: str, course_name: str, lessons: dict) -> str:
    header = f"{'=' * 60}\n{course_name} — {unit_name}\n{'=' * 60}\n"
    sections = [header]
    for _lesson_num, types in lessons.items():
        if "summary" in types:
            sections.append(format_summary(types["summary"]))
        if "quiz" in types:
            sections.append(format_quiz(types["quiz"]))
        if "practice" in types:
            sections.append(format_practice(types["practice"]))
        sections.append("")  # blank separator between lessons
    return "\n".join(sections)


def process_course(course_dir: Path, course_name: str):
    """Process all units inside a course directory."""
    unit_dirs = sorted(
        [d for d in course_dir.iterdir() if d.is_dir() and d.name != "unit_tests"],
        key=lambda d: _unit_sort_key(d.name),
    )
    if not unit_dirs:
        return 0
    out_course = OUTPUT_DIR / course_name
    out_course.mkdir(parents=True, exist_ok=True)
    count = 0
    for unit_dir in unit_dirs:
        lessons = collect_unit_files(unit_dir)
        if not lessons:
            continue
        text = build_unit_text(unit_dir.name, course_name, lessons)
        out_file = out_course / f"{unit_dir.name}.txt"
        out_file.write_text(text, encoding="utf-8")
        count += 1
    return count


def _unit_sort_key(name: str):
    m = re.search(r"(\d+)", name)
    return int(m.group(1)) if m else 999


def main():
    total_files = 0
    total_courses = 0
    for entry in sorted(CONTENT_DATA.iterdir()):
        if not entry.is_dir():
            continue
        course_name = entry.name
        # Handle AP Lessons which has an extra nesting level
        sub_entries = [d for d in entry.iterdir() if d.is_dir()]
        # Check if sub-entries are Unit dirs or sub-course dirs
        has_units = any(re.match(r"Unit\d+", d.name) for d in sub_entries)
        if has_units:
            n = process_course(entry, course_name)
            if n:
                total_courses += 1
                total_files += n
                print(f"  {course_name}: {n} unit files")
        else:
            # Sub-course directories (e.g. APLessons/AP Biology/)
            for sub in sorted(sub_entries, key=lambda d: d.name):
                safe_name = f"{course_name}/{sub.name}"
                n = process_course(sub, safe_name)
                if n:
                    total_courses += 1
                    total_files += n
                    print(f"  {safe_name}: {n} unit files")

    print(f"\nDone! Generated {total_files} text files across {total_courses} courses.")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
