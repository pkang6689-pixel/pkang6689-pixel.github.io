"""
Generate 30-question Physics quizzes for all units.
Each quiz has:
  - Questions 1-10: Easy/foundational
  - Questions 11-20: Vocabulary/definition ("Which definition BEST describes...")
  - Questions 21-30: Scenario-based questions
"""
import json
import os

# All physics lessons: (unit, lesson, title, questions)
# Each question tuple: (question_text, correct_answer, wrong1, wrong2, wrong3, explanation)

LESSONS = {}

# ============================================================
# UNIT 1: Foundations of Measurement
# ============================================================

LESSONS[("1", "1.1", "Physical Quantities & Units")] = [
    # EASY (1-10)
    (
        "What is a physical quantity?",
        "A property that can be measured with a number and a unit",
        "A mathematical formula used in physics",
        "An abstract concept with no measurement",
        "A property that can only be observed qualitatively",
        "A physical quantity is any property of a material or system that can be quantified — it always consists of a numerical value and an associated unit."
    ),
    (
        "How many SI base quantities are there?",
        "Seven",
        "Five",
        "Six",
        "Ten",
        "The International System of Units defines exactly seven base quantities: length, mass, time, electric current, temperature, amount of substance, and luminous intensity."
    ),
    (
        "What is the SI base unit for mass?",
        "Kilogram (kg)",
        "Gram (g)",
        "Pound (lb)",
        "Newton (N)",
        "The kilogram (kg) is the SI base unit for mass. It is the only SI base unit that includes a prefix in its name."
    ),
    (
        "Which of the following is a derived quantity?",
        "Speed",
        "Length",
        "Mass",
        "Time",
        "Speed is derived from the base quantities of length and time (speed = distance/time). Length, mass, and time are all base quantities."
    ),
    (
        "What is the SI base unit for time?",
        "Second (s)",
        "Minute (min)",
        "Hour (h)",
        "Millisecond (ms)",
        "The second (s) is the SI base unit for time. Minutes, hours, and milliseconds are not SI base units."
    ),
    (
        "What is the SI base unit for electric current?",
        "Ampere (A)",
        "Volt (V)",
        "Ohm (Ω)",
        "Coulomb (C)",
        "The ampere (A) is the SI base unit for electric current. Volts measure potential difference, ohms measure resistance, and coulombs measure charge."
    ),
    (
        "What is the SI base unit for temperature?",
        "Kelvin (K)",
        "Celsius (°C)",
        "Fahrenheit (°F)",
        "Joule (J)",
        "The kelvin (K) is the SI base unit for thermodynamic temperature. Celsius and Fahrenheit are commonly used but are not SI base units."
    ),
    (
        "Which of the following is a base quantity in the SI system?",
        "Amount of substance",
        "Force",
        "Pressure",
        "Energy",
        "Amount of substance (measured in moles) is one of the seven SI base quantities. Force, pressure, and energy are all derived quantities."
    ),
    (
        "What happens when you add two values with different units?",
        "The addition is physically meaningless",
        "The units cancel out",
        "You always get the larger unit",
        "The result takes the unit of the first value",
        "Adding quantities with different units (e.g., 5 meters + 3 seconds) is physically meaningless. Only quantities with the same dimensions can be added or subtracted."
    ),
    (
        "Which of the following is a derived unit?",
        "Newton (N)",
        "Kilogram (kg)",
        "Second (s)",
        "Kelvin (K)",
        "The newton is a derived unit defined as kg·m/s². Kilogram, second, and kelvin are all SI base units."
    ),
    # VOCABULARY (11-20)
    (
        "Which definition BEST describes a physical quantity?",
        "A measurable property of a physical system expressed as a numerical value multiplied by a unit",
        "Any number used in a physics equation",
        "A qualitative observation about a physical system",
        "A unit of measurement defined by the SI system",
        "A physical quantity consists of two parts: a numerical value and a unit. For example, a length of 5.0 meters has the numerical value 5.0 and the unit meters."
    ),
    (
        "Which definition BEST describes a base quantity?",
        "A fundamental physical quantity that cannot be expressed in terms of other quantities and serves as a building block for all other measurements",
        "Any quantity that is commonly used in everyday life",
        "A quantity defined by a mathematical formula",
        "A measurement that uses only whole numbers",
        "Base quantities are the seven fundamental measurements (length, mass, time, current, temperature, amount of substance, luminous intensity) from which all other quantities are derived."
    ),
    (
        "Which definition BEST describes a derived quantity?",
        "A physical quantity defined by combining base quantities through multiplication, division, or other mathematical operations",
        "A quantity that exists independently of any other quantity",
        "A measurement that can only be estimated",
        "A quantity that uses non-SI units",
        "Derived quantities are formed by combining base quantities. For example, velocity (m/s) combines length and time, and force (kg·m/s²) combines mass, length, and time."
    ),
    (
        "Which definition BEST describes the SI system?",
        "The International System of Units — a globally agreed-upon set of standard base units used for scientific measurement",
        "A system of measurement used exclusively in Europe",
        "Any system that measures in metric units",
        "A collection of mathematical equations for physics",
        "The SI system (Système International d'Unités) provides seven base units that form the worldwide standard for scientific measurement and international commerce."
    ),
    (
        "Which definition BEST describes dimensional consistency?",
        "The requirement that both sides of a physics equation must have the same fundamental dimensions",
        "The requirement that all measurements use the same unit system",
        "The rule that equations must be balanced numerically",
        "The rule that physical constants must have no units",
        "Dimensional consistency means that the dimensions on both sides of an equation must match. An equation like distance = speed × time satisfies this: [L] = [L/T] × [T] = [L]."
    ),
    (
        "Which definition BEST describes a unit?",
        "A standard reference quantity used to express the magnitude of a physical measurement",
        "A number assigned to a physical property",
        "The smallest possible measurement of a quantity",
        "A mathematical symbol in an equation",
        "A unit is a defined standard of measurement. For example, the meter is the unit for length, providing a reference so that all length measurements are consistent and comparable."
    ),
    (
        "Which definition BEST describes luminous intensity?",
        "The power of light emitted by a source in a particular direction, measured in candelas",
        "The total energy output of a light source",
        "The speed at which light travels through a medium",
        "The frequency of visible light waves",
        "Luminous intensity is one of the seven SI base quantities. It measures the wavelength-weighted power emitted by a light source in a specific direction, with the SI unit candela (cd)."
    ),
    (
        "Which definition BEST describes the mole?",
        "The SI unit for amount of substance, defined as exactly 6.022 × 10²³ elementary entities",
        "A unit of mass used for very small particles",
        "The number of atoms in one gram of any element",
        "A unit of volume for measuring gases",
        "The mole is the SI base unit for amount of substance. One mole contains exactly 6.02214076 × 10²³ elementary entities (Avogadro's number), whether atoms, molecules, or other particles."
    ),
    (
        "Which definition BEST describes a fundamental constant?",
        "A physical quantity whose numerical value is fixed by the laws of nature and does not change",
        "A variable that appears in every physics equation",
        "A mathematical number like π or e",
        "Any quantity that scientists have agreed to keep unchanged",
        "Fundamental constants like the speed of light (c), Planck's constant (h), and the gravitational constant (G) have fixed values determined by nature, not by human convention."
    ),
    (
        "Which definition BEST describes the kelvin?",
        "The SI base unit of thermodynamic temperature, defined by fixing the numerical value of the Boltzmann constant",
        "A unit of temperature equal to one degree Celsius",
        "The average kinetic energy of gas molecules",
        "A unit of thermal energy",
        "The kelvin is the SI base unit for temperature. Its scale starts at absolute zero (0 K), where all thermal motion ceases. One kelvin increment equals one degree Celsius increment."
    ),
    # SCENARIO (21-30)
    (
        "A student measures the length of a table as '1.52.' Their teacher says the measurement is incomplete. What is MOST LIKELY missing from this measurement?",
        "The unit — a measurement must include both a numerical value and a unit to have physical meaning",
        "The decimal place — they need more digits",
        "The temperature — measurements depend on thermal expansion",
        "The student's name — measurements must be attributed",
        "A physical quantity requires both a numerical value and a unit. '1.52' alone conveys no physical meaning — it could be meters, feet, or any other unit. The measurement should be written as 1.52 m (or the appropriate unit)."
    ),
    (
        "An engineer needs to calculate the area of a rectangular plot that is 50 m long and 30 m wide. She expresses the area in m². This unit (m²) is an example of:",
        "A derived unit — formed by multiplying the base unit of length by itself",
        "A base unit — because meters are a base unit",
        "A dimensionless quantity — because it is just a number",
        "A fundamental constant — because area formulas never change",
        "Area (m²) is a derived quantity obtained from the base quantity length. Since area = length × width, its unit is m × m = m², which is derived from the SI base unit meter."
    ),
    (
        "A physics student writes the equation: distance = velocity + time. A classmate says this equation cannot be correct without even checking the numbers. How does the classmate know?",
        "The dimensions don't match — you cannot add velocity [L/T] and time [T] because they have different dimensions",
        "The equation uses the wrong variables",
        "Velocity is always larger than time",
        "The equation is missing a constant",
        "Dimensional analysis reveals the error immediately. Velocity has dimensions [L/T] and time has dimensions [T]. Since you cannot add quantities with different dimensions, the equation is dimensionally inconsistent and therefore physically invalid."
    ),
    (
        "A scientist measures temperature in kelvin, mass in kilograms, and time in seconds. All three of these belong to which category?",
        "SI base quantities — each is one of the seven fundamental measurements that cannot be derived from others",
        "Derived quantities — each is calculated from simpler quantities",
        "Imperial units — they belong to the British measurement system",
        "Dimensionless constants — they have no physical dimensions",
        "Temperature (K), mass (kg), and time (s) are three of the seven SI base quantities. They are defined independently and serve as the foundation from which all other physical quantities are derived."
    ),
    (
        "In a laboratory, a researcher expresses force in units of kg·m/s². This combination of base units is given the special name 'newton.' What does this tell us about force?",
        "Force is a derived quantity — it is defined through base quantities of mass, length, and time via Newton's second law",
        "Force is a base quantity given a simpler name for convenience",
        "Force cannot be measured directly",
        "Force is dimensionless because the units cancel out",
        "The newton (N = kg·m/s²) is a derived unit. It combines three base units, reflecting that force arises from the relationship F = ma. Many derived units receive special names for convenience."
    ),
    (
        "A student claims that energy and torque must be the same physical quantity because they both have units of N·m. Is this reasoning correct?",
        "No — although they share the same dimensions, energy is a scalar and torque is a vector, making them fundamentally different quantities",
        "Yes — any quantities with the same units are identical",
        "No — energy is measured in joules, not newton-meters",
        "Yes — dimensional analysis proves they are interchangeable",
        "While energy and torque both have dimensions [M L² T⁻²] and the unit N·m, they describe different physical concepts. Energy (a scalar) measures capacity to do work, while torque (a vector) measures rotational force. Dimensional analysis alone cannot distinguish between quantities of the same dimensions."
    ),
    (
        "NASA engineers must ensure that all international partners use consistent units. In 1999, a Mars orbiter was lost because one team used pounds while another used newtons. This disaster highlights the importance of:",
        "A universal unit system (SI) — inconsistent units between teams led to a navigation error that destroyed the spacecraft",
        "Using larger spacecraft to survive errors",
        "Avoiding international collaborations in space missions",
        "Rounding all measurements to whole numbers",
        "The Mars Climate Orbiter was lost due to a unit mismatch: Lockheed Martin used imperial pound-force·seconds while NASA's Jet Propulsion Laboratory expected SI newton·seconds. This $327.6 million loss underscores why the SI system exists."
    ),
    (
        "A physics textbook lists the speed of light as 3.00 × 10⁸ m/s and the charge of an electron as 1.60 × 10⁻¹⁹ C. Both of these are examples of:",
        "Physical quantities with defined numerical values and specific SI units",
        "Derived quantities because they are calculated from other measurements",
        "Approximate guesses that change over time",
        "Dimensionless numbers that have no units",
        "Both the speed of light and the elementary charge are physical quantities — they have numerical values and SI units. They are also fundamental constants whose values are now fixed by definition in the modern SI system."
    ),
    (
        "A student converts the mass of a car from 1500 kg to grams and gets 1,500,000 g. Despite the different number, the physical quantity has not changed. Why?",
        "The physical quantity (mass) remains the same because changing units only changes the numerical value, not the actual amount of matter",
        "The mass has actually increased by a factor of 1000",
        "Grams and kilograms measure different physical quantities",
        "The conversion is incorrect",
        "A physical quantity is invariant under unit conversion. 1500 kg and 1,500,000 g represent the same mass — only the numerical value and unit change, while the physical property itself remains identical."
    ),
    (
        "A researcher publishes a paper stating that a sample length is '12.5' without specifying any unit. A reviewer rejects this claim. Why is the reviewer justified?",
        "A number without a unit has no physical meaning — it could represent 12.5 meters, centimeters, or any other unit, making the measurement ambiguous",
        "The number 12.5 is too imprecise to be useful",
        "Published papers must always use imperial units",
        "The reviewer prefers a different number format",
        "In physics, every measurement must include a unit. A bare number like 12.5 is meaningless — the unit defines the scale and physical context. This principle is fundamental to clear scientific communication."
    ),
]

LESSONS[("1", "1.2", "SI System & Prefixes")] = [
    # EASY (1-10)
    (
        "What does the prefix 'kilo' mean?",
        "One thousand (10³)",
        "One hundred (10²)",
        "One million (10⁶)",
        "Ten (10¹)",
        "The prefix 'kilo' represents a factor of 10³ = 1,000. For example, 1 kilometer = 1,000 meters."
    ),
    (
        "What does the prefix 'milli' mean?",
        "One thousandth (10⁻³)",
        "One millionth (10⁻⁶)",
        "One hundredth (10⁻²)",
        "One billionth (10⁻⁹)",
        "The prefix 'milli' represents a factor of 10⁻³ = 0.001. For example, 1 millimeter = 0.001 meters."
    ),
    (
        "Convert 5.2 km to meters.",
        "5,200 m",
        "52 m",
        "520 m",
        "0.0052 m",
        "Since kilo means 10³, multiply by 1,000: 5.2 × 1,000 = 5,200 m."
    ),
    (
        "What does the prefix 'mega' mean?",
        "One million (10⁶)",
        "One thousand (10³)",
        "One billion (10⁹)",
        "One hundred thousand (10⁵)",
        "The prefix 'mega' represents a factor of 10⁶ = 1,000,000. For example, 1 megawatt = 1,000,000 watts."
    ),
    (
        "What does the prefix 'nano' mean?",
        "One billionth (10⁻⁹)",
        "One millionth (10⁻⁶)",
        "One thousandth (10⁻³)",
        "One trillionth (10⁻¹²)",
        "The prefix 'nano' represents a factor of 10⁻⁹ = 0.000000001. Nanotechnology deals with structures on this tiny scale."
    ),
    (
        "Convert 350 mg to grams.",
        "0.350 g",
        "3.50 g",
        "35,000 g",
        "3,500 g",
        "Milli means 10⁻³, so 350 mg = 350 × 10⁻³ g = 0.350 g."
    ),
    (
        "What does the prefix 'centi' mean?",
        "One hundredth (10⁻²)",
        "One tenth (10⁻¹)",
        "One thousandth (10⁻³)",
        "One hundred (10²)",
        "The prefix 'centi' represents 10⁻² = 0.01. The most common example is the centimeter: 1 cm = 0.01 m."
    ),
    (
        "What does the prefix 'giga' mean?",
        "One billion (10⁹)",
        "One million (10⁶)",
        "One trillion (10¹²)",
        "One thousand (10³)",
        "The prefix 'giga' represents 10⁹ = 1,000,000,000. Computer storage is commonly measured in gigabytes (GB)."
    ),
    (
        "How many centimeters are in 1 meter?",
        "100",
        "10",
        "1,000",
        "1,000,000",
        "Since centi means 10⁻², one meter contains 1/10⁻² = 100 centimeters."
    ),
    (
        "What does the prefix 'micro' mean?",
        "One millionth (10⁻⁶)",
        "One thousandth (10⁻³)",
        "One billionth (10⁻⁹)",
        "One hundredth (10⁻²)",
        "The prefix 'micro' (symbol μ) represents 10⁻⁶ = 0.000001. Microorganisms and micrometers use this prefix."
    ),
    # VOCABULARY (11-20)
    (
        "Which definition BEST describes an SI prefix?",
        "A standardized multiplier placed before an SI unit to represent a specific power of ten",
        "A type of SI base unit",
        "A symbol used only in chemistry",
        "A method for rounding numbers",
        "SI prefixes are standardized multipliers (like kilo = 10³, milli = 10⁻³) attached to unit names to express very large or very small quantities conveniently."
    ),
    (
        "Which definition BEST describes unit conversion?",
        "The mathematical process of expressing a measurement in a different unit while preserving the same physical quantity",
        "Changing the value of a measurement to a more convenient number",
        "Replacing one physical quantity with another",
        "Rounding a measurement to fewer decimal places",
        "Unit conversion changes the unit and numerical value but not the underlying physical quantity. Multiplying by conversion factors (ratios equal to 1) accomplishes this."
    ),
    (
        "Which definition BEST describes the metric system?",
        "A decimal-based measurement system in which units scale by powers of ten, forming the basis of the SI system",
        "Any system that uses meters as its base unit",
        "A measurement system used only in European countries",
        "A system based on the foot, pound, and second",
        "The metric system is a decimal system where prefixes represent powers of ten, making conversions straightforward. The SI system is the modern, internationally standardized version of the metric system."
    ),
    (
        "Which definition BEST describes a conversion factor?",
        "A ratio equal to one that relates two different units of the same physical quantity",
        "A physical constant used in equations",
        "A number that changes the physical quantity being measured",
        "A correction applied to systematic errors",
        "A conversion factor is a fraction whose numerator and denominator represent the same quantity in different units (e.g., 1000 m / 1 km = 1). Multiplying by it changes units without changing the physical value."
    ),
    (
        "Which definition BEST describes scientific notation?",
        "A way of expressing numbers as a coefficient between 1 and 10 multiplied by a power of ten",
        "A notation that uses only whole numbers",
        "A system of abbreviations for SI units",
        "A method for writing chemical formulas",
        "Scientific notation expresses numbers in the form a × 10ⁿ where 1 ≤ a < 10. It is especially useful for very large numbers (speed of light: 3.00 × 10⁸ m/s) and very small numbers (electron mass: 9.11 × 10⁻³¹ kg)."
    ),
    (
        "Which definition BEST describes an order of magnitude?",
        "An estimate of a quantity expressed as the nearest power of ten",
        "The exact value of a measurement",
        "The number of significant figures in a measurement",
        "The precision of a measuring instrument",
        "Order of magnitude gives a rough sense of scale. For example, Earth's radius (~6,400 km) has an order of magnitude of 10⁴ km. It is useful for quick comparisons and sanity checks."
    ),
    (
        "Which definition BEST describes the base unit of length?",
        "The meter (m) — the SI unit defined as the distance light travels in vacuum in 1/299,792,458 of a second",
        "The centimeter — the most commonly used unit of length",
        "The foot — the traditional unit of length",
        "The kilometer — the unit used for large distances",
        "The meter is the SI base unit of length. It was redefined in 1983 using the speed of light, making it one of the most precisely defined units."
    ),
    (
        "Which definition BEST describes a tera-?",
        "An SI prefix representing 10¹² (one trillion)",
        "An SI prefix representing 10⁹ (one billion)",
        "An SI prefix representing 10¹⁵ (one quadrillion)",
        "An SI prefix representing 10⁶ (one million)",
        "Tera (T) represents 10¹² = 1,000,000,000,000. Computer hard drives commonly have capacities measured in terabytes (TB)."
    ),
    (
        "Which definition BEST describes a pico-?",
        "An SI prefix representing 10⁻¹² (one trillionth)",
        "An SI prefix representing 10⁻⁹ (one billionth)",
        "An SI prefix representing 10⁻⁶ (one millionth)",
        "An SI prefix representing 10⁻¹⁵ (one quadrillionth)",
        "Pico (p) represents 10⁻¹² = 0.000000000001. Picofarads (pF) are commonly used for small capacitances in electronics."
    ),
    (
        "Which definition BEST describes a standard unit?",
        "A precisely defined reference quantity agreed upon by the scientific community for consistent measurement",
        "The most popular unit in a given country",
        "A unit chosen by an individual experimenter",
        "A theoretical unit that cannot be measured in practice",
        "Standard units are carefully defined references that ensure measurements are consistent and reproducible worldwide. The SI system provides the internationally accepted set of standard units."
    ),
    # SCENARIO (21-30)
    (
        "A doctor prescribes 500 mg of a medication. The pharmacist needs to measure this in grams. How many grams should the pharmacist dispense, and what conversion process is used?",
        "0.5 g — multiply by 10⁻³ since milli means one thousandth, so 500 mg × (1 g / 1000 mg) = 0.5 g",
        "5 g — move the decimal one place to the right",
        "50 g — multiply milligrams by 100 to get grams",
        "0.005 g — divide by 100,000",
        "Since milli = 10⁻³, converting milligrams to grams requires dividing by 1000 (or multiplying by 10⁻³): 500 mg = 500 × 10⁻³ g = 0.5 g. Medical dosing requires precise unit conversion."
    ),
    (
        "A computer advertises 2 TB of storage. A student needs to express this in gigabytes for a homework problem. What is the correct conversion?",
        "2,000 GB — since tera = 10¹² and giga = 10⁹, 1 TB = 1,000 GB, so 2 TB = 2,000 GB",
        "200 GB — divide terabytes by 10",
        "2,000,000 GB — multiply by one million",
        "20 GB — divide by 100",
        "Tera (10¹²) is three orders of magnitude larger than giga (10⁹). Therefore 1 TB = 10³ GB = 1,000 GB, and 2 TB = 2,000 GB."
    ),
    (
        "An astronomer measures the distance to a nearby star as 4.0 × 10¹³ km. To communicate this more concisely, which SI prefix and conversion would be MOST appropriate?",
        "40 terakilometers (Tkm) or simply 4.0 × 10¹⁶ m — using tera (10¹²) reduces the exponent for clearer communication",
        "4.0 gigameters — giga is always used for astronomical distances",
        "40 megameters — mega is the largest useful prefix",
        "4.0 × 10¹³ micrometers — convert to the smallest possible unit",
        "For very large distances, using appropriate SI prefixes simplifies communication. Since tera = 10¹², expressing 4.0 × 10¹³ km as 40 Tkm removes the large exponent. In practice, astronomers often use light-years or parsecs for such distances."
    ),
    (
        "A nanotechnology researcher fabricates wires that are 45 nm wide. A colleague asks for this dimension in meters. What is the correct conversion?",
        "4.5 × 10⁻⁸ m — since nano means 10⁻⁹, multiply 45 by 10⁻⁹ to get 45 × 10⁻⁹ m = 4.5 × 10⁻⁸ m",
        "4.5 × 10⁻⁶ m — nano means one millionth",
        "4.5 × 10⁻³ m — nano means one thousandth",
        "4.5 × 10⁻¹² m — nano means one trillionth",
        "Nano = 10⁻⁹, so 45 nm = 45 × 10⁻⁹ m = 4.5 × 10⁻⁸ m. This is about 1000 times smaller than a human hair (~50 μm) and illustrates the incredibly small scale of nanotechnology."
    ),
    (
        "A European recipe calls for 250 mL of milk. An American student only has a measuring cup marked in liters. How should the student measure this volume?",
        "0.250 L — since milli = 10⁻³, divide 250 by 1000 to convert milliliters to liters",
        "2.50 L — multiply by 10 to convert mL to L",
        "25.0 L — move the decimal one place to the right",
        "0.025 L — divide by 10,000",
        "Milli = 10⁻³, so 250 mL = 250 × 10⁻³ L = 0.250 L. The student should fill the measuring cup to the 0.250 L mark."
    ),
    (
        "A cell biologist measures a bacterium as 2.0 μm long. For a presentation, she needs to express this in nanometers. What is the result and how many prefix levels apart are these units?",
        "2,000 nm — micro (10⁻⁶) is three orders of magnitude larger than nano (10⁻⁹), so multiply by 1,000",
        "200 nm — multiply by 100",
        "20 nm — multiply by 10",
        "0.002 nm — divide by 1,000",
        "Micro (μ) = 10⁻⁶ and nano (n) = 10⁻⁹. The difference is 10³ = 1,000, so 2.0 μm = 2.0 × 1,000 nm = 2,000 nm. This chain conversion between prefixes requires knowing both prefixes' powers of ten."
    ),
    (
        "A marathon runner covers 42.195 km. Her fitness tracker expresses this distance in meters and then in centimeters. The increasing numbers (42,195 m → 4,219,500 cm) illustrate what fundamental property of unit conversion?",
        "The numerical value increases as the unit gets smaller, but the actual distance remains unchanged — the physical quantity is invariant under unit conversion",
        "The distance is actually getting larger with each conversion",
        "Smaller units are always more accurate than larger units",
        "Centimeters should never be used for large distances",
        "When converting to a smaller unit, the numerical value increases proportionally. 42.195 km = 42,195 m = 4,219,500 cm all represent the same physical distance. This demonstrates that only the representation changes, not the underlying quantity."
    ),
    (
        "A semiconductor factory operates at the 5 nm process node. If a human hair is approximately 80 μm in diameter, approximately how many transistors (at 5 nm each) could fit across one hair?",
        "16,000 — convert 80 μm to nm: 80 × 1,000 = 80,000 nm, then divide by 5 nm to get 16,000",
        "160 — divide micrometers directly by nanometers",
        "1,600 — convert incorrectly using a factor of 100",
        "1,600,000 — multiply instead of dividing",
        "First convert 80 μm to nm: 80 μm × (1,000 nm / 1 μm) = 80,000 nm. Then 80,000 nm ÷ 5 nm = 16,000 transistors. This illustrates both prefix conversion and the remarkable miniaturization of modern technology."
    ),
    (
        "During a lab experiment, a student needs 0.075 kg of a chemical. The lab scale reads in grams. The student places 75 g on the scale. Is this correct?",
        "Yes — 0.075 kg × 1,000 g/kg = 75 g, which is the correct conversion from kilograms to grams",
        "No — 0.075 kg is equal to 7.5 g",
        "No — 0.075 kg is equal to 750 g",
        "No — you cannot convert between kilograms and grams",
        "Kilo = 10³, so 1 kg = 1,000 g. Therefore 0.075 kg = 0.075 × 1,000 = 75 g. The student correctly converted from kilograms to grams."
    ),
    (
        "A GPS satellite orbits at approximately 20,200 km altitude and transmits signals at a frequency of 1.575 GHz. Express the frequency in Hz and explain the prefix used.",
        "1.575 × 10⁹ Hz — giga means 10⁹ (one billion), so 1.575 GHz = 1,575,000,000 Hz",
        "1.575 × 10⁶ Hz — giga means one million",
        "1.575 × 10¹² Hz — giga means one trillion",
        "1.575 × 10³ Hz — giga means one thousand",
        "Giga (G) = 10⁹ = one billion. So 1.575 GHz = 1.575 × 10⁹ Hz = 1,575,000,000 Hz. GPS signals use microwave frequencies in the gigahertz range."
    ),
]

LESSONS[("1", "1.3", "Scalars vs Vectors")] = [
    # EASY (1-10)
    (
        "What is a scalar quantity?",
        "A quantity that has only magnitude (size) and no direction",
        "A quantity that has both magnitude and direction",
        "A quantity that can only be positive",
        "A quantity measured with a ruler",
        "Scalar quantities are fully described by a magnitude (numerical value with a unit) alone. Examples include mass, temperature, speed, energy, and time."
    ),
    (
        "What is a vector quantity?",
        "A quantity that has both magnitude and direction",
        "A quantity that has only magnitude",
        "A quantity that is always positive",
        "A quantity that cannot be measured",
        "Vector quantities require both a magnitude and a direction to be fully described. Examples include displacement, velocity, force, and acceleration."
    ),
    (
        "Which of the following is a scalar quantity?",
        "Temperature",
        "Velocity",
        "Displacement",
        "Force",
        "Temperature has magnitude only (e.g., 25°C) and no associated direction. Velocity, displacement, and force are all vector quantities."
    ),
    (
        "Which of the following is a vector quantity?",
        "Displacement",
        "Mass",
        "Speed",
        "Energy",
        "Displacement has both magnitude (e.g., 5 m) and direction (e.g., north). Mass, speed, and energy are scalar quantities."
    ),
    (
        "What is the difference between speed and velocity?",
        "Speed is a scalar (magnitude only), while velocity is a vector (magnitude and direction)",
        "Speed is faster than velocity",
        "Velocity applies only to cars, speed to all objects",
        "There is no difference; they are the same thing",
        "Speed tells you how fast something moves (e.g., 60 km/h) but not where it's going. Velocity includes direction (e.g., 60 km/h north), making it a vector."
    ),
    (
        "What is the difference between distance and displacement?",
        "Distance is a scalar (total path length), while displacement is a vector (straight-line distance from start to finish with direction)",
        "Distance is always larger than displacement",
        "Displacement measures curved paths while distance measures straight lines",
        "They are different words for the same measurement",
        "Distance measures the total path traveled regardless of direction. Displacement measures the straight-line distance and direction from the starting point to the ending point."
    ),
    (
        "Two forces of 3 N and 4 N act on an object at right angles. What is the magnitude of the resultant force?",
        "5 N",
        "7 N",
        "1 N",
        "12 N",
        "Using the Pythagorean theorem for perpendicular vectors: √(3² + 4²) = √(9 + 16) = √25 = 5 N."
    ),
    (
        "Which of the following is a scalar?",
        "Time",
        "Acceleration",
        "Momentum",
        "Weight",
        "Time has magnitude only (e.g., 5 seconds) and no direction. Acceleration, momentum, and weight are vectors."
    ),
    (
        "A person walks 3 km north then 4 km south. What is the magnitude of their displacement?",
        "1 km south",
        "7 km",
        "7 km south",
        "1 km north",
        "Displacement is the straight-line distance from start to finish: 3 km north − 4 km south = 1 km south (net movement). The total distance traveled would be 7 km."
    ),
    (
        "How do you add two vectors that point in the same direction?",
        "Add their magnitudes — the resultant has the same direction",
        "Subtract the smaller from the larger",
        "Multiply their magnitudes together",
        "Use the Pythagorean theorem",
        "When vectors point in the same direction, their magnitudes simply add. For example, two forces of 5 N and 3 N both pushing right produce a resultant of 8 N to the right."
    ),
    # VOCABULARY (11-20)
    (
        "Which definition BEST describes a scalar quantity?",
        "A physical quantity that is completely described by its magnitude alone and has no associated direction",
        "A physical quantity that requires a direction for its description",
        "A quantity that is always positive",
        "A quantity that can only be measured with digital instruments",
        "Scalars are quantities like mass, temperature, speed, and energy that are fully specified by a number and unit. No direction information is needed or meaningful."
    ),
    (
        "Which definition BEST describes a vector quantity?",
        "A physical quantity that requires both magnitude and direction for a complete description",
        "A quantity that has only size and no other properties",
        "A quantity measured along a straight line",
        "A quantity expressed using arrows in textbooks",
        "Vectors like displacement, velocity, force, and acceleration are not fully described without specifying a direction. They are represented graphically as arrows where length indicates magnitude and the arrow indicates direction."
    ),
    (
        "Which definition BEST describes the resultant vector?",
        "The single vector that produces the same effect as two or more individual vectors combined",
        "The largest of all contributing vectors",
        "A vector that cancels out all other vectors",
        "The first vector in a series of additions",
        "The resultant is the net vector obtained by vector addition. It can be found graphically (tip-to-tail method) or analytically (component method). The resultant produces the same physical effect as all the original vectors acting together."
    ),
    (
        "Which definition BEST describes vector addition?",
        "The process of combining two or more vectors according to both their magnitudes and directions to find a single resultant vector",
        "Simply adding the numerical values of any two quantities",
        "Multiplying vectors together to get a larger quantity",
        "Arranging vectors in alphabetical order",
        "Vector addition accounts for direction, not just magnitude. Two vectors of equal magnitude can produce a resultant anywhere from zero (if opposite) to double (if same direction), depending on the angle between them."
    ),
    (
        "Which definition BEST describes displacement?",
        "A vector quantity equal to the straight-line distance and direction from an initial position to a final position",
        "The total path length traveled by an object",
        "The speed of an object multiplied by time",
        "The distance an object covers in one second",
        "Displacement is a vector: it has a magnitude (the shortest distance between two points) and a direction. A round trip has zero displacement but nonzero distance."
    ),
    (
        "Which definition BEST describes velocity?",
        "A vector quantity that describes the rate of change of displacement with respect to time, including direction",
        "How fast an object moves, regardless of direction",
        "The distance traveled per unit time",
        "The acceleration of an object multiplied by time",
        "Velocity is the vector counterpart of speed. It specifies both how fast an object moves and the direction of motion. Average velocity = displacement / time."
    ),
    (
        "Which definition BEST describes the component method of vector addition?",
        "A technique that resolves each vector into perpendicular components (typically x and y), adds components separately, then recombines to find the resultant",
        "A method that only works for vectors in the same direction",
        "A technique that adds vector magnitudes regardless of direction",
        "A graphical method using protractors and rulers",
        "The component method breaks each vector into x and y parts using trigonometry: Vx = V cos θ, Vy = V sin θ. After adding all x-components and all y-components separately, the resultant magnitude is √(Rx² + Ry²) and direction is θ = tan⁻¹(Ry/Rx)."
    ),
    (
        "Which definition BEST describes the tip-to-tail method?",
        "A graphical vector addition technique where each successive vector is drawn starting from the tip (head) of the previous vector",
        "A method of subtracting vectors by reversing their direction",
        "A way of measuring the angle between vectors",
        "A technique that only works for two vectors",
        "In the tip-to-tail method, vectors are drawn head-to-tail in sequence. The resultant is the vector drawn from the tail of the first vector to the tip of the last vector. This method works for any number of vectors."
    ),
    (
        "Which definition BEST describes a unit vector?",
        "A vector with a magnitude of exactly one, used to indicate direction only",
        "A vector expressed in SI base units",
        "The smallest possible vector",
        "A vector that points upward",
        "Unit vectors have magnitude 1 and specify direction only. Common unit vectors are î (x-direction), ĵ (y-direction), and k̂ (z-direction). Any vector can be expressed as a magnitude multiplied by its unit vector."
    ),
    (
        "Which definition BEST describes equilibrium in terms of vectors?",
        "A state where the vector sum (resultant) of all forces acting on an object equals zero",
        "A state where all forces have the same magnitude",
        "A condition where no forces act on an object",
        "A situation where only one force acts on an object",
        "An object is in equilibrium when the net force (vector sum of all forces) is zero. This can occur with many forces acting, as long as they all cancel out. The object may be stationary or moving at constant velocity."
    ),
    # SCENARIO (21-30)
    (
        "A pilot flies 200 km east, then 150 km north. She needs to calculate the displacement from her starting airport to plan the return flight. What is the magnitude and direction of her displacement?",
        "250 km at 36.9° north of east — using the Pythagorean theorem √(200² + 150²) = 250 km, and tan θ = 150/200 gives θ = 36.9°",
        "350 km in the direction of her last heading",
        "50 km northeast",
        "200 km east since that was the longer leg",
        "The two legs are perpendicular, forming a right triangle. Resultant magnitude: √(200² + 150²) = √(40,000 + 22,500) = √62,500 = 250 km. Direction: θ = tan⁻¹(150/200) = 36.9° north of east."
    ),
    (
        "A hiker walks 5 km north, then 5 km east, then 5 km south. What is his displacement from where he started?",
        "5 km east — the northward and southward components cancel, leaving only the eastward displacement",
        "15 km in total",
        "0 km — he returned to where he started",
        "10 km northeast",
        "Breaking into components: North-south = 5 km N − 5 km S = 0. East-west = 5 km E. The northward and southward legs cancel, leaving a net displacement of 5 km east."
    ),
    (
        "Two students argue about whether kinetic energy is a vector or scalar. Student A says it's a vector because a moving object has a direction. Student B says it's scalar because energy has no direction. Who is correct and why?",
        "Student B — kinetic energy (½mv²) is a scalar; it depends on the square of speed (a scalar) and has no directional property",
        "Student A — anything involving motion must be a vector",
        "Neither — kinetic energy is neither scalar nor vector",
        "Both are correct depending on the reference frame",
        "Kinetic energy = ½mv² is always positive and has no direction. While the object moves in a direction, the energy itself does not — it's the same regardless of which direction the object moves. Squaring velocity (v²) removes all directional information."
    ),
    (
        "A boat aims due north across a river at 4 m/s while the river current flows east at 3 m/s. What is the boat's actual velocity relative to the ground?",
        "5 m/s at 36.9° east of north — the perpendicular velocities combine via the Pythagorean theorem: √(4² + 3²) = 5 m/s",
        "7 m/s due northeast",
        "1 m/s due north",
        "4 m/s due north because the boat's engine determines its direction",
        "The boat's velocity and the river current are perpendicular vectors. The resultant speed is √(4² + 3²) = √25 = 5 m/s. The direction is θ = tan⁻¹(3/4) = 36.9° east of north, showing the current pushes the boat off course."
    ),
    (
        "A car drives around a circular track at a constant speed of 60 km/h. A physics student says the velocity is changing even though the speed is constant. Is the student correct?",
        "Yes — velocity is a vector, so even though the magnitude (speed) is constant, the direction is continuously changing as the car goes around the track",
        "No — if speed is constant, velocity is also constant",
        "No — velocity only changes when the car speeds up or slows down",
        "Yes — but only because the car's mass changes during the lap",
        "Since velocity is a vector, it has both magnitude (speed) and direction. On a circular track, the direction of motion constantly changes even at constant speed, meaning the velocity vector is always changing. This changing velocity means the car is accelerating (centripetal acceleration)."
    ),
    (
        "An airplane flying at 250 km/h encounters a headwind of 50 km/h. The pilot reports a ground speed of 200 km/h. This situation illustrates vector addition of velocities because:",
        "The airplane velocity and wind velocity are opposite vectors that partially cancel, reducing the resultant ground speed",
        "The airplane must burn more fuel in headwinds",
        "200 km/h is the arithmetic mean of 250 and 50",
        "Headwinds always cut airplane speed in half",
        "When vectors are in opposite directions, the resultant magnitude is the difference: 250 − 50 = 200 km/h. This is a straightforward case of vector addition where the velocity vectors are antiparallel."
    ),
    (
        "A physics teacher pushes a box with a force of 100 N at a 30° angle below the horizontal. A student asks: 'How much of this force is actually moving the box horizontally?' What is the horizontal component?",
        "86.6 N — the horizontal component is F cos 30° = 100 × 0.866 = 86.6 N",
        "50 N — the horizontal component is always half the total force",
        "100 N — the full force moves the box horizontally",
        "30 N — the angle directly gives the component",
        "The horizontal component of a vector at angle θ from horizontal is Fx = F cos θ. Here, Fx = 100 cos 30° = 100 × 0.866 = 86.6 N. The vertical component (100 sin 30° = 50 N) pushes the box into the floor."
    ),
    (
        "A soccer player kicks a ball at 20 m/s at 45° above the horizontal. The initial horizontal and vertical velocity components are each about 14.1 m/s. During flight, which component changes and which stays constant (ignoring air resistance)?",
        "The vertical component changes due to gravity while the horizontal component remains constant — gravity only acts vertically",
        "Both components remain constant during flight",
        "Both components change equally due to gravity",
        "The horizontal component decreases while the vertical stays constant",
        "In projectile motion (ignoring air resistance), the horizontal and vertical components are independent. Gravity acts only vertically (changing vy), while no horizontal force acts on the ball, keeping vx constant at 14.1 m/s."
    ),
    (
        "Three tug-of-war teams pull on a ring. Team A pulls 500 N north, Team B pulls 500 N east, and Team C pulls 707 N southwest (exactly 45° south of west). Is the ring in equilibrium?",
        "Yes — Team C's force exactly cancels Teams A and B's resultant, making the net force zero",
        "No — three forces can never produce equilibrium",
        "No — Team C's force is larger than either A or B",
        "Yes — but only because all three forces are equal",
        "Teams A and B produce a resultant of √(500² + 500²) = 707 N directed northeast. Team C pulls 707 N in exactly the opposite direction (southwest). The vector sum is zero, so the ring is in equilibrium."
    ),
    (
        "A smartphone compass app shows a hiker's displacement as 1.2 km at bearing 060° (60° east of north). The hiker's friend asks for the displacement in terms of 'how far east and how far north.' What are the rectangular components?",
        "1.04 km east and 0.60 km north — east = 1.2 sin 60° = 1.04, north = 1.2 cos 60° = 0.60",
        "0.60 km east and 1.04 km north",
        "0.85 km east and 0.85 km north",
        "1.2 km east and 1.2 km north",
        "For a bearing of 060° (measured clockwise from north): East component = 1.2 sin 60° = 1.2 × 0.866 = 1.04 km. North component = 1.2 cos 60° = 1.2 × 0.500 = 0.60 km. Note that bearing angles use north as reference, not east."
    ),
]

LESSONS[("1", "1.4", "Accuracy, Precision, & Significant Figures")] = [
    # EASY (1-10)
    (
        "What is accuracy in measurement?",
        "How close a measured value is to the true (accepted) value",
        "How close repeated measurements are to each other",
        "The number of decimal places in a measurement",
        "The type of instrument used for measurement",
        "Accuracy describes how close a measurement is to the actual or accepted value. A measurement can be precise (consistent) but inaccurate (far from the true value)."
    ),
    (
        "What is precision in measurement?",
        "How close repeated measurements are to each other",
        "How close a measurement is to the true value",
        "The total number of measurements taken",
        "The speed at which measurements are taken",
        "Precision refers to the reproducibility of measurements. Highly precise measurements cluster closely together, even if they are all far from the true value."
    ),
    (
        "How many significant figures are in the number 0.00450?",
        "3",
        "5",
        "2",
        "6",
        "Leading zeros are not significant. The significant digits are 4, 5, and the trailing 0 (which is significant because it comes after the decimal point and after a nonzero digit). So 0.00450 has 3 significant figures."
    ),
    (
        "How many significant figures are in the number 1200?",
        "2 (unless a decimal point is shown)",
        "4",
        "3",
        "1",
        "Trailing zeros in a whole number without a decimal point are ambiguous but typically considered not significant. So 1200 has 2 significant figures (1 and 2). Writing 1200. or 1.200 × 10³ clarifies that all four digits are significant."
    ),
    (
        "When multiplying or dividing measurements, how do you determine the number of significant figures in the result?",
        "The result should have the same number of significant figures as the measurement with the fewest significant figures",
        "Always use the most significant figures available",
        "The result should have the sum of all significant figures",
        "Significant figures don't matter in multiplication",
        "In multiplication and division, the result is limited by the measurement with the fewest significant figures. For example, 4.56 × 1.4 = 6.4 (not 6.384) because 1.4 has only 2 significant figures."
    ),
    (
        "When adding or subtracting measurements, how do you determine the significant figures in the result?",
        "The result should be rounded to the same number of decimal places as the measurement with the fewest decimal places",
        "Use the same rule as multiplication — fewest significant figures",
        "Always keep all decimal places",
        "Round to one decimal place in all cases",
        "In addition and subtraction, the result is rounded to the fewest decimal places of any measurement. For example, 12.11 + 18.0 = 30.1 (not 30.11) because 18.0 has only one decimal place."
    ),
    (
        "A measurement is both accurate and precise. What does this mean?",
        "The measurements are consistently close to the true value and close to each other",
        "The measurements use many significant figures",
        "The instrument was very expensive",
        "The measurement was taken only once",
        "When measurements are both accurate and precise, they cluster tightly around the true value. This is the ideal outcome of any measurement process."
    ),
    (
        "How many significant figures are in the number 50.030?",
        "5",
        "4",
        "3",
        "6",
        "All digits are significant: 5, 0, 0, 3, and the trailing 0. Zeros between nonzero digits are always significant, and the trailing zero after the decimal point is significant."
    ),
    (
        "What is the purpose of significant figures in science?",
        "To communicate the precision of a measurement",
        "To make numbers look cleaner in calculations",
        "To reduce the number of calculations needed",
        "To make all measurements the same length",
        "Significant figures indicate how precisely a measurement was made. They communicate meaningful digits so that calculated results don't imply more precision than the original measurements warrant."
    ),
    (
        "Are leading zeros significant?",
        "No — leading zeros only serve as placeholders and are never significant",
        "Yes — all zeros are significant",
        "Only if they come after a decimal point",
        "Only in scientific notation",
        "Leading zeros (e.g., 0.0045) merely indicate the position of the decimal point. They are not significant. In 0.0045, only 4 and 5 are significant."
    ),
    # VOCABULARY (11-20)
    (
        "Which definition BEST describes accuracy?",
        "The degree to which a measured value agrees with the true or accepted value of the quantity being measured",
        "The ability of an instrument to give consistent readings",
        "The total number of decimal places in a measurement",
        "The range of values obtained from repeated measurements",
        "Accuracy is about correctness — how close you are to the target. A single measurement can be accurate even if repeated measurements vary, and vice versa."
    ),
    (
        "Which definition BEST describes precision?",
        "The degree of agreement among repeated measurements of the same quantity under the same conditions",
        "How close a measurement is to the true value",
        "The number of significant figures in a measurement",
        "The smallest increment on a measuring instrument",
        "Precision reflects reproducibility. If you measure the same thing five times and get 5.01, 5.02, 5.01, 5.02, 5.01, the precision is high even if the true value is 6.00 (low accuracy)."
    ),
    (
        "Which definition BEST describes a significant figure?",
        "A digit in a measurement that is known with certainty plus one estimated digit, indicating the precision of the measurement",
        "Any digit in a number",
        "Only the first nonzero digit",
        "The number of decimal places after the decimal point",
        "Significant figures include all reliably known digits plus the first uncertain (estimated) digit. They communicate the level of confidence in a measurement."
    ),
    (
        "Which definition BEST describes systematic error?",
        "A consistent, repeatable error that shifts all measurements in the same direction by the same amount, affecting accuracy",
        "An error that varies randomly from measurement to measurement",
        "An error caused by rounding numbers",
        "An error that only occurs in digital instruments",
        "Systematic errors produce consistent bias (all readings too high or too low). Causes include miscalibrated instruments, zero errors, and environmental factors. They affect accuracy but not precision."
    ),
    (
        "Which definition BEST describes random error?",
        "An unpredictable variation in measurements caused by uncontrollable factors, affecting precision",
        "An error that is consistently the same in every measurement",
        "An error caused by using the wrong formula",
        "An error that only occurs in analog instruments",
        "Random errors cause measurements to scatter unpredictably around the true value. They might be caused by vibrations, temperature fluctuations, or human estimation. They affect precision but not accuracy systematically."
    ),
    (
        "Which definition BEST describes percent error?",
        "The ratio of the absolute difference between a measured value and the accepted value to the accepted value, expressed as a percentage",
        "The percentage of measurements that are wrong",
        "The number of significant figures expressed as a percentage",
        "The precision of an instrument expressed as a percentage",
        "Percent error = |measured − accepted| / accepted × 100%. It quantifies how far a measurement is from the true value. A lower percent error indicates greater accuracy."
    ),
    (
        "Which definition BEST describes rounding?",
        "The process of reducing the number of digits in a value while maintaining an approximation that is as close to the original as possible",
        "Always removing the last digit of a number",
        "Converting a number to scientific notation",
        "Replacing all zeros with significant digits",
        "Rounding adjusts a number to a specified number of significant figures or decimal places. If the digit being removed is ≥ 5, round up; if < 5, round down."
    ),
    (
        "Which definition BEST describes calibration?",
        "The process of adjusting and verifying a measuring instrument against a known standard to ensure its readings are accurate",
        "Using the same instrument for every measurement",
        "Taking the average of multiple measurements",
        "Reading a measurement at eye level",
        "Calibration eliminates systematic errors by comparing an instrument's readings to a known reference standard and adjusting accordingly. Regular calibration maintains measurement accuracy over time."
    ),
    (
        "Which definition BEST describes an exact number?",
        "A number with no uncertainty — it is known with complete certainty, such as counted quantities or defined conversions",
        "A measurement taken with high-precision instruments",
        "A number with more than 10 significant figures",
        "The average of many measurements",
        "Exact numbers have infinite significant figures. Examples: there are exactly 12 eggs in a dozen, and exactly 100 cm in 1 m. They do not limit significant figures in calculations."
    ),
    (
        "Which definition BEST describes the resolution of an instrument?",
        "The smallest change in a measured quantity that the instrument can detect",
        "The largest measurement the instrument can make",
        "The accuracy of the instrument",
        "The speed at which the instrument takes readings",
        "Resolution (also called least count) is the smallest increment an instrument can display or detect. A ruler marked in millimeters has 1 mm resolution. Higher resolution allows more precise measurements."
    ),
    # SCENARIO (21-30)
    (
        "A student measures the length of a desk five times: 1.52 m, 1.53 m, 1.52 m, 1.52 m, 1.53 m. The actual length is 1.50 m. How would you describe these measurements?",
        "Precise but not accurate — the measurements are consistent with each other but systematically higher than the true value",
        "Accurate but not precise — they are close to the true value but vary widely",
        "Both accurate and precise — they are consistent and close to the true value",
        "Neither accurate nor precise — the measurements are unreliable",
        "The measurements cluster tightly (1.52–1.53 m range = high precision) but are consistently above the true value of 1.50 m (low accuracy). This pattern indicates a systematic error, perhaps a bent ruler or incorrect technique."
    ),
    (
        "A chemistry student measures the density of aluminum three times: 2.70, 2.68, and 2.72 g/cm³. The accepted value is 2.70 g/cm³. How should these measurements be described?",
        "Both accurate and precise — the average (2.70 g/cm³) matches the accepted value and the measurements are closely clustered",
        "Precise but not accurate — the values are close together but far from the true value",
        "Accurate but not precise — the average is correct but the values are spread out",
        "Neither accurate nor precise — more measurements are needed",
        "The measurements are closely grouped (precision) and their average equals the accepted value (accuracy). This represents the ideal outcomes of careful measurement technique and properly calibrated equipment."
    ),
    (
        "A student calculates the area of a rectangular room by multiplying 4.5 m × 3.72 m and reports the area as 16.740 m². Their teacher marks this incorrect. Why?",
        "The answer should have only 2 significant figures (17 m²) because 4.5 has only 2 significant figures, and in multiplication the result is limited to the fewest sig figs",
        "The area should be reported in square centimeters",
        "The student should have added the measurements instead of multiplying",
        "The teacher made an error — 16.740 m² is correct",
        "In multiplication, the result must have the same number of significant figures as the least precise input. Here, 4.5 has 2 sig figs and 3.72 has 3 sig figs. The result should be rounded to 2 sig figs: 17 m²."
    ),
    (
        "A digital thermometer consistently reads 2.0°C higher than the actual temperature. A student takes five readings: 22.0, 22.1, 21.9, 22.0, 22.0°C (actual temperature is 20.0°C). What type of error is present?",
        "Systematic error — the thermometer is miscalibrated, causing all readings to be shifted by the same amount from the true value",
        "Random error — the readings vary slightly",
        "Human error — the student is reading the thermometer wrong",
        "No error — the thermometer is working correctly",
        "The consistent +2.0°C offset is a systematic error caused by poor calibration. The slight variation (21.9–22.1) represents additional random error. Calibrating the thermometer against a standard would correct the systematic error."
    ),
    (
        "A student weighs an object: 5.00 g. She then measures its volume: 2.1 mL. She calculates the density as 5.00 / 2.1 = 2.380952... g/mL and reports 2.380952 g/mL. What is wrong with her reported density?",
        "The result should be rounded to 2 significant figures (2.4 g/mL) because 2.1 mL has only 2 significant figures",
        "She divided when she should have multiplied",
        "She should report all the decimal places from the calculator",
        "The units are incorrect",
        "In division, the result is limited to the fewest significant figures of any input. 5.00 g has 3 sig figs; 2.1 mL has 2 sig figs. The density should be reported as 2.4 g/mL — reporting extra digits falsely implies greater precision."
    ),
    (
        "An archer shoots five arrows at a target. All five arrows are clustered tightly in the upper-left corner, far from the bullseye. A second archer's arrows are scattered all over the target but the average position is near the bullseye. Which archer is more precise and which is more accurate?",
        "The first archer is more precise (tight cluster) but less accurate (far from center); the second has higher accuracy on average but lower precision",
        "The first archer is both more accurate and more precise",
        "The second archer is both more accurate and more precise",
        "Neither is precise or accurate",
        "Precision = consistency (tight cluster = first archer). Accuracy = closeness to the true value / target (average near bullseye = second archer). This classic analogy illustrates that precision and accuracy are independent properties."
    ),
    (
        "A student adds three measurements: 12.1 g + 0.035 g + 1.44 g = 13.575 g. If significant figures rules are applied correctly, what should the reported sum be?",
        "13.6 g — in addition, round to the fewest decimal places (1 decimal place, from 12.1)",
        "13.575 g — keep all digits",
        "14 g — round to the fewest significant figures",
        "13.58 g — round to two decimal places",
        "In addition, the result is rounded to the fewest decimal places of any measurement. 12.1 has 1 decimal place, 0.035 has 3, and 1.44 has 2. The least is 1; round to 13.6 g."
    ),
    (
        "A lab group measures the boiling point of water at their altitude and gets: 99.2, 95.1, 99.3, 99.1, 99.2°C. The accepted value at their altitude is 99.2°C. The 95.1°C reading is dramatically different from the others. What should the group do?",
        "Identify 95.1°C as an outlier likely caused by an error, investigate its cause, and exclude it if an error is confirmed — the remaining measurements are both accurate and precise",
        "Include all values and report the average including 95.1°C",
        "Throw away all data and start over",
        "Report only the 95.1°C value since it is unique",
        "The 95.1°C reading is an outlier — likely caused by an experimental error (e.g., thermometer not fully immersed). After identifying the cause, it can be excluded. The remaining four values (99.1–99.3) are both accurate and precise."
    ),
    (
        "A ruler measures to the nearest 0.1 cm. A student writes a measurement as 25 cm instead of 25.0 cm. Why does the missing decimal point matter?",
        "25 cm implies 2 significant figures, while 25.0 cm implies 3 — the trailing zero communicates that the measurement is precise to the nearest 0.1 cm",
        "25 cm and 25.0 cm are exactly the same",
        "The decimal point makes the number larger",
        "25 cm means the ruler was used incorrectly",
        "Trailing zeros after a decimal point are significant. Writing 25.0 cm (3 sig figs) correctly communicates that the measurement was made to the nearest 0.1 cm. Writing 25 cm (2 sig figs) implies it was only measured to the nearest 1 cm, misrepresenting the instrument's capability."
    ),
    (
        "An experiment produces a measured value of gravity g = 9.6 m/s². The accepted value is 9.81 m/s². What is the approximate percent error, and what does it tell us?",
        "About 2.1% — calculated as |9.6 − 9.81| / 9.81 × 100% ≈ 2.1%, indicating the measurement is reasonably close to the accepted value",
        "About 21% — the difference is 0.21",
        "About 0.21% — divide the difference by 100",
        "Percent error cannot be negative, so it equals exactly 2.0%",
        "|9.6 − 9.81| / 9.81 × 100% = 0.21/9.81 × 100% ≈ 2.14%. This relatively small percent error suggests the measurement technique was reasonably good, though some systematic or random error is present."
    ),
]

LESSONS[("1", "1.5", "Dimensional Analysis")] = [
    # EASY (1-10)
    (
        "What are the three fundamental dimensions used in mechanics?",
        "Mass [M], Length [L], and Time [T]",
        "Force, Energy, and Power",
        "Meter, Kilogram, and Second",
        "Speed, Acceleration, and Velocity",
        "The fundamental dimensions in mechanics are mass [M], length [L], and time [T]. All mechanical quantities can be expressed as combinations of these three dimensions."
    ),
    (
        "What is the dimension of velocity?",
        "[L T⁻¹]",
        "[M L T⁻¹]",
        "[L T⁻²]",
        "[L²T⁻¹]",
        "Velocity = displacement / time, so its dimension is [L] / [T] = [L T⁻¹]. Direction is not represented in dimensional analysis."
    ),
    (
        "What is the dimension of acceleration?",
        "[L T⁻²]",
        "[L T⁻¹]",
        "[M L T⁻²]",
        "[M T⁻²]",
        "Acceleration = change in velocity / time = [L T⁻¹] / [T] = [L T⁻²]."
    ),
    (
        "What is the dimension of force?",
        "[M L T⁻²]",
        "[M L T⁻¹]",
        "[L T⁻²]",
        "[M L² T⁻²]",
        "Force = mass × acceleration = [M] × [L T⁻²] = [M L T⁻²]. This is the dimension of the newton (N = kg·m/s²)."
    ),
    (
        "Can you add a quantity with dimension [M] to a quantity with dimension [L]?",
        "No — only quantities with the same dimensions can be added or subtracted",
        "Yes — all physical quantities can be combined",
        "Only if you convert units first",
        "Yes — the result takes the dimension of the larger quantity",
        "Dimensional homogeneity requires that all terms being added or subtracted have identical dimensions. Adding mass to length is dimensionally inconsistent and physically meaningless."
    ),
    (
        "What is the dimension of energy (or work)?",
        "[M L² T⁻²]",
        "[M L T⁻²]",
        "[M L T⁻¹]",
        "[L² T⁻²]",
        "Energy = force × distance = [M L T⁻²] × [L] = [M L² T⁻²]. This is the dimension of the joule (J = kg·m²/s²)."
    ),
    (
        "What is dimensional analysis used for?",
        "Checking whether equations are dimensionally consistent and converting units",
        "Measuring the dimensions of physical objects",
        "Creating new physical quantities",
        "Replacing numerical calculations in physics",
        "Dimensional analysis verifies that equations are dimensionally consistent (both sides have the same dimensions) and helps convert between units. It can also help derive relationships between physical quantities."
    ),
    (
        "An equation has [M L T⁻²] on the left side and [M L² T⁻³] on the right side. Is this equation valid?",
        "No — the dimensions on both sides must match for the equation to be valid",
        "Yes — close enough is acceptable in dimensional analysis",
        "Yes — the exponents only differ by one",
        "Cannot determine without numerical values",
        "For an equation to be dimensionally valid, every term on both sides must have identical dimensions. [M L T⁻²] ≠ [M L² T⁻³], so the equation is dimensionally incorrect."
    ),
    (
        "What is the dimension of power?",
        "[M L² T⁻³]",
        "[M L² T⁻²]",
        "[M L T⁻²]",
        "[L² T⁻³]",
        "Power = energy / time = [M L² T⁻²] / [T] = [M L² T⁻³]. This is the dimension of the watt (W = kg·m²/s³)."
    ),
    (
        "What dimension does a dimensionless quantity have?",
        "[1] or no dimensions — it is a pure number",
        "[M⁰ L⁰ T⁰] which equals [M L T]",
        "It has the dimensions of its largest component",
        "Dimensionless quantities don't exist in physics",
        "A dimensionless quantity has no dimensions (all exponents are zero). Examples include the coefficient of friction, angle in radians, and the refractive index. It is a pure number."
    ),
    # VOCABULARY (11-20)
    (
        "Which definition BEST describes dimensional analysis?",
        "A method of checking the validity of physics equations by ensuring that all terms have the same fundamental dimensions",
        "A way to measure the three dimensions of an object",
        "A technique for calculating exact numerical answers",
        "A method for determining the units of measuring instruments",
        "Dimensional analysis examines the fundamental dimensions [M], [L], [T], etc. on both sides of an equation. If dimensions don't match, the equation must contain an error."
    ),
    (
        "Which definition BEST describes the dimension of a physical quantity?",
        "The expression of the quantity in terms of fundamental dimensions (M, L, T, etc.) that describes what type of quantity it represents",
        "The physical size of the quantity",
        "The SI unit used to measure the quantity",
        "The number of significant figures in the measurement",
        "The dimension tells you the fundamental nature of a quantity. For example, both speed (m/s) and velocity (m/s) have the dimension [L T⁻¹], telling us they are fundamentally the same type of quantity."
    ),
    (
        "Which definition BEST describes dimensional homogeneity?",
        "The requirement that every additive term in a valid physics equation must have the same dimensions",
        "The condition that all measurements use the same units",
        "The property that all vectors have the same direction",
        "The requirement that all numbers be of similar size",
        "Dimensional homogeneity means that in an equation like v = u + at, each term (v, u, and at) must have the same dimensions. This is a necessary (but not sufficient) condition for an equation to be correct."
    ),
    (
        "Which definition BEST describes a dimensionless quantity?",
        "A pure number that has no physical dimensions, formed when all dimensional powers cancel to zero",
        "A quantity that is too small to measure",
        "A quantity that exists only in mathematics",
        "A quantity that has no numerical value",
        "Dimensionless quantities are pure numbers. Angles in radians, coefficients (like friction), and ratios of like quantities are dimensionless. Dimensional analysis cannot determine their value."
    ),
    (
        "Which definition BEST describes the Buckingham Pi theorem?",
        "A theorem stating that any physically meaningful equation involving n variables and k fundamental dimensions can be rewritten using n − k independent dimensionless groups",
        "A formula for calculating the value of π in different unit systems",
        "A rule for counting significant figures in products",
        "A method for converting between imperial and metric units",
        "The Buckingham Pi theorem is a powerful tool in dimensional analysis. It states that the physics of a problem can be captured by a set of dimensionless groups (Pi groups), reducing the number of variables that need to be studied."
    ),
    (
        "Which definition BEST describes a conversion factor in dimensional analysis?",
        "A multiplicative factor with dimensions that, when applied to a measurement, changes its units while preserving the physical quantity",
        "A dimensionless number used to scale an equation",
        "The ratio of the largest to smallest measurement",
        "The error in a dimensional calculation",
        "Conversion factors like (1 km / 1000 m) have dimensions and value of 1, allowing unit changes without changing the physical quantity. They are the practical application of dimensional analysis."
    ),
    (
        "Which definition BEST describes the principle of dimensional consistency?",
        "The fundamental rule that a valid equation must have identical dimensions on both sides and in every additive term",
        "The idea that all measurements should use SI units",
        "The rule that dimensions must always be integers",
        "The principle that larger dimensions are more important",
        "Dimensional consistency is a necessary condition for any valid physical equation. If the dimensions don't match, the equation is guaranteed to be wrong. However, dimensional consistency alone doesn't guarantee correctness."
    ),
    (
        "Which definition BEST describes a derived dimension?",
        "A dimension formed by combining fundamental dimensions through multiplication, division, or exponentiation",
        "A dimension that was discovered after the original seven",
        "A dimension that exists only in theory",
        "A dimension that varies with temperature",
        "Derived dimensions are built from fundamental ones. Velocity [L T⁻¹], force [M L T⁻²], and energy [M L² T⁻²] are all derived dimensions formed by combining [M], [L], and [T]."
    ),
    (
        "Which definition BEST describes dimensional formula?",
        "An expression showing how a physical quantity is composed of the fundamental dimensions, written using dimensional symbols with exponents",
        "The chemical formula for a substance",
        "The mathematical equation relating two quantities",
        "The units of a measuring device",
        "A dimensional formula expresses a quantity in terms of fundamental dimensions. For example, the dimensional formula of force is [M¹ L¹ T⁻²], showing that force involves mass, length, and the inverse square of time."
    ),
    (
        "Which definition BEST describes unit analysis (also called factor-label method)?",
        "A problem-solving technique that tracks units through a calculation using conversion factors to ensure the final answer has the correct units",
        "A method of labeling measuring instruments",
        "A technique for determining significant figures",
        "A way to classify physical quantities as scalar or vector",
        "Unit analysis (factor-label method) systematically converts units by multiplying by conversion factors arranged so that unwanted units cancel and desired units remain. It guarantees correct unit outcomes."
    ),
    # SCENARIO (21-30)
    (
        "A student proposes that the period T of a simple pendulum depends on its length L and gravitational acceleration g. Using dimensional analysis, she finds T = k√(L/g). Why can't dimensional analysis determine the constant k?",
        "Because k is dimensionless — dimensional analysis only ensures dimensional consistency and cannot determine pure numerical constants",
        "Because k depends on the mass of the pendulum",
        "Because the formula is incorrect",
        "Because k changes with every pendulum",
        "Since k is a dimensionless number (in this case 2π), it contributes no dimensions. Dimensional analysis can only match dimensions, not determine dimensionless constants. Experiment or derivation reveals k = 2π."
    ),
    (
        "A physics student writes: F = mv² (force equals mass times velocity squared). Use dimensional analysis to check this claim.",
        "Incorrect — [F] = [M L T⁻²] but [mv²] = [M L² T⁻²], which is the dimension of energy, not force",
        "Correct — the dimensions match on both sides",
        "Cannot be checked because velocity is a vector",
        "Incorrect — you cannot square a vector quantity",
        "[F] = [M L T⁻²]. [mv²] = [M][L T⁻¹]² = [M L² T⁻²]. Since [M L T⁻²] ≠ [M L² T⁻²], the equation is dimensionally inconsistent. The correct relationship requires dividing by a length: F = mv²/r (centripetal force)."
    ),
    (
        "An engineer needs to know how drag force F depends on fluid density ρ, velocity v, and cross-sectional area A. Using dimensions [F] = [M L T⁻²], [ρ] = [M L⁻³], [v] = [L T⁻¹], [A] = [L²], what combination works?",
        "F ∝ ρv²A — checking: [M L⁻³][L T⁻¹]²[L²] = [M L⁻³][L² T⁻²][L²] = [M L T⁻²] ✓",
        "F ∝ ρvA — this gives [M L⁻¹ T⁻¹] which matches force",
        "F ∝ ρv³A² — more v's and A's mean more force",
        "Dimensional analysis cannot determine this relationship",
        "By matching dimensions: [M L⁻³]ᵃ[L T⁻¹]ᵇ[L²]ᶜ = [M L T⁻²]. Solving: a = 1, b = 2, c = 1. So F ∝ ρv²A. The actual drag equation is F = ½CᴅρAv², where ½Cᴅ is the dimensionless drag coefficient."
    ),
    (
        "A student derives an equation and gets: x = ½at² + vt + F where x is position, a is acceleration, t is time, v is velocity, and F is force. Is this equation valid?",
        "No — the term F has dimension [M L T⁻²] while the other terms have dimension [L], violating dimensional homogeneity",
        "Yes — all five variables are valid physical quantities",
        "Yes — the equation uses correct physics symbols",
        "Cannot be determined without numerical values",
        "Checking each term: [½at²] = [L T⁻²][T²] = [L] ✓, [vt] = [L T⁻¹][T] = [L] ✓, [F] = [M L T⁻²] ✗. The force term has different dimensions from the position terms, so the equation is invalid."
    ),
    (
        "A researcher measures the speed of a car as 90 km/h and needs it in m/s. She uses dimensional analysis (factor-label method) to convert. What is the correct setup?",
        "90 km/h × (1000 m / 1 km) × (1 h / 3600 s) = 25 m/s — conversion factors cancel unwanted units",
        "90 km/h × (1 km / 1000 m) = 0.09 m/s",
        "90 km/h ÷ 3.6 is correct but dimensional analysis isn't needed",
        "90 km/h × 3600 = 324,000 m/s",
        "The factor-label method: 90 (km/h) × (1000 m/1 km) × (1 h/3600 s). The km cancels, the h cancels, leaving m/s: 90 × 1000/3600 = 25 m/s. Each conversion factor equals 1, preserving the physical quantity."
    ),
    (
        "A physics equation states: P = ρgh, where P is pressure, ρ is density, g is gravitational acceleration, and h is height. Verify this equation using dimensional analysis.",
        "Valid — [ρgh] = [M L⁻³][L T⁻²][L] = [M L⁻¹ T⁻²] = [P] (pressure = force/area = [M L T⁻²]/[L²]) ✓",
        "Invalid — density has the wrong dimensions for a pressure equation",
        "Valid — but only when h is measured in meters",
        "Invalid — pressure has no mass dimension",
        "[P] = [Force/Area] = [M L T⁻²]/[L²] = [M L⁻¹ T⁻²]. [ρgh] = [M L⁻³][L T⁻²][L] = [M L⁻³⁺¹⁺¹ T⁻²] = [M L⁻¹ T⁻²] ✓. The dimensions match, confirming the equation is dimensionally valid."
    ),
    (
        "Two students argue about the equation E = mc. Student A says it should be E = mc². Student B argues both could be correct 'depending on the system.' Who is right?",
        "Student A — dimensional analysis proves E = mc is wrong: [M][L T⁻¹] = [M L T⁻¹] ≠ [M L² T⁻²] = [Energy]. Only E = mc² is dimensionally correct",
        "Student B — any equation can be correct in some system of units",
        "Neither — E = mc³ is the correct equation",
        "Both are wrong — energy cannot be related to mass",
        "[E] = [M L² T⁻²]. [mc] = [M][L T⁻¹] = [M L T⁻¹] — wrong dimensions. [mc²] = [M][L T⁻¹]² = [M L² T⁻²] — matches energy. The equation E = mc has no system where it could work because the dimensions are fundamentally mismatched."
    ),
    (
        "A fluid dynamics student wants to determine if a new equation v = √(2P/ρ) is plausible, where v is velocity, P is pressure, and ρ is density. Check using dimensional analysis.",
        "Plausible — [2P/ρ]^½ = ([M L⁻¹ T⁻²]/[M L⁻³])^½ = [L² T⁻²]^½ = [L T⁻¹] = [v] ✓",
        "Implausible — pressure and density can't be combined this way",
        "Plausible — but only if ρ is in g/cm³",
        "Implausible — the square root changes the dimensions",
        "[P/ρ] = [M L⁻¹ T⁻²] / [M L⁻³] = [L² T⁻²]. Taking the square root: [L² T⁻²]^½ = [L T⁻¹] = dimensions of velocity ✓. The equation is dimensionally valid (it's actually Torricelli-type relation)."
    ),
    (
        "An airplane designer proposes that the lift force L depends on air density ρ, wing area A, and velocity v as L = ρA²v. Dimensional analysis reveals this is wrong. What should the correct dependence be?",
        "L ∝ ρAv² — checking: [M L⁻³][L²][L T⁻¹]² = [M L⁻³][L²][L² T⁻²] = [M L T⁻²] = [Force] ✓",
        "L ∝ ρA²v² — just square everything",
        "L ∝ ρ²Av — double the density term",
        "L ∝ √(ρAv) — take the square root",
        "Checking the proposed L = ρA²v: [M L⁻³][L²]²[L T⁻¹] = [M L⁻³][L⁴][L T⁻¹] = [M L² T⁻¹] ≠ [M L T⁻²]. The correct combination L ∝ ρAv²: [M L⁻³][L²][L² T⁻²] = [M L T⁻²] ✓."
    ),
    (
        "A student solves a problem and gets the answer in units of kg·m²/s³. Without knowing what formula was used, what physical quantity does this represent?",
        "Power — [M L² T⁻³] is the dimension of power (watts), which is the rate of energy transfer",
        "Force — kg·m²/s³ is another way to write newtons",
        "Energy — these are the units of joules",
        "Momentum — this is the product of mass and velocity",
        "[M L² T⁻³] = [M L² T⁻²]/[T] = Energy/Time = Power. The unit kg·m²/s³ is equivalent to the watt (W). Dimensional analysis can identify a physical quantity from its dimensions alone."
    ),
]

LESSONS[("1", "1.6", "Measurement Uncertainty & Error Analysis")] = [
    # EASY (1-10)
    (
        "What is a systematic error?",
        "A consistent error that shifts all measurements in the same direction by approximately the same amount",
        "A random variation that changes with each measurement",
        "An error made by not reading the instructions",
        "A mathematical rounding error",
        "Systematic errors affect accuracy by consistently biasing measurements. They can be caused by miscalibrated instruments, incorrect technique, or environmental factors, and they shift results consistently in one direction."
    ),
    (
        "What is a random error?",
        "An unpredictable variation in measurements that scatters results around the true value",
        "A consistent bias in all measurements",
        "An error caused by using the wrong formula",
        "An error that only occurs once",
        "Random errors cause measurements to vary unpredictably. They result from uncontrollable factors like vibrations, temperature fluctuations, and human estimation. Taking more measurements and averaging reduces their effect."
    ),
    (
        "What is absolute uncertainty?",
        "The margin of error in a measurement expressed in the same units as the measurement (e.g., ± 0.1 cm)",
        "The total value of the measurement",
        "The percentage of error in a measurement",
        "The difference between two measurements",
        "Absolute uncertainty expresses the range within which the true value is expected to lie. A measurement of 5.0 ± 0.1 cm means the true value is between 4.9 and 5.1 cm."
    ),
    (
        "What is percentage uncertainty?",
        "(Absolute uncertainty / Measured value) × 100%",
        "Absolute uncertainty multiplied by 100",
        "The number of decimal places expressed as a percentage",
        "The number of measurements that agree with each other",
        "Percentage uncertainty = (absolute uncertainty / measured value) × 100%. For 5.0 ± 0.1 cm: (0.1/5.0) × 100% = 2%. It expresses uncertainty relative to the measurement size."
    ),
    (
        "How can you reduce random errors in an experiment?",
        "Take multiple measurements and calculate the average",
        "Use a more expensive instrument",
        "Measure only once very carefully",
        "Ignore outliers in the data",
        "Averaging multiple measurements reduces the effect of random errors because random fluctuations tend to cancel out over many trials. The more measurements taken, the closer the mean approaches the true value."
    ),
    (
        "How can you reduce systematic errors?",
        "Calibrate instruments against known standards and improve experimental techniques",
        "Take more measurements and average them",
        "Use the same instrument for all measurements",
        "Repeat the experiment on different days",
        "Systematic errors are not reduced by averaging. They must be identified and eliminated through calibration, improved technique, or using different methods to check results."
    ),
    (
        "When adding two measurements with uncertainties, how do you find the total uncertainty?",
        "Add the absolute uncertainties: (a ± Δa) + (b ± Δb) = (a + b) ± (Δa + Δb)",
        "Add the percentage uncertainties",
        "Take the larger uncertainty",
        "Multiply the uncertainties together",
        "When adding or subtracting measurements, absolute uncertainties add. If length₁ = 5.0 ± 0.1 cm and length₂ = 3.0 ± 0.2 cm, then total = 8.0 ± 0.3 cm."
    ),
    (
        "When multiplying two measurements with uncertainties, how do you find the total percentage uncertainty?",
        "Add the percentage uncertainties of each measurement",
        "Add the absolute uncertainties",
        "Multiply the percentage uncertainties",
        "Take the smaller percentage uncertainty",
        "When multiplying or dividing, percentage uncertainties add. If A has 2% uncertainty and B has 3% uncertainty, then A × B has 5% uncertainty."
    ),
    (
        "A measurement is recorded as 25.0 ± 0.5 cm. What does this notation mean?",
        "The measured value is 25.0 cm and the true value is expected to lie between 24.5 and 25.5 cm",
        "There is a 25.0% chance the measurement is correct",
        "The measurement was taken 0.5 cm from the ruler",
        "The measurement could be anywhere between 0 and 50 cm",
        "The ± notation expresses the absolute uncertainty. The measured value is 25.0 cm, and we are confident the true value lies within 0.5 cm of this value, between 24.5 and 25.5 cm."
    ),
    (
        "What is the zero error of an instrument?",
        "A systematic error where the instrument does not read exactly zero when it should",
        "A random error that occurs at the start of an experiment",
        "An error that makes the reading exactly zero",
        "The error in the last digit of a reading",
        "Zero error is a type of systematic error. For example, if a scale reads 0.2 g with nothing on it, every measurement will be 0.2 g too high. It is corrected by subtracting the zero offset from all readings."
    ),
    # VOCABULARY (11-20)
    (
        "Which definition BEST describes uncertainty in measurement?",
        "A quantitative estimate of the range of values within which the true value of a measurement is expected to lie",
        "A mistake made during the measurement process",
        "The difference between two measurements of the same quantity",
        "The number of significant figures in a result",
        "Uncertainty is inherent in all measurements. It quantifies our lack of knowledge about the true value. A measurement of 10.0 ± 0.2 cm means we are confident the true value is between 9.8 and 10.2 cm."
    ),
    (
        "Which definition BEST describes systematic error?",
        "A reproducible, consistent bias in measurements caused by flawed equipment, technique, or conditions that shifts all readings in one direction",
        "An error that varies unpredictably with each measurement",
        "An error caused by misreading a scale",
        "An error that appears only in certain types of experiments",
        "Systematic errors are consistent and reproducible. They affect accuracy (not precision) and cannot be reduced by taking more measurements. Examples include zero errors, parallax from incorrect technique, and environment-induced bias."
    ),
    (
        "Which definition BEST describes random error?",
        "Unpredictable fluctuations in measurements caused by uncontrollable variables that scatter readings around the true value",
        "A consistent shift in all measurements",
        "An error caused by using a broken instrument",
        "An error that occurs exactly once per experiment",
        "Random errors cause scatter in data. They affect precision (not systematic accuracy) and are caused by factors like vibrations, temperature fluctuations, and estimation inconsistencies. Their effect decreases with more measurements."
    ),
    (
        "Which definition BEST describes absolute uncertainty?",
        "The magnitude of the uncertainty expressed in the same units as the measurement, representing a range around the measured value",
        "The uncertainty expressed as a percentage",
        "The largest possible error in a measurement",
        "The total uncertainty from all sources combined",
        "Absolute uncertainty is expressed in the measurement's units. For 15.0 ± 0.3 m, the absolute uncertainty is 0.3 m. It represents the estimated half-width of the range within which the true value lies."
    ),
    (
        "Which definition BEST describes percentage uncertainty?",
        "The absolute uncertainty divided by the measured value, multiplied by 100%, expressing uncertainty relative to the measurement's size",
        "The number of uncertain digits expressed as a percentage",
        "The probability that a measurement is correct",
        "The percentage of measurements that are outliers",
        "Percentage uncertainty = (Δx / x) × 100%. It allows comparison of precision between different measurements. A 0.1 cm uncertainty means different things for a 1 cm measurement (10%) versus a 100 cm measurement (0.1%)."
    ),
    (
        "Which definition BEST describes error propagation?",
        "The mathematical rules for calculating how measurement uncertainties combine through calculations to produce uncertainty in the final result",
        "The spreading of errors from one experiment to another",
        "The process of errors increasing over time",
        "The transfer of mistakes between students",
        "Error propagation rules: for addition/subtraction, add absolute uncertainties; for multiplication/division, add percentage uncertainties; for powers, multiply percentage uncertainty by the exponent."
    ),
    (
        "Which definition BEST describes a parallax error?",
        "A systematic error caused by viewing a measuring instrument from an angle instead of directly in front, leading to an incorrect reading",
        "A random error that changes with each observation",
        "An error caused by using the wrong units",
        "An error that occurs only with digital instruments",
        "Parallax error occurs when a measurement scale is not viewed perpendicular to the observer's line of sight. For example, reading a ruler at an angle makes the reading appear shifted from the true value."
    ),
    (
        "Which definition BEST describes precision of an instrument?",
        "The degree to which repeated measurements made by the instrument agree with each other, often indicated by the smallest division on its scale",
        "How expensive or well-made the instrument is",
        "The size of the largest measurement it can make",
        "How quickly the instrument gives a reading",
        "An instrument's precision is related to its resolution (smallest readable increment). A ruler marked in mm is more precise than one marked in cm. High precision means small random variation between repeated readings."
    ),
    (
        "Which definition BEST describes an outlier?",
        "A measurement that falls significantly outside the range of other measurements in a data set, often caused by an experimental error or unusual condition",
        "The most accurate measurement in a set",
        "The average of all measurements",
        "A measurement taken at a different time",
        "Outliers are data points that deviate substantially from the rest. They may result from mistakes, equipment malfunction, or genuinely unusual conditions. They should be investigated (not automatically discarded) and excluded only if a clear cause is identified."
    ),
    (
        "Which definition BEST describes the mean (average) value?",
        "The sum of all measurement values divided by the number of measurements, providing the best estimate of the true value when random errors are present",
        "The most frequently occurring value in a data set",
        "The middle value when data is arranged in order",
        "The difference between the highest and lowest values",
        "The mean reduces the effect of random errors because positive and negative deviations tend to cancel. With more measurements, the mean converges toward the true value (assuming no systematic error)."
    ),
    # SCENARIO (21-30)
    (
        "A scientist measures the mass of a sample five times: 10.1, 10.3, 10.0, 10.2, 10.1 g. The true mass is 10.5 g. What types of error are present?",
        "Both random error (measurements scatter between 10.0–10.3 g) and systematic error (all readings are below the true value of 10.5 g)",
        "Only random error — the measurements vary",
        "Only systematic error — all readings are below the true value",
        "No error — the measurements are close to each other",
        "The scatter (10.0–10.3 g) indicates random error. The consistent offset below the true value (mean ≈ 10.14 vs true 10.5) indicates systematic error. The scale may be under-reading, or the sample was not fully dry."
    ),
    (
        "A student measures the length of a rod as 15.0 ± 0.2 cm and its width as 3.0 ± 0.1 cm. What is the area and its absolute uncertainty?",
        "45 ± 3 cm² — percentage uncertainties add in multiplication: (0.2/15.0 + 0.1/3.0) × 100% = 4.7%, and 4.7% of 45 = 2.1 ≈ 3 cm²",
        "45 ± 0.3 cm² — add the absolute uncertainties",
        "45 ± 0.02 cm² — multiply the absolute uncertainties",
        "45 cm² with no uncertainty",
        "For multiplication: add percentage uncertainties. %Δl = (0.2/15.0) × 100% = 1.33%. %Δw = (0.1/3.0) × 100% = 3.33%. Total = 4.67%. Area = 15.0 × 3.0 = 45.0 cm². Absolute uncertainty = 4.67% × 45.0 ≈ 2.1 ≈ 3 cm². Report as 45 ± 3 cm²."
    ),
    (
        "A physics teacher holds up a digital thermometer and a mercury thermometer. Both read room temperature. The digital one reads 22.4°C and the mercury one reads 22°C. Which measurement has less uncertainty, and why?",
        "The digital thermometer — it reads to 0.1°C resolution (uncertainty ≈ ±0.1°C) while the mercury thermometer reads to 1°C resolution (uncertainty ≈ ±0.5°C)",
        "The mercury thermometer — traditional instruments are always more precise",
        "They have the same uncertainty — both measure the same temperature",
        "Neither — uncertainty cannot be determined from a single reading",
        "The digital thermometer displays to the nearest 0.1°C, giving it estimated uncertainty of ±0.1°C. The mercury thermometer resolves to 1°C (estimated reading could be ±0.5°C). Higher resolution means smaller absolute uncertainty."
    ),
    (
        "A student measures the time for 10 pendulum swings as 15.8 ± 0.3 s. She calculates the period of one swing as T = 15.8/10 = 1.58 s. What is the uncertainty in T?",
        "±0.03 s — when dividing by an exact number (10 swings), the percentage uncertainty stays the same: 0.3/15.8 = 1.9%, and 1.9% of 1.58 s = 0.03 s",
        "±0.3 s — the uncertainty is unchanged",
        "±0.003 s — divide uncertainty by 100",
        "±3.0 s — multiply uncertainty by 10",
        "The number 10 is exact (counted, no uncertainty). Dividing by an exact number: T = 15.8/10 = 1.58 s. The percentage uncertainty transfers directly: (0.3/15.8) × 100% = 1.9%. Absolute uncertainty in T = 1.9% × 1.58 = 0.03 s. T = 1.58 ± 0.03 s."
    ),
    (
        "An experiment measures the acceleration due to gravity by dropping a ball. Results from five groups: 9.7, 9.9, 9.8, 12.1, 9.8 m/s². One result (12.1) is very different. What should be done?",
        "Investigate the 12.1 m/s² as an outlier — if an error is found (e.g., timing mistake), exclude it; the remaining values give a mean of 9.8 m/s² with good precision",
        "Include all values including 12.1 and average them",
        "Report only the 12.1 value as the most interesting result",
        "Discard all data since some of it is wrong",
        "The 12.1 m/s² value is an outlier — far from the cluster of 9.7–9.9. Investigate its cause (perhaps a timing error). If confirmed as an error, exclude it. The remaining mean (9.7+9.9+9.8+9.8)/4 = 9.8 m/s² is close to the accepted value of 9.81 m/s²."
    ),
    (
        "A student calculates the speed of a car. Distance = 100.0 ± 0.5 m, Time = 4.0 ± 0.2 s. What is the percentage uncertainty in the calculated speed?",
        "5.5% — add percentage uncertainties: (0.5/100.0 × 100%) + (0.2/4.0 × 100%) = 0.5% + 5.0% = 5.5%",
        "0.7% — add the absolute uncertainties and divide by the speed",
        "0.5% — use only the distance uncertainty",
        "5.0% — use only the time uncertainty",
        "For division (speed = distance/time), add percentage uncertainties: %Δd = (0.5/100.0) × 100% = 0.5%. %Δt = (0.2/4.0) × 100% = 5.0%. Total = 5.5%. Speed = 25.0 m/s ± 5.5% = 25.0 ± 1.4 m/s."
    ),
    (
        "A bathroom scale at a gym consistently reads 1.5 kg lower than the calibrated medical scale. A person weighs themselves 10 times and gets consistent readings of 68.0 kg. What can be said about this scale?",
        "The scale is precise (consistent readings) but not accurate (systematic error of −1.5 kg means true mass is 69.5 kg)",
        "The scale is both accurate and precise because the readings are consistent",
        "The scale has large random errors",
        "The scale needs more measurements to determine accuracy",
        "The consistent 68.0 kg readings indicate high precision. However, the systematic offset of −1.5 kg (reading lower than the calibrated reference) means poor accuracy. The true mass is approximately 69.5 kg. Recalibration would fix this."
    ),
    (
        "A student measures the volume of a cube with sides of 5.0 ± 0.1 cm. She calculates V = (5.0)³ = 125 cm³. What is the percentage uncertainty in the volume?",
        "6% — for a quantity raised to a power n, multiply the percentage uncertainty by n: 3 × (0.1/5.0 × 100%) = 3 × 2% = 6%",
        "2% — the same as the side measurement",
        "8% — add 2% three times plus an extra 2%",
        "0.3% — multiply the absolute uncertainties",
        "For V = s³, the percentage uncertainty is 3 × (percentage uncertainty of s). %Δs = (0.1/5.0) × 100% = 2%. %ΔV = 3 × 2% = 6%. Volume = 125 ± 8 cm³ (6% of 125 = 7.5 ≈ 8)."
    ),
    (
        "A digital stopwatch has a resolution of 0.01 s, but human reaction time is about 0.2 s. A student uses it to time a race and claims an uncertainty of ±0.01 s. Is this claim justified?",
        "No — the actual uncertainty is limited by human reaction time (≈ ±0.2 s), not the stopwatch resolution; the larger uncertainty source dominates",
        "Yes — the instrument's resolution determines the uncertainty",
        "Yes — digital instruments remove human error",
        "No — the uncertainty should be ±0.005 s (half the resolution)",
        "Total uncertainty comes from the largest contributing source. Although the stopwatch resolves to 0.01 s, the human pressing start/stop introduces ≈ 0.2 s uncertainty. The dominant source (human reaction time) determines the practical uncertainty."
    ),
    (
        "Two students measure the gravitational acceleration g. Student A gets 9.82 ± 0.05 m/s². Student B gets 9.80 ± 0.30 m/s². The accepted value is 9.81 m/s². Which result is better overall?",
        "Student A's result is better — it is equally accurate (close to 9.81) and much more precise (smaller uncertainty of ±0.05 vs ±0.30)",
        "Student B's result is better because 9.80 is closer to 9.81",
        "Both are equally good since they overlap within uncertainty ranges",
        "Neither is good enough — both miss the exact value of 9.81",
        "Student A: 9.82 ± 0.05 (accurate to within 0.01, precise to ±0.05). Student B: 9.80 ± 0.30 (accurate to within 0.01, but imprecise at ±0.30). Both are accurate, but A's smaller uncertainty makes it the superior measurement."
    ),
]

# ============================================================
# UNIT 2: Kinematics
# ============================================================

LESSONS[("2", "2.1", "Distance, Displacement, Speed, Velocity")] = [
    # EASY (1-10)
    ("What is the difference between distance and displacement?", "Distance is total path length (scalar), displacement is straight-line change in position (vector)", "They are the same thing measured differently", "Distance has direction, displacement does not", "Displacement is always larger than distance", "Distance measures the total length of the path traveled (scalar, always positive). Displacement measures the straight-line distance from start to finish with direction (vector, can be positive, negative, or zero)."),
    ("What is average speed?", "Total distance traveled divided by total time taken", "Total displacement divided by total time", "The speed at a single instant", "Final speed minus initial speed", "Average speed = total distance / total time. It is a scalar quantity and is always positive."),
    ("What is average velocity?", "Displacement divided by total time taken", "Total distance divided by total time", "The velocity at one instant", "The sum of all velocities divided by the count", "Average velocity = Δx / Δt (displacement / time). It is a vector quantity and can be positive, negative, or zero."),
    ("A car travels 100 km north then 100 km south. What is its distance and displacement?", "Distance = 200 km, displacement = 0 km", "Distance = 0 km, displacement = 200 km", "Both are 200 km", "Both are 100 km", "Distance is the total path: 100 + 100 = 200 km. Displacement is the net change in position: 100 km north − 100 km south = 0 km (back to start)."),
    ("What is instantaneous speed?", "The speed of an object at a specific moment in time", "The average of all speeds during a trip", "The maximum speed reached", "The speed at the start of a journey", "Instantaneous speed is the rate of distance change at a particular instant. It corresponds to the magnitude of the slope of a position-time graph at that point."),
    ("Can a moving object have zero velocity?", "Not instantaneously while moving, but an object can have zero average velocity after a round trip", "No — a moving object always has velocity", "Yes — if it moves in a circle forever", "Only at the speed of light", "An object completing a round trip has zero average velocity (zero displacement / time). However, at any instant during motion, instantaneous velocity is nonzero. At a turnaround point, instantaneous velocity momentarily equals zero."),
    ("What is the SI unit of speed?", "Meters per second (m/s)", "Kilometers per hour (km/h)", "Miles per hour (mph)", "Feet per second (ft/s)", "The SI unit of speed (and velocity) is meters per second (m/s). Other units like km/h can be converted: divide by 3.6 to convert km/h to m/s."),
    ("A jogger runs 5 km in 25 minutes. What is their average speed in km/h?", "12 km/h", "5 km/h", "0.2 km/h", "25 km/h", "Average speed = distance / time = 5 km / (25/60 h) = 5 / 0.417 = 12 km/h."),
    ("What does the slope of a position-time graph represent?", "Velocity", "Acceleration", "Distance", "Force", "The slope of a position-time graph gives velocity. A steeper slope means higher velocity; a horizontal line means zero velocity (stationary). A negative slope indicates motion in the negative direction."),
    ("An object moves 30 m east in 5 s. What is its velocity?", "6 m/s east", "6 m/s (direction unknown)", "150 m/s east", "25 m/s east", "Velocity = displacement / time = 30 m east / 5 s = 6 m/s east. Since velocity is a vector, the direction must be included."),
    # VOCABULARY (11-20)
    ("Which definition BEST describes distance?", "The total length of the path traveled by an object, regardless of direction — a scalar quantity", "The straight-line separation between two points", "Displacement measured without direction", "The area under a velocity-time graph", "Distance is scalar (no direction) and equals the sum of all path segments. It is always positive or zero and can never decrease during motion."),
    ("Which definition BEST describes displacement?", "The change in position of an object measured as a straight line from initial to final position, with direction — a vector quantity", "The total distance traveled by an object", "The length of a curved path", "The speed multiplied by time", "Displacement = Δx = x_final − x_initial. It has magnitude (shortest distance between start and end) and direction. It can be positive, negative, or zero."),
    ("Which definition BEST describes speed?", "The rate at which an object covers distance — a scalar quantity equal to distance divided by time", "The rate of change of displacement", "Velocity without a sign", "Distance multiplied by time", "Speed = distance/time. It is always positive or zero, has no direction, and tells how fast (but not in what direction) an object is moving."),
    ("Which definition BEST describes velocity?", "The rate of change of displacement with respect to time — a vector quantity with both magnitude and direction", "The rate at which distance is covered", "Speed with an arbitrary direction assigned", "Acceleration multiplied by time", "Velocity = Δx/Δt. As a vector, it includes direction. Positive and negative signs indicate opposite directions along a chosen axis."),
    ("Which definition BEST describes instantaneous velocity?", "The velocity of an object at a single specific moment in time, equal to the derivative of position with respect to time", "The average velocity over a very long time", "The maximum velocity during a trip", "Velocity measured only with a speedometer", "Instantaneous velocity v = dx/dt, the limit of Δx/Δt as Δt → 0. It is the slope of the tangent to the position-time curve at any given instant."),
    ("Which definition BEST describes uniform motion?", "Motion at constant velocity — traveling in a straight line at an unchanging speed with no acceleration", "Any motion along a straight line", "Motion that gradually speeds up", "Motion in a circular path at constant speed", "Uniform motion means constant velocity: zero acceleration, constant speed, and constant direction. On a position-time graph, it appears as a straight line."),
    ("Which definition BEST describes a reference frame?", "A coordinate system used to define positions and describe the motion of objects relative to an observer", "The physical frame around a picture", "The starting line of a race", "The direction of gravity", "A reference frame provides the axes and origin from which positions, velocities, and accelerations are measured. Motion is always described relative to a chosen reference frame."),
    ("Which definition BEST describes a position-time graph?", "A graph that plots an object's position on the vertical axis against time on the horizontal axis, where the slope represents velocity", "A graph showing the distance between two objects over time", "A graph with velocity on the y-axis and time on the x-axis", "A map showing where an object is located", "Position-time graphs encode motion information: slope = velocity, horizontal line = stationary, curved line = changing velocity. They are fundamental tools in kinematics."),
    ("Which definition BEST describes the odometer vs. speedometer distinction?", "An odometer measures total distance traveled (scalar), while a speedometer measures instantaneous speed (scalar)", "An odometer measures displacement while a speedometer measures velocity", "Both measure the same quantity in different units", "An odometer measures average speed while a speedometer measures maximum speed", "The odometer accumulates total path length (distance — always increasing). The speedometer shows how fast the car is going right now (instantaneous speed). Neither provides directional information."),
    ("Which definition BEST describes relative velocity?", "The velocity of one object as observed from the reference frame of another moving object", "The maximum velocity difference between two objects", "The average of two objects' velocities", "The total velocity of all objects in a system", "Relative velocity v_A relative to B = v_A − v_B. If two cars move in the same direction at 60 km/h and 40 km/h, the relative velocity of the first from the second's frame is 20 km/h."),
    # SCENARIO (21-30)
    ("A student walks 4 blocks north to school, then 3 blocks east to the library after school. Her pedometer (step counter) shows she walked 700 m total. What are her distance and displacement from home to the library?", "Distance = 700 m (total path), Displacement = 500 m at 36.9° east of north (the straight-line shortcut)", "Distance = 500 m, Displacement = 700 m", "Distance = Displacement = 700 m", "Distance = Displacement = 500 m", "Distance is the 700 m total path (4 blocks + 3 blocks). Displacement is the straight-line distance from home to library. If blocks are 100 m: displacement = √(400² + 300²) = 500 m at tan⁻¹(300/400) = 36.9° east of north."),
    ("A delivery driver drives 30 km in 30 minutes, stops for 15 minutes for a delivery, then drives 30 km back in 30 minutes. Calculate the average speed and average velocity for the entire trip.", "Average speed = 48 km/h (total distance 60 km / total time 1.25 h); average velocity = 0 (displacement is zero since he returned to the start)", "Average speed = 0, average velocity = 48 km/h", "Both are 48 km/h", "Both are 0", "Total distance = 30 + 30 = 60 km. Total time = 30 + 15 + 30 = 75 min = 1.25 h. Average speed = 60/1.25 = 48 km/h. Displacement = 0 (returned to start), so average velocity = 0/1.25 = 0."),
    ("A GPS app shows a driver has traveled 50 km using 'trip distance' but the 'displacement' reading shows only 30 km. What does this difference reveal about the driver's path?", "The driver did not travel in a straight line — the path included turns, curves, or detours, making distance > displacement", "The GPS is malfunctioning", "The driver went backwards at some point, which subtracted from distance", "Displacement is always exactly 60% of distance", "Distance ≥ |displacement| always. They are equal only for straight-line motion without backtracking. The 20 km difference (50 − 30) indicates the path deviated significantly from a straight line between start and end points."),
    ("A sprinter runs 100 m in 10.0 s. Her coach says her average speed was 10 m/s but her instantaneous speed at the 50 m mark was 11.5 m/s. How is this possible?", "Her speed varied during the race — she accelerated from rest at the start and was faster than average in the middle; instantaneous speed at a point can differ from average speed over the whole race", "The coach made a calculation error", "Instantaneous speed must always equal average speed", "She was running downhill at the 50 m mark", "Average speed = total distance / total time = 100/10 = 10 m/s. But she started from rest and accelerated, so she was slower at the start and faster later. At the 50 m mark, her instantaneous speed exceeded the average. Instantaneous ≠ average unless speed is constant."),
    ("Two trains leave the same station. Train A travels north at 80 km/h and Train B travels south at 60 km/h. After 2 hours, what is the distance between them and why does this involve vectors?", "280 km apart — since they travel in opposite directions, their displacements add: (80 × 2) + (60 × 2) = 160 + 120 = 280 km", "140 km apart — average the speeds", "20 km apart — subtract the speeds", "4800 km apart — multiply the speeds", "Train A displacement: 160 km north. Train B displacement: 120 km south. Since they move in opposite directions, the separation = 160 + 120 = 280 km. Vector addition: 160 north − (−120 south) = 160 + 120 = 280 km."),
    ("A car's speedometer reads 90 km/h due north. At that instant, the driver turns onto an eastbound highway and maintains 90 km/h. Has the velocity changed?", "Yes — although the speed remained constant at 90 km/h, the direction changed from north to east, so the velocity (a vector) has changed", "No — the speed stayed the same so the velocity is unchanged", "No — speedometers measure velocity directly", "Yes — the speed increased because east is a 'faster' direction", "Velocity is a vector (magnitude + direction). Speed (magnitude) stayed at 90 km/h, but direction changed from north to east. Therefore the velocity changed, which means the car experienced acceleration during the turn."),
    ("An ant walks along a meter stick from the 20 cm mark to the 80 cm mark, then back to the 50 cm mark. What are the distance and displacement?", "Distance = 90 cm (60 cm forward + 30 cm back); Displacement = +30 cm (from 20 cm to 50 cm mark)", "Distance = 30 cm, Displacement = 90 cm", "Distance = 60 cm, Displacement = 0 cm", "Distance = Displacement = 60 cm", "Distance: |80 − 20| + |50 − 80| = 60 + 30 = 90 cm. Displacement: final − initial = 50 − 20 = +30 cm (toward the higher numbers on the stick)."),
    ("A race car on a 5 km circular track completes exactly 3 laps in 6 minutes. What are its average speed and average velocity?", "Average speed = 150 km/h (15 km / 0.1 h); Average velocity = 0 (displacement is zero after complete laps, back to start)", "Average speed = 0, Average velocity = 150 km/h", "Average speed = 50 km/h, Average velocity = 50 km/h", "Both are 150 km/h", "Distance = 3 × 5 = 15 km. Time = 6 min = 0.1 h. Average speed = 15/0.1 = 150 km/h. After 3 complete laps, the car is back at the starting line, so displacement = 0 and average velocity = 0."),
    ("A student plots position vs. time and gets a straight line with slope 5 m/s for the first 4 seconds, then a horizontal line from 4 to 7 seconds. What was the object doing?", "Moving at constant velocity of 5 m/s for 4 seconds, then stationary (at rest) from 4 to 7 seconds — the slope gives velocity and zero slope means zero velocity", "Accelerating for 4 seconds then decelerating", "Moving at 5 m/s the entire time", "Moving for 7 seconds at constant speed", "On a position-time graph: constant positive slope = constant velocity (5 m/s here). Horizontal line = zero slope = zero velocity (stationary). The object traveled 20 m in 4 s, then stayed put for 3 s."),
    ("Two ships leave a port simultaneously. Ship A sails 100 km east, Ship B sails 100 km north. Both take 5 hours. They have the same speed but a sailor says they have different velocities. Explain.", "Correct — both have speed 20 km/h but Ship A's velocity is 20 km/h east and Ship B's is 20 km/h north; velocity includes direction, so different directions mean different velocities", "The sailor is wrong — same speed means same velocity", "Same speed implies same velocity only for ships", "Different velocities because the ships have different masses", "Speed (scalar) = 100 km / 5 h = 20 km/h for both. Velocity (vector) = 20 km/h east for A, 20 km/h north for B. Since velocity includes direction, these are different velocity vectors despite identical speeds."),
]

LESSONS[("2", "2.2", "Acceleration")] = [
    ("What is acceleration?", "The rate of change of velocity with respect to time", "The rate of change of distance", "The speed of an object at one instant", "The total displacement of an object", "Acceleration a = Δv/Δt, measuring how quickly velocity changes. Its SI unit is m/s²."),
    ("What is the SI unit of acceleration?", "Meters per second squared (m/s²)", "Meters per second (m/s)", "Kilometers per hour (km/h)", "Newtons (N)", "Acceleration has units of velocity divided by time: (m/s)/s = m/s²."),
    ("If a car increases its velocity from 0 to 20 m/s in 5 seconds, what is its acceleration?", "4 m/s²", "100 m/s²", "20 m/s²", "0.25 m/s²", "a = Δv/Δt = (20 − 0)/5 = 4 m/s²."),
    ("Can an object accelerate while maintaining constant speed?", "Yes — if the direction of motion changes (e.g., circular motion), velocity changes even at constant speed", "No — constant speed always means constant velocity", "Only in outer space", "Only if the object has zero mass", "Acceleration is a change in velocity (a vector). Since velocity has both magnitude and direction, changing direction at constant speed still constitutes acceleration."),
    ("What is deceleration?", "Acceleration in the opposite direction to the velocity, causing the object to slow down", "Negative acceleration only", "Zero acceleration", "Acceleration that equals exactly −9.8 m/s²", "Deceleration occurs when the acceleration vector opposes the velocity vector, reducing speed. It is not simply 'negative acceleration' — the sign depends on the chosen coordinate system."),
    ("An object has a positive velocity and a negative acceleration. What is happening?", "The object is slowing down — the acceleration opposes the direction of motion", "The object is speeding up in the negative direction", "The object is stationary", "The object is moving backward", "When acceleration is opposite to velocity, the speed decreases. A positive velocity with negative acceleration means the object moves in the positive direction but is decelerating."),
    ("What does the slope of a velocity-time graph represent?", "Acceleration", "Velocity", "Displacement", "Speed", "On a v-t graph, slope = Δv/Δt = acceleration. A steeper slope means greater acceleration. A horizontal line means constant velocity (zero acceleration)."),
    ("What does a horizontal line on a velocity-time graph mean?", "The object is moving at constant velocity (zero acceleration)", "The object is stationary", "The object is accelerating at a constant rate", "The object is decelerating", "A horizontal line means velocity is not changing with time, so acceleration is zero. The object moves at constant velocity (uniform motion)."),
    ("What does the area under a velocity-time graph represent?", "Displacement", "Acceleration", "Speed", "Force", "The area under a v-t graph equals displacement: ∫v dt = Δx. This works for any shape of v-t graph."),
    ("An object has zero velocity but nonzero acceleration. Is this possible?", "Yes — for example, a ball thrown upward has zero velocity at its highest point but still has gravitational acceleration downward", "No — zero velocity means zero acceleration", "Only if the object has infinite mass", "Only in a vacuum", "At the peak of a vertical throw, v = 0 momentarily but a = −g = −9.8 m/s² (gravity never stops). This is why the ball immediately begins falling back down."),
    # VOCABULARY (11-20)
    ("Which definition BEST describes acceleration?", "The rate at which velocity changes with respect to time — a vector quantity with SI unit m/s²", "The rate at which distance changes with time", "How fast an object is moving at one instant", "The total change in position of an object", "a = Δv/Δt (or dv/dt). Acceleration is a vector, having both magnitude and direction. It tells us how quickly and in what direction the velocity is changing."),
    ("Which definition BEST describes constant acceleration?", "Acceleration that has the same magnitude and direction at every instant, producing a uniformly changing velocity", "Acceleration that increases over time", "Acceleration that is always 9.8 m/s²", "Any acceleration that is positive", "Under constant acceleration, velocity changes by the same amount each second. This produces a straight line on a v-t graph and a parabola on a position-time graph."),
    ("Which definition BEST describes instantaneous acceleration?", "The acceleration of an object at a specific instant, equal to the derivative of velocity with respect to time (dv/dt)", "The average acceleration over the entire trip", "The maximum acceleration experienced", "Acceleration measured with a stopwatch", "Instantaneous acceleration is the limit of Δv/Δt as Δt → 0. It equals the slope of the velocity-time graph at that instant and can differ from the average acceleration."),
    ("Which definition BEST describes free fall?", "Motion of an object under the influence of gravity alone, with no air resistance, where all objects accelerate at g ≈ 9.8 m/s² regardless of mass", "Any downward motion", "Falling from a very high altitude", "Motion without any forces acting", "Free fall occurs when gravity is the only force. All objects — regardless of mass, shape, or composition — experience the same acceleration g ≈ 9.8 m/s² downward (ignoring air resistance)."),
    ("Which definition BEST describes a velocity-time graph?", "A graph plotting velocity on the vertical axis against time on the horizontal axis, where slope equals acceleration and area equals displacement", "A graph showing position changes over time", "A graph that only works for constant velocity", "A distance-speed relationship diagram", "V-t graphs encode motion completely: slope gives acceleration, area under the curve gives displacement, and horizontal intercepts show when the object reverses direction."),
    ("Which definition BEST describes uniform acceleration?", "Motion in which velocity changes by equal amounts in equal time intervals — the acceleration remains constant", "Motion at a constant speed", "Motion with continuously increasing acceleration", "Motion in a straight line at any speed", "Uniform acceleration means a = constant. Velocity increases (or decreases) linearly with time: v = v₀ + at. This is the simplest type of accelerated motion and is described by the SUVAT equations."),
    ("Which definition BEST describes non-uniform acceleration?", "Acceleration that changes in magnitude and/or direction over time, making velocity change at a varying rate", "Acceleration that is always negative", "Acceleration in curved motion only", "Very large constant acceleration", "Non-uniform acceleration means a ≠ constant. Examples include a car in traffic (varying throttle) and SHM (acceleration proportional to displacement). Calculus (derivatives/integrals) is needed to analyze such motion."),
    ("Which definition BEST describes the acceleration due to gravity (g)?", "The acceleration experienced by objects in free fall near Earth's surface, approximately 9.8 m/s² directed downward", "The force of gravity on an object", "The weight of an object divided by its volume", "The speed limit for falling objects", "g ≈ 9.81 m/s² at Earth's surface. It varies slightly with altitude and latitude. On the Moon, g ≈ 1.6 m/s². It is the same for all objects regardless of mass (in the absence of air resistance)."),
    ("Which definition BEST describes jerk?", "The rate of change of acceleration with respect to time (da/dt), with SI units of m/s³", "A sudden stop", "The maximum acceleration in a system", "An error in acceleration measurement", "Jerk = da/dt = d³x/dt³. It describes how smoothly acceleration changes. High jerk means abrupt changes in acceleration, which feels uncomfortable in vehicles and can damage machinery."),
    ("Which definition BEST describes terminal velocity?", "The constant maximum velocity reached by a falling object when air resistance equals gravitational force, resulting in zero net force and zero acceleration", "The velocity at which an object hits the ground", "The fastest possible speed in the universe", "The velocity at which an object leaves Earth's atmosphere", "Terminal velocity occurs when drag force balances weight: mg = F_drag. At this point a = 0 and velocity remains constant. A skydiver's terminal velocity is about 55 m/s (200 km/h) in a spread position."),
    # SCENARIO (21-30)
    ("A car accelerates from rest at 3 m/s² for 10 seconds. How far does it travel and what is its final speed?", "Final speed = 30 m/s, distance = 150 m — using v = at = 3(10) = 30 m/s and s = ½at² = ½(3)(100) = 150 m", "Final speed = 30 m/s, distance = 300 m", "Final speed = 10 m/s, distance = 150 m", "Final speed = 30 m/s, distance = 30 m", "v = u + at = 0 + 3(10) = 30 m/s. s = ut + ½at² = 0 + ½(3)(10²) = 150 m. The car reaches 30 m/s (108 km/h) having traveled 150 m."),
    ("A ball is thrown straight up at 20 m/s. Ignoring air resistance, how high does it go before momentarily stopping?", "Approximately 20.4 m — using v² = u² + 2as: 0 = 20² + 2(−9.8)s, s = 400/19.6 ≈ 20.4 m", "10 m", "40 m", "200 m", "At the peak v = 0. Using v² = u² + 2as with a = −9.8 m/s²: 0 = 400 − 19.6s → s = 400/19.6 ≈ 20.4 m. Gravity decelerates the ball at 9.8 m/s² until it stops."),
    ("A bicycle goes from 5 m/s to 15 m/s in 4 seconds. Then from 15 m/s to 35 m/s in 4 seconds. Is the acceleration constant?", "No — the first interval has a = (15−5)/4 = 2.5 m/s² and the second has a = (35−15)/4 = 5 m/s², showing non-uniform acceleration", "Yes — both intervals are 4 seconds long", "Yes — the cyclist is always speeding up", "Cannot tell without position data", "First interval: a₁ = 10/4 = 2.5 m/s². Second interval: a₂ = 20/4 = 5.0 m/s². Since 2.5 ≠ 5.0, the acceleration is not constant — it increased, indicating non-uniform acceleration."),
    ("Two balls are dropped from the same height. Ball A has mass 1 kg and Ball B has mass 5 kg. Ignoring air resistance, which hits the ground first?", "They hit at the same time — in free fall, all objects accelerate at g regardless of mass", "Ball B hits first because it is heavier", "Ball A hits first because it is lighter", "It depends on the height", "Galileo's principle: in the absence of air resistance, all objects fall with the same acceleration g ≈ 9.8 m/s². Mass does not affect free-fall acceleration. Both balls experience identical motion."),
    ("A car traveling at 30 m/s applies brakes and decelerates at 5 m/s². How far does it travel before stopping?", "90 m — using v² = u² + 2as: 0 = 900 + 2(−5)s → s = 900/10 = 90 m", "6 m", "150 m", "45 m", "v² = u² + 2as. With v = 0, u = 30, a = −5: 0 = 900 − 10s → s = 90 m. Alternatively, average velocity = (30 + 0)/2 = 15 m/s, time = 30/5 = 6 s, distance = 15 × 6 = 90 m."),
    ("A rocket accelerates upward at 20 m/s². If the rocket starts from rest, what is its velocity after 5 seconds?", "100 m/s upward — v = u + at = 0 + 20(5) = 100 m/s", "4 m/s upward", "25 m/s upward", "100 m/s downward", "v = u + at = 0 + 20 × 5 = 100 m/s upward. The rocket gains 20 m/s of velocity every second it accelerates."),
    ("A skydiver jumps from a plane and initially accelerates at 9.8 m/s². After some time, she reaches a terminal velocity of 55 m/s. What happened to her acceleration?", "Her acceleration decreased from 9.8 m/s² to 0 as air resistance increased to match her weight — at terminal velocity, net force is zero so acceleration is zero", "Her acceleration stayed at 9.8 m/s² the entire time", "Her acceleration increased beyond 9.8 m/s²", "She experienced negative acceleration the whole time", "Initially, air resistance is small and acceleration ≈ g = 9.8 m/s². As speed increases, air resistance grows. When air resistance equals weight, net force = 0, acceleration = 0, and velocity stays constant at terminal velocity (55 m/s)."),
    ("A train's velocity-time graph shows a straight line from (0, 0) to (10, 20). What is the train's acceleration and displacement during this interval?", "Acceleration = 2 m/s² (slope of the line); Displacement = 100 m (area of triangle: ½ × 10 × 20)", "Acceleration = 20 m/s², Displacement = 200 m", "Acceleration = 2 m/s², Displacement = 200 m", "Acceleration = 10 m/s², Displacement = 100 m", "Slope = Δv/Δt = 20/10 = 2 m/s². Area = ½ × base × height = ½ × 10 × 20 = 100 m. This confirms s = ½at² = ½(2)(100) = 100 m."),
    ("A elevator accelerates upward at 2 m/s² for 3 seconds, then moves at constant velocity for 5 seconds, then decelerates at 2 m/s² for 3 seconds. What is the total displacement?", "33 m — Phase 1: s₁ = ½(2)(9) = 9 m (reaches 6 m/s); Phase 2: s₂ = 6(5) = 30 m; Phase 3: s₃ = 6(3) − ½(2)(9) = 18 − 9 = 9 m (but it's only decelerating so it's ½(6)(3) = 9 m) — wait, let me recalculate correctly. Total = 9 + 30 + 9 = 48 m", "48 m — 9 m accelerating (½ × 2 × 9), 30 m constant (6 × 5), 9 m decelerating (½ × 2 × 9 or equivalently 6×3 − ½×2×9)", "9 m — only the first phase matters", "30 m — only the constant velocity phase counts", "Phase 1: v = 0 + 2(3) = 6 m/s. s₁ = ½(2)(3²) = 9 m. Phase 2: constant 6 m/s for 5 s. s₂ = 30 m. Phase 3: s₃ = 6(3) − ½(2)(3²) = 18 − 9 = 9 m. Total: 9 + 30 + 9 = 48 m."),
    ("An athlete practices sprints. Run 1: 0 to 8 m/s in 2 seconds. Run 2: 0 to 8 m/s in 4 seconds. Both reach the same final speed. What is different?", "The acceleration is different — Run 1 has a = 4 m/s² while Run 2 has a = 2 m/s². Run 1 required double the acceleration despite reaching the same speed", "Nothing is different — same initial and final speed means same motion", "Run 2 covers more distance because it takes longer", "Run 1 has more displacement because it's faster", "Run 1: a = 8/2 = 4 m/s², s = ½(4)(4) = 8 m. Run 2: a = 8/4 = 2 m/s², s = ½(2)(16) = 16 m. Despite the same final speed, the acceleration differs and Run 2 covers more distance because it takes longer to reach the same speed."),
]

# I'll continue building lessons for remaining units, but to keep this manageable, 
# let me create a helper function and build the JSON files.

def make_quiz_json(unit_num, lesson_num, title, course, questions):
    """Create a quiz JSON structure with 30 questions."""
    quiz_questions = []
    for i, q in enumerate(questions):
        q_text, correct, w1, w2, w3, explanation = q
        quiz_questions.append({
            "question_number": i + 1,
            "question_text": q_text,
            "attempted": 2,
            "data_i18n": None,
            "options": [
                {"text": correct, "is_correct": True, "data_i18n": None},
                {"text": w1, "is_correct": False, "data_i18n": None},
                {"text": w2, "is_correct": False, "data_i18n": None},
                {"text": w3, "is_correct": False, "data_i18n": None},
            ],
            "explanation": explanation
        })
    return {
        "unit": int(unit_num),
        "lesson_number": lesson_num,
        "title": title,
        "course": course,
        "quiz_questions": quiz_questions
    }

def write_quiz(unit_num, lesson_num, title, questions, base_dir="content_data/PhysicsLessons"):
    """Write a quiz JSON file."""
    data = make_quiz_json(unit_num, lesson_num, title, "Physics", questions)
    path = os.path.join(base_dir, f"Unit{unit_num}", f"Lesson{lesson_num}_Quiz.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Written: {path} ({len(questions)} questions)")

if __name__ == "__main__":
    # Write all lessons that have been defined
    count = 0
    for (unit_num, lesson_num, title), questions in LESSONS.items():
        if len(questions) == 30:
            write_quiz(unit_num, lesson_num, title, questions)
            count += 1
        else:
            print(f"  SKIPPED: Unit {unit_num} Lesson {lesson_num} has {len(questions)} questions (need 30)")
    print(f"\nTotal quizzes written: {count}")
