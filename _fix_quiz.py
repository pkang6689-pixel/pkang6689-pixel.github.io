import json
import os

def verify_no_giveaways(data, filename):
    count = 0
    for question in data['quiz_questions']:
        correct = None
        wrongs = []
        for opt in question['options']:
            if opt['is_correct']:
                correct = opt['text']
            else:
                wrongs.append(opt['text'])
        avg_wrong = sum(len(w) for w in wrongs) / len(wrongs) if wrongs else 1
        if len(correct) >= 3 * avg_wrong:
            count += 1
            print(f"  Still giveaway Q{question['question_number']}: correct={len(correct)}, avg_wrong={avg_wrong:.0f}, ratio={len(correct)/avg_wrong:.1f}x")
    print(f"{filename}: Remaining giveaways: {count}")
    return count

def fix_file(filepath, fixes):
    with open(filepath, encoding='utf-8') as f:
        data = json.load(f)
    for q in data['quiz_questions']:
        qn = q['question_number']
        if qn in fixes:
            for opt_idx, new_text in fixes[qn]:
                q['options'][opt_idx]['text'] = new_text
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    basename = os.path.basename(filepath)
    print(f"{basename} written successfully")
    verify_no_giveaways(data, basename)

# ============================================================
# Lesson12.2_Quiz.json (17 giveaways)
# Topic: Alpha, beta, gamma radiation, penetrating power, units
# ============================================================
fix_file('content_data/ChemistryLessons/Unit12/Lesson12.2_Quiz.json', {
    2: [
        (0, "A massless photon of electromagnetic energy (gamma ray)"),
        (2, "A positively charged proton ejected from the nucleus"),
        (3, "A helium-4 nucleus with 2 protons and 2 neutrons"),
    ],
    3: [
        (0, "A charged particle with significant mass and momentum"),
        (1, "A high-speed electron emitted during nuclear decay"),
        (3, "A helium-4 nucleus released during alpha decay events"),
    ],
    7: [
        (0, "Decreases by 1 (proton converts to neutron)"),
        (1, "Increases by 2 (two neutrons convert to protons)"),
        (3, "Stays the same (no change in proton count)"),
    ],
    11: [
        (0, "Paper or thin cardboard sheets"),
        (1, "Human skin or clothing layers"),
        (2, "A thin sheet of aluminum foil"),
    ],
    12: [
        (1, "A single neutron with no electric charge"),
        (2, "An electron from the inner atomic shell"),
        (3, "A hydrogen-1 atom (1 proton and 1 electron)"),
    ],
    13: [
        (1, "A gamma photon released from the excited nucleus"),
        (2, "A helium nucleus with 2 protons and 2 neutrons"),
        (3, "A positron (antielectron with positive charge)"),
    ],
    14: [
        (0, "An alpha particle consisting of 2 protons and 2 neutrons from the nucleus"),
        (1, "A proton ejected from the nucleus during radioactive decay of the atom"),
        (2, "A positively charged neutron formed during nuclear fission of heavy atoms"),
    ],
    15: [
        (0, "Electrons emitted from the nucleus at high speed during beta decay events"),
        (2, "Protons ejected from the nucleus with high kinetic energy during nuclear decay"),
        (3, "Helium nuclei containing 2 protons and 2 neutrons emitted in alpha decay"),
    ],
    16: [
        (0, "Decreases by 1 (only one proton is lost in the decay)"),
        (2, "Stays the same (only neutrons are lost, not protons)"),
        (3, "Increases by 2 (two neutrons convert into protons)"),
    ],
    18: [
        (0, "Neutrons are the same as alpha particles in charge, mass, and penetrating ability through matter"),
        (1, "Neutrons have a +2 charge that causes them to ionize atoms strongly as they pass through tissue"),
        (2, "Neutrons are large and slow-moving particles that are easily stopped by a thin sheet of paper"),
    ],
    19: [
        (0, "Gamma radiation (penetrating electromagnetic photons)"),
        (1, "Beta radiation (high-energy electrons from nucleus)"),
        (3, "Neutron radiation (uncharged particles from fission)"),
    ],
    22: [
        (0, "Penetrating power of the radiation through materials"),
        (1, "Biological damage from different radiation types"),
        (2, "Number of nuclear decays per second in the source"),
    ],
    23: [
        (0, "It produces bright visible light that causes retinal damage and permanent blindness in exposed workers"),
        (2, "It heats tissue only, causing thermal burns without any chemical or molecular damage to the cells"),
        (3, "It causes chemical burns on the surface of the skin through direct contact with radioactive material"),
    ],
    24: [
        (1, "Neutron activation to make stable atoms radioactive inside the patient\u2019s body for imaging"),
        (2, "Gamma ray external beams directed at the patient from multiple angles outside the body"),
        (3, "Alpha emitters injected into the bloodstream that deposit energy in nearby body tissues"),
    ],
    25: [
        (1, "The nucleus absorbs a gamma ray photon, converting energy into mass and increasing the atomic number"),
        (2, "A neutron is emitted from the nucleus, reducing the mass number by one while keeping Z the same"),
        (3, "An electron is emitted from the nucleus as a beta particle, increasing the atomic number by one"),
    ],
    28: [
        (1, "It is only found outdoors in the open atmosphere where wind disperses it to safe concentration levels"),
        (2, "It emits only gamma rays that pass through the body without depositing significant energy in tissue"),
        (3, "It is a stable element with no radioactive decay, but its chemical toxicity damages lung tissue"),
    ],
    29: [
        (0, "Non-ionizing radiation is always more energetic than ionizing radiation because it includes microwaves and infrared that carry thermal energy"),
        (1, "Ionizing radiation includes only gamma rays from nuclear decay; all other types of radiation are classified as non-ionizing by definition"),
        (2, "Non-ionizing radiation is always harmful to living tissue because radio waves and visible light disrupt cellular processes at any exposure level"),
    ],
})

print()

# ============================================================
# Lesson12.4_Quiz.json (14 giveaways)
# Topic: Half-life, radioactive decay, carbon dating
# ============================================================
fix_file('content_data/ChemistryLessons/Unit12/Lesson12.4_Quiz.json', {
    7: [
        (0, "Nuclear forces between protons and neutrons"),
        (1, "Time elapsed since the sample was first created"),
        (2, "The type of isotope and its nuclear composition"),
    ],
    8: [
        (0, "50 g (after 1 half-life: 100\u219250 at 10 years)"),
        (1, "30 g (proportional: 100 \u00d7 30/100 remaining)"),
        (2, "25 g (after 2 half-lives: 100\u219250\u219225 at 20 yr)"),
    ],
    9: [
        (0, "10 g (after 3 half-lives: 80\u219240\u219220\u219210)"),
        (1, "80 g (no decay occurs over this time period)"),
        (2, "40 g (after 1 half-life: 80\u219240 at 5730 yr)"),
    ],
    10: [
        (0, "C-14 has a half-life of 1 second, so it decays quickly enough to measure in a laboratory within hours"),
        (1, "All carbon isotopes decay equally fast, making any carbon isotope suitable for reliable age dating"),
        (3, "C-14 is stable and never decays, so its concentration stays constant in living and dead organisms"),
    ],
    12: [
        (0, "\u03bb = t\u00bd (decay constant equals the half-life)"),
        (1, "\u03bb = 1/t\u00bd (simple reciprocal of half-life)"),
        (3, "\u03bb = t\u00bd \u00d7 ln2 (half-life multiplied by 0.693)"),
    ],
    13: [
        (0, "1/2 (one half-life elapsed)"),
        (1, "1/8 (three half-lives elapsed)"),
        (3, "1/4 (two half-lives elapsed)"),
    ],
    18: [
        (0, "15 minutes (2 half-lives: 600\u2192300\u2192150)"),
        (1, "30 minutes (1 half-life: 600\u2192300 remaining)"),
        (2, "5 minutes (6 half-lives: 600\u21929.4 remaining)"),
    ],
    19: [
        (1, "All isotopes in the decay chain have the same half-life and decay at exactly the same rate simultaneously"),
        (2, "All decay stops once the parent and daughter isotopes reach equal concentrations in the sample material"),
        (3, "Equilibrium is reached only when all radioactive material has fully decayed to stable daughter products"),
    ],
    23: [
        (1, "It is chemically inert and does not bond to any biological molecules in the body"),
        (2, "It only emits gamma rays that pass through bone tissue without causing significant damage"),
        (3, "It has a half-life of 1 second, so it decays before it can reach any organs in the body"),
    ],
    24: [
        (0, "75% (three-quarters of the sample)"),
        (1, "25% (one-quarter of the sample)"),
        (2, "100% (all of the original sample)"),
    ],
    25: [
        (1, "The half-life of the isotope (each isotope has its own fixed half-life value)"),
        (2, "The identity of the element and its position on the periodic table"),
        (3, "The number of atoms present in the sample at any given point in time"),
    ],
    27: [
        (1, "Sieverts (Sv) or Rems (rem)"),
        (2, "Joules (J) or Calories (cal)"),
        (3, "Grays (Gy) or Rads (rad)"),
    ],
    28: [
        (0, "30 years ago (exactly 1 full half-life of Cs-137)"),
        (2, "60 years ago (exactly 2 full half-lives of Cs-137)"),
        (3, "7.5 years ago (one quarter of a single half-life)"),
    ],
    30: [
        (0, "1/10 (approximately 10%)"),
        (1, "1/25 (approximately 4.0%)"),
        (2, "1/5 (approximately 20.0%)"),
    ],
})

print()

# ============================================================
# Lesson12.5_Quiz.json (15 giveaways)
# Topic: Applications: medicine, power, food irradiation, dating
# ============================================================
fix_file('content_data/ChemistryLessons/Unit12/Lesson12.5_Quiz.json', {
    1: [
        (0, "Build weapons using concentrated radioactive materials"),
        (1, "Clean water supplies by killing harmful bacteria"),
        (3, "Generate electricity in portable medical devices"),
    ],
    8: [
        (0, "Using neutron beams directed through the patient to image internal organ density"),
        (1, "Measuring the heat generated from radioactive decay of tracers in the body"),
        (3, "Reflecting X-rays off bones and dense structures to create contrast images"),
    ],
    9: [
        (1, "Sound waves focused on tumor cells to mechanically disrupt their cellular membranes"),
        (2, "Laser light only, directed at cancer cells to heat and destroy the tumor tissue"),
        (3, "Radioactive isotopes ingested as oral medicine that selectively target cancer cells"),
    ],
    11: [
        (0, "Neutron beams to irradiate food and make it safe for long-term storage and consumption"),
        (1, "Alpha particles directed at food surfaces to eliminate bacterial contamination entirely"),
        (3, "UV light only for surface decontamination of pre-packaged food products and beverages"),
    ],
    12: [
        (0, "Replace damaged tissues with regenerated cells activated by low-dose radiation treatment"),
        (2, "Provide energy to cells through radioactive decay powering cellular metabolism directly"),
        (3, "Kill bacteria inside the body using concentrated doses of targeted radiation beams"),
    ],
    13: [
        (0, "D\u2082O is less radioactive than regular water and reduces the radiation hazard in the reactor"),
        (1, "D\u2082O produces more energy per fission event than regular water due to its heavier mass"),
        (2, "D\u2082O is cheaper to produce and easier to purify in large industrial quantities for reactors"),
    ],
    17: [
        (0, "Iodine-131 (\u03b2 emitter used in thyroid imaging and treatment)"),
        (1, "Cobalt-60 (\u03b3 emitter used in industrial radiography sources)"),
        (3, "Uranium-235 (fissile isotope used as nuclear reactor fuel)"),
    ],
    18: [
        (1, "Contains medical waste from hospitals that used short-lived diagnostic radioisotopes"),
        (2, "Is only slightly radioactive and can be disposed of in standard municipal landfills"),
        (3, "Comes from fossil fuel combustion and contains naturally occurring radioactive materials"),
    ],
    19: [
        (0, "Aircraft engines using small nuclear reactors mounted on the wings for long-range flight"),
        (1, "Nuclear power plants that generate electricity for cities through controlled fission reactions"),
        (3, "Medical devices only, such as pacemakers and insulin pumps, using small sealed sources"),
    ],
    20: [
        (0, "It has a 100-year half-life, which provides continuous treatment over many decades for the patient"),
        (2, "It is a stable isotope that does not undergo radioactive decay, acting purely as a chemical agent"),
        (3, "It emits alpha particles that kill all cells in the body, requiring precise shielding for treatment"),
    ],
    21: [
        (1, "It produces no radiation at all during the fusion reaction or afterward from its products"),
        (2, "It uses uranium fuel enriched to high concentrations for the fusion process to operate"),
        (3, "It produces water as the only byproduct, with no other materials or energy released"),
    ],
    22: [
        (0, "Autoclaves only, using high-pressure steam to sterilize heat-resistant metal instruments"),
        (1, "Chemical disinfectants only, applied to surfaces to eliminate bacteria and viral pathogens"),
        (2, "UV light directed at the surface of instruments for short-duration sterilization cycles"),
    ],
    23: [
        (0, "Measuring mass only using a precision analytical balance to determine elemental composition"),
        (1, "Measuring optical spectrum using visible light absorption patterns of each element present"),
        (3, "Dissolving the sample in acid and then separating elements using chemical precipitation"),
    ],
    26: [
        (1, "Electrolysis of radioactive solutions to separate isotopes by their different ionic charges"),
        (2, "Natural radioactive decay only, collecting daughter isotopes produced over time in storage"),
        (3, "Fission of uranium fuel rods in a small reactor contained within the hospital facility"),
    ],
    29: [
        (0, "100 billion years (the sun will burn hydrogen far longer than the current age of the universe)"),
        (2, "4.6 billion years total lifetime (equal to the current age of the sun and solar system)"),
        (3, "1 billion years (the sun will exhaust its hydrogen supply within the next billion years)"),
    ],
})

print()

# ============================================================
# Lesson7.7_Quiz.json (10 giveaways)
# Topic: Stoichiometry, mole ratios, dimensional analysis
# ============================================================
fix_file('content_data/ChemistryLessons/Unit7/Lesson7.7_Quiz.json', {
    6: [
        (1, "Molar masses to directly convert between substances"),
        (2, "Atomic numbers from the periodic table of elements"),
        (3, "Avogadro\u2019s number (6.022 \u00d7 10\u00b2\u00b3 particles/mol)"),
    ],
    7: [
        (0, "No conversion needed; grams of one substance equal grams of another directly"),
        (1, "Direct division of masses using the ratio of molecular weights only"),
        (3, "Adding masses of reactants together to determine total product mass"),
    ],
    11: [
        (0, "The measurement of reaction speed and how quickly reactants are consumed and products are formed over time"),
        (2, "The arrangement of electrons in orbitals around the nucleus and their quantum mechanical energy levels"),
        (3, "The study of atomic structure, including protons, neutrons, and electrons that make up all elements"),
    ],
    12: [
        (1, "The number of atoms in a mole, defined by Avogadro\u2019s constant as 6.022 \u00d7 10\u00b2\u00b3 particles per mole"),
        (2, "The mass of one mole of a substance in grams, numerically equal to its atomic or molecular weight"),
        (3, "The ratio of protons to neutrons in the nucleus of an atom, which determines isotopic stability"),
    ],
    13: [
        (1, "A problem using only Avogadro\u2019s number to convert between particles and moles without mass calculations"),
        (2, "Weighing an object twice on different scales and comparing the two mass readings for accuracy"),
        (3, "Comparing the density of two substances to determine which one is heavier per unit volume"),
    ],
    16: [
        (0, "The equilibrium constant (K) that describes the balance between products and reactants"),
        (2, "The rate constant of a reaction that determines how fast the chemical process occurs"),
        (3, "The acceleration due to gravity (9.8 m/s\u00b2) used when calculating the weight of samples"),
    ],
    17: [
        (0, "The theoretical yield of the product calculated from the equation"),
        (2, "The molar mass of the substance in grams per mole from the table"),
        (3, "Avogadro\u2019s number (6.022 \u00d7 10\u00b2\u00b3) that converts moles to particles"),
    ],
    18: [
        (1, "The limiting reagent that is completely consumed first during the reaction"),
        (2, "The catalyst that speeds up the reaction without being consumed in it"),
        (3, "The excess reagent that remains unreacted after the reaction has completed"),
    ],
    20: [
        (0, "The charge on an ion in an ionic compound, indicating the number of electrons gained or lost by the atom"),
        (1, "The atomic number of an element, which represents the total number of protons found in the nucleus"),
        (3, "The subscript in a chemical formula, which indicates the number of atoms of each element per molecule"),
    ],
    28: [
        (1, "2:25 or 1:12.5"),
        (2, "1:1 (equal ratio)"),
        (3, "8:1 (inverse ratio)"),
    ],
})

print()

# ============================================================
# Lesson11.5_Quiz.json (10 giveaways)
# Topic: Enthalpy, entropy, Gibbs free energy, spontaneity
# ============================================================
fix_file('content_data/ChemistryLessons/Unit11/Lesson11.5_Quiz.json', {
    1: [
        (0, "Free energy available to do useful work"),
        (1, "Disorder or randomness of the system"),
        (3, "Temperature of the system in kelvins"),
    ],
    3: [
        (0, "Free energy available to do work"),
        (1, "Heat content at constant pressure"),
        (2, "Temperature of the surroundings"),
    ],
    8: [
        (1, "Pressure exerted by gas molecules"),
        (2, "Temperature of the surroundings"),
        (3, "Energy content at constant pressure"),
    ],
    10: [
        (0, "Heat flows spontaneously from cold objects to hot objects, never from hot to cold in nature"),
        (2, "Energy is conserved in all physical and chemical processes, including both heat and work"),
        (3, "Entropy never changes in any process; it remains constant regardless of temperature or pressure"),
    ],
    11: [
        (0, "Ice (most ordered crystalline solid phase)"),
        (2, "Liquid water (intermediate phase between ice and gas)"),
        (3, "They are equal in entropy regardless of phase"),
    ],
    13: [
        (1, "\u0394H > 0 and \u0394S < 0 (endothermic with decreasing entropy)"),
        (2, "\u0394S = 0 (no change in entropy during the reaction)"),
        (3, "\u0394H = 0 (no enthalpy change during the reaction)"),
    ],
    14: [
        (0, "\u0394G = 0 (the system is exactly at equilibrium with no net change)"),
        (1, "\u0394H < 0 and \u0394S > 0 (exothermic with increasing entropy)"),
        (3, "\u0394H = 0 and \u0394S > 0 (no enthalpy change with entropy increase)"),
    ],
    17: [
        (0, "\u0394S < 0 (entropy decreases, making the reaction less favorable)"),
        (1, "\u0394H becomes negative at higher temperatures due to increased energy"),
        (3, "Temperature has no effect on spontaneity because \u0394G depends only on \u0394H"),
    ],
    21: [
        (0, "Positive (melting is non-spontaneous at this temperature)"),
        (1, "Negative (melting is fully spontaneous at this temperature)"),
        (2, "Undefined (cannot be calculated at a phase transition)"),
    ],
    29: [
        (0, "\u0394G\u00b0 < 0 means equilibrium favors neither side and reactants and products are present in equal amounts"),
        (1, "K = \u0394G\u00b0 (the equilibrium constant is numerically equal to the standard free energy change)"),
        (3, "\u0394G\u00b0 = 0 at all equilibria regardless of the specific reaction or temperature conditions involved"),
    ],
})

print()
print("Done with all remaining files!")
