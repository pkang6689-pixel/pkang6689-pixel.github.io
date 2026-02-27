#!/usr/bin/env python3
"""
Extract full element textContent from lesson HTML files.
This matches how the modified applyTranslations() full-element matching works:
  - For <p>, <li>, <h3>, <h4>, <label>, <td>, <th> elements
  - Key = stripped-tags textContent (concatenation of all text nodes)
"""

import os
import re
from collections import Counter, defaultdict

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"
SCRIPTS = os.path.join(BASE, "scripts")

# ============================================================
# Step 1: Parse translation dictionaries
# ============================================================
def extract_translation_keys(js_file):
    keys = set()
    with open(js_file, 'r', encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*"([^"]+)"\s*:', line)
            if m:
                keys.add(m.group(1))
    return keys

print("Loading existing translation keys...")
chinese_keys = extract_translation_keys(os.path.join(SCRIPTS, "global_translations.js"))
spanish_keys = extract_translation_keys(os.path.join(SCRIPTS, "spanish_translations.js"))
hindi_keys = extract_translation_keys(os.path.join(SCRIPTS, "hindi_translations.js"))
print(f"  Chinese: {len(chinese_keys)}, Spanish: {len(spanish_keys)}, Hindi: {len(hindi_keys)}")

# ============================================================
# Step 2: Extract full element textContent from HTML files
# ============================================================
def strip_tags(html_str):
    """Remove HTML tags and normalize whitespace."""
    text = re.sub(r'<[^>]+>', '', html_str)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_element_texts(filepath):
    """Extract full textContent of content elements from HTML."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return []
    
    texts = []
    
    # Extract content from various element types
    # Match <p>...</p>, <li>...</li>, <h3>...</h3>, <h4>...</h4>, <label>...</label>
    tag_patterns = [
        (r'<p\b[^>]*>(.*?)</p>', 'p'),
        (r'<li\b[^>]*>(.*?)</li>', 'li'),
        (r'<h3\b[^>]*>(.*?)</h3>', 'h3'),
        (r'<h4\b[^>]*>(.*?)</h4>', 'h4'),
        (r'<label\b[^>]*>(.*?)</label>', 'label'),
    ]
    
    for pattern, tag in tag_patterns:
        for match in re.finditer(pattern, content, re.DOTALL | re.IGNORECASE):
            inner_html = match.group(1)
            # Skip if it contains nested block elements or forms
            if re.search(r'<(?:div|p|ul|ol|form|table|section)\b', inner_html, re.IGNORECASE):
                continue
            text = strip_tags(inner_html)
            if text and len(text) > 2:
                # Skip if it's just a number or single word that's too generic
                if re.match(r'^\d+\.?$', text):
                    continue
                texts.append((text, tag))
    
    # Also extract <a> link text (like "Next Up: Play", "Back to Algebra 1")
    for match in re.finditer(r'<a\b[^>]*>(.*?)</a>', content, re.DOTALL | re.IGNORECASE):
        text = strip_tags(match.group(1))
        if text and len(text) > 2 and not text.startswith('http'):
            texts.append((text, 'a'))
    
    # Extract <button> text
    for match in re.finditer(r'<button\b[^>]*>(.*?)</button>', content, re.DOTALL | re.IGNORECASE):
        text = strip_tags(match.group(1))
        if text and len(text) > 1:
            texts.append((text, 'button'))
    
    return texts

# ============================================================
# Step 3: Process all lesson files
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
        dirs[:] = [d for d in dirs if not d.startswith('_')]
        for f in files:
            if f.endswith('.html') and ('Summary' in f or 'Quiz' in f or 'Practice' in f):
                lesson_files.append(os.path.join(root, f))

print(f"Found {len(lesson_files)} lesson files")

# Track all content
all_content = Counter()  # text -> count
content_by_type = defaultdict(lambda: Counter())  # file_type -> {text: count}
content_by_course = defaultdict(lambda: Counter())  # course -> {text: count}
content_tags = {}  # text -> tag type

for filepath in lesson_files:
    fname = os.path.basename(filepath)
    # Determine file type
    ftype = 'Other'
    for t in ['Summary', 'Quiz', 'Practice']:
        if t in fname:
            ftype = t
            break
    # Determine course
    for cd in COURSE_DIRS:
        if cd in filepath:
            course = cd.replace('Lessons', '')
            break
    
    elements = extract_element_texts(filepath)
    for text, tag in elements:
        all_content[text] += 1
        content_by_type[ftype][text] += 1
        content_by_course[course][text] += 1
        content_tags[text] = tag

# ============================================================
# Step 4: Find what's missing from dictionaries
# ============================================================
SKIP_PATTERNS = [
    r'^Lesson \d+[A-B]?\.\d+',  # Lesson titles (handled by dynamic fallback)
    r'^Key Concepts:',           # Handled by dynamic data-i18n
    r'^\d+$',                    # Pure numbers
    r'^https?://',               # URLs
    r'^<!--',                    # HTML comments
]

def should_skip(text):
    for pat in SKIP_PATTERNS:
        if re.match(pat, text, re.IGNORECASE):
            return True
    return False

missing_all = {}  # text -> {course, type, tag, count}
for text, count in all_content.items():
    if should_skip(text):
        continue
    if text not in chinese_keys and text not in spanish_keys and text not in hindi_keys:
        missing_all[text] = {
            'count': count,
            'tag': content_tags.get(text, '?'),
        }

# Sort by count descending, then alphabetically
sorted_missing = sorted(missing_all.items(), key=lambda x: (-x[1]['count'], x[0]))

# ============================================================
# Step 5: Report
# ============================================================
print(f"\nTotal unique element texts extracted: {len(all_content)}")
print(f"Already translated: {len(all_content) - len(missing_all)}")
print(f"Missing from ALL dictionaries: {len(missing_all)}")

# By page type
for ftype in ['Summary', 'Quiz', 'Practice']:
    type_missing = sum(1 for t in content_by_type[ftype] if t in missing_all)
    print(f"  {ftype}: {len(content_by_type[ftype])} unique, {type_missing} missing")

# By course
for course in sorted(content_by_course.keys()):
    course_missing = sum(1 for t in content_by_course[course] if t in missing_all)
    print(f"  {course}: {len(content_by_course[course])} unique, {course_missing} missing")

# Write detailed report
output_file = os.path.join(os.path.dirname(BASE), "untranslated_fulltext_report.txt")
with open(output_file, 'w', encoding='utf-8') as out:
    out.write(f"FULL ELEMENT TEXT - UNTRANSLATED CONTENT REPORT\n")
    out.write(f"{'='*70}\n")
    out.write(f"Total unique element texts: {len(all_content)}\n")
    out.write(f"Already translated: {len(all_content) - len(missing_all)}\n")
    out.write(f"Missing: {len(missing_all)}\n\n")
    
    # Group by course for the missing strings
    missing_by_course = defaultdict(list)
    for text, info in sorted_missing:
        for course in sorted(content_by_course.keys()):
            if text in content_by_course[course]:
                missing_by_course[course].append((text, info))
    
    for course in sorted(missing_by_course.keys()):
        items = missing_by_course[course]
        out.write(f"\n{'='*70}\n")
        out.write(f"COURSE: {course} ({len(items)} missing strings)\n")
        out.write(f"{'='*70}\n")
        for text, info in items:
            out.write(f"  [{info['tag']:6s}] ({info['count']}x) {text}\n")

    # Also write all missing strings in a flat list for batch processing
    out.write(f"\n{'='*70}\n")
    out.write(f"ALL MISSING STRINGS (flat list for translation)\n")
    out.write(f"{'='*70}\n")
    for text, info in sorted_missing:
        out.write(f"{text}\n")

print(f"\nReport written to: {output_file}")

# Also write just the missing strings to a simple text file for processing
strings_file = os.path.join(os.path.dirname(BASE), "strings_to_translate.txt")
with open(strings_file, 'w', encoding='utf-8') as out:
    for text, info in sorted_missing:
        out.write(f"{text}\n")
print(f"Strings list written to: {strings_file}")
