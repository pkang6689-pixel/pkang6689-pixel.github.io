import os
import re
import glob

base = r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\CourseFiles'
files = glob.glob(os.path.join(base, '**', '*_Test_Practice.html'), recursive=True)

print(f'Found {len(files)} files')

changed = 0
skipped = 0

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()

    # Pattern: div with only one "Back to" button at the top
    # Match the entire div block containing just the Back to button
    top_div_pattern = re.compile(
        r'<div style="display:flex;gap:1rem;margin-bottom:1rem;flex-wrap:wrap;">\s*'
        r'(<button class="side-button" onclick="window\.location\.href=\'([^\']+)\'" '
        r'style="font-size:0\.9rem;padding:0\.5rem 1rem;">Back to ([^<]+)</button>)\s*'
        r'</div>\s*',
        re.DOTALL
    )

    # Pattern: Practice-actions div with Start Unit Test button
    practice_actions_pattern = re.compile(
        r'(<div class="Practice-actions" style="margin-top:2rem;display:flex;justify-content:flex-end;width:100%;">\s*)'
        r'(<button class="side-button" onclick="window\.location\.href=\'[^\']+\'" style="text-align:center;">Start Unit Test</button>)',
        re.DOTALL
    )

    # Also handle standalone Start Unit Test button (no Practice-actions wrapper)
    standalone_button_pattern = re.compile(
        r'(<button class="side-button" onclick="window\.location\.href=\'[^\']+\'" style="text-align:center;">Start Unit Test</button>)',
        re.DOTALL
    )

    top_match = top_div_pattern.search(content)
    bottom_match = practice_actions_pattern.search(content)
    standalone_match = standalone_button_pattern.search(content)

    if not top_match:
        print(f'  SKIP (no top back-button): {os.path.basename(filepath)}')
        skipped += 1
        continue

    back_button_html = top_match.group(1)

    if bottom_match:
        # Remove the top div block
        new_content = top_div_pattern.sub('', content, count=1)
        # Insert back button before Start Unit Test button in Practice-actions
        new_content = practice_actions_pattern.sub(
            r'\1' + back_button_html + '\n' + r'\2',
            new_content,
            count=1
        )
    elif standalone_match:
        # Remove the top div block
        new_content = top_div_pattern.sub('', content, count=1)
        # Wrap standalone button + back button in a flex div
        new_content = standalone_button_pattern.sub(
            '<div style="display:flex;gap:1rem;margin-top:2rem;justify-content:flex-end;width:100%;">'
            + back_button_html + '\n'
            + r'\1'
            + '</div>',
            new_content,
            count=1
        )
    else:
        print(f'  SKIP (no Practice-actions div): {os.path.basename(filepath)}')
        skipped += 1
        continue

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        changed += 1
        print(f'  UPDATED: {os.path.relpath(filepath, base)}')
    else:
        print(f'  NO CHANGE: {os.path.basename(filepath)}')
        skipped += 1

print(f'\nDone. Changed: {changed}, Skipped: {skipped}')
