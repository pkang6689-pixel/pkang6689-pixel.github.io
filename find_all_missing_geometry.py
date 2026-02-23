#!/usr/bin/env python3
"""Extract ALL data-en values from GeometryLessons Summary HTML files and check
which are missing from global_translations.js. Add any missing ones."""
import json
import re
import html as html_mod
from pathlib import Path

# ── Step 1: Extract all data-en values from HTML files ──
print("Step 1: Extracting all data-en values from GeometryLessons HTML files...")

geometry_path = Path('ArisEdu Project Folder/GeometryLessons')
html_files = sorted(geometry_path.rglob('*_Summary.html'))

all_data_en = set()
by_file = {}

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all data-en="..." values
    matches = re.findall(r'data-en="([^"]*)"', content)
    
    file_strings = set()
    for m in matches:
        decoded = html_mod.unescape(m)
        file_strings.add(decoded)
        all_data_en.add(decoded)
    
    rel = html_file.relative_to(geometry_path)
    by_file[str(rel)] = len(file_strings)

print(f"  Scanned {len(html_files)} summary files")
print(f"  Found {len(all_data_en)} unique data-en values\n")

# ── Step 2: Also extract plain text that's NOT wrapped in translatable spans ──
print("Step 2: Extracting non-wrapped text from lesson-notes divs...")

lesson_notes_pattern = r'<div[^>]*class="lesson-notes"[^>]*>(.*?)</div>'
non_wrapped_texts = set()

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    notes_matches = re.findall(lesson_notes_pattern, content, re.DOTALL)
    for notes_html in notes_matches:
        # Extract text from <p>, <li>, <h3>, <h4> tags
        # Get full text between tags
        tag_pattern = r'<(p|li|h[1-6]|td|th)[^>]*>(.*?)</\1>'
        for tag_match in re.finditer(tag_pattern, notes_html, re.DOTALL):
            inner = tag_match.group(2)
            # Strip all HTML tags to get plain text
            plain = re.sub(r'<[^>]+>', '', inner)
            plain = html_mod.unescape(plain).strip()
            # Clean up span artifacts  
            plain = re.sub(r'\w+">', '', plain)
            if plain and len(plain) > 3:
                non_wrapped_texts.add(plain)

print(f"  Found {len(non_wrapped_texts)} unique plain text segments\n")

# Combine all strings
all_strings = all_data_en | non_wrapped_texts
print(f"Total combined unique strings: {len(all_strings)}\n")

# ── Step 3: Load global translations ──
print("Step 3: Loading global_translations.js...")

global_js = Path('ArisEdu Project Folder/scripts/global_translations.js')
with open(global_js, 'r', encoding='utf-8') as f:
    js_content = f.read()

js_pattern = r'const translations = \{(.*?)\s*\};'
match = re.search(js_pattern, js_content, re.DOTALL)

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

print(f"  Current translations: {len(global_trans)}\n")

# ── Step 4: Find missing ──
print("Step 4: Finding missing strings...")

def normalize(s):
    return ' '.join(s.split())

global_norm = {normalize(k): k for k in global_trans}

missing_data_en = []
for s in sorted(all_data_en):
    n = normalize(s)
    if s not in global_trans and n not in global_norm:
        missing_data_en.append(s)

missing_plain = []
for s in sorted(non_wrapped_texts):
    n = normalize(s)
    if s not in global_trans and n not in global_norm and s not in all_data_en:
        missing_plain.append(s)

print(f"  Missing data-en values (critical - used by translator): {len(missing_data_en)}")
print(f"  Missing plain text (not wrapped in translatable spans): {len(missing_plain)}")

# Save results
output = {
    "missing_data_en_count": len(missing_data_en),
    "missing_data_en": missing_data_en,
    "missing_plain_text_count": len(missing_plain),
    "missing_plain_text": missing_plain
}

with open('all_missing_geometry_strings.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\n✓ Saved to all_missing_geometry_strings.json")

if missing_data_en:
    print(f"\nMissing data-en values:")
    print("-" * 80)
    for i, s in enumerate(missing_data_en[:30], 1):
        print(f"  {i}. {s}")

if missing_plain:
    print(f"\nMissing plain text (first 30):")
    print("-" * 80)
    for i, s in enumerate(missing_plain[:30], 1):
        print(f"  {i}. {s}")
