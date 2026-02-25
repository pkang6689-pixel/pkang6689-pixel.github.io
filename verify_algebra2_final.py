#!/usr/bin/env python3
"""
Final comprehensive verification of ALL Algebra 2 translation coverage.
Uses improved key extraction that handles escaped quotes.
"""
import os, re, json, html
from html.parser import HTMLParser

BASE = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
TRANS_FILE = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"

# ── Load existing translations with improved regex ──
existing = set()
with open(TRANS_FILE, "r", encoding="utf-8") as f:
    content = f.read()
for m in re.finditer(r'^\s*"((?:[^"\\]|\\.)*)"\s*:', content, re.MULTILINE):
    key = m.group(1).replace('\\"', '"').replace('\\\\', '\\')
    existing.add(key)

print(f"Total translation keys: {len(existing)}")

# ── Extract text from HTML files ──
def extract_quiz_content(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    strings = []
    for m in re.finditer(r'<p[^>]*>\s*(\d+\.\s*.+?)\s*</p>', content, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = html.unescape(text)
        if text: strings.append(text)
    for m in re.finditer(r'<input[^>]*>\s*(.+?)\s*</label>', content, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = html.unescape(text)
        if text: strings.append(text)
    return strings

def extract_summary_content(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    strings = []
    m = re.search(r'<div class="lesson-notes">(.*?)(?:</div>\s*){2,}', content, re.DOTALL)
    if m:
        for text_match in re.finditer(r'>([^<]+)<', m.group(1)):
            text = text_match.group(1).strip()
            text = html.unescape(text)
            if text and len(text) > 1: strings.append(text)
    return strings

def extract_video_content(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    strings = []
    for m in re.finditer(r'<h2[^>]*class="page-title"[^>]*>(.*?)</h2>', content, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = html.unescape(text)
        if text: strings.append(text)
    for m in re.finditer(r'<(?:button|a)[^>]*class="[^"]*(?:side-button|action-button|nav-button)[^"]*"[^>]*>(.*?)</(?:button|a)>', content, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = html.unescape(text)
        if text: strings.append(text)
    for m in re.finditer(r'<div[^>]*class="videos-panel-title"[^>]*>(.*?)</div>', content, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = html.unescape(text)
        if text: strings.append(text)
    for m in re.finditer(r'<span class="rubric-label">(.*?)</span>', content):
        strings.append(m.group(1).strip())
    for m in re.finditer(r'<span class="rubric-rating">(.*?)</span>', content):
        strings.append(m.group(1).strip())
    return strings

def extract_flashcard_content(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    strings = []
    m = re.search(r'window\.lessonFlashcards\s*=\s*\[(.*?)\];', content, re.DOTALL)
    if m:
        for field in re.findall(r'(?:question|answer)\s*:\s*"((?:[^"\\]|\\.)*)"', m.group(1)):
            field = field.replace('\\"', '"').replace('\\n', '\n').strip()
            if field: strings.append(field)
    return strings

# ── Process all files ──
all_strings = {}
by_type = {"Video": set(), "Summary": set(), "Practice": set(), "Quiz": set(), "Test": set()}

for root, dirs, files in os.walk(BASE):
    for fname in sorted(files):
        if not fname.endswith(".html"): continue
        fpath = os.path.join(root, fname)
        
        if "_Video" in fname: ftype, texts = "Video", extract_video_content(fpath)
        elif "_Summary" in fname: ftype, texts = "Summary", extract_summary_content(fpath)
        elif "_Practice" in fname: ftype, texts = "Practice", extract_flashcard_content(fpath)
        elif "_Quiz" in fname: ftype, texts = "Quiz", extract_quiz_content(fpath)
        elif "_Test" in fname: ftype, texts = "Test", extract_quiz_content(fpath)
        else: continue
        
        for t in texts:
            t = t.strip()
            if not t or len(t) <= 1: continue
            if re.match(r'^[\d\s.,+\-*/=<>()^\[\]{}|&%#@!~`]+$', t): continue
            if t not in all_strings: all_strings[t] = set()
            all_strings[t].add(fname)
            by_type[ftype].add(t)

# ── Check coverage ──
total = len(all_strings)
translated = sum(1 for t in all_strings if t in existing)
missing = total - translated

print(f"\n{'='*60}")
print(f" ALGEBRA 2 TRANSLATION COVERAGE REPORT")
print(f"{'='*60}")
print(f" Total unique strings extracted: {total}")
print(f" Translated:                     {translated}")
print(f" Missing:                        {missing}")
print(f" Coverage:                       {translated/total*100:.1f}%")
print(f"{'='*60}")

for ftype in ["Video", "Summary", "Practice", "Quiz", "Test"]:
    s = by_type[ftype]
    t = sum(1 for x in s if x in existing)
    m = len(s) - t
    pct = (t/len(s)*100) if s else 100
    status = "✓" if m == 0 else "✗"
    print(f" {status} {ftype:>10}: {t}/{len(s)} ({pct:.1f}%) - {m} missing")

print(f"{'='*60}")

if missing > 0:
    missing_list = [t for t in all_strings if t not in existing]
    print(f"\nMissing strings:")
    for s in sorted(missing_list)[:20]:
        print(f"  {repr(s[:120])}")
else:
    print("\n ALL ALGEBRA 2 CONTENT IS FULLY TRANSLATED!")
