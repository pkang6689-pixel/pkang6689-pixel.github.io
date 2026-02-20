#!/usr/bin/env python3
"""
Fix partial translations in global_translations.js
Replace mixed English/Chinese with proper full Chinese translations.
"""

from pathlib import Path
import re

TRANSLATIONS_FILE = Path(r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js")

# Full topic translations for compound phrases
TOPIC_TRANSLATIONS = {
    # Unit topics
    "aquatic ecosystems": "水生生态系统",
    "terrestrial biomes": "陆地生物群落",
    "astrobiology and the search for life beyond earth": "天体生物学和地球外生命的探索",
    "biochemistry in everyday life": "日常生活中的生物化学",
    "biodiversity": "生物多样性",
    "bioethics (cloning, stem cells, genetic privacy)": "生物伦理学（克隆、干细胞、基因隐私）",
    "biotechnology (crispr, cloning, gmos)": "生物技术（CRISPR、克隆、转基因生物）",
    "biotechnology and genetic engineering": "生物技术与基因工程",
    "carrying capacity and limiting factors": "承载力和限制因素",
    "cell discovery and theory": "细胞发现与学说",
    "cell structure and function": "细胞结构与功能",
    "cellular reproduction": "细胞繁殖",
    "cellular respiration": "细胞呼吸",
    "cellular transport": "细胞运输",
    "chemical energy and atp": "化学能和ATP",
    "chemical reactions and enzymes": "化学反应和酶",
    "circulatory system": "循环系统",
    "climate change and ecosystem shifts": "气候变化和生态系统变迁",
    "community ecology": "群落生态学",
    "conservation and sustainable development": "保护与可持续发展",
    "conserving biodiversity": "保护生物多样性",
    "digestive system": "消化系统",
    "dna and rna": "DNA和RNA",
    "dna replication, transcription, and translation": "DNA复制、转录和翻译",
    "endangered species and conservation strategies": "濒危物种和保护策略",
    "endocrine system": "内分泌系统",
    "energy flow in living systems": "生命系统中的能量流动",
    "environmental biology": "环境生物学",
    "fermentation": "发酵",
    "gene regulation and expression": "基因调控与表达",
    "global conservation efforts": "全球保护工作",
    "homeostasis": "稳态",
    "how organisms obtain energy": "生物如何获取能量",
    "human genetics and genetic disorders": "人类遗传学和遗传疾病",
    "human population growth and demographics": "人口增长和人口统计",
    "immune system": "免疫系统",
    "matter and atomic structure": "物质和原子结构",
    "medicine and pharmacology": "医学和药理学",
    "meiosis and sexual reproduction": "减数分裂和有性生殖",
    "mendelian genetics": "孟德尔遗传学",
    "microscopy and cell imaging": "显微镜术和细胞成像",
    "mitosis": "有丝分裂",
    "nervous system": "神经系统",
    "non-mendelian genetics": "非孟德尔遗传学",
    "organization of the human body": "人体组织",
    "photosynthesis": "光合作用",
    "population dynamics": "种群动态",
    "population regulation": "种群调节",
    "prokaryotic vs. eukaryotic cells": "原核细胞与真核细胞",
    "reproductive system": "生殖系统",
    "respiratory system": "呼吸系统",
    "stem cells and regenerative medicine": "干细胞和再生医学", 
    "structures and organelles": "结构与细胞器",
    "symbiosis and species interactions": "共生与物种相互作用",
    "the building blocks of life": "生命的组成单元",
    "the cell cycle and cancer": "细胞周期与癌症",
    "the plasma membrane": "质膜",
    "threats to biodiversity": "生物多样性的威胁",
    "water and its solutions": "水及其溶液",
    "ecological succession": "生态演替",
    "primary and secondary succession": "初级演替和次级演替",
    "energy in ecosystems": "生态系统中的能量",
    "food chains and food webs": "食物链和食物网",
    "biogeochemical cycles": "生物地球化学循环",
    "nitrogen and phosphorus cycles": "氮循环和磷循环",
    "the carbon and water cycles": "碳循环和水循环",
    "trophic levels and energy transfer": "营养级和能量传递",
    "producers, consumers, and decomposers": "生产者、消费者和分解者",
    "competition and predation": "竞争与捕食",
    "introduction to ecology": "生态学导论",
    "characteristics of life": "生命的特征",
    "introduction to biology": "生物学导论",
    "branches of biology": "生物学分支",
    "careers in biology": "生物学职业",
    "the scientific method": "科学方法",
    "scientific theories, laws, and hypotheses": "科学理论、定律和假说",
}

def fix_translations():
    with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixes_made = 0
    
    # Pattern-based replacements
    replacements = []
    
    for eng_topic, zh_topic in TOPIC_TRANSLATIONS.items():
        # Fix: What vocabulary is important for X?
        old_trans = content
        pattern = rf'"What vocabulary is important for {re.escape(eng_topic)}\?": "[^"]*"'
        new_val = f'"What vocabulary is important for {eng_topic}?": "对于{zh_topic}，哪些词汇很重要？"'
        content = re.sub(pattern, new_val, content, flags=re.IGNORECASE)
        
        # Fix: What should you remember about X?
        pattern = rf'"What should you remember about {re.escape(eng_topic)}\?": "[^"]*"'
        new_val = f'"What should you remember about {eng_topic}?": "关于{zh_topic}，你应该记住什么？"'
        content = re.sub(pattern, new_val, content, flags=re.IGNORECASE)
        
        # Fix: Why is X important in biology?
        pattern = rf'"Why is {re.escape(eng_topic)} important in biology\?": "[^"]*"'
        new_val = f'"Why is {eng_topic} important in biology?": "为什么{zh_topic}在生物学中很重要？"'
        content = re.sub(pattern, new_val, content, flags=re.IGNORECASE)
        
        # Fix: How is X studied by scientists?
        pattern = rf'"How is {re.escape(eng_topic)} studied by scientists\?": "[^"]*"'
        new_val = f'"How is {eng_topic} studied by scientists?": "科学家如何研究{zh_topic}？"'
        content = re.sub(pattern, new_val, content, flags=re.IGNORECASE)
        
        # Fix: What applications does X have?
        pattern = rf'"What applications does {re.escape(eng_topic)} have\?": "[^"]*"'
        new_val = f'"What applications does {eng_topic} have?": "{zh_topic}有什么应用？"'
        content = re.sub(pattern, new_val, content, flags=re.IGNORECASE)
        
        # Fix: What are the main concepts in X?
        pattern = rf'"What are the main concepts in {re.escape(eng_topic)}\?": "[^"]*"'
        new_val = f'"What are the main concepts in {eng_topic}?": "{zh_topic}的主要概念是什么？"'
        content = re.sub(pattern, new_val, content, flags=re.IGNORECASE)
        
        # Fix: What are examples of X in nature?
        pattern = rf'"What are examples of {re.escape(eng_topic)} in nature\?": "[^"]*"'
        new_val = f'"What are examples of {eng_topic} in nature?": "自然界中{zh_topic}的例子有哪些？"'
        content = re.sub(pattern, new_val, content, flags=re.IGNORECASE)
        
        # Fix: How does X relate to other biology topics?
        pattern = rf'"How does {re.escape(eng_topic)} relate to other biology topics\?": "[^"]*"'
        new_val = f'"How does {eng_topic} relate to other biology topics?": "{zh_topic}与其他生物学主题有什么关系？"'
        content = re.sub(pattern, new_val, content, flags=re.IGNORECASE)
        
        # Fix: What discoveries led to our understanding of X?
        pattern = rf'"What discoveries led to our understanding of {re.escape(eng_topic)}\?": "[^"]*"'
        new_val = f'"What discoveries led to our understanding of {eng_topic}?": "哪些发现促进了我们对{zh_topic}的理解？"'
        content = re.sub(pattern, new_val, content, flags=re.IGNORECASE)
        
        # Fix: A key topic in biology covering important concepts related to X
        pattern = rf'"A key topic in biology covering important concepts related to {re.escape(eng_topic)}": "[^"]*"'
        new_val = f'"A key topic in biology covering important concepts related to {eng_topic}": "生物学中涵盖{zh_topic}重要概念的关键主题"'
        content = re.sub(pattern, new_val, content, flags=re.IGNORECASE)
    
    # Also fix some specific broken translations
    specific_fixes = {
        # Why are there few top predators?
        '"Why are there few top predators?": "为什么there few top 捕食者s？"': 
            '"Why are there few top predators?": "为什么顶级捕食者很少？"',
    }
    
    for old, new in specific_fixes.items():
        if old in content:
            content = content.replace(old, new)
            fixes_made += 1
    
    with open(TRANSLATIONS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed translations in global_translations.js")

if __name__ == "__main__":
    fix_translations()
