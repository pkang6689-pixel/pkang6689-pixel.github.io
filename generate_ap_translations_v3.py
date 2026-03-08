"""
generate_ap_translations_v3.py
===============================
Fast AP course translation generator using Google Translate (free).
Uses threading to parallelize translation calls for speed.

Usage:
    python generate_ap_translations_v3.py
"""

import json
import os
import re
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from deep_translator import GoogleTranslator

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
AP_DIR = os.path.join(REPO_ROOT, "content_data", "AP_Courses")
OUT_DIR = os.path.join(REPO_ROOT, "ArisEdu Project Folder", "translations")

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

LANGUAGES = {
    "zh": ("zh-CN", "Chinese"),
    "es": ("es", "Spanish"),
    "hi": ("hi", "Hindi"),
}

MAX_WORKERS = 10  # concurrent translation threads
LOG_FILE = os.path.join(REPO_ROOT, "ap_v3_progress.txt")


def log(msg):
    """Print and log to file."""
    print(msg, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def strip_html(html_str):
    text = re.sub(r'<[^>]+>', '', html_str)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_strings(data):
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


def translate_one(text, gt_lang_code):
    """Translate a single string. Returns (original, translated) or (original, None) on error."""
    try:
        t = GoogleTranslator(source='en', target=gt_lang_code)
        result = t.translate(text)
        if result and result.strip():
            return (text, result.strip())
    except Exception:
        pass
    return (text, None)


def translate_strings_parallel(strings, gt_lang_code, lang_name):
    """Translate strings using thread pool for parallelism."""
    translations = {}
    total = len(strings)
    done = 0
    errors = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(translate_one, s, gt_lang_code): s for s in strings}
        
        for future in as_completed(futures):
            eng, trans = future.result()
            done += 1
            if trans:
                translations[eng] = trans
            else:
                errors += 1
            
            if done % 200 == 0 or done == total:
                log(f"    [{lang_name}] {done}/{total} ({errors} errors)")

    return translations


def save_progress(out_path, data):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    # Clear log file
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("")
    log("=" * 60)
    log("AP Course Translation Generator (Threaded Google Translate)")
    log("=" * 60)

    for filename, section_slug in AP_FILE_MAP.items():
        filepath = os.path.join(AP_DIR, filename)
        if not os.path.exists(filepath):
            log(f"\nSKIP: {filename} not found")
            continue

        log(f"\n--- {filename} -> {section_slug} ---")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        strings = extract_strings(data)
        log(f"  {len(strings)} unique strings")

        for lang_code, (gt_code, lang_name) in LANGUAGES.items():
            lang_dir = os.path.join(OUT_DIR, lang_code)
            os.makedirs(lang_dir, exist_ok=True)
            out_path = os.path.join(lang_dir, f"{section_slug}.json")

            existing = {}
            if os.path.exists(out_path):
                with open(out_path, "r", encoding="utf-8") as f:
                    try:
                        existing = json.load(f)
                    except json.JSONDecodeError:
                        existing = {}
                if existing:
                    log(f"  {lang_code}: {len(existing)} existing")

            missing = [s for s in strings if s not in existing]
            if not missing:
                log(f"  {lang_code}: All done [OK]")
                continue

            log(f"  {lang_code}: translating {len(missing)} strings...")
            start = time.time()
            new_translations = translate_strings_parallel(missing, gt_code, lang_name)
            elapsed = time.time() - start

            merged = {**existing, **new_translations}
            save_progress(out_path, merged)
            log(f"  {lang_code}: {len(new_translations)}/{len(missing)} translated in {elapsed:.0f}s -> {section_slug}.json")

    log(f"\n{'=' * 60}")
    log("Done!")


if __name__ == "__main__":
    main()
