import json
import re
import os

GLOBAL_TRANS_PATH = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js"
SPANISH_TRANS_PATH = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\spanish_translations.js"
HINDI_TRANS_PATH = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\hindi_translations.js"

def unescape_js_string(s):
    return s.replace(r'\"', '"').replace(r'\\', '\\')

def load_keys_from_js(filepath):
    keys = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        matches = re.finditer(r'^\s*["\']((?:[^"\\]|\\.)+)["\']\s*:\s*["\'].+?["\'],?$', content, re.MULTILINE)
        for match in matches:
            keys.add(unescape_js_string(match.group(1)))
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return keys

def load_full_js(filepath):
    """Returns list of (key, value, original_line) tuples or dict"""
    data = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # capture key and value to reconstruct
        matches = re.finditer(r'^\s*["\']((?:[^"\\]|\\.)+)["\']\s*:\s*["\']((?:[^"\\]|\\.)+)["\'],?$', content, re.MULTILINE)
        for match in matches:
            k = unescape_js_string(match.group(1))
            v = unescape_js_string(match.group(2))
            data[k] = v
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return data

def save_js(data, filepath, var_name):
    header = f"""/* {var_name.replace('Translations', '').capitalize()} Translations for ArisEdu */
(function() {{
    'use strict';

    const {var_name} = {{
"""
    footer = f"""
    }};

    // Export to global scope
    window.{var_name} = {var_name};
    window.arisEdu{var_name[0].upper() + var_name[1:]} = {var_name};

}})();
"""
    sorted_keys = sorted(data.keys())
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(header)
        for i, key in enumerate(sorted_keys):
            val = data[key]
            safe_key = key.replace('\\', '\\\\').replace('"', '\\"')
            safe_val = val.replace('\\', '\\\\').replace('"', '\\"')
            comma = "," if i < len(sorted_keys) - 1 else ""
            f.write(f'    "{safe_key}": "{safe_val}"{comma}\n')
        f.write(footer)
    print(f"Saved cleaned {filepath} with {len(data)} items.")

def cleanup(target_path, var_name):
    print(f"Cleaning {target_path}...")
    valid_keys = load_keys_from_js(GLOBAL_TRANS_PATH)
    current_data = load_full_js(target_path)
    
    cleaned_data = {}
    removed_count = 0
    
    for k, v in current_data.items():
        if k in valid_keys:
            cleaned_data[k] = v
        else:
            removed_count += 1
            # print(f"Removing orphaned key: {k}")
            
    if removed_count > 0:
        print(f"Removed {removed_count} orphaned keys.")
        save_js(cleaned_data, target_path, var_name)
    else:
        print("No orphaned keys found.")

if __name__ == "__main__":
    cleanup(SPANISH_TRANS_PATH, "spanishTranslations")
    cleanup(HINDI_TRANS_PATH, "hindiTranslations")
