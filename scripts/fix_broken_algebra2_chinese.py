#!/usr/bin/env python3
"""
Fix broken Algebra 2 Chinese translations in global_translations.js
"""

# Correct mappings for all Algebra 2 lessons (English -> proper Chinese)
FIXES = {
    # Unit 1
    "Lesson 1.1: Review of Functions & Notation": "第1.1课：函数和符号复习",
    "Lesson 1.2: Linear Equations & Graphing": "第1.2课：线性方程和图形",
    "Lesson 1.3: Systems of Linear Equations": "第1.3课：线性方程组",
    "Lesson 1.4: Solving Systems by Substitution": "第1.4课：用代入法解系统",
    "Lesson 1.5: Solving Systems by Elimination": "第1.5课：用消元法解系统",
    "Lesson 1.6: Applications of Linear Systems": "第1.6课：线性系统的应用",
    "Lesson 1.7: Inequalities & System of Inequalities": "第1.7课：不等式和不等式系统",
    "Lesson 1.8: Linear Programming": "第1.8课：线性规划",
    "Lesson 1.9: Advanced Linear Applications": "第1.9课：高级线性应用",
    # Unit 2
    "Lesson 2.1: Quadratic Functions & Parabolas": "第2.1课：二次函数和抛物线",
    "Lesson 2.2: Transformations of Quadratics": "第2.2课：二次函数的变换",
    "Lesson 2.3: Completing the Square": "第2.3课：配方法",
    "Lesson 2.4: Quadratic Formula & Discriminant": "第2.4课：二次公式和判别式",
    "Lesson 2.5: Graphing Quadratic Functions": "第2.5课：二次函数的图形",
    "Lesson 2.6: Applications of Quadratics": "第2.6课：二次的应用",
    "Lesson 2.7: Quadratic Inequalities": "第2.7课：二次不等式",
    # Unit 3
    "Lesson 3.1: Polynomial Operations": "第3.1课：多项式运算",
    "Lesson 3.2: Factoring Polynomials": "第3.2课：多项式的因式分解",
    "Lesson 3.3: Synthetic Division": "第3.3课：综合除法",
    "Lesson 3.4: Polynomial Graphs & Zeros": "第3.4课：多项式图形和零点",
    "Lesson 3.5: Remainder & Factor Theorems": "第3.5课：余数定理和因子定理",
    "Lesson 3.6: Complex Numbers & Polynomial Roots": "第3.6课：复数和多项式根",
    "Lesson 3.7: Higher-Degree Polynomials": "第3.7课：高次多项式",
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
    "Lesson 5.7: Natural Logarithms & e": "第5.7课：自然对数和e",
    # Unit 6
    "Lesson 6.1: Arithmetic Sequences": "第6.1课：等差数列",
    "Lesson 6.2: Geometric Sequences": "第6.2课：等比数列",
    "Lesson 6.3: Series & Summation Notation": "第6.3课：级数和求和记号",
    "Lesson 6.4: Infinite Geometric Series": "第6.4课：无穷几何级数",
    "Lesson 6.5: Applications & Mathematical Induction": "第6.5课：应用和数学归纳法",
    # Unit 7
    "Lesson 7.1: Counting Principles": "第7.1课：计数原理",
    "Lesson 7.2: Permutations & Combinations": "第7.2课：排列和组合",
    "Lesson 7.3: Probability Basics & Events": "第7.3课：概率基础和事件",
    "Lesson 7.4: Conditional Probability": "第7.4课：条件概率",
    "Lesson 7.5: Normal Distributions": "第7.5课：正态分布",
    "Lesson 7.6: Hypothesis Testing & Confidence Intervals": "第7.6课：假设检验和置信区间",
    "Lesson 7.7: Correlation & Linear Regression": "第7.7课：相关性和线性回归",
    # Unit 8
    "Lesson 8.1: Angles & Angle Measures": "第8.1课：角和角度量",
    "Lesson 8.2: Unit Circle & Trigonometric Ratios": "第8.2课：单位圆和三角比",
    "Lesson 8.3: Graphs of Trigonometric Functions": "第8.3课：三角函数的图形",
    "Lesson 8.4: Trigonometric Identities": "第8.4课：三角恒等式",
    "Lesson 8.5: Solving Trigonometric Equations": "第8.5课：解三角方程",
    "Lesson 8.6: Applications of Trigonometry": "第8.6课：三角学的应用",
    # Unit 9
    "Lesson 9.1: Conic Sections": "第9.1课：圆锥曲线",
    "Lesson 9.2: Parametric Equations": "第9.2课：参数方程",
    "Lesson 9.3: Vectors & Vector Operations": "第9.3课：向量和向量运算",
    "Lesson 9.4: Complex Numbers in Polar Form": "第9.4课：极坐标形式的复数",
}

def fix_chinese_translations():
    """Fix all broken Algebra 2 Chinese translations"""
    chinese_file = "ArisEdu Project Folder/scripts/global_translations.js"
    
    with open(chinese_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixed_count = 0
    
    for english_key, proper_chinese in FIXES.items():
        # Find and replace the broken version
        # It might be with "课程" prefix or other mixed formats
        import re
        
        # Pattern: "Lesson X.X: ... ": "[some broken Chinese-English mix]"
        pattern = f'    "{re.escape(english_key)}": ".*?",'
        
        # Check if we can find this pattern
        match = re.search(pattern, content)
        if match:
            old_entry = match.group(0)
            new_entry = f'    "{english_key}": "{proper_chinese}",'
            
            # Only replace if it contains "课程" (the broken ones)
            if "课程" in old_entry and english_key not in old_entry.split('": "')[1]:
                # Found a broken translation (has 课程 but doesn't have the key text in translation)
                content = content.replace(old_entry, new_entry, 1)
                fixed_count += 1
                print(f"Fixed: {english_key}")
    
    with open(chinese_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Fixed {fixed_count} broken Algebra 2 Chinese translations")

if __name__ == "__main__":
    fix_chinese_translations()
