#!/usr/bin/env python3
"""
Add progress tracking to "Next Lesson" buttons in quiz files.

When a student clicks "Next Lesson: X.Y" on a quiz page, this script
adds a localStorage.setItem() call so chem.html's progress tracker
marks that lesson as IN PROGRESS (orange) on the SVG course map.

localStorage key format: chem_u{unit}_l{lesson}_started = 'true'
"""

import os
import re
import glob

CHEM_LESSONS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "ArisEdu Project Folder", "ChemistryLessons"
)

# Pattern to match the Next Lesson button onclick
# Examples:
#   onclick="window.location.href='Lesson 3.2_Video.html'"
#   onclick="window.location.href='../Unit4/Lesson 4.1_Video.html'"
NEXT_BUTTON_RE = re.compile(
    r"""onclick="window\.location\.href='([^']*Lesson\s+(\w+)\.(\d+)_Video\.html)'">Next Lesson"""
)

def process_quiz_file(filepath):
    """Add localStorage progress tracking to a quiz file's Next Lesson button."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = NEXT_BUTTON_RE.search(content)
    if not match:
        return False  # No Next Lesson button (e.g., last quiz 12.5)

    href = match.group(1)
    unit = match.group(2)   # e.g., '3', '5A', '10'
    lesson = match.group(3) # e.g., '2', '1'

    # Check if already has localStorage (idempotent)
    if 'localStorage.setItem' in content:
        print(f"  SKIP (already has tracking): {os.path.basename(filepath)}")
        return False

    # Build the localStorage call
    ls_key = f"chem_u{unit}_l{lesson}_started"
    old_onclick = f"""onclick="window.location.href='{href}'" """
    new_onclick = f"""onclick="localStorage.setItem('{ls_key}','true'); window.location.href='{href}'" """

    # Some files may have the onclick without trailing space - handle both
    if old_onclick not in content:
        old_onclick = f"""onclick="window.location.href='{href}'\""""
        new_onclick = f"""onclick="localStorage.setItem('{ls_key}','true'); window.location.href='{href}'\""""

    if old_onclick not in content:
        print(f"  WARNING: Could not find onclick pattern in {os.path.basename(filepath)}")
        print(f"    Looking for: {old_onclick}")
        return False

    new_content = content.replace(old_onclick, new_onclick, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  UPDATED: {os.path.basename(filepath)} → {ls_key}")
    return True


def main():
    quiz_files = sorted(glob.glob(os.path.join(CHEM_LESSONS, "Unit*", "Lesson *_Quiz.html")))
    print(f"Found {len(quiz_files)} quiz files\n")

    updated = 0
    skipped = 0
    warnings = 0

    for qf in quiz_files:
        rel = os.path.relpath(qf, CHEM_LESSONS)
        result = process_quiz_file(qf)
        if result:
            updated += 1
        elif result is False:
            # Check if it was skipped or just has no button
            with open(qf, 'r') as f:
                c = f.read()
            if 'Next Lesson' not in c:
                skipped += 1
            elif 'localStorage.setItem' in c:
                skipped += 1

    print(f"\n{'='*50}")
    print(f"Updated: {updated}")
    print(f"Skipped: {skipped}")
    print(f"Total quiz files: {len(quiz_files)}")


if __name__ == "__main__":
    main()
