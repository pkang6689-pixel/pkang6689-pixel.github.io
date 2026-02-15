#!/usr/bin/env python3
"""Generate topic-specific content for Units 9-12 (Summary, Quiz, Practice files).
Replaces placeholder States of Matter content with real chemistry content."""

import os
import re
import glob

BASE = os.path.join(os.path.dirname(__file__), '..', 'ArisEdu Project Folder', 'ChemistryLessons')

# ─── Content Database ───────────────────────────────────────────────────────────

LESSONS = {
    # ── Unit 9: Solutions ──
    '9.1': {
        'topic': 'Solution Nomenclature',
        'summary': [
            ('Core Definitions', [
                ('<b>Solution</b>: A homogeneous mixture of two or more substances evenly distributed at the molecular level.', None),
                ('<b>Solute</b>: The substance that is dissolved in the solution (usually present in smaller amount).', None),
                ('<b>Solvent</b>: The substance that does the dissolving (usually present in larger amount).', None),
                ('<b>Aqueous Solution</b>: A solution where water is the solvent, denoted by (aq) in chemical equations.', None),
            ]),
        ],
        'quiz': [
            ('In a saltwater solution, what is the solute?', [('Salt', True), ('Water', False), ('The container', False), ('Air', False)]),
            ('What does the symbol (aq) indicate in a chemical equation?', [('The substance is dissolved in water', True), ('The substance is a gas', False), ('The substance is a solid', False), ('The reaction requires heat', False)]),
        ],
        'flashcards': [
            ('What is a solution?', 'A homogeneous mixture of two or more substances'),
            ('What is the solute?', 'The substance that is dissolved in smaller amount'),
            ('What is the solvent?', 'The substance doing the dissolving, usually in larger amount'),
            ('What does aqueous (aq) mean?', 'Dissolved in water'),
            ('In sugar water, what is the solvent?', 'Water'),
            ('In sugar water, what is the solute?', 'Sugar'),
            ('What type of mixture is a solution?', 'Homogeneous'),
            ('Can gases be solvents?', 'Yes — air is a solution of gases with nitrogen as solvent'),
            ('What is an alloy?', 'A solid solution of metals (e.g., brass = copper + zinc)'),
            ('What is a tincture?', 'A solution where alcohol is the solvent'),
        ],
    },
    '9.2': {
        'topic': 'Concentration',
        'summary': [
            ('Core Definitions', [
                ('<b>Concentration</b>: A measure of how much solute is dissolved in a given amount of solution.', None),
                ('<b>Concentrated Solution</b>: Contains a large amount of solute relative to solvent.', None),
                ('<b>Dilute Solution</b>: Contains a small amount of solute relative to solvent.', None),
                ('<b>Percent Concentration</b>: (mass of solute / mass of solution) × 100%.', None),
            ]),
        ],
        'quiz': [
            ('A solution with a large amount of solute relative to solvent is described as:', [('Concentrated', True), ('Dilute', False), ('Saturated', False), ('Unsaturated', False)]),
            ('How do you calculate percent concentration by mass?', [('(mass solute / mass solution) × 100', True), ('(mass solvent / mass solute) × 100', False), ('(volume solute / volume solution) × 100', False), ('(moles solute / mass solution) × 100', False)]),
        ],
        'flashcards': [
            ('What is concentration?', 'A measure of how much solute is dissolved in a given amount of solution'),
            ('What is a concentrated solution?', 'A solution with a large amount of solute relative to solvent'),
            ('What is a dilute solution?', 'A solution with a small amount of solute relative to solvent'),
            ('Formula for percent concentration by mass?', '(mass of solute ÷ mass of solution) × 100%'),
            ('What are the units of concentration?', 'Common units include %, molarity (M), ppm, and ppb'),
            ('What is ppm?', 'Parts per million — mg of solute per liter of solution'),
            ('If 5 g of salt is dissolved in 95 g of water, what is the percent concentration?', '5%  (5/100 × 100)'),
            ('Does adding more solvent increase or decrease concentration?', 'Decrease — dilutes the solution'),
            ('What is mass/volume percent?', '(mass solute in g / volume solution in mL) × 100%'),
            ('How can you increase the concentration of a solution?', 'Add more solute or evaporate some solvent'),
        ],
    },
    '9.3': {
        'topic': 'Dilution',
        'summary': [
            ('Core Definitions', [
                ('<b>Dilution</b>: The process of reducing the concentration of a solution by adding more solvent.', None),
                ('<b>Dilution Equation</b>: M₁V₁ = M₂V₂, where M is molarity and V is volume.', None),
                ('<b>Stock Solution</b>: A concentrated solution that is diluted to make a less concentrated solution.', None),
                ('<b>Key Principle</b>: The amount of solute stays the same during dilution — only solvent is added.', None),
            ]),
        ],
        'quiz': [
            ('Which equation is used for dilution calculations?', [('M₁V₁ = M₂V₂', True), ('PV = nRT', False), ('E = mc²', False), ('pH = −log[H⁺]', False)]),
            ('During dilution, what remains constant?', [('The amount (moles) of solute', True), ('The volume of solution', False), ('The concentration', False), ('The mass of solvent', False)]),
        ],
        'flashcards': [
            ('What is dilution?', 'Reducing concentration by adding more solvent'),
            ('What is the dilution equation?', 'M₁V₁ = M₂V₂'),
            ('What does M₁ represent?', 'The initial molarity (concentration)'),
            ('What does V₂ represent?', 'The final volume after dilution'),
            ('What stays constant during dilution?', 'The number of moles of solute'),
            ('What is a stock solution?', 'A concentrated solution used to prepare dilute solutions'),
            ('If M₁ = 6 M and V₁ = 2 L, and V₂ = 12 L, what is M₂?', '1 M'),
            ('Does dilution change the solute?', 'No — it only adds solvent'),
            ('How do you dilute an acid safely?', 'Add acid to water, never water to acid'),
            ('What is serial dilution?', 'Repeated dilution steps to achieve very low concentrations'),
        ],
    },
    '9.4': {
        'topic': 'Molarity',
        'summary': [
            ('Core Definitions', [
                ('<b>Molarity (M)</b>: The number of moles of solute per liter of solution. M = mol / L.', None),
                ('<b>Mole</b>: 6.022 × 10²³ particles (Avogadro\'s number).', None),
                ('<b>Standard Solution</b>: A solution with a precisely known molarity.', None),
                ('<b>Volumetric Flask</b>: Glassware used to prepare solutions of exact molarity.', None),
            ]),
        ],
        'quiz': [
            ('What is the formula for molarity?', [('Moles of solute ÷ liters of solution', True), ('Grams of solute ÷ liters of solution', False), ('Moles of solute ÷ kilograms of solvent', False), ('Mass of solute ÷ mass of solution', False)]),
            ('If 2 moles of NaCl are dissolved in 0.5 L of solution, what is the molarity?', [('4 M', True), ('1 M', False), ('2 M', False), ('0.25 M', False)]),
        ],
        'flashcards': [
            ('What is molarity?', 'Moles of solute per liter of solution (mol/L)'),
            ('What is the symbol for molarity?', 'M'),
            ('Formula for molarity?', 'M = moles of solute ÷ volume of solution in liters'),
            ('What is a 1 M solution?', 'A solution containing 1 mole of solute per liter'),
            ('How do you find moles from molarity?', 'moles = M × V (in liters)'),
            ('How do you find volume from molarity?', 'V = moles ÷ M'),
            ('What is a standard solution?', 'A solution with a precisely known concentration'),
            ('What is a volumetric flask used for?', 'Preparing solutions of exact molarity'),
            ('What is the difference between molarity and molality?', 'Molarity uses volume of solution; molality uses mass of solvent'),
            ('If 58.5 g NaCl dissolves in 1 L, what is the molarity?', '1 M (molar mass of NaCl = 58.5 g/mol)'),
        ],
    },
    '9.5': {
        'topic': 'Solution Types',
        'summary': [
            ('Core Definitions', [
                ('<b>Saturated Solution</b>: Contains the maximum amount of dissolved solute at a given temperature.', None),
                ('<b>Unsaturated Solution</b>: Contains less than the maximum amount of solute — more can dissolve.', None),
                ('<b>Supersaturated Solution</b>: Contains more dissolved solute than a saturated solution; unstable.', None),
                ('<b>Solubility</b>: The maximum amount of solute that dissolves in a given amount of solvent at a specific temperature.', None),
            ]),
        ],
        'quiz': [
            ('A solution that contains more solute than it can normally dissolve is:', [('Supersaturated', True), ('Saturated', False), ('Unsaturated', False), ('Dilute', False)]),
            ('What can you do to an unsaturated solution?', [('Dissolve more solute in it', True), ('Nothing — it is at maximum capacity', False), ('Cool it to precipitate solute', False), ('Filter out excess solute', False)]),
        ],
        'flashcards': [
            ('What is a saturated solution?', 'A solution holding the maximum amount of dissolved solute at a given temperature'),
            ('What is an unsaturated solution?', 'A solution that can still dissolve more solute'),
            ('What is a supersaturated solution?', 'A solution containing more solute than normally possible; it is unstable'),
            ('How do you make a supersaturated solution?', 'Dissolve solute at high temperature, then slowly cool without disturbance'),
            ('What happens if you add a seed crystal to a supersaturated solution?', 'Excess solute rapidly crystallizes out'),
            ('What is solubility?', 'The maximum grams of solute that dissolve in 100 g of solvent at a given temperature'),
            ('Does temperature affect solubility of solids?', 'Yes — most solids dissolve more at higher temperatures'),
            ('Does temperature affect solubility of gases?', 'Yes — gases are more soluble at lower temperatures'),
            ('What is dynamic equilibrium in a saturated solution?', 'Rate of dissolving equals rate of crystallization'),
            ('Is sea water saturated or unsaturated with NaCl?', 'Unsaturated — more salt can dissolve'),
        ],
    },
    '9.6': {
        'topic': 'Factors Affecting Solubility',
        'summary': [
            ('Core Definitions', [
                ('<b>Like Dissolves Like</b>: Polar solvents dissolve polar/ionic solutes; nonpolar solvents dissolve nonpolar solutes.', None),
                ('<b>Temperature Effect</b>: Increasing temperature usually increases solubility of solids but decreases solubility of gases.', None),
                ('<b>Pressure Effect</b>: Increasing pressure increases solubility of gases (Henry\'s Law) but has little effect on solids/liquids.', None),
                ('<b>Surface Area & Agitation</b>: Crushing solute and stirring increases the rate of dissolving (not solubility itself).', None),
            ]),
        ],
        'quiz': [
            ('According to "like dissolves like," which solvent best dissolves table salt (NaCl)?', [('Water (polar)', True), ('Hexane (nonpolar)', False), ('Oil', False), ('Gasoline', False)]),
            ('How does increasing pressure affect gas solubility?', [('It increases gas solubility', True), ('It decreases gas solubility', False), ('It has no effect', False), ('It causes the gas to solidify', False)]),
        ],
        'flashcards': [
            ('What does "like dissolves like" mean?', 'Polar solvents dissolve polar solutes; nonpolar solvents dissolve nonpolar solutes'),
            ('Why does sugar dissolve in water?', 'Both are polar molecules'),
            ('Why doesn\'t oil dissolve in water?', 'Oil is nonpolar and water is polar'),
            ('How does temperature affect solid solubility?', 'Most solids dissolve more at higher temperatures'),
            ('How does temperature affect gas solubility?', 'Gases dissolve less at higher temperatures'),
            ('What is Henry\'s Law?', 'Gas solubility is directly proportional to pressure above the liquid'),
            ('Why does a soda fizz when opened?', 'Pressure decreases, reducing CO₂ solubility, so gas escapes'),
            ('Does stirring change solubility?', 'No — it only increases the rate of dissolving'),
            ('Does crushing a solute change solubility?', 'No — it increases surface area and dissolving rate'),
            ('What is an immiscible liquid?', 'A liquid that does not dissolve in another (e.g., oil and water)'),
        ],
    },
    '9.7': {
        'topic': 'Colligative Properties',
        'summary': [
            ('Core Definitions', [
                ('<b>Colligative Properties</b>: Properties that depend on the number of solute particles, not their identity.', None),
                ('<b>Boiling Point Elevation</b>: Adding solute raises the boiling point of a solution above that of the pure solvent.', None),
                ('<b>Freezing Point Depression</b>: Adding solute lowers the freezing point of a solution below that of the pure solvent.', None),
                ('<b>Osmotic Pressure</b>: Pressure required to prevent osmosis across a semipermeable membrane.', None),
            ]),
        ],
        'quiz': [
            ('Why does adding salt to water raise its boiling point?', [('Solute particles interfere with vaporization', True), ('Salt is heavier than water', False), ('Salt reacts with water', False), ('Salt absorbs heat', False)]),
            ('Which is a colligative property?', [('Freezing point depression', True), ('Color of the solution', False), ('Density', False), ('Chemical reactivity', False)]),
        ],
        'flashcards': [
            ('What are colligative properties?', 'Properties that depend on the number of solute particles, not their identity'),
            ('Name three colligative properties.', 'Boiling point elevation, freezing point depression, osmotic pressure'),
            ('What is boiling point elevation?', 'Adding solute raises the boiling point of the solvent'),
            ('What is freezing point depression?', 'Adding solute lowers the freezing point of the solvent'),
            ('Why is salt put on icy roads?', 'It lowers the freezing point of water, melting the ice'),
            ('What is osmotic pressure?', 'Pressure needed to prevent osmosis through a semipermeable membrane'),
            ('What is vapor pressure lowering?', 'Solute particles reduce the number of solvent molecules that can evaporate'),
            ('Do colligative properties depend on solute identity?', 'No — only on the number of dissolved particles'),
            ('Which has a greater effect: NaCl or sugar at the same molality?', 'NaCl — it dissociates into 2 ions, doubling the particle count'),
            ('What is the van\'t Hoff factor (i)?', 'The number of particles a solute produces when dissolved'),
        ],
    },
    '9.8': {
        'topic': 'Solubility Curves',
        'summary': [
            ('Core Definitions', [
                ('<b>Solubility Curve</b>: A graph showing the relationship between solubility of a substance and temperature.', None),
                ('<b>Reading the Curve</b>: Points on the line = saturated; below = unsaturated; above = supersaturated.', None),
                ('<b>Endothermic Dissolving</b>: Most solid solutes show increasing solubility with temperature (curve slopes up).', None),
                ('<b>Gas Solubility</b>: Gas curves slope downward — gases become less soluble as temperature increases.', None),
            ]),
        ],
        'quiz': [
            ('On a solubility curve, a point below the line represents what type of solution?', [('Unsaturated', True), ('Saturated', False), ('Supersaturated', False), ('Insoluble', False)]),
            ('As temperature increases, the solubility of most solid solutes:', [('Increases', True), ('Decreases', False), ('Stays the same', False), ('Becomes zero', False)]),
        ],
        'flashcards': [
            ('What does a solubility curve show?', 'How solubility changes with temperature'),
            ('What does a point on the line of a solubility curve represent?', 'A saturated solution'),
            ('What does a point below the curve represent?', 'An unsaturated solution'),
            ('What does a point above the curve represent?', 'A supersaturated solution'),
            ('How do most solid solubility curves slope?', 'Upward — solubility increases with temperature'),
            ('How do gas solubility curves slope?', 'Downward — gases are less soluble at higher temperatures'),
            ('Which compound has a nearly flat solubility curve?', 'NaCl — its solubility changes very little with temperature'),
            ('Which compound has a steep solubility curve?', 'KNO₃ — its solubility increases dramatically with temperature'),
            ('What is the x-axis on a solubility curve?', 'Temperature (°C)'),
            ('What is the y-axis on a solubility curve?', 'Solubility (g solute per 100 g water)'),
        ],
    },

    # ── Unit 10: Acids & Bases ──
    '10.1': {
        'topic': 'Acid & Base Properties',
        'summary': [
            ('Core Definitions', [
                ('<b>Acid</b>: A substance that produces H⁺ (hydrogen) ions in solution; tastes sour; pH below 7.', None),
                ('<b>Base</b>: A substance that produces OH⁻ (hydroxide) ions in solution; tastes bitter, feels slippery; pH above 7.', None),
                ('<b>Arrhenius Definition</b>: Acids produce H⁺ in water; bases produce OH⁻ in water.', None),
                ('<b>Brønsted-Lowry Definition</b>: Acids are proton (H⁺) donors; bases are proton acceptors.', None),
            ]),
        ],
        'quiz': [
            ('Which ion do acids produce in solution?', [('H⁺', True), ('OH⁻', False), ('Na⁺', False), ('Cl⁻', False)]),
            ('A Brønsted-Lowry base is defined as a:', [('Proton acceptor', True), ('Proton donor', False), ('Electron donor', False), ('Electron acceptor', False)]),
        ],
        'flashcards': [
            ('What ion do acids produce?', 'H⁺ (hydrogen ions)'),
            ('What ion do bases produce?', 'OH⁻ (hydroxide ions)'),
            ('What does an acid taste like?', 'Sour'),
            ('What does a base feel like?', 'Slippery'),
            ('What is the Arrhenius definition of an acid?', 'A substance that produces H⁺ ions in water'),
            ('What is a Brønsted-Lowry acid?', 'A proton (H⁺) donor'),
            ('What is a Brønsted-Lowry base?', 'A proton (H⁺) acceptor'),
            ('What is the pH range of acids?', 'Below 7'),
            ('What is the pH of a neutral solution?', '7'),
            ('What color does litmus paper turn in acid?', 'Red'),
        ],
    },
    '10.2': {
        'topic': 'Binary Acids vs Oxyacids',
        'summary': [
            ('Core Definitions', [
                ('<b>Binary Acid</b>: An acid made of hydrogen and one other nonmetal element (e.g., HCl, HBr).', None),
                ('<b>Oxyacid</b>: An acid containing hydrogen, oxygen, and another element (e.g., H₂SO₄, HNO₃).', None),
                ('<b>Binary Acid Naming</b>: Use the prefix "hydro-" + root of the element + "-ic acid" (e.g., hydrochloric acid).', None),
                ('<b>Oxyacid Naming</b>: If the polyatomic ion ends in "-ate," the acid ends in "-ic acid"; if "-ite," then "-ous acid."', None),
            ]),
        ],
        'quiz': [
            ('Which of the following is a binary acid?', [('HCl', True), ('H₂SO₄', False), ('HNO₃', False), ('H₃PO₄', False)]),
            ('An oxyacid contains which elements?', [('Hydrogen, oxygen, and one other element', True), ('Only hydrogen and a nonmetal', False), ('Only oxygen and a metal', False), ('Hydrogen and a metal', False)]),
        ],
        'flashcards': [
            ('What is a binary acid?', 'An acid consisting of hydrogen and one other nonmetal'),
            ('What is an oxyacid?', 'An acid containing hydrogen, oxygen, and another element'),
            ('Give an example of a binary acid.', 'HCl (hydrochloric acid), HBr (hydrobromic acid)'),
            ('Give an example of an oxyacid.', 'H₂SO₄ (sulfuric acid), HNO₃ (nitric acid)'),
            ('How do you name a binary acid?', 'hydro- + root of element + -ic acid'),
            ('What is the name of HF as an acid?', 'Hydrofluoric acid'),
            ('If a polyatomic ion ends in -ate, how does the acid end?', '-ic acid'),
            ('If a polyatomic ion ends in -ite, how does the acid end?', '-ous acid'),
            ('H₂SO₄ comes from sulfate — what is its acid name?', 'Sulfuric acid'),
            ('H₂SO₃ comes from sulfite — what is its acid name?', 'Sulfurous acid'),
        ],
    },
    '10.3': {
        'topic': 'Naming Acids',
        'summary': [
            ('Core Definitions', [
                ('<b>Naming Binary Acids</b>: hydro- + element root + -ic acid. Example: HBr → hydrobromic acid.', None),
                ('<b>Naming Oxyacids (-ate)</b>: Drop "-ate," add "-ic acid." Example: H₂SO₄ (sulfate → sulfuric acid).', None),
                ('<b>Naming Oxyacids (-ite)</b>: Drop "-ite," add "-ous acid." Example: H₂SO₃ (sulfite → sulfurous acid).', None),
                ('<b>Writing Formulas</b>: Identify the anion, determine its charge, balance with H⁺ ions.', None),
            ]),
        ],
        'quiz': [
            ('What is the correct name for HBr in aqueous solution?', [('Hydrobromic acid', True), ('Bromic acid', False), ('Hydrogen bromide', False), ('Bromous acid', False)]),
            ('The acid H₂CO₃ is named:', [('Carbonic acid', True), ('Hydrocarbonic acid', False), ('Carbonous acid', False), ('Carbon acid', False)]),
        ],
        'flashcards': [
            ('How do you name HCl as an acid?', 'Hydrochloric acid'),
            ('How do you name HNO₃?', 'Nitric acid (from nitrate → -ic acid)'),
            ('How do you name HNO₂?', 'Nitrous acid (from nitrite → -ous acid)'),
            ('What prefix is used for binary acid names?', 'hydro-'),
            ('What suffix is used for binary acid names?', '-ic acid'),
            ('If the anion is phosphate (PO₄³⁻), what is the acid?', 'H₃PO₄ — phosphoric acid'),
            ('If the anion is chlorite (ClO₂⁻), what is the acid?', 'HClO₂ — chlorous acid'),
            ('Name HI as an acid.', 'Hydroiodic acid'),
            ('Name H₂C₂O₄ (from oxalate).', 'Oxalic acid'),
            ('What determines if an acid name uses hydro-?', 'Binary acids (no oxygen) use hydro-; oxyacids do not'),
        ],
    },
    '10.4': {
        'topic': 'Identifying Acids & Bases',
        'summary': [
            ('Core Definitions', [
                ('<b>Indicators</b>: Chemicals that change color depending on pH (e.g., litmus, phenolphthalein).', None),
                ('<b>Litmus Test</b>: Blue litmus turns red in acid; red litmus turns blue in base.', None),
                ('<b>Phenolphthalein</b>: Colorless in acid, turns pink/magenta in base (pH > 8.2).', None),
                ('<b>pH Paper</b>: Universal indicator paper that shows a range of colors for different pH values.', None),
            ]),
        ],
        'quiz': [
            ('What happens to blue litmus paper in an acidic solution?', [('It turns red', True), ('It stays blue', False), ('It turns green', False), ('It turns pink', False)]),
            ('Phenolphthalein turns pink in a:', [('Basic solution', True), ('Acidic solution', False), ('Neutral solution', False), ('Saturated solution', False)]),
        ],
        'flashcards': [
            ('What is an indicator?', 'A substance that changes color based on pH'),
            ('What does blue litmus paper do in acid?', 'Turns red'),
            ('What does red litmus paper do in base?', 'Turns blue'),
            ('What color is phenolphthalein in acid?', 'Colorless'),
            ('What color is phenolphthalein in base?', 'Pink/magenta'),
            ('What is pH paper?', 'Universal indicator paper showing different colors for different pH values'),
            ('How can you identify an acid by formula?', 'It starts with H (e.g., HCl, H₂SO₄)'),
            ('How can you identify a base by formula?', 'It ends with OH (e.g., NaOH, KOH)'),
            ('What is a Lewis acid?', 'An electron pair acceptor'),
            ('What is a Lewis base?', 'An electron pair donor'),
        ],
    },
    '10.5': {
        'topic': 'Strong vs Weak Acids & Bases',
        'summary': [
            ('Core Definitions', [
                ('<b>Strong Acid</b>: Completely dissociates (ionizes) in water. Examples: HCl, HNO₃, H₂SO₄.', None),
                ('<b>Weak Acid</b>: Only partially dissociates in water; establishes equilibrium. Example: CH₃COOH (acetic acid).', None),
                ('<b>Strong Base</b>: Completely dissociates in water. Examples: NaOH, KOH, Ca(OH)₂.', None),
                ('<b>Weak Base</b>: Only partially dissociates in water. Example: NH₃ (ammonia).', None),
            ]),
        ],
        'quiz': [
            ('Which of the following is a strong acid?', [('HCl', True), ('CH₃COOH', False), ('H₂CO₃', False), ('HF', False)]),
            ('A weak base in water:', [('Only partially dissociates', True), ('Completely dissociates', False), ('Does not dissociate at all', False), ('Produces H⁺ ions', False)]),
        ],
        'flashcards': [
            ('What is a strong acid?', 'An acid that completely dissociates in water'),
            ('Name three strong acids.', 'HCl, HNO₃, H₂SO₄'),
            ('What is a weak acid?', 'An acid that only partially dissociates in water'),
            ('Give an example of a weak acid.', 'CH₃COOH (acetic acid / vinegar)'),
            ('What is a strong base?', 'A base that completely dissociates in water'),
            ('Name two strong bases.', 'NaOH (sodium hydroxide), KOH (potassium hydroxide)'),
            ('What is a weak base?', 'A base that only partially dissociates in water'),
            ('Give an example of a weak base.', 'NH₃ (ammonia)'),
            ('Does strong/weak refer to concentration?', 'No — it refers to degree of dissociation'),
            ('How many strong acids should you memorize?', 'Six: HCl, HBr, HI, HNO₃, H₂SO₄, HClO₄'),
        ],
    },
    '10.6': {
        'topic': 'Neutralization Reactions',
        'summary': [
            ('Core Definitions', [
                ('<b>Neutralization</b>: A reaction between an acid and a base that produces water and a salt.', None),
                ('<b>General Equation</b>: Acid + Base → Salt + Water (HCl + NaOH → NaCl + H₂O).', None),
                ('<b>Titration</b>: A lab technique to determine the concentration of an acid or base using a neutralization reaction.', None),
                ('<b>Equivalence Point</b>: The point in a titration where moles of acid equal moles of base.', None),
            ]),
        ],
        'quiz': [
            ('What are the products of a neutralization reaction?', [('Salt and water', True), ('Acid and base', False), ('Gas and precipitate', False), ('Only water', False)]),
            ('In a titration, the equivalence point is when:', [('Moles of acid equal moles of base', True), ('pH equals 7', False), ('The indicator stops changing', False), ('Volume of acid equals volume of base', False)]),
        ],
        'flashcards': [
            ('What is a neutralization reaction?', 'A reaction between an acid and a base producing salt and water'),
            ('Acid + Base →', 'Salt + Water'),
            ('What is NaCl in HCl + NaOH → NaCl + H₂O?', 'The salt product'),
            ('What is titration?', 'A technique to find the concentration of an acid or base'),
            ('What is the equivalence point?', 'When moles of acid exactly equal moles of base'),
            ('What is an indicator used for in titration?', 'To signal the endpoint by changing color'),
            ('What is the endpoint of a titration?', 'When the indicator changes color (near equivalence point)'),
            ('What is a burette?', 'Graduated glass tube used to precisely add titrant'),
            ('Is the pH at equivalence always 7?', 'No — it depends on whether the acid/base is strong or weak'),
            ('What is a titrant?', 'The solution of known concentration added from the burette'),
        ],
    },
    '10.7': {
        'topic': 'Naming Salts from Neutralization',
        'summary': [
            ('Core Definitions', [
                ('<b>Salt</b>: An ionic compound formed from the cation of a base and the anion of an acid.', None),
                ('<b>Naming Rule</b>: The cation comes from the base (metal), and the anion comes from the acid.', None),
                ('<b>From Binary Acids</b>: The anion keeps the "-ide" ending. Example: HCl + NaOH → NaCl (sodium chloride).', None),
                ('<b>From Oxyacids</b>: The anion keeps the polyatomic name. Example: HNO₃ + KOH → KNO₃ (potassium nitrate).', None),
            ]),
        ],
        'quiz': [
            ('What salt is formed from HCl and KOH?', [('KCl (potassium chloride)', True), ('NaCl (sodium chloride)', False), ('KNO₃ (potassium nitrate)', False), ('HKCl', False)]),
            ('The cation in a salt comes from the:', [('Base', True), ('Acid', False), ('Water', False), ('Indicator', False)]),
        ],
        'flashcards': [
            ('What is a salt?', 'An ionic compound formed from a neutralization reaction'),
            ('Where does the cation in a salt come from?', 'The base'),
            ('Where does the anion in a salt come from?', 'The acid'),
            ('HCl + NaOH → ?', 'NaCl + H₂O'),
            ('H₂SO₄ + 2KOH → ?', 'K₂SO₄ + 2H₂O'),
            ('What salt forms from HNO₃ + NaOH?', 'NaNO₃ (sodium nitrate)'),
            ('What salt forms from HBr + Ca(OH)₂?', 'CaBr₂ (calcium bromide)'),
            ('How do binary acids affect salt names?', 'Anion ends in -ide (e.g., chloride from HCl)'),
            ('How do oxyacids affect salt names?', 'Anion keeps polyatomic ion name (e.g., sulfate from H₂SO₄)'),
            ('What salt forms from H₃PO₄ + 3NaOH?', 'Na₃PO₄ (sodium phosphate)'),
        ],
    },
    '10.8': {
        'topic': 'Buffer Solutions',
        'summary': [
            ('Core Definitions', [
                ('<b>Buffer</b>: A solution that resists changes in pH when small amounts of acid or base are added.', None),
                ('<b>Composition</b>: Made of a weak acid and its conjugate base, or a weak base and its conjugate acid.', None),
                ('<b>Buffer Capacity</b>: The amount of acid or base a buffer can absorb before pH changes significantly.', None),
                ('<b>Biological Example</b>: Blood is buffered at pH 7.4 by the carbonic acid–bicarbonate system (H₂CO₃/HCO₃⁻).', None),
            ]),
        ],
        'quiz': [
            ('A buffer solution is made of:', [('A weak acid and its conjugate base', True), ('A strong acid and a strong base', False), ('Two strong acids', False), ('Pure water and a salt', False)]),
            ('What does a buffer do?', [('Resists pH changes', True), ('Increases pH', False), ('Neutralizes all acids', False), ('Decreases volume', False)]),
        ],
        'flashcards': [
            ('What is a buffer?', 'A solution that resists changes in pH when small amounts of acid or base are added'),
            ('What are the components of an acidic buffer?', 'A weak acid and its conjugate base'),
            ('What are the components of a basic buffer?', 'A weak base and its conjugate acid'),
            ('Give an example of a buffer system in the body.', 'H₂CO₃/HCO₃⁻ (carbonic acid/bicarbonate) maintains blood pH at 7.4'),
            ('What is buffer capacity?', 'The amount of acid or base a buffer can neutralize before pH changes'),
            ('What is the Henderson-Hasselbalch equation?', 'pH = pKa + log([A⁻]/[HA])'),
            ('Why do buffers work?', 'The weak acid neutralizes added base; the conjugate base neutralizes added acid'),
            ('Can a strong acid/strong base make a buffer?', 'No — buffers require a weak acid or weak base'),
            ('What happens when buffer capacity is exceeded?', 'pH changes dramatically'),
            ('Name a common lab buffer.', 'Acetic acid/sodium acetate (CH₃COOH/CH₃COONa)'),
        ],
    },
    '10.9': {
        'topic': 'pH & pOH Scale',
        'summary': [
            ('Core Definitions', [
                ('<b>pH Scale</b>: Measures hydrogen ion concentration; ranges from 0 (most acidic) to 14 (most basic); 7 is neutral.', None),
                ('<b>pOH</b>: Measures hydroxide ion concentration. pH + pOH = 14 at 25°C.', None),
                ('<b>Acidic Solution</b>: pH < 7 (high [H⁺], low [OH⁻]).', None),
                ('<b>Basic Solution</b>: pH > 7 (low [H⁺], high [OH⁻]).', None),
            ]),
        ],
        'quiz': [
            ('A solution with pH 3 is:', [('Acidic', True), ('Basic', False), ('Neutral', False), ('Cannot be determined', False)]),
            ('If pH = 4, what is pOH?', [('10', True), ('4', False), ('7', False), ('14', False)]),
        ],
        'flashcards': [
            ('What is the pH scale range?', '0 to 14'),
            ('What pH is neutral?', '7'),
            ('Is pH 2 acidic or basic?', 'Acidic'),
            ('Is pH 12 acidic or basic?', 'Basic'),
            ('What is the relationship between pH and pOH?', 'pH + pOH = 14'),
            ('What does a lower pH mean?', 'Higher concentration of H⁺ ions (more acidic)'),
            ('What does a higher pH mean?', 'Higher concentration of OH⁻ ions (more basic)'),
            ('Is the pH scale linear or logarithmic?', 'Logarithmic — each unit is a 10× change'),
            ('A pH change from 3 to 1 is how much more acidic?', '100 times (10² = 100)'),
            ('What is the pH of pure water?', '7'),
        ],
    },
    '10.10': {
        'topic': 'Calculating pH and pOH using Log',
        'summary': [
            ('Core Definitions', [
                ('<b>pH Formula</b>: pH = −log[H⁺], where [H⁺] is the molar concentration of hydrogen ions.', None),
                ('<b>pOH Formula</b>: pOH = −log[OH⁻], where [OH⁻] is the molar concentration of hydroxide ions.', None),
                ('<b>Reverse Calculation</b>: [H⁺] = 10⁻ᵖᴴ and [OH⁻] = 10⁻ᵖᴼᴴ.', None),
                ('<b>Key Relationship</b>: pH + pOH = 14; [H⁺] × [OH⁻] = 1.0 × 10⁻¹⁴ at 25°C.', None),
            ]),
        ],
        'quiz': [
            ('What is the pH of a solution with [H⁺] = 1 × 10⁻⁵ M?', [('5', True), ('9', False), ('10⁻⁵', False), ('-5', False)]),
            ('If pH = 3, what is [H⁺]?', [('1 × 10⁻³ M', True), ('3 M', False), ('1 × 10⁻¹¹ M', False), ('0.3 M', False)]),
        ],
        'flashcards': [
            ('Formula for pH?', 'pH = −log[H⁺]'),
            ('Formula for pOH?', 'pOH = −log[OH⁻]'),
            ('How do you find [H⁺] from pH?', '[H⁺] = 10⁻ᵖᴴ'),
            ('How do you find [OH⁻] from pOH?', '[OH⁻] = 10⁻ᵖᴼᴴ'),
            ('What is Kw?', 'The ion product of water: [H⁺][OH⁻] = 1.0 × 10⁻¹⁴'),
            ('pH + pOH = ?', '14 (at 25°C)'),
            ('What is the pH if [H⁺] = 0.01 M?', '2  (−log(0.01) = 2)'),
            ('What is the pOH if [OH⁻] = 1 × 10⁻⁴ M?', '4'),
            ('If pH = 4, what is pOH?', '10'),
            ('If pH = 4, what is [H⁺]?', '1 × 10⁻⁴ M'),
        ],
    },

    # ── Unit 11: Thermochemistry ──
    '11.1': {
        'topic': 'Heat Conversion',
        'summary': [
            ('Core Definitions', [
                ('<b>Heat (q)</b>: Energy transferred between objects due to a temperature difference, measured in joules (J) or calories (cal).', None),
                ('<b>Joule (J)</b>: The SI unit of energy. 1 calorie = 4.184 joules.', None),
                ('<b>Calorie (cal)</b>: The amount of energy needed to raise 1 g of water by 1°C.', None),
                ('<b>Kilocalorie (kcal)</b>: 1 kcal = 1000 cal = 1 food Calorie (Cal).', None),
            ]),
        ],
        'quiz': [
            ('How many joules are in 1 calorie?', [('4.184 J', True), ('1 J', False), ('100 J', False), ('0.4184 J', False)]),
            ('What is a food Calorie (Cal) equal to?', [('1 kilocalorie', True), ('1 calorie', False), ('1 joule', False), ('1 kilojoule', False)]),
        ],
        'flashcards': [
            ('What is heat?', 'Energy transferred due to a temperature difference'),
            ('What is the SI unit of energy?', 'Joule (J)'),
            ('How many joules in 1 calorie?', '4.184 J'),
            ('How many calories in 1 kilocalorie?', '1000 calories'),
            ('What is a food Calorie?', '1 kilocalorie (1000 cal)'),
            ('Convert 500 cal to joules.', '500 × 4.184 = 2092 J'),
            ('Convert 8368 J to calories.', '8368 ÷ 4.184 = 2000 cal'),
            ('What is a kilojoule (kJ)?', '1000 joules'),
            ('Does heat flow from hot to cold or cold to hot?', 'Hot to cold'),
            ('What is temperature?', 'A measure of the average kinetic energy of particles'),
        ],
    },
    '11.2': {
        'topic': 'Specific Heat',
        'summary': [
            ('Core Definitions', [
                ('<b>Specific Heat (c)</b>: The amount of energy needed to raise 1 gram of a substance by 1°C.', None),
                ('<b>Formula</b>: q = mcΔT, where q = heat, m = mass, c = specific heat, ΔT = change in temperature.', None),
                ('<b>Water\'s Specific Heat</b>: 4.184 J/g°C — very high, which is why water heats and cools slowly.', None),
                ('<b>Units</b>: J/(g·°C) or cal/(g·°C).', None),
            ]),
        ],
        'quiz': [
            ('What is the specific heat formula?', [('q = mcΔT', True), ('PV = nRT', False), ('E = hf', False), ('pH = −log[H⁺]', False)]),
            ('Why does water heat up slowly?', [('It has a very high specific heat', True), ('It is a liquid', False), ('It is made of hydrogen and oxygen', False), ('It is transparent', False)]),
        ],
        'flashcards': [
            ('What is specific heat?', 'The energy needed to raise 1 gram of a substance by 1°C'),
            ('What is the formula for heat?', 'q = mcΔT'),
            ('What does q represent?', 'Heat energy (in joules)'),
            ('What does m represent?', 'Mass (in grams)'),
            ('What does c represent?', 'Specific heat capacity'),
            ('What does ΔT represent?', 'Change in temperature (T_final − T_initial)'),
            ('What is the specific heat of water?', '4.184 J/g°C'),
            ('Which has higher specific heat: water or metal?', 'Water'),
            ('Why is water used as a coolant?', 'Its high specific heat absorbs lots of energy without large temperature change'),
            ('If q is negative, what does that mean?', 'The substance released heat (exothermic)'),
        ],
    },
    '11.3': {
        'topic': 'Heat Capacity',
        'summary': [
            ('Core Definitions', [
                ('<b>Heat Capacity (C)</b>: The amount of heat needed to raise the temperature of an entire object by 1°C.', None),
                ('<b>Difference from Specific Heat</b>: Heat capacity depends on total mass; specific heat is per gram.', None),
                ('<b>Formula</b>: q = CΔT, where C = heat capacity of the object.', None),
                ('<b>Relationship</b>: C = m × c (heat capacity = mass × specific heat).', None),
            ]),
        ],
        'quiz': [
            ('Heat capacity depends on:', [('The mass and type of material', True), ('Only the type of material', False), ('Only the temperature', False), ('Only the volume', False)]),
            ('What is the relationship between heat capacity and specific heat?', [('C = m × c', True), ('C = c / m', False), ('c = C × m', False), ('C = ΔT × q', False)]),
        ],
        'flashcards': [
            ('What is heat capacity?', 'The heat needed to raise the temperature of an entire object by 1°C'),
            ('How does heat capacity differ from specific heat?', 'Heat capacity depends on total mass; specific heat is per gram'),
            ('Formula using heat capacity?', 'q = CΔT'),
            ('How do you calculate heat capacity from specific heat?', 'C = m × c'),
            ('Does a larger object have higher or lower heat capacity?', 'Higher — more mass means more energy needed'),
            ('Units of heat capacity?', 'J/°C'),
            ('Units of specific heat?', 'J/(g·°C)'),
            ('Two pools of different sizes have the same water temperature. Which needs more energy to heat?', 'The larger pool (higher heat capacity)'),
            ('Is specific heat an intensive or extensive property?', 'Intensive (does not depend on amount)'),
            ('Is heat capacity an intensive or extensive property?', 'Extensive (depends on amount/mass)'),
        ],
    },
    '11.4': {
        'topic': 'Calorimetry',
        'summary': [
            ('Core Definitions', [
                ('<b>Calorimetry</b>: The measurement of heat changes during chemical or physical processes.', None),
                ('<b>Calorimeter</b>: A device used to measure heat exchange. A simple version is a coffee-cup calorimeter.', None),
                ('<b>Principle</b>: q_lost = −q_gained. Heat lost by a hot object equals heat gained by a cold object.', None),
                ('<b>Bomb Calorimeter</b>: Used for combustion reactions; measures heat at constant volume.', None),
            ]),
        ],
        'quiz': [
            ('In calorimetry, q_lost by the hot object equals:', [('−q_gained by the cold object', True), ('q_gained by the cold object', False), ('Zero', False), ('Twice q_gained', False)]),
            ('A coffee-cup calorimeter operates at constant:', [('Pressure', True), ('Volume', False), ('Temperature', False), ('Mass', False)]),
        ],
        'flashcards': [
            ('What is calorimetry?', 'The measurement of heat changes in chemical or physical processes'),
            ('What is a calorimeter?', 'A device that measures heat exchange'),
            ('What is a coffee-cup calorimeter?', 'A simple calorimeter using insulated cups at constant pressure'),
            ('What is a bomb calorimeter?', 'A calorimeter for combustion at constant volume'),
            ('What is the key calorimetry principle?', 'q_lost = −q_gained (energy is conserved)'),
            ('If hot metal is placed in cool water, what happens?', 'Metal loses heat; water gains heat until thermal equilibrium'),
            ('What is thermal equilibrium?', 'When two objects reach the same temperature'),
            ('Formula used in calorimetry?', 'q = mcΔT for each substance; then set q_lost = −q_gained'),
            ('What assumption is made in simple calorimetry?', 'No heat is lost to the surroundings'),
            ('Why is water used in calorimeters?', 'Its specific heat is well-known (4.184 J/g°C)'),
        ],
    },
    '11.5': {
        'topic': 'Enthalpy Entropy Free Energy',
        'summary': [
            ('Core Definitions', [
                ('<b>Enthalpy (H)</b>: The total heat content of a system. ΔH < 0 = exothermic; ΔH > 0 = endothermic.', None),
                ('<b>Entropy (S)</b>: A measure of disorder/randomness. ΔS > 0 means disorder increases.', None),
                ('<b>Gibbs Free Energy (G)</b>: ΔG = ΔH − TΔS. If ΔG < 0, the reaction is spontaneous.', None),
                ('<b>Spontaneous Reaction</b>: Occurs without continuous outside energy input (ΔG < 0).', None),
            ]),
        ],
        'quiz': [
            ('A reaction with ΔG < 0 is:', [('Spontaneous', True), ('Non-spontaneous', False), ('At equilibrium', False), ('Impossible', False)]),
            ('An exothermic reaction has:', [('ΔH < 0 (negative)', True), ('ΔH > 0 (positive)', False), ('ΔS = 0', False), ('ΔG = 0', False)]),
        ],
        'flashcards': [
            ('What is enthalpy (H)?', 'The total heat content of a system'),
            ('What does ΔH < 0 mean?', 'Exothermic reaction — heat is released'),
            ('What does ΔH > 0 mean?', 'Endothermic reaction — heat is absorbed'),
            ('What is entropy (S)?', 'A measure of disorder or randomness'),
            ('What does ΔS > 0 mean?', 'Disorder increases'),
            ('What is Gibbs Free Energy?', 'ΔG = ΔH − TΔS; predicts spontaneity'),
            ('When is a reaction spontaneous?', 'When ΔG < 0'),
            ('When is a reaction non-spontaneous?', 'When ΔG > 0'),
            ('When is a reaction at equilibrium?', 'When ΔG = 0'),
            ('Which favors spontaneity: negative ΔH or positive ΔH?', 'Negative ΔH (exothermic)'),
        ],
    },
    '11.6': {
        'topic': "Hess's Law",
        'summary': [
            ('Core Definitions', [
                ("<b>Hess's Law</b>: The total enthalpy change for a reaction is the same regardless of the pathway taken.", None),
                ('<b>Application</b>: Add ΔH values of individual steps to find the overall ΔH of a reaction.', None),
                ('<b>Reversing a Reaction</b>: Changes the sign of ΔH. If forward is −100 kJ, reverse is +100 kJ.', None),
                ('<b>Multiplying a Reaction</b>: Multiply ΔH by the same factor. If doubled, ΔH doubles.', None),
            ]),
        ],
        'quiz': [
            ("Hess's Law states that enthalpy change depends on:", [('Only the initial and final states, not the path', True), ('The number of steps', False), ('The speed of the reaction', False), ('The temperature only', False)]),
            ('If a reaction is reversed, what happens to ΔH?', [('Its sign changes', True), ('It doubles', False), ('It stays the same', False), ('It becomes zero', False)]),
        ],
        'flashcards': [
            ("What is Hess's Law?", 'Total ΔH is the same regardless of the pathway — it depends only on initial and final states'),
            ("Why is Hess's Law useful?", 'It lets us calculate ΔH for reactions that are hard to measure directly'),
            ('If you reverse a reaction, what happens to ΔH?', 'The sign flips (positive ↔ negative)'),
            ('If you multiply a reaction by 2, what happens to ΔH?', 'ΔH is also multiplied by 2'),
            ('What is a state function?', 'A property that depends only on initial and final states, not the path'),
            ('Is enthalpy a state function?', 'Yes'),
            ('What is standard enthalpy of formation (ΔH°f)?', 'The enthalpy change when 1 mole of a compound forms from its elements in standard states'),
            ('What is the ΔH°f of an element in its standard state?', 'Zero'),
            ("How do you use Hess's Law with formation enthalpies?", 'ΔH°rxn = ΣΔH°f(products) − ΣΔH°f(reactants)'),
            ('What is an enthalpy diagram?', 'A diagram showing energy levels of reactants and products with ΔH arrows'),
        ],
    },

    # ── Unit 12: Nuclear Chemistry ──
    '12.1': {
        'topic': 'Nuclear Fusion and Fission',
        'summary': [
            ('Core Definitions', [
                ('<b>Nuclear Fission</b>: The splitting of a heavy nucleus into two lighter nuclei, releasing large amounts of energy.', None),
                ('<b>Nuclear Fusion</b>: The combining of two light nuclei into one heavier nucleus, releasing even more energy.', None),
                ('<b>Chain Reaction</b>: In fission, released neutrons trigger further fission events, sustaining the reaction.', None),
                ('<b>Mass Defect</b>: The difference between the mass of the nucleus and the sum of its individual protons and neutrons — converted to energy via E = mc².', None),
            ]),
        ],
        'quiz': [
            ('Nuclear fusion involves:', [('Combining light nuclei into a heavier one', True), ('Splitting heavy nuclei', False), ('Chemical bonding', False), ('Dissolving radioactive material', False)]),
            ('What powers the Sun?', [('Nuclear fusion', True), ('Nuclear fission', False), ('Combustion', False), ('Chemical reactions', False)]),
        ],
        'flashcards': [
            ('What is nuclear fission?', 'Splitting a heavy nucleus into two lighter nuclei'),
            ('What is nuclear fusion?', 'Combining two light nuclei into one heavier nucleus'),
            ('Which releases more energy: fission or fusion?', 'Fusion'),
            ('What powers the Sun?', 'Nuclear fusion (hydrogen → helium)'),
            ('What is a chain reaction?', 'Neutrons released from fission trigger additional fission events'),
            ('What is used in nuclear power plants?', 'Nuclear fission (usually uranium-235)'),
            ('What is mass defect?', 'The difference between expected and actual nuclear mass'),
            ('How is mass defect related to energy?', 'E = mc² — mass is converted to energy'),
            ('What is critical mass?', 'The minimum amount of fissile material needed to sustain a chain reaction'),
            ('Why is fusion hard to achieve on Earth?', 'It requires extremely high temperatures and pressure'),
        ],
    },
    '12.2': {
        'topic': 'Alpha Beta & Gamma Decay',
        'summary': [
            ('Core Definitions', [
                ('<b>Alpha Decay (α)</b>: Emission of a helium-4 nucleus (²₄He). Atomic number decreases by 2, mass number by 4.', None),
                ('<b>Beta Decay (β)</b>: A neutron converts to a proton and emits an electron (⁰₋₁e). Atomic number increases by 1.', None),
                ('<b>Gamma Decay (γ)</b>: Emission of high-energy electromagnetic radiation. No change in atomic or mass number.', None),
                ('<b>Penetrating Power</b>: α < β < γ. Alpha stopped by paper; beta by aluminum; gamma by lead/concrete.', None),
            ]),
        ],
        'quiz': [
            ('In alpha decay, the atomic number decreases by:', [('2', True), ('1', False), ('4', False), ('0', False)]),
            ('Which type of radiation has the greatest penetrating power?', [('Gamma', True), ('Alpha', False), ('Beta', False), ('They are all equal', False)]),
        ],
        'flashcards': [
            ('What is alpha decay?', 'Emission of a helium-4 nucleus (2 protons + 2 neutrons)'),
            ('What happens to atomic number in alpha decay?', 'Decreases by 2'),
            ('What happens to mass number in alpha decay?', 'Decreases by 4'),
            ('What is beta decay?', 'A neutron becomes a proton; an electron is emitted'),
            ('What happens to atomic number in beta decay?', 'Increases by 1'),
            ('What is gamma decay?', 'Emission of high-energy electromagnetic radiation'),
            ('Does gamma decay change atomic or mass number?', 'No'),
            ('What stops alpha particles?', 'A sheet of paper or skin'),
            ('What stops beta particles?', 'Aluminum foil or thin metal'),
            ('What stops gamma rays?', 'Thick lead or concrete'),
        ],
    },
    '12.3': {
        'topic': 'Nuclear Reactions',
        'summary': [
            ('Core Definitions', [
                ('<b>Nuclear Equation</b>: Shows the parent nucleus, emitted particle, and daughter nucleus. Mass and atomic numbers must balance.', None),
                ('<b>Transmutation</b>: The conversion of one element into another through nuclear reactions.', None),
                ('<b>Balancing Rule</b>: Sum of mass numbers on left = sum on right; sum of atomic numbers on left = sum on right.', None),
                ('<b>Particle Symbols</b>: α = ⁴₂He, β = ⁰₋₁e, γ = ⁰₀γ, neutron = ¹₀n, proton = ¹₁p.', None),
            ]),
        ],
        'quiz': [
            ('In a balanced nuclear equation, what must be conserved?', [('Mass number and atomic number', True), ('Only mass', False), ('Only charge', False), ('Volume and pressure', False)]),
            ('What is transmutation?', [('Changing one element into another via nuclear reaction', True), ('A chemical reaction', False), ('Phase change', False), ('Dissolving a substance', False)]),
        ],
        'flashcards': [
            ('What is a nuclear equation?', 'An equation showing radioactive decay or nuclear reaction with balanced mass and atomic numbers'),
            ('What must be balanced in nuclear equations?', 'Mass numbers and atomic numbers on both sides'),
            ('What is transmutation?', 'Converting one element into another through nuclear reactions'),
            ('What is the symbol for an alpha particle?', '⁴₂He'),
            ('What is the symbol for a beta particle?', '⁰₋₁e'),
            ('What is the symbol for a neutron?', '¹₀n'),
            ('What is the symbol for a proton?', '¹₁p'),
            ('What is a daughter nucleus?', 'The nucleus produced after decay'),
            ('What is a parent nucleus?', 'The original nucleus before decay'),
            ('Who first achieved artificial transmutation?', 'Ernest Rutherford'),
        ],
    },
    '12.4': {
        'topic': 'Half-Life Calculations',
        'summary': [
            ('Core Definitions', [
                ('<b>Half-Life (t½)</b>: The time it takes for half of a radioactive sample to decay.', None),
                ('<b>Formula</b>: Remaining = Original × (½)ⁿ, where n = number of half-lives elapsed.', None),
                ('<b>Finding n</b>: n = total time ÷ half-life.', None),
                ('<b>Key Feature</b>: Half-life is constant — it does not change regardless of the amount of sample.', None),
            ]),
        ],
        'quiz': [
            ('After 3 half-lives, what fraction of a sample remains?', [('1/8', True), ('1/4', False), ('1/2', False), ('1/16', False)]),
            ('If a substance has a half-life of 10 years, how much remains after 30 years from 80 g?', [('10 g', True), ('20 g', False), ('40 g', False), ('5 g', False)]),
        ],
        'flashcards': [
            ('What is half-life?', 'The time for half of a radioactive sample to decay'),
            ('Half-life formula?', 'Remaining = Original × (1/2)^n'),
            ('What is n in the half-life formula?', 'Number of half-lives elapsed (total time ÷ half-life)'),
            ('After 1 half-life, what fraction remains?', '1/2'),
            ('After 2 half-lives, what fraction remains?', '1/4'),
            ('After 4 half-lives, what fraction remains?', '1/16'),
            ('Is half-life affected by temperature or pressure?', 'No — it is constant for each isotope'),
            ('What is carbon-14 dating?', 'Using the half-life of C-14 (5730 years) to date organic materials'),
            ('100 g with t½ = 5 days. How much after 15 days?', '12.5 g (3 half-lives: 100→50→25→12.5)'),
            ('Can half-life be used to determine age of rocks?', 'Yes — using isotopes like uranium-238 or potassium-40'),
        ],
    },
    '12.5': {
        'topic': 'Applications of Nuclear Chemistry',
        'summary': [
            ('Core Definitions', [
                ('<b>Nuclear Power</b>: Fission of uranium-235 heats water to produce steam that drives turbines for electricity.', None),
                ('<b>Medical Uses</b>: Radioisotopes used in imaging (PET scans), cancer treatment (radiation therapy), and tracers.', None),
                ('<b>Carbon Dating</b>: Uses the decay of carbon-14 to determine the age of organic materials up to ~50,000 years.', None),
                ('<b>Food Irradiation</b>: Gamma rays kill bacteria in food to extend shelf life without making food radioactive.', None),
            ]),
        ],
        'quiz': [
            ('Nuclear power plants generate electricity using:', [('Fission of uranium-235', True), ('Fusion of hydrogen', False), ('Combustion of coal', False), ('Chemical batteries', False)]),
            ('Carbon-14 dating is used to determine the age of:', [('Organic materials', True), ('Rocks', False), ('Water', False), ('Metals', False)]),
        ],
        'flashcards': [
            ('How do nuclear power plants generate electricity?', 'Fission of U-235 heats water → steam → drives turbines'),
            ('What fuel is used in most nuclear reactors?', 'Uranium-235'),
            ('What is a PET scan?', 'Positron Emission Tomography — uses radioactive tracers to image body processes'),
            ('How is radiation used in cancer treatment?', 'Targeted radiation kills cancer cells (radiation therapy)'),
            ('What is carbon-14 dating?', 'Using C-14 decay to find the age of organic materials'),
            ('What is the half-life of carbon-14?', '5,730 years'),
            ('What is food irradiation?', 'Using gamma rays to kill bacteria and extend shelf life'),
            ('Does food irradiation make food radioactive?', 'No'),
            ('What is a radioactive tracer?', 'A radioisotope used to track chemical processes in the body or environment'),
            ('What is nuclear waste?', 'Spent fuel and contaminated materials from reactors; remains radioactive for thousands of years'),
        ],
    },
}

# ─── File Updaters ───────────────────────────────────────────────────────────────

def update_summary(filepath, lesson_id, data):
    """Replace placeholder summary with real content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build new summary HTML
    topic = data['topic']
    items = data['summary']
    lines = []
    lines.append(f'<h3>Key Concepts: {topic}</h3>')
    for section_title, bullets in items:
        lines.append(f'<p><b>{section_title}</b></p>')
        lines.append('<ul>')
        for bullet, _ in bullets:
            lines.append(f'<li>{bullet}</li>')
        lines.append('</ul>')
    new_html = '\n'.join(lines)

    # Replace the old summary content between <div class="lesson-notes"> ... </div>
    pattern = r'(<div class="lesson-notes">)\s*.*?\s*(</div>\s*<div class="summary-actions">)'
    replacement = r'\1\n' + new_html + r'\n\2'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


def update_quiz(filepath, lesson_id, data):
    """Replace placeholder quiz questions with real content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    questions = data['quiz']
    # Build quiz HTML
    quiz_html_parts = []
    for i, (question_text, options) in enumerate(questions, 1):
        q_name = f'q{i}'
        q_html = f'''
            <div class="quiz-question" style="margin-bottom: 2rem;" data-attempts="2">
                <p style="font-weight: 700; font-size: 1.45rem; margin-bottom: 1rem;">{i}. {question_text}</p>
'''
        for opt_text, is_correct in options:
            val = 'correct' if is_correct else 'wrong'
            q_html += f'''                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="{q_name}" value="{val}"> {opt_text}
                </label>
'''
        q_html += f'''                <div class="attempts-indicator"></div>
                <div style="margin-top:1.5rem;">
                    <button type="button" class="action-button" onclick="window.checkQuizAnswer('{q_name}', 'correct', this)">Submit Answer</button>
                    <button type="button" class="nav-button" onclick="window.resetQuizQuestion(this)" style="margin-left:0.5rem;">Try Again</button>
                </div>
            </div>'''
        quiz_html_parts.append(q_html)

    new_quiz = '\n'.join(quiz_html_parts)

    # Replace between <form id="quiz-form"> and </form>
    pattern = r'(<form id="quiz-form">)\s*.*?\s*(</form>)'
    replacement = r'\1\n' + new_quiz + r'\n            \n\2'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Fix the "Next Lesson" link
    parts = lesson_id.split('.')
    unit_num = parts[0]
    lesson_num = int(parts[1])
    
    # Get all lessons in this unit
    unit_lessons = sorted([lid for lid in LESSONS.keys() if lid.startswith(unit_num + '.')],
                          key=lambda x: float(x))
    current_idx = unit_lessons.index(lesson_id) if lesson_id in unit_lessons else -1
    
    if current_idx >= 0 and current_idx < len(unit_lessons) - 1:
        next_id = unit_lessons[current_idx + 1]
        next_topic = LESSONS[next_id]['topic']
        next_link = f"Lesson {next_id}_Video.html"
        next_label = f"Next Lesson: {next_id}"
    else:
        # Last lesson in unit — link to chem.html
        next_link = "../../chem.html"
        next_label = "Back to Chemistry"
    
    # Replace the next lesson button
    next_btn_pattern = r"onclick=\"window\.location\.href='[^']*'\">Next Lesson:[^<]*</button>"
    next_btn_replacement = f"onclick=\"window.location.href='{next_link}'\">{next_label}</button>"
    new_content = re.sub(next_btn_pattern, next_btn_replacement, new_content)
    
    # Also fix broken "Lesson 1.2" links
    old_link_pattern = r"onclick=\"window\.location\.href='Lesson 1\.2_Video\.html'\">Next Lesson: 1\.2</button>"
    if re.search(old_link_pattern, new_content):
        new_content = re.sub(old_link_pattern, next_btn_replacement, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


def update_practice(filepath, lesson_id, data):
    """Replace placeholder flashcard data with real content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    flashcards = data['flashcards']
    fc_lines = []
    for i, (q, a) in enumerate(flashcards):
        # Escape quotes
        q_escaped = q.replace("'", "\\'").replace('"', '\\"')
        a_escaped = a.replace("'", "\\'").replace('"', '\\"')
        comma = ',' if i < len(flashcards) - 1 else ''
        fc_lines.append(f'          {{ question: "{q_escaped}", answer: "{a_escaped}" }}{comma}')

    new_fc = '\n'.join(fc_lines)

    # Replace the flashcards array
    pattern = r'(window\.lessonFlashcards = \[)\s*.*?\s*(\];)'
    replacement = r'\1\n' + new_fc + r'\n        \2'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


# ─── Main ────────────────────────────────────────────────────────────────────────

def main():
    total_updated = 0
    total_errors = 0
    
    for lesson_id, data in sorted(LESSONS.items(), key=lambda x: [int(p) for p in x[0].split('.')]):
        unit_num = lesson_id.split('.')[0]
        unit_dir = os.path.join(BASE, f'Unit{unit_num}')
        
        prefix = f'Lesson {lesson_id}'
        
        # Summary
        summary_path = os.path.join(unit_dir, f'{prefix}_Summary.html')
        if os.path.exists(summary_path):
            try:
                if update_summary(summary_path, lesson_id, data):
                    print(f'  ✓ Updated {prefix}_Summary.html')
                    total_updated += 1
                else:
                    print(f'  - No change: {prefix}_Summary.html')
            except Exception as e:
                print(f'  ✗ Error {prefix}_Summary.html: {e}')
                total_errors += 1
        
        # Quiz
        quiz_path = os.path.join(unit_dir, f'{prefix}_Quiz.html')
        if os.path.exists(quiz_path):
            try:
                if update_quiz(quiz_path, lesson_id, data):
                    print(f'  ✓ Updated {prefix}_Quiz.html')
                    total_updated += 1
                else:
                    print(f'  - No change: {prefix}_Quiz.html')
            except Exception as e:
                print(f'  ✗ Error {prefix}_Quiz.html: {e}')
                total_errors += 1
        
        # Practice
        practice_path = os.path.join(unit_dir, f'{prefix}_Practice.html')
        if os.path.exists(practice_path):
            try:
                if update_practice(practice_path, lesson_id, data):
                    print(f'  ✓ Updated {prefix}_Practice.html')
                    total_updated += 1
                else:
                    print(f'  - No change: {prefix}_Practice.html')
            except Exception as e:
                print(f'  ✗ Error {prefix}_Practice.html: {e}')
                total_errors += 1
    
    print(f'\n=== Done: {total_updated} files updated, {total_errors} errors ===')

if __name__ == '__main__':
    main()
