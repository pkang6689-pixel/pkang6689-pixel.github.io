"""
Regenerate Geometry HTML files from Python data structures
This script takes the extracted lesson data and generates HTML files with full functionality
"""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from content_extraction_framework import (
    Lesson, HTMLRenderer, deserialize_lesson
)


def load_lessons_from_json(json_file: str) -> dict:
    """Load lessons from JSON file"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    lessons = {}
    for lesson_id, lesson_data in data.items():
        lessons[lesson_id] = deserialize_lesson(lesson_data)
    
    return lessons


def regenerate_html_files(lessons: dict, output_base_path: str):
    """Regenerate all HTML files from lesson data"""
    output_path = Path(output_base_path)
    
    for lesson_id, lesson in sorted(lessons.items()):
        # Create unit directory
        unit_dir = output_path / f"Unit{lesson.unit}"
        unit_dir.mkdir(parents=True, exist_ok=True)
        
        prefix = f"Lesson{lesson.lesson_number}"
        
        # Generate summary file
        if lesson.summary_sections:
            summary_html = HTMLRenderer.render_summary(lesson, prefix)
            summary_file = unit_dir / f"{prefix}_Summary.html"
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(summary_html)
            print(f"✓ Generated {prefix}_Summary.html")
        
        # Generate practice file
        if lesson.flashcards:
            practice_html = HTMLRenderer.render_practice(lesson, prefix)
            practice_file = unit_dir / f"{prefix}_Practice.html"
            with open(practice_file, 'w', encoding='utf-8') as f:
                f.write(practice_html)
            print(f"✓ Generated {prefix}_Practice.html")
        
        # Generate quiz file
        if lesson.quiz_questions:
            next_lesson_num = float(lesson.lesson_number) + 0.1
            next_lesson = f"Lesson{next_lesson_num:.1f}_Video"
            
            quiz_html = HTMLRenderer.render_quiz(lesson, lesson.course, next_lesson)
            quiz_file = unit_dir / f"{prefix}_Quiz.html"
            with open(quiz_file, 'w', encoding='utf-8') as f:
                f.write(quiz_html)
            print(f"✓ Generated {prefix}_Quiz.html")


def main():
    print("=" * 60)
    print("Geometry HTML Regeneration")
    print("=" * 60)
    
    content_data_dir = Path(r"c:\Users\Peter\pkang6689-pixel.github.io\content_data")
    json_file = content_data_dir / "geometry_lessons.json"
    
    if not json_file.exists():
        print(f"\n✗ JSON file not found: {json_file}")
        print("Please run: python extract_geometry_content.py first")
        return
    
    print(f"\nLoading lessons from {json_file}...")
    lessons = load_lessons_from_json(str(json_file))
    print(f"Loaded {len(lessons)} lessons")
    
    output_path = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\GeometryLessons"
    
    print(f"\nRegenerating HTML files in {output_path}...")
    regenerate_html_files(lessons, output_path)
    
    print("\n" + "=" * 60)
    print("HTML regeneration complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
