import json
import os

def check_file(filepath):
    with open(filepath, encoding='utf-8') as fh:
        data = json.load(fh)
    giveaways = []
    for q in data['quiz_questions']:
        correct = None; wrongs = []
        for o in q['options']:
            if o['is_correct']: correct = o['text']
            else: wrongs.append(o['text'])
        if correct and wrongs:
            avg_wrong = sum(len(w) for w in wrongs) / len(wrongs)
            if avg_wrong > 0 and len(correct) >= 3 * avg_wrong:
                giveaways.append(q['question_number'])
    status = "OK" if len(giveaways) == 0 else "FAIL"
    print(f'[{status}] {os.path.basename(filepath)}: {len(giveaways)} giveaways -> {giveaways}')
    return len(giveaways)

# ALL 21 files
files = [
    'content_data/AstronomyLessons/Unit3/Lesson3.1_Quiz.json',
    'content_data/AstronomyLessons/Unit3/Lesson3.2_Quiz.json',
    'content_data/AstronomyLessons/Unit3/Lesson3.3_Quiz.json',
    'content_data/AstronomyLessons/Unit3/Lesson3.4_Quiz.json',
    'content_data/AstronomyLessons/Unit3/Lesson3.5_Quiz.json',
    'content_data/AstronomyLessons/Unit3/Lesson3.6_Quiz.json',
    'content_data/AstronomyLessons/Unit3/Lesson3.7_Quiz.json',
    'content_data/AstronomyLessons/Unit5/Lesson5.3_Quiz.json',
    'content_data/AstronomyLessons/Unit5/Lesson5.4_Quiz.json',
    'content_data/AstronomyLessons/Unit5/Lesson5.5_Quiz.json',
    'content_data/AstronomyLessons/Unit5/Lesson5.6_Quiz.json',
    'content_data/AstronomyLessons/Unit5/Lesson5.7_Quiz.json',
    'content_data/AstronomyLessons/Unit5/Lesson5.8_Quiz.json',
    'content_data/AstronomyLessons/Unit6/Lesson6.1_Quiz.json',
    'content_data/AstronomyLessons/Unit6/Lesson6.2_Quiz.json',
    'content_data/AstronomyLessons/Unit6/Lesson6.3_Quiz.json',
    'content_data/AstronomyLessons/Unit6/Lesson6.4_Quiz.json',
    'content_data/AstronomyLessons/Unit6/Lesson6.5_Quiz.json',
    'content_data/AstronomyLessons/Unit6/Lesson6.6_Quiz.json',
    'content_data/AstronomyLessons/Unit6/Lesson6.7_Quiz.json',
    'content_data/AstronomyLessons/Unit7/Lesson7.7_Quiz.json',
]

total = 0
for f in files:
    total += check_file(f)
print(f'\nTotal giveaways across all 21 files: {total}')
