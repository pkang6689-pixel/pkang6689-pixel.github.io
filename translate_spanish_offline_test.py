#!/usr/bin/env python3
"""
Quick test of offline translation before running full batch.
"""

import json
from pathlib import Path

try:
    from transformers import MarianMTModel, MarianTokenizer
except ImportError:
    print("ERROR: transformers not installed")
    print("Install with: pip install transformers torch")
    exit(1)

MODEL_NAME = "Helsinki-NLP/Opus-MT-en-es"
TRANSLATIONS_DIR = Path("ArisEdu Project Folder/translations")


def main():
    print("=" * 60)
    print("Offline Spanish Translation - Test Mode")
    print("=" * 60)

    # Test 1: Load model
    print("\n[1] Loading MarianMT model...")
    print("(First time: downloads ~200MB model)")
    try:
        tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
        model = MarianMTModel.from_pretrained(MODEL_NAME)
        print("OK: Model loaded")
    except Exception as e:
        print(f"ERROR: Failed to load model: {e}")
        print("Make sure you have:")
        print("  - pip install transformers torch")
        print("  - Internet connection (for first-time download)")
        return

    # Test 2: Translate sample texts
    print("\n[2] Testing translation...")
    test_texts = [
        "What is algebra?",
        "Solve for x: 2x + 5 = 13",
        "The quadratic formula",
    ]

    try:
        inputs = tokenizer(test_texts, return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        translations = tokenizer.batch_decode(translated, skip_special_tokens=True)

        print("Translations:")
        for eng, esp in zip(test_texts, translations):
            print(f"  EN: {eng}")
            print(f"  ES: {esp}\n")

    except Exception as e:
        print(f"ERROR: Translation failed: {e}")
        return

    # Test 3: Check files
    print("[3] Checking translation files...")
    es_dir = TRANSLATIONS_DIR / "es"
    if not es_dir.exists():
        print(f"ERROR: Directory not found: {es_dir}")
        return

    all_files = list(es_dir.glob("**/*.json"))
    empty_files = []

    for f in all_files[:20]:
        try:
            with open(f, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if any(v == "" for v in data.values()):
                    empty_files.append(f)
                    if len(empty_files) >= 3:
                        break
        except:
            pass

    print(f"OK: Found {len(empty_files)} test files with empty translations")

    # Success!
    print("\n" + "=" * 60)
    print("SUCCESS: All tests passed!")
    print("Run: python translate_spanish_offline.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
