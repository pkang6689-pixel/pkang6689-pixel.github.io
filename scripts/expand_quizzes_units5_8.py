#!/usr/bin/env python3
"""Expand quiz files for Units 5A, 5B, 6, 7, 8 from 2 questions to 7 questions each."""

import os
import re
import random

BASE = os.path.join(os.path.dirname(__file__), '..', 'ArisEdu Project Folder', 'ChemistryLessons')

LESSONS = {
    # ===== UNIT 5A: Ionic Bonds & Nomenclature =====
    "Unit5A": {
        "5A.1": {
            "topic": "Introduction to Nomenclature",
            "questions": [
                ("Nomenclature in chemistry refers to:", "The system of naming compounds", ["The study of electrons", "How to balance equations", "The periodic table layout"]),
                ("The two main categories of chemical compounds are:", "Ionic and covalent", ["Organic and inorganic only", "Acids and bases", "Metals and nonmetals"]),
                ("In naming ionic compounds, the metal name comes:", "First", ["Last", "After the nonmetal", "It is not used"]),
                ("The suffix '-ide' indicates:", "A monatomic anion", ["A polyatomic ion", "An acid", "A metal"]),
                ("What type of compound is NaCl?", "Ionic compound", ["Covalent compound", "Organic compound", "Acid"]),
                ("Chemical formulas represent:", "The ratio of atoms in a compound", ["Only the mass", "Only the charge", "The color of its substance"]),
                ("The name for MgO is:", "Magnesium oxide", ["Magnesium oxygen", "Mono-magnesium oxide", "Magnesium dioxide"]),
            ]
        },
        "5A.2": {
            "topic": "Net Charge",
            "questions": [
                ("An ion with a positive charge is called a:", "Cation", ["Anion", "Isotope", "Neutron"]),
                ("An ion with a negative charge is called an:", "Anion", ["Cation", "Proton", "Positron"]),
                ("A neutral atom becomes a cation by:", "Losing electrons", ["Gaining electrons", "Losing protons", "Gaining neutrons"]),
                ("If an atom has 11 protons and 10 electrons, its charge is:", "+1", ["-1", "0", "+2"]),
                ("The net charge of Na⁺ is:", "+1 because it lost one electron", ["-1 because it gained one electron", "0 because it is neutral", "+2 because it lost two electrons"]),
                ("Cl⁻ has a charge of -1 because it:", "Gained one electron", ["Lost one electron", "Lost one proton", "Gained one proton"]),
                ("A neutral compound has:", "A net charge of zero", ["Only positive charges", "Only negative charges", "No ions"]),
            ]
        },
        "5A.3": {
            "topic": "Bond Formation",
            "questions": [
                ("Chemical bonds form to:", "Achieve a stable electron configuration", ["Increase energy", "Create radioactive atoms", "Decrease the number of protons"]),
                ("The octet rule states that atoms tend to:", "Gain, lose, or share electrons to have 8 valence electrons", ["Have 8 protons", "Form 8 bonds", "Have 8 neutrons"]),
                ("Ionic bonds form between:", "A metal and a nonmetal", ["Two nonmetals", "Two metals", "Two noble gases"]),
                ("In ionic bond formation, electrons are:", "Transferred from one atom to another", ["Shared equally", "Shared unequally", "Destroyed"]),
                ("Metals tend to form ions with:", "Positive charges (cations)", ["Negative charges (anions)", "No charge", "Variable charges only"]),
                ("Nonmetals tend to form ions with:", "Negative charges (anions)", ["Positive charges (cations)", "No charge", "Double positive charges"]),
                ("The driving force behind bond formation is:", "Achieving lower energy (more stable state)", ["Increasing energy", "Breaking apart atoms", "Removing protons"]),
            ]
        },
        "5A.4": {
            "topic": "Ionic Bonds",
            "questions": [
                ("An ionic bond is formed by:", "The transfer of electrons from a metal to a nonmetal", ["Sharing of electrons", "Nuclear fusion", "Magnetic attraction"]),
                ("Which property is characteristic of ionic compounds?", "High melting points", ["Low melting points", "Soft texture", "Poor conductivity in all states"]),
                ("Ionic compounds conduct electricity when:", "Dissolved in water or melted", ["In solid form", "Frozen", "In a vacuum"]),
                ("The crystal lattice structure of ionic compounds makes them:", "Hard and brittle", ["Soft and flexible", "Gaseous at room temperature", "Magnetic"]),
                ("NaCl is formed when sodium:", "Transfers one electron to chlorine", ["Shares electrons with chlorine", "Absorbs chlorine", "Repels chlorine"]),
                ("The electrostatic attraction in ionic bonds is between:", "Positive and negative ions", ["Two positive ions", "Two neutral atoms", "Protons and neutrons"]),
                ("Which pair would most likely form an ionic bond?", "Na and Cl", ["H and O", "C and H", "N and O"]),
            ]
        },
        "5A.5": {
            "topic": "Crisscross Method",
            "questions": [
                ("The crisscross method uses what numbers to write formulas?", "Ionic charges as subscripts", ["Atomic masses", "Atomic numbers", "Electron counts"]),
                ("Using the crisscross method for Al³⁺ and O²⁻, the formula is:", "Al₂O₃", ["AlO", "Al₃O₂", "AlO₃"]),
                ("For Ca²⁺ and Cl⁻, the crisscross method gives:", "CaCl₂", ["Ca₂Cl", "CaCl", "Ca₂Cl₂"]),
                ("After crisscrossing, you should always:", "Reduce subscripts to lowest ratio", ["Add the charges", "Multiply by 2", "Leave them as written"]),
                ("For K⁺ and S²⁻, the correct formula is:", "K₂S", ["KS", "KS₂", "K₂S₂"]),
                ("The formula for magnesium fluoride (Mg²⁺, F⁻) is:", "MgF₂", ["Mg₂F", "MgF", "Mg₂F₂"]),
                ("In the crisscross method, a subscript of 1 is:", "Not written", ["Always written", "Written only for metals", "Written as a superscript"]),
            ]
        },
        "5A.6": {
            "topic": "Naming Ionic Compounds",
            "questions": [
                ("The name for CaBr₂ is:", "Calcium bromide", ["Calcium bromine", "Calcium dibromide", "Di-calcium bromide"]),
                ("When naming ionic compounds, the cation is named:", "First, using the element name", ["Last", "With a prefix", "With the -ide suffix"]),
                ("The anion ending '-ide' replaces:", "The original ending of the nonmetal name", ["The metal name", "The charge number", "Nothing"]),
                ("What is the name of Li₂O?", "Lithium oxide", ["Dilithium oxide", "Lithium oxygen", "Lithium dioxide"]),
                ("Transition metals with multiple charges use:", "Roman numerals in the name", ["Greek prefixes", "Subscript numbers", "The suffix -ous or -ic only"]),
                ("The name for FeCl₃ is:", "Iron(III) chloride", ["Iron chloride", "Iron(II) chloride", "Tri-iron chloride"]),
                ("What is the name of Al₂O₃?", "Aluminum oxide", ["Dialuminum trioxide", "Aluminum(III) oxide", "Aluminum oxygen"]),
            ]
        },
        "5A.7": {
            "topic": "Polyatomic Ions",
            "questions": [
                ("A polyatomic ion is:", "A group of atoms with a net charge", ["A single atom with a charge", "A neutral molecule", "A type of element"]),
                ("The formula for the hydroxide ion is:", "OH⁻", ["HO⁺", "OH₂", "O₂H⁻"]),
                ("The name for the SO₄²⁻ ion is:", "Sulfate", ["Sulfite", "Sulfide", "Sulfur oxide"]),
                ("What is the formula for ammonium?", "NH₄⁺", ["NH₃", "NO₃⁻", "N₂H₄"]),
                ("The carbonate ion (CO₃²⁻) combined with sodium gives:", "Na₂CO₃", ["NaCO₃", "Na₃CO₃", "Na(CO₃)₂"]),
                ("Parentheses are used in formulas when:", "A polyatomic ion needs a subscript greater than 1", ["The compound is organic", "There is only one ion", "The metal has multiple charges"]),
                ("The nitrate ion has the formula:", "NO₃⁻", ["NO₂⁻", "N₂O₃⁻", "NH₄⁺"]),
            ]
        },
        "5A.8": {
            "topic": "Common Exceptions & Traditional Names",
            "questions": [
                ("Mercury(I) ion exists as:", "Hg₂²⁺ (diatomic pair)", ["Hg⁺", "Hg²⁺", "HgO"]),
                ("The traditional name 'ferrous' refers to:", "Fe²⁺ (iron with +2 charge)", ["Fe³⁺", "Fe⁰", "FeO₂"]),
                ("The traditional name 'ferric' refers to:", "Fe³⁺ (iron with +3 charge)", ["Fe²⁺", "Fe⁰", "Fe⁴⁺"]),
                ("Cuprous refers to copper with a charge of:", "+1", ["+2", "+3", "0"]),
                ("Which compound has a common name rather than systematic?", "Water (H₂O)", ["NaCl", "CaBr₂", "Al₂O₃"]),
                ("The suffix '-ous' in traditional naming indicates:", "The lower charge of the metal", ["The higher charge", "A nonmetal", "A polyatomic ion"]),
                ("The suffix '-ic' in traditional naming indicates:", "The higher charge of the metal", ["The lower charge", "A nonmetal", "An acid"]),
            ]
        },
    },
    # ===== UNIT 5B: Covalent Bonds & Nomenclature =====
    "Unit5B": {
        "5B.1": {
            "topic": "Covalent Bonds",
            "questions": [
                ("A covalent bond forms when atoms:", "Share electrons", ["Transfer electrons", "Lose protons", "Gain neutrons"]),
                ("Covalent bonds typically form between:", "Two nonmetals", ["A metal and a nonmetal", "Two metals", "A metal and a noble gas"]),
                ("A double bond involves sharing:", "4 electrons (2 pairs)", ["2 electrons (1 pair)", "6 electrons (3 pairs)", "1 electron"]),
                ("A triple bond involves sharing:", "6 electrons (3 pairs)", ["2 electrons", "4 electrons", "8 electrons"]),
                ("Covalent compounds generally have:", "Low melting and boiling points", ["Very high melting points", "High electrical conductivity", "Crystal lattice structures"]),
                ("A nonpolar covalent bond has:", "Equal sharing of electrons", ["Unequal sharing of electrons", "Complete transfer of electrons", "No electrons shared"]),
                ("A polar covalent bond has:", "Unequal sharing of electrons", ["Equal sharing of electrons", "Complete transfer of electrons", "No bond at all"]),
            ]
        },
        "5B.2": {
            "topic": "Naming Covalent Compounds",
            "questions": [
                ("Covalent compound names use:", "Greek prefixes to indicate number of atoms", ["Roman numerals", "No special system", "Only the element names"]),
                ("The prefix 'di-' means:", "2", ["1", "3", "4"]),
                ("The prefix 'tri-' means:", "3", ["2", "4", "5"]),
                ("The name for CO₂ is:", "Carbon dioxide", ["Carbon oxide", "Monocarbon dioxide", "Carbonic oxide"]),
                ("The name for N₂O₅ is:", "Dinitrogen pentoxide", ["Nitrogen pentoxide", "Dinitrogen oxide", "Nitrogen(V) oxide"]),
                ("The prefix 'mono-' is only used on:", "The second element", ["The first element", "Both elements", "Neither element"]),
                ("The name for PCl₃ is:", "Phosphorus trichloride", ["Phosphorus chloride", "Triphosphorus chloride", "Phosphorus(III) chloride"]),
            ]
        },
        "5B.3": {
            "topic": "Metallic Bonds",
            "questions": [
                ("Metallic bonds involve:", "A sea of delocalized electrons", ["Transfer of electrons", "Sharing of electron pairs", "Magnetic attraction"]),
                ("The 'sea of electrons' model explains why metals are:", "Good conductors of electricity", ["Poor conductors", "Brittle", "Gaseous"]),
                ("Metals are malleable because:", "Layers of atoms can slide past each other", ["They have no bonds", "Their electrons are fixed", "They are very light"]),
                ("Which property is due to metallic bonding?", "Luster (shininess)", ["Low boiling point", "Brittleness", "Electrical insulation"]),
                ("Metallic bonds are generally found in:", "Pure metals and alloys", ["Ionic compounds", "Covalent molecules", "Noble gases"]),
                ("An alloy is:", "A mixture of metals", ["A pure element", "An ionic compound", "A gas"]),
                ("Metals have high melting points because:", "Metallic bonds are strong throughout the structure", ["They have weak bonds", "They are always solid", "They contain no electrons"]),
            ]
        },
        "5B.4": {
            "topic": "Organic Compounds",
            "questions": [
                ("Organic compounds always contain:", "Carbon", ["Nitrogen", "Oxygen", "Sulfur"]),
                ("Carbon can form how many bonds?", "4", ["2", "6", "8"]),
                ("Hydrocarbons contain only:", "Carbon and hydrogen", ["Carbon and oxygen", "Hydrogen and oxygen", "Carbon and nitrogen"]),
                ("The simplest hydrocarbon is:", "Methane (CH₄)", ["Ethane (C₂H₆)", "Propane (C₃H₈)", "Butane (C₄H₁₀)"]),
                ("Organic compounds are the basis of:", "Living organisms and many fuels", ["Only plastics", "Only rocks", "Noble gases"]),
                ("A functional group determines:", "The chemical properties of an organic molecule", ["The number of carbons", "The mass of the molecule", "The atomic number"]),
                ("Isomers are compounds with:", "Same formula but different structures", ["Different formulas and structures", "Same structure and formula", "No carbon atoms"]),
            ]
        },
        "5B.5": {
            "topic": "Mixed Nomenclature Practice",
            "questions": [
                ("NaBr is named:", "Sodium bromide (ionic naming)", ["Sodium monobromide", "Monosodium bromide", "Sodium(I) bromide"]),
                ("CO is named:", "Carbon monoxide (covalent naming)", ["Carbon oxide", "Monocarbon monoxide", "Carbon(II) oxide"]),
                ("Fe₂O₃ is named:", "Iron(III) oxide", ["Iron oxide", "Diiron trioxide", "Ferrous oxide"]),
                ("To determine naming rules, first identify if the compound is:", "Ionic or covalent", ["Organic or inorganic", "Large or small", "Gaseous or solid"]),
                ("Which compound uses Greek prefixes in its name?", "N₂O₄ (dinitrogen tetroxide)", ["NaCl", "CaO", "FeBr₃"]),
                ("Which compound uses Roman numerals in its name?", "CuCl₂ (copper(II) chloride)", ["CO₂", "H₂O", "NaCl"]),
                ("The compound P₄O₁₀ is named:", "Tetraphosphorus decoxide", ["Phosphorus oxide", "Phosphorus(V) oxide", "Quadphosphorus oxide"]),
            ]
        },
    },
    # ===== UNIT 6: Chemical Reactions =====
    "Unit6": {
        "6.1": {
            "topic": "Types of Reactions",
            "questions": [
                ("In a synthesis reaction, two or more substances combine to form:", "One product", ["Two products", "No products", "An element"]),
                ("A decomposition reaction breaks:", "One compound into simpler substances", ["Two compounds into one", "Elements into atoms", "Products into reactants"]),
                ("In a single replacement reaction:", "One element replaces another in a compound", ["Two compounds swap ions", "A compound breaks apart", "Elements combine"]),
                ("A double replacement reaction involves:", "Two compounds exchanging ions", ["A single element replacing another", "Breaking down a compound", "Combining two elements"]),
                ("AB → A + B represents what type of reaction?", "Decomposition", ["Synthesis", "Single replacement", "Combustion"]),
                ("A + B → AB represents what type of reaction?", "Synthesis", ["Decomposition", "Double replacement", "Combustion"]),
                ("Which type of reaction always produces CO₂ and H₂O when hydrocarbons react?", "Combustion", ["Synthesis", "Decomposition", "Single replacement"]),
            ]
        },
        "6.2": {
            "topic": "Combustion Reactions",
            "questions": [
                ("A combustion reaction always requires:", "Oxygen", ["Nitrogen", "Helium", "Carbon dioxide"]),
                ("Complete combustion of a hydrocarbon produces:", "CO₂ and H₂O", ["CO and H₂O", "C and H₂", "CO₂ and H₂"]),
                ("Incomplete combustion occurs when:", "There is insufficient oxygen", ["There is too much oxygen", "No fuel is present", "Temperature is too high"]),
                ("Incomplete combustion produces:", "Carbon monoxide (CO) or soot (C)", ["Only CO₂ and H₂O", "Pure oxygen", "Noble gases"]),
                ("Combustion reactions are:", "Exothermic (release energy)", ["Endothermic (absorb energy)", "Neither exo- nor endothermic", "Always slow"]),
                ("Which of these is a combustion reaction?", "CH₄ + 2O₂ → CO₂ + 2H₂O", ["NaCl → Na + Cl₂", "2H₂ + O₂ → 2H₂O", "AgNO₃ + NaCl → AgCl + NaNO₃"]),
                ("The fuel in a combustion reaction is typically:", "A hydrocarbon or organic compound", ["A noble gas", "A metal oxide", "Pure oxygen"]),
            ]
        },
        "6.3": {
            "topic": "Redox Reactions",
            "questions": [
                ("In a redox reaction, oxidation is:", "The loss of electrons", ["The gain of electrons", "The gain of protons", "The loss of neutrons"]),
                ("Reduction is:", "The gain of electrons", ["The loss of electrons", "The gain of protons", "The loss of protons"]),
                ("The substance that is oxidized:", "Loses electrons and is the reducing agent", ["Gains electrons", "Is unchanged", "Gains protons"]),
                ("The mnemonic OIL RIG stands for:", "Oxidation Is Loss, Reduction Is Gain", ["Only Ions Lose, Reactants In Gain", "Oxygen Is Left, Reduction Is Gone", "Oxidation Is Last, Reduction Is Great"]),
                ("In the reaction Zn + Cu²⁺ → Zn²⁺ + Cu, zinc is:", "Oxidized (loses electrons)", ["Reduced (gains electrons)", "Unchanged", "A catalyst"]),
                ("Oxidation numbers help track:", "Electron transfer in redox reactions", ["Mass changes", "Temperature changes", "Pressure changes"]),
                ("A substance that causes another substance to be oxidized is:", "An oxidizing agent", ["A reducing agent", "A catalyst", "An inhibitor"]),
            ]
        },
        "6.4": {
            "topic": "Activation Energy",
            "questions": [
                ("Activation energy is the minimum energy needed to:", "Start a chemical reaction", ["End a chemical reaction", "Cool a reaction", "Create an element"]),
                ("On an energy diagram, activation energy is the height of the:", "Energy barrier (hill) between reactants and products", ["Bottom of the curve", "Product energy level", "Reactant energy level"]),
                ("A catalyst lowers the:", "Activation energy", ["Total energy released", "Number of reactants", "Temperature of the reaction"]),
                ("An exothermic reaction has products that are:", "Lower in energy than reactants", ["Higher in energy than reactants", "Equal in energy to reactants", "Always gases"]),
                ("An endothermic reaction has products that are:", "Higher in energy than reactants", ["Lower in energy than reactants", "Equal in energy to reactants", "Always solids"]),
                ("Without sufficient activation energy, a reaction:", "Will not occur", ["Will proceed faster", "Will release more energy", "Will become endothermic"]),
                ("The activated complex (transition state) is:", "The highest energy point during the reaction", ["The final product", "The initial reactant", "A catalyst"]),
            ]
        },
        "6.5": {
            "topic": "Balancing Equations",
            "questions": [
                ("A balanced equation has equal numbers of each type of:", "Atom on both sides", ["Molecule on both sides", "Compound on both sides", "Bond on both sides"]),
                ("Coefficients in a balanced equation represent:", "The number of molecules or moles", ["Subscripts of atoms", "Atomic numbers", "Charges"]),
                ("The law of conservation of mass requires that:", "Matter cannot be created or destroyed", ["Energy is always conserved", "Equations have same coefficients", "All reactions produce water"]),
                ("To balance H₂ + O₂ → H₂O, the balanced equation is:", "2H₂ + O₂ → 2H₂O", ["H₂ + O₂ → H₂O₂", "H₂ + O₂ → H₂O", "H₂ + 2O₂ → 2H₂O"]),
                ("When balancing equations, you should never change the:", "Subscripts", ["Coefficients", "Arrow direction", "State symbols"]),
                ("The balanced equation for Fe + O₂ → Fe₂O₃ is:", "4Fe + 3O₂ → 2Fe₂O₃", ["2Fe + O₂ → Fe₂O₃", "Fe + O₂ → FeO₂", "2Fe + 3O₂ → Fe₂O₃"]),
                ("What does the arrow (→) in a chemical equation mean?", "Yields / produces", ["Equals", "Is greater than", "Reacts backwards"]),
            ]
        },
        "6.6": {
            "topic": "Reaction Rates & Catalysts",
            "questions": [
                ("Increasing temperature generally:", "Speeds up a reaction", ["Slows down a reaction", "Has no effect", "Stops the reaction"]),
                ("A catalyst speeds up a reaction by:", "Providing an alternative pathway with lower activation energy", ["Increasing temperature", "Adding more reactant", "Changing the products"]),
                ("Increasing concentration of reactants:", "Increases the reaction rate", ["Decreases the reaction rate", "Has no effect", "Stops the reaction"]),
                ("Increasing surface area of a solid reactant:", "Increases the rate of reaction", ["Decreases the rate", "Has no effect", "Changes the products"]),
                ("An enzyme is a type of:", "Biological catalyst", ["Inhibitor", "Reactant", "Product"]),
                ("A catalyst is NOT consumed in the reaction, meaning it:", "Can be recovered unchanged after the reaction", ["Is always destroyed", "Changes into a new element", "Becomes a product"]),
                ("Collision theory states that reactions occur when particles:", "Collide with enough energy and correct orientation", ["Simply touch", "Are heated to extreme temperatures", "Are stationary"]),
            ]
        },
        "6.7": {
            "topic": "Chemical Equilibrium & Le Chatelier's Principle",
            "questions": [
                ("Chemical equilibrium is reached when:", "The rates of forward and reverse reactions are equal", ["All reactants are used up", "All products are formed", "The reaction stops completely"]),
                ("At equilibrium, the concentrations of reactants and products:", "Remain constant (but are not necessarily equal)", ["Are always equal", "Both equal zero", "Continue to change"]),
                ("Le Chatelier's principle states that a system at equilibrium:", "Shifts to counteract a stress applied to it", ["Remains unchanged regardless of stress", "Always shifts right", "Always shifts left"]),
                ("Adding more reactant to a system at equilibrium causes the equilibrium to shift:", "Toward the products (right)", ["Toward the reactants (left)", "Not at all", "In both directions"]),
                ("Increasing temperature in an exothermic reaction shifts equilibrium:", "Toward the reactants (left)", ["Toward the products (right)", "Not at all", "Causes explosion"]),
                ("Removing a product from a system at equilibrium shifts the equilibrium:", "Toward the products (right)", ["Toward the reactants (left)", "Not at all", "Causes the reaction to stop"]),
                ("The equilibrium constant (K) expresses the ratio of:", "Products to reactants at equilibrium", ["Reactants to products", "Energy to mass", "Temperature to pressure"]),
            ]
        },
    },
    # ===== UNIT 7: Stoichiometry =====
    "Unit7": {
        "7.1": {
            "topic": "Writing Correct Formulas",
            "questions": [
                ("A chemical formula shows:", "The types and numbers of atoms in a compound", ["Only the mass", "Only the charge", "The color of the compound"]),
                ("In H₂O, the subscript 2 means:", "There are 2 hydrogen atoms", ["There are 2 oxygen atoms", "There are 2 water molecules", "Hydrogen has charge 2"]),
                ("The formula for calcium chloride is:", "CaCl₂", ["Ca₂Cl", "CaCl", "Ca₃Cl₂"]),
                ("When writing formulas for ionic compounds:", "The charges must balance to zero", ["Subscripts are arbitrary", "The metal comes last", "Prefixes are required"]),
                ("The formula for aluminum sulfate is:", "Al₂(SO₄)₃", ["AlSO₄", "Al₃(SO₄)₂", "Al(SO₄)₃"]),
                ("Parentheses in a formula mean:", "The subscript outside applies to the entire polyatomic ion", ["The compound is organic", "The element is rare", "The charge is negative"]),
                ("The correct formula for iron(III) oxide is:", "Fe₂O₃", ["FeO", "Fe₃O₂", "FeO₃"]),
            ]
        },
        "7.2": {
            "topic": "Molar Mass & Molecular Mass",
            "questions": [
                ("Molar mass is measured in:", "Grams per mole (g/mol)", ["Moles per gram", "Kilograms", "Liters per mole"]),
                ("The molar mass of water (H₂O) is approximately:", "18 g/mol", ["16 g/mol", "20 g/mol", "2 g/mol"]),
                ("To find the molar mass of a compound, you:", "Add up the atomic masses of all atoms in the formula", ["Multiply atomic numbers", "Count only the heaviest atom", "Divide by Avogadro's number"]),
                ("The molar mass of NaCl is approximately:", "58.44 g/mol", ["35.45 g/mol", "22.99 g/mol", "23 g/mol"]),
                ("Molecular mass refers specifically to:", "Covalent (molecular) compounds", ["Ionic compounds only", "Elements only", "Noble gases only"]),
                ("Formula mass is typically used for:", "Ionic compounds", ["Molecular compounds only", "Elements only", "Gases only"]),
                ("The molar mass of CO₂ is approximately:", "44 g/mol", ["28 g/mol", "32 g/mol", "16 g/mol"]),
            ]
        },
        "7.3": {
            "topic": "Avogadro's Number",
            "questions": [
                ("Avogadro's number is approximately:", "6.02 × 10²³", ["6.02 × 10²²", "3.01 × 10²³", "6.02 × 10²⁴"]),
                ("One mole of any substance contains:", "6.02 × 10²³ particles", ["1 gram of particles", "100 atoms", "1 million molecules"]),
                ("Avogadro's number represents the number of particles in:", "One mole of a substance", ["One gram of a substance", "One liter of a gas", "One kilogram of a substance"]),
                ("How many molecules are in 2 moles of H₂O?", "1.204 × 10²⁴", ["6.02 × 10²³", "3.01 × 10²³", "1.806 × 10²⁴"]),
                ("The mole is used because atoms are:", "Too small to count individually", ["Too large to measure", "All identical", "Always in groups of 100"]),
                ("One mole of carbon-12 has a mass of:", "12 grams", ["6 grams", "1 gram", "24 grams"]),
                ("To convert from particles to moles, you:", "Divide by Avogadro's number", ["Multiply by Avogadro's number", "Add Avogadro's number", "Subtract Avogadro's number"]),
            ]
        },
        "7.4": {
            "topic": "Molar Conversions",
            "questions": [
                ("To convert grams to moles:", "Divide grams by molar mass", ["Multiply grams by molar mass", "Add molar mass to grams", "Divide molar mass by grams"]),
                ("To convert moles to grams:", "Multiply moles by molar mass", ["Divide moles by molar mass", "Add to Avogadro's number", "Subtract molar mass"]),
                ("How many moles are in 36 g of water (molar mass = 18 g/mol)?", "2 moles", ["0.5 moles", "18 moles", "36 moles"]),
                ("How many grams are in 0.5 moles of NaCl (molar mass = 58.44)?", "29.22 g", ["58.44 g", "116.88 g", ["14.61 g"]]),
                ("At STP, one mole of any gas occupies:", "22.4 liters", ["11.2 liters", "44.8 liters", "1 liter"]),
                ("The mole road map connects:", "Grams, moles, particles, and liters (for gases)", ["Only grams and moles", "Only particles and liters", "Only mass and volume"]),
                ("To convert moles to particles:", "Multiply by Avogadro's number", ["Divide by Avogadro's number", "Multiply by molar mass", "Divide by molar mass"]),
            ]
        },
        "7.5": {
            "topic": "Empirical vs. Molecular Formulas",
            "questions": [
                ("An empirical formula shows:", "The simplest whole-number ratio of atoms", ["The actual number of atoms", "Only the first element", "The molar mass"]),
                ("A molecular formula shows:", "The actual number of atoms in a molecule", ["The simplest ratio", "Only metals", "The volume"]),
                ("The empirical formula of C₆H₁₂O₆ is:", "CH₂O", ["C₆H₁₂O₆", "CHO", "C₃H₆O₃"]),
                ("To find an empirical formula from percent composition:", "Convert to moles, then find the simplest ratio", ["Just use the percentages as subscripts", "Divide all by the largest", "Multiply all by 100"]),
                ("If the empirical formula is CH₂O and molar mass is 180 g/mol:", "The molecular formula is C₆H₁₂O₆", ["The molecular formula is CH₂O", "The molecular formula is C₃H₆O₃", "It cannot be determined"]),
                ("The empirical formula of H₂O₂ is:", "HO", ["H₂O₂", "H₂O", "OH₂"]),
                ("An empirical formula mass of 30 with a molar mass of 60 gives a multiplier of:", "2", ["3", "1", "0.5"]),
            ]
        },
        "7.6": {
            "topic": "Limiting Reagents",
            "questions": [
                ("The limiting reagent is the reactant that:", "Is completely consumed first", ["Is left over", "Is added in excess", "Is the catalyst"]),
                ("The excess reagent is the reactant that:", "Remains after the reaction is complete", ["Runs out first", "Is the most expensive", "Is a catalyst"]),
                ("The limiting reagent determines:", "The maximum amount of product formed", ["The speed of the reaction", "The color of the product", "The temperature"]),
                ("To identify the limiting reagent, you must:", "Compare the mole ratio of reactants used vs. available", ["Just look at which has less mass", "Choose the smaller molecule", "Pick the first reactant listed"]),
                ("If you have 2 mol of H₂ and 2 mol of O₂ for 2H₂+O₂→2H₂O:", "H₂ is the limiting reagent", ["O₂ is the limiting reagent", "Both are limiting", "Neither is limiting"]),
                ("The amount of product calculated from the limiting reagent is:", "The theoretical yield", ["The actual yield", "The percent yield", "The excess"]),
                ("Excess reagent is important to know because:", "Some of it remains unreacted", ["It determines the product", "It is always the catalyst", "It evaporates"]),
            ]
        },
        "7.7": {
            "topic": "Stoichiometric Calculations",
            "questions": [
                ("Stoichiometry uses balanced equations to calculate:", "Amounts of reactants and products", ["Electron configurations", "Atomic numbers", "Bond angles"]),
                ("The coefficients in a balanced equation represent:", "Mole ratios", ["Mass ratios", "Volume ratios only", "Charge ratios"]),
                ("In the reaction 2H₂ + O₂ → 2H₂O, the mole ratio of H₂ to H₂O is:", "1:1", ["2:1", "1:2", "2:2"]),
                ("To solve a stoichiometry problem, the first step is:", "Write and balance the chemical equation", ["Convert to liters", "Find the atomic number", "Measure the temperature"]),
                ("If 4 moles of Al react in 4Al + 3O₂ → 2Al₂O₃, how many moles of Al₂O₃ form?", "2 mol", ["4 mol", "3 mol", "1 mol"]),
                ("Mole-to-mole conversions use:", "Coefficients from the balanced equation", ["Molar masses", "Avogadro's number", "Atomic numbers"]),
                ("Gram-to-gram conversions require:", "Converting to moles first, then using mole ratio", ["Direct division of masses", "Adding masses together", "No conversion"]),
            ]
        },
        "7.8": {
            "topic": "Percent Yield",
            "questions": [
                ("Percent yield is calculated as:", "(Actual yield / Theoretical yield) × 100", ["(Theoretical yield / Actual yield) × 100", "Actual − Theoretical × 100", "Theoretical + Actual × 100"]),
                ("Theoretical yield is:", "The maximum amount of product calculated from stoichiometry", ["The amount actually produced", "Always 100%", "The mass of reactants"]),
                ("Actual yield is:", "The amount of product actually obtained from an experiment", ["The calculated maximum", "Always greater than theoretical", "The mass of excess reagent"]),
                ("A percent yield greater than 100% usually indicates:", "Experimental error (impurities, measurement mistakes)", ["A perfect reaction", "Extra product was created from nothing", "The equation was unbalanced"]),
                ("Why is actual yield often less than theoretical yield?", "Side reactions, incomplete reactions, or loss during transfer", ["Atoms are destroyed", "Mass is not conserved", "The equation is wrong"]),
                ("If theoretical yield is 50 g and actual yield is 40 g, percent yield is:", "80%", ["125%", "90%", ["10%"]]),
                ("A high percent yield indicates:", "The reaction was efficient", ["The reaction failed", "Too much excess reagent", "The wrong product formed"]),
            ]
        },
    },
    # ===== UNIT 8: Gas Laws =====
    "Unit8": {
        "8.1": {
            "topic": "Monatomic & Diatomic Gases",
            "questions": [
                ("A monatomic gas consists of:", "Single atoms", ["Pairs of atoms", "Molecules of three atoms", "Ionic compounds"]),
                ("Noble gases are examples of:", "Monatomic gases", ["Diatomic gases", "Triatomic gases", "Ionic gases"]),
                ("The diatomic elements can be remembered by:", "HOFBrINCl (H₂, O₂, F₂, Br₂, I₂, N₂, Cl₂)", ["All metals", "All noble gases", "All halogens and metals"]),
                ("Oxygen gas exists naturally as:", "O₂ (diatomic)", ["O (monatomic)", "O₃ (triatomic) only", "O₄"]),
                ("Hydrogen gas in nature is:", "H₂ (diatomic)", ["H (monatomic)", "H₃ (triatomic)", "H₄"]),
                ("Which of these is NOT a diatomic element?", "Argon (Ar)", ["Nitrogen (N₂)", "Oxygen (O₂)", "Chlorine (Cl₂)"]),
                ("Diatomic molecules are held together by:", "Covalent bonds", ["Ionic bonds", "Metallic bonds", "Van der Waals forces only"]),
            ]
        },
        "8.2": {
            "topic": "Pressure & Standard Atmosphere",
            "questions": [
                ("Standard atmospheric pressure at sea level is:", "1 atm (101.325 kPa)", ["2 atm", "0.5 atm", "10 atm"]),
                ("1 atm is equal to:", "760 mmHg", ["100 mmHg", "500 mmHg", "1000 mmHg"]),
                ("Pressure is defined as:", "Force per unit area", ["Mass per unit volume", "Energy per unit time", "Volume per unit mass"]),
                ("A barometer measures:", "Atmospheric pressure", ["Temperature", "Volume", "Moles of gas"]),
                ("The SI unit of pressure is:", "Pascal (Pa)", ["Atmosphere (atm)", "Torr", "mmHg"]),
                ("As altitude increases, atmospheric pressure:", "Decreases", ["Increases", "Stays the same", "Doubles"]),
                ("1 atm equals how many torr?", "760 torr", ["100 torr", "1000 torr", "273 torr"]),
            ]
        },
        "8.3": {
            "topic": "Kinetic Molecular Theory",
            "questions": [
                ("According to kinetic molecular theory, gas particles are:", "In constant random motion", ["Stationary", "Moving in straight lines only", "Vibrating in place"]),
                ("Gas particles are assumed to have:", "No significant volume compared to the container", ["Large volumes", "Fixed positions", "Strong attractions"]),
                ("Collisions between gas particles are:", "Perfectly elastic (no energy lost)", ["Always inelastic", "Rare events", "Only at high temperatures"]),
                ("Temperature is a measure of the:", "Average kinetic energy of particles", ["Total potential energy", "Total number of particles", "Volume of the container"]),
                ("Gas pressure results from:", "Particles colliding with container walls", ["Gravity pulling on gas", "Magnetic forces", "Chemical reactions"]),
                ("At higher temperatures, gas particles move:", "Faster on average", ["Slower", "At the same speed", "Not at all"]),
                ("Kinetic molecular theory assumes intermolecular forces between gas particles are:", "Negligible", ["Very strong", "Equal to gravity", "Always attractive"]),
            ]
        },
        "8.4": {
            "topic": "Boyle's Law",
            "questions": [
                ("Boyle's Law states that pressure and volume are:", "Inversely proportional (at constant temperature)", ["Directly proportional", "Unrelated", "Always equal"]),
                ("The mathematical expression for Boyle's Law is:", "P₁V₁ = P₂V₂", ["P₁/V₁ = P₂/V₂", "P₁T₁ = P₂T₂", "V₁/T₁ = V₂/T₂"]),
                ("If pressure on a gas doubles (at constant T), the volume:", "Halves", ["Doubles", "Stays the same", "Triples"]),
                ("Boyle's Law applies at constant:", "Temperature", ["Pressure", "Volume", "Amount of gas and temperature changes"]),
                ("A gas has a volume of 4 L at 2 atm. At 1 atm, its volume is:", "8 L", ["2 L", "4 L", "16 L"]),
                ("The graph of P vs V for an ideal gas is:", "A hyperbola (inverse curve)", ["A straight line", "A parabola", "A circle"]),
                ("Boyle's Law explains why a balloon expands when:", "External pressure decreases (like going up in altitude)", ["Temperature increases", "More gas is added", "It gets wet"]),
            ]
        },
        "8.5": {
            "topic": "Charles' Law",
            "questions": [
                ("Charles' Law states that volume and temperature are:", "Directly proportional (at constant pressure)", ["Inversely proportional", "Unrelated", "Equal"]),
                ("The mathematical expression for Charles' Law is:", "V₁/T₁ = V₂/T₂", ["P₁V₁ = P₂V₂", "P₁/T₁ = P₂/T₂", "V₁T₁ = V₂T₂"]),
                ("Temperature in gas law calculations must be in:", "Kelvin", ["Celsius", "Fahrenheit", "Any unit"]),
                ("If temperature doubles (in Kelvin), volume:", "Doubles", ["Halves", "Stays the same", "Quadruples"]),
                ("To convert Celsius to Kelvin:", "Add 273", ["Subtract 273", "Multiply by 1.8", "Divide by 273"]),
                ("At absolute zero (0 K), the theoretical volume of a gas is:", "Zero", ["Maximum", "Infinite", "Unchanged"]),
                ("A gas at 300 K has a volume of 6 L. At 600 K (constant P), its volume is:", "12 L", ["3 L", "6 L", "24 L"]),
            ]
        },
        "8.6": {
            "topic": "Gay-Lussac's Law",
            "questions": [
                ("Gay-Lussac's Law relates:", "Pressure and temperature (at constant volume)", ["Pressure and volume", "Volume and temperature", "Moles and pressure"]),
                ("The formula for Gay-Lussac's Law is:", "P₁/T₁ = P₂/T₂", ["P₁V₁ = P₂V₂", "V₁/T₁ = V₂/T₂", "PV = nRT"]),
                ("As temperature increases at constant volume, pressure:", "Increases", ["Decreases", "Stays the same", "Becomes zero"]),
                ("A rigid container of gas at 300 K and 2 atm is heated to 600 K. The new pressure is:", "4 atm", ["1 atm", "2 atm", "8 atm"]),
                ("Gay-Lussac's Law requires constant:", "Volume and amount of gas", ["Pressure", "Temperature", "Number of moles only"]),
                ("An aerosol can may explode if heated because:", "Pressure increases with temperature in a fixed volume", ["Volume increases", "The gas escapes", "The metal expands"]),
                ("Pressure and temperature are:", "Directly proportional (at constant V)", ["Inversely proportional", "Unrelated", "Always equal"]),
            ]
        },
        "8.7": {
            "topic": "Combined Gas Law",
            "questions": [
                ("The combined gas law combines:", "Boyle's, Charles', and Gay-Lussac's laws", ["Only Boyle's and Charles'", "Ideal gas law and Dalton's", "Avogadro's and Boyle's"]),
                ("The combined gas law formula is:", "P₁V₁/T₁ = P₂V₂/T₂", ["PV = nRT", "P₁V₁ = P₂V₂", "V₁/T₁ = V₂/T₂"]),
                ("The combined gas law assumes the amount of gas:", "Remains constant", ["Changes", "Is always 1 mole", "Doubles"]),
                ("If Boyle's Law is a special case of the combined gas law, which variable is constant?", "Temperature", ["Pressure", "Volume", "Moles"]),
                ("If Charles' Law is a special case, which variable is constant?", "Pressure", ["Volume", "Temperature", "Mass"]),
                ("A gas at 2 atm, 4 L, and 300 K changes to 1 atm and 600 K. The new volume is:", "16 L", ["8 L", "4 L", "32 L"]),
                ("Temperature must be measured in which unit for the combined gas law?", "Kelvin", ["Celsius", "Fahrenheit", "Rankine"]),
            ]
        },
        "8.8": {
            "topic": "Ideal Gas Law",
            "questions": [
                ("The ideal gas law is expressed as:", "PV = nRT", ["P₁V₁ = P₂V₂", ["P/T = V/n"], "PV = mRT"]),
                ("In PV = nRT, R is the:", "Universal gas constant", ["Reaction rate", "Radius of atom", "Resistance"]),
                ("The value of R is 0.0821 when pressure is in:", "Atmospheres", ["Pascals", "Torr", "mmHg"]),
                ("The ideal gas law can be used to find:", "Any one variable if the other three are known", ["Only pressure", "Only volume", "Only temperature"]),
                ("How many moles of gas occupy 44.8 L at STP?", "2 mol", ["1 mol", "0.5 mol", "4 mol"]),
                ("STP stands for:", "Standard Temperature and Pressure (0°C, 1 atm)", ["Standard Total Pressure", "Simplified Temperature Protocol", "Super Thermal Pressure"]),
                ("At STP, one mole of any ideal gas occupies:", "22.4 L", ["11.2 L", "44.8 L", "1 L"]),
            ]
        },
        "8.9": {
            "topic": "Real Gases & Deviations",
            "questions": [
                ("Real gases deviate from ideal behavior at:", "High pressure and low temperature", ["Low pressure and high temperature", "All conditions equally", "Only at STP"]),
                ("At high pressure, gas particles are:", "Closer together, so intermolecular forces matter", ["Farther apart", "Moving faster", "Not affected"]),
                ("At low temperature, gas particles:", "Move slowly enough for attractions to matter", ["Move faster", "Have no volume", "Become ideal"]),
                ("The van der Waals equation corrects for:", "Molecular volume and intermolecular forces", ["Only temperature", "Only pressure", "Only mass"]),
                ("Which gas behaves most ideally?", "Helium (small, nonpolar)", ["Water vapor", "Ammonia", "Carbon dioxide"]),
                ("Ideal gas behavior assumes:", "No intermolecular forces and no particle volume", ["Strong forces between molecules", "Particles have significant volume", "Only elastic collisions at high pressure"]),
                ("Real gases are most ideal when:", "Temperature is high and pressure is low", ["Temperature is low and pressure is high", "At absolute zero", "In a closed container"]),
            ]
        },
    },
}


def generate_question_html(q_num, question, correct, wrongs):
    """Generate HTML for one quiz question with randomized answer order."""
    options = [(correct, "correct")] + [(w, "wrong") for w in wrongs]
    random.shuffle(options)
    
    labels = ""
    for text, value in options:
        labels += f"""
                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q{q_num}" value="{value}"> {text}
                </label>"""
    
    return f"""
            <div class="quiz-question" style="margin-bottom: 2rem;" data-attempts="2">
                <p style="font-weight: 700; font-size: 1.45rem; margin-bottom: 1rem;">{q_num}. {question}</p>{labels}
                <div class="attempts-indicator"></div>
                <div style="margin-top:1.5rem;">
                    <button type="button" class="action-button" onclick="window.checkQuizAnswer('q{q_num}', 'correct', this)">Submit Answer</button>
                    <button type="button" class="nav-button" onclick="window.resetQuizQuestion(this)" style="margin-left:0.5rem;">Try Again</button>
                </div>
            </div>"""


def process_quiz_file(filepath, questions):
    """Replace quiz questions in a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    form_start = content.find('<form id="quiz-form">')
    if form_start == -1:
        print(f"  WARNING: No quiz form found in {filepath}")
        return False
    
    form_end = content.find('</form>', form_start)
    if form_end == -1:
        print(f"  WARNING: No </form> found in {filepath}")
        return False
    
    questions_html = ""
    for i, (q, correct, wrongs) in enumerate(questions, 1):
        questions_html += generate_question_html(i, q, correct, wrongs)
    
    new_form_content = f'<form id="quiz-form">{questions_html}\n'
    
    new_content = content[:form_start] + new_form_content + content[form_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


def main():
    updated = 0
    errors = 0
    
    for unit_dir, lessons in LESSONS.items():
        for lesson_id, data in lessons.items():
            filename = f"Lesson {lesson_id}_Quiz.html"
            filepath = os.path.join(BASE, unit_dir, filename)
            
            if not os.path.exists(filepath):
                print(f"  ERROR: File not found: {filepath}")
                errors += 1
                continue
            
            if process_quiz_file(filepath, data["questions"]):
                print(f"  Updated: {unit_dir}/{filename} ({len(data['questions'])} questions)")
                updated += 1
            else:
                errors += 1
    
    print(f"\nDone! {updated} files updated, {errors} errors.")


if __name__ == "__main__":
    main()
