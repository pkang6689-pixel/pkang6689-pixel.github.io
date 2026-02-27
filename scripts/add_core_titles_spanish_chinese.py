#!/usr/bin/env python3
"""
Add missing core title Spanish and Chinese translations for better fallback lookup
"""

# Core titles for Spanish and Chinese (for all languages)
CORE_TITLES_SPANISH = {
    "Advanced Linear Applications": "Aplicaciones Lineales Avanzadas",
    "Quadratic Inequalities": "Desigualdades Cuadráticas",
    "Higher-Degree Polynomials": "Polinomios de Grado Superior",
    "Applications of Rational Functions": "Aplicaciones de Funciones Racionales",
    "Natural Logarithms & e": "Logaritmos Naturales y e",
    "Applications & Mathematical Induction": "Aplicaciones e Inducción Matemática",
    "Counting Principles": "Principios de Conteo",
    "Permutations & Combinations": "Permutaciones y Combinaciones",
    "Probability Basics & Events": "Fundamentos de Probabilidad y Eventos",
    "Conditional Probability": "Probabilidad Condicional",
    "Normal Distributions": "Distribuciones Normales",
    "Hypothesis Testing & Confidence Intervals": "Prueba de Hipótesis e Intervalos de Confianza",
    "Correlation & Linear Regression": "Correlación y Regresión Lineal",
    "Angles & Angle Measures": "Ángulos y Medidas de Ángulos",
    "Unit Circle & Trigonometric Ratios": "Círculo Unitario y Razones Trigonométricas",
    "Graphs of Trigonometric Functions": "Gráficos de Funciones Trigonométricas",
    "Trigonometric Identities": "Identidades Trigonométricas",
    "Solving Trigonometric Equations": "Resolución de Ecuaciones Trigonométricas",
    "Applications of Trigonometry": "Aplicaciones de la Trigonometría",
    "Conic Sections": "Secciones Cónicas",
    "Parametric Equations": "Ecuaciones Paramétricas",
    "Vectors & Vector Operations": "Vectores y Operaciones Vectoriales",
    "Complex Numbers in Polar Form": "Números Complejos en Forma Polar",
}

CORE_TITLES_CHINESE = {
    "Advanced Linear Applications": "高级线性应用",
    "Quadratic Inequalities": "二次不等式",
    "Higher-Degree Polynomials": "高次多项式",
    "Applications of Rational Functions": "有理函数的应用",
    "Natural Logarithms & e": "自然对数和e",
    "Applications & Mathematical Induction": "应用和数学归纳法",
    "Counting Principles": "计数原理",
    "Permutations & Combinations": "排列和组合",
    "Probability Basics & Events": "概率基础和事件",
    "Conditional Probability": "条件概率",
    "Normal Distributions": "正态分布",
    "Hypothesis Testing & Confidence Intervals": "假设检验和置信区间",
    "Correlation & Linear Regression": "相关性和线性回归",
    "Angles & Angle Measures": "角和角度量",
    "Unit Circle & Trigonometric Ratios": "单位圆和三角比",
    "Graphs of Trigonometric Functions": "三角函数的图形",
    "Trigonometric Identities": "三角恒等式",
    "Solving Trigonometric Equations": "解三角方程",
    "Applications of Trigonometry": "三角学的应用",
    "Conic Sections": "圆锥曲线",
    "Parametric Equations": "参数方程",
    "Vectors & Vector Operations": "向量和向量运算",
    "Complex Numbers in Polar Form": "极坐标形式的复数",
}

def add_core_titles():
    """Add core title translations for both Spanish and Chinese"""
    
    # Spanish
    spanish_file = "ArisEdu Project Folder/scripts/spanish_translations.js"
    with open(spanish_file, 'r', encoding='utf-8') as f:
        spanish_content = f.read()
    
    spanish_added = 0
    for key, translation in CORE_TITLES_SPANISH.items():
        if f'"{key}"' not in spanish_content:
            insertion_point = spanish_content.rfind('};')
            if insertion_point != -1:
                new_entry = f'\n    "{key}": "{translation}",'
                spanish_content = spanish_content[:insertion_point] + new_entry + spanish_content[insertion_point:]
                spanish_added += 1
    
    with open(spanish_file, 'w', encoding='utf-8') as f:
        f.write(spanish_content)
    
    # Chinese
    chinese_file = "ArisEdu Project Folder/scripts/global_translations.js"
    with open(chinese_file, 'r', encoding='utf-8') as f:
        chinese_content = f.read()
    
    chinese_added = 0
    for key, translation in CORE_TITLES_CHINESE.items():
        if f'"{key}"' not in chinese_content:
            insertion_point = chinese_content.rfind('};')
            if insertion_point != -1:
                new_entry = f'\n    "{key}": "{translation}",'
                chinese_content = chinese_content[:insertion_point] + new_entry + chinese_content[insertion_point:]
                chinese_added += 1
    
    with open(chinese_file, 'w', encoding='utf-8') as f:
        f.write(chinese_content)
    
    print(f"✅ Added {spanish_added} Spanish core title translations")
    print(f"✅ Added {chinese_added} Simplified Chinese core title translations")

if __name__ == "__main__":
    add_core_titles()
