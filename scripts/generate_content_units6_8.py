#!/usr/bin/env python3
"""Generate topic-specific content for Chemistry Units 6-8.
Replaces placeholder States-of-Matter content with real chemistry content.
"""
import os, re, glob, random

BASE = os.path.join(os.path.dirname(__file__), '..', 'ArisEdu Project Folder', 'ChemistryLessons')

CONTENT = {
    # ══════════════════ UNIT 6 ══════════════════
    "6.1": {
        "topic": "Types of Reactions",
        "summary_title": "Types of Reactions",
        "summary_bullets": [
            ("<b>Synthesis (Combination)</b>", "Two or more reactants combine to form one product: A + B → AB."),
            ("<b>Decomposition</b>", "One compound breaks down into two or more simpler substances: AB → A + B."),
            ("<b>Single Replacement</b>", "One element replaces another in a compound: A + BC → AC + B."),
            ("<b>Double Replacement</b>", "Ions in two compounds exchange partners: AB + CD → AD + CB."),
            ("<b>Combustion</b>", "A substance reacts with oxygen, releasing energy as heat and light."),
            ("<b>Precipitate</b>", "An insoluble solid formed in a double replacement reaction."),
        ],
        "quiz": [
            {
                "question": "A + B → AB is an example of what reaction type?",
                "correct": "Synthesis",
                "wrong": ["Decomposition", "Single replacement", "Combustion"]
            },
            {
                "question": "In a single replacement reaction, what happens?",
                "correct": "One element replaces another in a compound",
                "wrong": ["A compound breaks down", "Two compounds swap ions", "A substance burns in oxygen"]
            }
        ],
        "flashcards": [
            ("What is a synthesis reaction?", "Two or more reactants combine to form one product (A + B → AB)"),
            ("What is a decomposition reaction?", "One compound breaks into simpler substances (AB → A + B)"),
            ("What is a single replacement reaction?", "One element replaces another in a compound (A + BC → AC + B)"),
            ("What is a double replacement reaction?", "Two compounds swap ions (AB + CD → AD + CB)"),
            ("What is a combustion reaction?", "A substance reacts with oxygen, releasing heat and light"),
            ("What is a precipitate?", "An insoluble solid formed during a reaction"),
            ("What type of reaction is 2H₂ + O₂ → 2H₂O?", "Synthesis (combination)"),
            ("What type of reaction is 2H₂O → 2H₂ + O₂?", "Decomposition"),
            ("What type of reaction is Zn + CuSO₄ → ZnSO₄ + Cu?", "Single replacement"),
            ("What type of reaction is NaCl + AgNO₃ → AgCl + NaNO₃?", "Double replacement")
        ]
    },
    "6.2": {
        "topic": "Combustion Reactions",
        "summary_title": "Combustion Reactions",
        "summary_bullets": [
            ("<b>Combustion</b>", "A rapid reaction of a substance with oxygen that produces heat and light (fire)."),
            ("<b>Complete Combustion</b>", "Hydrocarbon + O₂ → CO₂ + H₂O; occurs with plenty of oxygen."),
            ("<b>Incomplete Combustion</b>", "Produces CO (carbon monoxide) or C (soot) instead of CO₂ due to limited oxygen."),
            ("<b>Hydrocarbon</b>", "A compound containing only carbon and hydrogen (e.g., CH₄, C₃H₈)."),
            ("<b>Fuel</b>", "A substance that undergoes combustion to release usable energy."),
            ("<b>Products of Complete Combustion</b>", "Always carbon dioxide (CO₂) and water (H₂O)."),
        ],
        "quiz": [
            {
                "question": "What are the products of complete combustion of a hydrocarbon?",
                "correct": "CO₂ and H₂O",
                "wrong": ["CO and H₂O", "C and H₂", "CO₂ and H₂"]
            },
            {
                "question": "What causes incomplete combustion?",
                "correct": "Limited oxygen supply",
                "wrong": ["Too much oxygen", "High temperature", "No fuel present"]
            }
        ],
        "flashcards": [
            ("What is combustion?", "A rapid reaction with oxygen producing heat and light"),
            ("What is complete combustion?", "Burning with plenty of O₂, producing CO₂ and H₂O"),
            ("What is incomplete combustion?", "Burning with limited O₂, producing CO or soot"),
            ("What is a hydrocarbon?", "A compound containing only carbon and hydrogen"),
            ("What are the products of complete combustion?", "Carbon dioxide and water"),
            ("What dangerous gas forms in incomplete combustion?", "Carbon monoxide (CO)"),
            ("Write the word equation for combustion of methane.", "Methane + Oxygen → Carbon Dioxide + Water"),
            ("Why is incomplete combustion dangerous?", "It produces toxic carbon monoxide gas"),
            ("What is needed for combustion to occur?", "Fuel, oxygen, and an ignition source (fire triangle)"),
            ("Is combustion exothermic or endothermic?", "Exothermic (releases energy)")
        ]
    },
    "6.3": {
        "topic": "Redox Reactions",
        "summary_title": "Redox Reactions",
        "summary_bullets": [
            ("<b>Oxidation</b>", "Loss of electrons (or gain of oxygen); oxidation number increases."),
            ("<b>Reduction</b>", "Gain of electrons (or loss of oxygen); oxidation number decreases."),
            ("<b>Redox Reaction</b>", "A reaction where oxidation and reduction occur simultaneously."),
            ("<b>Oxidizing Agent</b>", "The substance that is reduced (gains electrons); causes oxidation in another substance."),
            ("<b>Reducing Agent</b>", "The substance that is oxidized (loses electrons); causes reduction in another substance."),
            ("<b>OIL RIG</b>", "Memory aid: Oxidation Is Loss, Reduction Is Gain (of electrons)."),
        ],
        "quiz": [
            {
                "question": "What does OIL RIG stand for?",
                "correct": "Oxidation Is Loss, Reduction Is Gain",
                "wrong": ["Oxygen Is Light, Reduction Is Gas", "Oxidation Increases, Reduction Goes down", "Only In Labs, Reactions In Gas"]
            },
            {
                "question": "What happens to a substance that is oxidized?",
                "correct": "It loses electrons",
                "wrong": ["It gains electrons", "It gains protons", "It loses protons"]
            }
        ],
        "flashcards": [
            ("What is oxidation?", "Loss of electrons"),
            ("What is reduction?", "Gain of electrons"),
            ("What is a redox reaction?", "A reaction where oxidation and reduction occur simultaneously"),
            ("What mnemonic helps remember redox?", "OIL RIG — Oxidation Is Loss, Reduction Is Gain"),
            ("What is an oxidizing agent?", "The substance that gets reduced (gains electrons)"),
            ("What is a reducing agent?", "The substance that gets oxidized (loses electrons)"),
            ("In rusting, is iron oxidized or reduced?", "Oxidized (iron loses electrons)"),
            ("Can oxidation occur without reduction?", "No, they always occur together"),
            ("What happens to oxidation number during oxidation?", "It increases"),
            ("What happens to oxidation number during reduction?", "It decreases")
        ]
    },
    "6.4": {
        "topic": "Activation Energy",
        "summary_title": "Activation Energy",
        "summary_bullets": [
            ("<b>Activation Energy (Ea)</b>", "The minimum energy required for a chemical reaction to begin."),
            ("<b>Energy Diagram</b>", "A graph showing energy changes during a reaction; Ea is the 'hill' reactants must overcome."),
            ("<b>Exothermic Reaction</b>", "Products have less energy than reactants; energy is released."),
            ("<b>Endothermic Reaction</b>", "Products have more energy than reactants; energy is absorbed."),
            ("<b>Activated Complex</b>", "The unstable, high-energy transition state at the top of the energy barrier."),
            ("<b>Catalyst</b>", "A substance that lowers activation energy without being consumed in the reaction."),
        ],
        "quiz": [
            {
                "question": "What is activation energy?",
                "correct": "The minimum energy needed to start a reaction",
                "wrong": ["Energy released by a reaction", "Energy stored in products", "Total energy in reactants"]
            },
            {
                "question": "What does a catalyst do to activation energy?",
                "correct": "Lowers it",
                "wrong": ["Raises it", "Eliminates it", "Doubles it"]
            }
        ],
        "flashcards": [
            ("What is activation energy?", "The minimum energy required to start a chemical reaction"),
            ("What is an energy diagram?", "A graph showing energy changes during a reaction"),
            ("What is the activated complex?", "The unstable transition state at the peak of the energy barrier"),
            ("What does a catalyst do?", "Lowers activation energy without being consumed"),
            ("In an exothermic reaction, do products have more or less energy than reactants?", "Less energy"),
            ("In an endothermic reaction, do products have more or less energy than reactants?", "More energy"),
            ("Do all reactions need activation energy?", "Yes, even exothermic reactions need a small push"),
            ("What is the difference in energy between reactants and products called?", "Enthalpy change (ΔH)"),
            ("Does a catalyst change the overall energy released?", "No, it only changes the path (lower Ea)"),
            ("What provides activation energy for a match striking?", "Friction (heat)")
        ]
    },
    "6.5": {
        "topic": "Balancing Equations",
        "summary_title": "Balancing Equations",
        "summary_bullets": [
            ("<b>Law of Conservation of Mass</b>", "Matter cannot be created or destroyed; atoms must balance on both sides."),
            ("<b>Coefficient</b>", "A number placed in front of a formula to balance atoms (e.g., 2H₂O)."),
            ("<b>Subscript</b>", "A number within a formula showing how many atoms of an element are in a molecule; NEVER change subscripts."),
            ("<b>Balancing Steps</b>", "1) Write the unbalanced equation. 2) Count atoms on each side. 3) Add coefficients to balance. 4) Verify."),
            ("<b>Diatomic Elements</b>", "Elements that exist as pairs: H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂ (remember HONClBrIF)."),
            ("<b>Balanced Equation</b>", "An equation with equal numbers of each type of atom on both sides."),
        ],
        "quiz": [
            {
                "question": "What should you adjust to balance a chemical equation?",
                "correct": "Coefficients",
                "wrong": ["Subscripts", "Elements", "Products"]
            },
            {
                "question": "Which law requires equations to be balanced?",
                "correct": "Law of Conservation of Mass",
                "wrong": ["Law of Gravity", "Ideal Gas Law", "Hund's Rule"]
            }
        ],
        "flashcards": [
            ("Why must chemical equations be balanced?", "Law of Conservation of Mass — atoms can't be created or destroyed"),
            ("What is a coefficient?", "A number in front of a formula that balances atoms"),
            ("Can you change subscripts to balance an equation?", "No, never change subscripts"),
            ("What are the diatomic elements?", "H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂ (HONClBrIF)"),
            ("Balance: H₂ + O₂ → H₂O", "2H₂ + O₂ → 2H₂O"),
            ("What is a balanced equation?", "Equal numbers of each atom type on both sides"),
            ("What are the steps to balance an equation?", "Write equation, count atoms, add coefficients, verify"),
            ("Balance: N₂ + H₂ → NH₃", "N₂ + 3H₂ → 2NH₃"),
            ("What is a skeleton equation?", "An unbalanced equation showing reactants and products"),
            ("What does → mean in a chemical equation?", "Yields (produces)")
        ]
    },
    "6.6": {
        "topic": "Reaction Rates & Catalysts",
        "summary_title": "Reaction Rates & Catalysts",
        "summary_bullets": [
            ("<b>Reaction Rate</b>", "The speed at which reactants are converted to products."),
            ("<b>Collision Theory</b>", "Particles must collide with enough energy and proper orientation to react."),
            ("<b>Temperature Effect</b>", "Increasing temperature increases particle speed and collision frequency → faster rate."),
            ("<b>Concentration Effect</b>", "Higher concentration means more particles → more collisions → faster rate."),
            ("<b>Surface Area Effect</b>", "Smaller particles (greater surface area) react faster."),
            ("<b>Catalyst</b>", "Speeds up a reaction by lowering activation energy; is not consumed."),
        ],
        "quiz": [
            {
                "question": "According to collision theory, what must particles do to react?",
                "correct": "Collide with enough energy and proper orientation",
                "wrong": ["Touch each other gently", "Be the same size", "Be in the same state of matter"]
            },
            {
                "question": "How does increasing temperature affect reaction rate?",
                "correct": "It increases the rate",
                "wrong": ["It decreases the rate", "No effect", "It stops the reaction"]
            }
        ],
        "flashcards": [
            ("What is reaction rate?", "The speed at which reactants become products"),
            ("What is collision theory?", "Particles must collide with enough energy and proper orientation to react"),
            ("How does temperature affect reaction rate?", "Higher temperature → faster rate"),
            ("How does concentration affect reaction rate?", "Higher concentration → faster rate"),
            ("How does surface area affect reaction rate?", "Greater surface area → faster rate"),
            ("What is a catalyst?", "A substance that speeds up a reaction without being consumed"),
            ("What is an inhibitor?", "A substance that slows down a reaction"),
            ("Why does crushing a solid speed up a reaction?", "It increases surface area for more collisions"),
            ("What is activation energy?", "The minimum energy needed for a successful collision"),
            ("What is an enzyme?", "A biological catalyst")
        ]
    },
    "6.7": {
        "topic": "Chemical Equilibrium & Le Chatelier's Principle",
        "summary_title": "Chemical Equilibrium & Le Chatelier's Principle",
        "summary_bullets": [
            ("<b>Chemical Equilibrium</b>", "A state where the forward and reverse reaction rates are equal; concentrations remain constant."),
            ("<b>Reversible Reaction</b>", "A reaction that can proceed in both forward and reverse directions (⇌)."),
            ("<b>Le Chatelier's Principle</b>", "If a stress is applied to a system at equilibrium, the system shifts to relieve the stress."),
            ("<b>Adding Reactant</b>", "Shifts equilibrium toward products (forward)."),
            ("<b>Increasing Temperature</b>", "Shifts equilibrium in the endothermic direction."),
            ("<b>Changing Pressure</b>", "Increasing pressure shifts toward the side with fewer moles of gas."),
        ],
        "quiz": [
            {
                "question": "At chemical equilibrium, what is true?",
                "correct": "Forward and reverse reaction rates are equal",
                "wrong": ["All reactions have stopped", "Only products remain", "Only reactants remain"]
            },
            {
                "question": "Adding more reactant to a system at equilibrium will:",
                "correct": "Shift the equilibrium toward products",
                "wrong": ["Stop the reaction", "Shift toward more reactant", "Have no effect"]
            }
        ],
        "flashcards": [
            ("What is chemical equilibrium?", "When forward and reverse reaction rates are equal"),
            ("What is a reversible reaction?", "A reaction that can go in both directions (⇌)"),
            ("What is Le Chatelier's Principle?", "A system at equilibrium shifts to relieve applied stress"),
            ("What happens if you add more reactant?", "Equilibrium shifts toward products"),
            ("What happens if you remove product?", "Equilibrium shifts toward products (to make more)"),
            ("How does increasing temperature affect an exothermic reaction at equilibrium?", "Shifts toward reactants"),
            ("How does increasing pressure affect equilibrium?", "Shifts toward the side with fewer gas moles"),
            ("Does a catalyst affect equilibrium position?", "No, it only speeds up reaching equilibrium"),
            ("At equilibrium, do reactions stop?", "No, both forward and reverse reactions continue at equal rates"),
            ("What symbol represents a reversible reaction?", "⇌ (double arrow)")
        ]
    },
    # ══════════════════ UNIT 7 ══════════════════
    "7.1": {
        "topic": "Writing Correct Formulas",
        "summary_title": "Writing Correct Formulas",
        "summary_bullets": [
            ("<b>Chemical Formula</b>", "Uses element symbols and subscripts to show the composition of a compound (e.g., H₂O)."),
            ("<b>Cation</b>", "A positively charged ion formed when an atom loses electrons."),
            ("<b>Anion</b>", "A negatively charged ion formed when an atom gains electrons."),
            ("<b>Criss-Cross Method</b>", "Use the charge of each ion as the subscript of the other to write formulas."),
            ("<b>Polyatomic Ion</b>", "A group of atoms bonded together that carry a charge (e.g., SO₄²⁻, NH₄⁺)."),
            ("<b>Neutral Compound Rule</b>", "The total positive charge must equal the total negative charge in a formula."),
        ],
        "quiz": [
            {
                "question": "What method uses ion charges as subscripts for the other ion?",
                "correct": "Criss-cross method",
                "wrong": ["VSEPR method", "Subtraction method", "Electron method"]
            },
            {
                "question": "What must be true about the charges in a correct chemical formula?",
                "correct": "Total positive charge equals total negative charge",
                "wrong": ["Charges must be zero individually", "All atoms must be neutral", "Only positive charges are used"]
            }
        ],
        "flashcards": [
            ("What is a chemical formula?", "Symbols and subscripts showing a compound's composition"),
            ("What is a cation?", "A positively charged ion (lost electrons)"),
            ("What is an anion?", "A negatively charged ion (gained electrons)"),
            ("What is the criss-cross method?", "Using ion charges as subscripts for the other ion"),
            ("What is a polyatomic ion?", "A group of bonded atoms that carry a charge"),
            ("Write the formula for sodium chloride.", "NaCl"),
            ("Write the formula for calcium fluoride.", "CaF₂"),
            ("Write the formula for aluminum oxide.", "Al₂O₃"),
            ("What must be true about charges in a compound?", "Total positive = total negative (net charge is zero)"),
            ("What is the formula for ammonium sulfate?", "(NH₄)₂SO₄")
        ]
    },
    "7.2": {
        "topic": "Molar Mass & Molecular Mass",
        "summary_title": "Molar Mass & Molecular Mass",
        "summary_bullets": [
            ("<b>Molar Mass</b>", "The mass of one mole of a substance in grams per mole (g/mol); equals atomic mass from periodic table."),
            ("<b>Molecular Mass</b>", "The sum of the atomic masses of all atoms in a molecular formula."),
            ("<b>Formula Mass</b>", "The sum of atomic masses for ionic compounds."),
            ("<b>Calculating Molar Mass</b>", "Add up the atomic masses of each element multiplied by their subscript."),
            ("<b>Example: H₂O</b>", "2(1.01) + 16.00 = 18.02 g/mol."),
            ("<b>Units</b>", "Molar mass is expressed in g/mol; molecular mass in amu (atomic mass units)."),
        ],
        "quiz": [
            {
                "question": "What is molar mass?",
                "correct": "The mass of one mole of a substance in g/mol",
                "wrong": ["The number of atoms in a mole", "The density of a substance", "The volume of one mole"]
            },
            {
                "question": "What is the molar mass of H₂O?",
                "correct": "18.02 g/mol",
                "wrong": ["2.02 g/mol", "16.00 g/mol", "32.00 g/mol"]
            }
        ],
        "flashcards": [
            ("What is molar mass?", "The mass of one mole of a substance in g/mol"),
            ("How do you calculate molar mass?", "Add atomic masses of each element times their subscripts"),
            ("What is molecular mass?", "Sum of atomic masses of all atoms in a molecular formula"),
            ("What is formula mass?", "Sum of atomic masses for an ionic compound"),
            ("What is the molar mass of NaCl?", "58.44 g/mol (22.99 + 35.45)"),
            ("What is the molar mass of CO₂?", "44.01 g/mol (12.01 + 2×16.00)"),
            ("What unit is molar mass expressed in?", "g/mol"),
            ("What unit is molecular mass expressed in?", "amu (atomic mass units)"),
            ("What is the molar mass of O₂?", "32.00 g/mol"),
            ("Where do you find atomic masses?", "On the periodic table")
        ]
    },
    "7.3": {
        "topic": "Avogadro's Number",
        "summary_title": "Avogadro's Number",
        "summary_bullets": [
            ("<b>Avogadro's Number</b>", "6.022 × 10²³ — the number of particles (atoms, molecules, ions) in one mole."),
            ("<b>Mole</b>", "The SI unit for amount of substance; 1 mole = 6.022 × 10²³ particles."),
            ("<b>Mole-to-Particles</b>", "Multiply moles × 6.022 × 10²³ to find the number of particles."),
            ("<b>Particles-to-Moles</b>", "Divide number of particles by 6.022 × 10²³ to find moles."),
            ("<b>Amedeo Avogadro</b>", "Italian scientist who contributed to molecular theory; the number is named after him."),
            ("<b>Universal Counting Unit</b>", "A mole relates microscopic particles to macroscopic measurable amounts."),
        ],
        "quiz": [
            {
                "question": "What is Avogadro's number?",
                "correct": "6.022 × 10²³",
                "wrong": ["6.022 × 10²⁰", "3.0 × 10⁸", "1.66 × 10⁻²⁷"]
            },
            {
                "question": "How many particles are in 2 moles of a substance?",
                "correct": "1.204 × 10²⁴",
                "wrong": ["6.022 × 10²³", "3.011 × 10²³", "1.204 × 10²³"]
            }
        ],
        "flashcards": [
            ("What is Avogadro's number?", "6.022 × 10²³"),
            ("What is a mole?", "A unit of amount equal to 6.022 × 10²³ particles"),
            ("How do you convert moles to particles?", "Multiply moles × 6.022 × 10²³"),
            ("How do you convert particles to moles?", "Divide particles by 6.022 × 10²³"),
            ("How many atoms are in 1 mole of carbon?", "6.022 × 10²³ atoms"),
            ("Who is Avogadro's number named after?", "Amedeo Avogadro"),
            ("How many molecules are in 0.5 mol of H₂O?", "3.011 × 10²³"),
            ("What is the mole used for in chemistry?", "Counting atoms, molecules, or ions in measurable amounts"),
            ("How many moles is 1.204 × 10²⁴ particles?", "2 moles"),
            ("What unit is the mole an SI unit for?", "Amount of substance")
        ]
    },
    "7.4": {
        "topic": "Molar Conversions",
        "summary_title": "Molar Conversions",
        "summary_bullets": [
            ("<b>Moles to Grams</b>", "Multiply moles × molar mass (g/mol)."),
            ("<b>Grams to Moles</b>", "Divide grams by molar mass (g/mol)."),
            ("<b>Moles to Particles</b>", "Multiply moles × 6.022 × 10²³."),
            ("<b>Particles to Moles</b>", "Divide number of particles by 6.022 × 10²³."),
            ("<b>Moles to Liters (Gas at STP)</b>", "Multiply moles × 22.4 L/mol."),
            ("<b>Conversion Map</b>", "Particles ↔ Moles ↔ Grams; Moles ↔ Liters (gas at STP)."),
        ],
        "quiz": [
            {
                "question": "How do you convert moles to grams?",
                "correct": "Multiply moles × molar mass",
                "wrong": ["Divide moles by molar mass", "Multiply by Avogadro's number", "Divide by 22.4"]
            },
            {
                "question": "At STP, 1 mole of any gas occupies:",
                "correct": "22.4 liters",
                "wrong": ["1 liter", "100 liters", "6.022 liters"]
            }
        ],
        "flashcards": [
            ("How do you convert moles to grams?", "Multiply moles × molar mass"),
            ("How do you convert grams to moles?", "Divide grams by molar mass"),
            ("How do you convert moles to particles?", "Multiply moles × 6.022 × 10²³"),
            ("How do you convert moles to liters at STP?", "Multiply moles × 22.4 L/mol"),
            ("What is the molar volume of a gas at STP?", "22.4 L/mol"),
            ("How many grams is 2 moles of NaCl (58.44 g/mol)?", "116.88 g"),
            ("How many moles is 44 g of CO₂ (44 g/mol)?", "1 mole"),
            ("What is STP?", "Standard Temperature and Pressure (0°C, 1 atm)"),
            ("What is the conversion map for moles?", "Particles ↔ Moles ↔ Grams; Moles ↔ Liters (gas)"),
            ("How many liters is 3 moles of gas at STP?", "67.2 L")
        ]
    },
    "7.5": {
        "topic": "Empirical vs Molecular Formulas",
        "summary_title": "Empirical vs Molecular Formulas",
        "summary_bullets": [
            ("<b>Empirical Formula</b>", "The simplest whole-number ratio of atoms in a compound (e.g., CH₂O)."),
            ("<b>Molecular Formula</b>", "The actual number of atoms of each element in a molecule (e.g., C₆H₁₂O₆)."),
            ("<b>Finding Empirical Formula</b>", "Convert percentages to grams → to moles → divide by smallest mole value → round to whole numbers."),
            ("<b>Relationship</b>", "Molecular formula = n × empirical formula, where n = molar mass / empirical mass."),
            ("<b>Percent Composition</b>", "The percentage by mass of each element in a compound."),
            ("<b>Example</b>", "Glucose: empirical = CH₂O (30 g/mol), molecular = C₆H₁₂O₆ (180 g/mol), n = 6."),
        ],
        "quiz": [
            {
                "question": "What does an empirical formula show?",
                "correct": "The simplest whole-number ratio of atoms",
                "wrong": ["The exact number of atoms", "The 3D shape", "The electron configuration"]
            },
            {
                "question": "If the empirical formula is CH₂ and molar mass is 42 g/mol, what is the molecular formula?",
                "correct": "C₃H₆",
                "wrong": ["CH₂", "C₂H₄", "C₆H₁₂"]
            }
        ],
        "flashcards": [
            ("What is an empirical formula?", "The simplest whole-number ratio of atoms in a compound"),
            ("What is a molecular formula?", "The actual number of each atom in a molecule"),
            ("How do you find the empirical formula from percent composition?", "% → grams → moles → divide by smallest → whole numbers"),
            ("How do you find the molecular formula from empirical?", "Multiply empirical by n (molar mass ÷ empirical mass)"),
            ("What is percent composition?", "The percentage by mass of each element"),
            ("What is the empirical formula of glucose (C₆H₁₂O₆)?", "CH₂O"),
            ("What is n if molar mass is 180 and empirical mass is 30?", "n = 6"),
            ("Can a molecular formula be the same as its empirical formula?", "Yes, when n = 1 (e.g., H₂O)"),
            ("What is the empirical formula of C₄H₈?", "CH₂"),
            ("What does percent composition add up to?", "100%")
        ]
    },
    "7.6": {
        "topic": "Limiting Reagents",
        "summary_title": "Limiting Reagents",
        "summary_bullets": [
            ("<b>Limiting Reagent</b>", "The reactant that is completely consumed first and determines the maximum amount of product formed."),
            ("<b>Excess Reagent</b>", "The reactant that is left over after the reaction is complete."),
            ("<b>Finding the Limiting Reagent</b>", "Convert both reactants to moles of product; the one that produces LESS is the limiting reagent."),
            ("<b>Stoichiometry</b>", "Using mole ratios from balanced equations to calculate amounts of reactants/products."),
            ("<b>Theoretical Yield</b>", "The maximum amount of product calculated from the limiting reagent."),
            ("<b>Analogy</b>", "Like a sandwich recipe: if you run out of bread before cheese, bread is the limiting reagent."),
        ],
        "quiz": [
            {
                "question": "What is the limiting reagent?",
                "correct": "The reactant consumed first that limits product formation",
                "wrong": ["The reactant left over", "The product formed", "The catalyst"]
            },
            {
                "question": "How do you identify the limiting reagent?",
                "correct": "Find which reactant produces less product",
                "wrong": ["Pick the one with more mass", "Choose the one with fewer atoms", "Use the larger molecule"]
            }
        ],
        "flashcards": [
            ("What is a limiting reagent?", "The reactant consumed first, determining max product"),
            ("What is an excess reagent?", "The reactant left over after the reaction"),
            ("How do you find the limiting reagent?", "Convert both reactants to moles of product; smaller amount indicates the limiter"),
            ("What is theoretical yield?", "The maximum product based on the limiting reagent"),
            ("What is stoichiometry?", "Using mole ratios from balanced equations for calculations"),
            ("If 2 mol H₂ and 2 mol O₂ react (2H₂ + O₂ → 2H₂O), which is limiting?", "H₂ (needs 2 mol H₂ per 1 mol O₂)"),
            ("Does the limiting reagent always have fewer grams?", "No, it depends on mole ratios, not mass"),
            ("What happens to the excess reagent?", "Some is left unreacted"),
            ("Why is the limiting reagent important?", "It determines how much product can be made"),
            ("What does theoretical yield assume?", "100% of limiting reagent converts to product")
        ]
    },
    "7.7": {
        "topic": "Stoichiometric Calculations",
        "summary_title": "Stoichiometric Calculations",
        "summary_bullets": [
            ("<b>Stoichiometry</b>", "The calculation of quantities in chemical reactions using mole ratios from balanced equations."),
            ("<b>Mole Ratio</b>", "The ratio of moles of one substance to another from the coefficients of a balanced equation."),
            ("<b>Steps</b>", "1) Balance equation. 2) Convert given to moles. 3) Use mole ratio. 4) Convert to desired unit."),
            ("<b>Mass-to-Mass</b>", "Given grams → moles (÷ molar mass) → mole ratio → moles → grams (× molar mass)."),
            ("<b>Volume-to-Volume (Gas)</b>", "At STP, mole ratios equal volume ratios for gases."),
            ("<b>Balanced Equation is Key</b>", "All stoichiometric calculations begin with a correctly balanced equation."),
        ],
        "quiz": [
            {
                "question": "In stoichiometry, what connects two substances in a reaction?",
                "correct": "Mole ratio from the balanced equation",
                "wrong": ["Mass ratio", "Volume alone", "Temperature"]
            },
            {
                "question": "What is the first step in any stoichiometric calculation?",
                "correct": "Balance the chemical equation",
                "wrong": ["Find the limiting reagent", "Convert to liters", "Calculate density"]
            }
        ],
        "flashcards": [
            ("What is stoichiometry?", "Calculating quantities in reactions using balanced-equation mole ratios"),
            ("What is a mole ratio?", "Ratio of moles between substances from balanced equation coefficients"),
            ("What are the steps in a stoichiometric calculation?", "Balance → moles → mole ratio → desired unit"),
            ("In 2H₂ + O₂ → 2H₂O, what is the mole ratio of H₂ to O₂?", "2:1"),
            ("How do you convert grams to moles?", "Divide by molar mass"),
            ("How do you convert moles to grams?", "Multiply by molar mass"),
            ("What is a mass-to-mass calculation?", "Grams → moles → mole ratio → moles → grams"),
            ("For gases at STP, mole ratios equal what?", "Volume ratios"),
            ("Why must the equation be balanced first?", "Coefficients give the correct mole ratios"),
            ("In 2H₂ + O₂ → 2H₂O, how many moles of water from 3 mol H₂?", "3 moles H₂O")
        ]
    },
    "7.8": {
        "topic": "Percent Yield",
        "summary_title": "Percent Yield",
        "summary_bullets": [
            ("<b>Actual Yield</b>", "The amount of product actually obtained from an experiment."),
            ("<b>Theoretical Yield</b>", "The maximum amount of product calculated from stoichiometry (from limiting reagent)."),
            ("<b>Percent Yield</b>", "(Actual yield / Theoretical yield) × 100%."),
            ("<b>Why Less Than 100%</b>", "Side reactions, incomplete reactions, loss during transfer, or impurities."),
            ("<b>100% Yield</b>", "Means the actual yield equals the theoretical yield (rare in practice)."),
            ("<b>Greater Than 100%</b>", "Usually indicates experimental error (e.g., impurities adding mass)."),
        ],
        "quiz": [
            {
                "question": "What is the formula for percent yield?",
                "correct": "(Actual yield / Theoretical yield) × 100%",
                "wrong": ["(Theoretical / Actual) × 100%", "Actual − Theoretical", "Actual × Theoretical"]
            },
            {
                "question": "If theoretical yield is 50g and actual yield is 40g, what is percent yield?",
                "correct": "80%",
                "wrong": ["40%", "90%", "125%"]
            }
        ],
        "flashcards": [
            ("What is actual yield?", "The amount of product actually obtained from an experiment"),
            ("What is theoretical yield?", "The maximum product calculated from stoichiometry"),
            ("What is the formula for percent yield?", "(Actual ÷ Theoretical) × 100%"),
            ("Why is percent yield usually less than 100%?", "Side reactions, incomplete reactions, or transfer losses"),
            ("What does 100% yield mean?", "Actual yield equals theoretical yield"),
            ("If actual = 35g and theoretical = 50g, what is percent yield?", "70%"),
            ("Can percent yield exceed 100%?", "Not ideally; it suggests experimental error"),
            ("What determines theoretical yield?", "The limiting reagent and stoichiometry"),
            ("Why is percent yield important?", "It measures the efficiency of a reaction"),
            ("What could cause a yield greater than 100%?", "Impurities or incomplete drying of the product")
        ]
    },
    # ══════════════════ UNIT 8 ══════════════════
    "8.1": {
        "topic": "Monatomic & Diatomic Gases",
        "summary_title": "Monatomic & Diatomic Gases",
        "summary_bullets": [
            ("<b>Monatomic Gas</b>", "A gas made of single atoms (e.g., noble gases: He, Ne, Ar, Kr, Xe, Rn)."),
            ("<b>Diatomic Gas</b>", "A gas made of molecules with two atoms bonded together."),
            ("<b>Seven Diatomic Elements</b>", "H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂ — remember HONClBrIF."),
            ("<b>Noble Gases</b>", "Monatomic; full outer shells make them stable and unreactive."),
            ("<b>Diatomic in Equations</b>", "Always write diatomic elements as molecules (e.g., O₂, not O) in chemical equations."),
            ("<b>Most Abundant Gas</b>", "Nitrogen (N₂) makes up about 78% of Earth's atmosphere."),
        ],
        "quiz": [
            {
                "question": "Which of the following is a diatomic element?",
                "correct": "O₂",
                "wrong": ["He", "Ne", "Ar"]
            },
            {
                "question": "What mnemonic helps remember the diatomic elements?",
                "correct": "HONClBrIF",
                "wrong": ["VSEPR", "OIL RIG", "ROY G BIV"]
            }
        ],
        "flashcards": [
            ("What is a monatomic gas?", "A gas made of single atoms"),
            ("What is a diatomic gas?", "A gas made of two-atom molecules"),
            ("Name the seven diatomic elements.", "H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂"),
            ("What is the mnemonic for diatomic elements?", "HONClBrIF"),
            ("Are noble gases monatomic or diatomic?", "Monatomic"),
            ("Why are noble gases monatomic?", "Full outer shells — no need to bond"),
            ("What is the most abundant gas in the atmosphere?", "Nitrogen (N₂) at ~78%"),
            ("How should you write oxygen in a chemical equation?", "O₂ (diatomic), not O"),
            ("Is chlorine monatomic or diatomic?", "Diatomic (Cl₂)"),
            ("Give an example of a monatomic gas.", "Helium (He), Neon (Ne), or Argon (Ar)")
        ]
    },
    "8.2": {
        "topic": "Pressure & Standard Atmosphere",
        "summary_title": "Pressure & Standard Atmosphere",
        "summary_bullets": [
            ("<b>Pressure</b>", "Force per unit area exerted by gas particles colliding with container walls."),
            ("<b>Standard Atmosphere (atm)</b>", "1 atm = 101.325 kPa = 760 mmHg = 760 torr."),
            ("<b>Pascal (Pa)</b>", "The SI unit of pressure; 1 kPa = 1000 Pa."),
            ("<b>Barometer</b>", "An instrument that measures atmospheric pressure."),
            ("<b>Manometer</b>", "An instrument that measures the pressure of a gas in a container."),
            ("<b>STP</b>", "Standard Temperature and Pressure: 0°C (273 K) and 1 atm."),
        ],
        "quiz": [
            {
                "question": "1 atm equals how many mmHg?",
                "correct": "760 mmHg",
                "wrong": ["100 mmHg", "273 mmHg", "1000 mmHg"]
            },
            {
                "question": "What instrument measures atmospheric pressure?",
                "correct": "Barometer",
                "wrong": ["Thermometer", "Manometer", "Spectroscope"]
            }
        ],
        "flashcards": [
            ("What is pressure?", "Force per unit area from gas particles hitting container walls"),
            ("What is 1 atm in kPa?", "101.325 kPa"),
            ("What is 1 atm in mmHg?", "760 mmHg"),
            ("What is the SI unit of pressure?", "Pascal (Pa)"),
            ("What is a barometer?", "An instrument that measures atmospheric pressure"),
            ("What is a manometer?", "An instrument that measures gas pressure in a container"),
            ("What is STP?", "Standard Temperature and Pressure (0°C, 1 atm)"),
            ("What causes gas pressure?", "Collisions of gas particles with container walls"),
            ("What is 1 atm in torr?", "760 torr"),
            ("Does pressure increase with more gas particles?", "Yes, more collisions = higher pressure")
        ]
    },
    "8.3": {
        "topic": "Kinetic Molecular Theory",
        "summary_title": "Kinetic Molecular Theory",
        "summary_bullets": [
            ("<b>KMT Assumption 1</b>", "Gas particles are in constant, random, straight-line motion."),
            ("<b>KMT Assumption 2</b>", "Gas particles have negligible volume compared to the container."),
            ("<b>KMT Assumption 3</b>", "There are no attractive or repulsive forces between gas particles."),
            ("<b>KMT Assumption 4</b>", "Collisions between gas particles are perfectly elastic (no energy lost)."),
            ("<b>KMT Assumption 5</b>", "The average kinetic energy is proportional to absolute temperature (K)."),
            ("<b>Ideal Gas</b>", "A hypothetical gas that perfectly follows all KMT assumptions."),
        ],
        "quiz": [
            {
                "question": "According to KMT, gas particle collisions are:",
                "correct": "Perfectly elastic",
                "wrong": ["Inelastic", "Destructive", "Rare"]
            },
            {
                "question": "Average kinetic energy of gas particles is proportional to:",
                "correct": "Absolute temperature (K)",
                "wrong": ["Pressure only", "Volume only", "Number of particles"]
            }
        ],
        "flashcards": [
            ("What does KMT stand for?", "Kinetic Molecular Theory"),
            ("How do gas particles move according to KMT?", "Constant, random, straight-line motion"),
            ("Are forces between gas particles significant in KMT?", "No, they are assumed negligible"),
            ("What type of collisions do ideal gas particles have?", "Perfectly elastic (no energy lost)"),
            ("What is directly proportional to temperature in KMT?", "Average kinetic energy"),
            ("What is an ideal gas?", "A hypothetical gas that perfectly follows KMT"),
            ("Do gas particles have significant volume in KMT?", "No, volume is negligible compared to container"),
            ("What temperature scale is used in gas law calculations?", "Kelvin (K)"),
            ("How do you convert Celsius to Kelvin?", "Add 273 (K = °C + 273)"),
            ("What happens to gas particle speed as temperature increases?", "It increases")
        ]
    },
    "8.4": {
        "topic": "Boyle's Law",
        "summary_title": "Boyle's Law",
        "summary_bullets": [
            ("<b>Boyle's Law</b>", "At constant temperature, pressure and volume are inversely proportional: P₁V₁ = P₂V₂."),
            ("<b>Inverse Relationship</b>", "As pressure increases, volume decreases (and vice versa)."),
            ("<b>Constant Temperature</b>", "Boyle's Law only applies when temperature does not change."),
            ("<b>Example</b>", "Squeezing a balloon: increased pressure → decreased volume."),
            ("<b>Graph</b>", "P vs. V graph is a downward curve (hyperbola)."),
            ("<b>Units</b>", "Pressure and volume can use any units as long as they match on both sides."),
        ],
        "quiz": [
            {
                "question": "What is Boyle's Law formula?",
                "correct": "P₁V₁ = P₂V₂",
                "wrong": ["PV = nRT", "V₁/T₁ = V₂/T₂", "P₁/T₁ = P₂/T₂"]
            },
            {
                "question": "If pressure on a gas doubles, what happens to volume (at constant T)?",
                "correct": "Volume is halved",
                "wrong": ["Volume doubles", "Volume stays the same", "Volume triples"]
            }
        ],
        "flashcards": [
            ("State Boyle's Law.", "At constant temperature, P and V are inversely proportional"),
            ("What is Boyle's Law formula?", "P₁V₁ = P₂V₂"),
            ("What variable is held constant in Boyle's Law?", "Temperature"),
            ("If P increases, what happens to V?", "V decreases"),
            ("If V₁ = 4L at P₁ = 2 atm, what is V₂ at P₂ = 4 atm?", "2 L"),
            ("What type of relationship is P and V?", "Inverse"),
            ("What does a P vs V graph look like?", "A downward curve (hyperbola)"),
            ("Give a real-life example of Boyle's Law.", "Squeezing a syringe — smaller volume, higher pressure"),
            ("Does Boyle's Law apply if temperature changes?", "No, temperature must be constant"),
            ("Who discovered this gas law?", "Robert Boyle")
        ]
    },
    "8.5": {
        "topic": "Charles' Law",
        "summary_title": "Charles' Law",
        "summary_bullets": [
            ("<b>Charles' Law</b>", "At constant pressure, volume and temperature are directly proportional: V₁/T₁ = V₂/T₂."),
            ("<b>Direct Relationship</b>", "As temperature increases, volume increases (and vice versa)."),
            ("<b>Constant Pressure</b>", "Charles' Law only applies when pressure does not change."),
            ("<b>Temperature in Kelvin</b>", "Always use Kelvin for gas law calculations (K = °C + 273)."),
            ("<b>Absolute Zero</b>", "0 K (−273°C); theoretically, gas volume would be zero."),
            ("<b>Example</b>", "A hot air balloon rises because heated air expands (greater volume, same pressure)."),
        ],
        "quiz": [
            {
                "question": "What is Charles' Law formula?",
                "correct": "V₁/T₁ = V₂/T₂",
                "wrong": ["P₁V₁ = P₂V₂", "PV = nRT", "P₁/T₁ = P₂/T₂"]
            },
            {
                "question": "What temperature scale must be used in Charles' Law?",
                "correct": "Kelvin",
                "wrong": ["Celsius", "Fahrenheit", "Rankine"]
            }
        ],
        "flashcards": [
            ("State Charles' Law.", "At constant pressure, V and T are directly proportional"),
            ("What is Charles' Law formula?", "V₁/T₁ = V₂/T₂"),
            ("What variable is held constant?", "Pressure"),
            ("If temperature doubles, what happens to volume?", "Volume doubles"),
            ("What temperature scale must you use?", "Kelvin"),
            ("How do you convert °C to K?", "Add 273"),
            ("What is absolute zero?", "0 K (−273°C) — theoretically zero volume"),
            ("Give a real-life example of Charles' Law.", "Hot air balloon — heating air makes it expand"),
            ("If V₁ = 2L at T₁ = 300K, what is V₂ at T₂ = 600K?", "4 L"),
            ("Who discovered this gas law?", "Jacques Charles")
        ]
    },
    "8.6": {
        "topic": "Gay-Lussac's Law",
        "summary_title": "Gay-Lussac's Law",
        "summary_bullets": [
            ("<b>Gay-Lussac's Law</b>", "At constant volume, pressure and temperature are directly proportional: P₁/T₁ = P₂/T₂."),
            ("<b>Direct Relationship</b>", "As temperature increases, pressure increases (and vice versa)."),
            ("<b>Constant Volume</b>", "Applies to rigid containers where volume cannot change."),
            ("<b>Temperature in Kelvin</b>", "Always use Kelvin for gas law calculations."),
            ("<b>Example</b>", "A tire's pressure increases on a hot day (same volume, higher temperature)."),
            ("<b>Pressure Cooker</b>", "Sealed container: increasing temperature raises pressure, cooking food faster."),
        ],
        "quiz": [
            {
                "question": "What is Gay-Lussac's Law formula?",
                "correct": "P₁/T₁ = P₂/T₂",
                "wrong": ["V₁/T₁ = V₂/T₂", "P₁V₁ = P₂V₂", "PV = nRT"]
            },
            {
                "question": "In Gay-Lussac's Law, what is held constant?",
                "correct": "Volume",
                "wrong": ["Pressure", "Temperature", "Moles"]
            }
        ],
        "flashcards": [
            ("State Gay-Lussac's Law.", "At constant volume, P and T are directly proportional"),
            ("What is Gay-Lussac's Law formula?", "P₁/T₁ = P₂/T₂"),
            ("What is held constant?", "Volume"),
            ("If temperature doubles, what happens to pressure?", "Pressure doubles"),
            ("Give a real-life example.", "Tire pressure increases on a hot day"),
            ("What type of container does this law apply to?", "Rigid (constant volume) containers"),
            ("What temperature scale must be used?", "Kelvin"),
            ("Why does a sealed can explode if heated?", "Pressure increases with temperature in a fixed volume"),
            ("If P₁ = 2 atm at T₁ = 300K, what is P₂ at T₂ = 600K?", "4 atm"),
            ("What is the relationship type between P and T?", "Directly proportional")
        ]
    },
    "8.7": {
        "topic": "Combined Gas Law",
        "summary_title": "Combined Gas Law",
        "summary_bullets": [
            ("<b>Combined Gas Law</b>", "Combines Boyle's, Charles', and Gay-Lussac's: P₁V₁/T₁ = P₂V₂/T₂."),
            ("<b>When to Use</b>", "When pressure, volume, AND temperature all change (nothing held constant except moles)."),
            ("<b>Special Cases</b>", "Hold T constant → Boyle's; Hold P constant → Charles'; Hold V constant → Gay-Lussac's."),
            ("<b>Temperature</b>", "Must always be in Kelvin."),
            ("<b>Solving</b>", "Identify known values, solve for the unknown variable algebraically."),
            ("<b>Units</b>", "Pressure and volume units must be consistent on both sides."),
        ],
        "quiz": [
            {
                "question": "What is the Combined Gas Law formula?",
                "correct": "P₁V₁/T₁ = P₂V₂/T₂",
                "wrong": ["PV = nRT", "P₁V₁ = P₂V₂", "V₁/T₁ = V₂/T₂"]
            },
            {
                "question": "The Combined Gas Law combines which three laws?",
                "correct": "Boyle's, Charles', and Gay-Lussac's",
                "wrong": ["Newton's three laws", "Hess's and Dalton's", "Avogadro's and Boyle's"]
            }
        ],
        "flashcards": [
            ("What is the Combined Gas Law?", "P₁V₁/T₁ = P₂V₂/T₂"),
            ("What laws does it combine?", "Boyle's, Charles', and Gay-Lussac's"),
            ("When do you use the Combined Gas Law?", "When P, V, and T all change"),
            ("If T is constant, the Combined Law simplifies to?", "Boyle's Law (P₁V₁ = P₂V₂)"),
            ("If P is constant, it simplifies to?", "Charles' Law (V₁/T₁ = V₂/T₂)"),
            ("If V is constant, it simplifies to?", "Gay-Lussac's Law (P₁/T₁ = P₂/T₂)"),
            ("What temperature scale must be used?", "Kelvin"),
            ("What must be consistent on both sides?", "Units for P and V"),
            ("What is held constant in the Combined Gas Law?", "Only the amount of gas (moles)"),
            ("How do you solve for V₂?", "V₂ = P₁V₁T₂ / (T₁P₂)")
        ]
    },
    "8.8": {
        "topic": "Ideal Gas Law",
        "summary_title": "Ideal Gas Law",
        "summary_bullets": [
            ("<b>Ideal Gas Law</b>", "PV = nRT; relates pressure, volume, moles, and temperature."),
            ("<b>R (Gas Constant)</b>", "0.0821 L·atm/(mol·K) or 8.314 J/(mol·K)."),
            ("<b>n</b>", "The number of moles of gas."),
            ("<b>When to Use</b>", "When you need to find P, V, n, or T and have the other three values."),
            ("<b>Ideal vs. Real</b>", "Ideal gases perfectly follow PV = nRT; real gases deviate at high P and low T."),
            ("<b>Units Must Match R</b>", "If R = 0.0821, use atm, L, mol, and K."),
        ],
        "quiz": [
            {
                "question": "What is the Ideal Gas Law?",
                "correct": "PV = nRT",
                "wrong": ["P₁V₁ = P₂V₂", "E = mc²", "V₁/T₁ = V₂/T₂"]
            },
            {
                "question": "What is the value of R in L·atm/(mol·K)?",
                "correct": "0.0821",
                "wrong": ["8.314", "22.4", "6.022"]
            }
        ],
        "flashcards": [
            ("What is the Ideal Gas Law?", "PV = nRT"),
            ("What does each variable stand for in PV = nRT?", "P=pressure, V=volume, n=moles, R=gas constant, T=temperature"),
            ("What is R in L·atm/(mol·K)?", "0.0821"),
            ("What is R in J/(mol·K)?", "8.314"),
            ("When do you use the Ideal Gas Law?", "When you know 3 of 4 variables (P, V, n, T) and solve for the 4th"),
            ("What units must match when R = 0.0821?", "atm, L, mol, K"),
            ("Solve for n: PV = nRT → n = ?", "n = PV / RT"),
            ("What is the volume of 1 mol of gas at STP?", "22.4 L"),
            ("Do real gases perfectly follow PV = nRT?", "No, they deviate at high P and low T"),
            ("What does 'ideal' mean in ideal gas?", "Follows KMT perfectly — no intermolecular forces, negligible volume")
        ]
    },
    "8.9": {
        "topic": "Real Gases & Deviations",
        "summary_title": "Real Gases & Deviations",
        "summary_bullets": [
            ("<b>Real Gases</b>", "Actual gases that deviate from ideal behavior, especially at high pressure and low temperature."),
            ("<b>Intermolecular Forces</b>", "Real gas particles DO attract each other, unlike ideal gas assumptions."),
            ("<b>Particle Volume</b>", "Real gas particles DO occupy space, unlike the ideal assumption of negligible volume."),
            ("<b>High Pressure</b>", "Particles are forced close together; volume and intermolecular forces become significant."),
            ("<b>Low Temperature</b>", "Particles move slowly; attractive forces have greater effect, causing deviation."),
            ("<b>Most Ideal Behavior</b>", "Gases behave most ideally at HIGH temperature and LOW pressure."),
        ],
        "quiz": [
            {
                "question": "Under what conditions do real gases deviate most from ideal behavior?",
                "correct": "High pressure and low temperature",
                "wrong": ["Low pressure and high temperature", "Standard conditions", "In a vacuum"]
            },
            {
                "question": "What makes real gases different from ideal gases?",
                "correct": "They have intermolecular forces and particle volume",
                "wrong": ["They move in straight lines", "They have elastic collisions", "They have no mass"]
            }
        ],
        "flashcards": [
            ("What are real gases?", "Actual gases that deviate from ideal gas behavior"),
            ("When do real gases deviate most?", "At high pressure and low temperature"),
            ("When do gases behave most ideally?", "At high temperature and low pressure"),
            ("Why do real gases deviate at high pressure?", "Particles are close; volume and forces become significant"),
            ("Why do real gases deviate at low temperature?", "Slow particles; attractive forces have greater effect"),
            ("Do ideal gas particles attract each other?", "No (but real gas particles do)"),
            ("Do ideal gas particles have volume?", "No (assumed negligible, but real particles do)"),
            ("Which gas behaves most ideally?", "Helium (small, nonpolar, very weak forces)"),
            ("What is the van der Waals equation?", "A modified gas law that accounts for real gas behavior"),
            ("Why does He behave more ideally than NH₃?", "He has weaker intermolecular forces and smaller size")
        ]
    },
}

# ─── HELPER FUNCTIONS (same as Units 1-4 script) ──────────────────
def make_summary_html(data):
    lines = []
    lines.append(f'<h3>Key Concepts: {data["summary_title"]}</h3>')
    lines.append('<p><b>Core Definitions</b></p>')
    lines.append('<ul>')
    for label, desc in data["summary_bullets"]:
        lines.append(f'<li>{label}: {desc}</li>')
    lines.append('</ul>')
    return '\n'.join(lines)

def make_quiz_html(data):
    blocks = []
    for i, q in enumerate(data["quiz"], 1):
        options = [(q["correct"], "correct")] + [(w, "wrong") for w in q["wrong"]]
        random.seed(hash(q["question"]))
        random.shuffle(options)
        lines = []
        lines.append(f'            <div class="quiz-question" style="margin-bottom: 2rem;" data-attempts="2">')
        lines.append(f'                <p style="font-weight: 700; font-size: 1.45rem; margin-bottom: 1rem;">{i}. {q["question"]}</p>')
        for text, val in options:
            lines.append(f'            ')
            lines.append(f'                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">')
            lines.append(f'                    <input type="radio" name="q{i}" value="{val}"> {text}')
            lines.append(f'                </label>')
        lines.append(f'                ')
        lines.append(f'                <div class="attempts-indicator"></div>')
        lines.append(f'                <div style="margin-top:1.5rem;">')
        lines.append(f'                    <button type="button" class="action-button" onclick="window.checkQuizAnswer(\'q{i}\', \'correct\', this)">Submit Answer</button>')
        lines.append(f'                    <button type="button" class="nav-button" onclick="window.resetQuizQuestion(this)" style="margin-left:0.5rem;">Try Again</button>')
        lines.append(f'                </div>')
        lines.append(f'            </div>')
        blocks.append('\n'.join(lines))
    return '\n            \n'.join(blocks)

def make_flashcards_js(data):
    lines = ['    window.lessonFlashcards = [']
    for q, a in data["flashcards"]:
        q_esc = q.replace('"', '\\"')
        a_esc = a.replace('"', '\\"')
        lines.append(f'          {{ question: "{q_esc}", answer: "{a_esc}" }},')
    lines.append('      ];')
    return '\n'.join(lines)

# ─── FILE PROCESSING ──────────────────────────────────────────────
changes = 0
files_modified = 0

for lesson_id, data in CONTENT.items():
    unit_num = lesson_id.split('.')[0]
    unit_dir = f"Unit{unit_num}"
    unit_path = os.path.join(BASE, unit_dir)
    
    if not os.path.isdir(unit_path):
        print(f"  [SKIP] Unit directory not found: {unit_dir}")
        continue
    
    # ── SUMMARY ──
    if not data.get("skip_summary"):
        summary_glob = glob.glob(os.path.join(unit_path, f"Lesson {lesson_id}*_Summary.html"))
        for fpath in summary_glob:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'Solid' in content and 'Liquid' in content and 'Gas' in content and 'tightly packed' in content:
                new_summary = make_summary_html(data)
                pattern = r'(<div class="lesson-(?:notes|summary-content)">)\s*.*?\s*(</div>)'
                new_content, n = re.subn(pattern, replacement := f'\\1\n{new_summary}\n\\2', content, count=1, flags=re.DOTALL)
                if n > 0:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    changes += n; files_modified += 1
                    print(f"  [SUMMARY] Updated: {os.path.basename(fpath)}")
                else:
                    print(f"  [WARN] Pattern not matched: {os.path.basename(fpath)}")
            else:
                print(f"  [SKIP] Summary already has real content: {os.path.basename(fpath)}")
    
    # ── QUIZ ──
    if not data.get("skip_quiz"):
        quiz_glob = glob.glob(os.path.join(unit_path, f"Lesson {lesson_id}*_Quiz.html"))
        for fpath in quiz_glob:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            is_placeholder = ('state of matter' in content.lower() or 
                            'particles move most freely' in content.lower() or
                            'definite shape and volume' in content.lower() or
                            'Placeholder' in content)
            if is_placeholder:
                new_quiz = make_quiz_html(data)
                pattern = r'(<form id="quiz-form">)\s*.*?\s*(</form>)'
                new_content, n = re.subn(pattern, f'\\1\n\n{new_quiz}\n            \n\\2', content, count=1, flags=re.DOTALL)
                if n > 0:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    changes += n; files_modified += 1
                    print(f"  [QUIZ] Updated: {os.path.basename(fpath)}")
                else:
                    print(f"  [WARN] Quiz pattern not matched: {os.path.basename(fpath)}")
            else:
                print(f"  [SKIP] Quiz already has real content: {os.path.basename(fpath)}")
    
    # ── PRACTICE ──
    if not data.get("skip_practice"):
        practice_glob = glob.glob(os.path.join(unit_path, f"Lesson {lesson_id}*_Practice.html"))
        for fpath in practice_glob:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            is_placeholder = ('state of matter' in content.lower() and 'definite shape' in content.lower()) or \
                           ('tightly packed' in content.lower()) or \
                           ('move most freely' in content.lower()) or \
                           ('vibrate in fixed' in content.lower())
            if is_placeholder:
                new_flashcards = make_flashcards_js(data)
                pattern = r'window\.lessonFlashcards\s*=\s*\[.*?\];'
                new_content, n = re.subn(pattern, new_flashcards.strip(), content, count=1, flags=re.DOTALL)
                if n > 0:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    changes += n; files_modified += 1
                    print(f"  [PRACTICE] Updated: {os.path.basename(fpath)}")
                else:
                    print(f"  [WARN] Practice pattern not matched: {os.path.basename(fpath)}")
            else:
                print(f"  [SKIP] Practice already has real content: {os.path.basename(fpath)}")

print(f"\n{'='*60}")
print(f"Units 6-8 complete: {files_modified} files modified, {changes} changes")
