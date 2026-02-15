#!/usr/bin/env python3
"""Generate topic-specific content for Chemistry Units 1-4.
Replaces placeholder States-of-Matter content with real chemistry content.
"""
import os, re, glob

BASE = os.path.join(os.path.dirname(__file__), '..', 'ArisEdu Project Folder', 'ChemistryLessons')

# ─── CONTENT DATABASE ──────────────────────────────────────────────
# Each lesson has: summary_title, summary_bullets, quiz (2 questions), flashcards (10)
CONTENT = {
    # ══════════════════ UNIT 1 ══════════════════
    "1.1": {
        "topic": "States of Matter",
        "skip_summary": True,  # Already has real content
        "skip_practice": True,
        "skip_quiz": True,
    },
    "1.2": {
        "topic": "Phase Changes",
        "skip_summary": True,
        "skip_practice": True,
        "summary_title": "Phase Changes",
        "summary_bullets": [
            ("<b>Melting</b>", "The change from solid to liquid; occurs at the melting point."),
            ("<b>Freezing</b>", "The change from liquid to solid; occurs at the freezing point."),
            ("<b>Vaporization</b>", "The change from liquid to gas; includes boiling and evaporation."),
            ("<b>Condensation</b>", "The change from gas to liquid; occurs when gas loses energy."),
            ("<b>Sublimation</b>", "The change from solid directly to gas without passing through liquid."),
            ("<b>Deposition</b>", "The change from gas directly to solid without passing through liquid."),
        ],
        "quiz": [
            {
                "question": "What is the process of a liquid changing to a gas called?",
                "correct": "Vaporization",
                "wrong": ["Condensation", "Sublimation", "Deposition"]
            },
            {
                "question": "What term describes a solid changing directly to a gas?",
                "correct": "Sublimation",
                "wrong": ["Melting", "Freezing", "Evaporation"]
            }
        ],
        "flashcards": [
            ("What is melting?", "The change from solid to liquid"),
            ("What is freezing?", "The change from liquid to solid"),
            ("What is vaporization?", "The change from liquid to gas"),
            ("What is condensation?", "The change from gas to liquid"),
            ("What is sublimation?", "The change from solid directly to gas"),
            ("What is deposition?", "The change from gas directly to solid"),
            ("What must be added for melting to occur?", "Heat energy"),
            ("At what point does a solid become a liquid?", "The melting point"),
            ("Is boiling endothermic or exothermic?", "Endothermic (absorbs energy)"),
            ("Is freezing endothermic or exothermic?", "Exothermic (releases energy)")
        ]
    },
    "1.3": {
        "topic": "Intensive & Extensive Properties",
        "summary_title": "Intensive & Extensive Properties",
        "summary_bullets": [
            ("<b>Intensive Property</b>", "A property that does NOT depend on the amount of matter (e.g., density, color, boiling point)."),
            ("<b>Extensive Property</b>", "A property that DOES depend on the amount of matter (e.g., mass, volume, length)."),
            ("<b>Density</b>", "An intensive property equal to mass divided by volume (D = m/v)."),
            ("<b>Color</b>", "An intensive property — a small sample and a large sample have the same color."),
            ("<b>Mass</b>", "An extensive property — doubling the sample doubles the mass."),
            ("<b>Volume</b>", "An extensive property — the amount of space matter occupies changes with sample size."),
        ],
        "quiz": [
            {
                "question": "Which of the following is an intensive property?",
                "correct": "Density",
                "wrong": ["Mass", "Volume", "Length"]
            },
            {
                "question": "Which property depends on the amount of matter present?",
                "correct": "Mass",
                "wrong": ["Boiling point", "Color", "Density"]
            }
        ],
        "flashcards": [
            ("What is an intensive property?", "A property that does NOT depend on the amount of matter"),
            ("What is an extensive property?", "A property that DOES depend on the amount of matter"),
            ("Is density intensive or extensive?", "Intensive"),
            ("Is mass intensive or extensive?", "Extensive"),
            ("Is boiling point intensive or extensive?", "Intensive"),
            ("Is volume intensive or extensive?", "Extensive"),
            ("Give an example of an intensive property.", "Density, color, or boiling point"),
            ("Give an example of an extensive property.", "Mass, volume, or length"),
            ("Does color change with sample size?", "No, color is an intensive property"),
            ("Does length change with sample size?", "Yes, length is an extensive property")
        ]
    },
    "1.4": {
        "topic": "Mass, Volume & Density",
        "skip_summary": True,
        "skip_practice": True,
        "summary_title": "Mass, Volume & Density",
        "summary_bullets": [
            ("<b>Mass</b>", "The amount of matter in an object, measured in grams (g) or kilograms (kg)."),
            ("<b>Volume</b>", "The amount of space an object occupies, measured in liters (L) or cubic centimeters (cm³)."),
            ("<b>Density</b>", "Mass per unit volume: D = m / v."),
            ("<b>Water Displacement</b>", "A technique to measure the volume of an irregularly shaped object."),
            ("<b>Units of Density</b>", "Commonly g/mL or g/cm³."),
            ("<b>Floating & Sinking</b>", "Objects less dense than the liquid float; denser objects sink."),
        ],
        "quiz": [
            {
                "question": "What is the formula for density?",
                "correct": "D = mass / volume",
                "wrong": ["D = volume / mass", "D = mass × volume", "D = mass + volume"]
            },
            {
                "question": "An object with density less than water will:",
                "correct": "Float",
                "wrong": ["Sink", "Dissolve", "Evaporate"]
            }
        ],
        "flashcards": [
            ("What is mass?", "The amount of matter in an object"),
            ("What is volume?", "The amount of space an object occupies"),
            ("What is the formula for density?", "D = mass / volume"),
            ("What unit is density commonly expressed in?", "g/mL or g/cm³"),
            ("What is water displacement used for?", "Measuring the volume of irregularly shaped objects"),
            ("Will an object with a density of 0.8 g/mL float or sink in water?", "Float (less dense than water at 1.0 g/mL)"),
            ("What is the density of water?", "1.0 g/mL"),
            ("If mass = 50g and volume = 25mL, what is the density?", "2.0 g/mL"),
            ("What tool measures mass?", "A balance or scale"),
            ("What tool measures liquid volume?", "A graduated cylinder")
        ]
    },
    "1.5": {
        "topic": "Heterogeneous & Homogeneous Mixtures",
        "summary_title": "Heterogeneous & Homogeneous Mixtures",
        "summary_bullets": [
            ("<b>Mixture</b>", "A combination of two or more substances that are NOT chemically bonded."),
            ("<b>Homogeneous Mixture</b>", "A mixture with a uniform composition throughout; also called a solution (e.g., saltwater)."),
            ("<b>Heterogeneous Mixture</b>", "A mixture with a non-uniform composition; individual parts can be seen (e.g., salad, trail mix)."),
            ("<b>Solution</b>", "A homogeneous mixture where the solute is evenly distributed in the solvent."),
            ("<b>Colloid</b>", "A mixture where tiny particles are dispersed but do not settle out (e.g., milk, fog)."),
            ("<b>Suspension</b>", "A mixture where larger particles are dispersed and eventually settle out (e.g., muddy water)."),
        ],
        "quiz": [
            {
                "question": "Which type of mixture has a uniform composition throughout?",
                "correct": "Homogeneous",
                "wrong": ["Heterogeneous", "Suspension", "Colloid"]
            },
            {
                "question": "Which of the following is a heterogeneous mixture?",
                "correct": "Trail mix",
                "wrong": ["Saltwater", "Vinegar solution", "Air"]
            }
        ],
        "flashcards": [
            ("What is a mixture?", "A combination of two or more substances not chemically bonded"),
            ("What is a homogeneous mixture?", "A mixture with uniform composition throughout (a solution)"),
            ("What is a heterogeneous mixture?", "A mixture with non-uniform composition; parts can be distinguished"),
            ("Give an example of a homogeneous mixture.", "Saltwater"),
            ("Give an example of a heterogeneous mixture.", "Trail mix or salad"),
            ("What is a solution?", "A homogeneous mixture with solute evenly distributed in solvent"),
            ("What is a colloid?", "A mixture with tiny dispersed particles that do not settle"),
            ("What is a suspension?", "A mixture with large particles that settle out over time"),
            ("Is milk a colloid or a solution?", "A colloid"),
            ("Can the parts of a homogeneous mixture be seen with the naked eye?", "No")
        ]
    },
    "1.6": {
        "topic": "Physical & Chemical Properties",
        "summary_title": "Physical & Chemical Properties",
        "summary_bullets": [
            ("<b>Physical Property</b>", "A characteristic observed or measured without changing the substance's identity (e.g., color, density, melting point)."),
            ("<b>Chemical Property</b>", "A characteristic that describes a substance's ability to change into a new substance (e.g., flammability, reactivity)."),
            ("<b>Flammability</b>", "A chemical property describing a substance's ability to burn in oxygen."),
            ("<b>Reactivity</b>", "A chemical property describing how readily a substance reacts with other substances."),
            ("<b>Malleability</b>", "A physical property describing whether a substance can be hammered into thin sheets."),
            ("<b>Conductivity</b>", "A physical property describing how well a substance conducts heat or electricity."),
        ],
        "quiz": [
            {
                "question": "Which of the following is a chemical property?",
                "correct": "Flammability",
                "wrong": ["Color", "Density", "Melting point"]
            },
            {
                "question": "Melting point is an example of what type of property?",
                "correct": "Physical property",
                "wrong": ["Chemical property", "Reactive property", "Nuclear property"]
            }
        ],
        "flashcards": [
            ("What is a physical property?", "A characteristic observed without changing the substance's identity"),
            ("What is a chemical property?", "A characteristic describing a substance's ability to form new substances"),
            ("Is color a physical or chemical property?", "Physical property"),
            ("Is flammability a physical or chemical property?", "Chemical property"),
            ("Is density a physical or chemical property?", "Physical property"),
            ("Is reactivity a physical or chemical property?", "Chemical property"),
            ("Give two examples of physical properties.", "Color and melting point"),
            ("Give two examples of chemical properties.", "Flammability and reactivity"),
            ("What is malleability?", "The ability to be hammered into thin sheets"),
            ("What is conductivity?", "The ability to conduct heat or electricity")
        ]
    },
    "1.7": {
        "topic": "Physical & Chemical Changes",
        "skip_summary": True,
        "summary_title": "Physical & Chemical Changes",
        "summary_bullets": [
            ("<b>Physical Change</b>", "A change in appearance or form but NOT in chemical composition (e.g., cutting, melting)."),
            ("<b>Chemical Change</b>", "A change that produces one or more new substances with new properties (e.g., burning, rusting)."),
            ("<b>Signs of Chemical Change</b>", "Color change, gas production, precipitate formation, temperature change, light emission."),
            ("<b>Reversible Change</b>", "Many physical changes can be reversed (e.g., melting ice back to water)."),
            ("<b>Irreversible Change</b>", "Most chemical changes are difficult or impossible to reverse (e.g., burning wood)."),
            ("<b>Conservation of Mass</b>", "Matter is neither created nor destroyed during any change."),
        ],
        "quiz": [
            {
                "question": "Which of the following is a chemical change?",
                "correct": "Burning wood",
                "wrong": ["Cutting paper", "Melting ice", "Dissolving sugar"]
            },
            {
                "question": "Which is a sign of a chemical change?",
                "correct": "Gas production (bubbles)",
                "wrong": ["Change in shape", "Change in size", "Dissolving"]
            }
        ],
        "flashcards": [
            ("What is a physical change?", "A change in form or appearance, not in composition"),
            ("What is a chemical change?", "A change that produces new substances with new properties"),
            ("Is melting ice a physical or chemical change?", "Physical change"),
            ("Is burning wood a physical or chemical change?", "Chemical change"),
            ("Name three signs of a chemical change.", "Color change, gas production, temperature change"),
            ("Is dissolving sugar a physical or chemical change?", "Physical change"),
            ("Is rusting iron a physical or chemical change?", "Chemical change"),
            ("Can physical changes usually be reversed?", "Yes"),
            ("Can chemical changes usually be reversed?", "No, most are irreversible"),
            ("What law states matter cannot be created or destroyed?", "Law of Conservation of Mass")
        ]
    },
    "1.8": {
        "topic": "Energy & Matter",
        "summary_title": "Energy & Matter",
        "summary_bullets": [
            ("<b>Energy</b>", "The ability to do work or cause change; cannot be created or destroyed (Law of Conservation of Energy)."),
            ("<b>Kinetic Energy</b>", "The energy of motion; increases as particles move faster."),
            ("<b>Potential Energy</b>", "Stored energy based on position or composition."),
            ("<b>Thermal Energy</b>", "The total kinetic energy of all particles in a substance; related to temperature."),
            ("<b>Endothermic Process</b>", "A process that absorbs energy from the surroundings (feels cold)."),
            ("<b>Exothermic Process</b>", "A process that releases energy to the surroundings (feels hot)."),
        ],
        "quiz": [
            {
                "question": "What type of process absorbs energy from the surroundings?",
                "correct": "Endothermic",
                "wrong": ["Exothermic", "Isothermic", "Polythermic"]
            },
            {
                "question": "Energy of motion is called:",
                "correct": "Kinetic energy",
                "wrong": ["Potential energy", "Thermal energy", "Nuclear energy"]
            }
        ],
        "flashcards": [
            ("What is energy?", "The ability to do work or cause change"),
            ("What is kinetic energy?", "The energy of motion"),
            ("What is potential energy?", "Stored energy based on position or composition"),
            ("What is thermal energy?", "The total kinetic energy of all particles in a substance"),
            ("What is an endothermic process?", "A process that absorbs energy from the surroundings"),
            ("What is an exothermic process?", "A process that releases energy to the surroundings"),
            ("Does an endothermic process feel warm or cold?", "Cold (it absorbs heat from surroundings)"),
            ("Does an exothermic process feel warm or cold?", "Warm (it releases heat to surroundings)"),
            ("What is the Law of Conservation of Energy?", "Energy cannot be created or destroyed, only transformed"),
            ("Does temperature increase as particle motion increases?", "Yes")
        ]
    },
    # ══════════════════ UNIT 2 ══════════════════
    "2.1": {
        "topic": "Scientific Notation",
        "summary_title": "Scientific Notation",
        "summary_bullets": [
            ("<b>Scientific Notation</b>", "A way to express very large or very small numbers as a × 10ⁿ, where 1 ≤ a < 10."),
            ("<b>Coefficient</b>", "The number 'a' in scientific notation; must be between 1 and 10."),
            ("<b>Exponent</b>", "The power of 10 that indicates how many places the decimal moves."),
            ("<b>Positive Exponent</b>", "Indicates a large number; decimal moves to the right (e.g., 3.0 × 10³ = 3000)."),
            ("<b>Negative Exponent</b>", "Indicates a small number; decimal moves to the left (e.g., 2.5 × 10⁻² = 0.025)."),
            ("<b>Standard Form</b>", "Writing a number without scientific notation (e.g., 45000 instead of 4.5 × 10⁴)."),
        ],
        "quiz": [
            {
                "question": "What is 3,200 written in scientific notation?",
                "correct": "3.2 × 10³",
                "wrong": ["32 × 10²", "0.32 × 10⁴", "3.2 × 10⁻³"]
            },
            {
                "question": "In scientific notation, the coefficient must be:",
                "correct": "Between 1 and 10",
                "wrong": ["Greater than 10", "Less than 1", "A whole number"]
            }
        ],
        "flashcards": [
            ("What is scientific notation?", "A way to express numbers as a × 10ⁿ where 1 ≤ a < 10"),
            ("What is the coefficient in scientific notation?", "The number in front (must be between 1 and 10)"),
            ("What does a positive exponent mean?", "The number is large; decimal moves right"),
            ("What does a negative exponent mean?", "The number is small; decimal moves left"),
            ("Write 5,600 in scientific notation.", "5.6 × 10³"),
            ("Write 0.0042 in scientific notation.", "4.2 × 10⁻³"),
            ("What is 2.0 × 10⁴ in standard form?", "20,000"),
            ("What is 7.1 × 10⁻² in standard form?", "0.071"),
            ("How do you multiply numbers in scientific notation?", "Multiply coefficients, add exponents"),
            ("How do you divide numbers in scientific notation?", "Divide coefficients, subtract exponents")
        ]
    },
    "2.2": {
        "topic": "Significant Figures",
        "summary_title": "Significant Figures",
        "summary_bullets": [
            ("<b>Significant Figures</b>", "The digits in a measurement that are known with certainty plus one estimated digit."),
            ("<b>Non-zero Digits</b>", "All non-zero digits are always significant (e.g., 123 has 3 sig figs)."),
            ("<b>Captive Zeros</b>", "Zeros between non-zero digits are significant (e.g., 1002 has 4 sig figs)."),
            ("<b>Leading Zeros</b>", "Zeros before the first non-zero digit are NOT significant (e.g., 0.0045 has 2 sig figs)."),
            ("<b>Trailing Zeros</b>", "Zeros at the end of a number are significant only if there is a decimal point (e.g., 100. has 3 sig figs)."),
            ("<b>Exact Numbers</b>", "Numbers obtained by counting or by definition have unlimited significant figures."),
        ],
        "quiz": [
            {
                "question": "How many significant figures does 0.00560 have?",
                "correct": "3",
                "wrong": ["5", "2", "6"]
            },
            {
                "question": "Which type of zeros are NEVER significant?",
                "correct": "Leading zeros",
                "wrong": ["Captive zeros", "Trailing zeros with decimal", "All zeros are significant"]
            }
        ],
        "flashcards": [
            ("What are significant figures?", "Digits known with certainty plus one estimated digit"),
            ("Are non-zero digits always significant?", "Yes"),
            ("Are captive zeros significant?", "Yes (zeros between non-zero digits)"),
            ("Are leading zeros significant?", "No"),
            ("When are trailing zeros significant?", "Only when there is a decimal point"),
            ("How many sig figs in 0.0032?", "2"),
            ("How many sig figs in 100.0?", "4"),
            ("How many sig figs in 4500?", "2 (no decimal point)"),
            ("What are exact numbers?", "Numbers from counting or definitions with unlimited sig figs"),
            ("How many sig figs in 1.020?", "4")
        ]
    },
    "2.3": {
        "topic": "Accuracy vs Precision",
        "summary_title": "Accuracy vs Precision",
        "summary_bullets": [
            ("<b>Accuracy</b>", "How close a measurement is to the true or accepted value."),
            ("<b>Precision</b>", "How close repeated measurements are to each other (reproducibility)."),
            ("<b>Percent Error</b>", "Measures accuracy: |experimental − accepted| / accepted × 100%."),
            ("<b>High Accuracy, High Precision</b>", "Measurements are close to the true value AND close to each other."),
            ("<b>High Precision, Low Accuracy</b>", "Measurements are close to each other but far from the true value."),
            ("<b>Systematic Error</b>", "A consistent error that affects accuracy (e.g., a miscalibrated instrument)."),
        ],
        "quiz": [
            {
                "question": "What does accuracy measure?",
                "correct": "How close a measurement is to the true value",
                "wrong": ["How close measurements are to each other", "The number of sig figs", "The size of the measurement"]
            },
            {
                "question": "What is the formula for percent error?",
                "correct": "|experimental − accepted| / accepted × 100%",
                "wrong": ["accepted / experimental × 100%", "experimental × accepted / 100%", "accepted − experimental"]
            }
        ],
        "flashcards": [
            ("What is accuracy?", "How close a measurement is to the true value"),
            ("What is precision?", "How close repeated measurements are to each other"),
            ("Can measurements be precise but not accurate?", "Yes"),
            ("What does percent error measure?", "Accuracy of a measurement"),
            ("What is the percent error formula?", "|experimental − accepted| / accepted × 100%"),
            ("What causes low accuracy but high precision?", "Systematic error (e.g., miscalibrated instrument)"),
            ("What causes low precision?", "Random errors in measurement"),
            ("If the accepted value is 10 and you measure 9.5, what is percent error?", "5%"),
            ("What is a systematic error?", "A consistent error that shifts all measurements in one direction"),
            ("What is a random error?", "Unpredictable fluctuations in measurements")
        ]
    },
    "2.4": {
        "topic": "Metric System",
        "summary_title": "The Metric System",
        "summary_bullets": [
            ("<b>Metric System</b>", "A decimal-based system of measurement used in science; based on powers of 10."),
            ("<b>Base Units</b>", "Meter (length), gram (mass), liter (volume), second (time)."),
            ("<b>Kilo- (k)</b>", "Prefix meaning 1,000 times the base unit (1 km = 1000 m)."),
            ("<b>Centi- (c)</b>", "Prefix meaning 1/100 of the base unit (1 cm = 0.01 m)."),
            ("<b>Milli- (m)</b>", "Prefix meaning 1/1000 of the base unit (1 mm = 0.001 m)."),
            ("<b>Micro- (μ)</b>", "Prefix meaning 1/1,000,000 of the base unit."),
        ],
        "quiz": [
            {
                "question": "What metric prefix means 1/1000?",
                "correct": "Milli-",
                "wrong": ["Centi-", "Kilo-", "Micro-"]
            },
            {
                "question": "How many centimeters are in 1 meter?",
                "correct": "100",
                "wrong": ["10", "1000", "1"]
            }
        ],
        "flashcards": [
            ("What is the metric system?", "A decimal-based measurement system used in science"),
            ("What is the base unit for length?", "Meter (m)"),
            ("What is the base unit for mass?", "Gram (g)"),
            ("What is the base unit for volume?", "Liter (L)"),
            ("What does the prefix kilo- mean?", "1000 times the base unit"),
            ("What does the prefix centi- mean?", "1/100 of the base unit"),
            ("What does the prefix milli- mean?", "1/1000 of the base unit"),
            ("How many millimeters in 1 meter?", "1000"),
            ("How many milligrams in 1 gram?", "1000"),
            ("What does the prefix micro- mean?", "One millionth (10⁻⁶) of the base unit")
        ]
    },
    "2.5": {
        "topic": "Unit Conversions",
        "summary_title": "Unit Conversions",
        "summary_bullets": [
            ("<b>Dimensional Analysis</b>", "A method of converting units using conversion factors to cancel unwanted units."),
            ("<b>Conversion Factor</b>", "A ratio equal to 1 that relates two different units (e.g., 1 km / 1000 m)."),
            ("<b>Setting Up Conversions</b>", "Place the given unit in a position to cancel, and the desired unit in the answer position."),
            ("<b>Multi-step Conversion</b>", "Some conversions require more than one conversion factor chained together."),
            ("<b>Unit Cancellation</b>", "When a unit appears in both numerator and denominator, it cancels out."),
            ("<b>Always Check Units</b>", "The final answer must have the correct desired unit to verify the conversion."),
        ],
        "quiz": [
            {
                "question": "What method uses conversion factors to switch between units?",
                "correct": "Dimensional analysis",
                "wrong": ["Scientific notation", "Significant figures", "Percent error"]
            },
            {
                "question": "Convert 5 km to meters:",
                "correct": "5000 m",
                "wrong": ["500 m", "50 m", "0.005 m"]
            }
        ],
        "flashcards": [
            ("What is dimensional analysis?", "A method of converting units using conversion factors"),
            ("What is a conversion factor?", "A ratio equal to 1 that relates two units"),
            ("How many meters in 1 kilometer?", "1000 meters"),
            ("How many grams in 1 kilogram?", "1000 grams"),
            ("Convert 2500 mL to liters.", "2.5 L"),
            ("Convert 3.5 kg to grams.", "3500 g"),
            ("What happens when the same unit appears in numerator and denominator?", "It cancels out"),
            ("Convert 450 cm to meters.", "4.5 m"),
            ("What should you always check at the end of a conversion?", "That the final answer has the correct units"),
            ("Convert 0.25 L to mL.", "250 mL")
        ]
    },
    # ══════════════════ UNIT 3 ══════════════════
    "3.1": {
        "topic": "Electrons, Protons & Neutrons",
        "summary_title": "Electrons, Protons & Neutrons",
        "summary_bullets": [
            ("<b>Proton</b>", "A positively charged subatomic particle found in the nucleus; defines the element (atomic number)."),
            ("<b>Neutron</b>", "A neutral subatomic particle found in the nucleus; contributes to atomic mass."),
            ("<b>Electron</b>", "A negatively charged particle orbiting the nucleus in energy levels; very small mass."),
            ("<b>Atomic Number</b>", "The number of protons in an atom; identifies the element."),
            ("<b>Mass Number</b>", "The total number of protons + neutrons in the nucleus."),
            ("<b>Charge Balance</b>", "In a neutral atom, the number of protons equals the number of electrons."),
        ],
        "quiz": [
            {
                "question": "What subatomic particle determines the identity of an element?",
                "correct": "Proton",
                "wrong": ["Neutron", "Electron", "Photon"]
            },
            {
                "question": "What is the charge of a neutron?",
                "correct": "No charge (neutral)",
                "wrong": ["Positive", "Negative", "Variable"]
            }
        ],
        "flashcards": [
            ("What is a proton?", "A positively charged particle in the nucleus"),
            ("What is a neutron?", "A neutral particle in the nucleus"),
            ("What is an electron?", "A negatively charged particle orbiting the nucleus"),
            ("What does the atomic number represent?", "The number of protons in an atom"),
            ("What is the mass number?", "The total number of protons plus neutrons"),
            ("Where are protons and neutrons located?", "In the nucleus"),
            ("Where are electrons located?", "In energy levels (electron cloud) around the nucleus"),
            ("In a neutral atom, what equals the number of protons?", "The number of electrons"),
            ("Which particle has the smallest mass?", "Electron"),
            ("How do you find the number of neutrons?", "Mass number minus atomic number")
        ]
    },
    "3.2": {
        "topic": "Atomic Structure",
        "summary_title": "Atomic Structure",
        "summary_bullets": [
            ("<b>Nucleus</b>", "The dense, central core of an atom containing protons and neutrons."),
            ("<b>Electron Cloud</b>", "The region around the nucleus where electrons are most likely to be found."),
            ("<b>Energy Levels</b>", "Regions around the nucleus where electrons orbit; numbered 1, 2, 3, etc."),
            ("<b>Atomic Radius</b>", "The size of an atom measured from the nucleus to the outer electron cloud."),
            ("<b>Nuclear Force</b>", "The strong force that holds protons and neutrons together in the nucleus."),
            ("<b>Atom</b>", "The smallest unit of an element that retains the element's chemical properties."),
        ],
        "quiz": [
            {
                "question": "What is the dense center of an atom called?",
                "correct": "Nucleus",
                "wrong": ["Electron cloud", "Energy level", "Orbital"]
            },
            {
                "question": "Where are electrons most likely to be found?",
                "correct": "In the electron cloud around the nucleus",
                "wrong": ["Inside the nucleus", "Between atoms", "In the neutrons"]
            }
        ],
        "flashcards": [
            ("What is the nucleus?", "The dense central core containing protons and neutrons"),
            ("What is the electron cloud?", "The region around the nucleus where electrons are likely found"),
            ("What are energy levels?", "Regions around the nucleus where electrons orbit"),
            ("What holds the nucleus together?", "The strong nuclear force"),
            ("What is an atom?", "The smallest unit of an element retaining its chemical properties"),
            ("What is the atomic radius?", "The distance from the nucleus to the outer electron cloud"),
            ("Most of an atom is made of what?", "Empty space (electron cloud region)"),
            ("How many electrons can the first energy level hold?", "2"),
            ("How many electrons can the second energy level hold?", "8"),
            ("What determines the size of an atom?", "The number of energy levels (electron shells)")
        ]
    },
    "3.3": {
        "topic": "Quantum Mechanical Model & Orbitals",
        "summary_title": "Quantum Mechanical Model & Orbitals",
        "summary_bullets": [
            ("<b>Quantum Mechanical Model</b>", "The modern model of the atom that treats electrons as waves and defines probability regions (orbitals)."),
            ("<b>Orbital</b>", "A region of space where there is a high probability of finding an electron."),
            ("<b>s Orbital</b>", "Spherical-shaped orbital; each energy level has one s orbital (holds 2 electrons)."),
            ("<b>p Orbital</b>", "Dumbbell-shaped orbital; exists starting from the 2nd energy level (3 orbitals, holds 6 electrons)."),
            ("<b>d Orbital</b>", "Clover-shaped orbital; exists starting from the 3rd energy level (5 orbitals, holds 10 electrons)."),
            ("<b>Heisenberg Uncertainty Principle</b>", "You cannot simultaneously know both the exact position and momentum of an electron."),
        ],
        "quiz": [
            {
                "question": "What shape is an s orbital?",
                "correct": "Spherical",
                "wrong": ["Dumbbell", "Clover", "Cone"]
            },
            {
                "question": "How many electrons can a p sublevel hold?",
                "correct": "6",
                "wrong": ["2", "10", "14"]
            }
        ],
        "flashcards": [
            ("What is the quantum mechanical model?", "The modern atomic model treating electrons as waves with probability regions"),
            ("What is an orbital?", "A region where there is high probability of finding an electron"),
            ("What shape is an s orbital?", "Spherical"),
            ("What shape is a p orbital?", "Dumbbell"),
            ("How many electrons can one orbital hold?", "2"),
            ("How many p orbitals are in a sublevel?", "3 (holding 6 electrons total)"),
            ("What is the Heisenberg Uncertainty Principle?", "Cannot know both exact position and momentum of an electron simultaneously"),
            ("Starting at which energy level do p orbitals appear?", "2nd energy level"),
            ("Starting at which energy level do d orbitals appear?", "3rd energy level"),
            ("How many d orbitals are in a sublevel?", "5 (holding 10 electrons total)")
        ]
    },
    "3.4": {
        "topic": "EM Spectrum & Atomic Emission Spectra",
        "summary_title": "EM Spectrum & Atomic Emission Spectra",
        "summary_bullets": [
            ("<b>Electromagnetic Spectrum</b>", "The full range of electromagnetic radiation from radio waves to gamma rays."),
            ("<b>Wavelength (λ)</b>", "The distance between two consecutive wave peaks; measured in meters or nanometers."),
            ("<b>Frequency (ν)</b>", "The number of wave cycles per second; measured in hertz (Hz)."),
            ("<b>Speed of Light</b>", "c = λ × ν = 3.0 × 10⁸ m/s; wavelength and frequency are inversely related."),
            ("<b>Atomic Emission Spectrum</b>", "The unique pattern of light frequencies emitted by an element's excited electrons."),
            ("<b>Photon</b>", "A particle (quantum) of electromagnetic radiation; energy = hν."),
        ],
        "quiz": [
            {
                "question": "What is the relationship between wavelength and frequency?",
                "correct": "Inversely proportional",
                "wrong": ["Directly proportional", "No relationship", "Exponential"]
            },
            {
                "question": "What produces an atomic emission spectrum?",
                "correct": "Excited electrons releasing energy as light",
                "wrong": ["Protons splitting", "Neutrons vibrating", "Nuclear fusion"]
            }
        ],
        "flashcards": [
            ("What is the electromagnetic spectrum?", "The full range of EM radiation from radio waves to gamma rays"),
            ("What is wavelength?", "The distance between two consecutive wave peaks"),
            ("What is frequency?", "The number of wave cycles per second (Hz)"),
            ("What is the speed of light equation?", "c = λ × ν (3.0 × 10⁸ m/s)"),
            ("How are wavelength and frequency related?", "Inversely — as one increases, the other decreases"),
            ("What is a photon?", "A particle of electromagnetic radiation"),
            ("What is an atomic emission spectrum?", "The unique pattern of light frequencies emitted by an element"),
            ("What happens when an electron drops to a lower energy level?", "It emits a photon of light"),
            ("Which has more energy: radio waves or gamma rays?", "Gamma rays"),
            ("What is Planck's equation for photon energy?", "E = hν (energy = Planck's constant × frequency)")
        ]
    },
    "3.5": {
        "topic": "Radioactivity & Stability",
        "summary_title": "Radioactivity & Stability",
        "summary_bullets": [
            ("<b>Radioactivity</b>", "The spontaneous emission of radiation from an unstable nucleus."),
            ("<b>Nuclear Stability</b>", "Depends on the ratio of neutrons to protons; too many or too few neutrons = unstable."),
            ("<b>Band of Stability</b>", "The zone on a graph of neutrons vs. protons where stable nuclei exist."),
            ("<b>Alpha Decay</b>", "Emission of an alpha particle (²₄He); reduces atomic number by 2 and mass number by 4."),
            ("<b>Beta Decay</b>", "A neutron converts to a proton and emits a beta particle (electron); atomic number increases by 1."),
            ("<b>Gamma Radiation</b>", "High-energy electromagnetic radiation emitted from the nucleus; no change in mass or atomic number."),
        ],
        "quiz": [
            {
                "question": "What determines whether a nucleus is stable or radioactive?",
                "correct": "The neutron-to-proton ratio",
                "wrong": ["The number of electrons", "The atomic mass alone", "The element's color"]
            },
            {
                "question": "In alpha decay, the mass number decreases by:",
                "correct": "4",
                "wrong": ["1", "2", "0"]
            }
        ],
        "flashcards": [
            ("What is radioactivity?", "Spontaneous emission of radiation from an unstable nucleus"),
            ("What determines nuclear stability?", "The neutron-to-proton ratio"),
            ("What is the band of stability?", "The zone where stable nuclei exist on a neutrons vs. protons graph"),
            ("What is alpha decay?", "Emission of a helium-4 nucleus (2 protons, 2 neutrons)"),
            ("What is beta decay?", "A neutron converts to a proton, emitting an electron"),
            ("What is gamma radiation?", "High-energy EM radiation from the nucleus with no mass change"),
            ("How does alpha decay change atomic number?", "Decreases by 2"),
            ("How does beta decay change atomic number?", "Increases by 1"),
            ("Which type of radiation is most penetrating?", "Gamma radiation"),
            ("Which type of radiation is least penetrating?", "Alpha particles (stopped by paper)")
        ]
    },
    "3.6": {
        "topic": "Isotopes & Radioisotopes",
        "summary_title": "Isotopes & Radioisotopes",
        "summary_bullets": [
            ("<b>Isotope</b>", "Atoms of the same element with different numbers of neutrons (same protons, different mass numbers)."),
            ("<b>Radioisotope</b>", "An unstable isotope that undergoes radioactive decay."),
            ("<b>Atomic Mass</b>", "The weighted average mass of all naturally occurring isotopes of an element."),
            ("<b>Mass Number</b>", "The total number of protons and neutrons in a specific isotope."),
            ("<b>Isotope Notation</b>", "Written as Element-mass number (e.g., Carbon-14) or with superscript mass number."),
            ("<b>Percent Abundance</b>", "The percentage of each isotope found naturally; used to calculate atomic mass."),
        ],
        "quiz": [
            {
                "question": "What do isotopes of an element have in common?",
                "correct": "Same number of protons",
                "wrong": ["Same number of neutrons", "Same mass number", "Same atomic mass"]
            },
            {
                "question": "What is a radioisotope?",
                "correct": "An unstable isotope that undergoes radioactive decay",
                "wrong": ["A stable isotope", "An ion with extra electrons", "A molecule with radiation"]
            }
        ],
        "flashcards": [
            ("What is an isotope?", "Atoms of the same element with different numbers of neutrons"),
            ("What is a radioisotope?", "An unstable isotope that undergoes radioactive decay"),
            ("What do isotopes of the same element share?", "The same number of protons (atomic number)"),
            ("How do isotopes differ?", "They have different numbers of neutrons"),
            ("What is atomic mass?", "The weighted average mass of all naturally occurring isotopes"),
            ("What is Carbon-14?", "An isotope of carbon with 6 protons and 8 neutrons"),
            ("What is percent abundance?", "The percentage of each isotope found in nature"),
            ("How do you calculate atomic mass?", "Sum of (mass × percent abundance) for each isotope"),
            ("Do isotopes have the same chemical properties?", "Yes, because they have the same electrons"),
            ("What is mass number?", "Total protons + neutrons in an isotope")
        ]
    },
    "3.7": {
        "topic": "Element Synthesis",
        "summary_title": "Element Synthesis",
        "summary_bullets": [
            ("<b>Element Synthesis</b>", "The creation of new elements by bombarding target nuclei with high-speed particles."),
            ("<b>Particle Accelerator</b>", "A machine that speeds up charged particles to collide with target atoms."),
            ("<b>Transuranium Elements</b>", "Elements with atomic numbers greater than 92 (uranium); all are synthetic."),
            ("<b>Nuclear Fusion</b>", "Combining two lighter nuclei to form a heavier one; releases enormous energy."),
            ("<b>Synthetic Elements</b>", "Elements not found naturally; created in labs using nuclear reactions."),
            ("<b>Super-heavy Elements</b>", "Elements with very high atomic numbers (e.g., oganesson, element 118); extremely unstable."),
        ],
        "quiz": [
            {
                "question": "What are transuranium elements?",
                "correct": "Elements with atomic numbers greater than 92",
                "wrong": ["Elements lighter than hydrogen", "Elements found in nature only", "Nonmetal elements"]
            },
            {
                "question": "What tool is used to create synthetic elements?",
                "correct": "Particle accelerator",
                "wrong": ["Microscope", "Bunsen burner", "Centrifuge"]
            }
        ],
        "flashcards": [
            ("What is element synthesis?", "Creating new elements by bombarding nuclei with particles"),
            ("What is a particle accelerator?", "A machine that speeds up charged particles for nuclear collisions"),
            ("What are transuranium elements?", "Elements with atomic numbers greater than 92"),
            ("Are transuranium elements natural or synthetic?", "Synthetic (made in labs)"),
            ("What is nuclear fusion?", "Combining two lighter nuclei to form a heavier one"),
            ("What is the heaviest known element?", "Oganesson (element 118)"),
            ("Why are super-heavy elements unstable?", "Too many protons create strong repulsive forces"),
            ("Where does element synthesis occur in nature?", "In stars through nuclear fusion"),
            ("Who discovered the first transuranium element?", "Glenn Seaborg and team"),
            ("What element has atomic number 93?", "Neptunium")
        ]
    },
    "3.8": {
        "topic": "Atomic Theory",
        "summary_title": "Atomic Theory",
        "summary_bullets": [
            ("<b>Democritus</b>", "Greek philosopher who first proposed that matter is made of small, indivisible particles called 'atomos.'"),
            ("<b>Dalton's Atomic Theory</b>", "All matter is made of atoms; atoms of the same element are identical; atoms combine in whole-number ratios."),
            ("<b>Thomson's Model</b>", "Discovered the electron; proposed the 'plum pudding' model with negative charges in positive mass."),
            ("<b>Rutherford's Model</b>", "Discovered the nucleus through the gold foil experiment; most of the atom is empty space."),
            ("<b>Bohr's Model</b>", "Electrons orbit the nucleus in fixed energy levels (like planets around the sun)."),
            ("<b>Modern Model</b>", "The quantum mechanical model; electrons exist in probability clouds (orbitals), not fixed paths."),
        ],
        "quiz": [
            {
                "question": "Who discovered the nucleus through the gold foil experiment?",
                "correct": "Rutherford",
                "wrong": ["Thomson", "Bohr", "Dalton"]
            },
            {
                "question": "What model describes electrons as existing in probability clouds?",
                "correct": "Quantum mechanical model",
                "wrong": ["Bohr model", "Plum pudding model", "Dalton's model"]
            }
        ],
        "flashcards": [
            ("Who first proposed the idea of the atom?", "Democritus"),
            ("What did Dalton say about atoms of the same element?", "They are identical in mass and properties"),
            ("What did Thomson discover?", "The electron"),
            ("What was Thomson's model called?", "The plum pudding model"),
            ("What did Rutherford's gold foil experiment prove?", "Atoms have a small, dense, positive nucleus"),
            ("What did Bohr propose?", "Electrons orbit in fixed energy levels"),
            ("What is the modern atomic model called?", "The quantum mechanical model"),
            ("In the modern model, where are electrons found?", "In probability clouds called orbitals"),
            ("What is most of the atom made of?", "Empty space"),
            ("What experiment led to the discovery of the nucleus?", "The gold foil experiment")
        ]
    },
    # ══════════════════ UNIT 4 ══════════════════
    "4.1": {
        "topic": "Chemical Symbols",
        "summary_title": "Chemical Symbols",
        "summary_bullets": [
            ("<b>Chemical Symbol</b>", "A one- or two-letter abbreviation for an element (e.g., H for hydrogen, Na for sodium)."),
            ("<b>First Letter</b>", "Always capitalized (e.g., C for carbon)."),
            ("<b>Second Letter</b>", "Always lowercase (e.g., Ca for calcium, not CA)."),
            ("<b>Latin-Based Symbols</b>", "Some symbols come from Latin names (Na = natrium/sodium, Fe = ferrum/iron, Au = aurum/gold)."),
            ("<b>Periodic Table</b>", "The organized chart listing all known elements with their symbols, atomic numbers, and masses."),
            ("<b>Element vs. Compound</b>", "Elements have single symbols; compounds combine symbols (e.g., H₂O, NaCl)."),
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for sodium?",
                "correct": "Na",
                "wrong": ["So", "Sd", "S"]
            },
            {
                "question": "How is the second letter of a chemical symbol written?",
                "correct": "Lowercase",
                "wrong": ["Uppercase", "Subscript", "Italic"]
            }
        ],
        "flashcards": [
            ("What is a chemical symbol?", "A one- or two-letter abbreviation for an element"),
            ("What is the symbol for gold?", "Au (from Latin aurum)"),
            ("What is the symbol for iron?", "Fe (from Latin ferrum)"),
            ("What is the symbol for sodium?", "Na (from Latin natrium)"),
            ("How is the first letter of a symbol written?", "Capitalized"),
            ("How is the second letter of a symbol written?", "Lowercase"),
            ("What is the symbol for potassium?", "K (from Latin kalium)"),
            ("What is the symbol for silver?", "Ag (from Latin argentum)"),
            ("What is the symbol for carbon?", "C"),
            ("What is the symbol for oxygen?", "O")
        ]
    },
    "4.2": {
        "topic": "Periodic Table Arrangement",
        "summary_title": "Periodic Table Arrangement",
        "summary_bullets": [
            ("<b>Periods</b>", "Horizontal rows on the periodic table; elements in the same period have the same number of energy levels."),
            ("<b>Groups/Families</b>", "Vertical columns; elements in the same group have similar chemical properties and the same number of valence electrons."),
            ("<b>Metals</b>", "Found on the left side; good conductors, malleable, ductile, shiny."),
            ("<b>Nonmetals</b>", "Found on the right side; poor conductors, brittle as solids, dull."),
            ("<b>Metalloids</b>", "Found along the staircase line; have properties of both metals and nonmetals (e.g., silicon)."),
            ("<b>Atomic Number Order</b>", "Elements are arranged by increasing atomic number from left to right."),
        ],
        "quiz": [
            {
                "question": "What do elements in the same group have in common?",
                "correct": "Same number of valence electrons and similar properties",
                "wrong": ["Same number of neutrons", "Same mass number", "Same number of energy levels"]
            },
            {
                "question": "Where are metalloids found on the periodic table?",
                "correct": "Along the staircase line between metals and nonmetals",
                "wrong": ["Far left side", "Far right side", "Bottom row"]
            }
        ],
        "flashcards": [
            ("What are periods on the periodic table?", "Horizontal rows"),
            ("What are groups on the periodic table?", "Vertical columns"),
            ("What do elements in the same group share?", "Similar properties and same number of valence electrons"),
            ("Where are metals found?", "Left side of the periodic table"),
            ("Where are nonmetals found?", "Right side of the periodic table"),
            ("What are metalloids?", "Elements with properties of both metals and nonmetals"),
            ("How are elements arranged on the periodic table?", "By increasing atomic number"),
            ("What are properties of metals?", "Shiny, malleable, ductile, good conductors"),
            ("What are properties of nonmetals?", "Dull, brittle, poor conductors"),
            ("Give an example of a metalloid.", "Silicon or germanium")
        ]
    },
    "4.3": {
        "topic": "Valence Electrons & Reactivity",
        "summary_title": "Valence Electrons & Reactivity",
        "summary_bullets": [
            ("<b>Valence Electrons</b>", "Electrons in the outermost energy level; determine an element's chemical behavior."),
            ("<b>Octet Rule</b>", "Atoms tend to gain, lose, or share electrons to have 8 valence electrons (stable)."),
            ("<b>Alkali Metals (Group 1)</b>", "Have 1 valence electron; very reactive, easily lose 1 electron."),
            ("<b>Halogens (Group 17)</b>", "Have 7 valence electrons; very reactive, easily gain 1 electron."),
            ("<b>Noble Gases (Group 18)</b>", "Have 8 valence electrons (full outer shell); very stable and unreactive."),
            ("<b>Reactivity Trends</b>", "Metals become more reactive going down a group; nonmetals become more reactive going up."),
        ],
        "quiz": [
            {
                "question": "How many valence electrons do elements in Group 1 have?",
                "correct": "1",
                "wrong": ["2", "7", "8"]
            },
            {
                "question": "Why are noble gases unreactive?",
                "correct": "They have a full outer shell of electrons",
                "wrong": ["They have no electrons", "They are gases", "They are radioactive"]
            }
        ],
        "flashcards": [
            ("What are valence electrons?", "Electrons in the outermost energy level"),
            ("What is the octet rule?", "Atoms tend to have 8 valence electrons for stability"),
            ("How many valence electrons do alkali metals have?", "1"),
            ("How many valence electrons do halogens have?", "7"),
            ("How many valence electrons do noble gases have?", "8 (full outer shell)"),
            ("Why are alkali metals highly reactive?", "They easily lose their 1 valence electron"),
            ("Why are halogens highly reactive?", "They need only 1 more electron to fill their outer shell"),
            ("As you go down a group, does metal reactivity increase or decrease?", "Increase"),
            ("What determines an element's chemical behavior?", "Its valence electrons"),
            ("Which group is the most reactive family of metals?", "Group 1 (alkali metals)")
        ]
    },
    "4.4": {
        "topic": "Electron Suborbitals",
        "summary_title": "Electron Suborbitals",
        "summary_bullets": [
            ("<b>Sublevel (Subshell)</b>", "Subdivisions within energy levels: s, p, d, f."),
            ("<b>s Sublevel</b>", "1 orbital, holds up to 2 electrons; found in every energy level."),
            ("<b>p Sublevel</b>", "3 orbitals, holds up to 6 electrons; starts at energy level 2."),
            ("<b>d Sublevel</b>", "5 orbitals, holds up to 10 electrons; starts at energy level 3."),
            ("<b>f Sublevel</b>", "7 orbitals, holds up to 14 electrons; starts at energy level 4."),
            ("<b>Aufbau Principle</b>", "Electrons fill the lowest-energy sublevel first before moving to higher ones."),
        ],
        "quiz": [
            {
                "question": "How many electrons can the d sublevel hold?",
                "correct": "10",
                "wrong": ["2", "6", "14"]
            },
            {
                "question": "At which energy level does the f sublevel first appear?",
                "correct": "4",
                "wrong": ["1", "2", "3"]
            }
        ],
        "flashcards": [
            ("What are the four types of sublevels?", "s, p, d, f"),
            ("How many orbitals does the s sublevel have?", "1 (holds 2 electrons)"),
            ("How many orbitals does the p sublevel have?", "3 (holds 6 electrons)"),
            ("How many orbitals does the d sublevel have?", "5 (holds 10 electrons)"),
            ("How many orbitals does the f sublevel have?", "7 (holds 14 electrons)"),
            ("What is the Aufbau Principle?", "Electrons fill the lowest energy sublevel first"),
            ("At which energy level do p orbitals start?", "Energy level 2"),
            ("At which energy level do d orbitals start?", "Energy level 3"),
            ("At which energy level do f orbitals start?", "Energy level 4"),
            ("What is a sublevel?", "A subdivision within an energy level (s, p, d, or f)")
        ]
    },
    "4.5": {
        "topic": "Electron Configuration",
        "summary_title": "Electron Configuration",
        "summary_bullets": [
            ("<b>Electron Configuration</b>", "The arrangement of electrons in an atom's orbitals (e.g., 1s² 2s² 2p⁶)."),
            ("<b>Aufbau Principle</b>", "Electrons fill orbitals from lowest to highest energy."),
            ("<b>Pauli Exclusion Principle</b>", "Each orbital can hold a maximum of 2 electrons with opposite spins."),
            ("<b>Hund's Rule</b>", "Electrons fill orbitals of the same sublevel singly before pairing up."),
            ("<b>Noble Gas Shorthand</b>", "Uses the preceding noble gas symbol in brackets to abbreviate (e.g., [Ne] 3s² 3p³ for phosphorus)."),
            ("<b>Diagonal Rule</b>", "The filling order follows a diagonal pattern: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p..."),
        ],
        "quiz": [
            {
                "question": "What principle states electrons fill the lowest energy orbitals first?",
                "correct": "Aufbau Principle",
                "wrong": ["Hund's Rule", "Pauli Exclusion Principle", "Heisenberg Principle"]
            },
            {
                "question": "What is the electron configuration of carbon (atomic number 6)?",
                "correct": "1s² 2s² 2p²",
                "wrong": ["1s² 2s⁴", "1s² 2p⁴", "2s² 2p⁴"]
            }
        ],
        "flashcards": [
            ("What is electron configuration?", "The arrangement of electrons in an atom's orbitals"),
            ("What does the Aufbau Principle state?", "Electrons fill orbitals from lowest to highest energy"),
            ("What does the Pauli Exclusion Principle state?", "Each orbital holds a maximum of 2 electrons with opposite spins"),
            ("What does Hund's Rule state?", "Electrons fill orbitals singly before pairing in the same sublevel"),
            ("Write the electron configuration for oxygen (8 electrons).", "1s² 2s² 2p⁴"),
            ("What is noble gas shorthand?", "Using a noble gas symbol in brackets to abbreviate configuration"),
            ("What is the configuration of sodium using shorthand?", "[Ne] 3s¹"),
            ("What is the diagonal rule?", "The filling order: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p..."),
            ("How many electrons can the 2p sublevel hold?", "6"),
            ("Write the electron configuration for neon (10 electrons).", "1s² 2s² 2p⁶")
        ]
    },
    "4.6": {
        "topic": "Periodic Trends",
        "summary_title": "Periodic Trends",
        "summary_bullets": [
            ("<b>Atomic Radius</b>", "Increases going DOWN a group (more energy levels) and DECREASES going across a period (more protons pull electrons closer)."),
            ("<b>Ionization Energy</b>", "The energy required to remove an electron; INCREASES across a period and DECREASES down a group."),
            ("<b>Electronegativity</b>", "An atom's ability to attract electrons in a bond; INCREASES across a period and DECREASES down a group."),
            ("<b>Electron Affinity</b>", "The energy released when an atom gains an electron; generally increases across a period."),
            ("<b>Metallic Character</b>", "INCREASES going down a group and DECREASES going across a period."),
            ("<b>Fluorine</b>", "The most electronegative element on the periodic table."),
        ],
        "quiz": [
            {
                "question": "As you move across a period, what happens to atomic radius?",
                "correct": "It decreases",
                "wrong": ["It increases", "It stays the same", "It doubles"]
            },
            {
                "question": "Which element has the highest electronegativity?",
                "correct": "Fluorine",
                "wrong": ["Oxygen", "Cesium", "Helium"]
            }
        ],
        "flashcards": [
            ("What happens to atomic radius going down a group?", "It increases (more energy levels)"),
            ("What happens to atomic radius going across a period?", "It decreases (more protons pull electrons closer)"),
            ("What is ionization energy?", "The energy required to remove an electron"),
            ("What is electronegativity?", "An atom's ability to attract electrons in a bond"),
            ("Which element is the most electronegative?", "Fluorine"),
            ("What happens to ionization energy across a period?", "It increases"),
            ("What happens to metallic character down a group?", "It increases"),
            ("What is electron affinity?", "Energy released when an atom gains an electron"),
            ("What element has the largest atomic radius?", "Francium (bottom-left of periodic table)"),
            ("What happens to metallic character across a period?", "It decreases")
        ]
    },
    "4.7": {
        "topic": "Shielding Effect",
        "summary_title": "Shielding Effect",
        "summary_bullets": [
            ("<b>Shielding Effect</b>", "Inner electrons block (shield) outer electrons from the full nuclear charge."),
            ("<b>Effective Nuclear Charge (Zeff)</b>", "The net positive charge felt by valence electrons after shielding: Zeff = Z − S."),
            ("<b>More Shielding</b>", "As you go DOWN a group, more inner electron shells increase shielding, so outer electrons are held less tightly."),
            ("<b>Across a Period</b>", "Shielding stays roughly the same, but nuclear charge increases, so Zeff increases."),
            ("<b>Effect on Atomic Radius</b>", "Greater shielding → larger atomic radius (electrons are farther from nucleus)."),
            ("<b>Effect on Ionization Energy</b>", "Greater shielding → lower ionization energy (easier to remove outer electrons)."),
        ],
        "quiz": [
            {
                "question": "What does the shielding effect describe?",
                "correct": "Inner electrons blocking outer electrons from nuclear charge",
                "wrong": ["Protons repelling neutrons", "Electrons orbiting faster", "Nucleus getting smaller"]
            },
            {
                "question": "What happens to shielding as you go down a group?",
                "correct": "It increases",
                "wrong": ["It decreases", "It stays the same", "It disappears"]
            }
        ],
        "flashcards": [
            ("What is the shielding effect?", "Inner electrons block outer electrons from the full nuclear charge"),
            ("What is effective nuclear charge (Zeff)?", "The net positive charge felt by valence electrons"),
            ("How do you calculate Zeff?", "Zeff = Z (atomic number) − S (shielding electrons)"),
            ("What happens to shielding going down a group?", "It increases (more inner electron shells)"),
            ("What happens to Zeff across a period?", "It increases (more protons, same shielding)"),
            ("How does shielding affect atomic radius?", "More shielding = larger radius"),
            ("How does shielding affect ionization energy?", "More shielding = lower ionization energy"),
            ("Why do atoms get larger going down a group?", "Increased shielding lets outer electrons spread farther"),
            ("Do inner electrons or valence electrons cause shielding?", "Inner electrons"),
            ("Which has more shielding: Na or K?", "K (potassium has more inner electron shells)")
        ]
    },
    "4.8": {
        "topic": "VSEPR & Molecule Shapes",
        "summary_title": "VSEPR & Molecule Shapes",
        "summary_bullets": [
            ("<b>VSEPR Theory</b>", "Valence Shell Electron Pair Repulsion — electron pairs around a central atom arrange to minimize repulsion."),
            ("<b>Linear</b>", "2 bonding pairs, 0 lone pairs → 180° bond angle (e.g., CO₂)."),
            ("<b>Trigonal Planar</b>", "3 bonding pairs, 0 lone pairs → 120° bond angle (e.g., BF₃)."),
            ("<b>Tetrahedral</b>", "4 bonding pairs, 0 lone pairs → 109.5° bond angle (e.g., CH₄)."),
            ("<b>Bent</b>", "2 bonding pairs, 1-2 lone pairs → less than 120° or 109.5° (e.g., H₂O)."),
            ("<b>Lone Pairs</b>", "Non-bonding electron pairs that take up space and compress bond angles."),
        ],
        "quiz": [
            {
                "question": "What molecular shape does CO₂ have?",
                "correct": "Linear",
                "wrong": ["Bent", "Tetrahedral", "Trigonal planar"]
            },
            {
                "question": "What does VSEPR stand for?",
                "correct": "Valence Shell Electron Pair Repulsion",
                "wrong": ["Valence Suborbital Energy Pair Ratio", "Variable Shell Electron Proton Reduction", "Visual Structure Electron Pair Reflection"]
            }
        ],
        "flashcards": [
            ("What does VSEPR stand for?", "Valence Shell Electron Pair Repulsion"),
            ("What molecular shape has a 180° bond angle?", "Linear"),
            ("What molecular shape has a 120° bond angle?", "Trigonal planar"),
            ("What molecular shape has a 109.5° bond angle?", "Tetrahedral"),
            ("What shape does water (H₂O) have?", "Bent"),
            ("What shape does methane (CH₄) have?", "Tetrahedral"),
            ("What shape does CO₂ have?", "Linear"),
            ("What are lone pairs?", "Non-bonding electron pairs on the central atom"),
            ("How do lone pairs affect bond angles?", "They compress (reduce) bond angles"),
            ("What shape does BF₃ have?", "Trigonal planar")
        ]
    },
    "4.9": {
        "topic": "Suborbital Shapes",
        "summary_title": "Suborbital Shapes",
        "summary_bullets": [
            ("<b>s Orbital Shape</b>", "Spherical; exists in every energy level."),
            ("<b>p Orbital Shape</b>", "Dumbbell (figure-eight); 3 orientations along x, y, z axes."),
            ("<b>d Orbital Shape</b>", "Clover-leaf (most) and donut-dumbbell; 5 orientations."),
            ("<b>f Orbital Shape</b>", "Complex multi-lobed shapes; 7 orientations."),
            ("<b>Orbital Size</b>", "Orbitals of the same type get larger at higher energy levels (e.g., 3s > 2s > 1s)."),
            ("<b>Node</b>", "A region where the probability of finding an electron is zero."),
        ],
        "quiz": [
            {
                "question": "What shape is a p orbital?",
                "correct": "Dumbbell",
                "wrong": ["Spherical", "Clover-leaf", "Ring"]
            },
            {
                "question": "How many orientations does a d sublevel have?",
                "correct": "5",
                "wrong": ["1", "3", "7"]
            }
        ],
        "flashcards": [
            ("What shape is an s orbital?", "Spherical"),
            ("What shape is a p orbital?", "Dumbbell (figure-eight)"),
            ("What shape is a d orbital?", "Clover-leaf (most d orbitals)"),
            ("How many orientations do p orbitals have?", "3 (px, py, pz)"),
            ("How many orientations do d orbitals have?", "5"),
            ("How many orientations do f orbitals have?", "7"),
            ("What is a node?", "A region where the probability of finding an electron is zero"),
            ("Do orbitals get larger at higher energy levels?", "Yes (e.g., 3s is larger than 2s)"),
            ("Which orbital shape is the simplest?", "s orbital (spherical)"),
            ("What axes do the three p orbitals align with?", "x, y, and z axes")
        ]
    },
}

# ─── HELPER FUNCTIONS ──────────────────────────────────────────────
def make_summary_html(data):
    """Generate the inner summary HTML."""
    lines = []
    lines.append(f'<h3>Key Concepts: {data["summary_title"]}</h3>')
    lines.append('<p><b>Core Definitions</b></p>')
    lines.append('<ul>')
    for label, desc in data["summary_bullets"]:
        lines.append(f'<li>{label}: {desc}</li>')
    lines.append('</ul>')
    return '\n'.join(lines)

def make_quiz_html(data):
    """Generate the quiz questions HTML (just the two question divs)."""
    blocks = []
    for i, q in enumerate(data["quiz"], 1):
        # Build options — shuffle correct among wrong
        import random
        options = [(q["correct"], "correct")] + [(w, "wrong") for w in q["wrong"]]
        random.seed(hash(q["question"]))  # deterministic shuffle per question
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
    """Generate the flashcards JS array."""
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
        if not summary_glob:
            # Try alternate patterns
            summary_glob = glob.glob(os.path.join(unit_path, f"Lesson {lesson_id}_Summary.html"))
        
        for fpath in summary_glob:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if it has placeholder content (States of Matter markers)
            if 'Solid' in content and 'Liquid' in content and 'Gas' in content and 'tightly packed' in content:
                new_summary = make_summary_html(data)
                # Replace the inner content of lesson-notes or lesson-summary-content div
                pattern = r'(<div class="lesson-(?:notes|summary-content)">)\s*.*?\s*(</div>)'
                replacement = f'\\1\n{new_summary}\n\\2'
                new_content, n = re.subn(pattern, replacement, content, count=1, flags=re.DOTALL)
                if n > 0:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    changes += n
                    files_modified += 1
                    print(f"  [SUMMARY] Updated: {os.path.basename(fpath)}")
                else:
                    print(f"  [WARN] Pattern not matched: {os.path.basename(fpath)}")
            else:
                print(f"  [SKIP] Summary already has real content: {os.path.basename(fpath)}")
    
    # ── QUIZ ──
    if not data.get("skip_quiz"):
        quiz_glob = glob.glob(os.path.join(unit_path, f"Lesson {lesson_id}*_Quiz.html"))
        if not quiz_glob:
            quiz_glob = glob.glob(os.path.join(unit_path, f"Lesson {lesson_id}_Quiz.html"))
        
        for fpath in quiz_glob:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for placeholder quiz (States of Matter questions or generic placeholders)
            is_placeholder = ('state of matter' in content.lower() or 
                            'states of matter' in content.lower() or
                            'particles move most freely' in content.lower() or
                            'definite shape and volume' in content.lower() or
                            'Question 1 Placeholder' in content or
                            'Placeholder' in content)
            
            if is_placeholder:
                new_quiz = make_quiz_html(data)
                # Replace all quiz-question divs within the form
                pattern = r'(<form id="quiz-form">)\s*.*?\s*(</form>)'
                replacement = f'\\1\n\n{new_quiz}\n            \n\\2'
                new_content, n = re.subn(pattern, replacement, content, count=1, flags=re.DOTALL)
                if n > 0:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    changes += n
                    files_modified += 1
                    print(f"  [QUIZ] Updated: {os.path.basename(fpath)}")
                else:
                    print(f"  [WARN] Quiz pattern not matched: {os.path.basename(fpath)}")
            else:
                print(f"  [SKIP] Quiz already has real content: {os.path.basename(fpath)}")
    
    # ── PRACTICE (Flashcards) ──
    if not data.get("skip_practice"):
        practice_glob = glob.glob(os.path.join(unit_path, f"Lesson {lesson_id}*_Practice.html"))
        if not practice_glob:
            practice_glob = glob.glob(os.path.join(unit_path, f"Lesson {lesson_id}_Practice.html"))
        
        for fpath in practice_glob:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for placeholder flashcards
            is_placeholder = ('state of matter' in content.lower() and 
                            'definite shape' in content.lower()) or \
                           ('tightly packed' in content.lower()) or \
                           ('move most freely' in content.lower()) or \
                           ('vibrate in fixed' in content.lower())
            
            if is_placeholder:
                new_flashcards = make_flashcards_js(data)
                # Replace the flashcards array
                pattern = r'window\.lessonFlashcards\s*=\s*\[.*?\];'
                replacement = new_flashcards.strip()
                new_content, n = re.subn(pattern, replacement, content, count=1, flags=re.DOTALL)
                if n > 0:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    changes += n
                    files_modified += 1
                    print(f"  [PRACTICE] Updated: {os.path.basename(fpath)}")
                else:
                    print(f"  [WARN] Practice pattern not matched: {os.path.basename(fpath)}")
            else:
                print(f"  [SKIP] Practice already has real content: {os.path.basename(fpath)}")

print(f"\n{'='*60}")
print(f"Units 1-4 complete: {files_modified} files modified, {changes} changes")
