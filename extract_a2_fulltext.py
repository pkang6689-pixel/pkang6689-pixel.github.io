#!/usr/bin/env python3
"""Extract full element textContent from all Algebra 2 HTML files using BeautifulSoup."""
import os
import re
import json
from bs4 import BeautifulSoup
from collections import defaultdict

BASE = "ArisEdu Project Folder/Algebra2Lessons"
CAPTURE_TAGS = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'dt', 'dd',
                'label', 'td', 'th', 'button', 'a', 'span', 'strong', 'em', 'b']

def extract_text_from_file(filepath):
    """Extract full textContent for all relevant elements."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove scripts and styles
    for tag in soup.find_all(['script', 'style', 'noscript']):
        tag.decompose()
    
    results = []
    seen = set()
    
    for tag in soup.find_all(CAPTURE_TAGS):
        text = tag.get_text(separator='', strip=False)
        text = re.sub(r'\s+', ' ', text).strip()
        if text and len(text) > 1 and text not in seen:
            seen.add(text)
            results.append((tag.name, text))
    
    return results

def load_existing_translations(js_path):
    """Load existing translation keys from global_translations.js."""
    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    keys = set()
    # Match both "key": and 'key': patterns
    for m in re.finditer(r'(?:^|\n)\s*["\'](.+?)["\']\s*:', content):
        key = m.group(1)
        # Unescape
        key = key.replace("\\'", "'").replace('\\"', '"')
        keys.add(key)
    
    return keys

def classify_file(filename):
    """Classify file type."""
    fn = filename.lower()
    if '_summary' in fn:
        return 'Summary'
    elif '_quiz' in fn:
        return 'Quiz'
    elif '_practice' in fn:
        return 'Practice'
    elif '_video' in fn:
        return 'Video'
    elif '_test' in fn or 'test' in fn:
        return 'Test'
    return 'Other'

def main():
    js_path = "ArisEdu Project Folder/scripts/global_translations.js"
    existing = load_existing_translations(js_path)
    print(f"Existing translation keys: {len(existing)}")
    
    # Collect all strings by file type
    by_type = defaultdict(set)
    all_strings = {}  # text -> (tag, filetype, filename)
    
    for unit_dir in sorted(os.listdir(BASE)):
        unit_path = os.path.join(BASE, unit_dir)
        if not os.path.isdir(unit_path):
            continue
        for fname in sorted(os.listdir(unit_path)):
            if not fname.endswith('.html'):
                continue
            fpath = os.path.join(unit_path, fname)
            ftype = classify_file(fname)
            results = extract_text_from_file(fpath)
            for tag_name, text in results:
                by_type[ftype].add(text)
                if text not in all_strings:
                    all_strings[text] = (tag_name, ftype, fname)
    
    # Analyze
    total_unique = set()
    for ftype in sorted(by_type.keys()):
        strings = by_type[ftype]
        total_unique.update(strings)
        missing = [s for s in strings if s not in existing]
        print(f"\n{ftype}: {len(strings)} unique strings, {len(missing)} missing translations")
        # Show first 5 missing
        for s in sorted(missing, key=len, reverse=True)[:5]:
            print(f"  [{len(s)}] {s[:120]}...")
    
    all_missing = {s for s in total_unique if s not in existing}
    print(f"\n=== TOTALS ===")
    print(f"Total unique strings: {len(total_unique)}")
    print(f"Already translated: {len(total_unique) - len(all_missing)}")
    print(f"Missing translations: {len(all_missing)}")
    
    # Check which missing strings contain only math/numbers (don't need translation)
    math_only = set()
    needs_translation = set()
    for s in all_missing:
        # Strip math notation characters
        stripped = re.sub(r'[0-9a-zA-Z\s\.\,\;\:\!\?\(\)\[\]\{\}\+\-\*\/\=\<\>\|\^\_\~\#\@\$\%\&\\\'\"₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹√∞π°≤≥≠±∑∫∂→←↑↓⟨⟩·×÷∈∉⊂⊃∪∩∅∀∃∧∨¬⇒⇔]', '', s)
        if not stripped.strip():
            math_only.add(s)
        else:
            needs_translation.add(s)
    
    print(f"\nMath/notation only (no translation needed): {math_only}")
    print(f"Needs actual translation: {len(needs_translation)}")
    
    # Save missing strings to JSON for translation
    missing_by_type = defaultdict(list)
    for s in sorted(needs_translation, key=len, reverse=True):
        tag_name, ftype, fname = all_strings[s]
        missing_by_type[ftype].append({'text': s, 'tag': tag_name, 'file': fname})
    
    with open('algebra2_fulltext_missing.json', 'w', encoding='utf-8') as f:
        json.dump(missing_by_type, f, ensure_ascii=False, indent=2)
    
    print(f"\nSaved to algebra2_fulltext_missing.json")
    
    # Also save just Summary missing for priority work
    summary_missing = [item['text'] for item in missing_by_type.get('Summary', [])]
    print(f"\nSummary files missing: {len(summary_missing)}")
    for s in summary_missing[:10]:
        print(f"  [{len(s)}] {s[:140]}")

if __name__ == '__main__':
    main()
