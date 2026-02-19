"""Dump all untranslated quiz+flashcard strings grouped by unit for translation."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE, 'need_translation_quiz_flash.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)

by_unit = {}
for text, src in data.items():
    unit = src.split(':')[1]  # e.g. "U1"
    by_unit.setdefault(unit, []).append(text)

for unit in sorted(by_unit.keys(), key=lambda x: int(x[1:])):
    outpath = os.path.join(BASE, f'strings_{unit}.txt')
    with open(outpath, 'w', encoding='utf-8') as f:
        for s in sorted(by_unit[unit]):
            f.write(s + '\n')
    print(f"{unit}: {len(by_unit[unit])} strings -> strings_{unit}.txt")

# Also dump summary strings by unit
with open(os.path.join(BASE, 'need_translation_summary.json'), 'r', encoding='utf-8') as f:
    sdata = json.load(f)

summ_by_unit = {}
for text, src in sdata.items():
    unit = src.split(':')[1]
    summ_by_unit.setdefault(unit, []).append(text)

for unit in sorted(summ_by_unit.keys(), key=lambda x: int(x[1:])):
    outpath = os.path.join(BASE, f'strings_summary_{unit}.txt')
    with open(outpath, 'w', encoding='utf-8') as f:
        for s in sorted(summ_by_unit[unit]):
            f.write(s + '\n')
    print(f"Summary {unit}: {len(summ_by_unit[unit])} strings -> strings_summary_{unit}.txt")
