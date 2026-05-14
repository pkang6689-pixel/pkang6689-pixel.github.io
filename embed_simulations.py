#!/usr/bin/env python3
"""
embed_simulations.py
Creates _Simulation.html pages, patches _Summary.html Next Up buttons,
and updates taskbar.js simulationConfig + tbSimConfig for every mapped lesson.

Run from the repo root:
    python embed_simulations.py
"""

import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
COURSE_FILES = os.path.join(BASE, "ArisEdu Project Folder", "CourseFiles")
TASKBAR_JS   = os.path.join(BASE, "ArisEdu Project Folder", "scripts", "taskbar.js")

# ─── simulation metadata ───────────────────────────────────────────────────
# sim_file → (badge_icon, description)
SIM_META = {
    "phase_changes.html":         ("🧪", "Explore how heating and cooling drive transitions between solid, liquid, and gas. Adjust temperature and observe the heating curve in real time."),
    "chemistry_lab.html":         ("🧪", "Perform virtual chemistry lab experiments exploring chemical reactions, observations, and lab techniques."),
    "gas_laws.html":              ("⚗️", "Adjust pressure, volume, and temperature to visualize Boyle's, Charles's, and Avogadro's gas laws in action."),
    "titration.html":             ("🧪", "Simulate an acid-base titration and identify the equivalence point on a pH curve."),
    "electrochemistry.html":      ("⚡", "Explore redox reactions, cell potential, and the electrochemical series in an interactive galvanic cell."),
    "calorimetry.html":           ("🌡️", "Measure heat transfer in chemical reactions and calculate specific heat capacity using a virtual calorimeter."),
    "equilibrium.html":           ("⚖️", "Observe Le Chatelier's Principle by stressing a reversible reaction and watching equilibrium shift."),
    "atomic_orbitals.html":       ("⚛️", "Visualize s, p, d, and f electron orbitals and explore the quantum numbers that define electron configuration."),
    "stoichiometry.html":         ("🧮", "Balance chemical equations and calculate molar ratios, limiting reagents, and theoretical yields."),
    "solutions.html":             ("🧪", "Explore solubility, molarity, and the effects of temperature and pressure on aqueous solutions."),
    "periodic_table_sim.html":    ("📊", "Interact with the periodic table to explore periodic trends: atomic radius, ionization energy, and electronegativity."),
    "molecular_geometry.html":    ("🔬", "Build 3-D molecules and predict shapes using VSEPR theory and bond angles."),
    "nuclear_decay.html":         ("☢️", "Simulate alpha, beta, and gamma decay and track changes in atomic number and mass over time."),
    "reaction_rates.html":        ("⏱️", "Adjust concentration, temperature, and catalysts to observe how reaction rate changes."),
    "acid_base.html":             ("🧪", "Explore the pH scale, strong vs. weak acids and bases, and buffer behavior in interactive experiments."),

    "projectile_motion.html":     ("🎯", "Launch objects at different angles and speeds to visualize projectile trajectories and kinematics."),
    "pendulum.html":              ("🕰️", "Adjust length, mass, and gravity to study pendulum period, frequency, and simple harmonic motion."),
    "spring_shm.html":            ("🌀", "Explore Hooke's Law and simple harmonic motion by compressing and stretching a spring-mass system."),
    "wave_simulator.html":        ("〰️", "Manipulate frequency, wavelength, and amplitude to visualize transverse and longitudinal waves."),
    "standing_waves.html":        ("〰️", "Form standing waves on a string by adjusting frequency and observe harmonics and resonance."),
    "doppler_effect.html":        ("🔊", "Simulate the Doppler effect by moving a sound source and observer and hearing the frequency shift."),
    "circuit_builder.html":       ("💡", "Build and test series and parallel circuits with resistors, batteries, and meters."),
    "electric_fields.html":       ("⚡", "Visualize electric field lines and equipotential surfaces around point charges."),
    "magnetism.html":             ("🧲", "Explore magnetic fields, forces on moving charges, and the right-hand rule in 3-D simulations."),
    "optics.html":                ("🔦", "Trace light rays through lenses and mirrors to explore refraction, reflection, and image formation."),
    "inclined_plane.html":        ("📐", "Resolve forces on an object on a ramp: normal force, friction, and net acceleration."),
    "centripetal_force.html":     ("🔄", "Investigate circular motion by adjusting radius and speed to observe centripetal acceleration and force."),
    "momentum_collisions.html":   ("💥", "Simulate elastic and inelastic collisions and verify conservation of momentum and kinetic energy."),

    "biology_lab.html":           ("🔬", "Explore prokaryotic and eukaryotic cell structures, organelles, and their functions in a virtual lab."),
    "cell_membrane.html":         ("🧫", "Visualize diffusion, osmosis, and active transport across the phospholipid bilayer."),
    "mitosis.html":               ("🔬", "Step through the phases of mitosis — prophase, metaphase, anaphase, and telophase — interactively."),
    "meiosis.html":               ("🔬", "Follow meiosis I and II to see how genetic diversity arises through crossing over and independent assortment."),
    "dna_replication.html":       ("🧬", "Watch the DNA double helix unwind and see how complementary base pairing copies genetic information."),
    "protein_folding.html":       ("🧬", "Translate mRNA codons into amino acids and explore how polypeptides fold into functional proteins."),
    "genetics.html":              ("🧬", "Set up Punnett squares and explore dominant, recessive, and codominant inheritance patterns."),
    "natural_selection.html":     ("🌿", "Simulate natural selection: watch populations evolve under predation pressure and environmental change."),
    "evolution_tree.html":        ("🌳", "Build and interpret phylogenetic trees to visualize evolutionary relationships between species."),
    "photosynthesis.html":        ("🌱", "Adjust light intensity, CO₂ levels, and wavelength to observe the light-dependent and Calvin cycle reactions."),
    "ecosystem.html":             ("🌍", "Trace energy flow through food chains and webs, and explore trophic levels and ecosystem stability."),

    "nervous_system.html":        ("🧠", "Visualize neuron structure, action potentials, and synaptic transmission across the nervous system."),
    "immune_system.html":         ("🛡️", "Follow a pathogen through the body and observe how innate and adaptive immune responses eliminate it."),
    "circulatory_system.html":    ("❤️", "Explore heart anatomy, blood flow through chambers and valves, and the pulmonary vs. systemic circuits."),
    "respiratory.html":           ("🫁", "Visualize lung anatomy, gas exchange in alveoli, and the mechanics of breathing."),
    "digestive_system.html":      ("🫀", "Trace food through the digestive tract and explore enzymatic digestion and nutrient absorption."),

    "marine_science_lab.html":    ("🌊", "Conduct virtual marine science experiments exploring ocean sampling, species identification, and data collection."),
    "salinity.html":              ("🧂", "Explore how temperature and salinity affect seawater density and stratification."),
    "ocean_currents.html":        ("🌊", "Visualize surface and deep-water circulation, thermohaline conveyor, and wind-driven gyres."),
    "tides.html":                 ("🌕", "See how gravitational pull from the Moon and Sun creates tidal patterns along coastlines."),
    "coastal_erosion.html":       ("🏖️", "Simulate wave energy, sediment transport, and coastal landform development over time."),
    "deep_sea_vents.html":        ("🌋", "Explore the geology and chemosynthetic ecosystems around hydrothermal vent communities."),
    "ocean_acidification.html":   ("⚗️", "Model how rising CO₂ lowers ocean pH and affects calcifying organisms like corals and mollusks."),
    "marine_food_web.html":       ("🐟", "Map energy flow from phytoplankton to apex predators in a marine food web."),
    "plankton.html":              ("🦠", "Identify phytoplankton and zooplankton types and explore their roles at the base of the marine food web."),
    "kelp_forest.html":           ("🌿", "Explore the kelp forest ecosystem: producers, herbivores, and the keystone sea otter."),
    "coral_reef.html":            ("🪸", "Investigate coral bleaching, symbiosis with zooxanthellae, and the effects of warming ocean temperatures."),
    "oil_spill.html":             ("🛢️", "Simulate an oil spill response: track pollutant spread and test clean-up strategies."),
    "bioluminescence.html":       ("✨", "Discover how deep-sea organisms produce light and explore its ecological roles."),
    "whale_migration.html":       ("🐋", "Track humpback whale migration routes and learn how environmental cues guide their journeys."),
    "tsunami.html":               ("🌊", "Simulate tsunami generation from underwater earthquakes and observe wave propagation across ocean basins."),

    "mineral_identification.html":("💎", "Identify minerals using hardness, cleavage, color, and streak tests in a virtual identification lab."),
    "rock_cycle.html":            ("🪨", "Follow igneous, sedimentary, and metamorphic rocks through the full rock cycle with interactive pathways."),
    "soil_layers.html":           ("🌱", "Explore soil horizons — O, A, B, C, and R — and the processes that form each layer."),
    "earthquake.html":            ("📍", "Visualize P-waves, S-waves, and surface waves as they travel through Earth during an earthquake."),
    "volcano_sim.html":           ("🌋", "Explore shield, composite, and cinder cone volcanoes and simulate eruption style based on magma composition."),
    "erosion_deposition.html":    ("🏜️", "Model wind and water erosion, sediment transport, and deposition landforms over time."),
    "glacier.html":               ("🏔️", "Simulate glacial advance and retreat, erosion, and the formation of glacial landforms like moraines and fjords."),
    "fossils.html":               ("🦕", "Discover fossilization processes and use index fossils and stratigraphy to date rock layers."),
    "atmosphere.html":            ("🌤️", "Explore the troposphere, stratosphere, mesosphere, thermosphere, and exosphere and their properties."),
    "weather.html":               ("⛈️", "Simulate the interaction of air masses, fronts, and pressure systems to generate weather patterns."),
    "climate_zones.html":         ("🌐", "Explore how latitude, elevation, and ocean currents create Earth's major climate zones."),
    "carbon_cycle.html":          ("♻️", "Track carbon through the atmosphere, biosphere, hydrosphere, and lithosphere and see how human emissions alter the cycle."),
    "groundwater.html":           ("💧", "Explore aquifers, groundwater recharge, and the hydrologic cycle through interactive earth cross-sections."),

    "seasons.html":               ("🌍", "Simulate Earth's axial tilt and orbital position to see why the hemispheres experience opposite seasons."),
    "moon_phases.html":           ("🌙", "Rotate the Moon around Earth and observe how changing relative positions produce the lunar cycle phases."),
    "solar_system.html":          ("☀️", "Explore the planets, dwarf planets, and other bodies in our solar system with orbital simulations."),
    "gravity_sim.html":           ("🪐", "Simulate gravitational attraction between massive bodies and observe orbital mechanics and escape velocity."),
    "hr_diagram.html":            ("⭐", "Plot stars on the Hertzsprung-Russell diagram and explore how luminosity and temperature define stellar class."),
    "stellar_evolution.html":     ("✨", "Follow a star from nebula to white dwarf, neutron star, or black hole based on its initial mass."),
    "black_holes.html":           ("⚫", "Visualize spacetime curvature, event horizons, and the behavior of matter near a black hole."),
    "galaxies.html":              ("🌌", "Classify elliptical, spiral, and irregular galaxies and explore the evidence for dark matter."),
    "cosmic_distance.html":       ("📡", "Use parallax, Cepheid variables, and standard candles to measure cosmic distances across the universe."),
    "spectroscopy.html":          ("🌈", "Analyze emission and absorption spectra to identify elements in stars and determine their velocities via Doppler shift."),
    "astronomy_observatory.html": ("🔭", "Operate a virtual observatory: choose targets, adjust the telescope, and analyze celestial data."),
    "exoplanets.html":            ("🌍", "Detect exoplanets using the transit and radial velocity methods and characterize their properties."),
    "rocket_science.html":        ("🚀", "Design and launch a rocket, adjusting thrust, fuel, and trajectory to achieve orbit."),

    "triangle_centers.html":      ("📐", "Explore the circumcenter, incenter, centroid, and orthocenter of triangles with interactive constructions."),
    "transformations.html":       ("🔄", "Apply translations, reflections, rotations, and dilations to geometric figures on a coordinate plane."),
    "conic_sections.html":        ("📈", "Slice a cone at different angles to generate circles, ellipses, parabolas, and hyperbolas interactively."),
    "fractals.html":              ("🌀", "Generate Mandelbrot sets, Sierpinski triangles, and other fractals by exploring recursive geometric patterns."),

    "quadratic_explorer.html":    ("📈", "Adjust a, b, and c to see how the parabola shifts, stretches, and reflects on the coordinate plane."),
    "probability.html":           ("🎲", "Run probability experiments — coin flips, dice rolls, and card draws — and observe theoretical vs. experimental results."),

    "linear_equations.html":      ("📏", "Graph and solve systems of linear equations by adjusting slopes and intercepts interactively."),
    "complex_numbers.html":       ("🔢", "Visualize complex numbers on the Argand plane and perform arithmetic operations geometrically."),
    "vectors.html":               ("➡️", "Explore vector addition, scalar multiplication, dot product, and cross product with interactive diagrams."),

    "unit_circle.html":           ("⭕", "Explore the unit circle: visualize radian measures, coordinates, and the values of sin, cos, and tan."),
    "polar_coordinates.html":     ("🌀", "Convert between rectangular and polar coordinates and plot polar curves interactively."),

    "statistics_viz.html":        ("📊", "Explore mean, median, mode, standard deviation, and distribution shapes through interactive data visualization."),

    "matrix_operations.html":     ("🔢", "Perform matrix addition, multiplication, transposition, and inversion with step-by-step visualization."),
}

# ─── full lesson-to-simulation mapping ─────────────────────────────────────
# Format: (lessonFolder, lessonId, unit, sim_file, lesson_title)
MAPPING = [
    # Chemistry
    ("ChemistryLessons",    "1.1",  "Unit1",  "phase_changes.html",         "States of Matter"),
    ("ChemistryLessons",    "1.2",  "Unit1",  "phase_changes.html",         "Phase Changes"),
    ("ChemistryLessons",    "3.3",  "Unit3",  "atomic_orbitals.html",       "Quantum Mechanical Model"),
    ("ChemistryLessons",    "4.6",  "Unit4",  "periodic_table_sim.html",    "Periodic Trends"),
    ("ChemistryLessons",    "4.8",  "Unit4",  "molecular_geometry.html",    "Molecular Geometry & VSEPR"),
    ("ChemistryLessons",    "6.1",  "Unit6",  "chemistry_lab.html",         "Types of Chemical Reactions"),
    ("ChemistryLessons",    "6.3",  "Unit6",  "electrochemistry.html",      "Redox Reactions"),
    ("ChemistryLessons",    "6.6",  "Unit6",  "reaction_rates.html",        "Reaction Rates"),
    ("ChemistryLessons",    "6.7",  "Unit6",  "equilibrium.html",           "Chemical Equilibrium"),
    ("ChemistryLessons",    "7.7",  "Unit7",  "stoichiometry.html",         "Stoichiometric Calculations"),
    ("ChemistryLessons",    "8.4",  "Unit8",  "gas_laws.html",              "Gas Laws"),
    ("ChemistryLessons",    "9.4",  "Unit9",  "solutions.html",             "Molarity & Solutions"),
    ("ChemistryLessons",    "10.6", "Unit10", "titration.html",             "Neutralization & Titration"),
    ("ChemistryLessons",    "10.9", "Unit10", "acid_base.html",             "pH Scale & Buffers"),
    ("ChemistryLessons",    "11.4", "Unit11", "calorimetry.html",           "Calorimetry"),
    ("ChemistryLessons",    "12.2", "Unit12", "nuclear_decay.html",         "Nuclear Decay"),

    # Physics
    ("PhysicsLessons",      "2.5",  "Unit2",  "projectile_motion.html",     "Free Fall & Projectile Motion"),
    ("PhysicsLessons",      "3.6",  "Unit3",  "inclined_plane.html",        "Normal Force & Inclined Planes"),
    ("PhysicsLessons",      "3.7",  "Unit3",  "centripetal_force.html",     "Circular Motion & Centripetal Force"),
    ("PhysicsLessons",      "5.4",  "Unit5",  "momentum_collisions.html",   "Elastic & Inelastic Collisions"),
    ("PhysicsLessons",      "7.1",  "Unit7",  "spring_shm.html",            "Simple Harmonic Motion"),
    ("PhysicsLessons",      "7.2",  "Unit7",  "pendulum.html",              "Period, Frequency & Amplitude"),
    ("PhysicsLessons",      "7.4",  "Unit7",  "wave_simulator.html",        "Wave Properties"),
    ("PhysicsLessons",      "7.6",  "Unit7",  "standing_waves.html",        "Standing Waves & Resonance"),
    ("PhysicsLessons",      "7.7",  "Unit7",  "doppler_effect.html",        "Doppler Effect"),
    ("PhysicsLessons",      "9.1",  "Unit9",  "optics.html",                "Reflection & Refraction"),
    ("PhysicsLessons",      "10.2", "Unit10", "electric_fields.html",       "Electric Field & Potential"),
    ("PhysicsLessons",      "10.4", "Unit10", "circuit_builder.html",       "Current, Resistance & Ohm's Law"),
    ("PhysicsLessons",      "10.6", "Unit10", "magnetism.html",             "Magnetic Fields & Forces"),

    # Biology
    ("BiologyLessons",      "2.6",  "Unit2",  "ecosystem.html",             "Food Chains & Webs"),
    ("BiologyLessons",      "4.5",  "Unit4",  "natural_selection.html",     "Natural Selection"),
    ("BiologyLessons",      "5.3",  "Unit5",  "evolution_tree.html",        "Phylogenetic Trees"),
    ("BiologyLessons",      "6.2",  "Unit6",  "biology_lab.html",           "Prokaryotic vs Eukaryotic Cells"),
    ("BiologyLessons",      "6.4",  "Unit6",  "cell_membrane.html",         "Membrane Transport"),
    ("BiologyLessons",      "8.3",  "Unit8",  "photosynthesis.html",        "Light-Dependent Reactions"),
    ("BiologyLessons",      "9.3",  "Unit9",  "mitosis.html",               "Mitosis"),
    ("BiologyLessons",      "10.1", "Unit10", "meiosis.html",               "Overview of Meiosis"),
    ("BiologyLessons",      "11.1", "Unit11", "genetics.html",              "Mendel's Laws of Heredity"),
    ("BiologyLessons",      "12.2", "Unit12", "dna_replication.html",       "DNA Replication"),
    ("BiologyLessons",      "12.4", "Unit12", "protein_folding.html",       "Protein Synthesis"),

    # Anatomy
    ("AnatomyLessons",      "4.2",  "Unit4",  "nervous_system.html",        "Action Potentials & Neural Signaling"),
    ("AnatomyLessons",      "6.1",  "Unit6",  "circulatory_system.html",    "Structure of the Heart"),
    ("AnatomyLessons",      "7.1",  "Unit7",  "respiratory.html",           "Anatomy of the Respiratory System"),
    ("AnatomyLessons",      "8.1",  "Unit8",  "digestive_system.html",      "Anatomy of the Digestive System"),
    ("AnatomyLessons",      "10.1", "Unit10", "immune_system.html",         "Immune System Overview"),

    # Earth Science
    ("EarthScienceLessons", "1.2",  "Unit1",  "mineral_identification.html","Mineral Identification"),
    ("EarthScienceLessons", "1.4",  "Unit1",  "rock_cycle.html",            "The Rock Cycle"),
    ("EarthScienceLessons", "1.5",  "Unit1",  "soil_layers.html",           "Soil Formation & Horizons"),
    ("EarthScienceLessons", "2.4",  "Unit2",  "earthquake.html",            "Earthquakes & Seismic Waves"),
    ("EarthScienceLessons", "2.5",  "Unit2",  "volcano_sim.html",           "Volcanoes & Eruption Types"),
    ("EarthScienceLessons", "3.2",  "Unit3",  "erosion_deposition.html",    "Erosion & Deposition"),
    ("EarthScienceLessons", "3.4",  "Unit3",  "glacier.html",               "Glaciers & Ice Ages"),
    ("EarthScienceLessons", "4.4",  "Unit4",  "fossils.html",               "Fossils & Relative Dating"),
    ("EarthScienceLessons", "5.1",  "Unit5",  "atmosphere.html",            "Layers of the Atmosphere"),
    ("EarthScienceLessons", "5.5",  "Unit5",  "weather.html",               "Weather Fronts & Air Masses"),
    ("EarthScienceLessons", "6.3",  "Unit6",  "climate_zones.html",         "Climate Zones"),
    ("EarthScienceLessons", "6.4",  "Unit6",  "carbon_cycle.html",          "Greenhouse Effect & Carbon Cycle"),

    # Marine Science
    ("MarineScienceLessons","1.1",  "Unit1",  "marine_science_lab.html",    "Introduction to Marine Science"),
    ("MarineScienceLessons","2.1",  "Unit2",  "salinity.html",              "Properties of Seawater"),
    ("MarineScienceLessons","2.2",  "Unit2",  "ocean_currents.html",        "Ocean Currents & Circulation"),
    ("MarineScienceLessons","2.3",  "Unit2",  "tides.html",                 "Waves & Tides"),
    ("MarineScienceLessons","2.4",  "Unit2",  "coastal_erosion.html",       "Coastal Processes & Erosion"),
    ("MarineScienceLessons","3.5",  "Unit3",  "deep_sea_vents.html",        "Hydrothermal Vents"),
    ("MarineScienceLessons","4.3",  "Unit4",  "ocean_acidification.html",   "Ocean Acidification"),
    ("MarineScienceLessons","5.2",  "Unit5",  "marine_food_web.html",       "Marine Food Chains & Webs"),
    ("MarineScienceLessons","5.3",  "Unit5",  "plankton.html",              "Plankton & Primary Producers"),
    ("MarineScienceLessons","5.5",  "Unit5",  "kelp_forest.html",           "Kelp Forest Ecosystems"),
    ("MarineScienceLessons","7.5",  "Unit7",  "whale_migration.html",       "Marine Mammal Migration"),
    ("MarineScienceLessons","8.2",  "Unit8",  "oil_spill.html",             "Oil Spills & Pollution"),
    ("MarineScienceLessons","8.3",  "Unit8",  "coral_reef.html",            "Coral Reefs & Bleaching"),
    ("MarineScienceLessons","9.3",  "Unit9",  "bioluminescence.html",       "Deep-Sea Exploration & Bioluminescence"),

    # Astronomy
    ("AstronomyLessons",    "2.2",  "Unit2",  "seasons.html",               "Earth's Seasons"),
    ("AstronomyLessons",    "2.3",  "Unit2",  "moon_phases.html",           "Lunar Phases"),
    ("AstronomyLessons",    "3.1",  "Unit3",  "solar_system.html",          "Formation of the Solar System"),
    ("AstronomyLessons",    "3.8",  "Unit3",  "gravity_sim.html",           "Gravity & Orbital Mechanics"),
    ("AstronomyLessons",    "5.2",  "Unit5",  "hr_diagram.html",            "The H-R Diagram"),
    ("AstronomyLessons",    "5.3",  "Unit5",  "stellar_evolution.html",     "Stellar Evolution"),
    ("AstronomyLessons",    "5.7",  "Unit5",  "black_holes.html",           "Black Holes"),
    ("AstronomyLessons",    "6.1",  "Unit6",  "galaxies.html",              "Types of Galaxies"),
    ("AstronomyLessons",    "6.5",  "Unit6",  "cosmic_distance.html",       "Measuring Cosmic Distances"),
    ("AstronomyLessons",    "7.5",  "Unit7",  "rocket_science.html",        "Rocket Propulsion & Space Travel"),
    ("AstronomyLessons",    "8.5",  "Unit8",  "exoplanets.html",            "Detecting Exoplanets"),
    ("AstronomyLessons",    "9.1",  "Unit9",  "astronomy_observatory.html", "Observational Astronomy"),
    ("AstronomyLessons",    "9.4",  "Unit9",  "spectroscopy.html",          "Spectroscopy"),

    # Geometry
    ("GeometryLessons",     "5.1",  "Unit5",  "triangle_centers.html",      "Triangle Bisectors & Centers"),
    ("GeometryLessons",     "7.8",  "Unit7",  "fractals.html",              "Fractals & Self-Similarity"),
    ("GeometryLessons",     "9.1",  "Unit9",  "transformations.html",       "Translations & Reflections"),
    ("GeometryLessons",     "9.2",  "Unit9",  "transformations.html",       "Rotations"),
    ("GeometryLessons",     "9.3",  "Unit9",  "transformations.html",       "Dilations & Similarity"),
    ("GeometryLessons",     "10.9", "Unit10", "conic_sections.html",        "Conic Sections"),

    # Algebra 1
    ("Algebra1Lessons",     "6.1",  "Unit6",  "quadratic_explorer.html",    "Quadratic Functions & Parabolas"),
    ("Algebra1Lessons",     "12.1", "Unit12", "probability.html",           "Introduction to Probability"),

    # Algebra 2
    ("Algebra2Lessons",     "1.2",  "Unit1",  "linear_equations.html",      "Systems of Linear Equations"),
    ("Algebra2Lessons",     "3.6",  "Unit3",  "complex_numbers.html",       "Complex Numbers"),
    ("Algebra2Lessons",     "9.1",  "Unit9",  "conic_sections.html",        "Conic Sections"),
    ("Algebra2Lessons",     "9.3",  "Unit9",  "vectors.html",               "Introduction to Vectors"),

    # Trigonometry
    ("TrigonometryLessons", "1.5",  "Unit1",  "unit_circle.html",           "The Unit Circle"),
    ("TrigonometryLessons", "8.1",  "Unit8",  "polar_coordinates.html",     "Polar Coordinates"),
    ("TrigonometryLessons", "9.1",  "Unit9",  "vectors.html",               "Vectors in the Plane"),

    # Statistics
    ("StatisticsLessons",   "2.4",  "Unit2",  "statistics_viz.html",        "Data Visualization & Distributions"),
    ("StatisticsLessons",   "4.1",  "Unit4",  "probability.html",           "Basic Probability"),

    # Linear Algebra
    ("LinearAlgebraLessons","1.4",  "Unit1",  "matrix_operations.html",     "Matrix Operations"),
]

# ─── section tag used in translation_loader data-section attr ───────────────
SECTION_MAP = {
    "ChemistryLessons":    "chemistry",
    "PhysicsLessons":      "physics",
    "BiologyLessons":      "biology",
    "AnatomyLessons":      "anatomy",
    "EarthScienceLessons": "earth_science",
    "MarineScienceLessons":"marine_science",
    "AstronomyLessons":    "astronomy",
    "GeometryLessons":     "geometry",
    "Algebra1Lessons":     "algebra1",
    "Algebra2Lessons":     "algebra2",
    "TrigonometryLessons": "trigonometry",
    "StatisticsLessons":   "statistics",
    "LinearAlgebraLessons":"linear_algebra",
}


def make_sim_html(lesson_folder, lesson_id, sim_file, lesson_title, section, prefix):
    icon, desc = SIM_META.get(sim_file, ("🔬", "Explore this interactive simulation."))
    return f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>Lesson {lesson_id}: {lesson_title} Simulation</title>
  <script src="/_sdk/element_sdk.js"></script>
  <script src="../../../scripts/translation_loader.js" data-section="{section}" data-base="../../../translations"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet"/>
  <link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
  <style>
    @view-transition {{ navigation: auto; }}

    .sim-wrapper {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }}

    .sim-frame-container {{
      width: 100%;
      border-radius: 1rem;
      overflow: hidden;
      border: 2px solid rgba(148, 163, 184, 0.2);
      box-shadow: 0 4px 24px rgba(0,0,0,0.3);
      background: #0f172a;
      position: relative;
    }}

    .sim-frame-container iframe {{
      width: 100%;
      height: 600px;
      border: none;
      display: block;
      overflow: hidden;
    }}

    .sim-info-bar {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.75rem 1rem;
      background: rgba(148, 163, 184, 0.08);
      border-radius: 0.75rem;
      font-size: 0.875rem;
      color: #94a3b8;
    }}

    .sim-info-bar .sim-badge {{
      background: linear-gradient(135deg, #f59e0b, #ef4444);
      color: white;
      font-weight: 700;
      font-size: 0.75rem;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
    }}

    .sim-actions {{
      display: flex;
      justify-content: flex-end;
    }}

    .fullscreen-btn {{
      background: none;
      border: 1px solid rgba(148,163,184,0.3);
      color: #94a3b8;
      border-radius: 0.5rem;
      padding: 0.4rem 0.9rem;
      font-size: 0.8rem;
      cursor: pointer;
      transition: background 0.2s, color 0.2s;
    }}

    .fullscreen-btn:hover {{
      background: rgba(148,163,184,0.1);
      color: #f1f5f9;
    }}
  </style>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet"/>
  <script src="../../../theme_manager.js"></script>
</head>
<body class="dark-mode h-full">
  <script src="../../../scripts/taskbar.js"></script>
  <main class="main-container">
    <div id="simulation-content-view">
      <h2 class="page-title" data-i18n="Lesson {lesson_id}: {lesson_title} Simulation">Lesson {lesson_id}: {lesson_title} — Simulation</h2>
      <div class="diagram-card">
        <div class="sim-wrapper">

          <div class="sim-info-bar">
            <span class="sim-badge">{icon} Lab</span>
            <span>{desc}</span>
            <div class="sim-actions" style="margin-left:auto;">
              <button class="fullscreen-btn" onclick="toggleFullscreen()" title="Open simulation in full screen">&#x26F6; Fullscreen</button>
            </div>
          </div>

          <div class="sim-frame-container" id="sim-frame-container">
            <iframe
              id="sim-iframe"
              src="../../../labs/{sim_file}"
              title="{lesson_title} Simulation"
              allow="fullscreen"
              scrolling="no"
              sandbox="allow-scripts allow-same-origin allow-forms"
            ></iframe>
          </div>

          <div class="summary-actions">
            <a class="side-button" href="{prefix}_Practice.html" style="text-align:center; text-decoration:none; display:block;">Next Up: Practice</a>
          </div>

        </div>
      </div>
    </div>
  </main>

  <script>
    var iframe = document.getElementById('sim-iframe');

    function resizeIframe() {{
      try {{
        var doc = iframe.contentDocument || iframe.contentWindow.document;
        var h = Math.max(
          doc.body.scrollHeight,
          doc.body.offsetHeight,
          doc.documentElement.scrollHeight
        );
        if (h > 100) iframe.style.height = h + 'px';
      }} catch(e) {{}}
    }}

    iframe.addEventListener('load', function() {{
      resizeIframe();
      setTimeout(resizeIframe, 300);
      setTimeout(resizeIframe, 800);
    }});

    function toggleFullscreen() {{
      var container = document.getElementById('sim-frame-container');
      if (!document.fullscreenElement) {{
        (container.requestFullscreen || container.webkitRequestFullscreen || function(){{}}).call(container);
      }} else {{
        (document.exitFullscreen || document.webkitExitFullscreen || function(){{}}).call(document);
      }}
    }}
  </script>
</body>
</html>
'''


def patch_summary_next_up(summary_path, lesson_id):
    """Change 'Next Up: Play/Practice' link to point to _Simulation.html"""
    if not os.path.exists(summary_path):
        return False
    with open(summary_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Detect naming convention from the summary path itself
    basename = os.path.basename(summary_path)
    if basename.startswith("Lesson "):
        prefix = f"Lesson {lesson_id}"   # spaced
    else:
        prefix = f"Lesson{lesson_id}"    # no-space

    sim_link      = f"{prefix}_Simulation.html"
    practice_link = f"{prefix}_Practice.html"

    # Already patched?
    if sim_link in content:
        return False

    old = f'href="{practice_link}"'
    if old not in content:
        print(f"  WARNING: could not find Practice link in {summary_path}")
        return False

    new = f'href="{sim_link}"'
    count = content.count(old)
    if count > 1:
        idx = content.rfind(old)
        content = content[:idx] + new + content[idx+len(old):]
    else:
        content = content.replace(old, new, 1)

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def update_taskbar_js(new_entries):
    """Insert new simulationConfig and tbSimConfig entries into taskbar.js"""
    with open(TASKBAR_JS, "r", encoding="utf-8") as f:
        content = f.read()

    # Build the entry strings for simulationConfig (bottom progress bar)
    sim_lines = []
    tb_lines = []
    for key, icon in new_entries:
        esc_icon = icon  # keep emoji as-is; Python writes UTF-8
        sim_lines.append(f"      '{key}': {{ label: 'Simulation', icon: '{esc_icon}', url: baseName + '_Simulation.html' }}")
        tb_lines.append(f"        '{key}': {{ label: 'Simulation', icon: '{esc_icon}' }}")

    # Patch simulationConfig block (bottom bar)
    old_sim = "      'ChemistryLessons:1.1': { label: 'Simulation', icon: '\\uD83E\\uDDEA', url: baseName + '_Simulation.html' }"
    new_sim_block = old_sim + "\n" + ",\n".join(
        [""] + [l for l in sim_lines if "'ChemistryLessons:1.1'" not in l]
    )
    if old_sim in content:
        content = content.replace(old_sim, new_sim_block, 1)
    else:
        print("WARNING: simulationConfig anchor not found in taskbar.js")

    # Patch tbSimConfig block (taskbar center bar)
    old_tb = "        'ChemistryLessons:1.1': { label: 'Simulation', icon: '\\uD83E\\uDDEA' }"
    new_tb_block = old_tb + "\n" + ",\n".join(
        [""] + [l for l in tb_lines if "'ChemistryLessons:1.1'" not in l]
    )
    if old_tb in content:
        content = content.replace(old_tb, new_tb_block, 1)
    else:
        print("WARNING: tbSimConfig anchor not found in taskbar.js")

    with open(TASKBAR_JS, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    created = 0
    patched_summary = 0
    skipped = 0
    missing_summary = 0
    taskbar_entries = []  # (key, icon)

    # Chem 1.1 already done — include in taskbar entries so it's not duplicated
    # but don't re-create the sim file.
    already_done = {"ChemistryLessons:1.1"}

    for lesson_folder, lesson_id, unit, sim_file, lesson_title in MAPPING:
        key = f"{lesson_folder}:{lesson_id}"
        section = SECTION_MAP.get(lesson_folder, lesson_folder.lower())
        icon = SIM_META.get(sim_file, ("🔬", ""))[0]

        unit_dir = os.path.join(COURSE_FILES, lesson_folder, unit)
        # Determine naming convention (space vs no-space)
        spaced   = os.path.join(unit_dir, f"Lesson {lesson_id}_Summary.html")
        nospace  = os.path.join(unit_dir, f"Lesson{lesson_id}_Summary.html")
        if os.path.exists(spaced):
            summary_path = spaced
            sim_path     = os.path.join(unit_dir, f"Lesson {lesson_id}_Simulation.html")
        elif os.path.exists(nospace):
            summary_path = nospace
            sim_path     = os.path.join(unit_dir, f"Lesson{lesson_id}_Simulation.html")
        else:
            summary_path = spaced   # keep spaced as default for "not found" message
            sim_path     = os.path.join(unit_dir, f"Lesson {lesson_id}_Simulation.html")

        if not os.path.isdir(unit_dir):
            print(f"SKIP (no dir): {unit_dir}")
            skipped += 1
            taskbar_entries.append((key, icon))
            continue

        if not os.path.exists(summary_path):
            print(f"SKIP (no summary): {summary_path}")
            missing_summary += 1
            taskbar_entries.append((key, icon))
            continue

        taskbar_entries.append((key, icon))

        # Create simulation HTML
        if key not in already_done:
            # Determine prefix (space vs no-space) from whichever summary was found
            if os.path.basename(summary_path).startswith("Lesson "):
                prefix = f"Lesson {lesson_id}"
            else:
                prefix = f"Lesson{lesson_id}"

            if os.path.exists(sim_path):
                print(f"EXISTS (skip create): {sim_path}")
            else:
                html = make_sim_html(lesson_folder, lesson_id, sim_file, lesson_title, section, prefix)
                with open(sim_path, "w", encoding="utf-8") as f:
                    f.write(html)
                print(f"CREATED: {sim_path}")
                created += 1

        # Patch summary next-up button
        if key not in already_done:
            if patch_summary_next_up(summary_path, lesson_id):
                print(f"PATCHED summary: {summary_path}")
                patched_summary += 1
            else:
                print(f"SKIP patch (already done or missing link): {summary_path}")

    # Update taskbar.js
    print("\nUpdating taskbar.js...")
    update_taskbar_js(taskbar_entries)
    print("taskbar.js updated.")

    print(f"\nDone. Created: {created}, Summary patched: {patched_summary}, "
          f"Skipped (no dir): {skipped}, Missing summary: {missing_summary}")


if __name__ == "__main__":
    main()
