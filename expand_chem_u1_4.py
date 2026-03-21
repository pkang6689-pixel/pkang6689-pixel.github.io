#!/usr/bin/env python3
"""Expand Chemistry Units 1-4 from 7 to 20 quiz questions each (22 lessons)."""
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

# U1 L1.1: States of Matter
add_qs("u1_l1.1", [
    ("Which state of matter has a definite volume but no definite shape?", ["Solid", "*Liquid", "Gas", "Plasma"], "Liquids take the shape of their container but have fixed volume."),
    ("Plasma is a state of matter found in:", ["Ice", "Lake water", "*Stars and lightning", "Rocks"], "Plasma consists of ionized gas particles."),
    ("In which state do particles have the most kinetic energy?", ["Solid", "Liquid", "*Gas", "All states are equal"], "Gas particles move fastest and have highest KE."),
    ("What determines the state of a substance?", ["Only pressure", "Only chemical composition", "*Temperature and pressure", "Only volume"], "Both temperature and pressure affect phase."),
    ("Bose-Einstein condensate occurs at:", ["High temperature", "Room temperature", "*Temperatures near absolute zero", "Boiling point"], "BEC forms at extremely low temperatures."),
    ("The particles in a solid:", ["Move freely", "*Vibrate in fixed positions", "Are widely separated", "Have no energy"], "Solid particles vibrate but maintain position."),
    ("Surface tension in liquids is caused by:", ["Gravity alone", "*Cohesive forces between liquid molecules at the surface", "Gas pressure", "Temperature only"], "Unbalanced attractive forces at the surface."),
    ("Viscosity measures a liquid's:", ["Temperature", "Density", "*Resistance to flow", "Color"], "Higher viscosity = thicker, flows more slowly."),
    ("Amorphous solids differ from crystalline solids because they:", ["Are always liquids", "*Lack a regular, repeating particle arrangement", "Are harder", "Have higher melting points"], "Amorphous = irregular structure (glass, rubber)."),
    ("Which property is unique to gases?", ["Definite shape", "Definite volume", "*Gases expand to fill their entire container", "Incompressibility"], "Gases are highly compressible and fill any container."),
    ("The kinetic molecular theory states that all matter consists of:", ["Stationary atoms", "*Constantly moving particles", "Only electrons", "Waves"], "Particles are always in motion."),
    ("At what temperature do all particle motion theoretically stop?", ["0 degrees C", "100 degrees C", "*0 Kelvin (absolute zero, -273.15 degrees C)", "-100 degrees C"], "Absolute zero is the lowest possible temperature."),
    ("Deposition is the phase change from:", ["Solid to gas", "Liquid to gas", "*Gas directly to solid", "Gas to liquid"], "Deposition skips the liquid phase (frost forming)."),
])

# U1 L1.2: Phase Changes
add_qs("u1_l1.2", [
    ("Sublimation is the change from:", ["Liquid to gas", "Gas to liquid", "*Solid directly to gas", "Solid to liquid"], "Dry ice (CO2) sublimes at room temperature."),
    ("During a phase change, the temperature of a substance:", ["Increases rapidly", "Decreases", "*Remains constant (energy goes to breaking/forming intermolecular bonds)", "Fluctuates"], "Energy changes phase, not temperature."),
    ("The heat of fusion refers to energy for:", ["Boiling", "*Melting (solid to liquid at melting point)", "Sublimation", "Condensation"], "Fusion = melting."),
    ("The heat of vaporization is typically _____ than heat of fusion.", ["Lower", "Equal", "*Higher (more energy needed to fully separate particles)", "Zero"], "Going from liquid to gas requires more energy."),
    ("Condensation releases energy because:", ["Bonds break", "*Gas particles slow down and form intermolecular bonds, releasing kinetic energy as heat", "Temperature drops", "Volume increases"], "Exothermic process."),
    ("A heating curve shows:", ["Only temperature", "*Temperature vs. energy added, with flat regions during phase changes", "Volume vs. pressure", "Mass vs. density"], "Plateaus indicate phase transitions."),
    ("Freezing is the reverse of:", ["Boiling", "Sublimation", "*Melting", "Deposition"], "Freezing = liquid to solid; melting = solid to liquid."),
    ("Water's unusually high heat of vaporization is due to:", ["Its low mass", "*Strong hydrogen bonds between water molecules", "Its color", "Low density"], "H-bonds require significant energy to break."),
    ("At the triple point, a substance exists as:", ["Only solid", "Only liquid", "Only gas", "*Solid, liquid, and gas simultaneously (all three phases in equilibrium)"], "Unique T and P where all three coexist."),
    ("The critical point is where:", ["All matter freezes", "*The distinction between liquid and gas phases disappears (supercritical fluid forms)", "Temperature is zero", "Pressure is zero"], "Above critical point: supercritical fluid."),
    ("Evaporation differs from boiling because:", ["They are identical", "*Evaporation occurs only at the surface and at any temperature; boiling occurs throughout the liquid at the boiling point", "Evaporation needs more energy", "Boiling occurs at the surface only"], "Evaporation is a surface phenomenon."),
    ("Phase diagrams plot:", ["Mass vs. volume", "*Pressure vs. temperature, showing regions for each phase", "Time vs. temperature", "Energy vs. mass"], "P-T diagram showing phase boundaries."),
    ("Vapor pressure increases with:", ["Decreasing temperature", "*Increasing temperature (more molecules escape to gas phase)", "Increasing volume", "Decreasing surface area"], "Higher T = more evaporation = higher vapor pressure."),
])

# U1 L1.3: Intensive vs Extensive Properties
add_qs("u1_l1.3", [
    ("Mass is an _____ property.", ["Intensive", "*Extensive (depends on the amount of substance)", "Chemical", "Nuclear"], "More substance = more mass."),
    ("Color is an _____ property.", ["Extensive", "*Intensive (doesn't depend on amount)", "Chemical", "Nuclear"], "A drop of dye has the same color as a gallon."),
    ("Which is an extensive property?", ["Temperature", "Density", "*Volume", "Boiling point"], "Volume depends on the amount of matter."),
    ("Temperature is intensive because:", ["It changes with mass", "*It doesn't change when you split a sample in half", "It's always the same", "It depends on volume"], "A cup of 80C water is 80C whether you take half or all."),
    ("Density is intensive because:", ["It depends on mass", "It depends on volume", "*The ratio of mass to volume remains constant for a given substance regardless of sample size", "It varies with amount"], "d = m/V stays the same for any sample of the same substance."),
    ("Melting point is classified as:", ["Extensive", "*Intensive", "Neither", "Both"], "Melting point is a characteristic property independent of amount."),
    ("Which property would help you identify an unknown substance?", ["Mass", "Volume", "*Density or boiling point (intensive properties are characteristic of the substance)", "Weight"], "Intensive properties identify substances."),
    ("Doubling the mass of a sample changes its:", ["Density", "Boiling point", "*Volume (extensive properties scale with amount)", "Melting point"], "Extensive properties change with amount."),
    ("Conductivity (electrical/thermal) is:", ["Extensive", "*Intensive (copper conducts the same whether large or small piece)", "Neither", "Variable"], "Property of the material, not the amount."),
    ("The heat capacity of a sample is _____, while specific heat is _____.", ["Both intensive", "Both extensive", "*Extensive; intensive (heat capacity depends on mass; specific heat is per gram)", "Intensive; extensive"], "Heat capacity scales with size; specific heat doesn't."),
    ("Hardness on Mohs scale is:", ["Extensive", "*Intensive", "Chemical", "Not a property"], "Hardness identifies minerals regardless of size."),
    ("Which would NOT help identify a mystery liquid?", ["Boiling point", "Density", "*Mass of the sample", "Refractive index"], "Mass changes with sample size and doesn't identify the liquid."),
    ("Luster (shininess) of a metal is:", ["Extensive", "*Intensive", "Chemical", "Nuclear"], "A small piece of gold shines just like a large piece."),
])

# U1 L1.4: Density
add_qs("u1_l1.4", [
    ("A substance with density less than water will:", ["Sink", "*Float", "Dissolve", "Evaporate"], "Density < 1 g/mL means it floats in water."),
    ("Water has a density of approximately:", ["0.5 g/mL", "*1.0 g/mL", "2.0 g/mL", "10 g/mL"], "Water's density at room temperature is about 1 g/mL."),
    ("A block has mass 30 g and volume 10 cm^3. Its density is:", ["300 g/cm^3", "10/30 g/cm^3", "*3.0 g/cm^3", "40 g/cm^3"], "d = m/V = 30/10 = 3.0."),
    ("If density = 2.7 g/cm^3 and volume = 15 cm^3, the mass is:", ["17.7 g", "5.56 g", "*40.5 g", "12.3 g"], "m = d * V = 2.7 * 15 = 40.5 g."),
    ("To find the volume of an irregular solid, you can use:", ["A ruler", "A scale", "*Water displacement method", "A thermometer"], "Measure volume of water displaced."),
    ("Ice floats on water because:", ["Ice is a gas", "*Ice is less dense than liquid water (water expands when freezing)", "Ice has no mass", "Water repels ice"], "Unique property: solid water is less dense than liquid."),
    ("Specific gravity compares a substance's density to:", ["Air", "*Water (at 4 degrees C)", "Mercury", "Gold"], "Specific gravity = density of substance / density of water."),
    ("Which liquid layer would be on top: oil (0.9 g/mL) or honey (1.4 g/mL)?", ["Honey", "*Oil (less dense = floats on top)", "They mix evenly", "Neither floats"], "Less dense liquids float above denser ones."),
    ("Converting density to different units: 1 g/cm^3 = _____ kg/m^3", ["1", "10", "100", "*1000"], "1 g/cm^3 = 1000 kg/m^3."),
    ("A gas has _____ density than a liquid of the same substance.", ["Higher", "*Lower (gas particles are far apart, less mass per volume)", "The same", "Double"], "Gases are much less dense."),
    ("Temperature affects density because:", ["Mass changes", "*Volume changes (most materials expand when heated, decreasing density)", "Density is constant", "Only pressure matters"], "Thermal expansion decreases density."),
    ("An object with density exactly equal to the liquid will:", ["Float on top", "Sink to bottom", "*Remain suspended (neutrally buoyant)", "Dissolve"], "Equal densities = neutral buoyancy."),
    ("The densest common element at room temperature is:", ["Gold", "Lead", "*Osmium (22.59 g/cm^3)", "Iron"], "Osmium is the densest naturally occurring element."),
])

# U1 L1.5: Mixtures
add_qs("u1_l1.5", [
    ("A heterogeneous mixture has:", ["Uniform composition", "*Visibly different regions or components (non-uniform)", "Only one substance", "No mass"], "Components are distinguishable."),
    ("Which is a heterogeneous mixture?", ["Salt water", "Air", "*Salad", "Sugar dissolved in tea"], "You can see the separate ingredients."),
    ("Solutions are _____ mixtures.", ["Heterogeneous", "*Homogeneous (uniform throughout)", "Neither", "Pure substances"], "Dissolved solute distributes evenly."),
    ("In a solution, the component in the largest amount is the:", ["Solute", "*Solvent", "Precipitate", "Residue"], "Solvent = larger quantity; solute = dissolved substance."),
    ("Filtration separates mixtures based on:", ["Density", "Color", "*Particle size (solid particles caught by filter paper)", "Boiling point"], "Filter traps solid, allows liquid through."),
    ("Distillation separates mixtures based on:", ["Mass", "Color", "*Differences in boiling point", "Particle size"], "Lower BP substance evaporates first."),
    ("A colloid is:", ["A true solution", "*A mixture with intermediate-sized particles (1-1000 nm) that don't settle (like milk or fog)", "A heterogeneous mixture", "A pure element"], "Particles are between solution and suspension size."),
    ("The Tyndall effect (light scattering) is observed in:", ["True solutions", "*Colloids (particles are large enough to scatter light)", "Pure water", "Elements"], "Colloid particles scatter a beam of light."),
    ("Chromatography separates mixtures based on:", ["Mass only", "*How strongly different components adhere to a stationary phase vs. move with a mobile phase", "Size only", "Color only"], "Different affinities = different speeds."),
    ("An alloy is a _____ mixture of metals.", ["Heterogeneous", "*Homogeneous (uniform solid solution)", "Pure", "Separated"], "Bronze, steel, brass are alloys."),
    ("Decanting separates mixtures by:", ["Boiling", "Filtering", "*Carefully pouring off liquid from settled solid", "Magnetism"], "Pour liquid off the sediment."),
    ("Which technique would best separate salt from sand?", ["Filtration alone", "Magnet", "*Dissolve in water, filter out sand, then evaporate water to recover salt", "Decanting alone"], "Dissolve, filter, evaporate."),
    ("A suspension differs from a colloid because suspension particles:", ["Are smaller", "*Are larger and will eventually settle out if left undisturbed", "Never settle", "Are dissolved"], "Suspension particles settle; colloid particles don't."),
])

# U1 L1.6: Physical Properties
add_qs("u1_l1.6", [
    ("A physical property can be observed without:", ["Any equipment", "*Changing the substance's chemical identity", "Touching it", "Measuring it"], "No chemical change required."),
    ("Which is a physical property?", ["Flammability", "Reactivity with acid", "*Melting point", "Ability to rust"], "Melting involves no chemical change."),
    ("Malleability (ability to be hammered into sheets) is a physical property of:", ["All elements", "*Metals (like gold and aluminum)", "Gases only", "Nonmetals only"], "Metals are malleable."),
    ("Ductility means a substance can be:", ["Burned", "Dissolved", "*Drawn into thin wires", "Frozen"], "Copper and gold are highly ductile."),
    ("Odor is classified as a _____ property.", ["Chemical", "*Physical (you detect it without changing the substance)", "Nuclear", "Extensive"], "Smelling doesn't alter chemical composition."),
    ("Solubility is a physical property that measures:", ["Melting speed", "*How much solute dissolves in a given amount of solvent", "Conductivity", "Hardness"], "Physical dissolution, no chemical change."),
    ("The boiling point of a substance:", ["Is always 100 degrees C", "*Is a characteristic physical property that varies by substance and pressure", "Changes with mass", "Is a chemical property"], "Each substance has a unique BP at given pressure."),
    ("Which property can be measured without a chemical reaction?", ["Heat of combustion", "Reactivity", "Toxicity", "*Electrical conductivity"], "Conductivity is measured physically."),
    ("Crystal structure is a physical property because:", ["It involves chemistry", "*It describes the arrangement of particles without changing their identity", "It only applies to liquids", "It requires a reaction"], "Geometry of particle arrangement."),
    ("Magnetic properties (ferromagnetism) of iron are:", ["Chemical properties", "*Physical properties (no chemical change occurs when a magnet attracts iron)", "Nuclear properties", "Not properties"], "Magnetism is a physical interaction."),
    ("Refractive index measures how light:", ["Is absorbed", "*Bends when passing through a substance (each substance has a characteristic value)", "Is created", "Is blocked"], "Physical optical property."),
    ("Physical properties are used to:", ["Create new substances", "*Identify, describe, and classify substances without altering them", "Cause reactions", "Measure energy only"], "Identification tool."),
    ("Elasticity (ability to return to original shape) is:", ["A chemical property", "*A physical property", "Not measurable", "Only for gases"], "No chemical change involved."),
])

# U1 L1.7: Chemical Changes
add_qs("u1_l1.7", [
    ("A chemical change produces:", ["The same substance", "*One or more new substances with different properties", "Only physical changes", "No change"], "New chemical bonds form."),
    ("Evidence of a chemical change includes:", ["Dissolving", "*Color change, gas production, precipitate formation, energy change", "Melting", "Boiling"], "Observable signs of new substances forming."),
    ("Burning wood is a chemical change because:", ["Wood changes shape", "*New substances (ash, CO2, water vapor) form with different properties", "Wood melts", "Wood gets smaller"], "Combustion creates new chemical compounds."),
    ("Rusting of iron is a:", ["Physical change", "*Chemical change (iron reacts with oxygen to form iron oxide, a new substance)", "Phase change", "Nuclear change"], "Fe + O2 forms Fe2O3."),
    ("Which is NOT a chemical change?", ["Cooking an egg", "Silver tarnishing", "*Crushing a can", "Burning gasoline"], "Crushing only changes shape, not chemical identity."),
    ("A chemical property describes a substance's ability to:", ["Be measured", "Dissolve", "*Undergo a specific chemical change or reaction", "Change phase"], "Reactivity is a chemical property."),
    ("Flammability is a _____ property.", ["Physical", "*Chemical (describes ability to burn, which is a chemical reaction)", "Extensive", "Intensive"], "Burning changes chemical composition."),
    ("Reactivity with water is a _____ property.", ["Physical", "*Chemical", "Nuclear", "Optical"], "Sodium reacting with water produces new substances."),
    ("Tarnishing of silver involves:", ["Physical change only", "*Chemical reaction with sulfur compounds in air forming silver sulfide", "Melting", "No change"], "Ag + S compounds = Ag2S (black tarnish)."),
    ("Decomposition of hydrogen peroxide into water and oxygen is:", ["Physical", "*Chemical (H2O2 breaks into H2O + O2, new substances form)", "Neither", "A phase change"], "Chemical bonds break and reform."),
    ("Can a chemical change typically be reversed easily?", ["Yes, always", "*No, most chemical changes are difficult or impossible to reverse simply", "They reverse automatically", "Only with heat"], "Unlike physical changes, chemical changes are generally irreversible."),
    ("Photosynthesis is a chemical change because:", ["Plants grow bigger", "*CO2 and H2O are converted to glucose and O2 (new substances)", "Leaves change color in fall", "Water evaporates"], "6CO2 + 6H2O -> C6H12O6 + 6O2."),
    ("Digestion of food is a:", ["Physical change", "*Chemical change (enzymes break food into new molecules the body can use)", "Phase change", "Nuclear change"], "Complex molecules are broken into simpler ones."),
])

# U1 L1.8: Conservation of Energy
add_qs("u1_l1.8", [
    ("The total amount of energy in a closed system:", ["Increases over time", "Decreases over time", "*Remains constant (energy is conserved)", "Becomes zero"], "First law of thermodynamics."),
    ("Energy can be _____ but not _____ or _____.", ["Created; transferred; destroyed", "*Transformed/transferred; created; destroyed", "Destroyed; measured; observed", "Lost; gained; transferred"], "Energy changes form but total stays constant."),
    ("Kinetic energy is:", ["Stored energy", "*Energy of motion", "Thermal energy only", "Chemical energy only"], "Moving objects have kinetic energy."),
    ("Potential energy includes:", ["Only gravitational", "Only kinetic", "*Chemical, gravitational, elastic, and other stored forms of energy", "No forms"], "Stored energy in various forms."),
    ("In an exothermic reaction, energy is:", ["Absorbed from surroundings", "*Released to surroundings (products have less energy than reactants)", "Created", "Destroyed"], "Exothermic = energy out."),
    ("In an endothermic reaction, energy is:", ["Released", "*Absorbed from surroundings (products have more energy than reactants)", "Created from nothing", "Destroyed"], "Endothermic = energy in."),
    ("A ball at the top of a hill has maximum:", ["Kinetic energy", "*Potential energy (gravitational)", "Thermal energy", "Chemical energy"], "Height = gravitational PE."),
    ("As the ball rolls down, potential energy converts to:", ["More potential energy", "*Kinetic energy", "Chemical energy", "Nuclear energy"], "PE decreases as KE increases."),
    ("The law of conservation of mass in chemical reactions means:", ["Mass is created", "Mass is destroyed", "*Total mass of reactants = total mass of products", "Mass changes to energy"], "Mass is conserved in chemical reactions."),
    ("In a battery, _____ energy is converted to _____ energy.", ["Thermal; nuclear", "*Chemical; electrical", "Light; sound", "Nuclear; chemical"], "Chemical reactions in batteries produce electricity."),
    ("Solar panels convert _____ to _____.", ["Heat to light", "*Light energy to electrical energy", "Chemical to light", "Nuclear to chemical"], "Photovoltaic cells convert sunlight to electricity."),
    ("Entropy is the measure of:", ["Energy", "Temperature", "*Disorder or randomness in a system (tends to increase)", "Mass"], "Second law: entropy of the universe increases."),
    ("Which energy transformation occurs in a car engine?", ["Electrical to kinetic", "*Chemical (fuel) to thermal to kinetic (motion)", "Nuclear to thermal", "Kinetic to potential"], "Fuel combustion produces heat, which drives pistons."),
])

# U2 L2.1: Scientific Notation
add_qs("u2_l2.1", [
    ("Express 0.00032 in scientific notation:", ["32 x 10^-5", "3.2 x 10^-3", "*3.2 x 10^-4", "3.2 x 10^4"], "Move decimal 4 places right: 3.2 x 10^-4."),
    ("What is 6.02 x 10^23 in standard form?", ["602,000,000,000,000,000,000,000", "*602,000,000,000,000,000,000,000 (Avogadro's number)", "60.2 x 10^22", "6.02 x 10^-23"], "Move decimal 23 places right."),
    ("Multiply: (2 x 10^3)(3 x 10^4) =", ["6 x 10^7", "5 x 10^7", "*6 x 10^7", "6 x 10^12"], "Multiply coefficients, add exponents: 2*3=6, 3+4=7."),
    ("Divide: (8 x 10^6) / (2 x 10^2) =", ["4 x 10^8", "*4 x 10^4", "4 x 10^3", "6 x 10^4"], "Divide coefficients, subtract exponents: 8/2=4, 6-2=4."),
    ("The coefficient in scientific notation must be between:", ["0 and 1", "*1 and 10 (inclusive of 1, exclusive of 10)", "10 and 100", "Any numbers"], "Proper scientific notation: 1 <= coefficient < 10."),
    ("Add: 3.0 x 10^4 + 2.0 x 10^4 =", ["5.0 x 10^8", "*5.0 x 10^4", "5.0 x 10^3", "1.0 x 10^4"], "Same exponent: add coefficients."),
    ("Which is NOT in proper scientific notation?", ["3.5 x 10^2", "1.0 x 10^-3", "*12.5 x 10^3 (coefficient must be less than 10)", "9.9 x 10^0"], "12.5 is not between 1 and 10."),
    ("Express 12.5 x 10^3 in proper scientific notation:", ["12.5 x 10^3", "125 x 10^2", "*1.25 x 10^4", "0.125 x 10^5"], "Move decimal: 1.25 x 10^4."),
    ("The diameter of an atom is approximately 10^-10 m. This is:", ["1 millimeter", "1 micrometer", "*0.1 nanometers (1 angstrom)", "1 centimeter"], "Atomic scale is sub-nanometer."),
    ("Scientific notation is essential in chemistry because:", ["Numbers are always small", "*Chemistry involves extremely large (Avogadro) and small (atomic) numbers", "It looks impressive", "Calculators require it"], "Convenient for very large or very small values."),
    ("Convert: 5.67 x 10^-8 to standard notation:", ["0.0000567", "0.000000567", "*0.0000000567", "567 x 10^-10"], "Move decimal 8 places left."),
    ("On a calculator, E or EE button means:", ["Error", "Equals", "*x 10^ (enter the exponent after pressing E/EE)", "Exponent only"], "Calculator shorthand for scientific notation."),
    ("(1.5 x 10^3)^2 =", ["1.5 x 10^6", "*2.25 x 10^6", "3.0 x 10^6", "1.5 x 10^9"], "1.5^2 = 2.25, (10^3)^2 = 10^6."),
])

# U2 L2.2: Significant Figures
add_qs("u2_l2.2", [
    ("How many significant figures in 0.0200?", ["1", "2", "*3 (the 2 and both trailing zeros after the decimal)", "4"], "Leading zeros are not significant; trailing zeros after decimal are."),
    ("How many sig figs in 1,000?", ["4", "3", "2", "*1 (ambiguous, but typically 1 without a decimal point)"], "Without decimal: trailing zeros are ambiguous, assumed not significant."),
    ("How many sig figs in 1,000.?", ["1", "3", "*4 (the decimal point indicates all zeros are significant)", "5"], "Decimal point makes all digits significant."),
    ("When multiplying, the answer should have:", ["The most sig figs", "*The fewest sig figs of any factor", "Always 3 sig figs", "Unlimited sig figs"], "Multiplication/division: fewest sig figs rule."),
    ("When adding/subtracting, the answer should have:", ["Fewest sig figs", "*Fewest decimal places of any number in the calculation", "Most decimal places", "Always 2 decimal places"], "Addition/subtraction: fewest decimal places."),
    ("12.11 + 0.3 = _____ (properly rounded)", ["12.41", "*12.4 (round to 1 decimal place, matching 0.3)", "12.410", "12"], "0.3 has fewest decimal places (1)."),
    ("2.5 x 3.42 = _____ (proper sig figs)", ["8.55", "8.550", "*8.6 (2 sig figs, matching 2.5)", "9"], "2.5 has 2 sig figs, so answer has 2."),
    ("Exact numbers (like counts) have:", ["1 sig fig", "3 sig figs", "*Unlimited significant figures", "No sig figs"], "Counting numbers and defined values are exact."),
    ("The number 0.0050 has _____ significant figures.", ["1", "*2 (5 and the trailing zero)", "3", "4"], "Leading zeros are placeholders, not significant."),
    ("When rounding 2.450 to 2 sig figs:", ["2.4", "*2.4 (round-half-to-even rule) or 2.5 (depending on convention)", "2.5", "2.45"], "The '5' rounding rule varies by convention."),
    ("Scientific notation makes sig figs unambiguous because:", ["It eliminates zeros", "*Only significant digits appear in the coefficient (e.g., 1.0 x 10^3 = 2 sig figs)", "It rounds everything", "It adds precision"], "Coefficient shows exactly which digits are significant."),
    ("In the measurement 25.0 mL, the zero is:", ["Not significant", "*Significant (it indicates precision to the tenths place)", "A placeholder", "Uncertain"], "Trailing zero after decimal in a measurement is significant."),
    ("All nonzero digits are:", ["Sometimes significant", "*Always significant", "Never significant", "Significant only in scientific notation"], "Rule 1 of significant figures."),
])

# U2 L2.3: Accuracy & Precision
add_qs("u2_l2.3", [
    ("Precision refers to:", ["How close to the true value", "*How close repeated measurements are to EACH OTHER (reproducibility)", "How fast you measure", "How expensive the tool is"], "Precise = consistent/repeatable."),
    ("A measurement can be precise but not accurate if:", ["Measurements are scattered", "*All measurements cluster together but far from the true value (systematic error)", "Measurements are accurate", "Equipment works perfectly"], "Precise but inaccurate = systematic bias."),
    ("Random errors cause measurements to:", ["All be too high", "All be too low", "*Scatter equally above and below the true value", "Be perfectly accurate"], "Random errors fluctuate unpredictably."),
    ("Systematic errors cause measurements to:", ["Scatter randomly", "*Be consistently too high or too low (shifted in one direction)", "Be perfectly precise", "Cancel out"], "Systematic = bias in one direction."),
    ("Percent error formula: |(experimental - accepted)/accepted| x 100. If exp = 3.12 g/mL, accepted = 3.00 g/mL:", ["4.0%", "3.0%", "*4.0%", "0.12%"], "|3.12-3.00|/3.00 x 100 = 0.12/3.00 x 100 = 4.0%."),
    ("Which would improve accuracy?", ["Using the same broken thermometer", "*Calibrating instruments against known standards", "Repeating with the same error", "Measuring faster"], "Calibration eliminates systematic error."),
    ("Which would improve precision?", ["Using a different method each time", "Calibrating once", "*Using more precise instruments and controlling variables carefully", "Estimating values"], "Better equipment = more reproducible."),
    ("An analogy: accuracy is hitting the bullseye, precision is:", ["Missing every time", "*All shots clustered tightly together (even if not centered on bullseye)", "Random shots", "One lucky shot"], "Tight grouping = precise."),
    ("Increasing the number of trials improves the _____ of the average.", ["Precision only", "*Both accuracy (of the mean) and ability to detect random error", "Neither", "Only systematic error"], "More trials = better statistical average."),
    ("A student consistently reads a ruler 0.5 cm too high. This is a:", ["Random error", "*Systematic error (always biased in the same direction)", "No error", "Calculation error"], "Consistent bias = systematic."),
    ("Standard deviation measures:", ["Accuracy", "*Precision (the spread of data points around the mean)", "Systematic error", "Percent error"], "SD quantifies how spread out values are."),
    ("An instrument with higher resolution (smaller divisions) generally gives:", ["Less data", "*More precise measurements", "Less accurate results", "More systematic error"], "Finer divisions = more detail = higher precision."),
    ("Significant figures in a measurement reflect its:", ["Accuracy", "*Precision (the number of reliably known digits)", "Both equally", "Neither"], "Sig figs indicate measurement precision."),
])

# U2 L2.4: SI Units
add_qs("u2_l2.4", [
    ("The SI unit of length is the:", ["Foot", "Inch", "*Meter", "Yard"], "Meter is the base SI unit for length."),
    ("The SI unit of temperature is the:", ["Celsius", "Fahrenheit", "*Kelvin", "Rankine"], "Kelvin is the SI base unit."),
    ("K = C + _____", ["100", "32", "*273.15", "460"], "Kelvin = Celsius + 273.15."),
    ("To convert Celsius to Fahrenheit:", ["F = C + 32", "*F = (9/5)C + 32", "F = C - 32", "F = (5/9)C + 32"], "Standard conversion formula."),
    ("The prefix 'kilo-' means:", ["1/1000", "100", "*1000", "1,000,000"], "Kilo = 10^3."),
    ("The prefix 'milli-' means:", ["1000", "100", "*1/1000 (10^-3)", "1/100"], "Milli = 10^-3."),
    ("The prefix 'nano-' means:", ["10^-3", "10^-6", "*10^-9", "10^-12"], "Nano = one billionth."),
    ("1 cm = _____ m", ["100", "10", "*0.01", "0.001"], "Centi = 10^-2, so 1 cm = 0.01 m."),
    ("Dimensional analysis uses _____ to convert between units.", ["Addition", "Subtraction", "*Conversion factors (ratios equal to 1)", "Multiplication only"], "Unit ratios that equal 1."),
    ("Convert 2.5 kg to grams:", ["0.0025 g", "25 g", "*2500 g", "250 g"], "2.5 x 1000 = 2500 g."),
    ("Convert 500 mL to liters:", ["5 L", "50 L", "*0.5 L", "0.05 L"], "500/1000 = 0.5 L."),
    ("The SI unit of time is the:", ["Minute", "Hour", "*Second", "Day"], "Second is the base SI unit for time."),
    ("The SI unit of amount of substance is the:", ["Gram", "Liter", "*Mole", "Atom"], "Mole is the SI base unit for amount."),
])

# U2 L2.5: Unit Conversions
add_qs("u2_l2.5", [
    ("How many centimeters are in 1 meter?", ["10", "*100", "1000", "10000"], "1 m = 100 cm."),
    ("A conversion factor is a ratio that equals:", ["0", "2", "*1 (because the numerator and denominator represent the same quantity)", "Infinity"], "Equal numerator and denominator in different units."),
    ("Convert 3.5 hours to minutes:", ["35 min", "*210 min (3.5 x 60)", "350 min", "3500 min"], "3.5 * 60 = 210 minutes."),
    ("Convert 250 cm to meters:", ["25 m", "0.025 m", "*2.5 m", "0.25 m"], "250 / 100 = 2.5 m."),
    ("Multi-step conversion: 5 km to cm:", ["500 cm", "5000 cm", "50,000 cm", "*500,000 cm (5 x 1000 x 100)"], "5 km = 5000 m = 500,000 cm."),
    ("In dimensional analysis, units must _____ to cancel.", ["Add", "Be different", "*Appear in both numerator and denominator of successive conversion factors", "Be the same"], "Opposite positions cancel."),
    ("Convert 72 km/h to m/s:", ["72 m/s", "7.2 m/s", "*20 m/s (72 x 1000/3600)", "720 m/s"], "72000 m / 3600 s = 20 m/s."),
    ("1 inch = 2.54 cm. How many cm in 6 inches?", ["12.54 cm", "*15.24 cm", "25.4 cm", "6.54 cm"], "6 x 2.54 = 15.24 cm."),
    ("Convert 0.75 L to mL:", ["7.5 mL", "75 mL", "*750 mL", "7500 mL"], "0.75 x 1000 = 750 mL."),
    ("Density as a conversion factor: if d = 2.0 g/mL, what mass is 50 mL?", ["25 g", "52 g", "*100 g", "2.0 g"], "50 mL x 2.0 g/mL = 100 g."),
    ("When setting up a conversion, you should always check that:", ["Numbers are large", "Answers look nice", "*Unwanted units cancel and desired units remain", "You used addition"], "Unit analysis validates the setup."),
    ("Convert 37 degrees C (body temperature) to Kelvin:", ["37 K", "236 K", "*310 K (37 + 273)", "373 K"], "K = C + 273 = 310 K."),
    ("A student gets 0.005 km when converting 500 cm to km. Is this correct?", ["No, too small", "*Yes (500 cm = 5 m = 0.005 km)", "No, too large", "Cannot determine"], "500/100 = 5 m; 5/1000 = 0.005 km."),
])

# U3 L3.1: Atomic Structure
add_qs("u3_l3.1", [
    ("Protons are located in the:", ["Electron cloud", "*Nucleus", "Outer shell", "Between atoms"], "Protons are in the dense central nucleus."),
    ("Neutrons have a charge of:", ["Positive", "Negative", "*Zero (neutral)", "Variable"], "Neutrons have no electrical charge."),
    ("Electrons have a charge of:", ["Positive", "*Negative", "Zero", "Variable"], "Electrons carry a -1 charge."),
    ("The atomic number equals the number of:", ["Neutrons", "Electrons only", "*Protons", "Protons + neutrons"], "Atomic number = proton count = element identity."),
    ("In a neutral atom, the number of protons equals:", ["Neutrons", "Mass number", "*Electrons", "Nothing"], "Neutral: protons = electrons (charges balance)."),
    ("Most of an atom's mass comes from:", ["Electrons", "*Protons and neutrons (in the nucleus)", "Empty space", "The electron cloud"], "Nucleus contains nearly all the mass."),
    ("The nucleus is _____ compared to the total atom.", ["Very large", "*Extremely small (about 1/100,000 the diameter of the atom)", "The same size", "Half the size"], "Atom is mostly empty space."),
    ("Rutherford's gold foil experiment showed that:", ["Atoms are solid spheres", "Electrons are in the nucleus", "*Most of the atom is empty space with a dense, positive nucleus", "Atoms have no nucleus"], "Most alpha particles passed through; few bounced back."),
    ("Thomson's 'plum pudding' model was replaced because:", ["It was too simple", "*Rutherford showed the positive charge is concentrated in a tiny nucleus, not spread throughout", "Electrons don't exist", "It was correct"], "Gold foil experiment disproved it."),
    ("The number of protons defines:", ["The mass", "The charge only", "*The element's identity (changing protons changes the element)", "The period"], "Each element has a unique proton count."),
    ("Removing an electron from a neutral atom creates:", ["An anion", "*A cation (positive ion)", "A neutron", "A new element"], "Losing electron = net positive charge."),
    ("Adding an electron to a neutral atom creates:", ["A cation", "*An anion (negative ion)", "A proton", "A new element"], "Gaining electron = net negative charge."),
    ("Quarks make up:", ["Electrons", "*Protons and neutrons", "Photons", "Nothing in chemistry"], "Protons and neutrons are composed of quarks."),
])

# U3 L3.2: Mass Number & Isotopes
add_qs("u3_l3.2", [
    ("Mass number = protons + _____.", ["Electrons", "*Neutrons", "Energy", "Quarks"], "Mass number = p + n."),
    ("Carbon-14 has 6 protons and _____ neutrons.", ["6", "*8 (14 - 6)", "14", "12"], "Mass number - atomic number = neutrons."),
    ("Isotopes are atoms of the same element with different numbers of:", ["Protons", "Electrons", "*Neutrons", "All subatomic particles"], "Same protons, different neutrons."),
    ("The notation _{6}^{14}C means:", ["6 neutrons, 14 protons", "*6 protons (atomic number), 14 mass number (6p + 8n)", "14 protons, 6 electrons", "6 electrons, 14 neutrons"], "Subscript = atomic number, superscript = mass number."),
    ("Atomic mass on the periodic table is a _____ of naturally occurring isotopes.", ["Simple average", "*Weighted average (based on relative abundance)", "Sum", "Product"], "More abundant isotopes contribute more."),
    ("If chlorine-35 is 75% abundant and chlorine-37 is 25%, the atomic mass is:", ["36.0", "36.5", "*35.5 (0.75 x 35 + 0.25 x 37)", "37.0"], "Weighted average calculation."),
    ("Which are isotopes of each other?", ["C-12 and N-14", "*C-12 and C-14 (same element, different mass)", "O-16 and S-16", "H-1 and He-4"], "Same element (same Z), different mass number."),
    ("The mass of a proton is approximately:", ["0 amu", "*1 amu", "2 amu", "12 amu"], "Both protons and neutrons are approximately 1 amu."),
    ("Electron mass is approximately _____ of proton mass.", ["Equal", "Half", "*1/1836 (negligible compared to protons/neutrons)", "Double"], "Electrons are much lighter."),
    ("An amu (atomic mass unit) is defined as:", ["1 gram", "Mass of hydrogen", "*1/12 the mass of a carbon-12 atom", "Mass of an electron"], "Standard definition."),
    ("Hydrogen has three isotopes: protium(1), deuterium(2), tritium(3). Tritium has _____ neutron(s).", ["0", "1", "*2", "3"], "3 - 1 = 2 neutrons."),
    ("Isotopes of an element have the same:", ["Mass", "Number of neutrons", "*Chemical properties (same electron configuration)", "Mass number"], "Same protons and electrons = same chemistry."),
    ("A mass spectrometer separates isotopes based on:", ["Color", "Size", "*Mass-to-charge ratio", "Chemical reactivity"], "Different masses follow different paths in the instrument."),
])

# U3 L3.3: Quantum Mechanical Model
add_qs("u3_l3.3", [
    ("The quantum mechanical model treats electrons as:", ["Tiny planets orbiting the nucleus", "*Probability clouds (orbitals) rather than fixed paths", "Stationary particles", "Waves only"], "Electron position is described by probability."),
    ("Heisenberg's uncertainty principle states that:", ["Everything is certain", "*You cannot simultaneously know both the exact position and momentum of an electron", "Electrons are in fixed orbits", "Energy is continuous"], "Fundamental limit on measurement."),
    ("An orbital represents:", ["A fixed path", "*A region of space where there is a high probability of finding an electron", "The nucleus", "A neutron path"], "Probability region, not a defined orbit."),
    ("The principal quantum number (n) describes:", ["Spin", "Shape", "*The energy level and approximate distance from the nucleus", "Orientation"], "n = 1, 2, 3... Higher n = higher energy."),
    ("The angular momentum quantum number (l) describes:", ["Energy level", "*The shape of the orbital (s, p, d, f)", "Spin direction", "Distance from nucleus"], "l determines orbital shape."),
    ("The magnetic quantum number (m_l) describes:", ["Energy", "Shape", "*The orientation of the orbital in space", "Spin"], "m_l distinguishes orbitals within a sublevel."),
    ("The spin quantum number (m_s) can be:", ["0 or 1", "Only +1/2", "*+1/2 or -1/2", "Any integer"], "Two possible spin states."),
    ("According to the Pauli exclusion principle:", ["Electrons attract each other", "*No two electrons in an atom can have the same set of four quantum numbers", "Electrons can share orbitals freely", "Spin doesn't matter"], "Each electron has a unique quantum state."),
    ("The Aufbau principle states that electrons fill:", ["Random orbitals", "Highest energy first", "*Lowest available energy orbitals first", "Only s orbitals"], "Build up from lowest energy."),
    ("Hund's rule states that electrons fill orbitals of equal energy:", ["In pairs first", "*One at a time (with parallel spins) before pairing up", "Randomly", "In reverse order"], "Maximize unpaired electrons."),
    ("The Bohr model worked for _____ but failed for larger atoms.", ["Helium", "*Hydrogen (one electron)", "Carbon", "All atoms"], "Bohr's model only accurately predicts hydrogen spectra."),
    ("De Broglie proposed that electrons have:", ["Only particle properties", "*Wave-particle duality (wavelike behavior)", "No wave properties", "Only wave properties"], "Matter waves: lambda = h/mv."),
    ("Electron clouds are denser where:", ["Electrons never appear", "*The probability of finding an electron is higher", "The nucleus is located", "Protons exist"], "Darker cloud = higher probability."),
])

# U3 L3.4: Electromagnetic Spectrum
add_qs("u3_l3.4", [
    ("The relationship between frequency and wavelength is:", ["Direct", "*Inverse (as one increases, the other decreases)", "No relationship", "Exponential"], "c = lambda * nu; if lambda up, nu down."),
    ("The speed of light (c) is approximately:", ["3 x 10^6 m/s", "*3 x 10^8 m/s", "3 x 10^10 m/s", "186 m/s"], "Speed of all electromagnetic radiation in vacuum."),
    ("Which has the highest energy?", ["Radio waves", "Microwaves", "Visible light", "*Gamma rays"], "Highest frequency = shortest wavelength = highest energy."),
    ("Which has the longest wavelength?", ["*Radio waves", "X-rays", "Ultraviolet", "Gamma rays"], "Radio waves have the lowest frequency and longest wavelength."),
    ("The energy of a photon is calculated by:", ["E = mc", "E = hc", "*E = hf (Planck's constant times frequency)", "E = mv^2"], "Planck's equation: E = hf."),
    ("Planck's constant (h) is approximately:", ["6.02 x 10^23", "*6.626 x 10^-34 J*s", "3.0 x 10^8 m/s", "1.602 x 10^-19 C"], "Fundamental constant of quantum mechanics."),
    ("Excited atoms emit light when:", ["Protons vibrate", "*Electrons drop from higher to lower energy levels, releasing photons", "Neutrons split", "Atoms collide"], "Energy level transitions produce photons."),
    ("Line spectra (discrete colors) show that:", ["Electrons exist everywhere", "*Electron energy levels are quantized (only specific energies allowed)", "Light is continuous", "Atoms are opaque"], "Quantized energy = discrete spectral lines."),
    ("Each element has a _____ line spectrum.", ["Identical", "*Unique (like a fingerprint)", "Continuous", "Random"], "Element identification by emission spectrum."),
    ("Visible light spans wavelengths of approximately:", ["100-200 nm", "*380-700 nm", "700-1000 nm", "1-100 nm"], "Violet (380 nm) to red (700 nm)."),
    ("Infrared radiation is associated with:", ["Visible color", "Nuclear reactions", "*Heat (thermal radiation)", "X-ray imaging"], "We feel infrared as warmth."),
    ("UV radiation from the sun can cause:", ["Cooling", "*Sunburn and DNA damage", "Radio interference", "Sound waves"], "UV has enough energy to damage biological molecules."),
    ("The photoelectric effect demonstrated that light:", ["Is only a wave", "*Behaves as particles (photons) with quantized energy", "Has no energy", "Cannot eject electrons"], "Einstein's explanation: photon energy ejects electrons."),
])

# U3 L3.5: Radioactive Decay
add_qs("u3_l3.5", [
    ("Alpha decay emits:", ["An electron", "A photon", "*A helium-4 nucleus (2 protons + 2 neutrons)", "A neutron"], "Alpha particle = He-4 nucleus."),
    ("Beta decay converts a neutron into:", ["Another neutron", "*A proton and an electron (the electron is emitted)", "A photon", "An alpha particle"], "Beta particle = high-speed electron."),
    ("Gamma radiation is:", ["A particle", "*High-energy electromagnetic radiation (photon, no mass or charge)", "An alpha particle", "A beta particle"], "Gamma = pure energy, no mass."),
    ("Which radiation is stopped by a sheet of paper?", ["Beta", "Gamma", "*Alpha (lowest penetrating power)", "X-rays"], "Alpha particles are large and easily stopped."),
    ("Which radiation requires lead or thick concrete to stop?", ["Alpha", "Beta", "*Gamma", "Infrared"], "Gamma rays have the highest penetrating power."),
    ("Nuclear stability depends on:", ["Only protons", "Only neutrons", "*The ratio of neutrons to protons (n/p ratio)", "Only electrons"], "Balanced n/p ratio = stable nucleus."),
    ("Carbon-14 dating works because:", ["Carbon-14 is stable", "*Carbon-14 decays at a known rate (half-life ~5,730 years), allowing age calculation", "All carbon decays", "Carbon-14 is created in labs"], "Radioactive decay as a clock."),
    ("A chain reaction in nuclear fission occurs when:", ["Fusion starts", "*Neutrons from one fission event trigger additional fission events", "Alpha particles accumulate", "Gamma rays multiply"], "Self-sustaining fission process."),
    ("Nuclear fusion combines:", ["Heavy nuclei", "*Light nuclei to form heavier ones (releasing enormous energy)", "Protons and electrons", "Molecules"], "Stars are powered by fusion."),
    ("Positron emission is similar to beta decay but emits:", ["An electron", "*A positron (positive electron, antimatter)", "A neutron", "An alpha particle"], "Positron = anti-electron."),
    ("Electron capture occurs when:", ["An electron is emitted", "*The nucleus absorbs an inner-shell electron, converting a proton to a neutron", "Beta decay", "Gamma is emitted"], "Proton + electron = neutron."),
    ("Transmutation is:", ["A chemical reaction", "*Changing one element into another through nuclear reactions", "Dissolving a substance", "A phase change"], "Nuclear reactions change element identity."),
    ("The strong nuclear force:", ["Repels protons", "*Holds protons and neutrons together in the nucleus (overcomes electrostatic repulsion)", "Is electromagnetic", "Acts over long distances"], "Strongest force, but very short range."),
])

# U3 L3.6: Isotopes (detailed)
add_qs("u3_l3.6", [
    ("Radioisotopes are isotopes that:", ["Are stable", "*Are radioactive (undergo nuclear decay)", "Have no neutrons", "Are man-made only"], "Unstable isotopes that emit radiation."),
    ("Medical imaging uses radioisotopes like:", ["Carbon-12", "Oxygen-16", "*Technetium-99m (most commonly used in nuclear medicine)", "Iron-56"], "Tc-99m has ideal properties for imaging."),
    ("Iodine-131 is used to treat:", ["Broken bones", "Heart disease", "*Thyroid disorders (thyroid absorbs iodine selectively)", "Headaches"], "Targeted radiation therapy."),
    ("Stable isotopes have:", ["Too many protons", "Too many neutrons", "*A balanced neutron-to-proton ratio within the band of stability", "No neutrons"], "Balanced n/p ratio."),
    ("The band of stability is a plot of:", ["Mass vs. volume", "*Number of neutrons vs. number of protons for stable nuclei", "Energy vs. time", "Decay rate vs. mass"], "Stable nuclei fall within this band."),
    ("For light elements (Z < 20), stable nuclei tend to have:", ["Many more neutrons than protons", "*Approximately equal numbers of neutrons and protons (n/p ratio near 1)", "No neutrons", "Twice as many protons"], "Light elements: n approximately equals p."),
    ("For heavy elements, stable nuclei need:", ["Fewer neutrons", "*More neutrons than protons (higher n/p ratio) to offset proton-proton repulsion", "Equal p and n", "Only protons"], "Extra neutrons stabilize heavy nuclei."),
    ("Elements with Z > 83 (bismuth):", ["Are all stable", "*Have no stable isotopes (all are radioactive)", "Have only one isotope", "Are nonmetals"], "All elements above Bi are radioactive."),
    ("Enrichment of uranium increases the proportion of:", ["U-238", "*U-235 (the fissile isotope used in reactors and weapons)", "U-234", "Plutonium"], "Natural uranium is mostly U-238; U-235 is fissile."),
    ("Carbon-12 and carbon-13 are both:", ["Radioactive", "*Stable isotopes of carbon (C-14 is radioactive)", "Gases", "Man-made"], "Both occur naturally and are non-radioactive."),
    ("Isotope notation: hydrogen-2 (deuterium) has:", ["2 protons", "*1 proton and 1 neutron", "2 neutrons", "No neutrons"], "Mass 2 - atomic number 1 = 1 neutron."),
    ("Heavy water (D2O) contains:", ["Regular hydrogen", "*Deuterium (hydrogen-2) instead of protium (hydrogen-1)", "Tritium only", "No hydrogen"], "Deuterium-based water."),
    ("Isotopic abundance is measured by:", ["Color", "Smell", "*Mass spectrometry (separates isotopes by mass)", "Titration"], "Mass spectrometer determines isotope ratios."),
])

# U3 L3.7: Stellar Nucleosynthesis
add_qs("u3_l3.7", [
    ("The Big Bang primarily produced:", ["All elements", "Only iron", "*Hydrogen and helium (the lightest elements)", "Only carbon"], "Primordial nucleosynthesis: H, He, trace Li."),
    ("Stars fuse hydrogen into:", ["Carbon", "Iron", "*Helium (in main sequence stars)", "Uranium"], "Main sequence fusion: H to He."),
    ("Elements up to iron (Fe) are made by:", ["Radioactive decay", "*Nuclear fusion in stellar cores (progressively heavier fusion)", "Chemical reactions", "Fission"], "Successive fusion stages in massive stars."),
    ("Why does fusion stop at iron?", ["Iron is too heavy", "*Fusing iron requires more energy input than it releases (endothermic beyond this point)", "Iron is radioactive", "Stars run out of hydrogen"], "Iron is the most tightly bound nucleus."),
    ("Elements heavier than iron are primarily created in:", ["Our sun", "*Supernovae (the explosive death of massive stars) and neutron star mergers", "Small stars", "Planets"], "Extreme conditions needed for heavy element synthesis."),
    ("The Sun's primary fusion reaction converts:", ["Helium to carbon", "*Hydrogen to helium (proton-proton chain)", "Carbon to nitrogen", "Iron to gold"], "Proton-proton chain: 4H -> He + energy."),
    ("Gold, platinum, and uranium were created by:", ["The Sun", "The Big Bang", "*Supernovae and/or neutron star collisions (r-process nucleosynthesis)", "Volcanoes"], "Rapid neutron capture during extreme events."),
    ("The phrase 'we are made of star stuff' means:", ["Stars are alive", "Humans are stars", "*The elements in our bodies were forged in ancient stars", "Stars have DNA"], "Nucleosynthesis created Earth's elements."),
    ("A red giant star fuses helium into:", ["Hydrogen", "*Carbon and oxygen (triple-alpha process)", "Iron", "Uranium"], "Helium-burning phase: He -> C, O."),
    ("S-process (slow neutron capture) occurs in:", ["Supernovae", "*Asymptotic giant branch (AGB) stars over long periods", "The Big Bang", "Black holes"], "Slow capture creates elements up to bismuth."),
    ("R-process (rapid neutron capture) occurs in:", ["Main sequence stars", "The Sun", "*Supernovae and neutron star mergers (extreme neutron-rich environments)", "Planets"], "Creates heaviest elements very quickly."),
    ("The abundance of elements in the universe: _____ is most common.", ["Carbon", "Iron", "*Hydrogen (about 74% of baryonic matter)", "Oxygen"], "Hydrogen is overwhelmingly the most abundant element."),
    ("Earth's elements came from:", ["Only our Sun", "Only the Big Bang", "*A combination of Big Bang (H, He) and previous generations of stars (heavier elements)", "Space dust only"], "Multiple sources over cosmic time."),
])

# U3 L3.8: History of Atomic Theory
add_qs("u3_l3.8", [
    ("Democritus (ancient Greece) proposed that:", ["Atoms are divisible", "*Matter is made of indivisible particles called 'atomos'", "Elements are earth, water, fire, air", "Atoms don't exist"], "First atomic idea, but philosophical, not experimental."),
    ("Dalton's atomic theory (1803) stated that:", ["Atoms are divisible", "*All matter is made of indivisible atoms, each element has unique atoms with specific masses", "Electrons orbit nuclei", "Atoms contain subatomic particles"], "First modern, evidence-based atomic theory."),
    ("Thomson discovered the _____ in 1897.", ["Proton", "Neutron", "*Electron (using cathode ray tubes)", "Nucleus"], "Cathode ray experiments revealed negatively charged particles."),
    ("Thomson's model is called the _____ model.", ["Planetary", "*Plum pudding (electrons embedded in positive 'dough')", "Nuclear", "Cloud"], "Positive sphere with embedded electrons."),
    ("Millikan's oil drop experiment determined:", ["The mass of atoms", "*The charge of an electron (1.602 x 10^-19 C)", "The speed of light", "Avogadro's number"], "Precise electron charge measurement."),
    ("Rutherford discovered the nucleus using:", ["Cathode rays", "X-rays", "*Alpha particles aimed at gold foil", "Spectroscopy"], "Most passed through; some bounced back from dense nuclei."),
    ("Bohr's model (1913) improved on Rutherford by:", ["Removing the nucleus", "*Placing electrons in quantized energy levels (specific orbits with fixed energies)", "Adding neutrons", "Removing electrons"], "Quantized orbits explained hydrogen's spectrum."),
    ("Chadwick discovered the _____ in 1932.", ["Electron", "Proton", "*Neutron", "Positron"], "Last major subatomic particle discovered."),
    ("Schrodinger's equation (1926) describes:", ["Proton behavior", "*Electron behavior as a wave function (quantum mechanical model)", "Nuclear reactions", "Chemical bonding"], "Mathematical framework for quantum mechanics."),
    ("The modern atomic model is called the:", ["Bohr model", "Thomson model", "*Quantum mechanical (electron cloud) model", "Rutherford model"], "Current accepted model based on quantum mechanics."),
    ("Which scientist's work led directly to the nuclear model?", ["Thomson", "Dalton", "*Rutherford", "Bohr"], "Gold foil experiment proved the nuclear atom."),
    ("The progression of atomic models shows that science:", ["Never changes", "Was wrong before", "*Is self-correcting and models improve as new evidence is discovered", "Always agrees"], "Models evolve with new evidence."),
    ("Which of Dalton's postulates was later proven wrong?", ["Matter is made of atoms", "Elements have unique atoms", "*Atoms are indivisible (they contain subatomic particles)", "Atoms combine in ratios"], "Subatomic particles were discovered later."),
])

# U4 L4.1: Element Symbols
add_qs("u4_l4.1", [
    ("The symbol for sodium is:", ["So", "Sd", "*Na (from Latin 'natrium')", "S"], "Latin name origin."),
    ("The symbol for potassium is:", ["Po", "Pt", "*K (from Latin 'kalium')", "P"], "Latin-derived symbol."),
    ("The symbol for iron is:", ["Ir", "I", "*Fe (from Latin 'ferrum')", "In"], "Latin name for iron."),
    ("Element symbols always start with:", ["Any letter", "A lowercase letter", "*A capital letter (second letter, if present, is lowercase)", "Two capitals"], "Convention: first letter capitalized."),
    ("The symbol for lead is:", ["Le", "Ld", "*Pb (from Latin 'plumbum')", "Li"], "Origin of 'plumbing'."),
    ("The symbol for silver is:", ["Si", "Sr", "*Ag (from Latin 'argentum')", "Sv"], "Latin-derived."),
    ("Co is the symbol for:", ["Carbon monoxide", "*Cobalt", "Copper", "Chromium"], "Co = cobalt; Cu = copper; CO = carbon monoxide (two elements)."),
    ("How many elements are on the periodic table (as of 2024)?", ["100", "112", "*118", "150"], "Elements 1-118 are confirmed."),
    ("Elements 1-92 (except Tc and Pm) are:", ["All synthetic", "*Naturally occurring", "All gases", "All metals"], "Most elements up to uranium occur in nature."),
    ("Elements 93+ are:", ["All natural", "*Synthetic (made in laboratories or nuclear reactors)", "All stable", "All gases"], "Transuranium elements are man-made."),
    ("The symbol W represents:", ["Oxygen", "Water", "*Tungsten (from German 'Wolfram')", "Fluorine"], "W from Wolfram."),
    ("The symbol Hg represents:", ["Hydrogen gas", "Helium-gallium compound", "*Mercury (from Latin 'hydrargyrum')", "Hafnium-germanium"], "Hydrargyrum = liquid silver."),
    ("Sb is the symbol for:", ["Sulfur-boron", "*Antimony (from Latin 'stibium')", "Selenium-barium", "Scandium-bismuth"], "Latin-derived symbol."),
])

# U4 L4.2: Periodic Table Organization
add_qs("u4_l4.2", [
    ("Periods are _____ on the periodic table.", ["Columns", "*Rows (horizontal)", "Diagonal", "Scattered"], "Periods go left to right."),
    ("Groups (families) are _____ on the periodic table.", ["Rows", "*Columns (vertical)", "Diagonal", "Scattered"], "Groups go top to bottom."),
    ("Elements in the same group have similar:", ["Mass", "Size", "*Chemical properties (same number of valence electrons)", "Nucleus size"], "Same valence electron configuration = similar chemistry."),
    ("Metals are generally located on the _____ side of the periodic table.", ["Right", "*Left and center", "Top only", "Bottom only"], "Most elements are metals, on the left."),
    ("Nonmetals are generally located on the _____ side.", ["Left", "*Upper right", "Center", "Bottom"], "Nonmetals cluster in the upper right."),
    ("Metalloids (semimetals) are found:", ["In the center", "On the far right", "*Along the staircase line (diagonal boundary between metals and nonmetals)", "On the far left"], "Border between metals and nonmetals."),
    ("Group 1 elements are called:", ["Noble gases", "*Alkali metals", "Halogens", "Transition metals"], "Li, Na, K, Rb, Cs, Fr."),
    ("Group 17 elements are called:", ["Alkali metals", "Alkaline earth metals", "*Halogens", "Noble gases"], "F, Cl, Br, I, At."),
    ("Group 18 elements are called:", ["Halogens", "*Noble gases (very stable, rarely react)", "Alkali metals", "Transition metals"], "He, Ne, Ar, Kr, Xe, Rn."),
    ("The transition metals are found in groups:", ["1-2", "17-18", "*3-12", "13-16"], "d-block elements in the middle of the table."),
    ("Lanthanides and actinides are placed _____ the main table.", ["Above", "*Below (in two separate rows to keep the table compact)", "Inside", "On the right"], "f-block elements separated below."),
    ("Mendeleev organized elements by:", ["Alphabetical order", "*Atomic mass and similar properties (predicting gaps for undiscovered elements)", "Random order", "Density"], "Mendeleev's periodic law."),
    ("The modern periodic table is organized by:", ["Atomic mass", "*Atomic number (number of protons)", "Alphabetical order", "Discovery date"], "Moseley established atomic number as the organizing principle."),
])

# U4 L4.3: Valence Electrons
add_qs("u4_l4.3", [
    ("Valence electrons are found in the:", ["Nucleus", "Inner shells", "*Outermost (highest) energy level", "All shells equally"], "Outermost shell electrons."),
    ("Elements in Group 1 (alkali metals) have _____ valence electron(s).", ["0", "*1", "2", "8"], "Group number = valence electrons (for main group)."),
    ("Elements in Group 2 have _____ valence electrons.", ["1", "*2", "6", "8"], "Alkaline earth metals have 2 VE."),
    ("Elements in Group 18 (noble gases) have _____ valence electrons.", ["0", "4", "6", "*8 (except He which has 2)"], "Full outer shell = stable."),
    ("Carbon (Group 14) has _____ valence electrons.", ["2", "*4", "6", "14"], "Group 14: 4 valence electrons."),
    ("Valence electrons determine an element's:", ["Mass", "Density", "*Chemical reactivity and bonding behavior", "Nuclear stability"], "Chemical bonding depends on valence electrons."),
    ("Lewis dot structures show:", ["All electrons", "Only core electrons", "*Only valence electrons as dots around the element symbol", "Only protons"], "Dot notation for valence electrons."),
    ("Nitrogen has 5 valence electrons. Its Lewis dot structure shows:", ["3 dots", "*5 dots (one lone pair and 3 unpaired electrons)", "7 dots", "2 dots"], "N has 5 VE."),
    ("The octet rule states that atoms tend to:", ["Lose all electrons", "*Gain, lose, or share electrons to achieve 8 valence electrons", "Have zero electrons", "Have 2 electrons"], "Noble gas configuration = stable octet."),
    ("Hydrogen follows the _____ rule, not the octet rule.", ["Quartet", "*Duet (needs only 2 electrons to fill its 1s orbital)", "Sextet", "Octet"], "H only needs 2 electrons."),
    ("How does sodium achieve a stable configuration?", ["Gains 7 electrons", "*Loses 1 electron (becoming Na+ with the electron configuration of neon)", "Shares electrons", "Does nothing"], "Easier to lose 1 than gain 7."),
    ("How does chlorine achieve a stable configuration?", ["Loses 7 electrons", "*Gains 1 electron (becoming Cl- with the electron configuration of argon)", "Loses 1 electron", "Does nothing"], "Gains 1 to complete octet."),
    ("Metals tend to _____ electrons; nonmetals tend to _____ electrons.", ["Gain; gain", "Lose; lose", "*Lose; gain", "Share; share"], "Metals lose VE; nonmetals gain VE."),
])

# U4 L4.4: Electron Subshells
add_qs("u4_l4.4", [
    ("The s subshell can hold a maximum of _____ electrons.", ["1", "*2", "6", "10"], "1 orbital x 2 electrons = 2."),
    ("The p subshell can hold a maximum of _____ electrons.", ["2", "4", "*6", "10"], "3 orbitals x 2 electrons = 6."),
    ("The d subshell can hold a maximum of _____ electrons.", ["2", "6", "*10", "14"], "5 orbitals x 2 electrons = 10."),
    ("The f subshell can hold a maximum of _____ electrons.", ["6", "10", "*14", "18"], "7 orbitals x 2 electrons = 14."),
    ("Energy level n=1 contains only the _____ subshell.", ["p", "*s", "d", "f"], "First level: only 1s."),
    ("Energy level n=2 contains the _____ subshells.", ["s only", "*s and p", "s, p, and d", "s, p, d, and f"], "Second level: 2s and 2p."),
    ("Energy level n=3 contains:", ["s and p only", "*s, p, and d (3s, 3p, 3d)", "s, p, d, and f", "s only"], "Third level adds d."),
    ("The maximum number of electrons in energy level n is:", ["n", "n^3", "*2n^2", "8n"], "n=1: 2, n=2: 8, n=3: 18, n=4: 32."),
    ("The 4f subshell begins filling with the:", ["Transition metals", "*Lanthanides (rare earth elements)", "Noble gases", "Alkali metals"], "f-block begins with lanthanides."),
    ("The 3d subshell fills AFTER the:", ["3p", "3s", "*4s (due to energy level ordering: 4s fills before 3d)", "2p"], "Aufbau order: ...3p, 4s, 3d, 4p..."),
    ("Chromium's electron configuration is an exception because:", ["It has no electrons", "*It prefers a half-filled 3d^5 4s^1 configuration over 3d^4 4s^2 (extra stability from half-filled d)", "It follows normal rules", "It has no d electrons"], "Half-filled subshells have extra stability."),
    ("Copper's configuration is [Ar] 3d^10 4s^1 instead of 3d^9 4s^2 because:", ["Copper is unique", "*A fully filled 3d subshell is more stable than a filled 4s with partial 3d", "It follows Aufbau normally", "Copper has no 4s electrons"], "Full d-shell stability."),
    ("The shorthand (noble gas) notation for iron [Ar] 3d^6 4s^2 replaces:", ["Nothing", "*The first 18 electrons with [Ar] for convenience", "All electrons", "Only d electrons"], "Core electrons abbreviated as nearest noble gas."),
])

# U4 L4.5: Electron Configuration
add_qs("u4_l4.5", [
    ("Nitrogen (Z=7) has the electron configuration:", ["1s^2 2s^2 2p^4", "1s^2 2s^2 2p^2", "*1s^2 2s^2 2p^3", "1s^2 2s^2 3p^3"], "7 electrons: 2+2+3."),
    ("Chlorine (Z=17) has the configuration:", ["1s^2 2s^2 2p^6 3s^2 3p^4", "*1s^2 2s^2 2p^6 3s^2 3p^5", "1s^2 2s^2 2p^6 3s^2 3p^6", "1s^2 2s^2 2p^6 3s^2 3d^5"], "17 electrons total."),
    ("The noble gas shorthand for potassium (Z=19) is:", ["[Ne] 3s^2 3p^6 4s^1", "*[Ar] 4s^1", "[Kr] 4s^1", "[Ar] 3d^1"], "Ar has 18 electrons; K adds one more in 4s."),
    ("An orbital diagram uses arrows to show:", ["Protons", "Neutrons", "*Electron spin (+1/2 up arrow, -1/2 down arrow)", "Nuclear energy"], "Arrows represent electron spin direction."),
    ("How many unpaired electrons does nitrogen have?", ["0", "1", "*3 (one in each 2p orbital, per Hund's rule)", "5"], "2p^3: one electron in each of three 2p orbitals."),
    ("A paramagnetic element has:", ["No unpaired electrons", "*One or more unpaired electrons (attracted to magnetic fields)", "Only paired electrons", "No electrons"], "Unpaired electrons = paramagnetic."),
    ("A diamagnetic element has:", ["Unpaired electrons", "*All electrons paired (slightly repelled by magnetic fields)", "No electrons", "Only d electrons"], "All paired = diamagnetic."),
    ("The electron configuration of Ca^2+ (calcium ion) is:", ["[Ar] 4s^2", "1s^2 2s^2 2p^6 3s^2 3p^6 4s^2", "*[Ar] (lost both 4s electrons)", "[Ne] 3s^2"], "Ca loses 2 electrons from 4s to form Ca^2+."),
    ("The electron configuration of Cl^- is:", ["[Ne] 3s^2 3p^5", "*[Ar] (gains one electron to fill 3p fully)", "[Ne] 3s^2 3p^4", "[Kr]"], "Cl gains 1 electron: same as Ar."),
    ("Isoelectronic species have the same:", ["Atomic number", "Mass", "*Electron configuration (same number of electrons)", "Nuclear charge"], "Na+ and Ne are isoelectronic (both have 10 electrons)."),
    ("The Aufbau filling order after 3p is:", ["3d", "4p", "*4s (4s is lower energy than 3d)", "4f"], "4s fills before 3d."),
    ("Ground state vs. excited state: excited means:", ["Lowest energy", "*An electron has absorbed energy and moved to a higher energy level", "No electrons", "Nuclear decay"], "Excited = electrons in higher-than-normal levels."),
    ("When an excited electron falls back to ground state, it:", ["Absorbs energy", "*Emits a photon of light (specific wavelength depending on the energy gap)", "Disappears", "Becomes a proton"], "Energy released as light."),
])

# U4 L4.6: Periodic Trends - Atomic Radius
add_qs("u4_l4.6", [
    ("Atomic radius INCREASES going _____ a group.", ["Up", "*Down (more energy levels added = larger atom)", "It doesn't change", "Left"], "More shells = larger atom."),
    ("Atomic radius DECREASES going _____ across a period.", ["Down", "*Left to right (more protons pull electrons closer without adding new shells)", "Up", "Right to left"], "More nuclear charge, same energy level."),
    ("Which is larger: Na or K?", ["Na", "*K (one more energy level below Na)", "Same size", "Cannot determine"], "K has an additional electron shell."),
    ("Which is larger: Na or Cl?", ["Cl", "*Na (fewer protons pulling on same shell = larger)", "Same size", "Cannot determine"], "Na has less nuclear charge pulling on the 3rd shell."),
    ("The smallest atom on the periodic table is:", ["Hydrogen", "*Helium (highest nuclear charge for its size with only 1s electrons)", "Francium", "Lithium"], "He has 2 protons pulling on only 2 electrons very close."),
    ("The largest atom (by atomic radius) is:", ["Helium", "Hydrogen", "*Francium (most energy levels + least effective nuclear charge for its period)", "Oxygen"], "Bottom-left of the table."),
    ("Cations are _____ than their parent atoms.", ["Larger", "*Smaller (losing electrons reduces electron-electron repulsion; remaining electrons pulled closer)", "Same size", "Sometimes larger"], "Fewer electrons = smaller."),
    ("Anions are _____ than their parent atoms.", ["Smaller", "*Larger (gaining electrons increases electron-electron repulsion; electrons spread out more)", "Same size", "Sometimes smaller"], "More electrons = larger."),
    ("Rank in order of size: Na+, Na, Na-:", ["Na+ > Na > Na-", "All equal", "*Na- > Na > Na+ (more electrons = larger)", "Na > Na- > Na+"], "Most electrons = largest."),
    ("Effective nuclear charge (Z_eff) increases across a period because:", ["Electrons increase", "*Protons increase but shielding stays roughly constant (inner electrons don't fully block added protons)", "Neutrons increase", "Mass increases"], "More protons with similar shielding = higher Z_eff."),
    ("Isoelectronic ions: rank F^-, Na+, Mg^2+ by size:", ["All equal", "Mg^2+ > Na+ > F^-", "*F^- > Na+ > Mg^2+ (same electrons, but more protons = smaller)", "Na+ > F^- > Mg^2+"], "Higher Z pulls same electron count tighter."),
    ("The 'atomic radius' used in most tables is:", ["Nuclear radius", "Ionic radius", "*Half the distance between nuclei of two bonded identical atoms", "Diameter of the electron cloud"], "Covalent or metallic radius."),
    ("Lanthanide contraction refers to:", ["Lanthanides getting bigger", "*The unexpected small size of 3rd-row transition metals due to poor shielding by 4f electrons", "Lanthanides combining", "A phase change"], "4f electrons don't shield well."),
])

# U4 L4.7: Shielding & Effective Nuclear Charge
add_qs("u4_l4.7", [
    ("Core electrons _____ valence electrons from the full nuclear charge.", ["Attract", "*Shield/screen (reducing the effective nuclear charge felt by outer electrons)", "Repel toward the nucleus", "Have no effect on"], "Inner electrons block outer from full Z."),
    ("Z_eff = Z - S, where Z is _____ and S is _____.", ["Electrons, protons", "*Atomic number (total protons), shielding constant (core electrons roughly)", "Neutrons, electrons", "Mass, volume"], "Effective nuclear charge formula."),
    ("As you go across a period, Z_eff _____ because:", ["Decreases; fewer protons", "*Increases; protons increase but shielding from same-shell electrons is minimal", "Stays constant", "Fluctuates randomly"], "Same core shielding, more protons."),
    ("As you go down a group, the outermost electrons feel _____ Z_eff.", ["Higher", "Equal", "*Similar (added protons are offset by added shielding from new inner shell)", "Zero"], "Roughly balanced: more protons but more shielding."),
    ("Which electrons provide the MOST shielding?", ["Valence electrons", "*Core (inner) s and p electrons", "Outer d electrons", "No electrons shield"], "Inner s and p electrons are most effective shields."),
    ("D and f electrons are _____ shielders.", ["Excellent", "*Poor (they don't shield as effectively as s and p electrons due to their orbital shapes)", "Perfect", "Non-existent"], "Diffuse orbitals = poor shielding."),
    ("Slater's rules provide a way to:", ["Count atoms", "Measure mass", "*Estimate the shielding constant (S) for calculating Z_eff more accurately", "Find atomic radius"], "Systematic calculation of shielding."),
    ("Higher Z_eff means valence electrons are held:", ["Loosely", "*More tightly (harder to remove = higher ionization energy)", "Not at all", "Equally"], "Stronger pull on outer electrons."),
    ("Why is the 4s orbital filled before 3d?", ["4s is smaller", "*4s has lower energy (penetrates closer to nucleus despite being in a higher shell, less shielded)", "4 comes before 3", "3d doesn't exist"], "Penetration and shielding effects on energy levels."),
    ("Penetration refers to:", ["Electrons entering the nucleus", "*An orbital's probability of being found close to the nucleus (s > p > d > f in penetration)", "Nuclear reactions", "Chemical bonding"], "s electrons penetrate closest to the nucleus."),
    ("For the same shell (n), the energy order of subshells is:", ["All equal", "f < d < p < s", "*s < p < d < f (s has the lowest energy due to greatest penetration)", "p < s < d < f"], "More penetration = lower energy."),
    ("Ionization energy trends closely mirror _____ trends.", ["Atomic radius", "*Effective nuclear charge (higher Z_eff = higher IE)", "Mass", "Neutron count"], "Z_eff is the main driver of IE."),
    ("Electronegativity also correlates with Z_eff because:", ["They're unrelated", "*Higher Z_eff means the atom attracts bonding electrons more strongly", "They're inversely related", "Only for metals"], "Strong Z_eff pull = high electronegativity."),
])

# U4 L4.8: VSEPR Theory
add_qs("u4_l4.8", [
    ("VSEPR predicts molecular shape based on:", ["Atomic mass", "*Repulsion between electron pairs around the central atom", "Bond length", "Nuclear charge"], "Electron pairs repel to maximize distance."),
    ("A molecule with 2 bonding regions and 0 lone pairs has _____ geometry.", ["Bent", "Trigonal planar", "*Linear (180 degree bond angle)", "Tetrahedral"], "2 regions: linear."),
    ("A molecule with 3 bonding regions and 0 lone pairs has _____ geometry.", ["Linear", "*Trigonal planar (120 degree bond angles)", "Tetrahedral", "Bent"], "3 regions, no lone pairs: trigonal planar."),
    ("A molecule with 4 bonding regions and 0 lone pairs has _____ geometry.", ["Trigonal planar", "Linear", "*Tetrahedral (109.5 degree bond angles)", "Trigonal pyramidal"], "4 bonding pairs: tetrahedral."),
    ("Water (H2O) has 2 bonding and 2 lone pairs, making it:", ["Linear", "Tetrahedral", "*Bent (approximately 104.5 degrees)", "Trigonal planar"], "Lone pairs compress the bond angle."),
    ("Ammonia (NH3) has 3 bonding and 1 lone pair, making it:", ["Tetrahedral", "Trigonal planar", "*Trigonal pyramidal (approximately 107 degrees)", "Linear"], "One lone pair pushes the three bonds down."),
    ("Lone pairs occupy _____ space than bonding pairs.", ["Less", "Equal", "*More (exerting greater repulsive force)", "No"], "Lone pairs are more diffuse."),
    ("A molecule with 5 bonding regions has _____ geometry.", ["Tetrahedral", "*Trigonal bipyramidal (90 and 120 degree angles)", "Octahedral", "Linear"], "5 regions: trigonal bipyramidal."),
    ("A molecule with 6 bonding regions has _____ geometry.", ["Trigonal bipyramidal", "*Octahedral (90 degree angles)", "Hexagonal", "Linear"], "6 regions: octahedral."),
    ("SF6 has _____ geometry.", ["Tetrahedral", "Trigonal bipyramidal", "*Octahedral", "Square planar"], "6 bonding pairs around sulfur."),
    ("CO2 is _____ because its 2 double bonds point in opposite directions.", ["Bent", "Trigonal planar", "*Linear (180 degrees)", "Tetrahedral"], "Two electron regions = linear."),
    ("XeF2 (3 lone pairs, 2 bonding pairs) has _____ molecular geometry.", ["Trigonal bipyramidal", "*Linear (lone pairs in equatorial positions of trigonal bipyramid)", "Bent", "T-shaped"], "5 total electron regions but only 2 bonded atoms."),
    ("Molecular geometry vs. electron geometry: molecular geometry considers:", ["All electron pairs", "*Only the positions of ATOMS (ignoring lone pairs in naming the shape)", "Only lone pairs", "Only double bonds"], "Shape described by atom positions."),
])

# U4 L4.9: Orbital Shapes
add_qs("u4_l4.9", [
    ("The s orbital has a _____ shape.", ["Dumbbell", "Clover", "*Spherical", "Ring"], "s orbitals are spherically symmetric."),
    ("The p orbital has a _____ shape.", ["Spherical", "*Dumbbell (two lobes)", "Clover", "Ring"], "Two lobes on opposite sides of the nucleus."),
    ("How many p orbitals are there in each energy level (n >= 2)?", ["1", "2", "*3 (px, py, pz — oriented along x, y, z axes)", "6"], "Three mutually perpendicular p orbitals."),
    ("The d subshell contains _____ orbitals.", ["3", "*5", "7", "1"], "5 d orbitals with different orientations."),
    ("Most d orbitals have a _____ shape.", ["Spherical", "Dumbbell", "*Clover-leaf (four lobes)", "Ring and dumbbell"], "Four-lobed clover shape (except dz^2)."),
    ("The dz^2 orbital is unique because it has:", ["Four lobes", "*A donut (torus) around the center with two lobes along the z-axis", "A spherical shape", "Six lobes"], "Distinctive shape among d orbitals."),
    ("f orbitals contain _____ orbitals per subshell.", ["3", "5", "*7", "9"], "7 f orbitals with complex shapes."),
    ("As n increases, s orbitals:", ["Get smaller", "*Get larger (but remain spherical) with additional nodes", "Change shape", "Disappear"], "Higher n = larger orbital with more nodes."),
    ("A node is a region where:", ["Electron density is highest", "*The probability of finding an electron is zero", "Protons exist", "Bonds form"], "Nodes = zero electron probability."),
    ("The 2s orbital has _____ radial node(s), while 1s has _____.", ["0, 0", "*1, 0", "2, 1", "0, 1"], "Radial nodes = n - l - 1: for 2s: 2-0-1=1; for 1s: 1-0-1=0."),
    ("Orbital overlap in bonding occurs when:", ["Orbitals repel", "*Electron clouds from two atoms occupy the same region of space (forming a bond)", "Nuclei touch", "Orbitals disappear"], "Shared electron space forms bonds."),
    ("Sigma bonds form from:", ["Side-by-side orbital overlap", "*Head-on (end-to-end) orbital overlap along the internuclear axis", "No overlap", "Only s orbitals"], "Direct overlap along the bond axis."),
    ("Pi bonds form from:", ["Head-on overlap", "*Side-by-side (lateral) overlap of parallel p orbitals", "s orbital overlap", "d orbital overlap only"], "Parallel p orbital overlap above and below the bond axis."),
])

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

short = [(k, len(v.get("quiz_questions",[]))) for k,v in data.items() if len(v.get("quiz_questions",[]))<20]
if short:
    for k,n in short: print(f"STILL SHORT: {k} has {n}")
ct = sum(1 for v in data.values() if len(v.get('quiz_questions',[])) >= 20)
print(f"✅ Chemistry U1-U4: {ct} lessons at 20+ questions (out of {len(data)} total)")
