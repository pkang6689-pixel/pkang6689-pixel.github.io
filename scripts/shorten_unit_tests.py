#!/usr/bin/env python3
"""
shorten_unit_tests.py
Shortens Unit Test HTML files by:
1. Removing inline practice games HTML (now injected by unit_test.js)
2. Removing inline style blocks for quiz finish screen (now in unit_test.js)
3. Removing quiz finish screen HTML (now injected by unit_test.js)
4. Removing all inline <script> blocks (game switching, climb logic, showQuiz/showPractice, checkQuizCompletion)
5. Removing redundant search_data.js, search_logic.js, game_utils.js script tags
6. Adding unit_test.js script reference
"""

import os
import re
import glob

BASE = os.path.join(os.path.dirname(__file__), '..', 'ArisEdu Project Folder', 'ChemistryLessons')
BASE = os.path.normpath(BASE)

def shorten_test_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_lines = content.count('\n')

    # Extract the title
    title_match = re.search(r'<title>(.*?)</title>', content)
    page_title = title_match.group(1) if title_match else 'Unit Test'

    # Extract unit number for the practice title
    unit_match = re.search(r'Unit\s*(\d+)', page_title)
    unit_label = f'Unit {unit_match.group(1)}' if unit_match else page_title.replace(': Unit Test', '')

    # ===== Build the new file =====

    # 1. Extract head section, remove the dark-mode quiz finish styles
    head_match = re.search(r'(<head>.*?</head>)', content, re.DOTALL)
    if not head_match:
        print(f"  SKIP (no <head>): {filepath}")
        return

    head = head_match.group(1)

    # Remove the dark mode quiz finish screen style block
    head = re.sub(
        r'<style>\s*/\*\s*Dark Mode Support for Quiz Finish Screen\s*\*/.*?</style>',
        '',
        head,
        flags=re.DOTALL
    )

    # 2. Extract quiz content view (the unique part)
    quiz_start = content.find('<div id="quiz-content-view"')
    if quiz_start == -1:
        print(f"  SKIP (no quiz-content-view): {filepath}")
        return

    # Find the quiz form end - look for </form>
    form_end = content.find('</form>', quiz_start)
    if form_end == -1:
        print(f"  SKIP (no </form>): {filepath}")
        return

    # Get from quiz-content-view start through </form>
    quiz_section = content[quiz_start:form_end + len('</form>')]

    # 3. Build the shortened HTML
    new_html = f'''<!DOCTYPE html>

<html class="h-full" lang="en">{head}
<body class="dark-mode h-full">
<script src="../../scripts/taskbar.js"></script>
<main class="main-container">
<div id="practice-content-view">
<h2 class="page-title">{unit_label} Practice</h2>
</div>

{quiz_section}
</div>
</div>
</div>
</main>
<script src="../../scripts/lesson_video.js"></script>
<script src="../../scripts/quiz_ui.js"></script>
<script src="../../scripts/unit_test.js"></script>
<script src="../../scripts/blocks_puzzle.js"></script>
<script src="/ArisEdu Project Folder/scripts/game_utils.js"></script>
</body></html>
'''

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

    new_lines = new_html.count('\n')
    print(f"  {os.path.basename(filepath)}: {original_lines} -> {new_lines} lines (saved {original_lines - new_lines})")


def main():
    # Find all non-archive test files
    test_files = []
    for unit_dir in sorted(glob.glob(os.path.join(BASE, 'Unit*'))):
        if not os.path.isdir(unit_dir):
            continue
        for f in glob.glob(os.path.join(unit_dir, '*_Test.html')):
            test_files.append(f)

    print(f"Found {len(test_files)} unit test files to shorten:\n")

    for filepath in sorted(test_files):
        rel = os.path.relpath(filepath, BASE)
        print(f"Processing: {rel}")
        shorten_test_file(filepath)

    print(f"\nDone! Shortened {len(test_files)} files.")
    print("All shared code now lives in scripts/unit_test.js")


if __name__ == '__main__':
    main()
