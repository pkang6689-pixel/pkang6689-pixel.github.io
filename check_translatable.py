#!/usr/bin/env python3
"""Check which HTML files have translatable elements."""
from pathlib import Path
import re

html_files = sorted(Path('ArisEdu Project Folder').rglob('*.html'))
has_translatable = []
no_translatable = []

for f in html_files:
    content = f.read_text(encoding='utf-8', errors='ignore')
    count = content.count('class="translatable"')
    if count > 0:
        has_translatable.append((str(f), count))
    else:
        no_translatable.append(str(f))

print(f"Files WITH translatable elements: {len(has_translatable)}")
for f, c in has_translatable[:30]:
    print(f"  {c:4d} elements: {f}")
if len(has_translatable) > 30:
    print(f"  ... and {len(has_translatable)-30} more")

print(f"\nFiles WITHOUT translatable elements: {len(no_translatable)}")
for f in no_translatable[:15]:
    print(f"  {f}")
if len(no_translatable) > 15:
    print(f"  ... and {len(no_translatable)-15} more")
