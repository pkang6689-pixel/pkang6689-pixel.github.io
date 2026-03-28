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

# FILE 1: Lesson1.8_Quiz.json - Geological Resources (Ores, Fossil Fuels)
print("Fixing Lesson1.8_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit1/Lesson1.8_Quiz.json", {
    3: [  # Coal formation begins with:
        "Compression of ancient marine shell deposits on the ocean floor",
        "Volcanic ash layers that slowly accumulate over millions of years",
        "Chemical precipitation of calcium carbonate in shallow warm seas"
    ],
    5: [  # Petroleum (oil) forms from:
        "Decomposition of ancient tree roots that penetrated deep underground and were chemically altered by magmatic heat over time",
        "Mineral-rich groundwater that slowly accumulates in porous sandstone formations and undergoes gradual chemical transformation",
        "Molten rock that cools slowly in deep underground chambers, trapping carbon compounds from the surrounding sedimentary layers"
    ],
    7: [  # Fossil fuels are considered non-renewable because they:
        "Can only be extracted using techniques that permanently destroy the surrounding geological formations and aquifers",
        "Undergo rapid chemical decomposition once brought to the surface, losing most of their stored energy during processing",
        "Exist in such deep and inaccessible geological layers that current extraction technology can only reach a tiny fraction"
    ],
    8: [  # An oil trap requires:
        "Continuous volcanic heat from nearby magma chambers at depth",
        "A deep oceanic trench where tectonic plates converge together",
        "A thick layer of metamorphic rock with high mineral concentration"
    ],
    10: [  # Sand and gravel are the most used non-metallic resources for:
        "Manufacturing semiconductors and microchips for electronic devices",
        "Producing agricultural fertilizers for large-scale commercial farming",
        "Generating thermal energy through combustion at industrial power plants"
    ],
    15: [  # What are rare earth elements?
        "A category of highly radioactive heavy elements found exclusively in uranium ore deposits, used only in nuclear power generation and specialized medical imaging equipment",
        "A set of noble gases found in trace amounts in Earth's atmosphere that are harvested through cryogenic air separation for industrial welding and specialized lighting applications",
        "A classification of precious gemstone minerals including diamonds, rubies, and sapphires that form only under extreme pressure conditions deep within Earth's upper mantle"
    ],
    23: [  # Global demand for lithium - environmental concern
        "Lithium processing facilities release significant concentrations of mercury vapor into the surrounding atmosphere, creating severe respiratory and neurological hazards for nearby communities",
        "Extracting lithium from underground brine deposits permanently destabilizes geological formations above, triggering frequent induced seismic events and surface subsidence across the mining region",
        "Lithium brine evaporation generates large volumes of toxic fluorine compounds that accumulate in enclosed highland valleys and cannot be safely neutralized with existing chemical treatment methods"
    ],
    24: [  # Pipeline through active faults - geological hazards
        "Sustained high-altitude winds that progressively erode exposed pipeline sections and accelerate metal fatigue, eventually causing stress fractures along welded joints",
        "Gradual soil acidification from prolonged mineral weathering processes that corrodes buried pipeline sections and weakens critical structural connections over decades",
        "Periodic flooding from seasonal snowmelt that submerges pipeline access points and significantly complicates routine maintenance, inspection, and emergency repair schedules"
    ],
    28: [  # Recycling aluminum - geological resource conservation
        "Recycled aluminum contains residual contaminants from consumer use that limit its structural applications to low-grade products, so primary mining of bauxite ore remains necessary for most industrial purposes",
        "Aluminum recycling mainly reduces municipal landfill volume rather than mining demand, because recycled metal loses significant mass during each reprocessing cycle and cannot fully substitute for newly extracted material",
        "The energy required to collect, transport, sort, and reprocess used aluminum cans across a large metropolitan area nearly equals the energy saved by avoiding primary smelting, resulting in minimal net benefit"
    ],
    30: [  # Geothermal energy vs fossil fuels
        "Geothermal energy is classified as non-renewable since underground heat reservoirs are permanently depleted by steam extraction, making geothermal plants functionally identical to fossil fuel facilities in their long-term resource consumption patterns",
        "Geothermal energy shares the same fundamental sustainability limitations as fossil fuels because both depend on finite underground resources that formed over geological timescales and cannot be replenished once they are fully extracted",
        "Geothermal power generation releases more total carbon dioxide per kilowatt-hour than natural gas combustion because drilling into volcanic formations liberates trapped ancient carbon from buried limestone deposits deep underground"
    ]
})

# FILE 2: Lesson1.9_Quiz.json - Case Studies in Natural Hazards
print("Fixing Lesson1.9_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit1/Lesson1.9_Quiz.json", {
    2: [  # Tohoku earthquake caused the most deaths through:
        "Widespread structural collapse of high-rise buildings in central Tokyo",
        "Massive landslides triggered along Japan's mountainous inland regions",
        "Fires ignited by ruptured natural gas lines that spread through dense urban areas"
    ],
    3: [  # Haiti's 2010 earthquake killed over 200,000 because:
        "The earthquake triggered a powerful tsunami that inundated the entire southern coastline and low-lying river valleys",
        "Multiple strong aftershocks of nearly equal magnitude struck the same area every few minutes over the following week",
        "The earthquake's hypocenter was located at an extreme depth of over 300 kilometers beneath the island's surface"
    ],
    4: [  # Vesuvius preserved Pompeii because:
        "Toxic volcanic gases created an airtight chemical seal over the entire city that halted all biological decomposition processes",
        "Slow-moving basaltic lava flows gradually encased the city's structures in dense volcanic rock over a period of several weeks",
        "A sudden coastal flood surge carried mineral-rich marine sediment inland and buried the city under meters of waterlogged deposits"
    ],
    9: [  # Japan's building codes saved lives because:
        "Every residential structure in Japan was constructed entirely underground, which shielded all occupants from damaging surface seismic waves",
        "Japanese buildings are uniformly constructed from lightweight bamboo and wood composites that flex and absorb seismic energy without fracturing",
        "All major buildings in Japan were relocated to stable bedrock foundation sites after the 1995 Kobe earthquake to avoid ground amplification effects"
    ],
    11: [  # What is a natural hazard?
        "A man-made environmental disaster resulting from industrial pollution, toxic chemical spills, or structural engineering failures that threatens nearby communities and ecosystems",
        "A theoretical risk category assessed by insurance companies based on statistical models that predict potential property damage in a specific geographic region over time",
        "A designated government exclusion zone where all construction is permanently prohibited because of historical weather patterns recorded during the previous century of observations"
    ],
    13: [  # What is vulnerability in the context of natural hazards?
        "The total economic cost of repairing damaged infrastructure and rebuilding affected communities after a natural disaster has already struck a populated region",
        "The total physical energy released by a geological event, measured using standardized instruments such as seismographs and tiltmeters at monitoring stations",
        "The statistical probability that a particular type of natural hazard event will occur within a specific geographic region during a defined time period"
    ],
    14: [  # What is a pyroclastic surge?
        "A powerful earthquake-generated seismic wave that radiates outward through oceanic crust from a submarine volcanic eruption at extremely high velocity",
        "A sustained increase in magma chamber pressure that causes the volcanic vent to emit continuous streams of highly fluid basaltic lava downslope",
        "A large-volume debris avalanche composed of massive boulders and fragmented volcanic rock that slides slowly downhill under gravitational force alone"
    ],
    16: [  # What does 'land-use planning' mean in the context of natural hazards?
        "The scientific process of predicting exactly when and where natural hazards will strike so that authorities can issue mandatory evacuation orders well in advance",
        "A government compensation program that reimburses property owners financially after natural disasters damage their buildings, regardless of where they originally chose to build",
        "The engineering practice of reinforcing all existing structures in a region to withstand the maximum possible intensity of any anticipated natural hazard event"
    ],
    17: [  # What is a seismic gap?
        "A physical crack or opening that forms in Earth's surface along a fault line immediately after a major earthquake releases stored tectonic strain energy from the crust",
        "The measurable difference in seismic wave arrival times between primary and secondary waves recorded at a single monitoring station after a significant seismic event",
        "A region deep within Earth's mantle where seismic waves dramatically slow down due to partial melting of rock material at the boundary between major tectonic plates"
    ],
    22: [  # Simeulue village survived 2004 tsunami - what does this demonstrate?
        "Advanced engineering of reinforced concrete sea walls constructed by the village provided complete physical protection against all incoming tsunami wave energy along the coast",
        "The island's unique coastal bathymetry and offshore coral reef system naturally refracted and dissipated the tsunami wave energy before it could reach the shoreline population areas",
        "International aid organizations had recently installed a satellite-linked electronic warning siren system in the village that activated automatically when the earthquake was first detected"
    ],
    23: [  # Christchurch earthquake - what does this reveal?
        "Modern building codes are specifically calibrated for earthquakes above magnitude 7.0, so the moderate 6.3 event fell outside their designed protection range, exposing a significant gap in structural engineering standards",
        "New Zealand had recently relaxed its earthquake building codes to reduce construction costs, and the older buildings in Christchurch's central business district had not been retrofitted to meet even the previous safety standards",
        "All earthquake damage in Christchurch resulted solely from widespread soil liquefaction caused by the region's unusually high water table, which is a geological hazard that cannot be mitigated through any building code provisions"
    ],
    24: [  # Lupines as pioneer species at Mt. St. Helens
        "Lupines develop extremely deep root systems that penetrate hardened volcanic rock and mechanically break it apart, creating loose gravel substrates that other plant species eventually colonize",
        "Lupines produce concentrated alkaloid compounds that chemically sterilize the volcanic soil and eliminate competing fungal species, creating a clean mineral seedbed for the establishment of larger plant species",
        "Lupines attract large herbivore populations whose nutrient-rich waste deposits across the barren landscape provide the primary source of organic matter that enables initial soil formation processes"
    ],
    26: [  # 1985 Nevado del Ruiz - why did warnings fail?
        "The lahars traveled at velocities exceeding 500 kilometers per hour down narrow river channels, making physical evacuation of the town fundamentally impossible even with several hours of advance warning from monitoring stations",
        "Armero was situated directly inside the volcanic summit caldera, so the town was completely destroyed within seconds of the eruption onset, long before any warning signal could possibly have been transmitted to residents",
        "The volcano monitoring instruments installed on the slopes malfunctioned during the eruption due to electromagnetic interference from intense pyroclastic activity, preventing scientists from confirming that lahars had actually formed"
    ],
    27: [  # Hurricane Katrina levee failure lessons
        "Catastrophic natural disasters like major hurricanes are entirely beyond the influence of human engineering, and all flood protection infrastructure will inevitably fail during extreme weather events regardless of design quality or maintenance",
        "Levee and flood wall systems function effectively only during minor to moderate storm events and provide no meaningful protection during major hurricanes, so all coastal areas below sea level should be permanently abandoned as residential zones",
        "Hurricane Katrina was an unprecedented storm whose strength could not have been anticipated by any meteorological methods, demonstrating that natural disasters of this magnitude are fundamentally unpredictable and entirely unpreventable"
    ],
    28: [  # Climate change increasing natural hazards - coastal city planning
        "A significant reduction in tectonic plate movement rates caused by rising global temperatures, which will steadily decrease earthquake frequency and volcanic activity along all major plate boundaries worldwide",
        "An increase in meteorite impact frequency as climate change progressively weakens Earth's protective magnetic field, allowing substantially more space debris to penetrate the atmosphere and reach the surface",
        "Stronger gravitational tidal forces resulting from melting polar ice redistributing Earth's crustal mass, which will amplify seismic activity and trigger more frequent volcanic eruptions along continental margins"
    ],
    29: [  # Japan vs Haiti economics comparison
        "Wealthier nations consistently experience both higher death tolls and greater economic losses from natural disasters because their densely populated urban centers and valuable infrastructure create compounding cascading impacts that far exceed those seen in developing nations",
        "The difference in outcomes between Japan and Haiti was determined entirely by earthquake magnitude rather than national preparedness, since Japan's earthquake released hundreds of times more energy and therefore inevitably caused proportionally greater economic damage to the country",
        "Natural disaster impacts are determined solely by geological factors such as fault proximity, depth, and magnitude, while economic development levels and infrastructure investment have no measurable effect on either casualty numbers or financial losses from major seismic events"
    ],
    30: [  # Monthly earthquake drills worthwhile?
        "Earthquake drills show diminishing effectiveness when practiced more than once per year, and the fifty-year absence of significant seismic activity strongly confirms that the local fault system has fully released its accumulated tectonic strain and no longer poses a meaningful threat to the area",
        "Monthly drills are unnecessary because modern seismological monitoring networks and advanced computer models can now reliably predict major earthquakes several days in advance with sufficient accuracy, giving schools ample time to organize orderly evacuations without requiring any prior practice",
        "Frequent earthquake drills are primarily a legal liability precaution for school administrators rather than a genuine life-safety measure, and the considerable time and resources devoted to monthly practice sessions would be far more effectively allocated toward structural reinforcement of the building"
    ]
})

# FILE 3: Lesson4.8_Quiz.json - Case Studies in Paleontology
print("Fixing Lesson4.8_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit4/Lesson4.8_Quiz.json", {
    6: [  # What are the Ediacaran fossils known for?
        "Preserving the earliest known terrestrial insect fossils that document the initial colonization of land by arthropod species before the Cambrian",
        "Recording the first mass extinction event in geological history, when nearly all early marine invertebrate species suddenly vanished from the record",
        "Containing the earliest vertebrate fossils, including primitive jawless fish with bony external armor plates that dominated shallow Precambrian seas"
    ],
    8: [  # Why is Ambulocetus important?
        "It provides key evidence that modern whales descended directly from ancient marine reptiles like plesiosaurs during the late Mesozoic Era",
        "It represents the oldest known cetacean fossil in the record, predating all other whale ancestors by over one hundred million years",
        "It demonstrates that overall whale body size has remained essentially constant for fifty million years, contradicting gradual evolutionary change"
    ],
    16: [  # What does 'in situ' mean when describing a fossil discovery?
        "The fossil has been chemically treated with preservative resins at the excavation site to prevent deterioration during transportation to the laboratory",
        "The fossil was discovered by a certified professional paleontologist rather than an amateur collector, ensuring that proper documentation protocols were followed",
        "The fossil has been dated using radiometric isotope techniques and assigned a precise numerical age within the internationally standardized geological time scale"
    ],
    21: [  # Preserved soft tissue in T. rex bone - why surprising?
        "The structures identified were actually inorganic mineral deposits that crystallized inside the bone pore spaces long after burial, closely mimicking the visual appearance of biological cells without having any actual organic origin",
        "All large dinosaur bones routinely contain preserved soft tissue because their massive physical size creates anaerobic internal conditions that naturally prevent any microbial decomposition from occurring over geological time periods",
        "Burial in volcanic ash deposits routinely preserves intact cellular structures in vertebrate fossils, so discovering soft tissue in a specimen from that particular depositional environment was entirely expected by researchers"
    ],
    22: [  # Why do Cambrian organisms look unlike anything alive today?
        "The unusual appearance of Burgess Shale fossils results from severe preservation artifacts that distorted the original body shapes of organisms, making normal Cambrian animals appear unfamiliar and alien to modern scientific observers",
        "Cambrian organisms were fundamentally identical to modern species in their basic anatomy, but the extreme geological age of the Burgess Shale makes accurate morphological identification impossible using current paleontological laboratory methods",
        "Environmental conditions during the Cambrian were so radically different from present-day Earth that all organisms developed temporary physiological adaptations that disappeared once global conditions normalized later in geological history"
    ],
    23: [  # Whale evolution sequence - addressing criticism
        "The apparent evolutionary sequence is an artifact of incomplete fossil sampling, since only a tiny fraction of all species that ever lived become preserved as fossils, making any proposed chronological arrangement essentially speculative and scientifically unreliable",
        "Each fossil species in the proposed whale sequence originated independently as a fully formed organism, and their shared anatomical similarities simply reflect common environmental selection pressures rather than actual descent from shared evolutionary ancestors",
        "Paleontologists rely solely on the external physical appearance of fossils to construct evolutionary sequences, and since skeletal features alone can be highly misleading, the proposed whale lineage remains just one of many equally plausible alternative interpretations"
    ],
    24: [  # Maiasaura bone bed - what can be inferred about behavior?
        "The concentration of fossils in a single rock layer resulted from a prolonged drought that forced many solitary animals to die independently at the same dwindling water source over a period of several thousand years",
        "The presence of multiple age groups together indicates a catastrophic predator attack that overwhelmed the herd, and the apparent nesting structures were actually burrows created by small mammals long after the dinosaurs had already died",
        "Regional tectonic activity gradually transported individual fossils from many widely separated locations into a single deposit through lateral fault movement, creating an artificial concentration that does not reflect any actual social behavior"
    ],
    25: [  # Coprolites with pollen and insect parts - what does it reveal?
        "The mixed biological contents of the coprolite resulted from post-burial groundwater contamination that carried pollen grains and insect fragments into the fossilized material long after the original organism had died and been buried",
        "Coprolite analysis can reveal only the organism's very last meal before death and cannot provide any broader ecosystem information, since digestive chemical processes destroy most identifiable biological material well before fossilization occurs",
        "Plant pollen found within the coprolite was introduced entirely by wind contamination after surface deposition rather than through actual feeding, since airborne pollen grains commonly settle on all exposed surfaces in open sedimentary environments"
    ],
    27: [  # Homo naledi in Rising Star Cave - surprising implication
        "Homo naledi possessed a remarkably advanced brain structure that made it the most cognitively sophisticated hominin species yet discovered and the most likely direct evolutionary ancestor of modern Homo sapiens",
        "The Rising Star Cave discovery confirmed that all known hominin species followed an identical evolutionary trajectory, progressing uniformly from small-bodied tree-dwellers to large-brained bipedal walkers across the African continent",
        "Detailed skeletal analysis of Homo naledi remains revealed that the species manufactured advanced composite stone tools and deliberately controlled fire, capabilities previously documented only in much later Homo erectus populations"
    ],
    28: [  # Tooth enamel isotope ratios - scientific basis
        "Fossil tooth enamel fully absorbs surrounding sediment minerals during the fossilization process, completely replacing the original chemical composition, so isotope measurements reflect only burial environment conditions rather than the living animal's actual diet",
        "Isotope analysis of ancient fossil teeth requires first extracting intact DNA molecules preserved within the crystalline enamel structure, and the resulting genetic sequence data reveals which specific plant and animal species the organism consumed regularly",
        "Fossil tooth chemistry is determined solely by the mineral composition of the enclosing rock matrix in which the specimen was buried, making isotopic analysis useful for identifying geological formations but not for reconstructing the original diet of the animal"
    ],
    29: [  # Homo floresiensis challenged what assumption?
        "That all known hominin species were physiologically incapable of surviving on isolated islands due to severely limited food resources and dangerously reduced genetic diversity from small population sizes",
        "That every member of the genus Homo originated exclusively on the African continent and never successfully migrated to the remote islands of Southeast Asia during the Pleistocene epoch",
        "That only anatomically modern Homo sapiens possessed the cognitive capacity required to systematically manufacture and regularly use shaped stone tools throughout the entire Pleistocene period"
    ],
    30: [  # CT scanning of dinosaur egg - how does modern tech enhance research?
        "CT scanning provides only surface-level images of fossils and cannot penetrate dense mineralized material, so paleontologists must still physically break open specimens for internal examination using traditional mechanical preparation techniques",
        "Modern imaging technology has largely replaced physical fieldwork in paleontology, since researchers can now reconstruct entire skeletons from minimal fragmentary remains using artificial intelligence algorithms without any excavation",
        "CT scanning produces substantially lower resolution images than traditional optical microscopy techniques and is used primarily for public museum display purposes rather than for rigorous scientific research on vertebrate fossil specimens"
    ]
})

print("Batch 5 complete!")
