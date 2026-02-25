#!/usr/bin/env python3
"""
Generate comprehensive search index for all courses.
Includes lessons from all 6 courses: Algebra 1, Algebra 2, Geometry, Physics, Chemistry, Biology
"""

import os
import re
from pathlib import Path
import json
from bs4 import BeautifulSoup

# Base path to lessons
BASE_PATH = "ArisEdu Project Folder"

# Course configurations: (folder_name, course_display_name, unit_count)
COURSES = [
    ("Algebra1Lessons", "Algebra 1", 12),
    ("Algebra2Lessons", "Algebra 2", 9),
    ("GeometryLessons", "Geometry", 13),
    ("PhysicsLessons", "Physics", 11),
    ("ChemistryLessons", "Chemistry", 12),
    ("BiologyLessons", "Biology", 12),
]

search_index = []

def extract_title_from_html(file_path):
    """Extract lesson title from HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Try to extract from <title> tag first
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()
            # Clean up title
            title = title.replace(' - Summary', '').replace(' - Practice', '').replace(' - Quiz', '').replace(' - Video', '')
            return title
        
        # Fallback: try to extract from h2 with page-title class
        h2_match = re.search(r'<h2[^>]*class="[^"]*page-title[^"]*"[^>]*>(.*?)</h2>', content, re.IGNORECASE | re.DOTALL)
        if h2_match:
            title = h2_match.group(1).strip()
            title = re.sub(r'<[^>]+>', '', title)  # Remove HTML tags
            return title
        
        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def get_lesson_url(course_folder, unit, lesson):
    """Generate URL for a lesson."""
    return f"/ArisEdu Project Folder/{course_folder}/Unit{unit}/Lesson{unit}.{lesson}_Summary.html"

def scan_course(course_folder, course_name, unit_count):
    """Scan all lessons in a course."""
    items = []
    # Use absolute path from workspace root
    base_course_path = Path("/workspaces/ArisEdu") / BASE_PATH / course_folder
    
    # Iterate through units
    for unit in range(1, unit_count + 1):
        unit_path = base_course_path / f"Unit{unit}"
        
        if not unit_path.exists():
            continue
        
        # Find all lesson files (Summary files as primary source)
        # Handle both "Lesson1.1" and "Lesson 1.1" naming conventions
        lesson_files = sorted(unit_path.glob("Lesson*_Summary.html"))
        
        for lesson_file in lesson_files:
            # Extract lesson number from filename
            # Handles both "Lesson1.1_Summary.html" and "Lesson 1.1_Summary.html"
            match = re.search(r'Lesson\s*(\d+)\.(\d+)_Summary', lesson_file.name)
            if not match:
                continue
            
            unit_num = match.group(1)
            lesson_num = match.group(2)
            
            # Extract title
            title = extract_title_from_html(str(lesson_file))
            if not title:
                title = f"Lesson {unit_num}.{lesson_num}"
            
            # Generate URL (relative to workspace root)
            url = get_lesson_url(course_folder, unit_num, lesson_num)
            
            # Create subtitle
            subtitle = f"{course_name} - Unit {unit_num}, Lesson {lesson_num}"
            
            # Also add practice and quiz versions
            for lesson_type in ["Summary", "Practice", "Quiz"]:
                item = {
                    "title": title if lesson_type == "Summary" else f"{title} - {lesson_type}",
                    "subtitle": f"{subtitle} ({lesson_type})",
                    "url": url.replace("_Summary.html", f"_{lesson_type}.html"),
                    "content": f"{course_name} {subtitle} {lesson_type}"
                }
                items.append(item)
    
    return items

# Scan all courses
print("Generating comprehensive search index...")
for course_folder, course_name, unit_count in COURSES:
    print(f"Scanning {course_name}...")
    items = scan_course(course_folder, course_name, unit_count)
    search_index.extend(items)
    print(f"  Found {len(items)} items")

# Add course main pages (already in original, keeping them)
course_pages = [
    {
        "title": "ArisEdu Logo - ArisEdu",
        "subtitle": "index",
        "url": "/index.html",
        "content": "🔍 Search 🏠 Homepage 📚 Courses ⚙️ Settings 🔐 Login/Signup"
    },
    {
        "title": "High School Algebra 1",
        "subtitle": "algebra 1",
        "url": "/ArisEdu Project Folder/algebra1.html",
        "content": "Algebra 1 course page"
    },
    {
        "title": "High School Algebra 2",
        "subtitle": "algebra 2",
        "url": "/ArisEdu Project Folder/algebra2.html",
        "content": "Algebra 2 course page"
    },
    {
        "title": "High School Geometry",
        "subtitle": "geometry",
        "url": "/ArisEdu Project Folder/geometry.html",
        "content": "Geometry course page"
    },
    {
        "title": "High School Physics",
        "subtitle": "physics",
        "url": "/ArisEdu Project Folder/physics.html",
        "content": "Physics course page"
    },
    {
        "title": "High School Chemistry",
        "subtitle": "chemistry",
        "url": "/ArisEdu Project Folder/chem.html",
        "content": "Chemistry course page"
    },
    {
        "title": "High School Biology",
        "subtitle": "biology",
        "url": "/ArisEdu Project Folder/bio.html",
        "content": "Biology course page"
    },
    {
        "title": "Our Courses",
        "subtitle": "Courses",
        "url": "/ArisEdu Project Folder/Courses.html",
        "content": "ArisEdu offers Mathematics and Science courses"
    },
]

search_index = course_pages + search_index

# Write to file
output_file = Path(BASE_PATH).parent / "search_data.js"
print(f"\nWriting {len(search_index)} items to {output_file}...")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("const ARIS_EDU_SEARCH_INDEX = ")
    f.write(json.dumps(search_index, ensure_ascii=False, indent=2))
    f.write(";\n")

print(f"✓ Search index generated successfully!")
print(f"Total items: {len(search_index)}")
print(f"  - Course pages: 8")
print(f"  - Lessons: {len(search_index) - 8}")

# Print breakdown by course
for course_folder, course_name, _ in COURSES:
    course_items = [item for item in search_index if course_name in item.get('subtitle', '')]
    print(f"  - {course_name}: {len(course_items)} items")
