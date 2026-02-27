#!/usr/bin/env python3
"""
Add missing Algebra 2 Summary and variant Spanish translations
"""

# Base lessons that need Summary, Quiz, Practice variants
BASE_LESSONS_SPANISH = {
    "1.1": ("Review of Functions & Notation", "Revisión de Funciones y Notación"),
    "1.2": ("Linear Equations & Graphing", "Ecuaciones Lineales y Gráficos"),
    "1.3": ("Systems of Linear Equations", "Sistemas de Ecuaciones Lineales"),
    "1.4": ("Solving Systems by Substitution", "Resolver Sistemas por Sustitución"),
    "1.5": ("Solving Systems by Elimination", "Resolver Sistemas por Eliminación"),
    "1.6": ("Applications of Linear Systems", "Aplicaciones de Sistemas Lineales"),
    "1.7": ("Inequalities & System of Inequalities", "Desigualdades y Sistemas de Desigualdades"),
    "1.8": ("Linear Programming", "Programación Lineal"),
    "1.9": ("Advanced Linear Applications", "Aplicaciones Lineales Avanzadas"),
    "2.1": ("Quadratic Functions & Parabolas", "Funciones Cuadráticas y Parábolas"),
    "2.2": ("Transformations of Quadratics", "Transformaciones de Cuadráticos"),
    "2.3": ("Completing the Square", "Completar el Cuadrado"),
    "2.4": ("Quadratic Formula & Discriminant", "Fórmula Cuadrática y Discriminante"),
    "2.5": ("Graphing Quadratic Functions", "Gráficos de Funciones Cuadráticas"),
    "2.6": ("Applications of Quadratics", "Aplicaciones de Cuadráticos"),
    "2.7": ("Quadratic Inequalities", "Desigualdades Cuadráticas"),
    "3.1": ("Polynomial Operations", "Operaciones Polinomiales"),
    "3.2": ("Factoring Polynomials", "Factorización de Polinomios"),
    "3.3": ("Synthetic Division", "División Sintética"),
    "3.4": ("Polynomial Graphs & Zeros", "Gráficos de Polinomios y Ceros"),
    "3.5": ("Remainder & Factor Theorems", "Teoremas del Resto y del Factor"),
    "3.6": ("Complex Numbers & Polynomial Roots", "Números Complejos y Raíces Polinomiales"),
    "3.7": ("Higher-Degree Polynomials", "Polinomios de Grado Superior"),
    "4.1": ("Rational Expressions", "Expresiones Racionales"),
    "4.2": ("Operations on Rational Expressions", "Operaciones en Expresiones Racionales"),
    "4.3": ("Rational Equations", "Ecuaciones Racionales"),
    "4.4": ("Graphing Rational Functions", "Gráficos de Funciones Racionales"),
    "4.5": ("Asymptotes & Discontinuities", "Asíntotas y Discontinuidades"),
    "4.6": ("Applications of Rational Functions", "Aplicaciones de Funciones Racionales"),
    "5.1": ("Exponential Functions & Growth", "Funciones Exponenciales y Crecimiento"),
    "5.2": ("Exponential Decay & Applications", "Decaimiento Exponencial y Aplicaciones"),
    "5.3": ("Logarithms & Properties", "Logaritmos y Propiedades"),
    "5.4": ("Logarithmic Functions & Graphs", "Funciones Logarítmicas y Gráficos"),
    "5.5": ("Exponential & Logarithmic Equations", "Ecuaciones Exponenciales y Logarítmicas"),
    "5.6": ("Applications of Exponentials & Logs", "Aplicaciones de Exponenciales y Logaritmos"),
    "5.7": ("Natural Logarithms & e", "Logaritmos Naturales y e"),
    "6.1": ("Arithmetic Sequences", "Secuencias Aritméticas"),
    "6.2": ("Geometric Sequences", "Secuencias Geométricas"),
    "6.3": ("Series & Summation Notation", "Series y Notación de Sumatoria"),
    "6.4": ("Infinite Geometric Series", "Series Geométricas Infinitas"),
    "6.5": ("Applications & Mathematical Induction", "Aplicaciones e Inducción Matemática"),
    "7.1": ("Counting Principles", "Principios de Conteo"),
    "7.2": ("Permutations & Combinations", "Permutaciones y Combinaciones"),
    "7.3": ("Probability Basics & Events", "Fundamentos de Probabilidad y Eventos"),
    "7.4": ("Conditional Probability", "Probabilidad Condicional"),
    "7.5": ("Normal Distributions", "Distribuciones Normales"),
    "7.6": ("Hypothesis Testing & Confidence Intervals", "Prueba de Hipótesis e Intervalos de Confianza"),
    "7.7": ("Correlation & Linear Regression", "Correlación y Regresión Lineal"),
    "8.1": ("Angles & Angle Measures", "Ángulos y Medidas de Ángulos"),
    "8.2": ("Unit Circle & Trigonometric Ratios", "Círculo Unitario y Razones Trigonométricas"),
    "8.3": ("Graphs of Trigonometric Functions", "Gráficos de Funciones Trigonométricas"),
    "8.4": ("Trigonometric Identities", "Identidades Trigonométricas"),
    "8.5": ("Solving Trigonometric Equations", "Resolución de Ecuaciones Trigonométricas"),
    "8.6": ("Applications of Trigonometry", "Aplicaciones de la Trigonometría"),
    "9.1": ("Conic Sections", "Secciones Cónicas"),
    "9.2": ("Parametric Equations", "Ecuaciones Paramétricas"),
    "9.3": ("Vectors & Vector Operations", "Vectores y Operaciones Vectoriales"),
    "9.4": ("Complex Numbers in Polar Form", "Números Complejos en Forma Polar"),
}

def add_spanish_variants():
    """Add Summary and Quiz/Practice variants"""
    spanish_file = "ArisEdu Project Folder/scripts/spanish_translations.js"
    
    with open(spanish_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    variants = {}
    
    # Generate Summary variants
    for lesson_id, (english, spanish) in BASE_LESSONS_SPANISH.items():
        key = f"Lesson {lesson_id}: {english} - Summary"
        value = f"Lección {lesson_id}: {spanish} - Resumen"
        variants[key] = value
        
        # Quiz and Practice
        key_quiz = f"Lesson {lesson_id}: {english} - Quiz"
        value_quiz = f"Lección {lesson_id}: {spanish} - Prueba"
        variants[key_quiz] = value_quiz
        
        key_practice = f"Lesson {lesson_id}: {english} - Practice"
        value_practice = f"Lección {lesson_id}: {spanish} - Práctica"
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
    
    with open(spanish_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Added {added_count} Spanish variant translations (Summary, Quiz, Practice)")
    print(f"⚠️  {already_present} translations already present")
    print(f"Total processed: {added_count + already_present}")

if __name__ == "__main__":
    add_spanish_variants()
