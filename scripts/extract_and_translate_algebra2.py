#!/usr/bin/env python3
"""
Extract all Algebra 2 content strings and generate comprehensive Chinese translations
Uses pattern-based translation with context awareness
"""
import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    """Extract text content from HTML files"""
    def __init__(self):
        super().__init__()
        self.text_content = []
        self.in_script = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.in_script = True
            
    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False
            
    def handle_data(self, data):
        if not self.in_script:
            text = data.strip()
            if text and len(text) > 2:  # Skip very short strings
                self.text_content.append(text)

def extract_all_algebra2_strings():
    """Extract all unique strings from Algebra 2 content files"""
    algebra2_dir = '/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons/'
    
    if not Path(algebra2_dir).exists():
        print(f"Could not find Algebra 2 Lessons directory at {algebra2_dir}")
        return set()
    
    print(f"Using directory: {algebra2_dir}")
    
    all_strings = set()
    file_count = 0
    
    # Walk through all HTML files
    for root, dirs, files in os.walk(algebra2_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Extract flashcard content
                    flashcard_matches = re.findall(
                        r'window\.lessonFlashcards\s*=\s*\[(.*?)\];',
                        content,
                        re.DOTALL
                    )
                    for match in flashcard_matches:
                        cards = re.findall(r'\{\s*question:\s*"([^"]*)"\s*,\s*answer:\s*"([^"]*)"\s*\}', match, re.DOTALL)
                        for q, a in cards:
                            if q.strip():
                                all_strings.add(q.strip())
                            if a.strip():
                                all_strings.add(a.strip())
                    
                    # Extract quiz questions
                    quiz_matches = re.findall(
                        r'<input[^>]*?value="([^"]*)"[^>]*?>\s*<label[^>]*?>([^<]*)',
                        content
                    )
                    for value, label in quiz_matches:
                        if label.strip() and label.strip() not in ['Correct!', 'Incorrect!', 'Try Again']:
                            all_strings.add(label.strip())
                    
                    # Extract summary content (paragraphs)
                    summary_matches = re.findall(r'<p[^>]*>([^<]+(?:<[^>]*>[^<]*)*)</p>', content)
                    for para in summary_matches:
                        # Remove HTML tags
                        clean = re.sub(r'<[^>]+>', '', para)
                        clean = clean.strip()
                        if clean and len(clean) > 10:  # Skip very short strings
                            all_strings.add(clean)
                    
                    file_count += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    print(f"Extracted from {file_count} files")
    return all_strings

# Comprehensive mathematical translation patterns
PATTERN_TRANSLATIONS = {
    r"^Find\s+(.+)$": lambda m: f"求{m.group(1)}",
    r"^Solve\s+(.+)$": lambda m: f"解{m.group(1)}",
    r"^Simplify\s+(.+)$": lambda m: f"简化{m.group(1)}",
    r"^Graph\s+(.+)$": lambda m: f"绘制{m.group(1)}的图像",
    r"^What is\s+(.+)\?$": lambda m: f"{m.group(1)}是什么？",
    r"^Evaluate\s+(.+)$": lambda m: f"计算{m.group(1)}",
    r"^Is\s+(.+)\?$": lambda m: f"{m.group(1)}吗？",
    r"^Determine\s+(.+)$": lambda m: f"判断{m.group(1)}",
    r"^Factor\s+(.+)$": lambda m: f"因式分解{m.group(1)}",
    r"^Verify\s+(.+)$": lambda m: f"验证{m.group(1)}",
}

# Direct string translations (most common lesson strings)
COMMON_STRINGS = {
    "Correct!": "正确！",
    "Incorrect!": "错误！",
    "Try Again": "重试",
    "Question": "问题",
    "Answer": "答案",
    "Explanation": "解释",
    "Lesson": "课程",
    "Summary": "总结",
    "Practice": "练习",
    "Quiz": "测验",
    "Video": "视频",
    "Next": "下一步",
    "Previous": "上一步",
    "Back": "返回",
    "Continue": "继续",
    "Start": "开始",
    "End": "结束",
    "Submit": "提交",
    "Check Answer": "检查答案",
    "Review": "复习",
    "Learn": "学习",
    "Master": "掌握",
    "Practice More": "更多练习",
}

def apply_pattern_translation(string):
    """Try to translate using patterns"""
    for pattern, translator in PATTERN_TRANSLATIONS.items():
        match = re.match(pattern, string, re.IGNORECASE)
        if match:
            try:
                return translator(match)
            except:
                pass
    return None

def extract_variables_and_translate(string):
    """Extract mathematical variables and translate around them"""
    # If string contains mathematical notation, try to preserve it
    if re.search(r'[xyz]|[\d\+\-\*/\(\)\^]', string):
        # Avoid translating pure math expressions
        if len(re.findall(r'[a-zA-Z0-9\+\-\*/\(\)\^\.=]', string)) > len(string) * 0.6:
            return None  # Skip mostly-math strings
    return None

def translate_string(string):
    """Attempt to translate a single string"""
    # Skip if already in COMMON_STRINGS
    if string in COMMON_STRINGS:
        return COMMON_STRINGS[string]
    
    # Try pattern-based translation
    pattern_result = apply_pattern_translation(string)
    if pattern_result:
        return pattern_result
    
    # If string is mostly mathematical, skip  
    if extract_variables_and_translate(string):
        return None
    
    # For remaining strings, return None (will need manual curation or API)
    return None

def get_existing_translations(file_path):
    """Get all existing translations"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Extract all keys
        matches = re.findall(r'"([^"]+)":\s*"([^"]*)"', content)
        return {k: v for k, v in matches}
    except:
        return {}

def add_comprehensive_translations(output_file, new_translations):
    """Add translations to the global_translations.js file"""
    existing = get_existing_translations(output_file)
    
    # Filter to only add new ones
    to_add = {k: v for k, v in new_translations.items() if k not in existing}
    
    if not to_add:
        print("No new translations to add")
        return 0
    
    print(f"Adding {len(to_add)} new translations...")
    
    # Read file
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create translation entries
    translation_lines = []
    for eng, chin in sorted(to_add.items()):
        eng_esc = eng.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        chin_esc = chin.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        translation_lines.append(f'    "{eng_esc}": "{chin_esc}",')
    
    # Find insertion point
    last_entry = re.search(r'(".*?":\s*".*?",)\s*\n(\s*\}[,;]?)', content, re.DOTALL)
    if not last_entry:
        print("Could not find insertion point")
        return 0
    
    # Insert
    new_content = (
        content[:last_entry.end(1)] + '\n' +
        '\n'.join(translation_lines) + '\n' +
        content[last_entry.start(2):]
    )
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return len(to_add)

def main():
    trans_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
    
    print("=" * 70)
    print("ALGEBRA 2 COMPREHENSIVE TRANSLATION EXTRACTION")
    print("=" * 70)
    
    print("\nStep 1: Extracting all unique strings from Algebra 2 content...")
    all_strings = extract_all_algebra2_strings()
    print(f"  Extracted {len(all_strings)} unique strings")
    
    if not all_strings:
        print("  No strings found. Check directory paths.")
        return
    
    print("\nStep 2: Applying pattern-based translations...")
    translated = {}
    untranslated = []
    
    for string in sorted(all_strings):
        result = translate_string(string)
        if result:
            translated[string] = result
        else:
            untranslated.append(string)
    
    print(f"  Pattern-based translations: {len(translated)}")
    print(f"  Remaining untranslated: {len(untranslated)}")
    
    print("\nStep 3: Adding translations to global_translations.js...")
    # Add pattern-based translations
    added = add_comprehensive_translations(trans_file, translated)
    print(f"  Added {added} new translations")
    
    print("\n" + "=" * 70)
    print("TRANSLATION EXTRACTION COMPLETE")
    print("=" * 70)
    print(f"\nSummary:")
    print(f"  Total unique strings in Algebra 2: {len(all_strings)}")
    print(f"  Translations added: {added}")
    print(f"  Remaining (may require manual or API translation): {len(all_strings) - added}")
    print(f"\nNote: For the remaining strings, consider:")
    print(f"  1. AI-powered translation API (Google Translate, DeepL)")
    print(f"  2. Community-driven translation curation")
    print(f"  3. Using English fallback for mathematical expressions")

if __name__ == '__main__':
    main()
