#!/usr/bin/env python3
"""Generate Biology Unit Tests with 18 questions each."""

import os
import json
import random

# Unit topics from bio.html
UNITS = {
    1: {
        "title": "The Study of Life",
        "lessons": [
            "1.1 Introduction to Biology",
            "1.2 The Science of Life", 
            "1.3 The Nature of Science",
            "1.4 Characteristics of Life",
            "1.5 Levels of Biological Organization",
            "1.6 Branches of Biology",
            "1.7 Careers in Biology"
        ]
    },
    2: {
        "title": "Ecology",
        "lessons": [
            "2.1 Organisms and Their Relationships",
            "2.2 Flow of Energy in an Ecosystem",
            "2.3 Cycling of Matter",
            "2.4 Ecological Succession",
            "2.5 Niches and Habitat",
            "2.6 Food Chains, Webs, and Trophic Levels",
            "2.7 Human Impact on Ecosystems"
        ]
    },
    3: {
        "title": "Biomes and Biodiversity",
        "lessons": [
            "3.1 Community Ecology",
            "3.2 Biomes and Biodiversity",
            "3.3 Climate and Weather Patterns",
            "3.4 Terrestrial Biomes",
            "3.5 Aquatic Ecosystems"
        ]
    },
    4: {
        "title": "Evolution",
        "lessons": [
            "4.1 History of Evolutionary Thought",
            "4.2 Evidence of Evolution",
            "4.3 Sources of Genetic Variation",
            "4.4 Hardy-Weinberg Equilibrium",
            "4.5 Natural Selection and Adaptation",
            "4.6 Population Dynamics"
        ]
    },
    5: {
        "title": "Classification and Taxonomy",
        "lessons": [
            "5.1 Taxonomy Basics",
            "5.2 Cladistics and Classification",
            "5.3 Phylogenetic Trees",
            "5.4 Patterns of Evolution",
            "5.5 Speciation",
            "5.6 Domains and Kingdoms of Life"
        ]
    },
    6: {
        "title": "Cell Structure and Function",
        "lessons": [
            "6.1 Introduction to Cells",
            "6.2 Prokaryotic vs Eukaryotic Cells",
            "6.3 Organelles and Their Functions",
            "6.4 Membrane Transport",
            "6.5 Cell Communication",
            "6.6 Homeostasis"
        ]
    },
    7: {
        "title": "Cellular Respiration",
        "lessons": [
            "7.1 Overview of Cellular Respiration",
            "7.2 ATP and Cellular Energy",
            "7.3 Glycolysis",
            "7.4 The Krebs Cycle",
            "7.5 The Electron Transport Chain",
            "7.6 Fermentation"
        ]
    },
    8: {
        "title": "Photosynthesis",
        "lessons": [
            "8.1 Overview of Photosynthesis",
            "8.2 Chloroplast Structure",
            "8.3 Light-Dependent Reactions",
            "8.4 The Calvin Cycle",
            "8.5 Factors Affecting Photosynthesis"
        ]
    },
    9: {
        "title": "Cell Division - Mitosis",
        "lessons": [
            "9.1 Cell Growth and Division",
            "9.2 The Cell Cycle",
            "9.3 Mitosis",
            "9.4 Cytokinesis",
            "9.5 Cell Cycle Regulation and Cancer"
        ]
    },
    10: {
        "title": "Meiosis",
        "lessons": [
            "10.1 Overview of Meiosis",
            "10.2 Sexual Reproduction",
            "10.3 Meiosis I",
            "10.4 Meiosis II",
            "10.5 Crossing Over and Genetic Variation",
            "10.6 Nondisjunction and Genetic Disorders"
        ]
    },
    11: {
        "title": "Genetics",
        "lessons": [
            "11.1 Mendel and the Laws of Inheritance",
            "11.2 Monohybrid Crosses",
            "11.3 Dihybrid Crosses",
            "11.4 Non-Mendelian Inheritance",
            "11.5 Polygenic and Multifactorial Traits",
            "11.6 Human Genetics and Pedigrees"
        ]
    },
    12: {
        "title": "DNA and Biotechnology",
        "lessons": [
            "12.1 DNA Structure",
            "12.2 DNA Replication",
            "12.3 RNA and Transcription",
            "12.4 Protein Synthesis",
            "12.5 Genetic Engineering",
            "12.6 Biotechnology Applications"
        ]
    }
}

# Questions for each unit (18 questions with randomized correct answers)
UNIT_QUESTIONS = {
    1: [
        {"q": "What is the primary focus of biology as a scientific discipline?", "opts": ["The study of living organisms and their interactions", "The study of chemical reactions in laboratories", "The study of geological formations", "The study of weather patterns"], "correct": 0},
        {"q": "A scientist discovers a new organism that can reproduce, respond to stimuli, and maintain homeostasis, but does not appear to grow. What should the scientist conclude?", "opts": ["The organism may be in a dormant stage or growth occurs on a different timescale", "The organism is definitely not alive", "The organism is a type of mineral", "Growth is not an important characteristic"], "correct": 0},
        {"q": "Which characteristic of life explains why you shiver when cold and sweat when hot?", "opts": ["Reproduction", "Homeostasis", "Evolution", "Growth"], "correct": 1},
        {"q": "A plant bending toward sunlight demonstrates which characteristic of life?", "opts": ["Cellular organization", "Response to stimuli", "Reproduction", "Metabolism"], "correct": 1},
        {"q": "Which sequence correctly orders biological organization from smallest to largest?", "opts": ["Organ → Tissue → Cell → Organism", "Cell → Tissue → Organ → Organ System → Organism", "Tissue → Cell → Organ → Organism", "Organism → Organ System → Organ → Tissue"], "correct": 1},
        {"q": "At which level of organization would you study the interactions between a forest's trees, animals, fungi, and bacteria?", "opts": ["Organism", "Population", "Ecosystem", "Tissue"], "correct": 2},
        {"q": "A marine biologist studying whale migration patterns is working primarily at which level of organization?", "opts": ["Cellular", "Molecular", "Population", "Tissue"], "correct": 2},
        {"q": "Which branch of biology would study how antibiotic resistance spreads through bacterial populations over time?", "opts": ["Botany and zoology", "Anatomy and physiology", "Evolutionary biology and microbiology", "Marine biology only"], "correct": 2},
        {"q": "A scientist who studies the classification and naming of newly discovered species works in which field?", "opts": ["Ecology", "Genetics", "Physiology", "Taxonomy"], "correct": 3},
        {"q": "Which historical development was most crucial for biologists to confirm that all living things are made of cells?", "opts": ["The discovery of DNA structure", "The development of the scientific method", "The theory of evolution", "The invention of the microscope"], "correct": 3},
        {"q": "Darwin's theory of natural selection was revolutionary because it:", "opts": ["Provided a mechanism explaining how species change over time", "Was the first theory to suggest organisms reproduce", "Proved that all organisms are identical", "Showed that evolution does not occur"], "correct": 0},
        {"q": "In a controlled experiment testing fertilizer effects on plant growth, what serves as the control group?", "opts": ["Plants given the most fertilizer", "Plants grown without the fertilizer", "Plants grown in complete darkness", "Plants of different species"], "correct": 1},
        {"q": "Why must scientific experiments be repeatable by other researchers?", "opts": ["To make the original scientist famous", "To waste time and resources", "To verify the results are reliable and not due to error", "Repetition is not actually important"], "correct": 2},
        {"q": "CRISPR-Cas9 technology has revolutionized biology by allowing scientists to:", "opts": ["View atoms for the first time", "Travel back in time", "Eliminate all diseases instantly", "Edit specific genes with high precision"], "correct": 3},
        {"q": "How has DNA sequencing technology most impacted the field of taxonomy?", "opts": ["It allows classification based on genetic relationships rather than appearance alone", "It eliminated the need to study organisms", "It proved all organisms are unrelated", "It replaced microscopes entirely"], "correct": 0},
        {"q": "A hypothesis differs from a theory because a hypothesis:", "opts": ["Cannot be tested, while a theory can", "Is a testable prediction while a theory is well-supported by extensive evidence", "Is always correct, while a theory is always wrong", "Requires no observations"], "correct": 1},
        {"q": "Which career would involve studying disease outbreaks and their spread through populations?", "opts": ["Botanist", "Paleontologist", "Epidemiologist", "Marine biologist"], "correct": 2},
        {"q": "What distinguishes a scientific theory from a scientific law?", "opts": ["A theory explains why phenomena occur, a law describes what occurs", "A theory is proven while a law is unproven", "A law is more important than a theory", "There is no difference"], "correct": 0}
    ],
    2: [
        {"q": "What is the primary role of producers in an ecosystem?", "opts": ["Convert sunlight into chemical energy through photosynthesis", "Decompose dead organic matter", "Hunt and consume other organisms", "Break down nutrients in the soil"], "correct": 0},
        {"q": "In a food web, what would happen if all the primary consumers were removed?", "opts": ["Producers would decrease", "Producer populations would increase initially", "Nothing would change", "Secondary consumers would increase"], "correct": 1},
        {"q": "Which biogeochemical cycle involves the process of nitrogen fixation by bacteria?", "opts": ["Water cycle", "Carbon cycle", "Nitrogen cycle", "Phosphorus cycle"], "correct": 2},
        {"q": "During ecological succession, which community would you expect to appear first on bare rock?", "opts": ["Trees", "Grasses", "Shrubs", "Lichens and mosses"], "correct": 3},
        {"q": "An organism's niche includes:", "opts": ["Only its physical location", "Only its food sources", "Its role, resources used, and interactions with other species", "Only its predators"], "correct": 2},
        {"q": "At which trophic level is the most energy available?", "opts": ["Tertiary consumers", "Secondary consumers", "Primary consumers", "Producers"], "correct": 3},
        {"q": "What percentage of energy is typically transferred from one trophic level to the next?", "opts": ["100%", "50%", "10%", "1%"], "correct": 2},
        {"q": "Deforestation primarily affects the carbon cycle by:", "opts": ["Increasing carbon absorption", "Releasing stored carbon and reducing carbon uptake", "Increasing photosynthesis rates", "Having no effect"], "correct": 1},
        {"q": "Which type of relationship describes both organisms benefiting?", "opts": ["Parasitism", "Mutualism", "Commensalism", "Predation"], "correct": 1},
        {"q": "The greenhouse effect is primarily caused by:", "opts": ["Atmospheric gases trapping heat", "Ozone depletion", "Increased precipitation", "Volcanic activity only"], "correct": 0},
        {"q": "What is the term for the maximum population size an environment can sustain?", "opts": ["Population density", "Growth rate", "Carrying capacity", "Birth rate"], "correct": 2},
        {"q": "Primary succession differs from secondary succession because primary succession:", "opts": ["Occurs faster", "Begins in an area with no existing soil", "Only occurs in water", "Requires no pioneer species"], "correct": 1},
        {"q": "A climax community is characterized by:", "opts": ["Constant rapid change", "Stability and self-perpetuation", "Absence of biodiversity", "No decomposers"], "correct": 1},
        {"q": "Eutrophication in aquatic ecosystems is caused by:", "opts": ["Excess nutrients leading to algal blooms", "Decreased water temperature", "Increased predation", "Reduced sunlight"], "correct": 0},
        {"q": "Which organism would be classified as a decomposer?", "opts": ["Eagle", "Grass", "Mushroom", "Rabbit"], "correct": 2},
        {"q": "Biomagnification refers to:", "opts": ["Increasing organism size", "Concentration of toxins increasing up the food chain", "Decreasing biodiversity", "Increasing temperatures"], "correct": 1},
        {"q": "What is the relationship between a tick and a dog?", "opts": ["Mutualism", "Commensalism", "Parasitism", "Competition"], "correct": 2},
        {"q": "Invasive species often cause problems because they:", "opts": ["Lack natural predators in the new environment", "Increase biodiversity", "Improve ecosystem stability", "Reduce competition"], "correct": 0}
    ],
    3: [
        {"q": "Which factor primarily determines the type of biome found in a region?", "opts": ["Human activity", "Temperature and precipitation", "Soil color", "Ocean currents only"], "correct": 1},
        {"q": "The tundra biome is characterized by:", "opts": ["High rainfall and dense forests", "Permafrost and low-growing vegetation", "Hot temperatures year-round", "High biodiversity of trees"], "correct": 1},
        {"q": "In which biome would you find the greatest biodiversity?", "opts": ["Desert", "Tundra", "Tropical rainforest", "Grassland"], "correct": 2},
        {"q": "What adaptation helps desert plants survive with limited water?", "opts": ["Large leaves", "Shallow roots", "Thick waxy cuticles and water-storing tissues", "Deciduous leaves"], "correct": 2},
        {"q": "The photic zone in aquatic ecosystems is important because:", "opts": ["It is the coldest region", "Sunlight penetrates allowing photosynthesis", "It has the highest pressure", "No organisms live there"], "correct": 1},
        {"q": "Coral reefs are found primarily in:", "opts": ["Deep ocean trenches", "Warm, shallow, clear tropical waters", "Arctic regions", "Freshwater lakes"], "correct": 1},
        {"q": "What distinguishes a freshwater ecosystem from a marine ecosystem?", "opts": ["Temperature only", "Salt concentration", "Presence of fish", "Depth only"], "correct": 1},
        {"q": "Estuaries are important because they:", "opts": ["Have no life", "Serve as nurseries for many marine species", "Are too salty for life", "Have constant temperatures"], "correct": 1},
        {"q": "Which biome has the most dramatic temperature variations between seasons?", "opts": ["Tropical rainforest", "Temperate deciduous forest", "Desert", "Taiga"], "correct": 3},
        {"q": "Grasslands are characterized by:", "opts": ["Dense tree coverage", "Moderate rainfall supporting grasses but few trees", "Extreme cold", "High humidity year-round"], "correct": 1},
        {"q": "The rain shadow effect causes:", "opts": ["Increased rainfall on both sides of mountains", "Dry conditions on the leeward side of mountains", "Uniform precipitation everywhere", "No effect on climate"], "correct": 1},
        {"q": "Competition between species for the same resources is called:", "opts": ["Mutualism", "Parasitism", "Interspecific competition", "Predation"], "correct": 2},
        {"q": "A keystone species is important because:", "opts": ["It is the largest species", "Removing it causes major ecosystem changes", "It is the most abundant species", "It has no predators"], "correct": 1},
        {"q": "The benthic zone refers to:", "opts": ["The surface of a lake", "The bottom of an aquatic ecosystem", "The atmosphere", "The canopy of forests"], "correct": 1},
        {"q": "Which adaptation is common in taiga (boreal forest) trees?", "opts": ["Broad deciduous leaves", "Needle-like leaves and conical shape", "No leaves at all", "Thick bark only"], "correct": 1},
        {"q": "Biodiversity is highest at the equator because:", "opts": ["There is less competition", "Stable warm temperatures and high energy input", "There are more predators", "Fewer diseases exist"], "correct": 1},
        {"q": "What role do wetlands play in ecosystems?", "opts": ["They serve no purpose", "They filter water, provide habitat, and reduce flooding", "They only harbor mosquitoes", "They reduce biodiversity"], "correct": 1}
    ],
    4: [
        {"q": "Who proposed the theory of natural selection?", "opts": ["Charles Darwin and Alfred Russel Wallace", "Gregor Mendel", "Louis Pasteur", "Watson and Crick"], "correct": 0},
        {"q": "Homologous structures provide evidence for evolution because they:", "opts": ["Have identical functions", "Show common ancestry despite different functions", "Are identical in all species", "Only appear in mammals"], "correct": 1},
        {"q": "Fossils in deeper rock layers are generally:", "opts": ["Younger than fossils in upper layers", "Older than fossils in upper layers", "The same age as all fossils", "Not useful for dating"], "correct": 1},
        {"q": "Which is NOT a source of genetic variation?", "opts": ["Mutation", "Sexual reproduction", "Mitosis producing identical cells", "Crossing over"], "correct": 2},
        {"q": "Natural selection acts directly on:", "opts": ["Genes", "Phenotypes", "Alleles", "Chromosomes"], "correct": 1},
        {"q": "For Hardy-Weinberg equilibrium to occur, which condition must be met?", "opts": ["Population must be small", "Mating must be random", "Natural selection must occur", "Migration must be common"], "correct": 1},
        {"q": "If p = 0.6 for a dominant allele, what is the frequency of homozygous recessive individuals (q²)?", "opts": ["0.36", "0.16", "0.48", "0.04"], "correct": 1},
        {"q": "Genetic drift has the greatest effect on:", "opts": ["Large populations", "Small populations", "All populations equally", "Only plant populations"], "correct": 1},
        {"q": "The founder effect is an example of:", "opts": ["Natural selection", "Genetic drift", "Gene flow", "Sexual selection"], "correct": 1},
        {"q": "Analogous structures are similar because of:", "opts": ["Common ancestry", "Similar environmental pressures (convergent evolution)", "Genetic drift", "Sexual selection"], "correct": 1},
        {"q": "Vestigial structures are:", "opts": ["Fully functional organs", "Organs with reduced or no function that were useful in ancestors", "Only found in humans", "Evidence against evolution"], "correct": 1},
        {"q": "Stabilizing selection tends to:", "opts": ["Favor extreme phenotypes", "Reduce variation by favoring average phenotypes", "Split populations", "Increase mutation rates"], "correct": 1},
        {"q": "Directional selection occurs when:", "opts": ["Average phenotypes are favored", "One extreme phenotype is favored", "Both extremes are favored", "No phenotypes are favored"], "correct": 1},
        {"q": "Disruptive selection can lead to:", "opts": ["Reduced variation", "Speciation by favoring extreme phenotypes", "Extinction only", "No evolutionary change"], "correct": 1},
        {"q": "Fitness in evolutionary terms refers to:", "opts": ["Physical strength", "Reproductive success", "Lifespan", "Size"], "correct": 1},
        {"q": "Which evidence of evolution involves comparing DNA sequences?", "opts": ["Fossil record", "Homologous structures", "Molecular biology", "Biogeography"], "correct": 2},
        {"q": "Adaptive radiation occurs when:", "opts": ["Species become extinct", "One species rapidly diversifies into many species filling different niches", "Populations shrink", "Migration stops"], "correct": 1},
        {"q": "The bottleneck effect results from:", "opts": ["Gradual population growth", "A drastic reduction in population size", "Increased genetic diversity", "Immigration"], "correct": 1}
    ],
    5: [
        {"q": "The science of classifying and naming organisms is called:", "opts": ["Ecology", "Genetics", "Taxonomy", "Physiology"], "correct": 2},
        {"q": "Binomial nomenclature uses which two taxonomic levels?", "opts": ["Kingdom and phylum", "Family and order", "Genus and species", "Class and order"], "correct": 2},
        {"q": "Which taxonomic level is most inclusive?", "opts": ["Species", "Genus", "Family", "Domain"], "correct": 3},
        {"q": "Cladistics classifies organisms based on:", "opts": ["Physical appearance only", "Shared derived characteristics", "Size and color", "Habitat"], "correct": 1},
        {"q": "A phylogenetic tree shows:", "opts": ["The size of organisms", "Evolutionary relationships", "Geographic distribution", "Population sizes"], "correct": 1},
        {"q": "Organisms that share a more recent common ancestor are:", "opts": ["Less closely related", "More closely related", "From different domains", "Always the same species"], "correct": 1},
        {"q": "Convergent evolution produces:", "opts": ["Homologous structures", "Analogous structures", "Vestigial structures", "Identical DNA"], "correct": 1},
        {"q": "Allopatric speciation occurs when:", "opts": ["Populations are physically separated", "Populations live together", "No barriers exist", "Only in water"], "correct": 0},
        {"q": "Sympatric speciation can occur through:", "opts": ["Geographic isolation", "Polyploidy or habitat differentiation", "Migration only", "Extinction"], "correct": 1},
        {"q": "The three domains of life are:", "opts": ["Plants, Animals, Fungi", "Bacteria, Archaea, Eukarya", "Protists, Bacteria, Animals", "Vertebrates, Invertebrates, Plants"], "correct": 1},
        {"q": "Which domain includes organisms with membrane-bound organelles?", "opts": ["Bacteria", "Archaea", "Eukarya", "All of them"], "correct": 2},
        {"q": "Archaea differ from Bacteria in:", "opts": ["Cell wall composition and genetics", "Having no DNA", "Being multicellular", "Not being prokaryotes"], "correct": 0},
        {"q": "The kingdom Animalia includes organisms that are:", "opts": ["Autotrophic and unicellular", "Heterotrophic and multicellular", "Photosynthetic", "All prokaryotic"], "correct": 1},
        {"q": "A derived character is:", "opts": ["An ancestral trait", "A trait that evolved in a recent ancestor", "Found in all organisms", "Not useful in classification"], "correct": 1},
        {"q": "An outgroup in cladistics is used to:", "opts": ["Show the oldest organisms", "Determine which characters are ancestral vs derived", "Include all organisms", "Measure DNA"], "correct": 1},
        {"q": "Linnaeus organized his classification system based primarily on:", "opts": ["DNA sequences", "Physical similarities", "Behavior", "Geographic location"], "correct": 1},
        {"q": "Reproductive isolation is important for speciation because:", "opts": ["It increases mutation", "It prevents gene flow between populations", "It increases migration", "It has no effect"], "correct": 1},
        {"q": "The correct order of taxonomic classification from broadest to most specific is:", "opts": ["Species, Genus, Family, Order, Class, Phylum, Kingdom, Domain", "Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species", "Kingdom, Domain, Phylum, Order, Class, Family, Genus, Species", "Domain, Phylum, Kingdom, Class, Order, Family, Genus, Species"], "correct": 1}
    ],
    6: [
        {"q": "The cell theory states that:", "opts": ["Only animals have cells", "All living things are made of cells, cells are the basic unit of life, and cells come from existing cells", "Cells can arise spontaneously", "Only plants have cells"], "correct": 1},
        {"q": "Which organelle is found in both prokaryotic and eukaryotic cells?", "opts": ["Nucleus", "Mitochondria", "Ribosomes", "Endoplasmic reticulum"], "correct": 2},
        {"q": "The primary difference between prokaryotic and eukaryotic cells is:", "opts": ["Size only", "The presence of a membrane-bound nucleus", "Cell wall composition", "Number of chromosomes"], "correct": 1},
        {"q": "Which organelle is the site of protein synthesis?", "opts": ["Mitochondria", "Ribosome", "Golgi apparatus", "Lysosome"], "correct": 1},
        {"q": "The mitochondria is often called the powerhouse of the cell because it:", "opts": ["Stores genetic information", "Produces ATP through cellular respiration", "Synthesizes proteins", "Digests cellular waste"], "correct": 1},
        {"q": "The cell membrane is described as a fluid mosaic because:", "opts": ["It is made of water", "Phospholipids and proteins can move within the membrane", "It is solid", "It contains only lipids"], "correct": 1},
        {"q": "Osmosis is the diffusion of:", "opts": ["Solutes across a membrane", "Water across a selectively permeable membrane", "Proteins across a membrane", "Gases only"], "correct": 1},
        {"q": "If a cell is placed in a hypertonic solution, water will:", "opts": ["Move into the cell", "Move out of the cell", "Not move", "Both directions equally"], "correct": 1},
        {"q": "Active transport differs from passive transport because it:", "opts": ["Does not require energy", "Requires energy (ATP)", "Only moves water", "Only moves small molecules"], "correct": 1},
        {"q": "The endoplasmic reticulum with ribosomes attached is called:", "opts": ["Smooth ER", "Rough ER", "Golgi apparatus", "Lysosome"], "correct": 1},
        {"q": "The Golgi apparatus functions to:", "opts": ["Produce ATP", "Modify, package, and ship proteins", "Copy DNA", "Store water"], "correct": 1},
        {"q": "Lysosomes contain:", "opts": ["DNA", "Digestive enzymes", "Chlorophyll", "Ribosomes"], "correct": 1},
        {"q": "Plant cells differ from animal cells by having:", "opts": ["Mitochondria", "Cell wall, chloroplasts, and large central vacuole", "Ribosomes", "A nucleus"], "correct": 1},
        {"q": "Signal transduction involves:", "opts": ["Cells ignoring signals", "Converting an extracellular signal into an intracellular response", "Only electrical signals", "DNA replication"], "correct": 1},
        {"q": "Homeostasis refers to:", "opts": ["Rapid change in conditions", "Maintaining a stable internal environment", "Reproduction", "Growth only"], "correct": 1},
        {"q": "Facilitated diffusion requires:", "opts": ["ATP", "Transport proteins but no energy", "Endocytosis", "Active transport"], "correct": 1},
        {"q": "Which molecule is the main component of the cell membrane?", "opts": ["Carbohydrates", "Phospholipids", "DNA", "Proteins only"], "correct": 1},
        {"q": "Receptor proteins in the cell membrane function to:", "opts": ["Provide structure only", "Receive chemical signals from other cells", "Transport water", "Store energy"], "correct": 1}
    ],
    7: [
        {"q": "The overall equation for cellular respiration is:", "opts": ["C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP", "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂", "CO₂ + H₂O → O₂ + glucose", "ATP → ADP + energy"], "correct": 0},
        {"q": "ATP is considered the energy currency of the cell because:", "opts": ["It is made of gold", "It stores and releases energy for cellular work", "It is the largest molecule", "It contains oxygen"], "correct": 1},
        {"q": "Glycolysis occurs in which part of the cell?", "opts": ["Mitochondria", "Nucleus", "Cytoplasm", "Ribosome"], "correct": 2},
        {"q": "Glycolysis produces a net gain of:", "opts": ["4 ATP", "2 ATP and 2 NADH", "38 ATP", "No ATP"], "correct": 1},
        {"q": "The products of glycolysis that enter the Krebs cycle are:", "opts": ["Glucose", "Pyruvate (converted to Acetyl-CoA)", "Water", "Carbon dioxide"], "correct": 1},
        {"q": "The Krebs cycle takes place in the:", "opts": ["Cytoplasm", "Mitochondrial matrix", "Nucleus", "Ribosome"], "correct": 1},
        {"q": "The electron transport chain is located in the:", "opts": ["Cytoplasm", "Nucleus", "Inner mitochondrial membrane", "Ribosome"], "correct": 2},
        {"q": "The final electron acceptor in the electron transport chain is:", "opts": ["Carbon dioxide", "Glucose", "Oxygen", "Water"], "correct": 2},
        {"q": "The majority of ATP in cellular respiration is produced during:", "opts": ["Glycolysis", "Krebs cycle", "Electron transport chain", "Fermentation"], "correct": 2},
        {"q": "Fermentation occurs when:", "opts": ["Oxygen is plentiful", "Oxygen is absent or limited", "Only in plants", "ATP is not needed"], "correct": 1},
        {"q": "Lactic acid fermentation occurs in:", "opts": ["Plants only", "Muscle cells during intense exercise", "Only bacteria", "Mitochondria"], "correct": 1},
        {"q": "Alcoholic fermentation produces:", "opts": ["Lactic acid", "Ethanol and CO₂", "Oxygen", "Glucose"], "correct": 1},
        {"q": "NADH and FADH₂ function as:", "opts": ["Final products", "Electron carriers", "Enzymes", "Hormones"], "correct": 1},
        {"q": "How many ATP molecules are theoretically produced from one glucose molecule?", "opts": ["2", "4", "36-38", "100"], "correct": 2},
        {"q": "Chemiosmosis involves:", "opts": ["Breaking down glucose", "H⁺ ions flowing through ATP synthase to produce ATP", "Producing NADH only", "Glycolysis"], "correct": 1},
        {"q": "What molecule is regenerated to continue glycolysis?", "opts": ["ATP", "NAD⁺", "FADH₂", "Acetyl-CoA"], "correct": 1},
        {"q": "The purpose of cellular respiration is to:", "opts": ["Store glucose", "Release energy from food molecules to make ATP", "Produce oxygen", "Build proteins"], "correct": 1},
        {"q": "Aerobic respiration requires:", "opts": ["No oxygen", "Oxygen", "Only glucose", "Light"], "correct": 1}
    ],
    8: [
        {"q": "The overall equation for photosynthesis is:", "opts": ["C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O", "6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂", "ATP → ADP + energy", "O₂ → CO₂"], "correct": 1},
        {"q": "Photosynthesis occurs in which organelle?", "opts": ["Mitochondria", "Chloroplast", "Ribosome", "Nucleus"], "correct": 1},
        {"q": "The pigment primarily responsible for capturing light energy is:", "opts": ["Carotene", "Xanthophyll", "Chlorophyll", "Melanin"], "correct": 2},
        {"q": "Light-dependent reactions occur in the:", "opts": ["Stroma", "Thylakoid membranes", "Cytoplasm", "Matrix"], "correct": 1},
        {"q": "The Calvin cycle occurs in the:", "opts": ["Thylakoid", "Stroma", "Grana", "Mitochondria"], "correct": 1},
        {"q": "What is produced during the light-dependent reactions?", "opts": ["Glucose only", "ATP, NADPH, and O₂", "CO₂", "Water"], "correct": 1},
        {"q": "The oxygen released during photosynthesis comes from:", "opts": ["Carbon dioxide", "Water molecules", "Glucose", "ATP"], "correct": 1},
        {"q": "The Calvin cycle uses ATP and NADPH to:", "opts": ["Split water", "Fix carbon dioxide into glucose", "Release oxygen", "Produce chlorophyll"], "correct": 1},
        {"q": "Carbon fixation refers to:", "opts": ["Releasing CO₂", "Converting CO₂ into organic compounds", "Producing oxygen", "Breaking down glucose"], "correct": 1},
        {"q": "The enzyme that fixes CO₂ in the Calvin cycle is:", "opts": ["ATP synthase", "RuBisCO", "Helicase", "Polymerase"], "correct": 1},
        {"q": "Photosystem II and Photosystem I work together to:", "opts": ["Break down glucose", "Split water, transfer electrons, and produce ATP and NADPH", "Produce CO₂", "Release heat"], "correct": 1},
        {"q": "Which factors affect the rate of photosynthesis?", "opts": ["Light intensity, CO₂ concentration, and temperature", "Only water", "Only oxygen", "None"], "correct": 0},
        {"q": "At high temperatures, the rate of photosynthesis:", "opts": ["Always increases", "May decrease as enzymes denature", "Stays constant", "Is not affected"], "correct": 1},
        {"q": "When light intensity increases, photosynthesis rate:", "opts": ["Decreases", "Increases until reaching a maximum", "Stays same", "Stops completely"], "correct": 1},
        {"q": "The light-independent reactions are also called:", "opts": ["Glycolysis", "The dark reactions or Calvin cycle", "Krebs cycle", "Fermentation"], "correct": 1},
        {"q": "How many turns of the Calvin cycle are needed to produce one glucose molecule?", "opts": ["1", "3", "6", "12"], "correct": 2},
        {"q": "The primary purpose of photosynthesis is to:", "opts": ["Release oxygen", "Convert light energy into chemical energy stored in glucose", "Break down food", "Produce water"], "correct": 1}
    ],
    9: [
        {"q": "Why is cell division necessary for living organisms?", "opts": ["To produce energy", "For growth, repair, and reproduction", "To release oxygen", "To break down food"], "correct": 1},
        {"q": "The cell cycle consists of:", "opts": ["Only mitosis", "Interphase and M phase (mitosis and cytokinesis)", "Only cytokinesis", "Only DNA replication"], "correct": 1},
        {"q": "During which phase does DNA replication occur?", "opts": ["Mitosis", "S phase of interphase", "G1 phase", "Cytokinesis"], "correct": 1},
        {"q": "The correct order of mitosis phases is:", "opts": ["Anaphase, Metaphase, Prophase, Telophase", "Prophase, Metaphase, Anaphase, Telophase", "Telophase, Prophase, Anaphase, Metaphase", "Metaphase, Prophase, Telophase, Anaphase"], "correct": 1},
        {"q": "During prophase:", "opts": ["Chromosomes line up at the cell center", "Chromatin condenses into chromosomes and the nuclear envelope breaks down", "Sister chromatids separate", "The cell divides"], "correct": 1},
        {"q": "Chromosomes align at the cell's equator during:", "opts": ["Prophase", "Metaphase", "Anaphase", "Telophase"], "correct": 1},
        {"q": "Sister chromatids separate and move to opposite poles during:", "opts": ["Prophase", "Metaphase", "Anaphase", "Telophase"], "correct": 2},
        {"q": "During telophase:", "opts": ["Chromosomes condense", "Nuclear envelopes reform and chromosomes decondense", "Chromosomes align", "DNA replicates"], "correct": 1},
        {"q": "Cytokinesis in animal cells involves:", "opts": ["Cell plate formation", "Cleavage furrow pinching the cell in two", "No division", "DNA replication"], "correct": 1},
        {"q": "In plant cells, cytokinesis involves formation of:", "opts": ["Cleavage furrow", "Cell plate", "Spindle fibers only", "Centrioles"], "correct": 1},
        {"q": "The spindle fibers attach to chromosomes at the:", "opts": ["Telomere", "Centromere (kinetochore)", "Chromatid arm", "Nuclear envelope"], "correct": 1},
        {"q": "Checkpoints in the cell cycle:", "opts": ["Speed up division", "Ensure proper cell division and prevent errors", "Only occur in cancer", "Have no function"], "correct": 1},
        {"q": "Cancer cells differ from normal cells because they:", "opts": ["Divide in a controlled manner", "Divide uncontrollably, ignoring checkpoints", "Do not divide", "Only divide once"], "correct": 1},
        {"q": "The G1 checkpoint checks for:", "opts": ["Chromosome alignment", "Cell size, nutrients, and DNA damage", "Spindle attachment", "Cytokinesis completion"], "correct": 1},
        {"q": "The G2 checkpoint ensures:", "opts": ["Cell size is adequate", "DNA has replicated completely and correctly", "Chromosomes are aligned", "Cell plate has formed"], "correct": 1},
        {"q": "Cyclins and CDKs regulate:", "opts": ["Photosynthesis", "The cell cycle", "Respiration", "Digestion"], "correct": 1},
        {"q": "Tumor suppressor genes normally function to:", "opts": ["Promote cell division", "Slow or stop cell division", "Increase mutation rate", "Cause cancer"], "correct": 1}
    ],
    10: [
        {"q": "The purpose of meiosis is to:", "opts": ["Produce identical cells", "Produce gametes with half the chromosome number", "Repair damaged tissue", "Grow larger"], "correct": 1},
        {"q": "Meiosis produces:", "opts": ["2 diploid cells", "4 haploid cells", "4 diploid cells", "2 haploid cells"], "correct": 1},
        {"q": "Diploid (2n) means:", "opts": ["One set of chromosomes", "Two sets of chromosomes", "No chromosomes", "Four sets of chromosomes"], "correct": 1},
        {"q": "Haploid (n) cells contain:", "opts": ["Two sets of chromosomes", "One set of chromosomes", "No DNA", "Twice the normal DNA"], "correct": 1},
        {"q": "Homologous chromosomes pair up during:", "opts": ["Mitosis", "Meiosis I prophase", "Meiosis II", "Interphase"], "correct": 1},
        {"q": "Crossing over occurs during:", "opts": ["Metaphase II", "Prophase I", "Anaphase I", "Telophase II"], "correct": 1},
        {"q": "Crossing over increases genetic variation by:", "opts": ["Creating mutations", "Exchanging genetic material between homologous chromosomes", "Doubling DNA", "Deleting genes"], "correct": 1},
        {"q": "During Meiosis I, what separates?", "opts": ["Sister chromatids", "Homologous chromosomes", "Centrioles", "Organelles"], "correct": 1},
        {"q": "During Meiosis II, what separates?", "opts": ["Homologous chromosomes", "Sister chromatids", "Spindle fibers", "Nuclei"], "correct": 1},
        {"q": "How does Meiosis II differ from mitosis?", "opts": ["Meiosis II separates homologs", "Meiosis II starts with haploid cells, not diploid", "They are identical", "Meiosis II has DNA replication"], "correct": 1},
        {"q": "Independent assortment refers to:", "opts": ["Chromosomes always lining up the same way", "Random orientation of homologous pairs at metaphase I", "Crossing over", "Sister chromatid separation"], "correct": 1},
        {"q": "How many genetically unique gametes can be produced from one human cell undergoing meiosis?", "opts": ["4", "Millions due to crossing over and independent assortment", "46", "2"], "correct": 1},
        {"q": "Nondisjunction is:", "opts": ["Normal chromosome separation", "The failure of chromosomes to separate properly", "Crossing over", "DNA replication"], "correct": 1},
        {"q": "Down syndrome results from:", "opts": ["Too few chromosomes", "Nondisjunction causing trisomy 21", "Missing sex chromosome", "Deletion"], "correct": 1},
        {"q": "Klinefelter syndrome (XXY) results from:", "opts": ["Normal meiosis", "Nondisjunction of sex chromosomes", "Autosomal trisomy", "Deletion"], "correct": 1},
        {"q": "Turner syndrome (XO) is characterized by:", "opts": ["Extra X chromosome", "Having only one X chromosome and no second sex chromosome", "Extra Y chromosome", "Normal chromosomes"], "correct": 1},
        {"q": "Synapsis is:", "opts": ["Cell division", "The pairing of homologous chromosomes", "Sister chromatid separation", "Spindle formation"], "correct": 1},
        {"q": "A tetrad consists of:", "opts": ["Two chromosomes", "Four sister chromatids (two homologous chromosomes paired)", "One chromosome", "Four cells"], "correct": 1}
    ],
    11: [
        {"q": "Gregor Mendel is known as the father of genetics because he:", "opts": ["Discovered DNA", "Established fundamental laws of inheritance using pea plants", "Cloned organisms", "Invented the microscope"], "correct": 1},
        {"q": "The law of segregation states that:", "opts": ["Alleles blend together", "Allele pairs separate during gamete formation", "All traits are linked", "Mutations always occur"], "correct": 1},
        {"q": "The law of independent assortment states that:", "opts": ["Genes on the same chromosome always stay together", "Genes for different traits segregate independently", "All genes are linked", "Crossing over never occurs"], "correct": 1},
        {"q": "In a monohybrid cross Aa × Aa, the phenotypic ratio is:", "opts": ["1:1", "3:1", "9:3:3:1", "1:2:1"], "correct": 1},
        {"q": "The genotypic ratio of Aa × Aa is:", "opts": ["3:1", "1:2:1", "9:3:3:1", "1:1:1:1"], "correct": 1},
        {"q": "A dihybrid cross between AaBb × AaBb produces a phenotypic ratio of:", "opts": ["3:1", "1:2:1", "9:3:3:1", "1:1"], "correct": 2},
        {"q": "Incomplete dominance results in:", "opts": ["One allele completely masking the other", "A blended intermediate phenotype", "Both phenotypes showing equally", "No phenotype"], "correct": 1},
        {"q": "Codominance occurs when:", "opts": ["One allele is dominant", "Both alleles are fully expressed", "Alleles blend", "Neither allele is expressed"], "correct": 1},
        {"q": "An example of codominance is:", "opts": ["Height in humans", "AB blood type", "Eye color", "Widow's peak"], "correct": 1},
        {"q": "Multiple alleles means:", "opts": ["More than two alleles exist for a gene in a population", "A gene has only two alleles", "Alleles blend", "Genes are linked"], "correct": 0},
        {"q": "Polygenic inheritance involves:", "opts": ["One gene controlling one trait", "Multiple genes contributing to one trait", "One gene controlling multiple traits", "No genes involved"], "correct": 1},
        {"q": "An example of a polygenic trait in humans is:", "opts": ["Blood type", "Skin color", "Hitchhiker's thumb", "Tongue rolling"], "correct": 1},
        {"q": "Sex-linked traits are usually carried on the:", "opts": ["Y chromosome only", "X chromosome", "Autosomes", "Mitochondria"], "correct": 1},
        {"q": "Why are males more likely to express X-linked recessive disorders?", "opts": ["They have two X chromosomes", "They have only one X chromosome, so one recessive allele causes the trait", "They are stronger", "Y chromosome dominates"], "correct": 1},
        {"q": "A pedigree chart is used to:", "opts": ["Map genes on chromosomes", "Trace inheritance patterns in families", "Sequence DNA", "Clone organisms"], "correct": 1},
        {"q": "A carrier is an individual who:", "opts": ["Shows the recessive trait", "Has one recessive allele but doesn't show the trait", "Is homozygous dominant", "Has no alleles"], "correct": 1},
        {"q": "Epistasis occurs when:", "opts": ["Two genes are on the same chromosome", "One gene affects the expression of another gene", "Genes are on different chromosomes", "All alleles are codominant"], "correct": 1},
        {"q": "Pleiotropy means:", "opts": ["One gene affects multiple traits", "Multiple genes affect one trait", "Genes don't affect traits", "All traits are dominant"], "correct": 0}
    ],
    12: [
        {"q": "DNA is composed of nucleotides, each containing:", "opts": ["Sugar, phosphate, and a nitrogenous base", "Amino acids", "Lipids", "Only phosphate"], "correct": 0},
        {"q": "The four nitrogenous bases in DNA are:", "opts": ["Adenine, Uracil, Guanine, Cytosine", "Adenine, Thymine, Guanine, Cytosine", "Adenine, Thymine, Guanine, Uracil", "Only Adenine and Thymine"], "correct": 1},
        {"q": "According to base-pairing rules, adenine pairs with:", "opts": ["Guanine", "Cytosine", "Thymine", "Uracil"], "correct": 2},
        {"q": "DNA replication is described as semiconservative because:", "opts": ["Both strands are copied together", "Each new DNA molecule contains one original and one new strand", "DNA is not conserved", "Both strands are new"], "correct": 1},
        {"q": "The enzyme that unwinds DNA during replication is:", "opts": ["DNA polymerase", "Helicase", "Ligase", "Primase"], "correct": 1},
        {"q": "DNA polymerase functions to:", "opts": ["Unwind DNA", "Add nucleotides to the new strand", "Join Okazaki fragments", "Produce RNA"], "correct": 1},
        {"q": "RNA differs from DNA because RNA:", "opts": ["Is double-stranded", "Contains uracil instead of thymine and has ribose sugar", "Contains thymine", "Has no bases"], "correct": 1},
        {"q": "Transcription produces:", "opts": ["DNA", "mRNA from a DNA template", "Protein", "Lipids"], "correct": 1},
        {"q": "Transcription occurs in the:", "opts": ["Ribosome", "Cytoplasm", "Nucleus", "Mitochondria only"], "correct": 2},
        {"q": "Translation occurs at the:", "opts": ["Nucleus", "Ribosome", "Golgi", "Chloroplast"], "correct": 1},
        {"q": "A codon is:", "opts": ["A three-nucleotide sequence in mRNA coding for an amino acid", "A single nucleotide", "A protein", "Part of DNA only"], "correct": 0},
        {"q": "The start codon AUG codes for:", "opts": ["Stop signal", "Methionine", "Glycine", "Tryptophan"], "correct": 1},
        {"q": "tRNA functions to:", "opts": ["Carry genetic information", "Bring amino acids to the ribosome", "Copy DNA", "Store energy"], "correct": 1},
        {"q": "CRISPR-Cas9 is used for:", "opts": ["Copying DNA only", "Precise gene editing", "Protein synthesis", "Energy production"], "correct": 1},
        {"q": "PCR (polymerase chain reaction) is used to:", "opts": ["Delete genes", "Amplify specific DNA sequences", "Translate mRNA", "Edit genes"], "correct": 1},
        {"q": "A GMO (genetically modified organism) has:", "opts": ["No DNA", "DNA that has been altered using genetic engineering", "Only natural mutations", "No genes"], "correct": 1},
        {"q": "Gel electrophoresis separates DNA fragments based on:", "opts": ["Color", "Size", "Shape only", "Temperature"], "correct": 1},
        {"q": "Gene therapy aims to:", "opts": ["Remove all genes", "Treat diseases by correcting defective genes", "Create new species", "Eliminate DNA"], "correct": 1}
    ]
}

def shuffle_options(q_data):
    """Shuffle options and return question with proper format."""
    opts = q_data["opts"].copy()
    correct_answer = opts[q_data["correct"]]
    random.shuffle(opts)
    new_correct_idx = opts.index(correct_answer)
    correct_letter = chr(ord('a') + new_correct_idx)
    return {
        "q": q_data["q"],
        "a": opts[0],
        "b": opts[1],
        "c": opts[2],
        "d": opts[3],
        "correct": correct_letter
    }

def generate_test_html(unit_num, title, questions):
    """Generate HTML for a unit test."""
    questions_html = []
    
    for i, q_data in enumerate(questions, 1):
        q = shuffle_options(q_data)
        question_html = f'''<div class="quiz-question" data-attempts="2" style="margin-bottom: 2rem;">
<div class="attempts-indicator">Attempts left: 2</div>
<p style="font-weight: 700; font-size: 1.1rem; margin-bottom: 1rem;">{i}. {q['q']}</p>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q{i}" style="margin-right:0.5rem;" type="radio" value="a"/> {q['a']}
</label>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q{i}" style="margin-right:0.5rem;" type="radio" value="b"/> {q['b']}
</label>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q{i}" style="margin-right:0.5rem;" type="radio" value="c"/> {q['c']}
</label>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q{i}" style="margin-right:0.5rem;" type="radio" value="d"/> {q['d']}
</label>
<button class="side-button" onclick="checkQuizAnswer('q{i}', '{q['correct']}', this)" style="margin-top:0.5rem; font-size:1rem; padding:0.5rem 1rem; min-width:auto;" type="button">Check Answer</button>
<button class="side-button" onclick="getAnotherQuestion(this)" style="margin-top:0.5rem; font-size:1rem; padding:0.5rem 1rem; min-width:auto; margin-left:0.5rem; background: #64748b;" type="button">Get another question</button>
</div>'''
        questions_html.append(question_html)
    
    all_questions = '\n'.join(questions_html)
    
    html = f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Unit {unit_num}: Unit Test</title>
<script src="/_sdk/element_sdk.js"></script>
<script src="../../scripts/global_translations.js?v=3.2"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;family=Playfair+Display:wght@700&amp;display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
<style>@view-transition {{ navigation: auto; }}</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
<script src="../../theme_manager.js"></script>
</head>
<body class="dark-mode h-full">
<script src="../../scripts/taskbar.js"></script>
<main class="main-container">
<div id="practice-content-view" style="display:none;">
<h2 class="page-title">Unit {unit_num} Practice</h2>
</div>

<div id="quiz-content-view">
<h2 class="page-title">Unit {unit_num}: {title} - Unit Test</h2>
<div class="diagram-card">
<div class="quiz-container">
<form id="quiz-form">
{all_questions}
</form>
<div id="quiz-results" style="margin-top: 2rem; font-weight: bold; display:none; padding: 1rem; border-radius: 0.5rem;"></div>
<div class="summary-actions" style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
<button type="button" class="side-button" onclick="window.location.href='../../bio.html'">Back to Biology</button>
</div>
</div>
</div>
</div>
</main>
<script src="../../scripts/unit_test.js"></script>
<script src="/quiz_logic.js"></script>

<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
<script src="/ArisEdu Project Folder/scripts/game_utils.js"></script>
</body></html>
'''
    return html

def main():
    base_path = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\BiologyLessons"
    
    for unit_num in range(1, 13):
        unit_data = UNITS[unit_num]
        questions = UNIT_QUESTIONS[unit_num]
        
        unit_folder = os.path.join(base_path, f"Unit{unit_num}")
        test_file = os.path.join(unit_folder, f"Unit{unit_num}_Test.html")
        
        html_content = generate_test_html(unit_num, unit_data["title"], questions)
        
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Generated Unit {unit_num} Test: {test_file}")
    
    print("\nAll unit tests generated successfully!")

if __name__ == "__main__":
    main()
