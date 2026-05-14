import os
import glob
import re

base = r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\CourseFiles'
files = glob.glob(os.path.join(base, '**', '*_Test_Practice.html'), recursive=True)

top_pattern = re.compile(
    r'<div style="display:flex;gap:1rem;margin-bottom:1rem;flex-wrap:wrap;">\s*'
    r'<button class="side-button" onclick="window\.location\.href=\'[^\']+\'" '
    r'style="font-size:0\.9rem;padding:0\.5rem 1rem;">Back to ',
    re.DOTALL
)

still_at_top = []
for f in files:
    with open(f, encoding='utf-8') as fh:
        content = fh.read()
    if top_pattern.search(content):
        still_at_top.append(f)

print(f'Files still with Back to at top: {len(still_at_top)}')
for f in still_at_top[:20]:
    print(' ', os.path.relpath(f, base))
