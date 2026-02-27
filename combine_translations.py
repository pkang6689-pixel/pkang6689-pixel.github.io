#!/usr/bin/env python3
import json

# Load all three translation files
with open('translations_chinese.json', 'r', encoding='utf-8') as f:
    chinese = json.load(f)
with open('translations_spanish.json', 'r', encoding='utf-8') as f:
    spanish = json.load(f)
with open('translations_hindi.json', 'r', encoding='utf-8') as f:
    hindi = json.load(f)

# Create combined master file
master = {}
for key in chinese:
    master[key] = {
        'english': key,
        'chinese': chinese[key],
        'spanish': spanish[key],
        'hindi': hindi[key]
    }

# Save master file
with open('translations_master.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

print(f'Master file created with {len(master)} entries')
print('\nSample entries from each subject area:')
print('=' * 80)

# Show samples from different subjects
samples = [
    'Introduction to Biology',
    'States of Matter',
    'Points Lines and Planes',
    'Physical Quantities & Units'
]

for sample in samples:
    if sample in master:
        entry = master[sample]
        print(f"\n{sample}:")
        print(f"  中文 (Chinese): {entry['chinese']}")
        print(f"  Español (Spanish): {entry['spanish']}")
        print(f"  हिंदी (Hindi): {entry['hindi']}")
