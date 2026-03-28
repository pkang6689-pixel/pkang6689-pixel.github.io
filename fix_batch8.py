import json

def fix_file(filepath, fixes):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data["quiz_questions"]:
        qnum = q["question_number"]
        if qnum in fixes:
            new_wrongs = fixes[qnum]
            wrong_idx = 0
            for opt in q["options"]:
                if not opt["is_correct"]:
                    opt["text"] = new_wrongs[wrong_idx]
                    wrong_idx += 1
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f"  Fixed {len(fixes)} questions")

# FILE 1: Lesson10.1_Quiz.json - Review of Key Earth Science Concepts
print("Fixing Lesson10.1_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit10/Lesson10.1_Quiz.json", {
    12: [  # What is the asthenosphere?
        "The outermost gaseous layer of Earth's atmosphere extending hundreds of kilometers above the surface into near-space",
        "The thin biologically active layer of weathered rock and organic material covering Earth's continental land surfaces",
        "The dense solid metallic sphere at the very center of the Earth composed primarily of crystallized iron and nickel"
    ],
    13: [  # What is an aquifer?
        "A deep oceanic trench formed at a convergent plate boundary where one tectonic plate subducts beneath another",
        "An enclosed glass container designed for maintaining aquatic organisms in a controlled indoor laboratory environment",
        "An above-ground municipal water storage facility constructed from reinforced concrete or welded steel panels"
    ],
    14: [  # What does 'weathering' mean?
        "The large-scale horizontal movement of tectonic plates driven by convection currents circulating within Earth's mantle",
        "The explosive release of magma, volcanic gases, and fragmented rock from a volcanic vent during an eruption event",
        "The routine process of collecting atmospheric data and generating numerical forecasts of short-term weather conditions"
    ],
    18: [  # What does 'relative humidity' mean?
        "The specific temperature threshold at which liquid water transitions to a solid crystalline ice phase under standard atmospheric pressure",
        "The rate of molecular evaporation measured at the surface of an open body of water exposed to direct solar radiation",
        "The aggregate total mass of all water vapor molecules currently suspended throughout Earth's entire atmospheric column"
    ],
    19: [  # What is 'isostasy'?
        "The precise measurement of barometric atmospheric pressure variations recorded at a standardized ground-level weather monitoring station",
        "The comprehensive scientific study of earthquake phenomena including seismic wave propagation, fault mechanics, and ground motion analysis",
        "The calculated velocity at which individual tectonic plates translate horizontally across Earth's surface relative to a fixed reference frame"
    ],
    21: [  # Road cut layers - depositional environment
        "All three sedimentary rock layers precipitated simultaneously from a single large-scale chemical event affecting the entire basin",
        "The entire sequence formed exclusively through successive volcanic ash fall deposits from three closely spaced eruption episodes",
        "The layered sequence demonstrates conclusively that the region has been a continuously arid desert environment throughout its geological history"
    ],
    23: [  # Meandering river evolution
        "Faster water on the outer bank erodes sediment while slower water on the inner bank deposits material, so bends migrate outward and grow more pronounced",
        "All natural river channels maintain perfectly straight courses unless they encounter immovable bedrock obstacles blocking the flow path",
        "The gravitational force acting on flowing water affects only one lateral side of the channel, producing asymmetric erosion in a single direction"
    ],
    24: [  # Weather station records cold front passage
        "A mild onshore sea breeze circulation pattern developing along the coastline during the afternoon heating period",
        "An extended period of extreme high temperatures caused by a persistent upper-atmospheric high pressure ridge blocking cooler airflow",
        "A stationary frontal boundary with no significant changes in temperature, wind direction, or precipitation patterns at the surface"
    ],
    25: [  # Iridium layer and mass extinction
        "Non-avian dinosaur lineages gradually evolved through natural selection into the earliest placental mammal species over millions of years",
        "The iridium anomaly originated entirely from an extended period of unusually intense volcanic eruptions that had no effect on living organisms",
        "The geological and fossil evidence preserved at this particular stratigraphic boundary is too incomplete and unreliable for scientific interpretation"
    ],
    26: [  # Beach erosion from jetty construction
        "The sand grains composing the beach were gradually vaporized by persistent high surface temperatures during summer heatwave conditions",
        "The jetty structure has no measurable hydrodynamic effect on sediment transport processes along adjacent sections of the coastline",
        "Global sea levels have declined substantially over the past decade, exposing additional offshore sand deposits along this coastline"
    ],
    29: [  # Floodplain enrichment
        "Flooding events permanently destroy all existing soil fertility by stripping away the accumulated organic matter and mineral nutrients",
        "Local farmers deliberately spread the nutrient-rich sediment across their fields by hand before each anticipated seasonal flood event",
        "Strong tidal surges carried nutrient-rich marine sediment inland from the ocean and deposited it across the river valley's agricultural fields"
    ],
    30: [  # Glacier retreat and treeline advance
        "The glacier physically relocated to a different mountain range in the region due to shifting prevailing wind patterns over the decades",
        "Regional tectonic uplift of the mountain raised its summit elevation, which moved the existing glacier higher relative to the surrounding terrain",
        "Both topographic maps contain systematic surveying errors that make direct comparison between different time periods scientifically unreliable"
    ]
})

# FILE 2: Lesson10.2_Quiz.json - AP-Style Practice Problems
print("Fixing Lesson10.2_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit10/Lesson10.2_Quiz.json", {
    9: [  # Best evidence for continental drift
        "All continents on Earth currently experience identical climate and weather patterns regardless of their geographic latitude or position",
        "Ocean water maintains a uniform temperature at all depths and latitudes throughout the entire global marine basin system",
        "Earthquake epicenters occur exclusively along continental margins and are never detected in plate interior or oceanic regions"
    ],
    15: [  # Specific heat capacity and climate
        "The characteristic visible color that a substance emits when heated to incandescence in a laboratory furnace apparatus",
        "The absolute maximum temperature that any substance can theoretically reach before undergoing irreversible thermal decomposition",
        "The velocity at which thermal energy propagates through a solid material via molecular conduction between adjacent particles"
    ],
    17: [  # Milankovitch cycles
        "The regular seasonal migration patterns of large bird populations that traverse continental distances between breeding and wintering grounds",
        "The daily alternation between daylight and darkness caused by Earth's rotation on its axis once every twenty-four hours",
        "The predictable monthly oscillations in ocean tidal height caused by the gravitational interaction between the Moon and Earth"
    ],
    20: [  # Adiabatic cooling
        "The reduction in temperature that occurs when a material comes into direct physical contact with a mass of ice or frozen surface",
        "The artificial lowering of temperature achieved through mechanical refrigeration systems that compress and expand chemical coolants",
        "The gradual decrease in temperature that occurs when erupted lava flows downhill and loses thermal energy to the surrounding air"
    ],
    21: [  # Marine fossils at 4000m elevation
        "The fossil organisms were placed at that high-elevation location deliberately by human researchers as part of an experimental study",
        "The marine organisms physically migrated up the mountainside under their own power during their lifetime and died at the summit",
        "Global sea levels were over 4,000 meters higher than present during that geological period, submerging all current continental landmasses"
    ],
    23: [  # Ice core CO2-temperature lag interpretation
        "The ice core analytical data contains fundamental measurement errors that make all paleoclimate interpretations scientifically unreliable",
        "Atmospheric carbon dioxide concentrations always drive temperature changes instantaneously with zero time lag in the geological record",
        "The time lag proves conclusively that carbon dioxide has no causal effect on temperature and plays no role in the climate system"
    ],
    26: [  # Radiometric + fossil dating complementary
        "The radiometric zircon age directly contradicts the biostratigraphic age range established by the microfossils, proving one dating method is fundamentally flawed",
        "The volcanic ash layer must have been deposited at the wrong stratigraphic position through post-depositional bioturbation or tectonic disruption of the sediment sequence",
        "Only radiometric isotope dating provides scientifically valid age information; microfossil biostratigraphy cannot constrain the timing of geological events in any meaningful way"
    ],
    27: [  # Venus hotter than Mercury due to greenhouse
        "Venus is actually positioned closer to the Sun than Mercury in its orbital path through the inner solar system",
        "Mercury's surface reflects a greater proportion of incoming solar radiation than Venus, keeping Mercury significantly cooler",
        "Venus generates substantial quantities of internal heat through active nuclear fusion reactions occurring deep within its metallic core"
    ],
    28: [  # Stream table aquifer-aquitard model
        "Clay layers are always positioned stratigraphically above sand layers in every natural geological depositional environment on Earth",
        "Water percolates downward through all subsurface materials at identical infiltration rates regardless of grain size or mineral composition",
        "All geological substrate types exhibit exactly equal permeability values and transmit groundwater at the same volumetric flow rate"
    ],
    29: [  # Paleomagnetic stripes evidence for seafloor spreading
        "Dissolved salts and mineral ions in circulating ocean water gradually magnetize the exposed basaltic rocks on the shallow seafloor surface",
        "The ocean floor is actively subsiding and sinking toward the mantle at the central axis of each mid-ocean ridge spreading center",
        "Earth's magnetic field exists exclusively within the oceanic lithosphere and does not extend across continental landmasses or the atmosphere"
    ],
    30: [  # Same latitude, different climates
        "Both cities located at identical latitudes should theoretically experience identical climate conditions throughout the entire calendar year",
        "The humid city must be situated at a substantially higher elevation on a continental plateau, which increases precipitation through orographic lifting",
        "Geographic latitude is the sole factor that determines climate at any location on Earth, and no other variables have measurable influence"
    ]
})

# FILE 3: Lesson10.3_Quiz.json - Case Studies in AP Earth Science
print("Fixing Lesson10.3_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit10/Lesson10.3_Quiz.json", {
    1: [  # Eyjafjallajokull - what hazard caused flight cancellations?
        "Seismic ground shaking from the eruption that physically damaged runway pavement at airports across northern Europe",
        "Toxic sulfur dioxide gas emissions that accumulated at ground level across European cities and transportation hubs",
        "Fast-moving basaltic lava flows from the eruption that reached and destroyed airport infrastructure in Iceland"
    ],
    2: [  # 2004 tsunami mechanism
        "Multiple submarine volcanic eruptions along the entire length of the Indian Ocean spreading ridge occurred simultaneously with the earthquake",
        "Sustained tropical cyclone winds across the open Indian Ocean generated the massive wave energy that struck coastal communities",
        "The earthquake originated entirely beneath continental landmass and generated no direct interaction with the overlying ocean water"
    ],
    3: [  # Dust Bowl causes
        "A major continental glacial advance moved southward across the Great Plains region during the 1930s, burying farmland under thick ice",
        "Catastrophic riverine flooding from spring snowmelt completely washed away all topsoil from agricultural fields across the central Plains",
        "A series of explosive volcanic eruptions deposited thick ash layers across the Great Plains while ocean acidification damaged crop root systems"
    ],
    4: [  # Chesapeake Bay eutrophication cause
        "Offshore crude oil drilling operations conducted within the bay's navigable waters leaked petroleum into the marine environment",
        "Construction of large hydroelectric dams across the bay's major tributary rivers blocked natural water circulation patterns",
        "Commercial overfishing operations systematically removed excessive numbers of marine organisms from the bay's tidal food web"
    ],
    6: [  # Mt. St. Helens precursor signals
        "A significant and sustained reduction in the normal seasonal snowfall accumulation observed on the mountain's upper slopes",
        "Measurable fluctuations in the sea surface temperature of the nearby Pacific coastal waters detected by monitoring buoys",
        "A sudden and pronounced decrease in local earthquake activity below the volcano compared to the previous baseline readings"
    ],
    12: [  # What does 'liquefaction' mean?
        "The transformation of glacial ice into liquid meltwater triggered by the intense heat generated during nearby volcanic eruptions",
        "The phase transition of solid crystalline rock into flowing molten magma caused by the mechanical energy released during earthquake ground shaking",
        "The downstream movement of erupted volcanic lava as it flows along river channels and topographic low points on the volcanic slope"
    ],
    17: [  # What is a 'caldera'?
        "A small secondary parasitic vent located on the outer flank of a larger stratovolcano that intermittently releases steam and gas",
        "A specific classification of volcanic rock formation composed entirely of welded pyroclastic fragments and consolidated volcanic ash",
        "The prominent steep-sided conical peak that forms at the summit of a composite volcano through successive layers of lava and ash"
    ],
    18: [  # What does 'bioaccumulation' mean?
        "The systematic collection and cataloging of diverse living organisms within a designated biological nature reserve or conservation area",
        "The controlled cultivation and exponential growth of bacterial colonies in a nutrient-rich agar medium within a sterile laboratory setting",
        "The progressive accumulation of decomposing biological waste materials in engineered sanitary landfills over extended periods of operation"
    ],
    21: [  # New Orleans Katrina - non-meteorological factors
        "The hurricane's extreme wind speed and unprecedented rainfall intensity were the only factors responsible for the catastrophic urban flooding",
        "A powerful tectonic earthquake struck simultaneously beneath the city during the hurricane, fracturing underground infrastructure and sewer systems",
        "The Mississippi River spontaneously changed its primary channel course during the peak of the storm, redirecting floodwaters directly into the city"
    ],
    22: [  # Lake Nyos CO2 release mechanism
        "A full-scale volcanic eruption from the magma chamber directly beneath the lake ejected molten lava and pyroclastic material to the surface",
        "Extensive forest fires burning on the hillsides surrounding the lake generated massive quantities of carbon dioxide smoke that settled into the basin",
        "Ongoing chemical oxidation reactions between dissolved mineral compounds in the lake water and atmospheric gases at the surface produced the CO2"
    ],
    23: [  # Mt. Pinatubo cooling mechanism
        "The eruption released large quantities of ozone-depleting chlorofluorocarbon compounds that destroyed stratospheric ozone and cooled the global climate",
        "Volcanic ash particles settled preferentially onto polar ice caps and glaciers, increasing their surface albedo and reflecting more incoming solar radiation",
        "The dense volcanic ash cloud completely blocked all incoming solar radiation from reaching Earth's surface for a continuous period of approximately two years"
    ],
    24: [  # Dead Sea shrinking - Earth system explanation
        "Anthropogenic climate change and rising global temperatures are the sole and exclusive factor responsible for the accelerated shrinkage of the Dead Sea",
        "The Dead Sea naturally undergoes periodic cycles of evaporation and refilling over geological timescales, and the current decline will reverse on its own",
        "A newly formed underground drainage channel is carrying Dead Sea water through subsurface limestone conduits directly into the adjacent Mediterranean Sea basin"
    ],
    26: [  # Yellowstone 'overdue' claim evaluation
        "Three eruptions in 2.1 million years provides insufficient statistical data to establish any meaningful pattern or reliable estimate of future eruption recurrence intervals",
        "The Yellowstone volcanic system is permanently extinct and geologically incapable of producing any further eruptions regardless of future geological conditions",
        "The news article's characterization is scientifically accurate because the eruption is imminent, certain, and should be expected within the next few decades"
    ],
    27: [  # Salton Sea - interconnected Earth systems
        "This environmental situation involves exclusively geological processes with no human dimension, policy implications, or connections to public health concerns",
        "The problem is limited entirely to atmospheric air quality issues and has no meaningful connection to hydrological water management or biological systems",
        "Only hydrological water cycle processes are involved in this environmental case, with no significant interactions with geological, atmospheric, or biological systems"
    ],
    29: [  # Kilauea Leilani Estates - geoscience + policy analysis
        "Volcanic hazard maps produced by geological survey agencies are inherently unreliable and should never be incorporated into municipal land-use planning decisions",
        "The 2018 eruptive phase at Kilauea was completely unpredictable by any scientific monitoring method, and no preventive measures could have reduced the property damage",
        "The government should implement a comprehensive ban on all residential, commercial, and agricultural construction across the entirety of the Big Island of Hawaii"
    ],
    30: [  # Thwaites Glacier vulnerability
        "Thwaites is composed primarily of compacted snow and firn rather than consolidated glacial ice, making it structurally weaker than other Antarctic glaciers",
        "Thwaites is the smallest and least voluminous glacier on the entire Antarctic continent and therefore contributes negligibly to potential future sea-level change",
        "Thwaites Glacier is situated at a near-equatorial latitude where ambient air temperatures are consistently warmer than at the Antarctic polar regions"
    ]
})

print("Batch 8 complete!")
