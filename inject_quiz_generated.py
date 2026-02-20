import json
import re

# Load generated translations
with open('generated_quiz_translations.json', 'r', encoding='utf-8') as f:
    generated = json.load(f)

# Update global translations file
global_path = r"ArisEdu Project Folder/scripts/global_translations.js"
with open(global_path, 'r', encoding='utf-8') as f:
    content = f.read()

insertion_marker = 'const translations = {'
if insertion_marker not in content:
    print("Marker not found!")
    exit(1)

new_entries_str = "\n  /* Injected Quiz Translations Batch 3 (Generated Patterns) */\n"
for k, v in generated.items():
    k_esc = k.replace('"', '\\"')
    v_esc = v.replace('"', '\\"')
    if f'"{k_esc}":' not in content:
        new_entries_str += f'  "{k_esc}": "{v_esc}",\n'

new_content = content.replace(insertion_marker, insertion_marker + new_entries_str)

with open(global_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Update remaining strings
with open('quiz_strings_remaining.json', 'r', encoding='utf-8') as f:
    remaining = json.load(f)

remaining_after = []
processed_keys = set(generated.keys())
for item in remaining:
    if item not in processed_keys:
        remaining_after.append(item)

with open('quiz_strings_remaining.json', 'w', encoding='utf-8') as f:
    json.dump(remaining_after, f, indent=4, ensure_ascii=False)

print(f"Injected {len(generated)} generated items. {len(remaining_after)} remaining.")
