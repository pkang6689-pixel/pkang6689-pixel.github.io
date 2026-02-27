#!/usr/bin/env python3
"""Check chem.html strings against all translation files (Chinese, Spanish, Hindi)."""
import re, os

BASE = "ArisEdu Project Folder"

# Read chem.html
with open(os.path.join(BASE, "chem.html"), "r", encoding="utf-8") as f:
    chem = f.read()

# Extract translatable strings
popup_strings = re.findall(r"showLessonPopup\(event,\s*'([^']+)'\)", chem)
unit_labels = list(set(re.findall(r'<text[^>]*>([^<]+)</text>', chem)))
title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', chem)
page_title = title_match.group(1).strip() if title_match else None

all_strings = []
if page_title:
    all_strings.append(("Page Title", page_title))
for u in sorted(unit_labels):
    all_strings.append(("Unit Label", u))
for s in popup_strings:
    all_strings.append(("Lesson Popup", s))

# Read translation JS files
def read_translation_keys(filepath):
    """Extract all English keys from a translation JS file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Match "English text": "translation" patterns
    keys = set()
    for m in re.finditer(r'"([^"]+)"\s*:\s*"', content):
        keys.add(m.group(1))
    # Also match 'English text': 'translation' patterns  
    for m in re.finditer(r"'([^']+)'\s*:\s*'", content):
        keys.add(m.group(1))
    return keys

chinese_keys = read_translation_keys(os.path.join(BASE, "scripts", "global_translations.js"))
spanish_keys = read_translation_keys(os.path.join(BASE, "scripts", "spanish_translations.js"))
hindi_keys = read_translation_keys(os.path.join(BASE, "scripts", "hindi_translations.js"))

print(f"Translation keys loaded: Chinese={len(chinese_keys)}, Spanish={len(spanish_keys)}, Hindi={len(hindi_keys)}")
print()

# Check each string
missing_chinese = []
missing_spanish = []
missing_hindi = []

for category, text in all_strings:
    if text not in chinese_keys:
        missing_chinese.append((category, text))
    if text not in spanish_keys:
        missing_spanish.append((category, text))
    if text not in hindi_keys:
        missing_hindi.append((category, text))

print(f"=== MISSING CHINESE TRANSLATIONS ({len(missing_chinese)}/{len(all_strings)}) ===")
for cat, text in missing_chinese:
    print(f"  [{cat}] {text}")

print(f"\n=== MISSING SPANISH TRANSLATIONS ({len(missing_spanish)}/{len(all_strings)}) ===")
for cat, text in missing_spanish:
    print(f"  [{cat}] {text}")

print(f"\n=== MISSING HINDI TRANSLATIONS ({len(missing_hindi)}/{len(all_strings)}) ===")
for cat, text in missing_hindi:
    print(f"  [{cat}] {text}")

# Summary
print(f"\n=== SUMMARY ===")
print(f"Total translatable strings in chem.html: {len(all_strings)}")
print(f"Missing Chinese: {len(missing_chinese)}")
print(f"Missing Spanish: {len(missing_spanish)}")
print(f"Missing Hindi:   {len(missing_hindi)}")
