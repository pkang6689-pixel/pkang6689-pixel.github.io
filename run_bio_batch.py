#!/usr/bin/env python3
"""Runner script that combines all biology batch files and injects translations."""
import sys, io, ast

log = open('_bio_result.txt', 'w', encoding='utf-8')

try:
    # Syntax check all batch files
    for fname in ['batch_bio_templates.py', 'batch_bio_summary.py', 'batch_bio_quiz.py']:
        with open(fname, encoding='utf-8') as f:
            ast.parse(f.read())
        log.write(f"Syntax check {fname}: OK\n")

    sys.path.insert(0, r'c:\Users\Peter\pkang6689-pixel.github.io')

    # Redirect stdout
    old_stdout = sys.stdout
    sys.stdout = log

    # Import all batch files
    from batch_bio_templates import template_translations
    print(f"Template translations: {len(template_translations)}")

    from batch_bio_summary import summary_translations
    print(f"Summary translations: {len(summary_translations)}")

    from batch_bio_quiz import quiz_translations
    print(f"Quiz translations: {len(quiz_translations)}")

    # Combine all
    all_translations = {}
    all_translations.update(template_translations)
    all_translations.update(summary_translations)
    all_translations.update(quiz_translations)
    print(f"Total combined: {len(all_translations)}")

    # Inject
    from inject_translations_util import inject_all
    result = inject_all(all_translations)
    print(f"Result: {result}")

    sys.stdout = old_stdout

except Exception as e:
    try:
        sys.stdout = old_stdout
    except:
        pass
    log.write(f"\nERROR: {e}\n")
    import traceback
    traceback.print_exc(file=log)

finally:
    log.close()
    # Also print to console
    with open('_bio_result.txt', encoding='utf-8') as f:
        print(f.read())
