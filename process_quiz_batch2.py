import json
import os

# Load remaining strings
with open('quiz_strings_remaining.json', 'r', encoding='utf-8') as f:
    remaining = json.load(f)

# Take first batch (120 items)
batch = remaining[:120]
remaining_after = remaining[120:]

# Define translations for this batch
translations = {
    "Animal behavior": "动物行为",
    "Animal classification": "动物分类",
    "Animals": "动物",
    "Animals in natural habitats": "自然栖息地中的动物",
    "Are top predators": "是顶级捕食者",
    "Art and music": "艺术和音乐",
    "As many as possible": "尽可能多",
    "Astronomy": "天文学",
    "Backwards": "向后",
    "Bacteria": "细菌",
    "Bacteria to ecosystems": "细菌到生态系统",
    "Barnacles on whales are an example of:": "鲸鱼身上的藤壶是以下哪种例子：",
    "Based on faith alone": "仅基于信仰",
    "Bees and flowers demonstrate:": "蜜蜂和花朵展示了：",
    "Being objective means:": "客观意味着：",
    "Biochemistry combines biology with:": "生物化学将生物学与以下结合：",
    "Biology helps improve:": "生物学有助于改善：",
    "Biology studies organisms from:": "生物学研究生物，范围从：",
    "Biotechnology involves:": "生物技术涉及：",
    "Body function": "身体功能",
    "Body structure": "身体结构",
    "Both are harmed": "两者都受害",
    "Both plants and animals": "植物和动物",
    "Both species benefit": "两个物种都受益",
    "Both will thrive": "两者都会繁荣",
    "Building design": "建筑设计",
    "Building machines": "制造机器",
    "Burning forests": "燃烧森林",
    "Carbon cycle": "碳循环",
    "Carbon is released by:": "碳通过以下方式释放：",
    "Cell theory is an example of a:": "细胞学说是以下哪种例子：",
    "Cell, tissue, organ, system": "细胞、组织、器官、系统",
    "Certification only": "仅认证",
    "Chemical reactions for energy": "能量的化学反应",
    "Chemistry, physics, and math": "化学、物理和数学",
    "Climate change affects:": "气候变化影响：",
    "Climax species": "顶级物种",
    "Compete for limited resources": "争夺有限资源",
    "Competition doesn't exist": "竞争不存在",
    "Competition occurs when organisms:": "竞争发生在生物：",
    "Conservation efforts include:": "保护工作包括：",
    "Constant": "常数",
    "Control variable": "控制变量",
    "Cooking food": "烹饪食物",
    "Created new each time": "每次都重新创造",
    "Creating parks": "创建公园",
    "Crime investigation": "犯罪调查",
    "Crime scenes": "犯罪现场",
    "Crops": "农作物",
    "Crops and soil": "农作物和土壤",
    "Crystallization": "结晶",
    "Data is:": "数据是：",
    "Decomposers only": "仅分解者",
    "Decomposers work at:": "分解者工作于：",
    "Decomposers:": "分解者：",
    "Deforestation and urbanization": "森林砍伐和城市化",
    "Dense forests": "茂密的森林",
    "Dependent variable": "因变量",
    "Different species in an area": "某一区域内的不同物种",
    "Doctor": "医生",
    "Eat only plants": "只吃植物",
    "Eat other organisms": "吃其他生物",
    "Ecologist": "生态学家",
    "Ecology is the study of:": "生态学是研究：",
    "Ecosystems worldwide": "世界各地的生态系统",
    "Eliminate each other": "相互消除",
    "Energy flows through an ecosystem:": "能量流经生态系统：",
    "Evaporation and precipitation": "蒸发和降水",
    "Experiments always fail": "实验总是失败",
    "Extinct animals": "灭绝动物",
    "Fact": "事实",
    "Food chains show:": "食物链显示：",
    "Food source": "食物来源",
    "Fungi only": "仅真菌",
    "Geneticist": "遗传学家",
    "Genetics focuses on:": "遗传学关注：",
    "Geography only": "仅地理",
    "Geology": "地质学",
    "Growing larger": "变大",
    "Guess": "猜测",
    "Habitat destruction": "栖息地破坏",
    "Habitat destruction includes:": "栖息地破坏包括：",
    "Having cells": "拥有细胞",
    "Having strong opinions": "有强烈的意见",
    "Help each other": "互相帮助",
    "Herbivores": "食草动物",
    "Herbivores are:": "食草动物是：",
    "Heredity and genes": "遗传和基因",
    "Heterotrophs must:": "异养生物必须：",
    "History and language": "历史和语言",
    "How body parts function": "身体部位如何运作",
    "How does aquatic ecosystems affect living organisms?": "水生生态系统如何影响生物？",
    "How does astrobiology and the search for life beyond earth affect living organisms?": "天体生物学和寻找地外生命如何影响生物？",
    "How does biochemistry in everyday life affect living organisms?": "日常生活中的生物化学如何影响生物？",
    "How does biodiversity affect living organisms?": "生物多样性如何影响生物？",
    "How does bioethics (cloning, stem cells, genetic privacy) affect living organisms?": "生物伦理学（克隆、干细胞、基因隐私）如何影响生物？",
    "How does biotechnology (crispr, cloning, gmos) affect living organisms?": "生物技术（CRISPR、克隆、转基因生物）如何影响生物？",
    "How does biotechnology and genetic engineering affect living organisms?": "生物技术和基因工程如何影响生物？",
    "How does carrying capacity and limiting factors affect living organisms?": "环境容纳量和限制因子如何影响生物？",
    "How does cell discovery and theory affect living organisms?": "细胞发现和理论如何影响生物？",
    "How does cell structure and function affect living organisms?": "细胞结构和功能如何影响生物？",
    "How does cellular reproduction affect living organisms?": "细胞繁殖如何影响生物？",
    "How does cellular respiration affect living organisms?": "细胞呼吸如何影响生物？",
    "How does cellular transport affect living organisms?": "细胞运输如何影响生物？",
    "How does chemical energy and atp affect living organisms?": "化学能和 ATP 如何影响生物？",
    "How does chemical reactions and enzymes affect living organisms?": "化学反应和酶如何影响生物？",
    "How does circulatory system affect living organisms?": "循环系统如何影响生物？",
    "How does climate change and ecosystem shifts affect living organisms?": "气候变化和生态系统转变如何影响生物？",
    "How does community ecology affect living organisms?": "群落生态学如何影响生物？",
    "How does comparison of mitosis and meiosis affect living organisms?": "有丝分裂和减数分裂的比较如何影响生物？",
    "How does dna replication affect living organisms?": "DNA 复制如何影响生物？",
    "How does dna structure and function affect living organisms?": "DNA 结构和功能如何影响生物？",
    "How does digestive system affect living organisms?": "消化系统如何影响生物？",
    "How does dna, rna, and protein synthesis affect living organisms?": "DNA、RNA 和蛋白质合成如何影响生物？",
    "How does ecological relationships affect living organisms?": "生态关系如何影响生物？",
    "How does ecological succession affect living organisms?": "生态演替如何影响生物？",
    "How does endocrine system affect living organisms?": "内分泌系统如何影响生物？",
    "How does energy flow in ecosystems affect living organisms?": "生态系统中的能量流动如何影响生物？",
    "How does excretory system affect living organisms?": "排泄系统如何影响生物？",
    "How does fermentation affect living organisms?": "发酵如何影响生物？",
    "How does gene regulation and expression affect living organisms?": "基因调控和表达如何影响生物？",
    "How does global conservation efforts affect living organisms?": "全球保护工作如何影响生物？",
    "How does history of life on earth affect living organisms?": "地球生命史如何影响生物？",
    "How does homeostasis affect living organisms?": "稳态如何影响生物？",
    "How does how organisms obtain energy affect living organisms?": "生物如何获取能量如何影响生物？",
    "How does human genetics and genetic disorders affect living organisms?": "人类遗传学和遗传疾病如何影响生物？"
}

# Update global translations file
global_path = r"ArisEdu Project Folder/scripts/global_translations.js"
with open(global_path, 'r', encoding='utf-8') as f:
    content = f.read()

insertion_marker = 'const translations = {'
if insertion_marker not in content:
    print("Marker not found!")
    exit(1)

new_entries_str = "\n  /* Injected Quiz Translations Batch 2 */\n"
for k in batch:
    v = translations.get(k, k) # Use key as fallback if translation missing in dict
    k_esc = k.replace('"', '\\"')
    v_esc = v.replace('"', '\\"')
    if f'"{k_esc}":' not in content:
        new_entries_str += f'  "{k_esc}": "{v_esc}",\n'

new_content = content.replace(insertion_marker, insertion_marker + new_entries_str)

with open(global_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Update remaining file
with open('quiz_strings_remaining.json', 'w', encoding='utf-8') as f:
    json.dump(remaining_after, f, indent=4, ensure_ascii=False)

print(f"Injected {len(batch)} items. {len(remaining_after)} remaining.")
