"""
Fix Geometry Practice files to be consistent with Physics/Bio:
1. Add "Next Up: Quiz" navigation link after game containers
2. Add search scripts (search_data.js, search_logic.js) before other scripts
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


def fix_practice_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    lesson_id = get_lesson_id(filepath)
    if not lesson_id:
        return False

    # 1. Add "Next Up: Quiz" navigation section before </div> that closes practice-content-view
    # The practice-content-view contains game-hub + game-containers, we add nav after the last game container
    if 'Next Up: Quiz' not in content:
        nav_section = (
            f'\n<div class="Practice-actions" style="margin-top:2rem;display:flex;justify-content:flex-end;width:100%;">\n'
            f'<a class="side-button" href="Lesson{lesson_id}_Quiz.html" '
            f'style="text-align:center; text-decoration:none; display:block;">Next Up: Quiz</a>\n'
            f'</div>\n'
        )
        # Insert before the closing </div> of practice-content-view, which is right before </main>
        # Find the practice-content-view's closing </div>
        # Structure: <div id="practice-content-view"> ... </div> </main>
        pcv_start = content.find('<div id="practice-content-view">')
        if pcv_start != -1:
            # Find its matching closing </div> by tracking nesting
            depth = 0
            i = pcv_start
            pcv_close = -1
            while i < len(content):
                if content[i:i+4] == '<div':
                    depth += 1
                elif content[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        pcv_close = i
                        break
                i += 1
            if pcv_close != -1:
                content = content[:pcv_close] + nav_section + content[pcv_close:]

    # 2. Add search scripts before </main> closing tag, if not present
    if 'search_data.js' not in content:
        # Insert after </main>
        content = content.replace('</main>', '</main>\n' + SEARCH_SCRIPTS)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    files = glob.glob(os.path.join(BASE, "Unit*", "Lesson*_Practice.html"))
    files.sort()

    fixed = 0
    errors = []

    for filepath in files:
        try:
            if fix_practice_file(filepath):
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
