"""Add flashcards to all 73 Biology lessons (summaries & quizzes already exist)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "biology_lessons.json")

FC = {
    # ── Unit 1: Introduction to Biology ────────────────────────────
    "u1_l1.1": [
        ("Biology", "The scientific study of life and living organisms."),
        ("Organism", "Any individual living thing, from bacteria to blue whales."),
        ("Cell", "The basic structural and functional unit of all living organisms."),
        ("Biosphere", "The global sum of all ecosystems; everywhere life exists on Earth."),
        ("Evolution", "Change in heritable characteristics of populations over successive generations."),
    ],
    "u1_l1.2": [
        ("Scientific Method", "A systematic process: observe → hypothesize → experiment → analyze → conclude."),
        ("Hypothesis", "A testable, falsifiable prediction about the natural world."),
        ("Variable", "A factor that can change in an experiment (independent, dependent, controlled)."),
        ("Control Group", "The group in an experiment that is not exposed to the independent variable."),
        ("Peer Review", "Evaluation of scientific work by other qualified experts before publication."),
    ],
    "u1_l1.3": [
        ("Theory", "A well-supported explanation of natural phenomena, backed by extensive evidence."),
        ("Observation", "Using the senses or instruments to gather information about the natural world."),
        ("Inference", "A logical conclusion drawn from observations and prior knowledge."),
        ("Qualitative Data", "Descriptive, non-numerical observations (e.g., color, shape)."),
        ("Quantitative Data", "Numerical measurements (e.g., mass, temperature, length)."),
    ],
    "u1_l1.4": [
        ("Homeostasis", "The maintenance of stable internal conditions despite external changes."),
        ("Metabolism", "All chemical reactions within an organism that sustain life."),
        ("Reproduction", "The biological process by which organisms produce offspring."),
        ("Growth and Development", "Increase in size and complexity following genetic instructions."),
        ("Response to Stimuli", "The ability of organisms to react to environmental changes."),
    ],
    "u1_l1.5": [
        ("Levels of Organization", "Atom → molecule → organelle → cell → tissue → organ → organ system → organism → population → community → ecosystem → biosphere."),
        ("Population", "A group of individuals of the same species living in the same area."),
        ("Community", "All populations of different species living and interacting in an area."),
        ("Ecosystem", "A community of organisms and their physical environment interacting as a system."),
        ("Organ System", "A group of organs that work together to perform a major body function."),
    ],
    "u1_l1.6": [
        ("Zoology", "The branch of biology that studies animals."),
        ("Botany", "The branch of biology that studies plants."),
        ("Microbiology", "The study of microscopic organisms including bacteria, viruses, and fungi."),
        ("Genetics", "The study of heredity and the variation of inherited characteristics."),
        ("Ecology", "The study of interactions among organisms and their environment."),
    ],
    "u1_l1.7": [
        ("Biomedical Research", "Applying biology to develop medical treatments and technologies."),
        ("Marine Biologist", "A scientist who studies organisms in ocean and saltwater environments."),
        ("Epidemiologist", "A scientist who studies the spread and control of diseases in populations."),
        ("Forensic Biologist", "Uses biological evidence (DNA, blood) in criminal investigations."),
        ("Biotechnologist", "Applies biological processes for industrial, medical, or agricultural purposes."),
    ],

    # ── Unit 2: Ecology ───────────────────────────────────────────
    "u2_l2.1": [
        ("Symbiosis", "A close, long-term interaction between two species (mutualism, commensalism, parasitism)."),
        ("Predator-Prey Relationship", "Interaction where one organism hunts and feeds on another."),
        ("Competition", "Two or more organisms striving for the same limited resource."),
        ("Mutualism", "A symbiotic relationship in which both species benefit."),
        ("Parasitism", "A relationship where one organism benefits at the expense of another."),
    ],
    "u2_l2.2": [
        ("Producer", "An organism that makes its own food, usually by photosynthesis (autotroph)."),
        ("Consumer", "An organism that obtains energy by eating other organisms (heterotroph)."),
        ("Decomposer", "An organism that breaks down dead organic material, recycling nutrients."),
        ("Trophic Level", "Each step in a food chain where energy is transferred."),
        ("10% Rule", "Only about 10% of energy is passed from one trophic level to the next."),
    ],
    "u2_l2.3": [
        ("Carbon Cycle", "The biogeochemical cycle by which carbon is exchanged among the biosphere, geosphere, hydrosphere, and atmosphere."),
        ("Nitrogen Cycle", "The cycle of nitrogen conversion: fixation → nitrification → assimilation → denitrification."),
        ("Water Cycle", "Continuous movement of water: evaporation → condensation → precipitation → runoff."),
        ("Phosphorus Cycle", "Movement of phosphorus through the lithosphere, hydrosphere, and biosphere (no gas phase)."),
        ("Biogeochemical Cycle", "The pathway by which a chemical element moves through biotic and abiotic parts of an ecosystem."),
    ],
    "u2_l2.4": [
        ("Ecological Succession", "The gradual process by which ecosystems change and develop over time."),
        ("Primary Succession", "Succession on bare, lifeless surfaces (e.g., lava flows) – starts with pioneer species."),
        ("Secondary Succession", "Succession after a disturbance that leaves soil intact (e.g., after a fire)."),
        ("Pioneer Species", "The first organisms to colonize a barren area (e.g., lichens, mosses)."),
        ("Climax Community", "A stable, mature ecological community with little net change in species composition."),
    ],
    "u2_l2.5": [
        ("Niche", "An organism's role in its ecosystem, including its habitat, diet, and interactions."),
        ("Habitat", "The physical environment where an organism lives."),
        ("Fundamental Niche", "The full range of conditions and resources an organism could potentially use."),
        ("Realized Niche", "The actual conditions and resources an organism uses, limited by competition."),
        ("Competitive Exclusion", "Two species competing for the same niche cannot coexist indefinitely."),
    ],
    "u2_l2.6": [
        ("Food Chain", "A linear pathway showing who eats whom in an ecosystem."),
        ("Food Web", "A complex network of interconnected food chains in an ecosystem."),
        ("Primary Consumer", "An herbivore that feeds directly on producers (first trophic level of consumers)."),
        ("Secondary Consumer", "A carnivore or omnivore that eats primary consumers."),
        ("Tertiary Consumer", "A top predator that feeds on secondary consumers."),
    ],
    "u2_l2.7": [
        ("Deforestation", "Large-scale removal of forests, reducing biodiversity and increasing CO₂."),
        ("Pollution", "Introduction of harmful substances or energy into the environment."),
        ("Invasive Species", "Non-native organisms that spread and harm ecosystems when introduced."),
        ("Habitat Fragmentation", "Division of habitats into smaller, isolated patches by human activity."),
        ("Sustainability", "Meeting present needs without compromising future generations' ability to meet theirs."),
    ],

    # ── Unit 3: Community Ecology ──────────────────────────────────
    "u3_l3.1": [
        ("Species Richness", "The number of different species in a community."),
        ("Species Diversity", "A measure combining species richness and the evenness of their abundances."),
        ("Keystone Species", "A species with a disproportionately large effect on its ecosystem relative to its abundance."),
        ("Indicator Species", "A species whose presence or absence reflects environmental conditions."),
        ("Foundation Species", "A species that creates or maintains a habitat (e.g., coral, trees)."),
    ],
    "u3_l3.2": [
        ("Biome", "A large region characterized by its climate and dominant plant and animal life."),
        ("Tundra", "A cold, treeless biome with permafrost; short growing season."),
        ("Tropical Rainforest", "A warm, wet biome near the equator with the highest biodiversity."),
        ("Temperate Deciduous Forest", "A biome with moderate climate and trees that lose leaves seasonally."),
        ("Desert", "A biome receiving less than 25 cm of precipitation per year."),
    ],
    "u3_l3.3": [
        ("Freshwater Ecosystem", "Aquatic ecosystems with low salt concentration (lakes, rivers, wetlands)."),
        ("Marine Ecosystem", "Saltwater ecosystems including oceans, coral reefs, and estuaries."),
        ("Estuary", "A partially enclosed coastal body where freshwater and saltwater mix; highly productive."),
        ("Photic Zone", "The upper layer of water that receives enough light for photosynthesis."),
        ("Aphotic Zone", "The deep-water zone below the photic zone where no light penetrates."),
    ],
    "u3_l3.4": [
        ("Climate Change", "Long-term shift in global temperatures and weather patterns, largely driven by CO₂ emissions."),
        ("Greenhouse Effect", "Atmospheric gases trap heat, warming Earth's surface — enhanced by human activity."),
        ("Coral Bleaching", "Loss of symbiotic algae from coral due to water temperature stress."),
        ("Range Shift", "Species moving to higher latitudes or elevations as temperatures change."),
        ("Phenological Change", "Shifts in the timing of biological events (flowering, migration) due to climate change."),
    ],
    "u3_l3.5": [
        ("Commensalism", "A symbiotic relationship where one species benefits and the other is unaffected."),
        ("Amensalism", "An interaction where one species is harmed while the other is unaffected."),
        ("Coevolution", "Two species reciprocally influencing each other's evolution over time."),
        ("Mimicry", "Resemblance of one species to another for protection (Batesian) or mutual warning (Müllerian)."),
        ("Herbivory", "A form of predation where an organism eats plant material."),
    ],

    # ── Unit 4: Population ─────────────────────────────────────────
    "u4_l4.1": [
        ("Population Density", "The number of individuals per unit area or volume."),
        ("Birth Rate", "The number of births per 1,000 individuals per year."),
        ("Death Rate", "The number of deaths per 1,000 individuals per year."),
        ("Growth Rate", "The change in population size per time period: r = birth rate − death rate."),
        ("Immigration/Emigration", "Immigration: moving into a population. Emigration: moving out."),
    ],
    "u4_l4.2": [
        ("Exponential Growth", "Population growth in an ideal environment with unlimited resources (J-curve)."),
        ("Logistic Growth", "Population growth that slows as it approaches carrying capacity (S-curve)."),
        ("Demographic Transition", "The shift from high birth/death rates to low birth/death rates as societies develop."),
        ("Age Structure Diagram", "A graphical tool showing the distribution of age groups in a population."),
        ("Doubling Time", "The time it takes for a population to double; approx. 70 / growth rate (%)."),
    ],
    "u4_l4.3": [
        ("Carrying Capacity (K)", "The maximum population size an environment can sustain indefinitely."),
        ("Limiting Factor", "An environmental factor that restricts population growth (food, space, disease)."),
        ("Density-Dependent Factor", "A limiting factor whose effect depends on population density (disease, competition)."),
        ("Density-Independent Factor", "A limiting factor that affects a population regardless of density (natural disasters)."),
        ("Resource Depletion", "Exhaustion of a resource faster than it can be replenished."),
    ],
    "u4_l4.4": [
        ("r-Strategist", "Species that produce many offspring with little parental care (bacteria, insects)."),
        ("K-Strategist", "Species that produce few offspring with extensive parental care (elephants, whales)."),
        ("Population Crash", "A rapid decline in population size, often following overshooting carrying capacity."),
        ("Predator-Prey Cycle", "Oscillating population sizes of predators and prey that track each other."),
        ("Survivorship Curves", "Graphs showing survival rates per age group: Type I (late loss), II (constant), III (early loss)."),
    ],
    "u4_l4.5": [
        ("Conservation Biology", "The science of protecting and managing biodiversity and ecosystems."),
        ("Sustainable Development", "Development that meets current needs without compromising future generations."),
        ("Endangered Species", "A species at serious risk of extinction."),
        ("Protected Area", "A region managed to conserve nature (national parks, wildlife reserves)."),
        ("Restoration Ecology", "The science of restoring degraded or damaged ecosystems."),
    ],

    # ── Unit 5: Biodiversity ──────────────────────────────────────
    "u5_l5.1": [
        ("Biodiversity", "The variety of life at all levels: genetic, species, and ecosystem diversity."),
        ("Genetic Diversity", "The range of genetic variation within a species."),
        ("Species Diversity", "The number and relative abundance of species in an area."),
        ("Ecosystem Diversity", "The variety of different ecosystems in a given area."),
        ("Hotspot", "A region with exceptionally high biodiversity that is under threat."),
    ],
    "u5_l5.2": [
        ("Habitat Loss", "Destruction or degradation of natural habitats — the #1 threat to biodiversity."),
        ("Overexploitation", "Harvesting species faster than they can reproduce (overfishing, poaching)."),
        ("Pollution", "Contamination of air, water, or soil that harms organisms and ecosystems."),
        ("Invasive Species", "Non-native organisms that outcompete, prey on, or bring disease to native species."),
        ("Extinction Rate", "The rate at which species disappear; currently 100–1000× the natural background rate."),
    ],
    "u5_l5.3": [
        ("In-situ Conservation", "Protecting species in their natural habitats (national parks, reserves)."),
        ("Ex-situ Conservation", "Protecting species outside their habitats (zoos, seed banks, captive breeding)."),
        ("Biodiversity Hotspot", "An area with at least 1,500 endemic plant species that has lost ≥70% of habitat."),
        ("Reintroduction", "Releasing captive-bred or relocated organisms back into the wild."),
        ("Genetic Bank", "A facility that stores genetic material (seeds, sperm, DNA) for conservation."),
    ],
    "u5_l5.4": [
        ("Endangered Species Act", "US law protecting species listed as endangered or threatened."),
        ("IUCN Red List", "A global assessment of species' conservation status (LC, VU, EN, CR, EX)."),
        ("Captive Breeding", "Breeding endangered species in controlled settings for later reintroduction."),
        ("Habitat Corridor", "A strip of habitat connecting isolated patches, allowing wildlife movement."),
        ("Poaching", "Illegal hunting or capturing of animals, often for trade in body parts."),
    ],
    "u5_l5.5": [
        ("CITES", "Convention on International Trade in Endangered Species — regulates wildlife trade."),
        ("UNESCO World Heritage Site", "A place of cultural or natural significance protected under international treaty."),
        ("Community-Based Conservation", "Local people managing and benefiting from conservation efforts."),
        ("Ecotourism", "Responsible travel to natural areas that conserves the environment and improves local welfare."),
        ("Paris Agreement", "2015 international accord to limit global warming, indirectly protecting biodiversity."),
    ],

    # ── Unit 6: Chemistry of Life ──────────────────────────────────
    "u6_l6.1": [
        ("Atom", "The smallest unit of an element that retains its chemical properties."),
        ("Element", "A pure substance consisting of only one type of atom (e.g., C, H, O, N)."),
        ("Covalent Bond", "A chemical bond formed by sharing electron pairs between atoms."),
        ("Ionic Bond", "A bond formed by the transfer of electrons from one atom to another."),
        ("Hydrogen Bond", "A weak attraction between a hydrogen atom and an electronegative atom (O, N, F)."),
    ],
    "u6_l6.2": [
        ("Chemical Reaction", "A process that rearranges atoms to form new substances."),
        ("Enzyme", "A biological catalyst that speeds up chemical reactions without being consumed."),
        ("Activation Energy", "The minimum energy needed to start a chemical reaction."),
        ("Substrate", "The molecule(s) that an enzyme acts upon."),
        ("Active Site", "The region on an enzyme where the substrate binds."),
    ],
    "u6_l6.3": [
        ("Polarity", "Unequal sharing of electrons gives water molecules a partial positive and negative end."),
        ("Cohesion", "Water molecules sticking to each other via hydrogen bonds."),
        ("Adhesion", "Water molecules sticking to other surfaces."),
        ("Solvent", "A substance (often water) that dissolves a solute."),
        ("pH Scale", "Measures acidity/basicity; 7 is neutral, <7 is acidic, >7 is basic."),
    ],
    "u6_l6.4": [
        ("Carbohydrate", "Organic molecule (sugars, starches, cellulose) used for energy and structure; monomer: monosaccharide."),
        ("Lipid", "Hydrophobic organic molecules (fats, oils, waxes, phospholipids) for energy storage and membranes."),
        ("Protein", "Polymers of amino acids; functions include enzymes, structure, transport, and defense."),
        ("Nucleic Acid", "DNA and RNA; polymers of nucleotides that store and transmit genetic information."),
        ("Monomer/Polymer", "Monomer: a small repeating unit. Polymer: a large molecule made of linked monomers."),
    ],
    "u6_l6.5": [
        ("DNA", "Deoxyribonucleic acid — double helix carrying genetic instructions."),
        ("RNA", "Ribonucleic acid — single-stranded molecule involved in protein synthesis (mRNA, tRNA, rRNA)."),
        ("Nucleotide", "The monomer of nucleic acids: a sugar, phosphate group, and nitrogenous base."),
        ("Base Pairing", "A–T and G–C in DNA; A–U and G–C in RNA."),
        ("Double Helix", "The twisted-ladder shape of DNA, held together by hydrogen bonds between bases."),
    ],
    "u6_l6.6": [
        ("Dehydration Synthesis", "A reaction that joins monomers by removing a water molecule."),
        ("Hydrolysis", "Breaking a polymer into monomers by adding a water molecule."),
        ("Amino Acid", "The monomer of proteins; 20 common types, each with a unique R-group."),
        ("Saturated Fat", "A lipid with no double bonds between carbon atoms; solid at room temperature."),
        ("Unsaturated Fat", "A lipid with one or more double bonds; liquid at room temperature (oils)."),
    ],

    # ── Unit 7: Cell Biology ──────────────────────────────────────
    "u7_l7.1": [
        ("Cell Theory", "All living things are made of cells; cells are the basic unit of life; cells come from pre-existing cells."),
        ("Nucleus", "Membrane-bound organelle containing DNA; the cell's control center."),
        ("Cytoplasm", "The gel-like substance inside the cell membrane, containing organelles."),
        ("Mitochondria", "Organelle that produces ATP through cellular respiration — the 'powerhouse.'"),
        ("Ribosome", "Cellular structure where proteins are synthesized."),
    ],
    "u7_l7.2": [
        ("Robert Hooke", "First to observe and name 'cells' using cork in 1665."),
        ("Anton van Leeuwenhoek", "First to observe living microorganisms through a microscope."),
        ("Matthias Schleiden", "Concluded all plants are made of cells (1838)."),
        ("Theodor Schwann", "Concluded all animals are made of cells (1839)."),
        ("Rudolf Virchow", "Proposed that all cells arise from pre-existing cells (1855)."),
    ],
    "u7_l7.3": [
        ("Plasma Membrane", "A selectively permeable phospholipid bilayer surrounding the cell."),
        ("Phospholipid Bilayer", "Two layers of phospholipids with hydrophilic heads and hydrophobic tails."),
        ("Fluid Mosaic Model", "Model describing the membrane as a dynamic structure with proteins floating in a lipid bilayer."),
        ("Channel Protein", "A membrane protein that allows specific ions or molecules to pass through."),
        ("Cholesterol", "A lipid embedded in the membrane that maintains fluidity across temperatures."),
    ],
    "u7_l7.4": [
        ("Diffusion", "Movement of molecules from high to low concentration."),
        ("Osmosis", "Diffusion of water across a selectively permeable membrane."),
        ("Active Transport", "Movement of substances against the concentration gradient, requiring ATP."),
        ("Endocytosis", "The cell engulfs material by folding inward (phagocytosis, pinocytosis)."),
        ("Exocytosis", "The cell exports material by fusing vesicles with the plasma membrane."),
    ],
    "u7_l7.5": [
        ("Endoplasmic Reticulum", "Rough ER: protein synthesis/modification; Smooth ER: lipid synthesis/detox."),
        ("Golgi Apparatus", "Modifies, sorts, and packages proteins and lipids for transport."),
        ("Lysosome", "Organelle containing digestive enzymes to break down waste and foreign material."),
        ("Chloroplast", "Organelle in plant cells where photosynthesis occurs; contains chlorophyll."),
        ("Vacuole", "Storage organelle; large central vacuole in plant cells maintains turgor pressure."),
    ],
    "u7_l7.6": [
        ("Prokaryote", "A cell with no membrane-bound nucleus or organelles (bacteria, archaea)."),
        ("Eukaryote", "A cell with a membrane-bound nucleus and organelles (plants, animals, fungi, protists)."),
        ("Nucleoid", "The region in a prokaryote where the circular DNA is concentrated."),
        ("Cell Wall", "A rigid layer outside the plasma membrane in plants, fungi, and most bacteria."),
        ("Flagellum", "A whip-like structure used for cell movement, found in bacteria and some eukaryotes."),
    ],
    "u7_l7.7": [
        ("Light Microscope", "Uses visible light and lenses; magnifies up to ~1,000×."),
        ("Electron Microscope", "Uses electron beams for much higher magnification (up to ~2,000,000×)."),
        ("SEM (Scanning Electron Microscope)", "Produces detailed 3D images of cell surfaces."),
        ("TEM (Transmission Electron Microscope)", "Produces detailed 2D images of thin internal cell sections."),
        ("Staining", "Applying dye to cells to increase contrast and reveal structures under a microscope."),
    ],

    # ── Unit 8: Energy ─────────────────────────────────────────────
    "u8_l8.1": [
        ("Autotroph", "An organism that produces its own food from inorganic compounds (e.g., plants)."),
        ("Heterotroph", "An organism that obtains food by consuming other organisms."),
        ("Chemotroph", "An organism that obtains energy from chemical reactions (chemoautotrophs, chemoheterotrophs)."),
        ("Phototroph", "An organism that uses light energy to produce food (photosynthesis)."),
        ("Energy", "The ability to do work; life requires a constant input of energy."),
    ],
    "u8_l8.2": [
        ("ATP", "Adenosine triphosphate — the primary energy currency of cells."),
        ("ADP", "Adenosine diphosphate — formed when ATP releases energy by losing a phosphate."),
        ("Phosphorylation", "Adding a phosphate group to a molecule, often transferring energy from ATP."),
        ("Exergonic Reaction", "A reaction that releases energy (ΔG < 0)."),
        ("Endergonic Reaction", "A reaction that absorbs energy (ΔG > 0); often coupled with ATP hydrolysis."),
    ],
    "u8_l8.3": [
        ("Photosynthesis Equation", "6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂."),
        ("Chlorophyll", "A green pigment that absorbs light energy for photosynthesis."),
        ("Light Reactions", "Occur in thylakoids; convert light energy to ATP and NADPH, releasing O₂."),
        ("Calvin Cycle", "Occurs in the stroma; uses ATP and NADPH to fix CO₂ into glucose."),
        ("Thylakoid", "A membrane-bound compartment inside chloroplasts where light reactions occur."),
    ],
    "u8_l8.4": [
        ("Cellular Respiration Equation", "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP."),
        ("Glycolysis", "The first stage of respiration; splits glucose into 2 pyruvate in the cytoplasm (net 2 ATP)."),
        ("Krebs Cycle", "Occurs in the mitochondrial matrix; produces CO₂, NADH, FADH₂, and 2 ATP per glucose."),
        ("Electron Transport Chain", "Proteins in inner mitochondrial membrane use NADH/FADH₂ to produce ~34 ATP."),
        ("Aerobic", "Requiring oxygen; cellular respiration produces ~36–38 ATP per glucose aerobically."),
    ],
    "u8_l8.5": [
        ("Fermentation", "Anaerobic process that regenerates NAD⁺ so glycolysis can continue without O₂."),
        ("Lactic Acid Fermentation", "Pyruvate → lactic acid; occurs in muscle cells during intense exercise."),
        ("Alcoholic Fermentation", "Pyruvate → ethanol + CO₂; carried out by yeast."),
        ("Anaerobic", "Not requiring oxygen; fermentation yields only 2 ATP per glucose."),
        ("NAD⁺", "An electron carrier that is reduced to NADH during glycolysis and the Krebs cycle."),
    ],
    "u8_l8.6": [
        ("Chemiosmosis", "Movement of H⁺ ions through ATP synthase to generate ATP."),
        ("ATP Synthase", "An enzyme that uses the flow of H⁺ across a membrane to synthesize ATP."),
        ("Electron Carrier", "Molecules (NADH, FADH₂) that shuttle high-energy electrons to the ETC."),
        ("Coupled Reactions", "Energy released by an exergonic reaction drives an endergonic one."),
        ("Energy Pyramid", "Diagram showing energy loss at each trophic level (approximately 90% lost as heat)."),
    ],

    # ── Unit 9: Cell Division ──────────────────────────────────────
    "u9_l9.1": [
        ("Cell Cycle", "The ordered sequence of events from one cell division to the next (interphase + M phase)."),
        ("Interphase", "The phase where the cell grows and copies its DNA (G₁, S, G₂)."),
        ("Chromosome", "A coiled structure of DNA and protein; humans have 46 (23 pairs)."),
        ("Chromatid", "One copy of a duplicated chromosome joined at the centromere."),
        ("Centromere", "The region joining two sister chromatids; attachment point for spindle fibers."),
    ],
    "u9_l9.2": [
        ("Mitosis", "Division of the nucleus into two genetically identical daughter nuclei."),
        ("Prophase", "Chromosomes condense; spindle fibers form; nuclear envelope begins to break down."),
        ("Metaphase", "Chromosomes align at the cell's equator (metaphase plate)."),
        ("Anaphase", "Sister chromatids separate and move to opposite poles."),
        ("Cytokinesis", "Division of the cytoplasm; cleavage furrow in animals, cell plate in plants."),
    ],
    "u9_l9.3": [
        ("Meiosis", "A type of cell division that produces four haploid gametes from one diploid cell."),
        ("Crossing Over", "Exchange of genetic material between homologous chromosomes during meiosis I."),
        ("Independent Assortment", "Random orientation of homologous pairs during meiosis I increases genetic variation."),
        ("Haploid (n)", "A cell with one set of chromosomes (gametes in humans: n = 23)."),
        ("Diploid (2n)", "A cell with two sets of chromosomes (somatic cells in humans: 2n = 46)."),
    ],
    "u9_l9.4": [
        ("Tumor Suppressor Gene", "A gene that slows cell division or triggers apoptosis (e.g., p53)."),
        ("Oncogene", "A mutated gene that promotes uncontrolled cell growth."),
        ("Apoptosis", "Programmed cell death — a normal process to remove damaged or unneeded cells."),
        ("Benign Tumor", "An abnormal mass that is non-cancerous and does not spread."),
        ("Malignant Tumor", "A cancerous mass that can invade surrounding tissue and metastasize."),
    ],
    "u9_l9.5": [
        ("Stem Cell", "An undifferentiated cell capable of dividing and developing into specialized cell types."),
        ("Embryonic Stem Cell", "Pluripotent stem cells from early embryos that can become almost any cell type."),
        ("Adult Stem Cell", "Multipotent stem cells found in tissues like bone marrow; more limited differentiation."),
        ("Regenerative Medicine", "Using stem cells to repair or replace damaged tissues and organs."),
        ("Differentiation", "The process by which a cell becomes specialized for a specific function."),
    ],

    # ── Unit 10: Genetics ─────────────────────────────────────────
    "u10_l10.1": [
        ("Allele", "An alternative form of a gene (e.g., B for brown, b for blue)."),
        ("Dominant", "An allele that masks the effect of a recessive allele in a heterozygote."),
        ("Recessive", "An allele that is only expressed when homozygous (bb)."),
        ("Genotype", "An organism's genetic makeup (e.g., BB, Bb, bb)."),
        ("Phenotype", "An organism's observable traits resulting from its genotype and environment."),
    ],
    "u10_l10.2": [
        ("Incomplete Dominance", "The heterozygote shows an intermediate phenotype (e.g., red × white = pink)."),
        ("Codominance", "Both alleles are fully expressed in the heterozygote (e.g., AB blood type)."),
        ("Polygenic Inheritance", "A trait controlled by multiple genes (e.g., skin color, height)."),
        ("Epistasis", "One gene affects the expression of another gene."),
        ("Pleiotropy", "One gene influences multiple traits (e.g., sickle cell allele affects blood, organs)."),
    ],
    "u10_l10.3": [
        ("DNA Replication", "The process of copying DNA before cell division; semi-conservative."),
        ("Transcription", "DNA → mRNA; occurs in the nucleus."),
        ("Translation", "mRNA → protein; occurs at ribosomes."),
        ("Codon", "A three-nucleotide sequence in mRNA that codes for a specific amino acid."),
        ("Central Dogma", "DNA → RNA → Protein; the flow of genetic information."),
    ],
    "u10_l10.4": [
        ("Gene Regulation", "Mechanisms controlling when, where, and how much a gene is expressed."),
        ("Operon", "A group of genes transcribed together and regulated as a unit (e.g., lac operon)."),
        ("Promoter", "A DNA region where RNA polymerase binds to initiate transcription."),
        ("Epigenetics", "Heritable changes in gene expression not caused by changes in DNA sequence."),
        ("Transcription Factor", "A protein that binds DNA to help regulate gene expression."),
    ],
    "u10_l10.5": [
        ("CRISPR-Cas9", "A gene-editing tool that can precisely cut and modify specific DNA sequences."),
        ("GMO", "Genetically Modified Organism — an organism whose DNA has been altered in a lab."),
        ("Cloning", "Producing a genetically identical copy of an organism."),
        ("PCR", "Polymerase Chain Reaction — a technique to amplify specific DNA segments."),
        ("Gel Electrophoresis", "A technique that separates DNA fragments by size using an electric field."),
    ],
    "u10_l10.6": [
        ("Karyotype", "An image of an individual's chromosomes arranged by size and position of centromere."),
        ("Pedigree", "A chart showing the inheritance of a trait through generations of a family."),
        ("Autosomal Dominant", "A genetic disorder caused by one copy of a dominant allele on an autosome."),
        ("X-linked Recessive", "A disorder caused by a recessive allele on the X chromosome (more common in males)."),
        ("Genetic Counseling", "Professional guidance for individuals/families about inherited conditions and risks."),
    ],

    # ── Unit 11: Human Body Systems ────────────────────────────────
    "u11_l11.1": [
        ("Tissue", "A group of similar cells that perform a specific function (epithelial, connective, muscle, nervous)."),
        ("Organ", "A structure composed of two or more tissue types that performs a specific function."),
        ("Organ System", "A group of organs working together (e.g., circulatory, respiratory)."),
        ("Epithelial Tissue", "Covers body surfaces and lines cavities; protective, absorptive, secretory."),
        ("Connective Tissue", "Supports and binds other tissues (bone, blood, cartilage, fat)."),
    ],
    "u11_l11.2": [
        ("Heart", "A muscular organ that pumps blood through the circulatory system; 4 chambers."),
        ("Artery", "A blood vessel that carries blood away from the heart (usually oxygenated)."),
        ("Vein", "A blood vessel that carries blood toward the heart (usually deoxygenated)."),
        ("Capillary", "The smallest blood vessel where gas and nutrient exchange occurs."),
        ("Red Blood Cell", "An oxygen-carrying cell containing hemoglobin; has no nucleus in mammals."),
    ],
    "u11_l11.3": [
        ("Lungs", "The primary organs of respiration where gas exchange occurs."),
        ("Alveoli", "Tiny air sacs in the lungs where O₂ and CO₂ are exchanged with the blood."),
        ("Diaphragm", "A dome-shaped muscle below the lungs that contracts to enable inhalation."),
        ("Trachea", "The windpipe; conducts air from the larynx to the bronchi."),
        ("Bronchi", "Two large airways branching from the trachea into each lung."),
    ],
    "u11_l11.4": [
        ("Esophagus", "A muscular tube that moves food from the pharynx to the stomach via peristalsis."),
        ("Stomach", "An organ that churns food and secretes acid and enzymes for chemical digestion."),
        ("Small Intestine", "The primary site of nutrient absorption; lined with villi and microvilli."),
        ("Large Intestine", "Absorbs water and forms feces; contains beneficial bacteria."),
        ("Liver", "Produces bile, detoxifies blood, and stores glycogen."),
    ],
    "u11_l11.5": [
        ("Neuron", "A nerve cell that transmits electrical impulses; consists of dendrites, cell body, and axon."),
        ("Synapse", "The junction between two neurons where neurotransmitters transmit signals."),
        ("Central Nervous System", "The brain and spinal cord; processes and coordinates information."),
        ("Peripheral Nervous System", "All nerves outside the CNS; connects the body to the brain and spinal cord."),
        ("Reflex Arc", "A rapid, automatic response pathway: receptor → sensory neuron → CNS → motor neuron → effector."),
    ],
    "u11_l11.6": [
        ("Hormone", "A chemical messenger produced by endocrine glands, transported in blood to target cells."),
        ("Pituitary Gland", "The 'master gland' that controls other endocrine glands; located at the base of the brain."),
        ("Thyroid Gland", "Produces hormones (T3, T4) that regulate metabolism."),
        ("Insulin", "A hormone produced by the pancreas that lowers blood glucose levels."),
        ("Adrenal Glands", "Produce adrenaline (fight-or-flight) and cortisol (stress response)."),
    ],
    "u11_l11.7": [
        ("Immune System", "The body's defense against pathogens (bacteria, viruses, fungi, parasites)."),
        ("Innate Immunity", "Non-specific defenses present from birth (skin, mucus, phagocytes, inflammation)."),
        ("Adaptive Immunity", "Specific defense; B cells produce antibodies, T cells destroy infected cells."),
        ("Antibody", "A Y-shaped protein produced by B cells that binds to and neutralizes a specific antigen."),
        ("Vaccine", "A preparation that stimulates the immune system to provide protection against a disease."),
    ],
    "u11_l11.8": [
        ("Gamete", "A reproductive cell (sperm or egg) with a haploid number of chromosomes."),
        ("Fertilization", "The fusion of sperm and egg to form a diploid zygote."),
        ("Ovary", "Female reproductive organ that produces eggs and estrogen/progesterone."),
        ("Testis", "Male reproductive organ that produces sperm and testosterone."),
        ("Zygote", "A fertilized egg; the first cell of a new organism."),
    ],
    "u11_l11.9": [
        ("Homeostasis", "Maintaining a stable internal environment (temperature, pH, glucose, water balance)."),
        ("Negative Feedback", "A response that reduces the original stimulus, maintaining homeostasis (e.g., thermoregulation)."),
        ("Positive Feedback", "A response that amplifies the stimulus (e.g., blood clotting, childbirth contractions)."),
        ("Thermoregulation", "Maintaining body temperature through sweating, shivering, and blood flow changes."),
        ("Set Point", "The normal target value for a physiological variable (e.g., body temp ≈ 37°C)."),
    ],

    # ── Unit 12: Biotechnology & Frontiers ─────────────────────────
    "u12_l12.1": [
        ("Biotechnology", "The use of living systems and organisms to develop useful products."),
        ("Recombinant DNA", "DNA created by combining genetic material from multiple sources."),
        ("Gene Therapy", "Treating disease by inserting, altering, or replacing genes within a patient's cells."),
        ("Transgenic Organism", "An organism containing genes from another species."),
        ("Bioinformatics", "Using computers to analyze biological data, especially DNA sequences."),
    ],
    "u12_l12.2": [
        ("Bioethics", "The study of ethical issues arising from advances in biology and medicine."),
        ("Informed Consent", "A patient's voluntary agreement to a procedure after being fully informed of risks."),
        ("Genetic Privacy", "The right to keep one's genetic information confidential."),
        ("Cloning Debate", "Ethical questions around reproductive and therapeutic cloning of organisms."),
        ("Stem Cell Ethics", "Controversy over using embryonic stem cells, which requires destroying embryos."),
    ],
    "u12_l12.3": [
        ("Antibiotic", "A substance that kills or inhibits bacteria; resistance is a growing concern."),
        ("Vaccine", "A biological preparation providing immunity against a specific disease."),
        ("Pharmacogenomics", "Tailoring drug treatments based on an individual's genetic profile."),
        ("Clinical Trial", "A research study testing new medical treatments on human volunteers."),
        ("Antimicrobial Resistance", "The ability of microorganisms to resist drugs that once killed them."),
    ],
    "u12_l12.4": [
        ("Bioremediation", "Using organisms to clean up environmental pollutants."),
        ("Eutrophication", "Excess nutrients (N, P) in water causing algal blooms and oxygen depletion."),
        ("Biological Indicator", "An organism whose health reflects the condition of its ecosystem."),
        ("Carbon Sequestration", "Capturing and storing atmospheric CO₂ to mitigate climate change."),
        ("Biomagnification", "Increasing concentration of toxins at higher trophic levels."),
    ],
    "u12_l12.5": [
        ("Astrobiology", "The study of the origin, evolution, and potential for life in the universe."),
        ("Extremophile", "An organism thriving in extreme conditions (heat, acid, pressure, radiation)."),
        ("Habitable Zone", "The region around a star where liquid water could exist on a planet's surface."),
        ("Panspermia", "The hypothesis that life exists throughout the universe, distributed by meteoroids and dust."),
        ("Biosignature", "Any substance or phenomenon that provides evidence of past or present life."),
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

print(f"✅ Added flashcards to {count} Biology lessons")
