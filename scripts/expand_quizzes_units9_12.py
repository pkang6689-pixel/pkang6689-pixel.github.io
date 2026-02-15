#!/usr/bin/env python3
"""Expand quiz files for Units 9, 10, 11, 12 from 2 questions to 7 questions each."""

import os
import re
import random

BASE = os.path.join(os.path.dirname(__file__), '..', 'ArisEdu Project Folder', 'ChemistryLessons')

LESSONS = {
    # ===== UNIT 9: Solutions =====
    "Unit9": {
        "9.1": {
            "topic": "Solution Nomenclature",
            "questions": [
                ("In a solution, the solvent is the substance that:", "Dissolves the solute (present in greater amount)", ["Is dissolved", "Settles to the bottom", "Is always a solid"]),
                ("The solute is the substance that:", "Is dissolved in the solvent", ["Does the dissolving", "Is always a liquid", "Is always present in greater amount"]),
                ("An aqueous solution uses what as the solvent?", "Water", ["Alcohol", "Oil", "Mercury"]),
                ("The notation (aq) after a formula means:", "Dissolved in water (aqueous)", ["In gas phase", "A solid", "A pure liquid"]),
                ("A solution is a type of:", "Homogeneous mixture", ["Heterogeneous mixture", "Pure substance", "Element"]),
                ("In salt water, the solute is:", "Salt (NaCl)", ["Water", "Both equally", "Neither"]),
                ("A tincture is a solution that uses what as the solvent?", "Alcohol", ["Water", "Oil", "Gasoline"]),
            ]
        },
        "9.2": {
            "topic": "Concentration",
            "questions": [
                ("Concentration measures:", "The amount of solute in a given amount of solution", ["The temperature of a solution", "The color of a solution", "The volume of solvent only"]),
                ("A concentrated solution has:", "A large amount of solute relative to solvent", ["Very little solute", "No solute", "Only solvent"]),
                ("A dilute solution has:", "A small amount of solute relative to solvent", ["A large amount of solute", "No solvent", "Solid particles visible"]),
                ("Parts per million (ppm) is used for:", "Very small concentrations", ["Very large concentrations", "Only gases", "Only solids"]),
                ("Which solution is more concentrated: 5 g/L or 10 g/L?", "10 g/L", ["5 g/L", "They are equal", "Cannot determine"]),
                ("Mass percent is calculated as:", "(Mass of solute / Mass of solution) × 100", ["(Mass of solvent / Mass of solute) × 100", "Mass of solute × 100", "Mass of solution / 100"]),
                ("If 10 g of sugar is dissolved in 90 g of water, the mass percent is:", "10%", ["90%", ["9%"], "11%"]),
            ]
        },
        "9.3": {
            "topic": "Dilution",
            "questions": [
                ("The dilution equation is:", "M₁V₁ = M₂V₂", ["M₁ + V₁ = M₂ + V₂", "M₁/V₁ = M₂/V₂", "M₁V₂ = M₂V₁"]),
                ("Dilution involves adding more:", "Solvent to reduce concentration", ["Solute to increase concentration", "Heat to evaporate solvent", "Another solution"]),
                ("When you dilute a solution, the amount of solute:", "Stays the same", ["Increases", "Decreases", "Doubles"]),
                ("If 100 mL of 2 M solution is diluted to 200 mL, the new concentration is:", "1 M", ["2 M", "4 M", "0.5 M"]),
                ("Serial dilution is useful for:", "Creating very dilute solutions in steps", ["Concentrating solutions", "Removing solute", "Heating solutions"]),
                ("What volume of 6 M HCl is needed to make 300 mL of 2 M HCl?", "100 mL", ["200 mL", "50 mL", "300 mL"]),
                ("During dilution, you should always:", "Add acid to water (never water to acid)", ["Add water to acid", "Heat the solution first", "Freeze the solvent"]),
            ]
        },
        "9.4": {
            "topic": "Molarity",
            "questions": [
                ("Molarity (M) is defined as:", "Moles of solute per liter of solution", ["Grams of solute per liter", "Moles of solute per kilogram of solvent", "Liters of solution per mole"]),
                ("The units of molarity are:", "mol/L (or M)", ["g/L", "g/mL", "mol/kg"]),
                ("A 2 M NaCl solution contains:", "2 moles of NaCl per liter of solution", ["2 grams of NaCl per liter", "2 liters per mole", "2 moles per 100 mL"]),
                ("To calculate molarity, you need to know:", "Moles of solute and volume of solution in liters", ["Only the mass of solute", "Only the temperature", "Only the density"]),
                ("How many moles of NaOH are in 500 mL of 0.5 M solution?", "0.25 mol", ["0.5 mol", "1 mol", "0.1 mol"]),
                ("If 4 moles of solute are dissolved in 2 L of solution, the molarity is:", "2 M", ["4 M", ["0.5 M"], "8 M"]),
                ("Molarity changes with temperature because:", "Volume of solution changes with temperature", ["Mass doesn't change", "Moles change", "Solute evaporates"]),
            ]
        },
        "9.5": {
            "topic": "Solution Types",
            "questions": [
                ("A saturated solution:", "Contains the maximum amount of dissolved solute at a given temperature", ["Can dissolve more solute", "Has no solute", "Is always hot"]),
                ("An unsaturated solution:", "Can dissolve more solute", ["Has the maximum solute dissolved", "Has excess solute at the bottom", "Is always cold"]),
                ("A supersaturated solution:", "Contains more dissolved solute than normally possible", ["Has less solute than saturated", "Cannot exist", "Is always dilute"]),
                ("Adding a seed crystal to a supersaturated solution causes:", "Rapid crystallization of excess solute", ["More dissolving", "No change", "Evaporation"]),
                ("A suspension differs from a solution because:", "Particles are large enough to settle out", ["It is homogeneous", "Particles are dissolved", "It is always clear"]),
                ("A colloid has particles that:", "Are intermediate in size and don't settle", ["Are dissolved like a solution", "Settle like a suspension", "Are always visible"]),
                ("The Tyndall effect (light scattering) occurs in:", "Colloids", ["True solutions", "Pure water", "Elements"]),
            ]
        },
        "9.6": {
            "topic": "Factors Affecting Solubility",
            "questions": [
                ("For most solid solutes, increasing temperature:", "Increases solubility", ["Decreases solubility", "Has no effect", "Makes them insoluble"]),
                ("For gas solutes, increasing temperature:", "Decreases solubility", ["Increases solubility", "Has no effect", "Makes them more soluble"]),
                ("Increasing pressure significantly affects the solubility of:", "Gases", ["Solids", "Liquids", "All equally"]),
                ("'Like dissolves like' means:", "Polar solvents dissolve polar solutes", ["Any solvent dissolves anything", "Oil dissolves in water", "Nonpolar dissolves polar"]),
                ("Why does sugar dissolve in water?", "Both are polar", ["Both are nonpolar", "Sugar is a gas", "Water is nonpolar"]),
                ("Why doesn't oil dissolve in water?", "Oil is nonpolar and water is polar", ["Both are polar", "Oil is too heavy", "Water is nonpolar"]),
                ("Henry's Law states that gas solubility is:", "Directly proportional to pressure", ["Inversely proportional to pressure", "Unrelated to pressure", "Only dependent on temperature"]),
            ]
        },
        "9.7": {
            "topic": "Colligative Properties",
            "questions": [
                ("Colligative properties depend on:", "The number of solute particles, not their identity", ["The type of solute", "The color of the solution", "Only the solvent"]),
                ("Adding solute to a solvent causes the boiling point to:", "Increase (boiling point elevation)", ["Decrease", "Stay the same", "Become unpredictable"]),
                ("Adding solute to a solvent causes the freezing point to:", "Decrease (freezing point depression)", ["Increase", "Stay the same", "Double"]),
                ("Road salt works by:", "Lowering the freezing point of water", ["Raising the freezing point", "Melting ice with heat", "Absorbing water"]),
                ("Osmotic pressure is a colligative property related to:", "Movement of solvent across a semipermeable membrane", ["Boiling point only", "Color changes", "Gas pressure"]),
                ("Which solution has a higher boiling point: 1 M NaCl or 1 M glucose?", "1 M NaCl (produces 2 particles per formula unit)", ["1 M glucose", "They are equal", "Cannot determine"]),
                ("Vapor pressure lowering occurs because:", "Solute particles occupy surface area, reducing evaporation", ["Solute increases evaporation", "Solvent becomes heavier", "Temperature drops"]),
            ]
        },
        "9.8": {
            "topic": "Solubility Curves",
            "questions": [
                ("A solubility curve shows:", "How solubility changes with temperature", ["How pressure changes with volume", "The rate of a reaction", "Density vs. mass"]),
                ("A point below the solubility curve represents:", "An unsaturated solution", ["A saturated solution", "A supersaturated solution", "An insoluble substance"]),
                ("A point on the solubility curve represents:", "A saturated solution", ["An unsaturated solution", "A supersaturated solution", "A suspension"]),
                ("A point above the solubility curve represents:", "A supersaturated solution", ["An unsaturated solution", "A saturated solution", "An impossible solution"]),
                ("Most solid solubility curves slope:", "Upward (solubility increases with temperature)", ["Downward", "Flat (horizontal)", "In a circle"]),
                ("Gas solubility curves typically slope:", "Downward (solubility decreases with temperature)", ["Upward", "Flat", "Randomly"]),
                ("KNO₃ has a steeply rising solubility curve, meaning:", "Its solubility is very sensitive to temperature changes", ["It barely dissolves", "Temperature has no effect", "It is a gas"]),
            ]
        },
    },
    # ===== UNIT 10: Acids & Bases =====
    "Unit10": {
        "10.1": {
            "topic": "Acid & Base Properties",
            "questions": [
                ("Acids taste:", "Sour", ["Bitter", "Sweet", "Salty"]),
                ("Bases taste:", "Bitter", ["Sour", "Sweet", "No taste"]),
                ("Acids turn blue litmus paper:", "Red", ["Blue", "Green", "No change"]),
                ("Bases feel:", "Slippery", ["Rough", "Dry", "Gritty"]),
                ("Acids produce what ion in water?", "H⁺ (hydrogen ion / hydronium)", ["OH⁻ (hydroxide)", "Na⁺", "Cl⁻"]),
                ("Bases produce what ion in water?", "OH⁻ (hydroxide ion)", ["H⁺ (hydrogen ion)", "Na⁺", "SO₄²⁻"]),
                ("Bases turn red litmus paper:", "Blue", ["Red", "Green", "Yellow"]),
            ]
        },
        "10.2": {
            "topic": "Binary Acids vs. Oxyacids",
            "questions": [
                ("A binary acid contains:", "Hydrogen and one other nonmetal element", ["Hydrogen and oxygen", "Three different elements", "A metal and nonmetal"]),
                ("An oxyacid contains:", "Hydrogen, oxygen, and another nonmetal", ["Only hydrogen and a nonmetal", "Only metals", "No hydrogen"]),
                ("The naming prefix for binary acids is:", "Hydro-", ["Oxy-", "Per-", "Hypo-"]),
                ("The suffix for binary acid names is:", "-ic acid", ["-ous acid", "-ate acid", "-ide acid"]),
                ("HCl is named:", "Hydrochloric acid", ["Chloric acid", "Hydrogen chloride acid", "Perchloric acid"]),
                ("H₂SO₄ is an example of:", "An oxyacid", ["A binary acid", "A base", "A salt"]),
                ("HBr is named:", "Hydrobromic acid", ["Bromic acid", "Bromous acid", "Perbromic acid"]),
            ]
        },
        "10.3": {
            "topic": "Naming Acids",
            "questions": [
                ("If a polyatomic ion ends in '-ate', the acid name ends in:", "-ic acid", ["-ous acid", "-ide acid", "-hydro acid"]),
                ("If a polyatomic ion ends in '-ite', the acid name ends in:", "-ous acid", ["-ic acid", "-ate acid", "-ide acid"]),
                ("H₂SO₄ (from sulfate SO₄²⁻) is named:", "Sulfuric acid", ["Sulfurous acid", "Hydrosulfuric acid", "Persulfuric acid"]),
                ("H₂SO₃ (from sulfite SO₃²⁻) is named:", "Sulfurous acid", ["Sulfuric acid", "Hydrosulfurous acid", "Hyposulfuric acid"]),
                ("HNO₃ (from nitrate NO₃⁻) is named:", "Nitric acid", ["Nitrous acid", "Hydronitric acid", "Pernitric acid"]),
                ("HClO₃ (from chlorate ClO₃⁻) is named:", "Chloric acid", ["Chlorous acid", "Hydrochloric acid", "Perchloric acid"]),
                ("H₃PO₄ (from phosphate PO₄³⁻) is named:", "Phosphoric acid", ["Phosphorous acid", "Hydrophosphoric acid", "Perphosphoric acid"]),
            ]
        },
        "10.4": {
            "topic": "Identifying Acids & Bases",
            "questions": [
                ("According to Arrhenius, an acid:", "Produces H⁺ ions in water", ["Produces OH⁻ ions", "Accepts protons", "Donates electrons"]),
                ("According to Arrhenius, a base:", "Produces OH⁻ ions in water", ["Produces H⁺ ions", "Donates protons", "Accepts electrons"]),
                ("According to Brønsted-Lowry, an acid is a:", "Proton (H⁺) donor", ["Proton acceptor", "Electron donor", "Electron acceptor"]),
                ("According to Brønsted-Lowry, a base is a:", "Proton (H⁺) acceptor", ["Proton donor", "Electron acceptor", "Electron donor"]),
                ("The Lewis definition of an acid is:", "An electron pair acceptor", ["An electron pair donor", "A proton donor", "A proton acceptor"]),
                ("NaOH dissolved in water produces:", "Na⁺ and OH⁻ ions", ["H⁺ and Cl⁻ ions", "Na and O atoms", "H₂ gas"]),
                ("HCl dissolved in water produces:", "H⁺ and Cl⁻ ions", ["OH⁻ and Cl⁻ ions", "NaCl", "H₂O only"]),
            ]
        },
        "10.5": {
            "topic": "Strong vs. Weak Acids/Bases",
            "questions": [
                ("A strong acid:", "Completely dissociates (ionizes) in water", ["Partially dissociates", "Does not dissociate", "Is always concentrated"]),
                ("A weak acid:", "Partially dissociates in water", ["Completely dissociates", "Never dissociates", "Is always dilute"]),
                ("Which of these is a strong acid?", "HCl (hydrochloric acid)", ["CH₃COOH (acetic acid)", "H₂CO₃ (carbonic acid)", "HF (hydrofluoric acid)"]),
                ("Which of these is a weak acid?", "Acetic acid (CH₃COOH)", ["HNO₃", "H₂SO₄", "HCl"]),
                ("A strong base:", "Completely dissociates in water", ["Partially dissociates", "Does not dissolve", "Is always weak"]),
                ("NaOH is a:", "Strong base", ["Weak base", "Strong acid", "Weak acid"]),
                ("Strength vs. concentration: a dilute strong acid:", "Is fully dissociated but has few moles per liter", ["Is partially dissociated", "Is not an acid", "Cannot exist"]),
            ]
        },
        "10.6": {
            "topic": "Neutralization Reactions",
            "questions": [
                ("A neutralization reaction occurs between:", "An acid and a base", ["Two acids", "Two bases", "A metal and a nonmetal"]),
                ("The products of a neutralization reaction are:", "Water and a salt", ["Only water", "Only a salt", "A gas and a solid"]),
                ("The general equation for neutralization is:", "Acid + Base → Salt + Water", ["Acid + Acid → Salt", "Base + Base → Water", "Salt + Water → Acid"]),
                ("In HCl + NaOH → NaCl + H₂O, NaCl is the:", "Salt", ["Acid", "Base", "Water"]),
                ("A titration is used to determine:", "The concentration of an unknown acid or base", ["The color of a solution", "The temperature", "The mass of solute"]),
                ("The equivalence point in a titration is when:", "Moles of acid equal moles of base", ["The solution turns clear", "All water evaporates", "pH equals 0"]),
                ("An indicator in a titration:", "Changes color at or near the equivalence point", ["Adds acid to the solution", "Neutralizes the base", "Measures temperature"]),
            ]
        },
        "10.7": {
            "topic": "Naming Salts from Neutralization",
            "questions": [
                ("A salt is an ionic compound formed from:", "The cation of a base and the anion of an acid", ["Two acids", "Two bases", "A metal and a gas"]),
                ("HCl + NaOH produces the salt:", "NaCl (sodium chloride)", ["NaOH", "HCl₂", "NaH"]),
                ("H₂SO₄ + 2KOH produces the salt:", "K₂SO₄ (potassium sulfate)", ["KSO₄", "K₂SO₃", "KOH₂"]),
                ("The salt from HNO₃ + Ca(OH)₂ is:", "Ca(NO₃)₂ (calcium nitrate)", ["CaNO₃", "CaN₂O₃", "Ca₂NO₃"]),
                ("To name a salt, combine:", "The metal name and the anion name from the acid", ["The acid name and base name", "Only the metal name", "Only the nonmetal name"]),
                ("The salt from H₃PO₄ + 3NaOH is:", "Na₃PO₄ (sodium phosphate)", ["NaPO₄", "Na₃PO₃", "NaH₃PO₄"]),
                ("Salts formed from strong acid + strong base produce solutions that are:", "Neutral (pH ≈ 7)", ["Acidic", "Basic", "Always colored"]),
            ]
        },
        "10.8": {
            "topic": "Buffer Solutions",
            "questions": [
                ("A buffer solution resists changes in:", "pH", ["Temperature", "Volume", "Color"]),
                ("A buffer is typically made from:", "A weak acid and its conjugate base (or vice versa)", ["A strong acid and strong base", "Two strong acids", "Pure water"]),
                ("When a small amount of acid is added to a buffer:", "The conjugate base neutralizes it, keeping pH stable", ["pH drops dramatically", "The buffer breaks down", "Nothing happens"]),
                ("When a small amount of base is added to a buffer:", "The weak acid neutralizes it, keeping pH stable", ["pH rises dramatically", "The buffer evaporates", "A precipitate forms"]),
                ("Blood maintains a pH of about 7.4 using:", "The carbonic acid/bicarbonate buffer system", ["Pure water", "Strong acid buffers", "No buffer system"]),
                ("Buffer capacity refers to:", "The amount of acid or base a buffer can neutralize", ["The color of the buffer", "The temperature of the buffer", "The volume of the buffer"]),
                ("Adding large amounts of acid or base to a buffer:", "Can overwhelm the buffer capacity", ["Has no effect", "Makes the buffer stronger", "Always makes pH = 7"]),
            ]
        },
        "10.9": {
            "topic": "pH & pOH Scale",
            "questions": [
                ("The pH scale ranges from:", "0 to 14", ["1 to 10", "0 to 7", "-14 to 14"]),
                ("A pH of 7 is:", "Neutral", ["Acidic", "Basic", "Undefined"]),
                ("A pH less than 7 is:", "Acidic", ["Basic", "Neutral", "Undefined"]),
                ("A pH greater than 7 is:", "Basic (alkaline)", ["Acidic", "Neutral", "Impossible"]),
                ("pH + pOH always equals:", "14 (at 25°C)", ["7", "10", "0"]),
                ("As H⁺ concentration increases, pH:", "Decreases", ["Increases", "Stays the same", "Becomes 7"]),
                ("Each whole number change on the pH scale represents a factor of:", "10", ["2", "5", "100"]),
            ]
        },
        "10.10": {
            "topic": "Calculating pH and pOH using Log",
            "questions": [
                ("The formula for pH is:", "pH = -log[H⁺]", ["pH = log[H⁺]", "pH = -ln[H⁺]", "pH = [H⁺] × 10"]),
                ("The formula for pOH is:", "pOH = -log[OH⁻]", ["pOH = log[OH⁻]", "pOH = -ln[OH⁻]", "pOH = [OH⁻] × 10"]),
                ("If [H⁺] = 1 × 10⁻³ M, the pH is:", "3", ["10", "-3", "11"]),
                ("If pH = 5, the [H⁺] concentration is:", "1 × 10⁻⁵ M", ["5 M", "1 × 10⁵ M", "1 × 10⁻⁹ M"]),
                ("If pH = 2, the pOH is:", "12", ["2", "7", "14"]),
                ("A solution with [OH⁻] = 1 × 10⁻⁴ M has a pOH of:", "4", ["10", "-4", "8"]),
                ("To find [H⁺] from pH, you use:", "[H⁺] = 10⁻ᵖᴴ", ["[H⁺] = pH × 10", "[H⁺] = log(pH)", "[H⁺] = pH / 14"]),
            ]
        },
    },
    # ===== UNIT 11: Thermochemistry =====
    "Unit11": {
        "11.1": {
            "topic": "Heat Conversion",
            "questions": [
                ("Heat energy is measured in:", "Joules (J) or calories (cal)", ["Meters", "Kilograms", "Moles"]),
                ("1 calorie equals:", "4.184 joules", ["1 joule", "100 joules", "0.001 joules"]),
                ("1 kilocalorie (food Calorie) equals:", "1,000 calories", ["100 calories", "10 calories", "1 calorie"]),
                ("To convert joules to calories:", "Divide by 4.184", ["Multiply by 4.184", "Add 4.184", "Subtract 4.184"]),
                ("A dietary Calorie (capital C) equals:", "1 kilocalorie = 1,000 calories", ["1 calorie", "100 calories", "1 joule"]),
                ("500 calories equals how many joules?", "2,092 J", ["500 J", "119.5 J", "50,000 J"]),
                ("The SI unit of energy is:", "Joule (J)", ["Calorie", "Watt", "Newton"]),
            ]
        },
        "11.2": {
            "topic": "Specific Heat",
            "questions": [
                ("Specific heat is the amount of energy needed to:", "Raise 1 gram of a substance by 1°C", ["Melt 1 gram of a substance", "Boil 1 liter of water", "Cool 1 kg by 10°C"]),
                ("Water has a specific heat of:", "4.184 J/g·°C", ["1.0 J/g·°C", "2.0 J/g·°C", "0.5 J/g·°C"]),
                ("A substance with a high specific heat:", "Changes temperature slowly", ["Changes temperature quickly", "Is always a gas", "Has low mass"]),
                ("The formula q = mcΔT: q represents:", "Heat energy (joules)", ["Mass", "Specific heat", "Temperature"]),
                ("In q = mcΔT, m represents:", "Mass in grams", ["Molarity", "Moles", "Momentum"]),
                ("Metals generally have:", "Low specific heat values", ["High specific heat values", "No specific heat", "Variable specific heat"]),
                ("Water's high specific heat makes it useful for:", "Regulating temperature in organisms and environments", ["Conducting electricity", "Making strong materials", "Producing light"]),
            ]
        },
        "11.3": {
            "topic": "Heat Capacity",
            "questions": [
                ("Heat capacity is the amount of energy needed to:", "Raise the temperature of an object by 1°C", ["Change the phase of an object", "Dissolve a substance", "Compress a gas"]),
                ("Heat capacity differs from specific heat because it:", "Depends on the total mass of the object", ["Is per gram", "Is always the same", "Only applies to gases"]),
                ("The units of heat capacity are:", "J/°C (or cal/°C)", ["J/g·°C", "J/mol", "°C/J"]),
                ("A large body of water has a high heat capacity because:", "It has a large mass and high specific heat", ["Water has low specific heat", "It is always cold", "It evaporates easily"]),
                ("Doubling the mass of a substance:", "Doubles its heat capacity", ["Halves its heat capacity", "Has no effect", "Triples it"]),
                ("Heat capacity = specific heat ×:", "Mass", ["Temperature", "Volume", "Pressure"]),
                ("An object with high heat capacity:", "Requires more energy to change its temperature", ["Changes temperature easily", "Is always a metal", "Has low mass"]),
            ]
        },
        "11.4": {
            "topic": "Calorimetry",
            "questions": [
                ("Calorimetry is the measurement of:", "Heat transfer during chemical or physical processes", ["Pressure changes", "Volume changes", "Electrical current"]),
                ("A calorimeter works by:", "Measuring temperature change of water surrounding a reaction", ["Measuring pressure directly", "Weighing products", "Counting molecules"]),
                ("In a coffee-cup calorimeter, the assumption is:", "No heat is lost to the surroundings", ["All heat escapes", "Only gases are measured", "Temperature stays constant"]),
                ("The heat released by a reaction equals:", "The heat absorbed by the water (q = mcΔT)", ["The mass of the reactants", "Zero always", "The volume of the container"]),
                ("If water temperature rises in a calorimeter, the reaction is:", "Exothermic", ["Endothermic", "At equilibrium", "Impossible to tell"]),
                ("A bomb calorimeter measures reactions at constant:", "Volume", ["Pressure", "Temperature", "Mass"]),
                ("If 200 g of water rises by 5°C in a calorimeter, heat absorbed is:", "4,184 J (q = 200 × 4.184 × 5)", ["1,000 J", "200 J", "5,000 J"]),
            ]
        },
        "11.5": {
            "topic": "Enthalpy, Entropy, Free Energy",
            "questions": [
                ("Enthalpy (H) measures:", "Heat content of a system at constant pressure", ["Disorder of a system", "Free energy", "Temperature"]),
                ("A negative ΔH means the reaction is:", "Exothermic (releases heat)", ["Endothermic (absorbs heat)", "At equilibrium", "Impossible"]),
                ("Entropy (S) measures:", "The disorder or randomness of a system", ["Heat content", "Free energy", "Temperature"]),
                ("The second law of thermodynamics states:", "Entropy of the universe tends to increase", ["Energy is always conserved", "Entropy always decreases", "Heat flows from cold to hot"]),
                ("Gibbs free energy (G) determines:", "Whether a reaction is spontaneous", ["The temperature only", "The pressure only", "The color of products"]),
                ("A reaction is spontaneous when ΔG is:", "Negative", ["Positive", "Zero", "Infinite"]),
                ("The Gibbs free energy equation is:", "ΔG = ΔH − TΔS", ["ΔG = ΔH + TΔS", "ΔG = ΔH × ΔS", "ΔG = ΔH / TΔS"]),
            ]
        },
        "11.6": {
            "topic": "Hess's Law",
            "questions": [
                ("Hess's Law states that:", "The total enthalpy change is the same regardless of the pathway", ["Enthalpy depends on the path taken", "Only one-step reactions have enthalpy", "Entropy equals enthalpy"]),
                ("Hess's Law is based on the fact that enthalpy is a:", "State function", ["Path function", "Random variable", "Measurement error"]),
                ("To use Hess's Law, you can:", "Add enthalpies of individual steps to find the total", ["Only use one reaction", "Ignore intermediate steps", "Subtract all values"]),
                ("If a reaction is reversed, the sign of ΔH:", "Changes (becomes opposite)", ["Stays the same", "Becomes zero", "Doubles"]),
                ("If a reaction is multiplied by a factor, ΔH is:", "Multiplied by the same factor", ["Divided by the factor", "Unchanged", "Squared"]),
                ("Standard enthalpy of formation (ΔH°f) is measured:", "At 25°C and 1 atm", ["At 0°C and 0 atm", "At 100°C and 2 atm", "At any conditions"]),
                ("The standard enthalpy of formation of an element in its standard state is:", "Zero", ["Always positive", "Always negative", "Variable"]),
            ]
        },
    },
    # ===== UNIT 12: Nuclear Chemistry =====
    "Unit12": {
        "12.1": {
            "topic": "Nuclear Fusion and Fission",
            "questions": [
                ("Nuclear fission is the process of:", "Splitting a heavy nucleus into smaller nuclei", ["Combining light nuclei into a heavier one", "Removing electrons", "Adding neutrons"]),
                ("Nuclear fusion is the process of:", "Combining light nuclei into a heavier nucleus", ["Splitting heavy nuclei", "Ionizing atoms", "Breaking chemical bonds"]),
                ("The sun produces energy through:", "Nuclear fusion", ["Nuclear fission", "Chemical combustion", "Radioactive decay"]),
                ("Nuclear power plants use:", "Fission of uranium-235", ["Fusion of hydrogen", "Combustion of coal", "Solar energy"]),
                ("Fusion requires extremely high:", "Temperatures (millions of degrees)", ["Pressures only", "Volumes", "Number of atoms"]),
                ("The mass defect in nuclear reactions represents:", "Mass converted to energy (E = mc²)", ["Lost neutrons", "Gained protons", "Destroyed matter"]),
                ("Which process releases more energy per unit mass?", "Fusion", ["Fission", "They are equal", "Chemical combustion"]),
            ]
        },
        "12.2": {
            "topic": "Alpha, Beta, & Gamma Decay",
            "questions": [
                ("An alpha particle consists of:", "2 protons and 2 neutrons (He-4 nucleus)", ["1 proton and 1 neutron", "An electron", "A photon"]),
                ("A beta particle is:", "A high-energy electron emitted from the nucleus", ["A helium nucleus", "A photon", "A proton"]),
                ("Gamma radiation is:", "High-energy electromagnetic radiation (photons)", ["A particle with mass", "A helium nucleus", "An electron"]),
                ("Which type of radiation has the greatest penetrating power?", "Gamma", ["Alpha", "Beta", "All equal"]),
                ("Alpha particles can be stopped by:", "A sheet of paper", ["Lead shielding", "Concrete walls", "Nothing"]),
                ("In alpha decay, the atomic number decreases by:", "2", ["1", "4", "0"]),
                ("In beta decay, the atomic number:", "Increases by 1 (neutron converts to proton)", ["Decreases by 1", "Stays the same", "Increases by 2"]),
            ]
        },
        "12.3": {
            "topic": "Nuclear Reactions",
            "questions": [
                ("In nuclear equations, both mass number and atomic number must be:", "Conserved (balanced)", ["Created", "Destroyed", "Halved"]),
                ("Transmutation is the conversion of:", "One element into another", ["A solid to a liquid", "An acid to a base", "Energy to mass"]),
                ("Artificial transmutation can be achieved by:", "Bombarding nuclei with particles in an accelerator", ["Heating a substance", "Dissolving in water", "Applying pressure"]),
                ("When uranium-238 undergoes alpha decay, it becomes:", "Thorium-234", ["Uranium-234", "Plutonium-242", "Radium-226"]),
                ("A positron is the antiparticle of:", "An electron", ["A proton", "A neutron", "An alpha particle"]),
                ("Positron emission decreases the atomic number by:", "1 (proton converts to neutron)", ["2", "0", "4"]),
                ("In electron capture:", "An inner electron is absorbed by the nucleus", ["An electron is emitted", "A proton is emitted", "A neutron escapes"]),
            ]
        },
        "12.4": {
            "topic": "Half-Life Calculations",
            "questions": [
                ("Half-life is the time it takes for:", "Half of a radioactive sample to decay", ["All of a sample to decay", "A sample to double", "A reaction to complete"]),
                ("After 2 half-lives, what fraction of the original sample remains?", "1/4", ["1/2", "1/8", "1/16"]),
                ("After 3 half-lives, what fraction remains?", "1/8", ["1/4", "1/16", "1/3"]),
                ("If a sample has a half-life of 10 years, after 30 years:", "1/8 remains", ["1/4 remains", "1/16 remains", "None remains"]),
                ("Carbon-14 has a half-life of approximately:", "5,730 years", ["100 years", "1 million years", "24 hours"]),
                ("The half-life formula is:", "N = N₀ × (1/2)^(t/t½)", ["N = N₀ × 2^t", "N = N₀ / t", "N = N₀ × t½"]),
                ("Half-life is independent of:", "The amount of sample or external conditions", ["Time", "The type of isotope", "Nuclear forces"]),
            ]
        },
        "12.5": {
            "topic": "Applications of Nuclear Chemistry",
            "questions": [
                ("Radioactive tracers are used in medicine to:", "Track biological processes and diagnose diseases", ["Generate electricity", "Clean water", "Build weapons"]),
                ("Carbon-14 dating is used to determine the age of:", "Organic materials up to ~50,000 years old", ["Rocks billions of years old", "Living organisms only", "Metals"]),
                ("PET scans use:", "Positron-emitting isotopes", ["Alpha particles", "Gamma-only radiation", "X-rays"]),
                ("Nuclear energy produces electricity by using heat from fission to:", "Generate steam that turns turbines", ["Directly convert radiation to electricity", "Burn radioactive fuel", "Create fusion reactions"]),
                ("Radiation therapy treats cancer by:", "Targeting and killing cancer cells with radiation", ["Injecting radioactive dye", "Using only alpha particles", "Removing all cells"]),
                ("Food irradiation uses radiation to:", "Kill bacteria and extend shelf life", ["Make food radioactive", "Change the taste of food", "Heat food for cooking"]),
                ("The main concern with nuclear power is:", "Radioactive waste disposal and potential accidents", ["High fuel cost", "Low energy output", "Air pollution from burning"]),
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
