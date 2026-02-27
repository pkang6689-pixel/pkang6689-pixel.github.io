#!/usr/bin/env python3
"""Geometry translations batch - 310 strings × 3 languages (Chinese, Spanish, Hindi)."""
import sys, os
sys.path.insert(0, r"c:\Users\Peter\pkang6689-pixel.github.io")
from inject_translations_util import inject_all

translations = {
    # ===================== SUMMARY CONTENT (9) =====================
    'A biconditional statement (p \u2194 q) means "p if and only if q." It is true when both p and q have the same truth value.':
        ('双条件语句 (p \u2194 q) 表示"p 当且仅当 q"。当 p 和 q 具有相同的真值时，该语句为真。',
         'Una declaraci\u00f3n bicondicional (p \u2194 q) significa "p si y solo si q." Es verdadera cuando tanto p como q tienen el mismo valor de verdad.',
         'एक द्विशर्त कथन (p \u2194 q) का अर्थ है "p यदि और केवल यदि q।" यह तब सत्य होता है जब p और q दोनों का सत्य मान समान हो।'),
    'A conditional statement has the form "If p, then q" (written p \u2192 q). The hypothesis is p and the conclusion is q.':
        ('条件语句的形式为"如果 p，则 q"（写作 p \u2192 q）。假设为 p，结论为 q。',
         'Una declaraci\u00f3n condicional tiene la forma "Si p, entonces q" (escrito p \u2192 q). La hip\u00f3tesis es p y la conclusi\u00f3n es q.',
         'एक शर्त कथन का रूप "यदि p, तो q" (p \u2192 q लिखा जाता है) होता है। परिकल्पना p है और निष्कर्ष q है।'),
    'A ratio compares two quantities. It can be written as a:b, a/b, or "a to b".':
        ('比率比较两个量。它可以写为 a:b、a/b 或 "a 比 b"。',
         'Una raz\u00f3n compara dos cantidades. Se puede escribir como a:b, a/b, o "a a b".',
         'एक अनुपात दो मात्राओं की तुलना करता है। इसे a:b, a/b, या "a से b" के रूप में लिखा जा सकता है।'),
    'A sector is a "pie slice" of a circle defined by a central angle \u03b8.':
        ('扇形是由圆心角 \u03b8 定义的圆的"扇形区域"。',
         'Un sector es una "rebanada de pastel" de un c\u00edrculo definida por un \u00e1ngulo central \u03b8.',
         'एक त्रिज्यखंड एक वृत्त का "पाई स्लाइस" है जो केंद्रीय कोण \u03b8 द्वारा परिभाषित होता है।'),
    'Conjecture: "All prime numbers are odd." Counterexample: 2 is prime and even.':
        ('猜想："所有素数都是奇数。" 反例：2 是素数且是偶数。',
         'Conjetura: "Todos los n\u00fameros primos son impares." Contraejemplo: 2 es primo y par.',
         'अनुमान: "सभी अभाज्य संख्याएँ विषम हैं।" प्रतिउदाहरण: 2 अभाज्य और सम है।'),
    'Conjunction (p \u2227 q): "p AND q" \u2014 true only when BOTH p and q are true.':
        ('合取 (p \u2227 q)："p 且 q" \u2014 仅当 p 和 q 都为真时才为真。',
         'Conjunci\u00f3n (p \u2227 q): "p Y q" \u2014 verdadera solo cuando AMBOS p y q son verdaderos.',
         'संयोजन (p \u2227 q): "p और q" \u2014 केवल तभी सत्य जब p और q दोनों सत्य हों।'),
    'Disjunction (p \u2228 q): "p OR q" \u2014 true when AT LEAST ONE of p or q is true.':
        ('析取 (p \u2228 q)："p 或 q" \u2014 当 p 或 q 中至少一个为真时为真。',
         'Disyunci\u00f3n (p \u2228 q): "p O q" \u2014 verdadera cuando AL MENOS UNO de p o q es verdadero.',
         'वियोजन (p \u2228 q): "p या q" \u2014 तब सत्य जब p या q में से कम से कम एक सत्य हो।'),
    'In spherical geometry, "lines" are great circles. There are no parallel lines \u2014 every pair of great circles intersects at two points.':
        ('在球面几何中，"直线"是大圆。不存在平行线 \u2014 每对大圆都相交于两点。',
         'En geometr\u00eda esf\u00e9rica, las "l\u00edneas" son c\u00edrculos m\u00e1ximos. No hay l\u00edneas paralelas \u2014 cada par de c\u00edrculos m\u00e1ximos se intersecta en dos puntos.',
         'गोलीय ज्यामिति में, "रेखाएँ" महान वृत्त हैं। कोई समांतर रेखाएँ नहीं हैं \u2014 महान वृत्तों का प्रत्येक जोड़ा दो बिंदुओं पर प्रतिच्छेद करता है।'),
    'When the conclusion involves uniqueness ("there is exactly one...").':
        ('当结论涉及唯一性时（"恰好存在一个……"）。',
         'Cuando la conclusi\u00f3n involucra unicidad ("hay exactamente uno...").',
         'जब निष्कर्ष विशिष्टता से संबंधित हो ("ठीक एक है...")।'),

    # ===================== QUIZ QUESTIONS (285) =====================
    "1. A central angle has its vertex at the:":
        ("1. 圆心角的顶点位于：", "1. Un \u00e1ngulo central tiene su v\u00e9rtice en:", "1. एक केंद्रीय कोण का शीर्ष किस पर होता है:"),
    "1. A regular hexagon has how many lines of symmetry?":
        ("1. 正六边形有多少条对称轴？", "1. \u00bfCu\u00e1ntos ejes de simetr\u00eda tiene un hex\u00e1gono regular?", "1. एक नियमित षट्भुज में कितनी समरूपता रेखाएँ हैं?"),
    "1. A tangent line is always __________ to the radius at the point of tangency.":
        ("1. 切线在切点处始终__________于半径。", "1. Una l\u00ednea tangente siempre es __________ al radio en el punto de tangencia.", "1. एक स्पर्शरेखा स्पर्श बिंदु पर त्रिज्या के __________ होती है।"),
    "1. A translation is described by which mathematical object?":
        ("1. 平移由哪种数学对象描述？", "1. \u00bfQu\u00e9 objeto matem\u00e1tico describe una traslaci\u00f3n?", "1. स्थानांतरण किस गणितीय वस्तु द्वारा वर्णित किया जाता है?"),
    "1. An inscribed angle has its vertex located:":
        ("1. 圆内接角的顶点位于：", "1. Un \u00e1ngulo inscrito tiene su v\u00e9rtice ubicado:", "1. एक अंतर्लिखित कोण का शीर्ष कहाँ स्थित होता है:"),
    "1. Conic sections are formed by the intersection of a plane and a:":
        ("1. 圆锥曲线是由平面和什么的交线形成的：", "1. Las secciones c\u00f3nicas se forman por la intersecci\u00f3n de un plano y un:", "1. शंकु परिच्छेद एक समतल और किसके प्रतिच्छेदन से बनते हैं:"),
    "1. In 'If p, then q,' what is p called?":
        ("1. 在\u201c如果 p，则 q\u201d中，p 被称为什么？", "1. En 'Si p, entonces q', \u00bfc\u00f3mo se llama p?", "1. 'यदि p, तो q' में, p को क्या कहते हैं?"),
    "1. In geometric probability, the probability of hitting a region is based on:":
        ("1. 在几何概率中，击中某区域的概率基于：", "1. En probabilidad geom\u00e9trica, la probabilidad de golpear una regi\u00f3n se basa en:", "1. ज्यामितीय प्रायिकता में, किसी क्षेत्र को मारने की प्रायिकता किस पर आधारित है:"),
    "1. In spherical geometry, what takes the place of straight lines?":
        ("1. 在球面几何中，什么取代了直线？", "1. En geometr\u00eda esf\u00e9rica, \u00bfqu\u00e9 reemplaza a las l\u00edneas rectas?", "1. गोलीय ज्यामिति में, सीधी रेखाओं का स्थान क्या लेता है?"),
    "1. In the same circle, congruent chords intercept:":
        ("1. 在同一个圆中，全等弦所截的弧为：", "1. En el mismo c\u00edrculo, cuerdas congruentes interceptan:", "1. एक ही वृत्त में, सर्वांगसम जीवाएँ किसको काटती हैं:"),
    "1. The standard form equation of a circle with center (h, k) and radius r is:":
        ("1. 以 (h, k) 为圆心、r 为半径的圆的标准方程为：", "1. La ecuaci\u00f3n en forma est\u00e1ndar de un c\u00edrculo con centro (h, k) y radio r es:", "1. केंद्र (h, k) और त्रिज्या r वाले वृत्त का मानक रूप समीकरण है:"),
    "1. Two events are independent if:":
        ("1. 两个事件独立的条件是：", "1. Dos eventos son independientes si:", "1. दो घटनाएँ स्वतंत्र होती हैं यदि:"),
    "1. Two events are mutually exclusive if:":
        ("1. 两个事件互斥的条件是：", "1. Dos eventos son mutuamente excluyentes si:", "1. दो घटनाएँ परस्पर अपवर्जी होती हैं यदि:"),
    "1. Two figures are congruent if and only if they are related by a sequence of __________.":
        ("1. 两个图形全等当且仅当它们通过一系列__________相关联。", "1. Dos figuras son congruentes si y solo si est\u00e1n relacionadas por una secuencia de __________.", "1. दो आकृतियाँ सर्वांगसम होती हैं यदि और केवल यदि वे __________ के अनुक्रम से संबंधित हों।"),
    "1. Two similar figures have a scale factor of 3:5. What is the ratio of their areas?":
        ("1. 两个相似图形的比例因子为 3:5。它们的面积比是多少？", "1. Dos figuras similares tienen un factor de escala de 3:5. \u00bfCu\u00e1l es la raz\u00f3n de sus \u00e1reas?", "1. दो समरूप आकृतियों का स्केल गुणक 3:5 है। उनके क्षेत्रफलों का अनुपात क्या है?"),
    "1. Two solids are similar with a scale factor of k. What is the ratio of their surface areas?":
        ("1. 两个相似立体的比例因子为 k。它们的表面积比是多少？", "1. Dos s\u00f3lidos son similares con un factor de escala k. \u00bfCu\u00e1l es la raz\u00f3n de sus \u00e1reas de superficie?", "1. दो ठोस k के स्केल गुणक से समरूप हैं। उनके पृष्ठीय क्षेत्रफलों का अनुपात क्या है?"),
    "1. What does Cavalieri's Principle state?":
        ("1. 卡瓦列里原理是什么？", "1. \u00bfQu\u00e9 establece el Principio de Cavalieri?", "1. कैवलिएरी का सिद्धांत क्या कहता है?"),
    "1. What is a cross section of a solid?":
        ("1. 立体的截面是什么？", "1. \u00bfQu\u00e9 es una secci\u00f3n transversal de un s\u00f3lido?", "1. एक ठोस का अनुप्रस्थ काट क्या है?"),
    "1. What is a glide reflection?":
        ("1. 什么是滑移反射？", "1. \u00bfQu\u00e9 es una reflexi\u00f3n con deslizamiento?", "1. ग्लाइड परावर्तन क्या है?"),
    "1. What is a sample space in probability?":
        ("1. 概率中的样本空间是什么？", "1. \u00bfQu\u00e9 es un espacio muestral en probabilidad?", "1. प्रायिकता में प्रतिदर्श समष्टि क्या है?"),
    "1. What is a simulation in probability?":
        ("1. 概率中的模拟是什么？", "1. \u00bfQu\u00e9 es una simulaci\u00f3n en probabilidad?", "1. प्रायिकता में अनुकरण क्या है?"),
    "1. What is the Monte Carlo method?":
        ("1. 什么是蒙特卡洛方法？", "1. \u00bfQu\u00e9 es el m\u00e9todo Monte Carlo?", "1. मोंटे कार्लो विधि क्या है?"),
    "1. What is the area of a circle with radius 5 cm?":
        ("1. 半径为 5 厘米的圆的面积是多少？", "1. \u00bfCu\u00e1l es el \u00e1rea de un c\u00edrculo con radio de 5 cm?", "1. 5 सेमी त्रिज्या वाले वृत्त का क्षेत्रफल क्या है?"),
    "1. What is the area of a parallelogram with a base of 10 cm and a height of 6 cm?":
        ("1. 底为 10 厘米、高为 6 厘米的平行四边形的面积是多少？", "1. \u00bfCu\u00e1l es el \u00e1rea de un paralelogramo con base de 10 cm y altura de 6 cm?", "1. 10 सेमी आधार और 6 सेमी ऊँचाई वाले समांतर चतुर्भुज का क्षेत्रफल क्या है?"),
    "1. What is the area of a regular polygon with an apothem of 4 cm and a perimeter of 24 cm?":
        ("1. 边心距为 4 厘米、周长为 24 厘米的正多边形的面积是多少？", "1. \u00bfCu\u00e1l es el \u00e1rea de un pol\u00edgono regular con apotema de 4 cm y per\u00edmetro de 24 cm?", "1. 4 सेमी अपोथेम और 24 सेमी परिमाप वाले नियमित बहुभुज का क्षेत्रफल क्या है?"),
    "1. What is the area of a trapezoid with bases 8 cm and 14 cm and a height of 5 cm?":
        ("1. 上底 8 厘米、下底 14 厘米、高 5 厘米的梯形面积是多少？", "1. \u00bfCu\u00e1l es el \u00e1rea de un trapecio con bases de 8 cm y 14 cm y una altura de 5 cm?", "1. 8 सेमी और 14 सेमी आधार तथा 5 सेमी ऊँचाई वाले समलंब का क्षेत्रफल क्या है?"),
    "1. What is the definition of a circle?":
        ("1. 圆的定义是什么？", "1. \u00bfCu\u00e1l es la definici\u00f3n de un c\u00edrculo?", "1. वृत्त की परिभाषा क्या है?"),
    "1. What is the formula for the lateral area of a prism?":
        ("1. 棱柱的侧面积公式是什么？", "1. \u00bfCu\u00e1l es la f\u00f3rmula del \u00e1rea lateral de un prisma?", "1. प्रिज्म के पार्श्व क्षेत्रफल का सूत्र क्या है?"),
    "1. What is the image of (3, \u22124) after a 90\u00b0 counterclockwise rotation about the origin?":
        ("1. (3, \u22124) 绕原点逆时针旋转 90\u00b0 后的像是什么？", "1. \u00bfCu\u00e1l es la imagen de (3, \u22124) despu\u00e9s de una rotaci\u00f3n de 90\u00b0 en sentido antihorario alrededor del origen?", "1. मूल बिंदु के चारों ओर 90\u00b0 वामावर्त घूर्णन के बाद (3, \u22124) का प्रतिबिंब क्या है?"),
    "1. What is the image of (4, \u22126) after a dilation with scale factor 3 centered at the origin?":
        ("1. 以原点为中心、比例因子为 3 的缩放后 (4, \u22126) 的像是什么？", "1. \u00bfCu\u00e1l es la imagen de (4, \u22126) despu\u00e9s de una dilataci\u00f3n con factor de escala 3 centrada en el origen?", "1. मूल बिंदु पर केंद्रित स्केल गुणक 3 के विस्तारण के बाद (4, \u22126) का प्रतिबिंब क्या है?"),
    "1. What is the image of the point (3, \u22125) after a reflection over the x-axis?":
        ("1. 点 (3, \u22125) 关于 x 轴反射后的像是什么？", "1. \u00bfCu\u00e1l es la imagen del punto (3, \u22125) despu\u00e9s de una reflexi\u00f3n sobre el eje x?", "1. x-अक्ष पर परावर्तन के बाद बिंदु (3, \u22125) का प्रतिबिंब क्या है?"),
    "1. What is the lateral area formula for a regular pyramid?":
        ("1. 正棱锥的侧面积公式是什么？", "1. \u00bfCu\u00e1l es la f\u00f3rmula del \u00e1rea lateral de una pir\u00e1mide regular?", "1. एक नियमित पिरामिड के पार्श्व क्षेत्रफल का सूत्र क्या है?"),
    "1. What is the surface area formula for a sphere?":
        ("1. 球体的表面积公式是什么？", "1. \u00bfCu\u00e1l es la f\u00f3rmula del \u00e1rea de superficie de una esfera?", "1. गोले के पृष्ठीय क्षेत्रफल का सूत्र क्या है?"),
    "1. What is the value of 5! (5 factorial)?":
        ("1. 5!（5 的阶乘）的值是多少？", "1. \u00bfCu\u00e1l es el valor de 5! (5 factorial)?", "1. 5! (5 क्रमगुणित) का मान क्या है?"),
    "1. What is the volume formula for a prism?":
        ("1. 棱柱的体积公式是什么？", "1. \u00bfCu\u00e1l es la f\u00f3rmula del volumen de un prisma?", "1. प्रिज्म के आयतन का सूत्र क्या है?"),
    "1. What is the volume formula for a pyramid?":
        ("1. 棱锥的体积公式是什么？", "1. \u00bfCu\u00e1l es la f\u00f3rmula del volumen de una pir\u00e1mide?", "1. पिरामिड के आयतन का सूत्र क्या है?"),
    "1. What method approximates the area under a curve by dividing it into rectangles?":
        ("1. 什么方法通过将曲线下面积分成矩形来近似计算？", "1. \u00bfQu\u00e9 m\u00e9todo aproxima el \u00e1rea bajo una curva dividi\u00e9ndola en rect\u00e1ngulos?", "1. कौन सी विधि वक्र के नीचे के क्षेत्रफल को आयतों में विभाजित करके सन्निकट करती है?"),
    "1. When two chords intersect inside a circle, the angle formed equals:":
        ("1. 当两条弦在圆内相交时，所形成的角等于：", "1. Cuando dos cuerdas se cruzan dentro de un c\u00edrculo, el \u00e1ngulo formado es igual a:", "1. जब दो जीवाएँ एक वृत्त के अंदर प्रतिच्छेद करती हैं, तो बना कोण बराबर होता है:"),
    "1. When two chords intersect inside a circle, which relationship holds?":
        ("1. 当两条弦在圆内相交时，哪个关系成立？", "1. Cuando dos cuerdas se cruzan dentro de un c\u00edrculo, \u00bfqu\u00e9 relaci\u00f3n se cumple?", "1. जब दो जीवाएँ एक वृत्त के अंदर प्रतिच्छेद करती हैं, तो कौन सा संबंध सत्य है?"),
    "2. A bag has 5 red and 3 blue marbles. You draw one marble, replace it, then draw again. What is P(red, then blue)?":
        ("2. 一个袋子里有 5 个红色和 3 个蓝色弹珠。你抽出一个弹珠，放回，再抽一个。P(红, 然后蓝) 是多少？", "2. Una bolsa tiene 5 canicas rojas y 3 azules. Sacas una canica, la reemplazas y sacas otra. \u00bfCu\u00e1l es P(roja, luego azul)?", "2. एक थैले में 5 लाल और 3 नीली गोलियाँ हैं। आप एक गोली निकालते हैं, वापस रखते हैं, फिर दोबारा निकालते हैं। P(लाल, फिर नीली) क्या है?"),
    "2. A cone has a radius of 5 cm and a slant height of 13 cm. What is its lateral area? (Use \u03c0 \u2248 3.14)":
        ("2. 一个圆锥的半径为 5 厘米，斜高为 13 厘米。它的侧面积是多少？（取 \u03c0 \u2248 3.14）", "2. Un cono tiene un radio de 5 cm y una altura inclinada de 13 cm. \u00bfCu\u00e1l es su \u00e1rea lateral? (Usa \u03c0 \u2248 3.14)", "2. एक शंकु की त्रिज्या 5 सेमी और तिरछी ऊँचाई 13 सेमी है। इसका पार्श्व क्षेत्रफल क्या है? (\u03c0 \u2248 3.14 लें)"),
    "2. A dart is thrown randomly at a 10\u00d710 square board. A circle of radius 3 is drawn at the center. What is the approximate probability of hitting the circle?":
        ("2. 一个飞镖随机投向 10\u00d710 的正方形板。中心画有半径为 3 的圆。击中圆的近似概率是多少？", "2. Se lanza un dardo al azar en un tablero cuadrado de 10\u00d710. Se dibuja un c\u00edrculo de radio 3 en el centro. \u00bfCu\u00e1l es la probabilidad aproximada de dar en el c\u00edrculo?", "2. एक डार्ट 10\u00d710 के वर्गाकार बोर्ड पर यादृच्छिक रूप से फेंका जाता है। केंद्र पर त्रिज्या 3 का वृत्त बना है। वृत्त पर लगने की अनुमानित प्रायिकता क्या है?"),
    "2. A dilation with scale factor k where 0 < k < 1 produces a __________.":
        ("2. 比例因子 k（0 < k < 1）的缩放产生一个__________。", "2. Una dilataci\u00f3n con factor de escala k donde 0 < k < 1 produce un __________.", "2. स्केल गुणक k जहाँ 0 < k < 1 का विस्तारण एक __________ उत्पन्न करता है।"),
    "2. A minor arc has a measure that is:":
        ("2. 劣弧的度数为：", "2. Un arco menor tiene una medida que es:", "2. एक लघु चाप का माप होता है:"),
    "2. A rectangular prism has dimensions 3 cm \u00d7 5 cm \u00d7 8 cm. What is its surface area?":
        ("2. 一个长方体的尺寸为 3 cm \u00d7 5 cm \u00d7 8 cm。它的表面积是多少？", "2. Un prisma rectangular tiene dimensiones de 3 cm \u00d7 5 cm \u00d7 8 cm. \u00bfCu\u00e1l es su \u00e1rea de superficie?", "2. एक आयताकार प्रिज्म की विमाएँ 3 cm \u00d7 5 cm \u00d7 8 cm हैं। इसका पृष्ठीय क्षेत्रफल क्या है?"),
    "2. A rectangular prism has dimensions 3 \u00d7 4 \u00d7 5. What is its volume?":
        ("2. 一个长方体的尺寸为 3 \u00d7 4 \u00d7 5。它的体积是多少？", "2. Un prisma rectangular tiene dimensiones 3 \u00d7 4 \u00d7 5. \u00bfCu\u00e1l es su volumen?", "2. एक आयताकार प्रिज्म की विमाएँ 3 \u00d7 4 \u00d7 5 हैं। इसका आयतन क्या है?"),
    "2. A reflection is classified as which type of transformation?":
        ("2. 反射被归类为哪种变换？", "2. \u00bfQu\u00e9 tipo de transformaci\u00f3n es una reflexi\u00f3n?", "2. परावर्तन को किस प्रकार के रूपांतरण के रूप में वर्गीकृत किया जाता है?"),
    "2. A rhombus has diagonals of length 10 cm and 16 cm. What is its area?":
        ("2. 一个菱形的对角线长分别为 10 厘米和 16 厘米。它的面积是多少？", "2. Un rombo tiene diagonales de 10 cm y 16 cm. \u00bfCu\u00e1l es su \u00e1rea?", "2. एक समचतुर्भुज के विकर्णों की लंबाई 10 सेमी और 16 सेमी है। इसका क्षेत्रफल क्या है?"),
    "2. A similarity transformation consists of __________.":
        ("2. 相似变换由__________组成。", "2. Una transformaci\u00f3n de semejanza consiste en __________.", "2. एक समरूपता रूपांतरण __________ से मिलकर बनता है।"),
    "2. A square pyramid has a base edge of 6 and a height of 9. What is its volume?":
        ("2. 一个正四棱锥的底边长为 6，高为 9。它的体积是多少？", "2. Una pir\u00e1mide cuadrada tiene una arista de base de 6 y una altura de 9. \u00bfCu\u00e1l es su volumen?", "2. एक वर्गाकार पिरामिड की आधार भुजा 6 और ऊँचाई 9 है। इसका आयतन क्या है?"),
    "2. According to the Inscribed Angle Theorem, an inscribed angle is equal to:":
        ("2. 根据圆内接角定理，圆内接角等于：", "2. Seg\u00fan el Teorema del \u00c1ngulo Inscrito, un \u00e1ngulo inscrito es igual a:", "2. अंतर्लिखित कोण प्रमेय के अनुसार, अंतर्लिखित कोण बराबर होता है:"),
    "2. According to the Law of Large Numbers, what happens as the number of trials increases?":
        ("2. 根据大数定律，随着试验次数增加会发生什么？", "2. Seg\u00fan la Ley de los Grandes N\u00fameros, \u00bfqu\u00e9 sucede a medida que aumenta el n\u00famero de ensayos?", "2. बड़ी संख्या के नियम के अनुसार, प्रयोगों की संख्या बढ़ने पर क्या होता है?"),
    "2. For two secants from an external point, the correct relationship is:":
        ("2. 从外部点引出的两条割线的正确关系是：", "2. Para dos secantes desde un punto externo, la relaci\u00f3n correcta es:", "2. एक बाह्य बिंदु से दो छेदकों के लिए, सही संबंध है:"),
    "2. How many outcomes are in the sample space when flipping 3 coins?":
        ("2. 抛 3 枚硬币时样本空间有多少个结果？", "2. \u00bfCu\u00e1ntos resultados hay en el espacio muestral al lanzar 3 monedas?", "2. 3 सिक्के उछालते समय प्रतिदर्श समष्टि में कितने परिणाम हैं?"),
    "2. If a circle has a radius of 9 cm, what is its diameter?":
        ("2. 如果一个圆的半径为 9 厘米，它的直径是多少？", "2. Si un c\u00edrculo tiene un radio de 9 cm, \u00bfcu\u00e1l es su di\u00e1metro?", "2. यदि एक वृत्त की त्रिज्या 9 सेमी है, तो इसका व्यास क्या है?"),
    "2. If a diameter is perpendicular to a chord, what does it do to the chord?":
        ("2. 如果直径垂直于弦，它对弦有什么作用？", "2. Si un di\u00e1metro es perpendicular a una cuerda, \u00bfqu\u00e9 le hace a la cuerda?", "2. यदि व्यास जीवा के लंबवत है, तो यह जीवा पर क्या करता है?"),
    "2. In the general equation Ax\u00b2 + Cy\u00b2 + Dx + Ey + F = 0, if A = C, the conic is a:":
        ("2. 在一般方程 Ax\u00b2 + Cy\u00b2 + Dx + Ey + F = 0 中，如果 A = C，则圆锥曲线是：", "2. En la ecuaci\u00f3n general Ax\u00b2 + Cy\u00b2 + Dx + Ey + F = 0, si A = C, la c\u00f3nica es un:", "2. सामान्य समीकरण Ax\u00b2 + Cy\u00b2 + Dx + Ey + F = 0 में, यदि A = C, तो शंकु वक्र है:"),
    "2. The fixed point around which a rotation occurs is called the __________.":
        ("2. 旋转围绕的固定点称为__________。", "2. El punto fijo alrededor del cual ocurre una rotaci\u00f3n se llama __________.", "2. जिस स्थिर बिंदु के चारों ओर घूर्णन होता है उसे __________ कहते हैं।"),
    "2. The magnitude of vector <3, 4> is:":
        ("2. 向量 <3, 4> 的模为：", "2. La magnitud del vector <3, 4> es:", "2. सदिश <3, 4> का परिमाण है:"),
    "2. To estimate \u03c0 using Monte Carlo, you randomly generate points in a square and check if they fall inside a quarter circle. If 785 out of 1000 points land inside, what is the estimate for \u03c0?":
        ("2. 用蒙特卡洛方法估计 \u03c0，你在正方形中随机生成点并检查它们是否落在四分之一圆内。如果 1000 个点中有 785 个落在内部，\u03c0 的估计值是多少？", "2. Para estimar \u03c0 usando Monte Carlo, generas puntos aleatorios en un cuadrado y verificas si caen dentro de un cuarto de c\u00edrculo. Si 785 de 1000 puntos caen dentro, \u00bfcu\u00e1l es la estimaci\u00f3n de \u03c0?", "2. मोंटे कार्लो का उपयोग करके \u03c0 का अनुमान लगाने के लिए, आप एक वर्ग में यादृच्छिक बिंदु उत्पन्न करते हैं और जाँचते हैं कि वे चौथाई वृत्त के अंदर आते हैं या नहीं। यदि 1000 में से 785 बिंदु अंदर आते हैं, तो \u03c0 का अनुमान क्या है?"),
    "2. Two reflections over parallel lines that are 5 units apart produce which transformation?":
        ("2. 相距 5 个单位的两条平行线上的两次反射产生哪种变换？", "2. \u00bfQu\u00e9 transformaci\u00f3n producen dos reflexiones sobre l\u00edneas paralelas que est\u00e1n a 5 unidades de distancia?", "2. 5 इकाई दूर समांतर रेखाओं पर दो परावर्तन कौन सा रूपांतरण उत्पन्न करते हैं?"),
    "2. Two secants drawn from an external point form an angle equal to:":
        ("2. 从外部点引出的两条割线所形成的角等于：", "2. Dos secantes trazadas desde un punto externo forman un \u00e1ngulo igual a:", "2. एक बाह्य बिंदु से खींची गई दो छेदक रेखाएँ जो कोण बनाती हैं वह बराबर होता है:"),
    "2. Two similar solids have a scale factor of k. What is the ratio of their volumes?":
        ("2. 两个相似立体的比例因子为 k。它们的体积比是多少？", "2. Dos s\u00f3lidos similares tienen un factor de escala k. \u00bfCu\u00e1l es la raz\u00f3n de sus vol\u00famenes?", "2. दो समरूप ठोसों का स्केल गुणक k है। उनके आयतनों का अनुपात क्या है?"),
    "2. Two similar triangles have areas of 16 cm\u00b2 and 64 cm\u00b2. What is the scale factor of their corresponding sides?":
        ("2. 两个相似三角形的面积分别为 16 cm\u00b2 和 64 cm\u00b2。它们对应边的比例因子是多少？", "2. Dos tri\u00e1ngulos similares tienen \u00e1reas de 16 cm\u00b2 y 64 cm\u00b2. \u00bfCu\u00e1l es el factor de escala de sus lados correspondientes?", "2. दो समरूप त्रिभुजों के क्षेत्रफल 16 cm\u00b2 और 64 cm\u00b2 हैं। उनकी संगत भुजाओं का स्केल गुणक क्या है?"),
    "2. Two tangent segments drawn from the same external point are:":
        ("2. 从同一外部点引出的两条切线段是：", "2. Dos segmentos tangentes trazados desde el mismo punto externo son:", "2. एक ही बाह्य बिंदु से खींचे गए दो स्पर्शरेखा खंड हैं:"),
    "2. What does Euler's formula state for polyhedra?":
        ("2. 欧拉公式对多面体是什么？", "2. \u00bfQu\u00e9 establece la f\u00f3rmula de Euler para poliedros?", "2. बहुफलकों के लिए यूलर का सूत्र क्या कहता है?"),
    "2. What is a net in geometry?":
        ("2. 几何中的展开图是什么？", "2. \u00bfQu\u00e9 es una red en geometr\u00eda?", "2. ज्यामिति में जाल क्या है?"),
    "2. What is the area of a sector with radius 10 cm and central angle 90\u00b0?":
        ("2. 半径为 10 厘米、圆心角为 90\u00b0 的扇形面积是多少？", "2. \u00bfCu\u00e1l es el \u00e1rea de un sector con radio de 10 cm y \u00e1ngulo central de 90\u00b0?", "2. 10 सेमी त्रिज्या और 90\u00b0 केंद्रीय कोण वाले त्रिज्यखंड का क्षेत्रफल क्या है?"),
    "2. What is the area of a triangle with a base of 14 cm and a height of 9 cm?":
        ("2. 底为 14 厘米、高为 9 厘米的三角形面积是多少？", "2. \u00bfCu\u00e1l es el \u00e1rea de un tri\u00e1ngulo con base de 14 cm y altura de 9 cm?", "2. 14 सेमी आधार और 9 सेमी ऊँचाई वाले त्रिभुज का क्षेत्रफल क्या है?"),
    "2. What is the center and radius of the circle (x \u2212 3)\u00b2 + (y + 2)\u00b2 = 25?":
        ("2. 圆 (x \u2212 3)\u00b2 + (y + 2)\u00b2 = 25 的圆心和半径是什么？", "2. \u00bfCu\u00e1l es el centro y radio del c\u00edrculo (x \u2212 3)\u00b2 + (y + 2)\u00b2 = 25?", "2. वृत्त (x \u2212 3)\u00b2 + (y + 2)\u00b2 = 25 का केंद्र और त्रिज्या क्या है?"),
    "2. What is the central angle of a regular hexagon?":
        ("2. 正六边形的中心角是多少？", "2. \u00bfCu\u00e1l es el \u00e1ngulo central de un hex\u00e1gono regular?", "2. एक नियमित षट्भुज का केंद्रीय कोण क्या है?"),
    "2. What is the image of (5, \u22122) after the translation \u27e8\u22123, 4\u27e9?":
        ("2. (5, \u22122) 经平移 \u27e8\u22123, 4\u27e9 后的像是什么？", "2. \u00bfCu\u00e1l es la imagen de (5, \u22122) despu\u00e9s de la traslaci\u00f3n \u27e8\u22123, 4\u27e9?", "2. स्थानांतरण \u27e8\u22123, 4\u27e9 के बाद (5, \u22122) का प्रतिबिंब क्या है?"),
    "2. What is the order of rotational symmetry for a regular pentagon?":
        ("2. 正五边形的旋转对称阶数是多少？", "2. \u00bfCu\u00e1l es el orden de simetr\u00eda rotacional de un pent\u00e1gono regular?", "2. एक नियमित पंचभुज की घूर्णन समरूपता का क्रम क्या है?"),
    "2. What is the probability of rolling a 2 or a 5 on a standard die?":
        ("2. 掷一个标准骰子掷出 2 或 5 的概率是多少？", "2. \u00bfCu\u00e1l es la probabilidad de sacar un 2 o un 5 en un dado est\u00e1ndar?", "2. एक मानक पासे पर 2 या 5 आने की प्रायिकता क्या है?"),
    "2. What is the value of P(6, 2)?":
        ("2. P(6, 2) 的值是多少？", "2. \u00bfCu\u00e1l es el valor de P(6, 2)?", "2. P(6, 2) का मान क्या है?"),
    "2. What is the volume formula for a sphere?":
        ("2. 球体的体积公式是什么？", "2. \u00bfCu\u00e1l es la f\u00f3rmula del volumen de una esfera?", "2. गोले के आयतन का सूत्र क्या है?"),
    "2. When dividing the interval [a, b] into n subintervals, what is the width \u0394x of each subinterval?":
        ("2. 将区间 [a, b] 分成 n 个子区间时，每个子区间的宽度 \u0394x 是多少？", "2. Al dividir el intervalo [a, b] en n subintervalos, \u00bfcu\u00e1l es el ancho \u0394x de cada subintervalo?", "2. अंतराल [a, b] को n उप-अंतरालों में विभाजित करते समय, प्रत्येक उप-अंतराल की चौड़ाई \u0394x क्या है?"),
    "2. Which everyday analogy best illustrates Cavalieri's Principle?":
        ("2. 哪个日常类比最好地说明了卡瓦列里原理？", "2. \u00bfQu\u00e9 analog\u00eda cotidiana ilustra mejor el Principio de Cavalieri?", "2. कौन सी दैनिक उपमा कैवलिएरी के सिद्धांत को सबसे अच्छी तरह स्पष्ट करती है?"),
    "2. Why are there no parallel lines in spherical geometry?":
        ("2. 为什么球面几何中没有平行线？", "2. \u00bfPor qu\u00e9 no hay l\u00edneas paralelas en geometr\u00eda esf\u00e9rica?", "2. गोलीय ज्यामिति में समांतर रेखाएँ क्यों नहीं हैं?"),
    "3. A chord of a circle is best described as:":
        ("3. 圆的弦最好描述为：", "3. Una cuerda de un c\u00edrculo se describe mejor como:", "3. एक वृत्त की जीवा को सबसे अच्छे ढंग से वर्णित किया जाता है:"),
    "3. A common internal tangent of two circles:":
        ("3. 两个圆的公内切线：", "3. Una tangente interna com\u00fan de dos c\u00edrculos:", "3. दो वृत्तों की उभयनिष्ठ आंतरिक स्पर्शरेखा:"),
    "3. A figure has point symmetry if it maps onto itself after a rotation of __________.":
        ("3. 如果一个图形旋转__________后能映射到自身，则该图形具有点对称性。", "3. Una figura tiene simetr\u00eda puntual si se mapea sobre s\u00ed misma despu\u00e9s de una rotaci\u00f3n de __________.", "3. एक आकृति में बिंदु समरूपता होती है यदि यह __________ के घूर्णन के बाद स्वयं पर प्रतिचित्रित होती है।"),
    "3. A parabola is defined as the set of all points equidistant from:":
        ("3. 抛物线定义为到以下两者等距的所有点的集合：", "3. Una par\u00e1bola se define como el conjunto de todos los puntos equidistantes de:", "3. एक परवलय को किससे समदूरस्थ सभी बिंदुओं के समुच्चय के रूप में परिभाषित किया जाता है:"),
    "3. A sphere has a radius of 6 cm. What is its surface area? (Use \u03c0 \u2248 3.14)":
        ("3. 一个球体的半径为 6 厘米。它的表面积是多少？（取 \u03c0 \u2248 3.14）", "3. Una esfera tiene un radio de 6 cm. \u00bfCu\u00e1l es su \u00e1rea de superficie? (Usa \u03c0 \u2248 3.14)", "3. एक गोले की त्रिज्या 6 सेमी है। इसका पृष्ठीय क्षेत्रफल क्या है? (\u03c0 \u2248 3.14 लें)"),
    "3. A spinner is divided into sectors. A winning sector has a central angle of 90\u00b0. What is the probability of landing on the winning sector?":
        ("3. 一个转盘分成多个扇区。获胜扇区的圆心角为 90\u00b0。落在获胜扇区的概率是多少？", "3. Un spinner est\u00e1 dividido en sectores. Un sector ganador tiene un \u00e1ngulo central de 90\u00b0. \u00bfCu\u00e1l es la probabilidad de caer en el sector ganador?", "3. एक स्पिनर त्रिज्यखंडों में विभाजित है। विजयी त्रिज्यखंड का केंद्रीय कोण 90\u00b0 है। विजयी त्रिज्यखंड पर आने की प्रायिकता क्या है?"),
    "3. A tangent and a chord meet at a point on the circle. The angle formed equals:":
        ("3. 切线和弦在圆上一点相交。所形成的角等于：", "3. Una tangente y una cuerda se encuentran en un punto del c\u00edrculo. El \u00e1ngulo formado es igual a:", "3. एक स्पर्शरेखा और जीवा वृत्त पर एक बिंदु पर मिलती हैं। बना कोण बराबर होता है:"),
    "3. A tangent and a secant are drawn from the same external point. If the tangent = 6 and the whole secant = 9, what is the external segment of the secant?":
        ("3. 从同一外部点引出切线和割线。如果切线 = 6，整条割线 = 9，割线的外部线段是多少？", "3. Se trazan una tangente y una secante desde el mismo punto externo. Si la tangente = 6 y la secante completa = 9, \u00bfcu\u00e1l es el segmento externo de la secante?", "3. एक ही बाह्य बिंदु से एक स्पर्शरेखा और एक छेदक खींची जाती हैं। यदि स्पर्शरेखा = 6 और पूरी छेदक = 9, तो छेदक का बाह्य खंड क्या है?"),
    "3. According to Euler's formula, if a polyhedron has 8 vertices and 12 edges, how many faces does it have?":
        ("3. 根据欧拉公式，如果一个多面体有 8 个顶点和 12 条棱，它有多少个面？", "3. Seg\u00fan la f\u00f3rmula de Euler, si un poliedro tiene 8 v\u00e9rtices y 12 aristas, \u00bfcu\u00e1ntas caras tiene?", "3. यूलर के सूत्र के अनुसार, यदि एक बहुफलक में 8 शीर्ष और 12 किनारे हैं, तो इसके कितने फलक हैं?"),
    "3. Adding vectors <2, 5> and <3, -1> gives:":
        ("3. 向量 <2, 5> 和 <3, -1> 相加得到：", "3. Sumar los vectores <2, 5> y <3, -1> da:", "3. सदिश <2, 5> और <3, -1> को जोड़ने पर मिलता है:"),
    "3. An inscribed angle that intercepts a semicircle has a measure of:":
        ("3. 截半圆的圆内接角的度数为：", "3. Un \u00e1ngulo inscrito que intercepta un semic\u00edrculo tiene una medida de:", "3. एक अर्धवृत्त को काटने वाले अंतर्लिखित कोण का माप है:"),
    "3. Cavalieri's Principle proves that an oblique cylinder and a right cylinder with the same base and height have:":
        ("3. 卡瓦列里原理证明同底同高的斜圆柱和直圆柱具有：", "3. El Principio de Cavalieri demuestra que un cilindro oblicuo y un cilindro recto con la misma base y altura tienen:", "3. कैवलिएरी का सिद्धांत सिद्ध करता है कि समान आधार और ऊँचाई वाले तिरछे बेलन और सीधे बेलन में:"),
    "3. Drawing cards without replacement is an example of:":
        ("3. 无放回抽牌是以下哪种的例子：", "3. Sacar cartas sin reemplazo es un ejemplo de:", "3. बिना प्रतिस्थापन के पत्ते निकालना किसका उदाहरण है:"),
    "3. For events that are NOT mutually exclusive, P(A or B) equals:":
        ("3. 对于不互斥的事件，P(A 或 B) 等于：", "3. Para eventos que NO son mutuamente excluyentes, P(A o B) es igual a:", "3. जो घटनाएँ परस्पर अपवर्जी नहीं हैं, उनके लिए P(A या B) बराबर होता है:"),
    "3. How can Monte Carlo methods estimate the area of an irregular shape?":
        ("3. 蒙特卡洛方法如何估算不规则形状的面积？", "3. \u00bfC\u00f3mo pueden los m\u00e9todos Monte Carlo estimar el \u00e1rea de una forma irregular?", "3. मोंटे कार्लो विधियाँ किसी अनियमित आकार का क्षेत्रफल कैसे अनुमानित कर सकती हैं?"),
    "3. How many angles does a transversal create when crossing two lines?":
        ("3. 一条截线穿过两条直线时形成多少个角？", "3. \u00bfCu\u00e1ntos \u00e1ngulos crea una transversal al cruzar dos l\u00edneas?", "3. एक तिर्यक रेखा दो रेखाओं को काटते समय कितने कोण बनाती है?"),
    "3. How many ways can a committee of 3 be chosen from 10 people?":
        ("3. 从 10 人中选出 3 人委员会有多少种方式？", "3. \u00bfDe cu\u00e1ntas formas se puede elegir un comit\u00e9 de 3 personas de entre 10?", "3. 10 लोगों में से 3 की समिति कितने तरीकों से चुनी जा सकती है?"),
    "3. If the scale factor between two similar figures is 2:7, what is the ratio of their perimeters?":
        ("3. 如果两个相似图形的比例因子为 2:7，它们的周长比是多少？", "3. Si el factor de escala entre dos figuras similares es 2:7, \u00bfcu\u00e1l es la raz\u00f3n de sus per\u00edmetros?", "3. यदि दो समरूप आकृतियों के बीच स्केल गुणक 2:7 है, तो उनके परिमापों का अनुपात क्या है?"),
    "3. Is a dilation an isometry?":
        ("3. 缩放是等距变换吗？", "3. \u00bfUna dilataci\u00f3n es una isometr\u00eda?", "3. क्या विस्तारण एक समदूरी है?"),
    "3. Is a translation an isometry?":
        ("3. 平移是等距变换吗？", "3. \u00bfUna traslaci\u00f3n es una isometr\u00eda?", "3. क्या स्थानांतरण एक समदूरी है?"),
    "3. The apothem of a regular polygon is defined as:":
        ("3. 正多边形的边心距定义为：", "3. La apotema de un pol\u00edgono regular se define como:", "3. एक नियमित बहुभुज का अपोथेम इस प्रकार परिभाषित किया जाता है:"),
    "3. The equation x\u00b2 + y\u00b2 = 49 represents a circle centered at:":
        ("3. 方程 x\u00b2 + y\u00b2 = 49 表示以哪个点为圆心的圆：", "3. La ecuaci\u00f3n x\u00b2 + y\u00b2 = 49 representa un c\u00edrculo centrado en:", "3. समीकरण x\u00b2 + y\u00b2 = 49 किस पर केंद्रित वृत्त को दर्शाता है:"),
    "3. The height used to calculate the area of a parallelogram must be:":
        ("3. 用于计算平行四边形面积的高必须是：", "3. La altura usada para calcular el \u00e1rea de un paralelogramo debe ser:", "3. समांतर चतुर्भुज के क्षेत्रफल की गणना के लिए उपयोग की जाने वाली ऊँचाई होनी चाहिए:"),
    "3. The longest chord of any circle is the:":
        ("3. 任何圆的最长弦是：", "3. La cuerda m\u00e1s larga de cualquier c\u00edrculo es:", "3. किसी भी वृत्त की सबसे लंबी जीवा है:"),
    "3. The sum of angles in a spherical triangle is always:":
        ("3. 球面三角形的角之和总是：", "3. La suma de los \u00e1ngulos en un tri\u00e1ngulo esf\u00e9rico siempre es:", "3. गोलीय त्रिभुज में कोणों का योग हमेशा होता है:"),
    "3. Two reflections over intersecting lines that form a 35\u00b0 angle produce which transformation?":
        ("3. 两条相交且成 35\u00b0 角的直线上的两次反射产生哪种变换？", "3. \u00bfQu\u00e9 transformaci\u00f3n producen dos reflexiones sobre l\u00edneas que se cruzan formando un \u00e1ngulo de 35\u00b0?", "3. 35\u00b0 कोण बनाने वाली प्रतिच्छेदी रेखाओं पर दो परावर्तन कौन सा रूपांतरण उत्पन्न करते हैं?"),
    "3. Two similar cylinders have surface areas of 25\u03c0 and 100\u03c0. What is the scale factor?":
        ("3. 两个相似圆柱的表面积分别为 25\u03c0 和 100\u03c0。比例因子是多少？", "3. Dos cilindros similares tienen \u00e1reas de superficie de 25\u03c0 y 100\u03c0. \u00bfCu\u00e1l es el factor de escala?", "3. दो समरूप बेलनों का पृष्ठीय क्षेत्रफल 25\u03c0 और 100\u03c0 है। स्केल गुणक क्या है?"),
    "3. Using the Fundamental Counting Principle, how many outcomes are there when rolling two dice?":
        ("3. 使用基本计数原理，掷两个骰子有多少种结果？", "3. Usando el Principio Fundamental de Conteo, \u00bfcu\u00e1ntos resultados hay al lanzar dos dados?", "3. मूलभूत गणना सिद्धांत का उपयोग करते हुए, दो पासे फेंकने पर कितने परिणाम होते हैं?"),
    "3. What is the arc length of a sector with radius 6 cm and central angle 60\u00b0?":
        ("3. 半径 6 厘米、圆心角 60\u00b0 的扇形弧长是多少？", "3. \u00bfCu\u00e1l es la longitud de arco de un sector con radio de 6 cm y \u00e1ngulo central de 60\u00b0?", "3. 6 सेमी त्रिज्या और 60\u00b0 केंद्रीय कोण वाले त्रिज्यखंड की चाप लंबाई क्या है?"),
    "3. What is the area of a kite with diagonals of 12 m and 7 m?":
        ("3. 对角线分别为 12 米和 7 米的筝形面积是多少？", "3. \u00bfCu\u00e1l es el \u00e1rea de una cometa con diagonales de 12 m y 7 m?", "3. 12 मी और 7 मी विकर्ण वाली पतंग का क्षेत्रफल क्या है?"),
    "3. What is the area under y = x from x = 0 to x = 4?":
        ("3. 从 x = 0 到 x = 4，y = x 曲线下的面积是多少？", "3. \u00bfCu\u00e1l es el \u00e1rea bajo y = x desde x = 0 hasta x = 4?", "3. x = 0 से x = 4 तक y = x के नीचे का क्षेत्रफल क्या है?"),
    "3. What is the contrapositive of 'If p, then q'?":
        ("3.\u201c如果 p，则 q\u201d的逆否命题是什么？", "3. \u00bfCu\u00e1l es el contrarrec\u00edproco de 'Si p, entonces q'?", "3. 'यदि p, तो q' का प्रतिधनात्मक क्या है?"),
    "3. What is the coordinate rule for a 180\u00b0 rotation about the origin?":
        ("3. 绕原点旋转 180\u00b0 的坐标规则是什么？", "3. \u00bfCu\u00e1l es la regla de coordenadas para una rotaci\u00f3n de 180\u00b0 alrededor del origen?", "3. मूल बिंदु के चारों ओर 180\u00b0 घूर्णन का निर्देशांक नियम क्या है?"),
    "3. What is the first step in designing a simulation?":
        ("3. 设计模拟的第一步是什么？", "3. \u00bfCu\u00e1l es el primer paso para dise\u00f1ar una simulaci\u00f3n?", "3. अनुकरण डिजाइन करने का पहला चरण क्या है?"),
    "3. What is the image of (\u22122, 7) after a reflection over the line y = x?":
        ("3. (\u22122, 7) 关于直线 y = x 反射后的像是什么？", "3. \u00bfCu\u00e1l es la imagen de (\u22122, 7) despu\u00e9s de una reflexi\u00f3n sobre la l\u00ednea y = x?", "3. रेखा y = x पर परावर्तन के बाद (\u22122, 7) का प्रतिबिंब क्या है?"),
    "3. What is the measure of a semicircle?":
        ("3. 半圆的度数是多少？", "3. \u00bfCu\u00e1l es la medida de un semic\u00edrculo?", "3. एक अर्धवृत्त का माप क्या है?"),
    "3. What is the surface area formula for a cone?":
        ("3. 圆锥的表面积公式是什么？", "3. \u00bfCu\u00e1l es la f\u00f3rmula del \u00e1rea de superficie de un cono?", "3. शंकु के पृष्ठीय क्षेत्रफल का सूत्र क्या है?"),
    "3. What is the surface area formula for a cylinder?":
        ("3. 圆柱的表面积公式是什么？", "3. \u00bfCu\u00e1l es la f\u00f3rmula del \u00e1rea de superficie de un cilindro?", "3. बेलन के पृष्ठीय क्षेत्रफल का सूत्र क्या है?"),
    "3. What is the volume formula for a cone?":
        ("3. 圆锥的体积公式是什么？", "3. \u00bfCu\u00e1l es la f\u00f3rmula del volumen de un cono?", "3. शंकु के आयतन का सूत्र क्या है?"),
    "3. What is the volume formula for a cylinder?":
        ("3. 圆柱的体积公式是什么？", "3. \u00bfCu\u00e1l es la f\u00f3rmula del volumen de un cilindro?", "3. बेलन के आयतन का सूत्र क्या है?"),
    "3. Which coordinate rule represents a 90\u00b0 counterclockwise rotation?":
        ("3. 哪个坐标规则表示逆时针旋转 90\u00b0？", "3. \u00bfQu\u00e9 regla de coordenadas representa una rotaci\u00f3n de 90\u00b0 en sentido antihorario?", "3. कौन सा निर्देशांक नियम 90\u00b0 वामावर्त घूर्णन को दर्शाता है?"),
    "4. A 270\u00b0 counterclockwise rotation is the same as which clockwise rotation?":
        ("4. 逆时针旋转 270\u00b0 等同于哪个顺时针旋转？", "4. Una rotaci\u00f3n de 270\u00b0 en sentido antihorario es igual a qu\u00e9 rotaci\u00f3n en sentido horario?", "4. 270\u00b0 वामावर्त घूर्णन किस दक्षिणावर्त घूर्णन के समान है?"),
    "4. A cone has a height of 12 cm and a radius of 5 cm. What is its slant height?":
        ("4. 一个圆锥的高为 12 厘米，半径为 5 厘米。它的斜高是多少？", "4. Un cono tiene una altura de 12 cm y un radio de 5 cm. \u00bfCu\u00e1l es su altura inclinada?", "4. एक शंकु की ऊँचाई 12 सेमी और त्रिज्या 5 सेमी है। इसकी तिरछी ऊँचाई क्या है?"),
    "4. A cylinder has a radius of 4 cm and a height of 10 cm. What is its lateral area? (Use \u03c0 \u2248 3.14)":
        ("4. 一个圆柱的半径为 4 厘米，高为 10 厘米。它的侧面积是多少？（取 \u03c0 \u2248 3.14）", "4. Un cilindro tiene un radio de 4 cm y una altura de 10 cm. \u00bfCu\u00e1l es su \u00e1rea lateral? (Usa \u03c0 \u2248 3.14)", "4. एक बेलन की त्रिज्या 4 सेमी और ऊँचाई 10 सेमी है। इसका पार्श्व क्षेत्रफल क्या है? (\u03c0 \u2248 3.14 लें)"),
    "4. A diagonal of a parallelogram divides it into:":
        ("4. 平行四边形的对角线将其分为：", "4. Una diagonal de un paralelogramo lo divide en:", "4. समांतर चतुर्भुज का विकर्ण इसे किसमें विभाजित करता है:"),
    "4. A dilation preserves which of the following?":
        ("4. 缩放保留以下哪项？", "4. \u00bfCu\u00e1l de los siguientes preserva una dilataci\u00f3n?", "4. विस्तारण निम्नलिखित में से क्या संरक्षित करता है?"),
    "4. A figure has an area of 50 cm\u00b2. A similar figure has a scale factor of 3 relative to the original. What is the area of the larger figure?":
        ("4. 一个图形的面积为 50 cm\u00b2。一个相似图形相对于原图形的比例因子为 3。较大图形的面积是多少？", "4. Una figura tiene un \u00e1rea de 50 cm\u00b2. Una figura similar tiene un factor de escala de 3 respecto a la original. \u00bfCu\u00e1l es el \u00e1rea de la figura mayor?", "4. एक आकृति का क्षेत्रफल 50 cm\u00b2 है। एक समरूप आकृति का मूल के सापेक्ष स्केल गुणक 3 है। बड़ी आकृति का क्षेत्रफल क्या है?"),
    "4. A polygon whose sides are all tangent to an inscribed circle is called a:":
        ("4. 所有边都与内切圆相切的多边形称为：", "4. Un pol\u00edgono cuyos lados son todos tangentes a un c\u00edrculo inscrito se llama:", "4. एक बहुभुज जिसकी सभी भुजाएँ अंतर्लिखित वृत्त की स्पर्शरेखा हैं, कहलाता है:"),
    "4. A tree casts a 20 ft shadow when the sun's angle of elevation is 40\u00b0. The tree's height is about:":
        ("4. 当太阳仰角为 40\u00b0 时，一棵树投射 20 英尺的阴影。树的高度大约为：", "4. Un \u00e1rbol proyecta una sombra de 20 pies cuando el \u00e1ngulo de elevaci\u00f3n del sol es de 40\u00b0. La altura del \u00e1rbol es aproximadamente:", "4. जब सूर्य का उन्नयन कोण 40\u00b0 हो तब एक पेड़ 20 फुट की छाया बनाता है। पेड़ की ऊँचाई लगभग है:"),
    "4. Are compositions of transformations commutative (does order matter)?":
        ("4. 变换的组合是可交换的吗（顺序重要吗）？", "4. \u00bfSon conmutativas las composiciones de transformaciones (importa el orden)?", "4. क्या रूपांतरणों का संयोजन क्रम-विनिमेय है (क्या क्रम मायने रखता है)?"),
    "4. As the number of subintervals n approaches infinity, the Riemann sum approximation becomes:":
        ("4. 当子区间数 n 趋向无穷时，黎曼和近似变为：", "4. A medida que el n\u00famero de subintervalos n se acerca al infinito, la aproximaci\u00f3n de la suma de Riemann se convierte en:", "4. जब उप-अंतरालों की संख्या n अनंत की ओर जाती है, तो रीमान योग सन्निकटन बन जाता है:"),
    "4. For an ellipse, the sum of the distances from any point on the ellipse to the two foci is:":
        ("4. 对于椭圆，椭圆上任意一点到两个焦点的距离之和为：", "4. Para una elipse, la suma de las distancias desde cualquier punto de la elipse a los dos focos es:", "4. दीर्घवृत्त के लिए, दीर्घवृत्त पर किसी भी बिंदु से दो नाभियों तक की दूरियों का योग है:"),
    "4. For dependent events A and B, P(A and B) equals:":
        ("4. 对于相关事件 A 和 B，P(A 且 B) 等于：", "4. Para eventos dependientes A y B, P(A y B) es igual a:", "4. आश्रित घटनाओं A और B के लिए, P(A और B) बराबर होता है:"),
    "4. How can you find the center of rotation given a point and its image?":
        ("4. 给定一个点及其像，如何找到旋转中心？", "4. \u00bfC\u00f3mo se encuentra el centro de rotaci\u00f3n dado un punto y su imagen?", "4. एक बिंदु और उसके प्रतिबिंब दिए होने पर आप घूर्णन केंद्र कैसे ज्ञात कर सकते हैं?"),
    "4. How does accuracy of a Monte Carlo estimate change when the number of samples increases?":
        ("4. 当样本数量增加时，蒙特卡洛估计的准确度如何变化？", "4. \u00bfC\u00f3mo cambia la precisi\u00f3n de una estimaci\u00f3n Monte Carlo cuando aumenta el n\u00famero de muestras?", "4. नमूनों की संख्या बढ़ने पर मोंटे कार्लो अनुमान की सटीकता कैसे बदलती है?"),
    "4. How does the volume of a pyramid compare to a prism with the same base and height?":
        ("4. 棱锥的体积与同底同高棱柱相比如何？", "4. \u00bfC\u00f3mo se compara el volumen de una pir\u00e1mide con el de un prisma con la misma base y altura?", "4. एक पिरामिड का आयतन समान आधार और ऊँचाई वाले प्रिज्म से कैसे तुलना करता है?"),
    "4. How many lines of symmetry does a circle have?":
        ("4. 一个圆有多少条对称轴？", "4. \u00bfCu\u00e1ntos ejes de simetr\u00eda tiene un c\u00edrculo?", "4. एक वृत्त में कितनी समरूपता रेखाएँ हैं?"),
    "4. If angle A > angle B in \u25b3ABC, then:":
        ("4. 在 \u25b3ABC 中，如果角 A > 角 B，则：", "4. Si el \u00e1ngulo A > \u00e1ngulo B en \u25b3ABC, entonces:", "4. \u25b3ABC में यदि कोण A > कोण B, तो:"),
    "4. If the radius of a cylinder is doubled while the height stays the same, how does the volume change?":
        ("4. 如果圆柱的半径加倍而高度不变，体积如何变化？", "4. Si el radio de un cilindro se duplica mientras la altura permanece igual, \u00bfc\u00f3mo cambia el volumen?", "4. यदि बेलन की त्रिज्या दोगुनी कर दी जाए जबकि ऊँचाई समान रहे, तो आयतन कैसे बदलता है?"),
    "4. In the method of disks, what shape are the thin cross-sections used?":
        ("4. 在圆盘法中，使用的薄截面是什么形状？", "4. En el m\u00e9todo de discos, \u00bfqu\u00e9 forma tienen las secciones transversales delgadas utilizadas?", "4. डिस्क विधि में, उपयोग किए जाने वाले पतले अनुप्रस्थ काट किस आकार के होते हैं?"),
    "4. Scalar multiplication 3 \u00d7 <2, -1> =":
        ("4. 标量乘法 3 \u00d7 <2, -1> =", "4. Multiplicaci\u00f3n escalar 3 \u00d7 <2, -1> =", "4. अदिश गुणन 3 \u00d7 <2, -1> ="),
    "4. The Arc Addition Postulate states that adjacent arcs:":
        ("4. 弧加法公设指出相邻弧：", "4. El Postulado de Adici\u00f3n de Arcos establece que arcos adyacentes:", "4. चाप योग अभिगृहीत कहता है कि निकटवर्ती चाप:"),
    "4. The area of a segment of a circle is found by:":
        ("4. 圆弓形的面积通过以下方式求得：", "4. El \u00e1rea de un segmento de un c\u00edrculo se encuentra mediante:", "4. एक वृत्त के खंड का क्षेत्रफल किसके द्वारा ज्ञात किया जाता है:"),
    "4. The line of reflection is the __________ of the segment connecting a point and its image.":
        ("4. 反射线是连接一个点和其像的线段的__________。", "4. La l\u00ednea de reflexi\u00f3n es __________ del segmento que conecta un punto y su imagen.", "4. परावर्तन रेखा एक बिंदु और उसके प्रतिबिंब को जोड़ने वाले रेखाखंड का __________ है।"),
    "4. The median of a trapezoid with bases 6 and 18 is:":
        ("4. 上底为 6、下底为 18 的梯形中位线为：", "4. La mediana de un trapecio con bases 6 y 18 es:", "4. आधार 6 और 18 वाले समलंब की माध्यिका है:"),
    "4. The secant-tangent relationship states that tangent\u00b2 equals:":
        ("4. 割线-切线关系指出切线\u00b2 等于：", "4. La relaci\u00f3n secante-tangente establece que tangente\u00b2 es igual a:", "4. छेदक-स्पर्शरेखा संबंध कहता है कि स्पर्शरेखा\u00b2 बराबर होती है:"),
    "4. Three concentric circles have radii 1, 2, and 3. What is the probability that a randomly thrown dart lands in the innermost circle?":
        ("4. 三个同心圆的半径分别为 1、2 和 3。飞镖随机投掷后落在最内圈的概率是多少？", "4. Tres c\u00edrculos conc\u00e9ntricos tienen radios 1, 2 y 3. \u00bfCu\u00e1l es la probabilidad de que un dardo lanzado al azar caiga en el c\u00edrculo m\u00e1s interno?", "4. तीन संकेंद्रीय वृत्तों की त्रिज्या 1, 2, और 3 हैं। यादृच्छिक रूप से फेंके गए डार्ट के सबसे भीतरी वृत्त में गिरने की प्रायिकता क्या है?"),
    "4. To convert x\u00b2 + y\u00b2 + Dx + Ey + F = 0 to standard form, you should:":
        ("4. 要将 x\u00b2 + y\u00b2 + Dx + Ey + F = 0 转化为标准形式，你应该：", "4. Para convertir x\u00b2 + y\u00b2 + Dx + Ey + F = 0 a forma est\u00e1ndar, debes:", "4. x\u00b2 + y\u00b2 + Dx + Ey + F = 0 को मानक रूप में बदलने के लिए, आपको:"),
    "4. To prove 'a triangle cannot have two right angles' indirectly, you first assume:":
        ("4. 要间接证明\u201c三角形不能有两个直角\u201d，你首先假设：", "4. Para demostrar indirectamente que 'un tri\u00e1ngulo no puede tener dos \u00e1ngulos rectos', primero asumes:", "4. 'एक त्रिभुज में दो समकोण नहीं हो सकते' को अप्रत्यक्ष रूप से सिद्ध करने के लिए, पहले आप मानते हैं:"),
    "4. Two chords intersect inside a circle. If AE = 4, EB = 6, and CE = 3, what is ED?":
        ("4. 两条弦在圆内相交。如果 AE = 4, EB = 6, CE = 3，那么 ED 是多少？", "4. Dos cuerdas se cruzan dentro de un c\u00edrculo. Si AE = 4, EB = 6 y CE = 3, \u00bfcu\u00e1l es ED?", "4. दो जीवाएँ एक वृत्त के अंदर प्रतिच्छेद करती हैं। यदि AE = 4, EB = 6, और CE = 3, तो ED क्या है?"),
    "4. Two chords intersect inside a circle. The intercepted arcs measure 80\u00b0 and 40\u00b0. What is the angle?":
        ("4. 两条弦在圆内相交。截得的弧分别为 80\u00b0 和 40\u00b0。角度是多少？", "4. Dos cuerdas se cruzan dentro de un c\u00edrculo. Los arcos interceptados miden 80\u00b0 y 40\u00b0. \u00bfCu\u00e1l es el \u00e1ngulo?", "4. दो जीवाएँ एक वृत्त के अंदर प्रतिच्छेद करती हैं। कटे हुए चाप 80\u00b0 और 40\u00b0 मापते हैं। कोण क्या है?"),
    "4. Two inscribed angles intercept the same arc. What is true about them?":
        ("4. 两个圆内接角截同一段弧。关于它们的正确说法是什么？", "4. Dos \u00e1ngulos inscritos interceptan el mismo arco. \u00bfQu\u00e9 es verdad sobre ellos?", "4. दो अंतर्लिखित कोण एक ही चाप को काटते हैं। उनके बारे में क्या सत्य है?"),
    "4. What defines congruent solids?":
        ("4. 什么定义全等立体？", "4. \u00bfQu\u00e9 define a los s\u00f3lidos congruentes?", "4. सर्वांगसम ठोसों को क्या परिभाषित करता है?"),
    '4. What does a "trial" mean in the context of a simulation?':
        ("4. 在模拟的语境中，\u201c试验\u201d是什么意思？", '4. \u00bfQu\u00e9 significa un "ensayo" en el contexto de una simulaci\u00f3n?', '4. अनुकरण के संदर्भ में "प्रयोग" का क्या अर्थ है?'),
    "4. What happens to the orientation of a figure after a translation?":
        ("4. 平移后图形的方向会怎样？", "4. \u00bfQu\u00e9 le pasa a la orientaci\u00f3n de una figura despu\u00e9s de una traslaci\u00f3n?", "4. स्थानांतरण के बाद आकृति के अभिविन्यास पर क्या प्रभाव पड़ता है?"),
    "4. What is a great circle?":
        ("4. 什么是大圆？", "4. \u00bfQu\u00e9 es un gran c\u00edrculo?", "4. महान वृत्त क्या है?"),
    "4. What is an event in probability?":
        ("4. 概率中的事件是什么？", "4. \u00bfQu\u00e9 es un evento en probabilidad?", "4. प्रायिकता में घटना क्या है?"),
    "4. What is the circumference of a circle with a diameter of 14 cm? (Use \u03c0 \u2248 3.14)":
        ("4. 直径为 14 厘米的圆的周长是多少？（取 \u03c0 \u2248 3.14）", "4. \u00bfCu\u00e1l es la circunferencia de un c\u00edrculo con di\u00e1metro de 14 cm? (Usa \u03c0 \u2248 3.14)", "4. 14 सेमी व्यास वाले वृत्त की परिधि क्या है? (\u03c0 \u2248 3.14 लें)"),
    "4. What is the converse of 'If it rains, then the ground is wet'?":
        ("4.\u201c如果下雨，则地面是湿的\u201d的逆命题是什么？", "4. \u00bfCu\u00e1l es el rec\u00edproco de 'Si llueve, entonces el suelo est\u00e1 mojado'?", "4. 'यदि बारिश होती है, तो ज़मीन गीली होती है' का विलोम क्या है?"),
    "4. What is the interior angle of a regular octagon?":
        ("4. 正八边形的内角是多少？", "4. \u00bfCu\u00e1l es el \u00e1ngulo interior de un oct\u00e1gono regular?", "4. एक नियमित अष्टभुज का आंतरिक कोण क्या है?"),
    "4. What is the probability of drawing a King or a Heart from a standard 52-card deck?":
        ("4. 从标准 52 张牌中抽到国王或红心的概率是多少？", "4. \u00bfCu\u00e1l es la probabilidad de sacar un Rey o un Coraz\u00f3n de una baraja est\u00e1ndar de 52 cartas?", "4. मानक 52-पत्तों की गड्डी से किंग या हार्ट निकालने की प्रायिकता क्या है?"),
    "4. What is the spherical excess of a triangle?":
        ("4. 球面三角形的球面超量是什么？", "4. \u00bfCu\u00e1l es el exceso esf\u00e9rico de un tri\u00e1ngulo?", "4. एक त्रिभुज का गोलीय आधिक्य क्या है?"),
    "4. What is the value of 0! ?":
        ("4. 0! 的值是多少？", "4. \u00bfCu\u00e1l es el valor de 0!?", "4. 0! का मान क्या है?"),
    "4. Which type of drawing shows the top, front, and side views of a 3D object separately?":
        ("4. 哪种绘图类型分别显示 3D 物体的顶视图、正视图和侧视图？", "4. \u00bfQu\u00e9 tipo de dibujo muestra las vistas superior, frontal y lateral de un objeto 3D por separado?", "4. किस प्रकार का चित्र 3D वस्तु के ऊपर, सामने और पार्श्व दृश्यों को अलग-अलग दिखाता है?"),
    "5. A 1/24 scale model of a car is built. The volume of the model is what fraction of the original?":
        ("5. 制作了一辆汽车的 1/24 比例模型。模型的体积是原车的多少分之几？", "5. Se construye un modelo a escala 1/24 de un auto. \u00bfQu\u00e9 fracci\u00f3n del original es el volumen del modelo?", "5. एक कार का 1/24 स्केल मॉडल बनाया गया है। मॉडल का आयतन मूल का कितना अंश है?"),
    "5. A bag has 4 green and 6 yellow marbles. You draw two marbles without replacement. What is P(green, then green)?":
        ("5. 一个袋子里有 4 个绿色和 6 个黄色弹珠。你不放回抽两个弹珠。P(绿, 然后绿) 是多少？", "5. Una bolsa tiene 4 canicas verdes y 6 amarillas. Sacas dos canicas sin reemplazo. \u00bfCu\u00e1l es P(verde, luego verde)?", "5. एक थैले में 4 हरी और 6 पीली गोलियाँ हैं। आप बिना प्रतिस्थापन के दो गोलियाँ निकालते हैं। P(हरी, फिर हरी) क्या है?"),
    "5. A circle has a radius of 10 cm. What is the arc length of a 90\u00b0 arc?":
        ("5. 一个圆的半径为 10 厘米。90\u00b0 弧的弧长是多少？", "5. Un c\u00edrculo tiene un radio de 10 cm. \u00bfCu\u00e1l es la longitud de arco de un arco de 90\u00b0?", "5. एक वृत्त की त्रिज्या 10 सेमी है। 90\u00b0 चाप की चाप लंबाई क्या है?"),
    "5. A cone has a radius of 4 cm and a height of 9 cm. What is its volume? (Use \u03c0 \u2248 3.14)":
        ("5. 一个圆锥的半径为 4 厘米，高为 9 厘米。它的体积是多少？（取 \u03c0 \u2248 3.14）", "5. Un cono tiene un radio de 4 cm y una altura de 9 cm. \u00bfCu\u00e1l es su volumen? (Usa \u03c0 \u2248 3.14)", "5. एक शंकु की त्रिज्या 4 सेमी और ऊँचाई 9 सेमी है। इसका आयतन क्या है? (\u03c0 \u2248 3.14 लें)"),
    "5. A line that intersects a circle at exactly one point is called a:":
        ("5. 与圆恰好相交于一点的线称为：", "5. Una l\u00ednea que intersecta un c\u00edrculo en exactamente un punto se llama:", "5. एक रेखा जो वृत्त को ठीक एक बिंदु पर प्रतिच्छेद करती है, कहलाती है:"),
    "5. A restaurant offers 4 appetizers, 6 entr\u00e9es, and 3 desserts. How many different meals (one of each) are possible?":
        ("5. 一家餐厅提供 4 道开胃菜、6 道主菜和 3 道甜点。有多少种不同的套餐（每种一道）？", "5. Un restaurante ofrece 4 aperitivos, 6 platos principales y 3 postres. \u00bfCu\u00e1ntas comidas diferentes (una de cada) son posibles?", "5. एक रेस्टोरेंट 4 स्टार्टर, 6 मुख्य व्यंजन और 3 मिठाइयाँ प्रदान करता है। कितने अलग-अलग भोजन (प्रत्येक में से एक) संभव हैं?"),
    "5. A segment is 20 cm long. A point is chosen randomly. What is the probability that the point is within the first 5 cm?":
        ("5. 一条线段长 20 厘米。随机选择一个点。该点在前 5 厘米内的概率是多少？", "5. Un segmento mide 20 cm. Se elige un punto al azar. \u00bfCu\u00e1l es la probabilidad de que el punto est\u00e9 dentro de los primeros 5 cm?", "5. एक रेखाखंड 20 सेमी लंबा है। एक बिंदु यादृच्छिक रूप से चुना जाता है। बिंदु के पहले 5 सेमी में होने की प्रायिकता क्या है?"),
    "5. A square pyramid has a base edge of 10 cm and a slant height of 12 cm. What is its surface area?":
        ("5. 一个正四棱锥的底边长为 10 厘米，斜高为 12 厘米。它的表面积是多少？", "5. Una pir\u00e1mide cuadrada tiene una arista de base de 10 cm y una altura inclinada de 12 cm. \u00bfCu\u00e1l es su \u00e1rea de superficie?", "5. एक वर्गाकार पिरामिड की आधार भुजा 10 सेमी और तिरछी ऊँचाई 12 सेमी है। इसका पृष्ठीय क्षेत्रफल क्या है?"),
    "5. A tangent segment from an external point to a circle has length 12, and the distance from the point to the center is 13. What is the radius?":
        ("5. 从外部点到圆的切线段长为 12，该点到圆心的距离为 13。半径是多少？", "5. Un segmento tangente desde un punto externo a un c\u00edrculo tiene longitud 12, y la distancia del punto al centro es 13. \u00bfCu\u00e1l es el radio?", "5. एक बाह्य बिंदु से वृत्त तक स्पर्शरेखा खंड की लंबाई 12 है, और बिंदु से केंद्र की दूरी 13 है। त्रिज्या क्या है?"),
    "5. A triangle has sides of length 5, 12, and 13. After a dilation with scale factor 2, what are the new side lengths?":
        ("5. 一个三角形的边长为 5、12 和 13。比例因子为 2 的缩放后，新的边长是多少？", "5. Un tri\u00e1ngulo tiene lados de longitud 5, 12 y 13. Despu\u00e9s de una dilataci\u00f3n con factor de escala 2, \u00bfcu\u00e1les son las nuevas longitudes de los lados?", "5. एक त्रिभुज की भुजाओं की लंबाई 5, 12 और 13 है। स्केल गुणक 2 के विस्तारण के बाद, नई भुजा लंबाइयाँ क्या हैं?"),
    "5. Does a rotation preserve orientation?":
        ("5. 旋转是否保持方向？", "5. \u00bfUna rotaci\u00f3n preserva la orientaci\u00f3n?", "5. क्या घूर्णन अभिविन्यास को संरक्षित करता है?"),
    "5. Find the area of a triangle with sides a = 8 and b = 12 and included angle C = 30\u00b0.":
        ("5. 求边 a = 8、b = 12 且夹角 C = 30\u00b0 的三角形面积。", "5. Encuentra el \u00e1rea de un tri\u00e1ngulo con lados a = 8 y b = 12 y \u00e1ngulo incluido C = 30\u00b0.", "5. भुजा a = 8 और b = 12 तथा अंतर्विष्ट कोण C = 30\u00b0 वाले त्रिभुज का क्षेत्रफल ज्ञात करें।"),
    "5. How is the volume of a sphere derived using Cavalieri's Principle?":
        ("5. 如何使用卡瓦列里原理推导球体的体积？", "5. \u00bfC\u00f3mo se deriva el volumen de una esfera usando el Principio de Cavalieri?", "5. कैवलिएरी के सिद्धांत का उपयोग करके गोले का आयतन कैसे प्राप्त किया जाता है?"),
    "5. If 'All dogs are mammals' and 'Rex is a dog,' then:":
        ("5. 如果\u201c所有的狗都是哺乳动物\u201d且\u201cRex 是一只狗\u201d，则：", "5. Si 'Todos los perros son mam\u00edferos' y 'Rex es un perro', entonces:", "5. यदि 'सभी कुत्ते स्तनधारी हैं' और 'Rex एक कुत्ता है', तो:"),
    "5. If P(A) = 0.6, what is P(not A)?":
        ("5. 如果 P(A) = 0.6，那么 P(非 A) 是多少？", "5. Si P(A) = 0.6, \u00bfcu\u00e1l es P(no A)?", "5. यदि P(A) = 0.6, तो P(A नहीं) क्या है?"),
    "5. If a\u00b2 + b\u00b2 > c\u00b2, the triangle is:":
        ("5. 如果 a\u00b2 + b\u00b2 > c\u00b2，则三角形是：", "5. Si a\u00b2 + b\u00b2 > c\u00b2, el tri\u00e1ngulo es:", "5. यदि a\u00b2 + b\u00b2 > c\u00b2, तो त्रिभुज है:"),
    "5. In an inscribed quadrilateral, opposite angles are:":
        ("5. 在圆内接四边形中，对角的关系是：", "5. En un cuadril\u00e1tero inscrito, los \u00e1ngulos opuestos son:", "5. एक अंतर्लिखित चतुर्भुज में, सम्मुख कोण हैं:"),
    "5. Line symmetry means that a figure can be mapped onto itself by a __________.":
        ("5. 线对称意味着图形可以通过__________映射到自身。", "5. La simetr\u00eda lineal significa que una figura puede mapearse sobre s\u00ed misma mediante un __________.", "5. रेखा समरूपता का अर्थ है कि एक आकृति __________ द्वारा स्वयं पर प्रतिचित्रित हो सकती है।"),
    "5. The direction angle of vector <1, 1> is:":
        ("5. 向量 <1, 1> 的方向角为：", "5. El \u00e1ngulo de direcci\u00f3n del vector <1, 1> es:", "5. सदिश <1, 1> का दिशा कोण है:"),
    "5. The eccentricity of a circle is:":
        ("5. 圆的离心率为：", "5. La excentricidad de un c\u00edrculo es:", "5. एक वृत्त की उत्केंद्रता है:"),
    "5. The perpendicular bisector of a chord always passes through:":
        ("5. 弦的垂直平分线始终经过：", "5. La mediatriz de una cuerda siempre pasa por:", "5. एक जीवा का लंब समद्विभाजक हमेशा किससे होकर गुजरता है:"),
    "5. The ratio of the areas of two similar pentagons is 25:81. What is the ratio of their corresponding sides?":
        ("5. 两个相似五边形的面积比为 25:81。它们对应边的比是多少？", "5. La raz\u00f3n de las \u00e1reas de dos pent\u00e1gonos similares es 25:81. \u00bfCu\u00e1l es la raz\u00f3n de sus lados correspondientes?", "5. दो समरूप पंचभुजों के क्षेत्रफलों का अनुपात 25:81 है। उनकी संगत भुजाओं का अनुपात क्या है?"),
    "5. To find the area of a composite figure, you should:":
        ("5. 要求组合图形的面积，你应该：", "5. Para encontrar el \u00e1rea de una figura compuesta, debes:", "5. एक संयुक्त आकृति का क्षेत्रफल ज्ञात करने के लिए, आपको:"),
    "5. To simulate flipping a fair coin, which random number assignment would be appropriate?":
        ("5. 模拟抛掷公平硬币时，哪种随机数分配是合适的？", "5. Para simular el lanzamiento de una moneda justa, \u00bfqu\u00e9 asignaci\u00f3n de n\u00fameros aleatorios ser\u00eda apropiada?", "5. एक निष्पक्ष सिक्का उछालने का अनुकरण करने के लिए, कौन सा यादृच्छिक संख्या कार्यभार उपयुक्त होगा?"),
    "5. Two chords intersect inside a circle: AE = 3, EB = 8, CE = 4. What is ED?":
        ("5. 两条弦在圆内相交：AE = 3, EB = 8, CE = 4。ED 是多少？", "5. Dos cuerdas se cruzan dentro de un c\u00edrculo: AE = 3, EB = 8, CE = 4. \u00bfCu\u00e1l es ED?", "5. दो जीवाएँ एक वृत्त के अंदर प्रतिच्छेद करती हैं: AE = 3, EB = 8, CE = 4। ED क्या है?"),
    "5. Two figures are similar if and only if they are related by a __________.":
        ("5. 两个图形相似当且仅当它们通过一个__________相关联。", "5. Dos figuras son similares si y solo si est\u00e1n relacionadas por una __________.", "5. दो आकृतियाँ समरूप होती हैं यदि और केवल यदि वे एक __________ से संबंधित हों।"),
    "5. Two tangents from an external point intercept arcs of 250\u00b0 and 110\u00b0. What is the angle between the tangents?":
        ("5. 从外部点引出的两条切线截的弧分别为 250\u00b0 和 110\u00b0。切线之间的角是多少？", "5. Dos tangentes desde un punto externo interceptan arcos de 250\u00b0 y 110\u00b0. \u00bfCu\u00e1l es el \u00e1ngulo entre las tangentes?", "5. एक बाह्य बिंदु से दो स्पर्शरेखाएँ 250\u00b0 और 110\u00b0 के चाप काटती हैं। स्पर्शरेखाओं के बीच का कोण क्या है?"),
    "5. What does Cavalieri's Principle state?":
        ("5. 卡瓦列里原理是什么？", "5. \u00bfQu\u00e9 establece el Principio de Cavalieri?", "5. कैवलिएरी का सिद्धांत क्या कहता है?"),
    "5. What is a geodesic on a sphere?":
        ("5. 球面上的测地线是什么？", "5. \u00bfQu\u00e9 es una geod\u00e9sica en una esfera?", "5. गोले पर जियोडेसिक क्या है?"),
    "5. What is the area of a semicircle with diameter 12?":
        ("5. 直径为 12 的半圆面积是多少？", "5. \u00bfCu\u00e1l es el \u00e1rea de un semic\u00edrculo con di\u00e1metro 12?", "5. 12 व्यास वाले अर्धवृत्त का क्षेत्रफल क्या है?"),
    "5. What is the coordinate rule for reflecting a point over the y-axis?":
        ("5. 关于 y 轴反射一个点的坐标规则是什么？", "5. \u00bfCu\u00e1l es la regla de coordenadas para reflejar un punto sobre el eje y?", "5. y-अक्ष पर एक बिंदु को परावर्तित करने का निर्देशांक नियम क्या है?"),
    "5. What is the result of composing two isometries?":
        ("5. 两个等距变换的组合结果是什么？", "5. \u00bfCu\u00e1l es el resultado de componer dos isometr\u00edas?", "5. दो समदूरियों के संयोजन का परिणाम क्या है?"),
    "5. What is the volume of a hemisphere with radius r?":
        ("5. 半径为 r 的半球体积是多少？", "5. \u00bfCu\u00e1l es el volumen de un hemisferio con radio r?", "5. त्रिज्या r वाले अर्धगोले का आयतन क्या है?"),
    "5. When composing two translations \u27e82, 5\u27e9 and \u27e8\u22121, 3\u27e9, what is the resulting translation vector?":
        ("5. 组合两个平移 \u27e82, 5\u27e9 和 \u27e8\u22121, 3\u27e9 时，结果平移向量是什么？", "5. Al componer dos traslaciones \u27e82, 5\u27e9 y \u27e8\u22121, 3\u27e9, \u00bfcu\u00e1l es el vector de traslaci\u00f3n resultante?", "5. दो स्थानांतरणों \u27e82, 5\u27e9 और \u27e8\u22121, 3\u27e9 को संयोजित करते समय, परिणामी स्थानांतरण सदिश क्या है?"),
    "5. When does order matter in counting?":
        ("5. 在计数中，什么时候顺序重要？", "5. \u00bfCu\u00e1ndo importa el orden al contar?", "5. गिनती में क्रम कब मायने रखता है?"),
    "5. When you unroll the lateral surface of a cylinder, what shape do you get?":
        ("5. 展开圆柱的侧面，你得到什么形状？", "5. Cuando desenrollas la superficie lateral de un cilindro, \u00bfqu\u00e9 forma obtienes?", "5. जब आप बेलन की पार्श्व सतह खोलते हैं, तो आपको कौन सी आकृति मिलती है?"),
    "5. Which equation represents a circle with center (\u22121, 4) and radius 3?":
        ("5. 哪个方程表示以 (\u22121, 4) 为圆心、半径为 3 的圆？", "5. \u00bfQu\u00e9 ecuaci\u00f3n representa un c\u00edrculo con centro (\u22121, 4) y radio 3?", "5. कौन सा समीकरण केंद्र (\u22121, 4) और त्रिज्या 3 वाले वृत्त को दर्शाता है?"),
    "5. Which method uses trapezoids instead of rectangles for a more accurate area approximation?":
        ("5. 哪种方法使用梯形而非矩形来更准确地近似面积？", "5. \u00bfQu\u00e9 m\u00e9todo usa trapecios en lugar de rect\u00e1ngulos para una aproximaci\u00f3n de \u00e1rea m\u00e1s precisa?", "5. कौन सी विधि अधिक सटीक क्षेत्रफल सन्निकटन के लिए आयतों के बजाय समलंबों का उपयोग करती है?"),
    "5. Which of the following is NOT a common application of Monte Carlo methods?":
        ("5. 以下哪项不是蒙特卡洛方法的常见应用？", "5. \u00bfCu\u00e1l de las siguientes NO es una aplicaci\u00f3n com\u00fan de los m\u00e9todos Monte Carlo?", "5. निम्नलिखित में से कौन मोंटे कार्लो विधियों का सामान्य अनुप्रयोग नहीं है?"),
    "5. Which of the following is NOT a possible cross section of a cube?":
        ("5. 以下哪项不是立方体的可能截面？", "5. \u00bfCu\u00e1l de las siguientes NO es una posible secci\u00f3n transversal de un cubo?", "5. निम्नलिखित में से कौन एक घन का संभावित अनुप्रस्थ काट नहीं है?"),
    "5. Which property do both rhombi and kites share?":
        ("5. 菱形和筝形共有哪个性质？", "5. \u00bfQu\u00e9 propiedad comparten tanto los rombos como las cometas?", "5. समचतुर्भुज और पतंग दोनों में कौन सा गुण समान है?"),
    "6. A bounding rectangle has area 200 cm\u00b2. In a Monte Carlo simulation, 1500 out of 5000 random points land inside an irregular shape. What is the estimated area of the shape?":
        ("6. 一个边界矩形的面积为 200 cm\u00b2。在蒙特卡洛模拟中，5000 个随机点中有 1500 个落入不规则形状内。该形状的估计面积是多少？", "6. Un rect\u00e1ngulo delimitador tiene un \u00e1rea de 200 cm\u00b2. En una simulaci\u00f3n Monte Carlo, 1500 de 5000 puntos aleatorios caen dentro de una forma irregular. \u00bfCu\u00e1l es el \u00e1rea estimada de la forma?", "6. एक परिबद्ध आयत का क्षेत्रफल 200 cm\u00b2 है। मोंटे कार्लो अनुकरण में, 5000 यादृच्छिक बिंदुओं में से 1500 अनियमित आकार के अंदर गिरते हैं। आकार का अनुमानित क्षेत्रफल क्या है?"),
    "6. A composition of transformations means:":
        ("6. 变换的组合意味着：", "6. Una composici\u00f3n de transformaciones significa:", "6. रूपांतरणों का संयोजन का अर्थ है:"),
    "6. A counterexample to 'all rectangles are squares' is:":
        ("6.\u201c所有矩形都是正方形\u201d的反例是：", "6. Un contraejemplo de 'todos los rect\u00e1ngulos son cuadrados' es:", "6. 'सभी आयत वर्ग हैं' का प्रतिउदाहरण है:"),
    "6. A cylinder has a radius of 3 cm and a height of 7 cm. What is its volume? (Use \u03c0 \u2248 3.14)":
        ("6. 一个圆柱的半径为 3 厘米，高为 7 厘米。它的体积是多少？（取 \u03c0 \u2248 3.14）", "6. Un cilindro tiene un radio de 3 cm y una altura de 7 cm. \u00bfCu\u00e1l es su volumen? (Usa \u03c0 \u2248 3.14)", "6. एक बेलन की त्रिज्या 3 सेमी और ऊँचाई 7 सेमी है। इसका आयतन क्या है? (\u03c0 \u2248 3.14 लें)"),
    "6. A regular octagon has rotational symmetry of order 8. What is its angle of rotational symmetry?":
        ("6. 正八边形具有 8 阶旋转对称性。它的旋转对称角是多少？", "6. Un oct\u00e1gono regular tiene simetr\u00eda rotacional de orden 8. \u00bfCu\u00e1l es su \u00e1ngulo de simetr\u00eda rotacional?", "6. एक नियमित अष्टभुज में 8 क्रम की घूर्णन समरूपता है। इसका घूर्णन समरूपता कोण क्या है?"),
    "6. A secant and a tangent drawn from the same external point form an angle. This angle equals:":
        ("6. 从同一外部点引出的割线和切线形成一个角。这个角等于：", "6. Una secante y una tangente trazadas desde el mismo punto externo forman un \u00e1ngulo. Este \u00e1ngulo es igual a:", "6. एक ही बाह्य बिंदु से खींची गई छेदक और स्पर्शरेखा एक कोण बनाती हैं। यह कोण बराबर होता है:"),
    "6. A trapezoid has a median of 10 cm and a height of 8 cm. What is its area?":
        ("6. 一个梯形的中位线为 10 厘米，高为 8 厘米。它的面积是多少？", "6. Un trapecio tiene una mediana de 10 cm y una altura de 8 cm. \u00bfCu\u00e1l es su \u00e1rea?", "6. एक समलंब की माध्यिका 10 सेमी और ऊँचाई 8 सेमी है। इसका क्षेत्रफल क्या है?"),
    "6. A triangular prism has a base with sides 3, 4, and 5 cm, and a height of 12 cm. What is its lateral area?":
        ("6. 一个三棱柱的底面边长分别为 3、4 和 5 厘米，高为 12 厘米。它的侧面积是多少？", "6. Un prisma triangular tiene una base con lados de 3, 4 y 5 cm, y una altura de 12 cm. \u00bfCu\u00e1l es su \u00e1rea lateral?", "6. एक त्रिभुजाकार प्रिज्म के आधार की भुजाएँ 3, 4, और 5 सेमी हैं, और ऊँचाई 12 सेमी है। इसका पार्श्व क्षेत्रफल क्या है?"),
    "6. Can Cavalieri's Principle be applied in 2D?":
        ("6. 卡瓦列里原理可以应用于二维吗？", "6. \u00bfSe puede aplicar el Principio de Cavalieri en 2D?", "6. क्या कैवलिएरी का सिद्धांत 2D में लागू किया जा सकता है?"),
    "6. Cavalieri's Principle states that two figures have the same area if:":
        ("6. 卡瓦列里原理指出两个图形面积相同，如果：", "6. El Principio de Cavalieri establece que dos figuras tienen la misma \u00e1rea si:", "6. कैवलिएरी का सिद्धांत कहता है कि दो आकृतियों का क्षेत्रफल समान होता है यदि:"),
    "6. Circles that share the same center but have different radii are called:":
        ("6. 具有相同圆心但不同半径的圆称为：", "6. Los c\u00edrculos que comparten el mismo centro pero tienen diferentes radios se llaman:", "6. समान केंद्र लेकिन भिन्न त्रिज्या वाले वृत्त कहलाते हैं:"),
    "6. Does the area ratio rule for similar figures apply only to triangles?":
        ("6. 相似图形的面积比规则只适用于三角形吗？", "6. \u00bfLa regla de raz\u00f3n de \u00e1reas para figuras similares se aplica solo a tri\u00e1ngulos?", "6. क्या समरूप आकृतियों के लिए क्षेत्रफल अनुपात नियम केवल त्रिभुजों पर लागू होता है?"),
    "6. How can you test whether events A and B are independent?":
        ("6. 你如何检验事件 A 和 B 是否独立？", "6. \u00bfC\u00f3mo puedes verificar si los eventos A y B son independientes?", "6. आप कैसे जाँच सकते हैं कि घटनाएँ A और B स्वतंत्र हैं?"),
    "6. How many letters are used to name a major arc?":
        ("6. 命名优弧需要使用多少个字母？", "6. \u00bfCu\u00e1ntas letras se usan para nombrar un arco mayor?", "6. एक दीर्घ चाप का नाम रखने के लिए कितने अक्षरों का उपयोग किया जाता है?"),
    "6. If an intercepted arc measures 120\u00b0, what is the measure of the inscribed angle?":
        ("6. 如果截得的弧为 120\u00b0，圆内接角的度数是多少？", "6. Si un arco interceptado mide 120\u00b0, \u00bfcu\u00e1l es la medida del \u00e1ngulo inscrito?", "6. यदि कटा हुआ चाप 120\u00b0 मापता है, तो अंतर्लिखित कोण का माप क्या है?"),
    "6. If a\u00b2 + b\u00b2 < c\u00b2, the triangle is:":
        ("6. 如果 a\u00b2 + b\u00b2 < c\u00b2，则三角形是：", "6. Si a\u00b2 + b\u00b2 < c\u00b2, el tri\u00e1ngulo es:", "6. यदि a\u00b2 + b\u00b2 < c\u00b2, तो त्रिभुज है:"),
    "6. If the radius of a sphere is tripled, the volume is multiplied by:":
        ("6. 如果球体的半径增加到三倍，体积乘以：", "6. Si el radio de una esfera se triplica, el volumen se multiplica por:", "6. यदि गोले की त्रिज्या तीन गुनी कर दी जाए, तो आयतन किससे गुणा होता है:"),
    "6. If you double both the radius and the height of a cone, the volume is multiplied by:":
        ("6. 如果圆锥的半径和高度都加倍，体积乘以：", "6. Si duplicas tanto el radio como la altura de un cono, el volumen se multiplica por:", "6. यदि शंकु की त्रिज्या और ऊँचाई दोनों दोगुनी कर दें, तो आयतन किससे गुणा होता है:"),
    "6. In how many ways can 5 books be arranged on a shelf?":
        ("6. 5 本书在书架上有多少种排列方式？", "6. \u00bfDe cu\u00e1ntas formas se pueden organizar 5 libros en un estante?", "6. 5 किताबों को एक अलमारी पर कितने तरीकों से व्यवस्थित किया जा सकता है?"),
    "6. In the equation Ax\u00b2 + Cy\u00b2 + Dx + Ey + F = 0, if A and C have opposite signs, the conic is a:":
        ("6. 在方程 Ax\u00b2 + Cy\u00b2 + Dx + Ey + F = 0 中，如果 A 和 C 符号相反，则圆锥曲线是：", "6. En la ecuaci\u00f3n Ax\u00b2 + Cy\u00b2 + Dx + Ey + F = 0, si A y C tienen signos opuestos, la c\u00f3nica es una:", "6. समीकरण Ax\u00b2 + Cy\u00b2 + Dx + Ey + F = 0 में, यदि A और C के विपरीत चिह्न हैं, तो शंकु वक्र है:"),
    "6. Point A(2, 5) is reflected over the x-axis and then translated by \u27e83, \u22121\u27e9. What are the final coordinates?":
        ("6. 点 A(2, 5) 关于 x 轴反射，然后平移 \u27e83, \u22121\u27e9。最终坐标是什么？", "6. El punto A(2, 5) se refleja sobre el eje x y luego se traslada por \u27e83, \u22121\u27e9. \u00bfCu\u00e1les son las coordenadas finales?", "6. बिंदु A(2, 5) को x-अक्ष पर परावर्तित किया जाता है और फिर \u27e83, \u22121\u27e9 द्वारा स्थानांतरित किया जाता है। अंतिम निर्देशांक क्या हैं?"),
    "6. The Power of a Point theorem applies to which of the following configurations?":
        ("6. 幂点定理适用于以下哪种配置？", "6. \u00bfA cu\u00e1l de las siguientes configuraciones se aplica el teorema de la Potencia de un Punto?", "6. एक बिंदु की शक्ति प्रमेय निम्नलिखित में से किस विन्यास पर लागू होता है?"),
    "6. The general form of a circle equation is:":
        ("6. 圆方程的一般形式为：", "6. La forma general de la ecuaci\u00f3n de un c\u00edrculo es:", "6. वृत्त समीकरण का सामान्य रूप है:"),
    "6. Two chords in the same circle are congruent. What can you conclude about their distances from the center?":
        ("6. 同一个圆中两条弦全等。关于它们到圆心的距离你能得出什么结论？", "6. Dos cuerdas en el mismo c\u00edrculo son congruentes. \u00bfQu\u00e9 puedes concluir sobre sus distancias al centro?", "6. एक ही वृत्त में दो जीवाएँ सर्वांगसम हैं। उनकी केंद्र से दूरियों के बारे में आप क्या निष्कर्ष निकाल सकते हैं?"),
    "6. Two similar prisms have volumes of 64 cm\u00b3 and 512 cm\u00b3. What is the scale factor?":
        ("6. 两个相似棱柱的体积分别为 64 cm\u00b3 和 512 cm\u00b3。比例因子是多少？", "6. Dos prismas similares tienen vol\u00famenes de 64 cm\u00b3 y 512 cm\u00b3. \u00bfCu\u00e1l es el factor de escala?", "6. दो समरूप प्रिज्मों के आयतन 64 cm\u00b3 और 512 cm\u00b3 हैं। स्केल गुणक क्या है?"),
    "6. What distinguishes a prism from a pyramid?":
        ("6. 棱柱和棱锥有什么区别？", "6. \u00bfQu\u00e9 distingue a un prisma de una pir\u00e1mide?", "6. प्रिज्म को पिरामिड से क्या अलग करता है?"),
    "6. What happens to the orientation of a figure after a reflection?":
        ("6. 反射后图形的方向会怎样？", "6. \u00bfQu\u00e9 le pasa a la orientaci\u00f3n de una figura despu\u00e9s de una reflexi\u00f3n?", "6. परावर्तन के बाद आकृति के अभिविन्यास पर क्या प्रभाव पड़ता है?"),
    "6. What happens when the scale factor k is negative?":
        ("6. 当比例因子 k 为负时会发生什么？", "6. \u00bfQu\u00e9 sucede cuando el factor de escala k es negativo?", "6. जब स्केल गुणक k ऋणात्मक हो तो क्या होता है?"),
    "6. What is a lune in spherical geometry?":
        ("6. 球面几何中的月牙形是什么？", "6. \u00bfQu\u00e9 es una l\u00fanula en geometr\u00eda esf\u00e9rica?", "6. गोलीय ज्यामिति में ल्यून क्या है?"),
    "6. What is the central angle of a regular pentagon?":
        ("6. 正五边形的中心角是多少？", "6. \u00bfCu\u00e1l es el \u00e1ngulo central de un pent\u00e1gono regular?", "6. एक नियमित पंचभुज का केंद्रीय कोण क्या है?"),
    "6. What is the image of (\u22121, 6) after a 270\u00b0 counterclockwise rotation about the origin?":
        ("6. (\u22121, 6) 绕原点逆时针旋转 270\u00b0 后的像是什么？", "6. \u00bfCu\u00e1l es la imagen de (\u22121, 6) despu\u00e9s de una rotaci\u00f3n de 270\u00b0 en sentido antihorario alrededor del origen?", "6. मूल बिंदु के चारों ओर 270\u00b0 वामावर्त घूर्णन के बाद (\u22121, 6) का प्रतिबिंब क्या है?"),
    "6. When you unroll the lateral surface of a cone, what shape do you get?":
        ("6. 展开圆锥的侧面，你得到什么形状？", "6. Cuando desenrollas la superficie lateral de un cono, \u00bfqu\u00e9 forma obtienes?", "6. जब आप शंकु की पार्श्व सतह खोलते हैं, तो आपको कौन सी आकृति मिलती है?"),
    "6. Which formula correctly gives the area of a triangle using two sides and the included angle?":
        ("6. 哪个公式正确地给出了使用两边和夹角求三角形面积的公式？", "6. \u00bfQu\u00e9 f\u00f3rmula da correctamente el \u00e1rea de un tri\u00e1ngulo usando dos lados y el \u00e1ngulo incluido?", "6. कौन सा सूत्र दो भुजाओं और अंतर्विष्ट कोण का उपयोग करके त्रिभुज का क्षेत्रफल सही ढंग से देता है?"),
    "6. Which formula gives the area of a sector with central angle \u03b8 and radius r?":
        ("6. 哪个公式给出了圆心角 \u03b8、半径 r 的扇形面积？", "6. \u00bfQu\u00e9 f\u00f3rmula da el \u00e1rea de un sector con \u00e1ngulo central \u03b8 y radio r?", "6. कौन सा सूत्र केंद्रीय कोण \u03b8 और त्रिज्या r वाले त्रिज्यखंड का क्षेत्रफल देता है?"),
    "6. Which geometric measure is used in the length model of geometric probability?":
        ("6. 几何概率的长度模型中使用哪种几何度量？", "6. \u00bfQu\u00e9 medida geom\u00e9trica se usa en el modelo de longitud de probabilidad geom\u00e9trica?", "6. ज्यामितीय प्रायिकता के लंबाई मॉडल में कौन सा ज्यामितीय माप उपयोग किया जाता है?"),
    "6. Which of the following best describes a translation?":
        ("6. 以下哪项最好地描述了平移？", "6. \u00bfCu\u00e1l de las siguientes describe mejor una traslaci\u00f3n?", "6. निम्नलिखित में से कौन सा स्थानांतरण का सबसे अच्छा वर्णन करता है?"),
    "6. Which of the following is true about a common external tangent?":
        ("6. 关于公外切线，以下哪项是正确的？", "6. \u00bfCu\u00e1l de las siguientes es verdad sobre una tangente externa com\u00fan?", "6. उभयनिष्ठ बाह्य स्पर्शरेखा के बारे में निम्नलिखित में से कौन सत्य है?"),
    "6. Which pair of events is mutually exclusive?":
        ("6. 哪对事件是互斥的？", "6. \u00bfQu\u00e9 par de eventos es mutuamente excluyente?", "6. घटनाओं का कौन सा जोड़ा परस्पर अपवर्जी है?"),
    "6. Which tool is best for displaying the sample space of a two-stage experiment with different options at each stage?":
        ("6. 哪种工具最适合展示每个阶段有不同选项的两阶段实验的样本空间？", "6. \u00bfQu\u00e9 herramienta es mejor para mostrar el espacio muestral de un experimento de dos etapas con diferentes opciones en cada etapa?", "6. प्रत्येक चरण में भिन्न विकल्पों वाले दो-चरणीय प्रयोग के प्रतिदर्श समष्टि को प्रदर्शित करने के लिए कौन सा उपकरण सबसे अच्छा है?"),
    "6. Why are more trials better in a simulation?":
        ("6. 为什么在模拟中更多的试验更好？", "6. \u00bfPor qu\u00e9 m\u00e1s ensayos son mejores en una simulaci\u00f3n?", "6. अनुकरण में अधिक प्रयोग बेहतर क्यों हैं?"),
    "7. A central angle and an inscribed angle intercept the same arc. The central angle is:":
        ("7. 圆心角和圆内接角截同一段弧。圆心角是：", "7. Un \u00e1ngulo central y un \u00e1ngulo inscrito interceptan el mismo arco. El \u00e1ngulo central es:", "7. एक केंद्रीय कोण और एक अंतर्लिखित कोण एक ही चाप को काटते हैं। केंद्रीय कोण है:"),
    "7. A circle has an area of 64\u03c0 cm\u00b2. What is its radius?":
        ("7. 一个圆的面积为 64\u03c0 cm\u00b2。它的半径是多少？", "7. Un c\u00edrculo tiene un \u00e1rea de 64\u03c0 cm\u00b2. \u00bfCu\u00e1l es su radio?", "7. एक वृत्त का क्षेत्रफल 64\u03c0 cm\u00b2 है। इसकी त्रिज्या क्या है?"),
    "7. A circular dartboard has radius 10 in. A bullseye circle at the center has radius 2 in. What is the probability of hitting the bullseye?":
        ("7. 一个圆形靶的半径为 10 英寸。中心的靶心圆半径为 2 英寸。击中靶心的概率是多少？", "7. Un tablero de dardos circular tiene radio de 10 pulgadas. Un c\u00edrculo de diana en el centro tiene radio de 2 pulgadas. \u00bfCu\u00e1l es la probabilidad de dar en la diana?", "7. एक गोलाकार डार्टबोर्ड की त्रिज्या 10 इंच है। केंद्र पर बुल्सआई वृत्त की त्रिज्या 2 इंच है। बुल्सआई मारने की प्रायिकता क्या है?"),
    "7. A hyperbola is defined by the property that the __________ of distances from any point to the two foci is constant.":
        ("7. 双曲线由以下性质定义：任意一点到两个焦点的距离的__________是常数。", "7. Una hip\u00e9rbola se define por la propiedad de que __________ de las distancias desde cualquier punto a los dos focos es constante.", "7. अतिपरवलय इस गुण द्वारा परिभाषित होता है कि किसी भी बिंदु से दो नाभियों तक की दूरियों का __________ नियत होता है।"),
    "7. A parallelogram has a base of 15 m and an area of 120 m\u00b2. What is its height?":
        ("7. 一个平行四边形的底为 15 米，面积为 120 m\u00b2。它的高是多少？", "7. Un paralelogramo tiene una base de 15 m y un \u00e1rea de 120 m\u00b2. \u00bfCu\u00e1l es su altura?", "7. एक समांतर चतुर्भुज का आधार 15 मी और क्षेत्रफल 120 m\u00b2 है। इसकी ऊँचाई क्या है?"),
    "7. A regular polygon has an apothem of 5\u221a3 cm and a perimeter of 60 cm. What is its area?":
        ("7. 一个正多边形的边心距为 5\u221a3 厘米，周长为 60 厘米。它的面积是多少？", "7. Un pol\u00edgono regular tiene una apotema de 5\u221a3 cm y un per\u00edmetro de 60 cm. \u00bfCu\u00e1l es su \u00e1rea?", "7. एक नियमित बहुभुज का अपोथेम 5\u221a3 सेमी और परिमाप 60 सेमी है। इसका क्षेत्रफल क्या है?"),
    "7. A sample space is called uniform when:":
        ("7. 当以下情况时，样本空间被称为均匀的：", "7. Un espacio muestral se llama uniforme cuando:", "7. प्रतिदर्श समष्टि को समान कब कहा जाता है:"),
    "7. A triangle is translated by \u27e84, \u22127\u27e9. What is true about the image triangle?":
        ("7. 一个三角形经平移 \u27e84, \u22127\u27e9。关于像三角形的正确说法是什么？", "7. Un tri\u00e1ngulo se traslada por \u27e84, \u22127\u27e9. \u00bfQu\u00e9 es verdad sobre el tri\u00e1ngulo imagen?", "7. एक त्रिभुज को \u27e84, \u22127\u27e9 द्वारा स्थानांतरित किया जाता है। प्रतिबिंब त्रिभुज के बारे में क्या सत्य है?"),
    "7. A triangular pyramid has a base area of 24 cm\u00b2 and a height of 10 cm. What is its volume?":
        ("7. 一个三棱锥的底面积为 24 cm\u00b2，高为 10 厘米。它的体积是多少？", "7. Una pir\u00e1mide triangular tiene un \u00e1rea de base de 24 cm\u00b2 y una altura de 10 cm. \u00bfCu\u00e1l es su volumen?", "7. एक त्रिभुजाकार पिरामिड का आधार क्षेत्रफल 24 cm\u00b2 और ऊँचाई 10 सेमी है। इसका आयतन क्या है?"),
    "7. An isometric drawing shows how many faces of a 3D object in a single view?":
        ("7. 轴测图在单一视图中显示 3D 物体的多少个面？", "7. \u00bfCu\u00e1ntas caras de un objeto 3D muestra un dibujo isom\u00e9trico en una sola vista?", "7. एक समदूरी चित्र एक ही दृश्य में 3D वस्तु के कितने फलक दिखाता है?"),
    "7. Convert x\u00b2 + y\u00b2 \u2212 6x + 4y \u2212 12 = 0 to standard form. What is the radius?":
        ("7. 将 x\u00b2 + y\u00b2 \u2212 6x + 4y \u2212 12 = 0 转化为标准形式。半径是多少？", "7. Convierte x\u00b2 + y\u00b2 \u2212 6x + 4y \u2212 12 = 0 a forma est\u00e1ndar. \u00bfCu\u00e1l es el radio?", "7. x\u00b2 + y\u00b2 \u2212 6x + 4y \u2212 12 = 0 को मानक रूप में बदलें। त्रिज्या क्या है?"),
    "7. For mutually exclusive events A and B, what is P(A and B)?":
        ("7. 对于互斥事件 A 和 B，P(A 且 B) 是多少？", "7. Para eventos mutuamente excluyentes A y B, \u00bfcu\u00e1l es P(A y B)?", "7. परस्पर अपवर्जी घटनाओं A और B के लिए, P(A और B) क्या है?"),
    "7. From an external point, a tangent has length 8 and a secant has an external segment of 4. What is the whole secant length?":
        ("7. 从一个外部点，切线长为 8，割线的外部线段为 4。整条割线长是多少？", "7. Desde un punto externo, una tangente tiene longitud 8 y una secante tiene un segmento externo de 4. \u00bfCu\u00e1l es la longitud total de la secante?", "7. एक बाह्य बिंदु से, स्पर्शरेखा की लंबाई 8 और छेदक का बाह्य खंड 4 है। पूरी छेदक की लंबाई क्या है?"),
    "7. How do you find the scale factor from the ratio of surface areas of two similar solids?":
        ("7. 如何从两个相似立体的表面积比求比例因子？", "7. \u00bfC\u00f3mo se encuentra el factor de escala a partir de la raz\u00f3n de las \u00e1reas de superficie de dos s\u00f3lidos similares?", "7. दो समरूप ठोसों के पृष्ठीय क्षेत्रफलों के अनुपात से स्केल गुणक कैसे ज्ञात करते हैं?"),
    "7. How is the slant height \u2113 of a cone related to its height h and radius r?":
        ("7. 圆锥的斜高 \u2113 与其高 h 和半径 r 有什么关系？", "7. \u00bfC\u00f3mo se relaciona la altura inclinada \u2113 de un cono con su altura h y radio r?", "7. शंकु की तिरछी ऊँचाई \u2113 इसकी ऊँचाई h और त्रिज्या r से कैसे संबंधित है?"),
    "7. If p is 'It is raining' and p is true, what is ~p?":
        ("7. 如果 p 是\u201c正在下雨\u201d且 p 为真，那么 ~p 是什么？", "7. Si p es 'Est\u00e1 lloviendo' y p es verdadero, \u00bfqu\u00e9 es ~p?", "7. यदि p 'बारिश हो रही है' है और p सत्य है, तो ~p क्या है?"),
    "7. If the height of a prism is doubled while the base stays the same, the volume:":
        ("7. 如果棱柱的高度加倍而底面不变，体积：", "7. Si la altura de un prisma se duplica mientras la base permanece igual, el volumen:", "7. यदि प्रिज्म की ऊँचाई दोगुनी कर दी जाए जबकि आधार समान रहे, तो आयतन:"),
    "7. If two tangent segments from external point P to a circle have lengths (3x + 2) and (5x \u2212 6), what is x?":
        ("7. 如果从外部点 P 到圆的两条切线段长分别为 (3x + 2) 和 (5x \u2212 6)，x 是多少？", "7. Si dos segmentos tangentes desde el punto externo P a un c\u00edrculo tienen longitudes (3x + 2) y (5x \u2212 6), \u00bfcu\u00e1l es x?", "7. यदि बाह्य बिंदु P से वृत्त तक दो स्पर्शरेखा खंडों की लंबाई (3x + 2) और (5x \u2212 6) है, तो x क्या है?"),
    "7. In the surface area formula S = Ph + 2B for a prism, what does B represent?":
        ("7. 在棱柱的表面积公式 S = Ph + 2B 中，B 代表什么？", "7. En la f\u00f3rmula de \u00e1rea de superficie S = Ph + 2B para un prisma, \u00bfqu\u00e9 representa B?", "7. प्रिज्म के पृष्ठीय क्षेत्रफल सूत्र S = Ph + 2B में, B क्या दर्शाता है?"),
    "7. P(B|A) represents:":
        ("7. P(B|A) 表示：", "7. P(B|A) representa:", "7. P(B|A) दर्शाता है:"),
    "7. The 'ambiguous case' of the Law of Sines occurs with:":
        ("7. 正弦定理的\u201c模糊情形\u201d发生在：", "7. El 'caso ambiguo' de la Ley de Senos ocurre con:", "7. ज्या नियम का 'अस्पष्ट मामला' किसके साथ होता है:"),
    "7. The image and pre-image of a dilation are always __________.":
        ("7. 缩放的像和原像总是__________。", "7. La imagen y pre-imagen de una dilataci\u00f3n siempre son __________.", "7. विस्तारण का प्रतिबिंब और पूर्व-प्रतिबिंब हमेशा __________ होते हैं।"),
    "7. The measure of a central angle is equal to:":
        ("7. 圆心角的度数等于：", "7. La medida de un \u00e1ngulo central es igual a:", "7. केंद्रीय कोण का माप बराबर होता है:"),
    "7. The surface area of a sphere is equal to how many times the area of its great circle?":
        ("7. 球体的表面积等于其大圆面积的多少倍？", "7. \u00bfEl \u00e1rea de superficie de una esfera es igual a cu\u00e1ntas veces el \u00e1rea de su gran c\u00edrculo?", "7. गोले का पृष्ठीय क्षेत्रफल उसके महान वृत्त के क्षेत्रफल का कितना गुना होता है?"),
    "7. The value of \u03c0 can be derived geometrically by integrating:":
        ("7. \u03c0 的值可以通过积分几何方法导出：", "7. El valor de \u03c0 puede derivarse geom\u00e9tricamente integrando:", "7. \u03c0 का मान ज्यामितीय रूप से समाकलन करके प्राप्त किया जा सकता है:"),
    "7. Two chords intersect inside a circle. Which relationship is always true?":
        ("7. 两条弦在圆内相交。哪个关系始终成立？", "7. Dos cuerdas se cruzan dentro de un c\u00edrculo. \u00bfQu\u00e9 relaci\u00f3n es siempre verdadera?", "7. दो जीवाएँ एक वृत्त के अंदर प्रतिच्छेद करती हैं। कौन सा संबंध हमेशा सत्य है?"),
    "7. Two reflections over parallel lines always produce a __________.":
        ("7. 两条平行线上的两次反射总是产生一个__________。", "7. Dos reflexiones sobre l\u00edneas paralelas siempre producen un __________.", "7. समांतर रेखाओं पर दो परावर्तन हमेशा एक __________ उत्पन्न करते हैं।"),
    "7. Two similar rectangles have perimeters of 20 cm and 30 cm. If the smaller has an area of 24 cm\u00b2, what is the area of the larger?":
        ("7. 两个相似矩形的周长分别为 20 厘米和 30 厘米。如果较小的面积为 24 cm\u00b2，较大的面积是多少？", "7. Dos rect\u00e1ngulos similares tienen per\u00edmetros de 20 cm y 30 cm. Si el menor tiene un \u00e1rea de 24 cm\u00b2, \u00bfcu\u00e1l es el \u00e1rea del mayor?", "7. दो समरूप आयतों का परिमाप 20 सेमी और 30 सेमी है। यदि छोटे का क्षेत्रफल 24 cm\u00b2 है, तो बड़े का क्षेत्रफल क्या है?"),
    "7. Two solids both have a height of 10 cm. At every height, both have a cross-sectional area of 15 cm\u00b2. What can you conclude?":
        ("7. 两个立体都有 10 厘米的高度。在每个高度处，两者的截面面积都是 15 cm\u00b2。你能得出什么结论？", "7. Dos s\u00f3lidos tienen una altura de 10 cm. A cada altura, ambos tienen un \u00e1rea de secci\u00f3n transversal de 15 cm\u00b2. \u00bfQu\u00e9 puedes concluir?", "7. दो ठोसों की ऊँचाई 10 सेमी है। प्रत्येक ऊँचाई पर, दोनों का अनुप्रस्थ काट क्षेत्रफल 15 cm\u00b2 है। आप क्या निष्कर्ष निकाल सकते हैं?"),
    "7. What is a random walk?":
        ("7. 什么是随机游走？", "7. \u00bfQu\u00e9 es una caminata aleatoria?", "7. यादृच्छिक भ्रमण क्या है?"),
    "7. What is the image of (4, \u22121) after a reflection over the line y = \u2212x?":
        ("7. (4, \u22121) 关于直线 y = \u2212x 反射后的像是什么？", "7. \u00bfCu\u00e1l es la imagen de (4, \u22121) despu\u00e9s de una reflexi\u00f3n sobre la l\u00ednea y = \u2212x?", "7. रेखा y = \u2212x पर परावर्तन के बाद (4, \u22121) का प्रतिबिंब क्या है?"),
    "7. What is the inverse of 'If p, then q'?":
        ("7.\u201c如果 p，则 q\u201d的否命题是什么？", "7. \u00bfCu\u00e1l es el inverso de 'Si p, entonces q'?", "7. 'यदि p, तो q' का प्रतिलोम क्या है?"),
    "7. What is the value of C(8, 0)?":
        ("7. C(8, 0) 的值是多少？", "7. \u00bfCu\u00e1l es el valor de C(8, 0)?", "7. C(8, 0) का मान क्या है?"),
    "7. Which formula is used to find the area of a trapezoid?":
        ("7. 哪个公式用于求梯形的面积？", "7. \u00bfQu\u00e9 f\u00f3rmula se usa para encontrar el \u00e1rea de un trapecio?", "7. समलंब का क्षेत्रफल ज्ञात करने के लिए कौन सा सूत्र उपयोग किया जाता है?"),
    "7. Which of the following figures has exactly 1 line of symmetry?":
        ("7. 以下哪个图形恰好有 1 条对称轴？", "7. \u00bfCu\u00e1l de las siguientes figuras tiene exactamente 1 eje de simetr\u00eda?", "7. निम्नलिखित में से किस आकृति में ठीक 1 समरूपता रेखा है?"),
    "7. Which of the following is a real-world application of spherical geometry?":
        ("7. 以下哪项是球面几何的现实世界应用？", "7. \u00bfCu\u00e1l de las siguientes es una aplicaci\u00f3n del mundo real de la geometr\u00eda esf\u00e9rica?", "7. निम्नलिखित में से कौन गोलीय ज्यामिति का वास्तविक दुनिया का अनुप्रयोग है?"),
    "7. Which of the following transformations is NOT a rigid motion?":
        ("7. 以下哪种变换不是刚体运动？", "7. \u00bfCu\u00e1l de las siguientes transformaciones NO es un movimiento r\u00edgido?", "7. निम्नलिखित में से कौन सा रूपांतरण दृढ़ गति नहीं है?"),
    "7. Which point does NOT move during a rotation?":
        ("7. 旋转过程中哪个点不移动？", "7. \u00bfQu\u00e9 punto NO se mueve durante una rotaci\u00f3n?", "7. घूर्णन के दौरान कौन सा बिंदु नहीं चलता?"),
    "7. Which scenario uses the formula: angle = \u00bd(sum of arcs)?":
        ("7. 哪种情况使用公式：角 = \u00bd(弧之和)？", "7. \u00bfQu\u00e9 escenario usa la f\u00f3rmula: \u00e1ngulo = \u00bd(suma de arcos)?", "7. कौन सी स्थिति सूत्र: कोण = \u00bd(चापों का योग) का उपयोग करती है?"),
    "7. Which statement about circles is always true?":
        ("7. 关于圆的哪个说法始终正确？", "7. \u00bfQu\u00e9 afirmaci\u00f3n sobre c\u00edrculos es siempre verdadera?", "7. वृत्तों के बारे में कौन सा कथन हमेशा सत्य है?"),
    "7. You simulate rolling a die 600 times. About how many times would you expect to roll a 4?":
        ("7. 你模拟掷骰子 600 次。你预计大约掷出多少次 4？", "7. Simulas lanzar un dado 600 veces. \u00bfAproximadamente cu\u00e1ntas veces esperar\u00edas sacar un 4?", "7. आप 600 बार पासा फेंकने का अनुकरण करते हैं। लगभग कितनी बार 4 आने की उम्मीद होगी?"),

    # ===================== QUIZ ANSWERS (16) =====================
    "'It is not raining' and it is false":
        ("'没有在下雨'且为假", "'No est\u00e1 lloviendo' y es falso", "'बारिश नहीं हो रही है' और यह असत्य है"),
    "'It is raining' and it is true":
        ("'正在下雨'且为真", "'Est\u00e1 lloviendo' y es verdadero", "'बारिश हो रही है' और यह सत्य है"),
    "'It is sunny' and it is true":
        ("'天晴'且为真", "'Hace sol' y es verdadero", "'धूप है' और यह सत्य है"),
    "'It might rain' and it is unknown":
        ("'可能下雨'且为未知", "'Podr\u00eda llover' y es desconocido", "'बारिश हो सकती है' और यह अज्ञात है"),
    "AC (because 80\u00b0 > 60\u00b0)":
        ("AC（因为 80\u00b0 > 60\u00b0）", "AC (porque 80\u00b0 > 60\u00b0)", "AC (क्योंकि 80\u00b0 > 60\u00b0)"),
    "DF (because 60\u00b0 < 80\u00b0)":
        ("DF（因为 60\u00b0 < 80\u00b0）", "DF (porque 60\u00b0 < 80\u00b0)", "DF (क्योंकि 60\u00b0 < 80\u00b0)"),
    "Euclid's First Postulate":
        ("欧几里得第一公设", "Primer Postulado de Euclides", "यूक्लिड का प्रथम अभिगृहीत"),
    "No, because 2 + 3 = 5 < 6":
        ("不是，因为 2 + 3 = 5 < 6", "No, porque 2 + 3 = 5 < 6", "नहीं, क्योंकि 2 + 3 = 5 < 6"),
    "Side AB > Side BC":
        ("边 AB > 边 BC", "Lado AB > Lado BC", "भुजा AB > भुजा BC"),
    "Side AC > Side BC":
        ("边 AC > 边 BC", "Lado AC > Lado BC", "भुजा AC > भुजा BC"),
    "Side BC > Side AC":
        ("边 BC > 边 AC", "Lado BC > Lado AC", "भुजा BC > भुजा AC"),
    "Yes, because 2 + 6 > 3":
        ("是，因为 2 + 6 > 3", "S\u00ed, porque 2 + 6 > 3", "हाँ, क्योंकि 2 + 6 > 3"),
    "Yes, because 3 + 6 > 2":
        ("是，因为 3 + 6 > 2", "S\u00ed, porque 3 + 6 > 2", "हाँ, क्योंकि 3 + 6 > 2"),
    "Yes, because 7 + 10 = 17 > 12":
        ("是，因为 7 + 10 = 17 > 12", "S\u00ed, porque 7 + 10 = 17 > 12", "हाँ, क्योंकि 7 + 10 = 17 > 12"),
    "Yes, because a + a > a for any positive a":
        ("是，因为对于任何正数 a，a + a > a", "S\u00ed, porque a + a > a para cualquier a positivo", "हाँ, क्योंकि किसी भी धनात्मक a के लिए a + a > a"),
    "Yes, it is a degenerate triangle with area > 0":
        ("是，它是一个面积 > 0 的退化三角形", "S\u00ed, es un tri\u00e1ngulo degenerado con \u00e1rea > 0", "हाँ, यह क्षेत्रफल > 0 वाला एक अपभ्रष्ट त्रिभुज है"),
}

if __name__ == "__main__":
    print(f"Geometry batch: {len(translations)} translations")
    inject_all(translations)
