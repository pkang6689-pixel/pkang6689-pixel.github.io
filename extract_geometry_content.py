"""
Geometry Course Content Extraction Script
Extracts all lessons from GeometryLessons and stores in Python data format
"""

import json
from pathlib import Path
from typing import List, Dict
import re
import sys

# Add parent directory to path to import framework
sys.path.insert(0, str(Path(__file__).parent))
from content_extraction_framework import (
    Lesson, HTMLExtractor, HTMLRenderer, serialize_lesson, deserialize_lesson
)


class GeometryExtractor:
    """Extract all Geometry course content"""
    
    # Defines the structure of all Geometry lessons
    GEOMETRY_STRUCTURE = {
        1: {  # Unit 1
            'lessons': [
                {'number': '1.1', 'title': 'Introduction to Geometry'},
                {'number': '1.2', 'title': 'Points, Lines, and Planes'},
                {'number': '1.3', 'title': 'Measuring Distances'},
                {'number': '1.4', 'title': 'Measuring Angles'},
                # Add more lessons...
            ]
        },
        # Add more units...
        6: {  # Unit 6
            'lessons': [
                {'number': '6.1', 'title': 'Angles of Polygons'},
                # Add more lessons...
            ]
        }
    }
    
    def __init__(self, base_path: str = None):
        if base_path is None:
            base_path = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\GeometryLessons"
        self.base_path = Path(base_path)
        self.lessons: Dict[str, Lesson] = {}
    
    def extract_lesson(self, unit: int, lesson_num: str) -> Lesson:
        """Extract a single lesson from HTML files"""
        lesson_id = f"u{unit}_l{lesson_num}"
        prefix = f"Lesson{lesson_num}"
        
        # Construct file paths
        summary_file = self.base_path / f"Unit{unit}" / f"{prefix}_Summary.html"
        practice_file = self.base_path / f"Unit{unit}" / f"{prefix}_Practice.html"
        quiz_file = self.base_path / f"Unit{unit}" / f"{prefix}_Quiz.html"
        
        lesson = Lesson(
            unit=unit,
            lesson_number=lesson_num,
            title="",  # Will be extracted from files
            course="Geometry"
        )
        
        # Extract from summary
        if summary_file.exists():
            with open(summary_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lesson.summary_sections = HTMLExtractor.extract_summary_notes(content)
                
                # Extract title
                title_match = re.search(r'<title>Lesson ' + re.escape(lesson_num) + r': (.*?) - Summary</title>', content)
                if title_match:
                    lesson.title = title_match.group(1)
        
        # Extract from practice
        if practice_file.exists():
            with open(practice_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lesson.flashcards = HTMLExtractor.extract_flashcards(content)
        
        # Extract from quiz
        if quiz_file.exists():
            with open(quiz_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lesson.quiz_questions = HTMLExtractor.extract_quiz_questions(content)
        
        return lesson
    
    def extract_all_lessons(self) -> Dict[str, Lesson]:
        """Extract all available lessons from the file system"""
        # Dynamically find all lesson directories
        unit_dirs = sorted([d for d in self.base_path.iterdir() if d.is_dir() and d.name.startswith('Unit')])
        
        for unit_dir in unit_dirs:
            unit_num = int(unit_dir.name.replace('Unit', ''))
            
            # Find all lessons in this unit
            summary_files = list(unit_dir.glob('*_Summary.html'))
            
            for summary_file in sorted(summary_files):
                # Extract lesson number from filename like "Lesson6.1_Summary.html"
                match = re.search(r'Lesson([\d.]+)_Summary', summary_file.name)
                if match:
                    lesson_num = match.group(1)
                    try:
                        lesson = self.extract_lesson(unit_num, lesson_num)
                        self.lessons[f"u{unit_num}_l{lesson_num}"] = lesson
                        print(f"✓ Extracted Unit {unit_num}, Lesson {lesson_num}: {lesson.title}")
                    except Exception as e:
                        print(f"✗ Error extracting Unit {unit_num}, Lesson {lesson_num}: {e}")
        
        return self.lessons
    
    def save_to_python_script(self, output_file: str):
        """Save all lessons as a Python data structure"""
        script_content = '''"""
Geometry Course Content - Auto-generated from HTML extraction
This file contains all lesson content in Python data structures for easy modification and translation.

To regenerate HTML files, use: python regenerate_geometry_html.py
To translate, modify the TRANSLATIONS dictionary below and run regenerate.
To add new content, edit the lesson data directly.
"""

# All lessons organized by Unit and Lesson Number
GEOMETRY_LESSONS = {
'''
        
        # Organize by unit
        by_unit = {}
        for lesson_id, lesson in sorted(self.lessons.items()):
            unit = lesson.unit
            if unit not in by_unit:
                by_unit[unit] = []
            by_unit[unit].append((lesson_id, lesson))
        
        # Generate Python code
        for unit in sorted(by_unit.keys()):
            script_content += f"\n    # ===== UNIT {unit} =====\n"
            for lesson_id, lesson in by_unit[unit]:
                script_content += f"\n    '{lesson_id}': {{\n"
                script_content += f"        'unit': {lesson.unit},\n"
                script_content += f"        'lesson_number': '{lesson.lesson_number}',\n"
                script_content += f"        'title': '{lesson.title.replace(chr(39), chr(92) + chr(39))}',\n"
                script_content += f"        'course': 'Geometry',\n\n"
                
                # Summary sections
                script_content += "        'summary_sections': [\n"
                for section in lesson.summary_sections:
                    title = section.title.replace('"', '\\"')
                    content = section.content_html[:100].replace('"', '\\"') + "..."
                    script_content += f"            {{\n"
                    script_content += f'                "title": "{title}",\n'
                    script_content += f'                "content_html": """{section.content_html}\"\"\",\n'
                    script_content += f"            }},\n"
                script_content += "        ],\n\n"
                
                # Flashcards
                script_content += "        'flashcards': [\n"
                for card in lesson.flashcards:
                    q = card.question.replace('"', '\\"')
                    a = card.answer.replace('"', '\\"')
                    script_content += f'            {{"question": "{q}", "answer": "{a}"}},\n'
                script_content += "        ],\n\n"
                
                # Quiz questions
                script_content += "        'quiz_questions': [\n"
                for q in lesson.quiz_questions:
                    script_content += f"            {{\n"
                    script_content += f'                "number": {q.question_number},\n'
                    script_content += f'                "text": "{q.question_text.replace(chr(34), chr(92) + chr(34))}",\n'
                    script_content += f'                "options": [\n'
                    for opt in q.options:
                        opt_text = opt.text.replace('"', '\\"')
                        script_content += f'                    {{"text": "{opt_text}", "correct": {str(opt.is_correct).lower()}}},\n'
                    script_content += f'                ],\n'
                    script_content += f"            }},\n"
                script_content += "        ],\n"
                script_content += "    },\n"
        
        script_content += "\n}\n\n"
        
        # Add translations section
        script_content += """
# Translation dictionaries for multiple languages
# Add translations for non-English languages here
TRANSLATIONS = {
    'spanish': {
        # Example: 'Angles of Polygons': 'Ángulos de Polígonos',
    },
    'hindi': {
        # Example: 'Angles of Polygons': 'बहुभुजों के कोण',
    },
    'chinese': {
        # Example: 'Angles of Polygons': '多边形的角度',
    }
}

# Note: To modify content:
# 1. Edit the lesson dictionaries above (change text, add questions, etc)
# 2. Run: python regenerate_geometry_html.py
# 3. This will regenerate all HTML files with your changes

# Note: For translations:
# 1. Add translations to the TRANSLATIONS dictionary above
# 2. They will automatically apply when HTML is regenerated
# 3. The i18n system will use these for multi-language support
"""
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(script_content)
        
        print(f"\n✓ Saved to {output_file}")
    
    def save_to_json(self, output_file: str):
        """Save all lessons as JSON for easy editing"""
        data = {}
        for lesson_id, lesson in self.lessons.items():
            data[lesson_id] = serialize_lesson(lesson)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Saved JSON to {output_file}")


def main():
    print("=" * 60)
    print("Geometry Course Content Extraction")
    print("=" * 60)
    
    extractor = GeometryExtractor()
    
    # Extract all lessons
    print("\nExtracting all Geometry lessons...")
    lessons = extractor.extract_all_lessons()
    
    print(f"\nTotal lessons extracted: {len(lessons)}")
    
    # Save in multiple formats
    output_dir = Path(r"c:\Users\Peter\pkang6689-pixel.github.io\content_data")
    output_dir.mkdir(exist_ok=True)
    
    # Save as Python script
    extractor.save_to_python_script(str(output_dir / "geometry_lessons.py"))
    
    # Save as JSON
    extractor.save_to_json(str(output_dir / "geometry_lessons.json"))
    
    print("\n" + "=" * 60)
    print("Extraction complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Modify content in geometry_lessons.py as needed")
    print("2. Add translations to the TRANSLATIONS dictionary")
    print("3. Run: python regenerate_geometry_html.py")
    print("   This will regenerate HTML files with your changes")


if __name__ == "__main__":
    main()
