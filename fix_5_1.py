import json

path = "C:/Users/Peter/pkang6689-pixel.github.io/content_data/EnvironmentalScienceLessons/Unit5/Lesson5.1_Quiz.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixes = {
    4: [
        "Using powerful underground laser arrays to vaporize rock formations and release pockets of trapped natural gas deposits",
        "Excavating deep underground tunnel networks to physically reach and extract gas from shale formations hundreds of meters below",
        "Deploying specialized bacterial cultures underground that chemically decompose rock structures and liberate stored natural gas"
    ],
    6: [
        "Significantly enhanced respiratory capacity and improved overall lung function from regular exposure to underground mine conditions",
        "Measurable improvements in cardiovascular health and physical endurance gained through the demanding physical work of coal extraction",
        "No documented or scientifically recognized negative health effects associated with prolonged occupational exposure to coal mining dust"
    ],
    7: [
        "Only a single petroleum-derived product, specifically automotive gasoline, with no other commercial or industrial applications whatsoever",
        "Exclusively industrial lubricants and mechanical greases, with petroleum having no role in fuel production or chemical manufacturing",
        "Solely residential and commercial heating oil, with petroleum playing no part in transportation fuels or synthetic material production"
    ],
    10: [
        "Requires massive amounts of energy to extract, causes extensive landscape destruction, and produces significantly more greenhouse gases than conventional oil production",
        "Exists only in remote Antarctic ice sheets where international treaties permanently prohibit any form of resource extraction activity",
        "Generates absolutely no air pollution, water contamination, or greenhouse gas emissions during any phase of its extraction and processing"
    ],
    11: [
        "Any substance that produces fire or heat energy when ignited, including modern biomass materials and manufactured synthetic combustibles",
        "A recently synthesized fuel product derived from currently living plant material through modern industrial biochemical processing methods",
        "Any mineral or organic substance extracted from underground geological formations regardless of its age or method of original formation"
    ],
    12: [
        "Naturally purified and filtered water that flows cleanly from abandoned mine exit tunnels without any chemical contamination present",
        "An advanced engineering technique specifically designed to improve downstream water quality in rivers and streams located near mining sites",
        "The standard industrial process of washing and cleaning raw coal with treated water before it enters a combustion furnace for burning"
    ],
    13: [
        "A greenhouse gas that has absolutely no measurable effect on atmospheric temperature or any influence on global climate patterns",
        "A solid mineral form of carbon that is physically mined from underground deposits and burned directly as a replacement for standard coal",
        "A chemical compound identical to carbon dioxide that possesses no special thermal properties or atmospheric warming characteristics"
    ],
    14: [
        "The practice of placing extracted coal into reinforced underground storage bunkers for long-term preservation and future industrial use",
        "A natural biological process where forests and vegetation absorb atmospheric carbon dioxide through photosynthesis and long-term growth",
        "The counterintuitive strategy of burning additional fossil fuels at higher temperatures to chemically trap and neutralize carbon molecules"
    ],
    16: [
        "A naturally occurring gaseous compound used exclusively for residential home heating systems with no other industrial or commercial purposes",
        "A solid crystalline mineral that is physically excavated from mountainous terrain through conventional open-pit or underground mining methods",
        "A sustainably produced renewable liquid fuel manufactured entirely from currently cultivated agricultural crop materials and plant biomass"
    ],
    17: [
        "The observable temperature increase that occurs inside an actual glass-walled agricultural greenhouse structure due to trapped solar radiation",
        "A significant atmospheric cooling phenomenon caused by the reflective properties of industrial air pollution particles blocking incoming sunlight",
        "The detrimental effect that stratospheric ozone layer depletion has on terrestrial plant growth rates and agricultural crop productivity levels"
    ],
    18: [
        "A government program that provides financial tax refunds and monetary rebates to individuals and corporations that increase fossil fuel consumption",
        "A comprehensive excise tax applied uniformly to all products that contain any amount of carbon atoms in their basic chemical molecular structure",
        "A specialized import duty assessed on carbon fiber composite materials used in aerospace and advanced manufacturing industrial applications"
    ],
    19: [
        "An offshore deepwater drilling technique used exclusively for extracting crude oil deposits from beneath the ocean floor sediment layers",
        "A specialized coastal excavation method restricted to mining mineral deposits found only along saltwater shoreline and tidal zone environments",
        "A deep underground vertical shaft mining approach that accesses mineral deposits located far below the surface without any surface disturbance"
    ],
    23: [
        "Coal combustion in Chinese power plants produces absolutely no measurable air pollution or negative public health impacts in urban populations",
        "Renewable energy sources are permanently and fundamentally more expensive than coal power generation in every region of China without exception",
        "China possesses no viable renewable energy resources of any kind, including solar, wind, hydroelectric, or geothermal energy potential"
    ],
    24: [
        "An immediate and permanent prohibition on all forms of offshore drilling activity in every ocean and coastal waterway around the entire world",
        "Commence drilling operations immediately without conducting any environmental review, risk assessment, or habitat impact evaluation beforehand",
        "Marine mammal populations including whales will experience absolutely no negative effects from nearby offshore drilling activities or operations"
    ],
    25: [
        "Only catastrophic large-scale natural gas leaks have any meaningful impact on climate change while smaller infrastructure leaks are insignificant",
        "Natural gas pipeline leaks produce absolutely no environmental consequences because methane dissipates harmlessly when released into the atmosphere",
        "Any methane gas that escapes from pipeline infrastructure is naturally and completely absorbed by surrounding soil microorganisms within minutes"
    ],
    27: [
        "Residential property values consistently increase in areas located near active natural gas extraction wells and hydraulic fracturing operations",
        "The economic benefits and environmental costs of hydraulic fracturing are distributed equally and fairly among all members of affected communities",
        "Any environmental concerns raised about hydraulic fracturing operations are always exaggerated and lack credible scientific supporting evidence"
    ],
    28: [
        "Entirely natural volcanic activity that periodically releases stored carbon dioxide from deep underground magma chambers into the upper atmosphere",
        "Fundamental shifts in global ocean circulation patterns that have redistributed dissolved carbon dioxide between deep and surface ocean waters",
        "A significant increase in terrestrial plant decomposition rates driven by warmer soil temperatures and elevated microbial metabolic activity levels"
    ],
    29: [
        "Tropical and subtropical island nations receive insufficient solar radiation levels to generate meaningful amounts of photovoltaic electricity",
        "Diesel fuel-powered electricity generation is always and permanently less expensive than solar energy in every geographic location without exception",
        "Photovoltaic solar energy conversion technology is fundamentally incompatible with island electrical grid systems and cannot function in maritime environments"
    ],
    30: [
        "Exclusively the retail consumer price of automotive gasoline and how fuel costs affect household transportation budgets and personal spending patterns",
        "Only the basic chemical equations of hydrocarbon combustion reactions without connecting those reactions to broader environmental or health consequences",
        "Solely the atmospheric air pollution impacts of fossil fuel burning without considering water contamination, habitat destruction, or health effects"
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

print(f"Fixed {len(fixes)} questions in Lesson5.1_Quiz.json")
