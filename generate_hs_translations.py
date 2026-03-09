"""
generate_hs_translations.py
============================
Fills in missing translations for the 6 partially-translated high school courses.
Uses deep-translator (Google Translate, no API key needed) with chunking for speed.
Saves progress after every chunk so crashes don't lose work.

Courses: algebra_1, algebra_2, biology, chemistry, geometry, physics
"""

import json
import os
import re
import sys
import time
from deep_translator import GoogleTranslator

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(REPO_ROOT, "content_data")
OUT_DIR = os.path.join(REPO_ROOT, "ArisEdu Project Folder", "translations")

HS_FILE_MAP = {
    "algebra_1_lessons.json":   "algebra1",
    "algebra_2_lessons.json":   "algebra2",
    "biology_lessons.json":     "biology",
    "chemistry_lessons.json":   "chemistry",
    "geometry_lessons.json":    "geometry",
    "physics_lessons.json":     "physics",
}

LANGUAGES = {
    "zh": "zh-CN",
    "es": "es",
    "hi": "hi",
}

SEPARATOR = " ||| "
MAX_CHUNK_CHARS = 4500


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


def translate_chunk(texts, lang_code):
    joined = SEPARATOR.join(texts)
    for attempt in range(3):
        try:
            result = GoogleTranslator(source='en', target=lang_code).translate(joined)
            parts = result.split("|||")
            parts = [p.strip() for p in parts]
            if len(parts) == len(texts):
                return parts
            return None
        except Exception:
            if attempt < 2:
                time.sleep(3 * (attempt + 1))
    return None


def translate_one(text, lang_code):
    for attempt in range(5):
        try:
            return GoogleTranslator(source='en', target=lang_code).translate(text)
        except Exception:
            if attempt < 4:
                time.sleep(3 * (attempt + 1))
            else:
                return text


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def translate_and_save(missing, lang_code, out_path, existing):
    """Translate missing strings, saving to disk after every chunk."""
    merged = dict(existing)
    total = len(missing)
    done = 0
    start_time = time.time()

    # Build character-aware chunks
    chunks = []
    current_chunk = []
    current_len = 0
    for s in missing:
        added_len = len(s) + len(SEPARATOR)
        if current_len + added_len > MAX_CHUNK_CHARS and current_chunk:
            chunks.append(current_chunk)
            current_chunk = [s]
            current_len = len(s)
        else:
            current_chunk.append(s)
            current_len += added_len
    if current_chunk:
        chunks.append(current_chunk)

    for ci, chunk in enumerate(chunks):
        result = translate_chunk(chunk, lang_code)

        if result:
            for orig, trans in zip(chunk, result):
                merged[orig] = trans
                done += 1
        else:
            for s in chunk:
                merged[s] = translate_one(s, lang_code)
                done += 1

        # Save after every chunk
        save_json(out_path, merged)

        elapsed = time.time() - start_time
        rate = done / elapsed if elapsed > 0 else 0
        sys.stdout.write("\r    {}/{} translated ({:.0f} str/min)  ".format(
            done, total, rate * 60))
        sys.stdout.flush()

        time.sleep(0.2)

    print()
    return len(missing)


def main():
    log_path = os.path.join(REPO_ROOT, "hs_translation_log.txt")
    log = open(log_path, "w", encoding="utf-8")

    def log_print(msg):
        print(msg)
        log.write(msg + "\n")
        log.flush()

    log_print("=" * 60)
    log_print("High School Course Translation Gap-Fill")
    log_print("=" * 60)

    grand_total = 0

    for filename, section_slug in HS_FILE_MAP.items():
        filepath = os.path.join(CONTENT_DIR, filename)
        if not os.path.exists(filepath):
            log_print("SKIP: {} not found".format(filename))
            continue

        log_print("\n" + "-" * 50)
        log_print("Processing: {} -> {}".format(filename, section_slug))
        log_print("-" * 50)

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        strings = extract_strings(data)
        log_print("  Extracted {} unique strings from content_data".format(len(strings)))

        for lang_key, lang_code in LANGUAGES.items():
            lang_dir = os.path.join(OUT_DIR, lang_key)
            os.makedirs(lang_dir, exist_ok=True)
            out_path = os.path.join(lang_dir, "{}.json".format(section_slug))

            existing = {}
            if os.path.exists(out_path):
                with open(out_path, "r", encoding="utf-8") as f:
                    existing = json.load(f)

            missing = [s for s in strings if s not in existing]

            if not missing:
                log_print("  {}: All {} strings already translated".format(
                    lang_key, len(strings)))
                continue

            log_print("  {}: {} existing, {} missing -> translating...".format(
                lang_key, len(existing), len(missing)))

            added = translate_and_save(missing, lang_code, out_path, existing)
            grand_total += added

            # Re-read to report accurate count
            with open(out_path, "r", encoding="utf-8") as f:
                final = json.load(f)
            log_print("  {}: Wrote {} total keys to {}.json (+{} new)".format(
                lang_key, len(final), section_slug, added))

    log_print("\n" + "=" * 60)
    log_print("Done! Translated {} new strings total.".format(grand_total))
    log_print("=" * 60)
    log.close()


if __name__ == "__main__":
    main()
