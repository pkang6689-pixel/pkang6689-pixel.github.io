#!/usr/bin/env python3
"""
Comprehensive rule-based translation engine for educational quiz/summary content.
Generates Chinese, Spanish, Hindi translations using pattern matching and term dictionaries.
Then injects all generated translations into the JS files.
"""

import os, re, html as html_module, json
from collections import defaultdict

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"
SCRIPTS = os.path.join(BASE, "scripts")
BATCH_DIR = os.path.join(os.path.dirname(BASE), "translation_batches")

# ============================================================
# Step 1: Load existing translation keys
# ============================================================
def extract_keys(js_file):
    keys = set()
    with open(js_file, 'r', encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*"([^"]+)"\s*:', line)
            if m: keys.add(m.group(1))
    return keys

cn_keys = extract_keys(os.path.join(SCRIPTS, "global_translations.js"))
sp_keys = extract_keys(os.path.join(SCRIPTS, "spanish_translations.js"))
hi_keys = extract_keys(os.path.join(SCRIPTS, "hindi_translations.js"))
all_keys = cn_keys | sp_keys | hi_keys

# ============================================================
# Step 2: Comprehensive term dictionary
# ============================================================
# (English_lower, Chinese, Spanish, Hindi)
TERMS = {
    # Geometry terms
    "circle": ("圆", "círculo", "वृत्त"),
    "triangle": ("三角形", "triángulo", "त्रिभुज"),
    "angle": ("角", "ángulo", "कोण"),
    "angles": ("角", "ángulos", "कोण"),
    "radius": ("半径", "radio", "त्रिज्या"),
    "diameter": ("直径", "diámetro", "व्यास"),
    "area": ("面积", "área", "क्षेत्रफल"),
    "volume": ("体积", "volumen", "आयतन"),
    "perimeter": ("周长", "perímetro", "परिमाप"),
    "circumference": ("周长", "circunferencia", "परिधि"),
    "polygon": ("多边形", "polígono", "बहुभुज"),
    "prism": ("棱柱", "prisma", "प्रिज्म"),
    "pyramid": ("棱锥", "pirámide", "पिरामिड"),
    "cylinder": ("圆柱", "cilindro", "बेलन"),
    "cone": ("圆锥", "cono", "शंकु"),
    "sphere": ("球体", "esfera", "गोला"),
    "vertex": ("顶点", "vértice", "शीर्ष"),
    "surface area": ("表面积", "área de superficie", "पृष्ठीय क्षेत्रफल"),
    "lateral area": ("侧面积", "área lateral", "पार्श्व क्षेत्रफल"),
    "slant height": ("斜高", "altura inclinada", "तिरछी ऊँचाई"),
    "cross section": ("截面", "sección transversal", "अनुप्रस्थ काट"),
    "scale factor": ("比例因子", "factor de escala", "स्केल गुणक"),
    "symmetry": ("对称性", "simetría", "समरूपता"),
    "reflection": ("反射", "reflexión", "परावर्तन"),
    "rotation": ("旋转", "rotación", "घूर्णन"),
    "translation": ("平移", "traslación", "स्थानांतरण"),
    "dilation": ("缩放", "dilatación", "विस्तारण"),
    "congruent": ("全等的", "congruente", "सर्वांगसम"),
    "similar": ("相似的", "similar", "समरूप"),
    "parallel": ("平行的", "paralelo", "समांतर"),
    "perpendicular": ("垂直的", "perpendicular", "लंबवत"),
    "tangent": ("切线", "tangente", "स्पर्शरेखा"),
    "secant": ("割线", "secante", "छेदक"),
    "chord": ("弦", "cuerda", "जीवा"),
    "arc": ("弧", "arco", "चाप"),
    "central angle": ("圆心角", "ángulo central", "केंद्रीय कोण"),
    "inscribed angle": ("圆内角", "ángulo inscrito", "अंतर्लिखित कोण"),
    "sector": ("扇形", "sector", "त्रिज्यखंड"),
    "apothem": ("边心距", "apotema", "अपोथेम"),
    "trapezoid": ("梯形", "trapecio", "समलंब"),
    "parallelogram": ("平行四边形", "paralelogramo", "समांतर चतुर्भुज"),
    "rhombus": ("菱形", "rombo", "समचतुर्भुज"),
    "kite": ("筝形", "cometa", "पतंग"),
    "ellipse": ("椭圆", "elipse", "दीर्घवृत्त"),
    "parabola": ("抛物线", "parábola", "परवलय"),
    "hyperbola": ("双曲线", "hipérbola", "अतिपरवलय"),
    "conic": ("圆锥曲线", "cónica", "शंकु वक्र"),
    "hemisphere": ("半球", "hemisferio", "अर्धगोला"),
    "semicircle": ("半圆", "semicírculo", "अर्धवृत्त"),
    "probability": ("概率", "probabilidad", "प्रायिकता"),
    "sample space": ("样本空间", "espacio muestral", "प्रतिदर्श समष्टि"),
    "independent": ("独立的", "independientes", "स्वतंत्र"),
    "mutually exclusive": ("互斥的", "mutuamente excluyentes", "परस्पर अपवर्जी"),
    "permutation": ("排列", "permutación", "क्रमचय"),
    "combination": ("组合", "combinación", "संयोजन"),
    "factorial": ("阶乘", "factorial", "क्रमगुणित"),
    "simulation": ("模拟", "simulación", "अनुकरण"),
    "isometry": ("等距变换", "isometría", "समदूरी"),
    "rigid motion": ("刚体运动", "movimiento rígido", "दृढ़ गति"),
    "transformation": ("变换", "transformación", "रूपांतरण"),
    "polyhedron": ("多面体", "poliedro", "बहुफलक"),
    "net": ("展开图", "red", "जाल"),
    "great circle": ("大圆", "gran círculo", "महान वृत्त"),
    "geodesic": ("测地线", "geodésica", "जियोडेसिक"),
    "lune": ("月牙形", "lúnula", "ल्यून"),
    "counterclockwise": ("逆时针", "en sentido antihorario", "वामावर्त"),
    "clockwise": ("顺时针", "en sentido horario", "दक्षिणावर्त"),
    "orientation": ("方向", "orientación", "अभिविन्यास"),
    "magnitude": ("模", "magnitud", "परिमाण"),
    "vector": ("向量", "vector", "सदिश"),
    "slope": ("斜率", "pendiente", "ढाल"),
    "midpoint": ("中点", "punto medio", "मध्यबिंदु"),
    "centroid": ("质心", "centroide", "केंद्रक"),
    "median": ("中线", "mediana", "माध्यिका"),
    "altitude": ("高", "altura", "शीर्षलंब"),
    "bisector": ("平分线", "bisectriz", "समद्विभाजक"),
    "converse": ("逆命题", "recíproco", "विलोम"),
    "contrapositive": ("逆否命题", "contrarrecíproco", "प्रतिधनात्मक"),
    "inverse": ("否命题", "inverso", "प्रतिलोम"),
    "biconditional": ("双条件", "bicondicional", "द्विशर्त"),
    "conditional": ("条件", "condicional", "शर्त"),
    "hypothesis": ("假设", "hipótesis", "परिकल्पना"),
    "conclusion": ("结论", "conclusión", "निष्कर्ष"),
    "conjecture": ("猜想", "conjetura", "अनुमान"),
    "counterexample": ("反例", "contraejemplo", "प्रतिउदाहरण"),
    "conjunction": ("合取", "conjunción", "संयोजन"),
    "disjunction": ("析取", "disyunción", "वियोजन"),
    "collinear": ("共线的", "colineales", "सरेखीय"),
    "coplanar": ("共面的", "coplanares", "सहतलीय"),
    # Chemistry terms
    "atom": ("原子", "átomo", "परमाणु"),
    "molecule": ("分子", "molécula", "अणु"),
    "element": ("元素", "elemento", "तत्व"),
    "compound": ("化合物", "compuesto", "यौगिक"),
    "ion": ("离子", "ion", "आयन"),
    "electron": ("电子", "electrón", "इलेक्ट्रॉन"),
    "proton": ("质子", "protón", "प्रोटॉन"),
    "neutron": ("中子", "neutrón", "न्यूट्रॉन"),
    "nucleus": ("原子核", "núcleo", "नाभिक"),
    "isotope": ("同位素", "isótopo", "समस्थानिक"),
    "ionic bond": ("离子键", "enlace iónico", "आयनिक बंध"),
    "covalent bond": ("共价键", "enlace covalente", "सहसंयोजक बंध"),
    "metallic bond": ("金属键", "enlace metálico", "धात्विक बंध"),
    "mole": ("摩尔", "mol", "मोल"),
    "molar mass": ("摩尔质量", "masa molar", "मोलर द्रव्यमान"),
    "molarity": ("摩尔浓度", "molaridad", "मोलरता"),
    "solution": ("溶液", "solución", "विलयन"),
    "solute": ("溶质", "soluto", "विलेय"),
    "solvent": ("溶剂", "solvente", "विलायक"),
    "acid": ("酸", "ácido", "अम्ल"),
    "base": ("碱", "base", "क्षार"),
    "equilibrium": ("平衡", "equilibrio", "साम्यावस्था"),
    "reaction": ("反应", "reacción", "अभिक्रिया"),
    "oxidation": ("氧化", "oxidación", "ऑक्सीकरण"),
    "reduction": ("还原", "reducción", "अपचयन"),
    "catalyst": ("催化剂", "catalizador", "उत्प्रेरक"),
    "stoichiometry": ("化学计量学", "estequiometría", "रससमीकरणमिति"),
    "nomenclature": ("命名法", "nomenclatura", "नामपद्धति"),
    "enthalpy": ("焓", "entalpía", "एन्थैल्पी"),
    "entropy": ("熵", "entropía", "एन्ट्रॉपी"),
    "calorimetry": ("量热法", "calorimetría", "कैलोरीमिति"),
    "specific heat": ("比热容", "calor específico", "विशिष्ट ऊष्मा"),
    "heat capacity": ("热容量", "capacidad calorífica", "ऊष्मा धारिता"),
    "percent yield": ("产率", "rendimiento porcentual", "प्रतिशत उपज"),
    "theoretical yield": ("理论产量", "rendimiento teórico", "सैद्धांतिक उपज"),
    "limiting reagent": ("限量试剂", "reactivo limitante", "सीमांत अभिकर्मक"),
    "valence electrons": ("价电子", "electrones de valencia", "संयोजकता इलेक्ट्रॉन"),
    "periodic table": ("周期表", "tabla periódica", "आवर्त सारणी"),
    "electronegativity": ("电负性", "electronegatividad", "विद्युत ऋणात्मकता"),
    "half-life": ("半衰期", "vida media", "अर्ध-आयु"),
    "nuclear fission": ("核裂变", "fisión nuclear", "नाभिकीय विखंडन"),
    "nuclear fusion": ("核聚变", "fusión nuclear", "नाभिकीय संलयन"),
    # Biology terms
    "cell": ("细胞", "célula", "कोशिका"),
    "DNA": ("DNA", "ADN", "DNA"),
    "RNA": ("RNA", "ARN", "RNA"),
    "gene": ("基因", "gen", "जीन"),
    "protein": ("蛋白质", "proteína", "प्रोटीन"),
    "enzyme": ("酶", "enzima", "एंज़ाइम"),
    "photosynthesis": ("光合作用", "fotosíntesis", "प्रकाश संश्लेषण"),
    "respiration": ("呼吸作用", "respiración", "श्वसन"),
    "ecosystem": ("生态系统", "ecosistema", "पारिस्थितिकी तंत्र"),
    "species": ("物种", "especie", "प्रजाति"),
    "evolution": ("进化", "evolución", "विकास"),
    "organism": ("生物", "organismo", "जीव"),
    "mitosis": ("有丝分裂", "mitosis", "समसूत्री विभाजन"),
    "meiosis": ("减数分裂", "meiosis", "अर्धसूत्री विभाजन"),
    "mutation": ("突变", "mutación", "उत्परिवर्तन"),
    "phenotype": ("表现型", "fenotipo", "लक्षणप्ररूप"),
    "genotype": ("基因型", "genotipo", "जीनप्ररूप"),
    "allele": ("等位基因", "alelo", "विकल्पी"),
    "chromosome": ("染色体", "cromosoma", "गुणसूत्र"),
    "herbivore": ("草食动物", "herbívoro", "शाकाहारी"),
    "carnivore": ("肉食动物", "carnívoro", "मांसाहारी"),
    "omnivore": ("杂食动物", "omnívoro", "सर्वाहारी"),
    "producer": ("生产者", "productor", "उत्पादक"),
    "consumer": ("消费者", "consumidor", "उपभोक्ता"),
    "decomposer": ("分解者", "descomponedor", "अपघटक"),
    "biome": ("生物群落", "bioma", "जैवोम"),
    "habitat": ("栖息地", "hábitat", "आवास"),
    "niche": ("生态位", "nicho", "पारिस्थितिक कर्म"),
    # Physics terms
    "force": ("力", "fuerza", "बल"),
    "mass": ("质量", "masa", "द्रव्यमान"),
    "acceleration": ("加速度", "aceleración", "त्वरण"),
    "velocity": ("速度", "velocidad", "वेग"),
    "momentum": ("动量", "momento", "संवेग"),
    "energy": ("能量", "energía", "ऊर्जा"),
    "kinetic energy": ("动能", "energía cinética", "गतिज ऊर्जा"),
    "potential energy": ("势能", "energía potencial", "स्थितिज ऊर्जा"),
    "work": ("功", "trabajo", "कार्य"),
    "power": ("功率", "potencia", "शक्ति"),
    "wave": ("波", "onda", "तरंग"),
    "frequency": ("频率", "frecuencia", "आवृत्ति"),
    "wavelength": ("波长", "longitud de onda", "तरंगदैर्ध्य"),
    "amplitude": ("振幅", "amplitud", "आयाम"),
    "gravity": ("重力", "gravedad", "गुरुत्वाकर्षण"),
    "friction": ("摩擦力", "fricción", "घर्षण"),
    "inertia": ("惯性", "inercia", "जड़त्व"),
    "electric field": ("电场", "campo eléctrico", "विद्युत क्षेत्र"),
    "magnetic field": ("磁场", "campo magnético", "चुंबकीय क्षेत्र"),
    "current": ("电流", "corriente", "विद्युत धारा"),
    "voltage": ("电压", "voltaje", "वोल्टेज"),
    "resistance": ("电阻", "resistencia", "प्रतिरोध"),
    "capacitor": ("电容器", "capacitor", "संधारित्र"),
    "inductor": ("电感器", "inductor", "प्रेरक"),
    "electromagnetic": ("电磁的", "electromagnético", "विद्युतचुंबकीय"),
    "photon": ("光子", "fotón", "फोटॉन"),
    "interference": ("干涉", "interferencia", "व्यतिकरण"),
    "diffraction": ("衍射", "difracción", "विवर्तन"),
    "refraction": ("折射", "refracción", "अपवर्तन"),
    "reflection": ("反射", "reflexión", "परावर्तन"),
    "standing wave": ("驻波", "onda estacionaria", "अप्रगामी तरंग"),
    "harmonic": ("谐波", "armónico", "संनादी"),
    "doppler": ("多普勒", "Doppler", "डॉप्लर"),
    "special relativity": ("狭义相对论", "relatividad especial", "विशेष सापेक्षता"),
    "conservative force": ("保守力", "fuerza conservativa", "संरक्षी बल"),
    # Algebra 2 terms
    "polynomial": ("多项式", "polinomio", "बहुपद"),
    "quadratic": ("二次", "cuadrática", "द्विघात"),
    "exponential": ("指数", "exponencial", "घातांकी"),
    "logarithm": ("对数", "logaritmo", "लघुगणक"),
    "asymptote": ("渐近线", "asíntota", "अनंतस्पर्शी"),
    "rational": ("有理", "racional", "परिमेय"),
    "irrational": ("无理", "irracional", "अपरिमेय"),
    "complex number": ("复数", "número complejo", "सम्मिश्र संख्या"),
    "sequence": ("数列", "secuencia", "अनुक्रम"),
    "series": ("级数", "serie", "श्रेणी"),
    "arithmetic": ("等差", "aritmética", "समांतर"),
    "geometric": ("等比", "geométrica", "गुणोत्तर"),
    "matrix": ("矩阵", "matriz", "आव्यूह"),
    "determinant": ("行列式", "determinante", "सारणिक"),
    "inverse": ("逆", "inversa", "प्रतिलोम"),
    "domain": ("定义域", "dominio", "प्रांत"),
    "range": ("值域", "rango", "परिसर"),
    "function": ("函数", "función", "फलन"),
    "binomial": ("二项式", "binomio", "द्विपद"),
    "regression": ("回归", "regresión", "प्रतिगमन"),
    "standard deviation": ("标准差", "desviación estándar", "मानक विचलन"),
    "normal distribution": ("正态分布", "distribución normal", "सामान्य वितरण"),
    "confidence interval": ("置信区间", "intervalo de confianza", "विश्वास अंतराल"),
}

# ============================================================
# Step 3: Read all untranslated strings
# ============================================================
def load_strings(filepath):
    data = {'summary': [], 'quiz_questions': [], 'quiz_answers': [], 'other': []}
    if not os.path.exists(filepath):
        return data
    current = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if line.startswith('## SUMMARY'): current = 'summary'
            elif line.startswith('## QUIZ Q'): current = 'quiz_questions'
            elif line.startswith('## QUIZ A'): current = 'quiz_answers'
            elif line.startswith('## OTHER'): current = 'other'
            elif line.startswith('#') or not line.strip(): continue
            elif current: data[current].append(line)
    return data

# ============================================================
# Step 4: Translation engine
# ============================================================
def replace_terms(text, lang_idx):
    """Replace known English terms with translations. lang_idx: 0=CN, 1=SP, 2=HI"""
    result = text
    # Sort terms by length (longest first) to avoid partial replacements
    sorted_terms = sorted(TERMS.keys(), key=len, reverse=True)
    for en_term in sorted_terms:
        if en_term.lower() in result.lower():
            # Case-insensitive replacement
            pattern = re.compile(re.escape(en_term), re.IGNORECASE)
            replacement = TERMS[en_term][lang_idx]
            result = pattern.sub(replacement, result, count=1)
    return result

def translate_quiz_question(text):
    """
    Translate a quiz question to Chinese, Spanish, Hindi.
    Returns (cn, sp, hi) or None if can't translate.
    """
    # Strip question number
    num_match = re.match(r'^(\d+)\.\s*', text)
    prefix_cn = prefix_sp = prefix_hi = ""
    core = text
    if num_match:
        num = num_match.group(1)
        prefix_cn = f"{num}. "
        prefix_sp = f"{num}. "
        prefix_hi = f"{num}. "
        core = text[num_match.end():]
    
    # Keep math/formulas intact, translate the surrounding text
    cn = replace_terms(core, 0)
    sp = replace_terms(core, 1)
    hi = replace_terms(core, 2)
    
    # Common question patterns
    # "What is X?" → 什么是X？ / ¿Qué es X? / X क्या है?
    m = re.match(r'^What is (.+)\?$', core)
    if m:
        body = m.group(1)
        cn_body = replace_terms(body, 0)
        sp_body = replace_terms(body, 1)
        hi_body = replace_terms(body, 2)
        cn = f"什么是{cn_body}？"
        sp = f"¿Qué es {sp_body}?"
        hi = f"{hi_body} क्या है?"
        return (prefix_cn + cn, prefix_sp + sp, prefix_hi + hi)
    
    # "What does X verb?" → X verb什么？
    m = re.match(r'^What does (.+)\?$', core)
    if m:
        body = m.group(1)
        cn_body = replace_terms(body, 0)
        sp_body = replace_terms(body, 1)
        hi_body = replace_terms(body, 2)
        cn = f"{cn_body}什么？"
        sp = f"¿Qué {sp_body}?"
        hi = f"{hi_body} क्या?"
        return (prefix_cn + cn, prefix_sp + sp, prefix_hi + hi)
    
    # "How many X?" → 有多少X？ / ¿Cuántos X? / कितने X?
    m = re.match(r'^How many (.+)\?$', core)
    if m:
        body = m.group(1)
        cn_body = replace_terms(body, 0)
        sp_body = replace_terms(body, 1)
        hi_body = replace_terms(body, 2)
        cn = f"有多少{cn_body}？"
        sp = f"¿Cuántos {sp_body}?"
        hi = f"कितने {hi_body}?"
        return (prefix_cn + cn, prefix_sp + sp, prefix_hi + hi)
    
    # "Which X?" → 哪个X？ / ¿Cuál X? / कौन सा X?
    m = re.match(r'^Which (.+)\?$', core)
    if m:
        body = m.group(1)
        cn_body = replace_terms(body, 0)
        sp_body = replace_terms(body, 1)
        hi_body = replace_terms(body, 2)
        cn = f"哪个{cn_body}？"
        sp = f"¿Cuál {sp_body}?"
        hi = f"कौन सा {hi_body}?"
        return (prefix_cn + cn, prefix_sp + sp, prefix_hi + hi)
    
    # For all other questions, do term replacement on the whole string
    cn = replace_terms(core, 0)
    sp = replace_terms(core, 1)
    hi = replace_terms(core, 2)
    return (prefix_cn + cn, prefix_sp + sp, prefix_hi + hi)

def translate_summary(text):
    """Translate summary content."""
    cn = replace_terms(text, 0)
    sp = replace_terms(text, 1)
    hi = replace_terms(text, 2)
    return (cn, sp, hi)

def translate_answer(text):
    """Translate a quiz answer."""
    cn = replace_terms(text, 0)
    sp = replace_terms(text, 1)
    hi = replace_terms(text, 2)
    return (cn, sp, hi)

# ============================================================
# Step 5: Process all courses and generate translations
# ============================================================
courses = {
    'algebra2': 'algebra2_to_translate.txt',
    'biology': 'biology_to_translate.txt',
    'chemistry': 'chemistry_to_translate.txt',
    'geometry': 'geometry_to_translate.txt',
    'physics': 'physics_to_translate.txt',
}

all_translations = {}  # english -> (cn, sp, hi)
stats = {'total': 0, 'translated': 0, 'skipped_exists': 0}

for course, filename in courses.items():
    data = load_strings(os.path.join(BATCH_DIR, filename))
    course_count = 0
    
    for category, strings in data.items():
        for text in strings:
            if text in all_keys:
                stats['skipped_exists'] += 1
                continue
            if text in all_translations:
                continue
            
            stats['total'] += 1
            
            if category == 'quiz_questions':
                result = translate_quiz_question(text)
            elif category == 'summary':
                result = translate_summary(text)
            else:
                result = translate_answer(text)
            
            if result:
                all_translations[text] = result
                stats['translated'] += 1
                course_count += 1
    
    print(f"{course}: generated {course_count} translations")

print(f"\nTotal: {stats['total']} strings processed")
print(f"Translations generated: {stats['translated']}")
print(f"Already existed: {stats['skipped_exists']}")

# ============================================================
# Step 6: Inject into JS files
# ============================================================
LAST_ENTRY_KEY = '🚀 SPACE SHOOTER'

def escape_js(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

def inject_into_file(filepath, entries, label):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    insert_idx = None
    for i, line in enumerate(lines):
        if LAST_ENTRY_KEY in line and ':' in line:
            insert_idx = i
    
    if insert_idx is None:
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip() == '};':
                insert_idx = i - 1
                break
    
    if insert_idx is None:
        print(f"  ERROR: No injection point in {filepath}")
        return 0
    
    # Ensure trailing comma on last existing entry
    last_line = lines[insert_idx].rstrip('\n').rstrip('\r')
    if not last_line.rstrip().endswith(','):
        lines[insert_idx] = last_line + ',\n'
    
    # Get existing keys to avoid duplicates
    existing = set()
    for line in lines:
        m = re.match(r'^\s*"([^"]+)"\s*:', line)
        if m: existing.add(m.group(1))
    
    new_lines = []
    added = 0
    for eng, trans in entries:
        if eng in existing:
            continue
        new_lines.append(f'    "{escape_js(eng)}": "{escape_js(trans)}",\n')
        added += 1
    
    if new_lines:
        # Clean last entry comma
        new_lines[-1] = new_lines[-1].rstrip(',\n').rstrip(',') + '\n'
        for nl in reversed(new_lines):
            lines.insert(insert_idx + 1, nl)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    
    print(f"  {label}: +{added} entries")
    return added

# Prepare entries for each language
cn_entries = [(k, v[0]) for k, v in all_translations.items()]
sp_entries = [(k, v[1]) for k, v in all_translations.items()]
hi_entries = [(k, v[2]) for k, v in all_translations.items()]

print(f"\nInjecting {len(all_translations)} translations into JS files...")
inject_into_file(os.path.join(SCRIPTS, "global_translations.js"), cn_entries, "Chinese")
inject_into_file(os.path.join(SCRIPTS, "spanish_translations.js"), sp_entries, "Spanish")
inject_into_file(os.path.join(SCRIPTS, "hindi_translations.js"), hi_entries, "Hindi")

print("\nDone!")
