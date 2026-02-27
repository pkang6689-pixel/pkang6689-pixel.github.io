#!/usr/bin/env python3
"""
Fix all remaining corrupted Chinese translations
"""

# All entries that still have the corrupted format and need fixing
REMAINING_FIXES = [
    # Unit 1
    ("Lesson 1.4: Solving Systems by Substitution - Summary", "第1.4课：用代入法求解系统 - 总结"),
    ("Lesson 1.5: Solving Systems by Elimination - Summary", "第1.5课：用消元法求解系统 - 总结"),
    ("Lesson 1.6: Applications of Linear Systems - Summary", "第1.6课：线性系统的应用 - 总结"),
    ("Lesson 1.7: Inequalities & System of Inequalities - Summary", "第1.7课：不等式和不等式系统 - 总结"),
    ("Lesson 1.8: Linear Programming - Summary", "第1.8课：线性规划 - 总结"),
    ("Lesson 1.9: Advanced Linear Applications - Summary", "第1.9课：高级线性应用 - 总结"),
    # Unit 2
    ("Lesson 2.7: Quadratic Inequalities - Summary", "第2.7课：二次不等式 - 总结"),
    # Unit 3
    ("Lesson 3.7: Higher-Degree Polynomials - Summary", "第3.7课：高次多项式 - 总结"),
    # Unit 4
    ("Lesson 4.6: Applications of Rational Functions ⭐", "第4.6课：有理函数的应用"),
]

def fix_remaining():
    """Fix remaining corrupted entries"""
    filepath = "ArisEdu Project Folder/scripts/global_translations.js"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixed = 0
    for english_key, correct_chinese in REMAINING_FIXES:
        # Find the line with this key
        import re
        pattern = f'    "{re.escape(english_key)}": "[^"]*"(,)?'
        
        match = re.search(pattern, content)
        if match:
            old_text = match.group(0)
            comma = "," if old_text.endswith(",") else ""
            new_text = f'    "{english_key}": "{correct_chinese}"{comma}'
            
            content = content.replace(old_text, new_text, 1)
            fixed += 1
            print(f"✓ Fixed: {english_key[:50]}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Fixed {fixed}/{len(REMAINING_FIXES)} remaining entries")

if __name__ == "__main__":
    fix_remaining()
