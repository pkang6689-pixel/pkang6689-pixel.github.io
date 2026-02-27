#!/usr/bin/env python3
"""Batch 1: Algebra 1 translations + shared UI strings."""
import sys, html
sys.path.insert(0, r"c:\Users\Peter\pkang6689-pixel.github.io")
from inject_translations_util import inject_all

LQ = "\u201c"  # left curly double quote
RQ = "\u201d"  # right curly double quote

translations = {
    # ========== SHARED UI STRINGS ==========
    "&#x1F3C6; Leaderboard": (
        "\U0001F3C6 \u6392\u884c\u699c",
        "\U0001F3C6 Tabla de Clasificaci\u00f3n",
        "\U0001F3C6 \u0932\u0940\u0921\u0930\u092c\u094b\u0930\u094d\u0921"
    ),
    "Back to Algebra 2": (
        "\u8fd4\u56de\u4ee3\u6570 2",
        "Volver a \u00c1lgebra 2",
        "\u092c\u0940\u091c\u0917\u0923\u093f\u0924 2 \u092a\u0930 \u0935\u093e\u092a\u0938 \u091c\u093e\u090f\u0901"
    ),
    # ========== ALGEBRA 1 QUIZ QUESTIONS ==========
    "1. Solve: x + 3 &gt; 7": (
        "1. \u6c42\u89e3\uff1ax + 3 > 7",
        "1. Resuelve: x + 3 > 7",
        "1. \u0939\u0932 \u0915\u0930\u0947\u0902: x + 3 > 7"
    ),
    "1. Solve: x\u00b2 \u2212 4 &gt; 0": (
        "1. \u6c42\u89e3\uff1ax\u00b2 \u2212 4 > 0",
        "1. Resuelve: x\u00b2 \u2212 4 > 0",
        "1. \u0939\u0932 \u0915\u0930\u0947\u0902: x\u00b2 \u2212 4 > 0"
    ),
    "1. Solve: \u22123 &lt; x + 1 &lt; 7": (
        "1. \u6c42\u89e3\uff1a\u22123 < x + 1 < 7",
        "1. Resuelve: \u22123 < x + 1 < 7",
        "1. \u0939\u0932 \u0915\u0930\u0947\u0902: \u22123 < x + 1 < 7"
    ),
    "2. A compound inequality using &#x27;AND&#x27; represents:": (
        f"2. \u4f7f\u7528{LQ}AND{RQ}\u7684\u590d\u5408\u4e0d\u7b49\u5f0f\u8868\u793a\uff1a",
        "2. Una desigualdad compuesta usando 'AND' representa:",
        "2. 'AND' \u0915\u093e \u0909\u092a\u092f\u094b\u0917 \u0915\u0930\u0928\u0947 \u0935\u093e\u0932\u0940 \u0938\u0902\u092f\u0941\u0915\u094d\u0924 \u0905\u0938\u092e\u093f\u0915\u093e \u0926\u0930\u094d\u0936\u093e\u0924\u0940 \u0939\u0948:"
    ),
    "2. The &#x27;box&#x27; in a box plot represents:": (
        f"2. \u7bb1\u7ebf\u56fe\u4e2d\u7684{LQ}\u7bb1{RQ}\u8868\u793a\uff1a",
        "2. La 'caja' en un diagrama de caja representa:",
        "2. \u092c\u0949\u0915\u094d\u0938 \u092a\u094d\u0932\u0949\u091f \u092e\u0947\u0902 '\u092c\u0949\u0915\u094d\u0938' \u0926\u0930\u094d\u0936\u093e\u0924\u093e \u0939\u0948:"
    ),
    "2. The initial value &#x27;a&#x27; in y = a \u00b7 b\u02e3 is found at:": (
        "2. y = a \u00b7 b\u02e3 \u4e2d\u521d\u59cb\u503c 'a' \u7684\u4f4d\u7f6e\uff1a",
        "2. El valor inicial 'a' en y = a \u00b7 b\u02e3 se encuentra en:",
        "2. y = a \u00b7 b\u02e3 \u092e\u0947\u0902 \u092a\u094d\u0930\u093e\u0930\u0902\u092d\u093f\u0915 \u092e\u093e\u0928 'a' \u092f\u0939\u093e\u0901 \u092e\u093f\u0932\u0924\u093e \u0939\u0948:"
    ),
    "3. Solve: x &lt; 2 or x &gt; 8": (
        "3. \u6c42\u89e3\uff1ax < 2 \u6216 x > 8",
        "3. Resuelve: x < 2 o x > 8",
        "3. \u0939\u0932 \u0915\u0930\u0947\u0902: x < 2 \u092f\u093e x > 8"
    ),
    "3. Solve: |x| &lt; 4": (
        "3. \u6c42\u89e3\uff1a|x| < 4",
        "3. Resuelve: |x| < 4",
        "3. \u0939\u0932 \u0915\u0930\u0947\u0902: |x| < 4"
    ),
    "3. The first step in solving x\u00b2 \u2212 5x + 6 &lt; 0 is:": (
        "3. \u89e3 x\u00b2 \u2212 5x + 6 < 0 \u7684\u7b2c\u4e00\u6b65\u662f\uff1a",
        "3. El primer paso para resolver x\u00b2 \u2212 5x + 6 < 0 es:",
        "3. x\u00b2 \u2212 5x + 6 < 0 \u0939\u0932 \u0915\u0930\u0928\u0947 \u0915\u093e \u092a\u0939\u0932\u093e \u091a\u0930\u0923 \u0939\u0948:"
    ),
    "3. When graphing x &lt; 5, use:": (
        "3. \u7ed8\u5236 x < 5 \u7684\u56fe\u5f62\u65f6\uff0c\u4f7f\u7528\uff1a",
        "3. Al graficar x < 5, usa:",
        "3. x < 5 \u0915\u093e \u0917\u094d\u0930\u093e\u092b \u092c\u0928\u093e\u0924\u0947 \u0938\u092e\u092f, \u0909\u092a\u092f\u094b\u0917 \u0915\u0930\u0947\u0902:"
    ),
    "4. Solve: x\u00b2 \u2212 x \u2212 6 &gt; 0": (
        "4. \u6c42\u89e3\uff1ax\u00b2 \u2212 x \u2212 6 > 0",
        "4. Resuelve: x\u00b2 \u2212 x \u2212 6 > 0",
        "4. \u0939\u0932 \u0915\u0930\u0947\u0902: x\u00b2 \u2212 x \u2212 6 > 0"
    ),
    "4. Solve: |x| &gt; 6": (
        "4. \u6c42\u89e3\uff1a|x| > 6",
        "4. Resuelve: |x| > 6",
        "4. \u0939\u0932 \u0915\u0930\u0947\u0902: |x| > 6"
    ),
    "4. The graph of an &#x27;AND&#x27; inequality shows:": (
        f"4. {LQ}AND{RQ}\u4e0d\u7b49\u5f0f\u7684\u56fe\u5f62\u663e\u793a\uff1a",
        "4. La gr\u00e1fica de una desigualdad 'AND' muestra:",
        "4. 'AND' \u0905\u0938\u092e\u093f\u0915\u093e \u0915\u093e \u0917\u094d\u0930\u093e\u092b \u0926\u0930\u094d\u0936\u093e\u0924\u093e \u0939\u0948:"
    ),
    "5. For x\u00b2 &lt; 16:": (
        "5. \u5bf9\u4e8e x\u00b2 < 16\uff1a",
        "5. Para x\u00b2 < 16:",
        "5. x\u00b2 < 16 \u0915\u0947 \u0932\u093f\u090f:"
    ),
    "5. If a &lt; 0, the parabola has:": (
        "5. \u5982\u679c a < 0\uff0c\u629b\u7269\u7ebf\u5177\u6709\uff1a",
        "5. Si a < 0, la par\u00e1bola tiene:",
        "5. \u092f\u0926\u093f a < 0, \u0924\u094b \u092a\u0930\u0935\u0932\u092f \u092e\u0947\u0902 \u0939\u0948:"
    ),
    "5. In y = a \u00b7 b\u02e3, &#x27;a&#x27; represents:": (
        "5. \u5728 y = a \u00b7 b\u02e3 \u4e2d\uff0c'a' \u8868\u793a\uff1a",
        "5. En y = a \u00b7 b\u02e3, 'a' representa:",
        "5. y = a \u00b7 b\u02e3 \u092e\u0947\u0902, 'a' \u0926\u0930\u094d\u0936\u093e\u0924\u093e \u0939\u0948:"
    ),
    "5. Solve: 2x + 1 &gt; 5 AND 3x &lt; 18": (
        "5. \u6c42\u89e3\uff1a2x + 1 > 5 \u4e14 3x < 18",
        "5. Resuelve: 2x + 1 > 5 Y 3x < 18",
        "5. \u0939\u0932 \u0915\u0930\u0947\u0902: 2x + 1 > 5 \u0914\u0930 3x < 18"
    ),
    "6. Describing data &#x27;in context&#x27; means:": (
        f"6. \u5728{LQ}\u60c5\u5883\u4e2d{RQ}\u63cf\u8ff0\u6570\u636e\u610f\u5473\u7740\uff1a",
        "6. Describir datos 'en contexto' significa:",
        "6. \u0921\u0947\u091f\u093e \u0915\u094b '\u0938\u0902\u0926\u0930\u094d\u092d \u092e\u0947\u0902' \u0935\u0930\u094d\u0923\u0928 \u0915\u0930\u0928\u0947 \u0915\u093e \u0905\u0930\u094d\u0925 \u0939\u0948:"
    ),
    "6. If the distribution of &#x27;pass/fail&#x27; is the same for males and females:": (
        f"6. \u5982\u679c\u7537\u6027\u548c\u5973\u6027\u7684{LQ}\u901a\u8fc7/\u4e0d\u901a\u8fc7{RQ}\u5206\u5e03\u76f8\u540c\uff1a",
        "6. Si la distribuci\u00f3n de 'aprobado/reprobado' es la misma para hombres y mujeres:",
        "6. \u092f\u0926\u093f '\u092a\u093e\u0938/\u092b\u0947\u0932' \u0915\u093e \u0935\u093f\u0924\u0930\u0923 \u092a\u0941\u0930\u0941\u0937\u094b\u0902 \u0914\u0930 \u092e\u0939\u093f\u0932\u093e\u0913\u0902 \u0915\u0947 \u0932\u093f\u090f \u0938\u092e\u093e\u0928 \u0939\u0948:"
    ),
    "6. Pascal&#x27;s Triangle is used for:": (
        "6. \u5e15\u65af\u5361\u4e09\u89d2\u5f62\u7528\u4e8e\uff1a",
        "6. El Tri\u00e1ngulo de Pascal se usa para:",
        "6. \u092a\u093e\u0938\u094d\u0915\u0932 \u0915\u093e \u0924\u094d\u0930\u093f\u092d\u0941\u091c \u0915\u093f\u0938\u0915\u0947 \u0932\u093f\u090f \u0909\u092a\u092f\u094b\u0917 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948:"
    ),
    "6. Solve: x/4 &lt; 3": (
        "6. \u6c42\u89e3\uff1ax/4 < 3",
        "6. Resuelve: x/4 < 3",
        "6. \u0939\u0932 \u0915\u0930\u0947\u0902: x/4 < 3"
    ),
    "6. The &#x27;a&#x27; in the quadratic regression equation determines:": (
        "6. \u4e8c\u6b21\u56de\u5f52\u65b9\u7a0b\u4e2d\u7684 'a' \u51b3\u5b9a\u4e86\uff1a",
        "6. La 'a' en la ecuaci\u00f3n de regresi\u00f3n cuadr\u00e1tica determina:",
        "6. \u0926\u094d\u0935\u093f\u0918\u093e\u0924 \u092a\u094d\u0930\u0924\u093f\u0917\u092e\u0928 \u0938\u092e\u0940\u0915\u0930\u0923 \u092e\u0947\u0902 'a' \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u0930\u0924\u093e \u0939\u0948:"
    ),
    "7. A geometric sequence with |r| &gt; 1:": (
        "7. |r| > 1 \u7684\u7b49\u6bd4\u6570\u5217\uff1a",
        "7. Una secuencia geom\u00e9trica con |r| > 1:",
        "7. |r| > 1 \u0935\u093e\u0932\u0940 \u0917\u0941\u0923\u094b\u0924\u094d\u0924\u0930 \u0936\u094d\u0930\u0947\u0923\u0940:"
    ),
    "7. If a &#x27;solution&#x27; gives 0 in a denominator:": (
        f"7. \u5982\u679c\u4e00\u4e2a{LQ}\u89e3{RQ}\u4f7f\u5206\u6bcd\u4e3a\u96f6\uff1a",
        "7. Si una 'soluci\u00f3n' da 0 en un denominador:",
        "7. \u092f\u0926\u093f \u090f\u0915 '\u0939\u0932' \u0939\u0930 \u092e\u0947\u0902 0 \u0926\u0947\u0924\u093e \u0939\u0948:"
    ),
    "7. The &#x27;a&#x27; value in y = a(x\u2212h)\u00b2+k affects:": (
        "7. y = a(x\u2212h)\u00b2+k \u4e2d 'a' \u503c\u7684\u5f71\u54cd\uff1a",
        "7. El valor de 'a' en y = a(x\u2212h)\u00b2+k afecta:",
        "7. y = a(x\u2212h)\u00b2+k \u092e\u0947\u0902 'a' \u0915\u093e \u092e\u093e\u0928 \u092a\u094d\u0930\u092d\u093e\u0935\u093f\u0924 \u0915\u0930\u0924\u093e \u0939\u0948:"
    ),
    "7. The &#x27;k&#x27; in vertex form represents:": (
        "7. \u9876\u70b9\u5f62\u5f0f\u4e2d\u7684 'k' \u8868\u793a\uff1a",
        "7. La 'k' en la forma de v\u00e9rtice representa:",
        "7. \u0936\u0940\u0930\u094d\u0937 \u0930\u0942\u092a \u092e\u0947\u0902 'k' \u0926\u0930\u094d\u0936\u093e\u0924\u093e \u0939\u0948:"
    ),
    "7. The solution to x\u00b2 + 1 &gt; 0 is:": (
        "7. x\u00b2 + 1 > 0 \u7684\u89e3\u662f\uff1a",
        "7. La soluci\u00f3n de x\u00b2 + 1 > 0 es:",
        "7. x\u00b2 + 1 > 0 \u0915\u093e \u0939\u0932 \u0939\u0948:"
    ),
    "7. The value &#x27;a&#x27; in the regression model represents:": (
        "7. \u56de\u5f52\u6a21\u578b\u4e2d 'a' \u7684\u503c\u8868\u793a\uff1a",
        "7. El valor 'a' en el modelo de regresi\u00f3n representa:",
        "7. \u092a\u094d\u0930\u0924\u093f\u0917\u092e\u0928 \u092e\u0949\u0921\u0932 \u092e\u0947\u0902 'a' \u0915\u093e \u092e\u093e\u0928 \u0926\u0930\u094d\u0936\u093e\u0924\u093e \u0939\u0948:"
    ),
    "7. To graph y &gt; 2x + 1, you draw:": (
        "7. \u8981\u7ed8\u5236 y > 2x + 1 \u7684\u56fe\u5f62\uff0c\u9700\u8981\u753b\uff1a",
        "7. Para graficar y > 2x + 1, dibujas:",
        "7. y > 2x + 1 \u0915\u093e \u0917\u094d\u0930\u093e\u092b \u092c\u0928\u093e\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f, \u0906\u092a \u092c\u0928\u093e\u090f\u0901:"
    ),
    # ========== ALGEBRA 1 QUIZ ANSWERS ==========
    "Time doesn&#x27;t matter": (
        "\u65f6\u95f4\u4e0d\u91cd\u8981",
        "El tiempo no importa",
        "\u0938\u092e\u092f \u092e\u0939\u0924\u094d\u0935\u092a\u0942\u0930\u094d\u0923 \u0928\u0939\u0940\u0902 \u0939\u0948"
    ),
    "x &gt; 1 AND x &lt; 10": (
        "x > 1 \u4e14 x < 10",
        "x > 1 Y x < 10",
        "x > 1 \u0914\u0930 x < 10"
    ),
    "x &gt; 5 AND x &lt; 2": (
        "x > 5 \u4e14 x < 2",
        "x > 5 Y x < 2",
        "x > 5 \u0914\u0930 x < 2"
    ),
}

if __name__ == '__main__':
    print(f"Algebra 1 + Shared: {len(translations)} entries")
    inject_all(translations, decode_entities=True)
