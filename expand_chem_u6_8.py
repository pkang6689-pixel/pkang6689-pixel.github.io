#!/usr/bin/env python3
"""Expand Chemistry Units 6-8 from 7 to 20 quiz questions each."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "chemistry_lessons.json")

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

def add_qs(key, questions):
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

# ── UNIT 6 ──

# U6 L6.1: Synthesis Reactions
add_qs("u6_l6.1", [
    ("A synthesis reaction has the general form:", ["AB -> A + B", "*A + B -> AB", "AB + CD -> AD + CB", "A + BC -> AC + B"], "Two or more substances combine to form one product."),
    ("Which is a synthesis reaction?", ["2H2O -> 2H2 + O2", "*2Na + Cl2 -> 2NaCl", "Zn + CuSO4 -> ZnSO4 + Cu", "NaOH + HCl -> NaCl + H2O"], "Two elements combine to form a compound."),
    ("Rust formation (4Fe + 3O2 -> 2Fe2O3) is a:", ["Decomposition", "*Synthesis (elements combine into a compound)", "Single replacement", "Double replacement"], "Iron and oxygen combine."),
    ("In a synthesis reaction, the number of products is:", ["Two", "Three", "*One (a single, more complex product)", "Variable"], "Always forms one product."),
    ("2Mg + O2 -> 2MgO is synthesis because:", ["One reactant breaks apart", "*Two elements combine into one compound", "A catalyst is needed", "An acid reacts with a base"], "Metal + nonmetal = ionic compound."),
    ("Which elements commonly form synthesis reactions with oxygen?", ["Noble gases", "*Most metals and some nonmetals (forming oxides)", "Only halogens", "Only hydrogen"], "Many elements react with O2."),
    ("SO3 + H2O -> H2SO4 is a synthesis of:", ["An element", "A metal", "*An acid (sulfuric acid) from an oxide and water", "A base"], "Nonmetal oxide + water = acid."),
    ("CaO + H2O -> Ca(OH)2 is synthesis of:", ["An acid", "*A base (calcium hydroxide)", "A salt", "An element"], "Metal oxide + water = base."),
    ("Synthesis reactions are generally _____ (energy-wise).", ["Endothermic", "*Exothermic (release energy as new bonds form)", "Energy-neutral", "Nuclear"], "Forming bonds releases energy."),
    ("N2 + 3H2 -> 2NH3 (Haber process) is:", ["Decomposition", "*Synthesis (elements combine to form ammonia)", "Combustion", "Neutralization"], "Industrial synthesis of ammonia."),
    ("Direct combination is another name for:", ["Decomposition", "*Synthesis reaction", "Combustion", "Neutralization"], "Same type of reaction."),
    ("Which is NOT a synthesis reaction?", ["H2 + Cl2 -> 2HCl", "2K + Br2 -> 2KBr", "*CaCO3 -> CaO + CO2 (this is decomposition)", "C + O2 -> CO2"], "Breaking one compound into two = decomposition."),
    ("Predicting products of synthesis: what forms when Li reacts with O2?", ["LiO", "*Li2O (lithium oxide)", "LiO2", "Li2O2"], "Lithium forms Li+ ions; formula balances as Li2O."),
])

# U6 L6.2: Combustion Reactions
add_qs("u6_l6.2", [
    ("Complete combustion of a hydrocarbon produces:", ["CO + H2", "*CO2 + H2O", "C + H2O", "CO + H2O"], "Full oxidation yields carbon dioxide and water."),
    ("Incomplete combustion produces _____ instead of CO2.", ["O2", "*CO (carbon monoxide, a toxic gas) and/or soot (C)", "H2", "N2"], "Insufficient oxygen leads to incomplete products."),
    ("The general equation for combustion of CxHy is:", ["CxHy -> C + H2", "CxHy + H2O -> CO2", "*CxHy + O2 -> CO2 + H2O", "CxHy -> CO2 + H2"], "Hydrocarbon + oxygen."),
    ("Combustion always requires:", ["Water", "A catalyst", "*Oxygen (O2)", "Nitrogen"], "O2 is the oxidizer."),
    ("Which is a combustion reaction?", ["NaOH + HCl -> NaCl + H2O", "*CH4 + 2O2 -> CO2 + 2H2O", "Zn + CuSO4 -> ZnSO4 + Cu", "2H2O -> 2H2 + O2"], "Methane burning with oxygen."),
    ("The combustion of propane (C3H8) produces:", ["3C + 4H2", "*3CO2 + 4H2O", "C3H8O", "3CO + 4H2O"], "C3H8 + 5O2 -> 3CO2 + 4H2O."),
    ("Combustion reactions are always:", ["Endothermic", "*Exothermic (they release heat and light)", "Energy-neutral", "Slow"], "Burning releases energy."),
    ("The fire triangle requires fuel, heat, and:", ["Water", "Nitrogen", "*Oxygen", "Carbon"], "Three components needed for fire."),
    ("Carbon monoxide from incomplete combustion is dangerous because:", ["It smells bad", "*It binds to hemoglobin more strongly than O2, preventing oxygen transport in blood", "It is acidic", "It is visible"], "CO is odorless and binds irreversibly to hemoglobin."),
    ("Balancing C2H6 + O2: how many O2 molecules are needed?", ["2", "5", "*7/2 (or 7 with coefficient 2 for C2H6)", "3"], "2C2H6 + 7O2 -> 4CO2 + 6H2O (multiply by 2 to avoid fractions)."),
    ("Oxyacetylene torches burn C2H2 (acetylene) because:", ["It's cheap", "*The combustion produces extremely high temperatures (~3300 degrees C)", "It's safe", "It produces no CO2"], "Acetylene burns very hot."),
    ("Spontaneous combustion can occur when:", ["There's no oxygen", "*Heat builds up in a material (like oily rags) faster than it dissipates, reaching ignition temperature", "Temperature is below 0 degrees C", "In a vacuum"], "Self-heating can reach ignition point."),
    ("Cellular respiration (C6H12O6 + 6O2 -> 6CO2 + 6H2O) is similar to:", ["Synthesis", "Decomposition", "*Combustion (slow, controlled 'burning' of glucose)", "Neutralization"], "Same products as combustion, but controlled by enzymes."),
])

# U6 L6.3: Oxidation-Reduction (Redox)
add_qs("u6_l6.3", [
    ("Oxidation is defined as:", ["Gaining electrons", "*Losing electrons (increase in oxidation number)", "Gaining protons", "Losing protons"], "OIL: Oxidation Is Loss."),
    ("Reduction is defined as:", ["Losing electrons", "*Gaining electrons (decrease in oxidation number)", "Gaining protons", "Gaining oxygen"], "RIG: Reduction Is Gain."),
    ("The reducing agent is the substance that:", ["Gets reduced", "*Gets oxidized (it donates electrons, reducing the other substance)", "Gains electrons", "Stays unchanged"], "Reducing agent = electron donor."),
    ("The oxidizing agent is the substance that:", ["Gets oxidized", "*Gets reduced (it accepts electrons, oxidizing the other substance)", "Loses electrons", "Stays unchanged"], "Oxidizing agent = electron acceptor."),
    ("In 2Na + Cl2 -> 2NaCl, sodium is:", ["Reduced", "*Oxidized (Na -> Na+, loses an electron)", "Unchanged", "A catalyst"], "Na goes from 0 to +1."),
    ("In the same reaction, chlorine is:", ["Oxidized", "*Reduced (Cl2 -> 2Cl-, gains electrons)", "Unchanged", "A catalyst"], "Cl goes from 0 to -1."),
    ("Oxidation numbers help track:", ["Mass changes", "*Electron transfer in redox reactions", "Temperature", "Volume"], "Bookkeeping for electrons."),
    ("The oxidation number of a free element is:", ["1", "-1", "*0", "Variable"], "Uncombined elements have oxidation number 0."),
    ("An element in its elemental form (like O2, Fe, N2) has oxidation state:", ["Depends on the element", "*0 (always zero for free elements)", "+1", "-1"], "No charge transfer in pure elements."),
    ("Corrosion of metals is a _____ process.", ["Synthesis only", "*Redox (metal is oxidized; oxygen is reduced)", "Acid-base", "Nuclear"], "Metal loses electrons to oxygen/water."),
    ("In photosynthesis, water is _____ and CO2 is _____.", ["Reduced; oxidized", "*Oxidized; reduced (water loses electrons to split; CO2 gains them to form glucose)", "Both oxidized", "Both reduced"], "H2O is the electron source."),
    ("Electrochemistry (batteries, electrolysis) is based on:", ["Acid-base chemistry", "*Redox reactions (electron transfer between electrodes)", "Nuclear reactions", "Phase changes"], "Batteries convert chemical to electrical energy via redox."),
    ("A half-reaction shows:", ["The complete reaction", "*Only the oxidation OR only the reduction part separately", "Only the products", "Only the reactants"], "Separates the two electron-transfer processes."),
])

# U6 L6.4: Activation Energy
add_qs("u6_l6.4", [
    ("Activation energy (Ea) is the minimum energy needed to:", ["End a reaction", "*Start a chemical reaction (break initial bonds to begin the process)", "Cool a reaction", "Measure a reaction"], "Energy barrier for reaction initiation."),
    ("On an energy diagram, activation energy is the:", ["Lowest point", "*Height of the energy barrier from reactants to the transition state (peak)", "Final energy", "Total energy released"], "Energy hill between reactants and products."),
    ("A catalyst lowers the activation energy by:", ["Adding more reactant", "*Providing an alternative reaction pathway with a lower energy barrier", "Increasing temperature", "Removing products"], "Different path, lower Ea."),
    ("Enzymes are _____ catalysts found in living organisms.", ["Inorganic", "*Biological (protein-based)", "Non-functional", "Synthetic only"], "Enzymes speed up biochemical reactions."),
    ("Without sufficient activation energy, a reaction will:", ["Proceed quickly", "*Not proceed (reactants remain unchanged)", "Produce more energy", "Reverse"], "Energy barrier must be overcome."),
    ("Striking a match provides activation energy through:", ["Chemical addition", "*Friction (converting mechanical energy to heat)", "Electrical energy", "Light energy"], "Heat from friction ignites the match."),
    ("The transition state (activated complex) is:", ["A stable product", "*A temporary, high-energy, unstable arrangement of atoms at the top of the energy barrier", "A catalyst", "A reactant"], "Exists only momentarily at the peak."),
    ("For an exothermic reaction, the energy of products is _____ the energy of reactants.", ["Higher than", "*Lower than (energy is released to surroundings)", "Equal to", "Unrelated to"], "Products are more stable (lower energy)."),
    ("For an endothermic reaction, the energy of products is _____ the energy of reactants.", ["Lower than", "*Higher than (energy is absorbed from surroundings)", "Equal to", "Unrelated to"], "Products are less stable (higher energy)."),
    ("Catalysts are NOT consumed in the reaction and can be:", ["Used only once", "*Reused repeatedly (they are regenerated at the end of each reaction cycle)", "Destroyed after use", "Added to products"], "Catalyst returns to original form."),
    ("A reaction with LOW activation energy is likely to be:", ["Very slow", "*Fast (easier for molecules to overcome the energy barrier)", "Impossible", "Endothermic always"], "Lower barrier = faster reaction."),
    ("The Arrhenius equation relates reaction rate to:", ["Mass", "Volume", "*Temperature and activation energy (k = Ae^(-Ea/RT))", "Pressure only"], "Mathematical relationship between rate, T, and Ea."),
    ("Inhibitors _____ activation energy, _____ the reaction.", ["Lower; speeding up", "*Raise; slowing down (or increase the effective energy barrier)", "Don't affect; changing", "Remove; stopping"], "Inhibitors oppose catalysts."),
])

# U6 L6.5: Balancing Chemical Equations
add_qs("u6_l6.5", [
    ("A balanced equation has equal numbers of _____ on both sides.", ["Molecules", "*Atoms of each element", "Products", "Electrons only"], "Conservation of mass requires equal atoms."),
    ("Coefficients in a balanced equation represent:", ["Masses directly", "*Mole ratios (and molecule ratios) of reactants and products", "Temperatures", "Energies"], "Coefficients give mole proportions."),
    ("To balance: __Fe + __O2 -> __Fe2O3, the coefficients are:", ["1, 1, 1", "2, 3, 1", "*4, 3, 2", "3, 2, 1"], "4Fe + 3O2 -> 2Fe2O3 (4 Fe, 6 O each side)."),
    ("You should NEVER change _____ to balance an equation.", ["Coefficients", "*Subscripts (changing subscripts changes the chemical identity of the substance)", "Phases", "States"], "Subscripts = chemical formula; don't alter."),
    ("What does (aq) mean in a chemical equation?", ["Gaseous", "*Dissolved in water (aqueous solution)", "Pure liquid", "Solid"], "Aqueous = dissolved."),
    ("The state symbols are:", ["Only (s) and (l)", "*s (solid), l (liquid), g (gas), aq (aqueous)", "Only (g) and (s)", "Not used"], "Four state symbols."),
    ("Balance: __C3H8 + __O2 -> __CO2 + __H2O", ["1, 3, 3, 4", "*1, 5, 3, 4", "1, 5, 3, 8", "2, 5, 3, 4"], "C3H8 + 5O2 -> 3CO2 + 4H2O."),
    ("Balance: __Al + __HCl -> __AlCl3 + __H2", ["1, 1, 1, 1", "1, 3, 1, 1", "*2, 6, 2, 3", "2, 3, 2, 3"], "2Al + 6HCl -> 2AlCl3 + 3H2."),
    ("A skeleton equation is:", ["A balanced equation", "*An unbalanced equation showing reactants and products but without correct coefficients", "A decomposition equation", "A nuclear equation"], "Starting point before balancing."),
    ("The law behind balancing equations is:", ["Conservation of energy", "*Conservation of mass (atoms are neither created nor destroyed)", "Hess's law", "Avogadro's law"], "Mass is conserved in chemical reactions."),
    ("When balancing, it's often best to start with:", ["Oxygen", "*The most complex molecule (or elements appearing in only one reactant and one product)", "Hydrogen", "Any element"], "Save elements in multiple compounds for last."),
    ("In the equation 2H2 + O2 -> 2H2O, the coefficient 2 before H2O means:", ["2 grams of water", "2 atoms of water", "*2 moles (or molecules) of water are produced", "Water is doubled in mass"], "Coefficients = mole/molecule ratios."),
    ("A balanced equation allows calculation of:", ["Only masses", "Only moles", "*Mole ratios, mass ratios, and volume ratios (stoichiometry) between any species", "Nothing quantitative"], "Foundation of stoichiometry."),
])

# U6 L6.6: Temperature and Reaction Rate
add_qs("u6_l6.6", [
    ("Increasing temperature increases reaction rate because:", ["It adds more reactants", "*Particles move faster, collide more often and with greater energy (exceeding Ea more frequently)", "It acts as a catalyst", "It changes the products"], "Higher kinetic energy = more effective collisions."),
    ("The general rule: a 10 degrees C rise approximately _____ the reaction rate.", ["Halves", "*Doubles (rough approximation)", "Triples", "Has no effect"], "Common rule of thumb."),
    ("Collision theory states reactions occur when particles:", ["Are near each other", "*Collide with sufficient energy AND correct orientation", "Simply exist", "Are heated"], "Effective collisions require both energy and orientation."),
    ("Increasing concentration increases rate because:", ["Products increase", "*More particles in a given volume leads to more frequent collisions", "Temperature rises", "Activation energy drops"], "More reactant particles = more collisions."),
    ("Surface area affects reaction rate: a powder reacts _____ than a solid chunk.", ["Slower", "*Faster (more surface exposed for collisions with other reactants)", "At the same rate", "Not at all"], "Greater surface area = more contact."),
    ("At very low temperatures, most reactions:", ["Speed up", "*Slow down or stop (particles lack energy to overcome activation energy)", "Stay the same", "Reverse"], "Insufficient kinetic energy."),
    ("Food spoilage slows in a refrigerator because:", ["Bacteria die", "*Lower temperature slows chemical and biological reaction rates", "Oxygen is removed", "Light is blocked"], "Cold reduces reaction rates."),
    ("Maxwell-Boltzmann distribution shows that at higher temperatures:", ["Fewer particles have high energy", "*A larger fraction of particles have energy exceeding Ea", "All particles have the same energy", "Energy decreases"], "The distribution shifts to higher energies."),
    ("Which factor does NOT affect reaction rate?", ["Temperature", "Concentration", "*The color of the container (has no chemical effect)", "Presence of catalyst"], "Container color is irrelevant."),
    ("Pressure affects the rate of _____ reactions.", ["Only solid", "Only liquid", "*Gaseous (higher pressure = higher concentration of gas molecules)", "No"], "Compression increases gas concentration."),
    ("Nature of reactants affects rate: ionic compounds in solution react _____ than covalent compounds.", ["Slower", "*Faster (ions are already dissociated and can recombine quickly)", "At the same rate", "Not at all"], "Ion rearrangement is fast."),
    ("Glow sticks glow longer in cold water because:", ["They absorb more light", "*Lower temperature slows the chemiluminescent reaction", "Cold water is denser", "They produce more energy"], "Temperature-dependent reaction rate."),
    ("The rate constant (k) in a rate law _____ with increasing temperature.", ["Decreases", "*Increases (exponentially, per the Arrhenius equation)", "Stays constant", "Becomes zero"], "Higher T = larger k = faster reaction."),
])

# U6 L6.7: Chemical Equilibrium
add_qs("u6_l6.7", [
    ("Chemical equilibrium occurs when:", ["Reactions stop", "*The forward and reverse reaction rates are equal (no net change in concentrations)", "All reactants are consumed", "Temperature reaches zero"], "Dynamic equilibrium: both directions proceed equally."),
    ("At equilibrium, concentrations of reactants and products:", ["Are always equal", "Are zero", "*Remain constant (but not necessarily equal to each other)", "Continuously change"], "Constant but not necessarily the same."),
    ("The equilibrium constant (K) expression for aA + bB <=> cC + dD is:", ["K = [A][B]/[C][D]", "*K = [C]^c[D]^d / [A]^a[B]^b", "K = (a+b)/(c+d)", "K = [A]+[B]/[C]+[D]"], "Products over reactants, raised to stoichiometric powers."),
    ("If K >> 1, the equilibrium favors:", ["Reactants", "*Products (high product concentrations at equilibrium)", "Neither", "Cannot tell"], "Large K = mostly products."),
    ("If K << 1, the equilibrium favors:", ["Products", "*Reactants (low product concentrations at equilibrium)", "Neither", "Cannot tell"], "Small K = mostly reactants."),
    ("Le Chatelier's principle states that if a system at equilibrium is disturbed:", ["It stays the same", "*It shifts to partially counteract the disturbance and re-establish equilibrium", "It stops reacting", "It explodes"], "System opposes the change."),
    ("Adding more reactant to a system at equilibrium shifts it:", ["Left (toward reactants)", "*Right (toward products, to consume the added reactant)", "No change", "To a new reaction"], "System shifts to use up the excess."),
    ("Increasing temperature shifts an exothermic equilibrium:", ["Right", "*Left (toward reactants, to absorb the added heat)", "No change", "Both ways"], "System opposes added heat."),
    ("Increasing temperature shifts an endothermic equilibrium:", ["Left", "*Right (toward products, to absorb the added heat)", "No change", "Both ways"], "System uses heat by favoring endothermic direction."),
    ("A catalyst affects equilibrium by:", ["Shifting it right", "Shifting it left", "*Speeding up both forward and reverse rates equally (equilibrium reached faster but K unchanged)", "Changing K"], "Catalyst does not change K or equilibrium position."),
    ("Removing a product from an equilibrium system shifts it:", ["Left", "*Right (to replace the removed product)", "No change", "Down"], "System produces more product."),
    ("Changing pressure affects equilibria involving:", ["Solids only", "Liquids only", "*Gases (shifts toward the side with fewer moles of gas when pressure increases)", "All phases equally"], "Pressure changes affect gas-phase equilibria."),
    ("N2 + 3H2 <=> 2NH3: increasing pressure favors:", ["Reactants (4 moles gas)", "*Products (2 moles gas vs. 4 moles reactant gas)", "Neither", "Decomposition"], "Fewer moles of gas on product side."),
])

# ── UNIT 7 ──

# U7 L7.1: Chemical Formulas & Naming
add_qs("u7_l7.1", [
    ("An empirical formula shows:", ["Exact number of atoms", "*The simplest whole-number ratio of atoms in a compound", "Only the elements present", "The 3D structure"], "Simplest ratio (e.g., CH2O for glucose)."),
    ("A molecular formula shows:", ["The simplest ratio", "*The actual number of each type of atom in one molecule", "Only metals", "Only nonmetals"], "Glucose: C6H12O6 is molecular."),
    ("The formula for sodium chloride is:", ["NaCl2", "*NaCl", "Na2Cl", "SoCl"], "1:1 ratio of Na+ and Cl-."),
    ("In ionic compounds, the _____ is named first.", ["Anion", "*Cation (positive ion, usually the metal)", "Larger ion", "Nonmetal"], "Metal name first, then nonmetal with -ide."),
    ("The name of MgBr2 is:", ["Magnesium bromite", "*Magnesium bromide", "Magnesium dibromide", "Magnesium bromine"], "Mg = magnesium; Br^- = bromide."),
    ("For transition metals with multiple charges, Roman numerals indicate:", ["The group number", "*The charge of the metal ion", "The number of atoms", "The mass"], "FeCl2 = iron(II) chloride; FeCl3 = iron(III) chloride."),
    ("The name of CuO is:", ["Copper oxide", "*Copper(II) oxide (Cu has +2 charge here)", "Cuprous oxide", "Copper monoxide"], "Cu must be +2 to balance O^2-."),
    ("Binary molecular compounds use prefixes like:", ["Only mono-", "*Mono-, di-, tri-, tetra-, penta-, hexa-, etc.", "Only -ide suffix", "Roman numerals"], "Prefixes indicate number of atoms in covalent compounds."),
    ("N2O5 is named:", ["Nitrogen oxide", "Dinitrogen oxide", "*Dinitrogen pentoxide", "Nitrogen(V) oxide"], "2 nitrogen = di-; 5 oxygen = pent- + oxide."),
    ("The formula for aluminum sulfate is:", ["AlSO4", "Al2(SO4)", "*Al2(SO4)3", "Al3(SO4)2"], "Al^3+ and SO4^2-: need 2 Al and 3 SO4 to balance."),
    ("Parentheses in a formula mean:", ["Atoms are separate", "*The entire polyatomic group inside is multiplied by the subscript outside", "It's an acid", "It's a gas"], "Ca(OH)2 means 2 OH groups."),
    ("Hydrates have _____ incorporated into their crystal structure.", ["Acids", "Bases", "*Water molecules", "Ions only"], "CuSO4·5H2O = copper(II) sulfate pentahydrate."),
    ("-ide suffix indicates:", ["A polyatomic ion", "*A monatomic anion (in binary compounds)", "An acid", "A base"], "Chloride, bromide, oxide, etc."),
])

# U7 L7.2: Molar Mass
add_qs("u7_l7.2", [
    ("Molar mass is the mass of:", ["One atom", "*One mole of a substance (in grams per mole)", "One molecule", "One electron"], "Mass of 6.022 x 10^23 particles."),
    ("The molar mass of water (H2O) is approximately:", ["16 g/mol", "*18 g/mol (2(1) + 16)", "20 g/mol", "36 g/mol"], "2 hydrogen + 1 oxygen."),
    ("The molar mass of NaCl is:", ["35.5 g/mol", "*58.5 g/mol (23 + 35.5)", "23 g/mol", "70 g/mol"], "Na (23) + Cl (35.5)."),
    ("To find molar mass of a compound, you:", ["Add atomic numbers", "*Add the atomic masses of all atoms in the formula", "Multiply the formula by Avogadro's number", "Divide by atomic number"], "Sum of all atomic masses."),
    ("The molar mass of CO2 is:", ["28 g/mol", "*44 g/mol (12 + 2(16))", "32 g/mol", "60 g/mol"], "C (12) + 2 O (32) = 44."),
    ("The molar mass of Ca(OH)2 is:", ["57 g/mol", "*74 g/mol (40 + 2(16+1))", "58 g/mol", "90 g/mol"], "Ca(40) + 2×O(16) + 2×H(1) = 74."),
    ("Molar mass has units of:", ["g", "mol", "*g/mol", "g/L"], "Grams per mole."),
    ("The molar mass of glucose (C6H12O6) is:", ["100 g/mol", "*180 g/mol (6(12)+12(1)+6(16))", "162 g/mol", "200 g/mol"], "72 + 12 + 96 = 180."),
    ("To convert grams to moles, divide by:", ["Avogadro's number", "*Molar mass", "Density", "Volume"], "moles = grams / molar mass."),
    ("The molar mass of sulfuric acid (H2SO4) is:", ["80 g/mol", "96 g/mol", "*98 g/mol (2(1)+32+4(16))", "100 g/mol"], "2 + 32 + 64 = 98."),
    ("Which has a larger molar mass: O2 or N2?", ["N2", "*O2 (32 g/mol vs. 28 g/mol)", "They are equal", "Cannot determine"], "O2: 2(16)=32; N2: 2(14)=28."),
    ("Molar mass is numerically equal to:", ["Atomic number", "*Atomic/formula mass in amu (but with g/mol units)", "Density", "Avogadro's number"], "Same number, different units."),
    ("For mixtures, _____ molar mass is the weighted average.", ["Exact", "*Average (or apparent)", "Rounded", "Minimum"], "Used for gas mixtures like air."),
])

# U7 L7.3: Avogadro's Number
add_qs("u7_l7.3", [
    ("Avogadro's number is approximately:", ["6.02 x 10^22", "*6.022 x 10^23", "6.02 x 10^24", "3.01 x 10^23"], "The number of particles in one mole."),
    ("One mole of ANY substance contains:", ["The same mass", "The same volume", "*The same number of particles (6.022 x 10^23)", "The same density"], "Definition of a mole."),
    ("How many molecules are in 2 moles of water?", ["6.022 x 10^23", "*1.2044 x 10^24 (2 x 6.022 x 10^23)", "3.011 x 10^23", "12.044 x 10^24"], "Multiply moles by Avogadro's number."),
    ("How many moles are represented by 3.011 x 10^23 atoms?", ["1 mol", "*0.5 mol (3.011 x 10^23 / 6.022 x 10^23)", "2 mol", "0.25 mol"], "Divide by Avogadro's number."),
    ("The mole is the SI unit for:", ["Mass", "Volume", "Energy", "*Amount of substance"], "One of the seven SI base units."),
    ("At STP, one mole of any ideal gas occupies:", ["11.2 L", "*22.4 L (molar volume at STP)", "44.8 L", "1 L"], "Standard temperature and pressure."),
    ("One mole of carbon-12 has a mass of exactly:", ["6 g", "*12 g (by definition of the mole)", "24 g", "1 g"], "The basis for the mole definition."),
    ("How many atoms are in 1 mole of O2?", ["6.022 x 10^23", "*1.2044 x 10^24 (each molecule has 2 atoms)", "3.011 x 10^23", "6.022 x 10^24"], "1 mol O2 = 6.022e23 molecules x 2 atoms each."),
    ("If you have 18 g of water, you have _____ molecules.", ["1", "*Approximately 6.022 x 10^23 (18 g / 18 g/mol = 1 mol)", "18", "100"], "18 g = 1 mol of water."),
    ("Avogadro's number connects:", ["Mass and volume", "Energy and temperature", "*Microscopic particles to macroscopic amounts (moles)", "Pressure and volume"], "Bridge between atomic and lab scale."),
    ("How many formula units are in 1 mol of NaCl?", ["23", "58.5", "1", "*6.022 x 10^23"], "1 mole = Avogadro's number of formula units."),
    ("The term 'mole' comes from:", ["An animal", "*German 'Molekul' (molecule), meaning a quantity of substance", "A unit of energy", "Latin for 'mass'"], "Historical naming."),
    ("1 mmol (millimole) = _____ of a mole.", ["1/100", "*1/1000 (or 10^-3 mol)", "1/10", "1/1,000,000"], "Milli = 10^-3."),
])

# U7 L7.4: Gram-to-Mole Conversions
add_qs("u7_l7.4", [
    ("To convert grams to moles: moles = grams / _____.", ["Avogadro's number", "*Molar mass (g/mol)", "Density", "Volume"], "grams / (g/mol) = mol."),
    ("How many moles are in 40 g of NaOH (MM = 40 g/mol)?", ["0.5 mol", "*1 mol (40/40)", "2 mol", "40 mol"], "40 g / 40 g/mol = 1.0 mol."),
    ("How many grams are in 0.5 mol of H2O (MM = 18 g/mol)?", ["18 g", "*9 g (0.5 x 18)", "36 g", "0.5 g"], "mass = moles x molar mass."),
    ("How many moles are in 100 g of CaCO3 (MM = 100 g/mol)?", ["0.5 mol", "*1 mol (100/100)", "2 mol", "100 mol"], "100/100 = 1.0 mol."),
    ("Convert 5.0 mol of CO2 to grams (MM = 44 g/mol):", ["44 g", "88 g", "*220 g (5.0 x 44)", "22 g"], "moles x molar mass = grams."),
    ("A three-step conversion: 36 g of C -> moles -> molecules -> atoms:", ["6.022 x 10^23 atoms", "*1.807 x 10^24 atoms (36/12 = 3 mol, x 6.022e23 = 1.807e24 atoms)", "3 x 10^23 atoms", "36 atoms"], "36g/12g/mol = 3 mol x 6.022e23 = 1.807e24 atoms."),
    ("How many grams of KOH are in 0.25 mol? (K=39, O=16, H=1)", ["14 g", "28 g", "*14 g (MM=56, 0.25 x 56 = 14)", "56 g"], "KOH MM = 39+16+1 = 56; 0.25 x 56 = 14 g."),
    ("Convert 3.011 x 10^23 molecules of CO2 to grams:", ["44 g", "*22 g (0.5 mol x 44 g/mol)", "88 g", "11 g"], "3.011e23 / 6.022e23 = 0.5 mol; 0.5 x 44 = 22 g."),
    ("The mole roadmap connects: grams <-> moles <-> _____.", ["Liters only", "Temperature", "*Number of particles (atoms, molecules, or formula units)", "Pressure"], "Three key quantities connected through moles."),
    ("At STP, how many liters does 2 mol of O2 occupy?", ["22.4 L", "*44.8 L (2 x 22.4)", "11.2 L", "2 L"], "2 mol x 22.4 L/mol = 44.8 L."),
    ("What is the mass of 1.204 x 10^24 molecules of H2O?", ["18 g", "*36 g (2 mol x 18 g/mol)", "9 g", "54 g"], "1.204e24 / 6.022e23 = 2 mol; 2 x 18 = 36 g."),
    ("Percent composition by mass = (mass of element / molar mass of compound) x _____.", ["10", "*100", "1000", "Avogadro's number"], "Express as percentage."),
    ("The percent of oxygen in H2O is:", ["11%", "16%", "*89% (16/18 x 100)", "50%"], "Oxygen contributes 16 of 18 g/mol."),
])

# U7 L7.5: Empirical Formulas
add_qs("u7_l7.5", [
    ("An empirical formula represents:", ["The exact molecular structure", "*The simplest whole-number ratio of elements in a compound", "Only the most abundant element", "The 3D shape"], "Lowest ratio."),
    ("The empirical formula of C6H12O6 is:", ["C6H12O6", "*CH2O (divide all subscripts by 6)", "C3H6O3", "CHO"], "Simplest ratio: 1:2:1."),
    ("To determine an empirical formula from percent composition, first:", ["Find the molecular formula", "Measure density", "*Convert percentages to grams (assume 100 g sample), then to moles", "Count atoms"], "100 g sample makes percentages equal grams."),
    ("After converting to moles, the next step is:", ["Add all moles", "*Divide each by the smallest number of moles to get the mole ratio", "Multiply by molar mass", "Convert to grams"], "Get the simplest ratio."),
    ("If the mole ratio is 1:1.5:1, you should:", ["Round down", "Leave as is", "*Multiply all values by 2 to get whole numbers (2:3:2)", "Divide by 2"], "Must be whole numbers."),
    ("A compound is 40.0% C, 6.7% H, and 53.3% O. The empirical formula is:", ["C2H4O2", "*CH2O (from moles: 3.33C : 6.7H : 3.33O = 1:2:1)", "CHO", "C3H6O3"], "Mole ratio C:H:O = 1:2:1."),
    ("To determine a molecular formula from an empirical formula, you also need:", ["The color", "The phase", "*The molar mass of the actual compound", "The density"], "n = molecular mass / empirical mass."),
    ("If the empirical formula is CH2O (MM=30) and the molecular mass is 180 g/mol:", ["Molecular formula = CH2O", "*Molecular formula = C6H12O6 (180/30 = 6, multiply subscripts by 6)", "Molecular formula = C3H6O3", "Cannot determine"], "Multiplier = 180/30 = 6."),
    ("Combustion analysis determines empirical formulas by:", ["Weighing reactants", "*Measuring CO2 and H2O produced (to find mass of C and H in the sample)", "Calculating volume", "Measuring temperature"], "Carbon in CO2, hydrogen in H2O."),
    ("A compound containing only C, H, and O has its oxygen determined by:", ["Direct measurement always", "*Subtracting C and H masses from total mass (oxygen is found by difference)", "Combustion of oxygen", "Titration"], "O = sample mass - C mass - H mass."),
    ("The empirical formula of a compound with 1.0 mol Na, 1.0 mol S, and 2.0 mol O is:", ["NaSO", "Na2SO4", "*NaSO2 (1:1:2 ratio)", "Na2S2O4"], "Direct mole ratio: 1:1:2."),
    ("If the mole ratio gives Fe:O = 2:3, the empirical formula is:", ["FeO", "FeO3", "*Fe2O3", "Fe3O2"], "Directly from the ratio."),
    ("Combustion analysis is primarily used for compounds containing:", ["Metals", "Noble gases", "*Carbon and hydrogen (organic compounds)", "Only ionic compounds"], "Organic compound analysis."),
])

# U7 L7.6: Limiting Reagent
add_qs("u7_l7.6", [
    ("The limiting reagent is the reactant that:", ["Is in excess", "*Is completely consumed first, stopping the reaction", "Is the most expensive", "Acts as a catalyst"], "Controls the amount of product formed."),
    ("The excess reagent is the reactant that:", ["Runs out first", "*Remains after the reaction ends (not completely used up)", "Is always the solvent", "Produces more product"], "Leftover reactant."),
    ("In 2H2 + O2 -> 2H2O, if you have 3 mol H2 and 2 mol O2:", ["O2 is limiting", "*H2 is limiting (3 mol H2 needs 1.5 mol O2, but you need 3 to use all O2, and only have 3/2=1.5 mol O2 equivalent)", "Neither is limiting", "Both are limiting"], "3 mol H2 can react with 1.5 mol O2; 2 mol O2 is excess."),
    ("To identify the limiting reagent, compare:", ["Masses directly", "Volumes directly", "*Mole ratios to the stoichiometric ratio (the one that gives less product is limiting)", "Colors"], "Use stoichiometry to determine which runs out first."),
    ("Theoretical yield is:", ["The actual amount produced", "*The maximum amount of product calculated from the limiting reagent", "Always achieved in practice", "The mass of reactants"], "Best possible outcome assuming complete reaction."),
    ("Actual yield is usually _____ theoretical yield.", ["Greater than", "Equal to", "*Less than (due to incomplete reactions, side reactions, losses)", "Unrelated to"], "Real-world losses reduce yield."),
    ("If 4 mol of Na react with 3 mol of Cl2 (2Na + Cl2 -> 2NaCl):", ["Cl2 is limiting", "*Na is limiting (4 mol Na needs 2 mol Cl2; we have 3, so Na runs out first)", "Neither", "Both"], "4 mol Na / 2 = 2 mol Cl2 needed; we have 3, so Na limits."),
    ("After the above reaction, how much Cl2 remains?", ["0 mol", "*1 mol (started with 3, used 2)", "2 mol", "3 mol"], "3 - 2 = 1 mol excess Cl2."),
    ("A sandwich analogy: if you have 10 bread slices and 3 meat patties:", ["Bread is limiting", "*Meat is limiting (each sandwich needs 2 bread + 1 meat; 3 patties = 3 sandwiches, 4 bread left)", "Neither", "Both"], "Meat runs out first."),
    ("Method to find limiting reagent: calculate product from each reactant separately, the one that gives _____ product is limiting.", ["More", "*Less", "Equal", "No"], "Least product = from limiting reagent."),
    ("In a reaction with 10.0 g of A and 10.0 g of B, A (MM=10) gives 5 mol product and B (MM=20) gives 3 mol product:", ["A is limiting", "*B is limiting (produces less product)", "Equal amounts", "Cannot tell"], "B limits the product formation."),
    ("Why is identifying the limiting reagent important?", ["Just for fun", "*It determines the maximum product yield and is essential for accurate stoichiometric calculations", "It affects color", "It changes the reaction type"], "Controls quantitative outcomes."),
    ("In industrial chemistry, using slight excess of _____ reagent(s) ensures the expensive reactant is fully consumed.", ["The expensive", "*The cheaper (drive the limiting reagent to completion)", "No", "Both equally"], "Economic optimization."),
])

# U7 L7.7: Stoichiometry
add_qs("u7_l7.7", [
    ("Stoichiometry uses _____ from balanced equations to calculate amounts.", ["Masses directly", "*Mole ratios (coefficients)", "Volumes only", "Colors"], "Coefficients establish mole relationships."),
    ("In 2H2 + O2 -> 2H2O, the mole ratio of H2 to H2O is:", ["1:1", "*1:1 (2:2 simplifies to 1:1)", "2:1", "1:2"], "2 mol H2 produces 2 mol H2O; ratio is 1:1."),
    ("How many moles of O2 are needed to react with 6 mol of H2?", ["6 mol", "2 mol", "*3 mol (6 mol H2 x 1 mol O2/2 mol H2)", "1 mol"], "Mole ratio H2:O2 = 2:1."),
    ("Starting from grams, the stoichiometry sequence is:", ["Grams -> particles -> moles", "Moles -> grams directly", "*Grams of A -> moles of A -> moles of B -> grams of B (using molar mass and mole ratio)", "Grams divided by Avogadro's number"], "The 'mole bridge' connects two substances."),
    ("Given: 2Al + 3Cl2 -> 2AlCl3. How many grams of AlCl3 from 5.4 g Al?", ["13.35 g", "*26.7 g (5.4/27 = 0.2 mol Al -> 0.2 mol AlCl3 x 133.5 g/mol)", "53.4 g", "133.5 g"], "Step through moles."),
    ("A stoichiometric calculation requires, at minimum:", ["Just the balanced equation", "Just masses", "*A balanced equation AND an amount of at least one substance", "Temperature"], "Need the equation and a starting amount."),
    ("Volume stoichiometry at STP uses:", ["Molar mass", "*22.4 L/mol (molar volume of gas at STP)", "Density only", "1 L/mol"], "STP molar volume for gases."),
    ("In 2NaOH + H2SO4 -> Na2SO4 + 2H2O, 2 mol NaOH reacts with:", ["2 mol H2SO4", "*1 mol H2SO4", "0.5 mol H2SO4", "4 mol H2SO4"], "2:1 ratio of NaOH to H2SO4."),
    ("Stoichiometry can predict amounts of:", ["Only products", "Only reactants", "*Both reactants needed and products formed", "Neither"], "Works in both directions."),
    ("Solution stoichiometry uses _____ instead of grams.", ["Liters only", "*Molarity (M = mol/L) and volume together to get moles", "Temperature", "Pressure"], "moles = M x V(in liters)."),
    ("If an experiment requires 0.50 mol of NaCl, and you have a 2.0 M solution, what volume do you need?", ["1.0 L", "2.0 L", "*0.25 L (250 mL)", "0.50 L"], "V = mol/M = 0.50/2.0 = 0.25 L."),
    ("The mole ratio acts as a _____ between substances in a reaction.", ["Barrier", "*Conversion factor (bridge from moles of one substance to moles of another)", "Catalyst", "Inhibitor"], "The ratio links all species."),
    ("Gas stoichiometry at non-STP conditions also requires:", ["Only moles", "Only mass", "*The ideal gas law (PV = nRT) to relate moles to volume", "Nothing extra"], "PV=nRT for gas calculations at non-standard conditions."),
])

# U7 L7.8: Percent Yield
add_qs("u7_l7.8", [
    ("Percent yield = (actual yield / theoretical yield) x _____.", ["10", "*100", "1000", "Avogadro's number"], "Express as a percentage."),
    ("Theoretical yield is calculated using _____ from the limiting reagent.", ["Actual measurements", "*Stoichiometry (mole ratios and molar mass)", "Percent error", "Titration"], "Maximum possible product."),
    ("If theoretical yield is 50 g and actual yield is 40 g, percent yield is:", ["90%", "*80% (40/50 x 100)", "50%", "125%"], "40/50 x 100 = 80%."),
    ("A percent yield greater than 100% usually indicates:", ["A perfect experiment", "*Experimental error (impurities, incomplete drying, measurement mistakes)", "Exceptional skill", "A synthesis reaction"], "Physically impossible to exceed theoretical yield."),
    ("A high percent yield indicates:", ["Waste", "*Efficient conversion of reactants to products", "Poor technique", "Side reactions"], "More product formed relative to theoretical maximum."),
    ("Reasons actual yield is less than theoretical include:", ["Perfect conditions", "*Incomplete reactions, side reactions, transfer losses, and purification losses", "Too many reactants", "Using a catalyst"], "Multiple factors reduce yield."),
    ("If you need 100 g of product and expect 80% yield, you should start with enough reactants for:", ["80 g theoretical", "100 g theoretical", "*125 g theoretical (100/0.80 = 125)", "200 g theoretical"], "Account for the expected loss."),
    ("In a reaction with 75% yield, 30 g theoretical yield gives:", ["30 g actual", "75 g actual", "*22.5 g actual (30 x 0.75)", "100 g actual"], "actual = theoretical x (percent yield / 100)."),
    ("Which is NOT a reason for low percent yield?", ["Product left in container", "Side reactions", "Incomplete reaction", "*Using the correct amount of limiting reagent"], "Correct reagent amounts don't decrease yield."),
    ("In pharmaceutical manufacturing, _____ percent yield is especially important.", ["Low", "*High (maximizing drug production and minimizing waste)", "Average", "Variable"], "Drug synthesis must be efficient."),
    ("Multi-step synthesis percent yield: if step 1 = 90% and step 2 = 80%, overall yield:", ["170%", "85%", "*72% (0.90 x 0.80 x 100)", "10%"], "Multiply individual yields."),
    ("Atom economy differs from percent yield because it measures:", ["How much product forms", "*How much of the reactant atoms end up in the desired product (efficiency by design)", "Actual vs. theoretical", "Mass loss"], "Atom economy = (mass of useful product / mass of all products) x 100."),
    ("Green chemistry aims for _____ percent yield and _____ atom economy.", ["Low; low", "High; low", "Low; high", "*High; high (maximize efficiency and minimize waste)"], "Sustainable chemistry principles."),
])

# ── UNIT 8 ──

# U8 L8.1: Monatomic/Noble Gases
add_qs("u8_l8.1", [
    ("Noble gases are monatomic, meaning they exist as:", ["Molecules of 2 atoms", "*Individual single atoms (not bonded to other atoms)", "Crystals", "Ions"], "No bonding needed — full valence shell."),
    ("Noble gases have a full _____ shell.", ["Inner", "*Outer electron (valence, typically 8 electrons except He with 2)", "Nuclear", "Proton"], "Complete octet (or duet for He)."),
    ("Noble gases are in Group _____ of the periodic table.", ["1", "7", "14", "*18"], "Rightmost column."),
    ("The noble gases in order of increasing atomic number are:", ["Ne, He, Ar, Kr", "*He, Ne, Ar, Kr, Xe, Rn (Og is the newest)", "Ar, He, Ne, Kr", "Kr, Xe, He, Ne"], "Increasing Z: 2, 10, 18, 36, 54, 86, 118."),
    ("Noble gases are sometimes called:", ["Active gases", "Reactive gases", "*Inert gases (though some can form compounds under extreme conditions)", "Toxic gases"], "Very low reactivity."),
    ("Helium is used in balloons because:", ["It's cheap", "*It's lighter than air and non-flammable", "It's abundant", "It glows"], "Low density and safe."),
    ("Neon is used in:", ["Light bulbs", "*Neon signs (produces orange-red glow when electrified)", "Balloons", "Refrigerators"], "Characteristic neon glow."),
    ("Argon is used in:", ["Balloons", "Signs", "*Welding and light bulbs (inert atmosphere prevents oxidation)", "Medicine"], "Provides a non-reactive atmosphere."),
    ("Xenon can form compounds with:", ["No elements", "All elements", "*Fluorine and oxygen (under special conditions)", "Only metals"], "XeF2, XeF4, XeO3 exist despite xenon being noble."),
    ("The boiling points of noble gases _____ going down the group.", ["Decrease", "*Increase (larger atoms have stronger London dispersion forces)", "Stay the same", "Fluctuate"], "More electrons = stronger LDFs."),
    ("Noble gases have very low:", ["Atomic numbers", "*Reactivity and intermolecular forces (due to complete electron shells)", "Masses", "Energy"], "Full shells = minimal chemical interaction."),
    ("Radon (Rn) is a noble gas that is:", ["Very stable", "*Radioactive (health hazard from natural decay of uranium in soil)", "Completely harmless", "Extremely reactive"], "Rn-222 is a carcinogenic gas."),
    ("The first noble gas compound (XeF2) was synthesized in:", ["1800", "1900", "*1962 (by Neil Bartlett)", "2000"], "Proved noble gases aren't completely inert."),
])

# U8 L8.2: Atmospheric Pressure
add_qs("u8_l8.2", [
    ("Atmospheric pressure is caused by:", ["Wind", "*The weight of the air column above a given area", "The Sun's gravity", "Ocean currents"], "Column of air pushing down."),
    ("Standard atmospheric pressure at sea level is:", ["1 atm", "760 mmHg", "101.325 kPa", "*All of the above (these are equivalent units)"], "Different units for the same pressure."),
    ("A barometer measures:", ["Temperature", "Humidity", "*Atmospheric pressure", "Wind speed"], "Mercury barometer invented by Torricelli."),
    ("As altitude increases, atmospheric pressure:", ["Increases", "*Decreases (less air above you)", "Stays the same", "Doubles"], "Less air mass above = lower pressure."),
    ("760 mmHg equals:", ["760 atm", "*1 atm (exactly, by definition)", "760 kPa", "7.6 atm"], "Standard pressure relationship."),
    ("Convert 2.5 atm to mmHg:", ["380 mmHg", "*1900 mmHg (2.5 x 760)", "2500 mmHg", "190 mmHg"], "2.5 x 760 = 1900."),
    ("Convert 2.0 atm to kPa:", ["101.325 kPa", "*202.65 kPa (2.0 x 101.325)", "200 kPa", "50 kPa"], "2.0 x 101.325 = 202.65."),
    ("1 atm = _____ torr.", ["100", "500", "*760", "1013"], "Torr and mmHg are equivalent."),
    ("Pressure is defined as:", ["Force times area", "*Force per unit area (P = F/A)", "Mass per volume", "Energy per time"], "P = F/A."),
    ("SI unit of pressure is:", ["atm", "mmHg", "*Pascal (Pa, equal to N/m^2)", "torr"], "Pascal is the SI unit."),
    ("A manometer measures:", ["Only atmospheric pressure", "*The pressure of a gas in a container (open or closed)", "Temperature", "Volume"], "Compares gas pressure to atmospheric."),
    ("Weather changes in atmospheric pressure: low pressure often brings:", ["Clear skies", "*Stormy or rainy weather", "No change", "Heat waves"], "Low pressure = rising, cooling air = clouds/rain."),
    ("On top of Mount Everest, atmospheric pressure is about:", ["1 atm", "0.75 atm", "*0.33 atm (roughly one-third sea level)", "2 atm"], "Much lower than sea level."),
])

# U8 L8.3: Kinetic Molecular Theory
add_qs("u8_l8.3", [
    ("KMT states that gas particles are in:", ["Fixed positions", "*Constant, random, straight-line motion", "Circular orbits", "Stationary equilibrium"], "Continuous random movement."),
    ("Gas particles are assumed to have _____ volume in KMT.", ["Large", "Some", "*Negligible (point particles)", "Infinite"], "Ideal gas assumption."),
    ("Collisions between gas particles are:", ["Inelastic", "*Perfectly elastic (no net loss of kinetic energy)", "Partially elastic", "Sticky"], "Total KE is conserved."),
    ("Average kinetic energy of gas particles is directly proportional to:", ["Pressure", "Volume", "*Absolute temperature (in Kelvin)", "Molar mass"], "KE_avg = (3/2)kT."),
    ("At the same temperature, different gases have:", ["Different kinetic energies", "*The same average kinetic energy", "No kinetic energy", "Different temperatures"], "Same T = same average KE."),
    ("At the same temperature, lighter gases move _____ than heavier gases.", ["Slower", "*Faster (same KE but less mass means higher velocity)", "At the same speed", "Not at all"], "KE = (1/2)mv^2; lower m = higher v."),
    ("Gas pressure results from:", ["Gravity only", "*Particles colliding with container walls (each collision exerts force)", "Chemical bonds", "Magnetic fields"], "Momentum transfer to walls."),
    ("Graham's law states that lighter gases _____ faster.", ["Sink", "*Diffuse and effuse (rate inversely proportional to square root of molar mass)", "React", "Condense"], "Rate ∝ 1/√M."),
    ("Effusion is:", ["Gas mixing", "*Gas escaping through a tiny hole into a vacuum", "Gas dissolving", "Gas condensing"], "Movement through a small opening."),
    ("Diffusion is:", ["Gas through a hole", "*Gradual mixing of gases due to random motion", "Gas becoming liquid", "Gas pressurization"], "Spreading out over time."),
    ("The root-mean-square (rms) speed of a gas depends on:", ["Pressure only", "Volume only", "*Temperature and molar mass (v_rms = sqrt(3RT/M))", "Color"], "Higher T or lower M = faster."),
    ("At absolute zero (0 K), the KMT predicts:", ["Maximum motion", "*All molecular motion stops (theoretical, never truly reached)", "Gases become liquid", "Pressure increases"], "No kinetic energy at 0 K."),
    ("KMT explains why gases are compressible:", ["They're heavy", "*Particles are far apart with mostly empty space between them", "They have bonds", "They're magnetic"], "Empty space can be reduced."),
])

# U8 L8.4: Boyle's Law
add_qs("u8_l8.4", [
    ("Boyle's Law states that at constant temperature:", ["P and V are directly proportional", "*P and V are inversely proportional (PV = constant)", "P and T are proportional", "V and T are proportional"], "P1V1 = P2V2 at constant T."),
    ("If pressure doubles (at constant T), volume:", ["Doubles", "*Halves", "Stays the same", "Triples"], "Inverse relationship."),
    ("A gas at 2.0 atm occupies 5.0 L. At 4.0 atm (same T), the volume is:", ["10.0 L", "*2.5 L (P1V1 = P2V2; 2x5/4 = 2.5)", "5.0 L", "1.0 L"], "2.0 x 5.0 = 4.0 x V2; V2 = 2.5 L."),
    ("A gas at 1.0 atm occupies 10 L. What pressure gives 5 L (same T)?", ["0.5 atm", "*2.0 atm (1.0 x 10 = P2 x 5)", "1.0 atm", "5.0 atm"], "P2 = 10/5 = 2.0 atm."),
    ("Boyle's Law applies to _____ systems.", ["Open", "Heated", "*Closed (constant amount of gas at constant temperature)", "Reacting"], "Constant T and n."),
    ("On a P-V graph (Boyle's Law), the curve is a:", ["Straight line", "*Hyperbola (inverse relationship produces a curve)", "Parabola", "Circle"], "PV = k produces a hyperbolic curve."),
    ("Squeezing a balloon illustrates Boyle's Law: decreasing volume _____ pressure.", ["Decreases", "*Increases (same number of particles in less space = more collisions)", "Doesn't change", "Eliminates"], "More collisions per unit area."),
    ("A syringe demonstrates Boyle's Law when you:", ["Heat it", "*Push the plunger in (decrease volume, increase pressure)", "Cool it", "Add gas"], "Volume decreases, pressure increases."),
    ("Breathing uses Boyle's Law: when the diaphragm contracts, lung volume _____ and pressure _____.", ["Decreases; increases", "*Increases; decreases (air flows in because external pressure is now greater)", "Stays same; stays same", "Increases; increases"], "Expansion lowers internal pressure."),
    ("At very high pressures, real gases deviate from Boyle's Law because:", ["Gas particles have no volume", "*Particle volume becomes significant and intermolecular forces matter", "Temperature changes", "Pressure doesn't affect gases"], "Ideal gas assumptions break down."),
    ("Derive: if V1=3L, P1=1atm, V2=? at P2=0.5atm:", ["1.5 L", "*6 L (1x3 = 0.5xV2; V2=6)", "3 L", "0.5 L"], "Lower pressure = greater volume."),
    ("Boyle's Law was discovered in:", ["1862", "*1662 (by Robert Boyle, one of the first gas laws)", "1762", "1962"], "Robert Boyle's experiments with gas in a J-tube."),
    ("Underwater divers must be careful with Boyle's Law because:", ["Water is denser", "*Rapid ascent causes dissolved gases (mainly N2) in blood to expand, risking decompression sickness", "They run out of air", "Water pressure doesn't affect gases"], "Expanding gas bubbles in the body."),
])

# U8 L8.5: Charles's Law
add_qs("u8_l8.5", [
    ("Charles's Law states that at constant pressure:", ["V and T are inversely proportional", "*V and T (in Kelvin) are directly proportional (V/T = constant)", "P and T are proportional", "P and V are proportional"], "V1/T1 = V2/T2 at constant P."),
    ("Temperature in gas law calculations must be in:", ["Celsius", "Fahrenheit", "*Kelvin (absolute temperature scale)", "Any unit"], "Kelvin eliminates negative temperatures."),
    ("If temperature doubles (in K, at constant P), volume:", ["Halves", "*Doubles", "Stays the same", "Quadruples"], "Direct proportionality."),
    ("A gas at 300 K occupies 6.0 L. At 600 K (same P), V is:", ["3.0 L", "*12.0 L (V1/T1 = V2/T2; 6/300 = V2/600)", "6.0 L", "24.0 L"], "V2 = 6.0 x 600/300 = 12.0 L."),
    ("Convert 25 degrees C to Kelvin:", ["25 K", "*298 K (25 + 273)", "248 K", "325 K"], "K = C + 273."),
    ("A gas at 2.0 L and 200 K. At what T will V = 4.0 L?", ["100 K", "*400 K (2/200 = 4/T2; T2 = 400)", "200 K", "800 K"], "T2 = 4.0 x 200 / 2.0 = 400 K."),
    ("On a V-T graph (Charles's Law), the line is:", ["A curve", "*Straight line through the origin (direct proportionality in Kelvin)", "A hyperbola", "A circle"], "Linear with intercept at 0 K = 0 V."),
    ("Extrapolation of the Charles's Law line to zero volume gives:", ["0 degrees C", "100 K", "*0 K (-273.15 degrees C, absolute zero)", "-100 degrees C"], "Theoretical zero volume at absolute zero."),
    ("Hot air balloons rise because:", ["Hot air is heavier", "*Heating air inside the balloon decreases its density (V increases, less dense than surrounding cool air)", "Cold air sinks", "The balloon is magnetic"], "Charles's Law: V increases with T."),
    ("Why can't we use Celsius in Charles's Law?", ["Celsius is metric", "Celsius is too large", "*Celsius can be negative, which would give negative volumes (impossible)", "No reason"], "Kelvin ensures positive values."),
    ("A ball inflated indoors (20 degrees C) and taken outside (-10 degrees C) will:", ["Expand", "*Shrink (lower temperature = smaller volume)", "Stay the same", "Pop"], "Cold reduces gas volume."),
    ("Charles's Law was discovered by:", ["Robert Boyle", "*Jacques Charles (1787, published by Gay-Lussac)", "Joseph Gay-Lussac", "Amedeo Avogadro"], "Charles performed the experiments."),
    ("If a gas occupies 10.0 L at 273 K and is cooled to 136.5 K at constant P, its volume becomes:", ["20.0 L", "*5.0 L (10 x 136.5/273)", "10.0 L", "2.5 L"], "Temperature halved, volume halved."),
])

# U8 L8.6: Gay-Lussac's Law
add_qs("u8_l8.6", [
    ("Gay-Lussac's Law relates _____ and _____ at constant volume.", ["P and V", "*P and T (pressure is directly proportional to temperature in Kelvin)", "V and T", "V and n"], "P1/T1 = P2/T2 at constant V."),
    ("If temperature increases at constant volume, pressure:", ["Decreases", "*Increases (particles move faster, hitting walls harder and more often)", "Stays the same", "Reaches zero"], "Higher T = higher P."),
    ("A gas at 1.0 atm and 300 K is heated to 600 K (constant V). New pressure:", ["0.5 atm", "*2.0 atm (P2 = 1.0 x 600/300)", "1.0 atm", "3.0 atm"], "Doubled temperature = doubled pressure."),
    ("A tire with P=32 psi at 20 degrees C (293K). If T rises to 50 degrees C (323K):", ["Pressure decreases", "*Pressure increases to about 35.3 psi (32 x 323/293)", "Pressure stays 32 psi", "Volume doubles"], "Heating at constant volume raises pressure."),
    ("Pressure cookers work by Gay-Lussac's Law because:", ["They cool food", "*Sealed (constant V), so increased temperature increases pressure, raising the boiling point of water", "They add gas", "They remove heat"], "Higher pressure = higher boiling point."),
    ("Temperature must be in _____ for Gay-Lussac's Law.", ["Celsius", "Fahrenheit", "*Kelvin", "Any unit"], "Absolute temperature required."),
    ("A sealed container at 2.0 atm and 400 K is cooled to 200 K:", ["P increases to 4.0 atm", "P stays at 2.0 atm", "*P decreases to 1.0 atm (2.0 x 200/400)", "P = 0 atm"], "Half the temperature = half the pressure."),
    ("Warning labels on aerosol cans about heat relate to:", ["Charles's Law", "*Gay-Lussac's Law (heating a sealed can increases pressure, risking explosion)", "Boyle's Law", "Avogadro's Law"], "Fixed volume + high T = dangerous pressure."),
    ("On a P-T graph (Gay-Lussac's Law), the line is:", ["A hyperbola", "*A straight line through the origin (direct proportion in Kelvin)", "A curve", "A step function"], "Linear: P directly proportional to T."),
    ("At absolute zero (theoretically), the pressure would be:", ["Maximum", "*Zero (no molecular motion = no collisions = no pressure)", "1 atm", "Infinite"], "KMT: no motion = no pressure."),
    ("An autoclave sterilizes using Gay-Lussac's principle because:", ["It cools items", "*Sealed volume + heat = high pressure, which raises water's boiling point above 100 degrees C for more effective sterilization", "It applies chemicals", "It reduces pressure"], "Higher temperature killing microorganisms."),
    ("Solve: P1=3.0 atm, T1=150K, T2=450K. Find P2:", ["1.0 atm", "*9.0 atm (3.0 x 450/150)", "4.5 atm", "6.0 atm"], "P2 = 3.0 x 450/150 = 9.0 atm."),
    ("Gay-Lussac also discovered that gases combine in simple _____ ratios.", ["Mass", "*Volume (leading to the law of combining volumes)", "Energy", "Pressure"], "Gases react in ratios of small whole numbers of volumes."),
])

# U8 L8.7: Combined Gas Law
add_qs("u8_l8.7", [
    ("The combined gas law formula is:", ["PV = nRT", "*P1V1/T1 = P2V2/T2", "PV = k", "V/T = k"], "Combines Boyle's, Charles's, and Gay-Lussac's laws."),
    ("If P doubles and T is halved (constant n), V:", ["Doubles", "Stays the same", "Halves", "*Quarters (V2 = V1 x P1/P2 x T2/T1 = V1 x 0.5 x 0.5)"], "V is inversely proportional to P and directly proportional to T."),
    ("The combined gas law reduces to Boyle's Law when _____ is constant.", ["Pressure", "Volume", "*Temperature", "Mass"], "If T1=T2, then P1V1=P2V2."),
    ("The combined gas law reduces to Charles's Law when _____ is constant.", ["Temperature", "Volume", "*Pressure", "Mass"], "If P1=P2, then V1/T1=V2/T2."),
    ("A gas at 2.0 atm, 4.0 L, 300 K changes to 1.0 atm, 600 K. Find V2:", ["4.0 L", "8.0 L", "*16.0 L (4 x 2/1 x 600/300)", "2.0 L"], "V2 = 4.0 x (2.0/1.0) x (600/300) = 16.0 L."),
    ("A gas at 1.0 atm, 10.0 L, 200 K changes to 400 K, 2.0 atm. Find V2:", ["20 L", "*10.0 L (10 x 1/2 x 400/200)", "5.0 L", "40.0 L"], "V2 = 10 x (1.0/2.0) x (400/200) = 10.0 L."),
    ("STP stands for:", ["Standard Thermal Properties", "*Standard Temperature and Pressure (0 degrees C / 273 K and 1 atm)", "Scientific Testing Protocol", "Standard Technical Procedure"], "Defined reference conditions."),
    ("At STP, T = _____ K and P = _____ atm.", ["300; 1.0", "*273; 1.0 (0 degrees C and 1 atm)", "298; 1.0", "273; 2.0"], "0°C = 273 K; 1 atm."),
    ("A gas occupies 5.0 L at STP. What volume at 2.0 atm and 546 K?", ["2.5 L", "*5.0 L (5 x 1/2 x 546/273 = 5.0)", "10.0 L", "20.0 L"], "P doubles (halves V), T doubles (doubles V); net no change."),
    ("The combined gas law applies to a _____ amount of gas.", ["Variable", "*Fixed (constant n, same amount of gas)", "Increasing", "Reacting"], "Amount of gas must be constant."),
    ("To use the combined gas law, you need to know:", ["Only initial conditions", "Only final conditions", "*Initial and final values of two variables, plus one unknown", "All six values"], "5 knowns, 1 unknown."),
    ("A weather balloon launched at sea level (1 atm, 20°C, 1L) rises to altitude where P=0.5 atm, T=-20°C. V2:", ["0.5 L", "*1.73 L (1 x 1/0.5 x 253/293)", "2.0 L", "4.0 L"], "V2 = 1 x (1/0.5) x (253/293) = 1.73 L."),
    ("The combined gas law assumes:", ["Real gas behavior", "*Ideal gas behavior (no intermolecular forces, negligible particle volume)", "Constant temperature", "Chemical reactions"], "Ideal gas assumptions."),
])

# U8 L8.8: Ideal Gas Law
add_qs("u8_l8.8", [
    ("The ideal gas law equation is:", ["P1V1 = P2V2", "PV/T = constant", "*PV = nRT", "V = kT"], "Relates P, V, n, and T."),
    ("R (the ideal gas constant) equals:", ["0.0821 L·atm/(mol·K)", "8.314 J/(mol·K)", "*Both (different units for different calculations)", "1.0"], "R has multiple forms depending on units."),
    ("Calculate V for 1.0 mol of gas at STP: PV=nRT, V=nRT/P:", ["11.2 L", "*22.4 L (1 x 0.0821 x 273 / 1.0)", "44.8 L", "1.0 L"], "Molar volume at STP."),
    ("How many moles of gas in a 5.0 L container at 2.0 atm and 300 K?", ["0.20 mol", "0.61 mol", "*0.41 mol (n = PV/RT = 2x5/(0.0821x300))", "1.0 mol"], "n = 10/24.63 = 0.41 mol."),
    ("What pressure does 0.5 mol of gas exert in a 10 L container at 400 K?", ["0.821 atm", "*1.64 atm (P = nRT/V = 0.5 x 0.0821 x 400/10)", "2.0 atm", "0.5 atm"], "P = 16.42/10 = 1.64 atm."),
    ("The ideal gas law incorporates which variable the combined gas law does not?", ["Pressure", "Temperature", "*Amount of gas (n, in moles)", "Volume"], "n is included in PV = nRT."),
    ("Molar mass can be found using the ideal gas law: M = _____.", ["PV/RT", "nRT/P", "*dRT/P (where d is density in g/L)", "P/dRT"], "From PV = nRT and n = mass/M."),
    ("A gas has d = 1.96 g/L at STP. Its molar mass is:", ["22.4 g/mol", "*44 g/mol (1.96 x 22.4, or using M = dRT/P)", "28 g/mol", "2 g/mol"], "This is CO2 (44 g/mol)."),
    ("Dalton's Law of Partial Pressures: P_total = _____.", ["P1 x P2", "*P1 + P2 + P3 + ... (sum of individual gas pressures)", "P1 / P2", "P1 - P2"], "Each gas contributes independently."),
    ("In a mixture, the partial pressure of gas A = (mole fraction of A) x P_total. The mole fraction is:", ["Mass of A/total mass", "*Moles of A/total moles", "Volume of A/total volume", "Atoms of A/total atoms"], "Mole fraction = n_A / n_total."),
    ("An ideal gas _____ at high pressure and low temperature.", ["Behaves perfectly", "*Deviates from ideal behavior (real gas effects become significant)", "Becomes a solid", "Stops moving"], "Intermolecular forces and particle volume matter."),
    ("STP conditions for ideal gas calculations: T = 273 K, P = 1 atm gives molar volume:", ["11.2 L", "*22.4 L", "44.8 L", "100 L"], "Standard molar volume."),
    ("The ideal gas law can be used to determine the molar mass of an unknown gas by measuring:", ["Only temperature", "*Mass, volume, temperature, and pressure", "Only mass", "Only pressure"], "All four measurable quantities needed."),
])

# U8 L8.9: Real Gases
add_qs("u8_l8.9", [
    ("Real gases deviate from ideal behavior at:", ["Low pressure and high temperature", "All conditions equally", "*High pressure and/or low temperature", "STP only"], "Conditions where particles are closer together."),
    ("The van der Waals equation corrects for:", ["Only particle volume", "Only intermolecular forces", "*Both intermolecular forces (a) and particle volume (b)", "Temperature"], "(P + a/V^2)(V - b) = nRT."),
    ("The 'a' constant in van der Waals equation corrects for:", ["Particle volume", "*Intermolecular attractive forces (which reduce pressure from ideal)", "Temperature", "Mass"], "Attractions reduce collisions with walls."),
    ("The 'b' constant corrects for:", ["Intermolecular forces", "*The actual volume occupied by gas particles", "Temperature", "Pressure"], "Reduces the available volume."),
    ("At high pressure, gas particles are:", ["Far apart", "*Close together, so particle volume and intermolecular forces become significant", "Stationary", "Equal to ideal"], "Real gas effects appear."),
    ("At low temperature, gas particles:", ["Move faster", "*Move slower, allowing intermolecular attractions to affect behavior more", "Become ideal", "Escape the container"], "Attractions reduce pressure more when particles are slow."),
    ("Gases with stronger intermolecular forces have _____ 'a' values.", ["Lower", "*Higher (more correction needed for attractions)", "Zero", "Negative"], "More attraction = bigger 'a'."),
    ("Larger gas molecules have _____ 'b' values.", ["Lower", "*Higher (take up more physical space)", "Zero", "Negative"], "Bigger molecules = bigger volume correction."),
    ("Hydrogen (H2) behaves most ideally because:", ["It's the lightest", "*It has the weakest intermolecular forces and smallest molecular volume", "It's a gas", "It reacts easily"], "Closest to ideal gas assumptions."),
    ("At conditions approaching absolute zero, all real gases:", ["Become ideal", "*Liquefy or solidify (intermolecular forces dominate)", "Expand infinitely", "Become plasma"], "Phase transitions at low T."),
    ("The compressibility factor Z = PV/nRT. For an ideal gas, Z =:", ["0", "*1 (exactly)", "2", "Variable"], "Deviations from 1 indicate non-ideal behavior."),
    ("When Z > 1, the dominant effect is:", ["Attractive forces", "*Repulsive forces / molecular volume (actual volume > ideal volume at very high P)", "Neither", "Temperature"], "Particle volume makes real volume larger than predicted."),
    ("When Z < 1, the dominant effect is:", ["Molecular volume", "*Intermolecular attractions (reduce pressure below ideal prediction)", "Neither", "Temperature"], "Attractions reduce actual pressure."),
])

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

short = [(k, len(v.get("quiz_questions",[]))) for k,v in data.items() if len(v.get("quiz_questions",[]))<20]
ct = sum(1 for v in data.values() if len(v.get('quiz_questions',[])) >= 20)
print(f"✅ Chemistry U6-U8 done: {ct}/{len(data)} lessons at 20+ questions")
if short:
    print(f"Still short: {len(short)} lessons")
