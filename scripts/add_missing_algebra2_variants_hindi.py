#!/usr/bin/env python3
"""
Add missing variant Hindi translations (Quiz, Practice) for Algebra 2 Units 7, 8, 9 lessons
"""

import os

# Lessons that need Quiz and Practice variants
BASE_LESSONS_7_9 = {
    "7.1": ("Counting Principles", "पाठ 7.1: गणना सिद्धांत"),
    "7.2": ("Permutations & Combinations", "पाठ 7.2: क्रमचय और संयोजन"),
    "7.3": ("Probability Basics & Events", "पाठ 7.3: संभाव्यता मूलभूत सिद्धांत और घटनाएँ"),
    "7.4": ("Conditional Probability", "पाठ 7.4: सशर्त संभाव्यता"),
    "7.5": ("Normal Distributions", "पाठ 7.5: सामान्य वितरण"),
    "7.6": ("Hypothesis Testing & Confidence Intervals", "पाठ 7.6: परिकल्पना परीक्षण और आत्मविश्वास अंतराल"),
    "7.7": ("Correlation & Linear Regression", "पाठ 7.7: सहसंबंध और रैखिक प्रतिगमन"),
    "8.1": ("Angles & Angle Measures", "पाठ 8.1: कोण और कोण माप"),
    "8.2": ("Unit Circle & Trigonometric Ratios", "पाठ 8.2: इकाई वृत्त और त्रिकोणमितीय अनुपात"),
    "8.3": ("Graphs of Trigonometric Functions", "पाठ 8.3: त्रिकोणमितीय कार्यों के रेखांकन"),
    "8.4": ("Trigonometric Identities", "पाठ 8.4: त्रिकोणमितीय पहचान"),
    "8.5": ("Solving Trigonometric Equations", "पाठ 8.5: त्रिकोणमितीय समीकरण को हल करना"),
    "8.6": ("Applications of Trigonometry", "पाठ 8.6: त्रिकोणमिति के अनुप्रयोग"),
    "9.1": ("Conic Sections", "पाठ 9.1: शांकव खंड"),
    "9.2": ("Parametric Equations", "पाठ 9.2: पैरामीट्रिक समीकरण"),
    "9.3": ("Vectors & Vector Operations", "पाठ 9.3: सदिश और सदिश संक्रियाएँ"),
    "9.4": ("Complex Numbers in Polar Form", "पाठ 9.4: ध्रुवीय रूप में जटिल संख्याएँ"),
}

VARIANTS = ["Quiz", "Practice"]

def generate_variants():
    """Generate all Quiz and Practice variants"""
    variants_dict = {}
    
    for lesson_id, (english_title, hindi_title) in BASE_LESSONS_7_9.items():
        for variant in VARIANTS:
            # Create key for lesson variant
            key = f"Lesson {lesson_id}: {english_title} - {variant}"
            
            # Create hindi translation (suffix variant with Hindi word)
            hindi_variant_title = hindi_title.replace(f"पाठ {lesson_id.split('.')[0]}.", f"पाठ {lesson_id.split('.')[0]}.")
            if variant == "Quiz":
                hindi_value = hindi_variant_title.replace("पाठ", "पाठ").replace(":", f": {variant} -") if " - " not in hindi_variant_title else hindi_variant_title
                # Better: use consistent pattern
                hindi_value = hindi_title + " - प्रश्नोत्तरी"
            else:  # Practice
                hindi_value = hindi_title + " - अभ्यास"
            
            variants_dict[key] = hindi_value
    
    return variants_dict

def add_variants():
    """Add variant translations to hindi_translations.js"""
    hindi_file = "ArisEdu Project Folder/scripts/hindi_translations.js"
    
    variants_dict = generate_variants()
    
    with open(hindi_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count how many we successfully add
    added_count = 0
    already_present = 0
    
    for key, translation in variants_dict.items():
        # Check if already exists
        if f'"{key}"' in content:
            already_present += 1
            continue
        
        # Find insertion point
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
    
    print(f"✅ Added {added_count} Quiz and Practice variant translations for Algebra 2 Units 7-9")
    print(f"⚠️  {already_present} translations already present")
    print(f"Total processed: {added_count + already_present}")
    print(f"Variant types added: Quiz, Practice")

if __name__ == "__main__":
    add_variants()
