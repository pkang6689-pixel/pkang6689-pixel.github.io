#!/usr/bin/env python3
"""Expand Chemistry Units 9-12 from 7 to 20 quiz questions each (29 lessons)."""
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

# ── UNIT 9: Solutions ──

# U9 L9.1: Solvents & Solutes
add_qs("u9_l9.1", [
    ("The solvent is the component that:", ["Dissolves", "*Does the dissolving (present in the larger amount)", "Is always water", "Is always a solid"], "Solvent = larger quantity."),
    ("Water is called the 'universal solvent' because:", ["It dissolves everything", "*It dissolves more substances than any other common liquid (due to polarity)", "It's colorless", "It's cheap"], "Polarity allows water to dissolve many ionic and polar substances."),
    ("'Like dissolves like' means:", ["Only identical substances dissolve", "*Polar solvents dissolve polar/ionic solutes; nonpolar solvents dissolve nonpolar solutes", "All liquids mix", "Only water dissolves things"], "Similar intermolecular forces promote dissolving."),
    ("Oil doesn't dissolve in water because:", ["Oil is heavier", "Water is too cold", "*Oil is nonpolar and water is polar (unlike intermolecular forces)", "Oil is a gas"], "Nonpolar in polar = immiscible."),
    ("An aqueous solution has _____ as the solvent.", ["Alcohol", "Acetone", "*Water", "Any liquid"], "Aqueous = water-based."),
    ("Miscible liquids:", ["Don't mix", "*Mix completely in all proportions (like water and ethanol)", "Only mix with heat", "Form layers"], "Fully soluble in each other."),
    ("Immiscible liquids:", ["Mix completely", "*Do not mix (like oil and water, forming separate layers)", "React chemically", "Evaporate"], "Separate into layers."),
    ("When an ionic compound dissolves, ions are _____ by water molecules.", ["Repelled", "*Surrounded (hydrated/solvated) — positive ion attracts O; negative ion attracts H", "Destroyed", "Combined"], "Hydration stabilizes dissolved ions."),
    ("Dissolution of NaCl in water: Na+ is attracted to the _____ end of water.", ["Hydrogen (positive)", "*Oxygen (negative) end of water", "Neither end", "Both equally"], "Opposite charges attract: Na+ to δ- oxygen."),
    ("A tincture is a solution with _____ as the solvent.", ["Water", "*Alcohol (ethanol)", "Oil", "Acid"], "Tincture of iodine = iodine in alcohol."),
    ("An alloy is a _____ solution.", ["Liquid", "Gas", "*Solid (mixture of metals)", "Aqueous"], "Bronze, steel, brass are solid solutions."),
    ("Electrolytes dissolve to form:", ["Molecules only", "*Ions that conduct electricity in solution", "Gases", "Precipitates"], "Ionic compounds in water conduct electricity."),
    ("Strong electrolytes _____ completely in water.", ["Partially dissociate", "*Fully dissociate (all formula units separate into ions)", "Don't dissolve", "Evaporate"], "NaCl -> Na+ + Cl- completely."),
])

# U9 L9.2: Concentration
add_qs("u9_l9.2", [
    ("Concentration measures:", ["Volume of solvent", "Mass of container", "*The amount of solute dissolved in a given amount of solution", "Temperature"], "Quantifies how much solute is present."),
    ("A concentrated solution has:", ["Very little solute", "*A large amount of solute relative to solvent", "No solvent", "Only gas"], "High solute-to-solvent ratio."),
    ("A dilute solution has:", ["Lots of solute", "*A small amount of solute relative to solvent", "No water", "High viscosity"], "Low solute-to-solvent ratio."),
    ("Molarity (M) is defined as:", ["Moles of solute per kg of solvent", "*Moles of solute per liter of SOLUTION", "Grams of solute per liter", "Mass percent"], "M = mol solute / L solution."),
    ("Molality (m) is defined as:", ["Moles per liter of solution", "*Moles of solute per kilogram of SOLVENT", "Mass per volume", "Percent by mass"], "m = mol solute / kg solvent."),
    ("Mass percent = (mass of solute / mass of solution) x _____.", ["10", "*100", "1000", "Avogadro's number"], "Expressed as a percentage."),
    ("Parts per million (ppm) is used for:", ["Very concentrated solutions", "*Very dilute solutions (like contaminants in water)", "Solid mixtures only", "Gas pressure"], "mg/L or mg/kg."),
    ("If 5.0 g of NaCl is dissolved in 100 mL of solution, the approximate molarity is:", ["5 M", "0.5 M", "*0.86 M (5/58.5 = 0.0855 mol; 0.0855/0.1 L)", "8.6 M"], "5g / 58.5 g/mol / 0.1 L ≈ 0.86 M."),
    ("Increasing temperature generally _____ the solubility of solid solutes.", ["Decreases", "*Increases (for most solids, more dissolves at higher T)", "Has no effect", "Eliminates"], "Most solids dissolve better in hot water."),
    ("Increasing temperature _____ the solubility of gas solutes.", ["Increases", "*Decreases (gases escape from warmer solutions)", "Has no effect", "Doubles"], "Warm soda goes flat faster."),
    ("Mole fraction = moles of component / _____.", ["Moles of solvent", "*Total moles of ALL components in the mixture", "Liters of solution", "Mass of solution"], "X_A = n_A / (n_A + n_B + ...)."),
    ("A 2.0 M HCl solution means:", ["2 g per liter", "2 mL per liter", "*2.0 moles of HCl per liter of solution", "2% HCl"], "Molarity definition."),
    ("Normality (N) differs from molarity by accounting for:", ["Mass", "Volume", "*Equivalents (H+ donated or OH- accepted or electrons transferred per formula unit)", "Temperature"], "N = M x number of equivalents."),
])

# U9 L9.3: Dilution
add_qs("u9_l9.3", [
    ("The dilution equation is:", ["M = n/V", "*M1V1 = M2V2 (moles of solute remain constant)", "PV = nRT", "d = m/V"], "Dilution doesn't change moles of solute."),
    ("Dilution means:", ["Adding more solute", "*Adding more solvent to decrease concentration", "Heating the solution", "Removing solute"], "More solvent = lower concentration."),
    ("If you dilute 50 mL of 6.0 M HCl to 300 mL, the new concentration is:", ["6.0 M", "3.0 M", "*1.0 M (6.0 x 50 = M2 x 300; M2 = 1.0)", "0.5 M"], "M2 = 300/300 = 1.0 M."),
    ("How much 12 M HCl is needed to make 500 mL of 1.0 M HCl?", ["500 mL", "100 mL", "*41.7 mL (V1 = 1.0 x 500/12)", "12 mL"], "V1 = M2V2/M1."),
    ("When diluting a concentrated acid, always:", ["Add water to acid", "*Add acid to water (slowly, with stirring, to control heat release)", "Mix quickly", "Use no safety equipment"], "Adding acid to water is safer (exothermic dilution controlled better)."),
    ("Serial dilution involves:", ["A single dilution step", "*Multiple sequential dilutions (each reduces concentration by a fixed factor)", "Adding solute", "Evaporation"], "Common in biology for creating very dilute solutions."),
    ("A 1:10 dilution means:", ["10 mL solute + 90 mL solvent", "*1 part solution + 9 parts solvent = 10 total parts (concentration divided by 10)", "1:10 moles", "10:1 ratio"], "Final concentration is 1/10 of original."),
    ("During dilution, the number of moles of solute:", ["Increases", "Decreases", "*Stays the same (you only add solvent, not solute)", "Doubles"], "Conservation of solute."),
    ("Stock solutions are:", ["Final diluted solutions", "*Concentrated solutions stored for later dilution to working concentrations", "Pure solvents", "Saturated solutions"], "Made concentrated for storage efficiency."),
    ("If 25 mL of 4.0 M NaOH is diluted to 100 mL, M2 =:", ["4.0 M", "2.0 M", "*1.0 M (4.0 x 25/100)", "0.5 M"], "M1V1 = M2V2."),
    ("Dilution factor = V_final / V_initial. If DF = 5:", ["Concentration x 5", "*Concentration / 5 (one-fifth of original)", "Volume / 5", "No change"], "DF of 5 means 5x dilution."),
    ("In a lab, you need 250 mL of 0.50 M NaCl from a 5.0 M stock:", ["250 mL of stock", "12.5 mL of stock", "*25 mL of stock (V1 = 0.50 x 250/5.0)", "50 mL of stock"], "V1 = 125/5.0 = 25 mL."),
    ("Volumetric flasks are used in dilution to ensure:", ["Rapid mixing", "*Precise final volume (marked for accuracy)", "High temperature", "Maximum concentration"], "Accuracy in final volume."),
])

# U9 L9.4: Molarity Calculations
add_qs("u9_l9.4", [
    ("Calculate molarity: 2.0 mol NaCl in 500 mL solution:", ["0.5 M", "2.0 M", "*4.0 M (2.0/0.500)", "1.0 M"], "M = mol / L = 2.0 / 0.5 = 4.0 M."),
    ("How many moles of HCl in 250 mL of 0.40 M HCl?", ["0.40 mol", "0.25 mol", "*0.10 mol (0.40 x 0.250)", "1.0 mol"], "n = M × V = 0.40 × 0.250 = 0.10 mol."),
    ("What volume of 2.0 M NaOH contains 0.50 mol NaOH?", ["0.50 L", "*0.25 L (250 mL)", "2.0 L", "1.0 L"], "V = n/M = 0.50/2.0 = 0.25 L."),
    ("To make 1.0 L of 0.10 M NaCl (MM=58.5), you need:", ["10 g", "5.85 g", "*5.85 g (0.10 mol x 58.5 g/mol)", "1.0 g"], "0.10 mol × 58.5 = 5.85 g."),
    ("Molarity is temperature-dependent because:", ["Moles change", "*Volume of solution changes with temperature (thermal expansion)", "Mass changes", "It's not temperature-dependent"], "Liquid volumes expand/contract with T."),
    ("Convert 0.50 M to mmol/mL:", ["5.0 mmol/mL", "*0.50 mmol/mL (M ≡ mmol/mL)", "50 mmol/mL", "0.050 mmol/mL"], "1 M = 1 mol/L = 1 mmol/mL."),
    ("If 10 g of glucose (MM=180) is dissolved in enough water to make 500 mL:", ["0.111 M", "0.200 M", "*0.111 M (10/180/0.500)", "1.0 M"], "n = 10/180 = 0.0556 mol; M = 0.0556/0.500 = 0.111 M."),
    ("Solution stoichiometry: how many mL of 0.20 M AgNO3 to react with 25 mL of 0.30 M NaCl?", ["25 mL", "30 mL", "*37.5 mL (0.30 x 25/0.20 = 37.5)", "75 mL"], "1:1 ratio; mol NaCl = 0.0075; V = 0.0075/0.20 = 37.5 mL."),
    ("Molarity can also be written as mol/dm^3 because:", ["dm^3 = mL", "*1 dm^3 = 1 L (a cubic decimeter equals a liter)", "dm^3 = cm^3", "dm^3 = m^3"], "SI relationship."),
    ("Titration uses molarity to determine:", ["The color of a solution", "*The unknown concentration of a solution by reacting it with a solution of known concentration", "Temperature", "Density"], "Quantitative analysis technique."),
    ("At the equivalence point of a titration:", ["Indicator changes color", "*Moles of acid equal moles of base (stoichiometrically)", "The solution boils", "Volume doubles"], "Complete neutralization."),
    ("If a 0.10 M NaOH solution is used to titrate 25 mL of HCl and requires 30 mL:", ["HCl is 0.10 M", "*HCl is 0.12 M (0.10 x 30/25)", "HCl is 0.30 M", "HCl is 0.08 M"], "M_acid = M_base x V_base / V_acid."),
    ("When preparing a solution, dissolve solute first, then:", ["Heat to boiling", "Add exact volume of water", "*Add water to reach the desired final volume (not adding exact volume of water to the solute)", "Freeze"], "Final volume includes solute volume."),
])

# U9 L9.5: Saturated Solutions
add_qs("u9_l9.5", [
    ("A saturated solution contains:", ["No solute", "*The maximum amount of solute that can dissolve at that temperature", "Extra solvent", "Only solvent"], "No more can dissolve at that T."),
    ("An unsaturated solution:", ["Has excess solid", "*Can dissolve more solute (below maximum capacity)", "Is at maximum capacity", "Has no solvent"], "More solute can be added."),
    ("A supersaturated solution:", ["Has less solute than saturated", "*Contains MORE dissolved solute than a saturated solution normally holds at that temperature", "Is always stable", "Has no solute"], "Metastable state; excess solute can crystallize suddenly."),
    ("Supersaturated solutions are created by:", ["Adding more solvent", "*Dissolving solute at high temperature and then cooling slowly (without disturbing)", "Freezing", "Adding an acid"], "Hot solution cools without crystallizing."),
    ("Adding a seed crystal to a supersaturated solution causes:", ["Nothing", "*Rapid crystallization of the excess solute", "More dissolution", "Evaporation"], "Nucleation site triggers crystallization."),
    ("At the saturation point, dissolving and crystallization rates are:", ["Dissolving > crystallizing", "Crystallizing > dissolving", "*Equal (dynamic equilibrium between dissolving and crystallizing)", "Both zero"], "Dynamic equilibrium."),
    ("Solubility is typically expressed as:", ["mol/L only", "*grams of solute per 100 g of water (at a specified temperature)", "mL/mL", "Percent only"], "Convention: g solute / 100 g H2O."),
    ("Hand warmers use supersaturation: clicking the metal disc:", ["Heats the solution", "*Triggers crystallization of supersaturated sodium acetate, releasing heat (exothermic)", "Freezes the solution", "Adds a reagent"], "Crystallization releases stored energy."),
    ("If a saturated NaCl solution at 25°C has undissolved salt at the bottom:", ["The solution is unsaturated", "The solution is supersaturated", "*The solution is saturated with excess solid present", "More water is needed"], "Saturated + excess = equilibrium established."),
    ("Increasing temperature usually _____ the amount of solid that can dissolve.", ["Decreases", "*Increases (higher T = more dissolved at saturation)", "Has no effect", "Halves it"], "Most solids are more soluble at higher T."),
    ("Gases are _____ soluble at higher temperatures.", ["More", "*Less (gas molecules escape as temperature increases)", "Equally", "Not soluble at all"], "Thermal energy overcomes gas-solvent attractions."),
    ("Henry's Law relates gas solubility to:", ["Temperature only", "*Pressure (S = kP; more pressure = more gas dissolved)", "Concentration", "Volume"], "Proportional relationship."),
    ("Carbonated beverages are bottled under _____ to keep CO2 dissolved.", ["Low pressure", "*High pressure (increasing gas solubility per Henry's Law)", "Vacuum", "Extreme heat"], "Releasing pressure lets CO2 escape (fizz)."),
])

# U9 L9.6: Temperature & Solubility
add_qs("u9_l9.6", [
    ("For most solid solutes, solubility _____ with increasing temperature.", ["Decreases", "*Increases", "Stays constant", "Reaches zero"], "More dissolves in hotter water."),
    ("An exception: cerium sulfate (Ce2(SO4)3) _____ in solubility as temperature increases.", ["Increases", "*Decreases (one of the uncommon solids with inverse temperature dependence)", "Stays constant", "Fluctuates"], "Unusual behavior."),
    ("Dissolving is endothermic for most solids because:", ["Energy is released", "*Energy is needed to break the crystal lattice (breaking solute-solute bonds costs energy)", "Temperature drops", "It's exothermic"], "Lattice energy must be overcome."),
    ("Dissolving is exothermic when:", ["It always is", "*The energy released forming solute-solvent interactions exceeds the energy needed to separate solute and solvent particles", "Temperature decreases", "It never is"], "Hydration energy > lattice energy."),
    ("Instant cold packs dissolve _____ endothermically.", ["NaCl", "*Ammonium nitrate (NH4NO3) in water, absorbing heat", "Sugar", "Baking soda"], "Endothermic dissolution cools the pack."),
    ("Instant hot packs dissolve _____ exothermically.", ["NH4NO3", "*Calcium chloride (CaCl2) or magnesium sulfate in water, releasing heat", "NaCl", "KNO3"], "Exothermic dissolution heats the pack."),
    ("For gases, solubility _____ with increasing temperature.", ["Increases", "*Decreases (higher T gives gas particles more energy to escape solution)", "Remains same", "Depends on gas"], "Warm water holds less dissolved gas."),
    ("Thermal pollution (hot water discharge) harms aquatic life because:", ["Water is dirty", "*Dissolved oxygen decreases at higher temperatures (fish suffocate)", "Fish prefer heat", "It causes floods"], "Less O2 = stressful for aquatic organisms."),
    ("A solubility curve shows:", ["Pressure vs. temperature", "*Solubility (g solute/100g water) vs. temperature for different substances", "Volume vs. concentration", "Mass vs. time"], "Graphical tool for comparing solubilities."),
    ("On a solubility curve, points above the line represent:", ["Unsaturated solutions", "*Supersaturated solutions (contain more solute than the curve predicts at that T)", "Saturated solutions exactly", "Insoluble substances"], "Above the line = excess solute in solution."),
    ("Points below the solubility curve represent:", ["Supersaturated solutions", "Saturated solutions", "*Unsaturated solutions (could dissolve more)", "No solution"], "Below line = more can dissolve."),
    ("A substance with a steep solubility curve is _____ sensitive to temperature changes.", ["Not", "*Very (small T changes cause large solubility changes)", "Slightly", "Negatively"], "Steep slope = large effect."),
    ("Recrystallization works by:", ["Cooling unsaturated solution", "*Dissolving a solid in hot solvent then cooling to re-crystallize pure solid (impurities stay dissolved)", "Heating forever", "Adding acid"], "Purification technique using solubility differences."),
])

# U9 L9.7: Colligative Properties
add_qs("u9_l9.7", [
    ("Colligative properties depend on:", ["The identity of the solute", "The chemical formula of the solute", "*The NUMBER of dissolved particles (not their identity)", "The color of the solute"], "Quantity matters, not identity."),
    ("The four main colligative properties are:", ["Color, taste, smell, texture", "*Boiling point elevation, freezing point depression, vapor pressure lowering, and osmotic pressure", "Mass, volume, density, temperature", "pH, pOH, Ka, Kb"], "All depend on solute particle concentration."),
    ("Adding salt to water _____ the boiling point.", ["Lowers", "*Raises (boiling point elevation)", "Doesn't change", "Eliminates"], "More particles hinder evaporation."),
    ("Adding salt to ice _____ the freezing point.", ["Raises", "*Lowers (freezing point depression)", "Doesn't change", "Eliminates"], "Disrupts crystal formation."),
    ("Road salt works by:", ["Heating the road", "*Lowering the freezing point of water so ice melts at temperatures below 0 degrees C", "Insulating the ice", "Absorbing light"], "Freezing point depression in action."),
    ("Antifreeze in cars:", ["Raises freezing point", "*Lowers the freezing point and raises the boiling point of the coolant", "Has no colligative effect", "Only raises the boiling point"], "Protects engine in both cold and hot conditions."),
    ("Vapor pressure lowering occurs because:", ["Solute evaporates", "*Solute particles at the surface reduce the number of solvent molecules that can escape (fewer solvent particles at the surface)", "Temperature drops", "Volume increases"], "Raoult's Law: P = X_solvent * P°_solvent."),
    ("Osmotic pressure is the pressure needed to:", ["Evaporate a solution", "*Stop osmosis (prevent solvent from flowing through a semipermeable membrane to dilute a solution)", "Compress a gas", "Melt a solid"], "Related to dissolved particle concentration."),
    ("van't Hoff factor (i) accounts for:", ["Temperature changes", "*Dissociation of ionic compounds (number of particles produced per formula unit)", "Pressure changes", "Volume changes"], "NaCl: i = 2 (Na+ + Cl-); sugar: i = 1."),
    ("NaCl has van't Hoff factor i ≈:", ["1", "*2 (dissociates into Na+ and Cl-)", "3", "4"], "Two ions per formula unit."),
    ("CaCl2 has i ≈:", ["1", "2", "*3 (Ca2+ + 2Cl-)", "4"], "Three ions per formula unit."),
    ("Boiling point elevation: delta Tb = _____.", ["Kb x m", "*i x Kb x m (van't Hoff factor x molal boiling point constant x molality)", "Kb / m", "m / Kb"], "Full formula with i."),
    ("A 1.0 m NaCl solution has a _____ freezing point depression than a 1.0 m glucose solution.", ["Smaller", "*Greater (NaCl dissociates into 2 particles; glucose doesn't dissociate)", "Equal", "Cannot compare"], "More particles = greater effect."),
])

# U9 L9.8: Solubility Curves
add_qs("u9_l9.8", [
    ("A solubility curve plots:", ["Mass vs. volume", "*Grams of solute per 100 g water vs. temperature", "Temperature vs. pressure", "Concentration vs. time"], "Shows how much dissolves at each temperature."),
    ("On a typical solubility curve, KNO3 has a _____ slope.", ["Flat", "Slightly positive", "*Steeply positive (very temperature-sensitive)", "Negative"], "KNO3 solubility increases dramatically with T."),
    ("NaCl has a _____ solubility curve.", ["Steep", "Negative", "*Nearly flat (solubility changes little with temperature)", "Curved downward"], "NaCl dissolves about 36 g/100g from 0-100°C."),
    ("Reading a solubility curve: what is saturated at 60°C if the curve shows 110 g/100g H2O?", ["50 g in 100 g H2O", "*110 g dissolved in 100 g water (exactly what the curve indicates at that T)", "More than 110 g", "0 g"], "The curve value is the saturation point."),
    ("If you dissolve 80 g of substance X in 100 g water at 80°C, and the curve shows 100 g at 80°C:", ["Saturated", "*Unsaturated (80 < 100; could dissolve 20 more grams)", "Supersaturated", "Cannot tell"], "Below the curve = unsaturated."),
    ("Cooling the above solution to a temperature where solubility = 50 g/100g would make it:", ["Still unsaturated", "*Supersaturated (80 g dissolved but only 50 g should be at that T) until crystallization occurs", "Exactly saturated", "Dilute"], "Excess = 80 - 50 = 30 g would crystallize."),
    ("How many grams would crystallize in the above scenario?", ["50 g", "80 g", "*30 g (80 - 50 = 30 g excess)", "0 g"], "Excess above new saturation crystallizes."),
    ("Gases have _____ solubility curves (if shown).", ["Steeply increasing", "*Decreasing (less soluble at higher T)", "Flat", "No curve"], "Gas solubility decreases with T."),
    ("Using a solubility curve, you can predict whether mixing X grams at Y°C gives:", ["Color change", "*An unsaturated, saturated, or supersaturated solution", "A new compound", "Precipitation always"], "Comparison to the curve."),
    ("At the intersection of a solubility curve and a data point, the solution is:", ["Unsaturated", "*Saturated (exactly at the maximum for that temperature)", "Supersaturated", "Dilute"], "On the line = saturated."),
    ("When comparing substances on a solubility curve, the one with the highest curve at a given T is:", ["Least soluble", "*Most soluble (more grams dissolve at that temperature)", "Equally soluble", "Insoluble"], "Higher on graph = more soluble."),
    ("Solubility curves are determined experimentally by:", ["Guessing", "*Dissolving maximum amounts at various temperatures and measuring", "Calculations only", "Observation only"], "Empirical measurements at each T."),
    ("Fractional crystallization exploits:", ["Identical solubility curves", "*Different substances' solubility curves to separate them (cool a mixed solution; less-soluble substance crystallizes first)", "No temperature changes", "No solubility differences"], "Separation based on different curves."),
])

# ── UNIT 10: Acids & Bases ──

# U10 L10.1: Acid Properties
add_qs("u10_l10.1", [
    ("Acids taste:", ["Sweet", "Bitter", "*Sour", "Salty"], "Characteristic sour taste (don't taste in lab!)."),
    ("Acids turn blue litmus paper:", ["Blue", "*Red", "Green", "Orange"], "Acid = red litmus."),
    ("Acids react with metals to produce:", ["Oxides", "*Hydrogen gas (H2) and a salt", "Water only", "Oxygen gas"], "Active metals + acid -> salt + H2."),
    ("Acids produce _____ ions in water.", ["OH-", "*H+ (or H3O+, hydronium ions)", "Na+", "Cl-"], "H+ (proton) donors."),
    ("Hydrochloric acid has the formula:", ["HOCl", "*HCl", "ClOH", "H2Cl"], "Binary acid: H + Cl."),
    ("Acids are electrolytes because they:", ["Are nonpolar", "*Produce ions (H+ and anions) when dissolved in water, conducting electricity", "Are molecular", "Don't dissolve"], "Ionization creates conductive solution."),
    ("Acids react with carbonates to produce:", ["Only salt", "Only water", "*Salt, water, and CO2 gas (fizzing/bubbling)", "Only CO2"], "CaCO3 + 2HCl -> CaCl2 + H2O + CO2."),
    ("The hydrogen ion H+ in water actually exists as:", ["Free H+", "*Hydronium ion H3O+ (proton attached to water molecule)", "OH-", "H2"], "H+ + H2O -> H3O+."),
    ("Acids have pH values:", ["Greater than 7", "Equal to 7", "*Less than 7", "Greater than 14"], "Lower pH = more acidic."),
    ("Concentrated acids are more dangerous because:", ["They're colorless", "*They contain more H+ ions per volume, causing severe chemical burns", "They're dilute", "They have high pH"], "More acid = more corrosive."),
    ("Sulfuric acid (H2SO4) is a _____ acid.", ["Monoprotic", "*Diprotic (can donate 2 H+ ions per molecule)", "Triprotic", "Non-acid"], "Two ionizable hydrogens."),
    ("Which is NOT a property of acids?", ["Sour taste", "Conduct electricity", "React with metals", "*Feel slippery (this is a base property)"], "Slippery feel = bases."),
    ("Acid rain has a pH below:", ["7", "*5.6 (normal rain is slightly acidic at ~5.6 due to dissolved CO2; acid rain is lower)", "3", "10"], "Below normal rain pH."),
])

# U10 L10.2: Binary Acids
add_qs("u10_l10.2", [
    ("Binary acids contain:", ["Oxygen", "*Hydrogen bonded to a nonmetal (no oxygen)", "Three elements", "A metal"], "H + nonmetal."),
    ("The naming pattern for binary acids is:", ["Prefix + root + ic acid", "*Hydro- + root of nonmetal + -ic acid", "Root + -ous acid", "Per- + root + -ic acid"], "Hydro___ic acid."),
    ("HCl dissolved in water is named:", ["Chloric acid", "*Hydrochloric acid", "Hydrogen chloride", "Perchloric acid"], "Hydro + chlor + ic acid."),
    ("HBr dissolved in water is named:", ["Bromic acid", "*Hydrobromic acid", "Hydrogen bromide", "Perbromic acid"], "Hydro + brom + ic acid."),
    ("HF dissolved in water is named:", ["Fluoric acid", "*Hydrofluoric acid", "Hydrogen fluoride", "Perfluoric acid"], "Hydro + fluor + ic acid."),
    ("H2S dissolved in water is named:", ["Sulfuric acid", "*Hydrosulfuric acid", "Sulfurous acid", "Hydrogen sulfide gas"], "Hydro + sulfur + ic acid (in aqueous form)."),
    ("HI in water is:", ["Hydroiodic acid", "*Hydroiodic acid (correct)", "Iodic acid", "Periodic acid"], "Hydro + iod + ic acid."),
    ("When HCl is a pure gas (not in water), it's called:", ["Hydrochloric acid", "*Hydrogen chloride", "Chlorine gas", "Hydrochlorus acid"], "Named as a molecular compound when pure."),
    ("Binary acids are named differently in water vs. pure form because:", ["Convention is random", "*In water they ionize to produce H+ (acidic behavior), which the acid name reflects", "They change formula", "They change color"], "Aqueous ionization = acid naming."),
    ("The strength of binary acids _____ going down a group.", ["Decreases", "*Increases (bond gets weaker and easier to ionize as atom gets larger: HF < HCl < HBr < HI)", "Stays the same", "Varies randomly"], "Larger atom = weaker/longer H-X bond."),
    ("The strength of binary acids across a period (left to right):", ["Decreases", "*Increases (greater electronegativity = more polar H-X bond = easier to release H+)", "Stays the same", "First increases then decreases"], "More electronegative nonmetal = stronger acid."),
    ("HF is a _____ acid despite fluorine being the most electronegative element.", ["Strong", "*Weak (the H-F bond is very short and strong, harder to break despite polarity)", "Non-acid", "Neutral"], "Bond strength > polarity effect for HF."),
    ("Which is the strongest binary acid?", ["HF", "HCl", "HBr", "*HI (weakest bond, easiest to ionize)"], "Going down the group: larger atom = weaker bond = stronger acid."),
])

# U10 L10.3: Polyatomic Ion Naming
add_qs("u10_l10.3", [
    ("A polyatomic ion is:", ["A single atom with a charge", "*A group of covalently bonded atoms that carries an overall charge", "A noble gas", "A neutral molecule"], "Multiple atoms acting as one ion."),
    ("The sulfate ion has the formula:", ["SO3^2-", "*SO4^2- (sulfur bonded to four oxygens, charge -2)", "S^2-", "SO4^-"], "Common polyatomic ion."),
    ("The nitrate ion is:", ["NO2^-", "*NO3^- (nitrogen bonded to three oxygens, charge -1)", "N^3-", "NO^-"], "Nitrate = NO3-."),
    ("The carbonate ion is:", ["CO2", "CO3", "*CO3^2-", "C2O3^2-"], "Carbonate = CO3^2-."),
    ("-ate suffix means _____ oxygen than -ite suffix.", ["Fewer", "*More (e.g., sulfate SO4 vs. sulfite SO3)", "Same", "No oxygen"], "-ate has more O than -ite."),
    ("Nitrite vs. nitrate: nitrite is:", ["NO3^-", "*NO2^- (one less oxygen than nitrate)", "NO^-", "N2O^-"], "Nitrite = NO2-; nitrate = NO3-."),
    ("The prefix per- means:", ["Less oxygen than -ate", "*More oxygen than -ate (e.g., perchlorate ClO4- vs. chlorate ClO3-)", "No oxygen", "Fewer atoms"], "Per- adds one more O above -ate."),
    ("The prefix hypo- means:", ["More oxygen than -ite", "*Less oxygen than -ite (e.g., hypochlorite ClO- vs. chlorite ClO2-)", "No charge", "More charge"], "Hypo- has fewest oxygens."),
    ("The chlorine oxyanion series in order of increasing O:", ["ClO4-, ClO3-, ClO2-, ClO-", "*ClO- (hypochlorite), ClO2- (chlorite), ClO3- (chlorate), ClO4- (perchlorate)", "All have same O", "ClO3-, ClO4-, ClO-, ClO2-"], "1, 2, 3, 4 oxygens."),
    ("The hydroxide ion is:", ["OH", "HO2-", "*OH- (one oxygen + one hydrogen, charge -1)", "H2O-"], "Common base ion."),
    ("The ammonium ion is:", ["NH3", "NH2^-", "*NH4+ (four H bonded to N, positive charge)", "N2H4"], "The main positive polyatomic ion."),
    ("Phosphate ion: PO4^3- has _____ charge.", ["1-", "2-", "*3-", "4-"], "Phosphate carries -3 charge."),
    ("When naming compounds with polyatomic ions, the ion name stays:", ["Changed", "*Unchanged (the polyatomic ion keeps its name as a unit)", "Abbreviated", "Reversed"], "NaNO3 = sodium + nitrate (not nitrog-anything)."),
])

# U10 L10.4: Arrhenius Theory
add_qs("u10_l10.4", [
    ("Arrhenius defined an acid as a substance that:", ["Accepts protons", "*Produces H+ (hydrogen ions) in aqueous solution", "Produces OH-", "Reacts with metals"], "Arrhenius: acid = H+ producer."),
    ("Arrhenius defined a base as a substance that:", ["Donates protons", "Produces H+", "*Produces OH- (hydroxide ions) in aqueous solution", "Accepts electrons"], "Arrhenius: base = OH- producer."),
    ("A limitation of Arrhenius theory is that it only applies to:", ["Gases", "Solids", "*Aqueous (water) solutions", "Organic compounds"], "Doesn't explain non-aqueous acid-base behavior."),
    ("NaOH is an Arrhenius base because it:", ["Produces H+", "*Dissociates to produce Na+ and OH- in water", "Is neutral", "Is an acid"], "Sodium hydroxide releases OH-."),
    ("HNO3 is an Arrhenius acid because it:", ["Produces OH-", "*Ionizes to produce H+ and NO3- in water", "Is a base", "Is neutral"], "Nitric acid releases H+."),
    ("Bronsted-Lowry theory expanded the acid definition to:", ["Electron pair donors", "*Proton (H+) donors (not limited to aqueous solutions)", "OH- producers", "Metal dissolvers"], "Broader: any proton transfer."),
    ("Bronsted-Lowry bases are _____ acceptors.", ["Electron", "*Proton (H+)", "Hydroxide", "Water"], "Base accepts a proton."),
    ("Lewis acids are _____ pair acceptors.", ["Proton", "Hydroxide", "*Electron pair", "Ion"], "Broadest definition."),
    ("Lewis bases are _____ pair donors.", ["Proton", "Hydroxide", "*Electron pair", "Ion"], "Donate a lone pair."),
    ("NH3 acts as a Bronsted-Lowry base by:", ["Releasing OH-", "*Accepting a proton (H+) from water to form NH4+ and OH-", "Releasing H+", "Not reacting"], "NH3 + H2O -> NH4+ + OH-."),
    ("Conjugate acid-base pairs differ by:", ["An OH-", "*One proton (H+)", "An electron", "A neutron"], "Conjugate pair: one has one more H+."),
    ("The conjugate acid of NH3 is:", ["NH2-", "*NH4+", "N2H4", "NO3-"], "NH3 + H+ = NH4+."),
    ("Water can act as both an acid and a base. This property is called:", ["Neutralization", "*Amphoteric (or amphiprotic)", "Equilibrium", "Ionization"], "Water can donate or accept H+."),
])

# U10 L10.5: Strong vs. Weak Acids
add_qs("u10_l10.5", [
    ("A strong acid _____ completely in water.", ["Partially ionizes", "*Ionizes completely (100% of molecules dissociate into ions)", "Doesn't ionize", "Sometimes ionizes"], "Complete ionization."),
    ("A weak acid _____ in water.", ["Ionizes completely", "*Partially ionizes (equilibrium between ionized and un-ionized forms)", "Never ionizes", "Decomposes"], "Equilibrium between HA and H+/A-."),
    ("Which is a strong acid?", ["CH3COOH (acetic acid)", "HF (hydrofluoric acid)", "*HCl (hydrochloric acid)", "H2CO3 (carbonic acid)"], "HCl is one of the 6-7 strong acids."),
    ("The six common strong acids include: HCl, HBr, HI, H2SO4, HNO3, and:", ["HF", "*HClO4 (perchloric acid)", "CH3COOH", "H3PO4"], "The standard list of strong acids."),
    ("Ka (acid dissociation constant) measures:", ["Base strength", "*Acid strength (larger Ka = stronger acid = more ionization)", "Concentration", "Temperature"], "Ka = [H+][A-]/[HA] at equilibrium."),
    ("For strong acids, Ka is:", ["Very small", "Equal to 1", "*Very large (essentially infinite, since ionization is complete)", "Zero"], "Complete ionization = huge Ka."),
    ("For weak acids, Ka is:", ["Very large", "Infinite", "*Small (much less than 1, indicating partial ionization)", "Exactly 1"], "Small Ka = little ionization."),
    ("Acetic acid (CH3COOH) in water reaches equilibrium. Its Ka ≈ 1.8 x 10^-5, making it:", ["Strong", "*Weak (small Ka indicates limited ionization)", "Neutral", "A base"], "Small Ka = weak acid."),
    ("Strong bases include:", ["NH3", "*NaOH, KOH, Ca(OH)2 (Group 1 and 2 hydroxides)", "CH3OH", "Al(OH)3"], "Alkali and alkaline earth hydroxides."),
    ("A weak base has a small:", ["Ka", "*Kb (base dissociation constant)", "pH", "pOH"], "Kb measures base strength."),
    ("The stronger the acid, the _____ the conjugate base.", ["Stronger", "*Weaker (strong acid's conjugate base can't re-accept the proton easily)", "Same strength", "More dangerous"], "Inverse relationship."),
    ("Concentrated does NOT mean strong: concentrated HF is:", ["A strong acid", "*Still a weak acid (concentration affects amount, not degree of ionization)", "A strong base", "Neutral"], "Strength ≠ concentration."),
    ("Percent ionization = (ionized concentration / initial concentration) x 100. For a strong acid, this is:", ["Variable", "*~100%", "~1%", "~50%"], "Complete ionization."),
])

# U10 L10.6: Neutralization
add_qs("u10_l10.6", [
    ("Neutralization is the reaction between:", ["Two acids", "Two bases", "*An acid and a base (producing water and a salt)", "A metal and a nonmetal"], "Acid + base -> salt + water."),
    ("The general equation: acid + base -> _____ + _____.", ["Gas + precipitate", "*Salt + water", "Acid + base", "Metal + nonmetal"], "Products are salt (ionic compound) and water."),
    ("HCl + NaOH -> NaCl + H2O is a:", ["Synthesis", "Decomposition", "*Neutralization (acid + base -> salt + water)", "Redox"], "Classic neutralization."),
    ("H2SO4 + 2NaOH -> Na2SO4 + 2H2O requires 2 NaOH because:", ["NaOH is weak", "*H2SO4 is diprotic (provides 2 H+ ions, needing 2 OH- to neutralize)", "Na requires 2", "Water needs 2"], "Two H+ need two OH-."),
    ("At the equivalence point of a neutralization:", ["pH is always 7", "*Moles of H+ = moles of OH- (stoichiometrically balanced; pH depends on salt formed)", "Excess acid remains", "Excess base remains"], "Complete neutralization of all H+ and OH-."),
    ("The net ionic equation for strong acid + strong base neutralization is:", ["NaCl -> Na+ + Cl-", "*H+ + OH- -> H2O (spectator ions cancel out)", "Na + Cl -> NaCl", "H2 + O -> H2O"], "H+ and OH- combine to form water."),
    ("Antacids neutralize stomach acid by:", ["Adding more acid", "*Providing a base (like CaCO3, Mg(OH)2, or NaHCO3) to react with excess HCl", "Cooling the stomach", "Adding enzymes"], "Base neutralizes excess acid."),
    ("The heat produced during neutralization is called:", ["Heat of fusion", "Heat of vaporization", "*Heat of neutralization (approximately -57.1 kJ/mol for strong acid + strong base)", "Heat of combustion"], "Exothermic reaction."),
    ("A titration curve shows:", ["Color vs. temperature", "*pH vs. volume of titrant added, showing the equivalence point", "Mass vs. time", "Concentration vs. temperature"], "Graphical representation of titration progress."),
    ("Indicators change color at specific pH ranges, such as phenolphthalein which turns pink in:", ["Acid (pH < 7)", "*Base (pH > 8.2, approximately)", "Neutral solution", "Any solution"], "Phenolphthalein: colorless in acid, pink in base."),
    ("Weak acid + strong base at equivalence point has pH:", ["= 7", "*> 7 (conjugate base of weak acid makes solution basic)", "< 7", "= 0"], "Conjugate base hydrolyzes water."),
    ("Strong acid + weak base at equivalence point has pH:", ["= 7", "> 7", "*< 7 (conjugate acid of weak base makes solution acidic)", "= 14"], "Conjugate acid hydrolyzes water."),
    ("Polyprotic acids (like H3PO4) have _____ equivalence point(s).", ["1", "2", "*3 (one for each ionizable proton)", "0"], "H3PO4 can lose 3 protons sequentially."),
])

# U10 L10.7: Salts
add_qs("u10_l10.7", [
    ("A salt is the ionic compound produced by:", ["Evaporation", "*The reaction of an acid with a base (neutralization)", "Combustion", "Decomposition"], "Acid + base -> salt + water."),
    ("NaCl (table salt) comes from:", ["Mining only", "Ocean only", "*Both mining (rock salt) and neutralization of HCl + NaOH, plus ocean evaporation", "Neither"], "Multiple sources."),
    ("Salts from strong acid + strong base solutions are:", ["Always acidic", "Always basic", "*Neutral (neither ion hydrolyzes water significantly)", "Always colored"], "Strong + strong = neutral salt."),
    ("Salts from weak acid + strong base are:", ["Neutral", "*Basic (the conjugate base anion hydrolyzes water, producing OH-)", "Acidic", "Insoluble"], "Anion hydrolysis makes it basic."),
    ("Salts from strong acid + weak base are:", ["Neutral", "Basic", "*Acidic (the conjugate acid cation hydrolyzes water, producing H+)", "Insoluble"], "Cation hydrolysis makes it acidic."),
    ("NH4Cl in water is _____ because:", ["Basic; Cl- hydrolyzes", "*Acidic; NH4+ donates a proton to water (conjugate acid of weak base NH3)", "Neutral; no hydrolysis", "Insoluble"], "NH4+ is a weak acid."),
    ("NaCH3COO (sodium acetate) in water is _____ because:", ["Acidic", "*Basic; CH3COO- accepts a proton from water (conjugate base of weak acetic acid)", "Neutral", "Insoluble"], "Acetate ion hydrolyzes to form OH-."),
    ("Hydrolysis is the reaction of an ion with:", ["Acid", "Base", "*Water (to produce H+ or OH-)", "Another salt"], "Ion + H2O -> modified pH."),
    ("Solubility of salts varies: _____ salts are generally soluble.", ["All", "No", "*Most sodium, potassium, ammonium, and nitrate", "Most carbonates"], "Group 1 and NH4+ salts are generally soluble."),
    ("Generally insoluble salts include most:", ["Sodium salts", "Nitrate salts", "*Carbonates, phosphates, and sulfides (except with Group 1/NH4+)", "Chloride salts"], "Common insoluble anions."),
    ("A precipitate forms when _____ combine in solution.", ["Soluble ions", "*Insoluble ion combinations (according to solubility rules)", "Acids and bases always", "Only gases"], "Exceeding Ksp causes precipitation."),
    ("The solubility product (Ksp) represents:", ["Total concentration", "*The equilibrium constant for dissolving a slightly soluble salt (product of ion concentrations raised to powers)", "Reaction rate", "pH"], "Ksp = [cation]^m[anion]^n for a saturated solution."),
    ("Double replacement (metathesis) reactions often produce:", ["Only gases", "Only water", "*A precipitate, gas, or water (driving forces for the reaction to proceed)", "No products"], "Something must leave solution."),
])

# U10 L10.8: Buffers
add_qs("u10_l10.8", [
    ("A buffer is a solution that:", ["Amplifies pH changes", "*Resists changes in pH when small amounts of acid or base are added", "Has no pH", "Is always neutral"], "pH stabilizer."),
    ("Buffers consist of:", ["Two strong acids", "Two strong bases", "*A weak acid and its conjugate base (or a weak base and its conjugate acid)", "A strong acid and a strong base"], "Conjugate pair system."),
    ("The CH3COOH/CH3COO- buffer: added H+ reacts with:", ["CH3COOH", "*CH3COO- (the conjugate base neutralizes the added acid)", "Water only", "Nothing"], "Base component absorbs acid."),
    ("In the same buffer, added OH- reacts with:", ["CH3COO-", "*CH3COOH (the weak acid neutralizes the added base)", "Water only", "Nothing"], "Acid component absorbs base."),
    ("The Henderson-Hasselbalch equation: pH = pKa + log([A-]/[HA]). When [A-] = [HA]:", ["pH = 0", "pH = 14", "*pH = pKa (the log term is zero)", "pH = 7"], "Equal concentrations: log(1) = 0."),
    ("Buffer capacity is:", ["The pH of the buffer", "*The amount of acid or base a buffer can absorb before pH changes significantly", "The volume", "The color"], "Depends on concentrations of buffer components."),
    ("A buffer works best when pH is within _____ unit(s) of pKa.", ["2", "*1 (effective pH range: pKa ± 1)", "3", "0.5"], "Buffer effective range."),
    ("Blood pH is maintained at approximately:", ["6.0", "8.0", "*7.4 (by the carbonic acid/bicarbonate buffer system)", "7.0"], "H2CO3/HCO3- buffer in blood."),
    ("The carbonic acid buffer: H2CO3 <=> H+ + HCO3-. When blood becomes too acidic:", ["HCO3- is removed", "*HCO3- combines with excess H+ to form H2CO3 (then CO2 + H2O, exhaled as CO2)", "H2CO3 increases", "Nothing happens"], "Bicarbonate neutralizes excess acid."),
    ("When blood becomes too basic:", ["More HCO3- is added", "*H2CO3 dissociates to release H+ (or breathing slows to retain CO2)", "pH increases further", "Nothing happens"], "Carbonic acid releases protons."),
    ("Buffer solutions are essential in:", ["Only blood", "Only labs", "*Biological systems (blood, cells), industrial processes, and laboratory work", "Cooking only"], "Wide applications."),
    ("Phosphate buffer (H2PO4-/HPO4^2-) is important in:", ["Blood plasma mainly", "*Intracellular fluids (cells)", "Ocean chemistry", "Food only"], "Main intracellular buffer."),
    ("Adding a large excess of strong acid to a buffer will:", ["Have no effect", "Make the buffer stronger", "*Overwhelm the buffer capacity and cause pH to drop sharply", "Raise pH"], "Buffers have finite capacity."),
])

# U10 L10.9: pH Scale
add_qs("u10_l10.9", [
    ("The pH scale typically ranges from:", ["1 to 10", "*0 to 14 (though values outside this range are possible)", "0 to 7", "7 to 14"], "0 (very acidic) to 14 (very basic)."),
    ("A solution with pH = 7 is:", ["Acidic", "Basic", "*Neutral (equal H+ and OH- concentrations)", "Unknown"], "Pure water at 25°C."),
    ("A solution with pH = 3 is:", ["Basic", "Neutral", "*Acidic (high H+ concentration)", "Very basic"], "pH < 7 = acidic."),
    ("A solution with pH = 11 is:", ["Acidic", "Neutral", "*Basic (low H+ concentration, high OH-)", "Very acidic"], "pH > 7 = basic."),
    ("Each unit decrease in pH represents a _____ increase in H+ concentration.", ["2x", "5x", "*10x (tenfold, because pH is logarithmic)", "100x"], "pH is a log scale."),
    ("pH 3 has _____ times more H+ than pH 5.", ["2", "5", "10", "*100 (10^2, since the difference is 2 pH units)"], "10^(5-3) = 100x."),
    ("pOH measures:", ["Acid strength", "*Hydroxide ion concentration (pOH = -log[OH-])", "Temperature", "Volume"], "Analogous to pH but for OH-."),
    ("pH + pOH = _____ at 25 degrees C.", ["7", "*14", "10", "1"], "Fundamental relationship at 25°C."),
    ("If pH = 4, pOH = _____.", ["4", "*10 (14 - 4)", "7", "0"], "pOH = 14 - pH."),
    ("A pH of 1 is _____ than a pH of 2.", ["Less acidic", "Equally acidic", "*More acidic (10x more H+ ions)", "More basic"], "Lower pH = more acidic."),
    ("Common substances: lemon juice has pH ~_____, while bleach has pH ~_____.", ["7; 14", "*2; 13", "5; 8", "1; 7"], "Very acidic; very basic."),
    ("pH meters measure pH by:", ["Color change", "*Measuring the voltage difference between a reference and a glass electrode immersed in the solution", "Taste", "Temperature"], "Electrochemical measurement."),
    ("pH indicators like universal indicator change _____ across the pH range.", ["Size", "Smell", "*Color (different colors at different pH values)", "Volume"], "Visual pH estimation."),
])

# U10 L10.10: pH Calculations
add_qs("u10_l10.10", [
    ("pH = -log[H+]. If [H+] = 1 x 10^-4 M, pH =:", ["4 x 10^-1", "10^4", "*4", "0.0001"], "-log(10^-4) = 4."),
    ("If pH = 9, [H+] = :", ["9 M", "*1 x 10^-9 M", "1 x 10^9 M", "10^-5 M"], "[H+] = 10^(-pH) = 10^-9."),
    ("[OH-] = Kw / [H+], where Kw = :", ["1 x 10^-7", "*1 x 10^-14 (at 25 degrees C)", "7", "14"], "Water's autoionization constant."),
    ("If [H+] = 1 x 10^-3 M, [OH-] = :", ["1 x 10^-3 M", "*1 x 10^-11 M (10^-14 / 10^-3)", "1 x 10^-7 M", "1 x 10^-14 M"], "Kw / [H+] = OH-."),
    ("pOH = -log[OH-]. If [OH-] = 1 x 10^-5, pOH = :", ["5 x 10^-1", "*5", "9", "-5"], "-log(10^-5) = 5, and pH = 14-5 = 9."),
    ("For a 0.01 M HCl (strong acid) solution, pH = :", ["0.01", "*2 (-log(0.01) = -log(10^-2) = 2)", "12", "7"], "Strong acid: [H+] = 0.01 M = 10^-2."),
    ("For a 0.001 M NaOH (strong base), pOH = :", ["11", "*3 (-log(0.001) = 3), and pH = 11", "3", "7"], "Strong base: [OH-] = 10^-3, pOH = 3, pH = 11."),
    ("pH of pure water at 25°C:", ["0", "14", "*7.0 ([H+] = [OH-] = 10^-7)", "1.0"], "Neutral water."),
    ("For weak acids, pH calculation requires:", ["Just concentration", "Just Ka", "*Both initial concentration and Ka (using ICE table or quadratic approximation)", "Only pKa"], "Equilibrium calculation needed."),
    ("For 0.10 M acetic acid (Ka = 1.8 x 10^-5), [H+] = sqrt(Ka x C) ≈:", ["0.10 M", "*1.34 x 10^-3 M (sqrt(1.8e-5 x 0.10)), so pH ≈ 2.87", "1.8 x 10^-5 M", "0.50 M"], "Weak acid approximation."),
    ("For a diprotic acid (H2SO4), the first ionization is _____ and the second is _____.", ["Both weak", "*Strong (complete); weaker (partial for HSO4- -> SO4^2-)", "Both strong", "Neither ionizes"], "First H+ fully dissociates; second partially."),
    ("Significant figures in pH: pH = 2.00 has _____ significant figures in the mantissa.", ["1", "*2 (the digits after the decimal point represent sig figs from the concentration)", "3", "4"], "Only decimal places count for sig figs in log values."),
    ("If you mix 50 mL of 0.10 M HCl with 50 mL of 0.10 M NaOH, the pH is:", ["1", "13", "*7 (complete neutralization; equal moles of strong acid and strong base)", "0"], "Perfect neutralization → neutral solution."),
])

# ── UNIT 11: Thermochemistry ──

# U11 L11.1: Heat Energy
add_qs("u11_l11.1", [
    ("Heat is energy that flows due to:", ["Mass difference", "Volume change", "*Temperature difference between objects", "Color difference"], "Heat flows from hot to cold."),
    ("Temperature measures:", ["Total energy", "Heat content", "*Average kinetic energy of particles", "Mass of particles"], "How fast particles move on average."),
    ("Heat and temperature are:", ["The same thing", "Unrelated", "*Related but different (heat is energy transfer; temperature is intensity of energy)", "Identical in SI units"], "Heat = energy transferred; temperature = energy per particle."),
    ("The SI unit of heat energy is:", ["Celsius", "Calorie", "*Joule (J)", "Kelvin"], "Joule is the SI energy unit."),
    ("1 calorie = _____ joules.", ["1.00 J", "*4.184 J (exactly)", "0.239 J", "100 J"], "Conversion factor."),
    ("A food Calorie (capital C) = _____ calories (small c).", ["1", "10", "*1000 (1 kcal)", "100"], "1 Calorie = 1 kilocalorie."),
    ("Endothermic processes _____ heat from surroundings.", ["Release", "*Absorb (surroundings feel cooler)", "Destroy", "Create"], "Energy flows into the system."),
    ("Exothermic processes _____ heat to surroundings.", ["Absorb", "*Release (surroundings feel warmer)", "Destroy", "Create"], "Energy flows out of the system."),
    ("Melting ice is _____ (absorbs heat from surroundings).", ["Exothermic", "*Endothermic", "Neither", "Nuclear"], "Ice needs energy to melt."),
    ("Burning fuel is _____ (releases heat to surroundings).", ["Endothermic", "*Exothermic", "Neither", "Nuclear"], "Combustion releases energy."),
    ("The system is the part being:", ["Surrounding the experiment", "*Studied (the reaction or process itself)", "Ignored", "Unchanged"], "System = what you're studying."),
    ("The surroundings are everything _____ the system.", ["Inside", "*Outside (the environment around the reaction)", "Equal to", "Part of"], "Everything the system interacts with."),
    ("In q = mCdeltaT, a negative q means:", ["Heat was absorbed", "*Heat was released by the system (exothermic)", "Temperature increased", "No heat change"], "Negative q = exothermic."),
])

# U11 L11.2: Specific Heat
add_qs("u11_l11.2", [
    ("Specific heat is the amount of heat needed to raise 1 gram of a substance by:", ["10 degrees C", "*1 degree C (or 1 Kelvin)", "100 degrees C", "1000 degrees C"], "Energy per gram per degree."),
    ("Water's specific heat is:", ["1.0 J/g°C", "*4.184 J/g°C (unusually high for a common substance)", "2.0 J/g°C", "0.5 J/g°C"], "Water stores a lot of heat energy."),
    ("Water's high specific heat means:", ["It heats quickly", "*It resists temperature changes (takes a lot of energy to heat or cool)", "It freezes easily", "It boils at low temperature"], "Moderates temperature."),
    ("Metals generally have _____ specific heat compared to water.", ["Higher", "*Lower (they heat up and cool down quickly)", "Equal", "No comparable value"], "Metals have low specific heats."),
    ("The formula for heat transfer: q = _____.", ["mCT", "mC/T", "*mCdeltaT (mass x specific heat x temperature change)", "C/mT"], "Fundamental heat equation."),
    ("Calculate q: 100 g of water heated from 20°C to 70°C:", ["500 J", "1000 J", "*20,920 J (100 x 4.184 x 50)", "4184 J"], "q = 100 × 4.184 × 50 = 20,920 J."),
    ("How much heat to raise 50 g of aluminum (C=0.897 J/g°C) by 10°C?", ["897 J", "*448.5 J (50 x 0.897 x 10)", "89.7 J", "4485 J"], "q = 50 × 0.897 × 10 = 448.5 J."),
    ("If 5000 J heats 200 g of water, deltaT = :", ["25°C", "12°C", "*5.98°C (5000/(200 x 4.184))", "50°C"], "deltaT = q/(mC) = 5000/836.8 ≈ 5.98°C."),
    ("Specific heat is an _____ property.", ["Extensive", "*Intensive (does not depend on the amount of substance)", "Chemical", "Nuclear"], "Characteristic of the material."),
    ("Coastal areas have milder climates because:", ["Wind is constant", "*Water (high specific heat) absorbs and releases large amounts of heat slowly, moderating temperatures", "Ocean is salty", "Land heats faster"], "Ocean's thermal mass regulates climate."),
    ("In a specific heat experiment, the metal and water reach:", ["Different final temperatures", "*The same final temperature (thermal equilibrium)", "Absolute zero", "Boiling point"], "Heat flows until temperatures equalize."),
    ("q_lost by hot object = q_gained by cool object (assuming no heat loss), so:", ["m1C1deltaT1 > m2C2deltaT2", "m1C1deltaT1 < m2C2deltaT2", "*m1C1deltaT1 = m2C2deltaT2 (conservation of energy)", "No relationship"], "Heat exchanged is equal."),
    ("Units of specific heat are:", ["J/g", "J/°C", "*J/(g·°C) or J/(g·K)", "J·g/°C"], "Energy per mass per degree."),
])

# U11 L11.3: Heat Capacity
add_qs("u11_l11.3", [
    ("Heat capacity (C) is the amount of heat to raise a _____ by 1°C.", ["Gram", "Mole", "*Whole object or sample", "Liter"], "Total object, not per gram."),
    ("Heat capacity = mass x _____.", ["Temperature", "*Specific heat (C = m × c)", "Volume", "Pressure"], "Scales with amount."),
    ("A 500 g block of iron (c=0.449 J/g°C) has heat capacity:", ["449 J/°C", "0.449 J/°C", "*224.5 J/°C (500 x 0.449)", "4490 J/°C"], "C = m × c."),
    ("Heat capacity is an _____ property.", ["Intensive", "*Extensive (depends on the amount of material)", "Chemical", "Constant"], "More material = higher heat capacity."),
    ("Molar heat capacity is heat capacity per:", ["Gram", "Liter", "*Mole of substance", "Atom"], "C_m = J/(mol·°C)."),
    ("A large body of water has _____ heat capacity than a small pool.", ["Lower", "*Higher (more mass = more heat needed to change temperature)", "Equal", "No"], "More water = more thermal energy storage."),
    ("The heat capacity of a calorimeter must be known to:", ["Measure mass", "*Account for heat absorbed by the calorimeter itself in heat calculations", "Determine color", "Find density"], "Calorimeter constant corrects for this."),
    ("If a calorimeter has C = 15 J/°C and temperature rises 5°C, the calorimeter absorbed:", ["15 J", "5 J", "*75 J (15 x 5)", "150 J"], "q = C × deltaT."),
    ("Dulong-Petit law approximates molar heat capacity of solid elements at:", ["0 K", "*Room temperature (approximately 25 J/(mol·K) or 3R)", "1000 K", "100 K"], "Classical approximation."),
    ("The specific heat of steam (2.01 J/g°C) is _____ than liquid water's.", ["Higher", "*Lower (steam needs less energy per gram per degree because weaker intermolecular interactions in gas phase)", "Equal", "Variable"], "Phase affects specific heat."),
    ("The specific heat of ice (2.09 J/g°C) is _____ than liquid water's.", ["Higher", "*Lower", "Equal", "Negative"], "Solid phase has different heat capacity."),
    ("When choosing a coolant, high specific heat is desirable because:", ["It cools quickly", "*It absorbs more heat per unit mass per degree (more effective heat absorption)", "It's cheaper", "It weighs more"], "Better thermal energy storage."),
    ("In bomb calorimetry, the heat capacity of the bomb:", ["Is negligible", "*Must be precisely known and included in calculations (bomb constant)", "Is always zero", "Equals water's"], "Precise constant needed."),
])

# U11 L11.4: Calorimetry
add_qs("u11_l11.4", [
    ("Calorimetry is the measurement of:", ["Volume changes", "Pressure changes", "*Heat changes in chemical or physical processes", "Color changes"], "Quantifying heat transfer."),
    ("A coffee-cup calorimeter measures heat at:", ["Constant volume", "*Constant pressure (open to atmosphere)", "Constant temperature", "Constant mass"], "Open system = constant P."),
    ("A bomb calorimeter measures heat at:", ["Constant pressure", "*Constant volume (sealed rigid container)", "Constant temperature", "Both P and V change"], "Sealed = constant V."),
    ("In coffee-cup calorimetry, q_rxn = _____.", ["mCdeltaT", "-q_calorimeter", "*-(m_water × C_water × deltaT) (opposite sign because heat lost by reaction is gained by water)", "Zero"], "Heat of reaction = negative of heat gained by surroundings."),
    ("If the water temperature rises, the reaction is:", ["Endothermic", "*Exothermic (reaction releases heat to water, warming it)", "Neither", "Nuclear"], "Hot water = exothermic reaction."),
    ("If the water temperature drops, the reaction is:", ["Exothermic", "*Endothermic (reaction absorbs heat from water, cooling it)", "Neither", "Nuclear"], "Cold water = endothermic reaction."),
    ("In a calorimetry experiment, 100 mL of water (initially 22.0°C) rises to 28.5°C:", ["q = 0 J", "q = 650 J", "*q = 2720 J (100 × 4.184 × 6.5 = 2720)", "q = 100 J"], "q = 100 × 4.184 × 6.5 ≈ 2720 J."),
    ("The calorimeter constant is determined by:", ["Measuring the mass", "Estimating from materials", "*Running a reaction with known heat output and measuring the temperature change", "It's always zero"], "Calibration procedure."),
    ("Constant-pressure calorimetry gives:", ["Internal energy change (deltaU)", "*Enthalpy change (deltaH) directly", "Free energy change", "Work done"], "At constant P: q_p = deltaH."),
    ("Constant-volume calorimetry gives:", ["Enthalpy directly", "*Internal energy change (deltaU = q_v, since no PV work at constant V)", "Free energy", "Equilibrium constant"], "At constant V: no pressure-volume work."),
    ("Sources of error in calorimetry include:", ["Perfect insulation", "*Heat loss to surroundings, imprecise temperature readings, and heat absorbed by the calorimeter walls", "None possible", "Only human error"], "Real calorimeters aren't perfect."),
    ("When mixing hot metal with cold water in a calorimeter, assume:", ["Heat is created", "Heat is destroyed", "*q_metal = -q_water (heat lost by metal = heat gained by water, if insulation is perfect)", "No heat transfer"], "Conservation of energy."),
    ("Specific heat of an unknown metal can be found by:", ["Weighing it", "Measuring its volume", "*Heating it to a known T, adding to water in a calorimeter, and measuring final T (using q_metal = -q_water to solve for c)", "Magic"], "Classic calorimetry experiment."),
])

# U11 L11.5: Enthalpy
add_qs("u11_l11.5", [
    ("Enthalpy (H) is defined as:", ["Heat only", "*The total heat content of a system at constant pressure (H = U + PV)", "Temperature only", "Kinetic energy only"], "Thermodynamic state function."),
    ("deltaH < 0 means the reaction is:", ["Endothermic", "*Exothermic (releases heat to surroundings)", "At equilibrium", "Spontaneous necessarily"], "Negative enthalpy change = heat released."),
    ("deltaH > 0 means the reaction is:", ["Exothermic", "*Endothermic (absorbs heat from surroundings)", "At equilibrium", "Impossible"], "Positive enthalpy change = heat absorbed."),
    ("Standard enthalpy of formation (deltaH_f°) is the enthalpy change when:", ["Any compound forms", "*One mole of a compound forms from its elements in their standard states (25°C, 1 atm)", "A compound decomposes", "An element changes phase"], "Standard formation conditions."),
    ("The standard enthalpy of formation of any element in its standard state is:", ["Variable", "1 kJ/mol", "*Zero (by definition, the reference point)", "Cannot be measured"], "Elements in standard state: deltaH_f° = 0."),
    ("Enthalpy is a state function, meaning it depends on:", ["The path taken", "*Only the initial and final states (not how you get there)", "The speed of the reaction", "The catalyst used"], "Path-independent."),
    ("Standard conditions for enthalpy: temperature = _____ and pressure = _____.", ["0°C, 1 atm", "*25°C (298 K), 1 atm (or 1 bar)", "100°C, 1 atm", "STP (0°C, 1 atm)"], "Standard state ≠ STP."),
    ("Bond breaking _____ energy; bond forming _____ energy.", ["Releases; absorbs", "*Requires (absorbs); releases", "Neither requires nor releases", "Both require"], "Breaking bonds is endothermic; forming is exothermic."),
    ("For an exothermic reaction, the products have _____ enthalpy than the reactants.", ["Higher", "*Lower (energy was released)", "Equal", "Variable"], "Products more stable."),
    ("Energy diagrams for endothermic reactions show products:", ["Below reactants", "*Above reactants (products have more energy)", "At the same level", "Cannot be drawn"], "Energy goes up from reactants to products."),
    ("deltaH_rxn = sum(deltaH_f° products) - sum(deltaH_f° reactants). This uses:", ["Hess's law", "Le Chatelier's principle", "*Standard enthalpies of formation", "Ideal gas law"], "Formation enthalpy method."),
    ("For 2H2(g) + O2(g) -> 2H2O(l), deltaH = -572 kJ. Per mole of H2O:", ["572 kJ", "*-286 kJ (divide by 2 since 2 moles water formed)", "-572 kJ", "286 kJ"], "Half the total for 1 mol product."),
    ("Enthalpy changes are extensive: doubling the reaction amounts _____ deltaH.", ["Halves", "*Doubles", "Has no effect", "Squares"], "Proportional to amount of reaction."),
])

# U11 L11.6: Hess's Law
add_qs("u11_l11.6", [
    ("Hess's Law states that the total enthalpy change is:", ["Path-dependent", "*The same regardless of the path taken (sum of steps equals the overall change)", "Always zero", "Always negative"], "State function property."),
    ("If a reaction is reversed, deltaH:", ["Stays the same", "Doubles", "*Changes sign (exothermic becomes endothermic and vice versa)", "Becomes zero"], "Reverse reaction has opposite deltaH."),
    ("If a reaction is multiplied by 2, deltaH:", ["Stays the same", "*Doubles (enthalpy is proportional to amount)", "Halves", "Becomes zero"], "Scale coefficients = scale deltaH."),
    ("Hess's Law is useful because:", ["All reactions can be measured directly", "It's simple arithmetic", "*Some reactions are too slow, dangerous, or impractical to measure directly, so we calculate deltaH from known steps", "It always gives zero"], "Indirect determination of enthalpy."),
    ("Given: A->B (deltaH=+50kJ) and B->C (deltaH=-30kJ). A->C deltaH = :", ["80 kJ", "30 kJ", "*+20 kJ (+50 + (-30))", "-20 kJ"], "Sum of steps."),
    ("Given: C->D (deltaH=-100kJ). Find D->C deltaH:", ["-100 kJ", "0 kJ", "*+100 kJ (reverse the sign)", "-200 kJ"], "Reversed reaction."),
    ("Using Hess's Law with formation enthalpies: deltaH°rxn = sum(deltaH°f products) - sum(deltaH°f reactants). If deltaH°f(CO2)=-393.5 and deltaH°f(CO)=-110.5, for CO + 1/2O2 -> CO2:", ["-393.5 kJ", "-110.5 kJ", "*-283.0 kJ (-393.5 - (-110.5))", "504 kJ"], "-393.5 - (-110.5) = -283.0 kJ."),
    ("Bond enthalpy method: deltaH ≈ sum(bonds broken) - sum(bonds formed). Breaking bonds is:", ["Exothermic", "*Endothermic (positive energy input)", "Neutral", "Nuclear"], "Energy needed to break bonds."),
    ("If bonds broken = +800 kJ and bonds formed = -1000 kJ, deltaH ≈:", ["+1800 kJ", "*-200 kJ (reaction is exothermic; more energy released forming bonds than consumed breaking them)", "+200 kJ", "0 kJ"], "800 + (-1000) = -200 kJ."),
    ("Germain Hess formulated this law in:", ["1740", "1940", "*1840 (Hess's law of constant heat summation)", "1990"], "Published in 1840."),
    ("Hess's Law is a consequence of enthalpy being a:", ["Path function", "*State function (depends only on initial and final states)", "Variable", "Constant"], "Independent of path."),
    ("Calorimetry data combined with Hess's Law can determine:", ["Only simple reactions", "*Enthalpy changes for virtually any reaction (even those that can't be directly measured)", "Only combustion", "Nothing useful"], "Powerful combination."),
    ("Born-Haber cycle uses Hess's Law to analyze:", ["Organic reactions", "Gas laws", "*Formation of ionic compounds (lattice energy and other steps)", "Acid-base reactions"], "Steps: sublimation, ionization, electron affinity, lattice energy."),
])

# ── UNIT 12: Nuclear Chemistry ──

# U12 L12.1: Nuclear Fission
add_qs("u12_l12.1", [
    ("Nuclear fission is the splitting of a _____ nucleus into smaller nuclei.", ["Small", "*Large (heavy)", "Any", "Stable"], "Heavy nuclei split in fission."),
    ("Fission releases energy because the products have _____ binding energy per nucleon.", ["Less", "*More (products are more stable; mass is converted to energy)", "Equal", "No"], "Moving toward iron = more stable."),
    ("The most common fissile isotope used in reactors is:", ["U-238", "Pu-240", "*U-235 (absorbs slow neutrons and splits)", "C-14"], "Uranium-235 is fissile."),
    ("A chain reaction occurs when neutrons from one fission event:", ["Are absorbed", "Escape", "*Trigger additional fissions in nearby nuclei", "Become protons"], "Self-sustaining process."),
    ("A nuclear reactor controls the chain reaction using:", ["Water only", "*Control rods (absorb excess neutrons to manage reaction rate)", "Fuel rods only", "Heat"], "Control rods regulate neutron flux."),
    ("The moderator in a reactor (like water or graphite) _____ neutrons.", ["Absorbs", "Creates", "*Slows down (thermal neutrons are more effective at causing fission of U-235)", "Speeds up"], "Thermal neutrons = more fission."),
    ("E = mc^2 explains how a small mass loss in fission produces:", ["Little energy", "*Enormous energy (mass converts to energy; c^2 is very large)", "No energy", "Chemical energy only"], "Einstein's mass-energy equivalence."),
    ("Fission products are often:", ["Stable elements", "*Radioactive isotopes (requiring careful waste management)", "Noble gases only", "Harmless"], "Radioactive waste is a major concern."),
    ("Nuclear power plants use fission to:", ["Create new elements", "Split water directly", "*Generate heat, which produces steam to drive turbines and generators", "Produce light directly"], "Heat -> steam -> turbine -> electricity."),
    ("Critical mass is the minimum amount of fissile material needed to:", ["Start a reactor", "*Sustain a chain reaction (enough material to capture sufficient neutrons)", "Build a bomb", "Create fusion"], "Below critical mass: chain reaction dies out."),
    ("Uranium enrichment increases the percentage of:", ["U-238", "*U-235 from natural ~0.7% to 3-5% (for reactors) or >80% (for weapons)", "U-234", "Plutonium"], "Natural uranium has too little U-235."),
    ("Nuclear waste disposal is challenging because:", ["It's not radioactive", "It decays in days", "*Some waste remains radioactive for thousands to millions of years", "It's easy to store"], "Long-lived isotopes require long-term storage."),
    ("Chernobyl and Fukushima are examples of:", ["Fusion reactor failures", "*Fission reactor accidents (highlighting safety concerns)", "Chemical explosions only", "Successful decommissions"], "Nuclear fission safety incidents."),
])

# U12 L12.2: Alpha Particles
add_qs("u12_l12.2", [
    ("An alpha particle is identical to a _____ nucleus.", ["Hydrogen", "*Helium-4 (2 protons + 2 neutrons)", "Lithium", "Carbon"], "Alpha = He-4."),
    ("Alpha particles have a charge of:", ["+1", "*+2 (two protons)", "-1", "0"], "Two protons = 2+ charge."),
    ("Alpha radiation has _____ penetrating power.", ["High", "Medium", "*Low (stopped by paper or skin)", "No"], "Large, heavy particle = easily stopped."),
    ("Alpha decay decreases atomic number by _____ and mass number by _____.", ["1; 2", "2; 2", "*2; 4 (loses 2 protons and 2 neutrons)", "4; 2"], "Z decreases by 2; A decreases by 4."),
    ("U-238 undergoes alpha decay to form:", ["U-234", "Th-234 + gamma", "*Th-234 + He-4 (alpha particle)", "Pa-234"], "92 - 2 = 90 (Th); 238 - 4 = 234."),
    ("Alpha particles are dangerous primarily when:", ["Outside the body at a distance", "*Inhaled or ingested (internal exposure damages nearby tissue intensely)", "Near magnets", "Dissolved in water"], "Internally, alpha radiation is highly damaging."),
    ("Radon (Rn-222) decays by alpha emission to form:", ["Rn-218", "*Po-218 (222-4=218; 86-2=84=polonium)", "Pb-218", "At-218"], "Radon -> Polonium."),
    ("Alpha emitters are used in some _____ detectors.", ["Carbon monoxide", "Temperature", "*Smoke (americium-241 ionizes air; smoke disrupts the current)", "UV"], "Ionization smoke detectors."),
    ("In Rutherford's experiment, alpha particles were used to:", ["Create gold", "Split atoms", "*Probe the structure of atoms (most passed through gold foil; some bounced back revealing the nucleus)", "Measure temperature"], "Discovered the nuclear atom."),
    ("The mass of an alpha particle is approximately:", ["1 amu", "2 amu", "*4 amu", "8 amu"], "2p + 2n ≈ 4 amu."),
    ("Alpha particles can be stopped by:", ["Nothing", "Lead only", "*A sheet of paper, skin, or a few centimeters of air", "Only concrete"], "Lowest penetrating power."),
    ("Alpha decay is common in elements with Z > _____.", ["20", "50", "*83 (heavy elements above bismuth are radioactive)", "100"], "Heavy unstable nuclei."),
    ("The symbol for an alpha particle in nuclear equations can be written as:", ["e", "n", "*He-4 (or alpha)", "p"], "He-4 nucleus."),
])

# U12 L12.3: Nuclear Equations
add_qs("u12_l12.3", [
    ("In nuclear equations, both mass number and atomic number must be:", ["Different on each side", "*Conserved (balanced on both sides)", "Zero", "Doubled"], "Conservation laws applied."),
    ("In alpha decay: _{Z}^{A}X -> _{Z-2}^{A-4}Y + _{2}^{4}He. The missing daughter has:", ["Same Z and A", "*Z-2 and A-4 (reduced by alpha particle's numbers)", "Z+2 and A+4", "Z and A-4"], "Alpha carries away 2p and 4 mass units."),
    ("In beta decay: _{Z}^{A}X -> _{Z+1}^{A}Y + _{-1}^{0}e. The atomic number:", ["Decreases by 1", "*Increases by 1 (a neutron converts to a proton)", "Stays the same", "Doubles"], "n -> p + e; one more proton."),
    ("In positron emission: _{Z}^{A}X -> _{Z-1}^{A}Y + _{+1}^{0}e. The atomic number:", ["Increases by 1", "*Decreases by 1 (a proton converts to a neutron)", "Stays the same", "Increases by 2"], "Proton -> neutron + positron."),
    ("In electron capture: _{Z}^{A}X + _{-1}^{0}e -> _{Z-1}^{A}Y. The result is similar to:", ["Alpha decay", "*Positron emission (Z decreases by 1, A unchanged)", "Beta decay", "Gamma emission"], "Same Z change as positron emission."),
    ("Gamma emission changes:", ["Mass number", "Atomic number", "*Neither (gamma rays are pure energy photons with no mass or charge)", "Both"], "Gamma doesn't change the nucleus identity."),
    ("Balance: _{92}^{238}U -> _{90}^{234}Th + ?", ["Beta particle", "Gamma ray", "*_{2}^{4}He (alpha particle, since 238-234=4 and 92-90=2)", "Neutron"], "Mass and charge balance."),
    ("Balance: _{6}^{14}C -> _{7}^{14}N + ?", ["Alpha particle", "*_{-1}^{0}e (beta particle, since Z increases by 1, A stays same)", "Gamma ray", "Neutron"], "Beta decay: C-14 -> N-14."),
    ("Transmutation by bombardment: _{7}^{14}N + _{2}^{4}He -> _{8}^{17}O + ?", ["Alpha particle", "Beta particle", "*_{1}^{1}H (proton)", "Neutron"], "Balance: 7+2=8+1 (Z); 14+4=17+1 (A)."),
    ("Artificial transmutation involves:", ["Natural decay only", "*Bombarding nuclei with particles (protons, neutrons, alpha) to create new elements", "Chemical reactions", "Phase changes"], "Particle accelerators used."),
    ("The first artificial transmutation was performed by:", ["Marie Curie", "*Ernest Rutherford (1919, nitrogen to oxygen using alpha particles)", "Niels Bohr", "Albert Einstein"], "Rutherford changed nitrogen to oxygen."),
    ("Transuranium elements (Z > 92) are created by:", ["Natural processes", "Chemical combination", "*Nuclear bombardment in particle accelerators and reactors", "Electrolysis"], "Synthetic heavy elements."),
    ("When writing nuclear equations, the sum of subscripts (Z) on the left must equal the sum on the:", ["Top", "*Right (conservation of charge/atomic number)", "It doesn't need to balance", "Bottom"], "Atomic numbers balance."),
])

# U12 L12.4: Half-Life
add_qs("u12_l12.4", [
    ("Half-life is the time for _____ of a radioactive sample to decay.", ["All", "One quarter", "*Half (50%)", "One tenth"], "Definition of half-life."),
    ("After one half-life, the fraction remaining is:", ["1/4", "*1/2", "3/4", "0"], "50% remains."),
    ("After two half-lives, the fraction remaining is:", ["1/2", "*1/4 (1/2 x 1/2)", "1/8", "3/4"], "50% of 50% = 25%."),
    ("After three half-lives, the fraction remaining is:", ["1/4", "1/2", "*1/8 (1/2)^3", "1/16"], "12.5% remains."),
    ("The formula N = N0 x (1/2)^(t/t_half) calculates:", ["Rate constant", "Energy released", "*Amount of radioactive material remaining after time t", "Temperature"], "Exponential decay formula."),
    ("Carbon-14 has a half-life of about:", ["100 years", "1000 years", "*5,730 years", "1 million years"], "Used for dating up to ~50,000 years."),
    ("If you start with 80 g and the half-life is 10 days, after 30 days you have:", ["40 g", "20 g", "*10 g (80 -> 40 -> 20 -> 10, three half-lives)", "0 g"], "3 half-lives: 80/8 = 10 g."),
    ("Half-life is a _____ property (not affected by temperature, pressure, or chemical state).", ["Variable", "Chemical", "*Constant for a given isotope (independent of external conditions)", "Changing"], "Nuclear property, not chemical."),
    ("Radioactive dating works because:", ["All elements decay at the same rate", "*Each radioactive isotope has a known, constant half-life that can be used as a clock", "Rocks change color", "Carbon is always present"], "Decay rate as a chronometer."),
    ("Potassium-40 (t_half = 1.25 billion years) is used to date:", ["Recent artifacts", "Organic matter", "*Rocks and minerals (geological timescales)", "Water samples"], "Very long half-life for old rocks."),
    ("If only 1/16 of original sample remains, how many half-lives have passed?", ["2", "3", "*4 (1/2^4 = 1/16)", "5"], "(1/2)^n = 1/16; n = 4."),
    ("A sample's activity (decay rate) is measured in:", ["Grams", "*Becquerels (Bq, decays per second) or Curies (Ci)", "Moles", "Joules"], "Activity units."),
    ("The decay constant (lambda) relates to half-life by: lambda = _____.", ["t_half x 2", "t_half / 2", "*0.693 / t_half (ln2 / t_half)", "t_half^2"], "Mathematical relationship."),
])

# U12 L12.5: Radioactive Tracers
add_qs("u12_l12.5", [
    ("A radioactive tracer is a radioisotope used to:", ["Kill cells", "Generate energy", "*Track the path of a substance through a system (biological, chemical, or industrial)", "Create new elements"], "Follow where substances go."),
    ("In medicine, tracers help diagnose disease by:", ["Treating the disease directly", "*Allowing doctors to image organs/tissues using the radiation emitted (scans like PET, SPECT)", "Replacing injured tissue", "Measuring temperature"], "Medical imaging."),
    ("The most commonly used medical tracer is:", ["C-14", "I-131", "*Tc-99m (technetium-99m, ideal half-life of 6 hours and gamma emission)", "U-235"], "Tc-99m: short half-life, gamma emitter."),
    ("PET scans use positron-emitting tracers like:", ["Tc-99m", "*F-18 (fluorodeoxyglucose, FDG) to detect metabolically active tissues like cancer", "I-131", "Co-60"], "FDG-PET for cancer detection."),
    ("Iodine-131 is used both to diagnose and treat:", ["Heart disease", "Lung cancer", "*Thyroid conditions (thyroid selectively absorbs iodine)", "Bone fractures"], "Thyroid-targeting radioisotope."),
    ("Tracers work because the radioactive isotope:", ["Changes the substance's chemistry", "*Behaves chemically identically to the stable isotope but can be detected by its radiation", "Is visible light", "Has different properties"], "Same chemistry, detectable by radiation."),
    ("In agriculture, radioactive tracers can:", ["Kill pests", "*Track nutrient uptake by plants (e.g., P-32 to study phosphorus absorption)", "Increase crop yield", "Change soil composition"], "Understanding plant nutrition."),
    ("In industry, tracers detect:", ["Color changes", "*Leaks in pipelines, flow patterns, and mixing efficiency", "Magnetic fields", "Sound waves"], "Non-destructive testing."),
    ("Ideal medical tracers have:", ["Very long half-lives", "*Short half-lives (enough time for imaging but minimal radiation exposure), gamma emission, and target-specific uptake", "Alpha emission", "No radiation"], "Balance between usefulness and safety."),
    ("Autoradiography uses tracers to:", ["Take X-rays", "*Create images by exposing photographic film/plates to radiation from labeled molecules", "Measure temperature", "Count cells"], "Visualize radioactive labeling."),
    ("Carbon-14 labeling in research:", ["Is used for PET scans", "*Traces metabolic pathways by incorporating C-14 into organic molecules (e.g., photosynthesis studies)", "Has too short a half-life", "Emits gamma rays"], "Melvin Calvin used C-14 to map photosynthesis."),
    ("The radiation dose from medical tracers is _____ to be generally safe.", ["Extremely high", "*Carefully controlled and minimized (ALARA: As Low As Reasonably Achievable)", "Zero", "Unmeasured"], "Safety principle limits exposure."),
    ("Thallium-201 stress tests use the tracer to image:", ["Brain function", "Liver function", "*Heart blood flow (myocardial perfusion imaging)", "Bone density"], "Cardiac imaging."),
])

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

short = [(k, len(v.get("quiz_questions",[]))) for k,v in data.items() if len(v.get("quiz_questions",[]))<20]
ct = sum(1 for v in data.values() if len(v.get('quiz_questions',[])) >= 20)
print(f"✅ Chemistry U9-U12 done: {ct}/{len(data)} lessons at 20+ questions")
if short:
    for k,n in short: print(f"  STILL SHORT: {k} ({n}q)")
else:
    print("🎉 All Chemistry lessons at 20+ questions!")
