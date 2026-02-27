#!/usr/bin/env python3
"""
Add Hindi translations for empty Algebra 2 lessons in the hindi_translations.js file.
"""

import os
import re

# Mapping of English lesson titles to Hindi translations
ALGEBRA2_TRANSLATIONS = {
    "Lesson 3.3: Synthetic Division": "पाठ 3.3: सिंथेटिक विभाजन",
    "Lesson 3.4: Polynomial Graphs & Zeros": "पाठ 3.4: बहुपद ग्राफ और शून्य",
    "Lesson 3.5: Remainder & Factor Theorems": "पाठ 3.5: शेषफल और गुणनखंड प्रमेय",
    "Lesson 3.6: Complex Numbers & Polynomial Roots": "पाठ 3.6: सम्मिश्र संख्याएं और बहुपद मूल",
    
    "Lesson 4.1: Rational Expressions": "पाठ 4.1: परिमेय व्यंजक",
    "Lesson 4.2: Operations on Rational Expressions": "पाठ 4.2: परिमेय व्यंजकों पर संक्रियाएं",
    "Lesson 4.3: Rational Equations": "पाठ 4.3: परिमेय समीकरण",
    "Lesson 4.4: Graphing Rational Functions": "पाठ 4.4: परिमेय कार्यों को ग्राफ करना",
    "Lesson 4.5: Asymptotes & Discontinuities": "पाठ 4.5: अनंतस्पर्शी और असंततता",
    
    "Lesson 5.1: Exponential Functions & Growth": "पाठ 5.1: घातांकीय कार्य और वृद्धि",
    "Lesson 5.2: Exponential Decay & Applications": "पाठ 5.2: घातांकीय क्षय और अनुप्रयोग",
    "Lesson 5.3: Logarithms & Properties": "पाठ 5.3: लॉगरिदम और गुण",
    "Lesson 5.4: Logarithmic Functions & Graphs": "पाठ 5.4: लॉगरिदमिक कार्य और ग्राफ",
    "Lesson 5.5: Exponential & Logarithmic Equations": "पाठ 5.5: घातांकीय और लॉगरिदमिक समीकरण",
    "Lesson 5.6: Applications of Exponentials & Logs": "पाठ 5.6: घातांकीय और लॉगरिदम के अनुप्रयोग",
    
    "Lesson 6.1: Arithmetic Sequences": "पाठ 6.1: अंकगणितीय अनुक्रम",
    "Lesson 6.2: Geometric Sequences": "पाठ 6.2: ज्यामितीय अनुक्रम",
    "Lesson 6.3: Series & Summation Notation": "पाठ 6.3: श्रृंखला और योग संकेतन",
    "Lesson 6.4: Infinite Geometric Series": "पाठ 6.4: अनंत ज्यामितीय श्रृंखला",
    
    "Lesson 7.1: Counting Principles": "पाठ 7.1: गिनती के सिद्धांत",
}

def fix_empty_translations():
    """Replace empty translations with proper Hindi translations."""
    trans_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'ArisEdu Project Folder', 'scripts', 'hindi_translations.js'
    )
    
    with open(trans_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixed_count = 0
    
    for english_title, hindi_title in ALGEBRA2_TRANSLATIONS.items():
        # Pattern: "English Title": "",
        pattern = f'    "{english_title}": "",'
        replacement = f'    "{english_title}": "{hindi_title}",'
        
        if pattern in content:
            content = content.replace(pattern, replacement)
            fixed_count += 1
            print(f"✓ Fixed: {english_title}")
        else:
            print(f"⚠ Not found: {english_title}")
    
    # Write back
    with open(trans_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n{'='*60}")
    print(f"Fixed {fixed_count} empty translations")
    print(f"{'='*60}")

if __name__ == '__main__':
    fix_empty_translations()
