#!/usr/bin/env python3
"""
Extract summary and other content from Chemistry, Physics, Biology, Geometry
"""

import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser

class ContentExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_content = []
        self.in_content = False
        self.skip_tags = {'script', 'style', 'meta', 'link'}
        self.current_tag = None
    
    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags:
            self.current_tag = tag
        if tag == 'div':
            attrs_dict = dict(attrs)
            if 'lesson-notes' in attrs_dict.get('class', ''):
                self.in_content = True
    
    def handle_endtag(self, tag):
        if tag == 'div':
            self.in_content = False
    
    def handle_data(self, data):
        if self.in_content or self.current_tag in {'h2', 'h3', 'p', 'li', 'b'}:
            text = data.strip()
            if text and len(text) > 2:
                self.text_content.append(text)

def extract_from_file(file_path):
    """Extract text from HTML summary file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else ""
        
        # Extract content
        parser = ContentExtractor()
        parser.feed(content)
        
        strings = []
        if title:
            strings.append(title)
        strings.extend(parser.text_content)
        
        return strings
    except:
        return []

def extract_course(course_name, course_path):
    """Extract all content from a course"""
    all_strings = set()
    file_count = 0
    
    for root, dirs, files in os.walk(course_path):
        for file in sorted(files):
            if file.endswith('_Summary.html'):
                file_path = os.path.join(root, file)
                strings = extract_from_file(file_path)
                for s in strings:
                    if s and len(s.strip()) > 2:
                        all_strings.add(s.strip())
                file_count += 1
    
    return all_strings, file_count

def main():
    courses = {
        'Chemistry': '/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons/',
        'Physics': '/workspaces/ArisEdu/ArisEdu Project Folder/PhysicsLessons/',
        'Biology': '/workspaces/ArisEdu/ArisEdu Project Folder/BiologyLessons/',
        'Geometry': '/workspaces/ArisEdu/ArisEdu Project Folder/GeometryLessons/',
    }
    
    all_course_strings = {}
    total_unique = 0
    
    for course_name, course_path in courses.items():
        if Path(course_path).exists():
            print(f"Processing {course_name}...")
            strings, file_count = extract_course(course_name, course_path)
            all_course_strings[course_name] = list(strings)
            print(f"  Files: {file_count}")
            print(f"  Unique strings: {len(strings)}")
            total_unique += len(strings)
        else:
            print(f"Course {course_name} not found")
    
    print(f"\n=== TOTAL ===")
    print(f"Total unique strings: {total_unique}")
    
    # Save all strings
    with open('/workspaces/ArisEdu/other_courses_content.json', 'w', encoding='utf-8') as f:
        json.dump(all_course_strings, f, ensure_ascii=False, indent=2)
    
    # Flatten to single list for translation
    flat_strings = set()
    for strings_list in all_course_strings.values():
        flat_strings.update(strings_list)
    
    with open('/workspaces/ArisEdu/other_courses_strings_flat.json', 'w', encoding='utf-8') as f:
        json.dump(sorted(list(flat_strings)), f, ensure_ascii=False, indent=2)
    
    print(f"Saved to other_courses_content.json and other_courses_strings_flat.json")

if __name__ == "__main__":
    main()
