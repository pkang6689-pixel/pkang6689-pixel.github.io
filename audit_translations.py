#!/usr/bin/env python3
"""Comprehensive audit: extract all translatable strings from chemistry lesson HTML files
and check them against Chinese, Spanish, and Hindi translation dictionaries."""
import re, os, glob

BASE = "ArisEdu Project Folder"

def read_translation_keys(filepath):
    """Extract all English keys from a translation JS file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    keys = set()
    for m in re.finditer(r'"([^"\\]+(?:\\.[^"\\]*)*)"\s*:\s*"', content):
        keys.add(m.group(1))
    return keys

chinese_keys = read_translation_keys(os.path.join(BASE, "scripts", "global_translations.js"))
spanish_keys = read_translation_keys(os.path.join(BASE, "scripts", "spanish_translations.js"))
hindi_keys = read_translation_keys(os.path.join(BASE, "scripts", "hindi_translations.js"))

print(f"Translation keys: Chinese={len(chinese_keys)}, Spanish={len(spanish_keys)}, Hindi={len(hindi_keys)}")

# Collect translatable strings from lesson HTML files
all_missing = {"chinese": {}, "spanish": {}, "hindi": {}}

def extract_translatable_text(filepath):
    """Extract visible English text from HTML lesson files."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    strings = set()
    
    # Title
    for m in re.finditer(r'<title>([^<]+)</title>', content):
        strings.add(m.group(1).strip())
    
    # H1, H2, H3 headings
    for m in re.finditer(r'<h[1-3][^>]*>([^<]+)</h[1-3]>', content):
        text = m.group(1).strip()
        if text and not text.startswith('{') and len(text) > 1:
            strings.add(text)
    
    # data-en attributes
    for m in re.finditer(r'data-en="([^"]+)"', content):
        strings.add(m.group(1).strip())
    
    # Paragraphs with direct educational text (skip very long ones)
    for m in re.finditer(r'<p[^>]*class="[^"]*translatable[^"]*"[^>]*>([^<]+)</p>', content):
        text = m.group(1).strip()
        if text and len(text) > 2 and len(text) < 300:
            strings.add(text)
    
    # Button/span text with translatable class
    for m in re.finditer(r'class="[^"]*translatable[^"]*"[^>]*>([^<]+)</', content):
        text = m.group(1).strip()
        if text and len(text) > 1:
            strings.add(text)
    
    # showLessonPopup strings
    for m in re.finditer(r"showLessonPopup\(event,\s*'([^']+)'\)", content):
        strings.add(m.group(1))
    
    return strings

# Process all course pages
course_pages = glob.glob(os.path.join(BASE, "*.html"))
for fp in course_pages:
    strings = extract_translatable_text(fp)
    for s in strings:
        if s not in chinese_keys:
            all_missing["chinese"].setdefault(os.path.basename(fp), []).append(s)
        if s not in spanish_keys:
            all_missing["spanish"].setdefault(os.path.basename(fp), []).append(s)
        if s not in hindi_keys:
            all_missing["hindi"].setdefault(os.path.basename(fp), []).append(s)

# Process all ChemistryLesson HTML files
lesson_files = glob.glob(os.path.join(BASE, "ChemistryLessons", "**", "*.html"), recursive=True)
lesson_files.sort()

chem_lesson_missing_zh = {}
chem_lesson_missing_es = {}
chem_lesson_missing_hi = {}

for fp in lesson_files:
    if "_Templates" in fp:
        continue
    strings = extract_translatable_text(fp)
    relpath = os.path.relpath(fp, BASE)
    for s in strings:
        if s not in chinese_keys:
            chem_lesson_missing_zh.setdefault(relpath, []).append(s)
        if s not in spanish_keys:
            chem_lesson_missing_es.setdefault(relpath, []).append(s)
        if s not in hindi_keys:
            chem_lesson_missing_hi.setdefault(relpath, []).append(s)

# Report
total_zh = sum(len(v) for v in chem_lesson_missing_zh.values())
total_es = sum(len(v) for v in chem_lesson_missing_es.values())
total_hi = sum(len(v) for v in chem_lesson_missing_hi.values())

print(f"\n=== CHEMISTRY LESSONS - MISSING TRANSLATIONS ===")
print(f"Files scanned: {len(lesson_files)}")
print(f"Chinese missing: {total_zh} strings across {len(chem_lesson_missing_zh)} files")
print(f"Spanish missing: {total_es} strings across {len(chem_lesson_missing_es)} files")
print(f"Hindi missing:   {total_hi} strings across {len(chem_lesson_missing_hi)} files")

# Show sample of missing strings
if chem_lesson_missing_zh:
    print(f"\n--- Sample missing CHINESE translations (first 50) ---")
    count = 0
    seen = set()
    for fp, strings in sorted(chem_lesson_missing_zh.items()):
        for s in sorted(strings):
            if s not in seen:
                seen.add(s)
                print(f"  {s}")
                count += 1
                if count >= 50:
                    break
        if count >= 50:
            break

if chem_lesson_missing_es:
    print(f"\n--- Sample missing SPANISH translations (first 50) ---")
    count = 0
    seen = set()
    for fp, strings in sorted(chem_lesson_missing_es.items()):
        for s in sorted(strings):
            if s not in seen:
                seen.add(s)
                print(f"  {s}")
                count += 1
                if count >= 50:
                    break
        if count >= 50:
            break

if chem_lesson_missing_hi:
    print(f"\n--- Sample missing HINDI translations (first 50) ---")
    count = 0
    seen = set()
    for fp, strings in sorted(chem_lesson_missing_hi.items()):
        for s in sorted(strings):
            if s not in seen:
                seen.add(s)
                print(f"  {s}")
                count += 1
                if count >= 50:
                    break
        if count >= 50:
            break

# Also check course main pages
for lang_name, missing_dict in [("Chinese", all_missing["chinese"]), ("Spanish", all_missing["spanish"]), ("Hindi", all_missing["hindi"])]:
    total = sum(len(v) for v in missing_dict.values())
    if total:
        print(f"\n=== COURSE PAGES - MISSING {lang_name.upper()} ({total} strings) ===")
        for fp, strings in sorted(missing_dict.items()):
            for s in strings:
                print(f"  [{fp}] {s}")
