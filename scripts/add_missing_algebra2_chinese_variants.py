#!/usr/bin/env python3
"""
Add missing Algebra 2 Summary and variant Chinese translations
"""

# Base lessons that need Summary, Quiz, Practice variants (Chinese)
BASE_LESSONS_CHINESE = {
    "1.1": ("Review of Functions & Notation", "函数和符号复习"),
    "1.2": ("Linear Equations & Graphing", "线性方程和图形"),
    "1.3": ("Systems of Linear Equations", "线性方程组"),
    "1.4": ("Solving Systems by Substitution", "用代入法解系统"),
    "1.5": ("Solving Systems by Elimination", "用消元法解系统"),
    "1.6": ("Applications of Linear Systems", "线性系统的应用"),
    "1.7": ("Inequalities & System of Inequalities", "不等式和不等式系统"),
    "1.8": ("Linear Programming", "线性规划"),
    "1.9": ("Advanced Linear Applications", "高级线性应用"),
    "2.1": ("Quadratic Functions & Parabolas", "二次函数和抛物线"),
    "2.2": ("Transformations of Quadratics", "二次函数的变换"),
    "2.3": ("Completing the Square", "配方法"),
    "2.4": ("Quadratic Formula & Discriminant", "二次公式和判别式"),
    "2.5": ("Graphing Quadratic Functions", "二次函数的图形"),
    "2.6": ("Applications of Quadratics", "二次的应用"),
    "2.7": ("Quadratic Inequalities", "二次不等式"),
    "3.1": ("Polynomial Operations", "多项式运算"),
    "3.2": ("Factoring Polynomials", "多项式的因式分解"),
    "3.3": ("Synthetic Division", "综合除法"),
    "3.4": ("Polynomial Graphs & Zeros", "多项式图形和零点"),
    "3.5": ("Remainder & Factor Theorems", "余数定理和因子定理"),
    "3.6": ("Complex Numbers & Polynomial Roots", "复数和多项式根"),
    "3.7": ("Higher-Degree Polynomials", "高次多项式"),
    "4.1": ("Rational Expressions", "有理表达式"),
    "4.2": ("Operations on Rational Expressions", "有理表达式的运算"),
    "4.3": ("Rational Equations", "有理方程"),
    "4.4": ("Graphing Rational Functions", "有理函数的图形"),
    "4.5": ("Asymptotes & Discontinuities", "渐近线和不连续性"),
    "4.6": ("Applications of Rational Functions", "有理函数的应用"),
    "5.1": ("Exponential Functions & Growth", "指数函数和增长"),
    "5.2": ("Exponential Decay & Applications", "指数衰减和应用"),
    "5.3": ("Logarithms & Properties", "对数和性质"),
    "5.4": ("Logarithmic Functions & Graphs", "对数函数和图形"),
    "5.5": ("Exponential & Logarithmic Equations", "指数和对数方程"),
    "5.6": ("Applications of Exponentials & Logs", "指数和对数的应用"),
    "5.7": ("Natural Logarithms & e", "自然对数和e"),
    "6.1": ("Arithmetic Sequences", "等差数列"),
    "6.2": ("Geometric Sequences", "等比数列"),
    "6.3": ("Series & Summation Notation", "级数和求和记号"),
    "6.4": ("Infinite Geometric Series", "无穷几何级数"),
    "6.5": ("Applications & Mathematical Induction", "应用和数学归纳法"),
    "7.1": ("Counting Principles", "计数原理"),
    "7.2": ("Permutations & Combinations", "排列和组合"),
    "7.3": ("Probability Basics & Events", "概率基础和事件"),
    "7.4": ("Conditional Probability", "条件概率"),
    "7.5": ("Normal Distributions", "正态分布"),
    "7.6": ("Hypothesis Testing & Confidence Intervals", "假设检验和置信区间"),
    "7.7": ("Correlation & Linear Regression", "相关性和线性回归"),
    "8.1": ("Angles & Angle Measures", "角和角度量"),
    "8.2": ("Unit Circle & Trigonometric Ratios", "单位圆和三角比"),
    "8.3": ("Graphs of Trigonometric Functions", "三角函数的图形"),
    "8.4": ("Trigonometric Identities", "三角恒等式"),
    "8.5": ("Solving Trigonometric Equations", "解三角方程"),
    "8.6": ("Applications of Trigonometry", "三角学的应用"),
    "9.1": ("Conic Sections", "圆锥曲线"),
    "9.2": ("Parametric Equations", "参数方程"),
    "9.3": ("Vectors & Vector Operations", "向量和向量运算"),
    "9.4": ("Complex Numbers in Polar Form", "极坐标形式的复数"),
}

def add_chinese_variants():
    """Add Summary and Quiz/Practice variants (Chinese)"""
    chinese_file = "ArisEdu Project Folder/scripts/global_translations.js"
    
    with open(chinese_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    variants = {}
    
    # Generate Summary variants
    for lesson_id, (english, chinese) in BASE_LESSONS_CHINESE.items():
        key = f"Lesson {lesson_id}: {english} - Summary"
        value = f"第{lesson_id}课：{chinese} - 总结"
        variants[key] = value
        
        # Quiz and Practice
        key_quiz = f"Lesson {lesson_id}: {english} - Quiz"
        value_quiz = f"第{lesson_id}课：{chinese} - 测验"
        variants[key_quiz] = value_quiz
        
        key_practice = f"Lesson {lesson_id}: {english} - Practice"
        value_practice = f"第{lesson_id}课：{chinese} - 练习"
        variants[key_practice] = value_practice
    
    added_count = 0
    already_present = 0
    
    for key, translation in variants.items():
        if f'"{key}"' in content:
            already_present += 1
            continue
        
        insertion_point = content.rfind('};')
        if insertion_point != -1:
            new_entry = f'\n    "{key}": "{translation}",'
            content = content[:insertion_point] + new_entry + content[insertion_point:]
            added_count += 1
    
    with open(chinese_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Added {added_count} Simplified Chinese variant translations (Summary, Quiz, Practice)")
    print(f"⚠️  {already_present} translations already present")
    print(f"Total processed: {added_count + already_present}")

if __name__ == "__main__":
    add_chinese_variants()
