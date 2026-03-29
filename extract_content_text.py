#!/usr/bin/env python3
"""
Extract content from content_data/ JSON files and regenerate content_text/ .txt files.

Reads Summary, Quiz, and Practice (flashcard) JSON for each lesson and writes
formatted plain-text files grouped by unit.
"""

import json
import os
import re
from html.parser import HTMLParser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "content_data"
TEXT_DIR = BASE_DIR / "content_text"


# ── HTML → plain text ────────────────────────────────────────────────────────

class _HTMLStripper(HTMLParser):
    """Lightweight HTML tag stripper that preserves readable text."""
    def __init__(self):
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data):
        self.parts.append(data)

    def get_text(self) -> str:
        return "".join(self.parts)


def strip_html(html: str) -> str:
    """Return plain text from an HTML snippet."""
    s = _HTMLStripper()
    s.feed(html)
    text = s.get_text()
    # Collapse runs of blank lines into at most two newlines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ── JSON loaders ─────────────────────────────────────────────────────────────

def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def lesson_sort_key(lesson_num: str):
    """Sort lesson numbers like '1.1', '1.2', '5A.1' numerically/lexically."""
    parts = lesson_num.split(".")
    result = []
    for p in parts:
        # Try pure int first, else sort alphabetically
        try:
            result.append((0, int(p), ""))
        except ValueError:
            # e.g. "5A" → extract leading digits + trailing letters
            m = re.match(r"(\d+)(.*)", p)
            if m:
                result.append((0, int(m.group(1)), m.group(2)))
            else:
                result.append((1, 0, p))
    return tuple(result)


# ── Formatters ───────────────────────────────────────────────────────────────

def format_summary(data: dict) -> str:
    """Format a Summary JSON into plain-text section."""
    title = data.get("title", "")
    lines = [f"--- Lesson {data['lesson_number']}: {title} (Summary) ---", ""]

    sections = data.get("summary_sections", [])
    if sections:
        # Use the first section title as a heading hint
        first_title = sections[0].get("title", "Key Concepts")
        # Combine all section HTML
        combined_html = "\n".join(
            sec.get("content_html", "") for sec in sections
        )
        plain = strip_html(combined_html)
        if plain:
            lines.append(f"  Key Concepts: {title}")
            for para in plain.split("\n"):
                stripped = para.strip()
                if stripped:
                    lines.append(stripped)
            lines.append("")
    return "\n".join(lines)


def format_quiz(data: dict) -> str:
    """Format a Quiz JSON into plain-text section."""
    title = data.get("title", "")
    lines = [f"--- Lesson {data['lesson_number']}: {title} (Quiz) ---", ""]

    for q in data.get("quiz_questions", []):
        qnum = q.get("question_number", "")
        qtext = q.get("question_text", "")
        lines.append(f"  Q{qnum}. {qtext}")

        for opt in q.get("options", []):
            marker = "[*]" if opt.get("is_correct") else "[ ]"
            lines.append(f"    {marker} {opt.get('text', '')}")

        explanation = q.get("explanation", "")
        if explanation:
            lines.append(f"    Explanation: {explanation}")

        lines.append("")  # blank line between questions

    return "\n".join(lines)


def format_flashcards(data: dict) -> str:
    """Format a Practice/Flashcard JSON into plain-text section."""
    title = data.get("title", "")
    lines = [f"--- Lesson {data['lesson_number']}: {title} (Flashcards) ---", ""]

    for i, card in enumerate(data.get("flashcards", []), 1):
        q = card.get("question", "")
        a = card.get("answer", "")
        lines.append(f"  {i}. Q: {q}")
        lines.append(f"     A: {a}")
        lines.append("")

    return "\n".join(lines)


# ── Per-unit assembly ────────────────────────────────────────────────────────

def discover_lessons(unit_dir: Path) -> list[str]:
    """Return sorted list of lesson numbers found in a unit directory."""
    lessons = set()
    for f in unit_dir.iterdir():
        if f.suffix == ".json":
            m = re.match(r"Lesson([\d\w.]+)_", f.name)
            if m:
                lessons.add(m.group(1))
    return sorted(lessons, key=lesson_sort_key)


def build_unit_text(course_label: str, unit_name: str, unit_dir: Path) -> str:
    """Build the full .txt content for one unit."""
    sep = "=" * 60
    lines = [sep, f"{course_label} — {unit_name}", sep, ""]

    for lesson_num in discover_lessons(unit_dir):
        prefix = f"Lesson{lesson_num}"

        # Summary
        summary_path = unit_dir / f"{prefix}_Summary.json"
        if summary_path.exists():
            lines.append(format_summary(load_json(summary_path)))

        # Quiz
        quiz_path = unit_dir / f"{prefix}_Quiz.json"
        if quiz_path.exists():
            lines.append(format_quiz(load_json(quiz_path)))

        # Flashcards / Practice
        practice_path = unit_dir / f"{prefix}_Practice.json"
        if practice_path.exists():
            lines.append(format_flashcards(load_json(practice_path)))

    return "\n".join(lines).rstrip() + "\n"


# ── Main driver ──────────────────────────────────────────────────────────────

def process_course(course_data_dir: Path, course_text_dir: Path, course_label: str):
    """Process every unit in a course and write .txt files."""
    unit_dirs = sorted(
        [d for d in course_data_dir.iterdir() if d.is_dir() and d.name.startswith("Unit")],
        key=lambda d: int(re.search(r"\d+", d.name).group()) if re.search(r"\d+", d.name) else 0,
    )

    if not unit_dirs:
        return

    course_text_dir.mkdir(parents=True, exist_ok=True)

    for unit_dir in unit_dirs:
        unit_name = unit_dir.name  # e.g. "Unit1"
        txt_path = course_text_dir / f"{unit_name}.txt"
        content = build_unit_text(course_label, unit_name, unit_dir)
        txt_path.write_text(content, encoding="utf-8")
        print(f"  OK {txt_path.relative_to(BASE_DIR)}")


def main():
    print("Extracting content_data -> content_text ...\n")
    updated = 0

    for course_dir in sorted(DATA_DIR.iterdir()):
        if not course_dir.is_dir():
            continue

        course_name = course_dir.name  # e.g. "Algebra1Lessons" or "APLessons"

        # AP courses have an extra sub-folder level (e.g. APLessons/AP Biology/)
        sub_courses = [
            d for d in course_dir.iterdir()
            if d.is_dir() and d.name.startswith("AP ")
        ]

        if sub_courses:
            # AP-style: each sub-folder is its own course
            for sub in sorted(sub_courses, key=lambda d: d.name):
                label = f"{course_name}/{sub.name}"
                text_out = TEXT_DIR / course_name / sub.name
                print(f"[{label}]")
                process_course(sub, text_out, label)
                updated += 1
        else:
            # Standard course
            print(f"[{course_name}]")
            process_course(course_dir, TEXT_DIR / course_name, course_name)
            updated += 1

    print(f"\nDone — processed {updated} course(s).")


if __name__ == "__main__":
    main()
