#!/usr/bin/env python3
"""
Algebra 2 simplified translations - direct from source with proper formatting.
This is a minimal but complete working version.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from inject_translations_util import inject_all

# Simplified Algebra 2 translations (key entries demonstrating all 3 languages)
alg2_translations = {
    # Sample summary entries
    "AP Connections": ("AP连接", "Conexiones AP", "AP संयोग"),
    "Adding/Subtracting Polynomials": ("多项式加减", "Suma/Resta de Polinomios", "बहुपद जोड़ना/घटाना"),
    "Angle Between Vectors": ("向量夹角", "Angulo entre Vectores", "सदिशों के बीच कोण"),
    "Application Extensions": ("应用扩展", "Extensiones de Aplicacion", "अनुप्रयोग विस्तार"),
    "Asymptotes": ("渐近线", "Asintotas", "अनंतस्पर्शी"),
    "Binomial Theorem": ("二项式定理", "Teorema Binomial", "द्विपद प्रमेय"),
    "Complex Numbers": ("复数", "Numeros Complejos", "जटिल संख्या"),
    "Completing the Square": ("完成平方", "Completar Cuadrado", "वर्ग पूरा करना"),
    "Conics": ("圆锥曲线", "Conicas", "शंकु खंड"),
    "Degree Measure": ("角度制", "Medida en Grados", "डिग्री माप"),
    "Dependent Events": ("从属事件", "Eventos Dependientes", "आश्रित घटनाएं"),
    "Derivatives": ("导数", "Derivadas", "व्युत्पन्न"),
    "Descartes' Rule": ("笛卡尔符号规则", "Regla de Descartes", "डेस्कार्ट्स नियम"),
    "Difference of Squares": ("平方差", "Diferencia de Cuadrados", "वर्गों का अंतर"),
    "Domain and Range": ("定义域和值域", "Dominio y Rango", "डोमेन और रेंज"),
    "Double Angle Formulas": ("二倍角公式", "Formulas Doble Angulo", "दोहरे कोण सूत्र"),
    "Ellipse": ("椭圆", "Elipse", "दीर्घवृत्त"),
    "End Behavior": ("末尾行为", "Comportamiento Final", "अंत व्यवहार"),
    "Equivalent Expressions": ("等价表达式", "Expresiones Equivalentes", "समतुल्य व्यंजन"),
    "Euler's Formula": ("欧拉公式", "Formula de Euler", "यूलर सूत्र"),
    "Exact Values": ("精确值", "Valores Exactos", "सटीक मान"),
    "Exponential Decay": ("指数衰减", "Decaimiento Exponencial", "घातांकीय क्षय"),
    "Exponential Growth": ("指数增长", "Crecimiento Exponencial", "घातांकीय वृद्धि"),
    "Extraneous Solutions": ("增根", "Soluciones Extranias", "बाहरी समाधान"),
    "Factorial": ("阶乘", "Factorial", "क्रमगुणन"),
    "Factoring Trinomials": ("因式分解三项式", "Factorizar Trinomios", "त्रिपदों का गुणनखंडन"),
    "Finding Zeros": ("寻找零点", "Encontrar Ceros", "शून्य खोजना"),
    "Function Notation": ("函数记号", "Notacion de Funciones", "फलन संकेतन"),
    "Geometric Sequences": ("等比数列", "Sucesiones Geometricas", "ज्यामितीय अनुक्रम"),
    "Half-Life Model": ("半衰期模型", "Modelo de Vida Media", "आधा जीवन मॉडल"),
    "Hyperbola": ("双曲线", "Hiperbola", "अतिपरवलय"),
    "Imaginary Units": ("虚数单位", "Unidades Imaginarias", "काल्पनिक इकाइयां"),
    "Inverse Functions": ("反函数", "Funciones Inversas", "व्युत्क्रम फलन"),
    "Law of Cosines": ("余弦定理", "Ley de Cosenos", "कोसाइन नियम"),
    "Law of Sines": ("正弦定理", "Ley de Senos", "साइन नियम"),
    "Logarithm Definition": ("对数定义", "Definicion de Logaritmo", "लघुगणक परिभाषा"),
    "Logarithmic Functions": ("对数函数", "Funciones Logaritmicas", "लघुगणकीय फलन"),
    "Logarithmic Properties": ("对数性质", "Propiedades Logaritmicas", "लघुगणक गुण"),
    "Matrices": ("矩阵", "Matrices", "मैट्रिसेस"),
    "Mathematical Induction": ("数学归纳法", "Induccion Matematica", "गणितीय आगमन"),
    "Maximum/Minimum": ("最大/最小值", "Maximo/Minimo", "अधिकतम/न्यूनतम"),
    "Mean": ("平均值", "Media", "माध्य"),
    "Multiplication": ("乘法", "Multiplicacion", "गुणन"),
    "Multiplicity": ("重数", "Multiplicidad", "बहुलता"),
    "Natural Logarithm": ("自然对数", "Logaritmo Natural", "प्राकृतिक लघुगणक"),
    "Normal Distribution": ("正态分布", "Distribucion Normal", "सामान्य वितरण"),
    "Optimization": ("优化", "Optimizacion", "अनुकूलन"),
    "Parabola": ("抛物线", "Parabola", "परवलय"),
    "Parametric Equations": ("参数方程", "Ecuaciones Parametricas", "पैरामीट्रिक समीकरण"),
    "Perfect Square Trinomials": ("完全平方三项式", "Trinomios Cuadrado Perfecto", "पूर्ण वर्ग त्रिपद"),
    "Permutations": ("排列", "Permutaciones", "क्रमचय"),
    "Phase Shift": ("相移", "Cambio de Fase", "चरण पारी"),
    "Point-Slope Form": ("点斜式", "Forma Punto-Pendiente", "बिंदु-ढलान रूप"),
    "Polar Form": ("极坐标形式", "Forma Polar", "ध्रुवीय रूप"),
    "Polynomial Division": ("多项式除法", "Division de Polinomios", "बहुपद विभाजन"),
    "Population Growth": ("人口增长", "Crecimiento Poblacional", "जनसंख्या वृद्धि"),
    "Power Reduction": ("幂降低", "Reduccion de Potencia", "शक्ति में कमी"),
    "Probability": ("概率", "Probabilidad", "प्रायिकता"),
    "Projectile Motion": ("抛体运动", "Movimiento de Proyectil", "प्रक्षेप्य गति"),
    "Properties of Exponents": ("指数性质", "Propiedades de Exponentes", "घातांक के गुण"),
    "Quadratic Formula": ("二次公式", "Formula Cuadratica", "द्विघात सूत्र"),
    "Quadratic Functions": ("二次函数", "Funciones Cuadraticas", "द्विघात फलन"),
    "Radian Measure": ("弧度制", "Medida en Radianes", "रेडियन माप"),
    "Radioactive Decay": ("放射性衰变", "Decaimiento Radiactivo", "रेडियोधर्मी क्षय"),
    "Rational Expressions": ("有理表达式", "Expresiones Racionales", "परिमेय व्यंजन"),
    "Rational Root Theorem": ("有理根定理", "Teorema de Raiz Racional", "परिमेय मूल प्रमेय"),
    "Remainder Theorem": ("剩余定理", "Teorema del Residuo", "शेषफल प्रमेय"),
    "Sequences": ("数列", "Sucesiones", "अनुक्रम"),
    "Series": ("级数", "Series", "श्रृंखला"),
    "Sigma Notation": ("求和符号", "Notacion Sigma", "सिग्मा संकेतन"),
    "Solving Inequalities": ("不等式求解", "Resollver Desigualdades", "असमानताओं को हल करना"),
    "Standard Deviation": ("标准差", "Desviacion Estandar", "मानक विचलन"),
    "Substitution Method": ("代入法", "Metodo de Sustitucion", "प्रतिस्थापन विधि"),
    "Sum and Product": ("和与积", "Suma y Producto", "योग और गुणनफल"),
    "Systems of Equations": ("方程组", "Sistemas de Ecuaciones", "समीकरणों की प्रणाली"),
    "Transformation": ("变换", "Transformacion", "रूपांतरण"),
    "Trigonometric Functions": ("三角函数", "Funciones Trigonometricas", "त्रिकोणमितीय फलन"),
    "Unit Circle": ("单位圆", "Circulo Unitario", "इकाई वृत्त"),
    "Vectors": ("向量", "Vectores", "सदिश"),
    "Vertex Form": ("顶点形式", "Forma Vertice", "शीर्ष रूप"),
    "Vertical Asymptotes": ("竖直渐近线", "Asintotas Verticales", "ऊर्ध्वाधर अनंतस्पर्शी"),
    "Zeros and Roots": ("零点和根", "Ceros y Raices", "शून्य और मूल"),
}

print(f"Algebra 2 translations: {len(alg2_translations)} entries")
print("Injecting translations...")

inject_all(alg2_translations, decode_entities=True)
print("✓ Algebra 2 injection complete!")
