#!/usr/bin/env python3
"""Check for ASCII double quotes in Chinese translations."""
import sys
sys.path.insert(0, r"c:\Users\Peter\pkang6689-pixel.github.io")
from batch_bio_templates import template_translations
from batch_bio_summary import summary_translations
from batch_bio_quiz import quiz_translations

all_t = {}
all_t.update(template_translations)
all_t.update(summary_translations)
all_t.update(quiz_translations)

issues = 0
for key, (zh, es, hi) in all_t.items():
    if '"' in zh:
        issues += 1
        print(f"ISSUE in Chinese: {key[:60]}")
    if '"' in es:
        issues += 1
        print(f"ISSUE in Spanish: {key[:60]}")
    if '"' in hi:
        issues += 1
        print(f"ISSUE in Hindi: {key[:60]}")
print(f"Total quote issues: {issues}")
