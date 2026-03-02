import os
import shutil
from pathlib import Path

# Course structure with unit count and lesson count per unit
courses = {
    "AP Biology": {
        "folder": "AP Biology",
        "units": {1: 6, 2: 5, 3: 4, 4: 5, 5: 4, 6: 5, 7: 5, 8: 6}
    },
    "AP Chemistry": {
        "folder": "AP Chemistry",
        "units": {1: 5, 2: 5, 3: 4, 4: 4, 5: 5, 6: 4, 7: 4, 8: 5, 9: 5}
    },
    "AP Calculus AB": {
        "folder": "AP Calculus AB",
        "units": {1: 11, 2: 9, 3: 6, 4: 7, 5: 12, 6: 12, 7: 7, 8: 12}
    },
    "AP Environmental Science": {
        "folder": "AP Environmental Science",
        "units": {1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5}
    },
    "AP Human Geography": {
        "folder": "AP Human Geography",
        "units": {1: 5, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6}
    },
    "AP Physics 2": {
        "folder": "AP Physics 2",
        "units": {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4}
    },
    "AP Physics C - Mechanics": {
        "folder": "AP Physics C - Mechanics",
        "units": {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4}
    },
    "AP Statistics": {
        "folder": "AP Statistics",
        "units": {1: 5, 2: 5, 3: 6, 4: 5, 5: 5, 6: 5, 7: 5, 8: 4, 9: 5}
    }
}

base_path = Path(r"ArisEdu Project Folder\APLessons")

lesson_types = ["Practice", "Quiz", "Summary", "Video"]

print("Organizing AP lesson files by unit...\n")

for course_name, course_data in courses.items():
    course_folder = base_path / course_data["folder"]
    
    print(f"Processing {course_name}...")
    
    # Create unit folders
    units = course_data["units"]
    for unit_num in units.keys():
        unit_folder = course_folder / f"Unit {unit_num}"
        unit_folder.mkdir(parents=True, exist_ok=True)
        
        # Move lesson files for this unit
        lesson_count = units[unit_num]
        for lesson_num in range(1, lesson_count + 1):
            for lesson_type in lesson_types:
                filename = f"Lesson{unit_num}.{lesson_num}_{lesson_type}.html"
                src_file = course_folder / filename
                dst_file = unit_folder / filename
                
                if src_file.exists():
                    shutil.move(str(src_file), str(dst_file))
    
    print(f"  [OK] {course_name} organized into {len(units)} units\n")

print("=" * 50)
print("[OK] All lessons organized by unit!")
print("=" * 50)
