#!/usr/bin/env python3
"""
Find and add missing base Algebra 2 lesson translations
"""

import re

# All Algebra 2 lessons that should have base translations
ALGEBRA2_LESSONS = {
    "1.1": ("Review of Functions & Notation", "फ़ंक्शंस और नोटेशन की समीक्षा"),
    "1.2": ("Linear Equations & Graphing", "रैखिक समीकरण और रेखांकन"),
    "1.3": ("Systems of Linear Equations", "रैखिक समीकरणों की प्रणालियाँ"),
    "1.4": ("Solving Systems by Substitution", "प्रतिस्थापन द्वारा सिस्टम को हल करना"),
    "1.5": ("Solving Systems by Elimination", "उन्मूलन द्वारा सिस्टम को हल करना"),
    "1.6": ("Applications of Linear Systems", "रैखिक प्रणालियों के अनुप्रयोग"),
    "1.7": ("Inequalities & System of Inequalities", "असमानताएँ और असमानताओं की प्रणाली"),
    "1.8": ("Linear Programming", "रैखिक प्रोग्रामिंग"),
    "1.9": ("Advanced Linear Applications", "उन्नत रैखिक अनुप्रयोग"),
    "2.1": ("Quadratic Functions & Parabolas", "द्विघात फलन और परवलय"),
    "2.2": ("Transformations of Quadratics", "द्विघात का रूपांतरण"),
    "2.3": ("Completing the Square", "वर्ग को पूरा करना"),
    "2.4": ("Quadratic Formula & Discriminant", "द्विघात सूत्र और विवेचक"),
    "2.5": ("Graphing Quadratic Functions", "द्विघात कार्यों का रेखांकन"),
    "2.6": ("Applications of Quadratics", "द्विघात के अनुप्रयोग"),
    "2.7": ("Quadratic Inequalities", "द्विघात असमानताएँ"),
    "3.1": ("Polynomial Operations", "बहुपद संक्रियाएँ"),
    "3.2": ("Factoring Polynomials", "बहुपद का गुणनखंडन"),
    "3.3": ("Synthetic Division", "कृत्रिम विभाजन"),
    "3.4": ("Polynomial Graphs & Zeros", "बहुपद रेखांकन और शून्य"),
    "3.5": ("Remainder & Factor Theorems", "शेषफल और गुणनखंड प्रमेय"),
    "3.6": ("Complex Numbers & Polynomial Roots", "जटिल संख्याएँ और बहुपद के मूल"),
    "3.7": ("Higher-Degree Polynomials", "उच्च अंश के बहुपद"),
    "4.1": ("Rational Expressions", "परिमेय व्यंजक"),
    "4.2": ("Operations on Rational Expressions", "परिमेय व्यंजक पर संक्रियाएँ"),
    "4.3": ("Rational Equations", "परिमेय समीकरण"),
    "4.4": ("Graphing Rational Functions", "परिमेय कार्यों का रेखांकन"),
    "4.5": ("Asymptotes & Discontinuities", "स्पर्शोन्मुख और असंततता"),
    "4.6": ("Applications of Rational Functions", "परिमेय कार्यों के अनुप्रयोग"),
    "5.1": ("Exponential Functions & Growth", "घातांकीय कार्य और वृद्धि"),
    "5.2": ("Exponential Decay & Applications", "घातांकीय क्षय और अनुप्रयोग"),
    "5.3": ("Logarithms & Properties", "लॉगरिदम और गुण"),
    "5.4": ("Logarithmic Functions & Graphs", "लॉगरिदमिक कार्य और रेखांकन"),
    "5.5": ("Exponential & Logarithmic Equations", "घातांकीय और लॉगरिदमिक समीकरण"),
    "5.6": ("Applications of Exponentials & Logs", "घातांकीय और लॉगरिदम के अनुप्रयोग"),
    "5.7": ("Natural Logarithms & e", "प्राकृतिक लॉगरिदम और e"),
    "6.1": ("Arithmetic Sequences", "अंकगणितीय अनुक्रम"),
    "6.2": ("Geometric Sequences", "ज्यामितीय अनुक्रम"),
    "6.3": ("Series & Summation Notation", "श्रृंखला और समीकरण संकेतन"),
    "6.4": ("Infinite Geometric Series", "अनंत ज्यामितीय श्रृंखला"),
    "6.5": ("Applications & Mathematical Induction", "अनुप्रयोग और गणितीय प्रेरण"),
    "7.1": ("Counting Principles", "गणना सिद्धांत"),
    "7.2": ("Permutations & Combinations", "क्रमचय और संयोजन"),
    "7.3": ("Probability Basics & Events", "संभाव्यता मूलभूत सिद्धांत और घटनाएँ"),
    "7.4": ("Conditional Probability", "सशर्त संभाव्यता"),
    "7.5": ("Normal Distributions", "सामान्य वितरण"),
    "7.6": ("Hypothesis Testing & Confidence Intervals", "परिकल्पना परीक्षण और आत्मविश्वास अंतराल"),
    "7.7": ("Correlation & Linear Regression", "सहसंबंध और रैखिक प्रतिगमन"),
    "8.1": ("Angles & Angle Measures", "कोण और कोण माप"),
    "8.2": ("Unit Circle & Trigonometric Ratios", "इकाई वृत्त और त्रिकोणमितीय अनुपात"),
    "8.3": ("Graphs of Trigonometric Functions", "त्रिकोणमितीय कार्यों के रेखांकन"),
    "8.4": ("Trigonometric Identities", "त्रिकोणमितीय पहचान"),
    "8.5": ("Solving Trigonometric Equations", "त्रिकोणमितीय समीकरण को हल करना"),
    "8.6": ("Applications of Trigonometry", "त्रिकोणमिति के अनुप्रयोग"),
    "9.1": ("Conic Sections", "शांकव खंड"),
    "9.2": ("Parametric Equations", "पैरामीट्रिक समीकरण"),
    "9.3": ("Vectors & Vector Operations", "सदिश और सदिश संक्रियाएँ"),
    "9.4": ("Complex Numbers in Polar Form", "ध्रुवीय रूप में जटिल संख्याएँ"),
}

def find_missing_base_entries():
    """Find which base entries are missing from hindi_translations.js"""
    hindi_file = "ArisEdu Project Folder/scripts/hindi_translations.js"
    
    with open(hindi_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    missing = {}
    
    for lesson_id, (english_title, hindi_title) in ALGEBRA2_LESSONS.items():
        base_key = f"Lesson {lesson_id}: {english_title}"
        
        # Check if base entry exists (not Summary, not ⭐)
        if f'"{base_key}"' not in content:
            missing[base_key] = f"पाठ {lesson_id}: {hindi_title}"
    
    return missing

def add_missing_entries():
    """Add missing base entries to hindi_translations.js"""
    hindi_file = "ArisEdu Project Folder/scripts/hindi_translations.js"
    
    missing = find_missing_base_entries()
    
    if not missing:
        print("✅ All base entries present!")
        return 0
    
    with open(hindi_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add each missing entry
    for key, translation in missing.items():
        # Find insertion point
        insertion_point = content.rfind('};')
        
        if insertion_point != -1:
            new_entry = f'\n    "{key}": "{translation}",'
            content = content[:insertion_point] + new_entry + content[insertion_point:]
    
    # Write back
    with open(hindi_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Added {len(missing)} missing base lesson translations:")
    for key in sorted(missing.keys()):
        print(f"   - {key}")
    
    return len(missing)

if __name__ == "__main__":
    count = add_missing_entries()
