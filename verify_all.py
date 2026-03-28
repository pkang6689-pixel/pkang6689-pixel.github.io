import json
import os

base = "C:/Users/Peter/pkang6689-pixel.github.io/content_data/EnvironmentalScienceLessons"
files = [
    "Unit1/Lesson1.2_Quiz.json", "Unit1/Lesson1.3_Quiz.json", "Unit1/Lesson1.4_Quiz.json",
    "Unit1/Lesson1.5_Quiz.json", "Unit1/Lesson1.6_Quiz.json", "Unit1/Lesson1.7_Quiz.json",
    "Unit2/Lesson2.1_Quiz.json", "Unit2/Lesson2.2_Quiz.json", "Unit2/Lesson2.3_Quiz.json",
    "Unit2/Lesson2.4_Quiz.json", "Unit2/Lesson2.5_Quiz.json",
    "Unit4/Lesson4.3_Quiz.json", "Unit4/Lesson4.4_Quiz.json", "Unit4/Lesson4.5_Quiz.json",
    "Unit4/Lesson4.6_Quiz.json", "Unit4/Lesson4.7_Quiz.json",
    "Unit5/Lesson5.1_Quiz.json", "Unit5/Lesson5.2_Quiz.json",
    "Unit9/Lesson9.5_Quiz.json",
    "Unit10/Lesson10.3_Quiz.json", "Unit10/Lesson10.4_Quiz.json",
    "Unit10/Lesson10.5_Quiz.json", "Unit10/Lesson10.6_Quiz.json"
]

total_giveaways = 0
for lesson in files:
    path = f"{base}/{lesson}"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    giveaways = []
    for q in data['quiz_questions']:
        correct_len = 0
        wrong_lens = []
        for opt in q['options']:
            if opt['is_correct']:
                correct_len = len(opt['text'])
            else:
                wrong_lens.append(len(opt['text']))
        avg_wrong = sum(wrong_lens) / len(wrong_lens) if wrong_lens else 1
        ratio = correct_len / avg_wrong
        if ratio >= 3.0:
            giveaways.append(f"Q{q['question_number']}({ratio:.1f}x)")
    if giveaways:
        print(f"REMAINING: {lesson}: {len(giveaways)} giveaways: {', '.join(giveaways)}")
        total_giveaways += len(giveaways)
    else:
        print(f"OK: {lesson}: 0 giveaways")

print(f"\nTotal remaining giveaways across all 23 files: {total_giveaways}")
