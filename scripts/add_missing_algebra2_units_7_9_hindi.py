#!/usr/bin/env python3
"""
Add missing Hindi translations for Algebra 2 Units 7, 8, 9 lessons
"""

import os
import re

# Algebra 2 Unit 7, 8, 9 lessons with Hindi translations
MISSING_TRANSLATIONS = {
    # Unit 7 - Probability & Statistics
    "Lesson 7.1: Counting Principles": "पाठ 7.1: गणना सिद्धांत",
    "Lesson 7.1: Counting Principles - Summary": "पाठ 7.1: गणना सिद्धांत - सारांश",
    "Lesson 7.2: Permutations & Combinations": "पाठ 7.2: क्रमचय और संयोजन",
    "Lesson 7.2: Permutations & Combinations - Summary": "पाठ 7.2: क्रमचय और संयोजन - सारांश",
    "Lesson 7.3: Probability Basics & Events": "पाठ 7.3: संभाव्यता मूलभूत सिद्धांत और घटनाएँ",
    "Lesson 7.3: Probability Basics & Events - Summary": "पाठ 7.3: संभाव्यता मूलभूत सिद्धांत और घटनाएँ - सारांश",
    "Lesson 7.4: Conditional Probability": "पाठ 7.4: सशर्त संभाव्यता",
    "Lesson 7.4: Conditional Probability - Summary": "पाठ 7.4: सशर्त संभाव्यता - सारांश",
    "Lesson 7.5: Normal Distributions": "पाठ 7.5: सामान्य वितरण",
    "Lesson 7.5: Normal Distributions - Summary": "पाठ 7.5: सामान्य वितरण - सारांश",
    "Lesson 7.6: Hypothesis Testing & Confidence Intervals": "पाठ 7.6: परिकल्पना परीक्षण और आत्मविश्वास अंतराल",
    "Lesson 7.6: Hypothesis Testing & Confidence Intervals - Summary": "पाठ 7.6: परिकल्पना परीक्षण और आत्मविश्वास अंतराल - सारांश",
    "Lesson 7.7: Correlation & Linear Regression": "पाठ 7.7: सहसंबंध और रैखिक प्रतिगमन",
    "Lesson 7.7: Correlation & Linear Regression - Summary": "पाठ 7.7: सहसंबंध और रैखिक प्रतिगमन - सारांश",
    
    # Unit 8 - Trigonometry
    "Lesson 8.1: Angles & Angle Measures": "पाठ 8.1: कोण और कोण माप",
    "Lesson 8.1: Angles & Angle Measures - Summary": "पाठ 8.1: कोण और कोण माप - सारांश",
    "Lesson 8.2: Unit Circle & Trigonometric Ratios": "पाठ 8.2: इकाई वृत्त और त्रिकोणमितीय अनुपात",
    "Lesson 8.2: Unit Circle & Trigonometric Ratios - Summary": "पाठ 8.2: इकाई वृत्त और त्रिकोणमितीय अनुपात - सारांश",
    "Lesson 8.3: Graphs of Trigonometric Functions": "पाठ 8.3: त्रिकोणमितीय कार्यों के रेखांकन",
    "Lesson 8.3: Graphs of Trigonometric Functions - Summary": "पाठ 8.3: त्रिकोणमितीय कार्यों के रेखांकन - सारांश",
    "Lesson 8.4: Trigonometric Identities": "पाठ 8.4: त्रिकोणमितीय पहचान",
    "Lesson 8.4: Trigonometric Identities - Summary": "पाठ 8.4: त्रिकोणमितीय पहचान - सारांश",
    "Lesson 8.5: Solving Trigonometric Equations": "पाठ 8.5: त्रिकोणमितीय समीकरण को हल करना",
    "Lesson 8.5: Solving Trigonometric Equations - Summary": "पाठ 8.5: त्रिकोणमितीय समीकरण को हल करना - सारांश",
    "Lesson 8.6: Applications of Trigonometry": "पाठ 8.6: त्रिकोणमिति के अनुप्रयोग",
    "Lesson 8.6: Applications of Trigonometry - Summary": "पाठ 8.6: त्रिकोणमिति के अनुप्रयोग - सारांश",
    
    # Unit 9 - Advanced Topics
    "Lesson 9.1: Conic Sections": "पाठ 9.1: शांकव खंड",
    "Lesson 9.1: Conic Sections - Summary": "पाठ 9.1: शांकव खंड - सारांश",
    "Lesson 9.2: Parametric Equations": "पाठ 9.2: पैरामीट्रिक समीकरण",
    "Lesson 9.2: Parametric Equations - Summary": "पाठ 9.2: पैरामीट्रिक समीकरण - सारांश",
    "Lesson 9.3: Vectors & Vector Operations": "पाठ 9.3: सदिश और सदिश संक्रियाएँ",
    "Lesson 9.3: Vectors & Vector Operations - Summary": "पाठ 9.3: सदिश और सदिश संक्रियाएँ - सारांश",
    "Lesson 9.4: Complex Numbers in Polar Form": "पाठ 9.4: ध्रुवीय रूप में जटिल संख्याएँ",
    "Lesson 9.4: Complex Numbers in Polar Form - Summary": "पाठ 9.4: ध्रुवीय रूप में जटिल संख्याएँ - सारांश",
}

def add_translations():
    """Add missing translations to hindi_translations.js"""
    hindi_file = "ArisEdu Project Folder/scripts/hindi_translations.js"
    
    with open(hindi_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count how many we successfully add
    added_count = 0
    already_present = 0
    
    for key, translation in MISSING_TRANSLATIONS.items():
        # Check if already exists
        if f'"{key}"' in content:
            already_present += 1
            continue
        
        # Find a good insertion point - add before the closing brace of the translations object
        # We'll add before the last closing }; of the main translations object
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
    
    print(f"✅ Added {added_count} new Hindi translations for Algebra 2 Units 7-9")
    print(f"⚠️  {already_present} translations already present")
    print(f"Total processed: {added_count + already_present}")

if __name__ == "__main__":
    add_translations()
