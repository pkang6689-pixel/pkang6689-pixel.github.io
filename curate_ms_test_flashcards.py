"""
Curate msFlashcards for MS unit test practice files.

For each MS unit, this script:
1. Identifies which HS lessons are included in the MS course
2. Reads the individual lesson Practice.html files for those lessons
3. Extracts their flashcards (up to 5 per lesson)
4. Combines them into a window.msFlashcards array (capped at ~25)
5. Inserts/updates msFlashcards in the Unit*_Test_Practice.html file
"""

import os, re, json, glob

BASE = os.path.join(os.path.dirname(__file__), "ArisEdu Project Folder")

# ── MS Course → HS Folder → { unit: [lesson_numbers] } ──────────────────
# Derived from the actual MS course page links
MS_MAP = {
    "Algebra1Lessons": {
        "Unit1":  ["1.1","1.2","1.3","1.4","1.5","1.6","1.7"],
        "Unit2":  ["2.1","2.2","2.3","2.5"],
        "Unit3":  ["3.1","3.2","3.4","3.5","3.6"],
        "Unit4":  ["4.1","4.2","4.3","4.4","4.5"],
        "Unit5":  ["5.1","5.2"],
        "Unit6":  ["6.1","6.2"],
        "Unit7":  ["7.1","7.2"],
        "Unit12": ["12.1","12.2"],
    },
    "Algebra2Lessons": {
        "Unit1": ["1.1","1.2","1.3","1.4","1.5"],
        "Unit2": ["2.1","2.2","2.5","2.6"],
        "Unit3": ["3.1","3.2"],
    },
    "GeometryLessons": {
        "Unit1": ["1.1","1.2","1.3","1.4","1.5","1.6","1.7"],
        "Unit2": ["2.1"],
        "Unit3": ["3.1","3.2","3.3","3.4"],
        "Unit4": ["4.1","4.2","4.3","4.6"],
        "Unit5": ["5.1"],
        "Unit6": ["6.1","6.2","6.4","6.5"],
        "Unit7": ["7.1","7.2","7.3","7.7"],
        "Unit8": ["8.2","8.3"],
    },
    "PhysicsLessons": {
        "Unit1": ["1.1","1.2","1.3","1.4"],
        "Unit2": ["2.1","2.2","2.3"],
        "Unit3": ["3.1","3.2","3.3","3.4"],
        "Unit4": ["4.1","4.2","4.3"],
        "Unit5": ["5.1","5.2"],
    },
    "ChemistryLessons": {
        "Unit1":  ["1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8"],
        "Unit2":  ["2.1","2.2","2.3","2.4","2.5"],
        "Unit3":  ["3.1","3.2","3.8"],
        "Unit4":  ["4.1","4.2","4.3"],
        "Unit5A": ["5A.1","5A.2","5A.3","5A.4","5A.6"],
        "Unit5B": ["5B.1","5B.2","5B.3"],
        "Unit6":  ["6.1","6.2","6.4"],
        "Unit7":  ["7.1"],
    },
    "BiologyLessons": {
        "Unit1": ["1.1","1.2","1.3","1.4","1.5","1.6","1.7"],
        "Unit2": ["2.1","2.2","2.3","2.4","2.5","2.6","2.7"],
        "Unit3": ["3.1","3.2","3.3","3.4","3.5"],
        "Unit4": ["4.1","4.2","4.3","4.5"],
        "Unit5": ["5.1","5.6"],
        "Unit6": ["6.1","6.2","6.3","6.4","6.6"],
        "Unit7": ["7.1","7.2"],
        "Unit8": ["8.1","8.5"],
        "Unit9": ["9.1","9.2","9.3","9.4"],
    },
}

MAX_FLASHCARDS_PER_UNIT = 25  # Global cap
MAX_PER_LESSON = 5  # Max flashcards to keep from each lesson

def extract_flashcards(html_text):
    """Extract flashcards from window.lessonFlashcards = [...] in HTML."""
    # Match the array content
    m = re.search(r'window\.lessonFlashcards\s*=\s*\[', html_text)
    if not m:
        return []
    
    start = m.end()
    # Find the matching closing bracket
    depth = 1
    i = start
    while i < len(html_text) and depth > 0:
        if html_text[i] == '[':
            depth += 1
        elif html_text[i] == ']':
            depth -= 1
        i += 1
    
    array_content = html_text[start:i-1]
    
    # Parse individual flashcard objects
    flashcards = []
    # Match objects with double OR single quoted strings
    # Pattern: { question: "..." , answer: "..." } or { question: '...' , answer: '...' }
    # Also handles quoted keys like { "question": "..." }
    pattern_dq = re.compile(
        r'\{\s*"?question"?\s*:\s*"((?:[^"\\]|\\.)*)"\s*,\s*"?answer"?\s*:\s*"((?:[^"\\]|\\.)*)"\s*\}',
        re.DOTALL
    )
    pattern_sq = re.compile(
        r"""\{\s*"?question"?\s*:\s*'((?:[^'\\]|\\.)*)'\s*,\s*"?answer"?\s*:\s*'((?:[^'\\]|\\.)*)'\s*\}""",
        re.DOTALL
    )
    for match in pattern_dq.finditer(array_content):
        flashcards.append({
            "question": match.group(1),
            "answer": match.group(2)
        })
    if not flashcards:
        for match in pattern_sq.finditer(array_content):
            flashcards.append({
                "question": match.group(1),
                "answer": match.group(2)
            })
    
    return flashcards


def find_lesson_practice_file(unit_dir, lesson_num):
    """Find the Practice.html file for a given lesson number."""
    # Try common naming patterns
    patterns = [
        f"Lesson{lesson_num}_Practice.html",
        f"Lesson {lesson_num}_Practice.html",
        f"Lesson{lesson_num} _Practice.html",
        f"Lesson_{lesson_num}_Practice.html",
    ]
    
    # Also try with just the decimal part
    for p in patterns:
        full_path = os.path.join(unit_dir, p)
        if os.path.exists(full_path):
            return full_path
    
    # Glob fallback - look for files containing the lesson number
    # e.g., "Lesson 3.1_Practice.html" or "Lesson3.1_Practice.html"
    num_part = lesson_num.split(".")[-1] if "." in lesson_num else lesson_num
    unit_num = lesson_num.split(".")[0] if "." in lesson_num else ""
    
    for f in os.listdir(unit_dir):
        f_lower = f.lower()
        if '_practice.html' in f_lower and 'test' not in f_lower:
            # Check if lesson number matches
            # Match patterns like "Lesson 3.1" or "Lesson3.1" 
            m = re.search(r'lesson\s*(\d+[A-Ba-b]?)\.?(\d+)', f_lower)
            if m:
                file_unit = m.group(1)
                file_lesson = m.group(2)
                if lesson_num.lower() == f"{file_unit}.{file_lesson}":
                    return os.path.join(unit_dir, f)
                # Also check if just the lesson number part matches
                if num_part == file_lesson and (not unit_num or file_unit.lower() == unit_num.lower()):
                    return os.path.join(unit_dir, f)
    
    return None


def build_ms_flashcards(subject_folder, unit_name, ms_lessons):
    """Build curated msFlashcards for a unit test from individual lesson files."""
    unit_dir = os.path.join(BASE, subject_folder, unit_name)
    if not os.path.isdir(unit_dir):
        print(f"  WARNING: {unit_dir} not found")
        return []
    
    all_cards = []
    for lesson_num in ms_lessons:
        pfile = find_lesson_practice_file(unit_dir, lesson_num)
        if pfile:
            with open(pfile, 'r', encoding='utf-8', errors='ignore') as f:
                html = f.read()
            cards = extract_flashcards(html)
            if cards:
                # Take up to MAX_PER_LESSON from each lesson
                selected = cards[:MAX_PER_LESSON]
                all_cards.extend(selected)
                print(f"    Lesson {lesson_num}: {len(cards)} total → took {len(selected)}")
            else:
                print(f"    Lesson {lesson_num}: no flashcards found in {os.path.basename(pfile)}")
        else:
            print(f"    Lesson {lesson_num}: practice file not found in {unit_dir}")
    
    # Cap at MAX_FLASHCARDS_PER_UNIT
    if len(all_cards) > MAX_FLASHCARDS_PER_UNIT:
        # Evenly sample from the cards while preserving order
        step = len(all_cards) / MAX_FLASHCARDS_PER_UNIT
        indices = [int(i * step) for i in range(MAX_FLASHCARDS_PER_UNIT)]
        all_cards = [all_cards[i] for i in indices]
    
    return all_cards


def format_flashcards_js(cards, use_quoted_keys=False):
    """Format flashcards as a JS array string."""
    lines = []
    for c in cards:
        q = c["question"].replace('"', '\\"').replace('\n', '\\n')
        a = c["answer"].replace('"', '\\"').replace('\n', '\\n')
        if use_quoted_keys:
            lines.append(f'    {{ "question": "{q}", "answer": "{a}" }}')
        else:
            lines.append(f'    {{ question: "{q}", answer: "{a}" }}')
    return "[\n" + ",\n".join(lines) + "\n]"


def update_test_practice(subject_folder, unit_name, ms_cards, use_quoted_keys=False):
    """Insert or replace msFlashcards in the Test_Practice.html file."""
    test_file = os.path.join(BASE, subject_folder, unit_name, f"{unit_name}_Test_Practice.html")
    if not os.path.exists(test_file):
        print(f"  ERROR: {test_file} not found")
        return False
    
    with open(test_file, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    js_array = format_flashcards_js(ms_cards, use_quoted_keys)
    new_block = f"window.msFlashcards = {js_array};"
    
    # Check if msFlashcards already exists
    ms_pattern = re.compile(r'window\.msFlashcards\s*=\s*\[', re.DOTALL)
    ms_match = ms_pattern.search(html)
    
    if ms_match:
        # Replace existing msFlashcards
        start = ms_match.start()
        # Find end of the array + semicolon
        bracket_start = html.index('[', start)
        depth = 1
        i = bracket_start + 1
        while i < len(html) and depth > 0:
            if html[i] == '[':
                depth += 1
            elif html[i] == ']':
                depth -= 1
            i += 1
        # Skip trailing semicolon and whitespace
        end = i
        while end < len(html) and html[end] in ' \t':
            end += 1
        if end < len(html) and html[end] == ';':
            end += 1
        
        html = html[:start] + new_block + html[end:]
        action = "REPLACED"
    else:
        # Insert after window.lessonFlashcards array
        lf_pattern = re.compile(r'window\.lessonFlashcards\s*=\s*\[', re.DOTALL)
        lf_match = lf_pattern.search(html)
        if lf_match:
            # Find end of lessonFlashcards array
            bracket_start = html.index('[', lf_match.start())
            depth = 1
            i = bracket_start + 1
            while i < len(html) and depth > 0:
                if html[i] == '[':
                    depth += 1
                elif html[i] == ']':
                    depth -= 1
                i += 1
            # Skip trailing semicolon
            end = i
            while end < len(html) and html[end] in ' \t':
                end += 1
            if end < len(html) and html[end] == ';':
                end += 1
            
            html = html[:end] + "\n" + new_block + html[end:]
            action = "INSERTED"
        else:
            print(f"  ERROR: No lessonFlashcards found in {test_file}")
            return False
    
    with open(test_file, 'w', encoding='utf-8', newline='') as f:
        f.write(html)
    
    print(f"  {action} msFlashcards ({len(ms_cards)} cards) in {unit_name}_Test_Practice.html")
    return True


def main():
    total_updated = 0
    total_cards = 0
    
    for subject_folder, units in MS_MAP.items():
        print(f"\n{'='*60}")
        print(f"  {subject_folder}")
        print(f"{'='*60}")
        
        # Algebra2 uses quoted keys
        use_quoted = (subject_folder == "Algebra2Lessons")
        
        for unit_name, ms_lessons in sorted(units.items()):
            print(f"\n  {unit_name} ({len(ms_lessons)} MS lessons: {', '.join(ms_lessons)})")
            
            ms_cards = build_ms_flashcards(subject_folder, unit_name, ms_lessons)
            
            if not ms_cards:
                print(f"  SKIP: No flashcards collected for {unit_name}")
                continue
            
            if update_test_practice(subject_folder, unit_name, ms_cards, use_quoted):
                total_updated += 1
                total_cards += len(ms_cards)
    
    print(f"\n{'='*60}")
    print(f"  DONE: Updated {total_updated} files with {total_cards} total MS flashcards")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
