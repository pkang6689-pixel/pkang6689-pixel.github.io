#!/usr/bin/env python3
"""
Clean up Unit5A and Unit5B Practice files to match Unit10 format:
1. Remove inline switchToClimb/switchToFlashcards/DOMContentLoaded script block
2. Remove inline Climb Game Logic IIFE script block
3. Remove extra script tags (quiz_ui.js, blocks_puzzle.js, game_utils.js, search_data.js, search_logic.js)
4. Normalize script paths to relative
5. Add window.lessonFlashcards data
"""
import os
import re

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     "ArisEdu Project Folder", "ChemistryLessons")

# Flashcard data for each lesson
FLASHCARD_DATA = {
    # Unit 5A
    "5A.1": [
        {"question": "What type of electrons are involved in bond formation?", "answer": "Valence electrons"},
        {"question": "Is energy released or absorbed when bonds form?", "answer": "Released"},
        {"question": "Is energy released or absorbed when bonds break?", "answer": "Absorbed"},
        {"question": "What is nomenclature?", "answer": "The system of naming chemical compounds"},
        {"question": "What determines how a compound is named?", "answer": "The type of bond (ionic vs covalent)"},
        {"question": "What two main types of bonds are there?", "answer": "Ionic and covalent"},
        {"question": "Which electrons determine bonding behavior?", "answer": "Valence electrons"},
        {"question": "What holds atoms together in a compound?", "answer": "Chemical bonds"},
        {"question": "Why is naming compounds important in chemistry?", "answer": "It provides a universal way to identify substances"},
        {"question": "What is a chemical formula?", "answer": "A representation using symbols and numbers to show a compound's composition"},
    ],
    "5A.2": [
        {"question": "What is net charge?", "answer": "The overall charge of an atom or ion (protons minus electrons)"},
        {"question": "What is an ion?", "answer": "An atom that has gained or lost electrons"},
        {"question": "What is a cation?", "answer": "A positively charged ion (lost electrons)"},
        {"question": "What is an anion?", "answer": "A negatively charged ion (gained electrons)"},
        {"question": "What happens to the charge when an atom loses an electron?", "answer": "It becomes positive (cation)"},
        {"question": "What happens to the charge when an atom gains an electron?", "answer": "It becomes negative (anion)"},
        {"question": "What is the charge of a proton?", "answer": "+1"},
        {"question": "What is the charge of an electron?", "answer": "-1"},
        {"question": "If an atom has 11 protons and 10 electrons, what is its net charge?", "answer": "+1"},
        {"question": "What particle determines the charge of an ion?", "answer": "Electrons (gained or lost)"},
    ],
    "5A.3": [
        {"question": "What must happen for a chemical bond to form?", "answer": "Atoms must share or transfer valence electrons"},
        {"question": "What electrons are involved in bond formation?", "answer": "Valence electrons"},
        {"question": "Is energy released or absorbed when bonds form?", "answer": "Released"},
        {"question": "Is energy released or absorbed to break bonds?", "answer": "Absorbed"},
        {"question": "What is a stable electron configuration?", "answer": "A full outer electron shell (octet)"},
        {"question": "What is the octet rule?", "answer": "Atoms tend to gain, lose, or share electrons to have 8 valence electrons"},
        {"question": "How many valence electrons do noble gases have?", "answer": "8 (except helium which has 2)"},
        {"question": "Why do atoms form bonds?", "answer": "To achieve a stable electron configuration"},
        {"question": "What is the duet rule?", "answer": "Hydrogen and helium are stable with 2 electrons"},
        {"question": "Which group of elements rarely forms bonds?", "answer": "Noble gases (Group 18)"},
    ],
    "5A.4": [
        {"question": "Ionic bonds involve _____ of electrons.", "answer": "Transfer"},
        {"question": "Ionic bonds occur between what types of elements?", "answer": "Metal and nonmetal"},
        {"question": "What structure do ionic compounds form?", "answer": "Crystal lattice"},
        {"question": "Do ionic compounds conduct electricity?", "answer": "When melted or dissolved (electrolyte)"},
        {"question": "What is an electrolyte?", "answer": "A substance that conducts electricity when dissolved in water"},
        {"question": "Do ionic compounds have high or low melting points?", "answer": "High melting points"},
        {"question": "Which element transfers electrons in an ionic bond?", "answer": "The metal"},
        {"question": "Which element receives electrons in an ionic bond?", "answer": "The nonmetal"},
        {"question": "What is a crystal lattice?", "answer": "A repeating 3D pattern of alternating positive and negative ions"},
        {"question": "Are ionic compounds brittle or flexible?", "answer": "Brittle"},
    ],
    "5A.5": [
        {"question": "What is the crisscross method?", "answer": "A method where ion charges become subscripts in the chemical formula"},
        {"question": "Using crisscross, what is the formula for aluminum oxide (Al³⁺ and O²⁻)?", "answer": "Al₂O₃"},
        {"question": "Using crisscross, what is the formula for calcium chloride (Ca²⁺ and Cl⁻)?", "answer": "CaCl₂"},
        {"question": "What is the formula for sodium oxide (Na⁺ and O²⁻)?", "answer": "Na₂O"},
        {"question": "What do you do if the subscripts can be reduced?", "answer": "Simplify them to the lowest whole-number ratio"},
        {"question": "When do you use parentheses in a chemical formula?", "answer": "When a polyatomic ion needs a subscript greater than 1"},
        {"question": "What is the formula for magnesium chloride?", "answer": "MgCl₂"},
        {"question": "In the crisscross method, what becomes the subscript?", "answer": "The charge number of the other ion"},
        {"question": "What is the formula for potassium sulfide (K⁺ and S²⁻)?", "answer": "K₂S"},
        {"question": "Why must formulas have a net charge of zero?", "answer": "Because ionic compounds are electrically neutral"},
    ],
    "5A.6": [
        {"question": "What is the name for NaCl?", "answer": "Sodium chloride"},
        {"question": "What is the name for MgO?", "answer": "Magnesium oxide"},
        {"question": "Do we use prefixes for ionic compound names?", "answer": "No"},
        {"question": "How do we indicate multiple charges for transition metals?", "answer": "Roman numerals in parentheses"},
        {"question": "What ending do anions get in ionic naming?", "answer": "-ide"},
        {"question": "What is the name for CaBr₂?", "answer": "Calcium bromide"},
        {"question": "What is the name for FeCl₃?", "answer": "Iron(III) chloride"},
        {"question": "Which element is named first in an ionic compound?", "answer": "The metal (cation)"},
        {"question": "What is the name for Al₂O₃?", "answer": "Aluminum oxide"},
        {"question": "When are Roman numerals needed in ionic naming?", "answer": "When the metal can have more than one charge (transition metals)"},
    ],
    "5A.7": [
        {"question": "What is NO₃⁻?", "answer": "Nitrate"},
        {"question": "What is SO₄²⁻?", "answer": "Sulfate"},
        {"question": "What is OH⁻?", "answer": "Hydroxide"},
        {"question": "What is NH₄⁺?", "answer": "Ammonium"},
        {"question": "What is PO₄³⁻?", "answer": "Phosphate"},
        {"question": "What is a polyatomic ion?", "answer": "A group of atoms that carries a charge and acts as a single ion"},
        {"question": "What is CO₃²⁻?", "answer": "Carbonate"},
        {"question": "What ending do most polyatomic ions have?", "answer": "-ate or -ite"},
        {"question": "What is the formula for calcium hydroxide?", "answer": "Ca(OH)₂"},
        {"question": "Why do we use parentheses around polyatomic ions?", "answer": "To show the subscript applies to the entire polyatomic ion"},
    ],
    "5A.8": [
        {"question": "What is the common name for H₂O?", "answer": "Water"},
        {"question": "What is the common name for NH₃?", "answer": "Ammonia"},
        {"question": "What type of naming uses '-ous' and '-ic' suffixes?", "answer": "Traditional (or classical) naming"},
        {"question": "In traditional naming, '-ous' indicates what?", "answer": "The lower charge of a metal"},
        {"question": "In traditional naming, '-ic' indicates what?", "answer": "The higher charge of a metal"},
        {"question": "What is Fe²⁺ called in traditional naming?", "answer": "Ferrous"},
        {"question": "What is Fe³⁺ called in traditional naming?", "answer": "Ferric"},
        {"question": "What is Cu⁺ called in traditional naming?", "answer": "Cuprous"},
        {"question": "What is Cu²⁺ called in traditional naming?", "answer": "Cupric"},
        {"question": "What naming system uses Roman numerals instead of -ous/-ic?", "answer": "Stock system (IUPAC)"},
    ],
    # Unit 5B
    "5B.1": [
        {"question": "Covalent bonds involve _____ of electrons.", "answer": "Sharing"},
        {"question": "Covalent bonds occur between what types of elements?", "answer": "Nonmetal and nonmetal"},
        {"question": "Are covalent compounds usually electrolytes?", "answer": "No"},
        {"question": "Do covalent compounds have high or low melting points?", "answer": "Low (usually)"},
        {"question": "What is a molecule?", "answer": "A group of atoms held together by covalent bonds"},
        {"question": "How many electrons are shared in a single covalent bond?", "answer": "2 (one pair)"},
        {"question": "How many electrons are shared in a double bond?", "answer": "4 (two pairs)"},
        {"question": "How many electrons are shared in a triple bond?", "answer": "6 (three pairs)"},
        {"question": "Are covalent compounds typically solid, liquid, or gas at room temperature?", "answer": "They can be any state, but many are liquids or gases"},
        {"question": "Do covalent compounds dissolve well in water?", "answer": "Some do, some don't — depends on polarity"},
    ],
    "5B.2": [
        {"question": "What prefix means 1?", "answer": "Mono-"},
        {"question": "What prefix means 2?", "answer": "Di-"},
        {"question": "What prefix means 3?", "answer": "Tri-"},
        {"question": "What prefix means 4?", "answer": "Tetra-"},
        {"question": "What is the name for CO?", "answer": "Carbon monoxide"},
        {"question": "What is the name for CO₂?", "answer": "Carbon dioxide"},
        {"question": "What prefix means 5?", "answer": "Penta-"},
        {"question": "What prefix means 6?", "answer": "Hexa-"},
        {"question": "Do we use prefixes for ionic or covalent compound names?", "answer": "Covalent"},
        {"question": "What is the name for N₂O₅?", "answer": "Dinitrogen pentoxide"},
    ],
    "5B.3": [
        {"question": "Describe metallic bonding.", "answer": "Sea of electrons — metal cations surrounded by delocalized electrons"},
        {"question": "Are electrons fixed or mobile in metals?", "answer": "Mobile (delocalized)"},
        {"question": "What property allows metals to be hammered into sheets?", "answer": "Malleability"},
        {"question": "What property allows metals to be drawn into wires?", "answer": "Ductility"},
        {"question": "Why are metals good conductors of electricity?", "answer": "Because of their delocalized (free-moving) electrons"},
        {"question": "Why are metals good conductors of heat?", "answer": "Free electrons transfer kinetic energy quickly"},
        {"question": "What is metallic luster?", "answer": "The shiny appearance of metals due to electron interaction with light"},
        {"question": "Do metallic bonds involve transfer, sharing, or pooling of electrons?", "answer": "Pooling (delocalized sea of electrons)"},
        {"question": "What type of elements form metallic bonds?", "answer": "Metals with other metals"},
        {"question": "Are metals generally hard or soft?", "answer": "Most are hard, but some (like sodium) are soft"},
    ],
    "5B.4": [
        {"question": "What element is the basis of organic chemistry?", "answer": "Carbon"},
        {"question": "How many bonds can carbon form?", "answer": "4"},
        {"question": "What is a hydrocarbon?", "answer": "A compound made of only carbon and hydrogen"},
        {"question": "What is the simplest hydrocarbon?", "answer": "Methane (CH₄)"},
        {"question": "What type of bond do organic compounds primarily contain?", "answer": "Covalent bonds"},
        {"question": "What is an organic compound?", "answer": "A compound containing carbon (usually bonded to hydrogen and other elements)"},
        {"question": "What is the general formula for alkanes?", "answer": "CₙH₂ₙ₊₂"},
        {"question": "What prefix indicates 2 carbons?", "answer": "Eth-"},
        {"question": "What prefix indicates 3 carbons?", "answer": "Prop-"},
        {"question": "What suffix indicates a single bond (alkane)?", "answer": "-ane"},
    ],
    "5B.5": [
        {"question": "NaCl is named using which naming system?", "answer": "Ionic naming (no prefixes)"},
        {"question": "CO₂ is named using which naming system?", "answer": "Covalent naming (with prefixes)"},
        {"question": "How do you determine if a compound is ionic or covalent?", "answer": "Check if it contains a metal (ionic) or only nonmetals (covalent)"},
        {"question": "What is the name for MgCl₂?", "answer": "Magnesium chloride"},
        {"question": "What is the name for P₂O₅?", "answer": "Diphosphorus pentoxide"},
        {"question": "What is the name for CuO if copper has a +2 charge?", "answer": "Copper(II) oxide"},
        {"question": "What type of bond forms between Na and Cl?", "answer": "Ionic bond"},
        {"question": "What type of bond forms between N and O?", "answer": "Covalent bond"},
        {"question": "Do ionic compounds use prefixes in their names?", "answer": "No"},
        {"question": "Do covalent compounds use prefixes in their names?", "answer": "Yes"},
    ],
}


def format_flashcards(lesson_key):
    """Format flashcard data as a JavaScript array string."""
    cards = FLASHCARD_DATA.get(lesson_key, [])
    if not cards:
        return "[]"
    
    lines = []
    for card in cards:
        q = card["question"].replace('"', '\\"')
        a = card["answer"].replace('"', '\\"')
        lines.append(f'          {{ question: "{q}", answer: "{a}" }}')
    return "[\n" + ",\n".join(lines) + "\n      ]"


def clean_practice_file(filepath):
    """Clean a Practice HTML file to match the Unit10 format."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Extract lesson number for flashcard data
    bn = os.path.basename(filepath)
    m = re.search(r'Lesson (\d+[AB]?\.\d+)', bn)
    lesson_key = m.group(1) if m else None
    
    # 1. Remove inline switchToClimb/switchToFlashcards/DOMContentLoaded script block
    # Pattern: <script> ... window.switchToClimb = function() ... document.addEventListener('DOMContentLoaded' ... </script>
    pattern = r'<script>\s*\n\s*window\.switchToClimb\s*=\s*function.*?</script>'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        changes.append("Removed inline switchToClimb/switchToFlashcards/DOMContentLoaded block")
    
    # 2. Remove inline Climb Game Logic IIFE
    # Pattern: <script>\n// Climb Game Logic\n(function() { ... })();\n</script>
    pattern = r'<script>\s*\n\s*//\s*Climb Game Logic\s*\n\s*\(function\(\)\s*\{.*?\}\)\(\);\s*\n\s*</script>'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        changes.append("Removed inline Climb Game Logic IIFE (~350 lines)")
    
    # 3. Remove extra script tags
    extra_scripts = [
        (r'<script\s+src="[^"]*quiz_ui\.js"[^>]*>\s*</script>\s*\n?', "quiz_ui.js"),
        (r'<script\s+src="[^"]*blocks_puzzle\.js"[^>]*>\s*</script>\s*\n?', "blocks_puzzle.js"),
        (r'<script\s+src="[^"]*game_utils\.js"[^>]*>\s*</script>\s*\n?', "game_utils.js"),
        (r'<script\s+src="[^"]*search_data\.js"[^>]*>\s*</script>\s*\n?', "search_data.js"),
        (r'<script\s+src="[^"]*search_logic\.js"[^>]*>\s*</script>\s*\n?', "search_logic.js"),
    ]
    
    for pattern, name in extra_scripts:
        if re.search(pattern, content):
            content = re.sub(pattern, '', content)
            changes.append(f"Removed {name} script tag")
    
    # Also remove the HTML comment for search
    content = re.sub(r'<!-- ArisEdu Global Search -->\s*\n?', '', content)
    
    # 4. Normalize absolute script paths to relative
    abs_patterns = [
        (r'<script\s+src="/ArisEdu Project Folder/scripts/taskbar\.js"', '<script src="../../scripts/taskbar.js"'),
        (r'<script\s+src="/ArisEdu Project Folder/scripts/practice_games\.js"', '<script src="../../scripts/practice_games.js"'),
        (r'<script\s+src="/ArisEdu Project Folder/scripts/block_puzzle\.js"', '<script src="../../scripts/block_puzzle.js"'),
        (r'<script\s+src="/ArisEdu Project Folder/scripts/game_utils\.js"', '<script src="../../scripts/game_utils.js"'),
    ]
    
    for pattern, replacement in abs_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes.append(f"Normalized script path: {replacement.split('src=')[1]}")
    
    # 5. Add window.lessonFlashcards data if missing
    if lesson_key and 'window.lessonFlashcards =' not in content:
        flashcard_js = format_flashcards(lesson_key)
        # Insert before taskbar.js script tag
        insert_pattern = r'(<script\s+src="../../scripts/taskbar\.js")'
        replacement = f'''<!-- Game Logic & Data -->
<script>
    window.lessonFlashcards = {flashcard_js};
</script>
\\1'''
        if re.search(insert_pattern, content):
            content = re.sub(insert_pattern, replacement, content)
            changes.append(f"Added window.lessonFlashcards data ({len(FLASHCARD_DATA.get(lesson_key, []))} cards)")
    
    # 6. Clean up excessive blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    
    return []


def main():
    total_changes = 0
    files_changed = 0
    
    for unit in ['Unit5A', 'Unit5B']:
        unit_dir = os.path.join(BASE, unit)
        if not os.path.exists(unit_dir):
            print(f"Directory not found: {unit_dir}")
            continue
        
        print(f"\n=== {unit} ===")
        
        for fn in sorted(os.listdir(unit_dir)):
            if not fn.endswith('_Practice.html'):
                continue
            
            filepath = os.path.join(unit_dir, fn)
            changes = clean_practice_file(filepath)
            
            if changes:
                files_changed += 1
                total_changes += len(changes)
                print(f"  {fn}: {len(changes)} changes")
                for c in changes:
                    print(f"    - {c}")
            else:
                print(f"  {fn}: no changes needed")
    
    print(f"\n=== Summary ===")
    print(f"Files changed: {files_changed}")
    print(f"Total changes: {total_changes}")
    
    # Verify results
    print(f"\n=== Verification ===")
    for unit in ['Unit5A', 'Unit5B']:
        unit_dir = os.path.join(BASE, unit)
        for fn in sorted(os.listdir(unit_dir)):
            if not fn.endswith('_Practice.html'):
                continue
            filepath = os.path.join(unit_dir, fn)
            with open(filepath, 'r') as f:
                content = f.read()
            lines = content.count('\n') + 1
            
            issues = []
            if 'switchToClimb = function' in content:
                issues.append("still has inline switchToClimb")
            if '// Climb Game Logic' in content:
                issues.append("still has inline Climb Game Logic")
            if 'quiz_ui.js' in content:
                issues.append("still has quiz_ui.js")
            if 'blocks_puzzle.js' in content:
                issues.append("still has blocks_puzzle.js")
            if 'game_utils.js' in content:
                issues.append("still has game_utils.js")
            if 'window.lessonFlashcards =' not in content:
                issues.append("MISSING flashcard data")
            if 'taskbar.js' not in content:
                issues.append("MISSING taskbar.js")
            if 'practice_games.js' not in content:
                issues.append("MISSING practice_games.js")
            if 'block_puzzle.js' not in content:
                issues.append("MISSING block_puzzle.js")
            
            status = ", ".join(issues) if issues else "OK"
            print(f"  {fn}: {lines} lines — {status}")


if __name__ == "__main__":
    main()
