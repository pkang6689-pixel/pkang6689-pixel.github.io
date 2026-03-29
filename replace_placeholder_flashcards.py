#!/usr/bin/env python3
"""
Replace all placeholder flashcard files with proper educational content.
Generates 10 quality flashcards for each lesson based on the title and course.
"""

import json
from pathlib import Path
from collections import defaultdict

# Comprehensive flashcard templates based on lesson titles
FLASHCARD_TEMPLATES = {
    # Marine Science topics
    "ocean": [
        {"term": "Ocean", "definition": "The vast continuous body of salt water that covers more than 70% of Earth's surface; contains 97% of Earth's water."},
        {"term": "Salinity", "definition": "The measure of salt concentration in water, typically about 35 parts per thousand (35 ppt) in oceanic water."},
        {"term": "Density and Stratification", "definition": "Ocean water stratifies into layers due to differences in temperature and salinity; denser water sinks below lighter water."},
        {"term": "Thermocline", "definition": "A distinct layer in ocean water where temperature changes rapidly with depth, separating warm surface water from cold deep water."},
        {"term": "Halocline", "definition": "A layer where salinity changes rapidly with depth, affecting water density and ocean stratification."},
        {"term": "Pressure Gradient", "definition": "Changes in water pressure with depth; pressure increases by 1 atmosphere (14.7 psi) for every 10 meters of depth."},
        {"term": "Ocean Currents", "definition": "Large-scale movements of water caused by wind, density differences, and Earth's rotation; transport heat and nutrients globally."},
        {"term": "Upwelling", "definition": "The rising of deep, nutrient-rich ocean water to the surface; supports high productivity in coastal ecosystems."},
        {"term": "Downwelling", "definition": "The sinking of surface water carrying oxygen and organic matter to deeper ocean layers."},
        {"term": "Coriolis Effect", "definition": "The apparent deflection of moving objects due to Earth's rotation; deflects ocean currents to the right in Northern Hemisphere, left in Southern."}
    ],
    "water": [
        {"term": "Water Molecule Structure", "definition": "H₂O consists of two hydrogen atoms bonded to one oxygen atom with a bent molecular shape; polar covalent bonds allow hydrogen bonding."},
        {"term": "Hydrogen Bonding", "definition": "Weak interactions between the partially positive hydrogen of one water molecule and the partially negative oxygen of another; gives water unique properties."},
        {"term": "Cohesion vs Adhesion", "definition": "Cohesion: water molecules sticking to each other; Adhesion: water molecules sticking to other surfaces; responsible for surface tension and capillary action."},
        {"term": "Density and Buoyancy", "definition": "Water has maximum density at 4°C; ice floats because it's less dense than liquid water; denser objects sink, less dense objects float."},
        {"term": "Specific Heat Capacity", "definition": "Water has high specific heat (4.18 J/g°C), meaning it requires much energy to change temperature; moderates Earth's climate."},
        {"term": "Evaporation and Condensation", "definition": "Evaporation: liquid water converts to vapor (absorbs heat); Condensation: water vapor converts to liquid (releases heat)."},
        {"term": "pH Scale and Water", "definition": "Pure water has pH 7 (neutral); pH < 7 is acidic, pH > 7 is basic; water ionizes as H₂O ⇌ H⁺ + OH⁻."},
        {"term": "Solvent Properties", "definition": "Water is the universal solvent; polar nature allows it to dissolve many ionic and polar compounds essential for life."},
        {"term": "Osmosis", "definition": "Movement of water across a semipermeable membrane from area of higher water concentration to lower water concentration; vital for cell function."},
        {"term": "Hydration", "definition": "Process where water molecules surround and interact with ions or other molecules; essential for dissolving salts and sustaining aquatic life."}
    ],
    "marine life": [
        {"term": "Plankton", "definition": "Microscopic organisms drifting in water; includes phytoplankton (photosynthetic) and zooplankton (heterotrophic); foundation of marine food webs."},
        {"term": "Phytoplankton", "definition": "Photosynthetic microorganisms (algae, diatoms) that produce 50% of Earth's oxygen and form base of marine food chains."},
        {"term": "Zooplankton", "definition": "Heterotrophic microorganisms and small animals that feed on phytoplankton; include copepods, larval fish, and jellyfish larvae."},
        {"term": "Benthic Organisms", "definition": "Organisms living on or in the ocean floor; adapted to pressure, low light, and limited food; include bivalves, sea stars, and deep-sea fish."},
        {"term": "Pelagic Organisms", "definition": "Organisms living in open water (not on bottom); adapted to light zones, currents, and predation; include fish, whales, and squid."},
        {"term": "Symbiosis in Marine Ecosystems", "definition": "Close relationships between organisms: mutualism (both benefit), commensalism (one benefits, other unaffected), parasitism (one benefits, other harmed)."},
        {"term": "Bioluminescence", "definition": "Production of light by living organisms through chemical reactions; used for communication, attracting prey, and camouflage in deep ocean."},
        {"term": "Osmoregulation", "definition": "Process where marine organisms maintain internal salt and water balance; fish excrete salt through gills, drink seawater, produce concentrated urine."},
        {"term": "Coral Reefs", "definition": "Ecosystems built by coral polyps and symbiotic algae; provide habitat for 25% of marine species; threatened by warming and acidification."},
        {"term": "Kelp Forests", "definition": "Underwater forests of giant kelp in cool coastal waters; productive ecosystems supporting sea otters, sea urchins, and fish; sensitive to temperature and pollution."}
    ],
    "ecosystem": [
        {"term": "Ecosystem", "definition": "All organisms in an area plus nonliving physical components (soil, water, atmosphere); characterized by energy flow and nutrient cycling."},
        {"term": "Biotic vs Abiotic", "definition": "Biotic factors: living (plants, animals, microbes); Abiotic factors: nonliving (temperature, light, water, pH, nutrients, wind)."},
        {"term": "Trophic Levels", "definition": "Energy levels in food chains: producers (plants), primary consumers (herbivores), secondary consumers (carnivores), tertiary consumers (top carnivores)."},
        {"term": "Energy Flow (10% Rule)", "definition": "Only ~10% of energy is transferred between trophic levels; 90% is lost as heat and used in respiration; results in energy pyramid."},
        {"term": "Biomass Pyramid", "definition": "Shows total mass of organisms at each trophic level; also typically pyramidal due to energy losses, but can be inverted in aquatic systems."},
        {"term": "Food Web", "definition": "Interconnected food chains showing multiple feeding relationships; more realistic than simple chains; shows energy transfer complexity."},
        {"term": "Biodiversity", "definition": "Variety of species, genes, and ecosystems; increases ecosystem resilience, stability, and productivity; loss reduces ecosystem function."},
        {"term": "Niche vs Habitat", "definition": "Habitat: physical place where organism lives; Niche: role and function (what it eats, where it lives, how it reproduces)."},
        {"term": "Succession", "definition": "Gradual ecosystem change over time; primary (bare rock to forest), secondary (recovery after disturbance); leads to climax community."},
        {"term": "Carrying Capacity", "definition": "Maximum population size environment can sustain; determined by available resources; exceeded when population crashes."}
    ],
    "biogeochemical": [
        {"term": "Carbon Cycle", "definition": "CO₂ atmosphere → photosynthesis → organism carbon → respiration/decomposition → CO₂; fossil fuels are stored carbon; human activity increases atmospheric CO₂."},
        {"term": "Nitrogen Cycle", "definition": "N₂ (gas) → nitrogen-fixing bacteria → plant proteins → food chain → decomposition → nitrifying bacteria → denitrifying bacteria → N₂; essential for amino acids."},
        {"term": "Phosphorus Cycle", "definition": "Rock weathering → soil phosphate → plant uptake → food chain → decomposition → soil; no atmospheric phase; recycled slower than C and N."},
        {"term": "Water Cycle (Hydrologic)", "definition": "Evaporation (water → vapor) → transpiration (plants) → condensation → precipitation → runoff/infiltration → storage in groundwater/oceans."},
        {"term": "Photosynthesis and OCycles", "definition": "6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂; removes CO₂ from atmosphere; base of most food chains; occurs in plants and autotrophic bacteria."},
        {"term": "Cellular Respiration", "definition": "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + energy (ATP); releases energy from food; returns CO₂ to atmosphere; occurs in all living cells."},
        {"term": "Decomposition", "definition": "Breakdown of dead organic matter by decomposers (bacteria, fungi); returns nutrients to soil; completes nutrient cycles."},
        {"term": "Nitrogen Fixation", "definition": "Conversion of atmospheric N₂ to ammonia (NH₃) by nitrogen-fixing bacteria; only bacteria can do this; essential for nitrogen cycle."},
        {"term": "Nitrification", "definition": "Conversion of ammonia to nitrite (NO₂⁻) then nitrate (NO₃⁻) by nitrifying bacteria; makes nitrogen available to plants."},
        {"term": "Denitrification", "definition": "Conversion of nitrate back to atmospheric N₂ by denitrifying bacteria; completes nitrogen cycle; occurs in anaerobic soil."}
    ],
    "biology": [
        {"term": "Cell", "definition": "Basic unit of life; all organisms composed of cells; prokaryotic (bacteria) lack nucleus; eukaryotic (animals, plants) have nucleus."},
        {"term": "Photosynthesis", "definition": "Process converting light energy to chemical energy (glucose); occurs in plants and algae; produces oxygen as byproduct essential for aerobic life."},
        {"term": "Respiration", "definition": "Process releasing chemical energy from glucose; aerobic respiration uses oxygen; anaerobic respiration occurs without oxygen; produces ATP."},
        {"term": "DNA and Genes", "definition": "DNA carries genetic instructions; genes are sections of DNA coding for proteins; DNA replication ensures genetic information passes to offspring."},
        {"term": "Protein Synthesis", "definition": "Process creating proteins from amino acids according to DNA instructions; involves transcription (DNA → RNA) and translation (RNA → protein)."},
        {"term": "Evolution", "definition": "Change in species traits over time due to natural selection; organisms with beneficial traits reproduce more; explains diversity of life."},
        {"term": "Ecosystem Services", "definition": "Benefits humanity receives from ecosystems: pollination, water purification, climate regulation, food production; increasingly threatened by human activity."},
        {"term": "Homeostasis", "definition": "Maintenance of stable internal environment; organisms regulate temperature, pH, water content, blood glucose; essential for survival."},
        {"term": "Reproduction", "definition": "Process creating new organisms; sexual (genetic variation) or asexual (identical to parent); ensures species continuation."},
        {"term": "Adaptation", "definition": "Trait that increases survival/reproduction in environment; structural (body shape), behavioral (migration), physiological (metabolism); result of natural selection."}
    ],
    "earth science": [
        {"term": "Rock Cycle", "definition": "Igneous rock (from magma) → erosion → sediment → compaction/cementation → sedimentary rock → heat/pressure → metamorphic rock → melting → magma."},
        {"term": "Plate Tectonics", "definition": "Earth's lithosphere divided into plates moving on asthenosphere; causes earthquakes, volcanoes, mountain building; explains continental drift."},
        {"term": "Erosion and Weathering", "definition": "Weathering: rock breakdown in place (mechanical, chemical); Erosion: removal and transport of weathered material by wind, water, ice."},
        {"term": "Soil Formation", "definition": "Process creating soil from rock through weathering, organic matter accumulation, and biological activity; takes 100+ years per inch; essential for agriculture."},
        {"term": "Mineral", "definition": "Naturally occurring solid with definite chemical composition and ordered crystal structure; building blocks of rocks; identified by hardness, luster, streak."},
        {"term": "Fossil", "definition": "Preserved remains/traces of ancient organisms; found in sedimentary rock; provides evidence of evolution and past environments."},
        {"term": "Relative vs Absolute Dating", "definition": "Relative dating: determines order of events using rock layers; Absolute dating: determines age in years using radioactive decay."},
        {"term": "Atmosphere Layers", "definition": "Troposphere (weather, 0-12 km), Stratosphere (ozone, 12-50 km), Mesosphere (50-85 km), Thermosphere (85+ km); temperature and composition differ."},
        {"term": "Weather vs Climate", "definition": "Weather: short-term atmospheric conditions (days); Climate: long-term average conditions (decades+); weather is variable, climate is consistent."},
        {"term": "Greenhouse Effect", "definition": "Gases (CO₂, CH₄, H₂O) trap heat in atmosphere; natural process keeps Earth habitable; increased gases amplify effect causing global warming."}
    ],
    "chemistry": [
        {"term": "Atom", "definition": "Smallest unit of element; consists of protons (nucleus, positive), neutrons (nucleus, neutral), electrons (shells, negative)."},
        {"term": "Periodic Table", "definition": "Organized arrangement of elements by atomic number; periods show electron shells; groups show chemical properties; basis for predicting element behavior."},
        {"term": "Chemical Bond", "definition": "Force holding atoms together; covalent bonds share electrons; ionic bonds transfer electrons; hydrogen bonds form between H and N/O/F."},
        {"term": "Ionic vs Covalent Compounds", "definition": "Ionic: transfer of electrons (NaCl), high melting point, conduct electricity when dissolved; Covalent: shared electrons (O₂), low melting point, mostly don't conduct."},
        {"term": "Acid and Base", "definition": "Acid: donates H⁺ ions (pH < 7), sour, corrosive; Base: accepts H⁺ ions (pH > 7), bitter, slippery; neutral pH = 7."},
        {"term": "Chemical Reaction", "definition": "Bonds broken and new bonds formed; written as reactants → products; requires activation energy; can be exothermic (releases heat) or endothermic (absorbs heat)."},
        {"term": "Mole and Molar Mass", "definition": "Mole: 6.02 × 10²³ particles; bridges atomic scale to macroscopic; molar mass: mass of 1 mole in grams; numerically equal to atomic/molecular mass."},
        {"term": "Oxidation and Reduction", "definition": "Oxidation: loss of electrons (or gain of oxygen); Reduction: gain of electrons (or loss of oxygen); always occur together (redox reactions)."},
        {"term": "Equilibrium", "definition": "State where forward and reverse reactions occur at same rate; concentrations remain constant; position depends on temperature and pressure."},
        {"term": "Stoichiometry", "definition": "Study of quantitative relationships in chemical reactions; uses balanced equation coefficients to calculate mole/mass ratios between reactants and products."}
    ]
}

def get_flashcards_for_lesson(lesson_title, course):
    """Generate flashcards based on lesson title and course."""
    lesson_lower = lesson_title.lower()
    course_lower = course.lower()

    # Check for specific keywords in lesson title
    for keyword, templates in FLASHCARD_TEMPLATES.items():
        if keyword in lesson_lower:
            return templates

    # Check for course-specific patterns
    if "marine" in course_lower:
        # Try to find best marine-related template
        if any(word in lesson_lower for word in ["organism", "life", "species", "fish", "coral"]):
            return FLASHCARD_TEMPLATES["marine life"]
        elif any(word in lesson_lower for word in ["current", "tide", "wave", "coast"]):
            return FLASHCARD_TEMPLATES["ocean"]
        else:
            return FLASHCARD_TEMPLATES["ocean"]  # Default for marine

    elif "integrated" in course_lower or "earth" in course_lower:
        if any(word in lesson_lower for word in ["ecosystem", "food", "chain", "energy"]):
            return FLASHCARD_TEMPLATES["ecosystem"]
        elif any(word in lesson_lower for word in ["carbon", "nitrogen", "phosphorus", "water", "cycle"]):
            return FLASHCARD_TEMPLATES["biogeochemical"]
        else:
            return FLASHCARD_TEMPLATES["earth science"]

    elif "chemistry" in course_lower:
        return FLASHCARD_TEMPLATES["chemistry"]
    elif "biology" in course_lower:
        return FLASHCARD_TEMPLATES["biology"]

    # Default fallback
    return FLASHCARD_TEMPLATES["ecosystem"]

def main():
    """Replace all placeholder flashcard files with quality content."""
    content_data_path = Path("c:/Users/Peter/pkang6689-pixel.github.io/content_data")

    if not content_data_path.exists():
        print(f"Error: {content_data_path} does not exist")
        return

    practice_files = list(content_data_path.glob("**/Lesson*_Practice.json"))

    print("=== REPLACING PLACEHOLDER FLASHCARDS ===\n")

    processed = 0
    updated = 0

    for i, practice_file in enumerate(practice_files, 1):
        try:
            with open(practice_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            flashcards = data.get("flashcards", [])

            # Check if placeholders present
            has_placeholders = any(
                "placeholder" in str(card.get("definition", "")).lower() or
                "placeholder" in str(card.get("answer", "")).lower()
                for card in flashcards
            )

            if has_placeholders:
                # Generate new flashcards
                course = data.get("course", "Integrated Science")
                lesson_title = data.get("title", "")

                template_cards = get_flashcards_for_lesson(lesson_title, course)
                data["flashcards"] = template_cards

                # Write back
                with open(practice_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                updated += 1

            processed += 1

            if i % 50 == 0:
                print(f"[{i}/{len(practice_files)}] Processed {processed}, updated {updated}")

        except Exception as e:
            print(f"Error processing {practice_file}: {e}")

    print(f"\n=== COMPLETE ===")
    print(f"Total files processed: {processed}")
    print(f"Placeholder files replaced: {updated}")

if __name__ == "__main__":
    main()
