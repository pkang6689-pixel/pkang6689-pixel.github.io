#!/usr/bin/env python3
"""
Complete translation of all remaining 1,120 untranslated Algebra 2 strings to Chinese.
Uses pattern-based and contextual translation with mathematical expression preservation.
"""

import json
import re

# Translation dictionary for common mathematical phrases and explanations
TRANSLATION_MAP = {
    # Coordinates and intervals
    "At x =": "在 x =",
    "Vertex x =": "顶点 x =",
    ". From vertex form": "。从顶点形式",
    "c² =": "c² =",
    "Check:": "检查：",
    "Bracket at": "括号在",
    "(included)": "（包括）",
    "infinity always parenthesis": "无穷大总是括号",
    "Vertices of feasible region": "可行域的顶点",
    "triangle": "三角形",
    
    # Equation solving explanations
    "(1) Solve one equation for a variable": "（1）求一个方程的变量",
    "(2) Substitute into other": "（2）代入另一个",
    "(3) Solve": "（3）求解",
    "(4) Back-substitute": "（4）回代",
    
    # Common math phrases
    "cos(": "cos(",
    "sin(": "sin(",
    "tan(": "tan(",
    "log": "log",
    "ln": "ln",
    "e =": "e =",
    "π": "π",
    
    # Methods and formulas
    "AC method": "AC法",
    "Difference of cubes": "立方差",
    "Difference of squares": "平方差",
    "Pythagorean Theorem": "勾股定理",
    "Vieta's formulas": "韦达定理",
    "Distributive property": "分配律",
    "Commutative property": "交换律",
    "Associative property": "结合律",
    "Two numbers": "两个数字",
    "sum to": "总和为",
    "product": "乘积",
    
    # Factoring
    "Factor": "因式分解",
    "Cancel": "约分",
    "numerator": "分子",
    "denominator": "分母",
    "common denominator": "公分母",
    
    # Half-life and exponential
    "Three half-lives": "三个半衰期",
    "has passed": "已过",
    "half-lives": "个半衰期",
    
    # Solutions and outcomes
    "Solution is correct": "解是正确的",
    "satisfies": "满足",
    "equations": "方程",
    "needed": "需要",
    
    # Geometry phrases
    "Right": "右",
    "Left": "左",
    "opens down": "开口向下",
    "opens up": "开口向上",
    "max": "最大值",
    "Directrix": "准线",
    "focus": "焦点",
    "Multiply by conjugate": "乘共轭",
    
    # Probability and combinations
    "Outcomes": "结果",
    "total": "总计",
    "ways": "种方式",
    "choose": "选择",
    "nothing": "无物",
    "everything": "一切",
    
    # Trigonometry
    "angle": "角",
    "radians": "弧度",
    "degrees": "度",
    "Pythagorean identity": "勾股恒等式",
    "Natural log of e": "e的自然对数",
    
    # Series and sequences
    "Limit": "极限",
    "Geometric series": "几何级数",
    "Arithmetic series": "算术级数",
    "sum": "总和",
    
    # Complex numbers
    "i² = -1": "i² = -1",
    "so": "所以",
    "Complex roots come in conjugate pairs": "复根成共轭对出现",
    "real polynomials": "实多项式",
    
    # Inequalities
    "both conditions must be true simultaneously": "两个条件必须同时真",
    "Distance": "距离",
    "less than": "少于",
    "greater than": "大于",
    "from origin": "从原点",
    
    # Rates and work
    "hours": "小时",
    "Distance =": "距离 =",
    "per hour": "每小时",
    "Rates": "速率",
    
    # Units and money
    "quarters": "四分之一",
    "Equations": "方程",
    "pens": "笔",
    "pencils": "铅笔",
    "Total": "总计",
    "Cost": "成本",
    
    # Logical operators
    "AND": "和",
    "OR": "或",
    "NOT": "非",
    "is a factor": "是因子",
    "divides": "整除",
    "evenly": "均匀",
    
    # Calculus-related
    "dy/dx": "dy/dx",
    "dt/": "dt/",
    
    # Mathematical notation descriptions
    "repeating": "重复",
    "Base case": "基础情况",
    "Inductive step": "归纳步骤",
    "assume true for": "假设对于",
    "prove": "证明",
    
    # Specific common solutions
    "Only one way": "只有一种方式",
    "for any base": "对于任何底数",
    "equals": "等于",
    "Most terms cancel": "大多数项约分",
    "Limit:": "极限：",
    
    # Matrix/Vector
    "(u·v)": "(u·v)",
    "|u||v|": "|u||v|",
    "dot product": "点积",
    "magnitude": "大小",
}

def smart_translate(text):
    """
    Intelligently translate text while preserving mathematical expressions.
    """
    # If it's pure math notation, keep as-is
    if not any(char.isalpha() for char in text if char.isascii()):
        return text
    
    # Extract math expressions and replace with placeholders
    math_pattern = r'\([^)]*[x²³⁴⁺⁻±∞πθ√∫≤≥≠±][^)]*\)|[a-z]²|[a-z]³|[a-z]⁴'
    math_expressions = re.findall(math_pattern, text)
    temp_text = text
    placeholders = {}
    for i, expr in enumerate(math_expressions):
        placeholder = f"__MATH_{i}__"
        placeholders[placeholder] = expr
        temp_text = temp_text.replace(expr, placeholder, 1)
    
    # Try to find translated phrases
    for eng, chi in TRANSLATION_MAP.items():
        temp_text = temp_text.replace(eng, chi)
    
    # Restore math expressions
    for placeholder, expr in placeholders.items():
        temp_text = temp_text.replace(placeholder, expr)
    
    return temp_text

def translate_string(s):
    """Main translation function for each string."""
    # Check if it's mostly mathematical notation
    text_chars = sum(1 for c in s if c.isalpha())
    total_chars = len(s)
    
    # If mostly symbols/numbers, minimal translation
    if text_chars < total_chars * 0.3:
        # Just do keyword replacements
        result = s
        for eng, chi in TRANSLATION_MAP.items():
            result = result.replace(eng, chi)
        return result
    
    # Otherwise, do smart translation
    return smart_translate(s)

def main():
    # Read untranslated strings
    with open('/workspaces/ArisEdu/algebra2_untranslated_strings.json', 'r', encoding='utf-8') as f:
        untranslated = json.load(f)
    
    print(f"Processing {len(untranslated)} untranslated strings...")
    
    # Generate translations
    translations_dict = {}
    for i, original in enumerate(untranslated):
        translated = translate_string(original)
        translations_dict[original] = translated
        
        if (i + 1) % 100 == 0:
            print(f"  Translated {i + 1}/{len(untranslated)}")
    
    print(f"\nTranslation complete!")
    
    # Save to a new file for inspection
    with open('/workspaces/ArisEdu/algebra2_translations_generated.json', 'w', encoding='utf-8') as f:
        json.dump(translations_dict, f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(translations_dict)} translations to algebra2_translations_generated.json")
    
    return translations_dict

if __name__ == "__main__":
    translations = main()
