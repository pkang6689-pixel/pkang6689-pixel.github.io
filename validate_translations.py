#!/usr/bin/env python3
"""Validate global_translations.js for syntax errors."""
import re
import json

with open('ArisEdu Project Folder/scripts/global_translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the translations object
match = re.search(r'const translations = (\{.*?\});', content, re.DOTALL)
if not match:
    print("ERROR: Could not find translations object!")
    exit(1)

obj_str = match.group(1)

# Try to parse as JSON
try:
    parsed = json.loads(obj_str)
    print(f"Successfully parsed: {len(parsed)} entries")
except json.JSONDecodeError as e:
    print(f"JSON parse error at position {e.pos}: {e.msg}")
    # Show context
    start = max(0, e.pos - 200)
    end = min(len(obj_str), e.pos + 200)
    before = obj_str[start:e.pos]
    after = obj_str[e.pos:end]
    
    # Count line number within the object
    line_in_obj = obj_str[:e.pos].count('\n') + 1
    print(f"At line ~{line_in_obj} within translations object")
    print(f"\n--- BEFORE ERROR ---")
    print(before[-300:])
    print(f"\n--- >>> ERROR HERE <<< ---")
    print(after[:300])

# Also check for trailing backslashes that escape closing quotes
lines = content.split('\n')
problem_lines = []
for i, line in enumerate(lines, 1):
    s = line.strip()
    if not s or not s.startswith('"'):
        continue
    # Check if value ends with odd number of backslashes before closing quote
    # Pattern: value like "text\" which means the backslash escapes the quote
    stripped = s.rstrip(',')
    if stripped.endswith('"'):
        # Check what's before the closing quote
        inner = stripped[:-1]  # remove closing quote
        trailing_backslashes = 0
        for c in reversed(inner):
            if c == '\\':
                trailing_backslashes += 1
            else:
                break
        if trailing_backslashes % 2 == 1:
            problem_lines.append((i, line.strip()[:120]))

if problem_lines:
    print(f"\nFound {len(problem_lines)} lines with unescaped trailing backslash:")
    for line_no, ctx in problem_lines:
        print(f"  Line {line_no}: {ctx}")
else:
    print("\nNo trailing backslash issues found.")
