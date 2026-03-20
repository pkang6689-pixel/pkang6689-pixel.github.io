#!/usr/bin/env python3
"""Add 13 quiz questions to Biology lessons (→20 each). Units 1-4."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "biology_lessons.json")

def mq(qt, opts, exp):
    options = []
    for o in opts:
        c = o.startswith("*")
        options.append({"text": o.lstrip("*"), "is_correct": c, "data_i18n": None})
    return {"question_number": 0, "question_text": qt, "attempted": 2,
            "data_i18n": None, "options": options, "explanation": exp}

EXTRA = {}

# ── U1 L1.1 What is Biology? ──
EXTRA["u1_l1.1"] = [
    ("Biology is the study of:",["Rocks","Weather","*Living things","Stars"],"Bio = life, logos = study."),
    ("Which is a living organism?",["Rock","Water","*Mushroom","Ice"],"Fungi are living."),
    ("All living things are made of:",["Minerals","*Cells","Rocks","Air"],"Cell theory."),
    ("Living things need _____ to survive.",["Only water","Only sunlight","*Energy","Nothing"],"Energy requirement."),
    ("Which is NOT a characteristic of life?",["Growth","Reproduction","*Magnetism","Response to stimuli"],"Magnets are nonliving."),
    ("Living things maintain stable internal conditions through:",["Entropy","*Homeostasis","Osmosis only","Diffusion only"],"Internal balance."),
    ("The smallest unit of life is the:",["Organ","Tissue","*Cell","Atom"],"Cell = basic unit."),
    ("Biology includes the study of:",["Only animals","Only plants","*All living things (animals, plants, microbes, etc.)","Only humans"],"Broad scope."),
    ("Which process is unique to living things?",["Rusting","Erosion","*Metabolism","Evaporation"],"Chemical reactions in life."),
    ("DNA is important because it:",["Makes rocks","Creates weather","*Carries genetic information","Produces light"],"Hereditary material."),
    ("Organisms grow by:",["Absorbing minerals","*Increasing cell number and/or cell size","Evaporating","Crystallizing"],"Growth mechanisms."),
    ("An organism that can make its own food is called a(n):",["Heterotroph","Consumer","*Autotroph","Decomposer"],"Self-feeder."),
    ("Evolution is the change in _____ over time.",["Weather","Rocks","*Populations of organisms","Soil only"],"Biological evolution."),
]

# ── U1 L1.2 Scientific Method ──
EXTRA["u1_l1.2"] = [
    ("A hypothesis is a:",["Proven fact","*Testable prediction or explanation","Random guess","Law"],"Testable statement."),
    ("The independent variable is the one the scientist:",["Measures","Ignores","*Changes (manipulates)","Keeps the same"],"Manipulated variable."),
    ("The dependent variable is the one that is:",["Changed by the scientist","Kept constant","*Measured/observed (responds to the independent variable)","Eliminated"],"Response variable."),
    ("A control group is used to:",["Speed up the experiment","*Provide a baseline for comparison","Prove the hypothesis","Skip steps"],"Comparison standard."),
    ("Which is the correct order?",["Hypothesis → Observation → Experiment","*Observation → Question → Hypothesis → Experiment → Conclusion","Conclusion → Hypothesis → Experiment","Experiment → Observation → Question"],"Scientific method steps."),
    ("Repeating an experiment is called:",["Guessing","Hypothesizing","*Replication","Concluding"],"Reproducibility."),
    ("Data collected as numbers is called:",["Qualitative","Subjective","*Quantitative","Theoretical"],"Numerical data."),
    ("Data collected as descriptions is called:",["Quantitative","*Qualitative","Statistical","Numerical"],"Descriptive data."),
    ("A theory is a well-supported _____ that explains many observations.",["Guess","Fact","*Explanation","Question"],"Broad explanation."),
    ("A scientific law describes _____ but does not explain _____.",["Why, what","*What happens (pattern), why it happens","How, when","Nothing, everything"],"Law vs. theory."),
    ("Peer review means other scientists _____ the work.",["Ignore","Copy","*Evaluate and critique","Approve without reading"],"Quality check."),
    ("A good experiment tests only _____ variable at a time.",["Two","Zero","*One","All"],"Controlled experiment."),
    ("An unbiased experiment avoids:",["Data","Observations","*Personal opinions or expectations influencing results","Measurement"],"Objectivity."),
]

# ── U1 L1.3 Nature of Science ──
EXTRA["u1_l1.3"] = [
    ("Science is based on:",["Opinions","Beliefs","*Evidence and observation","Tradition"],"Empirical."),
    ("Scientific knowledge is:",["Permanent and unchangeable","*Tentative and subject to revision with new evidence","Based on authority","Random"],"Can be updated."),
    ("A model in science is:",["An exact copy","*A representation of a complex concept or process","A law","An opinion"],"Simplified representation."),
    ("Which is an example of a scientific model?",["A textbook","*A diagram of the solar system","A hypothesis","An opinion piece"],"Visual representation."),
    ("Science cannot answer questions about:",["How cells divide","What causes diseases","*Value judgments and moral questions","How evolution works"],"Outside science scope."),
    ("Empirical evidence comes from:",["Imagination","Faith","*Observation and experimentation","Authority"],"Direct evidence."),
    ("Technology and science are related because technology:",["Replaces science","Is unrelated","*Applies scientific knowledge to solve problems","Opposes science"],"Applied science."),
    ("A well-designed experiment must be:",["Expensive","*Reproducible and controlled","Fast","Done once only"],"Key criteria."),
    ("Scientific conclusions must be supported by:",["Popular vote","*Data and evidence","Tradition","Feelings"],"Evidence-based."),
    ("Pseudoscience differs from science because it:",["Uses experiments","Is peer-reviewed","*Lacks rigorous testing and evidence","Publishes results"],"Not science."),
    ("Scientific literacy means:",["Memorizing facts","Being a scientist","*Understanding scientific concepts and processes enough to make informed decisions","Reading textbooks"],"Public understanding."),
    ("Ethics in science involves:",["Ignoring rules","*Conducting research honestly and responsibly","Falsifying data","Skipping peer review"],"Research integrity."),
    ("An inference is:",["A direct observation","*A conclusion based on observations and reasoning","A random guess","A measurement"],"Logical deduction."),
]

# ── U1 L1.4 Characteristics of Life ──
EXTRA["u1_l1.4"] = [
    ("All living things are composed of one or more:",["Rocks","Atoms only","*Cells","Molecules only"],"Cell-based."),
    ("Maintaining a stable internal environment is called:",["Adaptation","*Homeostasis","Evolution","Metabolism"],"Internal balance."),
    ("The ability to produce offspring is:",["Growth","*Reproduction","Homeostasis","Metabolism"],"Creating new organisms."),
    ("Organisms respond to changes in their environment called:",["Adaptations","Mutations","*Stimuli","Genes"],"Environmental changes."),
    ("All the chemical reactions in an organism make up its:",["DNA","*Metabolism","Homeostasis","Reproduction"],"Chemical processes."),
    ("Growth and development follow instructions in an organism's:",["Environment","*DNA (genetic code)","Food","Water"],"Genetic blueprint."),
    ("Living things can _____ to their environment over generations.",["Not change","*Adapt (through evolution)","Only shrink","Only grow"],"Evolutionary adaptation."),
    ("Which is NOT needed by all living things?",["Energy","Water","*Sunlight (some organisms use chemical energy)","Nutrients"],"Chemotrophs exist."),
    ("Unicellular organisms are made of:",["Many cells","*One cell","No cells","Half a cell"],"Single-celled."),
    ("Multicellular organisms have:",["One cell","*Many cells working together","No cells","Only muscle cells"],"Many cells."),
    ("A virus is generally NOT considered living because it:",["Has DNA","Is small","*Cannot reproduce on its own (needs a host cell)","Moves"],"Lacks independent reproduction."),
    ("Asexual reproduction involves _____ parent(s).",["Two","*One","Three","Zero"],"Single parent."),
    ("Sexual reproduction involves _____ parent(s).",["One","*Two","Three","Zero"],"Two parents."),
]

# ── U1 L1.5 Levels of Organization ──
EXTRA["u1_l1.5"] = [
    ("From smallest to largest: cell → tissue → _____ → organ system → organism.",["Cell","Tissue","*Organ","Population"],"Organ level."),
    ("A group of similar cells working together forms a:",["Organ","*Tissue","Organism","System"],"Tissue definition."),
    ("A group of tissues working together forms a(n):",["Cell","Tissue","*Organ","Community"],"Organ definition."),
    ("The heart is an example of a(n):",["Cell","Tissue","*Organ","Organism"],"Organ."),
    ("An organ system is a group of _____ that work together.",["Cells","Tissues","*Organs","Organisms"],"System of organs."),
    ("All the organisms of one species in an area form a:",["Community","Ecosystem","*Population","Biome"],"Same species."),
    ("All the populations in an area form a:",["Population","Ecosystem","*Community","Biome"],"Multiple species."),
    ("A community plus its nonliving environment is a(n):",["Population","Community","*Ecosystem","Cell"],"Living + nonliving."),
    ("The biosphere includes:",["Only oceans","Only land","*All parts of Earth where life exists","Only the atmosphere"],"All life zones."),
    ("Which is the correct order from smallest to largest?",["Organ → Tissue → Cell","*Cell → Tissue → Organ → Organ System","Organism → Cell → Tissue","Organ System → Organ → Cell"],"Correct hierarchy."),
    ("Muscle tissue is found in which organ?",["Bone","Skin","*Heart","Hair"],"Cardiac muscle."),
    ("A biome is a large area characterized by its:",["Population","*Climate and dominant vegetation","Single species","Water only"],"Regional ecosystem type."),
    ("Individual → Population → Community → Ecosystem → _____ → Biosphere.",["Organism","*Biome","Cell","Tissue"],"Biome level."),
]

# ── U1 L1.6 Branches of Biology ──
EXTRA["u1_l1.6"] = [
    ("Botany is the study of:",["Animals","Fungi","*Plants","Bacteria"],"Plant science."),
    ("Zoology is the study of:",["Plants","*Animals","Fungi","Rocks"],"Animal science."),
    ("Microbiology studies:",["Large organisms","*Microorganisms (bacteria, viruses, etc.)","Plants","Rocks"],"Tiny organisms."),
    ("Ecology studies the interactions between organisms and their:",["DNA","Cells","*Environment","Genes"],"Organism-environment."),
    ("Genetics is the study of:",["Ecology","*Heredity and variation","Anatomy","Weather"],"Inheritance."),
    ("Anatomy studies the _____ of organisms.",["Function","Genes","*Structure","Ecology"],"Body structure."),
    ("Physiology studies the _____ of organisms.",["Structure","Genes","*Function (how body parts work)","Ecology"],"How things work."),
    ("Marine biology focuses on:",["Freshwater only","Land animals","*Ocean life","Desert life"],"Ocean organisms."),
    ("Paleontology studies:",["Living organisms","*Fossils and ancient life","Modern genetics","Chemistry"],"Ancient life."),
    ("Biochemistry studies the _____ of living things.",["Behavior","*Chemistry (chemical processes)","Movement","Ecology"],"Chemical basis of life."),
    ("Taxonomy is the science of:",["Anatomy","*Classification and naming of organisms","Genetics","Ecology"],"Naming & classifying."),
    ("Evolutionary biology studies how species _____ over time.",["Stay the same","*Change","Disappear only","Appear instantly"],"Change over time."),
    ("Biotechnology applies biology to develop:",["Theories only","*Products and technologies (medicines, GMOs, etc.)","Fossils","Taxonomy"],"Applied biology."),
]

# ── U1 L1.7 Careers in Biology ──
EXTRA["u1_l1.7"] = [
    ("A doctor practices:",["Botany","Ecology","*Medicine (applies biological knowledge to human health)","Geology"],"Medical career."),
    ("A veterinarian treats:",["Plants","*Animals","Rocks","Computers"],"Animal medicine."),
    ("A forensic scientist may use biology to:",["Cook food","*Solve crimes (DNA analysis, toxicology)","Build buildings","Design cars"],"Crime science."),
    ("An ecologist studies:",["Cells","*Ecosystems and organism interactions","Surgery","Pharmacy"],"Environmental science."),
    ("A pharmacist works with:",["Construction","*Medications (drugs)","Architecture","Astronomy"],"Drug dispensing."),
    ("A genetic counselor helps people understand:",["Weather","*Their genetic information and risks","Computers","Finance"],"Genetics career."),
    ("A marine biologist studies life in:",["Deserts","Forests","*Oceans and other marine environments","Mountains"],"Ocean life career."),
    ("A microbiologist studies:",["Large animals","*Bacteria, viruses, and other microorganisms","Plants only","Rocks"],"Microbiology career."),
    ("Biomedical engineering combines biology with:",["Art","History","*Engineering to design medical devices","Literature"],"Medical technology."),
    ("An epidemiologist studies the spread of:",["Rumors","*Diseases in populations","Stories","Music"],"Disease patterns."),
    ("A conservation biologist works to:",["Destroy habitats","*Protect endangered species and ecosystems","Build cities","Mine resources"],"Conservation career."),
    ("A nutritionist applies biology to:",["Mechanics","*Diet and health","Astronomy","Geology"],"Food and health."),
    ("A lab technician in biology:",["Teaches only","*Performs tests and analyzes biological samples","Does surgery","Designs buildings"],"Lab work."),
]

# ── U2 L2.1 Symbiosis & Biotic Interactions ──
EXTRA["u2_l2.1"] = [
    ("Mutualism is a relationship where:",["One benefits, one is harmed","*Both species benefit","Neither benefits","One benefits, other unaffected"],"Both gain."),
    ("Parasitism is a relationship where:",["Both benefit","*One benefits (parasite) and the other is harmed (host)","Neither benefits","Both are harmed"],"Parasite harms host."),
    ("Commensalism is a relationship where:",["Both benefit","Both are harmed","*One benefits and the other is neither helped nor harmed","One is harmed"],"One gains, other neutral."),
    ("A tick feeding on a dog is an example of:",["Mutualism","Commensalism","*Parasitism","Competition"],"Tick harms dog."),
    ("Bees pollinating flowers while collecting nectar is an example of:",["Parasitism","*Mutualism","Commensalism","Predation"],"Both benefit."),
    ("A remora fish riding on a shark is an example of:",["Parasitism","Mutualism","*Commensalism","Predation"],"Remora benefits; shark not affected."),
    ("Competition occurs when organisms:",["Help each other","*Compete for the same limited resources","Ignore each other","Decompose together"],"Same resource needs."),
    ("Predation involves a _____ catching and eating _____.",["Prey, predator","*Predator, prey","Host, parasite","Mutualist, commensalist"],"Hunter and hunted."),
    ("Mycorrhizae (fungi on plant roots) is an example of:",["Parasitism","*Mutualism (fungi get food, plant gets minerals)","Commensalism","Competition"],"Both benefit."),
    ("An organism that lives on or in another organism and harms it is a:",["Mutualist","Commensalist","*Parasite","Predator"],"Lives on host."),
    ("Interspecific competition is between:",["Members of the same species","*Members of different species","Only plants","Only animals"],"Between species."),
    ("Intraspecific competition is between:",["Different species","Plants and animals","*Members of the same species","Predator and prey"],"Within species."),
    ("Coevolution occurs when two species evolve _____ in response to each other.",["Independently","*Together (reciprocally)","Apart","Randomly"],"Mutual evolution."),
]

# ── U2 L2.2 Energy Flow in Ecosystems ──
EXTRA["u2_l2.2"] = [
    ("About what percentage of energy transfers between trophic levels?",["50%","25%","*10%","1%"],"10% rule."),
    ("A food chain shows:",["Random connections","*A single pathway of energy flow from producer to consumers","All feeding relationships","Only decomposers"],"Linear energy path."),
    ("A food web shows:",["One food chain","*Multiple interconnected food chains","Only producers","Only consumers"],"Complex feeding relationships."),
    ("Producers (autotrophs) get energy from:",["Other organisms","*Sunlight or chemical reactions (photosynthesis or chemosynthesis)","Consumers","Decomposers"],"Self-feeding."),
    ("Primary consumers eat:",["Other consumers","*Producers (plants/algae)","Decomposers","Nothing"],"Herbivores."),
    ("Secondary consumers eat:",["Producers","*Primary consumers","Tertiary consumers","Only plants"],"Eat herbivores."),
    ("Decomposers break down:",["Living organisms","*Dead organisms and waste (returning nutrients to soil)","Only rocks","Only water"],"Nutrient recycling."),
    ("An energy pyramid shows that energy _____ at each higher trophic level.",["Increases","*Decreases","Stays the same","Doubles"],"Energy loss as heat."),
    ("Most energy at each level is lost as:",["Food","Growth","*Heat (from cellular respiration)","Light"],"Metabolic heat."),
    ("The base of an energy pyramid is occupied by:",["Top predators","Secondary consumers","*Producers","Decomposers"],"Foundation level."),
    ("Trophic levels describe an organism's _____ in a food chain.",["Home","*Position (feeding level)","Size","Age"],"Feeding position."),
    ("Which has the MOST energy in an ecosystem?",["Top predators","Secondary consumers","*Producers","Tertiary consumers"],"Base has most."),
    ("Biomagnification means toxins _____ at higher trophic levels.",["Decrease","Stay the same","*Increase (concentrate)","Disappear"],"Toxin accumulation."),
]

# ── U2 L2.3 Matter Cycling ──
EXTRA["u2_l2.3"] = [
    ("Unlike energy, matter in ecosystems is:",["Lost","Used up","*Recycled (cycles through the ecosystem)","Created"],"Matter cycles."),
    ("The water cycle includes evaporation, condensation, and:",["Photosynthesis","*Precipitation","Decomposition","Mutation"],"Water cycle steps."),
    ("In the carbon cycle, plants absorb CO₂ through:",["Respiration","*Photosynthesis","Decomposition","Combustion"],"Carbon fixation."),
    ("Animals return carbon to the atmosphere through:",["Photosynthesis","*Cellular respiration (exhaling CO₂)","Nitrogen fixation","Condensation"],"Breathing."),
    ("Nitrogen fixation converts N₂ gas into forms usable by:",["Animals directly","*Plants (ammonia/nitrates in soil)","Rocks","Water"],"Bacteria fix nitrogen."),
    ("Which organisms perform nitrogen fixation?",["Plants","Animals","*Certain bacteria (e.g., Rhizobium)","Fungi"],"Bacterial process."),
    ("The phosphorus cycle does NOT have a significant:",["Soil phase","Water phase","*Atmospheric (gas) phase","Rock phase"],"No common gas form."),
    ("Decomposers are essential to nutrient cycles because they:",["Produce oxygen","*Break down dead matter and release nutrients back into the soil","Create energy","Fix nitrogen"],"Nutrient release."),
    ("Fossil fuels store carbon from:",["The atmosphere currently","*Ancient organisms (millions of years ago)","New plants","Ocean water"],"Ancient carbon."),
    ("Burning fossil fuels adds _____ to the atmosphere.",["Oxygen","Nitrogen","*Carbon dioxide (CO₂)","Water only"],"Combustion releases CO₂."),
    ("Transpiration is water loss from:",["Animals","Rocks","*Plants (through leaf stomata)","Soil only"],"Plant water release."),
    ("Denitrification converts nitrates back into:",["Ammonia","Plant-usable nitrogen","*Nitrogen gas (N₂) returned to the atmosphere","Phosphorus"],"Completes nitrogen cycle."),
    ("The oxygen cycle is closely linked to:",["The rock cycle","*The carbon cycle (photosynthesis produces O₂, respiration uses O₂)","The phosphorus cycle","Erosion"],"Carbon-oxygen link."),
]

# ── U2 L2.4 Ecological Succession ──
EXTRA["u2_l2.4"] = [
    ("Ecological succession is the gradual change in a _____ over time.",["Species","Population","*Community (species composition)","Gene"],"Community change."),
    ("Primary succession occurs on:",["Existing soil","Farmland","*Bare surfaces with NO soil (new lava, exposed rock)","Cleared forest"],"No soil."),
    ("Secondary succession occurs on:",["Bare rock","*Disturbed land that still has soil (after fire, flood)","The moon","New volcanic islands"],"Soil present."),
    ("Pioneer species in primary succession are often:",["Trees","Large mammals","*Lichens and mosses (first colonizers)","Fish"],"First colonizers."),
    ("A climax community is:",["The first stage","*The stable, mature community at the end of succession","A pioneer species","A disaster"],"Final stage."),
    ("Which event could start secondary succession?",["Volcanic eruption creating new land","Glacier retreat","*Forest fire (soil remains)","Formation of a new island"],"Disturbance with soil."),
    ("During succession, biodiversity generally:",["Decreases","Stays the same","*Increases (more species establish over time)","Fluctuates randomly"],"Increasing diversity."),
    ("Soil formation during primary succession is aided by:",["Animals only","*Pioneer species breaking down rock","Rain only","Wind only"],"Soil building."),
    ("Grasses and shrubs typically appear _____ trees in succession.",["After","At the same time as","*Before","Never"],"Early stages."),
    ("Succession after a volcanic eruption on bare lava is:",["Secondary","*Primary","Tertiary","No succession"],"No prior soil."),
    ("Which factor can restart succession?",["Photosynthesis","Migration","*Natural disasters (fire, hurricanes, floods)","Homeostasis"],"Disturbance."),
    ("Succession in a pond may eventually lead to a:",["Deeper pond","*Terrestrial (land) community","Ocean","Desert always"],"Pond filling in."),
    ("Humans can affect succession by:",["Not doing anything","Having no impact","*Activities like deforestation, farming, and development","Only planting trees"],"Anthropogenic impact."),
]

# ── U2 L2.5 Niches ──
EXTRA["u2_l2.5"] = [
    ("An organism's niche is its _____ in the ecosystem.",["Home","Location","*Role (job — what it eats, where it lives, how it interacts)","Name"],"Ecological role."),
    ("An organism's habitat is its:",["Niche","*Physical living place (where it lives)","Diet","Behavior"],"Where it lives."),
    ("Niche differs from habitat because niche includes:",["Only location","*Everything: diet, behavior, interactions, and requirements","Nothing","Size only"],"Comprehensive role."),
    ("The competitive exclusion principle states that two species cannot:",["Ever coexist","*Occupy the exact same niche in the same area indefinitely","Share any resources","Compete at all"],"Same niche = one wins."),
    ("Resource partitioning occurs when competing species:",["Fight to the death","*Divide resources to reduce competition (e.g., feed at different times or heights)","Share everything equally","Leave the habitat"],"Niche differentiation."),
    ("A generalist species:",["Uses very few resources","*Occupies a broad niche (eats many foods, tolerates varied conditions)","Lives in one place only","Is always rare"],"Broad niche."),
    ("A specialist species:",["Uses many resources","*Has a narrow niche (specific diet, habitat requirements)","Is found everywhere","Is always common"],"Narrow niche."),
    ("A realized niche is:",["The full potential niche","*The actual niche an organism occupies (limited by competition and other factors)","Hypothetical only","Always larger than fundamental"],"Actual vs. possible."),
    ("A fundamental niche is:",["The actual niche","*The full range of conditions an organism COULD occupy without competition","Always smaller than realized","An empty niche"],"Potential niche."),
    ("Keystone species have a _____ impact relative to their abundance.",["Small","No","*Disproportionately large","Equal"],"Large role, small numbers."),
    ("If a keystone species is removed, the community:",["Stays the same","*Changes significantly (structure collapses)","Improves always","Gains species"],"Major impact."),
    ("An example of niche partitioning is warblers feeding at different _____ in the same trees.",["Times","*Heights (different parts of the tree)","Temperatures","Colors"],"MacArthur's warblers."),
    ("Organisms with overlapping niches often experience:",["Mutualism","Parasitism","*Competition (for the same resources)","No interaction"],"Niche overlap = competition."),
]

# ── U2 L2.6 Trophic Structure ──
EXTRA["u2_l2.6"] = [
    ("Herbivores eat only:",["Meat","*Plants","Both plants and meat","Decomposing matter"],"Plant-eaters."),
    ("Carnivores eat:",["Plants only","*Other animals","Decomposing matter","Minerals"],"Meat-eaters."),
    ("Omnivores eat:",["Only plants","Only animals","*Both plants and animals","Only decomposing matter"],"Mixed diet."),
    ("Detritivores feed on:",["Living plants","Living animals","*Dead organic matter (detritus)","Rocks"],"Dead matter feeders."),
    ("Which trophic level has the MOST biomass in most ecosystems?",["Secondary consumers","*Producers","Tertiary consumers","Decomposers"],"Base of pyramid."),
    ("An apex predator is at the _____ of the food chain.",["Bottom","Middle","*Top","Outside"],"Top predator."),
    ("What happens if all producers in an ecosystem are removed?",["Nothing","Only herbivores die","*The entire food web collapses (no energy source)","Consumers adapt"],"Food web dependent on producers."),
    ("Scavengers eat:",["Living prey only","*Dead animals they did not kill (carrion)","Only plants","Only insects"],"Feed on carrion."),
    ("Vultures are an example of:",["Predators","Herbivores","*Scavengers","Autotrophs"],"Eat dead animals."),
    ("In a trophic cascade, changes at one level _____ throughout the food web.",["Stay contained","*Ripple (cascade effects up and down the food web)","Disappear","Have no effect"],"Cascading effects."),
    ("The reintroduction of wolves to Yellowstone is an example of a:",["Food chain","*Trophic cascade (wolves reduced elk, allowing vegetation to recover)","Mutualism","Parasitism"],"Cascade example."),
    ("Fungi are important decomposers that break down:",["Only animals","Only bacteria","*Dead plant and animal material","Rocks only"],"Fungal decomposition."),
    ("Bacteria decomposers help return _____ to the soil.",["Energy","Water","*Nutrients (nitrogen, phosphorus, etc.)","Oxygen only"],"Nutrient recycling."),
]

# ── U2 L2.7 Human Impacts on Ecosystems ──
EXTRA["u2_l2.7"] = [
    ("Deforestation leads to:",["More biodiversity","*Habitat loss, increased CO₂, and erosion","Cooler temperatures","More rainfall always"],"Forest destruction effects."),
    ("Pollution can include:",["Only air pollutants","*Air, water, and soil pollutants (chemicals, plastics, etc.)","Only noise","Only light"],"Multiple types."),
    ("The greenhouse effect is:",["Always harmful","*A natural process that warms Earth, but enhanced by human CO₂ emissions","Not real","Only from factories"],"Natural + enhanced."),
    ("Invasive species are organisms that:",["Always help ecosystems","*Are introduced to new areas and harm native species/ecosystems","Are always animals","Cannot survive in new habitats"],"Non-native harmful species."),
    ("Overfishing can lead to:",["Healthier oceans","*Collapse of fish populations and disrupted marine food webs","More fish","Cleaner water"],"Population collapse."),
    ("Urban sprawl affects ecosystems by:",["Increasing habitats","*Destroying natural habitats and fragmenting ecosystems","Having no impact","Increasing biodiversity"],"Habitat destruction."),
    ("Acid rain is caused primarily by:",["CO₂ only","*Sulfur dioxide (SO₂) and nitrogen oxides (NOₓ) from burning fossil fuels","Oxygen","Water vapor"],"Atmospheric pollution."),
    ("Ozone depletion is caused mainly by:",["CO₂","*Chlorofluorocarbons (CFCs)","Methane","Water"],"CFC damage."),
    ("Sustainable practices aim to:",["Use all resources immediately","*Meet present needs without compromising future generations' ability to meet theirs","Ignore environmental impact","Maximize profit only"],"Sustainability definition."),
    ("Recycling helps ecosystems by:",["Increasing pollution","*Reducing waste, conserving resources, and decreasing mining/extraction","Having no effect","Only saving money"],"Resource conservation."),
    ("Renewable energy sources include:",["Coal and oil","*Solar, wind, and hydroelectric (not depleted when used)","Nuclear only","Natural gas only"],"Clean energy."),
    ("Habitat fragmentation means:",["Habitats are connected","*Large habitats are broken into smaller, isolated pieces","Habitats are destroyed entirely","Habitats improve"],"Broken habitats."),
    ("Conservation efforts include protected areas such as:",["Shopping malls","*National parks, wildlife refuges, and marine sanctuaries","Factories","Airports"],"Protected lands."),
]

# ── U3 L3.1 Community Ecology ──
EXTRA["u3_l3.1"] = [
    ("A biological community consists of all the _____ living in one area.",["Organisms of one species","Abiotic factors","*Populations of different species interacting","Individuals of one species"],"Multiple species."),
    ("Species richness refers to the:",["Total number of individuals","*Number of different species in a community","Size of each population","Diversity index"],"Count of species."),
    ("Species evenness refers to:",["The total number of species","*How equally distributed individuals are among species","Species richness","Population size"],"Relative abundance."),
    ("High biodiversity generally makes a community more:",["Fragile","Simple","*Resilient (stable and resistant to disturbance)","Homogeneous"],"Stability."),
    ("Interspecific interactions include:",["Only competition","*Competition, predation, symbiosis, and commensalism","Only mutualism","Only parasitism"],"All interactions."),
    ("A dominant species is one that:",["Is rare","*Has the greatest biomass or abundance and major influence","Has no effect","Is always the smallest"],"Major influence."),
    ("Foundation species _____ the environment to benefit other species.",["Destroy","*Physically modify (e.g., corals build reefs, trees create canopy)","Heat","Pollute"],"Habitat engineers."),
    ("An ecological disturbance is:",["Normal stability","*An event that changes community structure (fire, flood, storm)","Evolution","Succession"],"Disruption."),
    ("Intermediate disturbance hypothesis states that _____ disturbance supports maximum diversity.",["No","Maximum","*Moderate (intermediate)","Constant"],"Balance between stability and disruption."),
    ("Trophic structure describes the _____ relationships in a community.",["Social","*Feeding (energy flow through producers, consumers, decomposers)","Spatial","Temporal"],"Food relationships."),
    ("Primary productivity is the rate at which _____ produce biomass.",["Consumers","Decomposers","*Producers (autotrophs)","Predators"],"Production rate."),
    ("Bottom-up control means the community is controlled by:",["Predators","*Nutrient availability and producer abundance","Top consumers","Temperature only"],"Resource-driven."),
    ("Top-down control means the community is controlled by:",["Producers","Decomposers","*Predators (consumers at higher trophic levels)","Soil only"],"Predator-driven."),
]

# ── U3 L3.2 Terrestrial Biomes ──
EXTRA["u3_l3.2"] = [
    ("Biomes are primarily determined by:",["Soil type only","Altitude only","*Climate (temperature and precipitation)","Longitude"],"Climate determines biome."),
    ("The tropical rainforest biome is characterized by:",["Cold temperatures","Low rainfall","*High temperature and heavy rainfall year-round","Dry conditions"],"Warm and wet."),
    ("Deserts receive less than _____ cm of rainfall per year.",["100","50","*25","10"],"Very dry."),
    ("Tundra is characterized by:",["Hot temperatures","*Permafrost and very cold temperatures","Heavy forests","High rainfall"],"Frozen ground."),
    ("The taiga (boreal forest) biome is dominated by:",["Deciduous trees","*Coniferous (evergreen needle-leaf) trees","Grasses","Cacti"],"Evergreens."),
    ("Temperate grasslands (prairies) receive:",["Very high rainfall","*Moderate rainfall (less than forests, more than deserts)","No rainfall","Only snow"],"Moderate precipitation."),
    ("Temperate deciduous forests have trees that:",["Keep leaves year-round","*Lose leaves in autumn (seasonal leaf drop)","Have needles","Are all cacti"],"Seasonal."),
    ("Savannas are tropical grasslands with:",["Dense forests","No trees","*Scattered trees","Snow cover"],"Grassland with trees."),
    ("Chaparral (Mediterranean) biomes have:",["Year-round rain","Very cold winters","*Hot, dry summers and mild, wet winters","Tropical conditions"],"Mediterranean climate."),
    ("Which biome has the highest biodiversity?",["Tundra","Desert","*Tropical rainforest","Taiga"],"Most diverse."),
    ("Permafrost is permanently frozen _____ found in tundra regions.",["Water","Rock","*Ground (soil)","Air"],"Frozen soil."),
    ("Altitude affects biomes similarly to:",["Longitude","*Latitude (higher altitude mimics higher latitude conditions)","Soil depth","Humidity only"],"Mountain zonation."),
    ("Biome boundaries are NOT always sharp because of:",["Exact lines","*Transitional zones (ecotones) between biomes","Walls","Fences"],"Gradual transitions."),
]

# ── U3 L3.3 Aquatic Ecosystems ──
EXTRA["u3_l3.3"] = [
    ("Freshwater ecosystems include:",["Only oceans","*Lakes, rivers, streams, and wetlands","Only coral reefs","Only deep sea"],"Freshwater types."),
    ("Marine (saltwater) ecosystems include:",["Lakes","Rivers","*Oceans, coral reefs, and estuaries","Ponds only"],"Ocean ecosystems."),
    ("Estuaries are areas where:",["Two oceans meet","*Freshwater and saltwater mix (river meets ocean)","Rain forms","Lakes drain"],"Mixing zones."),
    ("The photic zone is the part of the ocean that receives:",["No light","*Adequate sunlight for photosynthesis","Only moonlight","Only artificial light"],"Light zone."),
    ("The aphotic zone is:",["Well-lit","*Dark (no sunlight penetration)","Shallow","Warm"],"No light."),
    ("Coral reefs are built by:",["Fish","*Coral polyps (tiny animals that secrete calcium carbonate)","Algae alone","Sharks"],"Coral animals."),
    ("Wetlands are important because they:",["Are useless","*Filter water, prevent floods, and support biodiversity","Cause pollution","Only look nice"],"Ecosystem services."),
    ("The intertidal zone is the area:",["Deep in the ocean","*Between high and low tide marks (shore)","In the middle of the ocean","Underground"],"Tidal zone."),
    ("Kelp forests are found in:",["Freshwater","Deserts","*Cool, nutrient-rich coastal waters","Tropical rivers"],"Marine forests."),
    ("The open ocean (pelagic zone) is characterized by:",["Shallow water","*Vast, deep water far from shore","Coral reefs","Freshwater"],"Open water."),
    ("Hydrothermal vents support life through:",["Photosynthesis","*Chemosynthesis (bacteria use chemical energy)","Sunlight","Wind"],"Chemical energy source."),
    ("Salinity is the measure of _____ dissolved in water.",["Oxygen","Sugar","*Salt","Acid"],"Salt content."),
    ("Plankton are tiny organisms that form the base of _____ food webs.",["Terrestrial","*Aquatic (both freshwater and marine)","Desert","Forest"],"Aquatic base."),
]

# ── U3 L3.4 Climate Change & Ecosystem Shifts ──
EXTRA["u3_l3.4"] = [
    ("Climate change refers to long-term shifts in:",["Daily weather","*Global temperatures and weather patterns","Only wind","Seasons only"],"Long-term change."),
    ("The primary greenhouse gas from human activity is:",["Oxygen","*Carbon dioxide (CO₂)","Nitrogen","Argon"],"Main contributor."),
    ("Burning fossil fuels releases _____ that enhances the greenhouse effect.",["Oxygen","Water only","*CO₂ and other greenhouse gases","Nitrogen"],"Combustion emissions."),
    ("The greenhouse effect is:",["Entirely bad","*Natural and necessary, but human activities are enhancing it","Not real","Only from greenhouses"],"Natural process enhanced."),
    ("Rising global temperatures can cause:",["Thicker ice caps","*Melting ice, rising sea levels, and habitat changes","Cooler oceans","No effects"],"Temperature effects."),
    ("Ocean acidification is caused by oceans absorbing more:",["Oxygen","*CO₂ (forming carbonic acid, lowering pH)","Nitrogen","Salt"],"CO₂ absorption."),
    ("Climate change can shift biome boundaries toward the:",["Equator","Oceans","*Poles (warming pushes biomes poleward and upward)","Core of the Earth"],"Poleward shift."),
    ("Coral bleaching is caused by:",["Cold water","*Warmer water temperatures (corals expel symbiotic algae under heat stress)","Freshwater","Pollution only"],"Temperature stress."),
    ("Milankovitch cycles are natural climate variations caused by changes in Earth's:",["Magnetic field","*Orbit and tilt (orbital variations over thousands of years)","Atmosphere only","Core"],"Orbital cycles."),
    ("Deforestation contributes to climate change because trees that are cut no longer:",["Produce CO₂","*Absorb CO₂ (act as carbon sinks)","Release oxygen","Grow"],"Lost carbon sink."),
    ("Methane (CH₄) is a greenhouse gas released by:",["Only cars","*Livestock, wetlands, and fossil fuel extraction","Trees","Oceans only"],"Multiple sources."),
    ("Adaptation to climate change involves:",["Ignoring the problem","*Adjusting practices to cope with changes (levees, drought-resistant crops)","Stopping all activity","Only reducing emissions"],"Coping strategies."),
    ("Mitigation of climate change focuses on:",["Adapting to changes","*Reducing greenhouse gas emissions (preventing further change)","Doing nothing","Increasing emissions"],"Reducing the cause."),
]

# ── U3 L3.5 Symbiosis & Species Interactions (Advanced) ──
EXTRA["u3_l3.5"] = [
    ("Batesian mimicry is when a harmless species resembles a:",["Plant","*Harmful or toxic species (to deter predators)","Rock","Different habitat"],"False warning."),
    ("Müllerian mimicry is when two _____ species resemble each other.",["Harmless","*Harmful (both genuinely toxic/dangerous, reinforcing the warning)","Unrelated","Fossil"],"Shared warning."),
    ("Aposematic coloration is:",["Camouflage","*Bright warning coloration (signaling toxicity or danger)","Transparent coloring","No coloring"],"Warning colors."),
    ("Camouflage helps prey by:",["Attracting predators","*Blending with the environment (avoiding detection)","Standing out","Making noise"],"Hiding strategy."),
    ("Herbivory is an interaction between:",["Two animals","*A plant and an animal that eats it","Two fungi","A predator and prey animal"],"Plant-eater."),
    ("Plants defend against herbivory with:",["Speed","*Thorns, toxins, and tough structures","Camouflage","Migration"],"Chemical and physical defenses."),
    ("Obligate mutualism means the partners:",["Can survive alone","*Cannot survive without each other","Sometimes interact","Are competitors"],"Dependent partnership."),
    ("Facultative mutualism means the partners:",["Cannot survive alone","*Benefit from each other but can survive independently","Always compete","Are parasites"],"Optional benefit."),
    ("Cleaning symbiosis is when small organisms remove parasites from larger ones. This is:",["Parasitism","*Mutualism (cleaner gets food, host gets parasite removal)","Commensalism","Competition"],"Both benefit."),
    ("Brood parasitism (like cuckoo birds laying eggs in other nests) is a form of:",["Mutualism","*Parasitism","Commensalism","Decomposition"],"Exploiting host parents."),
    ("Social parasitism is one species exploiting the social behavior of another, as in:",["Bee pollination","*Slave-making ants raiding other ant colonies","Flower seed dispersal","Decomposition"],"Behavioral exploitation."),
    ("Facilitation is a positive interaction where one species _____ conditions for others.",["Worsens","*Improves (makes the environment more suitable)","Ignores","Destroys"],"Positive modification."),
    ("Allelopathy is when plants release chemicals that:",["Attract pollinators","*Inhibit the growth of nearby competing plants","Produce seeds","Fix nitrogen"],"Chemical competition."),
]

# ── U4 L4.1 Population Dynamics ──
EXTRA["u4_l4.1"] = [
    ("Population size is the total number of _____ in a population.",["Species","Communities","*Individuals","Ecosystems"],"Individual count."),
    ("Population density is the number of individuals per:",["Species","*Unit area (or volume)","Ecosystem","Biome"],"Individuals/area."),
    ("A population grows when:",["Death rate > birth rate","*Birth rate > death rate (and/or immigration > emigration)","They are equal","No births occur"],"Growth condition."),
    ("Exponential growth produces a _____ shaped curve.",["L","S","*J","U"],"Rapid increase."),
    ("Exponential growth occurs when resources are:",["Scarce","*Unlimited (no limiting factors)","Declining","Absent"],"No constraints."),
    ("Logistic growth produces a _____ shaped curve.",["J","*S (sigmoid)","L","U"],"Levels off."),
    ("In logistic growth, the population levels off at the:",["Minimum","*Carrying capacity (K)","Zero","Maximum growth rate"],"Environmental limit."),
    ("Carrying capacity (K) is the maximum population an environment can:",["Exceed","*Support sustainably (long-term)","Ignore","Eliminate"],"Sustainable maximum."),
    ("The growth rate slows as the population approaches:",["Zero","Birth rate","*Carrying capacity","Infinity"],"Resource limitation."),
    ("Natality refers to the _____ rate.",["Death","*Birth","Migration","Growth"],"Birth rate."),
    ("Mortality refers to the _____ rate.",["Birth","!Migration","*Death","Immigration"],"Death rate."),
    ("Immigration is the movement of individuals _____ a population.",["Out of","*Into","Away from","Between"],"Moving in."),
    ("Emigration is the movement of individuals _____ a population.",["Into","*Out of","Between","Within"],"Moving out."),
]

# ── U4 L4.2 Human Population Growth ──
EXTRA["u4_l4.2"] = [
    ("The current world population is approximately:",["3 billion","5 billion","*8 billion","12 billion"],"As of 2020s."),
    ("The human population grew most rapidly during the:",["Stone Age","Middle Ages","*20th century (due to medical advances and agriculture)","22nd century"],"Recent growth."),
    ("The demographic transition model shows populations moving from:",["Low birth/death to high","*High birth/death rates to low birth/death rates","No change","Random changes"],"Modernization effect."),
    ("A population pyramid shows the distribution of:",["Species richness","*Age and sex within a population","Income","Food resources"],"Age structure."),
    ("A rapidly growing population has a pyramid shape that is:",["Top-heavy","*Wide at the base (many young individuals)","Rectangular","Inverted"],"Many young."),
    ("A stable population has a pyramid that is approximately:",["Wide base","*Columnar (rectangular — similar numbers at each age)","Inverted","Triangular"],"Even ages."),
    ("A declining population has a pyramid that is:",["Wide at base","*Narrow at base (fewer young than old)","Square","Expanding"],"Few young."),
    ("Zero population growth occurs when birth rate equals:",["Immigration","*Death rate (population size stays constant)","Emigration","Growth rate"],"Birth = death."),
    ("Developed countries typically have _____ population growth rates.",["Very high","*Low (or even negative)","Moderate","Unpredictable"],"Low growth."),
    ("Developing countries typically have _____ population growth rates.",["Very low","Zero","*Higher (but often declining)","Negative"],"Higher growth."),
    ("The major factor reducing human death rates historically was:",["War","*Improved medicine, sanitation, and agriculture","Climate change","Predation"],"Health advances."),
    ("Doubling time is the time it takes a population to:",["Halve","*Double in size","Triple","Reach carrying capacity"],"Population doubling."),
    ("Family planning and education are ways to _____ population growth.",["Increase","*Slow (reduce birth rates through voluntary choices)","Have no effect on","Double"],"Growth management."),
]

# ── U4 L4.3 Carrying Capacity ──
EXTRA["u4_l4.3"] = [
    ("Limiting factors determine the _____ of a population.",["Growth rate only","Color","*Carrying capacity (maximum size an environment can sustain)","Location"],"Resource limits."),
    ("Density-dependent factors INCREASE in effect as population density:",["Decreases","Stays the same","*Increases (competition, disease, predation intensify)","Is eliminated"],"Affected by density."),
    ("Which is a density-dependent factor?",["Earthquake","*Competition for food","Volcanic eruption","Tornado"],"Increases with crowding."),
    ("Which is a density-independent factor?",["Disease","Competition","*Natural disaster (hurricane, flood, fire)","Parasitism"],"Affects all regardless of density."),
    ("Disease spreads more easily in _____ populations.",["Sparse","*Dense (crowded)","Small","Declining"],"Contact rate."),
    ("If a population exceeds carrying capacity, it will likely:",["Stay the same","Keep growing","*Decline (resources become insufficient, death rate increases)","Double"],"Overshoot and crash."),
    ("Carrying capacity can change over time due to:",["Nothing","*Environmental changes (climate, resource availability, human impact)","Only genetics","Evolution only"],"Dynamic K."),
    ("Food availability is a _____ limiting factor.",["Density-independent","*Density-dependent","Unrelated","Genetic"],"More organisms = less food each."),
    ("A drought reducing a population is an example of a _____ factor.",["Density-dependent","*Density-independent","Genetic","Behavioral"],"Affects all equally."),
    ("Intraspecific competition is competition _____ a species.",["Between","*Within (among members of the same species)","Outside of","Across"],"Same species competition."),
    ("Predation is a density-dependent factor because predators are attracted to _____ prey populations.",["Small","Declining","*Large (dense)","Absent"],"More prey = more predators."),
    ("Nesting sites and territory are examples of _____ resources that limit populations.",["Unlimited","Infinite","*Limited (finite)","Imaginary"],"Finite resources."),
    ("Overgrazing by herbivores reduces _____, which then limits the herbivore population.",["Predators","Water","*Vegetation (food supply)","Soil only"],"Food depletion."),
]

# ── U4 L4.4 Population Regulation ──
EXTRA["u4_l4.4"] = [
    ("r-selected species produce _____ offspring with _____ parental care.",["Few, much","*Many, little","Few, no","One, extensive"],"Quantity strategy."),
    ("K-selected species produce _____ offspring with _____ parental care.",["Many, little","*Few, much (extensive)","Many, much","None, no"],"Quality strategy."),
    ("Examples of r-selected species include:",["Elephants","Whales","*Insects, bacteria, and many fish (fast reproducers)","Humans"],"Fast reproducers."),
    ("Examples of K-selected species include:",["Mosquitoes","Bacteria","*Elephants, whales, and humans (slow reproducers)","Flies"],"Slow reproducers."),
    ("Territoriality regulates populations by:",["Increasing density","*Limiting access to resources (space, food, mates)","Increasing birth rates","Having no effect"],"Space defense."),
    ("Predator-prey cycles show _____ fluctuations.",["No","Random","*Regular oscillating (as prey increases, predators follow, then prey declines)","Constant"],"Boom-bust cycles."),
    ("When prey populations increase, predator populations typically:",["Decrease immediately","Stay the same","*Increase (after a lag — more food supports more predators)","Disappear"],"Lagging increase."),
    ("Density-dependent regulation tends to keep populations near:",["Zero","Maximum","*Carrying capacity (negative feedback)","Infinity"],"Equilibrium."),
    ("Negative feedback in population regulation means:",["Population always grows","*Growth rate decreases as population increases (self-regulating)","Population always shrinks","No regulation occurs"],"Self-correction."),
    ("Stress from overcrowding can reduce _____ in some species.",["Size","*Reproduction rates (behavioral/physiological stress response)","Lifespan always","Intelligence"],"Crowding stress."),
    ("Survivorship curves show the _____ rate of a cohort over time.",["Birth","*Survival (mortality pattern by age)","Migration","Growth"],"Age-specific survival."),
    ("Type I survivorship: most individuals survive to _____.",["Infancy","Youth","*Old age (low early mortality, high late mortality)","Birth only"],"Long-lived."),
    ("Type III survivorship: most mortality occurs:",["In old age","In middle age","*Early in life (many die young, few survive to adulthood)","Never"],"High juvenile mortality."),
]

# ── U4 L4.5 Conservation & Sustainable Development ──
EXTRA["u4_l4.5"] = [
    ("Conservation biology aims to:",["Exploit resources fully","*Protect and manage biodiversity and ecosystems","Ignore species loss","Only study fossils"],"Biodiversity protection."),
    ("Sustainable development meets present needs without:",["Any effort","*Compromising future generations' ability to meet their needs","Any cost","Economic growth"],"Future sustainability."),
    ("An endangered species is one that:",["Is extinct","*Is at risk of extinction","Is thriving","Has large populations"],"Extinction risk."),
    ("A threatened species is one that is likely to become:",["Extinct immediately","Common","*Endangered in the near future","A pest"],"Near-endangered."),
    ("Habitat destruction is the _____ cause of species extinction.",["Least important","Rarest","*Leading (most significant)","Only natural"],"Primary threat."),
    ("Protected areas like national parks help by:",["Removing all species","*Preserving natural habitats from development","Encouraging hunting","Mining resources"],"Habitat preservation."),
    ("Ex situ conservation means:",["Protecting in natural habitat","*Conserving species outside their natural habitat (zoos, botanical gardens, seed banks)","Ignoring the species","Hunting them"],"Off-site conservation."),
    ("In situ conservation means:",["Conservation in zoos","*Conservation in the organism's natural habitat","Lab conservation","Museum conservation"],"On-site conservation."),
    ("Ecotourism supports conservation by:",["Destroying habitats","*Generating income that funds habitat protection","Ignoring ecosystems","Promoting hunting"],"Sustainable tourism."),
    ("The Endangered Species Act (ESA) in the US:",["Allows unlimited hunting","*Provides legal protection for threatened and endangered species","Only applies to plants","Is voluntary"],"Legal protection."),
    ("Captive breeding programs aim to:",["Keep animals as pets","*Increase population numbers of endangered species for eventual release","Clone animals","Sell animals"],"Population recovery."),
    ("Wildlife corridors connect fragmented habitats to allow:",["Predation only","*Animal movement and gene flow between populations","Road building","Urban development"],"Habitat connectivity."),
    ("Reducing, reusing, and recycling supports sustainability by:",["Increasing waste","*Decreasing resource consumption and waste production","Having no impact","Creating pollution"],"3 R's."),
]

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for key, tuples in EXTRA.items():
    if key not in data:
        print(f"⚠️  {key} not found"); continue
    existing = data[key].get("quiz_questions", [])
    start = len(existing) + 1
    for i, (qt, opts, exp) in enumerate(tuples):
        q = mq(qt, opts, exp)
        q["question_number"] = start + i
        existing.append(q)
    data[key]["quiz_questions"] = existing
    count += 1

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Biology U1-U4: added questions to {count} lessons")
