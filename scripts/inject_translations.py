import json
import re
import html
import os

# Manual dictionary of core chemistry terms to Chinese
topic_translations = {
    "States of Matter": "物质状态",
    "Phase Changes": "相变",
    "Intensive & Extensive Properties": "强度性质与广度性质",
    "Mass, Volume, & Density": "质量、体积与密度",
    "Heterogeneous & Homogeneous Mixtures": "非均匀混合物与均匀混合物",
    "Physical & Chemical Properties": "物理性质与化学性质",
    "Physical & Chemical Changes": "物理变化与化学变化",
    "Energy & Matter": "能量与物质",
    "Pure Substances vs. Mixtures": "纯净物与混合物",
    "Scientific Notation": "科学计数法",
    "Significant Figures": "有效数字",
    "Accuracy vs. Precision": "准确度与精密度",
    "Metric System": "公制系统",
    "Unit Conversions": "单位换算",
    "Electrons, Protons, and Neutrons": "电子、质子和中子",
    "Atomic Structure": "原子结构",
    "Quantum Mechanical Model & Orbitals": "量子力学模型与轨道",
    "Electromagnetic Spectrum & Atomic Emission Spectra": "电磁光谱与原子发射光谱",
    "Radioactivity & Stability": "放射性与稳定性",
    "Isotopes & Radioisotopes": "同位素与放射性同位素",
    "Element Synthesis": "元素合成",
    "Atomic Theory": "原子理论",
    "Chemical Symbols": "化学符号",
    "Periodic Table Arrangement": "周期表排列",
    "Valence Electrons & Reactivity": "价电子与反应性",
    "Electron Suborbitals": "电子亚层",
    "Electron Configuration": "电子排布",
    "Periodic Trends": "周期性趋势",
    "Shielding Effect": "屏蔽效应",
    "VSEPR Molecule Shapes": "VSEPR 分子形状",
    "Suborbital Shapes": "亚层形状",
    "Ionic Bonds": "离子键",
    "Covalent Bonds": "共价键",
    "Metallic Bonds": "金属键",
    "Intermolecular Forces": "分子间作用力",
    "Naming Ionic Compounds": "命名离子化合物",
    "Naming Covalent Compounds": "命名共价化合物",
    "Writing Chemical Formulas": "书写化学式",
    "Lewis Structures": "路易斯结构式",
    "Molecular Geometry": "分子几何",
    "Polarity": "极性",
    "The Mole Concept": "摩尔概念",
    "Molar Mass": "摩尔质量",
    "Percent Composition": "百分比组成",
    "Empirical & Molecular Formulas": "经验式与分子式",
    "Balancing Chemical Equations": "配平化学方程式",
    "Types of Chemical Reactions": "化学反应类型",
    "Stoichiometry": "化学计量",
    "Limiting Reactants": "限制反应物",
    "Percent Yield": "产率百分比",
    "Gases": "气体",
    "Gas Laws": "气体定律",
    "Ideal Gas Law": "理想气体定律",
    "Kinetic Molecular Theory": "分子运动论",
    "Solutions": "溶液",
    "Solubility": "溶解度",
    "Concentration": "浓度",
    "Molarity": "摩尔浓度",
    "Dilutions": "稀释",
    "Acids and Bases": "酸和碱",
    "pH and pOH": "pH 和 pOH",
    "Titrations": "滴定",
    "Thermochemistry": "热化学",
    "Enthalpy": "焓",
    "Entropy": "熵",
    "Gibbs Free Energy": "吉布斯自由能",
    "Reaction Rates": "反应速率",
    "Chemical Equilibrium": "化学平衡",
    "Le Chatelier's Principle": "勒夏特列原理",
    "Redox Reactions": "氧化还原反应",
    "Electrochemistry": "电化学",
    "Nuclear Chemistry": "核化学",
    "Organic Chemistry": "有机化学",
    "Biochemistry": "生物化学",
    "Polymers": "聚合物",
    "Nanotechnology": "纳米技术",
    "Environmental Chemistry": "环境化学",
    "Green Chemistry": "绿色化学",
    "Quiz": "测验",
    "Test": "考试",
    "Summary": "总结",
    "Practice": "练习",
    "Video": "视频",
    "Pure Substances vs Mixtures": "纯净物与混合物",
    "Calculating pH and pOH using Log": "使用对数计算 pH 和 pOH",
    "Acid & Base Properties": "酸碱性质",
    "Properties of Acids  Bases": "酸碱性质",
    "Arrhenius vs BronstedLowry Definitions": "阿伦尼乌斯与布朗斯特-劳里定义",
    "Binary Acids vs. Oxyacids": "二元酸与含氧酸",
    "Naming Acids": "命名酸",
    "pH  pOH Scale": "pH 和 pOH 标度",
    "Calculating pH": "计算 pH",
    "Identifying Acids & Bases": "识别酸和碱",
    "Strong vs Weak Acids  Bases": "强酸强碱与弱酸弱碱",
    "Strong vs. Weak Acids/Bases": "强酸强碱与弱酸弱碱",
    "Neutralization Reactions": "中和反应",
    "Naming Salts from Neutralization": "命名中和反应生成的盐",
    "Buffer Solutions": "缓冲溶液",
    "Buffers": "缓冲液",
    "pH & pOH Scale": "pH 和 pOH 标度",
    "Energy Heat  Temperature": "能量、热量与温度",
    "Heat Conversion": "热量转换",
    "Specific Heat": "比热容",
    "Specific Heat Capacity": "比热容",
    "Calorimetry": "量热法",
    "Heat Capacity": "热容",
    "Enthalpy  Thermochemical Equations": "焓与热化学方程式",
    "Enthalpy (ΔH), Entropy (ΔS), Free Energy (ΔG)": "焓 (ΔH)、熵 (ΔS)、自由能 (ΔG)",
    "Enthalpy, Entropy, Free Energy": "焓、熵、自由能",
    "Hesss Law": "赫斯定律",
    "Hess’s Law": "赫斯定律",
    "Heating  Cooling Curves": "加热与冷却曲线",
    "Activation Energy": "活化能",
    "Collision Theory": "碰撞理论",
    "Nuclear Fusion and Fission": "核聚变与核裂变",
    "Alpha, Beta, & Gamma Decay": "α、β 和 γ 衰变",
    "Factors Affecting Reaction Rates": "影响反应速率的因素",
    "Reaction Rates & Catalysts": "反应速率与催化剂",
    "Chemical Equilibrium": "化学平衡",
    "Nuclear Reactions": "核反应",
    "Chemical Equilibrium & Le Chatelier's Principle": "化学平衡与勒夏特列原理",
    "Half-Life Calculations": "半衰期计算",
    "Le Chateliers Principle": "勒夏特列原理",
    "Equilibrium Constants Keq": "平衡常数 Keq",
    "Applications of Nuclear Chemistry": "核化学的应用",
    "Scientific Notation": "科学计数法",
    "Unit 1 Test": "第一单元测试",
    "Unit 2 Test": "第二单元测试",
    "Unit 3 Test": "第三单元测试",
    "Unit 4 Test": "第四单元测试",
    "Unit 5 Test": "第五单元测试",
    "Unit 6 Test": "第六单元测试",
    "Unit 7 Test": "第七单元测试",
    "Unit 8 Test": "第八单元测试",
    "Unit 9 Test": "第九单元测试",
    "Unit 10 Test": "第十单元测试",
    "Unit 11 Test": "第十一单元测试",
    "Unit 12 Test": "第十二单元测试",
    "Specific Heat Summary": "比热容总结",
    "Avogadro’s Number": "阿伏伽德罗常数",
    "Combined Gas Law": "联合气体定律",
    "Boyle’s Law": "波义耳定律",
    "Charles’ Law": "查理定律",
    "Gay-Lussac’s Law": "盖-吕萨克定律",
    "Ideal Gas Law": "理想气体定律",
    "Introduction to Nomenclature": "命名法简介",
    "Crisscross Method": "十字交叉法",
    "Common Exceptions & Traditional Names": "常见例外与传统名称",
    "Empirical vs. Molecular Formulas": "经验式与分子式",
    "Factors Affecting Solubility": "影响溶解度的因素",
    "Colligative Properties": "依数性",
    "Combustion Reactions": "燃烧反应",
    "Balancing Equations": "配平化学方程式",
    "Bond Formation": "键的形成"
}

def translate_phrase(phrase):
    # Unescape HTML entities
    phrase = html.unescape(phrase)
    
    # Try direct match first
    if phrase in topic_translations:
        return topic_translations[phrase]
    
    # Check for Lesson X.Y: Pattern
    lesson_match = re.match(r"(Lesson \d+\.\d+): (.*)", phrase)
    if lesson_match:
        prefix_eng = lesson_match.group(1)
        topic_eng = lesson_match.group(2)
        
        # Translate prefix
        prefix_chn = prefix_eng.replace("Lesson", "第") + "课"
        
        # Translate topic
        suffix_chn = ""
        main_topic_eng = topic_eng
        
        if topic_eng.endswith(" Summary"):
            main_topic_eng = topic_eng[:-8]
            suffix_chn = " 总结"
        elif topic_eng.endswith(" Quiz"):
            main_topic_eng = topic_eng[:-5]
            suffix_chn = " 测验"
        elif topic_eng.endswith(" Practice"):
            main_topic_eng = topic_eng[:-9]
            suffix_chn = " 练习"

        main_topic_eng_cleaned = re.sub(r'\s+', ' ', main_topic_eng).strip()
        
        topic_chn = topic_translations.get(main_topic_eng_cleaned, main_topic_eng)
        
        # If still english, try with replaced &
        if topic_chn == main_topic_eng:
             topic_chn = topic_translations.get(main_topic_eng_cleaned.replace("&", "&amp;"), main_topic_eng)

        return f"{prefix_chn}: {topic_chn}{suffix_chn}"

    # Try matching standalone topic with suffix
    if phrase.endswith(" Summary"):
        base = phrase[:-8].strip()
        if base in topic_translations:
            return topic_translations[base] + " 总结"
    
    return phrase

def main():
    try:
        # Re-run scan logic if needed or just use previously generated file
        # But here I assume I am just providing the tool.
        # Check if unique_titles.txt exists, if not, maybe prompt to run scan_titles.py
        if not os.path.exists("/workspaces/ArisEdu/scripts/unique_titles.txt"):
            print("unique_titles.txt not found. Running scan_titles.py...")
            os.system("python3 /workspaces/ArisEdu/scripts/scan_titles.py > /workspaces/ArisEdu/scripts/unique_titles.txt")
        
        with open("/workspaces/ArisEdu/scripts/unique_titles.txt", "r") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error: {e}")
        return

    new_translations = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("Found ") or line.startswith("---"):
            continue
            
        original_key = html.unescape(line)
        translated = translate_phrase(line)
        
        if translated != original_key:
            new_translations[original_key] = translated

        if line != original_key:
             translated_raw = translate_phrase(line)
             if translated_raw != line:
                 new_translations[line] = translated_raw
            
    for eng, chn in topic_translations.items():
        new_translations[eng] = chn

    # Output to global_translations.js
    global_trans_path = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"
    
    try:
        with open(global_trans_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading global_translations.js: {e}")
        return

    # Clean up previous injection
    marker_key = '"Accuracy vs. Precision":'
    marker_pos = content.find(marker_key)
    
    if marker_pos != -1:
        line_start = content.rfind('\n', 0, marker_pos)
        check_comma_pos = line_start - 1
        while content[check_comma_pos].isspace():
            check_comma_pos -= 1
        curr_cut_point = check_comma_pos if content[check_comma_pos] == ',' else line_start
        end_brace_index = content.rfind("  };")
        if end_brace_index == -1: end_brace_index = content.rfind("};")
        content = content[:curr_cut_point] + content[end_brace_index:]
        print("Removed previous injection block.")

    insertion_point = content.rfind("  };")
    if insertion_point == -1: insertion_point = content.rfind("};")
    
    output_lines = []
    
    if insertion_point != -1:
        prev_char_index = insertion_point - 1
        while content[prev_char_index].isspace():
            prev_char_index -= 1
        needs_comma = content[prev_char_index] != ',' and content[prev_char_index] != '{'
        
        for k in sorted(new_translations.keys()):
            v = new_translations[k]
            k_esc = k.replace('"', '\\"')
            v_esc = v.replace('"', '\\"')
            output_lines.append(f'  "{k_esc}": "{v_esc}",')

        start_str = ",\n" if needs_comma else "\n"
        to_insert = start_str + "\n".join(output_lines) + "\n"
        
        new_content = content[:insertion_point] + to_insert + content[insertion_point:]
        
        with open(global_trans_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully updated translations in {global_trans_path}")

if __name__ == "__main__":
    main()
