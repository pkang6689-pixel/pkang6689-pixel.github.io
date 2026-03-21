#!/usr/bin/env python3
"""Fix Biology u8_l8.1 and u8_l8.2 — add 7 more questions each to reach 20."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "biology_lessons.json")

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

def add_questions(key, questions):
    lesson = data[key]
    existing = lesson.get("quiz_questions", [])
    start = len(existing) + 1
    for i, (qt, opts, exp) in enumerate(questions):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        existing.append({"question_number": start + i, "question_text": qt, "attempted": 2,
                         "data_i18n": None, "options": options, "explanation": exp})
    lesson["quiz_questions"] = existing

# u8_l8.1: How Organisms Obtain Energy
add_questions("u8_l8.1", [
    ("Decomposers obtain energy by:", ["Photosynthesis", "Chemosynthesis", "*Breaking down dead organic matter", "Absorbing sunlight"], "Decomposers recycle nutrients from dead organisms."),
    ("Which organisms can make their own food?", ["Heterotrophs", "Consumers", "*Autotrophs (producers)", "Decomposers"], "Autotrophs produce food via photosynthesis or chemosynthesis."),
    ("The 10% rule in ecology refers to:", ["10% of species surviving", "*About 10% of energy being transferred between trophic levels", "10% of habitats remaining", "10% growth rate"], "Energy is lost as heat at each level."),
    ("Cellular respiration converts glucose into:", ["More glucose", "Sunlight", "*ATP (usable energy for cells)", "Proteins"], "Cells break down glucose to make ATP."),
    ("Which process do plants use to capture light energy?", ["Cellular respiration", "Fermentation", "*Photosynthesis", "Chemosynthesis"], "Plants convert light to chemical energy."),
    ("A food web differs from a food chain because it:", ["Is simpler", "Shows one path", "*Shows multiple interconnected feeding relationships", "Only includes producers"], "Food webs are more complex and realistic."),
    ("Primary consumers are also called:", ["Producers", "Carnivores", "*Herbivores", "Decomposers"], "Primary consumers eat producers (plants)."),
])

# u8_l8.2: Chemical Energy and ATP
add_questions("u8_l8.2", [
    ("How many phosphate groups does ATP have?", ["1", "2", "*3", "4"], "Adenosine TRI-phosphate has 3 phosphate groups."),
    ("The energy in ATP is released by:", ["Adding phosphate groups", "*Breaking the bond between the 2nd and 3rd phosphate groups (hydrolysis)", "Absorbing light", "Combining with oxygen"], "Hydrolysis of the terminal phosphate releases energy."),
    ("Which cellular process produces the MOST ATP?", ["Glycolysis", "Fermentation", "*Oxidative phosphorylation (electron transport chain)", "The Krebs cycle alone"], "The ETC produces about 34 of the ~36-38 ATP from one glucose."),
    ("ADP has _____ phosphate group(s) compared to ATP.", ["The same number of", "Three", "*One fewer (2 instead of 3)", "No"], "ADP = adenosine DI-phosphate (2 phosphate groups)."),
    ("Enzymes called ATPases function by:", ["Building ATP", "*Using energy from ATP hydrolysis to drive cellular work (like ion pumps)", "Storing glucose", "Producing oxygen"], "ATPases couple ATP hydrolysis to cellular processes."),
    ("Coupled reactions in cells involve:", ["Only ATP breakdown", "*Using energy from ATP hydrolysis to drive an otherwise unfavorable reaction", "No energy transfer", "Only heat production"], "Endergonic reactions are powered by ATP hydrolysis."),
    ("Without ATP, cells would NOT be able to:", ["Absorb sunlight", "*Perform active transport, muscle contraction, or synthesize macromolecules", "Exist as atoms", "Contain DNA"], "ATP powers most energy-requiring cellular processes."),
])

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Verify
short = [(k, len(v.get("quiz_questions",[]))) for k,v in data.items() if len(v.get("quiz_questions",[]))<20]
if short:
    for k,n in short:
        print(f"STILL SHORT: {k} has {n}")
else:
    print(f"✅ Biology: all {len(data)} lessons at 20+ questions")
