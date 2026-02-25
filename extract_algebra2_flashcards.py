#!/usr/bin/env python3
"""
Extract all flashcard questions and answers from Algebra 2 Practice HTML files
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
        
        # Look for window.lessonFlashcards = [...]
        pattern = r'window\.lessonFlashcards\s*=\s*\[(.*?)\]'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            return []
        
        flashcard_section = match.group(1)
        
        # Extract all question/answer pairs
        flashcards = []
        # Look for "question": "..." and "answer": "..."
        q_pattern = r'"question":\s*"([^"]*)"'
        a_pattern = r'"answer":\s*"([^"]*)"'
        
        questions = re.findall(q_pattern, flashcard_section)
        answers = re.findall(a_pattern, flashcard_section)
        
        # Zip them together (assuming they come in order)
        for q, a in zip(questions, answers):
            flashcards.append({
                'question': q.replace('\\"', '"').replace('\\n', '\n'),
                'answer': a.replace('\\"', '"').replace('\\n', '\n')
            })
        
        return flashcards
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []

def main():
    algebra2_dir = '/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons/'
    all_strings = set()
    file_count = 0
    total_flashcards = 0
    
    # Walk through all Practice files
    for root, dirs, files in os.walk(algebra2_dir):
        for file in sorted(files):
            if file.endswith('_Practice.html'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file}")
                
                flashcards = extract_flashcards_from_html(file_path)
                
                for fc in flashcards:
                    # Add both question and answer to the set
                    if fc['question'].strip():
                        all_strings.add(fc['question'].strip())
                    if fc['answer'].strip():
                        all_strings.add(fc['answer'].strip())
                    total_flashcards += 1
                
                file_count += 1
    
    print(f"\nExtracted {total_flashcards} flashcards from {file_count} practice files")
    print(f"Unique strings: {len(all_strings)}")
    
    # Save to file
    with open('/workspaces/ArisEdu/algebra2_flashcard_strings.json', 'w', encoding='utf-8') as f:
        json.dump(sorted(list(all_strings)), f, ensure_ascii=False, indent=2)
    
    return all_strings

if __name__ == "__main__":
    strings = main()
