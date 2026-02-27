#!/usr/bin/env python3
"""
Extract all unique untranslated text from lesson HTML files.
Compare against existing translation dictionaries to find gaps.
"""

import os
import re
from html.parser import HTMLParser
from collections import Counter

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"
SCRIPTS = os.path.join(BASE, "scripts")

# ============================================================
# Step 1: Parse translation dictionaries to get existing keys
# ============================================================
def extract_translation_keys(js_file):
    """Extract all English keys from a translation JS file."""
    keys = set()
    with open(js_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Match lines like:  "English text": "translation",
            m = re.match(r'^\s*"([^"]+)"\s*:', line)
            if m:
                keys.add(m.group(1))
    return keys

print("Loading existing translation keys...")
chinese_keys = extract_translation_keys(os.path.join(SCRIPTS, "global_translations.js"))
spanish_keys = extract_translation_keys(os.path.join(SCRIPTS, "spanish_translations.js"))
hindi_keys = extract_translation_keys(os.path.join(SCRIPTS, "hindi_translations.js"))

print(f"  Chinese keys: {len(chinese_keys)}")
print(f"  Spanish keys: {len(spanish_keys)}")
print(f"  Hindi keys:   {len(hindi_keys)}")

# Union of all keys (what's already translated in at least one language)
all_keys = chinese_keys | spanish_keys | hindi_keys
print(f"  Union of all keys: {len(all_keys)}")

# ============================================================
# Step 2: Extract text from lesson HTML files
# ============================================================
class TextExtractor(HTMLParser):
    """Extract text nodes from HTML, similar to how applyTranslations walks the DOM."""
    SKIP_TAGS = {'script', 'style', 'textarea', 'input', 'code', 'pre'}
    
    def __init__(self):
        super().__init__()
        self.texts = []
        self.skip_depth = 0
    
    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.SKIP_TAGS:
            self.skip_depth += 1
    
    def handle_endtag(self, tag):
        if tag.lower() in self.SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
    
    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        text = data.strip()
        if text and len(text) > 1:  # Skip single characters
            self.texts.append(text)

def extract_texts_from_html(filepath):
    """Extract all meaningful text nodes from an HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        parser = TextExtractor()
        parser.feed(content)
        return parser.texts
    except Exception as e:
        print(f"  ERROR parsing {filepath}: {e}")
        return []

# ============================================================
# Step 3: Find all lesson HTML files
# ============================================================
COURSE_DIRS = [
    "Algebra1Lessons", "Algebra2Lessons", "GeometryLessons",
    "BiologyLessons", "ChemistryLessons", "PhysicsLessons"
]

lesson_files = []
for course_dir in COURSE_DIRS:
    course_path = os.path.join(BASE, course_dir)
    if not os.path.isdir(course_path):
        continue
    for root, dirs, files in os.walk(course_path):
        # Skip _Templates
        dirs[:] = [d for d in dirs if not d.startswith('_')]
        for f in files:
            if f.endswith('.html') and ('Summary' in f or 'Quiz' in f or 'Practice' in f):
                lesson_files.append(os.path.join(root, f))

print(f"\nFound {len(lesson_files)} lesson HTML files")

# ============================================================
# Step 4: Extract all text and find what's missing
# ============================================================
# Patterns to skip (already handled by dynamic fallback or too generic)
SKIP_PATTERNS = [
    r'^Lesson \d+\.\d+',  # Lesson titles handled by data-i18n dynamic
    r'^Key Concepts:',     # Also handled by dynamic data-i18n
    r'^Score:?\s*\d*$',    # Dynamic score text
    r'^\d+$',              # Pure numbers
    r'^[A-Z]$',            # Single letters
    r'^[a-z]$',            # Single letters
    r'^\d+\.\d+$',        # Version numbers, lesson numbers
    r'^@',                 # CSS/JS artifacts
    r'^{',                 # JSON artifacts
    r'^function',          # JS code leak
    r'^var ',              # JS code leak
    r'^const ',            # JS code leak
    r'^let ',              # JS code leak
    r'^if\s*\(',           # JS code leak
    r'^document\.',        # JS code leak
    r'^window\.',          # JS code leak
    r'^https?://',         # URLs
]

def should_skip(text):
    for pat in SKIP_PATTERNS:
        if re.match(pat, text, re.IGNORECASE):
            return True
    return False

all_extracted = Counter()  # text -> count of files it appears in
missing_chinese = Counter()
missing_spanish = Counter()
missing_hindi = Counter()

file_type_counts = {'Summary': 0, 'Quiz': 0, 'Practice': 0}
file_type_missing = {'Summary': set(), 'Quiz': set(), 'Practice': set()}

for filepath in lesson_files:
    # Determine file type
    fname = os.path.basename(filepath)
    ftype = None
    for t in ['Summary', 'Quiz', 'Practice']:
        if t in fname:
            ftype = t
            break
    
    texts = extract_texts_from_html(filepath)
    file_type_counts[ftype] = file_type_counts.get(ftype, 0) + 1
    
    for text in texts:
        if should_skip(text):
            continue
        all_extracted[text] += 1
        if text not in chinese_keys:
            missing_chinese[text] += 1
            file_type_missing[ftype].add(text)
        if text not in spanish_keys:
            missing_spanish[text] += 1
        if text not in hindi_keys:
            missing_hindi[text] += 1

# ============================================================
# Step 5: Report
# ============================================================
print(f"\n{'='*60}")
print(f"RESULTS")
print(f"{'='*60}")
print(f"Total unique text strings extracted: {len(all_extracted)}")
print(f"Missing from Chinese dictionary: {len(missing_chinese)}")
print(f"Missing from Spanish dictionary: {len(missing_spanish)}")
print(f"Missing from Hindi dictionary:   {len(missing_hindi)}")
print(f"Missing from ALL dictionaries:   {len(set(missing_chinese) & set(missing_spanish) & set(missing_hindi))}")

# Check by page type
for ftype in ['Summary', 'Quiz', 'Practice']:
    strings_in_type = file_type_missing.get(ftype, set())
    print(f"\n  {ftype} pages: {file_type_counts.get(ftype, 0)} files, {len(strings_in_type)} unique missing strings (Chinese)")

# Sort missing strings by frequency (most common first)
print(f"\n{'='*60}")
print(f"TOP 50 MOST COMMON MISSING STRINGS (Chinese)")
print(f"{'='*60}")
all_missing = set(missing_chinese) | set(missing_spanish) | set(missing_hindi)
# Sort by how many files they appear in
sorted_missing = sorted(missing_chinese.items(), key=lambda x: -x[1])
for i, (text, count) in enumerate(sorted_missing[:50]):
    in_ch = "CH" if text in missing_chinese else "  "
    in_sp = "SP" if text in missing_spanish else "  "
    in_hi = "HI" if text in missing_hindi else "  "
    display = text[:80] + "..." if len(text) > 80 else text
    print(f"  {i+1:3d}. [{in_ch}|{in_sp}|{in_hi}] ({count:4d}x) {display}")

# Write full list to file
output_file = os.path.join(os.path.dirname(BASE), "untranslated_content_report.txt")
with open(output_file, 'w', encoding='utf-8') as out:
    out.write(f"UNTRANSLATED CONTENT REPORT\n")
    out.write(f"{'='*60}\n")
    out.write(f"Total unique text strings: {len(all_extracted)}\n")
    out.write(f"Missing Chinese: {len(missing_chinese)}\n")
    out.write(f"Missing Spanish: {len(missing_spanish)}\n")
    out.write(f"Missing Hindi:   {len(missing_hindi)}\n\n")
    
    # Categorize: common UI strings vs unique content
    common_strings = []  # appears in 10+ files
    unique_strings = []  # appears in <10 files
    
    for text, count in sorted_missing:
        if count >= 10:
            common_strings.append((text, count))
        else:
            unique_strings.append((text, count))
    
    out.write(f"\nCOMMON STRINGS (appear in 10+ files): {len(common_strings)}\n")
    out.write(f"{'='*60}\n")
    for text, count in common_strings:
        ch = "MISSING" if text in missing_chinese else "OK     "
        sp = "MISSING" if text in missing_spanish else "OK     "
        hi = "MISSING" if text in missing_hindi else "OK     "
        out.write(f"  ({count:4d}x) [CH:{ch}|SP:{sp}|HI:{hi}] {text}\n")
    
    out.write(f"\nUNIQUE CONTENT STRINGS (appear in <10 files): {len(unique_strings)}\n")
    out.write(f"{'='*60}\n")
    for text, count in unique_strings:
        ch = "MISSING" if text in missing_chinese else "OK     "
        sp = "MISSING" if text in missing_spanish else "OK     "
        hi = "MISSING" if text in missing_hindi else "OK     "
        out.write(f"  ({count:4d}x) [CH:{ch}|SP:{sp}|HI:{hi}] {text}\n")

print(f"\nFull report written to: {output_file}")
print(f"\nCommon strings (10+ files): {len(common_strings)}")
print(f"Unique content strings (<10 files): {len(unique_strings)}")
