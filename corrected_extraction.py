#!/usr/bin/env python3
"""
Corrected extraction: decode HTML entities BEFORE comparing to dictionary keys.
This gives accurate missing translation counts.
"""
import os, re, html as html_module
from collections import Counter, defaultdict

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"
SCRIPTS = os.path.join(BASE, "scripts")
OUT_DIR = os.path.join(os.path.dirname(BASE), "translation_batches")
os.makedirs(OUT_DIR, exist_ok=True)

def extract_translation_keys(js_file):
    keys = set()
    with open(js_file, 'r', encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*"([^"]+)"\s*:', line)
            if m:
                keys.add(m.group(1))
    return keys

chinese_keys = extract_translation_keys(os.path.join(SCRIPTS, "global_translations.js"))
spanish_keys = extract_translation_keys(os.path.join(SCRIPTS, "spanish_translations.js"))
hindi_keys = extract_translation_keys(os.path.join(SCRIPTS, "hindi_translations.js"))
all_translated = chinese_keys | spanish_keys | hindi_keys
print(f"Loaded: CH={len(chinese_keys)}, SP={len(spanish_keys)}, HI={len(hindi_keys)}, Union={len(all_translated)}")

def strip_tags(html_str):
    text = re.sub(r'<[^>]+>', '', html_str)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_element_texts(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return []
    results = []
    for pattern, tag in [
        (r'<p\b[^>]*>(.*?)</p>', 'p'),
        (r'<li\b[^>]*>(.*?)</li>', 'li'),
        (r'<h3\b[^>]*>(.*?)</h3>', 'h3'),
        (r'<h4\b[^>]*>(.*?)</h4>', 'h4'),
        (r'<label\b[^>]*>(.*?)</label>', 'label'),
        (r'<a\b[^>]*>(.*?)</a>', 'a'),
        (r'<button\b[^>]*>(.*?)</button>', 'button'),
    ]:
        for m in re.finditer(pattern, content, re.DOTALL | re.IGNORECASE):
            inner = m.group(1)
            if re.search(r'<(?:div|p|ul|ol|form|table|section)\b', inner, re.IGNORECASE):
                continue
            text = strip_tags(inner)
            # KEY FIX: decode HTML entities to match how browser renders text
            text = html_module.unescape(text)
            if text and len(text) > 1:
                results.append((text, tag))
    return results

COURSE_DIRS = {
    "Algebra1Lessons": "Algebra1",
    "Algebra2Lessons": "Algebra2",
    "GeometryLessons": "Geometry",
    "BiologyLessons": "Biology",
    "ChemistryLessons": "Chemistry",
    "PhysicsLessons": "Physics",
}

SKIP_PATTERNS = [
    r'^Lesson \d+[A-B]?\.\d+',
    r'^Key Concepts:',
    r'^\d+\.?\s*$',
    r'^https?://',
    r'^<!--',
]

def should_skip(text):
    for pat in SKIP_PATTERNS:
        if re.match(pat, text, re.IGNORECASE):
            return True
    return False

def is_math_expression(text):
    t = text
    # Pure numbers/money/measurements
    if re.match(r'^[\$\u20ac\u00a3]?[\d\.\-\+/,\s%\u00b0]+\s*(m/s|Hz|kg|mol|g|mL|L|J|N|W|V|A|\u03a9|Pa|atm|cm|mm|m|km|hrs?|hours?|min|sec|s|cal|kcal|kJ|eV)?\.?\s*$', t):
        return True
    # Coordinate pairs
    if re.match(r'^[\(\[\{][\d\.\-\u2212\+\u221e\u03c0,\s/]+[\)\]\}]$', t):
        return True
    # Math-dominated (no English words of 3+ chars, has math chars)
    english_words = re.findall(r'[a-zA-Z]{3,}', t)
    math_chars = len(re.findall(r'[\d=<>\u2264\u2265\u00b2\u00b3\u221a\u00b1\u00d7\u00f7\^()\[\]{}/\+\-\*\u00b7\u02e3\u207f\u03c0\u221e\u03c3\u03bc\u03bb\u03a9]', t))
    if len(english_words) == 0 and math_chars > 0:
        return True
    # Very short with no English words
    if len(t.replace(' ', '')) <= 5 and len(english_words) == 0:
        return True
    # Ratios
    if re.match(r'^\d+:\d+$', t):
        return True
    return False

# Process all lesson files
course_data = defaultdict(lambda: {'summary': [], 'quiz_questions': [], 'quiz_answers': [], 'other': []})
all_missing = Counter()  # text -> count

lesson_files = []
for dir_name, course_name in COURSE_DIRS.items():
    course_path = os.path.join(BASE, dir_name)
    if not os.path.isdir(course_path):
        continue
    for root, dirs, files in os.walk(course_path):
        dirs[:] = [d for d in dirs if not d.startswith('_')]
        for f in files:
            if not f.endswith('.html'):
                continue
            filepath = os.path.join(root, f)
            is_summary = 'Summary' in f
            is_quiz = 'Quiz' in f
            is_practice = 'Practice' in f
            if not (is_summary or is_quiz or is_practice):
                continue
            
            elements = extract_element_texts(filepath)
            for text, tag in elements:
                if should_skip(text) or text in all_translated or is_math_expression(text):
                    continue
                all_missing[text] += 1
                if is_summary:
                    course_data[course_name]['summary'].append(text)
                elif is_quiz:
                    if tag == 'p' and re.match(r'^\d+\.', text):
                        course_data[course_name]['quiz_questions'].append(text)
                    elif tag in ('label', 'button', 'a'):
                        course_data[course_name]['quiz_answers'].append(text)
                    else:
                        course_data[course_name]['other'].append(text)
                else:
                    course_data[course_name]['other'].append(text)

# Report
grand_total = 0
for course in sorted(course_data.keys()):
    data = course_data[course]
    s = sorted(set(data['summary']))
    q = sorted(set(data['quiz_questions']))
    a = sorted(set(data['quiz_answers']))
    o = sorted(set(data['other']))
    total = len(s) + len(q) + len(a) + len(o)
    grand_total += total
    print(f"\n{course}: {total} translatable strings")
    print(f"  Summary: {len(s)}, Quiz Q: {len(q)}, Quiz A: {len(a)}, Other: {len(o)}")
    
    outfile = os.path.join(OUT_DIR, f"{course.lower()}_to_translate.txt")
    with open(outfile, 'w', encoding='utf-8') as out:
        out.write(f"# {course} - Strings Needing Translation (ENTITY-DECODED)\n")
        out.write(f"# Total: {total}\n\n")
        out.write(f"## SUMMARY CONTENT ({len(s)})\n")
        for t in s: out.write(f"{t}\n")
        out.write(f"\n## QUIZ QUESTIONS ({len(q)})\n")
        for t in q: out.write(f"{t}\n")
        out.write(f"\n## QUIZ ANSWERS ({len(a)})\n")
        for t in a: out.write(f"{t}\n")
        out.write(f"\n## OTHER ({len(o)})\n")
        for t in o: out.write(f"{t}\n")

print(f"\n{'='*50}")
print(f"GRAND TOTAL: {grand_total} truly missing strings")
print(f"Per-course files: {OUT_DIR}")
