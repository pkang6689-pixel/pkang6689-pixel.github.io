#!/usr/bin/env python3
"""
Generate and add Hindi translations for all missing Algebra 2 lessons.
Creates translations for base lessons, Quiz, Summary, and Practice variations.
"""

import os
import re

# Base lesson translations
ALGEBRA2_BASE_LESSONS = {
    # Unit 1
    "Lesson 1.1: Review of Functions & Notation": "पाठ 1.1: फ़ंक्शंस और नोटेशन की समीक्षा",
    "Lesson 1.2: Linear Equations & Graphing": "पाठ 1.2: रैखिक समीकरण और रेखांकन",
    "Lesson 1.3: Systems of Linear Equations": "पाठ 1.3: रैखिक समीकरणों की प्रणालियाँ",
    "Lesson 1.4: Transformations of Functions": "पाठ 1.4: कार्यों के रूपांतरण",
    "Lesson 1.5: Inverse Functions": "पाठ 1.5: व्युत्क्रम कार्य",
    "Lesson 1.6: Piecewise Functions & Absolute Value": "पाठ 1.6: अংशबद्ध कार्य और निरपेक्ष मान",
    "Lesson 1.7: Quadratic Functions & Transformations": "पाठ 1.7: द्विघात कार्य और रूपांतरण",
    "Lesson 1.8: Complex Numbers": "पाठ 1.8: सम्मिश्र संख्याएं",
    
    # Unit 2
    "Lesson 2.1: Polynomial Functions": "पाठ 2.1: बहुपद कार्य",
    "Lesson 2.2: Polynomial Operations": "पाठ 2.2: बहुपद संक्रियाएं",
    "Lesson 2.3: Polynomial Division": "पाठ 2.3: बहुपद विभाजन",
    "Lesson 2.4: Zeros of Polynomials": "पाठ 2.4: बहुपद के शून्य",
    "Lesson 2.5: Graphing Polynomials": "पाठ 2.5: बहुपदों को ग्राफ करना",
    "Lesson 2.6: Polynomial Applications": "पाठ 2.6: बहुपद के अनुप्रयोग",
    
    # Unit 3
    "Lesson 3.1: Polynomial Basics": "पाठ 3.1: बहुपद मूल बातें",
    "Lesson 3.2: Polynomial Operations & Factoring": "पाठ 3.2: बहुपद संक्रियाएं और गुणनखंडन",
    
    # Unit 4
    "Lesson 4.7: Inverse Functions": "पाठ 4.7: व्युत्क्रम कार्य",
    
    # Unit 6
    "Lesson 6.5: Applications & Mathematical Induction": "पाठ 6.5: अनुप्रयोग और गणितीय प्रेरण",
}

def generate_variation_translations():
    """Generate the Quiz, Summary, and Practice variations."""
    variations = {}
    
    for base_title, base_hindi in ALGEBRA2_BASE_LESSONS.items():
        # Quiz version: "Lesson X.X: Title - Quiz"
        quiz_title = base_title.replace("Lesson ", "Lesson ").replace(":", ":") + " - Quiz"
        quiz_hindi = base_hindi + " - प्रश्नोत्तरी"
        
        # Summary version
        summary_title = base_title + " - Summary"
        summary_hindi = base_hindi + " - सारांश"
        
        # Practice version  
        practice_title = base_title + " Practice"
        practice_hindi = base_hindi + " अभ्यास"
        
        variations[quiz_title] = quiz_hindi
        variations[summary_title] = summary_hindi
        variations[practice_title] = practice_hindi
    
    return {**ALGEBRA2_BASE_LESSONS, **variations}

def add_missing_translations():
    """Add missing translations to the Hindi file."""
    trans_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'ArisEdu Project Folder', 'scripts', 'hindi_translations.js'
    )
    
    with open(trans_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    all_translations = generate_variation_translations()
    added_count = 0
    skipped_count = 0
    
    for english_title, hindi_title in all_translations.items():
        # Check if this translation already exists in the file
        pattern = f'"{english_title}":'
        
        if pattern in content:
            skipped_count += 1
        else:
            # Find insertion point: before the last lines with translations
            # Look for the last occurrence of "...", before the closing }
            
            # For safety, we'll add right before the very last closing bracket
            insert_pos = content.rfind('\n};')
            if insert_pos > 0:
                # Add the new translation
                new_entry = f'    "{english_title}": "{hindi_title}",\n'
                content = content[:insert_pos] + '\n' + new_entry + content[insert_pos:]
                added_count += 1
                print(f"✓ Added: {english_title}")
    
    # Write back
    with open(trans_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n{'='*60}")
    print(f"Added {added_count} new translations")
    print(f"Skipped {skipped_count} existing translations")
    print(f"{'='*60}")

if __name__ == '__main__':
    add_missing_translations()
