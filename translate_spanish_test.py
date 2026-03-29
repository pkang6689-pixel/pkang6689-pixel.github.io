#!/usr/bin/env python3
"""
Quick test of Gemini API translation before running full batch.
Tests with just a few files to verify setup is correct.
"""

import json
import time
import os
from pathlib import Path
from typing import Dict, List

try:
    # Try new package first
    import google.genai as genai
except ImportError:
    try:
        # Fall back to deprecated package
        import google.generativeai as genai
    except ImportError:
        print("ERROR: google.genai or google.generativeai not installed")
        print("Install with: pip install google-genai")
        exit(1)

MODEL_NAME = "gemini-2.0-flash"
TRANSLATIONS_DIR = Path("ArisEdu Project Folder/translations")

def configure_genai():
    """Configure Gemini API with API key."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: GOOGLE_API_KEY not set")
        print()
        print("Get a free API key:")
        print("  1. Visit: https://aistudio.google.com/app/apikey")
        print("  2. Click 'Create API Key'")
        print("  3. Copy the key")
        print()
        print("Set the environment variable:")
        print("  Windows:  set GOOGLE_API_KEY=your-key")
        print("  Linux:    export GOOGLE_API_KEY=your-key")
        print()
        return False

    try:
        genai.configure(api_key=api_key)
        print("OK: Gemini API configured")
        return True
    except Exception as e:
        print(f"ERROR: Failed to configure: {e}")
        return False


def test_translation():
    """Test translating a single batch."""
    test_texts = [
        "What is algebra?",
        "Solve for x: 2x + 5 = 13",
        "The quadratic formula is used to solve equations.",
        "Find the roots of the polynomial."
    ]

    print(f"\nTesting translation of {len(test_texts)} sample texts...")
    print("Sample texts:")
    for i, text in enumerate(test_texts, 1):
        print(f"  {i}. {text}")

    prompt = f"""Translate the following English texts to Spanish.
Return ONLY a JSON object with each English text as key and Spanish translation as value.
Example format: {{"key1": "translation1", "key2": "translation2"}}

Texts:
{json.dumps(test_texts, ensure_ascii=False)}

Return ONLY valid JSON, no explanation."""

    try:
        print("\nCalling Gemini API...")
        model = genai.GenerativeModel(model_name=MODEL_NAME)
        response = model.generate_content(prompt)

        if not response.text:
            print("ERROR: Empty response from API")
            return False

        # Parse response
        result_text = response.text.strip()
        if result_text.startswith("```json"):
            result_text = result_text[7:]
        if result_text.startswith("```"):
            result_text = result_text[3:]
        if result_text.endswith("```"):
            result_text = result_text[:-3]

        translations = json.loads(result_text.strip())

        print("\nOK: API responded successfully!")
        print("\nTranslations:")
        for eng, esp in translations.items():
            print(f"  EN: {eng}")
            print(f"  ES: {esp}\n")

        return True

    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse response as JSON: {e}")
        print(f"Response: {response.text[:200]}")
        return False
    except Exception as e:
        print(f"ERROR: API call failed: {e}")
        return False


def test_files():
    """Test with actual translation files."""
    print("\nChecking translation file structure...")

    es_dir = TRANSLATIONS_DIR / "es"
    if not es_dir.exists():
        print(f"ERROR: Directory not found: {es_dir}")
        return False

    # Find first 5 files with empty translations
    all_files = sorted(es_dir.glob("**/*.json"))
    files_with_empty = []

    for f in all_files[:20]:  # Check first 20 files
        try:
            with open(f, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if any(v == "" for v in data.values()):
                    files_with_empty.append(f)
                    if len(files_with_empty) >= 5:
                        break
        except:
            pass

    if not files_with_empty:
        print("ERROR: No JSON files with empty translations found in first 20 files")
        return False

    print(f"OK: Found {len(files_with_empty)} test files with empty translations")
    print("Sample files:")
    for f in files_with_empty:
        print(f"  - {f.relative_to(TRANSLATIONS_DIR)}")

    return True


def main():
    print("=" * 60)
    print("Spanish Translation - Test Mode")
    print("=" * 60)

    # Check API configuration
    print("\n[1] Configuring Gemini API...")
    if not configure_genai():
        return

    # Test API translation
    print("\n[2] Testing API translation...")
    if not test_translation():
        print("\nERROR: API translation test failed")
        return

    # Check file structure
    print("\n[3] Checking translation files...")
    if not test_files():
        print("\nERROR: No translation files found")
        return

    # Success!
    print("\n" + "=" * 60)
    print("SUCCESS: All tests passed!")
    print("Run: python translate_spanish.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
