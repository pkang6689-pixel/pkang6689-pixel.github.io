import json
import re
import os

# 1. Load existing translations
json_path = 'ArisEdu Project Folder/scripts/global_translations.js'

with open(json_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Define new keys to add
new_translations = {
  "Core Definitions": "核心定义",
  "Key Points": "关键点",
  "Next Up: Play": "下一步: 玩游戏",
  "Next Up: Practice": "下一步: 练习",
  "Example": "例如",
  "Q:": "问:",
  "A:": "答:",
  "Solid": "固体",
  "Liquid": "液体",
  "Gas": "气体",
  "Formula": "公式",
  "Mass Number": "质量数",
  "Atomic Number": "原子序数",
  "Proton": "质子",
  "Neutron": "中子",
  "Electron": "电子",
  "Charge Balance": "电荷平衡",
  "Another key detail to remember.": "另一个需要记住的关键细节。",
  "Summary point 3.": "总结点 3。",
  "Coefficient": "系数",
  "Units": "单位",
  "Volume": "体积",
  "Pressure": "压强",
  "Temperature": "温度",
  "Moles": "摩尔",
  "Valence Electrons": "价电子",
  "Ionic Bonds": "离子键",
  "Covalent Bonds": "共价键",
  "Metallic Bonds": "金属键",
  "Product": "生成物",
  "Reactant": "反应物",
  "Yield": "产量",
  "Scientific Notation": "科学记数法",
  "Significant Figures": "有效数字",
  "Unit Conversions": "单位换算",
  "Isotopes & Radioisotopes": "同位素与放射性同位素",
  "Radioactivity & Stability": "放射性与稳定性",
  "Bond Formation": "化学键形成",
  "Naming Ionic Bonds": "离子键命名",
  "Polyatomic Ions": "多原子离子",
  "Naming Ionic Compounds": "离子化合物命名",
  "Naming Covalent Compounds": "共价化合物命名",
  "Organic Compounds": "有机化合物",
  "Mixed Nomenclature Practice": "混合命名法练习",
  "Chemical Equilibrium & Le Chatelier’s Principle": "化学平衡与勒夏特列原理",
  "Monatomic & Diatomic Gases": "单原子与双原子气体",
  "Real Gases & Deviations": "真实气体与偏差",
  "Solubility Curves": "溶解度曲线",
  "Solution Nomenclature": "溶液命名法",
  "Solution Types": "溶液类型",
  "Stoichiometric Calculations": "化学计量计算",
  "Types of Reactions": "反应类型",
  "Writing Correct Formulas": "书写正确化学式",
  "Limiting Reagents": "限制试剂",
  "Dilution": "稀释",
  "Molar Conversions": "摩尔转换",
  "Molar Mass & Molecular Mass": "摩尔质量与分子质量",
  "Net Charge": "净电荷",
  "Crisscross Method": "交叉法",
  "Suborbital Shapes": "亚层形状",
  "Periodic Table Trends": "元素周期表趋势",
  "Reaction Energy Diagrams": "反应能量图",
  "Endothermic & Exothermic": "吸热与放热",
  "Phase Changes": "相变",
  "Heating Curves": "加热曲线",
  "Specific Heat Capacity": "比热容",
  "Calorimetry": "量热法",
  "Nuclear Fission": "核裂变",
  "Nuclear Fusion": "核聚变",
  "Half-Life Calculations": "半衰期计算",
  "Alpha, Beta, Gamma Decay": "Alpha, Beta, Gamma 衰变",
  "Electrons, Protons, and Neutrons": "电子、质子和中子",
  "Electrons, Protons & Neutrons": "电子、质子和中子",
  "Introduction to The Mole": "摩尔简介",
  "Empirical & Molecular Formulas": "经验式与分子式",
  "Percent Composition": "质量百分组成",
  "Balancing Equations": "配平化学方程式",
  "Predicting Products": "预测生成物",
  "Redox Reactions": "氧化还原反应",
  "Oxidation Numbers": "氧化数",
  "Acids & Bases Intro": "酸碱简介",
  "pH & pOH Calculations": "pH 与 pOH 计算",
  "Titration": "滴定",
  "Buffers": "缓冲液",
  "Gas Laws": "气体定律",
  "Ideal Gas Law": "理想气体状态方程",
  "Dalton's Law of Partial Pressures": "道尔顿分压定律",
  "Graham's Law of Effusion": "格雷厄姆气体扩散定律",
  "Kinetics & Reaction Rates": "动力学与反应速率",
  "Catalysts": "催化剂",
  "Equilibrium Constant (Keq)": "平衡常数 (Keq)",
  "Introduction to Nomenclature": "命名法简介",
  "Common Exceptions & Traditional Names": "常见例外与传统名称",
  "States of Matter": "物质状态",
  "The Three States of Matter": "物质的三种状态",
  "Intramolecular vs Intermolecular Forces": "分子内力与分子间力",
  "Hydrogen Bonding": "氢键",
  "Dipole-Dipole Forces": "偶极-偶极力",
  "London Dispersion Forces": "伦敦色散力",
  "Bohr Model vs Quantum Model": "玻尔模型与量子模型",
  "Electron Configuration": "电子排布",
  "Orbital Diagrams": "轨道图",
  "Quantum Numbers": "量子数",
  "Lewis Dot Structures": "路易斯点结构",
  "VSEPR Theory": "价层电子对互斥理论",
  "Hybridization": "杂化",
  "Resonance Structures": "共振结构",
  "Formal Charge": "形式电荷",
  "Polarity": "极性"
}

# 3. Create insertion string
insertion = ""
for key, val in new_translations.items():
    if f'"{key}"' not in content:
        # Check if it's already in the file even if key isn't quoted exactly the same way?
        # Assuming quoted keys.
         insertion += f'  "{key}": "{val}",\n'

# 4. Write back
if insertion:
    # Anchor point
    anchor = '"IN PROGRESS": "进行中"'
    
    if anchor in content:
        # We append after the anchor, adding a comma to the anchor line implicitly by replacing it?
        # No, the anchor line might not have a comma if it was the last one.
        # But in valid JSON/object, if we add more, the previous last one needs a comma.
        
        replacement = f'{anchor},\n{insertion.rstrip(",\n")}'
        new_content = content.replace(anchor, replacement)
        
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully injected {len([l for l in insertion.splitlines() if l])} new keys.")
    else:
        print(f"Could not find anchor '{anchor}' to inject translations.")
else:
    print("No new translations to inject.")

