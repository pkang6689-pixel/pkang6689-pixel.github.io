"""Test AP lessons functionality"""
import json
from pathlib import Path

ap_courses_path = Path(__file__).parent / 'content_data' / 'AP_Courses'

print("TESTING AP LESSONS CONTENT")
print("=" * 80)

# Test each course
for course_file in sorted(ap_courses_path.glob('ap_*.json')):
    print(f"\n[LOADING] {course_file.name}")
    
    try:
        with open(course_file, 'r', encoding='utf-8') as f:
            lessons = json.load(f)
        
        print(f"  [OK] JSON loaded successfully: {len(lessons)} lessons")
        
        # Check first lesson
        first_lesson_id = list(lessons.keys())[0]
        first_lesson = lessons[first_lesson_id]
        
        # Verify structure
        required_fields = ['title', 'summary_sections', 'flashcards', 'quiz_questions']
        missing_fields = [field for field in required_fields if field not in first_lesson]
        
        if missing_fields:
            print(f"  [ERROR] Missing fields: {missing_fields}")
        else:
            print(f"  [OK] Required fields present")
            print(f"       - Title: {first_lesson.get('title', 'N/A')[:50]}")
            print(f"       - Summary sections: {len(first_lesson.get('summary_sections', []))}")
            print(f"       - Flashcards: {len(first_lesson.get('flashcards', []))}")
            print(f"       - Quiz questions: {len(first_lesson.get('quiz_questions', []))}")
        
        # Check all lessons have complete content
        incomplete = []
        for lesson_id, lesson in lessons.items():
            summaries = len(lesson.get('summary_sections', []))
            flashcards = len(lesson.get('flashcards', []))
            quizzes = len(lesson.get('quiz_questions', []))
            
            if summaries < 4 or flashcards < 10 or quizzes < 7:
                incomplete.append(lesson_id)
        
        if incomplete:
            print(f"  [WARNING] {len(incomplete)} incomplete lessons found")
        else:
            print(f"  [OK] All {len(lessons)} lessons have complete content")
            
    except json.JSONDecodeError as e:
        print(f"  [ERROR] JSON decode error: {e}")
    except Exception as e:
        print(f"  [ERROR] {type(e).__name__}: {e}")

print("\n" + "=" * 80)
print("CONTENT VERIFICATION COMPLETE")
