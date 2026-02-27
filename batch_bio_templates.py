#!/usr/bin/env python3
"""Biology translations - templated entries (59 topics x 8 templates = 472 entries)."""

# 59 topics: (english, chinese, spanish, hindi)
TOPICS = [
    ("aquatic ecosystems", "水生生态系统", "ecosistemas acuáticos", "जलीय पारिस्थितिक तंत्र"),
    ("astrobiology and the search for life beyond earth", "天体生物学与地球之外的生命探索", "astrobiología y la búsqueda de vida más allá de la tierra", "खगोल जीव विज्ञान और पृथ्वी से परे जीवन की खोज"),
    ("biochemistry in everyday life", "日常生活中的生物化学", "bioquímica en la vida cotidiana", "दैनिक जीवन में जैव रसायन"),
    ("biodiversity", "生物多样性", "biodiversidad", "जैव विविधता"),
    ("bioethics (cloning, stem cells, genetic privacy)", "生物伦理学（克隆、干细胞、基因隐私）", "bioética (clonación, células madre, privacidad genética)", "जैव नैतिकता (क्लोनिंग, स्टेम सेल, आनुवंशिक गोपनीयता)"),
    ("biotechnology (crispr, cloning, gmos)", "生物技术（CRISPR、克隆、转基因生物）", "biotecnología (crispr, clonación, OGM)", "जैव प्रौद्योगिकी (क्रिस्पर, क्लोनिंग, जीएमओ)"),
    ("biotechnology and genetic engineering", "生物技术与基因工程", "biotecnología e ingeniería genética", "जैव प्रौद्योगिकी और आनुवंशिक इंजीनियरिंग"),
    ("carrying capacity and limiting factors", "承载力与限制因素", "capacidad de carga y factores limitantes", "वहन क्षमता और सीमित कारक"),
    ("cell discovery and theory", "细胞发现与理论", "descubrimiento y teoría celular", "कोशिका खोज और सिद्धांत"),
    ("cell structure and function", "细胞结构与功能", "estructura y función celular", "कोशिका संरचना और कार्य"),
    ("cellular reproduction", "细胞繁殖", "reproducción celular", "कोशिकीय प्रजनन"),
    ("cellular respiration", "细胞呼吸", "respiración celular", "कोशिकीय श्वसन"),
    ("cellular transport", "细胞运输", "transporte celular", "कोशिकीय परिवहन"),
    ("chemical energy and atp", "化学能与ATP", "energía química y ATP", "रासायनिक ऊर्जा और एटीपी"),
    ("chemical reactions and enzymes", "化学反应与酶", "reacciones químicas y enzimas", "रासायनिक प्रतिक्रियाएँ और एंजाइम"),
    ("circulatory system", "循环系统", "sistema circulatorio", "परिसंचरण तंत्र"),
    ("climate change and ecosystem shifts", "气候变化与生态系统变迁", "cambio climático y cambios en los ecosistemas", "जलवायु परिवर्तन और पारिस्थितिक तंत्र में बदलाव"),
    ("community ecology", "群落生态学", "ecología de comunidades", "समुदाय पारिस्थितिकी"),
    ("conservation and sustainable development", "保护与可持续发展", "conservación y desarrollo sostenible", "संरक्षण और सतत विकास"),
    ("conserving biodiversity", "保护生物多样性", "conservación de la biodiversidad", "जैव विविधता का संरक्षण"),
    ("digestive system", "消化系统", "sistema digestivo", "पाचन तंत्र"),
    ("dna and rna", "DNA与RNA", "ADN y ARN", "डीएनए और आरएनए"),
    ("dna replication, transcription, and translation", "DNA复制、转录与翻译", "replicación, transcripción y traducción del ADN", "डीएनए प्रतिकृति, प्रतिलेखन और अनुवाद"),
    ("endangered species and conservation strategies", "濒危物种与保护策略", "especies en peligro y estrategias de conservación", "लुप्तप्राय प्रजातियाँ और संरक्षण रणनीतियाँ"),
    ("endocrine system", "内分泌系统", "sistema endocrino", "अंतःस्रावी तंत्र"),
    ("energy flow in living systems", "生命系统中的能量流动", "flujo de energía en los sistemas vivos", "जीवित प्रणालियों में ऊर्जा प्रवाह"),
    ("environmental biology", "环境生物学", "biología ambiental", "पर्यावरण जीव विज्ञान"),
    ("fermentation", "发酵", "fermentación", "किण्वन"),
    ("gene regulation and expression", "基因调控与表达", "regulación y expresión génica", "जीन विनियमन और अभिव्यक्ति"),
    ("global conservation efforts", "全球保护行动", "esfuerzos globales de conservación", "वैश्विक संरक्षण प्रयास"),
    ("homeostasis", "稳态", "homeostasis", "समस्थिति"),
    ("how organisms obtain energy", "生物获取能量的方式", "cómo los organismos obtienen energía", "जीव ऊर्जा कैसे प्राप्त करते हैं"),
    ("human genetics and genetic disorders", "人类遗传学与遗传疾病", "genética humana y trastornos genéticos", "मानव आनुवंशिकी और आनुवंशिक विकार"),
    ("human population growth and demographics", "人口增长与人口统计学", "crecimiento de la población humana y demografía", "मानव जनसंख्या वृद्धि और जनसांख्यिकी"),
    ("immune system", "免疫系统", "sistema inmunológico", "प्रतिरक्षा प्रणाली"),
    ("matter and atomic structure", "物质与原子结构", "materia y estructura atómica", "पदार्थ और परमाणु संरचना"),
    ("medicine and pharmacology", "医学与药理学", "medicina y farmacología", "चिकित्सा और औषध विज्ञान"),
    ("meiosis and sexual reproduction", "减数分裂与有性生殖", "meiosis y reproducción sexual", "अर्धसूत्री विभाजन और लैंगिक प्रजनन"),
    ("mendelian genetics", "孟德尔遗传学", "genética mendeliana", "मेंडल की आनुवंशिकी"),
    ("microscopy and cell imaging", "显微镜技术与细胞成像", "microscopía e imagen celular", "सूक्ष्मदर्शी विज्ञान और कोशिका इमेजिंग"),
    ("mitosis", "有丝分裂", "mitosis", "समसूत्री विभाजन"),
    ("nervous system", "神经系统", "sistema nervioso", "तंत्रिका तंत्र"),
    ("non-mendelian genetics", "非孟德尔遗传学", "genética no mendeliana", "गैर-मेंडल आनुवंशिकी"),
    ("organization of the human body", "人体组织结构", "organización del cuerpo humano", "मानव शरीर का संगठन"),
    ("photosynthesis", "光合作用", "fotosíntesis", "प्रकाश संश्लेषण"),
    ("population dynamics", "种群动态", "dinámica de poblaciones", "जनसंख्या गतिकी"),
    ("population regulation", "种群调控", "regulación de poblaciones", "जनसंख्या विनियमन"),
    ("prokaryotic vs. eukaryotic cells", "原核细胞与真核细胞", "células procariotas vs. eucariotas", "प्रोकैरियोटिक बनाम यूकैरियोटिक कोशिकाएँ"),
    ("reproductive system", "生殖系统", "sistema reproductivo", "प्रजनन तंत्र"),
    ("respiratory system", "呼吸系统", "sistema respiratorio", "श्वसन तंत्र"),
    ("stem cells and regenerative medicine", "干细胞与再生医学", "células madre y medicina regenerativa", "स्टेम सेल और पुनर्योजी चिकित्सा"),
    ("structures and organelles", "结构与细胞器", "estructuras y orgánulos", "संरचनाएँ और कोशिकांग"),
    ("symbiosis and species interactions", "共生与物种间的相互作用", "simbiosis e interacciones entre especies", "सहजीवन और प्रजातियों की परस्पर क्रिया"),
    ("terrestrial biomes", "陆地生物群落", "biomas terrestres", "स्थलीय बायोम"),
    ("the building blocks of life", "生命的基本组成单元", "los bloques de construcción de la vida", "जीवन के निर्माण खंड"),
    ("the cell cycle and cancer", "细胞周期与癌症", "el ciclo celular y el cáncer", "कोशिका चक्र और कैंसर"),
    ("the plasma membrane", "细胞膜", "la membrana plasmática", "प्लाज्मा झिल्ली"),
    ("threats to biodiversity", "生物多样性面临的威胁", "amenazas a la biodiversidad", "जैव विविधता के लिए खतरे"),
    ("water and its solutions", "水及其溶液", "el agua y sus soluciones", "जल और इसके विलयन"),
]

template_translations = {}

for en, zh, es, hi in TOPICS:
    # Summary template
    template_translations[f"This lesson covers the fundamental concepts of {en} in biology."] = (
        f"本课涵盖了生物学中{zh}的基本概念。",
        f"Esta lección cubre los conceptos fundamentales de {es} en biología.",
        f"यह पाठ जीव विज्ञान में {hi} की मूलभूत अवधारणाओं को शामिल करता है।"
    )
    # Q1: Main focus
    template_translations[f"1. What is the main focus of {en}?"] = (
        f"1. {zh}的主要重点是什么？",
        f"1. ¿Cuál es el enfoque principal de {es}?",
        f"1. {hi} का मुख्य फोकस क्या है?"
    )
    # Q2: Which field
    template_translations[f"2. Which field of science studies {en}?"] = (
        f"2. 哪个科学领域研究{zh}？",
        f"2. ¿Qué campo de la ciencia estudia {es}?",
        f"2. विज्ञान का कौन सा क्षेत्र {hi} का अध्ययन करता है?"
    )
    # Q3: Why study
    template_translations[f"3. Why do biologists study {en}?"] = (
        f"3. 生物学家为什么研究{zh}？",
        f"3. ¿Por qué los biólogos estudian {es}?",
        f"3. जीवविज्ञानी {hi} का अध्ययन क्यों करते हैं?"
    )
    # Q4: Best described
    template_translations[f"4. How is {en} best described?"] = (
        f"4. 如何最好地描述{zh}？",
        f"4. ¿Cómo se describe mejor {es}?",
        f"4. {hi} का सबसे अच्छा वर्णन कैसे किया जाता है?"
    )
    # Q5: Evidence
    template_translations[f"5. What evidence supports our understanding of {en}?"] = (
        f"5. 什么证据支持我们对{zh}的理解？",
        f"5. ¿Qué evidencia respalda nuestra comprensión de {es}?",
        f"5. {hi} की हमारी समझ को कौन से प्रमाण समर्थन करते हैं?"
    )
    # Q6: Affect organisms
    template_translations[f"6. How does {en} affect living organisms?"] = (
        f"6. {zh}如何影响生物体？",
        f"6. ¿Cómo afecta {es} a los organismos vivos?",
        f"6. {hi} जीवित जीवों को कैसे प्रभावित करता है?"
    )
    # Q7: What is true
    template_translations[f"7. What is true about {en}?"] = (
        f"7. 关于{zh}，哪项是正确的？",
        f"7. ¿Qué es verdad sobre {es}?",
        f"7. {hi} के बारे में क्या सत्य है?"
    )
