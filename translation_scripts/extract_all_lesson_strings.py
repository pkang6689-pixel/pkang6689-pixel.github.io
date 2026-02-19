"""
Extract ALL unique untranslated strings from physics lesson files:
- Quiz files: questions + answer options
- Practice files: flashcard Q&A
- Summary files: headings, paragraphs, list items (text nodes)
Outputs a JSON file of untranslated strings.
"""
import os, re, json
from html.parser import HTMLParser

BASE = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..',
    'ArisEdu Project Folder', 'PhysicsLessons'
))
GLOBAL_JS = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..',
    'ArisEdu Project Folder', 'scripts', 'global_translations.js'
))
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'untranslated_lesson_strings.json')


def load_existing_translations():
    """Load all English keys already in global_translations.js."""
    with open(GLOBAL_JS, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find all "key": "value" pairs
    keys = set()
    for m in re.finditer(r'"([^"]+)":\s*"[^"]*"', content):
        keys.add(m.group(1))
    return keys


def extract_quiz_strings(filepath):
    """Extract questions and answer options from a quiz HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    strings = []
    
    # Questions: look for numbered questions in quiz-question elements or divs
    # Pattern: "1. What is a physical quantity?"
    for m in re.finditer(r'>\s*(\d+)\.\s+(.+?)\s*<', html):
        q = m.group(2).strip()
        if q and len(q) > 3:
            strings.append(q)
    
    # Answer options in onclick handlers or value attributes
    # Pattern: onclick="checkQuizAnswer('A', ...)" with visible text
    for m in re.finditer(r'checkQuizAnswer\([^)]+\)[^>]*>([^<]+)<', html):
        opt = m.group(1).strip()
        if opt and len(opt) > 0:
            # Remove letter prefix like "A) " or "A. "
            opt = re.sub(r'^[A-D]\)\s*', '', opt)
            opt = re.sub(r'^[A-D]\.\s*', '', opt)
            if opt:
                strings.append(opt)
    
    # Also try label/span patterns for answer text
    for m in re.finditer(r'<label[^>]*>\s*(?:<input[^>]*>)?\s*([^<]+)', html):
        opt = m.group(1).strip()
        opt = re.sub(r'^[A-D]\)\s*', '', opt)
        if opt and len(opt) > 1:
            strings.append(opt)
    
    # Try div.quiz-option or similar
    for m in re.finditer(r'class="[^"]*option[^"]*"[^>]*>([^<]+)', html):
        opt = m.group(1).strip()
        opt = re.sub(r'^[A-D]\)\s*', '', opt)
        if opt and len(opt) > 1:
            strings.append(opt)
    
    return strings


def extract_flashcard_strings(filepath):
    """Extract flashcard Q&A from a practice HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    strings = []
    
    # Pattern: { question: "...", answer: "..." }
    for m in re.finditer(r'question:\s*"((?:[^"\\]|\\.)*)"\s*,\s*answer:\s*"((?:[^"\\]|\\.)*)"', html):
        q = m.group(1).replace('\\"', '"').replace('\\n', ' ').strip()
        a = m.group(2).replace('\\"', '"').replace('\\n', ' ').strip()
        if q:
            strings.append(q)
        if a:
            strings.append(a)
    
    # Also try single-quoted version
    for m in re.finditer(r"question:\s*'((?:[^'\\]|\\.)*)'\s*,\s*answer:\s*'((?:[^'\\]|\\.)*)'", html):
        q = m.group(1).replace("\\'", "'").strip()
        a = m.group(2).replace("\\'", "'").strip()
        if q:
            strings.append(q)
        if a:
            strings.append(a)
    
    return strings


class SummaryTextExtractor(HTMLParser):
    """Extract text content from summary HTML, including text nodes split by inline elements."""
    def __init__(self):
        super().__init__()
        self.in_lesson_notes = False
        self.depth = 0
        self.texts = []
        self.current_tag = None
        self.skip_tags = {'script', 'style', 'a'}
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        cls = attrs_dict.get('class', '')
        if 'lesson-notes' in cls:
            self.in_lesson_notes = True
            self.depth = 0
        if self.in_lesson_notes:
            self.depth += 1
            self.current_tag = tag
            
    def handle_endtag(self, tag):
        if self.in_lesson_notes:
            self.depth -= 1
            if self.depth <= 0:
                self.in_lesson_notes = False
                
    def handle_data(self, data):
        if self.in_lesson_notes:
            text = data.strip()
            if text and len(text) > 1:
                self.texts.append(text)


def extract_summary_strings(filepath):
    """Extract translatable text from a summary HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    parser = SummaryTextExtractor()
    parser.feed(html)
    return parser.texts


def main():
    existing = load_existing_translations()
    print(f"Found {len(existing)} existing translation keys")
    
    all_strings = {}  # string -> source info
    quiz_count = 0
    flash_count = 0
    summary_count = 0
    
    for unit_num in range(1, 12):
        unit_dir = os.path.join(BASE, f'Unit{unit_num}')
        if not os.path.isdir(unit_dir):
            continue
        
        for fname in sorted(os.listdir(unit_dir)):
            fpath = os.path.join(unit_dir, fname)
            
            if fname.endswith('_Quiz.html'):
                strings = extract_quiz_strings(fpath)
                for s in strings:
                    if s not in all_strings:
                        all_strings[s] = f"quiz:U{unit_num}"
                quiz_count += len(strings)
                        
            elif fname.endswith('_Practice.html'):
                strings = extract_flashcard_strings(fpath)
                for s in strings:
                    if s not in all_strings:
                        all_strings[s] = f"flash:U{unit_num}"
                flash_count += len(strings)
                        
            elif fname.endswith('_Summary.html'):
                strings = extract_summary_strings(fpath)
                for s in strings:
                    if s not in all_strings:
                        all_strings[s] = f"summary:U{unit_num}"
                summary_count += len(strings)
    
    # Filter out already translated
    untranslated = {s: src for s, src in all_strings.items() if s not in existing}
    already = {s: src for s, src in all_strings.items() if s in existing}
    
    # Also filter out very short/trivial strings
    trivial = {'', '.', ',', ':', ';', '—', '–', '-'}
    untranslated = {s: src for s, src in untranslated.items() if s not in trivial}
    
    print(f"\nExtraction complete:")
    print(f"  Quiz strings found: {quiz_count}")
    print(f"  Flashcard strings found: {flash_count}")
    print(f"  Summary strings found: {summary_count}")
    print(f"  Total unique: {len(all_strings)}")
    print(f"  Already translated: {len(already)}")
    print(f"  Untranslated: {len(untranslated)}")
    
    # Organize by source type
    by_type = {'quiz': [], 'flash': [], 'summary': []}
    for s, src in untranslated.items():
        typ = src.split(':')[0]
        by_type[typ].append(s)
    
    print(f"\n  Quiz untranslated: {len(by_type['quiz'])}")
    print(f"  Flashcard untranslated: {len(by_type['flash'])}")
    print(f"  Summary untranslated: {len(by_type['summary'])}")
    
    # Write to JSON
    output = {
        '_meta': {
            'total_untranslated': len(untranslated),
            'quiz_count': len(by_type['quiz']),
            'flashcard_count': len(by_type['flash']),
            'summary_count': len(by_type['summary']),
        },
        'strings': {s: src for s, src in sorted(untranslated.items())}
    }
    
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\nWrote to {OUTPUT}")


if __name__ == '__main__':
    main()
