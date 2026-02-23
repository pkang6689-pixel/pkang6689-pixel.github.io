#!/usr/bin/env python3
"""Fix Chinese quote characters in the translation script that break Python string parsing."""
import re

with open('add_geometry_summary_translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Chinese left/right double quotes with their unicode escape sequences
# \u201c = left double quotation mark
# \u201d = right double quotation mark  
# \u2026 = horizontal ellipsis
# \u300a \u300b = angle brackets

# We need to be careful - only replace these inside string literals (translation values)
# Strategy: replace ALL Chinese quotes with escaped versions
content = content.replace('\u201c', '\\u201c')
content = content.replace('\u201d', '\\u201d')
content = content.replace('\u2026', '\\u2026')

with open('add_geometry_summary_translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Chinese quote characters in add_geometry_summary_translations.py")
