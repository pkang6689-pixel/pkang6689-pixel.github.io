"""
generate_ap_translations_v2.py
===============================
Extracts all English strings from AP course content_data JSONs
and generates translation JSON files for zh, es, hi.

Uses deep-translator (Google Translate, no API key needed).

Usage:
    python generate_ap_translations_v2.py

Output:
    ArisEdu Project Folder/translations/{lang}/ap_biology.json
    ArisEdu Project Folder/translations/{lang}/ap_calculus.json
    etc.
"""

import json
import os
import re
import time
import sys
from deep_translator import GoogleTranslator

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
AP_DIR = os.path.join(REPO_ROOT, "content_data", "AP_Courses")
OUT_DIR = os.path.join(REPO_ROOT, "ArisEdu Project Folder", "translations")

# Map AP JSON filenames to translation section slugs
AP_FILE_MAP = {
    "ap_biology_lessons.json":               "ap_biology",
    "ap_calculus_ab_lessons.json":            "ap_calculus",
    "ap_chemistry_lessons.json":              "ap_chemistry",
    "ap_environmental_science_lessons.json":  "ap_environmental_science",
    "ap_human_geography_lessons.json":        "ap_hug",
    "ap_physics_2_lessons.json":              "ap_physics2",
    "ap_physics_c_-_mechanics_lessons.json":  "ap_physics_mechanics",
    "ap_statistics_lessons.json":             "ap_statistics",
}

# lang_code_for_files -> (google_translate_code, display_name)
LANGUAGES = {
    "zh": ("zh-CN", "Chinese"),
    "es": ("es", "Spanish"),
    "hi": ("hi", "Hindi"),
}


def strip_html(html_str):
    """Remove HTML tags, returning plain text."""
    text = re.sub(r'<[^>]+>', '', html_str)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_strings(data):
    """Extract all translatable English strings from an AP course JSON."""
    strings = set()

    for lesson in data.values():
        if lesson.get('title'):
            strings.add(lesson['title'])
        if lesson.get('course'):
            strings.add(lesson['course'])

        for sec in lesson.get('summary_sections', []):
            if sec.get('title'):
                strings.add(sec['title'])
            if sec.get('content_html'):
                plain = strip_html(sec['content_html'])
                if plain:
                    strings.add(plain)

        for fc in lesson.get('flashcards', []):
            if fc.get('question'):
                strings.add(fc['question'])
            if fc.get('answer'):
                strings.add(fc['answer'])

        for qq in lesson.get('quiz_questions', []):
            if qq.get('question_text'):
                strings.add(qq['question_text'])
            if qq.get('explanation'):
                strings.add(qq['explanation'])
            for opt in qq.get('options', []):
                if opt.get('text'):
                    strings.add(opt['text'])

    strings.discard('')
    return sorted(strings)


def translate_strings(strings, gt_lang_code, lang_name):
    """Translate strings using Google Translate via deep-translator.
    
    Translates individually (Google Translate handles long strings fine).
    Uses translate_batch for efficiency where possible.
    """
    translator = GoogleTranslator(source='en', target=gt_lang_code)
    translations = {}
    total = len(strings)
    errors = 0
    MAX_ERRORS = 20  # stop if too many consecutive errors
    consecutive_errors = 0

    # deep-translator's translate_batch works with lists
    BATCH_SIZE = 50
    
    for i in range(0, total, BATCH_SIZE):
        batch = strings[i:i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        total_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
        
        print(f"    [{lang_name}] Batch {batch_num}/{total_batches} ({len(translations)}/{total} done)...", flush=True)
        
        try:
            results = translator.translate_batch(batch)
            for eng, trans in zip(batch, results):
                if trans and trans.strip():
                    translations[eng] = trans.strip()
            consecutive_errors = 0
        except Exception as e:
            print(f"    Batch error: {e}. Falling back to individual...", flush=True)
            time.sleep(2)
            # Translate individually as fallback
            for s in batch:
                try:
                    t = translator.translate(s)
                    if t and t.strip():
                        translations[s] = t.strip()
                    consecutive_errors = 0
                    time.sleep(0.3)
                except Exception as e2:
                    errors += 1
                    consecutive_errors += 1
                    if consecutive_errors >= MAX_ERRORS:
                        print(f"    Too many consecutive errors ({MAX_ERRORS}), stopping {lang_name}.", flush=True)
                        return translations
                    time.sleep(2)
        
        # Small delay between batches to avoid rate limiting
        time.sleep(0.5)
    
    print(f"    [{lang_name}] Completed: {len(translations)}/{total} translated ({errors} errors)", flush=True)
    return translations


def save_progress(out_path, merged):
    """Save translations to file (called periodically for checkpointing)."""
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)


def main():
    print("=" * 60)
    print("AP Course Translation Generator (Google Translate)")
    print("=" * 60)

    for filename, section_slug in AP_FILE_MAP.items():
        filepath = os.path.join(AP_DIR, filename)
        if not os.path.exists(filepath):
            print(f"\nSKIP: {filename} not found")
            continue

        print(f"\n{'-' * 50}")
        print(f"Processing: {filename} -> {section_slug}")
        print(f"{'-' * 50}")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        strings = extract_strings(data)
        print(f"  Extracted {len(strings)} unique strings")

        for lang_code, (gt_code, lang_name) in LANGUAGES.items():
            lang_dir = os.path.join(OUT_DIR, lang_code)
            os.makedirs(lang_dir, exist_ok=True)
            out_path = os.path.join(lang_dir, f"{section_slug}.json")

            # Load existing translations (merge, don't overwrite)
            existing = {}
            if os.path.exists(out_path):
                with open(out_path, "r", encoding="utf-8") as f:
                    try:
                        existing = json.load(f)
                    except json.JSONDecodeError:
                        existing = {}
                if existing:
                    print(f"  {lang_code}: {len(existing)} existing translations")

            # Find strings that still need translation
            missing = [s for s in strings if s not in existing]
            if not missing:
                print(f"  {lang_code}: All {len(strings)} strings already translated [OK]")
                continue

            print(f"  {lang_code}: {len(missing)} strings need translation")

            new_translations = translate_strings(missing, gt_code, lang_name)

            # Merge with existing
            merged = {**existing, **new_translations}

            save_progress(out_path, merged)
            print(f"  {lang_code}: Wrote {len(merged)} total strings to {section_slug}.json")

    print(f"\n{'=' * 60}")
    print("Done!")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
