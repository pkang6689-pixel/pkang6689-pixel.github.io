"""
generate_ap_translations_v4.py
================================
Fast AP course translation using chunked Google Translate calls.
Packs multiple strings per API call using ||| delimiter for ~50x speedup.
Resumes from existing translations (skips already-done).

Usage:
    python generate_ap_translations_v4.py
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
LOG_FILE = os.path.join(REPO_ROOT, "ap_v4_progress.txt")

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

DELIMITER = "\n|||\n"
CHAR_LIMIT = 4800  # Google Translate limit is ~5000 chars
SAVE_EVERY = 500   # Save progress every N translations


def log(msg):
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


def build_chunks(strings):
    """Group strings into chunks that fit within the character limit."""
    chunks = []
    current = []
    current_len = 0

    for s in strings:
        added = len(s) + len(DELIMITER)
        if current_len + added > CHAR_LIMIT and current:
            chunks.append(current)
            current = [s]
            current_len = len(s)
        else:
            current.append(s)
            current_len += added

    if current:
        chunks.append(current)
    return chunks


def translate_chunk(translator, chunk, retries=2):
    """Translate a chunk of strings joined by delimiter. Returns dict or None."""
    combined = DELIMITER.join(chunk)
    for attempt in range(retries + 1):
        try:
            result = translator.translate(combined)
            parts = re.split(r'\s*\|\|\|\s*', result)
            if len(parts) == len(chunk):
                return {eng: trans.strip() for eng, trans in zip(chunk, parts) if trans.strip()}
            else:
                # Delimiter mangled - fall back to one-by-one for this chunk
                translations = {}
                for s in chunk:
                    try:
                        t = translator.translate(s)
                        if t and t.strip():
                            translations[s] = t.strip()
                        time.sleep(0.2)
                    except Exception:
                        time.sleep(1)
                return translations
        except Exception as e:
            if attempt < retries:
                time.sleep(2 ** (attempt + 1))
            else:
                return None
    return None


def translate_course_language(strings, gt_lang_code, lang_name, out_path):
    """Translate all missing strings for one course-language combo."""
    # Load existing
    existing = {}
    if os.path.exists(out_path):
        try:
            with open(out_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except (json.JSONDecodeError, OSError):
            existing = {}

    missing = [s for s in strings if s not in existing]
    if not missing:
        log(f"    All {len(strings)} already done [OK]")
        return len(strings)

    log(f"    {len(missing)} to translate ({len(existing)} existing)")

    translator = GoogleTranslator(source='en', target=gt_lang_code)
    chunks = build_chunks(missing)
    translated = dict(existing)
    new_count = 0
    errors = 0

    for i, chunk in enumerate(chunks):
        result = translate_chunk(translator, chunk)
        if result:
            translated.update(result)
            new_count += len(result)
        else:
            errors += len(chunk)

        # Progress report every 10 chunks
        if (i + 1) % 10 == 0 or (i + 1) == len(chunks):
            log(f"    [{lang_name}] chunk {i+1}/{len(chunks)} - {new_count} new, {errors} errors")

        # Save periodically
        if new_count > 0 and new_count % SAVE_EVERY < len(chunk):
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(translated, f, ensure_ascii=False, indent=2)

        time.sleep(0.3)

    # Final save
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)

    log(f"    [{lang_name}] Done: {new_count} new translations, {errors} errors, {len(translated)} total")
    return len(translated)


def main():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("")

    log("=" * 60)
    log("AP Translation Generator v4 (Chunked Google Translate)")
    log("=" * 60)

    total_translated = 0
    start_time = time.time()

    for filename, section_slug in AP_FILE_MAP.items():
        filepath = os.path.join(AP_DIR, filename)
        if not os.path.exists(filepath):
            log(f"\nSKIP: {filename}")
            continue

        log(f"\n--- {section_slug} ({filename}) ---")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        strings = extract_strings(data)
        log(f"  {len(strings)} unique strings")

        for lang_code, (gt_code, lang_name) in LANGUAGES.items():
            lang_dir = os.path.join(OUT_DIR, lang_code)
            os.makedirs(lang_dir, exist_ok=True)
            out_path = os.path.join(lang_dir, f"{section_slug}.json")

            log(f"  [{lang_code}]")
            count = translate_course_language(strings, gt_code, lang_name, out_path)
            total_translated += count

    elapsed = time.time() - start_time
    log(f"\n{'=' * 60}")
    log(f"Done! {total_translated} total translations in {elapsed:.0f}s ({elapsed/60:.1f}min)")
    log("=" * 60)


if __name__ == "__main__":
    main()
