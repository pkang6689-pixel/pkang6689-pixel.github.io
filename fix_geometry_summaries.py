"""
Fix Geometry Summary files to match the Physics/Bio format:
1. Wrap content inside <div class="lesson-notes"> ... </div>
2. Replace <button class="action-button"> with <a class="side-button"> link
3. Remove inline styles from summary-actions div
4. Change button text from "Go to Practice" to "Next Up: Play"
5. Add search scripts and game_utils.js before </body>
"""

import os
import re
import glob

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\GeometryLessons"

BOTTOM_SCRIPTS = """\

<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
<script src="/ArisEdu Project Folder/scripts/game_utils.js"></script>"""


def get_lesson_id(filepath):
    basename = os.path.basename(filepath)
    m = re.search(r'Lesson(\d+\.\d+)', basename)
    return m.group(1) if m else None


def fix_summary_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    lesson_id = get_lesson_id(filepath)
    if not lesson_id:
        return False

    # 1. Add <div class="lesson-notes"> wrapper around content inside diagram-card
    # The content sits between <div class="diagram-card"> and <div class="summary-actions">
    # We need to wrap everything between those two in <div class="lesson-notes">...</div>
    if 'lesson-notes' not in content:
        # Find the diagram-card opening and summary-actions
        dc_match = re.search(r'(<div class="diagram-card">)\s*\n', content)
        sa_match = re.search(r'\n(\s*<div class="summary-actions")', content)
        
        if dc_match and sa_match:
            dc_end = dc_match.end()
            sa_start = sa_match.start()
            
            # Extract the content between diagram-card and summary-actions
            inner_content = content[dc_end:sa_start]
            
            # Wrap it in lesson-notes
            wrapped = '\n<div class="lesson-notes">\n' + inner_content.strip() + '\n</div>\n'
            
            content = content[:dc_end] + wrapped + content[sa_start:]

    # 2. Replace the summary-actions div and button with the correct format
    # Old: <div class="summary-actions" style="..."><button class="action-button" onclick="...">Go to Practice</button></div>
    # New: <div class="summary-actions"><a class="side-button" href="LessonX.X_Practice.html" style="text-align:center; text-decoration:none; display:block;">Next Up: Play</a></div>
    old_actions_pattern = r'<div class="summary-actions"[^>]*>.*?</div>'
    new_actions = (
        f'<div class="summary-actions">\n'
        f'<a class="side-button" href="Lesson{lesson_id}_Practice.html" '
        f'style="text-align:center; text-decoration:none; display:block;">Next Up: Play</a>\n'
        f'</div>'
    )
    content = re.sub(old_actions_pattern, new_actions, content, flags=re.DOTALL)

    # 3. Add bottom scripts before </body> if not present
    if 'search_data.js' not in content:
        content = content.replace('</body>', BOTTOM_SCRIPTS + '\n</body>')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    files = glob.glob(os.path.join(BASE, "Unit*", "Lesson*_Summary.html"))
    files.sort()

    fixed = 0
    errors = []

    for filepath in files:
        try:
            if fix_summary_file(filepath):
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
