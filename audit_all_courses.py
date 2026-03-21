#!/usr/bin/env python3
"""Audit ALL course JSON files for quality metrics."""
import json, os, re, glob

content_dir = "content_data"
files = sorted(glob.glob(os.path.join(content_dir, "*_lessons.json")))

for fpath in files:
    course = os.path.basename(fpath).replace("_lessons.json", "")
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_q = 0
    longest_correct = 0
    paren_hints = 0
    placeholders = 0
    lesson_count = 0

    for key in sorted(data.keys()):
        if not key.startswith("u"):
            continue
        lesson_count += 1
        qs = data[key].get("quiz_questions", [])
        for q in qs:
            total_q += 1
            opts = q.get("options", [])
            if not opts:
                continue
            lengths = [len(o["text"]) for o in opts]
            ci = next((i for i, o in enumerate(opts) if o["is_correct"]), -1)
            if ci >= 0 and lengths[ci] == max(lengths):
                longest_correct += 1
            for o in opts:
                if re.search(r'\(.*?(correct|right|answer|true)\)', o["text"], re.I):
                    paren_hints += 1
                    break
            txt = q.get("question_text", "") + " ".join(o["text"] for o in opts) + q.get("explanation", "")
            if "placeholder" in txt.lower() or "lorem ipsum" in txt.lower():
                placeholders += 1

    if total_q == 0:
        print(f"{course:30s} | {lesson_count:3d} lessons | 0 questions")
        continue
    pct = longest_correct / total_q * 100
    print(f"{course:30s} | {lesson_count:3d} lessons | {total_q:5d} qs | "
          f"longest=correct: {longest_correct}/{total_q} ({pct:4.0f}%) | "
          f"paren: {paren_hints} | placeholder: {placeholders}")
