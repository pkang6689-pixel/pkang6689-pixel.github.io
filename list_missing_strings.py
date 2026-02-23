#!/usr/bin/env python3
"""Extract all missing geometry summary strings and generate Chinese translations.
Uses a translation mapping approach for geometry-specific terms."""
import json

# Load missing strings
with open('missing_geometry_summary_strings.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

missing = data['missing_strings']
print(f"Total missing strings: {len(missing)}")

# Load existing dictionary
with open('geometry_translation_dict.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

print(f"Existing dictionary size: {len(existing)}")

# Collect unique missing strings (deduplicated)
unique_missing = {}
for item in missing:
    text = item['text'].strip()
    if text and text not in existing and text not in unique_missing:
        unique_missing[text] = item['unit']

print(f"Unique missing strings (not in dict): {len(unique_missing)}")

# Save the unique strings for translation
with open('geometry_strings_to_translate.json', 'w', encoding='utf-8') as f:
    json.dump(list(unique_missing.keys()), f, ensure_ascii=False, indent=2)

print(f"Saved {len(unique_missing)} strings to geometry_strings_to_translate.json")

# Print them grouped by unit
by_unit = {}
for text, unit in unique_missing.items():
    by_unit.setdefault(unit, []).append(text)

for unit in sorted(by_unit.keys()):
    strings = by_unit[unit]
    print(f"\n=== {unit} ({len(strings)} strings) ===")
    for s in strings:
        print(f"  {s[:150]}")
