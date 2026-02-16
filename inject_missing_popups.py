import json
import re

translation_file = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"

new_translations = {
    # Extracted missing popups
    "Dilution": "稀释",
    "Limiting Reagents": "限制试剂",
    "Molar Conversions": "摩尔转换",
    "Molar Mass & Molecular Mass": "摩尔质量与分子质量",
    "Net Charge": "净电荷",
    "Organic Compounds": "有机化合物",
    "Polyatomic Ions": "多原子离子",
    "Pressure, Standard Atmosphere": "压强，标准大气压",
    "Real Gases & Deviations": "真实气体与偏差",
    "Solubility Curves": "溶解度曲线",
    "Solution Nomenclature": "溶液命名法",
    "Solution Types": "溶液类型",
    "Stoichiometric Calculations": "化学计量计算",
    "Types of Reactions": "反应类型",
    "Writing Correct Formulas": "书写正确化学式",
    "Unit 5A Test": "第 5A 单元测试",
    "Unit 5B Test": "第 5B 单元测试",
    "Chemical Equilibrium & Le Chatelier’s Principle": "化学平衡与勒夏特列原理",
    "Mixed Nomenclature Practice": "混合命名法练习",
    "Monatomic & Diatomic Gases": "单原子与双原子气体",
    
    # Progress indicators
    "COMPLETED": "已完成",
    "IN PROGRESS": "进行中"
}

try:
    with open(translation_file, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'const translations\s*=\s*({[\s\S]*?});', content) or             re.search(r'window\.globalTranslations\s*=\s*({[\s\S]*?});', content)
            
    if not match:
        print("Error: Could not find translation object")
        exit(1)
        
    json_str = match.group(1)
    
    # Loose parse
    try:
        data = json.loads(json_str)
    except:
        json_str_fixed = re.sub(r',\s*}', '}', json_str)
        data = json.loads(json_str_fixed)

    added = 0
    for k, v in new_translations.items():
        if k not in data:
            data[k] = v
            added += 1
            
    print(f"Added {added} new translations.")
    
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1), new_json_str)
    
    with open(translation_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
except Exception as e:
    print(f"Error: {e}")
