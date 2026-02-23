#!/usr/bin/env python3
"""Extract all plain text lines from lesson_notes_extracted.txt and check against global_translations.js.
Then add missing ones to global_translations.js."""
import json
import re
from pathlib import Path

# ── Step 1: Parse all plain text lines from the extracted file ──
print("Step 1: Parsing plain text lines from lesson_notes_extracted.txt...")

plain_text_lines = []
in_plain_text = False

with open('lesson_notes_extracted.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        
        if line.startswith('PLAIN TEXT:'):
            in_plain_text = True
            continue
        
        if line.startswith('TRANSLATIONS FOUND') or line.startswith('(No translations found'):
            in_plain_text = False
            continue
        
        if line.startswith('[') and ']' in line and ('Unit' in line or 'Lesson' in line):
            in_plain_text = False
            continue
        
        if line.startswith('---') or line.startswith('==='):
            in_plain_text = False
            continue
        
        if in_plain_text and line.strip():
            cleaned = line.strip()
            # Skip artifacts from nested HTML spans
            cleaned = cleaned.replace('Collinear points">Non-', 'Non-')
            cleaned = cleaned.replace('Coplanar points">Non-', 'Non-')
            # Decode common HTML entities
            cleaned = cleaned.replace('&#x2190;&#x2192;', '←→')
            cleaned = cleaned.replace('&#x2245;', '≅')
            cleaned = cleaned.replace('&#x2260;', '≠')
            cleaned = cleaned.replace('&#x00b0;', '°')
            cleaned = cleaned.replace('&amp;', '&')
            cleaned = cleaned.replace('&lt;', '<')
            cleaned = cleaned.replace('&gt;', '>')
            cleaned = cleaned.replace('&quot;', '"')
            cleaned = cleaned.replace('&#x2019;', "'")
            cleaned = cleaned.replace('&#x201c;', '"')
            cleaned = cleaned.replace('&#x201d;', '"')
            cleaned = cleaned.replace('&#x2013;', '–')
            cleaned = cleaned.replace('&#x2014;', '—')
            cleaned = cleaned.replace('&#x00d7;', '×')
            cleaned = cleaned.replace('&#x00f7;', '÷')
            cleaned = cleaned.replace('&#x221a;', '√')
            cleaned = cleaned.replace('&#x03b8;', 'θ')
            cleaned = cleaned.replace('&#x03c0;', 'π')
            cleaned = cleaned.replace('&#x2248;', '≈')
            cleaned = cleaned.replace('&#x2264;', '≤')
            cleaned = cleaned.replace('&#x2265;', '≥')
            cleaned = cleaned.replace('&#x00b2;', '²')
            cleaned = cleaned.replace('&#x00b3;', '³')
            cleaned = cleaned.replace('&#x2081;', '₁')
            cleaned = cleaned.replace('&#x2082;', '₂')
            cleaned = cleaned.replace('&#x2220;', '∠')
            cleaned = cleaned.replace('&#x22a5;', '⊥')
            cleaned = cleaned.replace('&#x2225;', '∥')
            cleaned = cleaned.replace('&#x25b3;', '△')
            cleaned = cleaned.replace('&#x00bd;', '½')
            
            if len(cleaned) > 1:  # Skip single characters
                plain_text_lines.append(cleaned)

# Deduplicate while preserving order
seen = set()
unique_lines = []
for line in plain_text_lines:
    if line not in seen:
        seen.add(line)
        unique_lines.append(line)

print(f"  Parsed {len(plain_text_lines)} total lines")
print(f"  Unique lines: {len(unique_lines)}")

# ── Step 2: Load global translations ──
print("\nStep 2: Loading global_translations.js...")

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

print(f"  Current global translations: {len(global_trans)} entries")

# ── Step 3: Find missing lines ──
print("\nStep 3: Finding missing translations...")

# Also check with normalized whitespace
def normalize(s):
    return ' '.join(s.split())

global_normalized = {normalize(k): k for k in global_trans}

missing = []
present = 0
for line in unique_lines:
    norm = normalize(line)
    if line in global_trans or norm in global_normalized:
        present += 1
    else:
        missing.append(line)

print(f"  Already present: {present}")
print(f"  Missing: {len(missing)}")

# Save missing lines for reference
with open('missing_lesson_notes_strings.json', 'w', encoding='utf-8') as f:
    json.dump(missing, f, ensure_ascii=False, indent=2)

print(f"\n✓ Saved {len(missing)} missing strings to missing_lesson_notes_strings.json")

# Print first 30 missing for preview
if missing:
    print(f"\nFirst 30 missing strings:")
    print("-" * 80)
    for i, s in enumerate(missing[:30], 1):
        print(f"  {i}. {s}")
