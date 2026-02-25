#!/usr/bin/env python3
"""
Extract all untranslated summaries from Algebra 2 lesson files
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser
import json

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_content = []
        self.in_lesson_notes = False
        self.skip_tags = {'script', 'style', 'meta', 'link'}
        self.current_tag = None
    
    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags:
            self.current_tag = tag
        if tag == 'div':
            attrs_dict = dict(attrs)
            if 'lesson-notes' in attrs_dict.get('class', ''):
                self.in_lesson_notes = True
    
    def handle_endtag(self, tag):
        if tag == 'div':
            self.in_lesson_notes = False
    
    def handle_data(self, data):
        if self.in_lesson_notes or self.current_tag in {'h2', 'h3', 'p', 'li'}:
            text = data.strip()
            if text and len(text) > 2:
                self.text_content.append(text)

def extract_from_summary(file_path):
    """Extract text content from summary HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract lesson title
        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else ""
        
        # Extract lesson notes
        parser = TextExtractor()
        parser.feed(content)
        
        strings = []
        
        # Add title
        if title:
            strings.append(title)
        
        # Add extracted text
        strings.extend(parser.text_content)
        
        return strings
    except Exception as e:
        print(f"Error extracting from {file_path}: {e}")
        return []

def main():
    algebra2_dir = '/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons/'
    all_strings = set()
    file_count = 0
    
    # Walk through all Summary files
    for root, dirs, files in os.walk(algebra2_dir):
        for file in sorted(files):
            if file.endswith('_Summary.html'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file}")
                
                strings = extract_from_summary(file_path)
                for s in strings:
                    if s and len(s.strip()) > 2:
                        all_strings.add(s.strip())
                
                file_count += 1
    
    print(f"\nExtracted {len(all_strings)} unique strings from {file_count} summary files")
    
    # Save to file
    with open('/workspaces/ArisEdu/algebra2_summary_strings.json', 'w', encoding='utf-8') as f:
        json.dump(sorted(list(all_strings)), f, ensure_ascii=False, indent=2)
    
    return all_strings

if __name__ == "__main__":
    strings = main()
