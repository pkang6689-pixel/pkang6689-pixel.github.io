#!/usr/bin/env python3
"""
Run all Algebra 2 translation batches for injection into translations_master.json

Now uses consolidated algebra2_translations_database.py for cleaner organization.
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from inject_translations_util import inject_all

# Import all translations from consolidated database
from algebra2_translations_database import (
    summary_a_translations,
    summary_b_translations, 
    summary_c_translations,
    summary_d_translations,
    quiz_a_translations,
    quiz_b_translations,
    quiz_c_translations,
    quiz_d_translations,
    quiz_e_translations,
    answers_a_translations,
    answers_b_translations,
    answers_c_translations,
    answers_d_translations,
    all_translations as all_alg2_translations
)

# Use pre-combined translations from database
# (uncomment old method if needed):
# all_alg2_translations = {}
# all_alg2_translations.update(summary_a_translations)
# all_alg2_translations.update(summary_b_translations)
# ... etc

print(f"Total Algebra 2 entries to inject: {len(all_alg2_translations)}")
print(f"Summary A: {len(summary_a_translations)}")
print(f"Summary B: {len(summary_b_translations)}")
print(f"Summary C: {len(summary_c_translations)}")
print(f"Summary D: {len(summary_d_translations)}")
print(f"Quiz A: {len(quiz_a_translations)}")
print(f"Quiz B: {len(quiz_b_translations)}")
print(f"Quiz C: {len(quiz_c_translations)}")
print(f"Quiz D: {len(quiz_d_translations)}")
print(f"Quiz E: {len(quiz_e_translations)}")
print(f"Answers A: {len(answers_a_translations)}")
print(f"Answers B: {len(answers_b_translations)}")
print(f"Answers C: {len(answers_c_translations)}")
print(f"Answers D: {len(answers_d_translations)}")

# Inject all translations
print("\nInjecting Algebra 2 translations...")
inject_all(all_alg2_translations, decode_entities=True)
print("Algebra 2 injection complete!")
