"""
Fix Geometry Quiz files to be consistent with Physics/Bio:
1. Add search scripts (search_data.js, search_logic.js) before quiz_ui.js
"""

import os
import re
import glob

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\GeometryLessons"

SEARCH_SCRIPTS = """\
<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>"""


def get_lesson_id(filepath):
    basename = os.path.basename(filepath)
    m = re.search(r'Lesson(\d+\.\d+)', basename)
    return m.group(1) if m else None


def fix_quiz_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    lesson_id = get_lesson_id(filepath)
    if not lesson_id:
        return False

    # Add search scripts after quiz_ui.js (matching Physics/Bio order)
    if 'search_data.js' not in content:
        quiz_ui_tag = '<script src="../../scripts/quiz_ui.js"></script>'
        if quiz_ui_tag in content:
            content = content.replace(
                quiz_ui_tag,
                quiz_ui_tag + '\n' + SEARCH_SCRIPTS
            )
        else:
            # Fallback: insert before </body>
            content = content.replace('</body>', SEARCH_SCRIPTS + '\n</body>')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    files = glob.glob(os.path.join(BASE, "Unit*", "Lesson*_Quiz.html"))
    files.sort()

    fixed = 0
    errors = []

    for filepath in files:
        try:
            if fix_quiz_file(filepath):
                print(f"  OK: Lesson {get_lesson_id(filepath)}")
                fixed += 1
            else:
                print(f"  SKIP: Lesson {get_lesson_id(filepath)}")
        except Exception as e:
            print(f"  ERROR: {filepath}: {e}")
            errors.append(filepath)

    print(f"\nDone! Fixed {fixed}/{len(files)} files. Errors: {len(errors)}")
    if errors:
        for e in errors:
            print(f"  - {e}")


if __name__ == '__main__':
    main()
