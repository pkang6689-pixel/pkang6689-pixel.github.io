#!/usr/bin/env python3
"""
add_test_flashcards.py
Extracts window.lessonFlashcards from all Practice files in each unit,
combines them, and injects into the corresponding Unit Test file as a
<script> block before the other script tags.
This provides data for flashcard, mix & match, climb, and block puzzle games.
"""

import os
import re
import glob

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'ArisEdu Project Folder', 'ChemistryLessons'))


def extract_flashcards_from_practice(filepath):
    """Extract the lessonFlashcards array items from a Practice file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the window.lessonFlashcards = [...] block
    match = re.search(
        r'window\.lessonFlashcards\s*=\s*\[(.*?)\];',
        content,
        re.DOTALL
    )
    if not match:
        return []

    array_body = match.group(1)

    # Parse individual { question: "...", answer: "..." } objects
    items = []
    for obj_match in re.finditer(
        r'\{\s*question:\s*(["\'])(.*?)\1\s*,\s*answer:\s*(["\'])(.*?)\3\s*\}',
        array_body,
        re.DOTALL
    ):
        q = obj_match.group(2).replace('"', '\\"')
        a = obj_match.group(4).replace('"', '\\"')
        items.append((q, a))

    return items


def get_unit_flashcards(unit_dir):
    """Get combined flashcards from all Practice files in a unit directory."""
    practice_files = sorted(glob.glob(os.path.join(unit_dir, '*_Practice.html')))
    all_cards = []
    for pf in practice_files:
        cards = extract_flashcards_from_practice(pf)
        all_cards.extend(cards)
    return all_cards


def inject_flashcards_into_test(test_file, flashcards):
    """Inject the combined flashcards array into the test file."""
    with open(test_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if flashcards already injected
    if 'window.lessonFlashcards' in content:
        print(f"  Already has flashcards, replacing...")
        # Remove existing flashcard script block
        content = re.sub(
            r'<script>\s*window\.lessonFlashcards\s*=\s*\[.*?\];\s*</script>\s*',
            '',
            content,
            flags=re.DOTALL
        )

    # Build the flashcards script block
    lines = ['window.lessonFlashcards = [']
    for i, (q, a) in enumerate(flashcards):
        comma = ',' if i < len(flashcards) - 1 else ''
        lines.append(f'    {{ question: "{q}", answer: "{a}" }}{comma}')
    lines.append('];')
    script_block = '<script>\n' + '\n'.join(lines) + '\n</script>\n'

    # Insert before the first <script src="../../scripts/ tag
    # This ensures data is available before game scripts run
    insert_point = content.find('<script src="../../scripts/lesson_video.js">')
    if insert_point == -1:
        insert_point = content.find('<script src="../../scripts/')
    if insert_point == -1:
        # Fallback: insert before </body>
        insert_point = content.find('</body>')

    if insert_point == -1:
        print(f"  ERROR: Could not find insertion point in {test_file}")
        return False

    new_content = content[:insert_point] + script_block + content[insert_point:]

    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    # Map unit directories to their test files
    unit_dirs = sorted(glob.glob(os.path.join(BASE, 'Unit*')))

    processed = 0
    total_cards = 0

    for unit_dir in unit_dirs:
        if not os.path.isdir(unit_dir):
            continue

        unit_name = os.path.basename(unit_dir)

        # Skip Unit5A and Unit5B (no test files)
        if unit_name in ('Unit5A', 'Unit5B'):
            continue

        # Find test file
        test_files = glob.glob(os.path.join(unit_dir, '*_Test.html'))
        if not test_files:
            continue

        test_file = test_files[0]

        # For Unit5, look in Unit5A and Unit5B for practice files
        # (There's no Unit5 test, so skip)

        # Get flashcards from the unit's practice files
        flashcards = get_unit_flashcards(unit_dir)

        if not flashcards:
            print(f"  WARNING: No flashcards found in {unit_name}")
            continue

        rel_test = os.path.relpath(test_file, BASE)
        print(f"Processing: {rel_test} ({len(flashcards)} flashcards from {unit_name})")

        if inject_flashcards_into_test(test_file, flashcards):
            processed += 1
            total_cards += len(flashcards)
            print(f"  Injected {len(flashcards)} flashcards")

    print(f"\nDone! Updated {processed} test files with {total_cards} total flashcards.")
    print("Games now powered: Flashcards, Climb/Boost, Mix & Match, Block Puzzle")


if __name__ == '__main__':
    main()
