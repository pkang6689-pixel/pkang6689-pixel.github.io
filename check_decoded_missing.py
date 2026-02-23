#!/usr/bin/env python3
"""Properly decode all HTML entities in missing strings, check if decoded versions
exist in global_translations.js, and add any truly missing ones."""
import json
import re
import html
from pathlib import Path

# Load missing strings
with open('missing_lesson_notes_strings.json', 'r', encoding='utf-8') as f:
    missing_raw = json.load(f)

print(f"Missing strings with HTML entities: {len(missing_raw)}\n")

# Decode HTML entities and fix span artifacts
def clean_string(s):
    # Fix nested span artifacts like: Triangle">Isosceles Triangle
    s = re.sub(r'(\w+)">', '', s)
    # Decode ALL HTML entities
    s = html.unescape(s)
    return s.strip()

decoded = []
for raw in missing_raw:
    cleaned = clean_string(raw)
    decoded.append((raw, cleaned))

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

# Check decoded versions
def normalize(s):
    return ' '.join(s.split())

global_norm = {normalize(k): k for k in global_trans}

still_missing = []
matched_after_decode = 0

for raw, cleaned in decoded:
    norm = normalize(cleaned)
    if cleaned in global_trans:
        matched_after_decode += 1
    elif norm in global_norm:
        matched_after_decode += 1
    else:
        still_missing.append(cleaned)
        
print(f"Matched after decoding HTML entities: {matched_after_decode}")
print(f"Still truly missing: {len(still_missing)}")

if still_missing:
    print(f"\nTruly missing strings:")
    print("-" * 80)
    for i, s in enumerate(still_missing, 1):
        print(f"  {i}. {s}")
    
    # Save truly missing
    with open('truly_missing_strings.json', 'w', encoding='utf-8') as f:
        json.dump(still_missing, f, ensure_ascii=False, indent=2)
    print(f"\nSaved to truly_missing_strings.json")
else:
    print("\n✓ All strings already exist in global_translations.js after proper decoding!")
