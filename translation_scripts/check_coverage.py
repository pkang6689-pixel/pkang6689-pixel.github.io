"""
Check coverage: which of the 3992 needed strings are covered by existing JSON files?
"""
import json, glob, os, re
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)

# Load all existing translations from JSON files
all_translated = {}
for pattern in ["unit*_translations.json", "summary_U*_translations.json", 
                "quiz_translations_batch*.json", "batch1_translations.json"]:
    for f in glob.glob(os.path.join(SCRIPT_DIR, pattern)):
        try:
            data = json.load(open(f, encoding="utf-8"))
            all_translated.update(data)
        except:
            pass

print(f"Total translated strings in JSON files: {len(all_translated)}")

# Load needed strings
needed_quiz = {}
needed_flash = {}
needed_summary = {}

try:
    needed_quiz = json.load(open(os.path.join(SCRIPT_DIR, "need_translation_quiz_flash.json"), encoding="utf-8"))
    print(f"Quiz+flash strings needed: {len(needed_quiz)}")
except:
    print("need_translation_quiz_flash.json not found")

try:
    needed_summary = json.load(open(os.path.join(SCRIPT_DIR, "need_translation_summary.json"), encoding="utf-8"))
    print(f"Summary strings needed: {len(needed_summary)}")
except:
    print("need_translation_summary.json not found")

# Check coverage
all_needed = {}
if isinstance(needed_quiz, dict):
    all_needed.update(needed_quiz)
elif isinstance(needed_quiz, list):
    for s in needed_quiz:
        all_needed[s] = None
if isinstance(needed_summary, dict):
    all_needed.update(needed_summary)
elif isinstance(needed_summary, list):
    for s in needed_summary:
        all_needed[s] = None

covered = 0
missing = []
for k in all_needed:
    if k in all_translated:
        covered += 1
    else:
        missing.append(k)

print(f"\nCoverage: {covered}/{len(all_needed)} ({100*covered/max(len(all_needed),1):.1f}%)")
print(f"Missing: {len(missing)}")

if missing:
    # Write missing strings to file
    with open(os.path.join(SCRIPT_DIR, "still_missing_translations.json"), "w", encoding="utf-8") as f:
        json.dump(sorted(missing), f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(missing)} missing strings to still_missing_translations.json")
    
    # Show first 30
    print("\nFirst 30 missing strings:")
    for s in sorted(missing)[:30]:
        print(f"  {s}")
