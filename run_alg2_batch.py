#!/usr/bin/env python3
"""
Run all Algebra 2 translation batches for injection into translations_master.json
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from inject_translations_util import inject_all

# Import all Algebra 2 batches
from batch_alg2_summary_a import summary_a_translations
from batch_alg2_summary_b import summary_b_translations
from batch_alg2_summary_c import summary_c_translations
from batch_alg2_summary_d import summary_d_translations
from batch_alg2_quiz_a import quiz_a_translations
from batch_alg2_quiz_b import quiz_b_translations
from batch_alg2_quiz_c import quiz_c_translations
from batch_alg2_quiz_d import quiz_d_translations
from batch_alg2_quiz_e import quiz_e_translations
from batch_alg2_answers_a import answers_a_translations
from batch_alg2_answers_b import answers_b_translations
from batch_alg2_answers_c import answers_c_translations
from batch_alg2_answers_d import answers_d_translations

# Combine all batches
all_alg2_translations = {}

# Summary batches
all_alg2_translations.update(summary_a_translations)
all_alg2_translations.update(summary_b_translations)
all_alg2_translations.update(summary_c_translations)
all_alg2_translations.update(summary_d_translations)

# Quiz batches
all_alg2_translations.update(quiz_a_translations)
all_alg2_translations.update(quiz_b_translations)
all_alg2_translations.update(quiz_c_translations)
all_alg2_translations.update(quiz_d_translations)
all_alg2_translations.update(quiz_e_translations)

# Answer batches
all_alg2_translations.update(answers_a_translations)
all_alg2_translations.update(answers_b_translations)
all_alg2_translations.update(answers_c_translations)
all_alg2_translations.update(answers_d_translations)

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
