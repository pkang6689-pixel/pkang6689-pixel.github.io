#!/usr/bin/env python3
"""
Extract ALL unique question and answer strings from physics quiz HTML files.
Compare against existing translations in global_translations.js.
Output untranslated strings organized by unit as a Python dict.
"""

import os
import re
import sys
from collections import OrderedDict

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\PhysicsLessons"
TRANSLATIONS_FILE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js"
OUTPUT_FILE = r"c:\Users\Peter\pkang6689-pixel.github.io\scripts\physics_quiz_untranslated.py"
REPORT_FILE = r"c:\Users\Peter\pkang6689-pixel.github.io\scripts\quiz_extraction_report.txt"

def extract_quiz_strings(filepath):
    """Extract question texts and answer option texts from a quiz HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    questions = []
    answers = []
    
    # Extract question text from <p> tags inside quiz-question divs
    q_pattern = re.compile(r'<p[^>]*>\s*(\d+)\.\s*(.*?)\s*</p>', re.DOTALL)
    for m in q_pattern.finditer(content):
        q_text = m.group(2).strip()
        q_text = q_text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#39;', "'")
        q_text = q_text.replace('&nbsp;', ' ')
        q_text = re.sub(r'<[^>]+>', '', q_text)
        q_text = q_text.strip()
        if q_text:
            questions.append(q_text)
    
    # Extract answer option text from <label> tags containing <input type="radio">
    a_pattern = re.compile(r'<input\s+type="radio"[^>]*>\s*(.*?)\s*</label>', re.DOTALL)
    for m in a_pattern.finditer(content):
        a_text = m.group(1).strip()
        a_text = a_text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#39;', "'")
        a_text = a_text.replace('&nbsp;', ' ')
        a_text = re.sub(r'<[^>]+>', '', a_text)
        a_text = a_text.strip()
        if a_text:
            answers.append(a_text)
    
    return questions, answers

def load_existing_translations(filepath):
    """Load existing translation keys from global_translations.js."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    keys = set()
    key_pattern = re.compile(r'^\s*"((?:[^"\\]|\\.)*)"\s*:', re.MULTILINE)
    for m in key_pattern.finditer(content):
        key = m.group(1)
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
    
    report_lines = []
    
    report_lines.append("=" * 70)
    report_lines.append("PHYSICS QUIZ FILE INVENTORY")
    report_lines.append("=" * 70)
    total_files = 0
    for unit_name, files in sorted(units.items(), key=lambda x: int(re.search(r'\d+', x[0]).group())):
        report_lines.append(f"  {unit_name}: {len(files)} quiz files")
        total_files += len(files)
    report_lines.append(f"\n  TOTAL: {total_files} quiz files")
    
    # Extract all strings from all quiz files
    all_questions = set()
    all_answers = set()
    unit_questions = OrderedDict()
    unit_answers = OrderedDict()
    
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
    
    report_lines.append(f"\n{'=' * 70}")
    report_lines.append("EXTRACTION RESULTS")
    report_lines.append(f"{'=' * 70}")
    report_lines.append(f"  Total unique question strings: {len(all_questions)}")
    report_lines.append(f"  Total unique answer option strings: {len(all_answers)}")
    all_strings = all_questions | all_answers
    report_lines.append(f"  Total unique strings (combined): {len(all_strings)}")
    
    # Load existing translations
    existing_keys = load_existing_translations(TRANSLATIONS_FILE)
    report_lines.append(f"\n  Existing translation keys in global_translations.js: {len(existing_keys)}")
    
    # Check overlap
    translated_questions = all_questions & existing_keys
    translated_answers = all_answers & existing_keys
    translated_all = all_strings & existing_keys
    untranslated = all_strings - existing_keys
    
    # Also check numbered versions
    numbered_translated = set()
    for s in untranslated:
        for i in range(1, 20):
            numbered_key = f"{i}. {s}"
            if numbered_key in existing_keys:
                numbered_translated.add(s)
                break
    
    untranslated_final = untranslated - numbered_translated
    
    report_lines.append(f"\n  Already translated questions: {len(translated_questions)}")
    report_lines.append(f"  Already translated answers: {len(translated_answers)}")
    report_lines.append(f"  Already translated total: {len(translated_all)}")
    report_lines.append(f"  Translated with number prefix: {len(numbered_translated)}")
    report_lines.append(f"  NOT yet translated: {len(untranslated_final)}")
    
    # Show sample of translated strings
    report_lines.append(f"\n  Sample of already-translated strings (first 20):")
    for s in sorted(translated_all)[:20]:
        report_lines.append(f'    TRANSLATED: "{s}"')
    
    # Write report
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        for line in report_lines:
            f.write(line + '\n')
            print(line)
    
    # Now generate the Python dict file with ALL untranslated strings organized by unit
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        out.write("# Physics Quiz - Untranslated strings organized by unit\n")
        out.write("# Format: \"english\": \"english\"  (fill in Chinese translations later)\n")
        out.write(f"# Total untranslated: {len(untranslated_final)}\n")
        out.write(f"# Already translated: {len(translated_all)}\n\n")
        out.write("physics_quiz_translations = {\n")
        
        total_written = 0
        globally_seen = set()  # Track strings already written to avoid duplicates across lessons
        
        for unit_name in unit_questions:
            unit_num = re.search(r'\d+', unit_name).group()
            
            # Collect strings in lesson order (Q + A interleaved per lesson)
            unit_strings_written = 0
            unit_block = []
            
            for lesson_id, qs in unit_questions[unit_name]:
                lesson_strings = []
                
                # Add questions for this lesson
                for q in qs:
                    if q in untranslated_final and q not in globally_seen:
                        escaped = q.replace('\\', '\\\\').replace('"', '\\"')
                        lesson_strings.append(f'    "{escaped}": "{escaped}",\n')
                        globally_seen.add(q)
                
                # Add answers for this lesson
                lesson_idx = [i for i, (lid, _) in enumerate(unit_answers[unit_name]) if lid == lesson_id]
                if lesson_idx:
                    _, ans_list = unit_answers[unit_name][lesson_idx[0]]
                    for a in ans_list:
                        if a in untranslated_final and a not in globally_seen:
                            escaped = a.replace('\\', '\\\\').replace('"', '\\"')
                            lesson_strings.append(f'    "{escaped}": "{escaped}",\n')
                            globally_seen.add(a)
                
                if lesson_strings:
                    unit_block.append(f"    # {lesson_id}\n")
                    unit_block.extend(lesson_strings)
                    unit_strings_written += len(lesson_strings)
            
            if unit_block:
                out.write(f"\n    # --- Unit {unit_num} ---\n")
                for line in unit_block:
                    out.write(line)
                total_written += unit_strings_written
        
        out.write("}\n")
        
        # Also write the already-translated strings as a reference
        out.write(f"\n\n# Already translated strings ({len(translated_all)} total) - for reference only\n")
        out.write("already_translated = {\n")
        for s in sorted(translated_all):
            escaped = s.replace('\\', '\\\\').replace('"', '\\"')
            out.write(f'    "{escaped}",\n')
        out.write("}\n")
    
    print(f"\n  Output written to: {OUTPUT_FILE}")
    print(f"  Report written to: {REPORT_FILE}")
    print(f"  Total untranslated strings in dict: {total_written}")
    print(f"  (Note: deduplication across lessons means total may differ from per-lesson count)")

if __name__ == '__main__':
    main()
