#!/usr/bin/env python3
import json
import re

# Read the JSON translation files
with open('translations_chinese.json', 'r', encoding='utf-8') as f:
    chinese_dict = json.load(f)
with open('translations_spanish.json', 'r', encoding='utf-8') as f:
    spanish_dict = json.load(f)
with open('translations_hindi.json', 'r', encoding='utf-8') as f:
    hindi_dict = json.load(f)

# Create JavaScript format for each
def dict_to_js(d, indent=4):
    lines = []
    for k, v in sorted(d.items()):
        # Escape quotes and backslashes
        v_escaped = v.replace('\\', '\\\\').replace('"', '\\"')
        lines.append(f'{" " * indent}"{k}": "{v_escaped}",')
    return '\n'.join(lines)

print("=" * 80)
print("CHINESE TRANSLATIONS (339 entries)")
print("=" * 80)
chinese_js = dict_to_js(chinese_dict)
# Show first 10 and last 10
chinese_lines = chinese_js.split('\n')
for line in chinese_lines[:10]:
    print(line)
print(f"    ... ({len(chinese_lines)} total entries) ...")
for line in chinese_lines[-10:]:
    print(line)

print("\n" + "=" * 80)
print("SPANISH TRANSLATIONS (339 entries)")
print("=" * 80)
spanish_js = dict_to_js(spanish_dict)
spanish_lines = spanish_js.split('\n')
for line in spanish_lines[:10]:
    print(line)
print(f"    ... ({len(spanish_lines)} total entries) ...")
for line in spanish_lines[-10:]:
    print(line)

print("\n" + "=" * 80)
print("HINDI TRANSLATIONS (339 entries)")
print("=" * 80)
hindi_js = dict_to_js(hindi_dict)
hindi_lines = hindi_js.split('\n')
for line in hindi_lines[:10]:
    print(line)
print(f"    ... ({len(hindi_lines)} total entries) ...")
for line in hindi_lines[-10:]:
    print(line)

# Save the JS-formatted versions for easy integration
with open('chinese_translations_js_format.txt', 'w', encoding='utf-8') as f:
    f.write(chinese_js)
with open('spanish_translations_js_format.txt', 'w', encoding='utf-8') as f:
    f.write(spanish_js)
with open('hindi_translations_js_format.txt', 'w', encoding='utf-8') as f:
    f.write(hindi_js)

print("\n✅ JS-formatted files saved!")
print("   - chinese_translations_js_format.txt")
print("   - spanish_translations_js_format.txt")
print("   - hindi_translations_js_format.txt")
