"""
Enhanced AP Course Content Generator v2
Generates 7 quiz questions, 10 flashcards, and detailed summaries for all AP courses
"""

import json
from pathlib import Path
from typing import List, Dict, Tuple
import random

# Enhanced comprehensive content with detailed summaries and more flashcards/quizzes
ENHANCED_AP_CONTENT = {
    'AP Biology': {
        1: {
            '1.1': {
                'title': 'Properties of Water',
                'summaries': [
                    'Water is a polar molecule with the chemical formula H₂O, composed of one oxygen atom bonded to two hydrogen atoms. The unequal sharing of electrons between oxygen and hydrogen creates a polar covalent bond, with oxygen being more electronegative and carrying a partial negative charge while hydrogen atoms carry partial positive charges. This polarity is fundamental to water\'s unique properties and makes it essential for all known forms of life on Earth.',
                    'Hydrogen bonding occurs between the partially positive hydrogen atoms of one water molecule and the partially negative oxygen atoms of neighboring water molecules. Though individually weak (about 1/20th the strength of a covalent bond), hydrogen bonds collectively create strong intermolecular forces that give water its distinctive characteristics. These bonds are constantly breaking and reforming, allowing water to remain liquid at room temperature rather than existing as a gas like other similar-sized molecules such as methane.',
                    'Water exhibits an unusually high specific heat capacity of approximately 4.18 J/g°C, meaning it requires a large amount of energy to raise its temperature by one degree. This property allows water to moderate temperature changes in organisms and environments, providing thermal stability crucial for maintaining homeostasis. Additionally, water has high surface tension due to hydrogen bonding, allowing it to form capillaries and enabling some organisms to live on its surface.',
                    'Unlike most substances, water is denser in its liquid form than its solid form, which is why ice floats. This anomalous expansion upon freezing occurs because the crystalline structure of ice has more space between molecules than liquid water. This property is ecologically critical because floating ice insulates water bodies below, allowing aquatic organisms to survive under frozen surfaces during winter months.'
                ],
                'flashcards': [
                    ('What is a polar molecule?', 'A molecule with an unequal distribution of electron density, creating partial charges at opposite ends.'),
                    ('Why is hydrogen bonding important to water?', 'It creates strong intermolecular forces that give water its unique properties and high boiling point.'),
                    ('What is the specific heat of water?', '4.18 J/g°C - one of the highest of all common substances.'),
                    ('Why does ice float?', 'Ice is less dense than liquid water due to its crystalline structure having more space between molecules.'),
                    ('What is water\'s role as a universal solvent?', 'Its polarity allows it to dissolve many ionic and polar substances, earning it the title "universal solvent."'),
                    ('Define surface tension in water', 'The elastic property of water surface caused by hydrogen bonding that resists breaking.'),
                    ('How do hydrogen bonds affect water\'s boiling point?', 'They increase it significantly - water boils at 100°C, much higher than predicted based on molecular weight alone.'),
                    ('What percentage of Earth\'s water is salt water?', 'Approximately 97% of Earth\'s water is salt water found in oceans; only 3% is freshwater.'),
                    ('How does water\'s polarity relate to its solvent properties?', 'The polar nature of water allows it to surround and dissolve ionic compounds and other polar molecules.'),
                    ('What happens to water density as temperature increases?', 'Water density decreases as temperature increases above 4°C, causing water to expand.')
                ],
                'quiz_questions': [
                    ('A water molecule is polar because...', ['It has two hydrogen atoms', 'Oxygen is more electronegative than hydrogen', 'It forms hydrogen bonds', 'It is a liquid at room temperature'], 1),
                    ('Hydrogen bonds are formed between which atoms in water?', ['Two oxygen atoms', 'Two hydrogen atoms', 'A hydrogen atom and an oxygen atom', 'A hydrogen and a carbon atom'], 2),
                    ('Water\'s high specific heat capacity means...', ['It freezes at 0°C', 'It requires large amounts of energy to change temperature', 'It boils at 100°C', 'It can dissolve salt'], 1),
                    ('Which property of water allows it to moderate temperature in organisms?', ['Polarity', 'Surface tension', 'High specific heat', 'Density anomaly'], 2),
                    ('Ice floats because...', ['It is frozen', 'Hydrogen bonds hold it together', 'Its crystalline structure is less dense than liquid water', 'Solid water is always less dense than liquid water'], 2),
                    ('Water is called a universal solvent because...', ['It dissolves everything', 'Its polarity allows it to dissolve many ionic and polar substances', 'It has the highest boiling point', 'It has high surface tension'], 1),
                    ('The cohesion of water molecules is primarily due to...', ['Ionic bonds', 'Hydrogen bonds', 'Covalent bonds within water molecules', 'Van der Waals forces'], 1),
                ]
            },
            '1.2': {
                'title': 'Carbohydrates: Structure and Function',
                'summaries': [
                    'Carbohydrates are organic compounds with the general molecular formula (CH₂O)ₙ that serve as primary sources of energy and structural components in living organisms. They consist of carbon, hydrogen, and oxygen atoms arranged in chains or rings, with the ratio of hydrogen to oxygen typically being 2:1, the same as in water. Carbohydrates are classified into three main categories based on their size and complexity: monosaccharides (simple sugars), disaccharides (double sugars), and polysaccharides (complex carbohydrates).',
                    'Monosaccharides are the simplest carbohydrates, consisting of single sugar molecules with the general formula CₙH₂ₙOₙ. The most common monosaccharide is glucose (C₆H₁₂O₆), a six-carbon sugar that serves as a primary fuel for cellular respiration. Other important monosaccharides include fructose (fruit sugar) and galactose, which differ from glucose in the arrangement of their atoms but have the same molecular formula, making them isomers.',
                    'Disaccharides are formed when two monosaccharides unite through a dehydration synthesis reaction, which removes a water molecule and creates a glycosidic bond between the two sugars. Common disaccharides include sucrose (table sugar), maltose (malt sugar), and lactose (milk sugar). Each disaccharide has different properties and sources; for example, sucrose comes from plants, while lactose is found primarily in mammalian milk.',
                    'Polysaccharides are long chains or branched networks of monosaccharides linked by glycosidic bonds, serving various functions including energy storage and structural support. Starch and glycogen are storage polysaccharides that provide readily available energy, with starch being the energy storage molecule in plants and glycogen serving this function in animals. Cellulose is a structural polysaccharide that forms the cell walls of plants; its β-1,4-glycosidic bonds cannot be broken by human digestive enzymes, which is why cellulose is dietary fiber.'
                ],
                'flashcards': [
                    ('What is the general formula for carbohydrates?', '(CH₂O)ₙ - where n indicates the number of carbon atoms.'),
                    ('What is glucose and what is its molecular formula?', 'A six-carbon monosaccharide with the formula C₆H₁₂O₆; primary fuel for cellular respiration.'),
                    ('What bond connects monosaccharides together?', 'The glycosidic bond, formed during dehydration synthesis (condensation reaction).'),
                    ('Name three important disaccharides and their sources', 'Sucrose (plants), maltose (grains), and lactose (milk).'),
                    ('What is the function of starch?', 'Energy storage in plants; it is a polysaccharide made of glucose monomers.'),
                    ('How is glycogen similar to and different from starch?', 'Both are glucose polysaccharides for energy storage, but glycogen is more branched and serves storage in animals while starch functions in plants.'),
                    ('Why can\'t humans digest cellulose?', 'Humans lack the enzyme cellulase needed to break the β-1,4-glycosidic bonds in cellulose.'),
                    ('What is dehydration synthesis?', 'A reaction in which two molecules combine with the removal of a water molecule, forming a new bond.'),
                    ('Name at least two functions of carbohydrates in cells', 'Quick energy (glucose), long-term energy storage (starch/glycogen), structural support (cellulose), and raw materials for biosynthesis.'),
                    ('What makes cellulose a good structural material?', 'Its long, straight chains cross-link to form strong fibers; its β-1,4-glycosidic bonds are difficult to break.')
                ],
                'quiz_questions': [
                    ('The molecular formula CₙH₂ₙOₙ describes...', ['All carbohydrates', 'Monosaccharides only', 'Disaccharides and polysaccharides', 'All organic compounds'], 1),
                    ('Glucose, fructose, and galactose are isomers because they...', ['Have the same molecular formula but different structures', 'Have the same structure but different molecular formulas', 'Have the same number of oxygen atoms', 'Are all six-carbon sugars'], 0),
                    ('When two monosaccharides join, the reaction is called...', ['Hydrolysis', 'Dehydration synthesis', 'Deamination', 'Phosphorylation'], 1),
                    ('Starch and glycogen differ primarily in...', ['Their molecular formula', 'Where they are stored and their branching patterns', 'The type of glucose they contain', 'Their solubility in water'], 1),
                    ('Cellulose is a good structural material for plants because...', ['It is soluble in water', 'It forms strong, rigid fibers', 'It stores energy efficiently', 'It is easily digested'], 1),
                    ('Lactose intolerance occurs when people lack the enzyme...', ['Amylase', 'Cellulase', 'Lactase', 'Maltase'], 2),
                    ('Which carbohydrate serves as immediate energy for cells?', ['Starch', 'Glycogen', 'Glucose', 'Sucrose'], 2),
                ]
            },
        },
        2: {
            '2.1': {
                'title': 'Photosynthesis: Light Reactions',
                'summaries': [
                    'Photosynthesis is the fundamental process by which plants, algae, and some bacteria convert light energy into chemical energy stored in glucose, ultimately providing the energy base for nearly all life on Earth. The process occurs in two main stages: the light-dependent reactions and the light-independent reactions (Calvin cycle), with the light reactions occurring in the thylakoid membranes of chloroplasts and the Calvin cycle occurring in the stroma. Light reactions directly capture light energy and produce electron carriers and ATP that power the Calvin cycle.',
                    'The light reactions begin when photons of light are absorbed by photosystem II (PSII) in the thylakoid membrane, exciting electrons in chlorophyll molecules to higher energy states. This excitation causes water molecules to be split in a process called photolysis, releasing electrons, protons, and oxygen gas as a byproduct. The electrons from water replace those lost from chlorophyll, and the released protons accumulate in the thylakoid lumen, creating a proton gradient that will drive ATP synthesis.',
                    'The excited electrons travel through an electron transport chain from PSII to photosystem I (PSI), losing energy in the process that pumps additional protons into the thylakoid lumen, further increasing the proton gradient. At PSI, electrons are re-energized by additional light absorption and are used to reduce NADP⁺ to NADPH, which serves as a reducing agent in the Calvin cycle. Meanwhile, the accumulated proton gradient drives protons through the ATP synthase enzyme, producing ATP through chemiosmosis.',
                    'The light reactions produce two essential products for the Calvin cycle: ATP and NADPH, which are electron carriers generated from the oxidation of water. Additionally, oxygen gas is released as a waste product of photolysis, which is essential for aerobic respiration in most organisms. The efficiency of light reactions depends on light intensity, wavelength, and temperature, with different photosynthetic organisms having adapted to use different wavelengths of light.'
                ],
                'flashcards': [
                    ('What is photosynthesis?', 'The process of converting light energy into chemical energy stored in glucose using carbon dioxide and water.'),
                    ('Where do light reactions occur?', 'In the thylakoid membranes of chloroplasts.'),
                    ('What is the primary function of light reactions?', 'To capture light energy and produce ATP and NADPH for the Calvin cycle.'),
                    ('What two products are essential outputs of the light reactions?', 'ATP and NADPH, which are used as energy and electrons in the Calvin cycle.'),
                    ('What is photolysis?', 'The splitting of water molecules (H₂O) during light reactions to release electrons, protons, and O₂.'),
                    ('Name the two photosystems in light reactions and their roles', 'Photosystem II absorbs light first and splits water; Photosystem I re-energizes electrons and reduces NADP⁺ to NADPH.'),
                    ('What is chemiosmosis in the context of photosynthesis?', 'The process where a proton gradient across the thylakoid membrane drives ATP synthesis by ATP synthase.'),
                    ('Why is oxygen released during photosynthesis?', 'It is a byproduct of water photolysis and is essential for aerobic respiration in organisms.'),
                    ('What is the electron transport chain\'s role in light reactions?', 'It transfers electrons from PSII to PSI while pumping protons to build the gradient needed for ATP synthesis.'),
                    ('How do light intensity and wavelength affect photosynthesis?', 'Both affect the rate of photosynthesis; certain wavelengths (especially red and blue) are most effective for photosynthesis.')
                ],
                'quiz_questions': [
                    ('Light reactions occur in the...', ['Stroma', 'Thylakoid membrane', 'Inner mitochondrial membrane', 'Cytoplasm'], 1),
                    ('The splitting of water during photosynthesis is called...', ['Glycolysis', 'Photolysis', 'Lysis', 'Hydrolysis'], 1),
                    ('Which photosystem absorbs light first in the light reactions?', ['PSI', 'PSII', 'Both simultaneously', 'They alternate'], 1),
                    ('The proton gradient in the thylakoid lumen drives...', ['Glucose synthesis', 'Water hydrolysis', 'ATP synthesis', 'Electron transport'], 2),
                    ('NADPH produced in light reactions is used for...', ['Breaking down glucose', 'Fixing carbon dioxide in the Calvin cycle', 'Storing energy', 'Photolysis'], 1),
                    ('The oxygen released during photosynthesis comes from...', ['CO₂ from the air', 'Water molecules', 'The soil', 'Glucose breakdown'], 1),
                    ('Which of the following is NOT a product of light reactions?', ['ATP', 'NADPH', 'O₂', 'Glucose'], 3),
                ]
            },
        },
    },
    'AP Chemistry': {
        1: {
            '1.1': {
                'title': 'Atomic Structure and Subatomic Particles',
                'summaries': [
                    'Atoms are the basic building blocks of matter, consisting of a dense nucleus surrounded by electrons in electron shells or orbitals. The nucleus contains two types of subatomic particles with similar mass but opposite charges: protons (positive charge of +1.6 × 10⁻¹⁹ C) and neutrons (no charge). Electrons (negative charge of -1.6 × 10⁻¹⁹ C) occupy regions around the nucleus called orbitals, and weigh approximately 1/1836 of a proton\'s mass, making the electron negligible to atomic mass.',
                    'The atomic number of an element is defined as the number of protons in the nucleus and is unique to each element, determining its identity and chemical properties. For example, all atoms with 6 protons are carbon atoms, all atoms with 8 protons are oxygen atoms, and all atoms with 92 protons are uranium atoms. The number of electrons in a neutral atom equals the number of protons, making the overall charge of the atom neutral, although ions are formed when this balance is disrupted.',
                    'The mass number is the sum of protons and neutrons in a nucleus, representing the approximately mass of an atom in atomic mass units (amu). Isotopes are atoms of the same element (same number of protons) that differ in their number of neutrons and therefore have different mass numbers. For example, carbon-12 has 6 protons and 6 neutrons (mass number 12), while carbon-14 has 6 protons and 8 neutrons (mass number 14); both are carbon but with different masses and slightly different chemical properties.',
                    'The atomic mass of an element listed on the periodic table is the weighted average of the masses of all naturally occurring isotopes of that element, accounting for their relative abundances. For instance, since carbon-12 is much more abundant than carbon-13 or carbon-14 in nature, the atomic mass of carbon (12.01 amu) is very close to 12. Understanding the relationship between atomic number, mass number, and isotopes is crucial for explaining atomic behavior, radioactivity, and the chemical properties that determine how atoms bond.'
                ],
                'flashcards': [
                    ('What is atomic number?', 'The number of protons in the nucleus of an atom; it uniquely identifies an element.'),
                    ('What is mass number?', 'The sum of protons and neutrons in the nucleus (protons + neutrons).'),
                    ('What is an isotope?', 'Atoms of the same element with different numbers of neutrons, so they have different mass numbers.'),
                    ('What particles make up the nucleus?', 'Protons (positive charge) and neutrons (neutral charge).'),
                    ('Where are electrons located in an atom?', 'In electron shells or orbitals around the nucleus at various energy levels.'),
                    ('What is the charge of a proton, neutron, and electron?', 'Proton: +1; Neutron: 0 (neutral); Electron: -1.'),
                    ('How do you calculate the number of neutrons in an atom?', 'Subtract the atomic number (protons) from the mass number.'),
                    ('What is the relative mass of an electron compared to a proton?', 'An electron weighs approximately 1/1836 of a proton\'s mass.'),
                    ('How is atomic mass related to isotopes?', 'Atomic mass is the weighted average of all naturally occurring isotope masses based on their abundances.'),
                    ('Why do different isotopes of the same element have similar chemical properties?', 'Because they have the same number of protons and electrons, which determine chemical bonding and reactivity.')
                ],
                'quiz_questions': [
                    ('An atom has 6 protons and 8 neutrons. What is its mass number?', ['6', '8', '14', '2'], 2),
                    ('The atomic number determines...', ['Mass of the atom', 'Identity of the element', 'Number of neutrons', 'Number of electrons and protons combined'], 1),
                    ('Isotopes of an element differ in...', ['Number of protons', 'Number of electrons', 'Number of neutrons', 'Atomic number'], 2),
                    ('Which subatomic particle has the greatest mass?', ['Electron', 'Proton', 'Neutron', 'Proton and neutron equally'], 1),
                    ('A neutral atom of fluorine (atomic number 9) has how many electrons?', ['8', '9', '10', '17'], 1),
                    ('The periodic table shows atomic masses as weighted averages because...', ['Atoms have multiple isotopes with different abundances', 'It is easier to calculate', 'All atoms of an element are identical', 'Neutrons differ between atoms'], 0),
                    ('Carbon-12 and Carbon-14 are isotopes because they have...', ['Different atomic numbers', 'The same number of neutrons', 'The same number of protons but different neutrons', 'Different numbers of electrons'], 2),
                ]
            },
        },
    },
    'AP Calculus AB': {
        1: {
            '1.1': {
                'title': 'Limits and Continuity',
                'summaries': [
                    'A limit describes the value that a function approaches as the input (independent variable) approaches a specific value, written as lim(x→a) f(x) = L. This is a fundamental concept in calculus that allows us to analyze function behavior near a point, even when the function is not defined at that point. Importantly, for a limit to exist, the function must approach the same value from both the left side (left-hand limit) and the right side (right-hand limit) as x approaches the value a.',
                    'The formal ε-δ definition of a limit states that lim(x→a) f(x) = L if for every small positive number ε (epsilon), there exists a positive number δ (delta) such that whenever 0 < |x - a| < δ, we have |f(x) - L| < ε. This rigorous definition ensures that no matter how small an acceptable error bound ε we set, we can always find an interval around a (defined by δ) where all function values stay within that error bound of L. This formal approach is essential for proving limit properties and theorems.',
                    'A function is continuous at a point a if three conditions are satisfied: (1) f(a) is defined, (2) lim(x→a) f(x) exists, and (3) lim(x→a) f(x) = f(a). In other words, the function must be defined at the point, the limit must exist, and the limit must equal the actual function value at that point. A function is continuous on an interval if it is continuous at every point in that interval, meaning it can be drawn without lifting the pencil from the paper.',
                    'Different types of discontinuities occur when a function fails to be continuous at a point: a removable discontinuity (or hole) occurs when lim f(x) exists but either f(a) is undefined or does not equal the limit; a jump discontinuity occurs when the left and right limits exist but are not equal; an infinite discontinuity occurs when the function approaches infinity (like at a vertical asymptote). Understanding and identifying these discontinuities is crucial for analyzing function behavior and is foundational for studying derivatives and integrals.'
                ],
                'flashcards': [
                    ('Define a limit', 'The value a function approaches as the input approaches a specific value.'),
                    ('What does lim(x→a) f(x) = L mean?', 'As x approaches a, the function values f(x) approach L.'),
                    ('What are the three conditions for continuity at x = a?', 'f(a) is defined; lim f(x) as x→a exists; lim f(x) = f(a).'),
                    ('What is a removable discontinuity?', 'A hole in the graph where the limit exists but f(a) is undefined or does not equal the limit.'),
                    ('What is a jump discontinuity?', 'A point where the left-hand and right-hand limits exist but are not equal.'),
                    ('What is an infinite discontinuity?', 'A discontinuity where the function approaches infinity, usually at a vertical asymptote.'),
                    ('What is the difference between left-hand and right-hand limits?', 'Left-hand limit: approaching from values less than a; Right-hand limit: approaching from values greater than a.'),
                    ('Can a function be continuous at a point where it is not defined?', 'No. For continuity, the function must be defined at the point (f(a) must exist).'),
                    ('What does the ε-δ definition of a limit require?', 'For any ε > 0, there exists δ > 0 such that 0 < |x - a| < δ implies |f(x) - L| < ε.'),
                    ('If the left and right limits are equal, what can we conclude?', 'The limit exists and equals the common value of the left and right limits.')
                ],
                'quiz_questions': [
                    ('For lim(x→a) f(x) to equal L, what must be true?', ['f(a) = L', 'The left and right limits must be equal', 'f(a) must be defined', 'Both A and C'], 1),
                    ('A removable discontinuity can be eliminated by...', ['Factoring the numerator', 'Redefining f(a) to equal the limit', 'Taking the derivative', 'The limit doesn\'t exist'], 1),
                    ('At a jump discontinuity...', ['The function has a hole', 'The left and right limits are not equal', 'The function is undefined', 'The limit is infinite'], 1),
                    ('A function is continuous on an interval if...', ['It is continuous at every point in the interval', 'It is defined at every point', 'It has a limit at every point', 'Its derivative exists'], 0),
                    ('Which type of discontinuity occurs at a vertical asymptote?', ['Removable', 'Jump', 'Infinite', 'All of the above'], 2),
                    ('If lim(x→2) f(x) = 5 and f(2) = 5, then...', ['The function has a jump discontinuity', 'The function is continuous at x = 2', 'The function has a removable discontinuity', 'The limit does not exist'], 1),
                    ('The difference between lim(x→3⁻) f(x) and lim(x→3⁺) f(x) tells us...', ['Whether f(3) is defined', 'Whether the function is continuous', 'Whether a limit exists', 'The slope of the tangent line'], 2),
                ]
            },
        },
    },
    'AP Statistics': {
        1: {
            '1.1': {
                'title': 'Data Collection and Types of Variables',
                'summaries': [
                    'Statistics is the science of collecting, analyzing, and interpreting data to make informed decisions and understand patterns in populations. A population is the entire group of individuals or items under study, while a sample is a subset of the population from which data are actually collected. Statistical inference uses information from samples to make conclusions about populations, with the accuracy of these inferences depending on whether the sample is representative of the population and collected through appropriate methods.',
                    'Variables are characteristics that can take on different values among individuals in a population. Categorical variables (also called qualitative variables) describe qualities or categories that cannot be measured numerically, such as blood type, gender, or preference colors; they can be organized into categories but mathematical operations cannot be performed on them. Quantitative variables (also called numerical variables) represent measurable quantities with numerical values, such as height, weight, or test scores; these can be discrete (countable, like number of students) or continuous (measured on a continuum, like weight).',
                    'The method of data collection significantly affects the validity of statistical conclusions. A census collects data from every member of the population, providing complete information but being expensive and time-consuming for large populations. Surveys and observations collect sample data and are more practical, while experiments involve manipulating an independent variable to measure its effect on a dependent variable, allowing for cause-and-effect conclusions. Sampling bias occurs when the method of selecting the sample causes certain members of the population to be less likely to be included.',
                    'Common sampling methods include simple random sampling (each individual has equal chance of selection), stratified random sampling (population divided into strata and random samples taken from each), systematic sampling (selecting every kth individual), and cluster sampling (dividing population into clusters and randomly selecting some clusters). The goal of random sampling is to ensure the sample is representative of the population, though bias can still occur from non-response or measurement error. Understanding data collection methods is essential for evaluating the reliability of statistical studies and conclusions.'
                ],
                'flashcards': [
                    ('What is the difference between a population and a sample?', 'A population is the entire group being studied; a sample is a subset of the population.'),
                    ('Define a categorical variable with examples', 'A qualitative variable describing categories, such as gender, race, or brand preference; cannot be added or averaged.'),
                    ('Define a quantitative variable with examples', 'A numerical variable representing measurable quantities, such as height, weight, or test score; can be discrete or continuous.'),
                    ('What is the difference between discrete and continuous variables?', 'Discrete variables are countable and take specific values (like number of cars); continuous variables are measured and can take any value in a range (like height).'),
                    ('What is sampling bias?', 'Systematic error in selection of a sample that causes some members of the population to be less likely to be included.'),
                    ('Name four common sampling methods', 'Simple random, stratified random, systematic, and cluster sampling.'),
                    ('What is stratified random sampling?', 'Dividing the population into similar subgroups (strata) and randomly sampling from each stratum.'),
                    ('What is the advantage of a census over sampling?', 'A census provides complete data about the population, eliminating sampling error and bias from sample selection.'),
                    ('Why is random sampling important?', 'It helps ensure that the sample is representative of the population, reducing sampling bias and making inferences more valid.'),
                    ('What could cause a sample to not be representative of the population?', 'Sampling bias, non-response, measurement error, or using non-random selection methods.')
                ],
                'quiz_questions': [
                    ('Statistical inference uses data from a ________ to make conclusions about the ________', ['Sample, population', 'Population, sample', 'Variable, constant', 'Census, survey'], 0),
                    ('Which of the following is NOT a quantitative variable?', ['Height in centimeters', 'Eye color', 'Number of students', 'Weight in pounds'], 1),
                    ('A survey that collects gender, age, and income for all residents in a city is an example of...', ['An experiment', 'An observational study', 'A census (if all residents are surveyed)', 'A controlled study'], 2),
                    ('Stratified random sampling is different from simple random sampling because...', ['It guarantees no bias', 'It divides the population into strata and samples from each', 'It is always more expensive', 'It uses a predetermined pattern'], 1),
                    ('Which sampling method selects every kth individual from a list?', ['Stratified random', 'Cluster', 'Systematic', 'Simple random'], 2),
                    ('Sampling bias is most likely to occur when...', ['The sample size is too large', 'The selection method systematically excludes certain types of individuals', 'We conduct a census', 'We use stratified sampling'], 1),
                    ('A discrete variable differs from a continuous variable in that it...', ['Cannot be measured', 'Takes specific, countable values', 'Is always qualitative', 'Must be categorical'], 1),
                ]
            },
        },
    },
    'AP Environmental Science': {
        1: {
            '1.1': {
                'title': 'Energy Flow Through Ecosystems',
                'summaries': [
                    'An ecosystem is a community of interacting organisms and their abiotic physical environment, functioning as a unit through the flow of energy and cycling of matter. Energy entering an ecosystem comes primarily from the sun, where it is captured by producers (plants and photosynthetic organisms) through photosynthesis and converted into chemical energy stored in organic molecules. This energy then flows through trophic levels as organisms consume one another, with each transfer resulting in significant energy loss as heat through cellular respiration.',
                    'The 10% rule states that approximately 90% of the energy at one trophic level is lost to heat and cellular respiration, with only about 10% being available to organisms at the next trophic level as growth and reproduction. This low energy transfer efficiency means that ecosystems can support relatively few top predators compared to the enormous biomass of primary producers. The result is an energy pyramid, with a broad base of producers, a smaller layer of primary consumers (herbivores), fewer secondary consumers (carnivores), and very few tertiary consumers or top predators.',
                    'Trophic levels are hierarchical feeding levels in a food chain or food web: Producers (plants) occupy the first trophic level; Primary consumers (herbivores) occupy the second; Secondary consumers (carnivores) occupy the third; and Tertiary consumers (top carnivores) occupy the fourth or higher trophic level. Some organisms span multiple trophic levels as omnivores (eating both plants and meat) or detritivores (feeding on dead organic matter). Food webs, which consist of interconnected food chains, are more realistic representations of energy flow because most organisms feed on multiple species and are prey for multiple predators.',
                    'Efficiency in energy transfer can be calculated as (Total Energy Assimilated ÷ Total Energy Consumed) × 100%, with ecological efficiency typically around 10% for herbivores and 20% for carnivores due to differences in food digestibility and assimilation. This explains why agricultural systems producing animal protein (such as beef) are less efficient at feeding humans than plant-based agricultural systems, since plant protein requires fewer energy transfers. Understanding energy flow is essential for predicting carrying capacity of ecosystems, predicting population dynamics, and planning sustainable food production systems.'
                ],
                'flashcards': [
                    ('What is an ecosystem?', 'A community of organisms interacting with each other and their physical environment.'),
                    ('What is the primary source of energy for most ecosystems?', 'The sun. Producers capture light energy through photosynthesis.'),
                    ('What is the 10% rule?', 'Approximately 10% of energy is transferred to the next trophic level; 90% is lost as heat.'),
                    ('What are the four main trophic levels?', 'Producer, Primary consumer (herbivore), Secondary consumer, Tertiary consumer.'),
                    ('Define a food chain', 'A linear sequence showing energy transfer from producers through various trophic levels.'),
                    ('Why is a food web more realistic than a food chain?', 'Food webs show interconnected feeding relationships reflecting that most organisms eat multiple species and are preyed upon by multiple predators.'),
                    ('What is an omnivore?', 'An organism that feeds on both plants and animals, occupying multiple trophic levels.'),
                    ('What is a detritivore?', 'An organism that feeds on dead organic matter and decomposes, recycling nutrients.'),
                    ('Why are there fewer top predators than herbivores in an ecosystem?', 'Due to energy loss at each trophic level, there is much less energy available for top predators.'),
                    ('How does ecological efficiency affect food production?', 'Plant-based food production is more efficient than animal-based production because it requires fewer energy transfers.')
                ],
                'quiz_questions': [
                    ('Energy enters an ecosystem primarily through...', ['Decomposition', 'Photosynthesis by producers', 'Cellular respiration', 'Nutrients from soil'], 1),
                    ('The 10% rule explains why...', ['All energy is eventually lost', 'Ecosystems have pyramids of biomass', 'Top predators are rare compared to herbivores', 'Primary consumers outnumber producers'], 2),
                    ('A trophic level is defined by...', ['The type of organism', 'Its position in the food chain based on feeds and feeding', 'Its size', 'Its age'], 1),
                    ('In a food chain, producers are organisms that...', ['Consume plants and animals', 'Consume only plants', 'Manufacture food using light energy', 'Break down dead matter'], 2),
                    ('Which organism occupies multiple trophic levels?', ['Plants', 'Herbivores', 'Omnivores', 'Decomposers'], 2),
                    ('If producers in an ecosystem fix 10,000 kcal of energy, how much is available to secondary consumers?', ['10,000 kcal', '1,000 kcal', '100 kcal', '10 kcal'], 2),
                    ('Food webs are more realistic than food chains because they...', ['Show all organisms', 'Represent interconnected feeding relationships', 'Show energy flow', 'Include decomposers'], 1),
                ]
            },
        },
    },
    'AP Human Geography': {
        1: {
            '1.1': {
                'title': 'Geographic Scales and Spatial Perspectives',
                'summaries': [
                    'Geography examines phenomena across multiple scales of analysis, from the local scale (neighborhood, city) to the regional scale (state, country) to the national scale (entire country) to the global scale (world). Each scale offers different perspectives and contexts for understanding human phenomena such as culture, economy, politics, and environment. A phenomenon that appears one way at the local scale may have different meanings or causes when examined at the global scale, illustrating the importance of scale-dependent analysis in understanding complex human-environment relationships.',
                    'Place and location are foundational geographic concepts that, while related, have distinct meanings: location refers to the position of a place on Earth using geographic coordinates (absolute location) or in relation to other places (relative location), while place is a meaningful location imbued with cultural, social, historical, and personal significance. A house at 40°N, 75°W (a location) becomes a place through the memories, meanings, and social relationships associated with it. The same space can have different meanings in different cultural contexts, and places\'s meanings change over time as people, organizations, and events reshape them.',
                    'Spatial perspective emphasizes how geography connects places through patterns of interaction, influenced by distance, accessibility, and globalization. Globalization has reduced the friction of distance through advances in transportation and communication technology, allowing people, ideas, and products to flow across vast distances more rapidly. This has created a more interconnected world but has also led to cultural diffusion, economic interdependence, and environmental impacts that transcend local boundaries, making global-scale understanding increasingly important for addressing local issues.',
                    'Cartography, the art and science of map-making, involves representing the three-dimensional Earth on two-dimensional surfaces, which necessarily involves distortion. Different map projections preserve different properties—Mercator projects preserve direction and make navigation easier but distort area (making high-latitude regions appear larger); equal-area projections preserve relative sizes of regions but distort shape; Robinson projection is a compromise preserving moderate distortion of both property. Understanding map projections is essential for critically interpreting maps and recognizing how cartographic choices communicate certain perspectives and may perpetuate biases.'
                ],
                'flashcards': [
                    ('What is the difference between absolute and relative location?', 'Absolute location uses coordinates (latitude/longitude); relative location describes position relative to other places.'),
                    ('How are place and location different?', 'Location is the position on Earth; place includes cultural meaning and significance attached to location.'),
                    ('Define the local scale in geography', 'The scale of a neighborhood, city, or region; the scale at which people experience daily life.'),
                    ('What is the geographic scale of analysis?', 'The level of organizational complexity examined, from local to global, which affects how phenomena are understood.'),
                    ('What does cartography study?', 'The art and science of making maps, including methods of representing 3D Earth on 2D surfaces.'),
                    ('What is the Mercator projection and its main characteristic?', 'A map projection that preserves direction and is useful for navigation but distorts area, especially at high latitudes.'),
                    ('What is an equal-area projection?', 'A map projection that accurately represents relative sizes of regions, though it distorts shape.'),
                    ('How has globalization affected geographic scales?', 'It has increased connections between distant places through technology, transportation, and communication, reducing the friction of distance.'),
                    ('What is spatial perspective in geography?', 'An approach emphasizing how places connect through patterns of interaction, flows of people/ideas/goods, and geographic processes.'),
                    ('What is cultural diffusion?', 'The spread of cultural traits, ideas, practices, or innovations from one place or group to another.')
                ],
                'quiz_questions': [
                    ('The concept of scale in geography refers to...', ['Map scale', 'The level of geographic analysis from local to global', 'The size of geographic features', 'Relative vs. absolute location'], 1),
                    ('A place differs from a location in that place includes...', ['Exact coordinates', 'Cultural and social meaning', 'Direction and distance', 'Only physical characteristics'], 1),
                    ('Globalization has primarily affected geographic scale by...', ['Making local places irrelevant', 'Increasing connections across distances through technology and transportation', 'Centralizing all human activity', 'Eliminating regional differences'], 1),
                    ('Which map projection preserves accurate area but may distort shape?', ['Mercator', 'Equal-area', 'Robinson', 'Polar'], 1),
                    ('The term spatial perspective emphasizes...', ['Memorizing place names', 'How places connect through patterns of interaction and flows', 'Absolute location only', 'The importance of scale alone'], 1),
                    ('At the global scale, geographic analysis examines...', ['Individual neighborhoods', 'Countries and their boundaries', 'Worldwide patterns, processes, and interconnections', 'City-level phenomena'], 2),
                    ('Cultural diffusion is most enhanced by...', ['Geographic barriers', 'Globalization and improved transportation/communication', 'Isolation of regions', 'Increased local focus'], 1),
                ]
            },
        },
    },
    'AP Physics 2': {
        1: {
            '1.1': {
                'title': 'Fluids and Pressure',
                'summaries': [
                    'Pressure is defined as the normal force exerted per unit area, expressed mathematically as P = F/A and measured in pascals (Pa) in SI units. Unlike solids, fluids (liquids and gases) are unable to resist shear forces and therefore transmit pressure in all directions equally at any given depth. Hydrostatic pressure in a fluid at rest increases linearly with depth according to the equation P = ρgh, where ρ is the fluid density, g is gravitational acceleration, and h is the depth below the surface.',
                    'Archimedes\' Principle states that the buoyant force exerted on an object submerged in a fluid is equal to the weight of the fluid displaced by the object. This principle explains why objects float or sink: if the weight of the displaced fluid is greater than the weight of the object, the object experiences a net upward force and floats; if the weight of the object exceeds the weight of displaced fluid, it sinks. The buoyant force depends on the volume of the object and the density of the fluid, not on the mass or weight of the object itself.',
                    'Pascal\'s Principle states that pressure applied to an enclosed, incompressible fluid is transmitted undiminished throughout the fluid and to the walls of its container. This principle is the foundation of hydraulic systems, where a small force applied to a small piston can generate a large force on a large piston because pressure remains constant throughout the system (P = F₁/A₁ = F₂/A₂). Understanding fluid pressure is essential for designing pumps, brakes, and other hydraulic systems.',
                    'The continuity equation in fluid dynamics states that for an incompressible fluid flowing through a pipe or channel, the product of velocity and cross-sectional area is constant (A₁v₁ = A₂v₂). This means that when fluid flows through a narrower section of a tube, its velocity increases, and when it flows through a wider section, its velocity decreases. This principle explains phenomena such as why water flows faster out of a narrower nozzle and is essential for understanding flow rates in pipes and vessels.'
                ],
                'flashcards': [
                    ('Define pressure and give its SI unit', 'Pressure = Force/Area; SI unit is pascal (Pa) or N/m^2'),
                    ('What is hydrostatic pressure?', 'The pressure exerted by a fluid at rest at a given depth; increases with depth according to P = ρgh'),
                    ('State Archimedes\' Principle', 'The buoyant force on a submerged object equals the weight of fluid displaced by the object'),
                    ('When does an object float in a fluid?', 'When the buoyant force (weight of displaced fluid) is greater than or equal to the weight of the object'),
                    ('What is Pascal\'s Principle?', 'Pressure applied to an enclosed incompressible fluid is transmitted undiminished throughout the fluid'),
                    ('How is Pascal\'s Principle applied in hydraulic systems?', 'A small force on a small piston creates pressure that generates a large force on a larger piston'),
                    ('State the Continuity Equation', 'For an incompressible fluid, A₁v₁ = A₂v₂ (area times velocity is constant at all points)'),
                    ('What happens to velocity when fluid flow through a narrower section?', 'Velocity increases to maintain the same volumetric flow rate'),
                    ('What is atmospheric pressure at sea level?', '101.3 kPa or 1 atm'),
                    ('How does fluid pressure differ from pressure in solids?', 'Fluids transmit pressure equally in all directions; solids can support shear stress')
                ],
                'quiz_questions': [
                    ('Pressure in a static fluid increases with...', ['Temperature', 'Depth', 'Surface area', 'Container volume'], 1),
                    ('The SI unit for pressure is...', ['Newton (N)', 'Pascal (Pa)', 'Joule (J)', 'Watt (W)'], 1),
                    ('According to Archimedes\' Principle, the buoyant force depends on...', ['The mass of the object', 'The volume of fluid displaced and its density', 'The depth of the fluid', 'The temperature of the fluid'], 1),
                    ('A hydraulic lift works based on...', ['Archimedes\' Principle', 'Pascal\'s Principle', 'Continuity Equation', 'Boyle\'s Law'], 1),
                    ('In the Continuity Equation A₁v₁ = A₂v₂, if A₂ < A₁, then...', ['v₂ = v₁', 'v₂ < v₁', 'v₂ > v₁', 'v₂ is zero'], 2),
                    ('Water flows out of a faucet faster when the opening is smaller because...', ['Pressure increases', 'The Continuity Equation requires higher velocity in narrower sections', 'Gravity is stronger', 'The fluid is compressed'], 1),
                    ('Hydrostatic pressure at depth h is given by...', ['P = F/A', 'P = ρgh', 'P = nRT', 'P = P₀ + v²'], 1),
                ]
            },
        },
    },
    'AP Physics C - Mechanics': {
        1: {
            '1.1': {
                'title': 'Kinematics: Motion in One Dimension',
                'summaries': [
                    'Kinematics is the branch of mechanics that describes motion without considering the forces causing the motion. The fundamental kinematic quantities are displacement (change in position, a vector), velocity (rate of change of displacement, also a vector with both magnitude and direction), and acceleration (rate of change of velocity, a vector). Unlike distance (which measures total path length as a scalar) and speed (scalar magnitude of velocity), displacement and velocity include directional information essential for fully describing motion.',
                    'The five kinematic equations relate displacement (Δx), initial velocity (v₀), final velocity (v), acceleration (a), and time (t). These equations are valid only for constant acceleration motion: (1) v = v₀ + at, (2) Δx = v₀t + ½at², (3) v² = v₀² + 2aΔx, (4) Δx = vt - ½at² (using final velocity), and (5) Δx = ½(v₀ + v)t. Each equation is missing one of the five variables and is useful for solving problems where that variable is not needed.',
                    'Free fall is a special case of kinematics where the only force is gravity, giving objects a constant downward acceleration of g = 9.8 m/s² (or approximately 10 m/s² for estimates). Objects in free fall experience the same acceleration regardless of their mass, so a dropped bowling ball and feather fall at the same rate in the absence of air resistance. Starting from rest, an object free-falling for time t reaches a velocity of v = gt and falls a distance of d = ½gt².',
                    'Projectile motion combines horizontal and vertical kinematics independently: horizontal motion occurs at constant velocity (no acceleration in the horizontal direction), while vertical motion follows the equations for free fall with constant downward acceleration. The key insight is that these two motions are independent—the horizontal velocity does not affect vertical velocity or displacement, and vice versa. This allows us to solve projectile motion problems by treating horizontal and vertical components separately.'
                ],
                'flashcards': [
                    ('Define displacement', 'The vector quantity representing the change in position from initial to final location'),
                    ('What is the difference between distance and displacement?', 'Distance is the total path length (scalar); displacement is the straight-line change in position (vector)'),
                    ('Define velocity', 'The rate of change of displacement (vector quantity with magnitude and direction)'),
                    ('How does instantaneous velocity differ from average velocity?', 'Average velocity is total displacement over total time; instantaneous velocity is velocity at a specific instant'),
                    ('What is acceleration?', 'The rate of change of velocity (vector quantity)'),
                    ('State the five kinematic equations for constant acceleration', 'v = v₀ + at; Δx = v₀t + ½at²; v² = v₀² + 2aΔx; Δx = vt - ½at²; Δx = ½(v₀ + v)t'),
                    ('What is the acceleration due to gravity?', 'g = 9.8 m/s² or approximately 10 m/s² (directed downward)'),
                    ('In projectile motion, how are horizontal and vertical components treated?', 'They are treated independently; horizontal motion has constant velocity, vertical motion has constant acceleration'),
                    ('What does "free fall" mean in physics?', 'Motion under the influence of gravity alone, with acceleration g = 9.8 m/s² downward'),
                    ('Can two objects with different masses fall at different rates in the absence of air resistance?', 'No, all objects fall at the same rate with acceleration g regardless of mass')
                ],
                'quiz_questions': [
                    ('An object moves 3 meters east and then 4 meters west. Its displacement is...', ['7 meters west', '1 meter west', '7 meters', '1 meter east'], 3),
                    ('Velocity differs from speed because velocity is...', ['Always larger', 'A vector quantity with direction', 'Measured in m/s^2', 'Always zero at the turning point'], 1),
                    ('The kinematic equation v² = v₀² + 2aΔx does not include...', ['Velocity', 'Acceleration', 'Time', 'Displacement'], 2),
                    ('An object in free fall has...', ['Constant velocity', 'Constant acceleration of g = 9.8 m/s^2', 'Zero acceleration', 'Decreasing acceleration'], 1),
                    ('In projectile motion, horizontal velocity...', ['Increases due to gravity', 'Decreases due to air resistance', 'Remains constant', 'Becomes zero at maximum height'], 2),
                    ('Starting from rest, how far does an object fall in 2 seconds (g = 10 m/s^2)?', ['10 meters', '20 meters', '40 meters', '80 meters'], 2),
                    ('A bullet is fired horizontally from a cliff. Its horizontal velocity is...', ['Constant', 'Increasing', 'Decreasing', 'Zero at impact'], 0),
                ]
            },
        },
    },
}

def generate_enhanced_course_content(course_name: str, content_spec: Dict):
    """Generate enhanced content with 7 quiz questions, 10 flashcards, and detailed summaries"""
    
    # Handle special case for AP Physics C - Mechanics
    if course_name == 'AP Physics C - Mechanics':
        json_filename = 'ap_physics_c_-_mechanics_lessons.json'
    else:
        json_filename = f"{course_name.lower().replace(' ', '_').replace('-', '_')}_lessons.json"
    
    json_file = Path(__file__).parent / 'content_data' / json_filename
    
    print(f"\nGenerating enhanced content for {course_name}...")
    
    if not json_file.exists():
        print(f"[ERROR] File not found: {json_file}")
        return False
    
    with open(json_file, 'r', encoding='utf-8') as f:
        lessons_data = json.load(f)
    
    generated_count = 0
    
    for unit_num, lessons_in_unit in content_spec.items():
        unit_key = f"u{unit_num}"
        
        for lesson_num_str, lesson_content in lessons_in_unit.items():
            lesson_key = f"l{lesson_num_str}"
            lesson_id = f"{unit_key}_{lesson_key}"
            
            if lesson_id not in lessons_data:
                continue
            
            # Update title
            lessons_data[lesson_id]['title'] = lesson_content['title']
            
            # Generate summary sections from detailed summaries
            lessons_data[lesson_id]['summary_sections'] = []
            for i, summary_text in enumerate(lesson_content['summaries'], 1):
                lessons_data[lesson_id]['summary_sections'].append({
                    'title': f'Section {i}: {lesson_content["title"]}',
                    'content_html': f'<p>{summary_text}</p>',
                    'data_i18n': None
                })
            
            # Add 10 flashcards
            lessons_data[lesson_id]['flashcards'] = []
            for question, answer in lesson_content['flashcards']:
                lessons_data[lesson_id]['flashcards'].append({
                    'question': question,
                    'answer': answer,
                    'data_i18n_q': None,
                    'data_i18n_a': None
                })
            
            # Add 7 quiz questions
            lessons_data[lesson_id]['quiz_questions'] = []
            for i, (question_text, options, correct_idx) in enumerate(lesson_content['quiz_questions'], 1):
                quiz_q = {
                    'question_number': i,
                    'question_text': question_text,
                    'options': [],
                    'attempted': 2,
                    'data_i18n': None
                }
                
                for j, option_text in enumerate(options):
                    quiz_q['options'].append({
                        'text': option_text,
                        'is_correct': (j == correct_idx),
                        'data_i18n': None
                    })
                
                lessons_data[lesson_id]['quiz_questions'].append(quiz_q)
            
            generated_count += 1
            print(f"  [OK] {lesson_id}: {lesson_content['title']} (4 summaries, 10 flashcards, 7 quizzes)")
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(lessons_data, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] Generated enhanced content for {generated_count} lessons")
    return True


def main():
    print("="*70)
    print("ENHANCED AP COURSE CONTENT GENERATOR v2")
    print("Generating 7 quiz questions, 10 flashcards, and detailed summaries")
    print("="*70)
    
    results = {}
    
    for course_name, content_spec in ENHANCED_AP_CONTENT.items():
        results[course_name] = generate_enhanced_course_content(course_name, content_spec)
    
    # Summary
    print("\n" + "="*70)
    print("GENERATION SUMMARY")
    print("="*70)
    
    successful = sum(1 for v in results.values() if v)
    total = len(results)
    
    for course_name, success in results.items():
        status = "[OK]" if success else "[FAIL]"
        print(f"{course_name:30} {status}")
    
    print(f"\nTotal: {successful}/{total} courses completed successfully")


if __name__ == "__main__":
    main()
