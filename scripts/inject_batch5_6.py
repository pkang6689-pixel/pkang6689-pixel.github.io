
import json
import os

translation_file = "ArisEdu Project Folder/scripts/global_translations.js"
batch_file = "scripts/quiz_translations_batch5_6.json"

# Load new translations
new_translations = json.load(open(batch_file))

# Format new translations as JS properties
formatted_lines = []
for key, value in new_translations.items():
    # Escape quotes in key and value
    key_escaped = key.replace('"', '\\"').replace('\n', '\\n')
    value_escaped = value.replace('"', '\\"').replace('\n', '\\n')
    formatted_lines.append(f'  "{key_escaped}": "{value_escaped}",')

formatted_block = "\n".join(formatted_lines)

# Read the JS file
with open(translation_file, "r") as f:
    content = f.read()

# Find the injection point.
# It ends with "Count only the heaviest atom": "..." before the closing brace.
# But relies on exact match.
# Instead, find the line `};` that closes `translations`.
# It's at line 5918 approx.
# We can search for the start `const translations = {` and iterate to find matching brace,
# or just look for the `window.arisEduTranslations = translations;` line which follows immediately.

marker = "window.arisEduTranslations = translations;"
split_index = content.find(marker)

if split_index == -1:
    print("Error: Could not find marker window.arisEduTranslations = translations;")
    exit(1)

# Backtrack from marker to find the closing brace `};`
# The file content before marker should end with `};` (and whitespace/newlines)
# Let's find the last occurrence of `};` before `split_index`
brace_index = content.rfind("};", 0, split_index)

if brace_index == -1:
    print("Error: Could not find closing brace before marker.")
    exit(1)

# Insert the new translations before the brace
# We need to ensure the previous item has a comma.
# Usually in JSON properties in JS, trailing comma is allowed but maybe not present if it was valid JSON style.
# Check character before brace (ignoring whitespace).

before_brace = content[:brace_index]
after_brace = content[brace_index:]

# Insert
new_content = before_brace + "\n" + formatted_block + "\n" + after_brace

with open(translation_file, "w") as f:
    f.write(new_content)

print(f"Injected {len(new_translations)} translations into global_translations.js")
