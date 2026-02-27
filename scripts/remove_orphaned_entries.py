#!/usr/bin/env python3
"""
Remove all orphaned translation entries
"""

import re

filepath = "ArisEdu Project Folder/scripts/global_translations.js"

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where orphaned entries start (after first `};` that closes getTranslationDebugData)
# These are lines that look like: `    "Lesson ...": "..."`
# and are NOT inside the translations object

# Find the line with `};` that closes the function
debug_func_close = None
for i, line in enumerate(lines):
    if '};' in line and i > 32770:  # Look for the closing
        debug_func_close = i
        break

print(f"Found function close at line {debug_func_close + 1}")

# Find the next real code line (not a translation entry)
next_real_code = None
for i in range(debug_func_close + 1, len(lines)):
    line = lines[i].strip()
    # Skip empty lines and orphaned translation entries
    if not line or line.startswith('"Lesson'):
        continue
    elif line.startswith('"Complex Numbers') or line.startswith('"Advanced Linear'):
        # Still an orphaned entry
        continue
    elif 'if (document.readyState' in line or 'if (lang &&' in line or 'var lang' in line or 'document.addEventListener' in line:
        next_real_code = i
        break

print(f"Found next real code at line {next_real_code + 1}")

if debug_func_close and next_real_code:
    # Remove lines between them
    del lines[debug_func_close + 1:next_real_code]
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"✅ Removed {next_real_code - debug_func_close - 1} orphaned lines")
else:
    print("❌ Could not find boundaries")
