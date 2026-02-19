#!/usr/bin/env python3
"""
Extract ALL unique question and answer strings from physics quiz HTML files.
Compare against existing translations in global_translations.js.
Output untranslated strings organized by unit as a Python dict.
"""

import os
import re
import json
from collections import OrderedDict

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\PhysicsLessons"
TRANSLATIONS_FILE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js"

def extract_quiz_strings(filepath):
    """Extract question texts and answer option texts from a quiz HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    questions = []
    answers = []
    
    # Extract question text from <p> tags inside quiz-question divs
    # Pattern: numbered questions like "1. What is a physical quantity?"
    q_pattern = re.compile(r'<p[^>]*>\s*(\d+)\.\s*(.*?)\s*</p>', re.DOTALL)
    for m in q_pattern.finditer(content):
        # Only match questions inside quiz-question divs
        q_text = m.group(2).strip()
        # Clean HTML entities
        q_text = q_text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#39;', "'")
        q_text = q_text.replace('&nbsp;', ' ')
        # Remove any remaining HTML tags
        q_text = re.sub(r'<[^>]+>', '', q_text)
        q_text = q_text.strip()
        if q_text:
            questions.append(q_text)
    
    # Extract answer option text from <label> tags containing <input type="radio">
    # The text is after the <input> tag
    a_pattern = re.compile(r'<input\s+type="radio"[^>]*>\s*(.*?)\s*</label>', re.DOTALL)
    for m in a_pattern.finditer(content):
        a_text = m.group(1).strip()
        # Clean HTML entities
        a_text = a_text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#39;', "'")
        a_text = a_text.replace('&nbsp;', ' ')
        # Remove any remaining HTML tags
        a_text = re.sub(r'<[^>]+>', '', a_text)
        a_text = a_text.strip()
        if a_text:
            answers.append(a_text)
    
    return questions, answers

def load_existing_translations(filepath):
    """Load existing translation keys from global_translations.js."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all keys from the translations object
    # Keys are in format: "key string": "value string",
    keys = set()
    key_pattern = re.compile(r'^\s*"((?:[^"\\]|\\.)*)"\s*:', re.MULTILINE)
    for m in key_pattern.finditer(content):
        key = m.group(1)
        # Unescape
        key = key.replace('\\"', '"').replace('\\\\', '\\')
        keys.add(key)
    
    return keys

def main():
    # Discover all unit directories and quiz files
    units = {}
    for d in sorted(os.listdir(BASE)):
        unit_path = os.path.join(BASE, d)
        if os.path.isdir(unit_path) and d.startswith('Unit'):
            quiz_files = sorted([f for f in os.listdir(unit_path) if f.endswith('_Quiz.html')])
            units[d] = quiz_files
    
    print("=" * 70)
    print("PHYSICS QUIZ FILE INVENTORY")
    print("=" * 70)
    total_files = 0
    for unit_name, files in sorted(units.items(), key=lambda x: int(re.search(r'\d+', x[0]).group())):
        print(f"  {unit_name}: {len(files)} quiz files")
        for f in files:
            print(f"    - {f}")
        total_files += len(files)
    print(f"\n  TOTAL: {total_files} quiz files")
    
    # Extract all strings from all quiz files
    all_questions = set()
    all_answers = set()
    unit_questions = OrderedDict()  # unit -> list of (lesson, questions)
    unit_answers = OrderedDict()  # unit -> list of (lesson, answers)
    
    for unit_name, files in sorted(units.items(), key=lambda x: int(re.search(r'\d+', x[0]).group())):
        unit_questions[unit_name] = []
        unit_answers[unit_name] = []
        for qf in files:
            filepath = os.path.join(BASE, unit_name, qf)
            qs, ans = extract_quiz_strings(filepath)
            lesson_id = qf.replace('_Quiz.html', '')
            unit_questions[unit_name].append((lesson_id, qs))
            unit_answers[unit_name].append((lesson_id, ans))
            all_questions.update(qs)
            all_answers.update(ans)
    
    print(f"\n{'=' * 70}")
    print("EXTRACTION RESULTS")
    print(f"{'=' * 70}")
    print(f"  Total unique question strings: {len(all_questions)}")
    print(f"  Total unique answer option strings: {len(all_answers)}")
    all_strings = all_questions | all_answers
    print(f"  Total unique strings (combined): {len(all_strings)}")
    
    # Load existing translations
    existing_keys = load_existing_translations(TRANSLATIONS_FILE)
    print(f"\n  Existing translation keys in global_translations.js: {len(existing_keys)}")
    
    # Check overlap
    translated_questions = all_questions & existing_keys
    translated_answers = all_answers & existing_keys
    translated_all = all_strings & existing_keys
    untranslated = all_strings - existing_keys
    
    print(f"\n  Already translated questions: {len(translated_questions)}")
    print(f"  Already translated answers: {len(translated_answers)}")
    print(f"  Already translated total: {len(translated_all)}")
    print(f"  NOT yet translated: {len(untranslated)}")
    
    # Also check if numbered versions exist (e.g. "1. What is...")
    # Some translations might have the number prefix
    numbered_translated = set()
    for s in untranslated:
        for i in range(1, 20):
            numbered_key = f"{i}. {s}"
            if numbered_key in existing_keys:
                numbered_translated.add(s)
                break
    
    if numbered_translated:
        print(f"\n  Strings translated WITH number prefix (e.g. '1. ...'): {len(numbered_translated)}")
        untranslated_final = untranslated - numbered_translated
    else:
        untranslated_final = untranslated
    
    print(f"  Final untranslated strings: {len(untranslated_final)}")
    
    # Show which translated strings were found (sample)
    if translated_all:
        print(f"\n  Sample of already-translated strings:")
        for s in sorted(translated_all)[:20]:
            print(f"    ✓ \"{s}\"")
    
    # Output untranslated strings organized by unit
    print(f"\n{'=' * 70}")
    print("UNTRANSLATED STRINGS BY UNIT (Python dict format)")
    print(f"{'=' * 70}")
    
    print("\nphysics_quiz_translations = {")
    
    for unit_name in unit_questions:
        unit_num = re.search(r'\d+', unit_name).group()
        # Collect all untranslated strings for this unit
        unit_untranslated_q = OrderedDict()
        unit_untranslated_a = OrderedDict()
        
        for lesson_id, qs in unit_questions[unit_name]:
            for q in qs:
                if q in untranslated_final:
                    unit_untranslated_q[q] = q
        
        for lesson_id, ans in unit_answers[unit_name]:
            for a in ans:
                if a in untranslated_final:
                    unit_untranslated_a[a] = a
        
        all_unit_untranslated = OrderedDict()
        # Questions first, then answers
        for lesson_id, qs in unit_questions[unit_name]:
            for q in qs:
                if q in untranslated_final and q not in all_unit_untranslated:
                    all_unit_untranslated[q] = q
            # Interleave answers for this lesson
            lesson_idx = [i for i, (lid, _) in enumerate(unit_answers[unit_name]) if lid == lesson_id]
            if lesson_idx:
                _, ans_list = unit_answers[unit_name][lesson_idx[0]]
                for a in ans_list:
                    if a in untranslated_final and a not in all_unit_untranslated:
                        all_unit_untranslated[a] = a
        
        if all_unit_untranslated:
            print(f"\n    # --- Unit {unit_num} ---")
            for lesson_id, qs in unit_questions[unit_name]:
                # Print all strings (Q + A interleaved) for this lesson
                lesson_strings = OrderedDict()
                for q in qs:
                    if q in untranslated_final:
                        lesson_strings[q] = q
                # Get answers for this lesson
                lesson_idx = [i for i, (lid, _) in enumerate(unit_answers[unit_name]) if lid == lesson_id]
                if lesson_idx:
                    _, ans_list = unit_answers[unit_name][lesson_idx[0]]
                    for a in ans_list:
                        if a in untranslated_final:
                            lesson_strings[a] = a
                
                if lesson_strings:
                    print(f"    # {lesson_id}")
                    for s in lesson_strings:
                        # Escape any quotes in the string
                        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
                        print(f'    "{escaped}": "{escaped}",')
    
    print("}")
    
    # Also output a flat count summary
    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Total quiz files: {total_files}")
    print(f"  Total unique question strings: {len(all_questions)}")
    print(f"  Total unique answer strings: {len(all_answers)}")
    print(f"  Total unique combined: {len(all_strings)}")
    print(f"  Already translated: {len(translated_all)}")
    print(f"  Translated with number prefix: {len(numbered_translated)}")
    print(f"  Untranslated: {len(untranslated_final)}")

if __name__ == '__main__':
    main()
