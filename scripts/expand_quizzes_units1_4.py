#!/usr/bin/env python3
"""Expand quiz files for Units 1-4 from 2 questions to 7 questions each."""

import os
import re
import random

BASE = os.path.join(os.path.dirname(__file__), '..', 'ArisEdu Project Folder', 'ChemistryLessons')

# Each lesson: list of (question, correct_answer, [wrong1, wrong2, wrong3])
LESSONS = {
    # ===== UNIT 1: Properties of Matter =====
    "Unit1": {
        "1.1": {
            "topic": "States of Matter",
            "questions": [
                ("Which state of matter has a definite shape and definite volume?", "Solid", ["Liquid", "Gas", "Plasma"]),
                ("In which state do particles move most freely?", "Gas", ["Solid", "Liquid", "Plasma"]),
                ("Which state of matter takes the shape of its container but has a definite volume?", "Liquid", ["Solid", "Gas", "Plasma"]),
                ("What happens to molecular motion when temperature increases?", "It increases", ["It decreases", "It stays the same", "It stops completely"]),
                ("Which state of matter has the highest kinetic energy?", "Gas", ["Solid", "Liquid", "They are all equal"]),
                ("Plasma is created when a gas is given enough energy to:", "Ionize its atoms", ["Freeze its molecules", "Condense into a liquid", "Become a solid"]),
                ("Which property distinguishes a solid from a liquid?", "Definite shape", ["Mass", "Weight", "Temperature"]),
            ]
        },
        "1.2": {
            "topic": "Phase Changes",
            "questions": [
                ("What is the phase change from solid to liquid called?", "Melting", ["Freezing", "Evaporation", "Condensation"]),
                ("What is the phase change from gas to liquid called?", "Condensation", ["Evaporation", "Sublimation", "Deposition"]),
                ("What is sublimation?", "Solid directly changing to gas", ["Gas changing to liquid", "Liquid changing to solid", "Gas changing to solid"]),
                ("What is deposition?", "Gas directly changing to solid", ["Solid changing to gas", "Liquid changing to gas", "Solid changing to liquid"]),
                ("During a phase change, temperature:", "Remains constant", ["Increases rapidly", "Decreases rapidly", "Fluctuates randomly"]),
                ("Which phase change requires the absorption of energy?", "Evaporation", ["Freezing", "Condensation", "Deposition"]),
                ("What is the phase change from liquid to gas called?", "Vaporization", ["Melting", "Freezing", "Sublimation"]),
            ]
        },
        "1.3": {
            "topic": "Intensive & Extensive Properties",
            "questions": [
                ("Which is an intensive property?", "Density", ["Mass", "Volume", "Length"]),
                ("Which is an extensive property?", "Mass", ["Density", "Color", "Boiling point"]),
                ("Intensive properties do NOT depend on:", "The amount of matter", ["Temperature", "Pressure", "Chemical composition"]),
                ("Which of the following is an intensive property?", "Boiling point", ["Weight", "Volume", "Number of moles"]),
                ("If you cut a diamond in half, which property changes?", "Mass", ["Hardness", "Density", "Luster"]),
                ("Temperature is classified as:", "An intensive property", ["An extensive property", "Both intensive and extensive", "Neither intensive nor extensive"]),
                ("Which pair are both extensive properties?", "Mass and volume", ["Density and color", "Temperature and pressure", "Melting point and hardness"]),
            ]
        },
        "1.4": {
            "topic": "Mass, Volume, & Density",
            "questions": [
                ("What is the formula for density?", "Density = mass / volume", ["Density = volume / mass", "Density = mass × volume", "Density = mass + volume"]),
                ("If an object has a mass of 50 g and a volume of 25 mL, what is its density?", "2 g/mL", ["0.5 g/mL", "25 g/mL", "75 g/mL"]),
                ("An object with a density less than 1 g/mL will:", "Float in water", ["Sink in water", "Dissolve in water", "Remain suspended"]),
                ("What is the density of water at standard conditions?", "1 g/mL", ["10 g/mL", "0.1 g/mL", "100 g/mL"]),
                ("Which instrument measures volume of an irregular solid?", "Graduated cylinder (water displacement)", ["Ruler", "Balance", "Thermometer"]),
                ("If density is constant, what happens when mass doubles?", "Volume doubles", ["Volume halves", "Volume stays the same", "Volume triples"]),
                ("Which has the highest density?", "Lead", ["Wood", "Cork", "Air"]),
            ]
        },
        "1.5": {
            "topic": "Heterogeneous & Homogeneous Mixtures",
            "questions": [
                ("A homogeneous mixture is also called a:", "Solution", ["Suspension", "Colloid", "Compound"]),
                ("Which is an example of a heterogeneous mixture?", "Salad", ["Salt water", "Air", "Brass"]),
                ("In a solution, the substance being dissolved is called the:", "Solute", ["Solvent", "Mixture", "Element"]),
                ("Which of the following is a homogeneous mixture?", "Vinegar", ["Trail mix", "Sand and water", "Oil and water"]),
                ("What distinguishes a heterogeneous mixture?", "Visibly different parts", ["Uniform composition", "Fixed ratio of elements", "Only one phase present"]),
                ("Blood is classified as what type of mixture?", "Heterogeneous", ["Homogeneous", "Pure substance", "Element"]),
                ("Which technique can separate a homogeneous mixture?", "Distillation", ["Picking by hand", "Filtration alone", "Using a magnet"]),
            ]
        },
        "1.6": {
            "topic": "Physical & Chemical Properties",
            "questions": [
                ("Which is a physical property?", "Boiling point", ["Flammability", "Reactivity with acid", "Combustibility"]),
                ("Which is a chemical property?", "Flammability", ["Color", "Density", "Melting point"]),
                ("A physical property can be observed without:", "Changing the substance's identity", ["Measuring it", "Touching it", "Seeing it"]),
                ("Reactivity with oxygen is a:", "Chemical property", ["Physical property", "Intensive measurement", "Extensive measurement"]),
                ("Which is a physical property of iron?", "Silvery-gray color", ["Rusts in moist air", "Reacts with acid", "Burns in pure oxygen"]),
                ("Malleability (being hammered into sheets) is a:", "Physical property", ["Chemical property", "Nuclear property", "Biological property"]),
                ("Which observation indicates a chemical property?", "Iron rusting over time", ["Ice melting", "Sugar dissolving", "Glass breaking"]),
            ]
        },
        "1.7": {
            "topic": "Physical & Chemical Changes",
            "questions": [
                ("Which is an example of a chemical change?", "Burning wood", ["Cutting paper", "Melting ice", "Breaking glass"]),
                ("Which is a sign that a chemical change has occurred?", "Production of gas bubbles", ["Change in shape", "Change in size", "Change in state"]),
                ("Dissolving sugar in water is a:", "Physical change", ["Chemical change", "Nuclear change", "No change at all"]),
                ("Which is an example of a physical change?", "Freezing water", ["Rusting iron", "Cooking an egg", "Burning gasoline"]),
                ("A new substance is formed during a:", "Chemical change", ["Physical change", "Phase change", "No change"]),
                ("Which clue suggests a chemical change?", "Color change with new substance", ["Melting", "Evaporation", "Tearing"]),
                ("Baking a cake is an example of a:", "Chemical change", ["Physical change", "Phase change", "Dissolving"]),
            ]
        },
        "1.8": {
            "topic": "Energy & Matter",
            "questions": [
                ("The law of conservation of energy states that energy:", "Cannot be created or destroyed", ["Can be created from nothing", "Always decreases", "Only exists as heat"]),
                ("Kinetic energy is the energy of:", "Motion", ["Position", "Chemical bonds", "Nuclear reactions"]),
                ("Potential energy is stored energy due to:", "Position or composition", ["Speed", "Acceleration", "Friction"]),
                ("Which type of energy increases when an object is heated?", "Kinetic energy of particles", ["Nuclear energy", "Gravitational potential energy", "Electrical resistance"]),
                ("An endothermic process:", "Absorbs energy from surroundings", ["Releases energy to surroundings", "Creates energy", "Destroys energy"]),
                ("An exothermic process:", "Releases energy to surroundings", ["Absorbs energy from surroundings", "Destroys energy", "Creates energy"]),
                ("What happens to molecular kinetic energy when a substance is cooled?", "It decreases", ["It increases", "It stays the same", "It disappears"]),
            ]
        },
    },
    # ===== UNIT 2: Measurement =====
    "Unit2": {
        "2.1": {
            "topic": "Scientific Notation",
            "questions": [
                ("What is 4,500,000 in scientific notation?", "4.5 × 10⁶", ["45 × 10⁵", "0.45 × 10⁷", "4.5 × 10⁵"]),
                ("What is 0.00032 in scientific notation?", "3.2 × 10⁻⁴", ["3.2 × 10⁴", "32 × 10⁻⁵", "0.32 × 10⁻³"]),
                ("In scientific notation, the coefficient must be:", "Between 1 and 10", ["Greater than 10", "Less than 1", "A whole number"]),
                ("What is 6.02 × 10²³ in standard form?", "602,000,000,000,000,000,000,000", ["60,200,000", "6,020,000", "0.000602"]),
                ("When multiplying numbers in scientific notation, you:", "Add the exponents", ["Subtract the exponents", "Multiply the exponents", "Divide the exponents"]),
                ("What is (3 × 10⁴) × (2 × 10³)?", "6 × 10⁷", ["6 × 10¹²", "5 × 10⁷", "6 × 10¹"]),
                ("A negative exponent in scientific notation means the number is:", "Less than 1", ["Negative", "Greater than 10", "Imaginary"]),
            ]
        },
        "2.2": {
            "topic": "Significant Figures",
            "questions": [
                ("How many significant figures does 0.00450 have?", "3", ["5", "2", "6"]),
                ("How many significant figures does 1000 have?", "1", ["4", "3", "2"]),
                ("Leading zeros are:", "Never significant", ["Always significant", "Sometimes significant", "Significant only in decimals"]),
                ("Trailing zeros after a decimal point are:", "Always significant", ["Never significant", "Only sometimes significant", "Ignored in counting"]),
                ("How many significant figures does 2.050 have?", "4", ["3", "2", "5"]),
                ("When multiplying, the answer should have:", "The fewest sig figs of any factor", ["The most sig figs of any factor", "Unlimited sig figs", "Exactly 3 sig figs"]),
                ("Captive zeros (between non-zero digits) are:", "Always significant", ["Never significant", "Significant only after decimal", "Ignored"]),
            ]
        },
        "2.3": {
            "topic": "Accuracy vs. Precision",
            "questions": [
                ("Accuracy refers to how close a measurement is to the:", "True or accepted value", ["Mean of measurements", "Median value", "Other measurements"]),
                ("Precision refers to how close measurements are to:", "Each other", ["The true value", "Zero", "The expected value"]),
                ("A set of measurements can be precise but not accurate if they are:", "Close together but far from the true value", ["Spread out and far from true value", "Close to the true value but spread out", "Random"]),
                ("Percent error measures:", "Accuracy", ["Precision", "Reliability", "Reproducibility"]),
                ("The formula for percent error is:", "|experimental − accepted| / accepted × 100", ["accepted / experimental × 100", "experimental × accepted × 100", "experimental + accepted / 100"]),
                ("Random errors affect:", "Precision", ["Accuracy only", "Neither accuracy nor precision", "Only the first measurement"]),
                ("Systematic errors affect:", "Accuracy", ["Precision only", "Neither accuracy nor precision", "Only the last measurement"]),
            ]
        },
        "2.4": {
            "topic": "Metric System",
            "questions": [
                ("The SI base unit of mass is the:", "Kilogram", ["Gram", "Pound", "Ounce"]),
                ("The prefix 'kilo-' means:", "1,000", ["100", "0.001", "1,000,000"]),
                ("The prefix 'milli-' means:", "0.001 (one thousandth)", ["0.01 (one hundredth)", "1,000", "0.000001"]),
                ("Which unit would you use to measure the volume of a liquid?", "Liter", ["Gram", "Meter", "Kelvin"]),
                ("The SI base unit of length is the:", "Meter", ["Centimeter", "Kilometer", "Foot"]),
                ("1 centimeter equals:", "0.01 meters", ["0.001 meters", "0.1 meters", "10 meters"]),
                ("The prefix 'micro-' (μ) represents:", "10⁻⁶", ["10⁻³", "10⁻⁹", "10⁻²"]),
            ]
        },
        "2.5": {
            "topic": "Unit Conversions",
            "questions": [
                ("How many milliliters are in 2.5 liters?", "2,500 mL", ["250 mL", "25 mL", "25,000 mL"]),
                ("Dimensional analysis uses:", "Conversion factors", ["Estimation", "Guessing", "Rounding"]),
                ("A conversion factor is a ratio that equals:", "1", ["0", ["10"], "100"]),
                ("How many grams are in 3.5 kilograms?", "3,500 g", ["350 g", "35 g", "0.0035 g"]),
                ("When converting from a smaller unit to a larger unit, the numerical value:", "Decreases", ["Increases", "Stays the same", "Becomes negative"]),
                ("How many centimeters are in 1 meter?", "100 cm", ["10 cm", "1,000 cm", "0.01 cm"]),
                ("To convert °C to Kelvin, you:", "Add 273", ["Subtract 273", "Multiply by 1.8", "Divide by 273"]),
            ]
        },
    },
    # ===== UNIT 3: Atomic Structure =====
    "Unit3": {
        "3.1": {
            "topic": "Electrons, Protons, and Neutrons",
            "questions": [
                ("What subatomic particle determines the identity of an element?", "Proton", ["Electron", "Neutron", "Photon"]),
                ("What is the charge of a neutron?", "No charge (neutral)", ["Positive", "Negative", "Variable"]),
                ("Where are electrons located in an atom?", "In orbitals around the nucleus", ["Inside the nucleus", "Between atoms", "Free in space"]),
                ("What is the charge of an electron?", "Negative (-1)", ["Positive (+1)", "Neutral (0)", "Variable"]),
                ("Protons and neutrons are found in the:", "Nucleus", ["Electron cloud", "Outer shell", "Between atoms"]),
                ("The mass of an electron compared to a proton is:", "Much smaller (about 1/1836)", ["Equal", "Much larger", "Slightly larger"]),
                ("The atomic number equals the number of:", "Protons", ["Neutrons", "Electrons only", "Protons + neutrons"]),
            ]
        },
        "3.2": {
            "topic": "Atomic Structure",
            "questions": [
                ("The mass number of an atom equals:", "Protons + neutrons", ["Protons only", "Neutrons only", "Protons + electrons"]),
                ("An atom is electrically neutral because it has:", "Equal numbers of protons and electrons", ["No charged particles", "Only neutrons", "More neutrons than protons"]),
                ("The nucleus of an atom contains:", "Protons and neutrons", ["Electrons and protons", "Only protons", "Only electrons"]),
                ("Most of an atom's mass is concentrated in the:", "Nucleus", ["Electron cloud", "Outer shell", "Empty space"]),
                ("What determines the chemical properties of an atom?", "Number of electrons", ["Number of neutrons", "Total mass", "Size of nucleus"]),
                ("An atom of carbon-14 has how many neutrons?", "8", ["6", "14", "12"]),
                ("Most of an atom's volume is:", "Empty space (electron cloud)", ["Nucleus", "Protons", "Neutrons"]),
            ]
        },
        "3.3": {
            "topic": "Quantum Mechanical Model & Orbitals",
            "questions": [
                ("The quantum mechanical model describes electrons as:", "Probability clouds", ["Tiny solid spheres", "Fixed circular orbits", "Waves in the nucleus"]),
                ("An orbital is a region where:", "An electron is most likely found", ["Protons are located", "Neutrons orbit", "Energy is zero"]),
                ("How many electrons can one orbital hold?", "2", ["8", "4", "1"]),
                ("The s orbital has what shape?", "Spherical", ["Dumbbell", "Cloverleaf", "Ring"]),
                ("The p orbital has what shape?", "Dumbbell", ["Spherical", "Cubic", "Triangular"]),
                ("The principal quantum number (n) represents:", "Energy level", ["Orbital shape", "Spin direction", "Number of protons"]),
                ("How many orbitals are in a p sublevel?", "3", ["1", "5", "7"]),
            ]
        },
        "3.4": {
            "topic": "Electromagnetic Spectrum & Atomic Emission Spectra",
            "questions": [
                ("As wavelength increases, frequency:", "Decreases", ["Increases", "Stays the same", "Doubles"]),
                ("Which type of electromagnetic radiation has the highest energy?", "Gamma rays", ["Radio waves", "Microwaves", "Infrared"]),
                ("The speed of all electromagnetic radiation in a vacuum is:", "3 × 10⁸ m/s", ["3 × 10⁶ m/s", "3 × 10¹⁰ m/s", "1.5 × 10⁸ m/s"]),
                ("An emission spectrum is produced when electrons:", "Fall from higher to lower energy levels", ["Are removed from the atom", "Absorb neutrons", "Stop moving"]),
                ("Each element produces a unique emission spectrum called a:", "Line spectrum", ["Continuous spectrum", "Absorption band", "White light pattern"]),
                ("The relationship between energy and frequency is:", "Directly proportional (E = hf)", ["Inversely proportional", "No relationship", "Logarithmic"]),
                ("Planck's constant (h) has a value of approximately:", "6.626 × 10⁻³⁴ J·s", ["6.02 × 10²³", "3 × 10⁸ m/s", "9.8 m/s²"]),
            ]
        },
        "3.5": {
            "topic": "Radioactivity & Stability",
            "questions": [
                ("Radioactive decay occurs when an unstable nucleus:", "Emits radiation to become more stable", ["Gains electrons", "Absorbs neutrons", "Splits into equal halves always"]),
                ("A stable nucleus typically has a balanced ratio of:", "Protons to neutrons", ["Electrons to protons", "Mass to volume", "Energy to mass"]),
                ("Which element has no stable isotopes?", "Technetium", ["Carbon", "Oxygen", "Iron"]),
                ("The strong nuclear force holds together:", "Protons and neutrons in the nucleus", ["Electrons in orbitals", "Molecules in a solid", "Atoms in a gas"]),
                ("Atoms with too many neutrons tend to undergo:", "Beta decay", ["Alpha decay only", "Fusion", "No change"]),
                ("The band of stability refers to:", "Stable proton-to-neutron ratios", ["Electron configurations", "Chemical bond strengths", "Melting point ranges"]),
                ("Heavier elements (Z > 83) are generally:", "Radioactive", ["Stable", "Nonexistent", "Gaseous"]),
            ]
        },
        "3.6": {
            "topic": "Isotopes & Radioisotopes",
            "questions": [
                ("Isotopes of an element have different numbers of:", "Neutrons", ["Protons", "Electrons", "Valence electrons"]),
                ("Carbon-12 and Carbon-14 differ in their number of:", "Neutrons", ["Protons", "Electrons", "Energy levels"]),
                ("Radioisotopes are isotopes that are:", "Unstable and emit radiation", ["Always stable", "Artificially made only", "Non-existent in nature"]),
                ("The average atomic mass on the periodic table accounts for:", "Relative abundance of all isotopes", ["Only the most common isotope", "Only the lightest isotope", "Protons only"]),
                ("Carbon-14 dating is used to determine the age of:", "Organic materials", ["Rocks only", "Metals", "Water"]),
                ("Which isotope of hydrogen has one neutron?", "Deuterium", ["Protium", "Tritium", "Helium-3"]),
                ("Isotopes of the same element have the same:", "Chemical properties", ["Mass number", "Number of neutrons", "Atomic mass"]),
            ]
        },
        "3.7": {
            "topic": "Element Synthesis",
            "questions": [
                ("Elements heavier than iron are primarily formed by:", "Supernova explosions", ["Solar wind", "Chemical reactions on Earth", "Radioactive decay only"]),
                ("Nuclear fusion in stars primarily converts hydrogen into:", "Helium", ["Oxygen", "Carbon", "Iron"]),
                ("Synthetic elements are those that:", "Are created in laboratories", ["Occur naturally", "Have no protons", "Are always stable"]),
                ("The heaviest naturally occurring element is:", "Uranium", ["Plutonium", "Oganesson", "Fermium"]),
                ("Transuranium elements are elements with atomic number greater than:", "92", ["82", "100", "118"]),
                ("Particle accelerators are used to:", "Smash atoms together to create new elements", ["Slow down electrons", "Measure temperature", "Store radioactive waste"]),
                ("Stellar nucleosynthesis is the process of:", "Creating elements inside stars", ["Destroying elements in space", "Splitting atoms on Earth", "Cooling stars"]),
            ]
        },
        "3.8": {
            "topic": "Atomic Theory",
            "questions": [
                ("Who proposed the first atomic theory with experimental evidence?", "John Dalton", ["Aristotle", "Albert Einstein", "Marie Curie"]),
                ("J.J. Thomson discovered the:", "Electron", ["Proton", "Neutron", "Nucleus"]),
                ("Rutherford's gold foil experiment revealed the:", "Dense, positively charged nucleus", ["Electron cloud", "Neutron", "Electron shells"]),
                ("Bohr's model described electrons in:", "Fixed circular orbits with specific energy levels", ["Random locations", "The nucleus", "A continuous cloud"]),
                ("The plum pudding model was proposed by:", "J.J. Thomson", ["Ernest Rutherford", "Niels Bohr", "John Dalton"]),
                ("Dalton's atomic theory stated that atoms:", "Cannot be created or destroyed in chemical reactions", ["Can be split by chemistry", "Are made of smaller particles", "Have a nucleus"]),
                ("The modern quantum mechanical model was developed by:", "Schrödinger and Heisenberg", ["Dalton and Thomson", "Bohr and Rutherford", "Newton and Galileo"]),
            ]
        },
    },
    # ===== UNIT 4: Periodic Table & Electron Configuration =====
    "Unit4": {
        "4.1": {
            "topic": "Chemical Symbols",
            "questions": [
                ("What is the chemical symbol for gold?", "Au", ["Go", "Gd", "Ag"]),
                ("What is the chemical symbol for sodium?", "Na", ["So", "Sd", "S"]),
                ("The chemical symbol Fe represents:", "Iron", ["Fluorine", "Fermium", "Francium"]),
                ("Chemical symbols are derived from:", "Latin or English names of elements", ["Greek philosophy", "Random letters", "Atomic numbers"]),
                ("What is the chemical symbol for potassium?", "K", ["Po", "Pt", "P"]),
                ("How many letters can a chemical symbol have?", "One or two", ["Only one", "Exactly two", "Up to three"]),
                ("The second letter of a chemical symbol is always:", "Lowercase", ["Uppercase", "A number", "A Greek letter"]),
            ]
        },
        "4.2": {
            "topic": "Periodic Table Arrangement",
            "questions": [
                ("Elements in the periodic table are arranged by increasing:", "Atomic number", ["Atomic mass", "Number of neutrons", "Density"]),
                ("A horizontal row on the periodic table is called a:", "Period", ["Group", "Family", "Block"]),
                ("A vertical column on the periodic table is called a:", "Group (or family)", ["Period", "Row", "Series"]),
                ("Elements in the same group have similar:", "Chemical properties", ["Atomic masses", "Number of neutrons", "Colors"]),
                ("The periodic table was first organized by:", "Dmitri Mendeleev", ["John Dalton", "Niels Bohr", "Albert Einstein"]),
                ("How many periods are in the modern periodic table?", "7", ["6", "8", "18"]),
                ("The staircase line on the periodic table separates:", "Metals from nonmetals", ["Gases from solids", "Large from small atoms", "Natural from synthetic elements"]),
            ]
        },
        "4.3": {
            "topic": "Valence Electrons & Reactivity",
            "questions": [
                ("Valence electrons are found in the:", "Outermost energy level", ["Nucleus", "Innermost shell", "Between atoms"]),
                ("Group 1 elements (alkali metals) have how many valence electrons?", "1", ["2", "7", "8"]),
                ("Noble gases are unreactive because they have:", "A full valence shell", ["No electrons", "Only 1 electron", "No neutrons"]),
                ("As you move down a group, metallic reactivity:", "Increases", ["Decreases", "Stays the same", "Becomes zero"]),
                ("Halogens (Group 17) need how many more electrons to fill their valence shell?", "1", ["2", "3", "7"]),
                ("Which group of elements is most reactive?", "Alkali metals (Group 1)", ["Noble gases (Group 18)", "Alkaline earth metals (Group 2)", "Transition metals"]),
                ("Elements with 8 valence electrons follow the:", "Octet rule", ["Duet rule", "Pauli rule", "Hund's rule"]),
            ]
        },
        "4.4": {
            "topic": "Electron Suborbitals",
            "questions": [
                ("The four types of suborbitals are:", "s, p, d, f", ["a, b, c, d", "w, x, y, z", "1, 2, 3, 4"]),
                ("How many electrons can the s suborbital hold?", "2", ["6", "10", "14"]),
                ("How many electrons can the p suborbital hold?", "6", ["2", "10", "14"]),
                ("How many electrons can the d suborbital hold?", "10", ["2", "6", "14"]),
                ("How many electrons can the f suborbital hold?", "14", ["2", "6", "10"]),
                ("The d suborbital first appears at energy level:", "3", ["1", "2", "4"]),
                ("The f suborbital first appears at energy level:", "4", ["2", "3", "5"]),
            ]
        },
        "4.5": {
            "topic": "Electron Configuration",
            "questions": [
                ("The electron configuration of oxygen (Z=8) is:", "1s² 2s² 2p⁴", ["1s² 2s² 2p⁶", "1s² 2s² 2p²", "1s² 2p⁶"]),
                ("The Aufbau principle states that electrons fill:", "Lowest energy orbitals first", ["Highest energy orbitals first", "Randomly", "All at the same time"]),
                ("Hund's rule states that electrons in the same sublevel:", "Occupy orbitals singly before pairing", ["Always pair up first", "Have the same spin", "Skip orbitals"]),
                ("The Pauli exclusion principle states:", "No two electrons in the same orbital can have the same spin", ["Electrons always spin up", "Orbitals hold 3 electrons", "Electrons have no spin"]),
                ("What is the electron configuration of sodium (Z=11)?", "1s² 2s² 2p⁶ 3s¹", ["1s² 2s² 2p⁶ 3p¹", "1s² 2s² 3s²", "1s² 2s² 2p⁶ 2d¹"]),
                ("Noble gas shorthand for chlorine (Z=17) is:", "[Ne] 3s² 3p⁵", ["[Ar] 3s² 3p⁵", "[He] 3s² 3p⁵", "[Ne] 3s² 3d⁵"]),
                ("Which element has the configuration 1s² 2s² 2p⁶ 3s² 3p⁶?", "Argon", ["Neon", "Chlorine", "Potassium"]),
            ]
        },
        "4.6": {
            "topic": "Periodic Trends",
            "questions": [
                ("Atomic radius generally decreases across a period because:", "Increasing nuclear charge pulls electrons closer", ["Atoms lose electrons", "Neutrons are added", "Electrons are farther away"]),
                ("Ionization energy generally increases across a period because:", "Electrons are held more tightly", ["Atoms get bigger", "Electrons are farther from nucleus", "Neutrons increase"]),
                ("Electronegativity increases:", "Going up and to the right", ["Going down and to the left", "Only down a group", "Only across a period"]),
                ("Which element has the largest atomic radius?", "Francium (Fr)", ["Fluorine (F)", "Helium (He)", "Neon (Ne)"]),
                ("Which element has the highest electronegativity?", "Fluorine (F)", ["Cesium (Cs)", "Francium (Fr)", "Helium (He)"]),
                ("Going down a group, atomic radius:", "Increases", ["Decreases", "Stays the same", "Varies randomly"]),
                ("Going down a group, ionization energy:", "Decreases", ["Increases", "Stays the same", "Doubles"]),
            ]
        },
        "4.7": {
            "topic": "Shielding Effect",
            "questions": [
                ("The shielding effect occurs when inner electrons:", "Block the nuclear pull on outer electrons", ["Attract other atoms", "Merge with the nucleus", "Gain energy"]),
                ("As shielding increases, valence electrons are:", "Easier to remove", ["Harder to remove", "Unaffected", "Destroyed"]),
                ("Shielding effect increases as you go:", "Down a group", ["Across a period", "Up a group", "Diagonally"]),
                ("Effective nuclear charge (Z_eff) is the net charge felt by:", "Valence electrons", ["Inner electrons", "Protons", "Neutrons"]),
                ("More electron shells lead to:", "Greater shielding effect", ["Less shielding effect", "No shielding", "More nuclear charge"]),
                ("Which element has more shielding: Li or Cs?", "Cs (more electron shells)", ["Li (fewer electron shells)", "They are equal", "Neither has shielding"]),
                ("Effective nuclear charge increases across a period because:", "Protons increase but shielding stays roughly the same", ["Electrons decrease", "Neutrons increase", "Shielding increases faster"]),
            ]
        },
        "4.8": {
            "topic": "VSEPR Molecule Shapes",
            "questions": [
                ("VSEPR stands for:", "Valence Shell Electron Pair Repulsion", ["Very Simple Electron Pair Repulsion", "Variable Shape Electron Proton Ratio", "Valence Suborbital Electron Pair Rotation"]),
                ("A molecule with 4 bonding pairs and 0 lone pairs has what shape?", "Tetrahedral", ["Linear", "Trigonal planar", "Bent"]),
                ("A molecule with 2 bonding pairs and 0 lone pairs has what shape?", "Linear", ["Bent", "Trigonal planar", "Tetrahedral"]),
                ("A molecule with 3 bonding pairs and 1 lone pair has what shape?", "Trigonal pyramidal", ["Tetrahedral", "Trigonal planar", "Linear"]),
                ("The bond angle in a tetrahedral molecule is approximately:", "109.5°", ["120°", "180°", "90°"]),
                ("Lone pairs of electrons affect molecular shape by:", "Pushing bonding pairs closer together", ["Having no effect", "Making bonds longer", "Adding to the bond angle"]),
                ("Water (H₂O) has what molecular shape?", "Bent", ["Linear", "Trigonal planar", "Tetrahedral"]),
            ]
        },
        "4.9": {
            "topic": "Suborbital Shapes",
            "questions": [
                ("The s orbital has what shape?", "Spherical", ["Dumbbell", "Cloverleaf", "Ring"]),
                ("The p orbital has what shape?", "Dumbbell (figure-eight)", ["Spherical", "Cubic", "Star"]),
                ("The d orbital commonly has what shape?", "Cloverleaf", ["Spherical", "Dumbbell", "Pyramid"]),
                ("How many p orbitals exist in each energy level (n ≥ 2)?", "3", ["1", "5", "7"]),
                ("The three p orbitals are oriented along:", "The x, y, and z axes", ["Only the x axis", "Random directions", "The nucleus"]),
                ("As the principal quantum number increases, orbital size:", "Increases", ["Decreases", "Stays the same", "Becomes zero"]),
                ("The number of nodes in an orbital increases with:", "Higher energy levels", ["Lower energy levels", "More protons", "Fewer electrons"]),
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
    
    # Find the form section and replace its content
    form_start = content.find('<form id="quiz-form">')
    if form_start == -1:
        print(f"  WARNING: No quiz form found in {filepath}")
        return False
    
    form_end = content.find('</form>', form_start)
    if form_end == -1:
        print(f"  WARNING: No </form> found in {filepath}")
        return False
    
    # Build new questions HTML
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
