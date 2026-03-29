#!/usr/bin/env python3
"""
Offline Hindi translation using Hugging Face MarianMT models.
No API keys required - completely local and free.
Perfect for overnight batch processing.
"""

import json
import time
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import logging

try:
    from transformers import MarianMTModel, MarianTokenizer
except ImportError:
    print("ERROR: transformers not installed")
    print("Install with: pip install transformers torch")
    sys.exit(1)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('translation_progress_hindi.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
TRANSLATIONS_DIR = Path("ArisEdu Project Folder/translations")
LANGUAGE = "hi"  # Hindi
BATCH_SIZE = 5
MODEL_NAME = "Helsinki-NLP/Opus-MT-en-hi"  # English to Hindi

# Global model and tokenizer
model = None
tokenizer = None


def load_model():
    """Load MarianMT model and tokenizer."""
    global model, tokenizer

    if model is not None:
        return True

    try:
        logger.info(f"Loading translation model: {MODEL_NAME}")
        logger.info("(First run: downloads ~200MB model)")

        tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
        model = MarianMTModel.from_pretrained(MODEL_NAME)

        logger.info("Model loaded successfully!")
        return True

    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        return False


def translate_batch(texts: List[str]) -> Dict[str, str]:
    """Translate a batch of texts using local MarianMT model."""
    if not texts or model is None:
        return {}

    try:
        inputs = tokenizer(texts, return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        translations = tokenizer.batch_decode(translated, skip_special_tokens=True)

        result = {}
        for original, translated_text in zip(texts, translations):
            result[original] = translated_text

        return result

    except Exception as e:
        logger.error(f"Translation batch failed: {e}")
        return {}


def translate_json_file(file_path: Path) -> Tuple[int, int]:
    """Translate a single JSON file. Returns (translated_count, skipped_count)"""
    translated_count = 0
    skipped_count = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        logger.error(f"Failed to read {file_path}: {e}")
        return 0, 0

    empty_keys = [k for k, v in data.items() if v == ""]

    if not empty_keys:
        return 0, len(data)

    logger.info(f"Translating {len(empty_keys)} items in {file_path.relative_to(TRANSLATIONS_DIR)}")

    for i in range(0, len(empty_keys), BATCH_SIZE):
        batch = empty_keys[i:i + BATCH_SIZE]

        translations = translate_batch(batch)

        if not translations:
            logger.warning(f"Failed to translate batch in {file_path}")
            skipped_count += len(batch)
            continue

        for key in batch:
            if key in translations:
                data[key] = translations[key]
                translated_count += 1
            else:
                skipped_count += 1

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.debug(f"Saved {file_path}")
    except Exception as e:
        logger.error(f"Failed to write {file_path}: {e}")
        return 0, len(data)

    return translated_count, skipped_count


def find_translation_files() -> List[Path]:
    """Find all Hindi translation JSON files."""
    hi_dir = TRANSLATIONS_DIR / LANGUAGE
    if not hi_dir.exists():
        logger.error(f"Translation directory not found: {hi_dir}")
        return []

    files = sorted(hi_dir.glob("**/*.json"))
    logger.info(f"Found {len(files)} translation files for {LANGUAGE}")
    return files


def main():
    logger.info("=" * 60)
    logger.info("Starting OFFLINE Hindi translation (no API key needed)")
    logger.info("Using: Helsinki-NLP/Opus-MT-en-hi model")
    logger.info("=" * 60)

    if not load_model():
        logger.error("Cannot load translation model")
        return

    files = find_translation_files()
    if not files:
        logger.error("No translation files found")
        return

    total_translated = 0
    total_skipped = 0
    files_processed = 0
    start_time = time.time()

    try:
        for file_path in files:
            try:
                translated, skipped = translate_json_file(file_path)
                total_translated += translated
                total_skipped += skipped
                files_processed += 1

                if files_processed % 10 == 0:
                    elapsed = time.time() - start_time
                    logger.info(f"Progress: {files_processed}/{len(files)} files, "
                              f"{total_translated} translated, {elapsed:.0f}s elapsed")

            except Exception as e:
                logger.error(f"Error processing {file_path}: {e}")
                continue

    except KeyboardInterrupt:
        logger.info("Translation interrupted by user")

    elapsed = time.time() - start_time
    logger.info("=" * 60)
    logger.info(f"Translation Complete!")
    logger.info(f"  Files processed: {files_processed}/{len(files)}")
    logger.info(f"  Total translated: {total_translated}")
    logger.info(f"  Total skipped: {total_skipped}")
    logger.info(f"  Time elapsed: {elapsed:.1f}s ({elapsed/60:.1f}m)")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
