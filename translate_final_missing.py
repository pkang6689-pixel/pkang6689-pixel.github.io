#!/usr/bin/env python3
"""
Translate the 10 missing flashcard strings
"""

import json

# The 10 missing strings with simple translations
missing_translations = {
    "1.": "1.",
    "1/2.": "1/2.",
    "180°.": "180°.",
    "2π.": "2π.",
    "3.": "3.",
    "45°.": "45°.",
    "5.": "5.",
    "e ≈ ?": "e ≈ ?",
    "π.": "π.",
    "√2/2.": "√2/2.",
}

# Save translations
with open('/workspaces/ArisEdu/algebra2_final_missing_translations.json', 'w', encoding='utf-8') as f:
    json.dump(missing_translations, f, ensure_ascii=False, indent=2)

print(f"Created translation file for {len(missing_translations)} missing strings")

if __name__ == "__main__":
    print("Done!")
