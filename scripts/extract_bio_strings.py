#!/usr/bin/env python3
"""
Extract ALL text content from biology lessons for translation.
This extracts paragraphs, list items, headings - everything translatable.
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser

BASE_PATH = Path(r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\BiologyLessons")
OUTPUT_FILE = Path(r"c:\Users\Peter\pkang6689-pixel.github.io\scripts\bio_strings_to_translate.txt")

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.current_text = ""
        self.skip_tags = {'script', 'style', 'meta', 'link', 'title'}
        self.in_skip = 0
        
    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.in_skip += 1
            
    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.in_skip = max(0, self.in_skip - 1)
        # Save accumulated text when we hit certain tags
        if tag in {'p', 'li', 'h1', 'h2', 'h3', 'h4', 'b', 'label', 'span', 'div', 'a', 'button'}:
            if self.current_text.strip():
                self.texts.append(self.current_text.strip())
                self.current_text = ""
                
    def handle_data(self, data):
        if self.in_skip == 0:
            self.current_text += data

def extract_text_from_html(filepath):
    """Extract all visible text from an HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parser = TextExtractor()
        parser.feed(content)
        
        # Also get remaining text
        if parser.current_text.strip():
            parser.texts.append(parser.current_text.strip())
            
        return parser.texts
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

def extract_flashcard_strings(filepath):
    """Extract flashcard questions and answers."""
    strings = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = r'\{\s*question:\s*["\']([^"\']+)["\'],\s*answer:\s*["\']([^"\']+)["\']\s*\}'
        for match in re.finditer(pattern, content):
            strings.append(match.group(1))
            strings.append(match.group(2))
    except:
        pass
    return strings

def clean_text(text):
    """Clean and normalize text."""
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Skip if too short or just numbers/symbols
    if len(text) < 3:
        return None
    if text.isdigit():
        return None
    # Skip SVG/path data
    if text.startswith('M') and any(c in text for c in 'CcLlZz'):
        return None
    # Skip URLs
    if text.startswith('http') or '.html' in text or '.js' in text:
        return None
    # Skip CSS-like content
    if ':' in text and (';' in text or '{' in text):
        return None
    return text

def main():
    all_strings = set()
    
    # Process all HTML files
    for unit_num in range(1, 13):
        unit_folder = BASE_PATH / f"Unit{unit_num}"
        if not unit_folder.exists():
            continue
            
        print(f"Processing Unit {unit_num}...")
        
        for f in unit_folder.glob("*.html"):
            # Extract visible text
            texts = extract_text_from_html(f)
            for text in texts:
                cleaned = clean_text(text)
                if cleaned:
                    all_strings.add(cleaned)
            
            # Extract flashcard strings
            if "_Practice.html" in f.name or "_Test.html" in f.name:
                fc_strings = extract_flashcard_strings(f)
                for s in fc_strings:
                    cleaned = clean_text(s)
                    if cleaned:
                        all_strings.add(cleaned)
    
    # Sort and save
    sorted_strings = sorted(all_strings, key=lambda x: (len(x), x))
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for s in sorted_strings:
            f.write(s + '\n')
    
    print(f"\nExtracted {len(sorted_strings)} unique strings")
    print(f"Saved to {OUTPUT_FILE}")
    
    # Show some samples
    print("\nSample strings (first 30):")
    for s in sorted_strings[:30]:
        print(f"  - {s[:80]}{'...' if len(s) > 80 else ''}")

if __name__ == "__main__":
    main()
