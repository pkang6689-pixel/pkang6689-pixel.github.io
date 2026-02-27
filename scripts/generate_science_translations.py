#!/usr/bin/env python3
"""
Generate translations for Biology, Chemistry, Geometry, and Physics lesson titles
in Chinese (Simplified), Spanish, and Hindi for the educational platform.
"""
import sys
import io

# Fix encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Comprehensive translation dictionary for all lesson titles
TRANSLATIONS = {
    # BIOLOGY LESSONS (80 titles)
    "Introduction to Biology": {
        "chinese": "生物学导论",
        "spanish": "Introducción a la Biología",
        "hindi": "जीव विज्ञान का परिचय"
    },
    "The Science of Life": {
        "chinese": "生命科学",
        "spanish": "La Ciencia de la Vida",
        "hindi": "जीवन का विज्ञान"
    },
    "The Nature of Science": {
        "chinese": "科学的本质",
        "spanish": "La Naturaleza de la Ciencia",
        "hindi": "विज्ञान की प्रकृति"
    },
    "Characteristics of Life": {
        "chinese": "生命的特征",
        "spanish": "Características de la Vida",
        "hindi": "जीवन की विशेषताएं"
    },
    "Levels of Biological Organization": {
        "chinese": "生物学组织的层级",
        "spanish": "Niveles de Organización Biológica",
        "hindi": "जैविक संगठन के स्तर"
    },
    "Branches of Biology": {
        "chinese": "生物学的分支",
        "spanish": "Ramas de la Biología",
        "hindi": "जीव विज्ञान की शाखाएं"
    },
    "Careers in Biology": {
        "chinese": "生物学职业",
        "spanish": "Carreras en Biología",
        "hindi": "जीव विज्ञान में करियर"
    },
    "Mendelian Genetics": {
        "chinese": "孟德尔遗传学",
        "spanish": "Genética Mendeliana",
        "hindi": "मेंडेलियन आनुवंशिकता"
    },
    "Non-Mendelian Genetics": {
        "chinese": "非孟德尔遗传学",
        "spanish": "Genética No Mendeliana",
        "hindi": "गैर-मेंडेलियन आनुवंशिकता"
    },
    "DNA Replication Transcription and Translation": {
        "chinese": "DNA复制、转录和翻译",
        "spanish": "Replicación del ADN, Transcripción y Traducción",
        "hindi": "डीएनए प्रतिकृति, प्रतिलेखन और अनुवाद"
    },
    "Gene Regulation and Expression": {
        "chinese": "基因调控和表达",
        "spanish": "Regulación y Expresión Génica",
        "hindi": "जीन विनियमन और अभिव्यक्ति"
    },
    "Biotechnology (CRISPR, cloning, GMOs)": {
        "chinese": "生物技术（CRISPR、克隆、转基因生物）",
        "spanish": "Biotecnología (CRISPR, Clonación, Organismos Genéticamente Modificados)",
        "hindi": "जैव प्रौद्योगिकी (CRISPR, क्लोनिंग, जीएमओ)"
    },
    "Human Genetics and Genetic Disorders": {
        "chinese": "人类遗传学和遗传疾病",
        "spanish": "Genética Humana y Trastornos Genéticos",
        "hindi": "मानव आनुवंशिकता और आनुवंशिक विकार"
    },
    "Organization of the Human Body": {
        "chinese": "人体的组织",
        "spanish": "Organización del Cuerpo Humano",
        "hindi": "मानव शरीर का संगठन"
    },
    "Circulatory System": {
        "chinese": "循环系统",
        "spanish": "Sistema Circulatorio",
        "hindi": "परिसंचरण तंत्र"
    },
    "Respiratory System": {
        "chinese": "呼吸系统",
        "spanish": "Sistema Respiratorio",
        "hindi": "श्वसन तंत्र"
    },
    "Digestive System": {
        "chinese": "消化系统",
        "spanish": "Sistema Digestivo",
        "hindi": "पाचन तंत्र"
    },
    "Nervous System": {
        "chinese": "神经系统",
        "spanish": "Sistema Nervioso",
        "hindi": "तंत्रिका तंत्र"
    },
    "Endocrine System": {
        "chinese": "内分泌系统",
        "spanish": "Sistema Endocrino",
        "hindi": "अंतःस्रावी तंत्र"
    },
    "Immune System": {
        "chinese": "免疫系统",
        "spanish": "Sistema Inmunológico",
        "hindi": "प्रतिरक्षा तंत्र"
    },
    "Reproductive System": {
        "chinese": "生殖系统",
        "spanish": "Sistema Reproductivo",
        "hindi": "प्रजनन तंत्र"
    },
    "Homeostasis": {
        "chinese": "内稳定性",
        "spanish": "Homeostasis",
        "hindi": "होमिओस्टेसिस"
    },
    "Biotechnology and Genetic Engineering": {
        "chinese": "生物技术和遗传工程",
        "spanish": "Biotecnología e Ingeniería Genética",
        "hindi": "जैव प्रौद्योगिकी और आनुवंशिक इंजीनियरिंग"
    },
    "Bioethics (cloning, stem cells, genetic privacy)": {
        "chinese": "生物伦理学（克隆、干细胞、遗传隐私）",
        "spanish": "Bioética (Clonación, Células Madre, Privacidad Genética)",
        "hindi": "जैवनैतिकता (क्लोनिंग, स्टेम सेल, आनुवंशिक गोपनीयता)"
    },
    "Medicine and Pharmacology": {
        "chinese": "医学和药理学",
        "spanish": "Medicina y Farmacología",
        "hindi": "चिकित्सा विज्ञान और औषध विज्ञान"
    },
    "Environmental Biology": {
        "chinese": "环境生物学",
        "spanish": "Biología Ambiental",
        "hindi": "पर्यावरणीय जीव विज्ञान"
    },
    "Astrobiology and the Search for Life Beyond Earth": {
        "chinese": "天体生物学和地外生命的搜寻",
        "spanish": "Astrobiología y la Búsqueda de Vida Extraterrestre",
        "hindi": "खगोल जीव विज्ञान और पृथ्वी से परे जीवन की खोज"
    },
    "Organisms and Their Relationships": {
        "chinese": "生物及其关系",
        "spanish": "Organismos y Sus Relaciones",
        "hindi": "जीव और उनके संबंध"
    },
    "Flow of Energy in an Ecosystem": {
        "chinese": "生态系统中的能量流动",
        "spanish": "Flujo de Energía en un Ecosistema",
        "hindi": "पारिस्थितिकी तंत्र में ऊर्जा का प्रवाह"
    },
    "Cycling of Matter": {
        "chinese": "物质循环",
        "spanish": "Ciclos de la Materia",
        "hindi": "पदार्थ का चक्र"
    },
    "Ecological Succession": {
        "chinese": "生态演替",
        "spanish": "Sucesión Ecológica",
        "hindi": "पारिस्थितिक अनुक्रम"
    },
    "Niches and Habitat": {
        "chinese": "生态位和栖息地",
        "spanish": "Nichos y Hábitats",
        "hindi": "आला और आवास"
    },
    "Food Chains Webs and Trophic Levels": {
        "chinese": "食物链、食物网和营养级",
        "spanish": "Cadenas Alimentarias, Redes Tróficas y Niveles Tróficos",
        "hindi": "खाद्य श्रंखला, खाद्य जाल और पोषण स्तर"
    },
    "Human Impact on Ecosystems": {
        "chinese": "人类对生态系统的影响",
        "spanish": "Impacto Humano en los Ecosistemas",
        "hindi": "पारिस्थितिकी तंत्र पर मानव प्रभाव"
    },
    "Community Ecology": {
        "chinese": "群落生态学",
        "spanish": "Ecología de Comunidades",
        "hindi": "समुदाय पारिस्थितिकी"
    },
    "Terrestrial Biomes": {
        "chinese": "陆地生物群落",
        "spanish": "Biomas Terrestres",
        "hindi": "स्थलीय जैव क्षेत्र"
    },
    "Aquatic Ecosystems": {
        "chinese": "水生生态系统",
        "spanish": "Ecosistemas Acuáticos",
        "hindi": "जलीय पारिस्थितिकी तंत्र"
    },
    "Climate Change and Ecosystem Shifts": {
        "chinese": "气候变化和生态系统转变",
        "spanish": "Cambio Climático y Cambios en los Ecosistemas",
        "hindi": "जलवायु परिवर्तन और पारिस्थितिकी तंत्र परिवर्तन"
    },
    "Symbiosis and Species Interactions": {
        "chinese": "共生和物种相互作用",
        "spanish": "Simbiosis e Interacciones Interespecíficas",
        "hindi": "सहजीवन और प्रजाति अंतःक्रिया"
    },
    "Population Dynamics": {
        "chinese": "种群动态",
        "spanish": "Dinámica de Poblaciones",
        "hindi": "जनसंख्या गतिकी"
    },
    "Human Population Growth and Demographics": {
        "chinese": "人口增长和人口统计学",
        "spanish": "Crecimiento Demográfico Humano",
        "hindi": "मानव जनसंख्या वृद्धि और जनांकिकी"
    },
    "Carrying Capacity and Limiting Factors": {
        "chinese": "环境容纳量和限制因素",
        "spanish": "Capacidad de Carga y Factores Limitantes",
        "hindi": "वहन क्षमता और सीमित कारक"
    },
    "Population Regulation": {
        "chinese": "种群调控",
        "spanish": "Regulación de Poblaciones",
        "hindi": "जनसंख्या विनियमन"
    },
    "Conservation and Sustainable Development": {
        "chinese": "保护和可持续发展",
        "spanish": "Conservación y Desarrollo Sostenible",
        "hindi": "संरक्षण और टिकाऊ विकास"
    },
    "Biodiversity": {
        "chinese": "生物多样性",
        "spanish": "Biodiversidad",
        "hindi": "जैविक विविधता"
    },
    "Threats to Biodiversity": {
        "chinese": "对生物多样性的威胁",
        "spanish": "Amenazas a la Biodiversidad",
        "hindi": "जैविक विविधता के लिए खतरे"
    },
    "Conserving Biodiversity": {
        "chinese": "保护生物多样性",
        "spanish": "Conservación de la Biodiversidad",
        "hindi": "जैविक विविधता का संरक्षण"
    },
    "Endangered Species and Conservation Strategies": {
        "chinese": "濒危物种和保护策略",
        "spanish": "Especies en Peligro de Extinción y Estrategias de Conservación",
        "hindi": "संकटग्रस्त प्रजातियां और संरक्षण रणनीतियां"
    },
    "Global Conservation Efforts": {
        "chinese": "全球保护工作",
        "spanish": "Esfuerzos Globales de Conservación",
        "hindi": "वैश्विक संरक्षण प्रयास"
    },
    "Matter and Atomic Structure": {
        "chinese": "物质和原子结构",
        "spanish": "Materia y Estructura Atómica",
        "hindi": "पदार्थ और परमाणु संरचना"
    },
    "Chemical Reactions and Enzymes": {
        "chinese": "化学反应和酶",
        "spanish": "Reacciones Químicas y Enzimas",
        "hindi": "रासायनिक प्रतिक्रियाएं और एंजाइम"
    },
    "Water and Its Solutions": {
        "chinese": "水和水溶液",
        "spanish": "Agua y Sus Soluciones",
        "hindi": "पानी और उसके घोल"
    },
    "The Building Blocks of Life": {
        "chinese": "生命的基本单位",
        "spanish": "Los Bloques de Construcción de la Vida",
        "hindi": "जीवन के निर्माण खंड"
    },
    "DNA and RNA": {
        "chinese": "DNA和RNA",
        "spanish": "ADN y ARN",
        "hindi": "डीएनए और आरएनए"
    },
    "Biochemistry in Everyday Life": {
        "chinese": "日常生活中的生物化学",
        "spanish": "Bioquímica en la Vida Cotidiana",
        "hindi": "दैनंदिन जीवन में जैव रसायन"
    },
    "Cell Structure and Function": {
        "chinese": "细胞结构和功能",
        "spanish": "Estructura y Función Celular",
        "hindi": "कोशिका संरचना और कार्य"
    },
    "Cell Discovery and Theory": {
        "chinese": "细胞的发现和理论",
        "spanish": "Descubrimiento y Teoría Celular",
        "hindi": "कोशिका की खोज और सिद्धांत"
    },
    "The Plasma Membrane": {
        "chinese": "质膜",
        "spanish": "La Membrana Plasmática",
        "hindi": "प्लाज्मा झिल्ली"
    },
    "Cellular Transport": {
        "chinese": "细胞运输",
        "spanish": "Transporte Celular",
        "hindi": "कोशिका परिवहन"
    },
    "Structures and Organelles": {
        "chinese": "细胞结构和细胞器",
        "spanish": "Estructuras y Orgánulos Celulares",
        "hindi": "संरचनाएं और कोशिकांग"
    },
    "Prokaryotic vs. Eukaryotic Cells": {
        "chinese": "原核细胞与真核细胞",
        "spanish": "Células Procariotas vs. Eucariotas",
        "hindi": "प्रोकैरियोटिक बनाम यूकेरियोटिक कोशिकाएं"
    },
    "Microscopy and Cell Imaging": {
        "chinese": "显微镜和细胞成像",
        "spanish": "Microscopía e Imagen Celular",
        "hindi": "सूक्ष्मदर्शन और कोशिका इमेजिंग"
    },
    "How Organisms Obtain Energy": {
        "chinese": "生物如何获得能量",
        "spanish": "Cómo Obtienen Energía los Organismos",
        "hindi": "जीव ऊर्जा कैसे प्राप्त करते हैं"
    },
    "Chemical Energy and ATP": {
        "chinese": "化学能和ATP",
        "spanish": "Energía Química y ATP",
        "hindi": "रासायनिक ऊर्जा और एटीपी"
    },
    "Photosynthesis": {
        "chinese": "光合作用",
        "spanish": "Fotosíntesis",
        "hindi": "प्रकाश संश्लेषण"
    },
    "Cellular Respiration": {
        "chinese": "细胞呼吸",
        "spanish": "Respiración Celular",
        "hindi": "कोशिका श्वसन"
    },
    "Fermentation": {
        "chinese": "发酵",
        "spanish": "Fermentación",
        "hindi": "किण्वन"
    },
    "Energy Flow in Living Systems": {
        "chinese": "生物系统中的能量流动",
        "spanish": "Flujo de Energía en Sistemas Vivientes",
        "hindi": "जीवित प्रणालियों में ऊर्जा प्रवाह"
    },
    "Cellular Reproduction": {
        "chinese": "细胞繁殖",
        "spanish": "Reproducción Celular",
        "hindi": "कोशिका प्रजनन"
    },
    "Mitosis": {
        "chinese": "有丝分裂",
        "spanish": "Mitosis",
        "hindi": "समसूत्री विभाजन"
    },
    "Meiosis and Sexual Reproduction": {
        "chinese": "减数分裂和有性生殖",
        "spanish": "Meiosis y Reproducción Sexual",
        "hindi": "अर्धसूत्री विभाजन और लैंगिक प्रजनन"
    },
    "The Cell Cycle and Cancer": {
        "chinese": "细胞周期和癌症",
        "spanish": "Ciclo Celular y Cáncer",
        "hindi": "कोशिका चक्र और कैंसर"
    },
    "Stem Cells and Regenerative Medicine": {
        "chinese": "干细胞和再生医学",
        "spanish": "Células Madre y Medicina Regenerativa",
        "hindi": "स्टेम सेल और पुनर्जनन चिकित्सा"
    },

    # CHEMISTRY LESSONS (130+ titles)
    "States of Matter": {
        "chinese": "物质状态",
        "spanish": "Estados de la Materia",
        "hindi": "पदार्थ की अवस्थाएँ"
    },
    "Phase Changes": {
        "chinese": "物态变化",
        "spanish": "Cambios de Estado",
        "hindi": "अवस्था परिवर्तन"
    },
    "Intensive & Extensive Properties": {
        "chinese": "密集性和延伸性质",
        "spanish": "Propiedades Intensivas y Extensivas",
        "hindi": "गहन और व्यापक गुण"
    },
    "Mass Volume & Density": {
        "chinese": "质量、体积和密度",
        "spanish": "Masa, Volumen y Densidad",
        "hindi": "द्रव्यमान, आयतन और घनत्व"
    },
    "Heterogeneous & Homogeneous Mixtures": {
        "chinese": "不均一混合物与均一混合物",
        "spanish": "Mezclas Heterogéneas y Homogéneas",
        "hindi": "विषम और समांग मिश्रण"
    },
    "Physical & Chemical Properties": {
        "chinese": "物理性质和化学性质",
        "spanish": "Propiedades Físicas y Químicas",
        "hindi": "भौतिक और रासायनिक गुण"
    },
    "Physical & Chemical Changes": {
        "chinese": "物理变化和化学变化",
        "spanish": "Cambios Físicos y Químicos",
        "hindi": "भौतिक और रासायनिक परिवर्तन"
    },
    "Energy & Matter": {
        "chinese": "能量与物质",
        "spanish": "Energía y Materia",
        "hindi": "ऊर्जा और पदार्थ"
    },
    "Acid & Base Properties": {
        "chinese": "酸与碱的性质",
        "spanish": "Propiedades de Ácidos y Bases",
        "hindi": "अम्ल और क्षार के गुण"
    },
    "Binary Acids vs. Oxyacids": {
        "chinese": "二元酸与含氧酸",
        "spanish": "Ácidos Binarios vs. Oxiácidos",
        "hindi": "बाइनरी एसिड बनाम ऑक्सीएसिड"
    },
    "Naming Acids": {
        "chinese": "酸的命名",
        "spanish": "Nomenclatura de Ácidos",
        "hindi": "अम्लों का नामकरण"
    },
    "Identifying Acids & Bases": {
        "chinese": "鉴定酸与碱",
        "spanish": "Identificación de Ácidos y Bases",
        "hindi": "अम्ल और क्षार की पहचान"
    },
    "Strong vs. Weak Acids/Bases": {
        "chinese": "强酸强碱与弱酸弱碱",
        "spanish": "Ácidos y Bases Fuertes vs. Débiles",
        "hindi": "मजबूत और कमजोर अम्ल/क्षार"
    },
    "Neutralization Reactions": {
        "chinese": "中和反应",
        "spanish": "Reacciones de Neutralización",
        "hindi": "तटस्थीकरण प्रतिक्रिएं"
    },
    "Naming Salts from Neutralization": {
        "chinese": "中和反应生成的盐的命名",
        "spanish": "Nomenclatura de Sales de Neutralización",
        "hindi": "तटस्थीकरण से लवणों का नामकरण"
    },
    "Buffer Solutions": {
        "chinese": "缓冲溶液",
        "spanish": "Soluciones Amortiguadoras",
        "hindi": "बफर समाधान"
    },
    "pH & pOH Scale": {
        "chinese": "pH和pOH标度",
        "spanish": "Escala de pH y pOH",
        "hindi": "पीएच और पीओएच पैमाना"
    },
    "Heat Conversion": {
        "chinese": "热转换",
        "spanish": "Conversión de Calor",
        "hindi": "ऊष्मा रूपांतरण"
    },
    "Specific Heat": {
        "chinese": "比热",
        "spanish": "Calor Específico",
        "hindi": "विशिष्ट ऊष्मा"
    },
    "Heat Capacity": {
        "chinese": "热容量",
        "spanish": "Capacidad Calorífica",
        "hindi": "ऊष्मा क्षमता"
    },
    "Calorimetry": {
        "chinese": "量热法",
        "spanish": "Calorimetría",
        "hindi": "कैलोरीमेट्री"
    },
    "Enthalpy Entropy Free Energy": {
        "chinese": "焓、熵和自由能",
        "spanish": "Entalpía, Entropía y Energía Libre",
        "hindi": "एन्थैल्पी, एन्ट्रॉपी और मुक्त ऊर्जा"
    },
    "Hess's Law": {
        "chinese": "黑斯定律",
        "spanish": "Ley de Hess",
        "hindi": "हेस का नियम"
    },
    "Nuclear Fusion and Fission": {
        "chinese": "核聚变和核裂变",
        "spanish": "Fusión y Fisión Nuclear",
        "hindi": "नाभिकीय संलयन और विखंडन"
    },
    "Alpha Beta & Gamma Decay": {
        "chinese": "α、β和γ衰变",
        "spanish": "Desintegración Alfa, Beta y Gamma",
        "hindi": "अल्फा, बीटा और गामा क्षय"
    },
    "Nuclear Reactions": {
        "chinese": "核反应",
        "spanish": "Reacciones Nucleares",
        "hindi": "नाभिकीय प्रतिक्रियाएं"
    },
    "Half-Life Calculations": {
        "chinese": "半衰期计算",
        "spanish": "Cálculos de Vida Media",
        "hindi": "अर्ध-जीवन गणना"
    },
    "Applications of Nuclear Chemistry": {
        "chinese": "核化学的应用",
        "spanish": "Aplicaciones de Química Nuclear",
        "hindi": "नाभिकीय रसायन के अनुप्रयोग"
    },
    "Scientific Notation": {
        "chinese": "科学记数法",
        "spanish": "Notación Científica",
        "hindi": "वैज्ञानिक संकेतन"
    },
    "Significant Figures": {
        "chinese": "有效数字",
        "spanish": "Cifras Significativas",
        "hindi": "महत्वपूर्ण अंक"
    },
    "Accuracy vs. Precision": {
        "chinese": "准确度与精确度",
        "spanish": "Exactitud vs. Precisión",
        "hindi": "सटीकता बनाम परिशुद्धता"
    },
    "Metric System": {
        "chinese": "公制",
        "spanish": "Sistema Métrico",
        "hindi": "मेट्रिक प्रणाली"
    },
    "Unit Conversions": {
        "chinese": "单位转换",
        "spanish": "Conversiones de Unidades",
        "hindi": "इकाई रूपांतरण"
    },
    "Electrons Protons and Neutrons": {
        "chinese": "电子、质子和中子",
        "spanish": "Electrones, Protones y Neutrones",
        "hindi": "इलेक्ट्रॉन, प्रोटॉन और न्यूट्रॉन"
    },
    "Atomic Structure": {
        "chinese": "原子结构",
        "spanish": "Estructura Atómica",
        "hindi": "परमाणु संरचना"
    },
    "Quantum Mechanical Model & Orbitals": {
        "chinese": "量子力学模型和轨道",
        "spanish": "Modelo Mecánico Cuántico y Orbitales",
        "hindi": "क्वांटम यांत्रिक मॉडल और ऑर्बिटल"
    },
    "Electromagnetic Spectrum & Atomic Emission Spectra": {
        "chinese": "电磁波谱和原子发射光谱",
        "spanish": "Espectro Electromagnético y Espectros de Emisión Atómica",
        "hindi": "विद्युत चुंबकीय स्पेक्ट्रम और परमाणु उत्सर्जन स्पेक्ट्रा"
    },
    "Radioactivity & Stability": {
        "chinese": "放射性和稳定性",
        "spanish": "Radiactividad y Estabilidad",
        "hindi": "रेडियोसक्रियता और स्थिरता"
    },
    "Isotopes & Radioisotopes": {
        "chinese": "同位素和放射性同位素",
        "spanish": "Isótopos e Isótopos Radiactivos",
        "hindi": "समस्थानिक और रेडियोसमस्थानिक"
    },
    "Element Synthesis": {
        "chinese": "元素合成",
        "spanish": "Síntesis de Elementos",
        "hindi": "तत्व संश्लेषण"
    },
    "Atomic Theory": {
        "chinese": "原子论",
        "spanish": "Teoría Atómica",
        "hindi": "परमाणु सिद्धांत"
    },
    "Chemical Symbols": {
        "chinese": "化学符号",
        "spanish": "Símbolos Químicos",
        "hindi": "रासायनिक प्रतीक"
    },
    "Periodic Table Arrangement": {
        "chinese": "元素周期表的排列",
        "spanish": "Disposición de la Tabla Periódica",
        "hindi": "आवर्त सारणी की व्यवस्था"
    },
    "Valence Electrons & Reactivity": {
        "chinese": "价电子和反应性",
        "spanish": "Electrones de Valencia y Reactividad",
        "hindi": "संयोजकता इलेक्ट्रॉन और प्रतिक्रियाशीलता"
    },
    "Electron Suborbitals": {
        "chinese": "电子亚轨道",
        "spanish": "Suborbitales de Electrones",
        "hindi": "इलेक्ट्रॉन सबऑर्बिटल्स"
    },
    "Electron Configuration": {
        "chinese": "电子构型",
        "spanish": "Configuración Electrónica",
        "hindi": "इलेक्ट्रॉन विन्यास"
    },
    "Periodic Trends": {
        "chinese": "周期趋势",
        "spanish": "Tendencias Periódicas",
        "hindi": "आवर्त प्रवृत्तियां"
    },
    "Shielding Effect": {
        "chinese": "屏蔽效应",
        "spanish": "Efecto de Apantallamiento",
        "hindi": "परिरक्षण प्रभाव"
    },
    "VSEPR Molecule Shapes": {
        "chinese": "VSEPR分子形状",
        "spanish": "Formas Moleculares VSEPR",
        "hindi": "VSEPR अणु आकार"
    },
    "Suborbital Shapes": {
        "chinese": "亚轨道形状",
        "spanish": "Formas de Suborbitales",
        "hindi": "सबऑर्बिटल आकार"
    },
    "Introduction to Nomenclature": {
        "chinese": "命名法介绍",
        "spanish": "Introducción a la Nomenclatura",
        "hindi": "नामकरण का परिचय"
    },
    "Net Charge": {
        "chinese": "净电荷",
        "spanish": "Carga Neta",
        "hindi": "शुद्ध आवेश"
    },
    "Bond Formation": {
        "chinese": "键的形成",
        "spanish": "Formación de Enlaces",
        "hindi": "बंध निर्माण"
    },
    "Ionic Bonds": {
        "chinese": "离子键",
        "spanish": "Enlaces Iónicos",
        "hindi": "आयनिक बंध"
    },
    "Crisscross Method": {
        "chinese": "交叉法则",
        "spanish": "Método de Cruzamiento",
        "hindi": "क्रॉसओवर विधि"
    },
    "Naming Ionic Compounds": {
        "chinese": "离子化合物的命名",
        "spanish": "Nomenclatura de Compuestos Iónicos",
        "hindi": "आयनिक यौगिकों का नामकरण"
    },
    "Polyatomic Ions": {
        "chinese": "多原子离子",
        "spanish": "Iones Poliatómicos",
        "hindi": "बहु-परमाणु आयन"
    },
    "Common Exceptions & Traditional Names": {
        "chinese": "常见例外和传统名称",
        "spanish": "Excepciones Comunes y Nombres Tradicionales",
        "hindi": "सामान्य अपवाद और पारंपरिक नाम"
    },
    "Covalent Bonds": {
        "chinese": "共价键",
        "spanish": "Enlaces Covalentes",
        "hindi": "सहसंयोजक बंध"
    },
    "Naming Covalent Compounds": {
        "chinese": "共价化合物的命名",
        "spanish": "Nomenclatura de Compuestos Covalentes",
        "hindi": "सहसंयोजक यौगिकों का नामकरण"
    },
    "Metallic Bonds": {
        "chinese": "金属键",
        "spanish": "Enlaces Metálicos",
        "hindi": "धात्विक बंध"
    },
    "Organic Compounds": {
        "chinese": "有机化合物",
        "spanish": "Compuestos Orgánicos",
        "hindi": "जैविक यौगिक"
    },
    "Mixed Nomenclature Practice": {
        "chinese": "混合命名法练习",
        "spanish": "Práctica de Nomenclatura Mixta",
        "hindi": "मिश्रित नामकरण अभ्यास"
    },
    "Types of Reactions": {
        "chinese": "反应类型",
        "spanish": "Tipos de Reacciones",
        "hindi": "प्रतिक्रिया के प्रकार"
    },
    "Combustion Reactions": {
        "chinese": "燃烧反应",
        "spanish": "Reacciones de Combustión",
        "hindi": "दहन प्रतिक्रियाएं"
    },
    "Redox Reactions": {
        "chinese": "氧化还原反应",
        "spanish": "Reacciones Redox",
        "hindi": "रेडॉक्स प्रतिक्रियाएं"
    },
    "Activation Energy": {
        "chinese": "活化能",
        "spanish": "Energía de Activación",
        "hindi": "सक्रियकरण ऊर्जा"
    },
    "Balancing Equations": {
        "chinese": "平衡化学方程式",
        "spanish": "Equilibrado de Ecuaciones",
        "hindi": "समीकरणों को संतुलित करना"
    },
    "Reaction Rates & Catalysts": {
        "chinese": "反应速率和催化剂",
        "spanish": "Velocidades de Reacción y Catalizadores",
        "hindi": "प्रतिक्रिया दर और उत्प्रेरक"
    },
    "Chemical Equilibrium & Le Chatelier's Principle": {
        "chinese": "化学平衡和勒夏特列原理",
        "spanish": "Equilibrio Químico y Principio de Le Chatelier",
        "hindi": "रासायनिक संतुलन और ले चेटेलियर का सिद्धांत"
    },
    "Writing Correct Formulas": {
        "chinese": "书写正确的化学式",
        "spanish": "Escritura de Fórmulas Correctas",
        "hindi": "सही सूत्र लिखना"
    },
    "Molar Mass & Molecular Mass": {
        "chinese": "摩尔质量和相对分子质量",
        "spanish": "Masa Molar y Masa Molecular",
        "hindi": "मोलर द्रव्यमान और आणविक द्रव्यमान"
    },
    "Avogadro's Number": {
        "chinese": "阿伏伽德罗常数",
        "spanish": "Número de Avogadro",
        "hindi": "अवोगाद्रो की संख्या"
    },
    "Molar Conversions": {
        "chinese": "摩尔转换",
        "spanish": "Conversiones Molares",
        "hindi": "मोलर रूपांतरण"
    },
    "Empirical vs. Molecular Formulas": {
        "chinese": "经验式和分子式",
        "spanish": "Fórmulas Empíricas vs. Moleculares",
        "hindi": "अनुभवजन्य बनाम आणविक सूत्र"
    },
    "Limiting Reagents": {
        "chinese": "限制反应物",
        "spanish": "Reactivos Limitantes",
        "hindi": "सीमित अभिकारक"
    },
    "Stoichiometric Calculations": {
        "chinese": "化学计量计算",
        "spanish": "Cálculos Estequiométricos",
        "hindi": "स्टोइकियोमेट्रिक गणना"
    },
    "Percent Yield": {
        "chinese": "产率百分比",
        "spanish": "Rendimiento Porcentual",
        "hindi": "प्रतिशत उपज"
    },
    "Monatomic & Diatomic Gases": {
        "chinese": "单原子和双原子气体",
        "spanish": "Gases Monoatómicos y Diatómicos",
        "hindi": "एकपरमाणु और द्विपरमाणु गैसें"
    },
    "Pressure Standard Atmosphere": {
        "chinese": "压力和标准大气",
        "spanish": "Presión y Atmósfera Estándar",
        "hindi": "दबाव और मानक वातावरण"
    },
    "Kinetic Molecular Theory": {
        "chinese": "分子动理论",
        "spanish": "Teoría Cinética Molecular",
        "hindi": "गतिज आणविक सिद्धांत"
    },
    "Boyle's Law": {
        "chinese": "波义尔定律",
        "spanish": "Ley de Boyle",
        "hindi": "बॉयल का नियम"
    },
    "Charles' Law": {
        "chinese": "查理定律",
        "spanish": "Ley de Charles",
        "hindi": "चार्ल्स का नियम"
    },
    "Gay-Lussac's Law": {
        "chinese": "盖-吕萨克定律",
        "spanish": "Ley de Gay-Lussac",
        "hindi": "गे-लुसाक का नियम"
    },
    "Combined Gas Law": {
        "chinese": "综合气体定律",
        "spanish": "Ley de los Gases Combinados",
        "hindi": "संयुक्त गैस नियम"
    },
    "Ideal Gas Law": {
        "chinese": "理想气体定律",
        "spanish": "Ley de los Gases Ideales",
        "hindi": "आदर्श गैस नियम"
    },
    "Real Gases & Deviations": {
        "chinese": "真实气体和偏差",
        "spanish": "Gases Reales y Desviaciones",
        "hindi": "वास्तविक गैसें और विचलन"
    },
    "Solution Nomenclature": {
        "chinese": "溶液的命名",
        "spanish": "Nomenclatura de Soluciones",
        "hindi": "समाधान नामकरण"
    },
    "Concentration": {
        "chinese": "浓度",
        "spanish": "Concentración",
        "hindi": "सांद्रण"
    },
    "Dilution": {
        "chinese": "稀释",
        "spanish": "Dilución",
        "hindi": "पतलापन"
    },
    "Molarity": {
        "chinese": "摩尔浓度",
        "spanish": "Molaridad",
        "hindi": "मोलैरिटी"
    },
    "Solution Types": {
        "chinese": "溶液类型",
        "spanish": "Tipos de Soluciones",
        "hindi": "समाधान के प्रकार"
    },
    "Factors Affecting Solubility": {
        "chinese": "影响溶解度的因素",
        "spanish": "Factores que Afectan la Solubilidad",
        "hindi": "घुलनशीलता को प्रभावित करने वाले कारक"
    },
    "Colligative Properties": {
        "chinese": "依数性",
        "spanish": "Propiedades Coligativas",
        "hindi": "सम्मिलन गुण"
    },
    "Solubility Curves": {
        "chinese": "溶解度曲线",
        "spanish": "Curvas de Solubilidad",
        "hindi": "घुलनशीलता वक्र"
    },

    # GEOMETRY LESSONS (120+ titles)
    "Points Lines and Planes": {
        "chinese": "点、线和平面",
        "spanish": "Puntos, Líneas y Planos",
        "hindi": "बिंदु, रेखाएं और समतल"
    },
    "Linear Measure and Precision": {
        "chinese": "线性测度和精确度",
        "spanish": "Medida Lineal y Precisión",
        "hindi": "रैखिक माप और परिशुद्धता"
    },
    "Distance and Midpoints": {
        "chinese": "距离和中点",
        "spanish": "Distancia y Puntos Medios",
        "hindi": "दूरी और मध्य बिंदु"
    },
    "Angle Measure": {
        "chinese": "角的度量",
        "spanish": "Medida de Ángulos",
        "hindi": "कोण माप"
    },
    "Angle Relationships": {
        "chinese": "角的关系",
        "spanish": "Relaciones de Ángulos",
        "hindi": "कोण संबंध"
    },
    "Two-Dimensional Figures": {
        "chinese": "二维图形",
        "spanish": "Figuras Bidimensionales",
        "hindi": "द्वि-आयामी आकृतियां"
    },
    "Three-Dimensional Figures": {
        "chinese": "三维图形",
        "spanish": "Figuras Tridimensionales",
        "hindi": "त्रि-आयामी आकृतियां"
    },
    "Circles and Circumference": {
        "chinese": "圆和圆周",
        "spanish": "Círculos y Circunferencia",
        "hindi": "वृत्त और परिधि"
    },
    "Measuring Angles and Arcs": {
        "chinese": "角和弧的度量",
        "spanish": "Medida de Ángulos y Arcos",
        "hindi": "कोण और चाप माप"
    },
    "Arcs and Chords": {
        "chinese": "弧和弦",
        "spanish": "Arcos y Cuerdas",
        "hindi": "चाप और जीवाएं"
    },
    "Inscribed Angles": {
        "chinese": "圆周角",
        "spanish": "Ángulos Inscritos",
        "hindi": "अंतर्निहित कोण"
    },
    "Tangents": {
        "chinese": "切线",
        "spanish": "Tangentes",
        "hindi": "स्पर्श रेखाएं"
    },
    "Secants Tangents and Angle Measures": {
        "chinese": "割线、切线和角的度量",
        "spanish": "Secantes, Tangentes y Medidas de Ángulos",
        "hindi": "छेदक, स्पर्श रेखाएं और कोण माप"
    },
    "Special Segments in a Circle": {
        "chinese": "圆中的特殊线段",
        "spanish": "Segmentos Especiales en un Círculo",
        "hindi": "वृत्त में विशेष खंड"
    },
    "Equations of Circles": {
        "chinese": "圆的方程",
        "spanish": "Ecuaciones de Círculos",
        "hindi": "वृत्त के समीकरण"
    },
    "Conic Sections (intro)": {
        "chinese": "圆锥曲线（介绍）",
        "spanish": "Secciones Cónicas (Introducción)",
        "hindi": "शांकव खंड (परिचय)"
    },
    "Areas of Parallelograms and Triangles": {
        "chinese": "平行四边形和三角形的面积",
        "spanish": "Áreas de Paralelogramos y Triángulos",
        "hindi": "समांतर चतुर्भुज और त्रिभुजों के क्षेत्र"
    },
    "Areas of Trapezoids Rhombi and Kites": {
        "chinese": "梯形、菱形和风筝的面积",
        "spanish": "Áreas de Trapezoides, Rombos y Cometas",
        "hindi": "समलम्ब, समचतुर्भुज और पतंग के क्षेत्र"
    },
    "Areas of Circles and Sectors": {
        "chinese": "圆和扇形的面积",
        "spanish": "Áreas de Círculos y Sectores",
        "hindi": "वृत्त और त्रिज्य खंड के क्षेत्र"
    },
    "Areas of Regular Polygons and Composite Figures": {
        "chinese": "正多边形和复合图形的面积",
        "spanish": "Áreas de Polígonos Regulares y Figuras Compuestas",
        "hindi": "नियमित बहुभुज और मिश्रित आकृतियों के क्षेत्र"
    },
    "Areas of Similar Figures": {
        "chinese": "相似图形的面积",
        "spanish": "Áreas de Figuras Similares",
        "hindi": "समान आकृतियों के क्षेत्र"
    },
    "Integration in Area Calculations": {
        "chinese": "面积计算中的积分",
        "spanish": "Integración en Cálculos de Áreas",
        "hindi": "क्षेत्र गणना में एकीकरण"
    },
    "Representations of Three-Dimensional Figures": {
        "chinese": "三维图形的表示",
        "spanish": "Representaciones de Figuras Tridimensionales",
        "hindi": "त्रि-आयामी आकृतियों का प्रतिनिधित्व"
    },
    "Surface Areas of Prisms and Cylinders": {
        "chinese": "棱柱和圆柱的表面积",
        "spanish": "Áreas de Superficie de Prismas y Cilindros",
        "hindi": "प्रिज्म और सिलेंडर का सतह क्षेत्र"
    },
    "Surface Areas of Pyramids and Cones": {
        "chinese": "棱锥和圆锥的表面积",
        "spanish": "Áreas de Superficie de Pirámides y Conos",
        "hindi": "पिरामिड और शंकु का सतह क्षेत्र"
    },
    "Volumes of Prisms and Cylinders": {
        "chinese": "棱柱和圆柱的体积",
        "spanish": "Volúmenes de Prismas y Cilindros",
        "hindi": "प्रिज्म और सिलेंडर का आयतन"
    },
    "Volumes of Pyramids and Cones": {
        "chinese": "棱锥和圆锥的体积",
        "spanish": "Volúmenes de Pirámides y Conos",
        "hindi": "पिरामिड और शंकु का आयतन"
    },
    "Surface Areas and Volumes of Spheres": {
        "chinese": "球的表面积和体积",
        "spanish": "Áreas de Superficie y Volúmenes de Esferas",
        "hindi": "गोले का सतह क्षेत्र और आयतन"
    },
    "Spherical Geometry": {
        "chinese": "球面几何",
        "spanish": "Geometría Esférica",
        "hindi": "गोलाकार ज्यामिति"
    },
    "Congruent and Similar Solids": {
        "chinese": "合同的和相似的立体",
        "spanish": "Sólidos Congruentes y Similares",
        "hindi": "सर्वांगसम और समान ठोस"
    },
    "Cavalieri's Principle and Applications": {
        "chinese": "卡瓦列里原理和应用",
        "spanish": "Principio de Cavalieri y Aplicaciones",
        "hindi": "कैवेलियरी का सिद्धांत और अनुप्रयोग"
    },
    "Representing Sample Spaces": {
        "chinese": "样本空间的表示",
        "spanish": "Representación de Espacios Muestrales",
        "hindi": "नमूना स्थान का प्रतिनिधित्व"
    },
    "Permutations and Combinations": {
        "chinese": "排列和组合",
        "spanish": "Permutaciones y Combinaciones",
        "hindi": "क्रमचय और संयोजन"
    },
    "Geometric Probability": {
        "chinese": "几何概率",
        "spanish": "Probabilidad Geométrica",
        "hindi": "ज्यामितीय संभावना"
    },
    "Simulations": {
        "chinese": "模拟",
        "spanish": "Simulaciones",
        "hindi": "सिमुलेशन"
    },
    "Probabilities of Independent and Dependent Events": {
        "chinese": "独立和从属事件的概率",
        "spanish": "Probabilidades de Eventos Independientes y Dependientes",
        "hindi": "स्वतंत्र और आश्रित घटनाओं की संभावना"
    },
    "Probabilities of Mutually Exclusive Events": {
        "chinese": "互斥事件的概率",
        "spanish": "Probabilidades de Eventos Mutuamente Excluyentes",
        "hindi": "परस्पर अनन्य घटनाओं की संभावना"
    },
    "Monte Carlo Methods in Geometry": {
        "chinese": "几何中的蒙特卡罗方法",
        "spanish": "Métodos de Monte Carlo en Geometría",
        "hindi": "ज्यामिति में मोंटे कार्लो विधियां"
    },
    "Inductive Reasoning and Conjecture": {
        "chinese": "归纳推理和猜想",
        "spanish": "Razonamiento Inductivo y Conjetura",
        "hindi": "आगमनात्मक तर्क और अनुमान"
    },
    "Logic": {
        "chinese": "逻辑学",
        "spanish": "Lógica",
        "hindi": "तर्क"
    },
    "Conditional Statements": {
        "chinese": "条件语句",
        "spanish": "Enunciados Condicionales",
        "hindi": "सशर्त कथन"
    },
    "Deductive Reasoning": {
        "chinese": "演绎推理",
        "spanish": "Razonamiento Deductivo",
        "hindi": "निगमनात्मक तर्क"
    },
    "Postulates and Paragraph Proofs": {
        "chinese": "公理和段落证明",
        "spanish": "Postulados y Pruebas de Párrafo",
        "hindi": "अभिगृहीत और पैराग्राफ प्रमाण"
    },
    "Algebraic Proof": {
        "chinese": "代数证明",
        "spanish": "Prueba Algebraica",
        "hindi": "बीजगणितीय प्रमाण"
    },
    "Proving Segment Relationships": {
        "chinese": "证明线段关系",
        "spanish": "Prueba de Relaciones de Segmentos",
        "hindi": "खंड संबंध को साबित करना"
    },
    "Proving Angle Relationships": {
        "chinese": "证明角度关系",
        "spanish": "Prueba de Relaciones de Ángulos",
        "hindi": "कोण संबंध को साबित करना"
    },
    "Proofs in Coordinate Geometry": {
        "chinese": "坐标几何中的证明",
        "spanish": "Pruebas en Geometría Coordinada",
        "hindi": "समन्वय ज्यामिति में प्रमाण"
    },
    "Parallel Lines and Transversals": {
        "chinese": "平行线和横截线",
        "spanish": "Líneas Paralelas y Transversales",
        "hindi": "समानांतर रेखाएं और अनुप्रस्थ"
    },
    "Angles and Parallel Lines": {
        "chinese": "角和平行线",
        "spanish": "Ángulos y Líneas Paralelas",
        "hindi": "कोण और समानांतर रेखाएं"
    },
    "Slopes of Lines": {
        "chinese": "直线的斜率",
        "spanish": "Pendientes de Líneas",
        "hindi": "रेखाओं की ढलान"
    },
    "Equations of Lines": {
        "chinese": "直线的方程",
        "spanish": "Ecuaciones de Líneas",
        "hindi": "रेखाओं के समीकरण"
    },
    "Proving Lines Parallel": {
        "chinese": "证明直线平行",
        "spanish": "Prueba de Líneas Paralelas",
        "hindi": "समानांतर रेखाओं को साबित करना"
    },
    "Perpendiculars and Distance": {
        "chinese": "垂直和距离",
        "spanish": "Perpendiculares y Distancia",
        "hindi": "लंबवत और दूरी"
    },
    "Analytic Geometry Applications": {
        "chinese": "解析几何应用",
        "spanish": "Aplicaciones de Geometría Analítica",
        "hindi": "विश्लेषणात्मक ज्यामिति अनुप्रयोग"
    },
    "Classifying Triangles": {
        "chinese": "三角形的分类",
        "spanish": "Clasificación de Triángulos",
        "hindi": "त्रिभुजों का वर्गीकरण"
    },
    "Angles of Triangles": {
        "chinese": "三角形的角",
        "spanish": "Ángulos de Triángulos",
        "hindi": "त्रिभुज के कोण"
    },
    "Congruent Triangles": {
        "chinese": "合同三角形",
        "spanish": "Triángulos Congruentes",
        "hindi": "सर्वांगसम त्रिभुज"
    },
    "Proving Congruence SSS SAS": {
        "chinese": "证明全等（SSS、SAS）",
        "spanish": "Prueba de Congruencia (SSS, SAS)",
        "hindi": "सर्वांगसमता को साबित करना (SSS, SAS)"
    },
    "Proving Congruence ASA AAS": {
        "chinese": "证明全等（ASA、AAS）",
        "spanish": "Prueba de Congruencia (ASA, AAS)",
        "hindi": "सर्वांगसमता को साबित करना (ASA, AAS)"
    },
    "Isosceles and Equilateral Triangles": {
        "chinese": "等腰三角形和等边三角形",
        "spanish": "Triángulos Isósceles y Equiláteros",
        "hindi": "समद्विबाहु और समबाहु त्रिभुज"
    },
    "Congruence Transformations": {
        "chinese": "全等变换",
        "spanish": "Transformaciones de Congruencia",
        "hindi": "सर्वांगसमता परिवर्तन"
    },
    "Triangles and Coordinate Proof": {
        "chinese": "三角形和坐标证明",
        "spanish": "Triángulos y Prueba de Coordenadas",
        "hindi": "त्रिभुज और समन्वय प्रमाण"
    },
    "Bisectors of Triangles": {
        "chinese": "三角形的平分线",
        "spanish": "Bisectrices de Triángulos",
        "hindi": "त्रिभुजों के द्विभाजक"
    },
    "Medians and Altitudes of Triangles": {
        "chinese": "三角形的中线和高",
        "spanish": "Medianas y Altitudes de Triángulos",
        "hindi": "त्रिभुजों की माध्यिकाएं और ऊंचाइयां"
    },
    "Inequalities in One Triangle": {
        "chinese": "一个三角形中的不等式",
        "spanish": "Desigualdades en un Triángulo",
        "hindi": "एक त्रिभुज में असमानताएं"
    },
    "Indirect Proof": {
        "chinese": "间接证明",
        "spanish": "Prueba Indirecta",
        "hindi": "अप्रत्यक्ष प्रमाण"
    },
    "The Triangle Inequality": {
        "chinese": "三角形不等式",
        "spanish": "La Desigualdad del Triángulo",
        "hindi": "त्रिकोण असमानता"
    },
    "Inequalities in Two Triangles": {
        "chinese": "两个三角形中的不等式",
        "spanish": "Desigualdades en Dos Triángulos",
        "hindi": "दो त्रिभुजों में असमानताएं"
    },
    "Angles of Polygons": {
        "chinese": "多边形的角",
        "spanish": "Ángulos de Polígonos",
        "hindi": "बहुभुजों के कोण"
    },
    "Parallelograms": {
        "chinese": "平行四边形",
        "spanish": "Paralelogramos",
        "hindi": "समांतर चतुर्भुज"
    },
    "Tests for Parallelograms": {
        "chinese": "平行四边形的判定",
        "spanish": "Pruebas para Paralelogramos",
        "hindi": "समांतर चतुर्भुजों के लिए परीक्षण"
    },
    "Rectangles": {
        "chinese": "矩形",
        "spanish": "Rectángulos",
        "hindi": "आयत"
    },
    "Rhombi and Squares": {
        "chinese": "菱形和正方形",
        "spanish": "Rombos y Cuadrados",
        "hindi": "समचतुर्भुज और वर्ग"
    },
    "Kites and Trapezoids": {
        "chinese": "风筝和梯形",
        "spanish": "Cometas y Trapezoides",
        "hindi": "पतंग और समलम्ब"
    },
    "Regular Polygons and Symmetry": {
        "chinese": "正多边形和对称性",
        "spanish": "Polígonos Regulares y Simetría",
        "hindi": "नियमित बहुभुज और समरूपता"
    },
    "Ratios and Proportions": {
        "chinese": "比例和比例关系",
        "spanish": "Razones y Proporciones",
        "hindi": "अनुपात और समानुपात"
    },
    "Similar Polygons": {
        "chinese": "相似多边形",
        "spanish": "Polígonos Similares",
        "hindi": "समान बहुभुज"
    },
    "Similar Triangles": {
        "chinese": "相似三角形",
        "spanish": "Triángulos Similares",
        "hindi": "समान त्रिभुज"
    },
    "Parallel Lines and Proportional Parts": {
        "chinese": "平行线和比例线段",
        "spanish": "Líneas Paralelas y Partes Proporcionales",
        "hindi": "समानांतर रेखाएं और समानुपाती भाग"
    },
    "Parts of Similar Triangles": {
        "chinese": "相似三角形的部分",
        "spanish": "Partes de Triángulos Similares",
        "hindi": "समान त्रिभुजों के भाग"
    },
    "Similarity Transformations": {
        "chinese": "相似变换",
        "spanish": "Transformaciones de Similitud",
        "hindi": "समानता परिवर्तन"
    },
    "Scale Drawings and Models": {
        "chinese": "比例图和模型",
        "spanish": "Dibujos y Modelos a Escala",
        "hindi": "स्केल ड्राइंग और मॉडल"
    },
    "Fractals and Self-Similarity": {
        "chinese": "分形和自相似性",
        "spanish": "Fractales y Autosimilitud",
        "hindi": "भग्न और आत्म-समानता"
    },
    "Geometric Mean": {
        "chinese": "几何平均数",
        "spanish": "Media Geométrica",
        "hindi": "ज्यामितीय माध्य"
    },
    "The Pythagorean Theorem and Its Converse": {
        "chinese": "勾股定理及其逆定理",
        "spanish": "Teorema de Pitágoras y su Inverso",
        "hindi": "पाइथागोरस प्रमेय और इसका व्युत्क्रम"
    },
    "Special Right Triangles": {
        "chinese": "特殊直角三角形",
        "spanish": "Triángulos Rectángulos Especiales",
        "hindi": "विशेष समकोण त्रिभुज"
    },
    "Trigonometry": {
        "chinese": "三角函数",
        "spanish": "Trigonometría",
        "hindi": "त्रिकोणमिति"
    },
    "Angles of Elevation and Depression": {
        "chinese": "仰角和俯角",
        "spanish": "Ángulos de Elevación y Depresión",
        "hindi": "ऊंचाई और अवनति कोण"
    },
    "The Law of Sines and Cosines": {
        "chinese": "正弦定理和余弦定理",
        "spanish": "Ley de Senos y Cosenos",
        "hindi": "साइन और कोसाइन का नियम"
    },
    "Vectors": {
        "chinese": "向量",
        "spanish": "Vectores",
        "hindi": "सदिश"
    },
    "Polar Coordinates and Complex Numbers": {
        "chinese": "极坐标和复数",
        "spanish": "Coordenadas Polares y Números Complejos",
        "hindi": "ध्रुवीय निर्देशांक और जटिल संख्याएं"
    },
    "Reflections": {
        "chinese": "反射",
        "spanish": "Reflexiones",
        "hindi": "प्रतिबिम्ब"
    },
    "Translations": {
        "chinese": "平移",
        "spanish": "Traslaciones",
        "hindi": "अनुवाद"
    },
    "Rotations": {
        "chinese": "旋转",
        "spanish": "Rotaciones",
        "hindi": "घूर्णन"
    },
    "Compositions of Transformations": {
        "chinese": "变换的组合",
        "spanish": "Composiciones de Transformaciones",
        "hindi": "परिवर्तनों की रचना"
    },
    "Symmetry": {
        "chinese": "对称性",
        "spanish": "Simetría",
        "hindi": "समरूपता"
    },
    "Dilations": {
        "chinese": "扩张",
        "spanish": "Dilataciones",
        "hindi": "फैलाव"
    },
    "Transformations in the Coordinate Plane": {
        "chinese": "坐标平面中的变换",
        "spanish": "Transformaciones en el Plano Coordinado",
        "hindi": "समन्वय तल में परिवर्तन"
    },

    # PHYSICS LESSONS (120+ titles)
    "Physical Quantities & Units": {
        "chinese": "物理量和单位",
        "spanish": "Cantidades Físicas y Unidades",
        "hindi": "भौतिक मात्राएं और इकाइयां"
    },
    "SI System & Prefixes": {
        "chinese": "国际单位制和前缀",
        "spanish": "Sistema SI y Prefijos",
        "hindi": "SI प्रणाली और उपसर्ग"
    },
    "Scalars vs Vectors": {
        "chinese": "标量和矢量",
        "spanish": "Escalares vs Vectores",
        "hindi": "स्केलर और सदिश"
    },
    "Accuracy Precision & Significant Figures": {
        "chinese": "准确度、精确度和有效数字",
        "spanish": "Exactitud, Precisión y Cifras Significativas",
        "hindi": "सटीकता, परिशुद्धता और महत्वपूर्ण अंक"
    },
    "Dimensional Analysis": {
        "chinese": "量纲分析",
        "spanish": "Análisis Dimensional",
        "hindi": "आयामी विश्लेषण"
    },
    "Measurement Uncertainty & Error Analysis": {
        "chinese": "测量不确定性和误差分析",
        "spanish": "Incertidumbre de Medición y Análisis de Errores",
        "hindi": "मापन अनिश्चितता और त्रुटि विश्लेषण"
    },
    "Electric Charge & Coulomb's Law": {
        "chinese": "电荷和库伦定律",
        "spanish": "Carga Eléctrica y Ley de Coulomb",
        "hindi": "विद्युत आवेश और कूलम्ब का नियम"
    },
    "Electric Field & Potential": {
        "chinese": "电场和电势",
        "spanish": "Campo Eléctrico y Potencial",
        "hindi": "विद्युत क्षेत्र और संभावना"
    },
    "Capacitance": {
        "chinese": "电容",
        "spanish": "Capacitancia",
        "hindi": "समाई"
    },
    "Current Resistance & Ohm's Law": {
        "chinese": "电流、电阻和欧姆定律",
        "spanish": "Corriente, Resistencia y Ley de Ohm",
        "hindi": "करंट, प्रतिरोध और ओम का नियम"
    },
    "DC Circuits & Kirchhoff's Laws": {
        "chinese": "直流电路和基尔霍夫定律",
        "spanish": "Circuitos de CC y Leyes de Kirchhoff",
        "hindi": "डीसी सर्किट और किरचॉफ के नियम"
    },
    "Magnetic Fields & Forces": {
        "chinese": "磁场和磁力",
        "spanish": "Campos Magnéticos y Fuerzas",
        "hindi": "चुंबकीय क्षेत्र और बल"
    },
    "Electromagnetic Induction": {
        "chinese": "电磁感应",
        "spanish": "Inducción Electromagnética",
        "hindi": "विद्युत चुंबकीय प्रेरण"
    },
    "Alternating Current (AC) Circuits": {
        "chinese": "交流电路",
        "spanish": "Circuitos de Corriente Alterna (CA)",
        "hindi": "प्रत्यावर्ती धारा (एसी) सर्किट"
    },
    "Maxwell's Equations (introductory)": {
        "chinese": "麦克斯韦方程组（介绍）",
        "spanish": "Ecuaciones de Maxwell (Introductorio)",
        "hindi": "मैक्सवेल के समीकरण (परिचयात्मक)"
    },
    "Photoelectric Effect": {
        "chinese": "光电效应",
        "spanish": "Efecto Fotoeléctrico",
        "hindi": "प्रकाश विद्युत प्रभाव"
    },
    "Atomic Models": {
        "chinese": "原子模型",
        "spanish": "Modelos Atómicos",
        "hindi": "परमाणु मॉडल"
    },
    "Nuclear Physics (fission fusion decay)": {
        "chinese": "核物理学（裂变、聚变、衰变）",
        "spanish": "Física Nuclear (Fisión, Fusión, Desintegración)",
        "hindi": "परमाणु भौतिकी (विखंडन, संलयन, क्षय)"
    },
    "Relativity (special relativity basics)": {
        "chinese": "相对论（狭义相对论基础）",
        "spanish": "Relatividad (Conceptos Básicos de Relatividad Especial)",
        "hindi": "सापेक्षता (विशेष सापेक्षता मूल बातें)"
    },
    "Quantum Mechanics (wavefunctions uncertainty principle)": {
        "chinese": "量子力学（波函数、不确定性原理）",
        "spanish": "Mecánica Cuántica (Funciones de Onda, Principio de Incertidumbre)",
        "hindi": "क्वांटम यांत्रिकी (तरंग कार्य, अनिश्चितता सिद्धांत)"
    },
    "Particle Physics & Standard Model": {
        "chinese": "粒子物理学和标准模型",
        "spanish": "Física de Partículas y Modelo Estándar",
        "hindi": "कण भौतिकी और मानक मॉडल"
    },
    "Distance Displacement Speed Velocity": {
        "chinese": "距离、位移、速率和速度",
        "spanish": "Distancia, Desplazamiento, Rapidez y Velocidad",
        "hindi": "दूरी, विस्थापन, गति और वेग"
    },
    "Acceleration": {
        "chinese": "加速度",
        "spanish": "Aceleración",
        "hindi": "त्वरण"
    },
    "Graphical Analysis of Motion": {
        "chinese": "运动的图形分析",
        "spanish": "Análisis Gráfico del Movimiento",
        "hindi": "गति का ग्राफिकल विश्लेषण"
    },
    "Equations of Motion (constant acceleration)": {
        "chinese": "运动方程（恒定加速度）",
        "spanish": "Ecuaciones de Movimiento (Aceleración Constante)",
        "hindi": "गति के समीकरण (निरंतर त्वरण)"
    },
    "Free Fall & Projectile Motion": {
        "chinese": "自由落体和抛体运动",
        "spanish": "Caída Libre y Movimiento Proyectil",
        "hindi": "मुक्त पतन और प्रक्षेप्य गति"
    },
    "Relative Motion & Reference Frames": {
        "chinese": "相对运动和参考系",
        "spanish": "Movimiento Relativo y Marcos de Referencia",
        "hindi": "सापेक्ष गति और संदर्भ फ्रेम"
    },
    "Force & Interaction": {
        "chinese": "力和相互作用",
        "spanish": "Fuerza e Interacción",
        "hindi": "बल और अंतःक्रिया"
    },
    "Newton's First Law": {
        "chinese": "牛顿第一定律",
        "spanish": "Primera Ley de Newton",
        "hindi": "न्यूटन का पहला नियम"
    },
    "Newton's Second Law (F = ma)": {
        "chinese": "牛顿第二定律（F = ma）",
        "spanish": "Segunda Ley de Newton (F = ma)",
        "hindi": "न्यूटन का दूसरा नियम (F = ma)"
    },
    "Newton's Third Law": {
        "chinese": "牛顿第三定律",
        "spanish": "Tercera Ley de Newton",
        "hindi": "न्यूटन का तीसरा नियम"
    },
    "Friction & Tension": {
        "chinese": "摩擦力和张力",
        "spanish": "Fricción y Tensión",
        "hindi": "घर्षण और तनाव"
    },
    "Normal Force & Inclined Planes": {
        "chinese": "正常力和斜面",
        "spanish": "Fuerza Normal y Planos Inclinados",
        "hindi": "सामान्य बल और झुके हुए समतल"
    },
    "Circular Motion & Centripetal Force": {
        "chinese": "圆周运动和向心力",
        "spanish": "Movimiento Circular y Fuerza Centrípeta",
        "hindi": "परिपत्र गति और अभिकेंद्र बल"
    },
    "Non-Inertial Frames & Pseudo-Forces": {
        "chinese": "非惯性参考系和伪力",
        "spanish": "Marcos No Inerciales y Pseudo-Fuerzas",
        "hindi": "गैर-जड़ता संदर्भ फ्रेम और छद्म-बल"
    },
    "Work & Energy Transfer": {
        "chinese": "功和能量转移",
        "spanish": "Trabajo y Transferencia de Energía",
        "hindi": "कार्य और ऊर्जा हस्तांतरण"
    },
    "Kinetic Energy & Potential Energy": {
        "chinese": "动能和势能",
        "spanish": "Energía Cinética y Energía Potencial",
        "hindi": "गतिज ऊर्जा और स्थितिज ऊर्जा"
    },
    "Conservation of Energy": {
        "chinese": "能量守恒",
        "spanish": "Conservación de la Energía",
        "hindi": "ऊर्जा संरक्षण"
    },
    "Power & Efficiency": {
        "chinese": "功率和效率",
        "spanish": "Potencia y Eficiencia",
        "hindi": "शक्ति और दक्षता"
    },
    "Work-Energy Theorem": {
        "chinese": "功能定理",
        "spanish": "Teorema del Trabajo-Energía",
        "hindi": "कार्य-ऊर्जा प्रमेय"
    },
    "Conservative vs. Non-Conservative Forces": {
        "chinese": "保守力和非保守力",
        "spanish": "Fuerzas Conservativas vs. No Conservativas",
        "hindi": "रूढ़िवादी बनाम गैर-रूढ़िवादी बल"
    },
    "Linear Momentum": {
        "chinese": "线性动量",
        "spanish": "Momento Lineal",
        "hindi": "रैखिक संवेग"
    },
    "Impulse": {
        "chinese": "冲量",
        "spanish": "Impulso",
        "hindi": "आवेग"
    },
    "Conservation of Momentum": {
        "chinese": "动量守恒",
        "spanish": "Conservación del Momento",
        "hindi": "चेतना का संरक्षण"
    },
    "Elastic & Inelastic Collisions": {
        "chinese": "弹性碰撞和非弹性碰撞",
        "spanish": "Colisiones Elásticas e Inelásticas",
        "hindi": "लोचदार और अप्लास्टिक टकराव"
    },
    "Center of Mass": {
        "chinese": "质心",
        "spanish": "Centro de Masa",
        "hindi": "द्रव्यमान का केंद्र"
    },
    "Rocket Propulsion": {
        "chinese": "火箭推进",
        "spanish": "Propulsión de Cohetes",
        "hindi": "रॉकेट प्रणोदन"
    },
    "Newton's Law of Gravitation": {
        "chinese": "万有引力定律",
        "spanish": "Ley de Gravitación Universal de Newton",
        "hindi": "न्यूटन का गुरुत्वाकर्षण नियम"
    },
    "Gravitational Field Strength": {
        "chinese": "重力场强度",
        "spanish": "Intensidad del Campo Gravitacional",
        "hindi": "गुरुत्वाकर्षण क्षेत्र की शक्ति"
    },
    "Orbital Motion": {
        "chinese": "轨道运动",
        "spanish": "Movimiento Orbital",
        "hindi": "कक्षीय गति"
    },
    "Satellite Motion": {
        "chinese": "卫星运动",
        "spanish": "Movimiento de Satélites",
        "hindi": "उपग्रह गति"
    },
    "Escape Velocity": {
        "chinese": "逃逸速度",
        "spanish": "Velocidad de Escape",
        "hindi": "पलायन वेग"
    },
    "Kepler's Laws": {
        "chinese": "开普勒定律",
        "spanish": "Leyes de Kepler",
        "hindi": "केपलर के नियम"
    },
    "Simple Harmonic Motion (SHM)": {
        "chinese": "简谐运动（SHM）",
        "spanish": "Movimiento Armónico Simple (MAS)",
        "hindi": "सरल हार्मोनिक गति (SHM)"
    },
    "Period Frequency Amplitude": {
        "chinese": "周期、频率和振幅",
        "spanish": "Período, Frecuencia y Amplitud",
        "hindi": "अवधि, आवृत्ति और आयाम"
    },
    "Energy in SHM": {
        "chinese": "简谐运动中的能量",
        "spanish": "Energía en el Movimiento Armónico Simple",
        "hindi": "SHM में ऊर्जा"
    },
    "Wave Properties (wavelength speed frequency)": {
        "chinese": "波的性质（波长、速度、频率）",
        "spanish": "Propiedades de Ondas (Longitud de Onda, Rapidez, Frecuencia)",
        "hindi": "तरंग गुण (तरंग दैर्ध्य, गति, आवृत्ति)"
    },
    "Wave Superposition & Interference": {
        "chinese": "波的叠加和干涉",
        "spanish": "Superposición e Interferencia de Ondas",
        "hindi": "तरंग अध्यारोपण और व्यतिकरण"
    },
    "Standing Waves & Resonance": {
        "chinese": "驻波和共振",
        "spanish": "Ondas Estacionarias y Resonancia",
        "hindi": "स्थायी तरंगें और अनुनाद"
    },
    "Doppler Effect": {
        "chinese": "多普勒效应",
        "spanish": "Efecto Doppler",
        "hindi": "डॉप्लर प्रभाव"
    },
    "Wave-Particle Duality (introductory)": {
        "chinese": "波粒二象性（介绍）",
        "spanish": "Dualidad Onda-Partícula (Introductorio)",
        "hindi": "तरंग-कण द्वैत (परिचयात्मक)"
    },
    "Nature of Sound Waves": {
        "chinese": "声波的性质",
        "spanish": "Naturaleza de las Ondas de Sonido",
        "hindi": "ध्वनि तरंगों की प्रकृति"
    },
    "Speed of Sound": {
        "chinese": "声速",
        "spanish": "Velocidad del Sonido",
        "hindi": "ध्वनि की गति"
    },
    "Intensity & Loudness": {
        "chinese": "强度和响度",
        "spanish": "Intensidad y Sonoridad",
        "hindi": "तीव्रता और ज़ोर"
    },
    "Pitch & Frequency": {
        "chinese": "音高和频率",
        "spanish": "Tono y Frecuencia",
        "hindi": "पिच और आवृत्ति"
    },
    "Resonance in Air Columns": {
        "chinese": "气柱共鸣",
        "spanish": "Resonancia en Columnas de Aire",
        "hindi": "वायु स्तंभ में अनुनाद"
    },
    "Beats & Harmonics": {
        "chinese": "拍频和谐波",
        "spanish": "Pulsaciones y Armónicos",
        "hindi": "धड़कन और हार्मोनिक्स"
    },
    "Reflection & Refraction": {
        "chinese": "反射和折射",
        "spanish": "Reflexión y Refracción",
        "hindi": "प्रतिबिंब और अपवर्तन"
    },
    "Lenses & Mirrors": {
        "chinese": "透镜和镜子",
        "spanish": "Lentes y Espejos",
        "hindi": "लेंस और दर्पण"
    },
    "Total Internal Reflection": {
        "chinese": "全内反射",
        "spanish": "Reflexión Interna Total",
        "hindi": "पूर्ण आंतरिक प्रतिबिंब"
    },
    "Optical Instruments": {
        "chinese": "光学仪器",
        "spanish": "Instrumentos Ópticos",
        "hindi": "ऑप्टिकल उपकरण"
    },
    "Diffraction & Interference": {
        "chinese": "衍射和干涉",
        "spanish": "Difracción e Interferencia",
        "hindi": "विवर्तन और व्यतिकरण"
    },
    "Polarization": {
        "chinese": "偏振",
        "spanish": "Polarización",
        "hindi": "ध्रुवीकरण"
    }
}

def generate_translation_outputs():
    """Generate the three separate translation lists."""
    
    # Extract and sort unique lesson titles
    all_titles = sorted(set(TRANSLATIONS.keys()))
    
    # Create the three output dictionaries
    chinese_output = {}
    spanish_output = {}
    hindi_output = {}
    
    for title in all_titles:
        translations = TRANSLATIONS[title]
        chinese_output[title] = translations["chinese"]
        spanish_output[title] = translations["spanish"]
        hindi_output[title] = translations["hindi"]
    
    # Print results
    print("=" * 80)
    print("CHINESE (SIMPLIFIED) TRANSLATIONS")
    print("=" * 80)
    for title, translation in chinese_output.items():
        print(f'"{title}": "{translation}"')
    
    print("\n" + "=" * 80)
    print("SPANISH TRANSLATIONS")
    print("=" * 80)
    for title, translation in spanish_output.items():
        print(f'"{title}": "{translation}"')
    
    print("\n" + "=" * 80)
    print("HINDI TRANSLATIONS")
    print("=" * 80)
    for title, translation in hindi_output.items():
        print(f'"{title}": "{translation}"')
    
    # Return a summary
    return {
        "total_titles": len(all_titles),
        "chinese_translations": chinese_output,
        "spanish_translations": spanish_output,
        "hindi_translations": hindi_output
    }

if __name__ == "__main__":
    result = generate_translation_outputs()
    print(f"\n{'=' * 80}")
    print(f"SUMMARY: Generated {result['total_titles']} translations in 3 languages")
    print(f"{'=' * 80}")
