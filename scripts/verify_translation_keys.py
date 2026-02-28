#!/usr/bin/env python3
"""
Verify translation lookup compatibility.
Checks that HTML page titles can be found in translation dictionaries.
"""

import re
from pathlib import Path
from html.parser import HTMLParser

class PageTitleExtractor(HTMLParser):
    """Extract data-i18n values from HTML"""
    def __init__(self):
        super().__init__()
        self.titles = []
    
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if 'data-i18n' in attrs_dict:
            self.titles.append(attrs_dict['data-i18n'])

def extract_translation_keys(file_path):
    """Extract all translation keys from JS file"""
    content = file_path.read_text(encoding='utf-8')
    keys = set()
    
    # Match patterns like "key": "value",
    pattern = r'"([^"\\]*(?:\\.[^"\\]*)*)"\s*:\s*"'
    
    for match in re.finditer(pattern, content):
        key = match.group(1)
        # Unescape JSON strings
        key = key.replace('\\"', '"').replace('\\\\', '\\')
        keys.add(key)
    
    return keys

def extract_page_titles_from_html(html_path):
    """Extract translation keys from HTML page"""
    try:
        content = html_path.read_text(encoding='utf-8')
        parser = PageTitleExtractor()
        parser.feed(content)
        return parser.titles
    except:
        return []

def main():
    base_path = Path("ArisEdu Project Folder")
    trans_path = base_path / "scripts"
    
    # Load translation keys
    print("=" * 80)
    print("VERIFYING TRANSLATION LOOKUP COMPATIBILITY")
    print("=" * 80)
    
    trans_files = {
        "Chinese": trans_path / "global_translations.js",
        "Spanish": trans_path / "spanish_translations.js",
        "Hindi": trans_path / "hindi_translations.js",
    }
    
    all_trans_keys = {}
    for lang, file_path in trans_files.items():
        if file_path.exists():
            keys = extract_translation_keys(file_path)
            all_trans_keys[lang] = keys
            print(f"\n[{lang}] Loaded {len(keys):,} translation keys from {file_path.name}")
        else:
            print(f"\n[{lang}] File not found: {file_path}")
    
    # Sample HTML files to check
    sample_pages = [
        base_path / "Algebra1Lessons/Unit1/Lesson1.1_Summary.html",
        base_path / "Algebra1Lessons/Unit1/Lesson1.1_Practice.html",
        base_path / "PhysicsLessons/Unit5/Lesson 5.6_Summary.html",
        base_path / "BiologyLessons/Unit1/Lesson1.1_Summary.html",
    ]
    
    print("\n" + "=" * 80)
    print("CHECKING SAMPLE PAGES FOR TRANSLATION KEYS")
    print("=" * 80)
    
    total_checked = 0
    total_found = 0
    total_missing = 0
    
    for page_path in sample_pages:
        if not page_path.exists():
            continue
        
        print(f"\n[PAGE] {page_path.relative_to(base_path)}")
        
        titles = extract_page_titles_from_html(page_path)
        if not titles:
            print("  (no data-i18n attributes found)")
            continue
        
        for title in titles:
            total_checked += 1
            found_in_langs = []
            
            for lang, keys in all_trans_keys.items():
                if title in keys:
                    found_in_langs.append(lang)
                    total_found += 1
            
            if not found_in_langs:
                print(f"  ✗ NOT FOUND: {title}")
                total_missing += 1
            else:
                status = "✓" if len(found_in_langs) == len(all_trans_keys) else "⚠"
                langs_str = ", ".join(found_in_langs)
                print(f"  {status} {title[:50]}... ({langs_str})")
    
    print("\n" + "=" * 80)
    print(f"SUMMARY")
    print(f"  • Keys checked: {total_checked}")
    print(f"  • Found in translations: {total_found}")
    print(f"  • Missing keys: {total_missing}")
    
    if total_missing == 0:
        print(f"\n✓ All translation keys verified!")
    else:
        print(f"\n⚠ {total_missing} keys are missing from translations")
    print("=" * 80)

if __name__ == "__main__":
    main()
