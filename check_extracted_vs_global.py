#!/usr/bin/env python3
"""Check if all extracted lesson notes strings are in global_translations.js"""
import json
import re
from pathlib import Path

# Load extracted data
with open('lesson_notes_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# Load global translations
global_js = Path('ArisEdu Project Folder/scripts/global_translations.js')
with open(global_js, 'r', encoding='utf-8') as f:
    content = f.read()

js_pattern = r'const translations = \{(.*?)\s*\};'
match = re.search(js_pattern, content, re.DOTALL)

global_trans = {}
if match:
    translations_str = match.group(1)
    pair_pattern = r'"((?:[^"\\]|\\.)*)"\s*:\s*"((?:[^"\\]|\\.)*)"\s*(?:,|$)'
    for m in re.finditer(pair_pattern, translations_str):
        try:
            key = json.loads('"' + m.group(1) + '"')
            val = json.loads('"' + m.group(2) + '"')
            global_trans[key] = val
        except:
            pass

print(f"Global translations: {len(global_trans)} entries\n")

# Collect all unique EN strings from extracted translation pairs
all_extracted_pairs = {}
for entry in extracted:
    for en, zh in entry.get('translation_pairs', []):
        if en and zh:
            all_extracted_pairs[en] = zh

print(f"Unique extracted translation pairs: {len(all_extracted_pairs)}\n")

# Check which are missing
missing = []
present = []
for en, zh in all_extracted_pairs.items():
    if en in global_trans:
        present.append(en)
    else:
        missing.append((en, zh))

print(f"✓ Present in global_translations: {len(present)}")
print(f"✗ Missing from global_translations: {len(missing)}")

if missing:
    print(f"\n{'='*80}")
    print("MISSING TRANSLATIONS:")
    print('='*80)
    for i, (en, zh) in enumerate(missing, 1):
        print(f"\n{i}. EN: {en}")
        print(f"   ZH: {zh}")
else:
    print("\n✓ All extracted translations are already in global_translations.js!")
