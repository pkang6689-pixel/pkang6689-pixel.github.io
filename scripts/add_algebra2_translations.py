#!/usr/bin/env python3
"""
Add Algebra 2 translations to global_translations.js
Uses a combination of predefined translations and pattern-based generation
"""
import os
import re

def read_global_translations(file_path):
    """Read the existing translations dictionary"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the translations object
    match = re.search(r'const translations = \{(.*)\};', content, re.DOTALL)
    if not match:
        return content, {}
    
    return content, {}

def create_comprehensive_algebra2_translations():
    """Create comprehensive Chinese translations for Algebra 2"""
    translations = {
        # ===== UNIT 1: FUNCTIONS =====
        "Review of Functions & Notation": "函数与记号复习",
        "Key Concepts: Review of Functions & Notation": "关键概念：函数与记号复习",
        "Functions are relations that assign exactly one output to each input. A function f(x) can be evaluated by substituting a value for x and simplifying.": "函数是将每个输入值分配到恰好一个输出值的关系。函数f(x)可以通过替换x值并简化来计算。",
        "Function Notation: f(x) represents the output of function f when the input is x. This replaces the older y = notation and makes it clear which variable is the input.": "函数记号：f(x)表示当输入为x时函数f的输出。这取代了旧的y=符号，并清楚地表明哪个变量是输入。",
        "Domain and Range: The domain is the set of all possible input values, while the range is the set of all possible output values. Restrictions occur when denominators are zero or when values are under even-root radicals.": "定义域和值域：定义域是所有可能输入值的集合，而值域是所有可能输出值的集合。当分母为零或值在偶次根号下时会发生限制。",
        "Operations with Functions: Functions can be combined through addition, subtraction, multiplication, and division. Composition of functions (f ∘ g)(x) = f(g(x)) means apply g first, then apply f to the result.": "函数运算：可以通过加法、减法、乘法和除法来组合函数。函数复合(f ∘ g)(x) = f(g(x))表示先应用g，然后对结果应用f。",
        "f(x) = 2x + 3, what is f(5)?": "f(x) = 2x + 3，求f(5)？",
        "f(5) = 13. Substitute x=5: f(5) = 2(5) + 3 = 10 + 3 = 13.": "f(5) = 13。代入x=5：f(5) = 2(5) + 3 = 10 + 3 = 13。",
        "What is the domain of f(x) = √(x - 4)?": "求f(x) = √(x - 4)的定义域？",
        "x ≥ 4. Radicand must be non-negative.": "x ≥ 4。被开方数必须非负。",
        "What is the range of f(x) = |x|?": "f(x) = |x|的值域是什么？",
        "y ≥ 0. Absolute value is always non-negative.": "y ≥ 0。绝对值总是非负的。",
        "Find (f ∘ g)(2) if f(x) = x² and g(x) = x + 1": "若f(x) = x²，g(x) = x + 1，求(f ∘ g)(2)",
        "9. (f ∘ g)(2) = f(g(2)) = f(3) = 9.": "9. (f ∘ g)(2) = f(g(2)) = f(3) = 9。",
        "What is f⁻¹(x) if f(x) = 2x - 5?": "若f(x) = 2x - 5，求f⁻¹(x)？",
        "f⁻¹(x) = (x + 5)/2. Swap x and y, solve for y.": "f⁻¹(x) = (x + 5)/2。交换x和y，解出y。",
        "Is f(x) = 3x + 2 one-to-one?": "f(x) = 3x + 2是一一对应的吗？",
        "Yes. Linear functions with non-zero slope are one-to-one. Passes horizontal line test.": "是。斜率非零的一次函数是一一对应的。满足水平线测试。",
        "Find f(f⁻¹(7)) for any function f": "对任何函数f求f(f⁻¹(7))",
        "7. Composing function with its inverse returns original input.": "7. 函数与其反函数复合返回原始输入。",
        "If f(2) = 5, what is the point on the graph?": "如果f(2) = 5，图形上的点是什么？",
        "(2, 5). Graphs are plotted as (x, f(x)) points.": "(2, 5). 图像以(x, f(x))点的形式绘制。",
        "Determine if f(x) = x² is even or odd": "判断f(x) = x²是偶函数还是奇函数",
        "Even. f(-x) = f(x). Symmetric about y-axis.": "偶函数. f(-x) = f(x). 关于y轴对称。",
        "Find the vertex of f(x) = (x - 3)² + 2": "求f(x) = (x - 3)² + 2的顶点",
        "(3, 2). Vertex form f(x) = a(x - h)² + k has vertex (h, k).": "(3, 2). 顶点式f(x) = a(x - h)² + k的顶点为(h, k)。",
        
        # ===== UNIT 2: POLYNOMIAL & RATIONAL FUNCTIONS =====
        "Polynomial Functions": "多项式函数",
        "Rational Functions": "有理函数",
        "End Behavior": "端点行为",
        "Zeros and Multiplicity": "零点和重数",
        "Asymptotes": "渐近线",
        "Vertical Asymptotes": "竖直渐近线",
        "Horizontal Asymptotes": "水平渐近线",
        "Oblique Asymptotes": "斜渐近线",
        
        # ===== UNIT 3: QUADRATIC FUNCTIONS =====
        "Quadratic Functions": "二次函数",
        "f(x) = ax² + bx + c": "f(x) = ax² + bx + c",
        "Vertex": "顶点",
        "Axis of Symmetry": "对称轴",
        "Focus and Directrix": "焦点和准线",
        "Real Solutions": "实数解",
        "Complex Solutions": "复数解",
        "Discriminant": "判别式",
        "b² - 4ac": "b² - 4ac",
        
        # ===== UNIT 4: EXPONENTIAL & LOGARITHMIC =====
        "Exponential Functions": "指数函数",
        "f(x) = a · b^x": "f(x) = a · b^x",
        "Growth": "增长",
        "Decay": "衰退",
        "Half-life": "半衰期",
        "Logarithmic Functions": "对数函数",
        "Logarithm": "对数",
        "Natural Logarithm": "自然对数",
        "Common Logarithm": "常用对数",
        "Change of Base Formula": "换底公式",
        "log_b(x) = ln(x)/ln(b)": "log_b(x) = ln(x)/ln(b)",
        
        # ===== UNIT 5: SEQUENCES & SERIES =====
        "Sequences": "数列",
        "Series": "级数",
        "Arithmetic Sequences": "等差数列",
        "Geometric Sequences": "等比数列",
        "Common Difference": "公差",
        "Common Ratio": "公比",
        "First Term": "首项",
        "nth Term": "第n项",
        "a_n = a_1 + (n-1)d": "a_n = a_1 + (n-1)d",
        "Sum Formula": "求和公式",
        "S_n = n/2(a_1 + a_n)": "S_n = n/2(a_1 + a_n)",
        
        # ===== UNIT 6: TRIG & UNIT CIRCLE =====
        "Unit Circle": "单位圆",
        "Trigonometric Functions": "三角函数",
        "Sine": "正弦",
        "Cosine": "余弦",
        "Tangent": "正切",
        "Cotangent": "余切",
        "Secant": "正割",
        "Cosecant": "余割",
        "Radians": "弧度",
        "Degrees": "度",
        "Pythagorean Identity": "勾股恒等式",
        "sin²θ + cos²θ = 1": "sin²θ + cos²θ = 1",
        
        # ===== UNIT 7: SYSTEMS OF EQUATIONS =====
        "Systems of Equations": "方程组",
        "Linear Systems": "线性方程组",
        "Nonlinear Systems": "非线性方程组",
        "Substitution Method": "代入法",
        "Elimination Method": "消元法",
        "Matrix Method": "矩阵法",
        
        # ===== UNIT 8: MATRICES =====
        "Matrices": "矩阵",
        "Matrix Operations": "矩阵运算",
        "Add": "加",
        "Subtract": "减",
        "Multiply": "乘",
        "Scalar Multiplication": "标量乘法",
        "Determinant": "行列式",
        "Inverse Matrix": "逆矩阵",
        "Solution to Matrix Equation": "矩阵方程的解",
        
        # ===== UNIT 9: CONIC SECTIONS =====
        "Conic Sections": "圆锥曲线",
        "Circle": "圆",
        "(x - h)² + (y - k)² = r²": "(x - h)² + (y - k)² = r²",
        "Center": "圆心",
        "Radius": "半径",
        "Parabola": "抛物线",
        "y = a(x - h)² + k": "y = a(x - h)² + k",
        "Ellipse": "椭圆",
        "(x - h)²/a² + (y - k)²/b² = 1": "(x - h)²/a² + (y - k)²/b² = 1",
        "Hyperbola": "双曲线",
        "(x - h)²/a² - (y - k)²/b² = 1": "(x - h)²/a² - (y - k)²/b² = 1",
        "Foci": "焦点",
        "Vertices": "顶点",
        
        # ===== COMMON TERMS =====
        "Next Up: Quiz": "下一步：测验",
        "Next Up: Play": "下一步：练习",
        "Unit Test": "单元测试",
        "Review Flashcards": "复习闪卡",
        "Start Unit Test": "开始单元测试",
        "Other games": "其他游戏",
        "Flashcard Game": "闪卡游戏",
        "Boost": "提升",
        "Mix & Match": "配对",
        "Block Puzzle": "块对谜题",
    }
    
    return translations

def append_translations_to_file(file_path, new_translations):
    """Append new translations to global_translations.js"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the closing of the translations object
    # We need to add entries before the closing }
    
    # Create translation entries
    translation_lines = []
    for eng, chin in sorted(new_translations.items()):
        # Escape quotes and newlines
        eng_escaped = eng.replace('"', '\\"').replace('\n', '\\n')
        chin_escaped = chin.replace('"', '\\"').replace('\n', '\\n')
        translation_lines.append(f'    "{eng_escaped}": "{chin_escaped}",')
    
    new_entries = '\n'.join(translation_lines) + '\n'
    
    # Find where to insert (before the last closing brace of translations object)
    # Pattern: look for the end of an existing translation entry before };
    insert_pattern = r'(    "[^"]+": "[^"]+",\n)(\s*};)'
    
    if re.search(insert_pattern, content):
        # Insert before the closing };
        modified = re.sub(
            insert_pattern,
            r'\1' + new_entries + r'\2',
            content,
            count=1
        )
    else:
        print("Could not find insertion point. File structure may have changed.")
        return False
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified)
    
    return True

def main():
    trans_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
    
    print("Generating Algebra 2 Chinese translations...")
    new_trans = create_comprehensive_algebra2_translations()
    print(f"Generated {len(new_trans)} translation pairs")
    
    print(f"Appending to {trans_file}...")
    if append_translations_to_file(trans_file, new_trans):
        print("✓ Successfully added Algebra 2 translations!")
    else:
        print("✗ Failed to add translations")

if __name__ == '__main__':
    main()
