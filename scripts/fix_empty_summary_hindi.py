#!/usr/bin/env python3
"""
Fill in empty Summary translations for Algebra 2 lessons.
"""

import os
import re

# Map Summary titles to correct Hindi versions
SUMMARY_TRANSLATIONS = {
    "Lesson 3.3: Synthetic Division - Summary": "पाठ 3.3: सिंथेटिक विभाजन - सारांश",
    "Lesson 3.4: Polynomial Graphs & Zeros - Summary": "पाठ 3.4: बहुपद ग्राफ और शून्य - सारांश",
    "Lesson 3.5: Remainder & Factor Theorems - Summary": "पाठ 3.5: शेषफल और गुणनखंड प्रमेय - सारांश",
    "Lesson 3.6: Complex Numbers & Polynomial Roots - Summary": "पाठ 3.6: सम्मिश्र संख्याएं और बहुपद मूल - सारांश",
    
    "Lesson 4.1: Rational Expressions - Summary": "पाठ 4.1: परिमेय व्यंजक - सारांश",
    "Lesson 4.2: Operations on Rational Expressions - Summary": "पाठ 4.2: परिमेय व्यंजकों पर संक्रियाएं - सारांश",
    "Lesson 4.3: Rational Equations - Summary": "पाठ 4.3: परिमेय समीकरण - सारांश",
    "Lesson 4.4: Graphing Rational Functions - Summary": "पाठ 4.4: परिमेय कार्यों को ग्राफ करना - सारांश",
    "Lesson 4.5: Asymptotes & Discontinuities - Summary": "पाठ 4.5: अनंतस्पर्शी और असंततता - सारांश",
    
    "Lesson 5.1: Exponential Functions & Growth - Summary": "पाठ 5.1: घातांकीय कार्य और वृद्धि - सारांश",
    "Lesson 5.2: Exponential Decay & Applications - Summary": "पाठ 5.2: घातांकीय क्षय और अनुप्रयोग - सारांश",
    "Lesson 5.3: Logarithms & Properties - Summary": "पाठ 5.3: लॉगरिदम और गुण - सारांश",
    "Lesson 5.4: Logarithmic Functions & Graphs - Summary": "पाठ 5.4: लॉगरिदमिक कार्य और ग्राफ - सारांश",
    "Lesson 5.5: Exponential & Logarithmic Equations - Summary": "पाठ 5.5: घातांकीय और लॉगरिदमिक समीकरण - सारांश",
    "Lesson 5.6: Applications of Exponentials & Logs - Summary": "पाठ 5.6: घातांकीय और लॉगरिदम के अनुप्रयोग - सारांश",
    
    "Lesson 6.1: Arithmetic Sequences - Summary": "पाठ 6.1: अंकगणितीय अनुक्रम - सारांश",
    "Lesson 6.2: Geometric Sequences - Summary": "पाठ 6.2: ज्यामितीय अनुक्रम - सारांश",
    "Lesson 6.3: Series & Summation Notation - Summary": "पाठ 6.3: श्रृंखला और योग संकेतन - सारांश",
    "Lesson 6.4: Infinite Geometric Series - Summary": "पाठ 6.4: अनंत ज्यामितीय श्रृंखला - सारांश",
    
    "Lesson 7.1: Counting Principles - Summary": "पाठ 7.1: गिनती के सिद्धांत - सारांश",
}

def fill_empty_summaries():
    """Replace empty Summary translations with proper ones."""
    trans_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'ArisEdu Project Folder', 'scripts', 'hindi_translations.js'
    )
    
    with open(trans_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixed_count = 0
    
    for title, hindi_title in SUMMARY_TRANSLATIONS.items():
        # Pattern: "Title": "",
        pattern = f'    "{title}": "",'
        replacement = f'    "{title}": "{hindi_title}",'
        
        if pattern in content:
            content = content.replace(pattern, replacement)
            fixed_count += 1
            print(f"✓ Fixed: {title}")
        else:
            # Also check if it exists but with a translation already
            if f'"{title}":' in content:
                print(f"- Already has translation: {title}")
            else:
                print(f"⚠ Not found: {title}")
    
    # Write back
    with open(trans_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n{'='*60}")
    print(f"Fixed {fixed_count} empty Summary translations")
    print(f"{'='*60}")

if __name__ == '__main__':
    fill_empty_summaries()
