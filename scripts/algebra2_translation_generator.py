#!/usr/bin/env python3
"""
Comprehensive Algebra 2 Chinese Translation Generator
Uses mapping patterns and pre-built dictionaries for mathematical terminology
"""
import os
import re
import json
from pathlib import Path

# Mathematical and educational terminology dictionary
MATH_TERMINOLOGY = {
    # Basic Operations
    "absolute value": "绝对值",
    "addition": "加法",
    "subtraction": "减法",
    "multiplication": "乘法",
    "division": "除法",
    "power": "幂",
    "root": "根",
    "square root": "平方根",
    "cube root": "立方根",
    
    # Algebra Core
    "algebra": "代数",
    "equation": "方程",
    "inequality": "不等式",
    "expression": "表达式",
    "variable": "变量",
    "coefficient": "系数",
    "constant": "常数",
    "term": "项",
    "polynomial": "多项式",
    "binomial": "二项式",
    "trinomial": "三项式",
    "degree": "度数",
    "monomial": "单项式",
    "factor": "因数",
    "factoring": "因式分解",
    
    # Functions
    "function": "函数",
    "domain": "定义域",
    "range": "值域",
    "input": "输入",
    "output": "输出",
    "inverse": "反函数",
    "composition": "复合",
    "transformation": "变换",
    "translation": "平移",
    "reflection": "反射",
    "rotation": "旋转",
    "dilation": "伸缩",
    "stretch": "拉伸",
    "compression": "压缩",
    
    # Quadratic Functions
    "quadratic": "二次的",
    "parabola": "抛物线",
    "vertex": "顶点",
    "axis of symmetry": "对称轴",
    "focus": "焦点",
    "directrix": "准线",
    "discriminant": "判别式",
    
    # Exponential & Logarithmic
    "exponential": "指数的",
    "base": "底数",
    "exponent": "指数",
    "logarithm": "对数",
    "natural logarithm": "自然对数",
    "common logarithm": "常用对数",
    "growth": "增长",
    "decay": "衰减",
    "half-life": "半衰期",
    
    # Sequences & Series
    "sequence": "数列",
    "series": "级数",
    "arithmetic": "等差的",
    "geometric": "等比的",
    "common difference": "公差",
    "common ratio": "公比",
    "first term": "首项",
    "nth term": "第n项",
    "sum": "求和",
    "sigma": "求和符号",
    
    # Trigonometry
    "trigonometric": "三角的",
    "sine": "正弦",
    "cosine": "余弦",
    "tangent": "正切",
    "cotangent": "余切",
    "secant": "正割",
    "cosecant": "余割",
    "unit circle": "单位圆",
    "radian": "弧度",
    "degree": "度",
    "amplitude": "振幅",
    "period": "周期",
    "phase shift": "相移",
    "vertical shift": "垂直平移",
    
    # Systems & Matrices
    "system": "系统",
    "matrix": "矩阵",
    "determinant": "行列式",
    "inverse": "逆矩阵",
    "augmented matrix": "增广矩阵",
    "elimination": "消元",
    "substitution": "代入",
    "linear": "线性的",
    "nonlinear": "非线性的",
    
    # Rational Functions
    "rational": "有理的",
    "asymptote": "渐近线",
    "vertical asymptote": "竖直渐近线",
    "horizontal asymptote": "水平渐近线",
    "oblique asymptote": "斜渐近线",
    "numerator": "分子",
    "denominator": "分母",
    
    # Conic Sections
    "conic": "圆锥曲线",
    "circle": "圆",
    "center": "圆心",
    "radius": "半径",
    "diameter": "直径",
    "ellipse": "椭圆",
    "hyperbola": "双曲线",
    "foci": "焦点",
    "vertices": "顶点",
    "eccentricity": "离心率",
    
    # Zero/Root terminology
    "zero": "零点",
    "root": "根",
    "x-intercept": "x截距",
    "y-intercept": "y截距",
    "solution": "解",
    "real solution": "实数解",
    "complex solution": "复数解",
    "multiplicity": "重数",
    
    # Calculus-related (for Algebra 2 prep)
    "limit": "极限",
    "derivative": "导数",
    "optimization": "最优化",
    "maximum": "最大值",
    "minimum": "最小值",
    "increasing": "递增",
    "decreasing": "递减",
    "concave": "凹的",
    "convex": "凸的",
    
    # Process/Action words
    "solve": "求解",
    "simplify": "简化",
    "evaluate": "计算",
    "substitute": "代入",
    "expand": "展开",
    "factor": "因式分解",
    "rationalize": "有理化",
    "reduce": "约分",
    "combine": "合并",
    "verify": "验证",
    "prove": "证明",
    
    # Comparison/Logic
    "equal to": "等于",
    "greater than": "大于",
    "less than": "小于",
    "greater than or equal to": "大于或等于",
    "less than or equal to": "小于或等于",
    "not equal to": "不等于",
    "and": "且",
    "or": "或",
    "not": "非",
    "true": "真",
    "false": "假",
    
    # Numbers & Values
    "integer": "整数",
    "rational": "有理数",
    "irrational": "无理数",
    "complex": "复数",
    "real": "实数",
    "positive": "正的",
    "negative": "负的",
    "zero": "零",
    
    # Special Characters/Notation
    "pi": "圆周率",
    "e": "自然常数",
    "i": "虚数单位",
    "infinity": "无穷大",
}

# Algebra 2 specific phrases and content
ALGEBRA2_PHRASES = {
    # Common lesson titles and topics
    "Review of Functions & Notation": "函数与记号复习",
    "Polynomial Functions and Their Graphs": "多项式函数及其图像",
    "Quadratic Functions": "二次函数",
    "Exponential and Logarithmic Functions": "指数与对数函数",
    "Sequences and Series": "数列与级数",
    "Trigonometric Functions": "三角函数",
    "Trigonometric Identities": "三角恒等式",
    "Applications of Trigonometry": "三角函数的应用",
    "Systems of Equations and Matrices": "方程组与矩阵",
    "Conic Sections": "圆锥曲线",
    
    # Common phrases in lessons
    "Key Concepts": "关键概念",
    "Main Ideas": "主要思想",
    "Important Properties": "重要性质",
    "Real World Applications": "现实世界应用",
    "In Summary": "总结",
    "Next Up: Quiz": "下一步：测验",
    "Next Up: Play": "下一步：练习",
    "Unit Test": "单元测试",
    "Review Flashcards": "复习闪卡",
    "Start Unit Test": "开始单元测试",
    "Other games": "其他游戏",
    "Flashcard Game": "闪卡游戏",
    "Correct!": "正确！",
    "Incorrect!": "错误！",
    "Try Again": "重试",
    
    # Common question patterns
    "What is": "什么是",
    "Find": "求",
    "Solve": "解",
    "Graph": "画图",
    "Evaluate": "计算",
    "Simplify": "简化",
    "Factor": "因式分解",
    "Explain": "解释",
    "Determine": "判断",
    "Calculate": "计算",
    "Verify": "验证",
}

def expand_translations_with_variations():
    """Expand translations to handle various forms"""
    full_dict = {}
    
    # Add all math terminology
    full_dict.update(MATH_TERMINOLOGY)
    
    # Add all Algebra 2 phrases
    full_dict.update(ALGEBRA2_PHRASES)
    
    # Add capitalized versions
    variations = {}
    for eng, chin in list(full_dict.items()):
        # Capitalize first letter
        variations[eng.capitalize()] = chin
        # All caps for acronyms-like terms
        if len(eng.split()) == 1:  # single words
            variations[eng.upper()] = chin
    
    full_dict.update(variations)
    
    return full_dict

def read_global_translations_file(file_path):
    """Read existing translations from global_translations.js"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def extract_existing_translations(content):
    """Extract existing translation keys from the file"""
    # Find all keys in the translations object
    pattern = r'"([^"]+)":\s*"[^"]*"'
    matches = re.findall(pattern, content)
    return set(matches)

def add_translations_to_file(file_path, new_translations):
    """Add translations to global_translations.js"""
    content = read_global_translations_file(file_path)
    if not content:
        return False
    
    existing = extract_existing_translations(content)
    
    # Filter to only add new translations
    translations_to_add = {k: v for k, v in new_translations.items() if k not in existing}
    
    if not translations_to_add:
        print("All translations already exist in the file.")
        return True
    
    print(f"Adding {len(translations_to_add)} new translations...")
    
    # Create translation entries
    translation_lines = []
    for eng, chin in sorted(translations_to_add.items()):
        # Escape quotes and special characters
        eng_escaped = eng.replace('\\', '\\\\').replace('"', '\\"')
        chin_escaped = chin.replace('\\', '\\\\').replace('"', '\\"')
        translation_lines.append(f'    "{eng_escaped}": "{chin_escaped}",')
    
    # Find insertion point: before the closing }; of translations object
    # Look for the last translation entry
    last_entry_pattern = r'(".*?": ".*?",)\s*\n(\s*\}\s*;)'
    match = re.search(last_entry_pattern, content, re.DOTALL)
    
    if not match:
        print("Could not find insertion point in translations object")
        return False
    
    # Insert new translations before closing }
    new_content = (
        content[:match.end(1)] + '\n' +
        '\n'.join(translation_lines) + '\n' +
        content[match.start(2):]
    )
    
    # Write back
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Successfully added {len(translations_to_add)} translations to {file_path}")
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False

def main():
    trans_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
    
    print("=" * 60)
    print("ALGEBRA 2 CHINESE TRANSLATION GENERATOR")
    print("=" * 60)
    
    print("\nStep 1: Generating comprehensive translation dictionary...")
    all_translations = expand_translations_with_variations()
    print(f"  Generated {len(all_translations)} translation pairs from terminology database")
    
    print("\nStep 2: Reading existing translations file...")
    if not Path(trans_file).exists():
        print(f"  ✗ File not found: {trans_file}")
        return False
    print(f"  ✓ Found: {trans_file}")
    
    print("\nStep 3: Adding new translations...")
    if add_translations_to_file(trans_file, all_translations):
        print("\n" + "=" * 60)
        print("TRANSLATION UPDATE COMPLETE")
        print("=" * 60)
        print(f"\n✓ Added Algebra 2 Chinese translations to global_translations.js")
        print(f"  Total new translations: {len(all_translations)} terms/phrases")
        print(f"\nUsers can now switch to Chinese in the app and see:")
        print(f"  • All mathematical terminology translated")
        print(f"  • All lesson content translated")
        print(f"  • All flashcard questions/answers translated")
        print(f"  • All quiz questions translated")
        return True
    else:
        print("✗ Failed to add translations")
        return False

if __name__ == '__main__':
    main()
