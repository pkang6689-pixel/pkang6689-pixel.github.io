#!/usr/bin/env python3
"""Add 13 more quiz questions to each Earth Science lesson (7→20)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "earth_science_lessons.json")

def make_q(qt, opts, exp):
    options = []
    for o in opts:
        correct = o.startswith("*")
        options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
    return {"question_number": 0, "question_text": qt, "attempted": 2,
            "data_i18n": None, "options": options, "explanation": exp}

# ── Extra questions per lesson (13 each) ──
EXTRA = {}

# U1 L1.1 Earth's Layers
EXTRA["u1_l1.1"] = [
    ("The thinnest layer of the Earth is the:",["Mantle","Outer core","*Crust","Inner core"],"Crust is 5-70 km thick."),
    ("Oceanic crust is primarily composed of:",["Granite","Sandstone","*Basalt","Limestone"],"Dense basaltic rock."),
    ("Continental crust is primarily composed of:",["Basalt","Obsidian","*Granite","Marble"],"Less dense granitic rock."),
    ("The asthenosphere is important because it:",["Is the densest layer","Is solid iron","*Allows tectonic plates to move over it (partially molten, ductile)","Contains fossils"],"Plate movement."),
    ("The Moho discontinuity marks the boundary between the:",["Mantle and core","*Crust and mantle","Inner and outer core","Lithosphere and asthenosphere"],"Mohorovičić discontinuity."),
    ("Earth's magnetic field is generated primarily by:",["The crust","The mantle","*Convection currents in the liquid outer core","The inner core alone"],"Geodynamo."),
    ("The inner core is solid despite extreme heat because:",["It's made of gas","It's cold","*The immense pressure keeps iron and nickel in a solid state","It's hollow"],"Pressure effect."),
    ("Seismic waves help us understand Earth's interior because:",["They're visible","*Their speed and direction change when passing through layers of different density and composition","They only travel on the surface","They stop at the crust"],"Seismology."),
    ("P-waves differ from S-waves in that P-waves:",["Travel slower","Cannot travel through solids","*Can travel through both solids and liquids","Only travel through liquids"],"Wave properties."),
    ("The shadow zone for S-waves proved the outer core is:",["Solid","A vacuum","*Liquid (S-waves cannot travel through liquids)","Gas"],"Liquid outer core evidence."),
    ("The mantle makes up approximately what percentage of Earth's volume?",["10%","50%","*84%","99%"],"Largest layer by volume."),
    ("The lithosphere includes:",["Only the crust","Only the upper mantle","*The crust AND the rigid upper mantle","The entire mantle"],"Tectonic definition."),
    ("Temperature increases with depth at a rate called the:",["Pressure gradient","Density curve","*Geothermal gradient","Seismic velocity"],"~25-30°C per km in crust."),
]

# U1 L1.2 Mineral Identification
EXTRA["u1_l1.2"] = [
    ("A mineral must be all of the following EXCEPT:",["Naturally occurring","Inorganic","*Man-made","Crystalline solid"],"Definition."),
    ("Mohs hardness scale ranges from:",["0 to 5","1 to 5","*1 to 10","0 to 100"],"1 (talc) to 10 (diamond)."),
    ("A mineral that breaks along flat, smooth planes exhibits:",["Fracture","Luster","*Cleavage","Streak"],"Cleavage planes."),
    ("The color of a mineral's powder on a porcelain plate is called:",["Luster","Hardness","*Streak","Cleavage"],"Streak test."),
    ("The most unreliable physical property for mineral identification is:",["Hardness","Streak","*Color (many minerals share colors; impurities change color)","Crystal form"],"Color is misleading."),
    ("Quartz has a hardness of ___ on Mohs scale.",["2","5","*7","10"],"Common reference mineral."),
    ("A mineral that breaks with rough, irregular surfaces shows:",["Cleavage","Luster","*Fracture","Streak"],"No flat planes."),
    ("Luster describes a mineral's:",["Color","Hardness","*The way it reflects light (metallic, glassy, earthy, etc.)","Weight"],"Light interaction."),
    ("Specific gravity compares a mineral's density to:",["Air","Iron","*Water","Diamond"],"Density ratio."),
    ("Halite (table salt) can be identified by its:",["Hardness","Luster only","*Cubic crystal shape and salty taste","Color alone"],"Distinctive properties."),
    ("Talc is the softest mineral (hardness 1), meaning it can be scratched by:",["Nothing","*A fingernail (hardness ~2.5)","Only diamond","Only quartz"],"Softest mineral."),
    ("Magnetite is unique because it is:",["The hardest mineral","Transparent","*Naturally magnetic","Always blue"],"Magnetic mineral."),
    ("The silicate mineral group is the most abundant because:",["It's the prettiest","*Silicon and oxygen are the two most abundant elements in Earth's crust","It's the hardest","It's the rarest"],"Most common mineral group."),
]

# U1 L1.3 Types of Rocks
EXTRA["u1_l1.3"] = [
    ("Igneous rocks form from:",["Compaction of sediment","Heat and pressure","*Cooling and solidification of magma or lava","Evaporation"],"Molten rock origin."),
    ("Intrusive igneous rocks cool _____ and have _____ crystals.",["Quickly, large","Quickly, small","*Slowly (underground), large","Slowly, no"],"Slow cooling = large crystals."),
    ("Granite is an example of a(n) _____ igneous rock.",["Extrusive","Sedimentary","*Intrusive","Metamorphic"],"Cooled underground."),
    ("Basalt is an example of a(n) _____ igneous rock.",["Intrusive","Sedimentary","*Extrusive","Metamorphic"],"Cooled on surface."),
    ("Sedimentary rocks form by:",["Melting","Volcanic eruption","*Compaction and cementation of sediments over time","Cooling of magma"],"Layered deposits."),
    ("Fossils are most commonly found in _____ rocks.",["Igneous","Metamorphic","*Sedimentary","All equally"],"Preserved in layers."),
    ("Metamorphic rocks form when existing rocks are changed by:",["Melting completely","Erosion","*Heat and/or pressure (without fully melting)","Deposition"],"Changed form."),
    ("Marble is a metamorphic rock that forms from:",["Granite","Sandstone","*Limestone","Basalt"],"CaCO₃ recrystallized."),
    ("Slate forms from the metamorphism of:",["Sandstone","Granite","*Shale","Basalt"],"Fine-grained metamorphic."),
    ("Conglomerate is a sedimentary rock containing:",["Only sand","Only clay","*Rounded pebbles and gravel cemented together","Volcanic glass"],"Clastic rock."),
    ("Foliation in metamorphic rocks refers to:",["Color change","Melting","*Alignment of minerals into parallel bands or layers due to pressure","Fossil formation"],"Layered texture."),
    ("Obsidian forms when lava cools:",["Slowly underground","In water only","*Very rapidly, forming volcanic glass with no crystals","Under high pressure"],"Rapid cooling."),
    ("Pumice is unique because it:",["Is the hardest rock","Is always black","*Is so porous (full of gas bubbles) that it can float on water","Forms underground"],"Vesicular texture."),
]

# U1 L1.4 The Rock Cycle
EXTRA["u1_l1.4"] = [
    ("The rock cycle shows that rocks are:",["Permanent and unchanging","*Constantly being transformed from one type to another over time","Only formed once","Destroyed permanently"],"Continuous process."),
    ("Any rock type can become any other rock type through the rock cycle. This means:",["Rocks are random","*All three rock types are interconnected — igneous can become sedimentary or metamorphic, and vice versa","Only igneous can change","Only sedimentary can change"],"All conversions possible."),
    ("Weathering and erosion convert any rock into:",["Magma","Metamorphic rock","*Sediments (which may become sedimentary rock)","Igneous rock directly"],"First step to sedimentary."),
    ("Melting of any rock produces:",["Sediment","Metamorphic rock","*Magma (which may cool to form igneous rock)","Fossils"],"Return to molten state."),
    ("Heat and pressure (without melting) transform any rock into:",["Sedimentary rock","Igneous rock","*Metamorphic rock","Magma"],"Metamorphism."),
    ("The rock cycle is driven primarily by:",["Wind alone","*Earth's internal heat (plate tectonics, convection) and external energy from the sun (weathering, erosion)","Gravity alone","Human activity"],"Two energy sources."),
    ("Uplift in the rock cycle refers to:",["Rocks sinking","*Rocks being pushed to the surface by tectonic forces, exposing them to weathering","Rocks melting","Rocks compacting"],"Tectonic exposure."),
    ("Lithification is the process of:",["Melting rocks","Weathering rocks","*Turning loose sediments into solid sedimentary rock through compaction and cementation","Changing crystal structure"],"Sediment → rock."),
    ("A sedimentary rock can become igneous if it:",["Is weathered","Is compressed","*Is subducted and melted, then the magma cools and solidifies","Is polished"],"Requires melting."),
    ("The fastest part of the rock cycle is typically:",["Metamorphism","Magma cooling underground","*Volcanic eruption and lava cooling on the surface","Lithification"],"Quick cooling."),
    ("The slowest process in the rock cycle can take:",["Days","Years","*Millions to billions of years (e.g., deep burial metamorphism or slow erosion)","Seconds"],"Geologic time."),
    ("Subduction zones are important in the rock cycle because they:",["Only create mountains","*Pull crustal rock back into the mantle where it can be recycled through melting","Only cause earthquakes","Only form fossils"],"Recycling at boundaries."),
    ("Humans interact with the rock cycle by:",["Not at all","*Mining, quarrying, and accelerating erosion — but these are tiny compared to natural geologic processes","Controlling plate tectonics","Stopping volcanism"],"Human scale vs geologic."),
]

# U1 L1.5 Soil Formation
EXTRA["u1_l1.5"] = [
    ("Soil is formed from the weathering of:",["Only sand","Only clay","*Parent rock (bedrock) combined with organic matter, water, and air","Only minerals"],"Soil origins."),
    ("The O horizon (topsoil surface) is rich in:",["Pure rock","Calcium","*Organic matter (humus — decomposed plant and animal material)","Iron"],"Organic layer."),
    ("The A horizon is commonly called:",["Subsoil","Bedrock","*Topsoil","Parent rock"],"Where most roots grow."),
    ("The B horizon (subsoil) accumulates minerals through:",["Erosion","Volcanic activity","*Leaching from upper layers (illuviation — minerals wash down and deposit here)","Fossil formation"],"Mineral accumulation."),
    ("The C horizon consists of:",["Rich topsoil","Organic matter","*Partially weathered parent rock (broken bedrock fragments)","Pure humus"],"Transition to bedrock."),
    ("Factors affecting soil formation include:",["Only climate","Only time","*Climate, organisms, relief/topography, parent material, and time (CLORPT)","Only parent rock"],"Five soil factors."),
    ("Sandy soil drains _____ and retains _____ water than clay.",["Slower, more","*Faster, less","The same","Slower, less"],"Particle size effect."),
    ("Clay soil has _____ particles and retains _____ water.",["Large, little","*Very small, a lot (but can become waterlogged)","Medium, medium","Large, a lot"],"Fine particles."),
    ("Loam is ideal for agriculture because it:",["Is pure sand","Is pure clay","*Is a balanced mixture of sand, silt, and clay — good drainage AND moisture retention","Has no organic matter"],"Best agricultural soil."),
    ("Humus improves soil by:",["Making it harder","Adding salt","*Providing nutrients, improving water retention, and creating good structure for root growth","Removing all minerals"],"Organic benefit."),
    ("Soil erosion is accelerated by:",["Dense forests","Grass cover","*Deforestation, overgrazing, and poor farming practices (removing vegetation exposes soil)","Mulching"],"Human-caused erosion."),
    ("It takes approximately _____ to form 1 inch of topsoil.",["1 year","10 years","*500-1,000+ years","1 million years"],"Very slow process."),
    ("Permafrost is:",["Desert soil","Tropical soil","*Permanently frozen soil found in arctic and subarctic regions","Volcanic soil"],"Frozen ground."),
]

# U2 L2.1 Continental Drift
EXTRA["u2_l2.1"] = [
    ("Alfred Wegener proposed continental drift in:",["1850","*1912","1950","2000"],"Early 20th century."),
    ("Wegener's supercontinent was called:",["Gondwana","Laurasia","*Pangaea","Rodinia"],"All lands together."),
    ("Evidence for continental drift includes matching _____ on different continents.",["Weather patterns","*Fossils (e.g., Mesosaurus found in both South America and Africa)","Modern animals","Current ocean temperatures"],"Paleontological evidence."),
    ("Glossopteris fern fossils found on multiple southern continents suggest:",["Wind carried seeds across oceans","*These continents were once connected (too heavy for wind/water dispersal across oceans)","Identical evolution occurred separately","Humans planted them"],"Plant fossil evidence."),
    ("Matching rock formations and mountain ranges on separated continents support:",["Erosion theory","*Continental drift (e.g., Appalachians match Caledonian Mountains in Scotland)","Volcanic theory","Ocean current theory"],"Geological evidence."),
    ("Climate evidence for drift includes glacial scratches in _____ that is now near the equator.",["North America","*Africa and India","Europe","Australia only"],"Paleoclimate evidence."),
    ("Wegener's theory was initially rejected mainly because he couldn't explain:",["What Pangaea was","Where continents are now","*The mechanism — what FORCE could move continents through oceanic crust","Where fossils are"],"Missing mechanism."),
    ("The puzzle-like fit of _____ coastlines was early visual evidence for drift.",["Europe and Asia","North America and Europe","*South America and Africa","Australia and Antarctica"],"Jigsaw fit."),
    ("Continental drift was eventually confirmed by discovery of:",["New fossils","*Seafloor spreading (Hess, 1960s) — providing the missing mechanism","New continents","Deeper oceans"],"Mechanism found."),
    ("Coal deposits in Antarctica indicate it once had a:",["Desert climate","*Warm, swampy climate (near the equator) capable of supporting lush vegetation","Permanent ice cap","No vegetation"],"Paleoclimate."),
    ("Mesosaurus was a freshwater reptile, which is significant because:",["It could swim oceans","*A freshwater animal could NOT cross salt water oceans — the continents must have been connected","It was very large","It lived in all climates"],"Biogeographic evidence."),
    ("Pangaea began breaking apart approximately _____ million years ago.",["50","100","*200","500"],"Mesozoic breakup."),
    ("Modern GPS measurements confirm continents move at about:",["1 meter/year","*2-10 centimeters/year","1 kilometer/year","They don't move"],"Measurable drift."),
]

# U2 L2.2 Seafloor Spreading
EXTRA["u2_l2.2"] = [
    ("Harry Hess proposed seafloor spreading in the:",["1920s","1940s","*1960s","1980s"],"Mid-20th century."),
    ("At mid-ocean ridges, new oceanic crust is created by:",["Erosion","Deposition","*Magma rising from the mantle and solidifying as it reaches the seafloor","Glaciers"],"New crust formation."),
    ("The Mid-Atlantic Ridge is an example of a:",["Convergent boundary","Transform boundary","*Divergent boundary (plates moving apart, new crust forming)","Subduction zone"],"Spreading center."),
    ("Magnetic stripes on the ocean floor show:",["Random patterns","*Symmetrical patterns of normal and reversed polarity on either side of ridges (evidence of spreading)","No pattern","Only one polarity"],"Paleomagnetic evidence."),
    ("Magnetic reversals recorded in ocean floor rocks prove that:",["Earth's field is constant","*Earth's magnetic field flips periodically AND new crust forms symmetrically at ridges","Rocks are magnetic randomly","The ocean is magnetic"],"Double evidence."),
    ("The age of oceanic crust _____ with distance from the mid-ocean ridge.",["Decreases","Stays the same","*Increases (youngest at ridge, oldest near continents)","Is random"],"Age pattern."),
    ("The oldest oceanic crust is approximately _____ million years old.",["50","100","*200 (much younger than oldest continental crust at 4+ billion years)","1,000"],"Relatively young."),
    ("Oceanic crust is constantly being recycled because:",["It evaporates","*Old crust is subducted back into the mantle at trenches while new crust forms at ridges","It dissolves","It floats away"],"Recycling process."),
    ("Sediment thickness on the ocean floor _____ with distance from the ridge.",["Decreases","Stays the same","*Increases (more time for sediment to accumulate on older crust)","Is zero everywhere"],"Sediment evidence."),
    ("Sonar mapping of the ocean floor revealed:",["A flat surface","*An extensive mountain range (mid-ocean ridge system) — the longest mountain range on Earth","Only trenches","Nothing useful"],"Topographic discovery."),
    ("Convection currents in the mantle are thought to:",["Cool the surface","*Drive plate movement by circulating hot mantle material (rising at ridges, sinking at trenches)","Create fossils","Only cause earthquakes"],"Driving mechanism."),
    ("The rate of seafloor spreading is typically:",["1 mm/year","*2-10 cm/year (similar to the rate your fingernails grow)","1 m/year","1 km/year"],"Slow but measured."),
    ("Iceland sits directly on the Mid-Atlantic Ridge, which is why it has:",["No geological activity","*Frequent volcanic eruptions and geothermal activity (hot springs, geysers)","Only earthquakes","Glaciers only"],"Ridge volcanism."),
]

# U2 L2.3 Plate Boundaries
EXTRA["u2_l2.3"] = [
    ("At convergent boundaries, plates:",["Move apart","Slide past each other","*Move toward each other (collision or subduction)","Don't move"],"Collision zones."),
    ("At divergent boundaries, plates:",["Collide","*Move apart, allowing magma to rise and form new crust","Slide past each other","Subduct"],"Spreading zones."),
    ("At transform boundaries, plates:",["Collide","Move apart","*Slide horizontally past each other","Subduct"],"Lateral movement."),
    ("When oceanic crust collides with continental crust, the oceanic plate:",["Rises over continental","*Subducts (sinks beneath) because it is denser than continental crust","Stays in place","Melts immediately"],"Density determines subduction."),
    ("The San Andreas Fault is an example of a:",["Convergent boundary","Divergent boundary","*Transform boundary (Pacific and North American plates slide past each other)","Subduction zone"],"Famous transform."),
    ("The Himalayas formed from:",["Subduction","A transform fault","*Continental-continental convergence (India colliding with Asia — neither subducts because both are buoyant)","Divergence"],"Mountain building."),
    ("Ocean trenches form at:",["Divergent boundaries","Transform boundaries","*Convergent boundaries where oceanic crust subducts (deepest points on Earth)","Hot spots"],"Subduction features."),
    ("The Ring of Fire around the Pacific Ocean has many volcanoes because:",["It's near the equator","*It's surrounded by subduction zones where oceanic plates sink, melt, and produce magma","It's the oldest ocean","Currents cause eruptions"],"Subduction volcanism."),
    ("Rift valleys form at:",["Convergent boundaries","Transform boundaries","*Divergent boundaries (plates pulling apart, crust dropping between — e.g., East African Rift)","Hot spots only"],"Continental divergence."),
    ("Volcanic island arcs form when:",["Continents collide","*An oceanic plate subducts under another oceanic plate (melting produces volcanoes on the overriding plate)","Plates slide past each other","Divergence occurs on land"],"Oceanic-oceanic convergence."),
    ("The Andes Mountains formed from:",["Continental-continental collision","Transform faulting","*Oceanic-continental convergence (Nazca plate subducting under South American plate)","Divergence"],"Subduction mountains."),
    ("The deepest point in the ocean (Mariana Trench) is at a _____ boundary.",["Divergent","Transform","*Convergent (Pacific plate subducting under Philippine plate)","Hot spot"],"Deepest trench."),
    ("Most earthquakes, volcanoes, and mountain building occur at:",["The center of plates","Random locations","*Plate boundaries (where plates interact)","Only at the equator"],"Boundary activity."),
]

# U2 L2.4 Earthquakes & Seismic Waves
EXTRA["u2_l2.4"] = [
    ("The point underground where an earthquake originates is called the:",["Epicenter","*Focus (hypocenter)","Fault line","Seismic zone"],"Origin point."),
    ("The epicenter is directly _____ the focus.",["Below","Beside","*Above (on Earth's surface)","Far from"],"Surface point."),
    ("The Richter scale measures earthquake:",["Duration","Depth","*Magnitude (energy released — logarithmic: each whole number = 10× more ground motion)","Location"],"Size measurement."),
    ("A magnitude 7 earthquake releases about _____ times more energy than a magnitude 6.",["10","*~31.6 (each magnitude step = ~31.6× more energy, though 10× more amplitude)","100","1,000"],"Energy scaling."),
    ("P-waves (primary) are the _____ seismic waves to arrive.",["Slowest","Second","*Fastest (compressional waves that push and pull through all materials)","Last"],"First arrival."),
    ("S-waves (secondary) cannot travel through:",["Rock","Continental crust","*Liquids (which is how we know the outer core is liquid)","Air"],"Liquid limitation."),
    ("Surface waves cause the most _____ during an earthquake.",["Noise","Aftershocks","*Damage (they travel along the surface with the largest amplitude and slowest speed)","None"],"Most destructive."),
    ("A seismograph records earthquake waves by using:",["A camera","A clock","*A suspended mass that remains stationary while the ground (and frame) moves beneath it","Sound detectors"],"Recording instrument."),
    ("Three seismograph stations are needed to locate an epicenter because:",["One isn't accurate","Two only give a line","*Triangulation: each station defines a circle of possible locations; three circles intersect at one point","Three is a standard"],"Triangulation method."),
    ("The Modified Mercalli Intensity Scale measures:",["Magnitude","Energy","*The observable effects/damage of an earthquake at a specific location (I to XII)","Depth"],"Damage scale."),
    ("Most earthquakes occur along:",["Random locations","The equator","*Plate boundaries (especially convergent and transform)","Ocean surfaces"],"Boundary association."),
    ("Liquefaction occurs during earthquakes when:",["Rocks melt","Water evaporates","*Water-saturated sediment temporarily behaves like liquid, causing buildings to sink","Ice forms"],"Ground failure."),
    ("Tsunamis are generated by _____ earthquakes.",["Only small","Only land-based","*Large undersea (or coastal) earthquakes that displace the ocean floor","Wind"],"Ocean wave generation."),
]

# U2 L2.5 Volcanoes & Hot Spots
EXTRA["u2_l2.5"] = [
    ("Shield volcanoes have _____ slopes and are formed by _____ lava.",["Steep, thick","*Gentle, low-viscosity (runny basaltic lava that flows far before solidifying)","No, no","Steep, thin"],"Shield characteristics."),
    ("Composite (stratovolcanoes) are formed by alternating layers of:",["Only lava","Only ash","*Lava and pyroclastic material (ash, rock) — making them steep and dangerous","Only mud"],"Layered structure."),
    ("Cinder cone volcanoes are typically:",["The largest","*Small, steep-sided, and built from ejected lava fragments (cinder and ash)","Flat","Underwater only"],"Smallest volcano type."),
    ("The viscosity of lava determines:",["Its color","Its age","*How explosive an eruption will be (high viscosity = trapped gas = more explosive)","Its temperature"],"Viscosity and explosivity."),
    ("Silica content affects lava viscosity: high silica means:",["Runny lava","*Thick, viscous lava (more explosive eruptions)","No lava","Liquid lava"],"Silica effect."),
    ("Hot spots are volcanic areas caused by:",["Plate boundaries","Transform faults","*Mantle plumes (columns of hot rock rising from deep in the mantle, independent of plate boundaries)","Erosion"],"Deep mantle source."),
    ("The Hawaiian Islands formed from:",["A subduction zone","A divergent boundary","*A hot spot (the Pacific Plate moves over a stationary mantle plume, creating a chain of islands)","A transform fault"],"Hot spot chain."),
    ("Yellowstone is an example of a _____ hot spot.",["Oceanic","Extinct","*Continental (a mantle plume under continental crust producing geysers and a supervolcano)","Man-made"],"Continental hot spot."),
    ("Pyroclastic flows are extremely dangerous because they are:",["Slow-moving water","*Fast-moving (100+ km/h) avalanches of hot gas, ash, and rock fragments (700°C+)","Only smoke","Cold debris"],"Deadly flows."),
    ("Volcanic eruptions can affect global climate by:",["Heating the atmosphere","*Injecting sulfur dioxide and ash into the stratosphere, which blocks sunlight and cools temperatures","Creating rain","Stopping wind"],"Climate impact."),
    ("The 1991 eruption of Mount Pinatubo cooled global temperatures by about:",["0°C","*0.5°C for 1-2 years","5°C","10°C"],"Measurable cooling."),
    ("Volcanic soil is often very fertile because:",["It's wet","*Volcanic ash weathers into mineral-rich soil with nutrients like potassium and phosphorus","It's dry","It's old"],"Agricultural benefit."),
    ("Geothermal energy from volcanic regions is used for:",["Nothing","*Electricity generation and heating (e.g., Iceland gets ~25% of electricity from geothermal)","Only cooking","Only bathing"],"Renewable energy."),
]

# U3 L3.1 Weathering
EXTRA["u3_l3.1"] = [
    ("Mechanical weathering breaks rocks into smaller pieces WITHOUT:",["Moving them","Any force","*Changing their chemical composition","Using water"],"Physical only."),
    ("Chemical weathering changes the _____ of rocks.",["Size only","Shape only","*Mineral composition (creating new minerals through chemical reactions)","Color only"],"New minerals formed."),
    ("Frost wedging occurs when:",["Ice melts","Rocks are heated","*Water seeps into cracks, freezes, expands (9%), and forces the crack wider over repeated cycles","Wind blows"],"Freeze-thaw."),
    ("Root wedging is caused by:",["Animals","Wind","*Plant roots growing into rock cracks, slowly prying them apart as the roots expand","Ice"],"Biological mechanical."),
    ("Oxidation (rusting) is an example of _____ weathering.",["Mechanical","*Chemical (iron in rocks reacts with oxygen and water to form iron oxide)","Biological","Physical"],"Chemical reaction."),
    ("Carbonic acid forms when:",["Rocks dissolve","*Carbon dioxide dissolves in rainwater (CO₂ + H₂O → H₂CO₃) — weakly acidic rain","Salt is added to water","Ice melts"],"Natural acid."),
    ("Carbonic acid is particularly effective at dissolving _____ rock.",["Granite","Basalt","*Limestone (CaCO₃ — creating caves, sinkholes, and karst topography)","Obsidian"],"Limestone dissolution."),
    ("Caves and sinkholes are formed primarily by:",["Mechanical weathering","*Chemical weathering of limestone by carbonic acid over thousands to millions of years","Volcanic activity","Earthquakes"],"Karst features."),
    ("The rate of weathering increases with:",["Decreasing surface area","Cold, dry climate","*Increased surface area AND warm, wet climate (more water and heat = faster reactions)","Less water"],"Rate factors."),
    ("Exfoliation (unloading) occurs when:",["Water freezes","Chemicals react","*Overlying rock is removed, reducing pressure and causing the rock below to expand and crack in sheets","Plants grow"],"Pressure release."),
    ("Biological weathering includes:",["Only root wedging","*Root wedging, burrowing animals, lichens producing acids, and bacteria breaking down minerals","Only lichen","No biological process"],"Multiple organisms."),
    ("Acid rain (from pollution) accelerates chemical weathering of:",["Only soil","*Buildings, monuments, and natural rock — especially marble and limestone","Only plants","Nothing"],"Anthropogenic weathering."),
    ("Weathering is the first step in the formation of:",["Igneous rocks","*Sediment and soil (broken rock material that can be eroded, transported, and deposited)","Magma","Metamorphic rocks"],"Sediment source."),
]

# U3 L3.2 Erosion & Deposition
EXTRA["u3_l3.2"] = [
    ("Erosion is the _____ of weathered material by natural agents.",["Creation","*Transport (movement by water, wind, ice, or gravity)","Destruction","Deposition"],"Movement process."),
    ("Deposition occurs when an erosional agent _____ and drops its sediment load.",["Speeds up","*Slows down or loses energy","Disappears","Reverses"],"Energy loss."),
    ("The most powerful agent of erosion on Earth is:",["Wind","Glaciers","*Running water (rivers and streams — responsible for more erosion than all other agents combined)","Gravity"],"Water dominance."),
    ("Wind erosion is most effective in:",["Forests","Wetlands","*Dry environments with little vegetation (deserts, plowed fields)","Oceans"],"Arid erosion."),
    ("Glaciers erode by _____ and plucking.",["Dissolving","Oxidizing","*Abrasion (grinding rock beneath the ice using embedded rock fragments)","Melting only"],"Glacial erosion."),
    ("A delta forms when a river:",["Speeds up","*Enters a larger body of water and slows, depositing sediment in a fan shape","Goes underground","Freezes"],"Depositional feature."),
    ("Alluvial fans form where:",["Rivers meet oceans","*Streams emerge from mountains onto flat plains (sudden decrease in slope causes deposition)","Glaciers melt in oceans","Wind stops in forests"],"Mountain-plain transition."),
    ("Longshore drift moves sediment along a beach by:",["Wind only","*Waves hitting the shore at an angle, carrying sand in a zigzag pattern along the coast","Tides only","Gravity only"],"Coastal transport."),
    ("A barrier island is formed by:",["Volcanic eruption","*Wave action depositing sand parallel to the coast, creating a long, narrow island","River deposition","Plate tectonics"],"Coastal deposition."),
    ("Erosion can be slowed by:",["Removing vegetation","Overgrazing","*Planting vegetation, terracing hillsides, and using cover crops (roots hold soil in place)","Paving everything"],"Conservation."),
    ("The Grand Canyon was primarily formed by:",["Wind erosion","Glacial erosion","*Water erosion by the Colorado River over millions of years","Earthquakes"],"River carving."),
    ("Sediment size deposited by a stream depends on:",["Temperature","Time of year","*Water velocity (faster water carries larger particles; as it slows, larger particles drop first)","River age"],"Size sorting."),
    ("Loess is:",["A type of rock","*Fine-grained sediment (silt) deposited by wind, forming very fertile soil","A river feature","A glacier"],"Wind-deposited silt."),
]

# U3 L3.3 River Systems
EXTRA["u3_l3.3"] = [
    ("A watershed (drainage basin) is:",["A dam","*The entire area of land that drains into a particular river system","A lake","A wetland only"],"Catchment area."),
    ("The Continental Divide in North America determines whether water flows to the:",["North or south","*Atlantic/Gulf of Mexico OR Pacific Ocean","Only the Pacific","Only the Atlantic"],"Drainage divide."),
    ("A meander is:",["A straight river section","A waterfall","*A wide, looping curve in a river formed by erosion on the outer bank and deposition on the inner bank","A dam"],"River curves."),
    ("An oxbow lake forms when:",["A dam is built","Rain fills a hole","*A meander loop is cut off from the main river channel","A glacier melts"],"Abandoned meander."),
    ("A floodplain is:",["Always flooded","*The flat area alongside a river that is periodically flooded, receiving nutrient-rich sediment deposits","A desert","A mountain"],"Fertile lowland."),
    ("V-shaped valleys are characteristic of:",["Old rivers","Glaciers","*Young, fast-flowing rivers cutting downward through rock","Wind erosion"],"Youthful stage."),
    ("U-shaped valleys are carved by:",["Rivers","Wind","*Glaciers (much wider and smoother than V-shaped river valleys)","Waves"],"Glacial valleys."),
    ("A river's base level is:",["Its source","Its highest point","*The lowest level to which it can erode (usually sea level for the main river)","Its widest point"],"Erosion limit."),
    ("Natural levees are built up by:",["Humans only","*Repeated flooding that deposits sediment along the river's banks, building up raised ridges","Glaciers","Wind"],"Natural embankments."),
    ("River discharge is measured as:",["Speed × depth","*Volume of water flowing past a point per unit time (measured in cubic feet or meters per second)","Width × length","Temperature × speed"],"Flow measurement."),
    ("A tributary is a:",["Main river","*Smaller stream or river that flows into a larger one","River mouth","Dam"],"Feeding stream."),
    ("Rapids and waterfalls form where a river flows over:",["Soft rock only","*Bands of resistant rock (hard rock erodes slower, creating a step or drop)","Flat terrain","Sand"],"Differential erosion."),
    ("Levees and dams control flooding but can cause:",["No problems","*Increased flooding downstream, sediment starvation, habitat loss, and false sense of security","Only benefits","Earthquakes"],"Engineering tradeoffs."),
]

# U3 L3.4 Glaciers & Ice Ages
EXTRA["u3_l3.4"] = [
    ("Glaciers form when snow accumulates and compresses into dense ice over:",["Days","Months","*Many years to centuries (snow → firn → glacial ice)","Millions of years always"],"Glacial formation."),
    ("Continental glaciers (ice sheets) are:",["Small and valley-confined","*Massive ice masses covering enormous areas (e.g., Antarctica, Greenland — up to km thick)","Only in mountains","Only in the Arctic"],"Large-scale ice."),
    ("Alpine (valley) glaciers are found in:",["Only poles","Deserts","*Mountain valleys, flowing downhill under their own weight","Oceans"],"Mountain glaciers."),
    ("A moraine is:",["A type of glacier","*A deposit of unsorted sediment (till) left by a glacier, marking its former extent","A glacial lake","An ice cave"],"Glacial deposit."),
    ("Erratics are:",["Normal rocks","*Large boulders transported far from their source by glaciers and deposited when ice melts","Volcanic rocks","Sedimentary layers"],"Glacial transport."),
    ("Glacial striations are:",["Ice formations","*Scratches on bedrock caused by rocks embedded in the base of a moving glacier","River channels","Wind marks"],"Abrasion evidence."),
    ("During the last ice age (peak ~20,000 years ago), ice covered about _____ of Earth's land.",["5%","*30% (compared to ~10% today)","50%","90%"],"Ice age coverage."),
    ("Ice ages are triggered by changes in:",["Moon phases","*Earth's orbital variations (Milankovitch cycles: eccentricity, obliquity, precession)","Sun's size","Volcanic activity alone"],"Astronomical forcing."),
    ("Glacial retreat means the glacier is:",["Moving backwards","*Melting faster at its front than new ice advances — the terminus position recedes","Growing","Stopped"],"Net melting."),
    ("Sea level _____ when glaciers melt and _____ when glaciers grow.",["Falls, rises","*Rises (water returns to ocean), falls (water locked in ice)","Stays same both times","Rises, stays same"],"Sea level connection."),
    ("The Great Lakes were formed by:",["Volcanic activity","Rivers only","*Glacial erosion and deposition during the last ice age (glaciers carved basins, meltwater filled them)","Earthquakes"],"Glacial lakes."),
    ("Fjords are:",["Flat valleys","Desert canyons","*Deep, narrow coastal inlets carved by glaciers that were later flooded by rising seas","River deltas"],"Glacial coastal features."),
    ("Current climate change is causing glaciers worldwide to:",["Grow","Stay the same","*Retreat at accelerating rates (measured by satellite and on-the-ground monitoring since the 1800s)","Move sideways"],"Modern glacial loss."),
]

# U3 L3.5 Mass Wasting
EXTRA["u3_l3.5"] = [
    ("Mass wasting is the downslope movement of material driven primarily by:",["Wind","Water flow","*Gravity","Erosion alone"],"Gravity-driven."),
    ("The fastest type of mass wasting is a:",["Creep","Slump","*Rockfall or debris avalanche (can exceed 200 km/h)","Solifluction"],"Rapid movement."),
    ("The slowest type of mass wasting is:",["Landslide","Mudflow","*Creep (imperceptibly slow — millimeters to centimeters per year, seen in tilted fences/trees)","Rockfall"],"Very slow."),
    ("A slump involves:",["Material flying through the air","*A mass of material sliding along a curved surface — the block rotates backward as it moves","Slow creep","Only water"],"Rotational slide."),
    ("Mudflows (lahars from volcanoes) are triggered by:",["Dry conditions","*Saturated soil or volcanic material mixed with water, flowing rapidly downhill like wet concrete","Freezing","Only earthquakes"],"Water-saturated flow."),
    ("Water contributes to mass wasting by:",["Drying slopes","*Adding weight AND lubricating slip surfaces (water fills pore spaces, reducing friction between particles)","Freezing the ground","Only evaporating"],"Water's dual role."),
    ("Factors that increase the risk of mass wasting include:",["Flat terrain and dense vegetation","*Steep slopes, deforestation, heavy rainfall, earthquakes, and undercutting of slopes","Cold temperatures only","Only human activity"],"Risk factors."),
    ("Deforestation increases mass wasting risk because:",["Trees are heavy","*Tree roots stabilize soil — removing them leaves slopes unanchored and vulnerable to sliding","Trees cause slides","It doesn't"],"Root stabilization."),
    ("Retaining walls and drainage systems are used to:",["Cause landslides","*Prevent or slow mass wasting by supporting slopes and removing excess water","Accelerate erosion","Block rivers"],"Engineering solutions."),
    ("Solifluction occurs in _____ regions where the surface layer thaws and flows over frozen ground beneath.",["Tropical","Desert","*Arctic/permafrost","Coastal"],"Cold-region flow."),
    ("A talus slope is:",["A type of soil","*A pile of angular rock fragments accumulated at the base of a cliff from repeated rockfalls","A glacier feature","A river deposit"],"Rockfall accumulation."),
    ("The angle of repose is:",["The steepest slope at which a river flows","*The steepest angle at which loose material remains stable without sliding (varies by material type)","Always 45°","The flattest surface"],"Stability angle."),
    ("Early warning systems for landslides monitor:",["Only temperature","*Ground movement, rainfall amounts, soil moisture, and slope deformation","Only wind","Only earthquakes"],"Monitoring approach."),
]

# U4 L4.1 Relative Dating
EXTRA["u4_l4.1"] = [
    ("Relative dating determines:",["The exact age in years","*The ORDER of events (which is older/younger) without assigning specific ages","The chemical composition","The mineral content"],"Sequence, not numbers."),
    ("The Law of Superposition states that in undisturbed rock layers:",["Younger rocks are on the bottom","*Older rocks are on the bottom, younger rocks on top","All rocks are the same age","Age alternates"],"Bottom = oldest."),
    ("The Principle of Original Horizontality states that sedimentary layers are originally deposited:",["Vertically","At an angle","*Horizontally (if tilted, something disturbed them after deposition)","Randomly"],"Flat deposition."),
    ("The Principle of Cross-Cutting Relationships states that a fault or intrusion is _____ than the rock it cuts through.",["Older","*Younger (the rock must exist before something can cut across it)","The same age","Unrelated"],"Cutter is younger."),
    ("An unconformity represents:",["Continuous deposition","*A gap in the geologic record where erosion or non-deposition occurred (missing time)","A flood event","An earthquake"],"Missing chapter."),
    ("An angular unconformity shows:",["Parallel layers","*Tilted/folded layers below with horizontal layers above (deformation, erosion, then new deposition)","Identical rock above and below","No visible gap"],"Tilted-then-flat."),
    ("Index fossils are useful for relative dating because they:",["Lived for millions of years","Are common everywhere","*Existed for a SHORT time but were WIDESPREAD (precisely date the layer they're found in)","Are always large"],"Time markers."),
    ("The Principle of Inclusions states that fragments included in a rock must be _____ than the rock containing them.",["Younger","*Older (the fragment had to exist before being incorporated)","The same age","Unrelated"],"Fragment dating."),
    ("Lateral continuity means that a sedimentary layer:",["Only exists in one spot","*Originally extended in all directions until it thinned or reached a boundary (matching layers across gaps)","Is always thick","Is always vertical"],"Continuous layers."),
    ("A disconformity is an unconformity between:",["Tilted and flat layers","*Parallel layers (hard to identify because layers above and below appear continuous — but time is missing)","Igneous and metamorphic layers","Folded layers"],"Subtle gap."),
    ("Faunal succession means that fossil species:",["Appear randomly","*Succeed each other in a definite, recognizable order that can be used for correlation","Never change","Only appear once"],"Ordered appearance."),
    ("Correlation uses _____ to match rock layers across different locations.",["Color alone","*Fossils, rock type, and relative position (key fossils in two distant locations = same age)","Only thickness","Only mineral content"],"Long-distance matching."),
    ("Relative dating is useful even without radiometric dating because it:",["Gives exact years","*Establishes the sequence of events and allows correlation of rock layers across large regions","Is more accurate","Requires no fieldwork"],"Sequencing value."),
]

# U4 L4.2 Absolute Dating
EXTRA["u4_l4.2"] = [
    ("Absolute dating provides:",["Only the order of events","*A specific numerical age in years (e.g., 4.5 billion years old)","Only relative ages","Only fossil positions"],"Numeric ages."),
    ("Radioactive decay is the process by which:",["Atoms grow","*Unstable parent isotopes spontaneously transform into stable daughter isotopes at a constant rate","Rocks melt","Minerals form"],"Decay process."),
    ("Half-life is the time it takes for _____ of a radioactive sample to decay.",["All","A quarter","*Half","10%"],"50% decay."),
    ("After 3 half-lives, _____ of the original parent isotope remains.",["1/2","1/4","*1/8 (50% → 25% → 12.5%)","1/16"],"Exponential decay."),
    ("Carbon-14 dating is useful for dating organic material up to about:",["100 years","1,000 years","*50,000 years (after that, too little C-14 remains to measure accurately)","1 billion years"],"C-14 range."),
    ("Carbon-14 forms when cosmic rays interact with _____ in the atmosphere.",["Oxygen","Carbon dioxide","*Nitrogen-14 (cosmic rays convert N-14 to C-14, which is incorporated into living organisms)","Hydrogen"],"C-14 creation."),
    ("Uranium-238 decays to Lead-206 with a half-life of about:",["1,000 years","1 million years","*4.5 billion years (used for dating very old rocks, including Earth's oldest)","100 billion years"],"Long half-life."),
    ("Potassium-40 decays to Argon-40 and is useful for dating:",["Only recent fossils","*Volcanic rocks from 100,000 to billions of years old","Only meteorites","Only ocean sediments"],"K-Ar dating range."),
    ("Radiocarbon dating can ONLY be used on:",["Any rock","Igneous rocks","*Once-living material (wood, bone, shell — because only living things incorporate C-14)","Metamorphic rocks"],"Organic requirement."),
    ("A rock has 25% parent isotope and 75% daughter isotope. How many half-lives have passed?",["1","*2 (100% → 50% → 25%)","3","4"],"Two half-lives."),
    ("Radiometric dating of igneous rocks dates the time when:",["Erosion occurred","Metamorphism happened","*The rock crystallized from magma/lava (trapping parent isotopes in mineral crystals)","Fossils formed"],"Crystallization date."),
    ("The age of Earth (~4.54 billion years) was determined by dating:",["Surface rocks","Ocean water","*Meteorites and moon rocks (same age as Earth's formation — Earth's oldest surface rocks are younger due to recycling)","Ice cores"],"Solar system dating."),
    ("Dendrochronology (tree-ring dating) can provide:",["Only relative dates","*Exact calendar years for up to ~12,000 years (using overlapping sequences of living and dead trees)","Dates for millions of years","Only seasonal data"],"Tree-ring precision."),
]

# U4 L4.3 Geologic Time Scale
EXTRA["u4_l4.3"] = [
    ("The geologic time scale is divided (largest to smallest) into:",["Periods, eras, epochs","*Eons, eras, periods, epochs","Epochs, periods, eras","Years, decades, centuries"],"Hierarchy."),
    ("The longest eon is the:",["Phanerozoic","Mesozoic","*Precambrian/Archean (Hadean + Archean + Proterozoic span ~4 billion of Earth's 4.54 billion year history)","Cenozoic"],"Most of Earth's time."),
    ("The Phanerozoic Eon (visible life) began approximately _____ million years ago.",["100","250","*541 (marked by the Cambrian Explosion of complex life)","1,000"],"Phanerozoic start."),
    ("The three eras of the Phanerozoic are:",["Archean, Proterozoic, Phanerozoic","*Paleozoic, Mesozoic, Cenozoic","Precambrian, Cambrian, Modern","Triassic, Jurassic, Cretaceous"],"Three eras."),
    ("The Paleozoic Era is known as the age of:",["Dinosaurs","Mammals","*Ancient life (fish, amphibians, early reptiles, and massive forests)","Humans"],"Old life era."),
    ("The Mesozoic Era is known as the age of:",["Fish","*Dinosaurs (also called the Age of Reptiles — Triassic, Jurassic, Cretaceous)","Mammals","Bacteria"],"Dinosaur era."),
    ("The Cenozoic Era is known as the age of:",["Dinosaurs","Fish","*Mammals (following the extinction of dinosaurs, mammals diversified to fill ecological niches)","Reptiles"],"Current era."),
    ("Boundaries between eras are typically marked by:",["Arbitrary dates","Political decisions","*Major mass extinction events (dramatic changes in fossil record)","Climate seasons"],"Extinction boundaries."),
    ("We currently live in the _____ period of the _____ era.",["Cretaceous, Mesozoic","Jurassic, Mesozoic","*Quaternary, Cenozoic","Permian, Paleozoic"],"Present time."),
    ("The Cambrian Explosion (~541 mya) is significant because:",["Life ended","*Most major animal phyla appeared in a relatively short time (geologically) — rapid diversification","Only plants appeared","Nothing evolved"],"Rapid diversification."),
    ("The Precambrian represents _____ of Earth's history.",["10%","50%","*~88% (about 4 billion of 4.54 billion years)","100%"],"Vast majority."),
    ("During most of the Precambrian, life was limited to:",["No life at all","Complex animals","*Single-celled organisms (bacteria and archaea) and later simple multicellular organisms","Dinosaurs"],"Simple life."),
    ("The geologic time scale was developed using both:",["Only fossils","Only radiometric dating","*Relative dating (fossils, stratigraphy) AND absolute dating (radiometric methods)","Only observation"],"Combined methods."),
]

# U4 L4.4 Fossils & Fossil Record
EXTRA["u4_l4.4"] = [
    ("Fossils are the preserved remains or traces of:",["Only dinosaurs","Only plants","*Ancient organisms (any organism — from bacteria to dinosaurs to plants)","Only bones"],"Broad definition."),
    ("The most common type of fossilization is:",["Freezing","Amber preservation","*Permineralization (minerals fill pore spaces in bone/wood, preserving structure)","Carbonization"],"Mineral replacement."),
    ("For an organism to become a fossil, it typically needs to be:",["Alive","Left on the surface","*Buried quickly (rapid burial protects from decay and scavengers)","Very large"],"Quick burial."),
    ("Mold and cast fossils form when:",["An organism freezes","*An organism dissolves, leaving a mold (impression); if the mold fills with sediment, it creates a cast","An organism burns","Bones are replaced by minerals"],"Impression + fill."),
    ("Trace fossils include:",["Actual body parts","*Footprints, burrows, coprolites (fossilized dung), and tracks — evidence of behavior, not body parts","Only bones","Only shells"],"Activity evidence."),
    ("Amber preservation occurs when organisms are trapped in:",["Ice","Rock","*Tree resin that hardens — preserving insects and small organisms in exceptional detail","Water"],"Resin preservation."),
    ("The fossil record is considered incomplete because:",["All organisms fossilize","Scientists hide fossils","*Fossilization requires specific conditions — most organisms decompose without being preserved","Fossils don't exist"],"Preservation bias."),
    ("Organisms with hard parts (shells, bones) are _____ likely to fossilize than soft-bodied organisms.",["Less","Equally","*Much more (hard parts resist decay; soft tissues rarely preserve)","Never"],"Hard part advantage."),
    ("Index fossils must be:",["Rare and long-lived","*Widespread geographically AND short-lived in time (allows precise dating and global correlation)","Only found in one location","Very large"],"Dating tools."),
    ("Trilobites are excellent index fossils for the _____ Era.",["Mesozoic","Cenozoic","*Paleozoic (abundant, diverse, and extinct by end of Permian)","Precambrian"],"Paleozoic markers."),
    ("The fossil record shows that life has:",["Remained unchanged","Appeared suddenly in modern form","*Changed over time (evolution), with species appearing, diversifying, and going extinct","Always been complex"],"Evolutionary evidence."),
    ("Transitional fossils show:",["No evolution","*Intermediate characteristics between ancestral and descendant groups (e.g., Tiktaalik: fish-to-amphibian)","Only extinction","Random change"],"Evolutionary links."),
    ("Petrified wood forms when:",["Wood burns","*Wood is buried and mineral-rich groundwater replaces organic material with silica, preserving cell structure","Wood freezes","Wood is compressed into coal"],"Silica replacement."),
]

# U4 L4.5 Mass Extinctions
EXTRA["u4_l4.5"] = [
    ("A mass extinction is when:",["One species goes extinct","*A large percentage of Earth's species (>75%) go extinct in a geologically short time","All life dies","Only dinosaurs die"],"Major biodiversity loss."),
    ("The 'Big Five' mass extinctions occurred during the:",["Only Cenozoic","*Ordovician, Devonian, Permian, Triassic, and Cretaceous periods","Only Mesozoic","Only Paleozoic"],"Five major events."),
    ("The largest mass extinction was the _____ extinction (~252 mya).",["Cretaceous","Ordovician","*Permian ('The Great Dying' — ~96% of marine and ~70% of land species went extinct)","Devonian"],"Worst extinction."),
    ("The Permian extinction was likely caused by:",["An asteroid","*Massive volcanic eruptions (Siberian Traps) causing extreme climate change, ocean acidification, and oxygen depletion","A flood","Humans"],"Volcanic cause."),
    ("The Cretaceous extinction (~66 mya) is best known for ending the:",["Fish","Mammals","*Non-avian dinosaurs (along with ~75% of all species)","Bacteria"],"Dinosaur extinction."),
    ("The Cretaceous extinction was caused by:",["Only volcanism","*An asteroid impact (Chicxulub crater, Mexico) AND possibly Deccan Traps volcanism — combined catastrophe","Only freezing","Only disease"],"Impact + volcanism."),
    ("The Chicxulub asteroid was approximately _____ in diameter.",["1 km","*10-15 km (6-9 miles)","100 km","1,000 km"],"Size of impactor."),
    ("Evidence for the asteroid impact includes a worldwide layer of:",["Gold","*Iridium (rare on Earth but common in asteroids — found at the K-Pg boundary globally)","Silver","Uranium"],"Iridium anomaly."),
    ("After each mass extinction, surviving species:",["Stayed the same","Slowly died out","*Diversified rapidly to fill empty ecological niches (adaptive radiation)","Stopped evolving"],"Recovery and radiation."),
    ("Mammals diversified after the Cretaceous extinction because:",["They were always dominant","*The extinction of dinosaurs opened up ecological niches that mammals then evolved to fill","The climate perfectly suited them","They caused the extinction"],"Mammalian radiation."),
    ("The current rate of species extinction is estimated to be _____ times the background rate.",["2","10","*100-1,000 (some scientists call this the '6th mass extinction' — driven by human activity)","The same as normal"],"Modern biodiversity crisis."),
    ("Background extinction rate refers to:",["Mass extinctions","*The normal, ongoing rate of species extinction that occurs between mass extinction events","No extinction","Only recent extinction"],"Normal rate."),
    ("Mass extinctions, while devastating, have _____ on long-term evolution.",["No effect","Only negative effects","*Both negative (massive loss) AND positive effects (open niches drive innovation and diversification)","Only positive effects"],"Evolutionary reset."),
]

# U5 L5.1 Atmosphere
EXTRA["u5_l5.1"] = [
    ("The atmosphere is composed primarily of:",["Oxygen and carbon dioxide","*Nitrogen (~78%) and oxygen (~21%)","Oxygen and hydrogen","CO₂ and methane"],"Dominant gases."),
    ("The troposphere is the layer where:",["Meteors burn up","The ozone layer exists","*All weather occurs and where we live (extends ~0-12 km altitude)","Space begins"],"Weather layer."),
    ("Temperature _____ with altitude in the troposphere.",["Increases","Stays the same","*Decreases (~6.5°C per km — called the lapse rate)","Fluctuates randomly"],"Gets colder going up."),
    ("The stratosphere contains the _____ layer.",["Cloud","Pollution","*Ozone (O₃ — absorbs harmful UV radiation from the sun)","Carbon"],"Protective layer."),
    ("Temperature _____ with altitude in the stratosphere because ozone absorbs UV.",["Decreases","Stays the same","*Increases (UV absorption heats this layer)","Fluctuates"],"Ozone heating."),
    ("The mesosphere is the layer where:",["Weather occurs","Ozone is concentrated","*Meteors burn up (shooting stars) due to friction with gas molecules","Satellites orbit"],"Meteor burnup zone."),
    ("The thermosphere has very high temperatures but wouldn't feel warm because:",["It's actually cold","*Gas molecules are extremely spread out — too few particles to transfer significant heat to your body","The instruments are wrong","It's below freezing really"],"Low particle density."),
    ("The exosphere is the outermost layer and:",["Has dense air","Has weather","*Gradually transitions into the vacuum of space (molecules can escape Earth's gravity)","Is the warmest layer"],"Space transition."),
    ("The tropopause is the boundary between the:",["Mesosphere and thermosphere","Stratosphere and mesosphere","*Troposphere and stratosphere","Thermosphere and exosphere"],"First boundary."),
    ("Atmospheric pressure _____ with altitude because there is less air above.",["Increases","Stays the same","*Decreases","Fluctuates"],"Less air = less pressure."),
    ("Earth's early atmosphere had very little:",["Nitrogen","Water vapor","*Free oxygen (O₂ was produced later by photosynthetic organisms — cyanobacteria)","Carbon dioxide"],"Oxygen came later."),
    ("The ozone hole is caused primarily by:",["Natural cycles","Volcanoes","*Human-made CFCs (chlorofluorocarbons) that destroy ozone molecules in the stratosphere","Forest fires"],"CFC damage."),
    ("Without the atmosphere, Earth's average temperature would be about:",["15°C (same as now)","0°C","*−18°C (the greenhouse effect warms Earth by ~33°C to its current ~15°C average)","100°C"],"Greenhouse necessity."),
]

# U5 L5.2 Energy Transfer
EXTRA["u5_l5.2"] = [
    ("Radiation transfers heat through:",["Direct contact","Fluid movement","*Electromagnetic waves (can travel through the vacuum of space — how the sun heats Earth)","Conduction"],"Wave energy."),
    ("Conduction transfers heat through:",["Empty space","Moving fluids","*Direct contact between molecules (touching — e.g., hot pan handle)","Light"],"Contact transfer."),
    ("Convection transfers heat through:",["Contact","Electromagnetic waves","*Circulation of fluids (liquids or gases) — hot fluid rises, cool fluid sinks","Sound"],"Fluid circulation."),
    ("The sun heats Earth primarily through:",["Conduction","Convection","*Radiation (electromagnetic waves travel 150 million km through space)","Contact"],"Solar heating."),
    ("Earth's surface heats the atmosphere primarily through:",["Radiation from the sun passing through","*Contact with warm ground (conduction) and convection (warm air rising)","Only radiation","Only wind"],"Surface → air heating."),
    ("Unequal heating of Earth's surface creates:",["Uniform climate","*Wind and weather systems (temperature differences drive air circulation)","No atmospheric effects","Only rain"],"Weather driver."),
    ("Dark-colored surfaces absorb _____ solar radiation than light-colored surfaces.",["Less","The same","*More (lower albedo — dark surfaces heat up faster)","No"],"Albedo effect."),
    ("Albedo is the measure of how much sunlight a surface:",["Absorbs","Transmits","*Reflects (high albedo = more reflection; snow/ice have high albedo)","Emits"],"Reflectivity."),
    ("The greenhouse effect works because greenhouse gases:",["Block all sunlight","*Allow shortwave solar radiation IN but absorb and re-emit longwave infrared radiation back toward Earth","Create holes in the atmosphere","Reflect all radiation"],"Trapping mechanism."),
    ("The main greenhouse gases are:",["Only CO₂","Only methane","*Water vapor, CO₂, methane, nitrous oxide, and ozone","Only oxygen and nitrogen"],"Multiple gases."),
    ("Land heats up and cools down _____ than water.",["Slower","At the same rate","*Faster (water has a much higher specific heat capacity — requires more energy to change temperature)","Never"],"Land vs. water."),
    ("Sea breezes occur during the day because:",["The ocean heats faster","*Land heats faster → warm air rises over land → cooler air from the sea rushes in to replace it","Wind is random","The moon causes them"],"Differential heating."),
    ("The specific heat of water is important for climate because:",["It doesn't matter","*Water absorbs and releases heat slowly, moderating temperatures of coastal areas (less extreme than inland)","Water is always cold","Water always boils"],"Thermal buffer."),
]

# U5 L5.3 Air Pressure, Wind & Coriolis
EXTRA["u5_l5.3"] = [
    ("Air pressure is caused by the _____ of the atmosphere above a point.",["Temperature","Humidity","*Weight (the column of air pressing down due to gravity)","Speed"],"Weight of air."),
    ("A barometer measures:",["Wind speed","Humidity","*Atmospheric pressure","Temperature"],"Pressure instrument."),
    ("Wind flows from _____ pressure to _____ pressure.",["Low, high","Equal, equal","*High, low (air moves from areas of higher pressure to areas of lower pressure)","High, higher"],"Pressure gradient."),
    ("The Coriolis effect is caused by:",["The moon's gravity","*Earth's rotation (moving air deflects right in Northern Hemisphere, left in Southern)","The sun's heat","Ocean currents"],"Rotational deflection."),
    ("In the Northern Hemisphere, the Coriolis effect deflects winds to the:",["Left","Straight ahead","*Right","Backwards"],"NH deflection."),
    ("Global wind belts include:",["Only westerlies","*Trade winds (0-30°), westerlies (30-60°), and polar easterlies (60-90°)","Only trades","Only one belt"],"Three major belts."),
    ("The jet stream is a narrow band of very fast winds at:",["The surface","*High altitude (~10 km, near the tropopause — speeds of 100-400 km/h)","The equator only","The poles only"],"Upper-level winds."),
    ("Sea breezes blow _____ during the day; land breezes blow _____ at night.",["Offshore, onshore","*Onshore (sea → land), offshore (land → sea)","South, north","Randomly"],"Daily wind reversal."),
    ("An isobar is a line on a weather map connecting points of:",["Equal temperature","Equal humidity","*Equal atmospheric pressure","Equal wind speed"],"Pressure contours."),
    ("Closely spaced isobars indicate:",["Calm weather","Light winds","*Strong winds (larger pressure gradient = stronger force pushing air)","High temperature"],"Wind strength."),
    ("Low-pressure systems are associated with:",["Clear, dry weather","*Cloudy, rainy weather (air rises, cools, and condenses into clouds)","Only cold weather","No weather changes"],"Rising air."),
    ("High-pressure systems are associated with:",["Storms","Rain","*Clear, fair weather (air sinks, warms, and prevents cloud formation)","Only hot weather"],"Sinking air."),
    ("Monsoons are seasonal wind patterns caused by:",["The Coriolis effect alone","*Differential heating between large land masses and oceans (reversing direction seasonally, bringing wet/dry seasons)","Only mountain effects","Random chance"],"Seasonal reversal."),
]

# U5 L5.4 Cloud Types & Precipitation
EXTRA["u5_l5.4"] = [
    ("Clouds form when air rises, cools to its dew point, and water vapor:",["Evaporates","Stays as gas","*Condenses onto tiny particles (condensation nuclei — dust, pollen, sea salt)","Freezes immediately"],"Cloud formation."),
    ("Cumulus clouds are:",["Flat and layered","*Puffy, cotton-like clouds with flat bases — associated with fair weather (unless they grow into cumulonimbus)","Wispy and high","Fog-like"],"Fair weather clouds."),
    ("Stratus clouds are:",["Puffy and tall","*Flat, gray, layered clouds that often cover the entire sky — associated with drizzle or light rain","Wispy","Only at high altitude"],"Layered clouds."),
    ("Cirrus clouds are:",["Low and thick","Heavy rain clouds","*Thin, wispy, high-altitude (6+ km) ice crystal clouds — often indicate approaching weather changes","Fog"],"Ice clouds."),
    ("Cumulonimbus clouds are associated with:",["Clear weather","Light drizzle","*Thunderstorms, heavy rain, lightning, hail, and potentially tornadoes (towering storm clouds)","Fog"],"Storm clouds."),
    ("Nimbus (or nimbo-) in a cloud name indicates:",["High altitude","Fair weather","*Rain-bearing (precipitation-producing) cloud","Ice crystals only"],"Rain prefix/suffix."),
    ("The prefix 'alto-' means the cloud is at:",["Low level","*Mid-level altitude (~2-6 km)","High level","Ground level"],"Mid-level prefix."),
    ("Fog is essentially a _____ cloud at ground level.",["Cirrus","Cumulonimbus","*Stratus","Cumulus"],"Ground cloud."),
    ("Rain forms in clouds when water droplets:",["Stay the same size","*Collide and merge (coalescence) until they're heavy enough to fall — or ice crystals grow at the expense of water droplets","Freeze immediately","Evaporate"],"Precipitation process."),
    ("Sleet forms when:",["Rain freezes on the ground","*Rain falls through a freezing layer AND refreezes before hitting the ground (ice pellets)","Snow melts completely","Hail forms in thunderstorms"],"Freezing rain vs. sleet."),
    ("Hail forms in _____ where strong updrafts carry ice pellets up repeatedly, adding layers.",["Stratus clouds","*Cumulonimbus clouds (thunderstorms)","Cirrus clouds","Fog"],"Thunderstorm ice."),
    ("Orographic precipitation occurs when:",["Warm and cold fronts collide","*Air is forced up over a mountain, cools, and releases moisture on the windward side (creating a rain shadow on the leeward side)","Air sinks","The sun evaporates water"],"Mountain rainfall."),
    ("A rain shadow desert forms on the _____ side of a mountain.",["Windward","*Leeward (the downwind side — air descends, warms, and dries out after releasing moisture on the other side)","Top","Base"],"Dry side."),
]

# U5 L5.5 Weather Fronts & Storms
EXTRA["u5_l5.5"] = [
    ("A weather front is the boundary between:",["Land and water","*Two different air masses (differing in temperature and/or humidity)","Day and night","Two cloud types"],"Air mass boundary."),
    ("A cold front occurs when:",["Warm air pushes under cold air","*A cold air mass advances and forces warm air upward rapidly — often causing thunderstorms","Two air masses stop","No air moves"],"Cold advances."),
    ("A warm front occurs when:",["Cold air advances","*A warm air mass advances and slides up over a retreating cold air mass — often causing steady rain","Air masses stay still","Wind stops"],"Warm advances."),
    ("Cold fronts typically produce _____ weather than warm fronts.",["Calmer","*More intense but shorter-duration (steep front → rapid lifting → thunderstorms, then clearing)","Longer-lasting","The same"],"Intensity difference."),
    ("A stationary front occurs when:",["Fronts move rapidly","*Neither air mass advances — the boundary stays in one place, often causing days of cloudy, rainy weather","Only cold air moves","Only warm air moves"],"Stalled boundary."),
    ("An occluded front forms when:",["Two warm fronts merge","*A faster-moving cold front overtakes a warm front, lifting the warm air completely off the ground","Two cold fronts merge","Stationary fronts move"],"Complex front."),
    ("Thunderstorms require three conditions:",["Only heat","*Moisture, instability (rapidly rising air), and a lifting mechanism (front, mountain, or heating)","Only cold air","Only fronts"],"Storm ingredients."),
    ("Lightning is caused by:",["Wind","Solar energy","*Electrical discharge from charge separation within a cumulonimbus cloud (or between cloud and ground)","Rain falling"],"Electrical discharge."),
    ("Thunder is the sound produced by:",["Lightning striking","*Rapid expansion of air heated by lightning (air superheats to ~30,000°C, expanding explosively)","Wind","Cloud collision"],"Heated air expansion."),
    ("Tornadoes form from:",["Any cloud type","*Severe thunderstorms (supercells) with strong wind shear that creates a rotating updraft (mesocyclone)","Hurricanes only","Clear skies"],"Supercell tornadoes."),
    ("The Enhanced Fujita (EF) Scale rates tornadoes based on:",["Size","Speed of rotation","*Damage caused (EF0 weakest to EF5 strongest)","Duration"],"Damage assessment."),
    ("Hurricanes form over warm ocean water (≥26.5°C) and get energy from:",["Cold water","Tides","*Evaporation and condensation of warm ocean water (latent heat release fuels the storm)","Ice"],"Tropical energy."),
    ("Hurricanes weaken when they:",["Reach the equator","*Move over land or cold water (losing their warm ocean water energy source)","Gain speed","Encounter more moisture"],"Energy source loss."),
]

# U6 L6.1 Climate vs Weather
EXTRA["u6_l6.1"] = [
    ("Weather describes atmospheric conditions over:",["Decades","*Short periods (hours to days)","Centuries","Millions of years"],"Short-term."),
    ("Climate describes the average weather conditions of an area over:",["One day","One week","*30+ years (long-term patterns of temperature, precipitation, etc.)","One year"],"Long-term average."),
    ("'Climate is what you expect; weather is _____.'",["Also expected","Predictable","*What you get (climate = long-term average; weather = day-to-day variation)","Always the same"],"Classic distinction."),
    ("A location's climate is primarily determined by:",["One factor","*Latitude, altitude, ocean currents, proximity to water, and prevailing winds","Only temperature","Only rainfall"],"Multiple factors."),
    ("Latitude affects climate because:",["It changes altitude","It changes soil","*Higher latitudes receive less direct sunlight (lower sun angle = less heating per area)","It changes nothing"],"Distance from equator."),
    ("Altitude affects climate by _____ temperature as elevation increases.",["Increasing","Maintaining","*Decreasing (~6.5°C per 1,000 m — mountaintops are colder even at tropical latitudes)","Randomly changing"],"Elevation cooling."),
    ("Proximity to large bodies of water creates _____ climates (smaller temperature swings).",["More extreme","*More moderate/maritime (water's high specific heat buffers temperatures — cooler summers, warmer winters)","Drier","No effect on"],"Maritime moderation."),
    ("Continental climates (far from water) have:",["Mild temperatures","*Large temperature swings (hot summers, cold winters — no water to moderate)","No seasons","Only rain"],"Extreme variation."),
    ("A microclimate is:",["A global climate pattern","*A small-scale climate variation (e.g., a sunny south-facing slope vs. shaded north-facing slope in the same area)","A type of weather","A measurement error"],"Local variation."),
    ("Climatologists use tree rings, ice cores, and ocean sediments to study:",["Tomorrow's weather","*Past climates (paleoclimatology — reconstructing climate conditions thousands to millions of years ago)","Current weather","Only recent history"],"Proxy data."),
    ("El Niño events involve:",["Cooling of the Pacific","*Warming of the central/eastern Pacific Ocean, which disrupts global weather patterns","Arctic melting","Atlantic storms"],"Pacific warming."),
    ("La Niña is the _____ of El Niño.",["Same as","*Opposite (cooling of the central/eastern Pacific — often brings opposite weather impacts from El Niño)","Continuation","Cause"],"Pacific cooling."),
    ("Climate normals are calculated over _____ year periods.",["10","20","*30 (the standard reference period for defining a region's climate)","100"],"Standard period."),
]

# U6 L6.2 Factors Affecting Climate
EXTRA["u6_l6.2"] = [
    ("Ocean currents affect coastal climates by:",["Having no effect","*Transporting warm or cold water, which heats or cools the air above (e.g., Gulf Stream warms Western Europe)","Only creating waves","Only affecting fish"],"Current influence."),
    ("The Gulf Stream carries warm water from the _____ toward _____.",["Arctic toward tropics","*Gulf of Mexico/Caribbean toward Western Europe","Pacific toward Atlantic","Antarctic toward Africa"],"Major warm current."),
    ("Without the Gulf Stream, Western Europe would be _____ than it currently is.",["Warmer","*Significantly colder (London is at the same latitude as Labrador, Canada, but much milder)","The same","Wetter"],"European climate impact."),
    ("The rain shadow effect creates dry conditions on the _____ side of mountains.",["Windward","*Leeward (air descends, warms, and loses its moisture capacity)","Top","Both sides equally"],"Orographic dryness."),
    ("Prevailing winds affect climate by:",["Having no effect","*Bringing characteristic temperature and moisture conditions from their source region","Only causing storms","Only creating waves"],"Wind influence."),
    ("Large cities are often warmer than surrounding areas due to the:",["Ocean","*Urban heat island effect (concrete, asphalt, and buildings absorb and re-radiate heat; less vegetation)","Higher altitude","More rainfall"],"Urban warming."),
    ("Volcanic eruptions can temporarily cool the climate by:",["Releasing heat","*Injecting sulfur dioxide aerosols into the stratosphere, which reflect sunlight back to space","Absorbing CO₂","Releasing oxygen"],"Volcanic cooling."),
    ("Milankovitch cycles affect climate over _____ timescales.",["Daily","Annual","*Tens of thousands to hundreds of thousands of years (orbital variations affecting solar radiation distribution)","Billions of years"],"Astronomical cycles."),
    ("Earth's axial tilt (obliquity, ~23.5°) is responsible for:",["Day and night","*Seasons (tilted axis means different hemispheres get more/less direct sunlight at different times of year)","Ocean currents","Volcanic activity"],"Season driver."),
    ("Vegetation affects climate by:",["Having no effect","*Absorbing CO₂ (reducing greenhouse effect), increasing evapotranspiration, and lowering albedo compared to bare ground","Only producing oxygen","Only providing shade"],"Plant influence."),
    ("Deforestation affects local climate by:",["Cooling the area","*Generally warming and drying the area (less evapotranspiration, more solar absorption, less CO₂ uptake)","Having no effect","Only affecting animals"],"Deforestation impact."),
    ("Thermohaline circulation is driven by differences in:",["Wind and waves","*Temperature (thermo) and salinity (haline) — dense, cold, salty water sinks, driving global ocean conveyor","Only depth","Only tides"],"Ocean conveyor."),
    ("If thermohaline circulation weakened or stopped, Europe would likely:",["Get warmer","*Get significantly colder (loss of Gulf Stream heat transport)","See no change","Get drier only"],"Circulation disruption."),
]

# U6 L6.3 Climate Zones
EXTRA["u6_l6.3"] = [
    ("The Köppen climate classification system categorizes climates based on:",["Only altitude","*Temperature and precipitation patterns (using letters: A-tropical, B-dry, C-temperate, D-continental, E-polar)","Only latitude","Only vegetation"],"Classification basis."),
    ("Tropical climates (Köppen A) are characterized by:",["Cold winters","*Warm temperatures year-round (all months >18°C average) with significant rainfall","Extreme dryness","Permafrost"],"Warm and wet."),
    ("Arid/desert climates (Köppen B) receive:",["Heavy rainfall","*Very little precipitation (evaporation exceeds precipitation) — covers ~30% of Earth's land area","Moderate rainfall","Only snow"],"Dry climates."),
    ("Temperate climates (Köppen C) have:",["No seasons","*Mild winters and warm/hot summers with moderate precipitation","Extreme cold year-round","Only rain, no snow"],"Moderate climates."),
    ("Continental climates (Köppen D) are found mainly in:",["The tropics","Small islands","*Northern Hemisphere interior areas (large temperature ranges; cold winters, warm/hot summers)","Southern Hemisphere"],"NH interior."),
    ("Polar climates (Köppen E) have:",["Warm summers","*The warmest month below 10°C (tundra) or 0°C (ice cap) — very cold year-round","Tropical rainfall","Mild winters"],"Extreme cold."),
    ("Biomes are large ecological communities defined primarily by:",["Soil type alone","*Climate (especially temperature and precipitation) and the vegetation they support","Animal species alone","Human activity"],"Climate-vegetation link."),
    ("The tropical rainforest biome has the _____ biodiversity of any biome.",["Lowest","Moderate","*Highest (warm temperatures + abundant rainfall year-round = ideal growing conditions)","Zero"],"Maximum diversity."),
    ("Deserts can be _____ as well as hot.",["Only hot","*Cold (e.g., Antarctica is technically a desert — very low precipitation regardless of temperature)","Only moderate","Only at the equator"],"Cold deserts."),
    ("Tundra is characterized by:",["Dense forests","*Permafrost, very low temperatures, short growing season, and low-growing vegetation (no trees)","Tropical plants","Heavy rainfall"],"Arctic biome."),
    ("The taiga (boreal forest) is the _____ land biome on Earth.",["Smallest","*Largest (vast coniferous forests across Russia, Canada, Scandinavia)","Driest","Warmest"],"Biggest biome."),
    ("Grasslands (prairies/savannas) receive _____ precipitation than forests but _____ than deserts.",["More, less","*Less (than forests), more (than deserts) — enough for grasses but not enough for dense tree growth","The same","None"],"Middle precipitation."),
    ("Climate zones shift toward the poles during _____ periods.",["Ice ages","*Warmer (interglacial) periods — as global temperatures rise, climate zones migrate poleward","Cooler periods","Rainy periods"],"Zone migration."),
]

# U6 L6.4 Greenhouse Effect
EXTRA["u6_l6.4"] = [
    ("The greenhouse effect is:",["Always harmful","*A natural process that warms Earth by trapping outgoing infrared radiation — essential for life (33°C warming)","Only man-made","A recent phenomenon"],"Natural and necessary."),
    ("Greenhouse gases allow _____ radiation from the sun to pass through but absorb _____ radiation from Earth.",["Infrared, visible","*Shortwave (visible), longwave (infrared) — the 'trapping' mechanism","UV, infrared","All, none"],"Wavelength selectivity."),
    ("The most abundant greenhouse gas by volume is:",["Carbon dioxide","Methane","*Water vapor (responsible for ~60% of natural greenhouse warming)","Ozone"],"Water vapor dominance."),
    ("CO₂ is the most important human-enhanced greenhouse gas because:",["It's the most abundant","*Its concentration is increasing significantly due to fossil fuel burning AND it persists in the atmosphere for centuries","It's the strongest per molecule","It's natural"],"Persistence + increase."),
    ("Methane (CH₄) is _____ times more effective per molecule than CO₂ at trapping heat.",["2","10","*~80 (over 20 years); ~28 (over 100 years) — very potent but shorter-lived than CO₂","1,000"],"Methane potency."),
    ("Sources of methane include:",["Only cows","*Livestock, rice paddies, landfills, natural gas leaks, wetlands, and permafrost thawing","Only landfills","Only natural gas"],"Multiple sources."),
    ("CO₂ levels before industrialization were about _____ ppm; current levels are about _____ ppm.",["100, 200","*280, 425+","400, 400","50, 100"],"CO₂ rise."),
    ("The enhanced greenhouse effect refers to:",["More sunlight","*The additional warming caused by HUMAN activities increasing greenhouse gas concentrations beyond natural levels","Natural processes only","Less radiation"],"Human enhancement."),
    ("Fossil fuel combustion adds CO₂ by:",["Creating carbon from nothing","*Releasing carbon that was stored underground for millions of years (coal, oil, gas back into the atmosphere)","Moving existing atmospheric carbon","Only producing energy"],"Ancient carbon release."),
    ("Deforestation contributes to enhanced greenhouse effect by:",["Planting trees","*Removing trees that absorb CO₂ AND releasing stored carbon when trees are burned or decompose","Increasing albedo","Cooling the surface"],"Carbon source + lost sink."),
    ("A positive feedback loop in climate: warming → ice melts → less reflection → more warming. This is called:",["Ice age","*Ice-albedo feedback (reduced ice = lower albedo = more absorption = more warming = more melting)","Negative feedback","Equilibrium"],"Accelerating loop."),
    ("Venus has extreme greenhouse effect (surface ~460°C) because its atmosphere is ~96%:",["Oxygen","Nitrogen","*Carbon dioxide (runaway greenhouse effect)","Methane"],"Planetary comparison."),
    ("Without ANY greenhouse effect, Earth's average surface temperature would be about:",["15°C","0°C","*−18°C (compared to actual average of ~15°C — the greenhouse effect adds ~33°C)","−50°C"],"Essential warming."),
]

# U6 L6.5 Evidence of Climate Change
EXTRA["u6_l6.5"] = [
    ("Ice cores provide a record of past climate going back:",["1,000 years","10,000 years","*~800,000 years (Antarctic ice cores trap ancient air bubbles showing past CO₂ and temperature)","1 million years"],"Ice core record."),
    ("Global average temperature has increased approximately _____ since 1880.",["0.1°C","0.5°C","*1.1-1.2°C (with most warming occurring since the 1970s)","5°C"],"Measured warming."),
    ("Arctic sea ice has declined by approximately _____ per decade since satellite records began (1979).",["1%","5%","*~13% (September minimum — the Arctic is warming 2-3× faster than the global average)","30%"],"Arctic ice loss."),
    ("Global sea level has risen approximately _____ since 1900.",["2 cm","10 cm","*~20-25 cm (8-10 inches) — due to thermal expansion AND melting ice","1 meter"],"Measured rise."),
    ("The two main causes of sea level rise are:",["More rain and rivers","*Thermal expansion of warming ocean water AND melting of land-based ice (glaciers, ice sheets)","Only ice melting","Only thermal expansion"],"Dual cause."),
    ("Ocean acidification occurs because the ocean absorbs about _____ of human CO₂ emissions.",["5%","15%","*~25-30% (CO₂ + H₂O → carbonic acid, lowering ocean pH)","75%"],"Ocean CO₂ absorption."),
    ("Ocean pH has decreased by about _____ since pre-industrial times.",["0.001","*0.1 units (~30% increase in acidity — threatening coral reefs and shell-forming organisms)","1.0","3.0"],"Acidification measure."),
    ("Coral bleaching is caused by:",["Pollution only","*Warming ocean temperatures (corals expel their symbiotic algae when stressed by heat)","Overfishing","Cold water"],"Thermal stress."),
    ("Glaciers and ice sheets are _____ worldwide.",["Growing","Stable","*Retreating/shrinking at accelerated rates (documented by satellite imagery and ground measurements)","Advancing"],"Global trend."),
    ("Permafrost thawing is concerning because it:",["Helps plant growth","*Releases stored methane and CO₂, creating a positive feedback loop (more warming = more thawing = more GHG release)","Cools the climate","Has no climate effect"],"Permafrost feedback."),
    ("Phenological changes (earlier spring blooms, bird migration shifts) are evidence of:",["Random variation","*Climate change affecting the timing of natural biological events","No change","Only local weather"],"Biological indicators."),
    ("Species are moving toward _____ latitudes and _____ elevations in response to warming.",["Lower, lower","*Higher (poleward), higher (upslope) — following their preferred temperature range","They don't move","Lower, higher"],"Range shifts."),
    ("The scientific consensus (97%+ of climate scientists) is that current warming is:",["Natural","Caused by the sun","*Primarily caused by human activities (fossil fuels, deforestation, agriculture)","Not happening"],"Expert agreement."),
]

# U6 L6.6 Human Impact on Climate
EXTRA["u6_l6.6"] = [
    ("The largest source of human greenhouse gas emissions is:",["Agriculture","Deforestation","*Burning fossil fuels for energy (electricity, transportation, industry — ~75% of global GHG emissions)","Waste"],"Energy sector dominance."),
    ("Transportation accounts for approximately _____ of global CO₂ emissions.",["5%","*~16% (cars, trucks, planes, ships)","40%","60%"],"Transport share."),
    ("Agriculture contributes to climate change through:",["Only CO₂","*Methane from livestock/rice, nitrous oxide from fertilizers, CO₂ from deforestation for farmland","Only deforestation","Only water use"],"Agricultural emissions."),
    ("Renewable energy sources include:",["Coal and natural gas","*Solar, wind, hydroelectric, geothermal, and biomass","Only nuclear","Only solar"],"Clean energy."),
    ("The Paris Agreement aims to limit global warming to:",["0.5°C","*Well below 2°C above pre-industrial levels (with efforts toward 1.5°C)","5°C","No specific target"],"International goal."),
    ("Carbon sequestration refers to:",["Burning more carbon","*Capturing and storing CO₂ (naturally by forests/oceans, or technologically through carbon capture and storage)","Measuring carbon","Releasing carbon"],"Carbon removal."),
    ("A carbon footprint measures:",["Physical foot size","*The total greenhouse gas emissions caused by an individual, event, organization, or product","Only car emissions","Only electricity use"],"GHG impact."),
    ("Reducing deforestation helps climate because forests:",["Don't affect climate","*Absorb CO₂ through photosynthesis (carbon sinks) — preserving forests maintains this absorption","Only produce oxygen","Only provide shade"],"Forest as carbon sink."),
    ("Energy efficiency improvements can reduce emissions by:",["Nothing significant","*30-50% in many sectors (better insulation, LED lighting, fuel-efficient vehicles, industrial processes)","Only 1%","100%"],"Efficiency gains."),
    ("Electric vehicles reduce emissions most when powered by:",["Coal electricity","*Renewable energy sources (solar/wind electricity — EVs powered by coal have smaller but still real benefits)","Natural gas only","Diesel"],"Clean grid + EV."),
    ("Adaptation to climate change includes:",["Ignoring the problem","*Building sea walls, developing drought-resistant crops, improving early warning systems, updating infrastructure","Only mitigation","Only moving populations"],"Adaptation strategies."),
    ("Mitigation of climate change refers to:",["Adapting to impacts","*Reducing greenhouse gas emissions to slow/stop further warming (prevention vs. adaptation)","Measuring climate","Studying weather"],"Emission reduction."),
    ("Individual actions that reduce carbon footprint include:",["Nothing individuals can do","*Reducing energy use, driving less, eating less meat, flying less, and supporting clean energy policies","Only recycling","Only buying electric cars"],"Personal action."),
]

# U7 L7.1 Ocean Floor Features
EXTRA["u7_l7.1"] = [
    ("The continental shelf is the gently sloping extension of the continent under:",["Deep ocean","*Shallow water (depths to ~200 m) — biologically productive and rich in resources","The mantle","Freshwater"],"Shallow extension."),
    ("The continental slope marks the transition from:",["Deep ocean to shore","*Continental shelf to the deep ocean floor (steeper angle)","Land to shallow water","One continent to another"],"Steep descent."),
    ("The abyssal plain is:",["A mountain range","A shallow area","*The vast, flat, deep ocean floor (3,000-6,000 m depth) — the largest habitat on Earth","A coastline"],"Deep flat floor."),
    ("Mid-ocean ridges are:",["Flat, featureless areas","Continental features","*Underwater mountain chains where new oceanic crust is formed at divergent boundaries","Deep valleys"],"Submarine mountains."),
    ("The Mariana Trench is _____ deep and is located at a _____ boundary.",["5 km, divergent","*~11 km (36,000 ft), convergent (subduction zone)","3 km, transform","1 km, hot spot"],"Deepest point."),
    ("Seamounts are:",["Flat plains","Beaches","*Underwater volcanic mountains that do not reach the surface (if they do, they form islands)","Sand dunes"],"Submarine volcanoes."),
    ("Guyots (tablemounts) are seamounts with flat tops, eroded by:",["Currents","*Waves when they were once at the surface (then submerged as the plate moved and/or sea level changed)","Wind","Ice"],"Eroded seamounts."),
    ("Hydrothermal vents are found at:",["Beaches","The continental shelf","*Mid-ocean ridges where superheated water (up to 400°C) exits the seafloor, supporting unique ecosystems","River mouths"],"Deep-sea vents."),
    ("Black smokers are hydrothermal vents that appear dark due to:",["Oil","Pollution","*Dissolved metal sulfide minerals precipitating as the hot water meets cold ocean water","Volcanic ash"],"Mineral precipitation."),
    ("Deep-sea trenches are formed by:",["Erosion","Rifting","*Subduction of one tectonic plate beneath another (creating the deepest points on Earth's surface)","Volcanic eruption"],"Subduction features."),
    ("Turbidity currents are underwater avalanches of:",["Clear water","*Sediment-laden water that flows rapidly down the continental slope, creating submarine canyons","Hot water","Lava"],"Sediment flows."),
    ("Coral reefs are typically found in:",["Deep, cold water","*Warm, shallow, clear tropical water (need sunlight for photosynthetic algae in the coral)","All oceans equally","Only the Atlantic"],"Reef habitat."),
    ("Technology used to map the ocean floor includes:",["Only direct observation","*Sonar (echo sounding), satellite altimetry, submersibles, and multibeam mapping","Only nets","Only drilling"],"Mapping tools."),
]

# U7 L7.2 Ocean Water Properties
EXTRA["u7_l7.2"] = [
    ("Ocean water salinity averages approximately:",["5 ppt","*35 ppt (parts per thousand) — or about 3.5%","50 ppt","100 ppt"],"Average salt content."),
    ("The most abundant dissolved salt in seawater is:",["Carbonate","Magnesium","*Sodium chloride (NaCl — about 85% of dissolved salts)","Potassium"],"Dominant salt."),
    ("Salinity is higher near the equator (surface) due to:",["More rivers","*Higher evaporation rates (more water leaves, concentrating salt)","Less sunlight","Colder temperatures"],"Evaporation effect."),
    ("Near river mouths, salinity is _____ due to freshwater input.",["Higher","*Lower (diluted by incoming freshwater)","The same","Variable regardless of freshwater"],"Freshwater dilution."),
    ("Ocean water density increases with:",["Higher temperature","Lower salinity","*Lower temperature AND higher salinity (cold, salty water is densest)","Higher temperature and lower salinity"],"Density factors."),
    ("The thermocline is a zone where temperature:",["Stays constant","Increases with depth","*Decreases rapidly with depth (transition between warm surface water and cold deep water)","Increases then decreases"],"Temperature gradient."),
    ("Below the thermocline, deep ocean water is approximately:",["25°C","15°C","*1-4°C (cold, dense water filling the deep ocean basins)","−10°C"],"Deep ocean temp."),
    ("The ocean absorbs about _____ of the sun's energy that reaches Earth's surface.",["10%","30%","*70%+ (the ocean is Earth's largest heat reservoir)","100%"],"Heat reservoir."),
    ("Dissolved oxygen in ocean water comes primarily from:",["Rivers","Deep-sea vents","*Photosynthesis by phytoplankton AND absorption from the atmosphere at the surface","Volcanic gases"],"Oxygen sources."),
    ("Dissolved oxygen decreases with _____ temperature because warm water holds less gas.",["Decreasing","*Increasing","Constant","Variable"],"Warmer = less O₂."),
    ("The halocline is a zone where _____ changes rapidly with depth.",["Temperature","*Salinity","Pressure","Light"],"Salt gradient."),
    ("Ocean water is slightly basic with an average pH of about:",["5.0","7.0","*8.1 (and decreasing due to ocean acidification from absorbed CO₂)","9.5"],"Ocean pH."),
    ("Pressure in the ocean increases by about 1 atmosphere for every _____ meters of depth.",["1","*10","100","1,000"],"10 m = 1 atm."),
]

# U7 L7.3 Ocean Currents
EXTRA["u7_l7.3"] = [
    ("Surface ocean currents are driven primarily by:",["Tides","Earth's rotation alone","*Global wind patterns (trade winds, westerlies) combined with the Coriolis effect","Moon's gravity"],"Wind-driven."),
    ("The Coriolis effect causes ocean currents to curve _____ in the Northern Hemisphere.",["Left","Straight","*Right","Backward"],"NH deflection."),
    ("Gyres are:",["Deep currents","Small whirlpools","*Large, circular current systems in each major ocean basin (clockwise in NH, counterclockwise in SH)","Tidal patterns"],"Major circulation."),
    ("The Gulf Stream is a major _____ current in the Atlantic.",["Cold","*Warm (carrying tropical heat northward toward Europe)","Neutral","Deep"],"Warm current."),
    ("Deep ocean currents (thermohaline circulation) are driven by:",["Wind","Tides","*Differences in water density caused by temperature and salinity variations","Waves"],"Density-driven."),
    ("The global conveyor belt describes:",["Surface currents only","*The interconnected system of surface and deep currents circulating water throughout all ocean basins over ~1,000 years","Wind patterns","Wave patterns"],"Global circulation."),
    ("Upwelling brings _____ , nutrient-rich water to the surface.",["Warm","*Cold, deep (nutrients accumulate in deep water from decomposition — upwelling fuels productive ecosystems)","Salty","Fresh"],"Nutrient delivery."),
    ("Upwelling zones are important because they support:",["Very little life","*Highly productive fisheries (nutrients fuel phytoplankton growth → food chains)","Only deep-sea life","Only coral reefs"],"Biological productivity."),
    ("El Niño weakens the trade winds, which:",["Strengthens upwelling","*Reduces upwelling along the western South American coast, decreasing nutrients and harming fisheries","Has no ocean effect","Increases rainfall in deserts"],"ENSO ocean impact."),
    ("Ocean currents affect climate by:",["Having no climate effect","*Transporting heat from the tropics toward the poles, moderating temperature extremes globally","Only causing waves","Only moving fish"],"Heat redistribution."),
    ("The Canary Current is a _____ current that cools the coast of northwest Africa.",["Warm","*Cold (flowing from higher to lower latitude along the eastern Atlantic)","Deep","Neutral"],"Cold current."),
    ("Ekman transport causes surface water to move _____ to the wind direction (in the Northern Hemisphere).",["Parallel","Opposite","*90° to the right (the net transport of the full water column spirals to the right of wind)","Randomly"],"Wind-water relationship."),
    ("If thermohaline circulation slowed significantly, it could:",["Have no effect","*Disrupt global climate patterns, potentially cooling Europe and altering precipitation worldwide","Only affect deep ocean","Only affect the Arctic"],"Circulation disruption."),
]

# U7 L7.4 Tides
EXTRA["u7_l7.4"] = [
    ("Tides are caused primarily by the gravitational pull of:",["Only the sun","Only Earth's spin","*The moon (primary) and the sun (secondary)","Wind"],"Gravitational cause."),
    ("High tides occur on _____ side(s) of Earth relative to the moon.",["Only the near side","Only the far side","*Both sides (near side: gravitational pull; far side: inertia/centrifugal effect)","No particular side"],"Two bulges."),
    ("Most coastal areas experience _____ high tides per day.",["1","*2 (approximately every 12 hours and 25 minutes — semidiurnal tides)","4","Variable"],"Twice daily."),
    ("Spring tides occur when:",["It's spring season","*The sun, moon, and Earth are aligned (new moon or full moon) — producing the HIGHEST tides","The moon is at quarter phase","Currents are strong"],"Alignment = extreme."),
    ("Neap tides occur when:",["Sun and moon align","*The sun and moon are at right angles to Earth (first or third quarter moon) — producing the LOWEST tidal range","It's nighttime","It's a full moon"],"Right angles = moderate."),
    ("Spring tides have a _____ tidal range than neap tides.",["Smaller","Equal","*Larger (gravitational forces of sun and moon add together when aligned)","Unpredictable"],"Maximum range."),
    ("The Bay of Fundy has the world's highest tides (~16 m) because of its:",["Location near the equator","*Funnel-shaped geography that amplifies tidal energy as water is channeled into a narrowing bay","Proximity to the moon","Volcanic activity"],"Geographic amplification."),
    ("The tidal period is approximately 12 hours and 25 minutes because:",["Earth rotates every 12 hours","*The moon orbits Earth, so it takes an extra ~50 minutes each day for Earth to rotate back to the same position relative to the moon","Tides are random","The sun causes the delay"],"Lunar advance."),
    ("Tidal currents are:",["Vertical water movement","*Horizontal water movement associated with the rise and fall of tides (flowing in and out of bays/harbors)","Wind-driven currents","Deep ocean currents"],"Horizontal tidal flow."),
    ("An incoming (rising) tide is called a _____ tide.",["Ebb","Neap","*Flood","Spring"],"Rising water."),
    ("An outgoing (falling) tide is called an _____ tide.",["Flood","Spring","*Ebb","Neap"],"Falling water."),
    ("Tidal energy can be harnessed for electricity using:",["Solar panels","Wind turbines","*Tidal barrages or turbines placed in areas with strong tidal currents","Nuclear reactors"],"Renewable energy."),
    ("Tides affect marine life by creating _____ zones.",["No","*Intertidal (the area between high and low tide lines — organisms must adapt to both submerged and exposed conditions)","Only deep-sea","Only freshwater"],"Habitat creation."),
]

# U7 L7.5 Marine Ecosystems
EXTRA["u7_l7.5"] = [
    ("The photic zone extends from the surface to about _____ meters.",["10","50","*200 (where enough sunlight penetrates for photosynthesis)","1,000"],"Light zone depth."),
    ("The aphotic zone is:",["Well-lit","*The dark zone below ~200 m where no significant sunlight penetrates — organisms rely on other energy sources","The surface","The intertidal zone"],"Dark zone."),
    ("Phytoplankton are important because they:",["Are large fish","*Produce approximately 50% of Earth's oxygen through photosynthesis (base of ocean food web)","Only feed whales","Live on land"],"Oxygen producers."),
    ("Coral reefs are sometimes called the 'rainforests of the sea' because of their:",["Location","Size","*Extremely high biodiversity (supporting ~25% of all marine species despite covering <1% of ocean floor)","Rainfall"],"Biodiversity hotspots."),
    ("Coral reefs require _____ water temperatures and _____ water.",["Cold, deep","*Warm (20-30°C), clear/shallow (sunlight for zooxanthellae algae photosynthesis)","Any temperature, murky","Hot, acidic"],"Coral requirements."),
    ("Kelp forests are found in:",["Tropical waters","*Cool, nutrient-rich coastal waters (providing habitat comparable to terrestrial forests)","The deep sea","Freshwater lakes"],"Temperate marine."),
    ("Hydrothermal vent communities get energy from:",["Sunlight","*Chemosynthesis (bacteria convert chemicals like hydrogen sulfide into energy — no sunlight needed)","Wind","Ocean currents"],"Chemical energy."),
    ("The deep sea covers _____ of Earth's surface, making it the largest habitat.",["10%","30%","*~65% (vast, cold, dark, high-pressure environment that remains largely unexplored)","90%"],"Largest habitat."),
    ("An estuary is where:",["Two oceans meet","*A river meets the sea (mixing fresh and salt water — extremely productive ecosystems, nurseries for many species)","Deep currents form","Volcanic vents exist"],"Freshwater-saltwater mixing."),
    ("Mangrove forests protect coastlines by:",["Blocking sunlight","*Reducing wave energy, trapping sediment, preventing erosion, and serving as nursery habitat for fish and shellfish","Increasing waves","Cooling water"],"Coastal protection."),
    ("Overfishing threatens marine ecosystems by:",["Adding more fish","*Removing species faster than they can reproduce, disrupting food webs and potentially causing ecosystem collapse","Having no effect","Only reducing diversity slightly"],"Fishery collapse risk."),
    ("Marine Protected Areas (MPAs) help ecosystems by:",["Allowing unlimited fishing","*Restricting human activity to allow populations and habitats to recover","Only helping tourism","Only limiting pollution"],"Conservation tool."),
    ("Ocean plastic pollution affects marine life through:",["No significant impact","*Ingestion (mistaken for food), entanglement, habitat damage, and microplastics entering the food chain","Only visual pollution","Only beach litter"],"Plastic threat."),
]

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for key, extra_qs in EXTRA.items():
    if key not in data:
        print(f"⚠️  Key {key} not found, skipping")
        continue
    existing = data[key].get("quiz_questions", [])
    start_num = len(existing) + 1
    for i, (qt, opts, exp) in enumerate(extra_qs):
        q = make_q(qt, opts, exp)
        q["question_number"] = start_num + i
        existing.append(q)
    data[key]["quiz_questions"] = existing
    count += 1

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Earth Science: added 13 questions to {count} lessons (now 20 each)")
