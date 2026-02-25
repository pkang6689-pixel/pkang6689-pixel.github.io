#!/usr/bin/env python3
"""Verify the final 2 long strings are properly stored and will be matched."""
import re

TRANS_FILE = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"
with open(TRANS_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Extract keys using regex that handles escaped quotes
existing = set()
for m in re.finditer(r'^\s*"((?:[^"\\]|\\.)*)"\s*:', content, re.MULTILINE):
    key = m.group(1).replace('\\"', '"').replace('\\\\', '\\')
    existing.add(key)

print(f"Total keys (improved regex): {len(existing)}")

# The actual strings as they appear in the HTML (extracted by the parser)
test1 = 'Selection of objects where ORDER DOESN\'T MATTER. C(n,r) = n!/(r!(n-r)!), also written "n choose r". Always C(n,r) ≤ P(n,r). Example: choosing 3 of 5 books: C(5,3) = 5!/(3!2!) = 10.'
test2 = 'Occur at x-values where denominator is zero (and not cancelled by numerator). These are "forbidden" x-values. Graph approaches these lines but never touches them. Plot as dashed vertical lines.'

print(f"Test1 in existing: {test1 in existing}")
print(f"Test2 in existing: {test2 in existing}")

# Also check if they exist in the file content directly
if "ORDER DOESN" in content:
    print("ORDER DOESN found in file")
if "forbidden" in content:
    print('"forbidden" found in file')

# Show how the keys appear for these entries
for line_no, line in enumerate(content.split('\n'), 1):
    if 'ORDER DOESN' in line and '":' in line:
        print(f"\nLine {line_no}: {line[:200]}...")
    if '"forbidden"' in line and '":' in line:
        print(f"\nLine {line_no}: {line[:200]}...")
