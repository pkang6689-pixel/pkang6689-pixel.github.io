#!/usr/bin/env python3
"""
Comprehensively fix ALL corrupted Chinese translations in Algebra 2
"""

import re
import os

# All correct Chinese mappings for Algebra 2
ALGEBRA2_TRANSLATIONS = {
    # Unit 1
    "Lesson 1.1: Review of Functions & Notation": "第1.1课：函数和符号复习",
    "Lesson 1.2: Linear Equations & Graphing": "第1.2课：线性方程和图形",
    "Lesson 1.3: Systems of Linear Equations": "第1.3课：线性方程组",
    "Lesson 1.4: Solving Systems by Substitution & Elimination": "第1.4课：用代入法和消元法求解系统",
    "Lesson 1.5: Graphing Systems & Applications": "第1.5课：用图表表示系统和应用",
    "Lesson 1.6: Linear Inequalities & Systems": "第1.6课：线性不等式和系统",
    "Lesson 1.7: Absolute Value Equations & Inequalities": "第1.7课：绝对值方程和不等式",
    "Lesson 1.8: Piecewise Functions": "第1.8课：分段函数",
    "Lesson 1.9: Advanced Linear Applications ⭐": "第1.9课：高级线性应用",
    # Unit 2
    "Lesson 2.1: Quadratic Functions & Parabolas": "第2.1课：二次函数和抛物线",
    "Lesson 2.2: Transformations of Quadratics": "第2.2课：二次函数的变换",
    "Lesson 2.3: Completing the Square": "第2.3课：配方法",
    "Lesson 2.4: Quadratic Formula & Discriminant": "第2.4课：二次公式和判别式",
    "Lesson 2.5: Graphing Quadratic Functions": "第2.5课：二次函数的图形",
    "Lesson 2.6: Applications of Quadratics": "第2.6课：二次的应用",
    "Lesson 2.7: Quadratic Inequalities ⭐": "第2.7课：二次不等式",
    # Unit 3
    "Lesson 3.1: Polynomial Operations": "第3.1课：多项式运算",
    "Lesson 3.2: Factoring Polynomials": "第3.2课：多项式的因式分解",
    "Lesson 3.3: Synthetic Division": "第3.3课：综合除法",
    "Lesson 3.4: Polynomial Graphs & Zeros": "第3.4课：多项式图形和零点",
    "Lesson 3.5: Remainder & Factor Theorems": "第3.5课：余数定理和因子定理",
    "Lesson 3.6: Complex Numbers & Polynomial Roots": "第3.6课：复数和多项式根",
    "Lesson 3.7: Higher-Degree Polynomials ⭐": "第3.7课：高次多项式",
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

def fix_corrupted_translations():
    """Fix all corrupted Chinese translations"""
    filepath = "ArisEdu Project Folder/scripts/global_translations.js"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixed_count = 0
    errors = []
    
    # Fix base lessons (not Summary, Quiz, or Practice)
    for english_key, correct_chinese in ALGEBRA2_TRANSLATIONS.items():
        # Skip if this is already a special variant
        if " - " in english_key:
            continue
        
        # Find the base lesson line
        pattern = f'    "{re.escape(english_key)}": "[^"]*"(,)?'
        matches = list(re.finditer(pattern, content))
        
        if matches:
            match = matches[0]
            old_text = match.group(0)
            # Preserve the comma if it was there
            comma = "," if old_text.endswith(",") else ""
            new_text = f'    "{english_key}": "{correct_chinese}"{comma}'
            
            if content.replace(old_text, new_text, 1) != content:
                content = content.replace(old_text, new_text, 1)
                fixed_count += 1
                print(f"✓ Fixed base: {english_key}")
            else:
                errors.append(f"Could not replace base: {english_key}")
    
    # Fix Summary variants
    for english_key, correct_chinese in ALGEBRA2_TRANSLATIONS.items():
        if " - " in english_key:
            continue
        
        summary_key = f"{english_key} - Summary"
        summary_chinese = f"{correct_chinese} - 总结"
        
        # Find any line with the English key
        pattern = f'    "{re.escape(summary_key)}": "[^"]*"(,)?'
        matches = list(re.finditer(pattern, content))
        
        if matches:
            match = matches[0]
            old_text = match.group(0)
            comma = "," if old_text.endswith(",") else ""
            new_text = f'    "{summary_key}": "{summary_chinese}"{comma}'
            
            if content.replace(old_text, new_text, 1) != content:
                content = content.replace(old_text, new_text, 1)
                fixed_count += 1
                print(f"✓ Fixed summary: {summary_key}")
            else:
                errors.append(f"Could not replace summary: {summary_key}")
    
    # Write back the fixed content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Successfully fixed {fixed_count} translations")
    if errors:
        print(f"\n⚠️ {len(errors)} entries had issues:")
        for error in errors[:5]:  # Show first 5
            print(f"  - {error}")

if __name__ == "__main__":
    fix_corrupted_translations()
