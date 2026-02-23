#!/usr/bin/env python3
"""
Extract all visible text from ALL 98 geometry summary HTML files
and identify strings missing from the translation dictionary.

Uses Python's html.parser (no BeautifulSoup dependency).
"""

import os
import re
import json
import glob
from html.parser import HTMLParser
from html import unescape
from collections import OrderedDict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GEOMETRY_DIR = os.path.join(BASE_DIR, 'ArisEdu Project Folder', 'GeometryLessons')
DICT_FILE = os.path.join(BASE_DIR, 'geometry_translation_dict.json')
OUTPUT_FILE = os.path.join(BASE_DIR, 'missing_geometry_summary_strings.json')


def remove_span_tags(html):
    """
    Remove ALL <span ...> and </span> tags while preserving text content.
    Handles malformed HTML where data-en attributes contain nested HTML tags.
    Uses character-by-character scanning to properly handle quoted attributes.
    """
    # Step 1: Remove </span> (simple string replacement)
    html = html.replace('</span>', '')

    # Step 2: Remove opening <span ...> tags
    # We must handle the case where attribute values contain '>' characters
    # (from nested HTML in data-en attributes).
    # Strategy: when inside a quoted attribute value, don't treat '>' as tag-close.
    result = []
    i = 0
    n = len(html)
    while i < n:
        # Check for <span (case insensitive)
        if i + 5 < n and html[i] == '<' and html[i+1:i+5].lower() == 'span':
            # Check that next char is space, >, or / (not <spanish> etc.)
            next_ch = html[i+5] if i+5 < n else ''
            if next_ch in (' ', '>', '/', '\t', '\n', '\r'):
                # Found a <span tag - scan to find the real closing >
                j = i + 5
                in_quote = False
                quote_char = None
                while j < n:
                    ch = html[j]
                    if in_quote:
                        if ch == quote_char:
                            in_quote = False
                    else:
                        if ch == '"' or ch == "'":
                            in_quote = True
                            quote_char = ch
                        elif ch == '>':
                            j += 1  # skip the >
                            break
                    j += 1
                i = j
                continue
        result.append(html[i])
        i += 1
    return ''.join(result)


class SummaryTextExtractor(HTMLParser):
    """
    Extract visible text from geometry summary HTML files.
    Collects text from h2, h3, p, li, th, td, and a elements.
    """

    def __init__(self):
        super().__init__()
        self.texts = []            # Final list of extracted text strings

        # State: are we inside the lesson-notes div?
        self.in_lesson_notes = False
        self.lesson_notes_div_depth = 0
        self.div_depth = 0

        # State: are we inside a summary-actions div?
        self.in_summary_actions = False
        self.summary_actions_div_depth = 0

        # State: are we currently collecting text for a target element?
        self.collecting = False
        self.collect_tag = None
        self.collect_depth = 0
        self.current_parts = []

        # Skip script/style content
        self.skip_depth = 0

        # Elements whose text we want to extract
        self.content_tags = {'h3', 'p', 'li', 'th', 'td'}

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Skip script/style
        if tag in ('script', 'style'):
            self.skip_depth += 1
            return
        if self.skip_depth:
            return

        # Track div nesting
        if tag == 'div':
            self.div_depth += 1
            cls = attrs_dict.get('class', '')
            if 'lesson-notes' in cls:
                self.in_lesson_notes = True
                self.lesson_notes_div_depth = self.div_depth
            if 'summary-actions' in cls:
                self.in_summary_actions = True
                self.summary_actions_div_depth = self.div_depth

        # Decide whether to start collecting text
        if not self.collecting:
            should_collect = False

            # h2 page title (anywhere)
            if tag == 'h2':
                should_collect = True
            # Content elements inside lesson-notes
            elif self.in_lesson_notes and tag in self.content_tags:
                should_collect = True
            # Links inside summary-actions
            elif self.in_summary_actions and tag == 'a':
                should_collect = True

            if should_collect:
                self.collecting = True
                self.collect_tag = tag
                self.collect_depth = 1
                self.current_parts = []
        else:
            # Handle nested same-tag
            if tag == self.collect_tag:
                self.collect_depth += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return

        # Track div nesting
        if tag == 'div':
            if self.in_lesson_notes and self.div_depth == self.lesson_notes_div_depth:
                self.in_lesson_notes = False
            if self.in_summary_actions and self.div_depth == self.summary_actions_div_depth:
                self.in_summary_actions = False
            self.div_depth = max(0, self.div_depth - 1)

        # Finish collecting when the target element closes
        if self.collecting and tag == self.collect_tag:
            self.collect_depth -= 1
            if self.collect_depth <= 0:
                text = ''.join(self.current_parts).strip()
                text = re.sub(r'\s+', ' ', text)  # normalize whitespace
                if text and len(text) > 1:
                    self.texts.append(text)
                self.collecting = False
                self.collect_tag = None
                self.current_parts = []

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.collecting:
            self.current_parts.append(data)

    def handle_entityref(self, name):
        if self.skip_depth:
            return
        if self.collecting:
            try:
                self.current_parts.append(unescape(f'&{name};'))
            except Exception:
                self.current_parts.append(f'&{name};')

    def handle_charref(self, name):
        if self.skip_depth:
            return
        if self.collecting:
            try:
                self.current_parts.append(unescape(f'&#{name};'))
            except Exception:
                self.current_parts.append(f'&#{name};')

    def error(self, message):
        pass  # Ignore HTML parsing errors


def extract_texts_from_file(filepath):
    """
    Extract all visible text strings from a summary HTML file.
    Returns a list of text strings.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Pre-process: remove all <span ...> and </span> tags
    # This cleanly handles the nested-HTML-in-data-en-attribute issue
    html = remove_span_tags(html)

    parser = SummaryTextExtractor()
    try:
        parser.feed(html)
    except Exception as e:
        print(f"  WARNING: parser error in {os.path.basename(filepath)}: {e}")

    return parser.texts


def normalize(text):
    """Normalize text for dictionary comparison."""
    t = text.strip()
    t = re.sub(r'\s+', ' ', t)
    return t


def build_lookup_set(trans_dict):
    """
    Build a set of normalized dictionary keys for fast lookup.
    Also builds an alternative set with common variations.
    """
    keys_exact = set(trans_dict.keys())
    keys_normalized = set()
    for k in keys_exact:
        keys_normalized.add(normalize(k))
    return keys_exact, keys_normalized


def is_in_dictionary(text, keys_exact, keys_normalized):
    """Check if text (or its normalized form) exists in the dictionary."""
    if text in keys_exact:
        return True
    n = normalize(text)
    if n in keys_normalized:
        return True
    # Also try with/without trailing period
    if n.endswith('.'):
        if n[:-1].strip() in keys_normalized:
            return True
    else:
        if (n + '.') in keys_normalized:
            return True
    return False


# Strings that are UI/navigation elements, not lesson content
SKIP_STRINGS = {
    'Next Up: Play',
    'Next Up: Practice',
}


def should_skip(text):
    """Determine if a string should be skipped (not lesson content)."""
    t = normalize(text)
    if t in SKIP_STRINGS:
        return True
    if len(t) <= 2:
        return True
    # Skip if it's purely a lesson title like "Lesson X.X: ..."
    # (these are translated via page title mechanism, not dictionary)
    if re.match(r'^Lesson \d+\.\d+:', t):
        return True
    return False


def get_unit_sort_key(unit_key):
    """Sort units numerically."""
    m = re.search(r'(\d+)', unit_key)
    return int(m.group(1)) if m else 999


def get_lesson_sort_key(filename):
    """Sort lessons numerically."""
    m = re.search(r'Lesson(\d+)\.(\d+)', filename)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    return (999, 999)


def main():
    # Load translation dictionary
    print("Loading translation dictionary...")
    with open(DICT_FILE, 'r', encoding='utf-8') as f:
        trans_dict = json.load(f)

    keys_exact, keys_normalized = build_lookup_set(trans_dict)
    print(f"  Dictionary has {len(keys_exact)} entries")

    # Find all summary files
    pattern = os.path.join(GEOMETRY_DIR, 'Unit*', 'Lesson*_Summary.html')
    summary_files = sorted(glob.glob(pattern))
    print(f"  Found {len(summary_files)} summary files\n")

    if not summary_files:
        print("ERROR: No summary files found!")
        print(f"  Looked in: {pattern}")
        return

    # Process each file
    all_missing = OrderedDict()     # unit -> {filename -> [strings]}
    all_extracted = OrderedDict()   # unit -> {filename -> [strings]}
    total_strings = 0
    total_found = 0
    total_missing = 0
    total_skipped = 0
    files_with_missing = 0

    for filepath in summary_files:
        rel_path = os.path.relpath(filepath, GEOMETRY_DIR)
        unit_match = re.search(r'Unit(\d+)', rel_path)
        unit_num = unit_match.group(1) if unit_match else '?'
        unit_key = f'Unit {unit_num}'
        filename = os.path.basename(filepath)

        texts = extract_texts_from_file(filepath)
        file_missing = []

        for text in texts:
            total_strings += 1

            if should_skip(text):
                total_skipped += 1
                continue

            if is_in_dictionary(text, keys_exact, keys_normalized):
                total_found += 1
            else:
                # Check it's not a duplicate in this file's missing list
                n = normalize(text)
                already_listed = any(normalize(s) == n for s in file_missing)
                if not already_listed:
                    file_missing.append(text)
                    total_missing += 1

        # Store extracted texts
        if unit_key not in all_extracted:
            all_extracted[unit_key] = OrderedDict()
        all_extracted[unit_key][filename] = texts

        # Store missing
        if file_missing:
            if unit_key not in all_missing:
                all_missing[unit_key] = OrderedDict()
            all_missing[unit_key][filename] = file_missing
            files_with_missing += 1

    # Sort units and files
    sorted_missing = OrderedDict()
    for unit_key in sorted(all_missing.keys(), key=get_unit_sort_key):
        sorted_files = OrderedDict()
        for fn in sorted(all_missing[unit_key].keys(), key=get_lesson_sort_key):
            sorted_files[fn] = all_missing[unit_key][fn]
        sorted_missing[unit_key] = sorted_files

    # Print summary
    print("=" * 80)
    print("GEOMETRY SUMMARY STRINGS - MISSING TRANSLATION REPORT")
    print("=" * 80)
    print(f"  Total summary files processed:   {len(summary_files)}")
    print(f"  Total text strings extracted:     {total_strings}")
    print(f"  Skipped (UI/titles):              {total_skipped}")
    print(f"  Found in dictionary:              {total_found}")
    print(f"  MISSING from dictionary:          {total_missing}")
    print(f"  Files with missing strings:       {files_with_missing}")
    print("=" * 80)

    # Print missing strings grouped by unit
    for unit_key, files in sorted_missing.items():
        unit_total = sum(len(v) for v in files.values())
        print(f"\n{'─' * 70}")
        print(f"  {unit_key}  ({unit_total} missing strings)")
        print(f"{'─' * 70}")
        for filename, strings in files.items():
            print(f"\n  {filename}  ({len(strings)} missing)")
            for i, s in enumerate(strings, 1):
                # Truncate very long strings for display
                display = s if len(s) <= 120 else s[:117] + '...'
                print(f"    {i}. {display}")

    # Build output JSON
    output = OrderedDict()
    output['summary'] = OrderedDict([
        ('total_files', len(summary_files)),
        ('total_strings_extracted', total_strings),
        ('skipped_ui_titles', total_skipped),
        ('found_in_dictionary', total_found),
        ('missing_from_dictionary', total_missing),
        ('files_with_missing_strings', files_with_missing),
    ])

    # Flatten missing strings for easy consumption
    missing_flat = []
    for unit_key, files in sorted_missing.items():
        for filename, strings in files.items():
            for s in strings:
                missing_flat.append(OrderedDict([
                    ('unit', unit_key),
                    ('file', filename),
                    ('text', s),
                ]))

    output['missing_strings'] = missing_flat
    output['missing_by_unit'] = sorted_missing

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n\nResults saved to: {OUTPUT_FILE}")
    print(f"Total missing strings: {total_missing}")


if __name__ == '__main__':
    main()
