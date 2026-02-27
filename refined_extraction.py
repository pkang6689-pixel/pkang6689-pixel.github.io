#!/usr/bin/env python3
"""
Refined extraction: separates truly translatable content from math/formulas.
Produces per-course lists ready for translation generation.
"""

import os, re
from collections import Counter, defaultdict

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"
SCRIPTS = os.path.join(BASE, "scripts")
OUT_DIR = os.path.join(os.path.dirname(BASE), "translation_batches")
os.makedirs(OUT_DIR, exist_ok=True)

# Load existing keys
def extract_translation_keys(js_file):
    keys = set()
    with open(js_file, 'r', encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*"([^"]+)"\s*:', line)
            if m:
                keys.add(m.group(1))
    return keys

all_translated = (
    extract_translation_keys(os.path.join(SCRIPTS, "global_translations.js")) |
    extract_translation_keys(os.path.join(SCRIPTS, "spanish_translations.js")) |
    extract_translation_keys(os.path.join(SCRIPTS, "hindi_translations.js"))
)

# HTML text extraction
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
            if text and len(text) > 1:
                results.append((text, tag))
    return results

def is_math_expression(text):
    """Enhanced filter: returns True if text is a math expression that doesn't need translation."""
    t = text.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
    t = t.replace('&#x1F3C6;', '').replace('&#x2705;', '').replace('&#x274C;', '')
    
    # Pure numbers, money, measurements with only numbers+units
    if re.match(r'^[\$€£]?[\d\.\-\+/,\s%°]+\s*(m/s|Hz|kg|mol|g|mL|L|J|N|W|V|A|Ω|Pa|atm|cm|mm|m|km|hrs?|hours?|min|sec|s|cal|kcal|kJ|eV)?\.?\s*$', t):
        return True
    
    # Coordinate pairs and intervals: (1, 4), (-2, ∞), [0, 2π]
    if re.match(r'^[\(\[\{][\d\.\-−\+∞π,\s/]+[\)\]\}]$', t):
        return True
    
    # Math-heavy: dominated by math symbols, variables, operators
    # Count English word characters vs math characters
    english_words = re.findall(r'[a-zA-Z]{3,}', t)  # words of 3+ letters
    math_chars = len(re.findall(r'[\d=<>≤≥²³√±×÷^()\[\]{}/\+\-\*·ˣⁿπ∞σμλΩ]', t))
    
    if len(english_words) == 0 and math_chars > 0:
        return True
    
    # Formulas: E = mgh, F = ma, PV = nRT, etc.
    if re.match(r'^[A-Za-z_]+[\s]*=[\s]*[A-Za-z\d\s\+\-\*/\(\)\^²³√·½¼¾]+$', t) and len(english_words) == 0:
        return True
    
    # Math equations: x² + 5x + 6, (x−3)(x+4), etc.
    if re.match(r'^[xyz\d\s\+\-\*/=\(\)²³√^,\.·<>≤≥≠±∞]+$', t):
        return True
    
    # Very short with only 1-2 character "words": "x", "y", "pH", "ΔH"
    if len(t.replace(' ', '')) <= 5 and len(english_words) == 0:
        return True
    
    # Ratios: 1:2, 2:7, 9:16
    if re.match(r'^\d+:\d+$', t):
        return True
    
    # Chemical formulas only: NaCl, H₂O, Fe₂O₃ (no English words except element symbols)
    if re.match(r'^[A-Z][a-z]?[\d₀₁₂₃₄₅₆₇₈₉]*(\s*[\+\-→⟶]\s*[A-Z][a-z]?[\d₀₁₂₃₄₅₆₇₈₉]*)*$', t):
        return True
    
    # Scientific notation: 6.02 × 10²³
    if re.match(r'^[\d\.]+\s*[×x]\s*10[\d²³⁴⁵⁶⁷⁸⁹]+', t):
        return True
    
    return False

# Patterns to skip
SKIP_PATTERNS = [
    r'^Lesson \d+[A-B]?\.\d+',  # Dynamic fallback
    r'^Key Concepts:',
    r'^\d+$',
    r'^https?://',
    r'^<!--',
]

def should_skip(text):
    for pat in SKIP_PATTERNS:
        if re.match(pat, text, re.IGNORECASE):
            return True
    return False

# Collect files
COURSE_DIRS = {
    "Algebra1Lessons": "Algebra1",
    "Algebra2Lessons": "Algebra2",
    "GeometryLessons": "Geometry",
    "BiologyLessons": "Biology",
    "ChemistryLessons": "Chemistry",
    "PhysicsLessons": "Physics",
}

course_data = defaultdict(lambda: {'summary': [], 'quiz_questions': [], 'quiz_answers': [], 'other': []})

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
                
                # Categorize
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

# Report and write per-course files
grand_total = 0
for course in sorted(course_data.keys()):
    data = course_data[course]
    summary_unique = sorted(set(data['summary']))
    quiz_q_unique = sorted(set(data['quiz_questions']))
    quiz_a_unique = sorted(set(data['quiz_answers']))
    other_unique = sorted(set(data['other']))
    total = len(summary_unique) + len(quiz_q_unique) + len(quiz_a_unique) + len(other_unique)
    grand_total += total
    
    print(f"\n{course}: {total} translatable strings")
    print(f"  Summary: {len(summary_unique)}, Quiz Q: {len(quiz_q_unique)}, Quiz A: {len(quiz_a_unique)}, Other: {len(other_unique)}")
    
    # Write to file
    outfile = os.path.join(OUT_DIR, f"{course.lower()}_to_translate.txt")
    with open(outfile, 'w', encoding='utf-8') as out:
        out.write(f"# {course} - Strings Needing Translation\n")
        out.write(f"# Total: {total}\n\n")
        
        out.write(f"## SUMMARY CONTENT ({len(summary_unique)})\n")
        for t in summary_unique:
            out.write(f"{t}\n")
        
        out.write(f"\n## QUIZ QUESTIONS ({len(quiz_q_unique)})\n")
        for t in quiz_q_unique:
            out.write(f"{t}\n")
        
        out.write(f"\n## QUIZ ANSWERS ({len(quiz_a_unique)})\n")
        for t in quiz_a_unique:
            out.write(f"{t}\n")
        
        out.write(f"\n## OTHER ({len(other_unique)})\n")
        for t in other_unique:
            out.write(f"{t}\n")

print(f"\n{'='*50}")
print(f"GRAND TOTAL: {grand_total} translatable strings")
print(f"Per-course files written to: {OUT_DIR}")
