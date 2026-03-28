import json

path = "C:/Users/Peter/pkang6689-pixel.github.io/content_data/EnvironmentalScienceLessons/Unit5/Lesson5.2_Quiz.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixes = {
    1: [
        "Combustion of uranium fuel pellets inside a conventional high-temperature furnace similar to a coal-fired boiler system",
        "Nuclear fusion reactions that combine hydrogen isotopes under extreme pressure to create helium and release thermal energy",
        "Exothermic chemical reactions between refined metallic compounds that generate enough sustained heat to boil water for steam"
    ],
    3: [
        "A relatively minor and contained radioactive leak that was fully controlled within the reactor building without external release",
        "Structural damage limited exclusively to the outer reactor containment building shell with no compromise of the inner core systems",
        "An incident where absolutely no measurable radioactive contamination was released beyond the immediate boundaries of the plant site"
    ],
    4: [
        "A series of deliberate human operator errors committed during a routine maintenance procedure that compromised all reactor cooling systems",
        "A coordinated terrorist attack on the facility that simultaneously disabled multiple independent safety and backup power generation systems",
        "Gradual deterioration of aging equipment and structural components that had not been properly maintained or replaced on the recommended schedule"
    ],
    5: [
        "Sourcing and transporting sufficient volumes of cooling water from nearby rivers or ocean sources to maintain safe reactor operating temperatures",
        "Recruiting and training enough qualified nuclear engineers, technicians, and safety personnel to operate complex modern reactor facilities",
        "Generating enough total electrical output from nuclear fission to meet increasing baseload electricity demand in growing population centers"
    ],
    7: [
        "Exclusively minor noise pollution from surface-level equipment operations at mine sites without any chemical or radiological contamination",
        "Absolutely no documented or scientifically measurable environmental impacts of any kind associated with commercial uranium mining operations",
        "Only localized airborne dust particle production from earth-moving activities at the mine site without any toxic or radioactive component"
    ],
    8: [
        "The radioactive material completely decays into stable non-radioactive atoms within a single 24,000-year half-life period and becomes entirely safe",
        "After exactly 24,000 years the plutonium-239 becomes entirely safe for human handling and can be disposed of through conventional waste methods",
        "Plutonium-239 has been definitively shown to be non-radioactive and poses no significant radiation hazard during storage or handling procedures"
    ],
    13: [
        "The standard industrial process of chemically reprocessing and recycling used nuclear fuel rods to extract remaining fissile material for reuse",
        "A carefully planned and controlled shutdown procedure that safely brings a nuclear reactor from full power to a cold non-operating condition",
        "The routine and expected day-to-day operational behavior of a nuclear reactor running within its normal design parameters and safety margins"
    ],
    16: [
        "A sequence of cascading chemical explosions that propagate through connected fuel storage systems and amplify destructive energy with each detonation",
        "A specialized water-cooling circulation system engineered to remove excess thermal energy from reactor components during normal power generation",
        "The physical interconnection of multiple nuclear power generating stations through a shared high-voltage electrical transmission distribution grid"
    ],
    17: [
        "A type of nuclear weapon detonation process that occurs exclusively in military applications and has no relevance to civilian energy production",
        "The controversial practice of disposing radioactive nuclear waste materials by dumping sealed containers into deep ocean trenches for permanent storage",
        "The process of breaking apart heavy atomic nuclei like uranium or plutonium into smaller fragments to release the binding energy stored within them"
    ],
    19: [
        "The procedure of removing spent fuel rod assemblies from the reactor core and placing them in cooling water pools after they finish generating power",
        "The practice of supplementing nuclear fuel pellets with essential vitamin and mineral additives to enhance the efficiency of the fission chain reaction",
        "The initial step of physically excavating uranium ore from underground or open-pit mine sites before it undergoes any chemical processing or refinement"
    ],
    20: [
        "A recreational swimming pool facility constructed at a nuclear power plant campus specifically for the physical fitness and relaxation of plant workers",
        "An aquaculture fish farming pond located adjacent to a nuclear facility that uses warm discharge water to accelerate commercial fish growth rates",
        "A natural freshwater lake situated near a nuclear power station that receives and dissipates waste thermal energy from the reactor steam condensing system"
    ],
    21: [
        "One nation made the objectively correct decision while the other nation made a clearly wrong choice about nuclear energy policy direction and investment",
        "Both Germany and France have completely phased out all nuclear electricity generation and transitioned entirely to renewable energy sources by now",
        "Nuclear energy technology presents absolutely identical safety risks, economic costs, and environmental consequences in every country regardless of context"
    ],
    23: [
        "There are absolutely no additional financial costs or obligations of any kind after the initial construction of a nuclear power plant is completed",
        "The only significant ongoing expense is the periodic purchase of processed uranium fuel assemblies needed to sustain the nuclear fission chain reaction",
        "Insurance premiums against potential nuclear accidents represent the sole meaningful operational cost beyond the initial construction capital expenditure"
    ],
    24: [
        "Small modular reactor technology has already been extensively deployed and commercially operated for multiple decades across dozens of countries worldwide",
        "Small modular reactors operate through entirely non-nuclear chemical energy conversion processes that require no fissile uranium or plutonium fuel material",
        "Small modular reactor designs have completely eliminated all radioactive waste production through advanced fuel recycling and neutron capture technology"
    ],
    25: [
        "All animal species are completely immune to ionizing radiation exposure and suffer absolutely no biological harm from living in contaminated environments",
        "All radioactive contamination from the 1986 Chernobyl disaster has completely dissipated and the exclusion zone is now safe for permanent human habitation",
        "Chronic exposure to elevated levels of ionizing radiation is actually beneficial for wildlife health and promotes increased reproduction and genetic fitness"
    ],
    26: [
        "The urgent practical necessity of immediately halting all commercial and recreational fishing activities throughout the entire Pacific Ocean basin",
        "A well-established scientific principle that radioactive contamination cannot physically travel through or be transported by ocean water currents",
        "Conclusive scientific evidence that all fish species harvested from anywhere in the Pacific Ocean are now permanently unsafe for human consumption"
    ],
    27: [
        "A widely accepted scientific finding that nuclear energy production generates significantly more carbon dioxide emissions per kilowatt-hour than coal plants",
        "Whether anthropogenic climate change is actually occurring or is simply a natural cyclical variation in global temperature patterns over geological timescales",
        "Whether commercially available photovoltaic solar panel systems can generate any measurable electrical output during nighttime hours without direct sunlight"
    ],
    28: [
        "A coincidental statistical correlation with no established causal connection between uranium mining activities and observed community health outcomes",
        "Definitive epidemiological proof that commercial uranium mining operations produce absolutely no adverse health effects in surrounding residential populations",
        "Clear evidence that all mineral extraction mining operations provide substantial direct economic benefits to every local community in the surrounding area"
    ],
    29: [
        "Nuclear power generating facilities never reach the end of their operational lifespan and therefore never require decommissioning or dismantlement procedures",
        "The complete process of decommissioning a retired nuclear power plant typically requires only a few working days and minimal specialized technical expertise",
        "Decommissioning retired nuclear facilities is completely free of cost and can be accomplished instantly with no ongoing waste management financial obligations"
    ],
    30: [
        "Only perform mathematical calculations of radioactive decay half-lives without connecting nuclear science concepts to broader energy policy considerations",
        "Simply describe the mechanical engineering principles of how nuclear fission reactors operate without analyzing environmental or societal trade-offs involved",
        "Only memorize the specific calendar dates and geographic locations of major nuclear accidents without analyzing their causes or long-term environmental impacts"
    ]
}

for q in data['quiz_questions']:
    qn = q['question_number']
    if qn in fixes:
        wrong_idx = 0
        for opt in q['options']:
            if not opt['is_correct']:
                opt['text'] = fixes[qn][wrong_idx]
                wrong_idx += 1

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Fixed {len(fixes)} questions in Lesson5.2_Quiz.json")
