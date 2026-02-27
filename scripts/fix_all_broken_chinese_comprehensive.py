#!/usr/bin/env python3
"""
Comprehensively fix all broken Algebra 2 Chinese translations
"""

import re

CORRECT_MAPPINGS = {
    # Unit 2
    "Lesson 2.3: Completing the Square": "第2.3课：配方法",
    "Lesson 2.4: Quadratic Formula & Discriminant": "第2.4课：二次公式和判别式",
    "Lesson 2.5: Graphing Quadratic Functions": "第2.5课：二次函数的图形",
    "Lesson 2.6: Applications of Quadratics": "第2.6课：二次的应用",
    # Unit 3
    "Lesson 3.1: Polynomial Operations": "第3.1课：多项式运算",
    "Lesson 3.2: Factoring Polynomials": "第3.2课：多项式的因式分解",
    "Lesson 3.3: Synthetic Division": "第3.3课：综合除法",
    "Lesson 3.4: Polynomial Graphs & Zeros": "第3.4课：多项式图形和零点",
    "Lesson 3.5: Remainder & Factor Theorems": "第3.5课：余数定理和因子定理",
    "Lesson 3.6: Complex Numbers & Polynomial Roots": "第3.6课：复数和多项式根",
    # Unit 4
    "Lesson 4.1: Rational Expressions": "第4.1课：有理表达式",
    "Lesson 4.2: Operations on Rational Expressions": "第4.2课：有理表达式的运算",
    "Lesson 4.3: Rational Equations": "第4.3课：有理方程",
    "Lesson 4.4: Graphing Rational Functions": "第4.4课：有理函数的图形",
    "Lesson 4.5: Asymptotes & Discontinuities": "第4.5课：渐近线和不连续性",
    "Lesson 4.6: Applications of Rational Functions": "第4.6课：有理函数的应用",
    # Unit 5
    "Lesson 5.1: Exponential Functions & Growth": "第5.1课：指数函数和增长",
    "Lesson 5.2: Exponential Decay & Applications": "第5.2课：指数衰减和应用",
    "Lesson 5.3: Logarithms & Properties": "第5.3课：对数和性质",
    "Lesson 5.4: Logarithmic Functions & Graphs": "第5.4课：对数函数和图形",
    "Lesson 5.5: Exponential & Logarithmic Equations": "第5.5课：指数和对数方程",
    "Lesson 5.6: Applications of Exponentials & Logs": "第5.6课：指数和对数的应用",
    # Unit 6
    "Lesson 6.1: Arithmetic Sequences": "第6.1课：等差数列",
    "Lesson 6.2: Geometric Sequences": "第6.2课：等比数列",
    "Lesson 6.3: Series & Summation Notation": "第6.3课：级数和求和记号",
    "Lesson 6.4: Infinite Geometric Series": "第6.4课：无穷几何级数",
    "Lesson 6.5: Applications & Mathematical Induction": "第6.5课：应用和数学归纳法",
}

def fix_all_chinese():
    """Fix all broken Chinese translations at once"""
    chinese_file = "ArisEdu Project Folder/scripts/global_translations.js"
    
    with open(chinese_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixed_count = 0
    
    for english_key, correct_chinese in CORRECT_MAPPINGS.items():
        # Use regex to find and replace any broken version
        # Looking for the key followed by any translation value
        pattern = f'        "{re.escape(english_key)}": "[^"]*",'
        
        matches = list(re.finditer(pattern, content))
        if matches:
            match = matches[0]
            old_text = match.group(0)
            new_text = f'        "{english_key}": "{correct_chinese}",'
            
            # Only replace if the old translation looks bad (contains course/课程 pattern)
            if '课程' in old_text and ('Review' in old_text or 'Quadratic' in old_text or 'Linear' in old_text or 
                                       'Rational' in old_text or 'Exponential' in old_text or 'Series' in old_text or
                                       'Arithmetic' in old_text or 'Geometric' in  old_text or 'Polynomial' in old_text):
                content = content.replace(old_text, new_text, 1)
                fixed_count += 1
                print(f"✓ Fixed: {english_key}")
    
    with open(chinese_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Fixed {fixed_count} Chinese translations")

if __name__ == "__main__":
    fix_all_chinese()
