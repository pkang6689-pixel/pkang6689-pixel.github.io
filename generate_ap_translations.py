"""
generate_ap_translations.py
=============================
Extracts all English strings from AP course content_data JSONs
and generates translation JSON files for zh, es, hi.

Uses deep-translator (Google Translate, no API key needed).

Usage:
    python generate_ap_translations.py

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

LANGUAGES = {
    "zh": "Simplified Chinese",
    "es": "Spanish",
    "hi": "Hindi",
}


def strip_html(html_str):
    """Remove HTML tags, returning plain text."""
    text = re.sub(r'<[^>]+>', '', html_str)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_strings(data):
    """Extract all translatable English strings from an AP course JSON."""
    strings = set()

    for lesson in data.values():
        # Lesson title
        if lesson.get('title'):
            strings.add(lesson['title'])
        # Course name
        if lesson.get('course'):
            strings.add(lesson['course'])

        # Summary sections
        for sec in lesson.get('summary_sections', []):
            if sec.get('title'):
                strings.add(sec['title'])
            if sec.get('content_html'):
                # Store the plain-text version (what the DOM will show)
                plain = strip_html(sec['content_html'])
                if plain:
                    strings.add(plain)

        # Flashcards
        for fc in lesson.get('flashcards', []):
            if fc.get('question'):
                strings.add(fc['question'])
            if fc.get('answer'):
                strings.add(fc['answer'])

        # Quiz questions
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


def translate_batch_gemini(strings, target_lang, target_lang_name, api_key):
    """Translate a batch of strings using Gemini API."""
    try:
        import google.generativeai as genai
    except ImportError:
        print("  google-generativeai not installed. Install with: pip install google-generativeai")
        return None

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    translations = {}
    batch_size = 30  # Translate in batches to stay within context limits

    for i in range(0, len(strings), batch_size):
        batch = strings[i:i + batch_size]
        batch_num = i // batch_size + 1
        total_batches = (len(strings) + batch_size - 1) // batch_size
        print(f"    Batch {batch_num}/{total_batches} ({len(batch)} strings)...", end="", flush=True)

        # Build the prompt
        numbered = "\n".join(f"{j+1}. {s}" for j, s in enumerate(batch))
        prompt = f"""Translate these English educational content strings to {target_lang_name}.
Return ONLY a JSON object mapping each English string to its {target_lang_name} translation.
Keep mathematical formulas, chemical formulas, variable names, and numbers unchanged.
Keep HTML entities as-is. Maintain the same academic tone.

Strings to translate:
{numbered}

Return format: {{"English string": "{target_lang_name} translation", ...}}
Return ONLY valid JSON, no markdown formatting, no code blocks."""

        try:
            response = model.generate_content(prompt)
            text = response.text.strip()
            # Remove markdown code block if present
            if text.startswith('```'):
                text = re.sub(r'^```\w*\n?', '', text)
                text = re.sub(r'\n?```$', '', text)
            result = json.loads(text)
            translations.update(result)
            print(f" OK ({len(result)} translated)")
        except json.JSONDecodeError as e:
            print(f" JSON parse error: {e}")
            # Try to salvage partial results
            try:
                # Sometimes Gemini adds trailing commas
                cleaned = re.sub(r',\s*}', '}', text)
                result = json.loads(cleaned)
                translations.update(result)
                print(f"    Salvaged {len(result)} translations")
            except Exception:
                print(f"    Could not salvage batch, skipping")
        except Exception as e:
            print(f" API error: {e}")

        # Rate limiting
        time.sleep(1)

    return translations


def translate_strings(strings, lang_code, lang_name, api_key=None):
    """Translate strings to target language."""
    if api_key:
        print(f"  Using Gemini API for {lang_name}...")
        result = translate_batch_gemini(strings, lang_code, lang_name, api_key)
        if result:
            return result

    # Fallback: return empty dict (no translations generated)
    print(f"  No API key — skipping {lang_name} (set GEMINI_API_KEY env var)")
    return {}


def main():
    api_key = os.environ.get('GEMINI_API_KEY', '')

    print("=" * 60)
    print("AP Course Translation Generator")
    print("=" * 60)

    if api_key:
        print(f"Gemini API key found ({api_key[:8]}...)")
    else:
        print("No GEMINI_API_KEY set - will generate empty translation files.")
        print("Set the env var and re-run to generate actual translations.")

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

        for lang_code, lang_name in LANGUAGES.items():
            lang_dir = os.path.join(OUT_DIR, lang_code)
            os.makedirs(lang_dir, exist_ok=True)
            out_path = os.path.join(lang_dir, f"{section_slug}.json")

            # Load existing translations if file exists (merge, don't overwrite)
            existing = {}
            if os.path.exists(out_path):
                with open(out_path, "r", encoding="utf-8") as f:
                    existing = json.load(f)
                print(f"  {lang_code}: {len(existing)} existing translations")

            # Find strings that still need translation
            missing = [s for s in strings if s not in existing]
            if not missing:
                print(f"  {lang_code}: All {len(strings)} strings already translated [OK]")
                continue

            print(f"  {lang_code}: {len(missing)} strings need translation")

            new_translations = translate_strings(missing, lang_code, lang_name, api_key)

            # Merge
            merged = {**existing, **new_translations}

            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(merged, f, ensure_ascii=False, indent=2)
            print(f"  {lang_code}: Wrote {len(merged)} total strings to {section_slug}.json")

    print(f"\n{'=' * 60}")
    print("Done!")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
