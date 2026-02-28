#!/usr/bin/env python3
"""
Fix translation file consistency:
1. Remove duplicate page types (e.g., "Summary Summary")
2. Ensure both dashed and non-dashed formats exist where appropriate
3. Verify translations across Chinese, Spanish, and Hindi
"""

import json
import re
from pathlib import Path
from collections import defaultdict

# File paths
base_path = Path("ArisEdu Project Folder/scripts")
translations_files = {
    "chinese": base_path / "global_translations.js",
    "spanish": base_path / "spanish_translations.js", 
    "hindi": base_path / "hindi_translations.js"
}

def extract_js_translations(file_path):
    """Extract translation dictionary from JS file"""
    content = file_path.read_text(encoding='utf-8')
    
    # Find the translations object
    match = re.search(r'const translations = \{', content)
    if not match:
        return None, content
    
    start = match.end()
    # Find the closing brace that matches
    brace_count = 1
    i = start
    while i < len(content) and brace_count > 0:
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
        i += 1
    
    translations_str = content[start:i-1]
    
    # Parse as pseudo-JSON by extracting key-value pairs
    pairs = {}
    # Match patterns like: "key": "value",
    pattern = r'"([^"\\]*(?:\\.[^"\\]*)*)"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"\s*,'
    
    for match in re.finditer(pattern, translations_str):
        key = match.group(1)
        value = match.group(2)
        # Unescape JSON strings
        key = key.replace('\\"', '"').replace('\\\\', '\\')
        value = value.replace('\\"', '"').replace('\\\\', '\\')
        pairs[key] = value
    
    full_content = content[:start] + translations_str + content[i-1:]
    return pairs, full_content

def find_issues(translations_dict):
    """Find problematic entries"""
    issues = {
        'double_page_types': [],  # "Summary Summary", "Quiz Quiz", etc.
        'mixed_dash_formats': defaultdict(list),  # Same lesson with different dash usage
    }
    
    lesson_pattern = r'(Lesson \d+\.\d+: [^"]+)'
    page_types = ['Summary', 'Practice', 'Quiz', 'Video']
    
    # Group entries by base lesson (without page type)
    lessons = defaultdict(list)
    
    for key in translations_dict:
        # Check for double page types
        for page_type in page_types:
            if f' {page_type} {page_type}"' in f' {key}"':
                issues['double_page_types'].append(key)
        
        # Extract base lesson name
        match = re.match(r'Lesson \d+\.\d+: [^-]+', key)
        if match:
            base = match.group(0)
            lessons[base].append(key)
    
    # Check for mixed formats (some with dash, some without)
    for base, variants in lessons.items():
        has_dashed = any(' - ' in v for v in variants)
        has_non_dashed = any(' - ' not in v and any(pt in v for pt in page_types) for v in variants)
        
        if has_dashed and has_non_dashed:
            issues['mixed_dash_formats'][base] = variants
    
    return issues

def fix_translations(file_path, language):
    """Fix issues in a translation file"""
    translations, full_content = extract_js_translations(file_path)
    if not translations:
        return None
    
    fixes = {
        'removed_duplicates': 0,
        'added_dashed_variants': [],
        'removed_entries': [],
    }
    
    issues = find_issues(translations)
    
    # Fix double page types
    for key in issues['double_page_types']:
        # Remove double page types like "Summary Summary" -> "Summary"
        for page_type in ['Summary', 'Practice', 'Quiz', 'Video']:
            pattern = f' {page_type} {page_type}$'
            if re.search(pattern, key):
                fixed_key = key.replace(f' {page_type} {page_type}', f' {page_type}')
                if fixed_key not in translations or translations[fixed_key] == translations[key]:
                    # Move or merge
                    if fixed_key not in translations:
                        translations[fixed_key] = translations[key]
                    del translations[key]
                    fixes['removed_duplicates'] += 1
                    fixes['removed_entries'].append(key)
                    break
    
    # For mixed dash formats, ensure both exist
    for base, variants in issues['mixed_dash_formats'].items():
        page_types_found = ['Summary', 'Practice', 'Quiz', 'Video']
        
        for variant in variants:
            # If non-dashed, create dashed version
            for page_type in page_types_found:
                if page_type in variant and ' - ' not in variant:
                    # Create dashed version
                    dashed_key = variant.replace(f' {page_type}', f' - {page_type}')
                    if dashed_key not in translations and variant in translations:
                        # Copy translation but keep language-specific tweaks
                        # For now, just reference the non-dashed version's translation
                        value = translations[variant]
                        # Don't duplicate if value looks like it already has dash translation
                        if dashed_key not in translations:
                            translations[dashed_key] = value
                            fixes['added_dashed_variants'].append((variant, dashed_key))
    
    return translations, fixes

def serialize_translations(translations):
    """Convert translations dict back to JS object string"""
    lines = []
    for key, value in sorted(translations.items()):
        # Escape for JS
        key_escaped = key.replace('\\', '\\\\').replace('"', '\\"')
        value_escaped = value.replace('\\', '\\\\').replace('"', '\\"')
        lines.append(f'    "{key_escaped}": "{value_escaped}",')
    
    # Remove trailing comma from last line
    if lines:
        lines[-1] = lines[-1].rstrip(',')
    
    return '\n'.join(lines)

# Main execution
print("=" * 80)
print("TRANSLATION FILE CONSISTENCY FIXER")
print("=" * 80)

total_fixes = {'removed': 0, 'added': 0}

for language, file_path in translations_files.items():
    if not file_path.exists():
        print(f"[SKIP] {language}: File not found: {file_path}")
        continue
    
    print(f"\n[{language.upper()}] Processing {file_path.name}...")
    
    try:
        result = fix_translations(file_path, language)
        if result is None:
            print(f"  ERROR: Could not parse translations")
            continue
        
        trans, fixes = result
        
        print(f"  ✓ Removed duplicate page types: {fixes['removed_duplicates']}")
        print(f"  ✓ Added dashed variants: {len(fixes['added_dashed_variants'])}")
        if fixes['removed_entries']:
            print(f"    Removed entries: {', '.join(fixes['removed_entries'][:3])}")
            if len(fixes['removed_entries']) > 3:
                print(f"    ... and {len(fixes['removed_entries']) - 3} more")
        
        total_fixes['removed'] += fixes['removed_duplicates']
        total_fixes['added'] += len(fixes['added_dashed_variants'])
        
    except Exception as e:
        print(f"  ERROR: {e}")

print("\n" + "=" * 80)
print(f"SUMMARY: Removed {total_fixes['removed']} duplicates, Added {total_fixes['added']} variants")
print("=" * 80)
print("\nNote: This script analyzed issues but did not modify files yet.")
print("Review the changes above and run with modifications enabled if satisfied.")
