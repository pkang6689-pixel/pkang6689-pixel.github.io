"""
Parse content_text/*.txt files and populate translation JSON files
with English text strings (key = English text, value = "").
"""
import json
import os
import re
from pathlib import Path

CONTENT_TEXT = Path("content_text")
TRANSLATIONS = Path("ArisEdu Project Folder/translations")
LANGUAGES = ["es", "hi", "zh"]

# Section header pattern: --- Lesson X.Y: Title (Type) ---
SECTION_RE = re.compile(
    r'^---\s+Lesson\s+([\d.]+):\s+(.+?)\s+\((Summary|Quiz|Flashcards)\)\s+---$'
)

# Quiz patterns
QUESTION_RE = re.compile(r'^\s*Q(\d+)\.\s+(.+)$')
OPTION_RE = re.compile(r'^\s*\[\s*\*?\s*\]\s+(.+)$')
EXPLANATION_RE = re.compile(r'^\s*Explanation:\s+(.+)$')

# Flashcard patterns
FLASHCARD_Q_RE = re.compile(r'^\s*\d+\.\s*Q:\s*(.+)$')
FLASHCARD_A_RE = re.compile(r'^\s*A:\s*(.+)$')

# Summary sub-headers we want to skip as structural, not translatable
SUMMARY_HEADER_RE = re.compile(
    r'^(Key Concepts:|Overview|Key Definitions|Real-World Applications|Example:)\s*(.*)'
)


def parse_txt_file(txt_path):
    """Parse a unit .txt file and return dict of {(lesson_num, section_type): [strings]}."""
    sections = {}
    current_key = None
    current_lines = []

    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip("\n")
        m = SECTION_RE.match(line.strip())
        if m:
            # Save previous section
            if current_key:
                sections[current_key] = current_lines
            lesson_num = m.group(1)
            section_type = m.group(3)  # Summary, Quiz, or Flashcards
            current_key = (lesson_num, section_type)
            current_lines = []
            continue
        if current_key:
            current_lines.append(line)

    # Save last section
    if current_key:
        sections[current_key] = current_lines

    return sections


def extract_summary_strings(lines):
    """Extract translatable strings from a Summary section.
    Each non-blank, non-header line is treated as a separate translatable string.
    """
    strings = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Skip the "Key Concepts:" prefix but keep the title text
        if stripped.startswith("Key Concepts:"):
            text = stripped[len("Key Concepts:"):].strip()
            if text:
                strings.append(text)
            continue
        # Skip sub-section headers
        if stripped in ("Overview", "Key Definitions", "Real-World Applications"):
            continue
        # "Example: <text>" lines - keep the text after "Example:"
        if stripped.startswith("Example:"):
            text = stripped[len("Example:"):].strip()
            if text:
                strings.append(text)
            continue
        # Every other non-empty line is a separate translatable string
        strings.append(stripped)

    return strings


def extract_quiz_strings(lines):
    """Extract translatable strings from a Quiz section."""
    strings = []
    # Track multi-line questions
    current_question = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Check for question
        qm = QUESTION_RE.match(line)
        if qm:
            if current_question:
                strings.append(current_question)
            current_question = qm.group(2).strip()
            continue

        # Check for option
        om = OPTION_RE.match(line)
        if om:
            # If we have a pending multi-line question, save it first
            if current_question:
                strings.append(current_question)
                current_question = None
            strings.append(om.group(1).strip())
            continue

        # Check for explanation
        em = EXPLANATION_RE.match(line)
        if em:
            if current_question:
                strings.append(current_question)
                current_question = None
            strings.append(em.group(1).strip())
            continue

        # Continuation of a multi-line question
        if current_question:
            current_question += " " + stripped

    if current_question:
        strings.append(current_question)

    return strings


def extract_flashcard_strings(lines):
    """Extract translatable strings from a Flashcards section."""
    strings = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        qm = FLASHCARD_Q_RE.match(line)
        if qm:
            text = qm.group(1).strip()
            if text:
                strings.append(text)
            continue
        am = FLASHCARD_A_RE.match(line)
        if am:
            text = am.group(1).strip()
            if text:
                strings.append(text)
            continue
    return strings


def section_type_to_filename(section_type):
    """Map section type from txt to JSON filename suffix."""
    mapping = {
        "Summary": "Summary",
        "Quiz": "Quiz",
        "Flashcards": "Practice",
    }
    return mapping.get(section_type, section_type)


def process_txt_file(txt_path, course_rel_path):
    """
    Process a single .txt file, extract strings, and write to translation JSONs.
    course_rel_path: e.g. "BiologyLessons" or "APLessons/AP Biology"
    txt_path: path to the .txt file
    """
    # Determine unit from filename (e.g. "Unit2.txt" -> "Unit2")
    unit_name = txt_path.stem  # e.g. "Unit2"

    sections = parse_txt_file(txt_path)
    files_written = 0

    for (lesson_num, section_type), lines in sections.items():
        # Extract strings based on section type
        if section_type == "Summary":
            strings = extract_summary_strings(lines)
        elif section_type == "Quiz":
            strings = extract_quiz_strings(lines)
        elif section_type == "Flashcards":
            strings = extract_flashcard_strings(lines)
        else:
            continue

        if not strings:
            continue

        # Build translation dict: key = English text, value = ""
        trans_dict = {}
        for s in strings:
            s = s.strip()
            if s and s not in trans_dict:
                trans_dict[s] = ""

        if not trans_dict:
            continue

        # Determine target filename
        file_suffix = section_type_to_filename(section_type)
        json_filename = f"Lesson{lesson_num}_{file_suffix}.json"

        # Write to each language
        for lang in LANGUAGES:
            target_dir = TRANSLATIONS / lang / course_rel_path / unit_name
            target_file = target_dir / json_filename

            # Create directory if needed
            target_dir.mkdir(parents=True, exist_ok=True)

            # Write JSON
            with open(target_file, "w", encoding="utf-8") as f:
                json.dump(trans_dict, f, ensure_ascii=False, indent=2)

        files_written += 1

    return files_written


def main():
    total_files = 0
    total_strings = 0

    # Walk content_text directory
    for course_dir in sorted(CONTENT_TEXT.iterdir()):
        if not course_dir.is_dir():
            continue

        course_name = course_dir.name  # e.g. "BiologyLessons"

        # Check for .txt files directly in course dir
        txt_files = list(course_dir.glob("*.txt"))
        if txt_files:
            for txt_file in sorted(txt_files):
                n = process_txt_file(txt_file, course_name)
                total_files += n
                print(f"  {course_name}/{txt_file.name} -> {n} section files")

        # Check for subdirectories (AP courses)
        for sub_dir in sorted(course_dir.iterdir()):
            if sub_dir.is_dir():
                sub_txt_files = list(sub_dir.glob("*.txt"))
                rel_path = f"{course_name}/{sub_dir.name}"
                for txt_file in sorted(sub_txt_files):
                    n = process_txt_file(txt_file, rel_path)
                    total_files += n
                    print(f"  {rel_path}/{txt_file.name} -> {n} section files")

    print(f"\nTotal: {total_files} section files written across {len(LANGUAGES)} languages")


if __name__ == "__main__":
    main()
