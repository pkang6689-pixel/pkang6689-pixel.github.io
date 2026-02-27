#!/usr/bin/env python3
"""Generate and inject missing translations for all three languages."""
import re, os, json

BASE = "ArisEdu Project Folder"

# ===============================================================
# MISSING TRANSLATIONS - CHINESE (Simplified)
# ===============================================================
missing_chinese = {
    # Unit labels
    "Unit 5A": "单元 5A",
    "Unit 5B": "单元 5B",
    
    # --- Dashboard / UI ---
    "Welcome back!": "欢迎回来！",
    "Top Performers": "优秀学员",
    "Dashboard - ArisEdu": "仪表板 - ArisEdu",
    "Achievements & Badges": "成就和徽章",
    "ArisEdu Logo": "ArisEdu 标志",
    
    # --- FAQ / Legal ---
    "FAQ - ArisEdu": "常见问题 - ArisEdu",
    "Frequently Asked Questions": "常见问题",
    "Terms of Service & Privacy Policy": "服务条款和隐私政策",
    "1. Introduction": "1. 引言",
    "2. Information We Collect": "2. 我们收集的信息",
    "3. How We Use Your Information": "3. 我们如何使用您的信息",
    "4. Sharing of Information": "4. 信息共享",
    "5. Cookies and Tracking": "5. Cookie 和追踪",
    "6. Data Security": "6. 数据安全",
    "7. Children's Privacy": "7. 儿童隐私",
    "8. Third-Party Links and Resources": "8. 第三方链接和资源",
    "9. Your Rights": "9. 您的权利",
    "10. Changes to This Policy": "10. 本政策的变更",
    "11. Contact Information": "11. 联系信息",
    "Still have questions?": "还有问题？",
    
    # --- Login ---
    "Login/Signup - ArisEdu": "登录/注册 - ArisEdu",
    "Get Started": "开始使用",
    
    # --- Preferences ---
    "Taskbar Settings": "任务栏设置",
    "Danger Zone": "危险区域",
    
    # --- Games ---
    "PAUSED": "已暂停",
    "Session Expired!": "会话已过期！",
    "Block Puzzle - Logic Challenge": "方块拼图 - 逻辑挑战",
    "Mix & Match - Vocabulary Game": "配对游戏 - 词汇游戏",
    "YOU WIN!": "你赢了！",
    "Pac-Man - Arcade": "吃豆人 - 街机",
    "LEVEL COMPLETE!": "关卡完成！",
    "Platformer - Arcade": "平台跳跃 - 街机",
    "Snake - Arcade": "贪吃蛇 - 街机",
    "DESTROYED": "被摧毁",
    "Space Shooter - Arcade": "太空射击 - 街机",
    "Tetris - Arcade": "俄罗斯方块 - 街机",
    
    # --- Forums ---
    "ArisEdu Forums": "ArisEdu 论坛",
    "Suggest a Feature": "建议功能",
    "Student Forums": "学生论坛",
    
    # --- Chemistry Lesson Keys (Units 10-12) ---
    "Key Concepts: Calculating pH and pOH using Log": "核心概念：使用对数计算 pH 和 pOH",
    "Key Concepts: Binary Acids vs Oxyacids": "核心概念：二元酸与含氧酸",
    "Key Concepts: Strong vs Weak Acids & Bases": "核心概念：强酸碱与弱酸碱",
    "Key Concepts: Naming Salts from Neutralization": "核心概念：中和反应命名盐",
    "Key Concepts: Buffer Solutions": "核心概念：缓冲溶液",
    "Key Concepts: Enthalpy Entropy Free Energy": "核心概念：焓、熵、自由能",
    "Key Concepts: Hess's Law": "核心概念：赫斯定律",
    "Mix &amp; Match": "配对游戏",
    
    # --- Algebra 1 popup strings ---
    "High School Algebra 1": "高中代数 1",
    "Systems with Quadratics": "二次方程组",
    "Multiplying Polynomials": "多项式乘法",
    "Outliers & Their Effects": "离群值及其影响",
    "Association in Categorical Data": "分类数据中的关联",
    "Compound Inequalities": "复合不等式",
    "Solving by Factoring — GCF & Grouping": "通过因式分解求解 — 最大公因数与分组",
    "Sample Spaces & Basic Probability": "样本空间与基本概率",
    "Graphing in Vertex Form": "顶点式作图",
    "Absolute Value Equations & Inequalities": "绝对值方程与不等式",
    "Quadratic Regression": "二次回归",
    "Arithmetic Sequences as Functions": "作为函数的等差数列",
    "Adding & Subtracting Rational Expressions": "有理表达式的加减",
    "Systems of Equations — Substitution & Elimination": "方程组 — 代入法与消元法",
    "Line of Best Fit": "最佳拟合线",
    "Systems of Inequalities": "不等式组",
    "Piecewise & Step Functions": "分段函数与阶梯函数",
    "Adding & Subtracting Polynomials": "多项式加减",
    "Function Transformations": "函数变换",
    "Relative Frequency": "相对频率",
    "Key Features of Parabolas": "抛物线的关键特征",
    "Probability with Combinatorics": "组合概率",
    "Graphing in Standard Form": "标准式作图",
    "Relations & Functions": "关系与函数",
    "Transformations of Quadratic Functions": "二次函数变换",
    "Exponential vs. Linear Models": "指数模型与线性模型",
    "Literal Equations": "字面方程",
    "Residuals & Residual Plots": "残差与残差图",
    "The Discriminant": "判别式",
    "Multiplying & Dividing Rational Expressions": "有理表达式的乘除",
    "Interpreting Exponential Models": "解读指数模型",
    "Describing Distributions": "描述分布",
    "Scatter Plots & Correlation": "散点图与相关性",
    "Compound Interest": "复利",
    "Solving Exponential Equations": "解指数方程",
    "Comparing Linear, Exponential, & Quadratic Models": "比较线性、指数和二次模型",
    "Box Plots & Dot Plots": "箱线图与点图",
    "Multi-Step Equations": "多步方程",
    "Recursive & Explicit Formulas": "递推公式与显式公式",
    "Correlation vs. Causation": "相关性与因果关系",
    "Independent & Dependent Events": "独立事件与相关事件",
    "Domain & Range": "定义域与值域",
    "Arithmetic & Geometric Sequences Review": "等差与等比数列复习",
    "Equations with Variables on Both Sides": "两边含变量的方程",
    "Evaluating & Interpreting Functions": "计算与解读函数",
    "Introduction to Series": "级数入门",
    "One-Step & Two-Step Equations": "一步与两步方程",
    "Exponential Equations from Tables & Graphs": "从表格和图形推导指数方程",
    "Special Products & Factoring Patterns": "特殊乘积与因式分解模式",
    "Exponential Regression": "指数回归",
    "Measures of Spread": "离散程度量",
    "One-Step & Two-Step Inequalities": "一步与两步不等式",
    "Dividing Polynomials": "多项式除法",
    "Two-Way Tables": "双向表",
    "Solving by Factoring — Trinomials": "通过因式分解求解 —三项式",
    "Rational Exponents": "有理指数",
    "Two-Way Frequency Tables": "双向频率表",
    "Rate of Change & Slope": "变化率与斜率",
    "Data Distributions": "数据分布",
    "Solving Radical Equations": "解根式方程",
    "Transformations of Exponential Functions": "指数函数变换",
    
    # --- Algebra 2 popup strings ---
    "High School Algebra 2": "高中代数 2",
    "1.1 Review of Functions & Notation": "1.1 函数与符号复习",
    "1.2 Linear Equations & Graphing": "1.2 线性方程与作图",
    "1.3 Systems of Linear Equations": "1.3 线性方程组",
    "1.4 Solving Systems by Substitution": "1.4 代入法解方程组",
    "1.5 Solving Systems by Elimination": "1.5 消元法解方程组",
    "1.6 Applications of Linear Systems": "1.6 线性方程组的应用",
    "1.7 Inequalities & System of Inequalities": "1.7 不等式与不等式组",
    "1.8 Linear Programming": "1.8 线性规划",
    "1.9 Advanced Linear Applications": "1.9 高级线性应用",
    "2.1 Quadratic Functions & Parabolas": "2.1 二次函数与抛物线",
    "2.2 Transformations of Quadratics": "2.2 二次函数变换",
    "2.3 Completing the Square": "2.3 完成平方",
    "2.4 Quadratic Formula & Discriminant": "2.4 二次公式与判别式",
    "2.5 Graphing Quadratic Functions": "2.5 二次函数作图",
    "2.6 Applications of Quadratics": "2.6 二次方程的应用",
    "2.7 Quadratic Inequalities": "2.7 二次不等式",
    "3.1 Polynomial Operations": "3.1 多项式运算",
    "3.2 Factoring Polynomials": "3.2 多项式因式分解",
    "3.3 Synthetic Division": "3.3 综合除法",
    "3.4 Polynomial Graphs & Zeros": "3.4 多项式图形与零点",
    "3.5 Remainder & Factor Theorems": "3.5 余式定理与因式定理",
    "3.6 Complex Numbers & Polynomial Roots": "3.6 复数与多项式根",
    "3.7 Higher-Degree Polynomials": "3.7 高次多项式",
    "4.1 Rational Expressions": "4.1 有理表达式",
    "4.2 Operations on Rational Expressions": "4.2 有理表达式运算",
    "4.3 Rational Equations": "4.3 有理方程",
    "4.4 Graphing Rational Functions": "4.4 有理函数作图",
    "4.5 Asymptotes & Discontinuities": "4.5 渐近线与间断点",
    "4.6 Applications of Rational Functions": "4.6 有理函数的应用",
    "5.1 Exponential Functions & Growth": "5.1 指数函数与增长",
    "5.2 Exponential Decay & Applications": "5.2 指数衰减与应用",
    "5.3 Logarithms & Properties": "5.3 对数与性质",
    "5.4 Logarithmic Functions & Graphs": "5.4 对数函数与图形",
    "5.5 Exponential & Logarithmic Equations": "5.5 指数与对数方程",
    "5.6 Applications of Exponentials & Logs": "5.6 指数与对数的应用",
    "5.7 Natural Logarithms & e": "5.7 自然对数与 e",
    "6.1 Arithmetic Sequences": "6.1 等差数列",
    "6.2 Geometric Sequences": "6.2 等比数列",
    "6.3 Series & Summation Notation": "6.3 级数与求和符号",
    "6.4 Infinite Geometric Series": "6.4 无穷等比级数",
    "6.5 Applications & Mathematical Induction": "6.5 应用与数学归纳法",
    "7.1 Counting Principles": "7.1 计数原理",
    "7.2 Permutations & Combinations": "7.2 排列与组合",
    "7.3 Probability Basics & Events": "7.3 概率基础与事件",
    "7.4 Conditional Probability": "7.4 条件概率",
    "7.5 Normal Distributions": "7.5 正态分布",
    "7.6 Hypothesis Testing & Confidence Intervals": "7.6 假设检验与置信区间",
    "7.7 Correlation & Linear Regression": "7.7 相关性与线性回归",
    "8.1 Angles & Angle Measures": "8.1 角与角度",
    "8.2 Unit Circle & Trigonometric Ratios": "8.2 单位圆与三角比",
    "8.3 Graphs of Trigonometric Functions": "8.3 三角函数图形",
    "8.4 Trigonometric Identities": "8.4 三角恒等式",
    "8.5 Solving Trigonometric Equations": "8.5 解三角方程",
    "8.6 Applications of Trigonometry": "8.6 三角学的应用",
    "9.1 Conic Sections": "9.1 圆锥曲线",
    "9.2 Parametric Equations": "9.2 参数方程",
    "9.3 Vectors & Vector Operations": "9.3 向量与向量运算",
    "9.4 Complex Numbers in Polar Form": "9.4 极坐标形式的复数",
    
    # --- Geometry popup strings ---
    "High School Geometry": "高中几何",
    "Lesson 2.2: Logic ⭐": "第 2.2 课：逻辑 ⭐",
    "Lesson 2.4: Deductive Reasoning ⭐": "第 2.4 课：演绎推理 ⭐",
    "Lesson 2.9: Proofs in Coordinate Geometry ⭐": "第 2.9 课：坐标几何中的证明 ⭐",
    "Lesson 3.7: Analytic Geometry Applications ⭐": "第 3.7 课：解析几何应用 ⭐",
    "Lesson 4.8: Triangles and Coordinate Proof ⭐": "第 4.8 课：三角形与坐标证明 ⭐",
    "Lesson 5.4: Indirect Proof ⭐": "第 5.4 课：间接证明 ⭐",
    "Lesson 6.2: Parallelograms": "第 6.2 课：平行四边形",
    "Lesson 6.7: Regular Polygons and Symmetry ⭐": "第 6.7 课：正多边形与对称性 ⭐",
    "Lesson 7.8: Fractals and Self-Similarity ⭐": "第 7.8 课：分形与自相似性 ⭐",
    "Lesson 8.4: Trigonometry ⭐": "第 8.4 课：三角学 ⭐",
    "Lesson 8.6: The Law of Sines and Cosines ⭐": "第 8.6 课：正弦与余弦定律 ⭐",
    "Lesson 8.7: Vectors ⭐": "第 8.7 课：向量 ⭐",
    "Lesson 8.8: Polar Coordinates and Complex Numbers ⭐": "第 8.8 课：极坐标与复数 ⭐",
    "Lesson 12.9: Cavalieri's Principle and Applications ⭐": "第 12.9 课：卡瓦列里原理及其应用 ⭐",
    
    # --- Physics popup strings ---
    "10.9 ⭐ Maxwell's Equations (introductory)": "10.9 ⭐ 麦克斯韦方程组（入门）",
    "6.6 ⭐ Kepler's Laws": "6.6 ⭐ 开普勒定律",
}

# ===============================================================
# MISSING TRANSLATIONS - SPANISH
# ===============================================================
missing_spanish = {
    "Unit 5A": "Unidad 5A",
    "Unit 5B": "Unidad 5B",
    
    # --- Dashboard / UI ---
    "Welcome back!": "¡Bienvenido de nuevo!",
    "Top Performers": "Mejores Estudiantes",
    "Dashboard - ArisEdu": "Panel de Control - ArisEdu",
    "Achievements & Badges": "Logros e Insignias",
    "Switch Account": "Cambiar Cuenta",
    "Choose Profile Picture": "Elegir Foto de Perfil",
    "ArisEdu Logo": "Logo de ArisEdu",
    
    # --- FAQ / Legal ---
    "FAQ - ArisEdu": "Preguntas Frecuentes - ArisEdu",
    "Frequently Asked Questions": "Preguntas Frecuentes",
    "Terms of Service & Privacy Policy": "Términos de Servicio y Política de Privacidad",
    "1. Introduction": "1. Introducción",
    "2. Information We Collect": "2. Información que Recopilamos",
    "3. How We Use Your Information": "3. Cómo Usamos Tu Información",
    "4. Sharing of Information": "4. Compartir Información",
    "5. Cookies and Tracking": "5. Cookies y Seguimiento",
    "6. Data Security": "6. Seguridad de Datos",
    "7. Children's Privacy": "7. Privacidad Infantil",
    "8. Third-Party Links and Resources": "8. Enlaces y Recursos de Terceros",
    "9. Your Rights": "9. Tus Derechos",
    "10. Changes to This Policy": "10. Cambios a Esta Política",
    "11. Contact Information": "11. Información de Contacto",
    "Still have questions?": "¿Aún tienes preguntas?",
    
    # --- Login ---
    "Login/Signup - ArisEdu": "Iniciar Sesión/Registrarse - ArisEdu",
    "Get Started": "Comenzar",
    
    # --- Preferences ---
    "Taskbar Settings": "Configuración de la Barra de Tareas",
    "Danger Zone": "Zona de Peligro",
    
    # --- Games ---
    "PAUSED": "PAUSADO",
    "Session Expired!": "¡Sesión Expirada!",
    "Block Puzzle - Logic Challenge": "Rompecabezas de Bloques - Desafío Lógico",
    "Mix & Match - Vocabulary Game": "Combinar y Emparejar - Juego de Vocabulario",
    "YOU WIN!": "¡GANASTE!",
    "Pac-Man - Arcade": "Pac-Man - Arcade",
    "LEVEL COMPLETE!": "¡NIVEL COMPLETADO!",
    "Platformer - Arcade": "Plataformas - Arcade",
    "Snake - Arcade": "Serpiente - Arcade",
    "DESTROYED": "DESTRUIDO",
    "Space Shooter - Arcade": "Disparos Espaciales - Arcade",
    "Tetris - Arcade": "Tetris - Arcade",
    
    # --- Forums ---
    "ArisEdu Forums": "Foros de ArisEdu",
    "Suggest a Feature": "Sugerir una Función",
    "Student Forums": "Foros de Estudiantes",
    
    # --- Chemistry ---
    "Key Concepts: Calculating pH and pOH using Log": "Conceptos Clave: Cálculo de pH y pOH usando Logaritmos",
    "Key Concepts: Binary Acids vs Oxyacids": "Conceptos Clave: Ácidos Binarios vs Oxoácidos",
    "Key Concepts: Strong vs Weak Acids & Bases": "Conceptos Clave: Ácidos y Bases Fuertes vs Débiles",
    "Key Concepts: Naming Salts from Neutralization": "Conceptos Clave: Nomenclatura de Sales de Neutralización",
    "Key Concepts: Buffer Solutions": "Conceptos Clave: Soluciones Amortiguadoras",
    "Key Concepts: Enthalpy Entropy Free Energy": "Conceptos Clave: Entalpía, Entropía, Energía Libre",
    "Key Concepts: Hess's Law": "Conceptos Clave: Ley de Hess",
    "Mix &amp; Match": "Combinar y Emparejar",
    
    # --- Algebra 1 ---
    "High School Algebra 1": "Álgebra 1 de Preparatoria",
    "Systems with Quadratics": "Sistemas con Cuadráticas",
    "Multiplying Polynomials": "Multiplicación de Polinomios",
    "Outliers & Their Effects": "Valores Atípicos y Sus Efectos",
    "Association in Categorical Data": "Asociación en Datos Categóricos",
    "Compound Inequalities": "Desigualdades Compuestas",
    "Solving by Factoring — GCF & Grouping": "Resolución por Factorización — MCD y Agrupación",
    "Sample Spaces & Basic Probability": "Espacios Muestrales y Probabilidad Básica",
    "Graphing in Vertex Form": "Graficación en Forma de Vértice",
    "Absolute Value Equations & Inequalities": "Ecuaciones e Inecuaciones con Valor Absoluto",
    "Quadratic Regression": "Regresión Cuadrática",
    "Arithmetic Sequences as Functions": "Secuencias Aritméticas como Funciones",
    "Adding & Subtracting Rational Expressions": "Suma y Resta de Expresiones Racionales",
    "Systems of Equations — Substitution & Elimination": "Sistemas de Ecuaciones — Sustitución y Eliminación",
    "Line of Best Fit": "Línea de Mejor Ajuste",
    "Systems of Inequalities": "Sistemas de Desigualdades",
    "Piecewise & Step Functions": "Funciones a Trozos y Escalonadas",
    "Adding & Subtracting Polynomials": "Suma y Resta de Polinomios",
    "Function Transformations": "Transformaciones de Funciones",
    "Relative Frequency": "Frecuencia Relativa",
    "Key Features of Parabolas": "Características Clave de Parábolas",
    "Probability with Combinatorics": "Probabilidad con Combinatoria",
    "Graphing in Standard Form": "Graficación en Forma Estándar",
    "Relations & Functions": "Relaciones y Funciones",
    "Transformations of Quadratic Functions": "Transformaciones de Funciones Cuadráticas",
    "Exponential vs. Linear Models": "Modelos Exponenciales vs. Lineales",
    "Literal Equations": "Ecuaciones Literales",
    "Residuals & Residual Plots": "Residuos y Gráficos de Residuos",
    "The Discriminant": "El Discriminante",
    "Multiplying & Dividing Rational Expressions": "Multiplicación y División de Expresiones Racionales",
    "Interpreting Exponential Models": "Interpretación de Modelos Exponenciales",
    "Describing Distributions": "Descripción de Distribuciones",
    "Scatter Plots & Correlation": "Diagramas de Dispersión y Correlación",
    "Compound Interest": "Interés Compuesto",
    "Solving Exponential Equations": "Resolución de Ecuaciones Exponenciales",
    "Comparing Linear, Exponential, & Quadratic Models": "Comparación de Modelos Lineales, Exponenciales y Cuadráticos",
    "Box Plots & Dot Plots": "Diagramas de Caja y Diagramas de Puntos",
    "Multi-Step Equations": "Ecuaciones de Varios Pasos",
    "Recursive & Explicit Formulas": "Fórmulas Recursivas y Explícitas",
    "Correlation vs. Causation": "Correlación vs. Causalidad",
    "Independent & Dependent Events": "Eventos Independientes y Dependientes",
    "Domain & Range": "Dominio y Rango",
    "Arithmetic & Geometric Sequences Review": "Repaso de Secuencias Aritméticas y Geométricas",
    "Equations with Variables on Both Sides": "Ecuaciones con Variables en Ambos Lados",
    "Evaluating & Interpreting Functions": "Evaluación e Interpretación de Funciones",
    "Introduction to Series": "Introducción a las Series",
    "One-Step & Two-Step Equations": "Ecuaciones de Uno y Dos Pasos",
    "Exponential Equations from Tables & Graphs": "Ecuaciones Exponenciales a partir de Tablas y Gráficas",
    "Special Products & Factoring Patterns": "Productos Especiales y Patrones de Factorización",
    "Exponential Regression": "Regresión Exponencial",
    "Measures of Spread": "Medidas de Dispersión",
    "One-Step & Two-Step Inequalities": "Desigualdades de Uno y Dos Pasos",
    "Dividing Polynomials": "División de Polinomios",
    "Two-Way Tables": "Tablas de Doble Entrada",
    "Solving by Factoring — Trinomials": "Resolución por Factorización — Trinomios",
    "Rational Exponents": "Exponentes Racionales",
    "Two-Way Frequency Tables": "Tablas de Frecuencia de Doble Entrada",
    "Rate of Change & Slope": "Tasa de Cambio y Pendiente",
    "Data Distributions": "Distribuciones de Datos",
    "Solving Radical Equations": "Resolución de Ecuaciones Radicales",
    "Transformations of Exponential Functions": "Transformaciones de Funciones Exponenciales",
    
    # --- Algebra 2 ---
    "High School Algebra 2": "Álgebra 2 de Preparatoria",
    "1.1 Review of Functions & Notation": "1.1 Repaso de Funciones y Notación",
    "1.2 Linear Equations & Graphing": "1.2 Ecuaciones Lineales y Graficación",
    "1.3 Systems of Linear Equations": "1.3 Sistemas de Ecuaciones Lineales",
    "1.4 Solving Systems by Substitution": "1.4 Resolución de Sistemas por Sustitución",
    "1.5 Solving Systems by Elimination": "1.5 Resolución de Sistemas por Eliminación",
    "1.6 Applications of Linear Systems": "1.6 Aplicaciones de Sistemas Lineales",
    "1.7 Inequalities & System of Inequalities": "1.7 Desigualdades y Sistemas de Desigualdades",
    "1.8 Linear Programming": "1.8 Programación Lineal",
    "1.9 Advanced Linear Applications": "1.9 Aplicaciones Lineales Avanzadas",
    "2.1 Quadratic Functions & Parabolas": "2.1 Funciones Cuadráticas y Parábolas",
    "2.2 Transformations of Quadratics": "2.2 Transformaciones de Cuadráticas",
    "2.3 Completing the Square": "2.3 Completar el Cuadrado",
    "2.4 Quadratic Formula & Discriminant": "2.4 Fórmula Cuadrática y Discriminante",
    "2.5 Graphing Quadratic Functions": "2.5 Graficación de Funciones Cuadráticas",
    "2.6 Applications of Quadratics": "2.6 Aplicaciones de Cuadráticas",
    "2.7 Quadratic Inequalities": "2.7 Desigualdades Cuadráticas",
    "3.1 Polynomial Operations": "3.1 Operaciones con Polinomios",
    "3.2 Factoring Polynomials": "3.2 Factorización de Polinomios",
    "3.3 Synthetic Division": "3.3 División Sintética",
    "3.4 Polynomial Graphs & Zeros": "3.4 Gráficas de Polinomios y Ceros",
    "3.5 Remainder & Factor Theorems": "3.5 Teorema del Residuo y del Factor",
    "3.6 Complex Numbers & Polynomial Roots": "3.6 Números Complejos y Raíces de Polinomios",
    "3.7 Higher-Degree Polynomials": "3.7 Polinomios de Grado Superior",
    "4.1 Rational Expressions": "4.1 Expresiones Racionales",
    "4.2 Operations on Rational Expressions": "4.2 Operaciones con Expresiones Racionales",
    "4.3 Rational Equations": "4.3 Ecuaciones Racionales",
    "4.4 Graphing Rational Functions": "4.4 Graficación de Funciones Racionales",
    "4.5 Asymptotes & Discontinuities": "4.5 Asíntotas y Discontinuidades",
    "4.6 Applications of Rational Functions": "4.6 Aplicaciones de Funciones Racionales",
    "5.1 Exponential Functions & Growth": "5.1 Funciones Exponenciales y Crecimiento",
    "5.2 Exponential Decay & Applications": "5.2 Decaimiento Exponencial y Aplicaciones",
    "5.3 Logarithms & Properties": "5.3 Logaritmos y Propiedades",
    "5.4 Logarithmic Functions & Graphs": "5.4 Funciones Logarítmicas y Gráficas",
    "5.5 Exponential & Logarithmic Equations": "5.5 Ecuaciones Exponenciales y Logarítmicas",
    "5.6 Applications of Exponentials & Logs": "5.6 Aplicaciones de Exponenciales y Logaritmos",
    "5.7 Natural Logarithms & e": "5.7 Logaritmos Naturales y e",
    "6.1 Arithmetic Sequences": "6.1 Secuencias Aritméticas",
    "6.2 Geometric Sequences": "6.2 Secuencias Geométricas",
    "6.3 Series & Summation Notation": "6.3 Series y Notación de Sumatoria",
    "6.4 Infinite Geometric Series": "6.4 Series Geométricas Infinitas",
    "6.5 Applications & Mathematical Induction": "6.5 Aplicaciones e Inducción Matemática",
    "7.1 Counting Principles": "7.1 Principios de Conteo",
    "7.2 Permutations & Combinations": "7.2 Permutaciones y Combinaciones",
    "7.3 Probability Basics & Events": "7.3 Probabilidad Básica y Eventos",
    "7.4 Conditional Probability": "7.4 Probabilidad Condicional",
    "7.5 Normal Distributions": "7.5 Distribuciones Normales",
    "7.6 Hypothesis Testing & Confidence Intervals": "7.6 Prueba de Hipótesis e Intervalos de Confianza",
    "7.7 Correlation & Linear Regression": "7.7 Correlación y Regresión Lineal",
    "8.1 Angles & Angle Measures": "8.1 Ángulos y Medidas de Ángulos",
    "8.2 Unit Circle & Trigonometric Ratios": "8.2 Círculo Unitario y Razones Trigonométricas",
    "8.3 Graphs of Trigonometric Functions": "8.3 Gráficas de Funciones Trigonométricas",
    "8.4 Trigonometric Identities": "8.4 Identidades Trigonométricas",
    "8.5 Solving Trigonometric Equations": "8.5 Resolución de Ecuaciones Trigonométricas",
    "8.6 Applications of Trigonometry": "8.6 Aplicaciones de Trigonometría",
    "9.1 Conic Sections": "9.1 Secciones Cónicas",
    "9.2 Parametric Equations": "9.2 Ecuaciones Paramétricas",
    "9.3 Vectors & Vector Operations": "9.3 Vectores y Operaciones con Vectores",
    "9.4 Complex Numbers in Polar Form": "9.4 Números Complejos en Forma Polar",
    
    # --- Geometry ---
    "High School Geometry": "Geometría de Preparatoria",
    "Lesson 2.2: Logic ⭐": "Lección 2.2: Lógica ⭐",
    "Lesson 2.4: Deductive Reasoning ⭐": "Lección 2.4: Razonamiento Deductivo ⭐",
    "Lesson 2.9: Proofs in Coordinate Geometry ⭐": "Lección 2.9: Demostraciones en Geometría Analítica ⭐",
    "Lesson 3.7: Analytic Geometry Applications ⭐": "Lección 3.7: Aplicaciones de Geometría Analítica ⭐",
    "Lesson 4.8: Triangles and Coordinate Proof ⭐": "Lección 4.8: Triángulos y Demostración Analítica ⭐",
    "Lesson 5.4: Indirect Proof ⭐": "Lección 5.4: Demostración Indirecta ⭐",
    "Lesson 6.2: Parallelograms": "Lección 6.2: Paralelogramos",
    "Lesson 6.7: Regular Polygons and Symmetry ⭐": "Lección 6.7: Polígonos Regulares y Simetría ⭐",
    "Lesson 7.8: Fractals and Self-Similarity ⭐": "Lección 7.8: Fractales y Autosimilitud ⭐",
    "Lesson 8.4: Trigonometry ⭐": "Lección 8.4: Trigonometría ⭐",
    "Lesson 8.6: The Law of Sines and Cosines ⭐": "Lección 8.6: Ley de Senos y Cosenos ⭐",
    "Lesson 8.7: Vectors ⭐": "Lección 8.7: Vectores ⭐",
    "Lesson 8.8: Polar Coordinates and Complex Numbers ⭐": "Lección 8.8: Coordenadas Polares y Números Complejos ⭐",
    "Lesson 12.9: Cavalieri's Principle and Applications ⭐": "Lección 12.9: Principio de Cavalieri y Aplicaciones ⭐",
    
    # --- Physics ---
    "10.9 ⭐ Maxwell's Equations (introductory)": "10.9 ⭐ Ecuaciones de Maxwell (introducción)",
    "6.6 ⭐ Kepler's Laws": "6.6 ⭐ Leyes de Kepler",
    
    # --- Arcade ---
    "Arcade": "Arcade",
}

# ===============================================================
# MISSING TRANSLATIONS - HINDI
# ===============================================================
missing_hindi = {
    "Unit 5A": "इकाई 5A",
    "Unit 5B": "इकाई 5B",
    
    # --- Dashboard / UI ---
    "Welcome back!": "वापसी पर स्वागत है!",
    "Top Performers": "शीर्ष प्रदर्शनकर्ता",
    "Dashboard - ArisEdu": "डैशबोर्ड - ArisEdu",
    "Achievements & Badges": "उपलब्धियाँ और बैज",
    "Switch Account": "खाता बदलें",
    "Choose Profile Picture": "प्रोफ़ाइल चित्र चुनें",
    "ArisEdu Logo": "ArisEdu लोगो",
    
    # --- FAQ / Legal ---
    "FAQ - ArisEdu": "अक्सर पूछे जाने वाले प्रश्न - ArisEdu",
    "Frequently Asked Questions": "अक्सर पूछे जाने वाले प्रश्न",
    "Terms of Service & Privacy Policy": "सेवा की शर्तें और गोपनीयता नीति",
    "1. Introduction": "1. परिचय",
    "2. Information We Collect": "2. हम जो जानकारी एकत्र करते हैं",
    "3. How We Use Your Information": "3. हम आपकी जानकारी का उपयोग कैसे करते हैं",
    "4. Sharing of Information": "4. जानकारी साझा करना",
    "5. Cookies and Tracking": "5. कुकीज़ और ट्रैकिंग",
    "6. Data Security": "6. डेटा सुरक्षा",
    "7. Children's Privacy": "7. बच्चों की गोपनीयता",
    "8. Third-Party Links and Resources": "8. तृतीय-पक्ष लिंक और संसाधन",
    "9. Your Rights": "9. आपके अधिकार",
    "10. Changes to This Policy": "10. इस नीति में परिवर्तन",
    "11. Contact Information": "11. संपर्क जानकारी",
    "Still have questions?": "अभी भी प्रश्न हैं?",
    
    # --- Login ---
    "Login/Signup - ArisEdu": "लॉगिन/साइनअप - ArisEdu",
    "Get Started": "शुरू करें",
    
    # --- Preferences ---
    "Taskbar Settings": "टास्कबार सेटिंग्स",
    "Danger Zone": "खतरे का क्षेत्र",
    
    # --- Games ---
    "PAUSED": "रुका हुआ",
    "Session Expired!": "सत्र समाप्त!",
    "Block Puzzle - Logic Challenge": "ब्लॉक पहेली - तर्क चुनौती",
    "Mix & Match - Vocabulary Game": "मिलान खेल - शब्दावली खेल",
    "YOU WIN!": "आप जीत गए!",
    "Pac-Man - Arcade": "पैक-मैन - आर्केड",
    "LEVEL COMPLETE!": "स्तर पूरा!",
    "Platformer - Arcade": "प्लेटफ़ॉर्मर - आर्केड",
    "Snake - Arcade": "सांप - आर्केड",
    "DESTROYED": "नष्ट",
    "Space Shooter - Arcade": "अंतरिक्ष शूटर - आर्केड",
    "Tetris - Arcade": "टेट्रिस - आर्केड",
    
    # --- Forums ---
    "ArisEdu Forums": "ArisEdu फ़ोरम",
    "Suggest a Feature": "सुविधा सुझाएँ",
    "Student Forums": "छात्र फ़ोरम",
    
    # --- Chemistry ---
    "Key Concepts: Calculating pH and pOH using Log": "मुख्य अवधारणाएँ: लॉग का उपयोग करके pH और pOH की गणना",
    "Key Concepts: Binary Acids vs Oxyacids": "मुख्य अवधारणाएँ: बाइनरी अम्ल बनाम ऑक्सीअम्ल",
    "Key Concepts: Strong vs Weak Acids & Bases": "मुख्य अवधारणाएँ: प्रबल बनाम दुर्बल अम्ल और क्षार",
    "Key Concepts: Naming Salts from Neutralization": "मुख्य अवधारणाएँ: उदासीनीकरण से लवण का नामकरण",
    "Key Concepts: Buffer Solutions": "मुख्य अवधारणाएँ: बफर विलयन",
    "Key Concepts: Enthalpy Entropy Free Energy": "मुख्य अवधारणाएँ: एन्थैल्पी, एन्ट्रॉपी, मुक्त ऊर्जा",
    "Key Concepts: Hess's Law": "मुख्य अवधारणाएँ: हेस का नियम",
    "Mix &amp; Match": "मिलान खेल",
    
    # --- Algebra 1 ---
    "High School Algebra 1": "हाई स्कूल बीजगणित 1",
    "Systems with Quadratics": "द्विघात समीकरण निकाय",
    "Multiplying Polynomials": "बहुपदों का गुणन",
    "Outliers & Their Effects": "बाह्य मान और उनके प्रभाव",
    "Association in Categorical Data": "श्रेणीबद्ध डेटा में संबंध",
    "Compound Inequalities": "संयुक्त असमिकाएँ",
    "Solving by Factoring — GCF & Grouping": "गुणनखंडन द्वारा हल — म.स.प. और समूहन",
    "Sample Spaces & Basic Probability": "प्रतिदर्श स्थान और मूल प्रायिकता",
    "Graphing in Vertex Form": "शीर्ष रूप में ग्राफ बनाना",
    "Absolute Value Equations & Inequalities": "निरपेक्ष मान समीकरण और असमिकाएँ",
    "Quadratic Regression": "द्विघात प्रतिगमन",
    "Arithmetic Sequences as Functions": "फलन के रूप में समांतर श्रेणी",
    "Adding & Subtracting Rational Expressions": "परिमेय व्यंजकों का योग और व्यवकलन",
    "Systems of Equations — Substitution & Elimination": "समीकरण निकाय — प्रतिस्थापन और विलोपन",
    "Line of Best Fit": "सर्वोत्तम फिट रेखा",
    "Systems of Inequalities": "असमिका निकाय",
    "Piecewise & Step Functions": "खंडशः और सोपान फलन",
    "Adding & Subtracting Polynomials": "बहुपदों का योग और व्यवकलन",
    "Function Transformations": "फलन रूपांतरण",
    "Relative Frequency": "सापेक्ष आवृत्ति",
    "Key Features of Parabolas": "परवलय की प्रमुख विशेषताएँ",
    "Probability with Combinatorics": "क्रम-संयोजन के साथ प्रायिकता",
    "Graphing in Standard Form": "मानक रूप में ग्राफ बनाना",
    "Relations & Functions": "संबंध और फलन",
    "Transformations of Quadratic Functions": "द्विघात फलनों का रूपांतरण",
    "Exponential vs. Linear Models": "चरघातांकी बनाम रैखिक मॉडल",
    "Literal Equations": "शाब्दिक समीकरण",
    "Residuals & Residual Plots": "अवशिष्ट और अवशिष्ट आलेख",
    "The Discriminant": "विविक्तकर",
    "Multiplying & Dividing Rational Expressions": "परिमेय व्यंजकों का गुणन और भाग",
    "Interpreting Exponential Models": "चरघातांकी मॉडलों की व्याख्या",
    "Describing Distributions": "वितरणों का वर्णन",
    "Scatter Plots & Correlation": "प्रकीर्ण आलेख और सहसंबंध",
    "Compound Interest": "चक्रवृद्धि ब्याज",
    "Solving Exponential Equations": "चरघातांकी समीकरण हल करना",
    "Comparing Linear, Exponential, & Quadratic Models": "रैखिक, चरघातांकी और द्विघात मॉडलों की तुलना",
    "Box Plots & Dot Plots": "बॉक्स प्लॉट और डॉट प्लॉट",
    "Multi-Step Equations": "बहु-चरण समीकरण",
    "Recursive & Explicit Formulas": "पुनरावर्ती और स्पष्ट सूत्र",
    "Correlation vs. Causation": "सहसंबंध बनाम कारण",
    "Independent & Dependent Events": "स्वतंत्र और आश्रित घटनाएँ",
    "Domain & Range": "प्रांत और परिसर",
    "Arithmetic & Geometric Sequences Review": "समांतर और गुणोत्तर श्रेणी समीक्षा",
    "Equations with Variables on Both Sides": "दोनों तरफ चरों वाले समीकरण",
    "Evaluating & Interpreting Functions": "फलनों का मूल्यांकन और व्याख्या",
    "Introduction to Series": "श्रेणी का परिचय",
    "One-Step & Two-Step Equations": "एक-चरण और दो-चरण समीकरण",
    "Exponential Equations from Tables & Graphs": "तालिकाओं और ग्राफ से चरघातांकी समीकरण",
    "Special Products & Factoring Patterns": "विशेष गुणनफल और गुणनखंडन पैटर्न",
    "Exponential Regression": "चरघातांकी प्रतिगमन",
    "Measures of Spread": "विस्तार की माप",
    "One-Step & Two-Step Inequalities": "एक-चरण और दो-चरण असमिकाएँ",
    "Dividing Polynomials": "बहुपदों का भाग",
    "Two-Way Tables": "द्विमार्गी सारणी",
    "Solving by Factoring — Trinomials": "गुणनखंडन द्वारा हल — त्रिपद",
    "Rational Exponents": "परिमेय घातांक",
    "Two-Way Frequency Tables": "द्विमार्गी आवृत्ति सारणी",
    "Rate of Change & Slope": "परिवर्तन की दर और ढाल",
    "Data Distributions": "डेटा वितरण",
    "Solving Radical Equations": "मूलक समीकरण हल करना",
    "Transformations of Exponential Functions": "चरघातांकी फलनों का रूपांतरण",
    
    # --- Algebra 2 ---
    "High School Algebra 2": "हाई स्कूल बीजगणित 2",
    "1.1 Review of Functions & Notation": "1.1 फलन और संकेतन की समीक्षा",
    "1.2 Linear Equations & Graphing": "1.2 रैखिक समीकरण और ग्राफ बनाना",
    "1.3 Systems of Linear Equations": "1.3 रैखिक समीकरण निकाय",
    "1.4 Solving Systems by Substitution": "1.4 प्रतिस्थापन द्वारा निकाय हल करना",
    "1.5 Solving Systems by Elimination": "1.5 विलोपन द्वारा निकाय हल करना",
    "1.6 Applications of Linear Systems": "1.6 रैखिक निकायों के अनुप्रयोग",
    "1.7 Inequalities & System of Inequalities": "1.7 असमिकाएँ और असमिका निकाय",
    "1.8 Linear Programming": "1.8 रैखिक प्रोग्रामिंग",
    "1.9 Advanced Linear Applications": "1.9 उन्नत रैखिक अनुप्रयोग",
    "2.1 Quadratic Functions & Parabolas": "2.1 द्विघात फलन और परवलय",
    "2.2 Transformations of Quadratics": "2.2 द्विघात रूपांतरण",
    "2.3 Completing the Square": "2.3 वर्ग पूर्ण करना",
    "2.4 Quadratic Formula & Discriminant": "2.4 द्विघात सूत्र और विविक्तकर",
    "2.5 Graphing Quadratic Functions": "2.5 द्विघात फलनों का ग्राफ बनाना",
    "2.6 Applications of Quadratics": "2.6 द्विघात के अनुप्रयोग",
    "2.7 Quadratic Inequalities": "2.7 द्विघात असमिकाएँ",
    "3.1 Polynomial Operations": "3.1 बहुपद संक्रियाएँ",
    "3.2 Factoring Polynomials": "3.2 बहुपदों का गुणनखंडन",
    "3.3 Synthetic Division": "3.3 संश्लिष्ट भाग",
    "3.4 Polynomial Graphs & Zeros": "3.4 बहुपद ग्राफ और शून्यक",
    "3.5 Remainder & Factor Theorems": "3.5 शेषफल और गुणनखंड प्रमेय",
    "3.6 Complex Numbers & Polynomial Roots": "3.6 सम्मिश्र संख्याएँ और बहुपद मूल",
    "3.7 Higher-Degree Polynomials": "3.7 उच्च घात बहुपद",
    "4.1 Rational Expressions": "4.1 परिमेय व्यंजक",
    "4.2 Operations on Rational Expressions": "4.2 परिमेय व्यंजकों पर संक्रियाएँ",
    "4.3 Rational Equations": "4.3 परिमेय समीकरण",
    "4.4 Graphing Rational Functions": "4.4 परिमेय फलनों का ग्राफ बनाना",
    "4.5 Asymptotes & Discontinuities": "4.5 अनंतस्पर्शी और असंतत",
    "4.6 Applications of Rational Functions": "4.6 परिमेय फलनों के अनुप्रयोग",
    "5.1 Exponential Functions & Growth": "5.1 चरघातांकी फलन और वृद्धि",
    "5.2 Exponential Decay & Applications": "5.2 चरघातांकी क्षय और अनुप्रयोग",
    "5.3 Logarithms & Properties": "5.3 लघुगणक और गुणधर्म",
    "5.4 Logarithmic Functions & Graphs": "5.4 लघुगणकीय फलन और ग्राफ",
    "5.5 Exponential & Logarithmic Equations": "5.5 चरघातांकी और लघुगणकीय समीकरण",
    "5.6 Applications of Exponentials & Logs": "5.6 चरघातांकी और लघुगणक के अनुप्रयोग",
    "5.7 Natural Logarithms & e": "5.7 प्राकृतिक लघुगणक और e",
    "6.1 Arithmetic Sequences": "6.1 समांतर श्रेणी",
    "6.2 Geometric Sequences": "6.2 गुणोत्तर श्रेणी",
    "6.3 Series & Summation Notation": "6.3 श्रेणी और योग संकेतन",
    "6.4 Infinite Geometric Series": "6.4 अनंत गुणोत्तर श्रेणी",
    "6.5 Applications & Mathematical Induction": "6.5 अनुप्रयोग और गणितीय आगमन",
    "7.1 Counting Principles": "7.1 गणना सिद्धांत",
    "7.2 Permutations & Combinations": "7.2 क्रमचय और संचय",
    "7.3 Probability Basics & Events": "7.3 प्रायिकता मूल बातें और घटनाएँ",
    "7.4 Conditional Probability": "7.4 सशर्त प्रायिकता",
    "7.5 Normal Distributions": "7.5 सामान्य वितरण",
    "7.6 Hypothesis Testing & Confidence Intervals": "7.6 परिकल्पना परीक्षण और विश्वास अंतराल",
    "7.7 Correlation & Linear Regression": "7.7 सहसंबंध और रैखिक प्रतिगमन",
    "8.1 Angles & Angle Measures": "8.1 कोण और कोण माप",
    "8.2 Unit Circle & Trigonometric Ratios": "8.2 इकाई वृत्त और त्रिकोणमितीय अनुपात",
    "8.3 Graphs of Trigonometric Functions": "8.3 त्रिकोणमितीय फलनों के ग्राफ",
    "8.4 Trigonometric Identities": "8.4 त्रिकोणमितीय सर्वसमिकाएँ",
    "8.5 Solving Trigonometric Equations": "8.5 त्रिकोणमितीय समीकरण हल करना",
    "8.6 Applications of Trigonometry": "8.6 त्रिकोणमिति के अनुप्रयोग",
    "9.1 Conic Sections": "9.1 शंक्वाकार खंड",
    "9.2 Parametric Equations": "9.2 प्राचलिक समीकरण",
    "9.3 Vectors & Vector Operations": "9.3 सदिश और सदिश संक्रियाएँ",
    "9.4 Complex Numbers in Polar Form": "9.4 ध्रुवीय रूप में सम्मिश्र संख्याएँ",
    
    # --- Geometry ---
    "High School Geometry": "हाई स्कूल ज्यामिति",
    "Lesson 2.2: Logic ⭐": "पाठ 2.2: तर्कशास्त्र ⭐",
    "Lesson 2.4: Deductive Reasoning ⭐": "पाठ 2.4: निगमनात्मक तर्क ⭐",
    "Lesson 2.9: Proofs in Coordinate Geometry ⭐": "पाठ 2.9: निर्देशांक ज्यामिति में प्रमाण ⭐",
    "Lesson 3.7: Analytic Geometry Applications ⭐": "पाठ 3.7: विश्लेषणात्मक ज्यामिति अनुप्रयोग ⭐",
    "Lesson 4.8: Triangles and Coordinate Proof ⭐": "पाठ 4.8: त्रिभुज और निर्देशांक प्रमाण ⭐",
    "Lesson 5.4: Indirect Proof ⭐": "पाठ 5.4: अप्रत्यक्ष प्रमाण ⭐",
    "Lesson 6.2: Parallelograms": "पाठ 6.2: समांतर चतुर्भुज",
    "Lesson 6.7: Regular Polygons and Symmetry ⭐": "पाठ 6.7: सम बहुभुज और समरूपता ⭐",
    "Lesson 7.8: Fractals and Self-Similarity ⭐": "पाठ 7.8: भग्न और स्व-समरूपता ⭐",
    "Lesson 8.4: Trigonometry ⭐": "पाठ 8.4: त्रिकोणमिति ⭐",
    "Lesson 8.6: The Law of Sines and Cosines ⭐": "पाठ 8.6: ज्या और कोज्या का नियम ⭐",
    "Lesson 8.7: Vectors ⭐": "पाठ 8.7: सदिश ⭐",
    "Lesson 8.8: Polar Coordinates and Complex Numbers ⭐": "पाठ 8.8: ध्रुवीय निर्देशांक और सम्मिश्र संख्याएँ ⭐",
    "Lesson 12.9: Cavalieri's Principle and Applications ⭐": "पाठ 12.9: कैवेलिएरी सिद्धांत और अनुप्रयोग ⭐",
    
    # --- Physics ---
    "10.9 ⭐ Maxwell's Equations (introductory)": "10.9 ⭐ मैक्सवेल के समीकरण (परिचयात्मक)",
    "6.6 ⭐ Kepler's Laws": "6.6 ⭐ केप्लर के नियम",
    
    # --- Arcade ---
    "Arcade": "आर्केड",
}


def format_js_entry(key, value):
    """Format a single key:value pair for JS object."""
    # Escape double quotes in key and value
    k = key.replace('\\', '\\\\').replace('"', '\\"')
    v = value.replace('\\', '\\\\').replace('"', '\\"')
    return f'    "{k}": "{v}"'


def inject_translations(filepath, marker_before, entries):
    """Inject new translation entries before the closing marker in the file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the marker line and inject before it
    idx = content.rfind(marker_before)
    if idx == -1:
        print(f"  ERROR: Could not find marker '{marker_before}' in {filepath}")
        return False
    
    # Build the injection string
    lines = []
    for key, value in entries.items():
        lines.append(format_js_entry(key, value))
    
    injection = ",\n" + ",\n".join(lines) + "\n"
    
    # Find the last entry before marker (should end with a quote possibly followed by newline)
    # We look for the position just before the marker
    new_content = content[:idx].rstrip()
    # Remove trailing comma if present
    if new_content.endswith(','):
        new_content = new_content[:-1]
    
    new_content += injection + content[idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


# Inject into Chinese (global_translations.js)
print("Injecting Chinese translations...")
zh_path = os.path.join(BASE, "scripts", "global_translations.js")
# The Chinese dict ends with: }; followed by window.arisEduTranslations
if inject_translations(zh_path, "    };\n\n    // ── Expose Chinese translations globally", missing_chinese):
    print(f"  Added {len(missing_chinese)} Chinese entries")

# Inject into Spanish
print("Injecting Spanish translations...")
es_path = os.path.join(BASE, "scripts", "spanish_translations.js")
if inject_translations(es_path, "};\n\n    // Export to global scope\n    if (typeof spanishTranslations", missing_spanish):
    print(f"  Added {len(missing_spanish)} Spanish entries")

# Inject into Hindi
print("Injecting Hindi translations...")
hi_path = os.path.join(BASE, "scripts", "hindi_translations.js")
if inject_translations(hi_path, "};\n\n    // Export to global scope\n    if (typeof hindiTranslations", missing_hindi):
    print(f"  Added {len(missing_hindi)} Hindi entries")

print("\nDone! Run audit again to verify.")
