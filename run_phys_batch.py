#!/usr/bin/env python3
"""Runner: inject ALL physics translations (quiz + summary) into the 3 JS files."""

import ast, sys, os

# ── 1. Syntax-check every batch file ──────────────────────────────
batch_files = [
    "batch_phys_answers.py",
    "batch_phys_quiz_a.py",
    "batch_phys_quiz_b.py",
    "batch_phys_quiz_c.py",
    "batch_phys_quiz_d.py",
    "batch_phys_summary_a.py",
    "batch_phys_summary_b.py",
    "batch_phys_summary_c.py",
    "batch_phys_summary_d.py",
]

print("=== Syntax-checking batch files ===")
for fname in batch_files:
    with open(fname, "r", encoding="utf-8") as f:
        source = f.read()
    try:
        ast.parse(source)
        print(f"  OK  {fname}")
    except SyntaxError as e:
        print(f"  FAIL {fname}: {e}")
        sys.exit(1)

# ── 2. Redirect stdout to log file ────────────────────────────────
log_path = "_phys_result.txt"
log_file = open(log_path, "w", encoding="utf-8")
old_stdout = sys.stdout
sys.stdout = log_file

try:
    # ── 3. Import batches ──────────────────────────────────────────
    from batch_phys_answers   import answer_translations
    from batch_phys_quiz_a    import quiz_a_translations
    from batch_phys_quiz_b    import quiz_b_translations
    from batch_phys_quiz_c    import quiz_c_translations
    from batch_phys_quiz_d    import quiz_d_translations
    from batch_phys_summary_a import summary_a_translations
    from batch_phys_summary_b import summary_b_translations
    from batch_phys_summary_c import summary_c_translations
    from batch_phys_summary_d import summary_d_translations

    combined = {}
    for d in [
        answer_translations,
        quiz_a_translations, quiz_b_translations,
        quiz_c_translations, quiz_d_translations,
        summary_a_translations, summary_b_translations,
        summary_c_translations, summary_d_translations,
    ]:
        combined.update(d)

    print(f"Combined entries: {len(combined)}")

    # ── 4. Inject ──────────────────────────────────────────────────
    from inject_translations_util import inject_all
    inject_all(combined)

finally:
    sys.stdout = old_stdout
    log_file.close()
    # Print log to console for visibility
    with open(log_path, "r", encoding="utf-8") as f:
        result = f.read()
    print(result)
