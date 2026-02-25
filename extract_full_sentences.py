#!/usr/bin/env python3
"""
Extract the FULL textContent of every translatable element (p, h3, li, h2, etc.)
from ALL Algebra 2 Summary files. This captures complete sentences as they would
appear to the translateNode() function, which checks element.textContent.

Also extract from Quiz and Test files: full question text and answer labels.
"""
import os, re, json, html
from html.parser import HTMLParser

BASE = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
TRANS_FILE = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"

# ── Load existing translations (with escaped-quote handling) ──
existing = set()
with open(TRANS_FILE, "r", encoding="utf-8") as f:
    content = f.read()
for m in re.finditer(r'^\s*"((?:[^"\\]|\\.)*)"\s*:', content, re.MULTILINE):
    key = m.group(1).replace('\\"', '"').replace('\\\\', '\\')
    existing.add(key)
print(f"Existing translation keys: {len(existing)}")


class ElementTextExtractor(HTMLParser):
    """
    Extracts the full textContent of block-level and inline semantic elements.
    This mimics what the browser gives you with element.textContent.
    """
    # Elements whose full textContent we want to capture
    CAPTURE_TAGS = {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'dt', 'dd',
                    'figcaption', 'caption', 'label', 'td', 'th', 'b', 'strong',
                    'span', 'em', 'button', 'a'}
    SKIP_TAGS = {'script', 'style', 'meta', 'link', 'head', 'noscript', 'svg', 'path'}
    
    def __init__(self):
        super().__init__()
        self.results = []  # list of (tag, textContent)
        self.skip_depth = 0
        self.capture_stack = []  # stack of (tag, text_parts)
        
    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth > 0:
            return
        if tag in self.CAPTURE_TAGS:
            self.capture_stack.append((tag, []))
    
    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS:
            self.skip_depth -= 1
            return
        if self.skip_depth > 0:
            return
        if tag in self.CAPTURE_TAGS and self.capture_stack:
            ctag, parts = self.capture_stack.pop()
            if ctag == tag:
                full_text = ''.join(parts).strip()
                # Normalize whitespace (like browser textContent does)
                full_text = re.sub(r'\s+', ' ', full_text).strip()
                if full_text and len(full_text) > 1:
                    self.results.append((tag, full_text))
                    # Also propagate text up to parent capture elements
                    if self.capture_stack:
                        self.capture_stack[-1][1].append(' '.join(parts))
    
    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        # Add text to all active capture elements
        for i in range(len(self.capture_stack)):
            self.capture_stack[i][1].append(data)


def extract_element_text(filepath):
    """Extract full textContent of all translatable elements."""
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    parser = ElementTextExtractor()
    parser.feed(raw)
    return parser.results


def extract_flashcard_strings(filepath):
    """Extract flashcard question/answer strings from Practice files."""
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    strings = []
    m = re.search(r'window\.lessonFlashcards\s*=\s*\[(.*?)\];', raw, re.DOTALL)
    if m:
        block = m.group(1)
        for field in re.findall(r'(?:question|answer)\s*:\s*"((?:[^"\\]|\\.)*)"', block):
            field = field.replace('\\"', '"').replace('\\n', '\n').strip()
            if field and len(field) > 1:
                strings.append(field)
    return strings


# ── Process ALL Algebra 2 files ──
all_strings = {}  # text -> set of source files
by_type = {}

file_count = 0
for root, dirs, files in os.walk(BASE):
    for fname in sorted(files):
        if not fname.endswith(".html"):
            continue
        fpath = os.path.join(root, fname)
        file_count += 1
        
        # Determine file type
        if "_Summary" in fname:
            ftype = "Summary"
        elif "_Video" in fname:
            ftype = "Video"
        elif "_Practice" in fname:
            ftype = "Practice"
        elif "_Quiz" in fname:
            ftype = "Quiz"
        elif "_Test" in fname:
            ftype = "Test"
        else:
            continue
        
        if ftype not in by_type:
            by_type[ftype] = set()
        
        # Extract text based on file type
        if ftype == "Practice":
            texts = extract_flashcard_strings(fpath)
            for t in texts:
                t = t.strip()
                if not t or len(t) <= 1:
                    continue
                if t not in all_strings:
                    all_strings[t] = set()
                all_strings[t].add(fname)
                by_type[ftype].add(t)
        else:
            # For all file types, extract full element textContent
            elements = extract_element_text(fpath)
            for tag, text in elements:
                text = html.unescape(text).strip()
                if not text or len(text) <= 1:
                    continue
                # Skip pure numbers/math symbols
                if re.match(r'^[\d\s.,+\-*/=<>()^\[\]{}|&%#@!~`]+$', text):
                    continue
                if text not in all_strings:
                    all_strings[text] = set()
                all_strings[text].add(fname)
                by_type[ftype].add(text)

print(f"\nProcessed {file_count} files")
print(f"Total unique strings: {len(all_strings)}")
for ftype in sorted(by_type.keys()):
    print(f"  {ftype}: {len(by_type[ftype])}")

# ── Find missing ──
missing = {}
for text, sources in all_strings.items():
    if text not in existing:
        missing[text] = list(sources)

print(f"\nMissing translations: {len(missing)}")
for ftype in sorted(by_type.keys()):
    count = sum(1 for t in by_type[ftype] if t in missing)
    print(f"  {ftype} missing: {count}")

# ── Show samples ──
for ftype in sorted(by_type.keys()):
    missing_in_type = [t for t in by_type[ftype] if t in missing]
    if missing_in_type:
        print(f"\n--- {ftype} missing (first 15) ---")
        for s in sorted(missing_in_type, key=len, reverse=True)[:15]:
            print(f"  [{len(s):>4}] {s[:150]}...")

# ── Save ──
with open("/workspaces/ArisEdu/algebra2_missing_full.json", "w", encoding="utf-8") as f:
    json.dump(missing, f, ensure_ascii=False, indent=2)

print(f"\nSaved to algebra2_missing_full.json")
