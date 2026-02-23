#!/usr/bin/env python3
"""Extract all lesson-notes content from GeometryLessons HTML files with translations."""
import os
import re
import json
from pathlib import Path
from collections import defaultdict

def load_global_translations():
    """Load translations from global_translations.js"""
    translations = {}
    try:
        global_js_path = Path('ArisEdu Project Folder/scripts/global_translations.js')
        with open(global_js_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract the translations object using regex
        # Pattern: match everything between "const translations = {" and "};"
        js_pattern = r'const translations = \{(.*?)\s*\};'
        match = re.search(js_pattern, content, re.DOTALL)
        
        if match:
            translations_str = match.group(1)
            
            # Parse each key-value pair
            # Pattern handles quoted strings and escaped quotes
            pair_pattern = r'"((?:[^"\\]|\\.)*)"\s*:\s*"((?:[^"\\]|\\.)*)"\s*(?:,|$)'
            
            for key_match in re.finditer(pair_pattern, translations_str):
                key = key_match.group(1)
                value = key_match.group(2)
                
                # Unescape JSON strings
                key = json.loads('"' + key + '"')
                value = json.loads('"' + value + '"')
                
                translations[key] = value
        
        print(f"✓ Loaded {len(translations)} translations from global_translations.js\n")
        return translations
    except Exception as e:
        print(f"⚠ Error loading translations: {e}\n")
        return {}

# Load translations first
global_translations = load_global_translations()

# Find all HTML files in GeometryLessons
geometry_lessons_path = Path('ArisEdu Project Folder/GeometryLessons')

if not geometry_lessons_path.exists():
    print(f"Error: {geometry_lessons_path} not found")
    exit(1)

html_files = sorted(geometry_lessons_path.rglob('*.html'))
print(f"Found {len(html_files)} HTML files")

all_notes = []
by_unit = defaultdict(lambda: defaultdict(list))

# Pattern to extract content within div class="lesson-notes"
# This handles nested HTML and multiple divs per file
pattern = r'<div[^>]*class="lesson-notes"[^>]*>(.*?)</div>'

# Pattern to extract content within div class="lesson-notes"
# This handles nested HTML and multiple divs per file
pattern = r'<div[^>]*class="lesson-notes"[^>]*>(.*?)</div>'

extracted_count = 0
files_with_notes = 0

def extract_plain_text(html):
    """Extract plain text from HTML, preserving line breaks and structure."""
    # Remove script and style elements
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    
    # Convert br tags to newlines
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    
    # Remove HTML tags but keep content
    text = re.sub(r'<[^>]+>', '', text)
    
    # Decode HTML entities
    text = text.replace('&quot;', '"')
    text = text.replace('&amp;', '&')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&nbsp;', ' ')
    text = text.replace('\u00a0', ' ')
    
    # Clean up whitespace
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join([line for line in lines if line])
    
    return text

def find_translations_in_text(text, trans_dict):
    """Find segments of text that have translations."""
    matches = []
    # Sort by length (longest first) to avoid partial matches
    sorted_keys = sorted(trans_dict.keys(), key=len, reverse=True)
    
    for key in sorted_keys:
        if key.lower() in text.lower():
            # Case-insensitive search
            pattern = re.compile(re.escape(key), re.IGNORECASE)
            if pattern.search(text):
                matches.append((key, trans_dict[key]))
    
    return matches

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all lesson-notes divs
        matches = re.findall(pattern, content, re.DOTALL)
        
        if matches:
            files_with_notes += 1
            
            # Extract unit and lesson info from filename
            relative_path = html_file.relative_to(geometry_lessons_path)
            parts = relative_path.parts
            unit = parts[0] if len(parts) > 0 else 'Unknown'
            filename = parts[1] if len(parts) > 1 else 'Unknown'
            
            for match_idx, match in enumerate(matches):
                extracted_count += 1
                
                # Clean up the HTML content
                cleaned_html = match.strip()
                plain_text = extract_plain_text(cleaned_html)
                
                # Find translations for this text
                found_translations = find_translations_in_text(plain_text, global_translations)
                
                # Store with metadata
                entry = {
                    'unit': unit,
                    'file': filename,
                    'html_content': cleaned_html,
                    'plain_text': plain_text,
                    'translations_found': len(found_translations),
                    'translation_pairs': found_translations,
                    'file_path': str(relative_path)
                }
                
                all_notes.append(entry)
                by_unit[unit][filename].append(entry)
    
    except Exception as e:
        print(f"Error processing {html_file}: {e}")

print(f"✓ Extracted {extracted_count} lesson-notes divs from {files_with_notes} files\n")

# Save to JSON for machine processing
import json

with open('lesson_notes_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_notes, f, ensure_ascii=False, indent=2)

print(f"✓ Saved to lesson_notes_extracted.json")

# Save to formatted text file for human review
with open('lesson_notes_extracted.txt', 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("EXTRACTED LESSON NOTES FROM GEOMETRY LESSONS WITH TRANSLATIONS\n")
    f.write("=" * 80 + "\n\n")
    
    for idx, entry in enumerate(all_notes, 1):
        f.write(f"\n[{idx}] {entry['file_path']}\n")
        f.write("-" * 80 + "\n")
        
        f.write("PLAIN TEXT:\n")
        f.write(entry['plain_text'])
        f.write("\n\n")
        
        if entry['translation_pairs']:
            f.write(f"TRANSLATIONS FOUND ({entry['translations_found']}):\n")
            for original, translated in entry['translation_pairs']:
                f.write(f"\n  EN: {original}\n")
                f.write(f"  ZH: {translated}\n")
            f.write("\n")
        else:
            f.write("(No translations found for this section)\n\n")

print(f"✓ Saved to lesson_notes_extracted.txt")

# Print summary by unit
print("\nSummary by unit:")
total_translations_found = 0
for unit in sorted(by_unit.keys()):
    file_count = len(by_unit[unit])
    note_count = sum(len(entries) for entries in by_unit[unit].values())
    trans_count = sum(
        entry.get('translations_found', 0) 
        for entries in by_unit[unit].values() 
        for entry in (entries if isinstance(entries, list) else [entries])
    )
    total_translations_found += trans_count
    print(f"  {unit}: {file_count} files, {note_count} lesson-notes, {trans_count} translations")

print("\n" + "=" * 80)
print(f"TOTAL: {extracted_count} lesson-notes sections extracted")
print(f"TOTAL TRANSLATIONS FOUND: {total_translations_found}")
print("=" * 80)
