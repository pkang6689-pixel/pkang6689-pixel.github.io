#!/usr/bin/env python3
"""
Add missing Algebra 2 Spanish translations for all lessons
"""

# All Algebra 2 lessons with Spanish translations
ALGEBRA2_LESSONS_SPANISH = {
    # Unit 1
    "Lesson 1.1: Review of Functions & Notation": "Lección 1.1: Revisión de Funciones y Notación",
    "Lesson 1.2: Linear Equations & Graphing": "Lección 1.2: Ecuaciones Lineales y Gráficos",
    "Lesson 1.3: Systems of Linear Equations": "Lección 1.3: Sistemas de Ecuaciones Lineales",
    "Lesson 1.4: Solving Systems by Substitution": "Lección 1.4: Resolver Sistemas por Sustitución",
    "Lesson 1.5: Solving Systems by Elimination": "Lección 1.5: Resolver Sistemas por Eliminación",
    "Lesson 1.6: Applications of Linear Systems": "Lección 1.6: Aplicaciones de Sistemas Lineales",
    "Lesson 1.7: Inequalities & System of Inequalities": "Lección 1.7: Desigualdades y Sistemas de Desigualdades",
    "Lesson 1.8: Linear Programming": "Lección 1.8: Programación Lineal",
    "Lesson 1.9: Advanced Linear Applications": "Lección 1.9: Aplicaciones Lineales Avanzadas",
    # Unit 2
    "Lesson 2.1: Quadratic Functions & Parabolas": "Lección 2.1: Funciones Cuadráticas y Parábolas",
    "Lesson 2.2: Transformations of Quadratics": "Lección 2.2: Transformaciones de Cuadráticos",
    "Lesson 2.3: Completing the Square": "Lección 2.3: Completar el Cuadrado",
    "Lesson 2.4: Quadratic Formula & Discriminant": "Lección 2.4: Fórmula Cuadrática y Discriminante",
    "Lesson 2.5: Graphing Quadratic Functions": "Lección 2.5: Gráficos de Funciones Cuadráticas",
    "Lesson 2.6: Applications of Quadratics": "Lección 2.6: Aplicaciones de Cuadráticos",
    "Lesson 2.7: Quadratic Inequalities": "Lección 2.7: Desigualdades Cuadráticas",
    # Unit 3
    "Lesson 3.1: Polynomial Operations": "Lección 3.1: Operaciones Polinomiales",
    "Lesson 3.2: Factoring Polynomials": "Lección 3.2: Factorización de Polinomios",
    "Lesson 3.3: Synthetic Division": "Lección 3.3: División Sintética",
    "Lesson 3.4: Polynomial Graphs & Zeros": "Lección 3.4: Gráficos de Polinomios y Ceros",
    "Lesson 3.5: Remainder & Factor Theorems": "Lección 3.5: Teoremas del Resto y del Factor",
    "Lesson 3.6: Complex Numbers & Polynomial Roots": "Lección 3.6: Números Complejos y Raíces Polinomiales",
    "Lesson 3.7: Higher-Degree Polynomials": "Lección 3.7: Polinomios de Grado Superior",
    # Unit 4
    "Lesson 4.1: Rational Expressions": "Lección 4.1: Expresiones Racionales",
    "Lesson 4.2: Operations on Rational Expressions": "Lección 4.2: Operaciones en Expresiones Racionales",
    "Lesson 4.3: Rational Equations": "Lección 4.3: Ecuaciones Racionales",
    "Lesson 4.4: Graphing Rational Functions": "Lección 4.4: Gráficos de Funciones Racionales",
    "Lesson 4.5: Asymptotes & Discontinuities": "Lección 4.5: Asíntotas y Discontinuidades",
    "Lesson 4.6: Applications of Rational Functions": "Lección 4.6: Aplicaciones de Funciones Racionales",
    # Unit 5
    "Lesson 5.1: Exponential Functions & Growth": "Lección 5.1: Funciones Exponenciales y Crecimiento",
    "Lesson 5.2: Exponential Decay & Applications": "Lección 5.2: Decaimiento Exponencial y Aplicaciones",
    "Lesson 5.3: Logarithms & Properties": "Lección 5.3: Logaritmos y Propiedades",
    "Lesson 5.4: Logarithmic Functions & Graphs": "Lección 5.4: Funciones Logarítmicas y Gráficos",
    "Lesson 5.5: Exponential & Logarithmic Equations": "Lección 5.5: Ecuaciones Exponenciales y Logarítmicas",
    "Lesson 5.6: Applications of Exponentials & Logs": "Lección 5.6: Aplicaciones de Exponenciales y Logaritmos",
    "Lesson 5.7: Natural Logarithms & e": "Lección 5.7: Logaritmos Naturales y e",
    # Unit 6
    "Lesson 6.1: Arithmetic Sequences": "Lección 6.1: Secuencias Aritméticas",
    "Lesson 6.2: Geometric Sequences": "Lección 6.2: Secuencias Geométricas",
    "Lesson 6.3: Series & Summation Notation": "Lección 6.3: Series y Notación de Sumatoria",
    "Lesson 6.4: Infinite Geometric Series": "Lección 6.4: Series Geométricas Infinitas",
    "Lesson 6.5: Applications & Mathematical Induction": "Lección 6.5: Aplicaciones e Inducción Matemática",
    # Unit 7
    "Lesson 7.1: Counting Principles": "Lección 7.1: Principios de Conteo",
    "Lesson 7.2: Permutations & Combinations": "Lección 7.2: Permutaciones y Combinaciones",
    "Lesson 7.3: Probability Basics & Events": "Lección 7.3: Fundamentos de Probabilidad y Eventos",
    "Lesson 7.4: Conditional Probability": "Lección 7.4: Probabilidad Condicional",
    "Lesson 7.5: Normal Distributions": "Lección 7.5: Distribuciones Normales",
    "Lesson 7.6: Hypothesis Testing & Confidence Intervals": "Lección 7.6: Prueba de Hipótesis e Intervalos de Confianza",
    "Lesson 7.7: Correlation & Linear Regression": "Lección 7.7: Correlación y Regresión Lineal",
    # Unit 8
    "Lesson 8.1: Angles & Angle Measures": "Lección 8.1: Ángulos y Medidas de Ángulos",
    "Lesson 8.2: Unit Circle & Trigonometric Ratios": "Lección 8.2: Círculo Unitario y Razones Trigonométricas",
    "Lesson 8.3: Graphs of Trigonometric Functions": "Lección 8.3: Gráficos de Funciones Trigonométricas",
    "Lesson 8.4: Trigonometric Identities": "Lección 8.4: Identidades Trigonométricas",
    "Lesson 8.5: Solving Trigonometric Equations": "Lección 8.5: Resolución de Ecuaciones Trigonométricas",
    "Lesson 8.6: Applications of Trigonometry": "Lección 8.6: Aplicaciones de la Trigonometría",
    # Unit 9
    "Lesson 9.1: Conic Sections": "Lección 9.1: Secciones Cónicas",
    "Lesson 9.2: Parametric Equations": "Lección 9.2: Ecuaciones Paramétricas",
    "Lesson 9.3: Vectors & Vector Operations": "Lección 9.3: Vectores y Operaciones Vectoriales",
    "Lesson 9.4: Complex Numbers in Polar Form": "Lección 9.4: Números Complejos en Forma Polar",
}

def add_spanish_translations():
    """Add missing Spanish translations to spanish_translations.js"""
    spanish_file = "ArisEdu Project Folder/scripts/spanish_translations.js"
    
    with open(spanish_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    added_count = 0
    already_present = 0
    
    for key, translation in ALGEBRA2_LESSONS_SPANISH.items():
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
    
    print(f"✅ Added {added_count} Spanish translations for Algebra 2")
    print(f"⚠️  {already_present} translations already present")
    print(f"Total processed: {added_count + already_present}")

if __name__ == "__main__":
    add_spanish_translations()
