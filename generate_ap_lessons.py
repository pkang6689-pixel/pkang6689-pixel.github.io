#!/usr/bin/env python3
"""
Generate AP lesson files with the format: LessonX.Y_(Practice/Quiz/Summary/Video).html
"""

import os
from pathlib import Path

# Define course structure: course_name -> (folder_name, units_dict)
# units_dict: unit_number -> number_of_lessons
courses = {
    "AP Biology": {
        "folder": "AP Biology",
        "units": {
            1: 6, 2: 5, 3: 4, 4: 5, 5: 4, 6: 5, 7: 5, 8: 6
        }
    },
    "AP Chemistry": {
        "folder": "AP Chemistry",
        "units": {
            1: 5, 2: 5, 3: 4, 4: 4, 5: 5, 6: 4, 7: 4, 8: 5, 9: 5
        }
    },
    "AP Calculus AB": {
        "folder": "AP Calculus AB",
        "units": {
            1: 11, 2: 9, 3: 6, 4: 7, 5: 12, 6: 12, 7: 7, 8: 12
        }
    },
    "AP Environmental Science": {
        "folder": "AP Environmental Science",
        "units": {
            1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5
        }
    },
    "AP Human Geography": {
        "folder": "AP Human Geography",
        "units": {
            1: 5, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6
        }
    },
    "AP Physics 2": {
        "folder": "AP Physics 2",
        "units": {
            9: 4, 10: 4, 11: 4, 12: 4, 13: 4, 14: 4, 15: 4
        }
    },
    "AP Physics C - Mechanics": {
        "folder": "AP Physics C - Mechanics",
        "units": {
            1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4
        }
    },
    "AP Statistics": {
        "folder": "AP Statistics",
        "units": {
            1: 5, 2: 5, 3: 6, 4: 5, 5: 5, 6: 5, 7: 5, 8: 4, 9: 5
        }
    }
}

# Lesson types to create for each lesson
lesson_types = ["Practice", "Quiz", "Summary", "Video"]

# Base path
base_path = Path(r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\APLessons")

def create_lesson_file(course_name, unit_num, lesson_num, lesson_type):
    """Create a single lesson file."""
    folder_path = base_path / courses[course_name]["folder"]
    folder_path.mkdir(parents=True, exist_ok=True)
    
    filename = f"Lesson{unit_num}.{lesson_num}_{lesson_type}.html"
    filepath = folder_path / filename
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lesson {unit_num}.{lesson_num} {lesson_type} - {course_name}</title>
</head>
<body>
    <h1>Lesson {unit_num}.{lesson_num} {lesson_type}</h1>
    <p>Coming soon...</p>
</body>
</html>"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return filepath

def main():
    """Generate all lesson files."""
    total_files = 0
    
    for course_name, course_data in courses.items():
        units = course_data["units"]
        print(f"\nGenerating files for {course_name}...")
        
        for unit_num, num_lessons in units.items():
            for lesson_num in range(1, num_lessons + 1):
                for lesson_type in lesson_types:
                    filepath = create_lesson_file(course_name, unit_num, lesson_num, lesson_type)
                    total_files += 1
                    if total_files % 20 == 0:
                        print(f"  Created {total_files} files...")
        
        print(f"  [OK] {course_name} complete")
    
    print(f"\n{'='*50}")
    print(f"[OK] Successfully created {total_files} lesson files!")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
