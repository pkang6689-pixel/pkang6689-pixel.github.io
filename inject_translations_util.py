#!/usr/bin/env python3
"""
Translation injection utility.
Takes a dictionary of translations and injects them into all 3 translation JS files.

Usage:
    from inject_translations import inject_all
    inject_all({
        "English text": ("Chinese translation", "Spanish translation", "Hindi translation"),
        ...
    })
"""

import os
import re
import html as html_module

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"
SCRIPTS = os.path.join(BASE, "scripts")

FILES = {
    'chinese': os.path.join(SCRIPTS, "global_translations.js"),
    'spanish': os.path.join(SCRIPTS, "spanish_translations.js"),
    'hindi':   os.path.join(SCRIPTS, "hindi_translations.js"),
}

# Marker: the last entry in each file (all three end with the same key)
LAST_ENTRY_KEY = '🚀 SPACE SHOOTER'

def escape_js_string(s):
    """Escape a string for use inside JS double quotes."""
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '')
    return s

def decode_html_entities(s):
    """Decode HTML entities to actual characters."""
    return html_module.unescape(s)

def extract_existing_keys(filepath):
    """Get all existing translation keys from a JS file."""
    keys = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*"([^"]+)"\s*:', line)
            if m:
                keys.add(m.group(1))
    return keys

def inject_into_file(filepath, entries, lang_label):
    """
    Inject translation entries into a JS file.
    entries: list of (english_key, translation) tuples
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the last SPACE SHOOTER entry line
    insert_idx = None
    for i, line in enumerate(lines):
        if LAST_ENTRY_KEY in line and ':' in line:
            insert_idx = i
    
    if insert_idx is None:
        # Fallback: find the closing }; 
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip() == '};':
                insert_idx = i - 1
                break
    
    if insert_idx is None:
        print(f"  ERROR: Could not find injection point in {filepath}")
        return 0
    
    # Ensure the last entry has a trailing comma
    last_line = lines[insert_idx].rstrip('\n').rstrip('\r')
    if not last_line.rstrip().endswith(','):
        lines[insert_idx] = last_line + ',\n'
    
    # Build new entries
    new_lines = []
    existing_keys = extract_existing_keys(filepath)
    added = 0
    skipped = 0
    
    for eng_key, translation in entries:
        if eng_key in existing_keys:
            skipped += 1
            continue
        escaped_key = escape_js_string(eng_key)
        escaped_val = escape_js_string(translation)
        new_lines.append(f'    "{escaped_key}": "{escaped_val}",\n')
        added += 1
    
    if new_lines:
        # Remove trailing comma from last new entry (to be clean)
        last = new_lines[-1]
        new_lines[-1] = last.rstrip(',\n').rstrip(',') + '\n'
        
        # Insert after the last existing entry
        for nl in reversed(new_lines):
            lines.insert(insert_idx + 1, nl)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    
    print(f"  {lang_label}: +{added} entries ({skipped} already existed)")
    return added

def inject_all(translations_dict, decode_entities=True):
    """
    Inject translations into all 3 language files.
    
    translations_dict format:
        {
            "English text": ("Chinese translation", "Spanish translation", "Hindi translation"),
            ...
        }
    
    If decode_entities=True, HTML entities in keys are decoded to actual characters.
    """
    print(f"Injecting {len(translations_dict)} translation entries...")
    
    # Prepare entries for each language
    chinese_entries = []
    spanish_entries = []
    hindi_entries = []
    
    for eng_key, (ch, sp, hi) in translations_dict.items():
        if decode_entities:
            eng_key = decode_html_entities(eng_key)
        chinese_entries.append((eng_key, ch))
        spanish_entries.append((eng_key, sp))
        hindi_entries.append((eng_key, hi))
    
    total = 0
    total += inject_into_file(FILES['chinese'], chinese_entries, 'Chinese')
    total += inject_into_file(FILES['spanish'], spanish_entries, 'Spanish')
    total += inject_into_file(FILES['hindi'],   hindi_entries,   'Hindi')
    
    print(f"Total new entries added: {total}")
    return total

if __name__ == '__main__':
    # Test with a small example
    test = {
        "Test Entry": ("测试条目", "Entrada de prueba", "परीक्षण प्रविष्टि"),
    }
    inject_all(test, decode_entities=False)
