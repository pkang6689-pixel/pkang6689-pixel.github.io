#!/usr/bin/env python3
"""
Extract and translate biology lesson content (flashcards, quizzes, summaries).
This generates translations for global_translations.js.
"""

import os
import re
import json
from pathlib import Path

BASE_PATH = Path(r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\BiologyLessons")
TRANSLATIONS_FILE = Path(r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js")

# Pre-defined translations for common biology terms and phrases
BIOLOGY_VOCAB = {
    # Common terms
    "biology": "生物学",
    "Biology": "生物学",
    "life": "生命",
    "Life": "生命",
    "organisms": "生物",
    "Organisms": "生物",
    "organism": "生物",
    "Organism": "生物",
    "cells": "细胞",
    "cell": "细胞",
    "Cell": "细胞",
    "Cells": "细胞",
    "DNA": "DNA",
    "RNA": "RNA",
    "ATP": "ATP",
    "ecosystem": "生态系统",
    "Ecosystem": "生态系统",
    "evolution": "进化",
    "Evolution": "进化",
    "genetics": "遗传学",
    "Genetics": "遗传学",
    "photosynthesis": "光合作用",
    "Photosynthesis": "光合作用",
    "respiration": "呼吸作用",
    "Respiration": "呼吸作用",
    "metabolism": "新陈代谢",
    "Metabolism": "新陈代谢",
    "homeostasis": "稳态",
    "Homeostasis": "稳态",
    "mitosis": "有丝分裂",
    "Mitosis": "有丝分裂",
    "meiosis": "减数分裂",
    "Meiosis": "减数分裂",
    "protein": "蛋白质",
    "Protein": "蛋白质",
    "enzyme": "酶",
    "Enzyme": "酶",
    "chromosome": "染色体",
    "Chromosome": "染色体",
    "gene": "基因",
    "Gene": "基因",
    "allele": "等位基因",
    "Allele": "等位基因",
    "species": "物种",
    "Species": "物种",
    "population": "种群",
    "Population": "种群",
    "community": "群落",
    "Community": "群落",
    "biome": "生物群落",
    "Biome": "生物群落",
    "biosphere": "生物圈",
    "Biosphere": "生物圈",
    "ecology": "生态学",
    "Ecology": "生态学",
    "energy": "能量",
    "Energy": "能量",
    "producer": "生产者",
    "Producer": "生产者",
    "consumer": "消费者",
    "Consumer": "消费者",
    "decomposer": "分解者",
    "Decomposer": "分解者",
    "nucleus": "细胞核",
    "Nucleus": "细胞核",
    "cytoplasm": "细胞质",
    "Cytoplasm": "细胞质",
    "membrane": "膜",
    "Membrane": "膜",
    "mitochondria": "线粒体",
    "Mitochondria": "线粒体",
    "chloroplast": "叶绿体",
    "Chloroplast": "叶绿体",
    "ribosome": "核糖体",
    "Ribosome": "核糖体",
    "prokaryote": "原核生物",
    "Prokaryote": "原核生物",
    "eukaryote": "真核生物",
    "Eukaryote": "真核生物",
    "prokaryotic": "原核的",
    "Prokaryotic": "原核的",
    "eukaryotic": "真核的",
    "Eukaryotic": "真核的",
    "heredity": "遗传",
    "Heredity": "遗传",
    "inheritance": "遗传",
    "Inheritance": "遗传",
    "dominant": "显性",
    "Dominant": "显性",
    "recessive": "隐性",
    "Recessive": "隐性",
    "genotype": "基因型",
    "Genotype": "基因型",
    "phenotype": "表型",
    "Phenotype": "表型",
    "mutation": "突变",
    "Mutation": "突变",
    "adaptation": "适应",
    "Adaptation": "适应",
    "natural selection": "自然选择",
    "Natural selection": "自然选择",
    "Natural Selection": "自然选择",
    "fossil": "化石",
    "Fossil": "化石",
    "taxonomy": "分类学",
    "Taxonomy": "分类学",
    "kingdom": "界",
    "Kingdom": "界",
    "domain": "域",
    "Domain": "域",
    "phylum": "门",
    "Phylum": "门",
    "class": "纲",
    "Class": "纲",
    "order": "目",
    "Order": "目",
    "family": "科",
    "Family": "科",
    "genus": "属",
    "Genus": "属",
    "bacteria": "细菌",
    "Bacteria": "细菌",
    "virus": "病毒",
    "Virus": "病毒",
    "fungi": "真菌",
    "Fungi": "真菌",
    "plant": "植物",
    "Plant": "植物",
    "animal": "动物",
    "Animal": "动物",
    "tissue": "组织",
    "Tissue": "组织",
    "organ": "器官",
    "Organ": "器官",
    "system": "系统",
    "System": "系统",
    "True": "正确",
    "False": "错误",
    "true": "正确",
    "false": "错误",
}

# Complete flashcard translations for all units
FLASHCARD_TRANSLATIONS = {
    # Unit 1 - Introduction to Biology
    "What is biology?": "什么是生物学？",
    "The scientific study of life and living organisms": "对生命和生物的科学研究",
    "What does 'bios' mean in Greek?": "'bios' 在希腊语中是什么意思？",
    "Life": "生命",
    "What does 'logos' mean in Greek?": "'logos' 在希腊语中是什么意思？",
    "Study or knowledge": "研究或知识",
    "Name three reasons to study biology.": "列举三个学习生物学的原因。",
    "Understanding health/disease, developing medicines, addressing environmental challenges": "了解健康/疾病、开发药物、应对环境挑战",
    "What sciences does modern biology integrate?": "现代生物学整合了哪些科学？",
    "Chemistry, physics, and mathematics": "化学、物理和数学",
    "What is the scope of biology?": "生物学的范围是什么？",
    "From microscopic bacteria to massive ecosystems": "从微观的细菌到庞大的生态系统",
    "How does biology help with disease?": "生物学如何帮助对抗疾病？",
    "By understanding causes, prevention, and treatment of illnesses": "通过了解疾病的原因、预防和治疗",
    "How does biology impact agriculture?": "生物学如何影响农业？",
    "By improving crop yields, disease resistance, and food production": "通过提高作物产量、抗病性和食品生产",
    "What makes something 'living'?": "什么使某物成为'活的'？",
    "It exhibits characteristics of life like metabolism, growth, and reproduction": "它表现出新陈代谢、生长和繁殖等生命特征",
    "Why is biology considered an interdisciplinary science?": "为什么生物学被认为是一门跨学科科学？",
    "It combines principles from chemistry, physics, and math to study life": "它结合化学、物理和数学原理来研究生命",
    
    # Scientific Method
    "What is the scientific method?": "什么是科学方法？",
    "A systematic approach to investigating phenomena through observation, hypothesis, experimentation, and conclusion": "通过观察、假设、实验和结论来系统研究现象的方法",
    "What is a hypothesis?": "什么是假设？",
    "A testable explanation for observations": "对观察结果的可检验解释",
    "What is a control group?": "什么是对照组？",
    "A group in an experiment that is not exposed to the variable being tested": "实验中不接受测试变量的组",
    "What does 'reproducible' mean in science?": "在科学中'可重复性'是什么意思？",
    "Other scientists can repeat the experiment and get the same results": "其他科学家可以重复实验并得到相同的结果",
    "What is a variable in an experiment?": "实验中的变量是什么？",
    "A factor that can be changed or controlled": "可以改变或控制的因素",
    "What is the independent variable?": "什么是自变量？",
    "The variable that the scientist changes or manipulates": "科学家改变或操纵的变量",
    "What is the dependent variable?": "什么是因变量？",
    "The variable that is measured in response to changes": "响应变化而测量的变量",
    "What is data in science?": "在科学中数据是什么？",
    "Information collected during an experiment": "实验过程中收集的信息",
    "Why do scientists use controls?": "为什么科学家使用对照？",
    "To have a baseline for comparing experimental results": "为比较实验结果提供基线",
    "What makes an experiment valid?": "什么使实验有效？",
    "Proper controls, single variable changes, and reproducibility": "适当的对照、单一变量变化和可重复性",
    
    # Nature of Science
    "What does 'empirical' mean?": "'经验性'是什么意思？",
    "Based on observation and experimentation": "基于观察和实验",
    "What is a scientific theory?": "什么是科学理论？",
    "A well-tested explanation supported by extensive evidence": "经过充分验证并有大量证据支持的解释",
    "What is a scientific law?": "什么是科学定律？",
    "A description of a natural phenomenon that always occurs": "对总是发生的自然现象的描述",
    "Why is science considered 'tentative'?": "为什么科学被认为是'暂时性的'？",
    "Because conclusions can change with new evidence": "因为结论可能随着新证据而改变",
    "What does 'objective' mean in science?": "在科学中'客观'是什么意思？",
    "Minimizing personal bias in observations and conclusions": "在观察和结论中尽量减少个人偏见",
    "Give an example of a scientific theory.": "举一个科学理论的例子。",
    "Cell theory, theory of evolution, germ theory": "细胞学说、进化论、病菌学说",
    "Give an example of a scientific law.": "举一个科学定律的例子。",
    "Law of gravity, laws of thermodynamics": "万有引力定律、热力学定律",
    "What does 'testable' mean?": "'可检验'是什么意思？",
    "Claims can be verified or proven false through experimentation": "主张可以通过实验验证或证明为假",
    "How is a theory different from a guess?": "理论与猜测有什么不同？",
    "A theory is supported by extensive evidence and testing": "理论有大量证据和测试支持",
    "Why must science be evidence-based?": "为什么科学必须基于证据？",
    "To ensure conclusions are based on facts, not opinions": "确保结论基于事实而非意见",
    
    # Characteristics of Life
    "What is homeostasis?": "什么是稳态？",
    "Maintaining stable internal conditions": "维持稳定的内部环境",
    "What is metabolism?": "什么是新陈代谢？",
    "Chemical reactions to obtain and use energy": "获取和使用能量的化学反应",
    "What is the basic unit of life?": "生命的基本单位是什么？",
    "The cell": "细胞",
    "What does 'response to stimuli' mean?": "'对刺激的反应'是什么意思？",
    "Reacting to changes in the environment": "对环境变化作出反应",
    "What is adaptation?": "什么是适应？",
    "Evolving over generations to better survive in an environment": "经过世代进化以更好地在环境中生存",
    "Name the 7 characteristics of life.": "列举生命的7个特征。",
    "Organization, metabolism, homeostasis, growth, reproduction, response, adaptation": "组织性、新陈代谢、稳态、生长、繁殖、反应、适应",
    "What is reproduction?": "什么是繁殖？",
    "The process of producing offspring": "产生后代的过程",
    "What is growth in living things?": "生物的生长是什么？",
    "An increase in size and/or number of cells": "细胞大小和/或数量的增加",
    "Why is organization important for life?": "为什么组织性对生命很重要？",
    "Cells provide structure and carry out life functions": "细胞提供结构并执行生命功能",
    "How do organisms maintain homeostasis?": "生物如何维持稳态？",
    "Through internal regulation of temperature, pH, water, etc.": "通过内部调节温度、pH值、水分等",
    
    # Levels of Organization
    "What is a population?": "什么是种群？",
    "All members of one species living in the same area": "生活在同一区域的同一物种的所有成员",
    "What is a community?": "什么是群落？",
    "All populations of different species living in the same area": "生活在同一区域的不同物种的所有种群",
    "What is an ecosystem?": "什么是生态系统？",
    "A community plus its physical environment": "群落加上其物理环境",
    "What is the biosphere?": "什么是生物圈？",
    "All ecosystems on Earth; the global sum of all life": "地球上所有的生态系统；所有生命的全球总和",
    "What is the correct order from smallest to largest?": "从小到大的正确顺序是什么？",
    "Cell → Tissue → Organ → Organ System → Organism": "细胞 → 组织 → 器官 → 器官系统 → 生物体",
    "What is an organelle?": "什么是细胞器？",
    "A specialized structure within a cell that performs a specific function": "细胞内执行特定功能的专门结构",
    "What is a tissue?": "什么是组织？",
    "A group of similar cells working together": "一组相似细胞共同工作",
    "What is an organ?": "什么是器官？",
    "A structure made of different tissues working together": "由不同组织共同工作组成的结构",
    "What is an organ system?": "什么是器官系统？",
    "Multiple organs working together for a common function": "多个器官为共同功能而协同工作",
    "What is the smallest level of life?": "生命的最小层次是什么？",
    "Atom, then molecule": "原子，然后是分子",
    
    # Branches of Biology
    "What is zoology?": "什么是动物学？",
    "The study of animals": "对动物的研究",
    "What is botany?": "什么是植物学？",
    "The study of plants": "对植物的研究",
    "What is microbiology?": "什么是微生物学？",
    "The study of microorganisms": "对微生物的研究",
    "What is genetics?": "什么是遗传学？",
    "The study of heredity and genes": "对遗传和基因的研究",
    "What is ecology?": "什么是生态学？",
    "The study of organisms and their environments": "对生物及其环境的研究",
    "What is the difference between anatomy and physiology?": "解剖学和生理学有什么区别？",
    "Anatomy studies structure; physiology studies function": "解剖学研究结构；生理学研究功能",
    "What is biochemistry?": "什么是生物化学？",
    "The study of chemical processes in living things": "对生物中化学过程的研究",
    "What is cell biology?": "什么是细胞生物学？",
    "The study of cell structure and function": "对细胞结构和功能的研究",
    "What is marine biology?": "什么是海洋生物学？",
    "The study of ocean organisms and ecosystems": "对海洋生物和生态系统的研究",
    "What is immunology?": "什么是免疫学？",
    "The study of the immune system": "对免疫系统的研究",
    
    # Careers in Biology
    "Name three healthcare careers related to biology.": "列举三个与生物学相关的医疗职业。",
    "Doctor, nurse, pharmacist": "医生、护士、药剂师",
    "What does a wildlife biologist do?": "野生动物生物学家做什么？",
    "Studies animals in their natural habitats and works on conservation": "研究自然栖息地中的动物并从事保护工作",
    "What is biotechnology?": "什么是生物技术？",
    "The use of living systems to develop products and technologies": "利用生命系统开发产品和技术",
    "What degree is typically needed for biology careers?": "生物学职业通常需要什么学位？",
    "At least a bachelor's degree": "至少学士学位",
    "What does a forensic scientist do?": "法医科学家做什么？",
    "Applies biological knowledge to solve crimes": "运用生物学知识解决犯罪",
    "What does an ecologist study?": "生态学家研究什么？",
    "The relationships between organisms and their environment": "生物与其环境之间的关系",
    "What is a genetic engineer?": "什么是基因工程师？",
    "A scientist who modifies genes to create desired traits": "修改基因以创造所需性状的科学家",
    "What does a pharmacist do?": "药剂师做什么？",
    "Prepares and dispenses medications": "准备和分发药物",
    "What does an agronomist do?": "农学家做什么？",
    "Studies crops and soil to improve food production": "研究作物和土壤以改善食品生产",
    "What advanced degree helps biology careers?": "什么高级学位有助于生物学职业？",
    "Master's or doctoral degree": "硕士或博士学位",
}

# Quiz question translations
QUIZ_TRANSLATIONS = {
    # Common quiz phrases
    "What is biology?": "什么是生物学？",
    "The scientific study of life": "对生命的科学研究",
    "The study of rocks": "对岩石的研究",
    "The study of weather": "对天气的研究",
    "The study of stars": "对恒星的研究",
    "The word 'biology' comes from which language?": "'生物学'这个词来自哪种语言？",
    "Greek": "希腊语",
    "Latin": "拉丁语",
    "French": "法语",
    "German": "德语",
    "Which is NOT a reason to study biology?": "以下哪项不是学习生物学的原因？",
    "Predicting earthquakes": "预测地震",
    "Understanding disease": "了解疾病",
    "Developing medicines": "开发药物",
    "Improving agriculture": "改善农业",
    "Submit Answer": "提交答案",
    "Try Again": "重试",
    "Correct!": "正确！",
    "Incorrect": "错误",
    "Attempts left:": "剩余尝试次数：",
    "Check Answer": "检查答案",
    "Get another question": "获取另一个问题",
}

# Summary translations
SUMMARY_TRANSLATIONS = {
    "Key Concepts:": "关键概念：",
    "Key Concepts": "关键概念",
    "Summary": "总结",
    "What is Biology?": "什么是生物学？",
    "Why Study Biology?": "为什么学习生物学？",
    "Living things": "生物",
    "Understanding health and disease": "了解健康和疾病",
    "Developing new medicines and treatments": "开发新药物和治疗方法",
    "Addressing environmental challenges": "应对环境挑战",
    "Improving agriculture and food production": "改善农业和食品生产",
    "Next Up: Play": "下一步：练习",
    "Next Up: Quiz": "下一步：测验",
    "Next Up: Practice": "下一步：练习",
    "Next Up: Summary": "下一步：总结",
}

def extract_flashcards_from_file(filepath):
    """Extract flashcard questions and answers from a practice HTML file."""
    strings = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find flashcard content
        pattern = r'\{\s*question:\s*["\']([^"\']+)["\'],\s*answer:\s*["\']([^"\']+)["\']\s*\}'
        for match in re.finditer(pattern, content):
            strings.add(match.group(1))
            strings.add(match.group(2))
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return strings

def extract_quiz_strings_from_file(filepath):
    """Extract quiz questions and answers from a quiz HTML file."""
    strings = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract question text (after the number)
        questions = re.findall(r'<p[^>]*>\s*\d+\.\s*([^<]+)</p>', content)
        for q in questions:
            strings.add(q.strip())
        
        # Extract answer options
        answers = re.findall(r'<input[^>]*>\s*([^<]+)</label>', content)
        for a in answers:
            strings.add(a.strip())
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return strings

def extract_summary_strings_from_file(filepath):
    """Extract summary text from a summary HTML file."""
    strings = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract headings
        headings = re.findall(r'<h3>([^<]+)</h3>', content)
        for h in headings:
            strings.add(h.strip())
        
        # Extract bold text
        bolds = re.findall(r'<b>([^<]+)</b>', content)
        for b in bolds:
            strings.add(b.strip())
        
        # Extract list items
        items = re.findall(r'<li>([^<]+)</li>', content)
        for i in items:
            strings.add(i.strip())
        
        # Extract paragraph text
        paras = re.findall(r'<p>([^<]+)</p>', content)
        for p in paras:
            if p.strip():
                strings.add(p.strip())
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return strings

def collect_all_bio_strings():
    """Collect all translatable strings from biology lessons."""
    all_strings = set()
    
    for unit_num in range(1, 13):
        unit_folder = BASE_PATH / f"Unit{unit_num}"
        if not unit_folder.exists():
            continue
            
        for f in unit_folder.glob("*.html"):
            if "_Practice.html" in f.name:
                all_strings.update(extract_flashcards_from_file(f))
            elif "_Quiz.html" in f.name:
                all_strings.update(extract_quiz_strings_from_file(f))
            elif "_Summary.html" in f.name:
                all_strings.update(extract_summary_strings_from_file(f))
            elif "_Test.html" in f.name:
                # Unit tests have both flashcards and quiz questions
                all_strings.update(extract_flashcards_from_file(f))
                all_strings.update(extract_quiz_strings_from_file(f))
    
    return all_strings

def generate_translations_dict():
    """Combine all pre-defined translations."""
    translations = {}
    translations.update(FLASHCARD_TRANSLATIONS)
    translations.update(QUIZ_TRANSLATIONS)
    translations.update(SUMMARY_TRANSLATIONS)
    return translations

def add_translations_to_file(new_translations):
    """Add translations to global_translations.js."""
    with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check what's already there
    existing_count = 0
    new_count = 0
    
    # Build the new translations string for ones that don't exist
    translations_to_add = {}
    for eng, zh in new_translations.items():
        if f'"{eng}"' not in content and eng not in ['True', 'False', 'true', 'false']:
            translations_to_add[eng] = zh
            new_count += 1
        else:
            existing_count += 1
    
    if not translations_to_add:
        print(f"All {existing_count} translations already exist.")
        return
    
    # Format new translations
    new_lines = '\n  /* Biology Content Translations */\n'
    for eng, zh in sorted(translations_to_add.items()):
        eng_escaped = eng.replace('"', '\\"').replace("'", "\\'")
        zh_escaped = zh.replace('"', '\\"').replace("'", "\\'")
        new_lines += f'  "{eng_escaped}": "{zh_escaped}",\n'
    
    # Find insertion point
    match = re.search(r'(/\* Biology Lesson Translations \*/)', content)
    if match:
        insert_pos = match.end()
        # Find the end of the biology lesson translations section
        # Insert after the last entry in that section
        section_end = content.find('\n};', insert_pos)
        if section_end > 0:
            # Find last comma before section end
            last_comma = content.rfind(',\n', insert_pos, section_end)
            if last_comma > 0:
                content = content[:last_comma+2] + new_lines[2:] + content[last_comma+2:]
    else:
        # Insert before the closing of translations object
        match = re.search(r'(\n\};\n\n\s+// Expose translations globally)', content)
        if match:
            insert_pos = match.start(1)
            content = content[:insert_pos] + new_lines + content[insert_pos:]
    
    with open(TRANSLATIONS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Added {new_count} new translations ({existing_count} already existed)")

def main():
    print("Collecting biology strings...")
    all_strings = collect_all_bio_strings()
    print(f"Found {len(all_strings)} unique strings")
    
    print("\nGenerating translations...")
    translations = generate_translations_dict()
    print(f"Have {len(translations)} pre-defined translations")
    
    print("\nAdding to global_translations.js...")
    add_translations_to_file(translations)
    
    # Report untranslated strings
    untranslated = [s for s in all_strings if s not in translations and len(s) > 3]
    if untranslated:
        print(f"\n{len(untranslated)} strings still need translation (showing first 20):")
        for s in sorted(untranslated)[:20]:
            print(f"  - {s[:80]}...")

if __name__ == "__main__":
    main()
