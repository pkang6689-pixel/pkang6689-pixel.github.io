#!/usr/bin/env python3
"""Add extracted lesson notes translations to global_translations.js"""
import json
from pathlib import Path

# Load the extracted translations
print("Loading extracted translations...")
with open('lesson_notes_extracted.json', 'r', encoding='utf-8') as f:
    extracted_data = json.load(f)

# Collect all unique translation pairs
new_translations = {}
for entry in extracted_data:
    for english, chinese in entry.get('translation_pairs', []):
        if english and chinese and english not in new_translations:
            new_translations[english] = chinese

print(f"✓ Found {len(new_translations)} unique extracted translations\n")

# Load the current global_translations.js
global_js_path = Path('ArisEdu Project Folder/scripts/global_translations.js')
with open(global_js_path, 'r', encoding='utf-8') as f:
    global_content = f.read()

# Find the translations object and parse it
import re

js_pattern = r'const translations = \{(.*?)\s*\};'
match = re.search(js_pattern, global_content, re.DOTALL)

current_translations = {}
if match:
    translations_str = match.group(1)
    pair_pattern = r'"((?:[^"\\]|\\.)*)"\s*:\s*"((?:[^"\\]|\\.)*)"\s*(?:,|$)'
    
    for key_match in re.finditer(pair_pattern, translations_str):
        key = key_match.group(1)
        value = key_match.group(2)
        
        try:
            key = json.loads('"' + key + '"')
            value = json.loads('"' + value + '"')
            current_translations[key] = value
        except:
            pass

print(f"Current global_translations.js has {len(current_translations)} entries")

# Find translations that are new (not in global yet)
new_count = 0
for en, zh in new_translations.items():
    if en not in current_translations:
        current_translations[en] = zh
        new_count += 1

print(f"✓ Adding {new_count} new translations to global_translations.js\n")

# Rebuild the JavaScript file
output = """/* Global Translations for ArisEdu */
(function() {
    const translations = {
"""

# Sort translations by key for consistency
sorted_items = sorted(current_translations.items())
for i, (key, value) in enumerate(sorted_items):
    json_key = json.dumps(key, ensure_ascii=False)
    json_value = json.dumps(value, ensure_ascii=False)
    comma = "," if i < len(sorted_items) - 1 else ""
    output += f'    {json_key}: {json_value}{comma}\n'

output += """    };

    // Function to get translation
    function getTranslation(key) {
        return translations[key] || key;
    }

    // Function to translate element content
    function translateElement(element) {
        if (element.hasAttribute('data-en')) {
            const english = element.getAttribute('data-en');
            element.textContent = getTranslation(english);
        }
    }

    // Translate all elements with class "translatable"
    document.addEventListener('DOMContentLoaded', function() {
        const translatableElements = document.querySelectorAll('.translatable');
        translatableElements.forEach(el => {
            translateElement(el);
        });
    });

    // Export for use in other scripts
    window.translations = translations;
    window.getTranslation = getTranslation;

})();
"""

# Write the updated file
with open(global_js_path, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"✓ Updated global_translations.js")
print(f"✓ Total translations now: {len(current_translations)}")
print(f"✓ New translations added: {new_count}")
