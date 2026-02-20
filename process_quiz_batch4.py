import json
import os

# Load remaining strings
with open('quiz_strings_remaining.json', 'r', encoding='utf-8') as f:
    remaining = json.load(f)

# Take next batch (120 items)
batch = remaining[:120]
remaining_after = remaining[120:]

# Translations
translations = {
    "How many characteristics of life are there?": "有多少种生命特征？",
    "How many variables should change at a time?": "一次应该改变多少个变量？",
    "Human anatomy": "人体解剖学",
    "Hunts and eats other organisms": "捕猎并吃其他生物",
    "If two species have the exact same niche:": "如果两个物种拥有完全相同的生态位：",
    "Ignore each other": "互相忽视",
    "Ignore environmental impact": "忽视环境影响",
    "Ignoring evidence": "忽视证据",
    "In commensalism:": "在片利共生中：",
    "In mutualism, how many species benefit?": "在互利共生中，有多少物种受益？",
    "In one direction": "在一个方向上",
    "In the ocean": "在海洋中",
    "Increase competition": "增加竞争",
    "Increasing pollution": "增加污染",
    "Independent variable": "自变量",
    "Information collected during experiments": "实验期间收集的信息",
    "Interconnected food chains": "相互连接的食物链",
    "Intermediate species": "中间物种",
    "Introducing invasive species": "引入入侵物种",
    "Invasive species are:": "入侵物种是：",
    "Is hunted by others": "被其他生物捕猎",
    "It cannot be observed": "无法观察到",
    "It cannot be tested": "无法测试",
    "It changes randomly": "随机变化",
    "It is not real": "这不是真实的",
    "It is studied using scientific methods": "使用科学方法研究它",
    "It only exists in theory": "它仅存在于理论中",
    "It only works once": "它只起作用一次",
    "Its predator": "它的捕食者",
    "Its prey": "它的猎物",
    "Job": "工作",
    "Law": "定律",
    "Laws never change": "定律从不改变",
    "Lichens are examples of:": "地衣是以下哪种例子：",
    "Live in different areas": "生活在不同区域",
    "Lives alone": "独自生活",
    "Living and non-living components": "生物和非生物成分",
    "Lost forever": "永远丢失",
    "Made of producers only": "仅由生产者组成",
    "Maintaining a stable internal environment is called:": "维持稳定的内部环境被称为：",
    "Making assumptions": "做出假设",
    "Many animals": "许多动物",
    "Many generations": "许多代",
    "Matter in ecosystems is:": "生态系统中的物质是：",
    "Matter is:": "物质是：",
    "Medicines": "药物",
    "Meet needs without harming the future": "满足需求而不损害未来",
    "Metabolism involves:": "新陈代谢涉及：",
    "Microorganisms": "微生物",
    "Minimizing personal bias": "最小化个人偏见",
    "Modern biology integrates:": "现代生物学整合了：",
    "Most biology careers require:": "大多数生物学职业需要：",
    "Most energy is lost as:": "大部分能量流失为：",
    "Movement": "运动",
    "Moving around": "四处移动",
    "Native to the area": "该地区的本地物种",
    "Nature": "自然",
    "Neither progresses": "都不进展",
    "Neither species": "两个物种都不",
    "Neither survives": "都无法生存",
    "Never created or destroyed": "从未创造或破坏",
    "Niches are unlimited": "生态位是无限的",
    "Nitrogen cycle": "氮循环",
    "Nitrogen fixation": "固氮作用",
    "Nitrogen fixation is done by:": "固氮作用由以下完成：",
    "No formal education": "没有正规教育",
    "No soil present": "不存在土壤",
    "No succession": "没有演替",
    "No trophic levels": "没有营养级",
    "Non-native species that harm ecosystems": "损害生态系统的非本地物种",
    "Not using resources": "不使用资源",
    "Nurse": "护士",
    "Omnivores eat:": "杂食动物吃：",
    "On bare rock": "在裸露的岩石上",
    "On new islands": "在新岛屿上",
    "One benefits, one is unaffected": "一方受益，一方不受影响",
    "One community": "一个群落",
    "One ecosystem": "一个生态系统",
    "One is harmed": "一方受害",
    "One is killed": "一方被杀",
    "One lifetime": "一生",
    "One population": "一个种群",
    "One species only": "仅一个物种",
    "One will outcompete the other": "一方将胜过另一方",
    "Only a high school diploma": "只有高中文凭",
    "Only animals": "只有动物",
    "Only benefit humans": "只造福人类",
    "Only computer work": "只有计算机工作",
    "Only decomposers": "仅分解者",
    "Only decomposition": "仅分解",
    "Only eating food": "只吃食物",
    "Only eats plants": "只吃植物",
    "Only found in deserts": "只在沙漠中发现",
    "Only found in living things": "只在生物中发现",
    "Only groundwater": "只有地下水",
    "Only humans": "只有人类",
    "Only in living things": "只在生物中",
    "Only in the ocean": "只在海洋中",
    "Only its predators": "只有它的捕食者",
    "Only its prey": "只有它的猎物",
    "Only plants": "只有植物",
    "Only producers": "仅生产者",
    "Only rocks": "只有岩石",
    "Only sunlight": "只有阳光",
    "Organ system": "器官系统",
    "Organisms and their environment": "生物及其环境",
    "Organisms in a zoo": "动物园里的生物",
    "Over millions of years": "数百万年",
    "Overuse of resources": "过度使用资源",
    "Pioneer species": "先锋物种",
    "Pioneer species are:": "先锋物种是：",
    "Place to live": "居住的地方",
    "Planting trees": "植树",
    "Plants only": "仅植物",
    "Plants, animals, and climate": "植物、动物和气候",
    "Plastic waste": "塑料废物",
    "Pollution": "污染",
    "Population": "种群",
    "Populations share resources": "种群共享资源",
    "Predation": "捕食",
    "Predator-Prey": "捕食者-猎物",
    "Predator-Prey relationship is:": "捕食者-猎物关系是：",
    "Primary succession occurs:": "初生演替发生于：",
    "Producers (Autotrophs)": "生产者（自养生物）",
    "Producers → Consumers → Decomposers": "生产者 → 消费者 → 分解者",
    "Proves everything": "证明一切",
    "Quantitative data contains:": "定量数据包含：",
    "Questions": "问题",
    "Random changes": "随机变化",
    "Random guessing": "随机猜测",
    "Rapidly": "迅速地",
    "Recycled": "回收",
    "Reduce waste": "减少废物",
    "Refusing new ideas": "拒绝新想法"
}

# Inject
global_path = r"ArisEdu Project Folder/scripts/global_translations.js"
with open(global_path, 'r', encoding='utf-8') as f:
    content = f.read()

insertion_marker = 'const translations = {'
if insertion_marker not in content:
    print("Marker not found!")
    exit(1)

new_entries_str = "\n  /* Injected Quiz Translations Batch 4 */\n"
for k in batch:
    v = translations.get(k, k)
    k_esc = k.replace('"', '\\"')
    v_esc = v.replace('"', '\\"')
    if f'"{k_esc}":' not in content:
        new_entries_str += f'  "{k_esc}": "{v_esc}",\n'

new_content = content.replace(insertion_marker, insertion_marker + new_entries_str)

with open(global_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Update remaining
with open('quiz_strings_remaining.json', 'w', encoding='utf-8') as f:
    json.dump(remaining_after, f, indent=4, ensure_ascii=False)

print(f"Injected {len(batch)} items. {len(remaining_after)} remaining.")
