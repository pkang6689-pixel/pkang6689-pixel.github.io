#!/usr/bin/env python3
"""
Identify and report on low-quality flashcards in practice files.
Classifies flashcards by quality and provides a summary.
"""

import json
from pathlib import Path
from collections import defaultdict

def evaluate_flashcard(card):
    """
    Evaluate a flashcard and return quality assessment.
    Returns: (is_low_quality, reason)
    """

    # Handle term/definition schema
    if "term" in card and "definition" in card:
        term = card.get("term", "").strip()
        defn = card.get("definition", "").strip()

        if not term or not defn:
            return True, "empty"

        # Definition is just a formula with no explanation
        if len(defn.split()) <= 2 and any(sym in defn for sym in ['=', '+', '−', '×', '÷', '^']):
            return True, "formula_only"

        # Definition too vague or trivial
        if len(defn.split()) < 3:
            return True, "too_short"

        return False, "good"

    # Handle question/answer schema
    elif "question" in card and "answer" in card:
        q = card.get("question", "").strip()
        a = card.get("answer", "").strip()

        if not q or not a:
            return True, "empty"

        # Trivial one-word answer to definition question
        if q.lower().startswith("what is") and len(a.split()) == 1 and q.count("?") == 1:
            return True, "trivial_definition"

        # Single word/number answers that don't add value
        if len(a.split()) == 1 and len(a) < 5 and not any(sym in a for sym in ['°', 'π', '√', '^']):
            return True, "trivial_answer"

        return False, "good"

    return False, "unknown_schema"

def main():
    """Scan all practice files and report on quality."""
    content_data_path = Path("c:/Users/Peter/pkang6689-pixel.github.io/content_data")

    if not content_data_path.exists():
        print(f"Error: {content_data_path} does not exist")
        return

    practice_files = list(content_data_path.glob("**/Lesson*_Practice.json"))

    quality_stats = defaultdict(int)
    files_with_issues = []
    total_cards = 0
    low_quality_cards = 0

    for practice_file in practice_files:
        try:
            with open(practice_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            flashcards = data.get("flashcards", [])
            file_low_quality = []

            for card in flashcards:
                total_cards += 1
                is_low_quality, reason = evaluate_flashcard(card)
                quality_stats[reason] += 1

                if is_low_quality:
                    low_quality_cards += 1
                    file_low_quality.append((card, reason))

            if file_low_quality:
                files_with_issues.append((practice_file, file_low_quality))

        except Exception as e:
            print(f"Error processing {practice_file}: {e}")

    # Print summary
    print("=== FLASHCARD QUALITY ASSESSMENT ===\n")
    print(f"Total practice files: {len(practice_files)}")
    print(f"Total flashcards: {total_cards}")
    print(f"Low-quality flashcards: {low_quality_cards} ({100*low_quality_cards/total_cards:.1f}%)\n")

    print("Quality breakdown:")
    for reason, count in sorted(quality_stats.items(), key=lambda x: -x[1]):
        pct = 100 * count / total_cards
        print(f"  {reason}: {count} ({pct:.1f}%)")

    print(f"\n\nFiles with quality issues: {len(files_with_issues)}")
    print("\nTop files with low-quality flashcards:")

    files_by_issue_count = sorted(files_with_issues, key=lambda x: -len(x[1]))[:20]

    for filepath, issues in files_by_issue_count:
        print(f"\n{filepath.name} ({len(issues)} issues)")
        for card, reason in issues[:3]:
            if "term" in card:
                term = card.get("term", "")[:50]
                defn = card.get("definition", "")[:60]
                print(f"  [{reason}] {term}: {defn}...")
            else:
                q = card.get("question", "")[:50]
                a = card.get("answer", "")[:40]
                print(f"  [{reason}] Q: {q} -> A: {a}")

if __name__ == "__main__":
    main()
