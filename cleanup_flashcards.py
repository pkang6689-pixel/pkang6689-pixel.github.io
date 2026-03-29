#!/usr/bin/env python3
"""
Remove low-quality/trivial flashcards from all practice files.
Keeps only educational flashcards that promote understanding.
"""

import json
from pathlib import Path
from collections import defaultdict

def is_low_quality(card):
    """Return True if card should be removed."""

    # Handle term/definition schema
    if "term" in card and "definition" in card:
        term = card.get("term", "").strip()
        defn = card.get("definition", "").strip()

        if not term or not defn:
            return True

        # Definition is just a formula with no explanation
        if len(defn.split()) <= 2 and any(sym in defn for sym in ['=', '+', '−', '×', '÷', '^']):
            return True

        # Definition too vague or trivial
        if len(defn.split()) < 3:
            return True

        return False

    # Handle question/answer schema
    elif "question" in card and "answer" in card:
        q = card.get("question", "").strip()
        a = card.get("answer", "").strip()

        if not q or not a:
            return True

        # Pure formula memorization: "Func(value) = ?" with just a number/formula answer
        if ("=" in q and q.strip().endswith("?")) and len(a.split()) == 1:
            # Examples: "cos(π/3) = ?", "sin(π/6) = ?", etc.
            return True

        # Pure value lookup: "Period of X?" -> "number", "Amplitude?" -> "number"
        if q.strip().endswith("?") and len(a.split()) <= 1 and not a.startswith("When"):
            # But keep questions like "Can you...", "Is it...", "Does..."
            if any(start in q for start in ["Can ", "Is ", "Does ", "Should ", "Would "]):
                return False
            # And keep longer questions
            if len(q.split()) > 6:
                return False
            # One word answer to simple question is usually trivial
            return True

        # Trivial definition: "What is X?" with one-word answer
        if q.lower().startswith("what is") and len(a.split()) == 1:
            return True

        return False

    return False

def main():
    """Remove low-quality flashcards from all practice files."""
    content_data_path = Path("c:/Users/Peter/pkang6689-pixel.github.io/content_data")

    if not content_data_path.exists():
        print(f"Error: {content_data_path} does not exist")
        return

    practice_files = list(content_data_path.glob("**/Lesson*_Practice.json"))

    stats = {
        "files_processed": 0,
        "files_modified": 0,
        "total_cards_before": 0,
        "total_cards_removed": 0,
        "cards_removed_by_file": []
    }

    for practice_file in practice_files:
        try:
            with open(practice_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            flashcards = data.get("flashcards", [])
            original_count = len(flashcards)

            # Filter out low-quality cards
            filtered_cards = [card for card in flashcards if not is_low_quality(card)]
            removed_count = original_count - len(filtered_cards)

            stats["total_cards_before"] += original_count
            stats["total_cards_removed"] += removed_count
            stats["files_processed"] += 1

            # Write back if any were removed
            if removed_count > 0:
                data["flashcards"] = filtered_cards
                with open(practice_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                stats["files_modified"] += 1
                stats["cards_removed_by_file"].append((practice_file.name, removed_count, original_count))

        except Exception as e:
            print(f"Error processing {practice_file}: {e}")

    # Print summary
    print("=== FLASHCARD CLEANUP COMPLETE ===\n")
    print(f"Files processed: {stats['files_processed']}")
    print(f"Files modified: {stats['files_modified']}")
    print(f"Total cards before: {stats['total_cards_before']}")
    print(f"Total cards removed: {stats['total_cards_removed']}")
    print(f"Retention rate: {100 * (stats['total_cards_before'] - stats['total_cards_removed']) / stats['total_cards_before']:.1f}%\n")

    if stats["cards_removed_by_file"]:
        print("Files with removals (showing first 20):")
        for filename, removed, total in sorted(stats["cards_removed_by_file"], key=lambda x: -x[1])[:20]:
            print(f"  {filename}: removed {removed}/{total}")

if __name__ == "__main__":
    main()
