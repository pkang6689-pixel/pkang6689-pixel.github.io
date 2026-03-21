#!/usr/bin/env python3
"""Audit all Integrated Science lessons for quality metrics."""
import json, os, re

PATH = os.path.join("content_data", "integrated_science_lessons.json")
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

units = {}
for key in sorted(data.keys()):
    if not key.startswith("u"):
        continue
    unit = key.split("_")[0]
    if unit not in units:
        units[unit] = []
    units[unit].append(key)

total_q = 0
total_longest = 0
total_paren = 0
total_placeholder = 0

for unit in sorted(units.keys(), key=lambda x: int(x[1:])):
    lessons = units[unit]
    unit_q = 0
    unit_longest = 0
    unit_paren = 0
    unit_placeholder = 0
    for lkey in lessons:
        qs = data[lkey].get("quiz_questions", [])
        for q in qs:
            unit_q += 1
            opts = q.get("options", [])
            if not opts:
                continue
            lengths = [len(o["text"]) for o in opts]
            correct_idx = next((i for i, o in enumerate(opts) if o["is_correct"]), -1)
            if correct_idx >= 0 and lengths[correct_idx] == max(lengths):
                unit_longest += 1
            for o in opts:
                if re.search(r'\(.*?(correct|right|answer|true)\)', o["text"], re.I):
                    unit_paren += 1
                    break
            txt = q.get("question_text", "") + " ".join(o["text"] for o in opts) + q.get("explanation", "")
            if "placeholder" in txt.lower() or "lorem ipsum" in txt.lower():
                unit_placeholder += 1

    pct_longest = (unit_longest / unit_q * 100) if unit_q else 0
    print(f"{unit}: {len(lessons)} lessons, {unit_q} questions | "
          f"longest=correct: {unit_longest}/{unit_q} ({pct_longest:.0f}%) | "
          f"paren hints: {unit_paren} | placeholders: {unit_placeholder}")
    total_q += unit_q
    total_longest += unit_longest
    total_paren += unit_paren
    total_placeholder += unit_placeholder

print(f"\n{'='*70}")
print(f"TOTAL: {sum(len(v) for v in units.values())} lessons, {total_q} questions")
print(f"  Longest=correct:  {total_longest}/{total_q} ({total_longest/total_q*100:.0f}%)")
print(f"  Paren hints:      {total_paren}")
print(f"  Placeholders:     {total_placeholder}")
