#!/usr/bin/env python3
"""
Automated translation generator for educational content.
Uses pattern matching and term dictionaries to generate Chinese, Spanish, Hindi translations.
Handles common quiz question/answer patterns across all courses.
"""

import os, re, json, html as html_module
from collections import defaultdict

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"
SCRIPTS = os.path.join(BASE, "scripts")
BATCH_DIR = os.path.join(os.path.dirname(BASE), "translation_batches")

# ============================================================
# Load existing translation keys for term lookup
# ============================================================
def load_translations(js_file):
    """Load English -> Translation dictionary from JS file."""
    d = {}
    with open(js_file, 'r', encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*"([^"]+)"\s*:\s*"([^"]*)"', line)
            if m:
                d[m.group(1)] = m.group(2)
    return d

print("Loading existing translations...")
cn_dict = load_translations(os.path.join(SCRIPTS, "global_translations.js"))
sp_dict = load_translations(os.path.join(SCRIPTS, "spanish_translations.js"))
hi_dict = load_translations(os.path.join(SCRIPTS, "hindi_translations.js"))
print(f"  CN={len(cn_dict)}, SP={len(sp_dict)}, HI={len(hi_dict)}")

# ============================================================
# Common educational term translations
# ============================================================
TERM_DICT = {
    # Math terms
    "circle": ("圆", "círculo", "वृत्त"),
    "triangle": ("三角形", "triángulo", "त्रिभुज"),
    "angle": ("角", "ángulo", "कोण"),
    "radius": ("半径", "radio", "त्रिज्या"),
    "diameter": ("直径", "diámetro", "व्यास"),
    "area": ("面积", "área", "क्षेत्रफल"),
    "volume": ("体积", "volumen", "आयतन"),
    "perimeter": ("周长", "perímetro", "परिमाप"),
    "circumference": ("圆周", "circunferencia", "परिधि"),
    "polygon": ("多边形", "polígono", "बहुभुज"),
    "prism": ("棱柱", "prisma", "प्रिज्म"),
    "pyramid": ("棱锥", "pirámide", "पिरामिड"),
    "cylinder": ("圆柱", "cilindro", "बेलन"),
    "cone": ("圆锥", "cono", "शंकु"),
    "sphere": ("球", "esfera", "गोला"),
    "vertex": ("顶点", "vértice", "शीर्ष"),
    "edge": ("边", "arista", "किनारा"),
    "face": ("面", "cara", "फलक"),
    "symmetry": ("对称", "simetría", "समरूपता"),
    "reflection": ("反射", "reflexión", "परावर्तन"),
    "rotation": ("旋转", "rotación", "घूर्णन"),
    "translation": ("平移", "traslación", "स्थानांतरण"),
    "dilation": ("缩放", "dilatación", "विस्तारण"),
    "congruent": ("全等", "congruente", "सर्वांगसम"),
    "similar": ("相似", "similar", "समरूप"),
    "parallel": ("平行", "paralelo", "समांतर"),
    "perpendicular": ("垂直", "perpendicular", "लंबवत"),
    "tangent": ("切线", "tangente", "स्पर्शरेखा"),
    "secant": ("割线", "secante", "छेदक रेखा"),
    "chord": ("弦", "cuerda", "जीवा"),
    "arc": ("弧", "arco", "चाप"),
    "sector": ("扇形", "sector", "त्रिज्यखंड"),
    "surface area": ("表面积", "área de superficie", "पृष्ठीय क्षेत्रफल"),
    "lateral area": ("侧面积", "área lateral", "पार्श्व क्षेत्रफल"),
    "slant height": ("斜高", "altura inclinada", "तिरछी ऊंचाई"),
    "cross section": ("截面", "sección transversal", "अनुप्रस्थ काट"),
    "isometry": ("等距变换", "isometría", "समदूरी"),
    "transformation": ("变换", "transformación", "रूपांतरण"),
    "rigid motion": ("刚体运动", "movimiento rígido", "दृढ़ गति"),
    "scale factor": ("比例因子", "factor de escala", "स्केल गुणक"),
    "probability": ("概率", "probabilidad", "प्रायिकता"),
    "sample space": ("样本空间", "espacio muestral", "प्रतिदर्श समष्टि"),
    "independent": ("独立", "independiente", "स्वतंत्र"),
    "mutually exclusive": ("互斥", "mutuamente excluyentes", "परस्पर अपवर्जी"),
    "permutation": ("排列", "permutación", "क्रमचय"),
    "combination": ("组合", "combinación", "संयोजन"),
    "factorial": ("阶乘", "factorial", "क्रमगुणित"),
    "simulation": ("模拟", "simulación", "अनुकरण"),
    "apothem": ("边心距", "apotema", "अपोदम"),
    "trapezoid": ("梯形", "trapecio", "समलंब"),
    "parallelogram": ("平行四边形", "paralelogramo", "समांतर चतुर्भुज"),
    "rhombus": ("菱形", "rombo", "विषमकोण समचतुर्भुज"),
    "kite": ("筝形", "cometa", "पतंग"),
    "ellipse": ("椭圆", "elipse", "दीर्घवृत्त"),
    "parabola": ("抛物线", "parábola", "परवलय"),
    "hyperbola": ("双曲线", "hipérbola", "अतिपरवलय"),
    "conic": ("圆锥曲线", "cónica", "शंकु वक्र"),
    "hemisphere": ("半球", "hemisferio", "अर्धगोला"),
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
    "bond": ("键", "enlace", "बंध"),
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
    "pH": ("pH", "pH", "pH"),
    "equilibrium": ("平衡", "equilibrio", "साम्यावस्था"),
    "reaction": ("反应", "reacción", "अभिक्रिया"),
    "oxidation": ("氧化", "oxidación", "ऑक्सीकरण"),
    "reduction": ("还原", "reducción", "अपचयन"),
    "catalyst": ("催化剂", "catalizador", "उत्प्रेरक"),
    "exothermic": ("放热", "exotérmica", "ऊष्माक्षेपी"),
    "endothermic": ("吸热", "endotérmica", "ऊष्माशोषी"),
    "enthalpy": ("焓", "entalpía", "एन्थैल्पी"),
    "entropy": ("熵", "entropía", "एन्ट्रॉपी"),
    "stoichiometry": ("化学计量", "estequiometría", "रससमीकरणमिति"),
    "nomenclature": ("命名法", "nomenclatura", "नामपद्धति"),
    "valence": ("化合价", "valencia", "संयोजकता"),
    "orbital": ("轨道", "orbital", "कक्षक"),
    "periodic table": ("周期表", "tabla periódica", "आवर्त सारणी"),
    # Biology terms
    "cell": ("细胞", "célula", "कोशिका"),
    "DNA": ("DNA", "ADN", "DNA"),
    "RNA": ("RNA", "ARN", "RNA"),
    "gene": ("基因", "gen", "जीन"),
    "protein": ("蛋白质", "proteína", "प्रोटीन"),
    "enzyme": ("酶", "enzima", "एंजाइम"),
    "photosynthesis": ("光合作用", "fotosíntesis", "प्रकाश संश्लेषण"),
    "respiration": ("呼吸作用", "respiración", "श्वसन"),
    "ecosystem": ("生态系统", "ecosistema", "पारिस्थितिकी तंत्र"),
    "species": ("物种", "especie", "प्रजाति"),
    "evolution": ("进化", "evolución", "विकास"),
    "mutation": ("突变", "mutación", "उत्परिवर्तन"),
    "mitosis": ("有丝分裂", "mitosis", "समसूत्री विभाजन"),
    "meiosis": ("减数分裂", "meiosis", "अर्धसूत्री विभाजन"),
    "organism": ("生物体", "organismo", "जीव"),
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
    "electric field": ("电场", "campo eléctrico", "विद्युत क्षेत्र"),
    "magnetic field": ("磁场", "campo magnético", "चुंबकीय क्षेत्र"),
    "current": ("电流", "corriente", "धारा"),
    "voltage": ("电压", "voltaje", "वोल्टेज"),
    "resistance": ("电阻", "resistencia", "प्रतिरोध"),
    "gravity": ("重力", "gravedad", "गुरुत्वाकर्षण"),
    "friction": ("摩擦力", "fricción", "घर्षण"),
    "inertia": ("惯性", "inercia", "जड़त्व"),
}

# ============================================================
# Load per-course untranslated strings
# ============================================================
def load_course_strings(filename):
    """Load strings from a to_translate.txt file."""
    filepath = os.path.join(BATCH_DIR, filename)
    if not os.path.exists(filepath):
        return {'summary': [], 'quiz_questions': [], 'quiz_answers': [], 'other': []}
    
    data = {'summary': [], 'quiz_questions': [], 'quiz_answers': [], 'other': []}
    current = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if line.startswith('## SUMMARY'):
                current = 'summary'
            elif line.startswith('## QUIZ QUESTIONS'):
                current = 'quiz_questions'
            elif line.startswith('## QUIZ ANSWERS'):
                current = 'quiz_answers'
            elif line.startswith('## OTHER'):
                current = 'other'
            elif line.startswith('#') or not line.strip():
                continue
            elif current:
                data[current].append(line)
    return data

# ============================================================
# Attempt term lookup in existing dictionaries
# ============================================================
def lookup_term(text):
    """Try to find translation of a term/phrase in existing dictionaries."""
    # Exact match
    if text in cn_dict and text in sp_dict and text in hi_dict:
        return (cn_dict[text], sp_dict[text], hi_dict[text])
    # Case-insensitive
    text_lower = text.lower()
    for d, translations in [(cn_dict, 0), (sp_dict, 1), (hi_dict, 2)]:
        for k, v in d.items():
            if k.lower() == text_lower:
                result = [None, None, None]
                result[0] = cn_dict.get(k, cn_dict.get(text, None))
                result[1] = sp_dict.get(k, sp_dict.get(text, None))
                result[2] = hi_dict.get(k, hi_dict.get(text, None))
                if all(result):
                    return tuple(result)
                break
    # Check TERM_DICT
    if text_lower in TERM_DICT:
        return TERM_DICT[text_lower]
    return None

# ============================================================
# Count strings per course and report
# ============================================================
courses = ['algebra1', 'algebra2', 'geometry', 'biology', 'chemistry', 'physics']
all_strings = []

for course in courses:
    data = load_course_strings(f"{course}_to_translate.txt")
    total = sum(len(v) for v in data.values())
    if total == 0:
        continue
    
    # Try auto-translating
    auto_translated = 0
    manual_needed = 0
    
    for category, strings in data.items():
        for s in strings:
            # Check if exact match exists
            t = lookup_term(s)
            if t:
                auto_translated += 1
            else:
                manual_needed += 1
                all_strings.append((course, category, s))
    
    print(f"{course}: {total} total, {auto_translated} auto-translatable, {manual_needed} need translation")

print(f"\nTotal needing manual translation: {len(all_strings)}")

# ============================================================
# Write summary by course
# ============================================================
output = os.path.join(os.path.dirname(BASE), "translation_work_summary.txt")
with open(output, 'w', encoding='utf-8') as out:
    out.write(f"TRANSLATION WORK SUMMARY\n")
    out.write(f"========================\n\n")
    out.write(f"Total strings needing translation: {len(all_strings)}\n\n")
    
    for course in courses:
        course_strings = [(cat, s) for c, cat, s in all_strings if c == course]
        if not course_strings:
            continue
        out.write(f"\n{'='*60}\n")
        out.write(f"{course.upper()} ({len(course_strings)} strings)\n")
        out.write(f"{'='*60}\n")
        
        for cat, s in course_strings:
            out.write(f"  [{cat:15s}] {s}\n")

print(f"Work summary: {output}")

# Report how many quiz questions follow common patterns
pattern_counts = defaultdict(int)
for course, cat, s in all_strings:
    if cat == 'quiz_questions':
        # Strip question number
        q = re.sub(r'^\d+\.\s*', '', s)
        if q.startswith('What is'):
            pattern_counts['What is...'] += 1
        elif q.startswith('How many') or q.startswith('How much'):
            pattern_counts['How many/much...'] += 1
        elif q.startswith('If '):
            pattern_counts['If...'] += 1
        elif q.startswith('Which'):
            pattern_counts['Which...'] += 1
        elif q.startswith('A ') or q.startswith('An ') or q.startswith('The '):
            pattern_counts['A/An/The...'] += 1
        elif q.startswith('Two '):
            pattern_counts['Two...'] += 1
        elif q.startswith('Find') or q.startswith('Calculate') or q.startswith('Solve') or q.startswith('Convert'):
            pattern_counts['Find/Calc/Solve...'] += 1
        elif q.startswith('According') or q.startswith('In '):
            pattern_counts['According/In...'] += 1
        else:
            pattern_counts['Other'] += 1

print(f"\nQuiz question patterns:")
for pat, count in sorted(pattern_counts.items(), key=lambda x: -x[1]):
    print(f"  {pat}: {count}")
