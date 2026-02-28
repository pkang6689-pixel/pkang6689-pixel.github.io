#!/usr/bin/env python3
"""
ms_unit_test_filter.py
Processes unit test files to add MS-specific content filtering.
- Practice files: Adds window.msFlashcards array with only MS-relevant flashcards
- Quiz files: Adds data-hs-only="true" to questions about HS-only topics
"""

import re, os, math

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ArisEdu Project Folder")

# Mapping of course -> unit -> {hs: full lesson list, ms: kept lesson list}
MS_LESSONS = {
    'ChemistryLessons': {
        '3': {'hs': ['3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8'], 'ms': ['3.1','3.2','3.8']},
        '4': {'hs': ['4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8','4.9'], 'ms': ['4.1','4.2','4.3']},
        '5A': {'hs': ['5A.1','5A.2','5A.3','5A.4','5A.5','5A.6','5A.7','5A.8'], 'ms': ['5A.1','5A.2','5A.3','5A.4','5A.6']},
        '5B': {'hs': ['5B.1','5B.2','5B.3','5B.4','5B.5'], 'ms': ['5B.1','5B.2','5B.3']},
        '6': {'hs': ['6.1','6.2','6.3','6.4','6.5','6.6','6.7'], 'ms': ['6.1','6.2','6.4']},
        '7': {'hs': ['7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8'], 'ms': ['7.1']},
    },
    'BiologyLessons': {
        '4': {'hs': ['4.1','4.2','4.3','4.4','4.5','4.6'], 'ms': ['4.1','4.2','4.3','4.5']},
        '5': {'hs': ['5.1','5.2','5.3','5.4','5.5','5.6'], 'ms': ['5.1','5.6']},
        '6': {'hs': ['6.1','6.2','6.3','6.4','6.5','6.6'], 'ms': ['6.1','6.2','6.3','6.4','6.6']},
        '7': {'hs': ['7.1','7.2','7.3','7.4','7.5','7.6'], 'ms': ['7.1','7.2']},
        '8': {'hs': ['8.1','8.2','8.3','8.4','8.5'], 'ms': ['8.1','8.5']},
        '9': {'hs': ['9.1','9.2','9.3','9.4','9.5'], 'ms': ['9.1','9.2','9.3','9.4']},
    },
    'PhysicsLessons': {
        '1': {'hs': ['1.1','1.2','1.3','1.4','1.5','1.6'], 'ms': ['1.1','1.2','1.3','1.4']},
        '2': {'hs': ['2.1','2.2','2.3','2.4','2.5','2.6'], 'ms': ['2.1','2.2','2.3']},
        '3': {'hs': ['3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8'], 'ms': ['3.1','3.2','3.3','3.4']},
        '4': {'hs': ['4.1','4.2','4.3','4.4','4.5','4.6'], 'ms': ['4.1','4.2','4.3']},
        '5': {'hs': ['5.1','5.2','5.3','5.4','5.5','5.6'], 'ms': ['5.1','5.2']},
    },
    'Algebra1Lessons': {
        '2': {'hs': ['2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9'], 'ms': ['2.1','2.2','2.3','2.5']},
        '3': {'hs': ['3.1','3.2','3.3','3.4','3.5','3.6','3.7'], 'ms': ['3.1','3.2','3.4','3.5','3.6']},
        '4': {'hs': ['4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8'], 'ms': ['4.1','4.2','4.3','4.4','4.5']},
        '5': {'hs': ['5.1','5.2','5.3','5.4','5.5','5.6','5.7','5.8','5.9','5.10'], 'ms': ['5.1','5.2']},
        '6': {'hs': ['6.1','6.2','6.3','6.4','6.5','6.6'], 'ms': ['6.1','6.2']},
        '7': {'hs': ['7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8'], 'ms': ['7.1','7.2']},
        '12': {'hs': ['12.1','12.2','12.3','12.4'], 'ms': ['12.1','12.2']},
    },
    'Algebra2Lessons': {
        '1': {'hs': ['1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9'], 'ms': ['1.1','1.2','1.3','1.4','1.5']},
        '2': {'hs': ['2.1','2.2','2.3','2.4','2.5','2.6','2.7'], 'ms': ['2.1','2.2','2.5','2.6']},
        '3': {'hs': ['3.1','3.2','3.3','3.4','3.5','3.6','3.7'], 'ms': ['3.1','3.2']},
    },
    'GeometryLessons': {
        '2': {'hs': ['2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9'], 'ms': ['2.1']},
        '3': {'hs': ['3.1','3.2','3.3','3.4','3.5','3.6','3.7'], 'ms': ['3.1','3.2','3.3','3.4']},
        '4': {'hs': ['4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8'], 'ms': ['4.1','4.2','4.3','4.6']},
        '5': {'hs': ['5.1','5.2','5.3','5.4','5.5','5.6'], 'ms': ['5.1']},
        '6': {'hs': ['6.1','6.2','6.3','6.4','6.5','6.6','6.7'], 'ms': ['6.1','6.2','6.4','6.5']},
        '7': {'hs': ['7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8'], 'ms': ['7.1','7.2','7.3','7.7']},
        '8': {'hs': ['8.1','8.2','8.3','8.4','8.5','8.6','8.7','8.8'], 'ms': ['8.2','8.3']},
    },
}

def assign_lessons(total_items, hs_lessons):
    """Assign each item index to an HS lesson based on proportional position."""
    n = len(hs_lessons)
    assignments = []
    for i in range(total_items):
        # Which lesson group does this index belong to?
        lesson_idx = min(int(i * n / total_items), n - 1)
        assignments.append(hs_lessons[lesson_idx])
    return assignments

def get_ms_keep_indices(total_items, hs_lessons, ms_lessons):
    """Return set of indices to keep for MS mode."""
    assignments = assign_lessons(total_items, hs_lessons)
    ms_set = set(ms_lessons)
    return [i for i, lesson in enumerate(assignments) if lesson in ms_set]

def extract_flashcards(content):
    """Extract individual flashcard objects from window.lessonFlashcards array."""
    # Find the lessonFlashcards array
    match = re.search(r'window\.lessonFlashcards\s*=\s*\[', content)
    if not match:
        return None, None, None
    
    start = match.start()
    # Find matching closing bracket
    bracket_count = 0
    array_start = content.index('[', match.start())
    pos = array_start
    for i in range(array_start, len(content)):
        if content[i] == '[':
            bracket_count += 1
        elif content[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                pos = i
                break
    
    array_content = content[array_start+1:pos]
    
    # Split into individual flashcard objects
    cards = []
    card_pattern = re.compile(r'\{[^}]+\}', re.DOTALL)
    for m in card_pattern.finditer(array_content):
        cards.append(m.group().strip())
    
    # Find the end of the full statement (after ];)
    end_pos = content.index(';', pos) + 1 if ';' in content[pos:pos+5] else pos + 1
    
    return cards, start, end_pos

def process_practice_file(filepath, hs_lessons, ms_lessons):
    """Add window.msFlashcards to a practice file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already processed
    if 'window.msFlashcards' in content:
        return False, "Already processed"
    
    cards, start, end_pos = extract_flashcards(content)
    if not cards:
        return False, "No flashcards found"
    
    keep_indices = get_ms_keep_indices(len(cards), hs_lessons, ms_lessons)
    
    if len(keep_indices) == len(cards):
        return False, "All flashcards are MS-appropriate"
    
    # Build msFlashcards array
    ms_cards = [cards[i] for i in keep_indices]
    ms_array = "window.msFlashcards = [\n    " + ",\n    ".join(ms_cards) + "\n];"
    
    # Insert after the lessonFlashcards statement
    insert_point = end_pos
    # Find end of line
    while insert_point < len(content) and content[insert_point] in ('\n', '\r', ' '):
        insert_point += 1
    
    new_content = content[:end_pos] + "\n\n// MS Mode: curated flashcard subset (auto-generated)\n" + ms_array + "\n" + content[insert_point:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, f"Kept {len(keep_indices)}/{len(cards)} flashcards for MS"

def process_quiz_file(filepath, hs_lessons, ms_lessons):
    """Add data-hs-only='true' to HS-only quiz questions."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already processed
    if 'data-hs-only' in content:
        return False, "Already processed"
    
    # Count quiz questions
    question_pattern = re.compile(r'<div\s+class="quiz-question"')
    matches = list(question_pattern.finditer(content))
    
    if not matches:
        return False, "No quiz questions found"
    
    total_q = len(matches)
    keep_indices = set(get_ms_keep_indices(total_q, hs_lessons, ms_lessons))
    
    hs_only_count = total_q - len(keep_indices)
    if hs_only_count == 0:
        return False, "All questions are MS-appropriate"
    
    # Process in reverse order to maintain positions
    new_content = content
    for idx in range(len(matches) - 1, -1, -1):
        if idx not in keep_indices:
            m = matches[idx]
            # Replace class="quiz-question" with class="quiz-question" data-hs-only="true"
            old_tag = new_content[m.start():m.end()]
            new_tag = old_tag.replace('class="quiz-question"', 'class="quiz-question" data-hs-only="true"')
            new_content = new_content[:m.start()] + new_tag + new_content[m.end():]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, f"Marked {hs_only_count}/{total_q} questions as HS-only"

def main():
    total_practice = 0
    total_quiz = 0
    
    for course_folder, units in MS_LESSONS.items():
        print(f"\n{'='*60}")
        print(f"Processing {course_folder}")
        print('='*60)
        
        for unit, info in sorted(units.items(), key=lambda x: (len(x[0]), x[0])):
            hs = info['hs']
            ms = info['ms']
            
            unit_dir = os.path.join(BASE, course_folder, f"Unit{unit}")
            practice_file = os.path.join(unit_dir, f"Unit{unit}_Test_Practice.html")
            quiz_file = os.path.join(unit_dir, f"Unit{unit}_Test.html")
            
            print(f"\n  Unit {unit}: HS={len(hs)} lessons, MS={len(ms)} lessons")
            
            # Process practice file
            if os.path.exists(practice_file):
                ok, msg = process_practice_file(practice_file, hs, ms)
                status = "✓" if ok else "–"
                print(f"    {status} Practice: {msg}")
                if ok: total_practice += 1
            else:
                print(f"    ✗ Practice: FILE NOT FOUND")
            
            # Process quiz file
            if os.path.exists(quiz_file):
                ok, msg = process_quiz_file(quiz_file, hs, ms)
                status = "✓" if ok else "–"
                print(f"    {status} Quiz: {msg}")
                if ok: total_quiz += 1
            else:
                print(f"    ✗ Quiz: FILE NOT FOUND")
    
    print(f"\n{'='*60}")
    print(f"DONE: Modified {total_practice} practice files, {total_quiz} quiz files")
    print('='*60)

if __name__ == '__main__':
    main()
