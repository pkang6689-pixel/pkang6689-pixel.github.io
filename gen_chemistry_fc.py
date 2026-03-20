"""Add flashcards to all 83 Chemistry lessons."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "chemistry_lessons.json")

FC = {
    # ── Unit 1: Matter ──────────────────────────────────────────────
    "u1_l1.1": [
        ("Solid", "Matter with definite shape and definite volume; particles vibrate in fixed positions."),
        ("Liquid", "Matter with definite volume but indefinite shape; particles slide past each other."),
        ("Gas", "Matter with no definite shape or volume; particles move freely and fill containers."),
        ("Plasma", "An ionized gas of free electrons and ions; the most common state of matter in the universe."),
        ("Phase", "A physically distinct form of matter (solid, liquid, gas, plasma)."),
    ],
    "u1_l1.2": [  # Phase Changes
        ("Melting", "Transition from solid to liquid; requires energy (endothermic)."),
        ("Freezing", "Transition from liquid to solid; releases energy (exothermic)."),
        ("Evaporation", "Transition from liquid to gas at the surface; endothermic."),
        ("Condensation", "Transition from gas to liquid; exothermic."),
        ("Sublimation", "Transition directly from solid to gas without passing through the liquid phase."),
    ],
    "u1_l1.3": [
        ("Intensive Property", "A property that does NOT depend on the amount of substance (density, color, boiling point)."),
        ("Extensive Property", "A property that DOES depend on the amount of substance (mass, volume, length)."),
        ("Density", "Mass per unit volume (d = m/v); an intensive property."),
        ("Boiling Point", "The temperature at which a liquid becomes a gas; an intensive property."),
        ("Melting Point", "The temperature at which a solid becomes a liquid; an intensive property."),
    ],
    "u1_l1.4": [  # Density
        ("Density Formula", "d = m/v; mass divided by volume. Units: g/mL or g/cm³."),
        ("Water Density", "1.00 g/mL at 4°C — the standard reference for liquid density."),
        ("Float vs Sink", "An object floats if its density is less than the fluid; sinks if greater."),
        ("Volume by Displacement", "Measuring an irregular object's volume by the water it displaces."),
        ("Density Units", "Common units: g/mL, g/cm³, kg/m³. 1 g/mL = 1 g/cm³."),
    ],
    "u1_l1.5": [
        ("Heterogeneous Mixture", "A mixture with visibly different components throughout (trail mix, salad)."),
        ("Homogeneous Mixture", "A mixture with uniform composition throughout; also called a solution (salt water)."),
        ("Solution", "A homogeneous mixture of a solute dissolved in a solvent."),
        ("Colloid", "A mixture with particles that are larger than in a solution but don't settle (milk, fog)."),
        ("Suspension", "A mixture with large particles that eventually settle out (muddy water)."),
    ],
    "u1_l1.6": [  # Practice Review
        ("Element", "A pure substance made of one type of atom; listed on the periodic table."),
        ("Compound", "A substance made of two or more elements chemically bonded in a fixed ratio."),
        ("Mixture", "Two or more substances physically combined; can be separated by physical means."),
        ("Pure Substance", "Matter with a constant composition — either an element or a compound."),
        ("Physical Separation", "Separating mixtures using physical methods: filtration, distillation, evaporation."),
    ],
    "u1_l1.7": [  # Chemical vs Physical Changes
        ("Physical Change", "A change in form or appearance without changing the substance's identity (melting ice)."),
        ("Chemical Change", "A change that produces a new substance with different properties (burning, rusting)."),
        ("Signs of Chemical Change", "Color change, gas production, precipitate formation, temperature/energy change, odor change."),
        ("Reversibility", "Physical changes are usually reversible; chemical changes are usually irreversible."),
        ("Law of Conservation of Mass", "Mass is neither created nor destroyed in a chemical reaction."),
    ],
    "u1_l1.8": [  # Energy & Matter
        ("Kinetic Energy", "Energy of motion; increases with temperature as particles move faster."),
        ("Potential Energy", "Stored energy due to position or chemical bonds."),
        ("Endothermic", "A process that absorbs heat from surroundings (melting, evaporation)."),
        ("Exothermic", "A process that releases heat to surroundings (freezing, condensation, combustion)."),
        ("Thermal Energy", "Total kinetic energy of all particles in a substance; proportional to temperature."),
    ],

    # ── Unit 2: Measurement ─────────────────────────────────────────
    "u2_l2.1": [
        ("Scientific Notation", "Expressing numbers as a × 10ⁿ where 1 ≤ a < 10."),
        ("Coefficient", "The number 'a' in scientific notation (must be 1–9.999…)."),
        ("Exponent", "The power of 10 in scientific notation; positive for large, negative for small numbers."),
        ("Standard Form", "The regular decimal notation of a number (e.g., 602,000,000,000,000,000,000,000)."),
        ("Order of Magnitude", "The power of 10 closest to a quantity; used for quick comparisons."),
    ],
    "u2_l2.2": [
        ("Significant Figures", "All digits known with certainty plus one estimated digit in a measurement."),
        ("Non-zero Rule", "All non-zero digits are significant."),
        ("Leading Zeros", "Zeros before the first non-zero digit are NOT significant (0.0045 has 2 sig figs)."),
        ("Trailing Zeros", "Zeros after a decimal point ARE significant (2.500 has 4 sig figs)."),
        ("Multiplication Rule", "The answer has the same number of sig figs as the least precise measurement."),
    ],
    "u2_l2.3": [  # Accuracy vs Precision
        ("Accuracy", "How close a measurement is to the true (accepted) value."),
        ("Precision", "How close repeated measurements are to each other."),
        ("Percent Error", "|(Experimental − Accepted) / Accepted| × 100%."),
        ("Systematic Error", "A consistent, repeatable error in the same direction (miscalibrated instrument)."),
        ("Random Error", "Irregular, unpredictable deviations that average out over many measurements."),
    ],
    "u2_l2.4": [  # The Metric System
        ("SI System", "The International System of Units — the standard system of measurement in science."),
        ("Kilo-", "SI prefix meaning 1,000 (10³). 1 kg = 1,000 g."),
        ("Centi-", "SI prefix meaning 1/100 (10⁻²). 1 cm = 0.01 m."),
        ("Milli-", "SI prefix meaning 1/1,000 (10⁻³). 1 mL = 0.001 L."),
        ("Base Units", "Fundamental SI units: meter (m), kilogram (kg), second (s), kelvin (K), mole (mol)."),
    ],
    "u2_l2.5": [
        ("Dimensional Analysis", "A problem-solving method using conversion factors to switch between units."),
        ("Conversion Factor", "A ratio equal to 1 used to convert units (e.g., 1 km / 1000 m)."),
        ("Unit Cancellation", "Arranging conversion factors so unwanted units cancel out."),
        ("Multi-step Conversion", "Chaining multiple conversion factors to go from one unit to another."),
        ("Derived Unit", "A unit formed by combining base units (e.g., m/s for speed, kg/m³ for density)."),
    ],

    # ── Unit 3: Atomic Structure ────────────────────────────────────
    "u3_l3.1": [  # Electrons, Protons & Neutrons
        ("Proton", "A positively charged subatomic particle in the nucleus; defines the element (atomic number)."),
        ("Neutron", "A neutral subatomic particle in the nucleus; contributes to mass number."),
        ("Electron", "A negatively charged particle orbiting the nucleus; determines bonding and chemistry."),
        ("Atomic Number", "The number of protons in the nucleus of an atom; identifies the element."),
        ("Mass Number", "The total number of protons + neutrons in an atom's nucleus."),
    ],
    "u3_l3.2": [  # Atomic Structure
        ("Nucleus", "The dense central core of an atom containing protons and neutrons."),
        ("Electron Cloud", "The region around the nucleus where electrons are likely to be found."),
        ("Energy Level", "A fixed region around the nucleus where electrons with a specific energy are found (n = 1, 2, 3…)."),
        ("Atomic Radius", "The distance from the nucleus to the outermost electron; decreases across a period."),
        ("Ion", "An atom that has gained or lost electrons, giving it a net electric charge."),
    ],
    "u3_l3.3": [  # Quantum Mechanical Model
        ("Orbital", "A three-dimensional region around the nucleus where an electron is most likely found."),
        ("s Orbital", "A spherical orbital that holds up to 2 electrons; exists in every energy level."),
        ("p Orbital", "A dumbbell-shaped orbital; three per energy level (starting at n = 2), holding up to 6 electrons."),
        ("Heisenberg Uncertainty Principle", "It's impossible to simultaneously know both the exact position and momentum of an electron."),
        ("Quantum Numbers", "Four numbers (n, l, mₗ, mₛ) that describe the state of an electron in an atom."),
    ],
    "u3_l3.4": [  # EM Spectrum & Emission Spectra
        ("Electromagnetic Spectrum", "The range of all EM radiation: radio, microwave, IR, visible, UV, X-ray, gamma."),
        ("Wavelength (λ)", "The distance between successive wave crests; measured in nm or m."),
        ("Frequency (ν)", "The number of wave crests passing a point per second; measured in Hz."),
        ("Photon", "A particle (quantum) of electromagnetic radiation; energy E = hν."),
        ("Emission Spectrum", "The set of specific wavelengths emitted by an excited element — a chemical fingerprint."),
    ],
    "u3_l3.5": [
        ("Radioactivity", "The spontaneous emission of particles or energy from an unstable nucleus."),
        ("Nuclear Stability", "A nucleus is stable when the strong nuclear force overcomes proton-proton repulsion."),
        ("Band of Stability", "The region on a neutron-vs-proton graph where stable nuclei are found."),
        ("Radioactive Decay", "The process by which an unstable nucleus loses energy by emitting radiation."),
        ("Nuclear Force", "The strong force that holds protons and neutrons together in the nucleus."),
    ],
    "u3_l3.6": [
        ("Isotope", "Atoms of the same element with different numbers of neutrons (same Z, different A)."),
        ("Radioisotope", "An isotope with an unstable nucleus that undergoes radioactive decay."),
        ("Atomic Mass", "The weighted average mass of all naturally occurring isotopes of an element (in amu)."),
        ("Mass Spectrometer", "An instrument that measures the masses and relative abundances of isotopes."),
        ("Carbon-14", "A radioisotope used in radiocarbon dating of organic remains (half-life ≈ 5,730 years)."),
    ],
    "u3_l3.7": [  # Element Synthesis
        ("Particle Accelerator", "A device that accelerates charged particles to high speeds, used to create new elements."),
        ("Transuranium Element", "An element with atomic number greater than 92 (uranium); all are synthetic."),
        ("Nuclear Fusion", "Combining light nuclei to form a heavier nucleus; powers stars."),
        ("Nucleosynthesis", "The formation of elements in stars through nuclear reactions."),
        ("Superheavy Elements", "Elements beyond Z = 103; created in labs, very unstable, short-lived."),
    ],
    "u3_l3.8": [
        ("Dalton's Atomic Theory", "All matter is made of indivisible atoms; atoms of the same element are identical."),
        ("Thomson Model", "The 'plum pudding' model — electrons embedded in a positive sphere."),
        ("Rutherford Model", "Discovered the dense, positive nucleus via the gold foil experiment (1911)."),
        ("Bohr Model", "Electrons orbit the nucleus in fixed energy levels; explained hydrogen spectrum."),
        ("Quantum Mechanical Model", "Current model: electrons exist in probability orbitals, not fixed orbits."),
    ],

    # ── Unit 4: Periodic Table ──────────────────────────────────────
    "u4_l4.1": [
        ("Chemical Symbol", "A one- or two-letter abbreviation for an element (e.g., Na, Cl, Fe)."),
        ("Periodic Table", "A tabular arrangement of elements by increasing atomic number and recurring properties."),
        ("Group/Family", "A vertical column on the periodic table; elements share similar chemical properties."),
        ("Period", "A horizontal row on the periodic table; properties change systematically across."),
        ("Atomic Notation", "Writing an element with its mass number and atomic number (e.g., ¹²₆C)."),
    ],
    "u4_l4.2": [
        ("Metals", "Elements that are shiny, malleable, ductile, and good conductors; left/center of table."),
        ("Nonmetals", "Elements that are dull, brittle, poor conductors; upper right of table."),
        ("Metalloids", "Elements with properties between metals and nonmetals (B, Si, Ge, As, Sb, Te, Po)."),
        ("Alkali Metals", "Group 1: highly reactive metals with 1 valence electron (Li, Na, K, etc.)."),
        ("Noble Gases", "Group 18: very stable, unreactive gases with full valence shells (He, Ne, Ar, etc.)."),
    ],
    "u4_l4.3": [
        ("Valence Electron", "An electron in the outermost energy level; determines an element's reactivity."),
        ("Octet Rule", "Atoms tend to gain, lose, or share electrons to have 8 valence electrons."),
        ("Reactivity of Metals", "Increases down a group (easier to lose electrons)."),
        ("Reactivity of Nonmetals", "Increases up a group and to the right (easier to gain electrons)."),
        ("Halogen", "Group 17 elements; very reactive nonmetals with 7 valence electrons (F, Cl, Br, I)."),
    ],
    "u4_l4.4": [  # Electron Suborbitals
        ("Sublevel/Subshell", "Divisions within energy levels: s, p, d, f with increasing energy."),
        ("s Subshell", "Holds up to 2 electrons in 1 orbital; present in all energy levels."),
        ("p Subshell", "Holds up to 6 electrons in 3 orbitals; starts at n = 2."),
        ("d Subshell", "Holds up to 10 electrons in 5 orbitals; starts at n = 3."),
        ("f Subshell", "Holds up to 14 electrons in 7 orbitals; starts at n = 4."),
    ],
    "u4_l4.5": [
        ("Electron Configuration", "The arrangement of electrons in an atom's orbitals (e.g., 1s² 2s² 2p⁶ 3s¹ for Na)."),
        ("Aufbau Principle", "Electrons fill the lowest energy orbitals first."),
        ("Pauli Exclusion Principle", "No two electrons in an atom can have all four quantum numbers identical (max 2 per orbital)."),
        ("Hund's Rule", "Electrons fill orbitals of equal energy singly before pairing up."),
        ("Noble Gas Shorthand", "Writing electron configuration using the preceding noble gas (e.g., [Ne] 3s¹ for Na)."),
    ],
    "u4_l4.6": [
        ("Ionization Energy", "The energy needed to remove an electron; increases across a period, decreases down a group."),
        ("Electronegativity", "The ability of an atom to attract electrons in a bond; increases across and up (F is highest)."),
        ("Atomic Radius", "The size of an atom; increases down a group, decreases across a period."),
        ("Electron Affinity", "The energy change when an electron is added to a neutral atom."),
        ("Periodic Trend", "A pattern in element properties that repeats across periods and down groups."),
    ],
    "u4_l4.7": [
        ("Shielding Effect", "Inner electrons block outer electrons from the full nuclear charge."),
        ("Effective Nuclear Charge (Zeff)", "The net positive charge experienced by valence electrons; Zeff = Z − shielding."),
        ("Core Electrons", "Inner electrons that shield valence electrons from the nucleus."),
        ("Coulomb's Law (atomic)", "Attraction between nucleus and electron increases with charge, decreases with distance."),
        ("Trend Explanation", "Atoms get smaller across a period because Zeff increases while shielding stays roughly constant."),
    ],
    "u4_l4.8": [  # VSEPR & Molecule Shapes
        ("VSEPR Theory", "Valence Shell Electron Pair Repulsion: electron pairs around a central atom arrange to minimize repulsion."),
        ("Linear", "Molecular shape with a 180° bond angle (e.g., CO₂, BeCl₂)."),
        ("Tetrahedral", "4 bonding pairs, 0 lone pairs → bond angles of 109.5° (e.g., CH₄)."),
        ("Trigonal Planar", "3 bonding pairs, 0 lone pairs → bond angles of 120° (e.g., BF₃)."),
        ("Bent", "A nonlinear shape due to lone pairs on the central atom (e.g., H₂O, 104.5°)."),
    ],
    "u4_l4.9": [  # Suborbital Shapes
        ("s Orbital Shape", "Spherical; one per energy level."),
        ("p Orbital Shape", "Dumbbell-shaped; three per energy level (px, py, pz), mutually perpendicular."),
        ("d Orbital Shape", "Cloverleaf or donut-belt shapes; five per energy level starting at n = 3."),
        ("f Orbital Shape", "Complex multi-lobed shapes; seven per energy level starting at n = 4."),
        ("Node", "A region where the probability of finding an electron is zero."),
    ],

    # ── Unit 6: Chemical Reactions ──────────────────────────────────
    "u6_l6.1": [
        ("Synthesis Reaction", "Two or more reactants combine to form one product: A + B → AB."),
        ("Decomposition Reaction", "One compound breaks down into two or more simpler substances: AB → A + B."),
        ("Single Replacement", "An element replaces another in a compound: A + BC → AC + B."),
        ("Double Replacement", "Two compounds exchange ions: AB + CD → AD + CB."),
        ("Activity Series", "A ranking of elements by their ability to displace others in single replacement reactions."),
    ],
    "u6_l6.2": [
        ("Combustion Reaction", "A substance reacts with oxygen, producing heat and light. Hydrocarbon → CO₂ + H₂O."),
        ("Complete Combustion", "All fuel burns in excess O₂; products are CO₂ and H₂O."),
        ("Incomplete Combustion", "Insufficient O₂; produces CO (carbon monoxide) or C (soot)."),
        ("Hydrocarbon", "An organic compound containing only hydrogen and carbon (e.g., CH₄, C₃H₈)."),
        ("Exothermic Nature", "Combustion always releases energy (exothermic), which is why fuels are useful."),
    ],
    "u6_l6.3": [
        ("Oxidation", "Loss of electrons (increase in oxidation number). 'OIL' — Oxidation Is Loss."),
        ("Reduction", "Gain of electrons (decrease in oxidation number). 'RIG' — Reduction Is Gain."),
        ("Oxidizing Agent", "The substance that is reduced (gains electrons); causes oxidation in others."),
        ("Reducing Agent", "The substance that is oxidized (loses electrons); causes reduction in others."),
        ("Oxidation Number", "A number indicating the apparent charge on an atom in a compound."),
    ],
    "u6_l6.4": [
        ("Activation Energy", "The minimum energy required for reactant molecules to undergo a chemical reaction."),
        ("Catalyst", "A substance that lowers activation energy and speeds up a reaction without being consumed."),
        ("Transition State", "The highest-energy arrangement of atoms during a reaction; unstable intermediate."),
        ("Energy Diagram", "A graph showing energy changes during a reaction (reactants → transition state → products)."),
        ("Exothermic vs Endothermic", "Exothermic: products lower energy than reactants. Endothermic: products higher."),
    ],
    "u6_l6.5": [
        ("Balanced Equation", "A chemical equation with equal numbers of each atom on both sides."),
        ("Coefficient", "A number placed before a formula in a balanced equation to indicate the number of units."),
        ("Law of Conservation of Mass", "In a chemical reaction, total mass of reactants equals total mass of products."),
        ("Subscript", "A number in a chemical formula indicating the number of atoms of an element (H₂O: 2 H's)."),
        ("Balancing Steps", "1) Write unbalanced equation. 2) Count atoms. 3) Add coefficients. 4) Verify."),
    ],
    "u6_l6.6": [  # Reaction Rates & Catalysts
        ("Reaction Rate", "The speed at which reactants are consumed or products are formed."),
        ("Collision Theory", "Reactions occur when particles collide with enough energy and correct orientation."),
        ("Temperature Effect", "Increasing temperature increases kinetic energy and collision frequency → faster reaction."),
        ("Concentration Effect", "Higher concentration means more particles, more collisions, faster reaction."),
        ("Surface Area Effect", "Smaller particle size → greater surface area → faster reaction."),
    ],
    "u6_l6.7": [  # Chemical Equilibrium
        ("Chemical Equilibrium", "A state where forward and reverse reactions occur at equal rates; concentrations stay constant."),
        ("Le Chatelier's Principle", "If a system at equilibrium is stressed, it shifts to partially counteract the stress."),
        ("Reversible Reaction", "A reaction that can proceed in both forward and reverse directions: A + B ⇌ C + D."),
        ("Equilibrium Constant (Keq)", "The ratio of product concentrations to reactant concentrations at equilibrium."),
        ("Shift in Equilibrium", "Adding reactant → shifts right. Adding product → shifts left. Temperature/pressure also cause shifts."),
    ],

    # ── Unit 7: Stoichiometry ───────────────────────────────────────
    "u7_l7.1": [  # Writing Correct Formulas
        ("Cation", "A positively charged ion (lost electrons); metals typically form cations (Na⁺, Ca²⁺)."),
        ("Anion", "A negatively charged ion (gained electrons); nonmetals typically form anions (Cl⁻, O²⁻)."),
        ("Criss-Cross Method", "A technique for writing formulas: swap the charges of the ions as subscripts."),
        ("Polyatomic Ion", "A charged group of covalently bonded atoms (e.g., SO₄²⁻, NH₄⁺, NO₃⁻)."),
        ("Chemical Formula", "A representation showing the types and numbers of atoms in a compound (H₂O, NaCl)."),
    ],
    "u7_l7.2": [
        ("Molar Mass", "The mass of one mole of a substance, in grams per mole (g/mol)."),
        ("Molecular Mass", "The sum of atomic masses of all atoms in a molecular formula."),
        ("Formula Mass", "The sum of atomic masses for an ionic compound's formula unit."),
        ("Atomic Mass Unit (amu)", "One-twelfth the mass of a carbon-12 atom; ~1.66 × 10⁻²⁴ g."),
        ("Calculating Molar Mass", "Add up the atomic masses (from periodic table) of all atoms in the formula."),
    ],
    "u7_l7.3": [
        ("Avogadro's Number", "6.022 × 10²³ — the number of particles in one mole of a substance."),
        ("Mole", "The SI unit for amount of substance; equals 6.022 × 10²³ particles."),
        ("Moles to Particles", "Multiply moles by 6.022 × 10²³."),
        ("Particles to Moles", "Divide number of particles by 6.022 × 10²³."),
        ("One Mole", "12.00 g of C-12; 6.022 × 10²³ atoms, molecules, or formula units."),
    ],
    "u7_l7.4": [  # Molar Conversions
        ("Moles to Grams", "Multiply moles by molar mass (g/mol)."),
        ("Grams to Moles", "Divide grams by molar mass."),
        ("Moles to Liters (gas at STP)", "Multiply moles by 22.4 L/mol."),
        ("STP", "Standard Temperature and Pressure: 0°C (273.15 K) and 1 atm."),
        ("Molar Volume", "At STP, one mole of any ideal gas occupies 22.4 L."),
    ],
    "u7_l7.5": [  # Empirical vs Molecular Formulas
        ("Empirical Formula", "The simplest whole-number ratio of atoms in a compound (e.g., CH₂O for glucose)."),
        ("Molecular Formula", "The actual number of atoms in a molecule (e.g., C₆H₁₂O₆ for glucose)."),
        ("Percent Composition", "The percentage by mass of each element in a compound."),
        ("Finding Empirical Formula", "Convert % to grams → moles → divide by smallest → simplify to whole numbers."),
        ("Empirical to Molecular", "Divide molar mass by empirical formula mass to find the multiplier."),
    ],
    "u7_l7.6": [
        ("Limiting Reagent", "The reactant completely consumed first; determines the maximum yield of product."),
        ("Excess Reagent", "The reactant that remains after the limiting reagent is used up."),
        ("Theoretical Yield", "The maximum amount of product predicted by stoichiometry from the limiting reagent."),
        ("Identifying Limiting Reagent", "Convert both reactants to moles of product; the one giving less product is limiting."),
        ("Stoichiometric Ratio", "The mole ratio of reactants and products from the balanced equation."),
    ],
    "u7_l7.7": [
        ("Stoichiometry", "Calculations relating amounts of reactants and products in a chemical reaction."),
        ("Mole Ratio", "The ratio of moles of one substance to another from the balanced equation coefficients."),
        ("Mass-to-Mass Problem", "Convert given mass → moles → use mole ratio → moles of target → mass."),
        ("Balanced Equation Coefficients", "Provide the mole ratios needed for stoichiometric conversions."),
        ("Dimensional Analysis in Stoich", "Use conversion factors: molar mass and mole ratios to solve problems."),
    ],
    "u7_l7.8": [
        ("Percent Yield", "(Actual yield / Theoretical yield) × 100%."),
        ("Actual Yield", "The amount of product actually obtained from an experiment."),
        ("Theoretical Yield", "The maximum predicted product from stoichiometry."),
        ("Reasons for Low Yield", "Incomplete reactions, side reactions, transfer losses, impure reagents."),
        ("100% Yield", "Rarely achieved; actual yield is almost always less than theoretical."),
    ],

    # ── Unit 8: Gas Laws ────────────────────────────────────────────
    "u8_l8.1": [
        ("Monatomic Gas", "A gas consisting of single atoms (He, Ne, Ar — noble gases)."),
        ("Diatomic Gas", "A gas whose molecules consist of two atoms (H₂, O₂, N₂, F₂, Cl₂, Br₂, I₂)."),
        ("Diatomic Elements", "The seven diatomic elements: H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂ (BrINClHOF)."),
        ("Ideal Gas", "A hypothetical gas whose particles have no volume and no intermolecular forces."),
        ("Gas Behavior", "Gases expand to fill containers, are compressible, and exert pressure."),
    ],
    "u8_l8.2": [  # Pressure
        ("Pressure", "Force per unit area; measured in atm, kPa, mmHg, or psi."),
        ("Standard Atmosphere", "1 atm = 101.325 kPa = 760 mmHg = 760 torr."),
        ("Barometer", "An instrument that measures atmospheric pressure using a column of mercury."),
        ("Manometer", "A device that measures the pressure of an enclosed gas relative to atmospheric pressure."),
        ("STP", "Standard Temperature and Pressure: 0°C (273.15 K) and 1 atm."),
    ],
    "u8_l8.3": [
        ("Kinetic Molecular Theory", "Gas particles are in constant random motion; collisions are perfectly elastic."),
        ("Temperature and KE", "Average kinetic energy of gas particles is directly proportional to absolute temperature (K)."),
        ("Elastic Collision", "A collision where total kinetic energy is conserved (no energy lost)."),
        ("Random Motion", "Gas particles move in straight lines in all directions until they collide."),
        ("Gas Particle Volume", "Negligible compared to the volume of the container (ideal gas assumption)."),
    ],
    "u8_l8.4": [
        ("Boyle's Law", "P₁V₁ = P₂V₂; at constant temperature, pressure and volume are inversely proportional."),
        ("Inverse Relationship", "As one variable increases, the other decreases (P ↑ → V ↓)."),
        ("Constant Temperature", "Boyle's Law requires temperature to remain unchanged (isothermal)."),
        ("Compression", "Decreasing volume increases pressure (more collisions per unit area)."),
        ("Application", "Syringes, breathing mechanics, hydraulic systems."),
    ],
    "u8_l8.5": [
        ("Charles' Law", "V₁/T₁ = V₂/T₂; at constant pressure, volume is directly proportional to temperature (K)."),
        ("Direct Relationship", "As temperature increases, volume increases (V ↑ when T ↑)."),
        ("Absolute Zero", "0 K (−273.15°C) — the theoretical temperature where gas volume would be zero."),
        ("Kelvin Scale", "The absolute temperature scale; K = °C + 273.15. Must use Kelvin in gas laws."),
        ("Application", "Hot air balloons rise because heated air expands, becoming less dense."),
    ],
    "u8_l8.6": [
        ("Gay-Lussac's Law", "P₁/T₁ = P₂/T₂; at constant volume, pressure is directly proportional to temperature (K)."),
        ("Constant Volume", "The container's volume doesn't change (e.g., a rigid sealed container)."),
        ("Pressure-Temperature Link", "Heating a gas in a rigid container increases pressure (more energetic collisions)."),
        ("Application", "Pressure cookers, tire pressure increasing on hot days."),
        ("Safety Concern", "Aerosol cans can explode if heated — Gay-Lussac's Law in action."),
    ],
    "u8_l8.7": [
        ("Combined Gas Law", "(P₁V₁)/T₁ = (P₂V₂)/T₂; combines Boyle's, Charles', and Gay-Lussac's laws."),
        ("When to Use", "Use when pressure, volume, AND temperature all change."),
        ("Deriving Individual Laws", "Hold one variable constant to get Boyle's (T), Charles' (P), or Gay-Lussac's (V)."),
        ("Units Required", "T must be in Kelvin; P and V can be any consistent units."),
        ("Problem-Solving", "Identify which variables change, plug in known values, solve for the unknown."),
    ],
    "u8_l8.8": [
        ("Ideal Gas Law", "PV = nRT; relates pressure, volume, moles, and temperature of an ideal gas."),
        ("R (Gas Constant)", "0.0821 L·atm/(mol·K) or 8.314 J/(mol·K)."),
        ("n (Moles)", "The amount of gas in moles."),
        ("Applications", "Calculate any one variable (P, V, n, or T) if the other three are known."),
        ("Ideal vs Real", "Works well at high T and low P; real gases deviate at high P and low T."),
    ],
    "u8_l8.9": [  # Real Gases
        ("Real Gas", "An actual gas whose behavior deviates from the ideal gas law at high P or low T."),
        ("Intermolecular Forces", "Attractions between gas molecules; cause real gases to occupy less volume than predicted."),
        ("Particle Volume", "At high pressures, the actual volume of gas particles becomes significant."),
        ("Van der Waals Equation", "(P + a/V²)(V − b) = nRT — corrects for intermolecular forces (a) and particle volume (b)."),
        ("When Gases Are Most Ideal", "At high temperatures and low pressures."),
    ],

    # ── Unit 9: Solutions ───────────────────────────────────────────
    "u9_l9.1": [  # Solution Nomenclature
        ("Solute", "The substance being dissolved (usually in smaller amount)."),
        ("Solvent", "The substance doing the dissolving (usually in larger amount — often water)."),
        ("Aqueous Solution", "A solution where water is the solvent."),
        ("Dissolution", "The process of a solute dissolving in a solvent."),
        ("Like Dissolves Like", "Polar solvents dissolve polar/ionic solutes; nonpolar dissolves nonpolar."),
    ],
    "u9_l9.2": [
        ("Concentration", "The amount of solute dissolved in a given amount of solution."),
        ("Molarity (M)", "Moles of solute per liter of solution: M = mol/L."),
        ("Mass Percent", "(mass of solute / mass of solution) × 100%."),
        ("Parts Per Million (ppm)", "(mass of solute / mass of solution) × 10⁶; used for very dilute solutions."),
        ("Concentrated vs Dilute", "Concentrated: high solute ratio. Dilute: low solute ratio."),
    ],
    "u9_l9.3": [
        ("Dilution", "Adding solvent to reduce the concentration of a solution."),
        ("Dilution Equation", "M₁V₁ = M₂V₂; moles of solute remain constant during dilution."),
        ("Stock Solution", "A concentrated solution that will be diluted to a lower concentration."),
        ("Serial Dilution", "A series of successive dilutions, each reducing concentration by a fixed ratio."),
        ("Application", "Making lab solutions at desired concentrations from concentrated stock."),
    ],
    "u9_l9.4": [
        ("Molarity", "Moles of solute per liter of solution (mol/L); most common concentration unit in chemistry."),
        ("Calculating Molarity", "M = mol of solute / V of solution (in liters)."),
        ("Finding Moles from Molarity", "mol = M × V (liters)."),
        ("Finding Volume from Molarity", "V = mol / M."),
        ("Using Molarity in Stoichiometry", "Convert volume + molarity to moles, then use mole ratios."),
    ],
    "u9_l9.5": [  # Solution Types
        ("Saturated Solution", "Contains the maximum amount of solute that can dissolve at a given temperature."),
        ("Unsaturated Solution", "Contains less solute than the maximum; more can dissolve."),
        ("Supersaturated Solution", "Contains more dissolved solute than normally possible; unstable — crystallizes if disturbed."),
        ("Solubility", "The maximum amount of solute that dissolves in a given amount of solvent at a specific temperature."),
        ("Solubility Rules", "Guidelines predicting whether ionic compounds dissolve in water (e.g., all Na⁺ salts are soluble)."),
    ],
    "u9_l9.6": [
        ("Temperature and Solubility", "Solubility of solids generally increases with temperature; gases decrease."),
        ("Pressure and Solubility", "Henry's Law: gas solubility increases with pressure (e.g., CO₂ in soda)."),
        ("Agitation", "Stirring increases the rate of dissolving (exposes fresh solvent to solute)."),
        ("Particle Size", "Smaller solute particles dissolve faster (greater surface area)."),
        ("Nature of Solute/Solvent", "Polar-polar and nonpolar-nonpolar pairs dissolve well; unlike pairs do not."),
    ],
    "u9_l9.7": [
        ("Colligative Property", "A property that depends on the number of solute particles, not their identity."),
        ("Boiling Point Elevation", "Adding solute raises the boiling point of a solvent."),
        ("Freezing Point Depression", "Adding solute lowers the freezing point of a solvent (road salt on ice)."),
        ("Osmotic Pressure", "Pressure needed to stop osmosis across a semipermeable membrane."),
        ("Vapor Pressure Lowering", "Solute particles reduce the rate of evaporation, lowering vapor pressure."),
    ],
    "u9_l9.8": [
        ("Solubility Curve", "A graph showing the solubility of a substance vs. temperature."),
        ("Reading a Solubility Curve", "Points on the curve = saturated; below = unsaturated; above = supersaturated."),
        ("Endothermic Dissolving", "Most solids: solubility increases with temperature (upward-sloping curve)."),
        ("Exothermic Dissolving", "Some salts (e.g., Ce₂(SO₄)₃): solubility decreases with temperature."),
        ("Gases on Solubility Curves", "Gas solubility always decreases with increasing temperature."),
    ],

    # ── Unit 10: Acids & Bases ──────────────────────────────────────
    "u10_l10.1": [
        ("Acid", "A substance that donates H⁺ ions (Arrhenius) or protons (Brønsted-Lowry) in solution."),
        ("Base", "A substance that donates OH⁻ ions (Arrhenius) or accepts protons (Brønsted-Lowry)."),
        ("Arrhenius Definition", "Acid: produces H⁺ in water. Base: produces OH⁻ in water."),
        ("Brønsted-Lowry Definition", "Acid: proton (H⁺) donor. Base: proton acceptor."),
        ("Amphoteric", "A substance that can act as both an acid and a base (e.g., water)."),
    ],
    "u10_l10.2": [
        ("Binary Acid", "An acid with only hydrogen and one other element (e.g., HCl, HF, H₂S)."),
        ("Oxyacid", "An acid containing hydrogen, oxygen, and another element (e.g., HNO₃, H₂SO₄)."),
        ("Naming Binary Acids", "Prefix 'hydro-' + root of element + '-ic acid' (HCl → hydrochloric acid)."),
        ("Naming Oxyacids", "Based on the polyatomic ion: -ate → -ic acid; -ite → -ous acid."),
        ("Common Oxyacids", "HNO₃ (nitric), H₂SO₄ (sulfuric), H₃PO₄ (phosphoric), HClO₃ (chloric)."),
    ],
    "u10_l10.3": [
        ("Naming Acids", "Binary: hydro___ic acid. Oxyacid: ___ic or ___ous acid based on the ion."),
        ("Sulfuric Acid", "H₂SO₄ — a strong diprotic oxyacid; widely used in industry."),
        ("Hydrochloric Acid", "HCl — a strong binary acid; found in stomach acid."),
        ("Nitric Acid", "HNO₃ — a strong oxyacid used in fertilizers and explosives."),
        ("Acetic Acid", "CH₃COOH — a weak organic acid; the main component of vinegar."),
    ],
    "u10_l10.4": [
        ("Litmus Test", "Blue litmus turns red in acid; red litmus turns blue in base."),
        ("Phenolphthalein", "An indicator that is colorless in acid and pink in base."),
        ("Taste (lab-unsafe)", "Acids taste sour; bases taste bitter and feel slippery."),
        ("Electrolyte", "Acids and bases conduct electricity in solution because they produce ions."),
        ("pH Indicator", "A substance that changes color depending on the pH of a solution."),
    ],
    "u10_l10.5": [
        ("Strong Acid", "Completely ionizes in water (HCl, HNO₃, H₂SO₄, HBr, HI, HClO₄)."),
        ("Weak Acid", "Partially ionizes in water; establishes equilibrium (CH₃COOH, HF, H₂CO₃)."),
        ("Strong Base", "Completely dissociates in water (NaOH, KOH, Ca(OH)₂)."),
        ("Weak Base", "Partially ionizes in water (NH₃, CH₃NH₂)."),
        ("Degree of Ionization", "Strong: ~100% ionized. Weak: <100% ionized; most remains molecular."),
    ],
    "u10_l10.6": [
        ("Neutralization", "Acid + Base → Salt + Water (HCl + NaOH → NaCl + H₂O)."),
        ("Salt", "An ionic compound formed from the cation of a base and the anion of an acid."),
        ("Net Ionic Equation", "H⁺(aq) + OH⁻(aq) → H₂O(l) — the essence of neutralization."),
        ("Titration", "A lab technique to determine the concentration of an acid or base using a known solution."),
        ("Equivalence Point", "The point in a titration where moles of acid equal moles of base."),
    ],
    "u10_l10.7": [
        ("Naming Salts", "Name the cation (from base) + anion (from acid): NaOH + HCl → sodium chloride."),
        ("Sodium Chloride (NaCl)", "Table salt; from NaOH + HCl neutralization."),
        ("Calcium Sulfate (CaSO₄)", "A salt from Ca(OH)₂ + H₂SO₄; used in plaster."),
        ("Potassium Nitrate (KNO₃)", "A salt from KOH + HNO₃; used in fertilizers and fireworks."),
        ("Ammonium Chloride (NH₄Cl)", "A salt from NH₃ + HCl; used in dry cell batteries."),
    ],
    "u10_l10.8": [
        ("Buffer Solution", "A solution that resists changes in pH when small amounts of acid or base are added."),
        ("Buffer Components", "A weak acid and its conjugate base (or a weak base and its conjugate acid)."),
        ("Buffer Mechanism", "The weak acid neutralizes added base; conjugate base neutralizes added acid."),
        ("Buffer Capacity", "The amount of acid or base a buffer can neutralize before pH changes significantly."),
        ("Biological Buffers", "Blood uses carbonic acid–bicarbonate buffer to maintain pH ≈ 7.4."),
    ],
    "u10_l10.9": [
        ("pH Scale", "Measures acidity: 0–6.9 acidic, 7 neutral, 7.1–14 basic."),
        ("pH", "−log[H⁺]; lower pH = more acidic."),
        ("pOH", "−log[OH⁻]; lower pOH = more basic."),
        ("pH + pOH = 14", "At 25°C, the sum of pH and pOH always equals 14."),
        ("Neutral Solution", "pH = 7; [H⁺] = [OH⁻] = 10⁻⁷ M at 25°C."),
    ],
    "u10_l10.10": [
        ("pH Calculation", "pH = −log[H⁺]; if [H⁺] = 10⁻³ M then pH = 3."),
        ("pOH Calculation", "pOH = −log[OH⁻]; if [OH⁻] = 10⁻⁵ M then pOH = 5."),
        ("Finding [H⁺] from pH", "[H⁺] = 10^(−pH)."),
        ("Finding [OH⁻] from pOH", "[OH⁻] = 10^(−pOH)."),
        ("One pH Unit", "A change of 1 pH unit = a 10-fold change in [H⁺]."),
    ],

    # ── Unit 11: Thermochemistry ────────────────────────────────────
    "u11_l11.1": [
        ("Heat (q)", "Energy transferred between objects due to a temperature difference; measured in joules or calories."),
        ("Calorie", "The energy needed to raise 1 g of water by 1°C. 1 cal = 4.184 J."),
        ("Joule", "The SI unit of energy. 1 kJ = 1000 J."),
        ("Temperature vs Heat", "Temperature: average KE of particles. Heat: total energy transferred."),
        ("Heat Conversion", "Convert between J, kJ, cal, and kcal using: 1 cal = 4.184 J, 1 kcal = 4184 J."),
    ],
    "u11_l11.2": [
        ("Specific Heat", "The amount of heat needed to raise 1 g of a substance by 1°C (J/g·°C)."),
        ("Water's Specific Heat", "4.184 J/g·°C — very high, which moderates Earth's climate."),
        ("q = mcΔT", "Heat = mass × specific heat × temperature change."),
        ("High Specific Heat", "Absorbs a lot of heat with little temperature change (water, metals resist temp change less)."),
        ("Using q = mcΔT", "Solve for any variable: q (heat), m (mass), c (specific heat), or ΔT."),
    ],
    "u11_l11.3": [
        ("Heat Capacity", "The amount of heat needed to raise the temperature of an object by 1°C (J/°C)."),
        ("C = mc", "Heat capacity = mass × specific heat."),
        ("Specific Heat vs Heat Capacity", "Specific heat is per gram; heat capacity is for the whole object."),
        ("Molar Heat Capacity", "Heat capacity per mole of substance (J/mol·°C)."),
        ("Application", "Objects with high heat capacity (oceans) change temperature slowly."),
    ],
    "u11_l11.4": [
        ("Calorimetry", "The measurement of heat changes during chemical or physical processes."),
        ("Calorimeter", "An insulated device used to measure heat exchange in a reaction."),
        ("Coffee-Cup Calorimeter", "A simple constant-pressure calorimeter used for reactions in solution."),
        ("Bomb Calorimeter", "A constant-volume calorimeter for measuring energy in combustion reactions."),
        ("Heat Lost = Heat Gained", "In a calorimeter: q_hot + q_cold = 0 (conservation of energy)."),
    ],
    "u11_l11.5": [
        ("Enthalpy (H)", "The total heat content of a system at constant pressure."),
        ("ΔH (Enthalpy Change)", "ΔH < 0: exothermic. ΔH > 0: endothermic."),
        ("Entropy (S)", "A measure of disorder or randomness in a system; tends to increase."),
        ("Free Energy (G)", "ΔG = ΔH − TΔS; ΔG < 0 means a reaction is spontaneous."),
        ("Spontaneous Reaction", "A reaction that occurs without external energy input (ΔG < 0)."),
    ],
    "u11_l11.6": [
        ("Hess's Law", "The total enthalpy change is the same regardless of the pathway (if same initial and final states)."),
        ("Enthalpy of Formation", "ΔH°f: the enthalpy change when 1 mole of a compound forms from its elements in standard states."),
        ("Using Hess's Law", "Add, reverse, or multiply given reactions to match the target reaction; adjust ΔH accordingly."),
        ("Enthalpy Diagram", "A visual showing reactant and product energy levels and ΔH for each step."),
        ("Application", "Calculate ΔH for reactions that are difficult to measure directly."),
    ],

    # ── Unit 12: Nuclear Chemistry ──────────────────────────────────
    "u12_l12.1": [
        ("Nuclear Fission", "Splitting a heavy nucleus into lighter nuclei, releasing enormous energy (nuclear power)."),
        ("Nuclear Fusion", "Combining light nuclei into a heavier nucleus; releases even more energy (powers the sun)."),
        ("Chain Reaction", "A self-sustaining series of fission events; each fission triggers more."),
        ("Critical Mass", "The minimum amount of fissile material needed to sustain a chain reaction."),
        ("Mass-Energy Equivalence", "E = mc²; mass is converted to energy in nuclear reactions."),
    ],
    "u12_l12.2": [  # Alpha, Beta & Gamma Decay
        ("Alpha Decay", "Nucleus emits an alpha particle (⁴₂He); mass number decreases by 4, atomic number by 2."),
        ("Beta Decay", "A neutron converts to a proton, emitting a beta particle (electron); atomic number increases by 1."),
        ("Gamma Radiation", "High-energy electromagnetic radiation emitted after alpha or beta decay; no change in mass or charge."),
        ("Penetrating Power", "Alpha < Beta < Gamma; alpha stopped by paper, beta by aluminum, gamma by lead."),
        ("Ionizing Radiation", "Radiation with enough energy to remove electrons from atoms (alpha, beta, gamma)."),
    ],
    "u12_l12.3": [
        ("Nuclear Equation", "Shows the decay of a nucleus: the sum of mass numbers and atomic numbers must balance."),
        ("Transmutation", "Conversion of one element into another through nuclear reactions."),
        ("Balancing Nuclear Equations", "Total mass numbers equal on both sides; total atomic numbers equal on both sides."),
        ("Positron Emission", "A proton converts to a neutron, emitting a positron (e⁺); atomic number decreases by 1."),
        ("Electron Capture", "An inner electron is captured by the nucleus; a proton becomes a neutron."),
    ],
    "u12_l12.4": [  # Half-Life
        ("Half-Life", "The time for half of a radioactive sample to decay; constant for each isotope."),
        ("Half-Life Formula", "N = N₀ × (1/2)ⁿ where n = number of half-lives."),
        ("Number of Half-Lives", "n = total time / half-life."),
        ("Decay Curve", "A graph showing exponential decrease of a radioactive sample over time."),
        ("Application", "Carbon-14 dating uses half-life (5,730 years) to date organic materials."),
    ],
    "u12_l12.5": [  # Applications
        ("Nuclear Power", "Fission of U-235 in reactors generates electricity; produces radioactive waste."),
        ("Medical Imaging", "Radioisotopes like Tc-99m are used in medical scans (PET, SPECT)."),
        ("Carbon Dating", "Using C-14 decay to determine the age of organic remains (up to ~50,000 years)."),
        ("Food Irradiation", "Using gamma rays to kill bacteria and extend shelf life of food."),
        ("Radiation Therapy", "Using targeted radiation to destroy cancer cells."),
    ],
}

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for key, cards in FC.items():
    if key in data:
        data[key]["flashcards"] = [{"term": t, "definition": d} for t, d in cards]
        count += 1

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added flashcards to {count} Chemistry lessons")
