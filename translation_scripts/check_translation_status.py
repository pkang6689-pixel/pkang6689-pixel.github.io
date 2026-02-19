"""Check how many lesson strings still need translation."""
import json, re, os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
GT_PATH = os.path.join(ROOT, 'ArisEdu Project Folder', 'scripts', 'global_translations.js')
UNTRANS_PATH = os.path.join(BASE, 'untranslated_lesson_strings.json')
BATCH1_PATH = os.path.join(BASE, 'batch1_translations.json')

# Read global_translations.js and extract existing keys
with open(GT_PATH, 'r', encoding='utf-8') as f:
    content = f.read()
# Match "key": "value" patterns
keys = set(re.findall(r'"([^"]+)":\s*"[^"]*"', content))
print(f"Existing translation keys in global_translations.js: {len(keys)}")

# Load untranslated strings
with open(UNTRANS_PATH, 'r', encoding='utf-8') as f:
    d = json.load(f)
strings = d['strings']  # dict: text -> source
print(f"Total untranslated lesson strings: {len(strings)}")

already = [t for t in strings if t in keys]
print(f"Already in global_translations.js: {len(already)}")
still_need = {t: s for t, s in strings.items() if t not in keys}
print(f"Still need translation: {len(still_need)}")

# Break down by type
quiz_need = {t: s for t, s in still_need.items() if s.startswith('quiz')}
flash_need = {t: s for t, s in still_need.items() if s.startswith('flash')}
summ_need = {t: s for t, s in still_need.items() if s.startswith('summary')}
print(f"  Quiz: {len(quiz_need)}")
print(f"  Flashcard: {len(flash_need)}")
print(f"  Summary: {len(summ_need)}")

# Check batch1 status
if os.path.exists(BATCH1_PATH):
    with open(BATCH1_PATH, 'r', encoding='utf-8') as f:
        b1 = json.load(f)
    b1_in_js = sum(1 for t in b1 if t in keys)
    b1_not_in_js = len(b1) - b1_in_js
    print(f"\nBatch1: {len(b1)} entries, {b1_in_js} already in JS, {b1_not_in_js} NOT yet injected")

# Write the still-needed strings grouped by unit and type for translation
quiz_by_unit = {}
flash_by_unit = {}
summ_by_unit = {}
for t, s in still_need.items():
    typ, unit = s.split(':')
    if typ == 'quiz':
        quiz_by_unit.setdefault(unit, []).append(t)
    elif typ == 'flash':
        flash_by_unit.setdefault(unit, []).append(t)
    elif typ == 'summary':
        summ_by_unit.setdefault(unit, []).append(t)

print("\nQuiz strings by unit:")
for u in sorted(quiz_by_unit.keys()):
    print(f"  {u}: {len(quiz_by_unit[u])}")
print("Flashcard strings by unit:")
for u in sorted(flash_by_unit.keys()):
    print(f"  {u}: {len(flash_by_unit[u])}")
print("Summary strings by unit:")
for u in sorted(summ_by_unit.keys()):
    print(f"  {u}: {len(summ_by_unit[u])}")

# Write quiz+flash strings to a file for translation
output = {}
for t, s in still_need.items():
    if not s.startswith('summary'):
        output[t] = s
json.dump(output, open(os.path.join(BASE, 'need_translation_quiz_flash.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2, sort_keys=True)
print(f"\nWrote {len(output)} quiz+flash strings to need_translation_quiz_flash.json")

# Write summary strings  
summ_out = {}
for t, s in still_need.items():
    if s.startswith('summary'):
        summ_out[t] = s
json.dump(summ_out, open(os.path.join(BASE, 'need_translation_summary.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2, sort_keys=True)
print(f"Wrote {len(summ_out)} summary strings to need_translation_summary.json")
