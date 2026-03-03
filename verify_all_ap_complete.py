"""Comprehensive verification of ALL AP course content"""
import json
from pathlib import Path
from collections import defaultdict

content_data = Path(__file__).parent / 'content_data'

courses = [
    'ap_biology_lessons.json',
    'ap_chemistry_lessons.json',
    'ap_calculus_ab_lessons.json',
    'ap_statistics_lessons.json',
    'ap_environmental_science_lessons.json',
    'ap_human_geography_lessons.json',
    'ap_physics_2_lessons.json',
    'ap_physics_c_-_mechanics_lessons.json',
]

print("COMPREHENSIVE AP CONTENT VERIFICATION")
print("="*80)

total_lessons = 0
complete_lessons = 0
incomplete_lessons = 0

for course_file in courses:
    json_file = content_data / course_file
    if not json_file.exists():
        continue
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    course_name = course_file.replace('_lessons.json', '').replace('_', ' ').title()
    
    # Count lessons
    complete = 0
    incomplete = 0
    total = len(data)
    
    for lesson_id, lesson_data in data.items():
        summaries = len(lesson_data.get('summary_sections', []))
        flashcards = len(lesson_data.get('flashcards', []))
        quizzes = len(lesson_data.get('quiz_questions', []))
        
        if summaries >= 4 and flashcards >= 10 and quizzes >= 7:
            complete += 1
        else:
            incomplete += 1
    
    total_lessons += total
    complete_lessons += complete
    incomplete_lessons += incomplete
    
    status = "COMPLETE" if incomplete == 0 else f"INCOMPLETE (missing {incomplete})"
    print(f"\n{course_name}")
    print(f"  Total lessons: {total:3} | Complete: {complete:3} | {status}")

print("\n" + "="*80)
print(f"OVERALL SUMMARY")
print("="*80)
print(f"Total lessons across all AP courses: {total_lessons}")
print(f"Lessons with complete content:     {complete_lessons}")
print(f"Lessons still incomplete:          {incomplete_lessons}")

if incomplete_lessons == 0:
    print(f"\n[SUCCESS] All {total_lessons} AP lessons are now complete!")
else:
    print(f"\n[WARNING] {incomplete_lessons} lessons still need content")
