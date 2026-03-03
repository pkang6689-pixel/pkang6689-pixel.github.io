"""
Generic Course Content Extraction Script
Extracts any course content and stores in Python data format

Usage:
    python extract_course_content.py Chemistry c:\path\to\ChemistryLessons
    python extract_course_content.py "Algebra 1" c:\path\to\Algebra1Lessons
"""

import json
from pathlib import Path
from typing import List, Dict
import re
import sys
from argparse import ArgumentParser

sys.path.insert(0, str(Path(__file__).parent))
from content_extraction_framework import (
    Lesson, HTMLExtractor, serialize_lesson
)


class GenericCourseExtractor:
    """Extract any course content"""
    
    def __init__(self, course_name: str, base_path: str):
        self.course_name = course_name
        self.base_path = Path(base_path)
        self.lessons: Dict[str, Lesson] = {}
    
    def extract_lesson(self, unit: int, lesson_num: str) -> Lesson:
        """Extract a single lesson from HTML files"""
        prefix = f"Lesson{lesson_num}"
        prefix_with_space = f"Lesson {lesson_num}"
        
        # Construct file paths - try multiple naming conventions
        summary_file = self._find_file([
            self.base_path / f"Unit{unit}" / f"{prefix_with_space}_Summary.html",
            self.base_path / f"Unit{unit}" / f"{prefix}_Summary.html",
            self.base_path / f"Unit {unit}" / f"{prefix_with_space}_Summary.html",
            self.base_path / f"Unit {unit}" / f"{prefix}_Summary.html",
        ])
        
        practice_file = self._find_file([
            self.base_path / f"Unit{unit}" / f"{prefix_with_space}_Practice.html",
            self.base_path / f"Unit{unit}" / f"{prefix}_Practice.html",
            self.base_path / f"Unit {unit}" / f"{prefix_with_space}_Practice.html",
            self.base_path / f"Unit {unit}" / f"{prefix}_Practice.html",
        ])
        
        quiz_file = self._find_file([
            self.base_path / f"Unit{unit}" / f"{prefix_with_space}_Quiz.html",
            self.base_path / f"Unit{unit}" / f"{prefix}_Quiz.html",
            self.base_path / f"Unit {unit}" / f"{prefix_with_space}_Quiz.html",
            self.base_path / f"Unit {unit}" / f"{prefix}_Quiz.html",
        ])
        
        lesson = Lesson(
            unit=unit,
            lesson_number=lesson_num,
            title="",
            course=self.course_name
        )
        
        # Extract from summary
        if summary_file and summary_file.exists():
            with open(summary_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lesson.summary_sections = HTMLExtractor.extract_summary_notes(content)
                
                # Extract title
                title_match = re.search(
                    r'<title>\s*Lesson\s*' + re.escape(lesson_num) + r':\s*(.*?)\s*-\s*Summary\s*</title>',
                    content,
                    re.IGNORECASE
                )
                if title_match:
                    lesson.title = title_match.group(1)
        
        # Extract from practice
        if practice_file and practice_file.exists():
            with open(practice_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lesson.flashcards = HTMLExtractor.extract_flashcards(content)
        
        # Extract from quiz
        if quiz_file and quiz_file.exists():
            with open(quiz_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lesson.quiz_questions = HTMLExtractor.extract_quiz_questions(content)
        
        return lesson
    
    @staticmethod
    def _find_file(paths: List[Path]) -> Path:
        """Find first existing file from list of paths"""
        for path in paths:
            if path.exists():
                return path
        return None
    
    def extract_all_lessons(self) -> Dict[str, Lesson]:
        """Extract all available lessons from the file system"""
        unit_dirs = sorted([d for d in self.base_path.iterdir() if d.is_dir() and (d.name.startswith('Unit') or d.name.startswith('Unit '))])
        
        for unit_dir in unit_dirs:
            # Extract unit number
            unit_match = re.search(r'Unit\s*(\d+)', unit_dir.name)
            if not unit_match:
                continue
            
            unit_num = int(unit_match.group(1))
            
            # Find all lessons in this unit (handles both "Lesson1.1" and "Lesson 1.1" formats)
            summary_files = list(unit_dir.glob('*Summary.html'))
            
            for summary_file in sorted(summary_files):
                match = re.search(r'Lesson\s*([\d.]+)_Summary', summary_file.name)
                if match:
                    lesson_num = match.group(1)
                    try:
                        lesson = self.extract_lesson(unit_num, lesson_num)
                        self.lessons[f"u{unit_num}_l{lesson_num}"] = lesson
                        print(f"[OK] Extracted Unit {unit_num}, Lesson {lesson_num}: {lesson.title[:50]}")
                    except Exception as e:
                        print(f"[ERROR] Error extracting Unit {unit_num}, Lesson {lesson_num}: {e}")
        
        return self.lessons
    
    def save_to_json(self, output_dir: str):
        """Save lessons as JSON"""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filename = self.course_name.lower().replace(' ', '_')
        output_file = output_dir / f"{filename}_lessons.json"
        
        data = {}
        for lesson_id, lesson in self.lessons.items():
            data[lesson_id] = serialize_lesson(lesson)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return output_file
    
    def save_summary(self, output_dir: str):
        """Save extraction summary"""
        output_dir = Path(output_dir)
        filename = self.course_name.lower().replace(' ', '_')
        summary_file = output_dir / f"{filename}_extraction_summary.txt"
        
        summary = f"""Extraction Summary for {self.course_name}
{'='*60}

Total Lessons Extracted: {len(self.lessons)}

Lessons by Unit:
"""
        
        by_unit = {}
        for lesson_id, lesson in sorted(self.lessons.items()):
            unit = lesson.unit
            if unit not in by_unit:
                by_unit[unit] = []
            by_unit[unit].append(lesson)
        
        for unit in sorted(by_unit.keys()):
            summary += f"\nUnit {unit}: {len(by_unit[unit])} lessons\n"
            for lesson in by_unit[unit]:
                summary += f"  - Lesson {lesson.lesson_number}: {lesson.title}\n"
                summary += f"    • Summary sections: {len(lesson.summary_sections)}\n"
                summary += f"    • Flashcards: {len(lesson.flashcards)}\n"
                summary += f"    • Quiz questions: {len(lesson.quiz_questions)}\n"
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        return summary_file


def main():
    parser = ArgumentParser(description='Extract course content from HTML files')
    parser.add_argument('course', help='Course name (e.g., "Chemistry", "Algebra 1")')
    parser.add_argument('base_path', help='Path to course lessons folder')
    parser.add_argument('--output-dir', default=r"c:\Users\Peter\pkang6689-pixel.github.io\content_data",
                        help='Output directory for JSON files')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print(f"{args.course} Course Content Extraction")
    print("=" * 60)
    
    if not Path(args.base_path).exists():
        print(f"\n[ERROR] Path not found: {args.base_path}")
        return
    
    extractor = GenericCourseExtractor(args.course, args.base_path)
    
    print(f"\nExtracting all {args.course} lessons...")
    lessons = extractor.extract_all_lessons()
    
    print(f"\nTotal lessons extracted: {len(lessons)}")
    
    # Save outputs
    json_file = extractor.save_to_json(args.output_dir)
    summary_file = extractor.save_summary(args.output_dir)
    
    print(f"\n[OK] JSON saved to: {json_file}")
    print(f"[OK] Summary saved to: {summary_file}")
    
    print("\n" + "=" * 60)
    print("Extraction complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
