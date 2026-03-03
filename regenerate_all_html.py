"""
Regenerate HTML files for all courses from extracted content
"""

import json
import subprocess
from pathlib import Path
import sys

COURSES = {
    'Chemistry': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\ChemistryLessons',
    'Algebra 1': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\Algebra1Lessons',
    'Algebra 2': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\Algebra2Lessons',
    'Biology': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\BiologyLessons',
    'Geometry': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\GeometryLessons',
    'Physics': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\PhysicsLessons',
}

OUTPUT_DIR = r'c:\Users\Peter\pkang6689-pixel.github.io\content_data'


def regenerate_course(course_name: str, output_path: str) -> bool:
    """Regenerate HTML for a single course"""
    print(f"\n{'='*60}")
    print(f"Regenerating {course_name}...")
    print(f"{'='*60}")
    
    filename = course_name.lower().replace(' ', '_')
    json_file = Path(OUTPUT_DIR) / f"{filename}_lessons.json"
    
    if not json_file.exists():
        print(f"[ERROR] JSON file not found: {json_file}")
        print(f"  Please run: python extract_all_courses.py")
        return False
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from content_extraction_framework import deserialize_lesson, HTMLRenderer
        
        # Load JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Regenerate HTML files
        Path(output_path).mkdir(parents=True, exist_ok=True)
        
        count = 0
        for lesson_id, lesson_data in data.items():
            try:
                lesson = deserialize_lesson(lesson_data)
                
                # Create unit directory
                unit_dir = Path(output_path) / f"Unit{lesson.unit}"
                unit_dir.mkdir(parents=True, exist_ok=True)
                
                prefix = f"Lesson{lesson.lesson_number}"
                
                # Generate summary file
                if lesson.summary_sections:
                    summary_html = HTMLRenderer.render_summary(lesson, prefix)
                    summary_file = unit_dir / f"{prefix}_Summary.html"
                    with open(summary_file, 'w', encoding='utf-8') as f:
                        f.write(summary_html)
                
                # Generate practice file
                if lesson.flashcards:
                    practice_html = HTMLRenderer.render_practice(lesson, prefix)
                    practice_file = unit_dir / f"{prefix}_Practice.html"
                    with open(practice_file, 'w', encoding='utf-8') as f:
                        f.write(practice_html)
                
                # Generate quiz file
                if lesson.quiz_questions:
                    next_lesson_num = float(lesson.lesson_number) + 0.1
                    next_lesson = f"Lesson{next_lesson_num:.1f}_Video"
                    
                    quiz_html = HTMLRenderer.render_quiz(lesson, lesson.course, next_lesson)
                    quiz_file = unit_dir / f"{prefix}_Quiz.html"
                    with open(quiz_file, 'w', encoding='utf-8') as f:
                        f.write(quiz_html)
                
                count += 1
            except Exception as e:
                print(f"  [ERROR] Error regenerating {lesson_id}: {e}")
        
        print(f"[OK] Regenerated {count} lessons for {course_name}")
        return True
    
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        return False


def main():
    print("\n" + "="*60)
    print("Master HTML Regeneration - All Courses")
    print("="*60)
    
    results = {}
    for course_name, output_path in COURSES.items():
        results[course_name] = regenerate_course(course_name, output_path)
    
    # Summary
    print("\n" + "="*60)
    print("REGENERATION SUMMARY")
    print("="*60)
    
    for course_name, success in results.items():
        status = "[OK]" if success else "[FAIL]"
        print(f"{course_name:20} {status}")
    
    total = len(results)
    successful = sum(1 for v in results.values() if v)
    
    print(f"\nTotal: {successful}/{total} courses regenerated successfully")
    
    if successful == total:
        print("\n[OK] All HTML files regenerated successfully!")


if __name__ == "__main__":
    main()
