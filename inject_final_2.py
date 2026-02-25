#!/usr/bin/env python3
"""Add the final 2 long summary strings."""
import re

TRANS_FILE = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"

with open(TRANS_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# The two strings with their translations
entries = [
    ('Selection of objects where ORDER DOESN\'T MATTER. C(n,r) = n!/(r!(n-r)!), also written "n choose r". Always C(n,r) ≤ P(n,r). Example: choosing 3 of 5 books: C(5,3) = 5!/(3!2!) = 10.',
     '选择对象时顺序不重要。C(n,r) = n!/(r!(n-r)!)，也写作"n选r"。始终 C(n,r) ≤ P(n,r)。例如：从5本书中选3本：C(5,3) = 5!/(3!2!) = 10。'),
    ('Occur at x-values where denominator is zero (and not cancelled by numerator). These are "forbidden" x-values. Graph approaches these lines but never touches them. Plot as dashed vertical lines.',
     '出现在分母为零（且未被分子约去）的x值处。这些是"禁止"的x值。图形趋近这些线但永远不触碰它们。画为虚线垂直线。'),
]

# Build insertion lines
insertion_lines = []
for key, val in entries:
    k_js = key.replace('\\', '\\\\').replace('"', '\\"')
    v_js = val.replace('\\', '\\\\').replace('"', '\\"')
    insertion_lines.append(f'    "{k_js}": "{v_js}",')

insertion = '\n'.join(insertion_lines) + '\n'

# Insert before the }; that closes the translations object
# Find the last "...": "...", line then the }; after it
lines = content.split('\n')
last_entry = None
for i, line in enumerate(lines):
    if re.match(r'^\s*".*?"\s*:', line):
        last_entry = i

if last_entry is not None:
    for i in range(last_entry + 1, len(lines)):
        if lines[i].strip() == '};':
            # Insert before this line
            new_lines = lines[:i] + insertion.strip().split('\n') + lines[i:]
            with open(TRANS_FILE, "w", encoding="utf-8") as f:
                f.write('\n'.join(new_lines))
            print(f"Added 2 translations at line {i+1}")
            print(f"Total lines: {len(new_lines)}")
            break
else:
    print("ERROR: Could not find entry point")
