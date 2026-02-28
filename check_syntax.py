#!/usr/bin/env python3
import re

files = [
    'ArisEdu Project Folder/scripts/global_translations.js',
    'ArisEdu Project Folder/scripts/spanish_translations.js', 
    'ArisEdu Project Folder/scripts/hindi_translations.js'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Look for lines that should have commas but don't
    errors = []
    for i, line in enumerate(lines, 1):
        # Skip comments and empty lines
        if line.strip().startswith('//') or not line.strip():
            continue
        # Check if line ends with a quote but no comma before the newline
        # Pattern: "key": "value" at end of line
        if re.search(r'^\s+"[^"]+"\s*:\s*"[^"]*"\s*$', line):
            errors.append((i, line.strip()[:80]))
    
    if errors:
        print(f'{filepath}: Found {len(errors)} lines missing commas')
        for line_no, content in errors[:10]:
            print(f'  Line {line_no}: {content}...')
    else:
        print(f'✓ {filepath.split("/")[-1]}: No missing commas detected')
