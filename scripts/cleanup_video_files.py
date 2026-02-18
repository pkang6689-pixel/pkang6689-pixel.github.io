"""
Cleanup Video files: Replace dynamic toggle-based view switching with simple href links.
Removes embedded Summary, Practice, and Quiz views from _Video.html files.
Removes unnecessary inline scripts and external script tags related to games/quizzes.
"""

import os
import re
import glob

base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                        "ArisEdu Project Folder", "PhysicsLessons")

video_files = glob.glob(os.path.join(base_dir, "Unit*", "Lesson*_Video.html"))
print(f"Found {len(video_files)} Video files\n")

modified = 0
errors = []

for filepath in sorted(video_files):
    filename = os.path.basename(filepath)
    match = re.match(r'Lesson(\d+\.\d+)_Video\.html', filename)
    if not match:
        errors.append(f"Could not extract lesson number from {filename}")
        continue
    lesson_num = match.group(1)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Replace toggleToSummary button with href link
    content = content.replace(
        '<button class="side-button" onclick="toggleToSummary(event)">Next Up: Summary</button>',
        f'<a class="side-button" href="Lesson{lesson_num}_Summary.html">Next Up: Summary</a>'
    )

    # 2. Remove embedded views (Summary, Practice, Quiz) - everything from
    #    the summary comment to right before </main>
    content = re.sub(
        r'\s*<!-- Embedded Summary View.*?(?=</main>)',
        '\n',
        content,
        flags=re.DOTALL
    )

    # 3. Remove practice_games.js and quiz_ui.js script tags
    content = re.sub(r'\s*<script src="[^"]*practice_games\.js[^"]*"></script>', '', content)
    content = re.sub(r'\s*<script src="[^"]*quiz_ui\.js[^"]*"></script>', '', content)

    # 4. Remove inline script block with game switching (switchToClimb, switchToFlashcards)
    content = re.sub(
        r'\s*<script>\s*\n\s*window\.switchToClimb.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # 5. Remove inline script block with Climb Game Logic
    content = re.sub(
        r'\s*<script>\s*\n// Climb Game Logic.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # 6. Remove blocks_puzzle.js and game_utils.js script tags
    content = re.sub(r'\s*<script src="[^"]*blocks_puzzle\.js[^"]*"></script>', '', content)
    content = re.sub(r'\s*<script src="[^"]*game_utils\.js[^"]*"></script>', '', content)

    # 7. Clean up extra blank lines (3+ consecutive newlines -> 2)
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        modified += 1
        removed = len(original) - len(content)
        print(f"  OK: {filename} ({len(original)} -> {len(content)} chars, -{removed})")
    else:
        print(f"  UNCHANGED: {filename}")

print(f"\nModified: {modified}/{len(video_files)} files")
if errors:
    print(f"\nErrors:")
    for e in errors:
        print(f"  - {e}")
