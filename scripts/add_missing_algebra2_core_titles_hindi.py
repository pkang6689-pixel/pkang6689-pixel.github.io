#!/usr/bin/env python3
"""
Add missing core title Hindi translations for Algebra 2 Units 7, 8, 9 lessons
"""

import os
import re

# Core titles (without "Lesson X.X:") for fallback translation
MISSING_CORE_TITLES = {
    # Unit 7
    "Counting Principles": "गणना सिद्धांत",
    "Permutations & Combinations": "क्रमचय और संयोजन",
    "Probability Basics & Events": "संभाव्यता मूलभूत सिद्धांत और घटनाएँ",
    "Conditional Probability": "सशर्त संभाव्यता",
    "Normal Distributions": "सामान्य वितरण",
    "Hypothesis Testing & Confidence Intervals": "परिकल्पना परीक्षण और आत्मविश्वास अंतराल",
    "Correlation & Linear Regression": "सहसंबंध और रैखिक प्रतिगमन",
    
    # Unit 8
    "Angles & Angle Measures": "कोण और कोण माप",
    "Unit Circle & Trigonometric Ratios": "इकाई वृत्त और त्रिकोणमितीय अनुपात",
    "Graphs of Trigonometric Functions": "त्रिकोणमितीय कार्यों के रेखांकन",
    "Trigonometric Identities": "त्रिकोणमितीय पहचान",
    "Solving Trigonometric Equations": "त्रिकोणमितीय समीकरण को हल करना",
    "Applications of Trigonometry": "त्रिकोणमिति के अनुप्रयोग",
    
    # Unit 9
    "Conic Sections": "शांकव खंड",
    "Parametric Equations": "पैरामीट्रिक समीकरण",
    "Vectors & Vector Operations": "सदिश और सदिश संक्रियाएँ",
    "Complex Numbers in Polar Form": "ध्रुवीय रूप में जटिल संख्याएँ",
}

def add_translations():
    """Add missing core title translations to hindi_translations.js"""
    hindi_file = "ArisEdu Project Folder/scripts/hindi_translations.js"
    
    with open(hindi_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count how many we successfully add
    added_count = 0
    already_present = 0
    
    for key, translation in MISSING_CORE_TITLES.items():
        # Check if already exists
        if f'"{key}"' in content:
            already_present += 1
            continue
        
        # Find a good insertion point - add before the closing brace of the translations object
        insertion_point = content.rfind('};')
        
        if insertion_point != -1:
            # Create the new entry
            new_entry = f'\n    "{key}": "{translation}",'
            
            # Insert it
            content = content[:insertion_point] + new_entry + content[insertion_point:]
            added_count += 1
    
    # Write back
    with open(hindi_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Added {added_count} core title Hindi translations for Algebra 2 Units 7-9")
    print(f"⚠️  {already_present} translations already present")
    print(f"Total processed: {added_count + already_present}")

if __name__ == "__main__":
    add_translations()
