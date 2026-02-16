
import json
import os

json_file_path = "/workspaces/ArisEdu/scripts/quiz_translations_filtered_1.json"
js_file_path = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"

with open(json_file_path, 'r', encoding='utf-8') as f:
    new_translations = json.load(f)

with open(js_file_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Find the end of the translations object
# We look for the last "};" which closes the "const translations = {" block.
# Assuming the file structure is correct and "};" appears near the end of the object definition.
# Based on my read, it is at line 5016.
# However, to be safe, I can search for `};` and verify it's the right place.

closure_index = js_content.rfind('};')
if closure_index == -1:
    print("Could not find the closing brace for translations object.")
    exit(1)

# Ensure it's the correct closure. The file continues after this closure.
# The `read_file` output showed:
# };
#
#     // Expose translations globally
#     window.arisEduTranslations = translations;

insertion_point = closure_index

# Prepare the string to insert
to_insert = "\n"
for key, value in new_translations.items():
    # Escape quotes in key and value
    safe_key = key.replace('"', '\\"')
    safe_value = value.replace('"', '\\"')
    # Check if key already exists to avoid duplicates is a good idea, but the user said "append them".
    # I will stick to appending. If duplicates exist, the last one wins in JS object logic usually, 
    # but having many duplicates increases file size.
    # However, searching for existing keys in a huge JS string is error prone without parsing.
    # I'll just append.
    
    to_insert += f'  "{safe_key}": "{safe_value}",\n'

# Construct new content
new_content = js_content[:insertion_point] + to_insert + js_content[insertion_point:]

with open(js_file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected translations.")
