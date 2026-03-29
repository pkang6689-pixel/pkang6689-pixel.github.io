#!/usr/bin/env python3
"""
Background translation script using Google Gemini API (free tier).
Fills in Spanish translations for empty JSON values across all courses.
Runs with automatic rate limiting and error recovery.
"""

import json
import os
import time
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import logging

try:
    # Try new package first
    import google.genai as genai
except ImportError:
    try:
        # Fall back to deprecated package
        import google.generativeai as genai
    except ImportError:
        print("ERROR: google.genai or google.generativeai not installed.")
        print("Install with: pip install google-genai")
        sys.exit(1)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('translation_progress.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
TRANSLATIONS_DIR = Path("ArisEdu Project Folder/translations")
LANGUAGE = "es"  # Spanish
BATCH_SIZE = 10  # Process 10 keys at a time per API call
DELAY_BETWEEN_BATCHES = 2  # 2 second delay between batches to avoid rate limiting
DELAY_BETWEEN_FILES = 0.5  # Small delay between files
MAX_RETRIES = 3

# Gemini model configuration
MODEL_NAME = "gemini-2.0-flash"  # Free tier model
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]


def configure_genai():
    """Configure Google Generative AI with API key from environment."""
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        logger.error("GOOGLE_API_KEY environment variable not set!")
        logger.error("\nTo use this service:")
        logger.error("  1. Get free API key from: https://aistudio.google.com/app/apikey")
        logger.error("  2. Set environment variable:")
        logger.error("     Windows:  set GOOGLE_API_KEY=your-key")
        logger.error("     Linux:    export GOOGLE_API_KEY=your-key")
        logger.error("  3. Run again: python translate_spanish.py")
        return False

    try:
        genai.configure(api_key=api_key)
        logger.info("Configured Gemini API with API key")
        return True
    except Exception as e:
        logger.error(f"Failed to configure Gemini API: {e}")
        return False


def translate_batch(texts: List[str], target_language: str = "Spanish") -> Dict[str, str]:
    """Translate a batch of texts using Gemini API."""
    if not texts:
        return {}

    # Create prompt for batch translation
    prompt = f"""Translate the following English texts to {target_language}.
Return ONLY a JSON object with the same keys mapped to Spanish translations.
Do not add any explanation or additional text.

Texts to translate:
{json.dumps(texts, ensure_ascii=False)}

Return only valid JSON with the translations."""

    for attempt in range(MAX_RETRIES):
        try:
            model = genai.GenerativeModel(model_name=MODEL_NAME, safety_settings=safety_settings)
            response = model.generate_content(prompt)

            if not response.text:
                logger.warning(f"Empty response from Gemini API (attempt {attempt + 1})")
                time.sleep(2 ** attempt)  # Exponential backoff
                continue

            # Parse JSON response
            try:
                result_text = response.text.strip()
                # Remove markdown code blocks if present
                if result_text.startswith("```json"):
                    result_text = result_text[7:]
                if result_text.startswith("```"):
                    result_text = result_text[3:]
                if result_text.endswith("```"):
                    result_text = result_text[:-3]

                translations = json.loads(result_text.strip())
                return translations
            except json.JSONDecodeError as e:
                logger.warning(f"Failed to parse Gemini response as JSON: {e}")
                logger.debug(f"Response was: {response.text[:200]}")
                time.sleep(2 ** attempt)
                continue

        except Exception as e:
            logger.warning(f"Gemini API error (attempt {attempt + 1}): {e}")
            time.sleep(2 ** attempt)  # Exponential backoff
            continue

    logger.error(f"Failed to translate batch after {MAX_RETRIES} retries")
    return {}


def translate_json_file(file_path: Path) -> Tuple[int, int]:
    """
    Translate a single JSON file.
    Returns (translated_count, skipped_count, error_count)
    """
    translated_count = 0
    skipped_count = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        logger.error(f"Failed to read {file_path}: {e}")
        return 0, 0

    # Find empty translations
    empty_keys = [k for k, v in data.items() if v == ""]

    if not empty_keys:
        # All translations complete
        return 0, len(data)

    logger.info(f"Translating {len(empty_keys)} items in {file_path.relative_to(TRANSLATIONS_DIR)}")

    # Process in batches
    for i in range(0, len(empty_keys), BATCH_SIZE):
        batch = empty_keys[i:i + BATCH_SIZE]

        # Translate batch
        translations = translate_batch(batch, target_language="Spanish")

        if not translations:
            logger.warning(f"Failed to translate batch in {file_path}")
            skipped_count += len(batch)
            continue

        # Update data with translations
        for key in batch:
            if key in translations:
                data[key] = translations[key]
                translated_count += 1
            else:
                skipped_count += 1

        # Rate limiting
        time.sleep(DELAY_BETWEEN_BATCHES)

    # Write back to file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.debug(f"Saved {file_path}")
    except Exception as e:
        logger.error(f"Failed to write {file_path}: {e}")
        return 0, len(data)

    time.sleep(DELAY_BETWEEN_FILES)
    return translated_count, skipped_count


def find_translation_files() -> List[Path]:
    """Find all Spanish translation JSON files."""
    es_dir = TRANSLATIONS_DIR / LANGUAGE
    if not es_dir.exists():
        logger.error(f"Translation directory not found: {es_dir}")
        return []

    files = sorted(es_dir.glob("**/*.json"))
    logger.info(f"Found {len(files)} translation files for {LANGUAGE}")
    return files


def main():
    logger.info("=" * 60)
    logger.info("Starting background Spanish translation with Gemini API")
    logger.info("=" * 60)

    # Configure API
    try:
        configure_genai()
    except Exception as e:
        logger.error(f"Failed to configure Gemini API: {e}")
        logger.info("Note: You may need to set GOOGLE_API_KEY environment variable")
        return

    # Find files
    files = find_translation_files()
    if not files:
        logger.error("No translation files found")
        return

    # Process files
    total_translated = 0
    total_skipped = 0
    files_processed = 0

    try:
        for file_path in files:
            try:
                translated, skipped = translate_json_file(file_path)
                total_translated += translated
                total_skipped += skipped
                files_processed += 1

                if files_processed % 10 == 0:
                    logger.info(f"Progress: {files_processed}/{len(files)} files, "
                              f"{total_translated} translated")

            except Exception as e:
                logger.error(f"Error processing {file_path}: {e}")
                continue

    except KeyboardInterrupt:
        logger.info("Translation interrupted by user")

    # Summary
    logger.info("=" * 60)
    logger.info(f"Translation Summary:")
    logger.info(f"  Files processed: {files_processed}/{len(files)}")
    logger.info(f"  Total translated: {total_translated}")
    logger.info(f"  Total skipped: {total_skipped}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
