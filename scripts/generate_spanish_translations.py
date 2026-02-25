import json
import re
import time
import os
from deep_translator import GoogleTranslator

# Paths
GLOBAL_TRANS_PATH = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js"
SPANISH_TRANS_PATH = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\spanish_translations.js"

def log_message(msg):
    with open("translation_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {msg}\n")
    print(msg)

def unescape_js_string(s):
    # Basic unescape for JS strings captured raw
    return s.replace(r'\"', '"').replace(r'\\', '\\')

def load_keys_from_js(filepath):
    """
    Extracts keys from a JS file that defines a `translations` object.
    It looks for lines like `"Key": "Value",`
    """
    keys = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find "Key": "Value" pattern
        # Be robust about spacing and quotes
        # This matches: "Key String": "Value String"
        # We only capture the key.
        matches = re.finditer(r'^\s*["\']((?:[^"\\]|\\.)+)["\']\s*:\s*["\'].+?["\'],?$', content, re.MULTILINE)
        for match in matches:
            raw_key = match.group(1)
            # We need to unescape because the regex captured the escaping backslashes
            keys.append(unescape_js_string(raw_key))
            
    except Exception as e:
        log_message(f"Error reading {filepath}: {e}")
    return keys

def load_existing_spanish_translations(filepath):
    """
    Loads existing translations from spanish_translations.js if it exists.
    Returns a dictionary of {key: value}.
    """
    translations = {}
    if not os.path.exists(filepath):
        return translations
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Parse content to find existing key-values
        matches = re.finditer(r'^\s*["\']((?:[^"\\]|\\.)+)["\']\s*:\s*["\']((?:[^"\\]|\\.)+)["\'],?$', content, re.MULTILINE)
        for match in matches:
            raw_key = match.group(1)
            raw_val = match.group(2)
            translations[unescape_js_string(raw_key)] = unescape_js_string(raw_val)
            
    except Exception as e:
        log_message(f"Error reading existing Spanish translations: {e}")
        
    return translations

def save_spanish_translations(translations, filepath):
    """
    Writes the translations to spanish_translations.js in the correct format.
    """
    header = """/* Spanish Translations for ArisEdu */
(function() {
    'use strict';

    const spanishTranslations = {
"""
    footer = """
    };

    // Export to global scope
    window.spanishTranslations = spanishTranslations;
    window.arisEduSpanishTranslations = spanishTranslations;

})();
"""
    
    # Sort keys for consistency
    sorted_keys = sorted(translations.keys())
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(header)
        for i, key in enumerate(sorted_keys):
            val = translations[key]
            # Escape " in key and value
            # Since key is now unescaped string, we re-escape it for writing to JS
            safe_key = key.replace('\\', '\\\\').replace('"', '\\"') # Escape backslashes first, then quotes
            safe_val = val.replace('\\', '\\\\').replace('"', '\\"')
             # Add comma except for last item
            comma = "," if i < len(sorted_keys) - 1 else ""
            f.write(f'    "{safe_key}": "{safe_val}"{comma}\n')
        f.write(footer)
        
    log_message(f"Saved {len(translations)} translations to {filepath}")

def run_translation():
    # 1. Get all English keys from global_translations.js
    log_message(f"Loading source keys from {GLOBAL_TRANS_PATH}...")
    source_keys = load_keys_from_js(GLOBAL_TRANS_PATH)
    log_message(f"Found {len(source_keys)} source keys.")
    
    # 2. Get existing Spanish translations
    log_message(f"Loading existing translations from {SPANISH_TRANS_PATH}...")
    existing_translations = load_existing_spanish_translations(SPANISH_TRANS_PATH)
    log_message(f"Found {len(existing_translations)} existing translations.")
    
    # 3. Identify missing keys
    missing_keys = [k for k in source_keys if k not in existing_translations]
    log_message(f"Missing {len(missing_keys)} translations.")
    
    if not missing_keys:
        log_message("All keys are already translated!")
        return

    # 4. Translate missing keys in batches
    BATCH_SIZE = 50
    missing_count = len(missing_keys)
    log_message(f"Starting to translate {missing_count} keys in batches of {BATCH_SIZE}...")
    
    # Using GoogleTranslator for better batch support, or iterate if needed
    translator = GoogleTranslator(source='en', target='es')
    
    # Keep track of updated keys
    for k in missing_keys:
        existing_translations[k] = ""  # Placeholder
        
    keys_to_translate = missing_keys
    
    new_translations_count = 0
    
    # Loop through chunks
    for i in range(0, missing_count, BATCH_SIZE):
        chunk = keys_to_translate[i : i + BATCH_SIZE]
        
        try:
            # Be nice to the API
            if i > 0:
                 time.sleep(1.5) 
            
            log_message(f"Translating chunk {i//BATCH_SIZE + 1}/{(missing_count // BATCH_SIZE) + 1} (Items {i+1}-{min(i+BATCH_SIZE, missing_count)})...")
            
            translated_chunk = translator.translate_batch(chunk)
            
            # Update our main dictionary
            for idx, trans in enumerate(translated_chunk):
                original_key = chunk[idx]
                if trans:
                    existing_translations[original_key] = trans
                    new_translations_count += 1
                else:
                    # Fallback if translation fails/returns empty
                    existing_translations[original_key] = original_key

            log_message(f"  -> Success in chunk {i//BATCH_SIZE + 1}. Total translated: {new_translations_count}")

            # Save every 500 items (10 chunks) to be safe
            if new_translations_count > 0 and new_translations_count % 500 == 0:
                 log_message("Saving intermediate progress...")
                 save_spanish_translations(existing_translations, SPANISH_TRANS_PATH)

        except Exception as e:
            log_message(f"Error translating chunk starting at index {i}: {e}")
            # If a chunk fails, try to save progress so far
            if new_translations_count > 0:
                 save_spanish_translations(existing_translations, SPANISH_TRANS_PATH)
            time.sleep(5)
            continue

    # Final Save
    if new_translations_count > 0:
        log_message("Saving final updated translations...")
        save_spanish_translations(existing_translations, SPANISH_TRANS_PATH)
        log_message(f"Done! Added {new_translations_count} new translations.")
    else:
        log_message("No new translations were generated.")

if __name__ == "__main__":
    run_translation()
