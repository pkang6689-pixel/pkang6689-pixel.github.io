#!/usr/bin/env python3
"""
Filter untranslated strings to find only those that actually need translation.
Math expressions, coordinates, formulas, numbers should NOT be translated.
"""

import os
import re
from collections import Counter, defaultdict

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"
SCRIPTS = os.path.join(BASE, "scripts")

# Load existing keys
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

# Read strings
strings_file = os.path.join(os.path.dirname(BASE), "strings_to_translate.txt")
with open(strings_file, 'r', encoding='utf-8') as f:
    all_strings = [line.strip() for line in f if line.strip()]

print(f"Total raw untranslated strings: {len(all_strings)}")

def is_math_or_untranslatable(text):
    """Return True if string is a math expression, number, or doesn't need translation."""
    # Decode HTML entities for checking
    t = text.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
    t = t.replace('&#x1F3C6;', '')  # emoji
    
    # Pure numbers, decimals, fractions
    if re.match(r'^[\d\.\-\+/,\s%]+$', t):
        return True
    
    # Coordinate pairs: (1, 4), (-2, 3)
    if re.match(r'^\([\d\.\-−,\s]+\)$', t):
        return True
    
    # Simple math expressions: x = 2, x > 3, y = mx + b, etc.
    # These are dominated by variables, operators, numbers
    alpha_chars = re.findall(r'[a-zA-Z]', t)
    if len(alpha_chars) <= 3 and re.search(r'[=<>≤≥²³√±×÷^]|x\s*[+\-*/]|[+\-*/]\s*x', t):
        return True
    
    # Math-heavy expressions (lots of math symbols, few English words)
    if re.match(r'^[\d\s\.\-\+\*/=<>≤≥²³√±×÷^()x,yznmabc;:|\[\]{}·ˣⁿ]+$', t):
        return True
    
    # Scientific formulas: E = mgh, F = kx, etc.
    if re.match(r'^[A-Z][\s]*=[\s]*', t) and len(t) < 20:
        if not any(word in t.lower() for word in ['is', 'the', 'of', 'an', 'are', 'has']):
            return True
    
    # Degree values: 60°, 135°
    if re.match(r'^[\d\.]+°$', t):
        return True
    
    # Ratios: 1:2, 2:7
    if re.match(r'^\d+:\d+$', t):
        return True
    
    # Polynomial expressions with parentheses
    if re.match(r'^\([^)]*[xy²³][^)]*\)', t) and len(re.findall(r'[a-zA-Z]{2,}', t)) == 0:
        return True
    
    # Variables only: x, y, n, nCr, P(A), P(B)
    if re.match(r'^[A-Za-z][\(\)A-Za-z·]*$', t) and len(t) < 10:
        if not t.lower() in ['the', 'is', 'are', 'an', 'all', 'both', 'none', 'yes', 'no', 'maybe',
                              'mass', 'atom', 'iron', 'prime', 'slope', 'mixed', 'varies', 'depends']:
            return True
    
    # HTML entities that are just special chars
    if re.match(r'^[&#;x0-9A-Fa-f]+$', t):
        return True
    
    # Very short single character or symbol
    if len(t) <= 1:
        return True
    
    # Expressions like "P(A)·P(B)", "n·p·(1−p)"
    if re.match(r'^[A-Za-z\(\)·\d\+\-\*/−p]+$', t) and '·' in t:
        return True
    
    # Trig/math: π/2, √3/2, etc.
    if re.match(r'^[πσμ√∞±≈∝∫∑∏∂∇\d\s/\.\-\+\*]+$', t):
        return True
    
    return False

# Categorize strings
needs_translation = []
math_skip = []
already_short_skip = []  # Single words that are too context-dependent

for text in all_strings:
    if is_math_or_untranslatable(text):
        math_skip.append(text)
    else:
        needs_translation.append(text)

print(f"Math/formula (skip): {len(math_skip)}")
print(f"Needs translation: {len(needs_translation)}")

# Further categorize by content type
ui_strings = []          # Buttons, links, navigation
quiz_questions = []      # "1. Solve: ..." or "Which of the following..."
quiz_answers_words = []  # Short word answers like "both", "neither"
summary_content = []     # Educational content paragraphs
lesson_titles = []       # "Lesson X.X: ..."
other = []

for text in needs_translation:
    t = text.replace('&gt;', '>').replace('&lt;', '<')
    
    if re.match(r'^Lesson \d+', t):
        lesson_titles.append(text)
    elif re.match(r'^\d+\.\s+', t):
        quiz_questions.append(text)
    elif any(kw in t for kw in ['Back to', 'Next Up', 'Leaderboard', 'Submit', 'Try Again',
                                  'Play Again', 'Restart', 'Pause', 'Resume']):
        ui_strings.append(text)
    elif len(text.split()) <= 3 and len(text) < 30:
        quiz_answers_words.append(text)
    elif len(text.split()) >= 5:
        summary_content.append(text)
    else:
        other.append(text)

print(f"\nCATEGORIES:")
print(f"  UI strings: {len(ui_strings)}")
print(f"  Lesson titles: {len(lesson_titles)}")
print(f"  Quiz questions: {len(quiz_questions)}")
print(f"  Quiz answer words (short): {len(quiz_answers_words)}")
print(f"  Summary content (5+ words): {len(summary_content)}")
print(f"  Other: {len(other)}")

# Write categorized output
output = os.path.join(os.path.dirname(BASE), "categorized_translations_needed.txt")
with open(output, 'w', encoding='utf-8') as out:
    out.write("="*70 + "\n")
    out.write(f"CATEGORIZED UNTRANSLATED STRINGS\n")
    out.write(f"Total needing translation: {len(needs_translation)}\n")
    out.write("="*70 + "\n\n")
    
    out.write(f"\n--- UI STRINGS ({len(ui_strings)}) ---\n")
    for t in sorted(ui_strings):
        out.write(f"  {t}\n")
    
    out.write(f"\n--- LESSON TITLES ({len(lesson_titles)}) ---\n")
    for t in sorted(lesson_titles):
        out.write(f"  {t}\n")
    
    out.write(f"\n--- QUIZ QUESTIONS ({len(quiz_questions)}) ---\n")
    for t in sorted(quiz_questions):
        out.write(f"  {t}\n")
    
    out.write(f"\n--- QUIZ ANSWER WORDS ({len(quiz_answers_words)}) ---\n")
    for t in sorted(quiz_answers_words):
        out.write(f"  {t}\n")
    
    out.write(f"\n--- SUMMARY CONTENT ({len(summary_content)}) ---\n")
    for t in sorted(summary_content):
        out.write(f"  {t}\n")
    
    out.write(f"\n--- OTHER ({len(other)}) ---\n")
    for t in sorted(other):
        out.write(f"  {t}\n")

    out.write(f"\n--- MATH/FORMULA SKIPPED ({len(math_skip)}) ---\n")
    for t in sorted(math_skip)[:100]:
        out.write(f"  {t}\n")
    if len(math_skip) > 100:
        out.write(f"  ... and {len(math_skip)-100} more\n")

print(f"Categorized report: {output}")
