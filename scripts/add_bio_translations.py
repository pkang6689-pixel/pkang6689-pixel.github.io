#!/usr/bin/env python3
"""Add biology lesson translations to global_translations.js"""

import re
import os

TRANSLATIONS_FILE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js"

# Biology lesson translations (English -> Chinese)
BIO_TRANSLATIONS = {
    # Unit names
    "Unit 1": "第一单元",
    "Unit 2": "第二单元",
    "Unit 3": "第三单元",
    "Unit 4": "第四单元",
    "Unit 5": "第五单元",
    "Unit 6": "第六单元",
    "Unit 7": "第七单元",
    "Unit 8": "第八单元",
    "Unit 9": "第九单元",
    "Unit 10": "第十单元",
    "Unit 11": "第十一单元",
    "Unit 12": "第十二单元",
    
    # Unit Test names
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
    
    # Unit 1: The Study of Life
    "The Study of Life": "生命的研究",
    "1.1 Introduction to Biology": "1.1 生物学导论",
    "1.2 The Science of Life": "1.2 生命科学",
    "1.3 The Nature of Science": "1.3 科学的本质",
    "1.4 Characteristics of Life": "1.4 生命的特征",
    "1.5 Levels of Biological Organization": "1.5 生物组织层次",
    "1.6 Branches of Biology": "1.6 生物学分支",
    "1.7 Careers in Biology": "1.7 生物学职业",
    
    # Unit 2: Ecology
    "Ecology": "生态学",
    "2.1 Organisms and Their Relationships": "2.1 生物及其关系",
    "2.2 Flow of Energy in an Ecosystem": "2.2 生态系统中的能量流动",
    "2.3 Cycling of Matter": "2.3 物质循环",
    "2.4 Ecological Succession": "2.4 生态演替",
    "2.5 Niches and Habitat": "2.5 生态位与栖息地",
    "2.6 Food Chains, Webs, and Trophic Levels": "2.6 食物链、食物网与营养级",
    "2.7 Human Impact on Ecosystems": "2.7 人类对生态系统的影响",
    
    # Unit 3: The Biosphere
    "The Biosphere": "生物圈",
    "3.1 Community Ecology": "3.1 群落生态学",
    "3.2 Biomes and Biodiversity": "3.2 生物群落与生物多样性",
    "3.3 Climate and Weather Patterns": "3.3 气候与天气模式",
    "3.4 Terrestrial Biomes": "3.4 陆地生物群落",
    "3.5 Aquatic Ecosystems": "3.5 水生生态系统",
    
    # Unit 4: Evolution
    "Evolution": "进化",
    "4.1 History of Evolutionary Thought": "4.1 进化思想史",
    "4.2 Evidence of Evolution": "4.2 进化的证据",
    "4.3 Sources of Genetic Variation": "4.3 遗传变异的来源",
    "4.4 Hardy-Weinberg Equilibrium": "4.4 哈迪-温伯格平衡",
    "4.5 Natural Selection and Adaptation": "4.5 自然选择与适应",
    "4.6 Population Dynamics": "4.6 种群动态",
    
    # Unit 5: Classification
    "Classification": "分类学",
    "5.1 Taxonomy Basics": "5.1 分类学基础",
    "5.2 Cladistics and Classification": "5.2 支序分类学与分类",
    "5.3 Phylogenetic Trees": "5.3 系统发育树",
    "5.4 Patterns of Evolution": "5.4 进化模式",
    "5.5 Speciation": "5.5 物种形成",
    "5.6 Domains and Kingdoms of Life": "5.6 生物的域与界",
    
    # Unit 6: Cells
    "Cells": "细胞",
    "6.1 Introduction to Cells": "6.1 细胞导论",
    "6.2 Prokaryotic vs Eukaryotic Cells": "6.2 原核细胞与真核细胞",
    "6.3 Organelles and Their Functions": "6.3 细胞器及其功能",
    "6.4 Membrane Transport": "6.4 膜运输",
    "6.5 Cell Communication": "6.5 细胞通讯",
    "6.6 Homeostasis": "6.6 稳态",
    
    # Unit 7: Cellular Respiration
    "Cellular Respiration": "细胞呼吸",
    "7.1 Overview of Cellular Respiration": "7.1 细胞呼吸概述",
    "7.2 ATP and Cellular Energy": "7.2 ATP与细胞能量",
    "7.3 Glycolysis": "7.3 糖酵解",
    "7.4 The Krebs Cycle": "7.4 克雷布斯循环",
    "7.5 The Electron Transport Chain": "7.5 电子传递链",
    "7.6 Fermentation": "7.6 发酵",
    
    # Unit 8: Photosynthesis
    "Photosynthesis": "光合作用",
    "8.1 Overview of Photosynthesis": "8.1 光合作用概述",
    "8.2 Chloroplast Structure": "8.2 叶绿体结构",
    "8.3 Light-Dependent Reactions": "8.3 光反应",
    "8.4 The Calvin Cycle": "8.4 卡尔文循环",
    "8.5 Factors Affecting Photosynthesis": "8.5 影响光合作用的因素",
    
    # Unit 9: Cell Cycle
    "Cell Cycle": "细胞周期",
    "Cell Division": "细胞分裂",
    "9.1 Cell Growth and Division": "9.1 细胞生长与分裂",
    "9.2 The Cell Cycle": "9.2 细胞周期",
    "9.3 Mitosis": "9.3 有丝分裂",
    "9.4 Cytokinesis": "9.4 胞质分裂",
    "9.5 Cell Cycle Regulation and Cancer": "9.5 细胞周期调控与癌症",
    
    # Unit 10: Meiosis
    "Meiosis": "减数分裂",
    "10.1 Overview of Meiosis": "10.1 减数分裂概述",
    "10.2 Sexual Reproduction": "10.2 有性生殖",
    "10.3 Meiosis I": "10.3 减数分裂I",
    "10.4 Meiosis II": "10.4 减数分裂II",
    "10.5 Crossing Over and Genetic Variation": "10.5 交叉互换与遗传变异",
    "10.6 Nondisjunction and Genetic Disorders": "10.6 染色体不分离与遗传疾病",
    
    # Unit 11: Genetics
    "Genetics": "遗传学",
    "Mendelian Genetics": "孟德尔遗传学",
    "11.1 Mendel and the Laws of Inheritance": "11.1 孟德尔与遗传定律",
    "11.2 Monohybrid Crosses": "11.2 单因子杂交",
    "11.3 Dihybrid Crosses": "11.3 双因子杂交",
    "11.4 Non-Mendelian Inheritance": "11.4 非孟德尔遗传",
    "11.5 Polygenic and Multifactorial Traits": "11.5 多基因与多因素性状",
    "11.6 Human Genetics and Pedigrees": "11.6 人类遗传学与家系图",
    
    # Unit 12: Molecular Biology
    "Molecular Biology": "分子生物学",
    "DNA and Biotechnology": "DNA与生物技术",
    "12.1 DNA Structure": "12.1 DNA结构",
    "12.2 DNA Replication": "12.2 DNA复制",
    "12.3 RNA and Transcription": "12.3 RNA与转录",
    "12.4 Protein Synthesis": "12.4 蛋白质合成",
    "12.5 Genetic Engineering": "12.5 基因工程",
    "12.6 Biotechnology Applications": "12.6 生物技术应用",
    
    # Page titles with Lesson prefix
    "Lesson 1.1: Introduction to Biology": "第1.1课：生物学导论",
    "Lesson 1.2: The Science of Life": "第1.2课：生命科学",
    "Lesson 1.3: The Nature of Science": "第1.3课：科学的本质",
    "Lesson 1.4: Characteristics of Life": "第1.4课：生命的特征",
    "Lesson 1.5: Levels of Biological Organization": "第1.5课：生物组织层次",
    "Lesson 1.6: Branches of Biology": "第1.6课：生物学分支",
    "Lesson 1.7: Careers in Biology": "第1.7课：生物学职业",
    
    "Lesson 2.1: Organisms and Their Relationships": "第2.1课：生物及其关系",
    "Lesson 2.2: Flow of Energy in an Ecosystem": "第2.2课：生态系统中的能量流动",
    "Lesson 2.3: Cycling of Matter": "第2.3课：物质循环",
    "Lesson 2.4: Ecological Succession": "第2.4课：生态演替",
    "Lesson 2.5: Niches and Habitat": "第2.5课：生态位与栖息地",
    "Lesson 2.6: Food Chains, Webs, and Trophic Levels": "第2.6课：食物链、食物网与营养级",
    "Lesson 2.7: Human Impact on Ecosystems": "第2.7课：人类对生态系统的影响",
    
    "Lesson 3.1: Community Ecology": "第3.1课：群落生态学",
    "Lesson 3.2: Biomes and Biodiversity": "第3.2课：生物群落与生物多样性",
    "Lesson 3.3: Climate and Weather Patterns": "第3.3课：气候与天气模式",
    "Lesson 3.4: Terrestrial Biomes": "第3.4课：陆地生物群落",
    "Lesson 3.5: Aquatic Ecosystems": "第3.5课：水生生态系统",
    
    "Lesson 4.1: History of Evolutionary Thought": "第4.1课：进化思想史",
    "Lesson 4.2: Evidence of Evolution": "第4.2课：进化的证据",
    "Lesson 4.3: Sources of Genetic Variation": "第4.3课：遗传变异的来源",
    "Lesson 4.4: Hardy-Weinberg Equilibrium": "第4.4课：哈迪-温伯格平衡",
    "Lesson 4.5: Natural Selection and Adaptation": "第4.5课：自然选择与适应",
    "Lesson 4.6: Population Dynamics": "第4.6课：种群动态",
    
    "Lesson 5.1: Taxonomy Basics": "第5.1课：分类学基础",
    "Lesson 5.2: Cladistics and Classification": "第5.2课：支序分类学与分类",
    "Lesson 5.3: Phylogenetic Trees": "第5.3课：系统发育树",
    "Lesson 5.4: Patterns of Evolution": "第5.4课：进化模式",
    "Lesson 5.5: Speciation": "第5.5课：物种形成",
    "Lesson 5.6: Domains and Kingdoms of Life": "第5.6课：生物的域与界",
    
    "Lesson 6.1: Introduction to Cells": "第6.1课：细胞导论",
    "Lesson 6.2: Prokaryotic vs Eukaryotic Cells": "第6.2课：原核细胞与真核细胞",
    "Lesson 6.3: Organelles and Their Functions": "第6.3课：细胞器及其功能",
    "Lesson 6.4: Membrane Transport": "第6.4课：膜运输",
    "Lesson 6.5: Cell Communication": "第6.5课：细胞通讯",
    "Lesson 6.6: Homeostasis": "第6.6课：稳态",
    
    "Lesson 7.1: Overview of Cellular Respiration": "第7.1课：细胞呼吸概述",
    "Lesson 7.2: ATP and Cellular Energy": "第7.2课：ATP与细胞能量",
    "Lesson 7.3: Glycolysis": "第7.3课：糖酵解",
    "Lesson 7.4: The Krebs Cycle": "第7.4课：克雷布斯循环",
    "Lesson 7.5: The Electron Transport Chain": "第7.5课：电子传递链",
    "Lesson 7.6: Fermentation": "第7.6课：发酵",
    
    "Lesson 8.1: Overview of Photosynthesis": "第8.1课：光合作用概述",
    "Lesson 8.2: Chloroplast Structure": "第8.2课：叶绿体结构",
    "Lesson 8.3: Light-Dependent Reactions": "第8.3课：光反应",
    "Lesson 8.4: The Calvin Cycle": "第8.4课：卡尔文循环",
    "Lesson 8.5: Factors Affecting Photosynthesis": "第8.5课：影响光合作用的因素",
    
    "Lesson 9.1: Cell Growth and Division": "第9.1课：细胞生长与分裂",
    "Lesson 9.2: The Cell Cycle": "第9.2课：细胞周期",
    "Lesson 9.3: Mitosis": "第9.3课：有丝分裂",
    "Lesson 9.4: Cytokinesis": "第9.4课：胞质分裂",
    "Lesson 9.5: Cell Cycle Regulation and Cancer": "第9.5课：细胞周期调控与癌症",
    
    "Lesson 10.1: Overview of Meiosis": "第10.1课：减数分裂概述",
    "Lesson 10.2: Sexual Reproduction": "第10.2课：有性生殖",
    "Lesson 10.3: Meiosis I": "第10.3课：减数分裂I",
    "Lesson 10.4: Meiosis II": "第10.4课：减数分裂II",
    "Lesson 10.5: Crossing Over and Genetic Variation": "第10.5课：交叉互换与遗传变异",
    "Lesson 10.6: Nondisjunction and Genetic Disorders": "第10.6课：染色体不分离与遗传疾病",
    
    "Lesson 11.1: Mendel and the Laws of Inheritance": "第11.1课：孟德尔与遗传定律",
    "Lesson 11.2: Monohybrid Crosses": "第11.2课：单因子杂交",
    "Lesson 11.3: Dihybrid Crosses": "第11.3课：双因子杂交",
    "Lesson 11.4: Non-Mendelian Inheritance": "第11.4课：非孟德尔遗传",
    "Lesson 11.5: Polygenic and Multifactorial Traits": "第11.5课：多基因与多因素性状",
    "Lesson 11.6: Human Genetics and Pedigrees": "第11.6课：人类遗传学与家系图",
    
    "Lesson 12.1: DNA Structure": "第12.1课：DNA结构",
    "Lesson 12.2: DNA Replication": "第12.2课：DNA复制",
    "Lesson 12.3: RNA and Transcription": "第12.3课：RNA与转录",
    "Lesson 12.4: Protein Synthesis": "第12.4课：蛋白质合成",
    "Lesson 12.5: Genetic Engineering": "第12.5课：基因工程",
    "Lesson 12.6: Biotechnology Applications": "第12.6课：生物技术应用",
    
    # Practice page titles
    "Lesson 1.1: Introduction to Biology Practice": "第1.1课：生物学导论 练习",
    "Lesson 1.2: The Science of Life Practice": "第1.2课：生命科学 练习",
    "Lesson 1.3: The Nature of Science Practice": "第1.3课：科学的本质 练习",
    "Lesson 1.4: Characteristics of Life Practice": "第1.4课：生命的特征 练习",
    "Lesson 1.5: Levels of Biological Organization Practice": "第1.5课：生物组织层次 练习",
    "Lesson 1.6: Branches of Biology Practice": "第1.6课：生物学分支 练习",
    "Lesson 1.7: Careers in Biology Practice": "第1.7课：生物学职业 练习",
    
    # Quiz page titles
    "Lesson 1.1: Introduction to Biology Quiz": "第1.1课：生物学导论 测验",
    "Lesson 1.2: The Science of Life Quiz": "第1.2课：生命科学 测验",
    "Lesson 1.3: The Nature of Science Quiz": "第1.3课：科学的本质 测验",
    "Lesson 1.4: Characteristics of Life Quiz": "第1.4课：生命的特征 测验",
    "Lesson 1.5: Levels of Biological Organization Quiz": "第1.5课：生物组织层次 测验",
    "Lesson 1.6: Branches of Biology Quiz": "第1.6课：生物学分支 测验",
    "Lesson 1.7: Careers in Biology Quiz": "第1.7课：生物学职业 测验",
    
    # Unit Test page titles
    "Unit 1: The Study of Life - Unit Test": "第一单元：生命的研究 - 单元测试",
    "Unit 2: Ecology - Unit Test": "第二单元：生态学 - 单元测试",
    "Unit 3: The Biosphere - Unit Test": "第三单元：生物圈 - 单元测试",
    "Unit 4: Evolution - Unit Test": "第四单元：进化 - 单元测试",
    "Unit 5: Classification - Unit Test": "第五单元：分类学 - 单元测试",
    "Unit 6: Cells - Unit Test": "第六单元：细胞 - 单元测试",
    "Unit 7: Cellular Respiration - Unit Test": "第七单元：细胞呼吸 - 单元测试",
    "Unit 8: Photosynthesis - Unit Test": "第八单元：光合作用 - 单元测试",
    "Unit 9: Cell Cycle - Unit Test": "第九单元：细胞周期 - 单元测试",
    "Unit 10: Meiosis - Unit Test": "第十单元：减数分裂 - 单元测试",
    "Unit 11: Genetics - Unit Test": "第十一单元：遗传学 - 单元测试",
    "Unit 12: Molecular Biology - Unit Test": "第十二单元：分子生物学 - 单元测试",
    
    # Review Flashcards titles
    "Unit 1 Review Flashcards": "第一单元 复习卡片",
    "Unit 2 Review Flashcards": "第二单元 复习卡片",
    "Unit 3 Review Flashcards": "第三单元 复习卡片",
    "Unit 4 Review Flashcards": "第四单元 复习卡片",
    "Unit 5 Review Flashcards": "第五单元 复习卡片",
    "Unit 6 Review Flashcards": "第六单元 复习卡片",
    "Unit 7 Review Flashcards": "第七单元 复习卡片",
    "Unit 8 Review Flashcards": "第八单元 复习卡片",
    "Unit 9 Review Flashcards": "第九单元 复习卡片",
    "Unit 10 Review Flashcards": "第十单元 复习卡片",
    "Unit 11 Review Flashcards": "第十一单元 复习卡片",
    "Unit 12 Review Flashcards": "第十二单元 复习卡片",
    
    # Navigation buttons
    "Start Unit Test": "开始单元测试",
    "Review Flashcards": "复习卡片",
    "Back to Biology": "返回生物",
    "Next Up: Quiz": "下一步：测验",
    "Next Up: Summary": "下一步：总结",
    "Next Up: Practice": "下一步：练习",
    
    # Common UI elements
    "High School Biology": "高中生物",
    "High School: Biology": "高中：生物",
    "Check Answer": "检查答案",
    "Get another question": "获取另一个问题",
    "Attempts left:": "剩余尝试次数：",
    "Shuffle": "随机排列",
}

def add_translations():
    with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if biology translations already exist
    if '/* Biology Lesson Translations */' in content:
        print("Biology translations already exist. Skipping.")
        return
    
    # Build the new translations string
    new_translations = '\n  /* Biology Lesson Translations */\n'
    for eng, zh in BIO_TRANSLATIONS.items():
        # Escape quotes
        eng_escaped = eng.replace('"', '\\"')
        zh_escaped = zh.replace('"', '\\"')
        new_translations += f'  "{eng_escaped}": "{zh_escaped}",\n'
    
    # Find the end of the translations object - looking for:  };\n\n    // Expose translations globally
    match = re.search(r'(\n\};\n\n\s+// Expose translations globally)', content)
    if match:
        insert_pos = match.start(1)
        content = content[:insert_pos] + new_translations + content[insert_pos:]
        
        with open(TRANSLATIONS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Added {len(BIO_TRANSLATIONS)} biology translations to global_translations.js")
    else:
        print("Could not find insertion point in global_translations.js")

if __name__ == "__main__":
    add_translations()
