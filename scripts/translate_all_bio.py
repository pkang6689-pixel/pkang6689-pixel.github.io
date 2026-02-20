#!/usr/bin/env python3
"""
Comprehensive Biology Content Translation Generator
Generates Chinese translations for ALL extracted biology strings.
"""

import re
from pathlib import Path

INPUT_FILE = Path(r"c:\Users\Peter\pkang6689-pixel.github.io\scripts\bio_strings_to_translate.txt")
TRANSLATIONS_FILE = Path(r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js")

# Core biology term translations
CORE_TERMS = {
    "biology": "生物学",
    "life": "生命",
    "cell": "细胞",
    "cells": "细胞",
    "organism": "生物",
    "organisms": "生物",
    "ecosystem": "生态系统",
    "ecosystems": "生态系统",
    "energy": "能量",
    "dna": "DNA",
    "rna": "RNA",
    "atp": "ATP",
    "gene": "基因",
    "genes": "基因",
    "genetics": "遗传学",
    "evolution": "进化",
    "ecology": "生态学",
    "photosynthesis": "光合作用",
    "respiration": "呼吸作用",
    "cellular respiration": "细胞呼吸",
    "metabolism": "新陈代谢",
    "homeostasis": "稳态",
    "mitosis": "有丝分裂",
    "meiosis": "减数分裂",
    "protein": "蛋白质",
    "enzyme": "酶",
    "enzymes": "酶",
    "chromosome": "染色体",
    "chromosomes": "染色体",
    "tissue": "组织",
    "organ": "器官",
    "organs": "器官",
    "population": "种群",
    "community": "群落",
    "biome": "生物群落",
    "biomes": "生物群落",
    "biosphere": "生物圈",
    "habitat": "栖息地",
    "niche": "生态位",
    "species": "物种",
    "adaptation": "适应",
    "reproduction": "繁殖",
    "biodiversity": "生物多样性",
    "conservation": "保护",
    "fermentation": "发酵",
    "biotechnology": "生物技术",
    "immune system": "免疫系统",
    "nervous system": "神经系统",
    "digestive system": "消化系统",
    "circulatory system": "循环系统",
    "respiratory system": "呼吸系统",
    "endocrine system": "内分泌系统",
    "reproductive system": "生殖系统",
    "plasma membrane": "质膜",
    "organelle": "细胞器",
    "organelles": "细胞器",
    "nucleus": "细胞核",
    "mitochondria": "线粒体",
    "chloroplast": "叶绿体",
    "ribosome": "核糖体",
    "prokaryotic": "原核的",
    "eukaryotic": "真核的",
    "autotroph": "自养生物",
    "heterotroph": "异养生物",
    "producer": "生产者",
    "producers": "生产者",
    "consumer": "消费者",
    "consumers": "消费者",
    "decomposer": "分解者",
    "decomposers": "分解者",
    "food chain": "食物链",
    "food web": "食物网",
    "trophic level": "营养级",
    "primary succession": "初级演替",
    "secondary succession": "次级演替",
    "pioneer species": "先锋物种",
    "climax community": "顶极群落",
    "symbiosis": "共生",
    "mutualism": "互利共生",
    "commensalism": "偏利共生",
    "parasitism": "寄生",
    "predation": "捕食",
    "predator": "捕食者",
    "prey": "猎物",
    "competition": "竞争",
    "herbivore": "草食动物",
    "herbivores": "草食动物",
    "carnivore": "肉食动物",
    "carnivores": "肉食动物",
    "omnivore": "杂食动物",
    "omnivores": "杂食动物",
    "hypothesis": "假设",
    "theory": "理论",
    "law": "定律",
    "scientific method": "科学方法",
    "variable": "变量",
    "control group": "对照组",
    "independent variable": "自变量",
    "dependent variable": "因变量",
    "nitrogen fixation": "固氮",
    "carbon cycle": "碳循环",
    "nitrogen cycle": "氮循环",
    "water cycle": "水循环",
    "phosphorus cycle": "磷循环",
    "biogeochemical cycle": "生物地球化学循环",
    "mendelian genetics": "孟德尔遗传学",
    "non-mendelian genetics": "非孟德尔遗传学",
    "carrying capacity": "承载力",
    "limiting factors": "限制因素",
    "population dynamics": "种群动态",
    "population regulation": "种群调节",
    "ecological succession": "生态演替",
    "environmental biology": "环境生物学",
    "aquatic ecosystems": "水生生态系统",
    "terrestrial biomes": "陆地生物群落",
    "cellular transport": "细胞运输",
    "cellular reproduction": "细胞繁殖",
    "community ecology": "群落生态学",
    "genetic engineering": "基因工程",
    "stem cells": "干细胞",
    "regenerative medicine": "再生医学",
    "genetic disorders": "遗传疾病",
    "human genetics": "人类遗传学",
    "climate change": "气候变化",
    "ecosystem shifts": "生态系统变迁",
    "endangered species": "濒危物种",
    "conservation strategies": "保护策略",
    "sustainable development": "可持续发展",
    "renewable energy": "可再生能源",
    "deforestation": "森林砍伐",
    "urbanization": "城市化",
    "overexploitation": "过度开发",
    "habitat destruction": "栖息地破坏",
    "invasive species": "入侵物种",
    "crispr": "CRISPR",
    "cloning": "克隆",
    "gmos": "转基因生物",
    "bioethics": "生物伦理学",
    "astrobiology": "天体生物学",
    "botany": "植物学",
    "zoology": "动物学",
    "microbiology": "微生物学",
    "immunology": "免疫学",
    "biochemistry": "生物化学",
    "cell biology": "细胞生物学",
    "marine biology": "海洋生物学",
    "anatomy": "解剖学",
    "physiology": "生理学",
    "pharmacology": "药理学",
    "medicine": "医学",
    "transcription": "转录",
    "translation": "翻译",
    "dna replication": "DNA复制",
    "cell cycle": "细胞周期",
    "cancer": "癌症",
    "cell discovery": "细胞发现",
    "cell theory": "细胞学说",
    "microscopy": "显微镜术",
    "cell imaging": "细胞成像",
    "chemical energy": "化学能",
    "chemical reactions": "化学反应",
    "gene regulation": "基因调控",
    "gene expression": "基因表达",
    "matter": "物质",
    "atomic structure": "原子结构",
    "building blocks of life": "生命的组成单元",
    "energy flow": "能量流动",
    "living systems": "生命系统",
    "human body": "人体",
    "sexual reproduction": "有性生殖",
    "resource partitioning": "资源分配",
    "competitive exclusion": "竞争排斥",
    "realized niche": "实际生态位",
    "fundamental niche": "基本生态位",
    "primary consumer": "初级消费者",
    "secondary consumer": "次级消费者",
    "tertiary consumer": "三级消费者",
    "sustainable practices": "可持续做法",
    "global conservation": "全球保护",
    "water and its solutions": "水及其溶液",
    "structures and organelles": "结构与细胞器",
}

# Direct translations for specific strings
DIRECT_TRANSLATIONS = {
    "The sun": "太阳",
    "The cell": "细胞",
    "Certain bacteria": "某些细菌",
    "Lichens and mosses": "地衣和苔藓",
    "Atom, then molecule": "原子，然后是分子",
    "Producers (level 1)": "生产者（第1级）",
    "The study of plants": "植物学研究",
    "The study of animals": "动物学研究",
    "The study of microorganisms": "微生物学研究",
    "The study of the immune system": "免疫系统研究",
    "The study of heredity and genes": "遗传和基因研究",
    "The study of organisms and their environments": "生物及其环境研究",
    "The study of chemical processes in living things": "生物体内化学过程研究",
    "The study of cell structure and function": "细胞结构和功能研究",
    "The study of ocean organisms and ecosystems": "海洋生物和生态系统研究",
    "Doctor, nurse, pharmacist": "医生、护士、药剂师",
    "How do plants get carbon?": "植物如何获取碳？",
    "Unlike energy, matter is:": "与能量不同，物质是：",
    "Bare rock or hardened lava": "裸露岩石或硬化熔岩",
    "Grasses, shrubs, then trees": "草、灌木，然后是树木",
    "Recycled through ecosystems": "在生态系统中循环",
    "Animals that eat only plants": "只吃植物的动物",
    "Animals that eat only other animals": "只吃其他动物的动物",
    "Animals that eat both plants and animals": "既吃植物又吃动物的动物",
    "Chemistry, physics, and mathematics": "化学、物理和数学",
    "A testable explanation for observations": "对观察结果的可检验解释",
    "Information collected during an experiment": "实验过程中收集的信息",
    "A factor that can be changed or controlled": "可以改变或控制的因素",
    "Chemical reactions to obtain and use energy": "获取和使用能量的化学反应",
    "An increase in size and/or number of cells": "细胞大小和/或数量的增加",
    "The process of producing offspring": "产生后代的过程",
    "Law of gravity, laws of thermodynamics": "万有引力定律、热力学定律",
    "Cell theory, theory of evolution, germ theory": "细胞学说、进化论、病原体学说",
    "A well-tested explanation supported by extensive evidence": "经过充分验证并有大量证据支持的解释",
    "A description of a natural phenomenon that always occurs": "对总是发生的自然现象的描述",
    "Proper controls, single variable changes, and reproducibility": "适当的对照、单一变量变化和可重复性",
    "To have a baseline for comparing experimental results": "为比较实验结果提供基准",
    "To ensure conclusions are based on facts, not opinions": "确保结论基于事实而非意见",
    "A theory is supported by extensive evidence and testing": "理论有大量证据和测试支持",
    "The variable that the scientist changes or manipulates": "科学家改变或操纵的变量",
    "The variable that is measured in response to changes": "响应变化而测量的变量",
    "The physical place where an organism lives": "生物生活的物理场所",
    "A feeding level in an ecosystem": "生态系统中的摄食级别",
    "A feeding level in a food chain or web": "食物链或食物网中的摄食级别",
    "Interconnected food chains in an ecosystem": "生态系统中相互连接的食物链",
    "Only about 10% of energy transfers to the next trophic level": "只有约10%的能量转移到下一个营养级",
    "Because only 10% of energy passes to each level": "因为每一级只有10%的能量传递",
    "Lost as heat through metabolism": "通过新陈代谢以热量形式损失",
    "Organisms that make their own food through photosynthesis": "通过光合作用自己制造食物的生物",
    "Organisms that obtain energy by eating other organisms": "通过吃其他生物获取能量的生物",
    "Break down dead organisms and recycle nutrients": "分解死亡生物并回收养分",
    "The first organisms to colonize an area during succession": "演替过程中最先定居某地区的生物",
    "A stable, mature ecological community": "稳定、成熟的生态群落",
    "Because soil and seeds are already present": "因为土壤和种子已经存在",
    "Succession that occurs in lifeless areas with no soil": "在没有土壤的无生命地区发生的演替",
    "Succession that occurs after a disturbance when soil remains": "土壤保留时扰动后发生的演替",
    "After a forest fire or abandoned farmland": "森林火灾后或废弃农田",
    "Bees pollinating flowers while getting nectar": "蜜蜂在采蜜时为花授粉",
    "Ticks feeding on dogs, tapeworms in intestines": "蜱虫吸食狗的血，绦虫在肠道中",
    "Water, carbon, nitrogen, and phosphorus cycles": "水、碳、氮和磷循环",
    "It does not have an atmospheric component": "它没有大气成分",
    "The conversion of atmospheric nitrogen into usable forms by bacteria": "细菌将大气氮转化为可用形式",
    "Through photosynthesis, taking in CO2": "通过光合作用，吸收CO2",
    "How is carbon released into the atmosphere?": "碳如何释放到大气中？",
    "Through respiration, decomposition, and combustion": "通过呼吸作用、分解和燃烧",
    "Evaporation, condensation, precipitation, collection": "蒸发、凝结、降水、汇集",
    "Two species cannot occupy the exact same niche indefinitely": "两个物种不能无限期地占据完全相同的生态位",
    "One species will outcompete the other": "一个物种将胜过另一个",
    "Species dividing resources to reduce competition": "物种分配资源以减少竞争",
    "The full range of conditions an organism could potentially use": "生物可能使用的全部条件范围",
    "The actual conditions an organism uses due to competition": "由于竞争生物实际使用的条件",
    "A close, long-term relationship between two different species": "两个不同物种之间的密切、长期关系",
    "A symbiotic relationship where both species benefit": "双方都受益的共生关系",
    "A relationship where one species benefits and the other is unaffected": "一个物种受益而另一个不受影响的关系",
    "A relationship where one species benefits while harming the other": "一个物种受益同时伤害另一个的关系",
    "When one organism kills and eats another": "当一种生物捕食另一种时",
    "An organism that hunts and kills other organisms for food": "捕食其他生物作为食物的生物",
    "An organism that is hunted and eaten by a predator": "被捕食者猎捕和吃掉的生物",
    "When organisms compete for the same limited resources": "当生物为相同的有限资源竞争时",
    "The gradual change in species composition of a community over time": "群落物种组成随时间的逐渐变化",
    "An organism that produces its own food": "自己生产食物的生物",
    "An organism that eats producers (herbivore)": "吃生产者的生物（草食动物）",
    "An organism that eats primary consumers (carnivore)": "吃初级消费者的生物（肉食动物）",
    "A top predator that eats secondary consumers": "吃次级消费者的顶级捕食者",
    "An organism that must eat other organisms for energy": "必须吃其他生物获取能量的生物",
    "The variety of life in an area": "一个地区生命的多样性",
    "The protection and preservation of natural resources": "自然资源的保护和保存",
    "The elimination of natural habitats through human activities": "通过人类活动消除自然栖息地",
    "The clearing of forests for human use": "为人类使用而砍伐森林",
    "Harvesting a resource faster than it can naturally replenish": "以比自然补充更快的速度收获资源",
    "A non-native species that causes harm when introduced to a new ecosystem": "引入新生态系统时造成危害的非本地物种",
    "They outcompete native species for resources": "它们在资源方面胜过本地物种",
    "The growth of cities and conversion of natural areas to urban use": "城市发展和将自然区域转变为城市使用",
    "Air pollution, water pollution, soil pollution": "空气污染、水污染、土壤污染",
    "Energy from sources that are naturally replenished, like solar and wind": "来自自然补充的能源，如太阳能和风能",
    "Activities that meet current needs without compromising future generations": "满足当前需求而不损害后代的活动",
    "The scientific study of life and living organisms": "对生命和生物的科学研究",
    "All members of one species living in the same area": "生活在同一地区的同一物种的所有成员",
    "All populations of different species living in the same area": "生活在同一地区的不同物种的所有种群",
    "A community plus its physical environment": "群落加上其物理环境",
    "All ecosystems on Earth; the global sum of all life": "地球上所有的生态系统；所有生命的全球总和",
    "A group of similar cells working together": "一组相似细胞共同工作",
    "A structure made of different tissues working together": "由不同组织共同工作组成的结构",
    "A specialized structure within a cell that performs a specific function": "细胞内执行特定功能的专门结构",
    "Cells provide structure and carry out life functions": "细胞提供结构并执行生命功能",
    "Through internal regulation of temperature, pH, water, etc.": "通过内部调节温度、pH值、水分等",
    "Organization, metabolism, homeostasis, growth, reproduction, response, adaptation": "组织性、新陈代谢、稳态、生长、繁殖、应激性、适应性",
    "Evolving over generations to better survive in an environment": "通过世代进化以更好地适应环境",
    "Maintaining stable internal conditions": "维持稳定的内部条件",
    "Cell → Tissue → Organ → Organ System → Organism": "细胞 → 组织 → 器官 → 器官系统 → 生物体",
    "From microscopic bacteria to massive ecosystems": "从微观细菌到庞大的生态系统",
    "Understanding health/disease, developing medicines, addressing environmental challenges": "了解健康/疾病、开发药物、应对环境挑战",
    "By understanding causes, prevention, and treatment of illnesses": "通过了解疾病的原因、预防和治疗",
    "By improving crop yields, disease resistance, and food production": "通过提高作物产量、抗病性和粮食生产",
    "It combines principles from chemistry, physics, and math to study life": "它结合化学、物理和数学原理来研究生命",
    "Anatomy studies structure; physiology studies function": "解剖学研究结构；生理学研究功能",
    "A systematic approach to investigating phenomena through observation, hypothesis, experimentation, and conclusion": "通过观察、假设、实验和结论系统研究现象的方法",
    "A group in an experiment that is not exposed to the variable being tested": "实验中不接受测试变量的组",
    "Studies animals in their natural habitats and works on conservation": "研究自然栖息地中的动物并从事保护工作",
    "The use of living systems to develop products and technologies": "利用生命系统开发产品和技术",
    "Applies biological knowledge to solve crimes": "运用生物学知识解决犯罪",
    "The relationships between organisms and their environment": "生物与其环境之间的关系",
    "A scientist who modifies genes to create desired traits": "修改基因以创造所需性状的科学家",
    "Prepares and dispenses medications": "准备和分发药物",
    "Studies crops and soil to improve food production": "研究作物和土壤以改善粮食生产",
    "Through observation, experimentation, and analysis": "通过观察、实验和分析",
    "It helps us understand how living systems work and interact": "它帮助我们了解生命系统如何工作和相互作用",
    "Key concepts, processes, and their significance": "关键概念、过程及其意义",
    "Technical terms and definitions specific to this topic": "特定于该主题的技术术语和定义",
    "Observable phenomena and processes in living organisms": "生物体中可观察的现象和过程",
    "Key principles and terms essential to understanding this topic": "理解该主题所必需的关键原则和术语",
    "It connects to various aspects of cellular function and organism behavior": "它与细胞功能和生物行为的各个方面相关联",
    "Scientific research and experimentation over many years": "多年的科学研究和实验",
    "The recycling of matter through living and non-living parts of an ecosystem": "物质在生态系统的生物和非生物部分之间循环",
    "A single pathway showing how energy flows from one organism to another": "显示能量如何从一个生物流向另一个生物的单一途径",
}

# Pattern templates for generating translations
def translate_what_is(topic):
    """Translate 'What is X?' questions."""
    topic_zh = translate_topic(topic)
    return f"什么是{topic_zh}？"

def translate_topic(topic):
    """Translate a topic name to Chinese."""
    topic_lower = topic.lower().strip().rstrip('?')
    
    # Check direct mapping
    if topic_lower in CORE_TERMS:
        return CORE_TERMS[topic_lower]
    
    # Try compound terms
    for eng, zh in CORE_TERMS.items():
        if eng in topic_lower:
            topic_lower = topic_lower.replace(eng, zh)
    
    return topic_lower

def generate_pattern_translations(strings):
    """Generate translations for patterned strings."""
    translations = {}
    
    for s in strings:
        # Skip if already translated
        if s in DIRECT_TRANSLATIONS:
            translations[s] = DIRECT_TRANSLATIONS[s]
            continue
            
        s_lower = s.lower()
        
        # Pattern: What is X?
        match = re.match(r"what is (?:an? |the )?(.+)\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"什么是{topic_zh}？"
            continue
        
        # Pattern: What are X?
        match = re.match(r"what are (?:the )?(.+)\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"什么是{topic_zh}？"
            continue
            
        # Pattern: Why is X important in biology?
        match = re.match(r"why is (.+) important in biology\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"为什么{topic_zh}在生物学中很重要？"
            continue
            
        # Pattern: How is X studied by scientists?
        match = re.match(r"how is (.+) studied by scientists\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"科学家如何研究{topic_zh}？"
            continue
            
        # Pattern: What applications does X have?
        match = re.match(r"what applications does (.+) have\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"{topic_zh}有什么应用？"
            continue
            
        # Pattern: What are the main concepts in X?
        match = re.match(r"what are the main concepts in (.+)\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"{topic_zh}的主要概念是什么？"
            continue
            
        # Pattern: What are examples of X in nature?
        match = re.match(r"what are examples of (.+) in nature\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"自然界中{topic_zh}的例子有哪些？"
            continue
            
        # Pattern: What should you remember about X?
        match = re.match(r"what should you remember about (.+)\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"关于{topic_zh}，你应该记住什么？"
            continue
            
        # Pattern: What vocabulary is important for X?
        match = re.match(r"what vocabulary is important for (.+)\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"对于{topic_zh}，哪些词汇很重要？"
            continue
            
        # Pattern: How does X relate to other biology topics?
        match = re.match(r"how does (.+) relate to other biology topics\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"{topic_zh}与其他生物学主题有什么关系？"
            continue
            
        # Pattern: What discoveries led to our understanding of X?
        match = re.match(r"what discoveries led to our understanding of (.+)\?", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"哪些发现促进了我们对{topic_zh}的理解？"
            continue
            
        # Pattern: A key topic in biology covering important concepts related to X
        match = re.match(r"a key topic in biology covering important concepts related to (.+)", s_lower)
        if match:
            topic = match.group(1)
            topic_zh = translate_topic(topic)
            translations[s] = f"生物学中涵盖{topic_zh}重要概念的关键主题"
            continue
            
        # Pattern: What does a X do?
        match = re.match(r"what does (?:a |an )?(.+) do\?", s_lower)
        if match:
            role = match.group(1)
            role_zh = translate_topic(role)
            translations[s] = f"{role_zh}是做什么的？"
            continue
            
        # Pattern: Name X
        match = re.match(r"name (?:three |the |four |)(.+)", s_lower)
        if match:
            thing = match.group(1).rstrip('.')
            thing_zh = translate_topic(thing)
            translations[s] = f"列举{thing_zh}。"
            continue
            
        # Pattern: Give an example of X
        match = re.match(r"give an example of (?:a |an |where )?(.+)", s_lower)
        if match:
            thing = match.group(1).rstrip('.')
            thing_zh = translate_topic(thing)
            translations[s] = f"举一个{thing_zh}的例子。"
            continue
            
        # Pattern: How does X?
        match = re.match(r"how does (.+)\?", s_lower)
        if match:
            thing = match.group(1)
            thing_zh = translate_topic(thing)
            translations[s] = f"{thing_zh}是如何的？"
            continue
            
        # Pattern: Why is X?
        match = re.match(r"why is (.+)\?", s_lower)
        if match and "important" not in s_lower:
            thing = match.group(1)
            thing_zh = translate_topic(thing)
            translations[s] = f"为什么{thing_zh}？"
            continue
            
        # Pattern: Why are X?
        match = re.match(r"why are (.+)\?", s_lower)
        if match:
            thing = match.group(1)
            thing_zh = translate_topic(thing)
            translations[s] = f"为什么{thing_zh}？"
            continue
    
    return translations

def add_translations_to_file(translations):
    """Add all translations to global_translations.js."""
    with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Filter out already existing
    new_translations = {}
    existing = 0
    for eng, zh in translations.items():
        eng_escaped = eng.replace('"', '\\"').replace("'", "\\'")
        if f'"{eng}"' not in content and f'"{eng_escaped}"' not in content:
            new_translations[eng] = zh
        else:
            existing += 1
    
    if not new_translations:
        print(f"All {existing} translations already exist.")
        return
    
    # Build new lines
    new_lines = '\n  /* Complete Biology Content Translations */\n'
    for eng, zh in sorted(new_translations.items()):
        eng_escaped = eng.replace('"', '\\"').replace("'", "\\'")
        zh_escaped = zh.replace('"', '\\"').replace("'", "\\'")
        new_lines += f'  "{eng_escaped}": "{zh_escaped}",\n'
    
    # Insert before closing
    match = re.search(r'(\n\};\n\n\s+// Expose translations globally)', content)
    if match:
        insert_pos = match.start(1)
        content = content[:insert_pos] + new_lines + content[insert_pos:]
        
        with open(TRANSLATIONS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Added {len(new_translations)} new translations ({existing} already existed)")
    else:
        print("Could not find insertion point")

def main():
    # Read all strings
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        strings = [line.strip() for line in f if line.strip()]
    
    print(f"Processing {len(strings)} strings...")
    
    # Generate translations
    translations = generate_pattern_translations(strings)
    translations.update(DIRECT_TRANSLATIONS)
    
    print(f"Generated {len(translations)} translations")
    
    # Add to file
    add_translations_to_file(translations)

if __name__ == "__main__":
    main()
