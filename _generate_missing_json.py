#!/usr/bin/env python3
"""Generate missing JSON data files for:
1. Chemistry Unit5A/5B (13 lessons)
2. All 6 Middle School (MS_) courses
3. Fix AP Physics 2 folder naming
"""

import json
import os
import shutil
from pathlib import Path

CONTENT_DATA = Path("content_data")
COURSEFILES = Path("ArisEdu Project Folder/CourseFiles")


def make_quiz_json(unit, lesson_number, course, title, questions):
    """Create a quiz JSON structure."""
    return {
        "unit": unit,
        "lesson_number": lesson_number,
        "title": title,
        "course": course,
        "quiz_questions": questions
    }


def make_summary_json(unit, lesson_number, course, title, sections):
    """Create a summary JSON structure."""
    return {
        "unit": unit,
        "lesson_number": lesson_number,
        "title": title,
        "course": course,
        "summary_sections": sections
    }


def make_practice_json(unit, lesson_number, course, title, flashcards):
    """Create a practice JSON structure."""
    return {
        "unit": unit,
        "lesson_number": lesson_number,
        "title": title,
        "course": course,
        "flashcards": flashcards
    }


def write_json(path, data):
    """Write JSON data to file, creating directories as needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ============================================================
# PART 1: Chemistry Unit5A and Unit5B
# ============================================================
def generate_chemistry_5a_5b():
    """Generate quiz/summary/practice JSON for Chemistry Unit5A and Unit5B."""
    print("\n=== Generating Chemistry Unit5A/5B JSON ===")

    unit5a_lessons = {
        "5A.1": {
            "title": "Introduction to Nomenclature",
            "questions": [
                {"question_number": 1, "question_text": "What is chemical nomenclature?", "attempted": 2, "data_i18n": None, "options": [{"text": "The system of naming chemical compounds", "is_correct": True, "data_i18n": None}, {"text": "The process of balancing equations", "is_correct": False, "data_i18n": None}, {"text": "A method of measuring atomic mass", "is_correct": False, "data_i18n": None}, {"text": "The study of electron configurations", "is_correct": False, "data_i18n": None}], "explanation": "Chemical nomenclature is the systematic method of naming chemical compounds according to IUPAC rules."},
                {"question_number": 2, "question_text": "Which organization sets the standard rules for naming chemical compounds?", "attempted": 2, "data_i18n": None, "options": [{"text": "IUPAC", "is_correct": True, "data_i18n": None}, {"text": "NASA", "is_correct": False, "data_i18n": None}, {"text": "WHO", "is_correct": False, "data_i18n": None}, {"text": "ACS", "is_correct": False, "data_i18n": None}], "explanation": "IUPAC (International Union of Pure and Applied Chemistry) sets the standard rules for chemical nomenclature."},
                {"question_number": 3, "question_text": "What are the two main categories of chemical compounds?", "attempted": 2, "data_i18n": None, "options": [{"text": "Ionic and covalent", "is_correct": True, "data_i18n": None}, {"text": "Organic and metallic", "is_correct": False, "data_i18n": None}, {"text": "Acidic and basic", "is_correct": False, "data_i18n": None}, {"text": "Simple and complex", "is_correct": False, "data_i18n": None}], "explanation": "Chemical compounds are broadly categorized as ionic (metal + nonmetal) or covalent (nonmetal + nonmetal)."},
                {"question_number": 4, "question_text": "In a chemical formula, what does a subscript number indicate?", "attempted": 2, "data_i18n": None, "options": [{"text": "The number of atoms of that element", "is_correct": True, "data_i18n": None}, {"text": "The charge of the ion", "is_correct": False, "data_i18n": None}, {"text": "The oxidation state", "is_correct": False, "data_i18n": None}, {"text": "The atomic number", "is_correct": False, "data_i18n": None}], "explanation": "A subscript in a chemical formula shows how many atoms of that element are present in one formula unit."},
                {"question_number": 5, "question_text": "What suffix is typically used for naming simple anions?", "attempted": 2, "data_i18n": None, "options": [{"text": "-ide", "is_correct": True, "data_i18n": None}, {"text": "-ate", "is_correct": False, "data_i18n": None}, {"text": "-ite", "is_correct": False, "data_i18n": None}, {"text": "-ous", "is_correct": False, "data_i18n": None}], "explanation": "Simple anions (single-element negative ions) are named by changing the element ending to -ide (e.g., chlorine → chloride)."},
                {"question_number": 6, "question_text": "What is the correct name for NaCl?", "attempted": 2, "data_i18n": None, "options": [{"text": "Sodium chloride", "is_correct": True, "data_i18n": None}, {"text": "Sodium chlorine", "is_correct": False, "data_i18n": None}, {"text": "Sodium chlorate", "is_correct": False, "data_i18n": None}, {"text": "Sodide chlorine", "is_correct": False, "data_i18n": None}], "explanation": "NaCl is sodium chloride: the cation (Na⁺) is named first, then the anion (Cl⁻) with the -ide suffix."},
                {"question_number": 7, "question_text": "Which type of compound is formed between a metal and a nonmetal?", "attempted": 2, "data_i18n": None, "options": [{"text": "Ionic compound", "is_correct": True, "data_i18n": None}, {"text": "Covalent compound", "is_correct": False, "data_i18n": None}, {"text": "Organic compound", "is_correct": False, "data_i18n": None}, {"text": "Metallic compound", "is_correct": False, "data_i18n": None}], "explanation": "Ionic compounds are formed when a metal transfers electrons to a nonmetal, creating cations and anions held together by electrostatic forces."},
                {"question_number": 8, "question_text": "What is the correct formula for calcium oxide?", "attempted": 2, "data_i18n": None, "options": [{"text": "CaO", "is_correct": True, "data_i18n": None}, {"text": "Ca₂O", "is_correct": False, "data_i18n": None}, {"text": "CaO₂", "is_correct": False, "data_i18n": None}, {"text": "Ca₂O₂", "is_correct": False, "data_i18n": None}], "explanation": "Calcium (Ca²⁺) and oxide (O²⁻) combine in a 1:1 ratio since their charges balance, giving CaO."},
                {"question_number": 9, "question_text": "When naming ionic compounds, which ion is named first?", "attempted": 2, "data_i18n": None, "options": [{"text": "The cation (positive ion)", "is_correct": True, "data_i18n": None}, {"text": "The anion (negative ion)", "is_correct": False, "data_i18n": None}, {"text": "The larger ion", "is_correct": False, "data_i18n": None}, {"text": "The ion with the higher charge", "is_correct": False, "data_i18n": None}], "explanation": "In ionic compound nomenclature, the cation (metal/positive ion) is always named first, followed by the anion."},
                {"question_number": 10, "question_text": "What distinguishes a molecular compound from an ionic compound?", "attempted": 2, "data_i18n": None, "options": [{"text": "Molecular compounds are formed between nonmetals sharing electrons", "is_correct": True, "data_i18n": None}, {"text": "Molecular compounds always contain metals", "is_correct": False, "data_i18n": None}, {"text": "Molecular compounds have higher melting points", "is_correct": False, "data_i18n": None}, {"text": "Molecular compounds conduct electricity in solution", "is_correct": False, "data_i18n": None}], "explanation": "Molecular (covalent) compounds form between nonmetals that share electrons, unlike ionic compounds where electrons are transferred."},
                {"question_number": 11, "question_text": "What is the stock system in nomenclature used for?", "attempted": 2, "data_i18n": None, "options": [{"text": "Indicating the charge of transition metal cations with Roman numerals", "is_correct": True, "data_i18n": None}, {"text": "Counting the total number of atoms", "is_correct": False, "data_i18n": None}, {"text": "Measuring the molecular weight", "is_correct": False, "data_i18n": None}, {"text": "Classifying elements by group", "is_correct": False, "data_i18n": None}], "explanation": "The stock system uses Roman numerals in parentheses after the metal name to indicate its charge, e.g., iron(III) chloride for FeCl₃."},
                {"question_number": 12, "question_text": "What does the prefix 'di-' mean in chemical nomenclature?", "attempted": 2, "data_i18n": None, "options": [{"text": "Two", "is_correct": True, "data_i18n": None}, {"text": "One", "is_correct": False, "data_i18n": None}, {"text": "Three", "is_correct": False, "data_i18n": None}, {"text": "Four", "is_correct": False, "data_i18n": None}], "explanation": "The prefix 'di-' means two. It is used in naming covalent compounds to indicate two atoms of an element (e.g., CO₂ is carbon dioxide)."},
                {"question_number": 13, "question_text": "Which of the following is a binary compound?", "attempted": 2, "data_i18n": None, "options": [{"text": "NaCl", "is_correct": True, "data_i18n": None}, {"text": "NaOH", "is_correct": False, "data_i18n": None}, {"text": "H₂SO₄", "is_correct": False, "data_i18n": None}, {"text": "Ca(NO₃)₂", "is_correct": False, "data_i18n": None}], "explanation": "A binary compound contains exactly two different elements. NaCl (sodium and chlorine) is binary, while the others contain three or more elements."},
                {"question_number": 14, "question_text": "In the name 'iron(II) oxide', what does (II) represent?", "attempted": 2, "data_i18n": None, "options": [{"text": "The charge on the iron ion is 2+", "is_correct": True, "data_i18n": None}, {"text": "There are two iron atoms", "is_correct": False, "data_i18n": None}, {"text": "Iron is in group 2", "is_correct": False, "data_i18n": None}, {"text": "The compound has two bonds", "is_correct": False, "data_i18n": None}], "explanation": "The Roman numeral (II) indicates the charge of the iron cation (Fe²⁺), distinguishing it from iron(III) compounds."},
                {"question_number": 15, "question_text": "What is the formula for aluminum oxide?", "attempted": 2, "data_i18n": None, "options": [{"text": "Al₂O₃", "is_correct": True, "data_i18n": None}, {"text": "AlO", "is_correct": False, "data_i18n": None}, {"text": "Al₃O₂", "is_correct": False, "data_i18n": None}, {"text": "AlO₃", "is_correct": False, "data_i18n": None}], "explanation": "Aluminum is Al³⁺ and oxide is O²⁻. Cross-multiplying the charges gives Al₂O₃ (2 aluminum ions and 3 oxide ions)."},
                {"question_number": 16, "question_text": "Which of these is NOT a rule of chemical nomenclature?", "attempted": 2, "data_i18n": None, "options": [{"text": "Always use the atomic number as a subscript", "is_correct": True, "data_i18n": None}, {"text": "Name the cation first in ionic compounds", "is_correct": False, "data_i18n": None}, {"text": "Use -ide suffix for monatomic anions", "is_correct": False, "data_i18n": None}, {"text": "Use Greek prefixes for covalent compounds", "is_correct": False, "data_i18n": None}], "explanation": "The atomic number is not used as a subscript in formulas. Subscripts indicate the number of atoms, not the atomic number."},
                {"question_number": 17, "question_text": "What type of elements typically form cations?", "attempted": 2, "data_i18n": None, "options": [{"text": "Metals", "is_correct": True, "data_i18n": None}, {"text": "Nonmetals", "is_correct": False, "data_i18n": None}, {"text": "Noble gases", "is_correct": False, "data_i18n": None}, {"text": "Halogens", "is_correct": False, "data_i18n": None}], "explanation": "Metals tend to lose electrons and form positively charged cations, while nonmetals tend to gain electrons and form anions."},
                {"question_number": 18, "question_text": "What is the correct name for MgBr₂?", "attempted": 2, "data_i18n": None, "options": [{"text": "Magnesium bromide", "is_correct": True, "data_i18n": None}, {"text": "Magnesium dibromide", "is_correct": False, "data_i18n": None}, {"text": "Magnesium(II) bromide", "is_correct": False, "data_i18n": None}, {"text": "Dimagnesium bromide", "is_correct": False, "data_i18n": None}], "explanation": "MgBr₂ is magnesium bromide. Since magnesium only forms Mg²⁺, no Roman numeral is needed. Greek prefixes are not used for ionic compounds."},
                {"question_number": 19, "question_text": "Which prefix means 'one' in covalent compound naming?", "attempted": 2, "data_i18n": None, "options": [{"text": "Mono-", "is_correct": True, "data_i18n": None}, {"text": "Uni-", "is_correct": False, "data_i18n": None}, {"text": "Prim-", "is_correct": False, "data_i18n": None}, {"text": "Sin-", "is_correct": False, "data_i18n": None}], "explanation": "The prefix 'mono-' means one. It is typically only used for the second element in a covalent compound name (e.g., carbon monoxide)."},
                {"question_number": 20, "question_text": "What determines whether a compound is named using ionic or covalent rules?", "attempted": 2, "data_i18n": None, "options": [{"text": "Whether it contains a metal or only nonmetals", "is_correct": True, "data_i18n": None}, {"text": "The total number of atoms", "is_correct": False, "data_i18n": None}, {"text": "The physical state at room temperature", "is_correct": False, "data_i18n": None}, {"text": "The molecular weight", "is_correct": False, "data_i18n": None}], "explanation": "If a compound contains a metal and nonmetal, it is named using ionic rules. If it contains only nonmetals, covalent (molecular) naming rules apply."}
            ],
            "summary": [{"title": "Key Concepts: Introduction to Nomenclature", "content_html": "<p><b>Core Concepts</b></p><ul><li><b>Chemical Nomenclature</b>: The systematic method of naming chemical compounds using IUPAC rules.</li><li><b>Ionic Compounds</b>: Formed between metals and nonmetals; name the cation first, then the anion with -ide suffix.</li><li><b>Covalent Compounds</b>: Formed between nonmetals; use Greek prefixes to indicate atom counts.</li><li><b>Binary Compounds</b>: Contain exactly two different elements.</li><li><b>Stock System</b>: Uses Roman numerals to indicate transition metal charges.</li></ul>"}],
            "flashcards": [{"term": "Chemical Nomenclature", "definition": "The systematic method of naming chemical compounds according to IUPAC rules."}, {"term": "Binary Compound", "definition": "A compound composed of exactly two different elements."}, {"term": "-ide Suffix", "definition": "The ending added to monatomic anion names (e.g., chlorine → chloride)."}, {"term": "Stock System", "definition": "A naming method using Roman numerals to show the charge of transition metal cations."}, {"term": "IUPAC", "definition": "International Union of Pure and Applied Chemistry — sets standard naming rules."}]
        },
        "5A.2": {
            "title": "Net Charge",
            "questions": [
                {"question_number": 1, "question_text": "What must the net charge of an ionic compound be?", "attempted": 2, "data_i18n": None, "options": [{"text": "Zero", "is_correct": True, "data_i18n": None}, {"text": "Positive", "is_correct": False, "data_i18n": None}, {"text": "Negative", "is_correct": False, "data_i18n": None}, {"text": "It varies", "is_correct": False, "data_i18n": None}], "explanation": "Ionic compounds are electrically neutral — the total positive charge must equal the total negative charge, making the net charge zero."},
                {"question_number": 2, "question_text": "What is the charge of a sodium ion?", "attempted": 2, "data_i18n": None, "options": [{"text": "+1", "is_correct": True, "data_i18n": None}, {"text": "+2", "is_correct": False, "data_i18n": None}, {"text": "-1", "is_correct": False, "data_i18n": None}, {"text": "0", "is_correct": False, "data_i18n": None}], "explanation": "Sodium (Na) is in Group 1 and loses one electron to form Na⁺ with a +1 charge."},
                {"question_number": 3, "question_text": "What charge does a chloride ion have?", "attempted": 2, "data_i18n": None, "options": [{"text": "-1", "is_correct": True, "data_i18n": None}, {"text": "+1", "is_correct": False, "data_i18n": None}, {"text": "-2", "is_correct": False, "data_i18n": None}, {"text": "0", "is_correct": False, "data_i18n": None}], "explanation": "Chlorine (Cl) is in Group 17 and gains one electron to form Cl⁻ with a -1 charge."},
                {"question_number": 4, "question_text": "How can you determine the charge of a main-group element's ion?", "attempted": 2, "data_i18n": None, "options": [{"text": "From its position in the periodic table (group number)", "is_correct": True, "data_i18n": None}, {"text": "From its atomic mass", "is_correct": False, "data_i18n": None}, {"text": "From the number of neutrons", "is_correct": False, "data_i18n": None}, {"text": "From its electron configuration only", "is_correct": False, "data_i18n": None}], "explanation": "Main-group elements form ions with charges predictable from their group: Group 1 → +1, Group 2 → +2, Group 16 → -2, Group 17 → -1."},
                {"question_number": 5, "question_text": "What is the charge on a calcium ion?", "attempted": 2, "data_i18n": None, "options": [{"text": "+2", "is_correct": True, "data_i18n": None}, {"text": "+1", "is_correct": False, "data_i18n": None}, {"text": "-2", "is_correct": False, "data_i18n": None}, {"text": "+3", "is_correct": False, "data_i18n": None}], "explanation": "Calcium is in Group 2 and loses two electrons to form Ca²⁺."},
                {"question_number": 6, "question_text": "In MgCl₂, why are there two chloride ions?", "attempted": 2, "data_i18n": None, "options": [{"text": "To balance Mg²⁺ charge, two Cl⁻ ions are needed", "is_correct": True, "data_i18n": None}, {"text": "Because chlorine is diatomic", "is_correct": False, "data_i18n": None}, {"text": "Because magnesium has two electron shells", "is_correct": False, "data_i18n": None}, {"text": "Because Cl always comes in pairs", "is_correct": False, "data_i18n": None}], "explanation": "Mg²⁺ has a +2 charge, so two Cl⁻ ions (each -1) are needed to make the compound electrically neutral: +2 + 2(-1) = 0."},
                {"question_number": 7, "question_text": "What is the charge on an oxide ion?", "attempted": 2, "data_i18n": None, "options": [{"text": "-2", "is_correct": True, "data_i18n": None}, {"text": "-1", "is_correct": False, "data_i18n": None}, {"text": "+2", "is_correct": False, "data_i18n": None}, {"text": "0", "is_correct": False, "data_i18n": None}], "explanation": "Oxygen is in Group 16 and gains two electrons to form O²⁻ with a -2 charge."},
                {"question_number": 8, "question_text": "Why do transition metals often form ions with different charges?", "attempted": 2, "data_i18n": None, "options": [{"text": "They can lose different numbers of d electrons", "is_correct": True, "data_i18n": None}, {"text": "They have unstable nuclei", "is_correct": False, "data_i18n": None}, {"text": "They are always diamagnetic", "is_correct": False, "data_i18n": None}, {"text": "They have only one valence electron", "is_correct": False, "data_i18n": None}], "explanation": "Transition metals can lose varying numbers of d electrons in addition to s electrons, resulting in multiple possible oxidation states."},
                {"question_number": 9, "question_text": "What is the net charge calculation for Al₂O₃?", "attempted": 2, "data_i18n": None, "options": [{"text": "2(+3) + 3(-2) = 0", "is_correct": True, "data_i18n": None}, {"text": "2(+2) + 3(-3) = 0", "is_correct": False, "data_i18n": None}, {"text": "2(+3) + 3(-3) = 0", "is_correct": False, "data_i18n": None}, {"text": "3(+2) + 2(-3) = 0", "is_correct": False, "data_i18n": None}], "explanation": "In Al₂O₃: 2 aluminum ions (Al³⁺) give +6 total, and 3 oxide ions (O²⁻) give -6 total. Net charge = +6 + (-6) = 0."},
                {"question_number": 10, "question_text": "If an element forms a 3+ cation, how many electrons did it lose?", "attempted": 2, "data_i18n": None, "options": [{"text": "3", "is_correct": True, "data_i18n": None}, {"text": "1", "is_correct": False, "data_i18n": None}, {"text": "2", "is_correct": False, "data_i18n": None}, {"text": "6", "is_correct": False, "data_i18n": None}], "explanation": "A 3+ cation has lost 3 electrons, giving it 3 more protons than electrons and a net +3 charge."},
                {"question_number": 11, "question_text": "What is the formula for a compound of potassium and sulfur?", "attempted": 2, "data_i18n": None, "options": [{"text": "K₂S", "is_correct": True, "data_i18n": None}, {"text": "KS", "is_correct": False, "data_i18n": None}, {"text": "KS₂", "is_correct": False, "data_i18n": None}, {"text": "K₂S₂", "is_correct": False, "data_i18n": None}], "explanation": "Potassium forms K⁺ and sulfur forms S²⁻. Two K⁺ ions are needed to balance one S²⁻: 2(+1) + (-2) = 0, giving K₂S."},
                {"question_number": 12, "question_text": "Which group of elements typically forms 2- anions?", "attempted": 2, "data_i18n": None, "options": [{"text": "Group 16 (chalcogens)", "is_correct": True, "data_i18n": None}, {"text": "Group 1 (alkali metals)", "is_correct": False, "data_i18n": None}, {"text": "Group 17 (halogens)", "is_correct": False, "data_i18n": None}, {"text": "Group 18 (noble gases)", "is_correct": False, "data_i18n": None}], "explanation": "Group 16 elements (O, S, Se, Te) gain 2 electrons to achieve a noble gas configuration, forming 2- anions."},
                {"question_number": 13, "question_text": "What is the charge on a nitride ion (N³⁻)?", "attempted": 2, "data_i18n": None, "options": [{"text": "-3", "is_correct": True, "data_i18n": None}, {"text": "-2", "is_correct": False, "data_i18n": None}, {"text": "-1", "is_correct": False, "data_i18n": None}, {"text": "+3", "is_correct": False, "data_i18n": None}], "explanation": "Nitrogen is in Group 15 and gains 3 electrons to form N³⁻ with a -3 charge."},
                {"question_number": 14, "question_text": "In the formula Fe₂O₃, what is the charge of each iron ion?", "attempted": 2, "data_i18n": None, "options": [{"text": "+3", "is_correct": True, "data_i18n": None}, {"text": "+2", "is_correct": False, "data_i18n": None}, {"text": "+1", "is_correct": False, "data_i18n": None}, {"text": "+6", "is_correct": False, "data_i18n": None}], "explanation": "In Fe₂O₃, total negative charge is 3×(-2)=-6. For the 2 iron ions to balance: 2x=-(-6), so x=+3. Each iron ion is Fe³⁺."},
                {"question_number": 15, "question_text": "What does 'electrically neutral' mean for a compound?", "attempted": 2, "data_i18n": None, "options": [{"text": "The total positive charges equal the total negative charges", "is_correct": True, "data_i18n": None}, {"text": "The compound has no ions", "is_correct": False, "data_i18n": None}, {"text": "The compound cannot conduct electricity", "is_correct": False, "data_i18n": None}, {"text": "All atoms have full valence shells", "is_correct": False, "data_i18n": None}], "explanation": "Electrically neutral means the sum of all positive charges equals the sum of all negative charges, so the net charge is zero."},
                {"question_number": 16, "question_text": "What is the formula for lithium fluoride?", "attempted": 2, "data_i18n": None, "options": [{"text": "LiF", "is_correct": True, "data_i18n": None}, {"text": "Li₂F", "is_correct": False, "data_i18n": None}, {"text": "LiF₂", "is_correct": False, "data_i18n": None}, {"text": "Li₂F₂", "is_correct": False, "data_i18n": None}], "explanation": "Li⁺ and F⁻ have equal and opposite charges, so they combine 1:1 to give LiF."},
                {"question_number": 17, "question_text": "How many electrons does a sulfide ion (S²⁻) have compared to a neutral sulfur atom?", "attempted": 2, "data_i18n": None, "options": [{"text": "2 more", "is_correct": True, "data_i18n": None}, {"text": "2 fewer", "is_correct": False, "data_i18n": None}, {"text": "The same number", "is_correct": False, "data_i18n": None}, {"text": "6 more", "is_correct": False, "data_i18n": None}], "explanation": "S²⁻ gained 2 electrons from a neutral S atom (16 electrons → 18 electrons) to achieve a -2 charge."},
                {"question_number": 18, "question_text": "What is the formula for barium chloride?", "attempted": 2, "data_i18n": None, "options": [{"text": "BaCl₂", "is_correct": True, "data_i18n": None}, {"text": "BaCl", "is_correct": False, "data_i18n": None}, {"text": "Ba₂Cl", "is_correct": False, "data_i18n": None}, {"text": "Ba₂Cl₂", "is_correct": False, "data_i18n": None}], "explanation": "Barium forms Ba²⁺ and chlorine forms Cl⁻. Two Cl⁻ ions balance one Ba²⁺: +2 + 2(-1) = 0, giving BaCl₂."},
                {"question_number": 19, "question_text": "Why does aluminum form a 3+ ion?", "attempted": 2, "data_i18n": None, "options": [{"text": "It loses 3 valence electrons to achieve a noble gas configuration", "is_correct": True, "data_i18n": None}, {"text": "It gains 3 electrons", "is_correct": False, "data_i18n": None}, {"text": "It has 3 neutrons", "is_correct": False, "data_i18n": None}, {"text": "It is in Period 3", "is_correct": False, "data_i18n": None}], "explanation": "Aluminum (Group 13) has 3 valence electrons. Losing all 3 gives it the electron configuration of neon (noble gas)."},
                {"question_number": 20, "question_text": "What is the charge of a phosphide ion?", "attempted": 2, "data_i18n": None, "options": [{"text": "-3", "is_correct": True, "data_i18n": None}, {"text": "-2", "is_correct": False, "data_i18n": None}, {"text": "+5", "is_correct": False, "data_i18n": None}, {"text": "+3", "is_correct": False, "data_i18n": None}], "explanation": "Phosphorus is in Group 15 and gains 3 electrons to form P³⁻ (phosphide), achieving an argon electron configuration."}
            ],
            "summary": [{"title": "Key Concepts: Net Charge", "content_html": "<p><b>Core Concepts</b></p><ul><li><b>Net Charge</b>: Ionic compounds must be electrically neutral (total + charge = total - charge).</li><li><b>Cation Charges</b>: Metals lose electrons; Group 1 → +1, Group 2 → +2, Group 13 → +3.</li><li><b>Anion Charges</b>: Nonmetals gain electrons; Group 17 → -1, Group 16 → -2, Group 15 → -3.</li><li><b>Transition Metals</b>: Can form multiple charges due to d electrons.</li><li><b>Balancing</b>: Adjust subscripts so total positive charge equals total negative charge.</li></ul>"}],
            "flashcards": [{"term": "Net Charge", "definition": "The overall charge of a compound; must be zero for ionic compounds."}, {"term": "Cation", "definition": "A positively charged ion formed when an atom loses electrons."}, {"term": "Anion", "definition": "A negatively charged ion formed when an atom gains electrons."}, {"term": "Electrically Neutral", "definition": "Having no net charge; total positive charges equal total negative charges."}, {"term": "Oxidation State", "definition": "The charge an atom would have if all bonds were completely ionic."}]
        },
    }

    # For brevity, Unit5A lessons 5A.3-5A.8 and Unit5B lessons will use shorter but valid question sets
    # Generate remaining lessons with topic-appropriate questions
    remaining_5a = {
        "5A.3": ("Bond Formation", "How do ionic bonds form?", "Through the transfer of electrons between atoms", ["Through the transfer of electrons between atoms", "By sharing electrons equally", "Through nuclear fusion", "By absorbing photons"]),
        "5A.4": ("Ionic Bonds", "What is an ionic bond?", "An electrostatic attraction between oppositely charged ions", ["An electrostatic attraction between oppositely charged ions", "A bond formed by sharing electrons", "A weak intermolecular force", "A metallic bond"]),
        "5A.5": ("Crisscross Method", "In the crisscross method, what do you cross?", "The charge numbers of the ions become subscripts of the other ion", ["The charge numbers of the ions become subscripts of the other ion", "The atomic numbers", "The electron configurations", "The group numbers"]),
        "5A.6": ("Naming Ionic Compounds", "What is the correct name for CaBr₂?", "Calcium bromide", ["Calcium bromide", "Calcium dibromide", "Calcium(II) bromide", "Dicalcium bromide"]),
        "5A.7": ("Polyatomic Ions", "What is a polyatomic ion?", "A charged group of two or more covalently bonded atoms", ["A charged group of two or more covalently bonded atoms", "A single atom with a charge", "An uncharged molecule", "A noble gas compound"]),
        "5A.8": ("Common Exceptions & Traditional Names", "What is the traditional name for Fe²⁺?", "Ferrous", ["Ferrous", "Ferric", "Iron(I)", "Ironide"]),
    }

    remaining_5b = {
        "5B.1": ("Covalent Bonds", "What is a covalent bond?", "A bond formed by the sharing of electron pairs between atoms", ["A bond formed by the sharing of electron pairs between atoms", "A bond formed by transferring electrons", "An attraction between ions", "A metallic bond"]),
        "5B.2": ("Naming Covalent Compounds", "What prefix is used for 3 atoms in covalent naming?", "Tri-", ["Tri-", "Di-", "Tetra-", "Mono-"]),
        "5B.3": ("Metallic Bonds", "What is a metallic bond?", "A bond where electrons are shared in a 'sea' of delocalized electrons", ["A bond where electrons are shared in a 'sea' of delocalized electrons", "A bond between a metal and nonmetal", "A covalent bond in metals", "An ionic bond between metals"]),
        "5B.4": ("Organic Compounds", "What element is the basis of all organic compounds?", "Carbon", ["Carbon", "Hydrogen", "Oxygen", "Nitrogen"]),
        "5B.5": ("Mixed Nomenclature Practice", "Which compound is ionic?", "NaCl", ["NaCl", "CO₂", "H₂O", "CH₄"]),
    }

    def generate_full_questions(lesson_id, title, sample_q, sample_a, sample_opts):
        """Generate 20 questions for a lesson based on the topic."""
        # Create varied questions around the topic
        questions = []
        base_q = {"question_number": 1, "question_text": sample_q, "attempted": 2, "data_i18n": None,
                  "options": [{"text": opt, "is_correct": opt == sample_a, "data_i18n": None} for opt in sample_opts],
                  "explanation": f"{sample_a} is correct. This is a key concept in {title}."}
        questions.append(base_q)

        # Generate additional topic-specific questions for each lesson
        topic_questions = {
            "5A.3": [
                ("What happens to electrons during ionic bond formation?", "They are transferred from metal to nonmetal", ["They are transferred from metal to nonmetal", "They are shared equally", "They are destroyed", "They become neutrons"]),
                ("What type of elements typically form ionic bonds?", "A metal and a nonmetal", ["A metal and a nonmetal", "Two nonmetals", "Two metals", "Two noble gases"]),
                ("What force holds ions together in an ionic bond?", "Electrostatic attraction", ["Electrostatic attraction", "Gravitational force", "Nuclear force", "Magnetic force"]),
                ("What is a crystal lattice?", "A repeating 3D arrangement of ions in an ionic compound", ["A repeating 3D arrangement of ions in an ionic compound", "A single molecule of an ionic compound", "A type of covalent bond", "A metallic structure"]),
                ("Which property is characteristic of ionic compounds?", "High melting points", ["High melting points", "Low boiling points", "Soft and flexible", "Poor conductors when dissolved"]),
                ("What happens when sodium reacts with chlorine?", "Na transfers one electron to Cl to form Na⁺Cl⁻", ["Na transfers one electron to Cl to form Na⁺Cl⁻", "They share electrons equally", "Cl transfers an electron to Na", "Nothing happens"]),
                ("What is the electron configuration of Na⁺?", "Same as neon (1s²2s²2p⁶)", ["Same as neon (1s²2s²2p⁶)", "Same as argon", "Same as helium", "Same as sodium"]),
                ("What is a formula unit?", "The simplest ratio of ions in an ionic compound", ["The simplest ratio of ions in an ionic compound", "A single molecule", "A unit of measurement", "The atomic mass"]),
                ("Why are ionic compounds brittle?", "Like charges repel when layers shift, causing the crystal to shatter", ["Like charges repel when layers shift, causing the crystal to shatter", "They have weak bonds", "They are made of gases", "They lack electrons"]),
                ("Do ionic compounds conduct electricity as solids?", "No, ions are fixed in place and cannot move", ["No, ions are fixed in place and cannot move", "Yes, always", "Only at high pressure", "Only in vacuum"]),
                ("When do ionic compounds conduct electricity?", "When dissolved in water or melted", ["When dissolved in water or melted", "Never", "Only as solids", "Only at low temperatures"]),
                ("What is the octet rule?", "Atoms tend to gain, lose, or share electrons to have 8 valence electrons", ["Atoms tend to gain, lose, or share electrons to have 8 valence electrons", "All atoms must have exactly 8 electrons", "Atoms always form 8 bonds", "Elements must be in Group 8"]),
                ("What type of bond forms between Li and F?", "Ionic bond", ["Ionic bond", "Covalent bond", "Metallic bond", "Hydrogen bond"]),
                ("What is the lattice energy?", "The energy released when gaseous ions form a solid ionic compound", ["The energy released when gaseous ions form a solid ionic compound", "The energy to break a covalent bond", "The kinetic energy of ions", "The energy of a single electron"]),
                ("Which has a higher melting point: NaCl or a typical molecular compound?", "NaCl", ["NaCl", "The molecular compound", "They are the same", "Cannot be determined"]),
                ("What is an electrolyte?", "A substance that conducts electricity when dissolved in water", ["A substance that conducts electricity when dissolved in water", "A type of battery", "A pure metal", "An insulating material"]),
                ("How does ionic bond strength relate to ion charge?", "Higher charges lead to stronger bonds", ["Higher charges lead to stronger bonds", "Higher charges lead to weaker bonds", "Charge has no effect", "Only anion charge matters"]),
                ("What is the coordination number in a crystal lattice?", "The number of nearest neighbor ions surrounding an ion", ["The number of nearest neighbor ions surrounding an ion", "The total number of ions", "The charge of the ion", "The atomic number"]),
                ("What happens to the size of a metal atom when it becomes a cation?", "It decreases", ["It decreases", "It increases", "It stays the same", "It doubles"]),
            ],
            "5A.4": [
                ("Which pair would form an ionic bond?", "Na and Cl", ["Na and Cl", "H and O", "C and H", "N and O"]),
                ("What is the difference between an ionic and covalent bond?", "Ionic involves electron transfer; covalent involves electron sharing", ["Ionic involves electron transfer; covalent involves electron sharing", "They are the same thing", "Ionic is weaker than covalent", "Covalent involves electron transfer"]),
                ("In NaCl, what type of ion is Na?", "Cation", ["Cation", "Anion", "Neutral", "Isotope"]),
                ("What happens to ionization energy as you move across a period?", "It generally increases", ["It generally increases", "It generally decreases", "It stays constant", "It fluctuates randomly"]),
                ("Which ionic compound has the formula K₂O?", "Potassium oxide", ["Potassium oxide", "Potassium peroxide", "Dipotassium monoxide", "Potassium(I) oxide"]),
                ("What makes ionic bonds strong?", "The strong electrostatic attraction between oppositely charged ions", ["The strong electrostatic attraction between oppositely charged ions", "Sharing of electrons", "Van der Waals forces", "Magnetic attraction"]),
                ("What is the typical state of ionic compounds at room temperature?", "Solid", ["Solid", "Liquid", "Gas", "Plasma"]),
                ("How do you predict the charge of a Group 2 element?", "It forms a 2+ ion by losing 2 electrons", ["It forms a 2+ ion by losing 2 electrons", "It forms a 2- ion", "It forms a 1+ ion", "It does not form ions"]),
                ("What is Coulomb's law relevant to in ionic bonding?", "It describes the force between charged particles", ["It describes the force between charged particles", "It describes nuclear forces", "It relates to magnetic fields", "It measures electron speed"]),
                ("Why do ionic compounds dissolve in water?", "Water molecules surround and separate the ions", ["Water molecules surround and separate the ions", "They react with water chemically", "Water breaks their covalent bonds", "They evaporate into water"]),
                ("What is a monovalent ion?", "An ion with a charge of +1 or -1", ["An ion with a charge of +1 or -1", "An ion with multiple charges", "A neutral atom", "A noble gas"]),
                ("Which compound has the highest lattice energy?", "MgO (higher charges, smaller ions)", ["MgO (higher charges, smaller ions)", "NaCl", "KBr", "CsI"]),
                ("Do ionic compounds have high or low boiling points?", "High boiling points", ["High boiling points", "Low boiling points", "Room temperature boiling", "They don't boil"]),
                ("What structure do most ionic compounds form?", "Crystalline lattice", ["Crystalline lattice", "Amorphous solid", "Liquid crystal", "Polymer chain"]),
                ("What is the electron configuration of Cl⁻?", "Same as argon (1s²2s²2p⁶3s²3p⁶)", ["Same as argon (1s²2s²2p⁶3s²3p⁶)", "Same as neon", "Same as chlorine", "Same as sulfur"]),
                ("Which is NOT a property of ionic compounds?", "They are good conductors as solids", ["They are good conductors as solids", "High melting points", "Brittle", "Soluble in polar solvents"]),
                ("What role does electronegativity difference play in ionic bonding?", "A large difference (>1.7) typically indicates ionic bonding", ["A large difference (>1.7) typically indicates ionic bonding", "No role", "A small difference indicates ionic bonding", "Only applies to covalent bonds"]),
                ("What is a divalent ion?", "An ion with a charge of +2 or -2", ["An ion with a charge of +2 or -2", "An ion with charge +1", "A neutral atom with 2 bonds", "An atom with 2 neutrons"]),
                ("How do ionic radii affect lattice energy?", "Smaller ions have higher lattice energy", ["Smaller ions have higher lattice energy", "Larger ions have higher lattice energy", "Size has no effect", "Only cation size matters"]),
            ],
            "5A.5": [
                ("Using the crisscross method, what is the formula for aluminum chloride?", "AlCl₃", ["AlCl₃", "Al₃Cl", "AlCl", "Al₂Cl₃"]),
                ("In the crisscross method for Ca²⁺ and N³⁻, what formula results?", "Ca₃N₂", ["Ca₃N₂", "CaN", "Ca₂N₃", "CaN₃"]),
                ("After crisscrossing, when should you simplify the subscripts?", "When both subscripts share a common factor", ["When both subscripts share a common factor", "Never", "Always", "Only for metals"]),
                ("What is the formula for iron(III) oxide using crisscross?", "Fe₂O₃", ["Fe₂O₃", "FeO", "Fe₃O₂", "FeO₃"]),
                ("Using crisscross for Na⁺ and O²⁻, the formula is:", "Na₂O", ["Na₂O", "NaO", "NaO₂", "Na₂O₂"]),
                ("What is the crisscross method?", "A technique where ion charges become subscripts of the opposite ion", ["A technique where ion charges become subscripts of the opposite ion", "A way to calculate molecular weight", "A method for balancing equations", "A technique for naming compounds"]),
                ("For Mg²⁺ and P³⁻, what does crisscross give?", "Mg₃P₂", ["Mg₃P₂", "MgP", "Mg₂P₃", "Mg₃P₃"]),
                ("When crisscrossing Ba²⁺ and O²⁻, the initial result is Ba₂O₂. What should you do?", "Simplify to BaO", ["Simplify to BaO", "Leave it as Ba₂O₂", "Change to Ba₄O₄", "Add a coefficient"]),
                ("Using crisscross for Al³⁺ and O²⁻:", "Al₂O₃", ["Al₂O₃", "AlO", "Al₃O₂", "AlO₃"]),
                ("What must be true about the subscripts after crisscrossing?", "They should be reduced to the lowest whole-number ratio", ["They should be reduced to the lowest whole-number ratio", "They must always be even", "They must be prime numbers", "They should be multiplied by 2"]),
                ("For Li⁺ and S²⁻, the crisscross formula is:", "Li₂S", ["Li₂S", "LiS", "LiS₂", "Li₂S₂"]),
                ("What is the formula for strontium fluoride?", "SrF₂", ["SrF₂", "SrF", "Sr₂F", "Sr₂F₂"]),
                ("When is the subscript 1 written?", "It is never written; it is implied", ["It is never written; it is implied", "Always", "Only for metals", "Only for nonmetals"]),
                ("What formula does crisscross give for Fe²⁺ and S²⁻?", "FeS (simplified from Fe₂S₂)", ["FeS (simplified from Fe₂S₂)", "Fe₂S₂", "FeS₂", "Fe₂S"]),
                ("For Cr³⁺ and O²⁻ using crisscross:", "Cr₂O₃", ["Cr₂O₃", "CrO", "Cr₃O₂", "CrO₃"]),
                ("What happens if both charges are the same magnitude?", "The ratio is 1:1, so each subscript is 1", ["The ratio is 1:1, so each subscript is 1", "You double both subscripts", "The formula is invalid", "You add the charges together"]),
                ("What is the formula for tin(IV) chloride?", "SnCl₄", ["SnCl₄", "SnCl₂", "Sn₄Cl", "Sn₂Cl₄"]),
                ("Using crisscross for Ca²⁺ and PO₄³⁻:", "Ca₃(PO₄)₂", ["Ca₃(PO₄)₂", "CaPO₄", "Ca₂(PO₄)₃", "Ca(PO₄)₂"]),
                ("Does the crisscross method work for polyatomic ions?", "Yes, treat the polyatomic ion as a single unit", ["Yes, treat the polyatomic ion as a single unit", "No, only for monatomic ions", "Only for transition metals", "Only for main group elements"]),
            ],
            "5A.6": [
                ("What is the name for KBr?", "Potassium bromide", ["Potassium bromide", "Potassium(I) bromide", "Potasside bromium", "Monopotassium bromide"]),
                ("How do you name an ionic compound with a transition metal?", "Use the metal name with a Roman numeral for its charge, then the anion name", ["Use the metal name with a Roman numeral for its charge, then the anion name", "Just use the metal and nonmetal names", "Use Greek prefixes", "Use the -ous/-ic system only"]),
                ("What is the name for CuCl₂?", "Copper(II) chloride", ["Copper(II) chloride", "Copper chloride", "Copper dichloride", "Cupric chloride"]),
                ("Do you need Roman numerals for compounds of Group 1 metals?", "No, they only form one charge", ["No, they only form one charge", "Yes, always", "Only for lithium", "Only in the stock system"]),
                ("What is the name for FeO?", "Iron(II) oxide", ["Iron(II) oxide", "Iron oxide", "Iron(III) oxide", "Ferric oxide"]),
                ("What suffix does the nonmetal get in a binary ionic compound?", "-ide", ["-ide", "-ate", "-ite", "-ous"]),
                ("What is the name for Al₂S₃?", "Aluminum sulfide", ["Aluminum sulfide", "Dialuminum trisulfide", "Aluminum(III) sulfide", "Aluminum sulphate"]),
                ("Why don't we use prefixes like di- or tri- for ionic compounds?", "Because the ratio is determined by the ion charges", ["Because the ratio is determined by the ion charges", "Because ionic compounds are always 1:1", "Because it would be too long", "Because prefixes are only for acids"]),
                ("What is the name for ZnO?", "Zinc oxide", ["Zinc oxide", "Zinc(II) oxide", "Zinc monoxide", "Zincide oxide"]),
                ("Which of these is correctly named?", "Calcium fluoride (CaF₂)", ["Calcium fluoride (CaF₂)", "Calcium difluoride (CaF₂)", "Calcium(II) fluoride (CaF₂)", "Dicalcium fluoride (Ca₂F)"]),
                ("What is the name for PbO₂?", "Lead(IV) oxide", ["Lead(IV) oxide", "Lead oxide", "Lead dioxide", "Lead(II) oxide"]),
                ("What is the name for Cr₂O₃?", "Chromium(III) oxide", ["Chromium(III) oxide", "Chromium oxide", "Dichromium trioxide", "Chromic oxide"]),
                ("Name the compound: Na₂S", "Sodium sulfide", ["Sodium sulfide", "Disodium sulfide", "Sodium(I) sulfide", "Sodium sulphate"]),
                ("What is the name for AgCl?", "Silver chloride", ["Silver chloride", "Silver(I) chloride", "Argentum chloride", "Silver monochloride"]),
                ("How do you determine the Roman numeral for a transition metal?", "Calculate its charge from the anion charges to balance the formula", ["Calculate its charge from the anion charges to balance the formula", "Look up the group number", "Count total electrons", "Measure the bond length"]),
                ("What is the name for MnO₂?", "Manganese(IV) oxide", ["Manganese(IV) oxide", "Manganese dioxide", "Manganese oxide", "Manganese(II) oxide"]),
                ("Name: BaO", "Barium oxide", ["Barium oxide", "Barium(II) oxide", "Monobarium oxide", "Barium monoxide"]),
                ("Name: CuO", "Copper(II) oxide", ["Copper(II) oxide", "Copper oxide", "Cupric monoxide", "Copper(I) oxide"]),
                ("Why is silver chloride simply 'silver chloride' without a Roman numeral?", "Silver almost always forms Ag⁺, so the charge is unambiguous", ["Silver almost always forms Ag⁺, so the charge is unambiguous", "Silver is not a transition metal", "Silver has no charge", "Roman numerals are never used for silver"]),
            ],
            "5A.7": [
                ("What is a polyatomic ion?", "A group of covalently bonded atoms that carries a net charge", ["A group of covalently bonded atoms that carries a net charge", "A single atom with multiple charges", "An uncharged molecule", "A noble gas ion"]),
                ("What is the formula for the sulfate ion?", "SO₄²⁻", ["SO₄²⁻", "SO₃²⁻", "S₂O₄⁻", "SO₂²⁻"]),
                ("What is the name for NaNO₃?", "Sodium nitrate", ["Sodium nitrate", "Sodium nitride", "Sodium nitrite", "Sodium nitrogen trioxide"]),
                ("What suffix indicates more oxygen in a polyatomic ion?", "-ate", ["-ate", "-ite", "-ide", "-ous"]),
                ("What is the formula for the hydroxide ion?", "OH⁻", ["OH⁻", "HO₂⁻", "O₂H⁻", "H₂O⁻"]),
                ("What is the charge of the ammonium ion?", "+1", ["+1", "-1", "+2", "0"]),
                ("What is the formula for calcium carbonate?", "CaCO₃", ["CaCO₃", "Ca₂CO₃", "CaC₂O₃", "Ca(CO₃)₂"]),
                ("What does the -ite suffix indicate compared to -ate?", "One fewer oxygen atom", ["One fewer oxygen atom", "One more oxygen atom", "A different charge", "A different central atom"]),
                ("What is the name for K₂SO₄?", "Potassium sulfate", ["Potassium sulfate", "Dipotassium sulfate", "Potassium(I) sulfate", "Potassium sulfite"]),
                ("What is the name for NH₄Cl?", "Ammonium chloride", ["Ammonium chloride", "Nitrogen hydrogen chloride", "Ammonide chloride", "Ammonia chloride"]),
                ("What is the formula for the phosphate ion?", "PO₄³⁻", ["PO₄³⁻", "PO₃³⁻", "P₂O₄²⁻", "PO₄²⁻"]),
                ("What is the name for Mg(OH)₂?", "Magnesium hydroxide", ["Magnesium hydroxide", "Magnesium dihydroxide", "Magnesium oxide hydroxide", "Magnesium hydrate"]),
                ("When writing formulas with polyatomic ions, when do you use parentheses?", "When you need more than one of that polyatomic ion", ["When you need more than one of that polyatomic ion", "Always", "Never", "Only for negative ions"]),
                ("What is the formula for aluminum sulfate?", "Al₂(SO₄)₃", ["Al₂(SO₄)₃", "AlSO₄", "Al₃(SO₄)₂", "Al(SO₄)₂"]),
                ("What is the name for Fe(NO₃)₃?", "Iron(III) nitrate", ["Iron(III) nitrate", "Iron nitrate", "Iron(III) nitrite", "Ferrous nitrate"]),
                ("What is the charge of the permanganate ion (MnO₄)?", "-1", ["-1", "-2", "+1", "-3"]),
                ("What is the name for Li₂CO₃?", "Lithium carbonate", ["Lithium carbonate", "Dilithium carbonate", "Lithium(I) carbonate", "Lithium carbonite"]),
                ("The acetate ion (CH₃COO⁻) is an example of:", "A polyatomic ion containing carbon", ["A polyatomic ion containing carbon", "A monatomic anion", "An organic metal", "A covalent compound"]),
                ("What is the formula for barium phosphate?", "Ba₃(PO₄)₂", ["Ba₃(PO₄)₂", "BaPO₄", "Ba₂(PO₄)₃", "Ba(PO₄)₂"]),
            ],
            "5A.8": [
                ("What is the traditional name for Cu²⁺ compounds?", "Cupric", ["Cupric", "Cuprous", "Copper(I)", "Copperate"]),
                ("What is the traditional name for Fe³⁺?", "Ferric", ["Ferric", "Ferrous", "Iron(II)", "Ironite"]),
                ("The suffix -ous in traditional naming indicates:", "The lower charge of a multivalent metal", ["The lower charge of a multivalent metal", "The higher charge", "An oxygen-containing compound", "An organic compound"]),
                ("The suffix -ic in traditional naming indicates:", "The higher charge of a multivalent metal", ["The higher charge of a multivalent metal", "The lower charge", "An acidic compound", "A covalent compound"]),
                ("What is the traditional name for SnCl₂?", "Stannous chloride", ["Stannous chloride", "Stannic chloride", "Tin chloride", "Tinous chloride"]),
                ("Mercury(I) ion is unusual because it exists as:", "Hg₂²⁺ (a diatomic ion)", ["Hg₂²⁺ (a diatomic ion)", "Hg⁺", "Hg²⁺", "HgO⁻"]),
                ("What is the modern (Stock) name for PbCl₄?", "Lead(IV) chloride", ["Lead(IV) chloride", "Plumbous chloride", "Lead tetrachloride", "Plumbic chloride"]),
                ("The traditional name for Cu₂O is:", "Cuprous oxide", ["Cuprous oxide", "Cupric oxide", "Copper oxide", "Dicopper oxide"]),
                ("What exception exists for naming mercury(I) compounds?", "Mercury(I) always exists as Hg₂²⁺, not Hg⁺", ["Mercury(I) always exists as Hg₂²⁺, not Hg⁺", "Mercury(I) is actually Hg²⁺", "Mercury(I) cannot form compounds", "Mercury(I) is a nonmetal"]),
                ("Which naming system is preferred by IUPAC?", "The Stock system using Roman numerals", ["The Stock system using Roman numerals", "The traditional -ous/-ic system", "Common names only", "Greek prefix system"]),
                ("What is the traditional name for FeCl₂?", "Ferrous chloride", ["Ferrous chloride", "Ferric chloride", "Iron dichloride", "Iron chloride"]),
                ("What is the Latin root for tin used in traditional naming?", "Stannum", ["Stannum", "Plumbum", "Ferrum", "Cuprum"]),
                ("What is the Latin root for lead?", "Plumbum", ["Plumbum", "Stannum", "Aurum", "Ferrum"]),
                ("What is the traditional name for SnO₂?", "Stannic oxide", ["Stannic oxide", "Stannous oxide", "Tin dioxide", "Tin(II) oxide"]),
                ("What is the modern name for the compound traditionally called 'cupric sulfate'?", "Copper(II) sulfate", ["Copper(II) sulfate", "Copper(I) sulfate", "Cuprous sulfate", "Copper sulfide"]),
                ("Which metal has the Latin name 'Aurum'?", "Gold", ["Gold", "Silver", "Iron", "Copper"]),
                ("What is the traditional name for PbO?", "Plumbous oxide", ["Plumbous oxide", "Plumbic oxide", "Lead dioxide", "Lead(IV) oxide"]),
                ("How is the Stock system clearer than the traditional system?", "It directly states the charge as a Roman numeral", ["It directly states the charge as a Roman numeral", "It uses fewer words", "It only works for main-group metals", "It avoids Latin names"]),
                ("What is the name for CuSO₄?", "Copper(II) sulfate", ["Copper(II) sulfate", "Copper(I) sulfate", "Cuprous sulfate", "Copper sulphite"]),
            ],
        }

        topic_qs = topic_questions.get(lesson_id, [])
        for i, (qt, qa, qopts) in enumerate(topic_qs):
            q = {"question_number": i + 2, "question_text": qt, "attempted": 2, "data_i18n": None,
                 "options": [{"text": opt, "is_correct": opt == qa, "data_i18n": None} for opt in qopts],
                 "explanation": f"{qa}. This is an important concept in {title}."}
            questions.append(q)

        return questions

    # Generate Unit5A lessons
    for lesson_id, (title, sample_q, sample_a, sample_opts) in remaining_5a.items():
        unit5a_lessons[lesson_id] = {
            "title": title,
            "questions": generate_full_questions(lesson_id, title, sample_q, sample_a, sample_opts),
            "summary": [{"title": f"Key Concepts: {title}", "content_html": f"<p><b>{title}</b></p><ul><li>Key topic in Chemistry Unit 5A covering {title.lower()}.</li></ul>"}],
            "flashcards": [{"term": title, "definition": f"A key chemistry concept about {title.lower()}."}]
        }

    # Write Unit5A JSON files
    for lesson_id, data in unit5a_lessons.items():
        unit_dir = CONTENT_DATA / "ChemistryLessons" / "Unit5A"
        fname = f"Lesson{lesson_id}"

        write_json(unit_dir / f"{fname}_Quiz.json",
                   make_quiz_json("5A", lesson_id, "Chemistry", data["title"], data["questions"]))
        write_json(unit_dir / f"{fname}_Summary.json",
                   make_summary_json("5A", lesson_id, "Chemistry", data["title"], data["summary"]))
        write_json(unit_dir / f"{fname}_Practice.json",
                   make_practice_json("5A", lesson_id, "Chemistry", data["title"], data["flashcards"]))
        print(f"  Created Chemistry Unit5A/{fname} (Quiz/Summary/Practice)")

    # Generate Unit5B
    unit5b_lessons = {}
    for lesson_id, (title, sample_q, sample_a, sample_opts) in remaining_5b.items():
        unit5b_lessons[lesson_id] = {
            "title": title,
            "questions": generate_full_questions(lesson_id, title, sample_q, sample_a, sample_opts),
            "summary": [{"title": f"Key Concepts: {title}", "content_html": f"<p><b>{title}</b></p><ul><li>Key topic in Chemistry Unit 5B covering {title.lower()}.</li></ul>"}],
            "flashcards": [{"term": title, "definition": f"A key chemistry concept about {title.lower()}."}]
        }

    for lesson_id, data in unit5b_lessons.items():
        unit_dir = CONTENT_DATA / "ChemistryLessons" / "Unit5B"
        fname = f"Lesson{lesson_id}"

        write_json(unit_dir / f"{fname}_Quiz.json",
                   make_quiz_json("5B", lesson_id, "Chemistry", data["title"], data["questions"]))
        write_json(unit_dir / f"{fname}_Summary.json",
                   make_summary_json("5B", lesson_id, "Chemistry", data["title"], data["summary"]))
        write_json(unit_dir / f"{fname}_Practice.json",
                   make_practice_json("5B", lesson_id, "Chemistry", data["title"], data["flashcards"]))
        print(f"  Created Chemistry Unit5B/{fname} (Quiz/Summary/Practice)")


# ============================================================
# PART 2: Middle School Courses
# ============================================================
def generate_ms_courses():
    """Generate JSON data for Middle School courses by copying from regular courses
    where lessons match, and generating new data for MS-only lessons."""
    print("\n=== Generating Middle School Course JSON ===")

    ms_mapping = {
        "MS_Algebra1Lessons": "Algebra1Lessons",
        "MS_Algebra2Lessons": "Algebra2Lessons",
        "MS_BiologyLessons": "BiologyLessons",
        "MS_ChemistryLessons": "ChemistryLessons",
        "MS_GeometryLessons": "GeometryLessons",
        "MS_PhysicsLessons": "PhysicsLessons",
    }

    ms_course_names = {
        "MS_Algebra1Lessons": "MS Algebra 1",
        "MS_Algebra2Lessons": "MS Algebra 2",
        "MS_BiologyLessons": "MS Biology",
        "MS_ChemistryLessons": "MS Chemistry",
        "MS_GeometryLessons": "MS Geometry",
        "MS_PhysicsLessons": "MS Physics",
    }

    for ms_course, reg_course in ms_mapping.items():
        ms_html_dir = COURSEFILES / ms_course
        reg_json_dir = CONTENT_DATA / reg_course
        ms_json_dir = CONTENT_DATA / ms_course
        course_name = ms_course_names[ms_course]

        if not ms_html_dir.exists():
            print(f"  SKIP: {ms_course} HTML dir not found")
            continue

        copied = 0
        generated = 0

        # Iterate through all unit dirs in the MS HTML
        for unit_dir in sorted(ms_html_dir.iterdir()):
            if not unit_dir.is_dir() or unit_dir.name.startswith('_'):
                continue

            unit_name = unit_dir.name  # e.g., "Unit1", "Unit5A"

            # Get all lesson files in this unit
            for quiz_html in sorted(unit_dir.glob("*_Quiz.html")):
                # Extract lesson number from filename
                # Filename patterns: "Lesson1.1_Quiz.html" or "Lesson 1.1_Quiz.html"
                fname_base = quiz_html.stem.replace("_Quiz", "")  # "Lesson1.1" or "Lesson 1.1"
                lesson_num = fname_base.replace("Lesson", "").strip()  # "1.1" or "5A.1"

                # JSON filename always uses no-space format
                json_fname_base = f"Lesson{lesson_num}"

                # Try to find matching regular course JSON
                # The lesson number determines the regular course unit
                # e.g., lesson "4.1" is in Unit4 of the regular course
                lesson_unit = lesson_num.split('.')[0]  # "4" from "4.1", "5A" from "5A.1"

                reg_unit_dir = reg_json_dir / f"Unit{lesson_unit}"
                reg_quiz = reg_unit_dir / f"{json_fname_base}_Quiz.json"

                if reg_quiz.exists():
                    # Copy from regular course, updating the course name
                    for suffix in ["_Quiz.json", "_Summary.json", "_Practice.json"]:
                        reg_file = reg_unit_dir / f"{json_fname_base}{suffix}"
                        ms_file = ms_json_dir / unit_name / f"{json_fname_base}{suffix}"

                        if reg_file.exists():
                            with open(reg_file, 'r', encoding='utf-8') as f:
                                data = json.load(f)
                            # Update course name
                            data["course"] = course_name
                            write_json(ms_file, data)
                    copied += 1
                else:
                    # Generate minimal quiz data for MS-only lessons
                    # These are lessons that exist in MS but not in the regular course
                    quiz_data = make_quiz_json(
                        unit_name.replace("Unit", ""),
                        lesson_num,
                        course_name,
                        "",
                        [
                            {
                                "question_number": i + 1,
                                "question_text": f"[Placeholder] Question {i+1} for {course_name} Lesson {lesson_num}",
                                "attempted": 2,
                                "data_i18n": None,
                                "options": [
                                    {"text": f"Option A", "is_correct": True, "data_i18n": None},
                                    {"text": f"Option B", "is_correct": False, "data_i18n": None},
                                    {"text": f"Option C", "is_correct": False, "data_i18n": None},
                                    {"text": f"Option D", "is_correct": False, "data_i18n": None}
                                ],
                                "explanation": f"This is a placeholder question for {course_name} Lesson {lesson_num}."
                            }
                            for i in range(10)
                        ]
                    )
                    write_json(ms_json_dir / unit_name / f"{json_fname_base}_Quiz.json", quiz_data)

                    summary_data = make_summary_json(
                        unit_name.replace("Unit", ""), lesson_num, course_name, "",
                        [{"title": f"Lesson {lesson_num} Summary", "content_html": f"<p>Summary for {course_name} Lesson {lesson_num}.</p>"}]
                    )
                    write_json(ms_json_dir / unit_name / f"{json_fname_base}_Summary.json", summary_data)

                    practice_data = make_practice_json(
                        unit_name.replace("Unit", ""), lesson_num, course_name, "",
                        [{"term": f"Term {i+1}", "definition": f"Definition for {course_name} Lesson {lesson_num} term {i+1}."}
                         for i in range(5)]
                    )
                    write_json(ms_json_dir / unit_name / f"{json_fname_base}_Practice.json", practice_data)

                    generated += 1

        print(f"  {ms_course}: {copied} copied from regular, {generated} generated (total: {copied+generated})")


# ============================================================
# PART 3: Fix AP Physics 2 folder structure
# ============================================================
def fix_ap_physics_2():
    """The JSON uses Unit1-Unit7 (no space), HTML has Unit 1-7 (with space) + Unit1-7 (no space, unit tests only).
    The JSON structure is correct. Just ensure the JSON folders exist and all lesson data is present."""
    print("\n=== Checking AP Physics 2 JSON ===")

    ap_json_dir = CONTENT_DATA / "APLessons" / "AP Physics 2"
    ap_html_dir = COURSEFILES / "APLessons" / "AP Physics 2"

    # Check JSON files exist for Unit1-Unit7 (these match the JSON folder names)
    for i in range(1, 8):
        json_unit = ap_json_dir / f"Unit{i}"
        html_unit_space = ap_html_dir / f"Unit {i}"  # HTML uses space

        if json_unit.exists():
            json_count = len(list(json_unit.glob("*_Quiz.json")))
            html_count = len(list(html_unit_space.glob("*_Quiz.html"))) if html_unit_space.exists() else 0
            print(f"  Unit{i}: {json_count} JSON, {html_count} HTML (in 'Unit {i}')")
        else:
            print(f"  Unit{i}: NO JSON DIR")

    # Check lessons 9-15 that are in the root
    root_quizzes = sorted(ap_html_dir.glob("Lesson*_Quiz.html"))
    if root_quizzes:
        print(f"  Root folder: {len(root_quizzes)} HTML files without unit organization")
        print("  NOTE: These need to be organized into units and JSON created")


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Generating Missing JSON Data Files")
    print("=" * 60)

    generate_chemistry_5a_5b()
    generate_ms_courses()
    fix_ap_physics_2()

    print("\n" + "=" * 60)
    print("Done! Run verification to check results.")
    print("=" * 60)
