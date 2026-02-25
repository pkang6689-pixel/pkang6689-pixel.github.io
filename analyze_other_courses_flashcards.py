#!/usr/bin/env python3
"""
Extract flashcard content from all courses and check what needs translation
"""

import os
import re
import json
from pathlib import Path

def extract_flashcards_from_html(file_path):
    """Extract flashcard questions and answers from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = r'window\.lessonFlashcards\s*=\s*\[(.*?)\]'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            return []
        
        flashcard_section = match.group(1)
        
        flashcards = []
        q_pattern = r'"question":\s*"([^"]*)"'
        a_pattern = r'"answer":\s*"([^"]*)"'
        
        questions = re.findall(q_pattern, flashcard_section)
        answers = re.findall(a_pattern, flashcard_section)
        
        for q, a in zip(questions, answers):
            flashcards.append({
                'question': q.replace('\\"', '"').replace('\\n', '\n'),
                'answer': a.replace('\\"', '"').replace('\\n', '\n')
            })
        
        return flashcards
    except Exception as e:
        return []

def extract_from_course(course_name, course_path):
    """Extract flashcards from all lessons in a course"""
    all_strings = set()
    flashcard_count = 0
    
    for root, dirs, files in os.walk(course_path):
        for file in sorted(files):
            if file.endswith('_Practice.html'):
                file_path = os.path.join(root, file)
                flashcards = extract_flashcards_from_html(file_path)
                
                for fc in flashcards:
                    if fc['question'].strip():
                        all_strings.add(fc['question'].strip())
                    if fc['answer'].strip():
                        all_strings.add(fc['answer'].strip())
                    flashcard_count += 1
    
    return all_strings, flashcard_count

def main():
    courses = {
        'Chemistry': '/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons/',
        'Physics': '/workspaces/ArisEdu/ArisEdu Project Folder/PhysicsLessons/',
        'Biology': '/workspaces/ArisEdu/ArisEdu Project Folder/BiologyLessons/',
        'Geometry': '/workspaces/ArisEdu/ArisEdu Project Folder/GeometryLessons/',
    }
    
    results = {}
    total_flashcards = 0
    
    for course_name, course_path in courses.items():
        if Path(course_path).exists():
            print(f"\nProcessing {course_name}...")
            strings, count = extract_from_course(course_name, course_path)
            results[course_name] = {
                'flashcard_count': count,
                'unique_strings': len(strings),
                'strings': sorted(list(strings))
            }
            print(f"  Flashcards: {count}")
            print(f"  Unique strings: {len(strings)}")
            total_flashcards += count
        else:
            print(f"Course {course_name} not found at {course_path}")
    
    print(f"\n=== SUMMARY ===")
    print(f"Total flashcards across all courses: {total_flashcards}")
    print(f"Total unique strings needing translation: {sum(r['unique_strings'] for r in results.values())}")
    
    # Save results
    with open('/workspaces/ArisEdu/other_courses_flashcard_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    return results

if __name__ == "__main__":
    main()
