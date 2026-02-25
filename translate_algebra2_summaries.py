#!/usr/bin/env python3
"""
Translate missing Algebra 2 summary strings to Chinese
"""

import json
import re

# Expanded translation dictionary for summary content
SUMMARY_TRANSLATIONS = {
    # Lesson titles and headers
    "Lesson": "课程",
    "Summary": "总结",
    "Key Concepts:": "关键概念：",
    "Key Formulas:": "关键公式：",
    "Key Terms:": "关键术语：",
    
    # Common phrase structures
    "are relations that": "是关系，其中",
    "is the set of": "是...的集合",
    "is represented by": "由...表示",
    "can be found": "可以被找到",
    "are used to": "被用于",
    "are combined": "被结合",
    "represents": "表示",
    "describes": "描述",
    "occurs when": "发生在",
    "applies when": "适用于",
    "Restrictions occur": "限制发生在",
    "occurs at": "发生在",
    "occurs for": "发生于",
    "when": "当",
    "where": "其中",
    "if and only if": "当且仅当",
    
    # Mathematical concepts
    "Function": "函数",
    "function": "函数",
    "output": "输出",
    "input": "输入",
    "Domain": "定义域",
    "domain": "定义域",
    "Range": "值域",
    "range": "值域",
    "Vertex": "顶点",
    "vertex": "顶点",
    "Parabola": "抛物线",
    "parabola": "抛物线",
    "Circle": "圆",
    "circle": "圆",
    "Ellipse": "椭圆",
    "ellipse": "椭圆",
    "Hyperbola": "双曲线",
    "hyperbola": "双曲线",
    "Center": "中心",
    "center": "中心",
    "Radius": "半径",
    "radius": "半径",
    "Asymptote": "渐近线",
    "asymptote": "渐近线",
    "Axis": "轴",
    "axis": "轴",
    "Symmetry": "对称",
    "symmetry": "对称",
    "Focal": "焦点的",
    "focal": "焦点的",
    "Directrix": "准线",
    "directrix": "准线",
    "Denominator": "分母",
    "denominator": "分母",
    "Numerator": "分子",
    "numerator": "分子",
    "Polynomial": "多项式",
    "polynomial": "多项式",
    "Factor": "因子",
    "factor": "因子",
    "Exponent": "指数",
    "exponent": "指数",
    "Radical": "根号",
    "radical": "根号",
    "Rational": "有理",
    "rational": "有理",
    "Logarithm": "对数",
    "logarithm": "对数",
    "Natural log": "自然对数",
    
    # Operations
    "add": "加",
    "subtract": "减",
    "multiply": "乘",
    "divide": "除",
    "solve": "解",
    "Solve": "解",
    "simplify": "简化",
    "Simplify": "简化",
    "graph": "绘制图像",
    "Graph": "绘制图像",
    "factor": "因式分解",
    "Factor": "因式分解",
    "expand": "展开",
    "Expand": "展开",
    
    # Properties and relationships
    "inverse": "反函数",
    "composition": "复合",
    "substitution": "代入",
    "elimination": "消元",
    "Matrix": "矩阵",
    "matrix": "矩阵",
    "determinant": "行列式",
    "Cramer's rule": "克拉默法则",
    "Sequence": "数列",
    "sequence": "数列",
    "Series": "级数",
    "series": "级数",
    "Arithmetic": "算术",
    "arithmetic": "算术",
    "Geometric": "几何",
    "geometric": "几何",
    "sum": "和",
    "Sum": "和",
    
    # Solutions and answers
    "Solution": "解",
    "solution": "解",
    "Solutions": "解",
    "solutions": "解",
    "Answer": "答案",
    "answer": "答案",
    "Example": "例子",
    "example": "例子",
    "Note:": "注意：",
    "note:": "注意：",
    "Tips:": "提示：",
    "tip:": "提示：",
    "Remember:": "记住：",
    "remember:": "记住：",
    
    # Methods and procedures
    "Method": "方法",
    "method": "方法",
    "Step": "步骤",
    "step": "步骤",
    "Complete": "完成",
    "complete": "完成",
    "Square": "平方",
    "square": "平方",
    "Formula": "公式",
    "formula": "公式",
    "Theorem": "定理",
    "theorem": "定理",
    
    # Specific common phrases in summaries
    "assign exactly one": "分配恰好一个",
    "The domain is": "定义域是",
    "The range is": "值域是",
    "opens upward": "向上开口",
    "opens downward": "向下开口",
    "opens to the right": "向右打开",
    "opens to the left": "向左打开",
    "forms a U shape": "形成U形",
    "reflects across": "关于...反射",
    "moves horizontally": "水平移动",
    "moves vertically": "垂直移动",
    "Translations": "平移",
    "translations": "平移",
    "Reflections": "反射",
    "reflections": "反射",
    "Stretches": "拉伸",
    "stretches": "拉伸",
    "Compressions": "压缩",
    "compressions": "压缩",
    "Growth": "增长",
    "growth": "增长",
    "Decay": "衰减",
    "decay": "衰减",
    "Half-life": "半衰期",
    "half-life": "半衰期",
    "Intersection": "交点",
    "intersection": "交点",
    "Union": "并集",
    "union": "并集",
    
    # Mathematical notation descriptions
    "equals": "等于",
    "approximately equals": "约等于",
    "not equal": "不等于",
    "less than": "小于",
    "greater than": "大于",
    "less than or equal": "小于或等于",
    "greater than or equal": "大于或等于",
    "infinity": "无穷大",
    
    # Descriptive words
    "complex": "复杂",
    "real": "实数",
    "distinct": "不同的",
    "unique": "唯一",
    "unique solution": "唯一解",
    "no solution": "无解",
    "infinite solutions": "无穷多个解",
    "positive": "正数",
    "negative": "负数",
    "zero": "零",
    "constant": "常数",
    
    # Conditional phrases
    "If": "如果",
    "if": "如果",
    "Then": "那么",
    "then": "那么",
    "For": "对于",
    "for": "对于",
    "such that": "使得",
    "provided": "假设",
    "unless": "除非",
    
    # Degree measurement
    "degree": "度",
    "degrees": "度",
    "radian": "弧度",
    "radians": "弧度",
}

def smart_translate_summary(text):
    """Intelligently translate summary text to Chinese"""
    
    # If mostly mathematical notation, do minimal translation
    text_chars = sum(1 for c in text if c.isalpha())
    total_chars = len(text)
    
    result = text
    
    # Try exact phrase matches first (for better context)
    for eng, chi in sorted(SUMMARY_TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        # Use word boundaries for short phrases
        if len(eng) <= 15:
            pattern = r'\b' + re.escape(eng) + r'\b'
            result = re.sub(pattern, chi, result, flags=re.IGNORECASE)
        else:
            # For longer phrases, do exact replacement
            result = result.replace(eng, chi)
    
    return result

def main():
    # Read missing summary strings
    with open('/workspaces/ArisEdu/algebra2_summary_missing.json', 'r', encoding='utf-8') as f:
        missing_strings = json.load(f)
    
    print(f"Processing {len(missing_strings)} missing summary strings...")
    
    # Generate translations
    translations_dict = {}
    for i, original in enumerate(missing_strings):
        translated = smart_translate_summary(original)
        translations_dict[original] = translated
        
        if (i + 1) % 100 == 0:
            print(f"  Translated {i + 1}/{len(missing_strings)}")
    
    print(f"\nTranslation complete!")
    
    # Save to file
    with open('/workspaces/ArisEdu/algebra2_summary_translations.json', 'w', encoding='utf-8') as f:
        json.dump(translations_dict, f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(translations_dict)} translations to algebra2_summary_translations.json")
    
    return translations_dict

if __name__ == "__main__":
    translations = main()
