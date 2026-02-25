#!/usr/bin/env python3
"""
Extract ALL translatable text from every Algebra 2 HTML file
(Video, Summary, Practice, Quiz, Test) and compare against global_translations.js
"""
import os, re, json, html
from html.parser import HTMLParser

BASE = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
TRANS_FILE = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"

# ── 1. Load existing translations ──────────────────────────────────────
existing = set()
with open(TRANS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        m = re.match(r'^\s*"(.+?)"\s*:', line)
        if m:
            existing.add(m.group(1))
print(f"Existing translation keys: {len(existing)}")

# ── 2. Extract visible text from HTML ──────────────────────────────────
class TextExtractor(HTMLParser):
    SKIP_TAGS = {'script', 'style', 'meta', 'link', 'head', 'noscript', 'svg', 'path'}
    
    def __init__(self):
        super().__init__()
        self.texts = []
        self.skip_depth = 0
        self.tag_stack = []
    
    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
    
    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
        if tag in self.SKIP_TAGS:
            self.skip_depth -= 1
    
    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        text = data.strip()
        if text:
            self.texts.append(text)

def extract_visible_text(filepath):
    """Extract all visible text from an HTML file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    parser = TextExtractor()
    parser.feed(content)
    return parser.texts

def extract_flashcard_content(filepath):
    """Extract flashcard question/answer from Practice files."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    strings = []
    # Match window.lessonFlashcards array
    m = re.search(r'window\.lessonFlashcards\s*=\s*\[(.*?)\];', content, re.DOTALL)
    if m:
        block = m.group(1)
        for field in re.findall(r'(?:question|answer)\s*:\s*"((?:[^"\\]|\\.)*)"', block):
            field = field.replace('\\"', '"').replace('\\n', '\n').strip()
            if field:
                strings.append(field)
    return strings

def extract_quiz_content(filepath):
    """Extract quiz question text and answer options from Quiz files."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    strings = []
    
    # Quiz questions (in <p> tags typically)
    for m in re.finditer(r'<p[^>]*>\s*(\d+\.\s*.+?)\s*</p>', content, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = html.unescape(text)
        if text:
            strings.append(text)
    
    # Answer labels - text after radio input
    for m in re.finditer(r'<input[^>]*>\s*(.+?)\s*</label>', content, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = html.unescape(text)
        if text:
            strings.append(text)
    
    return strings

def extract_unit_test_content(filepath):
    """Extract unit test question text and answer options."""
    return extract_quiz_content(filepath)  # Same structure

def extract_summary_content(filepath):
    """Extract summary/lesson notes text."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    strings = []
    
    # Get lesson-notes div content
    m = re.search(r'<div class="lesson-notes">(.*?)</div>\s*</div>', content, re.DOTALL)
    if not m:
        m = re.search(r'<div class="lesson-notes">(.*?)(?:</div>\s*){2,}', content, re.DOTALL)
    if m:
        block = m.group(1)
        # Extract text from tags
        for text_match in re.finditer(r'>([^<]+)<', block):
            text = text_match.group(1).strip()
            text = html.unescape(text)
            if text and len(text) > 1:
                strings.append(text)
    
    return strings

def extract_video_content(filepath):
    """Extract video page text (titles, button labels, rubric text)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    strings = []
    
    # Page titles
    for m in re.finditer(r'<h2[^>]*class="page-title"[^>]*>(.*?)</h2>', content, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = html.unescape(text)
        if text:
            strings.append(text)
    
    # Button text
    for m in re.finditer(r'<(?:button|a)[^>]*class="[^"]*(?:side-button|action-button|nav-button)[^"]*"[^>]*>(.*?)</(?:button|a)>', content, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = html.unescape(text)
        if text:
            strings.append(text)
    
    # Videos panel title
    for m in re.finditer(r'<div[^>]*class="videos-panel-title"[^>]*>(.*?)</div>', content, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = html.unescape(text)
        if text:
            strings.append(text)
    
    # Rubric labels
    for m in re.finditer(r'<span class="rubric-label">(.*?)</span>', content):
        strings.append(m.group(1).strip())
    for m in re.finditer(r'<span class="rubric-rating">(.*?)</span>', content):
        strings.append(m.group(1).strip())
    
    return strings

# ── 3. Process all files ───────────────────────────────────────────────
all_strings = {}  # text -> set of source files
by_type = {"Video": set(), "Summary": set(), "Practice": set(), "Quiz": set(), "Test": set()}

for root, dirs, files in os.walk(BASE):
    for fname in sorted(files):
        if not fname.endswith(".html"):
            continue
        fpath = os.path.join(root, fname)
        
        if "_Video" in fname:
            ftype = "Video"
            texts = extract_video_content(fpath)
        elif "_Summary" in fname:
            ftype = "Summary"
            texts = extract_summary_content(fpath)
        elif "_Practice" in fname:
            ftype = "Practice"
            texts = extract_flashcard_content(fpath)
        elif "_Quiz" in fname:
            ftype = "Quiz"
            texts = extract_quiz_content(fpath)
        elif "_Test" in fname:
            ftype = "Test"
            texts = extract_unit_test_content(fpath)
        else:
            continue
        
        for t in texts:
            t = t.strip()
            if not t:
                continue
            # Skip pure numbers, single chars, pure math symbols
            if re.match(r'^[\d\s.,+\-*/=<>()^\[\]{}|&%#@!~`]+$', t):
                continue
            if len(t) <= 1:
                continue
            
            if t not in all_strings:
                all_strings[t] = set()
            all_strings[t].add(fname)
            by_type[ftype].add(t)

print(f"\nTotal unique strings extracted: {len(all_strings)}")
for ftype, strings in by_type.items():
    print(f"  {ftype}: {len(strings)} unique strings")

# ── 4. Find missing translations ──────────────────────────────────────
missing = {}
for text, sources in all_strings.items():
    if text not in existing:
        missing[text] = list(sources)

print(f"\nMissing translations: {len(missing)}")
for ftype in by_type:
    count = sum(1 for t in by_type[ftype] if t in missing)
    print(f"  {ftype} missing: {count}")

# Show samples of missing strings by type
for ftype in by_type:
    missing_in_type = [t for t in by_type[ftype] if t in missing]
    if missing_in_type:
        print(f"\n--- {ftype} missing samples (first 10) ---")
        for s in sorted(missing_in_type)[:10]:
            print(f"  [{len(s):>4}] {s[:120]}")

# ── 5. Save missing strings ──────────────────────────────────────────
with open("/workspaces/ArisEdu/algebra2_all_missing.json", "w", encoding="utf-8") as f:
    json.dump(missing, f, ensure_ascii=False, indent=2)

print(f"\nSaved missing strings to algebra2_all_missing.json")
