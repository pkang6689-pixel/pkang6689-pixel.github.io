#!/usr/bin/env python3
"""Fix Biology u8_l8.1 and u8_l8.2 — add 7 more questions each to reach 20."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "biology_lessons.json")

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

def add_questions(key, questions):
    lesson = data[key]
    existing = lesson.get("quiz_questions", [])
    start = len(existing) + 1
    for i, (qt, opts, exp) in enumerate(questions):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        existing.append({"question_number": start + i, "question_text": qt, "attempted": 2,
                         "data_i18n": None, "options": options, "explanation": exp})
    lesson["quiz_questions"] = existing

# u8_l8.1 — Check topic from first question
q1 = data["u8_l8.1"]["quiz_questions"][0]["question_text"]
print(f"u8_l8.1 topic hint: {q1[:80]}")
title1 = data["u8_l8.1"].get("title", "")
print(f"u8_l8.1 title: {title1}")

title2 = data["u8_l8.2"].get("title", "")
q2 = data["u8_l8.2"]["quiz_questions"][0]["question_text"]
print(f"u8_l8.2 title: {title2}, hint: {q2[:80]}")

# Based on Unit 8 of biology, these are likely ecology-related
# Let me check all existing questions to understand the topics better
for q in data["u8_l8.1"]["quiz_questions"]:
    print(f"  8.1 Q: {q['question_text'][:60]}")
print()
for q in data["u8_l8.2"]["quiz_questions"]:
    print(f"  8.2 Q: {q['question_text'][:60]}")
