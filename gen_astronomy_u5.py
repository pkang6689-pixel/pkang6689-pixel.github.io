#!/usr/bin/env python3
"""Astronomy Unit 5 – Stars (8 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "astronomy_lessons.json")
COURSE = "Astronomy"

def build_lesson(unit, idx, title, summary_html, flashcards, quiz):
    key = f"u{unit}_l{unit}.{idx}"
    fc = [{"term": t, "definition": d} for t, d in flashcards]
    qs = []
    for qi, (qt, opts, exp) in enumerate(quiz, 1):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        qs.append({"question_number": qi, "question_text": qt, "attempted": 2,
                    "data_i18n": None, "options": options, "explanation": exp})
    return key, {
        "unit": unit, "lesson_number": f"{unit}.{idx}", "title": title, "course": COURSE,
        "summary_sections": [{"title": f"Key Concepts: {title}", "content_html": summary_html, "data_i18n": None}],
        "flashcards": fc, "quiz_questions": qs
    }

lessons = {}

# 5.1
k,v = build_lesson(5,1,"Properties of Stars (Temperature, Luminosity, Size)",
    "<h3>Properties of Stars</h3>"
    "<h4>Temperature</h4>"
    "<p>Measured via color/spectral type. O (>30,000 K, blue) → B → A → F → G → K → M (<3,500 K, red). Mnemonic: Oh Be A Fine Girl/Guy, Kiss Me.</p>"
    "<h4>Luminosity</h4>"
    "<p>Total energy output. Ranges from 0.0001 L☉ (dim red dwarfs) to >1,000,000 L☉ (hypergiants). Absolute magnitude measures intrinsic brightness.</p>"
    "<h4>Size</h4>"
    "<p>Ranges from neutron stars (~20 km) to supergiants (>1,000 R☉). Related through L = 4πR²σT⁴.</p>",
    [("Spectral Type","Classification of stars by temperature/absorption lines: O B A F G K M (hot to cool)."),
     ("Luminosity","Total energy radiated per second; measured in solar luminosities (L☉) or watts."),
     ("Absolute Magnitude","Brightness of a star if placed at 10 parsecs; measures intrinsic luminosity."),
     ("Apparent Magnitude","Brightness as seen from Earth; depends on luminosity AND distance."),
     ("Parallax","Apparent shift of a nearby star against distant background; used to measure distance (d = 1/p parsecs).")],
    [("The spectral classification sequence from hottest to coolest is:",["M K G F A B O","*O B A F G K M","A B C D E F G","G K M O B A F"],"Oh Be A Fine Girl/Guy, Kiss Me."),
     ("O-type stars have surface temperatures:",["<3,500 K","5,000–6,000 K","*>30,000 K","10,000 K"],"The hottest spectral type."),
     ("The Sun is a _____ -type star.",["O","A","*G (G2V, ~5,800 K)","M"],"Yellow, medium temperature."),
     ("M-type stars are:",["Blue and hot","*Red and cool (<3,500 K)","Yellow and medium","White and very hot"],"Coolest main spectral type."),
     ("Luminosity is measured in:",["Meters","Kilograms","*Solar luminosities (L☉) or watts","Kelvin"],"Energy output per second."),
     ("Absolute magnitude measures a star's brightness at a standard distance of:",["1 AU","1 light-year","*10 parsecs","100 parsecs"],"Intrinsic brightness."),
     ("Apparent magnitude depends on:",["Only luminosity","*Both luminosity and distance from the observer","Only distance","Only color"],"Two factors."),
     ("Stellar parallax decreases with:",["Closer distance","*Greater distance (farther stars show smaller parallax shifts)","Lower temperature","Higher luminosity"],"p = 1/d."),
     ("A star with a parallax of 0.1 arcseconds is at a distance of:",["0.1 parsecs","1 parsec","*10 parsecs","100 parsecs"],"d = 1/p = 1/0.1 = 10 pc."),
     ("The most luminous stars can be over _____ times the Sun's luminosity.",["10","1,000","*1,000,000","10"],"Hypergiants are enormously luminous."),
     ("The faintest red dwarfs have luminosities roughly:",["Equal to the Sun","*0.0001 L☉ or less","10 L☉","100 L☉"],"Very dim."),
     ("A star's color indicates its:",["Age primarily","Distance","*Surface temperature (blue = hot, red = cool)","Mass only"],"Planck spectrum peak shifts with temperature."),
     ("The relationship L = 4πR²σT⁴ connects:",["Only mass and luminosity","*Luminosity, radius, and temperature","Only distance and brightness","Only color and size"],"Stefan-Boltzmann law."),
     ("A star with the same temperature as the Sun but 100× its radius would be _____ times more luminous.",["100","*10,000 (100² = 10,000)","1,000","10"],"L ∝ R²."),
     ("Stellar masses range from about:",["0.5 to 2 M☉","*~0.08 to ~300 M☉","1 to 10 M☉","Only 1 M☉"],"Below 0.08 M☉ → brown dwarf."),
     ("The mass-luminosity relation for main sequence stars is approximately:",["L ∝ M","L ∝ M²","*L ∝ M^3.5 (luminosity increases rapidly with mass)","L ∝ M⁰·⁵"],"Small mass increase → large luminosity increase."),
     ("Distance to nearby stars is primarily measured using:",["Radar","*Stellar parallax (trigonometric method)","Only brightness","Sound waves"],"Geometric method."),
     ("One parsec equals approximately:",["1 light-year","*3.26 light-years","10 light-years","100 light-years"],"Parallax of 1 arcsecond."),
     ("Binary star systems are useful for determining:",["Color","*Stellar masses (from orbital dynamics using Kepler's laws)","Only distance","Nothing"],"Orbits reveal masses."),
     ("Understanding stellar properties is the foundation of:",["Nothing","*Stellar astrophysics, the HR diagram, and understanding stellar evolution","Only naming stars","Only navigation"],"Core knowledge.")]
)
lessons[k]=v

# 5.2
k,v = build_lesson(5,2,"Hertzsprung-Russell Diagram",
    "<h3>Hertzsprung-Russell (HR) Diagram</h3>"
    "<p>Plots stars by <b>luminosity</b> (y-axis, increasing upward) vs <b>temperature</b> (x-axis, decreasing rightward → hot on left, cool on right).</p>"
    "<h4>Key Regions</h4>"
    "<ul><li><b>Main Sequence:</b> Diagonal band; ~90% of stars; fusing H to He. Hotter/more-massive stars at upper left; cooler/less-massive at lower right.</li>"
    "<li><b>Red Giants/Supergiants:</b> Upper right; large, cool, luminous (L ∝ R², so huge R compensates for low T).</li>"
    "<li><b>White Dwarfs:</b> Lower left; small, hot, dim (small R despite high T).</li></ul>",
    [("HR Diagram","Plot of luminosity vs temperature; reveals evolutionary stages and stellar classes."),
     ("Main Sequence","Diagonal band on the HR diagram where stars fuse hydrogen; ~90% of all stars."),
     ("Red Giant Region","Upper-right of HR diagram; cool but very luminous stars (large radius)."),
     ("White Dwarf Region","Lower-left of HR diagram; hot but dim stars (very small radius)."),
     ("Instability Strip","Vertical region on the HR diagram where pulsating variable stars (e.g., Cepheids) are found.")],
    [("The HR diagram plots _____ on the y-axis and _____ on the x-axis.",["Mass vs distance","*Luminosity vs temperature (or spectral type)","Size vs age","Color vs mass"],"Core axes."),
     ("On the HR diagram, temperature increases:",["Upward","Downward","To the right","*To the left (conventional)"],"Hot on the left, cool on the right."),
     ("The main sequence runs from:",["Upper right to lower left","*Upper left (hot, luminous) to lower right (cool, dim)","Horizontally","Vertically"],"Diagonal band."),
     ("Approximately _____ of all stars are on the main sequence.",["10%","50%","*~90%","100%"],"Most stars are in their hydrogen-burning phase."),
     ("Where on the HR diagram are red giants?",["Lower left","Lower right","*Upper right (cool but very luminous)","Center"],"Large radius → high luminosity despite low T."),
     ("Where on the HR diagram are white dwarfs?",["Upper right","Upper left","*Lower left (hot but very dim)","Center"],"Small radius → low luminosity despite high T."),
     ("A star at the upper-left of the main sequence is:",["Cool and dim","*Hot and luminous (massive O/B-type stars)","Cool and luminous","Hot and dim"],"Most massive MS stars."),
     ("A star at the lower-right of the main sequence is:",["Hot and luminous","*Cool and dim (low-mass M-type red dwarfs)","Large and bright","None exist there"],"Least massive MS stars."),
     ("The Sun is located:",["Upper left","Lower left","*Roughly in the middle of the main sequence (G2, ~5,800 K, 1 L☉)","Upper right"],"Average main sequence star."),
     ("The HR diagram was independently created by:",["Newton and Einstein","*Ejnar Hertzsprung and Henry Norris Russell (early 1900s)","Kepler and Galileo","Hubble and Slipher"],"Named after both astronomers."),
     ("A star that moves off the main sequence to the upper right is becoming a:",["White dwarf","*Red giant (expanding and cooling)","Neutron star","Black hole"],"Post-main-sequence evolution."),
     ("Cepheid variable stars are found in the:",["Main sequence","White dwarf region","*Instability strip (vertical region crossing the HR diagram)","Lower right"],"Pulsating stars."),
     ("The HR diagram reveals that luminosity and temperature are _____ for main sequence stars.",["Unrelated","*Correlated (hotter MS stars are more luminous)","Inversely related on MS","Random"],"Positive correlation on the MS."),
     ("A blue supergiant would be located:",["Lower right","*Upper left (extremely hot and luminous)","Lower left","Center"],"Hottest and most luminous."),
     ("A red dwarf would be located:",["Upper right","Upper left","*Lower right (cool and dim)","Lower left"],"Coolest main sequence stars."),
     ("If you know a star's position on the HR diagram, you can estimate its:",["Only color","*Temperature, luminosity, approximate size, and evolutionary stage","Only mass","Nothing"],"Very informative."),
     ("The HR diagram is one of the most important tools in astronomy because:",["It's pretty","*It organizes stars by observable properties and reveals patterns of stellar evolution","It's simple","It's historical only"],"Foundational tool."),
     ("Stars spend most of their lives on the main sequence because:",["They don't evolve","*Hydrogen fusion is the longest-lasting phase; post-MS stages are much shorter","Main sequence is the only phase","They are stuck"],"H → He is the most stable energy source."),
     ("The color of a star corresponds to its position along the _____ axis of the HR diagram.",["y (luminosity)","*x (temperature/spectral type)","Neither axis","Both axes equally"],"Temperature determines color."),
     ("Mastering the HR diagram is essential for AP astronomy because:",["It's easy points","*It connects stellar properties, classification, and evolution in a single framework","It's optional","It's only historical"],"Central organizing concept.")]
)
lessons[k]=v

# 5.3
k,v = build_lesson(5,3,"Star Formation (Nebulae)",
    "<h3>Star Formation</h3>"
    "<h4>Molecular Clouds</h4>"
    "<p>Stars form in cold, dense molecular clouds (giant molecular clouds, GMCs). Composed of H₂, He, and dust. Triggered by shockwaves (supernovae, cloud collisions) → gravitational collapse → fragmentation.</p>"
    "<h4>Protostars</h4>"
    "<p>Collapsing fragment heats up → protostar embedded in a disk. When core reaches ~10 million K → hydrogen fusion begins → star joins the main sequence.</p>"
    "<h4>T Tauri Stars</h4>"
    "<p>Young, pre-main-sequence stars with strong stellar winds and jets; variable brightness; surrounded by disks that may form planets.</p>",
    [("Molecular Cloud","Cold, dense region of gas (mostly H₂) and dust where stars form; also called stellar nurseries."),
     ("Protostar","Collapsing core of gas and dust that hasn't yet started hydrogen fusion; heated by gravitational contraction."),
     ("T Tauri Star","Young, pre-main-sequence star exhibiting variability, strong winds, and a surrounding protoplanetary disk."),
     ("Jeans Mass","Minimum mass of a gas cloud needed for gravitational collapse to overcome thermal pressure."),
     ("Herbig-Haro Object","Small, bright nebulosity produced by jets from protostars hitting surrounding gas.")],
    [("Stars form in:",["Outer space vacuum","*Cold, dense molecular clouds (stellar nurseries)","The Sun's corona","Galaxy centers only"],"Molecular clouds are star factories."),
     ("Molecular clouds are primarily composed of:",["Oxygen","*Molecular hydrogen (H₂), helium, and trace dust","Iron","Carbon dioxide"],"H₂ dominant."),
     ("Gravitational collapse of a cloud can be triggered by:",["Nothing","*Supernova shockwaves, cloud collisions, or density perturbations","Only gravity","Only magnetic fields"],"External triggers compress gas."),
     ("A protostar generates heat through:",["Nuclear fusion","*Gravitational contraction (potential energy → thermal energy)","Chemical combustion","Electricity"],"Not yet fusing hydrogen."),
     ("A protostar becomes a main-sequence star when:",["It reaches a certain size","*Its core temperature reaches ~10 million K, igniting hydrogen fusion","It stops collapsing","It cools down"],"Fusion onset defines a star."),
     ("The Jeans mass determines:",["A star's color","*The minimum cloud mass needed for gravitational collapse to begin","A star's luminosity","A star's age"],"Critical threshold."),
     ("T Tauri stars are:",["Old, dying stars","*Young, pre-main-sequence stars with variability and strong stellar winds","White dwarfs","Main sequence stars"],"Active, young stars."),
     ("Herbig-Haro objects are produced by:",["Supernovae","*Bipolar jets from protostars colliding with surrounding gas","Galaxy mergers","Comets"],"Dramatic protostellar outflows."),
     ("Protoplanetary disks around young stars can form:",["Only dust","*Planets, moons, asteroids, and comets","Stars","Galaxies"],"Planet formation."),
     ("The Orion Nebula (M42) is a famous example of:",["A planetary nebula","*An active star-forming region","A supernova remnant","A galaxy"],"Visible stellar nursery."),
     ("The Pillars of Creation (Eagle Nebula) show:",["Dead stars","*Columns of gas and dust where new stars are forming","Black holes","Galaxy arms"],"Iconic Hubble image."),
     ("More massive stars form _____ than less massive stars.",["Slower","*Faster (more gravitational compression, quicker collapse)","At the same rate","Only in different galaxies"],"High-mass stars form and evolve quickly."),
     ("Brown dwarfs are:",["Failed planets","*Sub-stellar objects (<0.08 M☉) that failed to reach fusion temperature","Dead stars","Neutron stars"],"Not massive enough to sustain H fusion."),
     ("Star formation efficiency in molecular clouds is typically:",["100%","*~1–10% (most gas doesn't form stars)","50%","0%"],"Low efficiency."),
     ("Infrared telescopes are critical for studying star formation because:",["Stars are cold","*Dust in molecular clouds blocks visible light but is transparent to infrared","They are cheaper","They are on the ground"],"See through dust."),
     ("The initial mass function (IMF) describes:",["How stars move","*The distribution of stellar masses at formation — low-mass stars are far more common","Star colors","Star distances"],"Many small stars, few massive ones."),
     ("Stellar winds from massive young stars can:",["Do nothing","*Blow away remaining gas, halting further star formation in the vicinity","Create stars","Form planets"],"Feedback regulates star formation."),
     ("Multiple star systems often form because:",["Stars merge later","*Cloud fragments produce several protostars in close proximity","Only one star forms per cloud","Gravity doesn't fragment"],"Binary and multiple systems common."),
     ("Understanding star formation helps us understand:",["Nothing about Earth","*The origin of our solar system, galaxy evolution, and the chemical enrichment of the universe","Only bright nebulae","Only astronomy"],"Connects to many topics."),
     ("The timescale for a Sun-like star to form is approximately:",["1 year","100 years","*~50 million years (from cloud collapse to main sequence)","10 billion years"],"Relatively short cosmically.")]
)
lessons[k]=v

# 5.4
k,v = build_lesson(5,4,"Main Sequence Stars",
    "<h3>Main Sequence Stars</h3>"
    "<p>Stars spend ~90% of their lives on the main sequence, fusing hydrogen to helium in their cores. The main sequence is a <b>mass sequence</b>: mass determines temperature, luminosity, color, and lifetime.</p>"
    "<h4>Mass-Luminosity Relation</h4>"
    "<p>L ∝ M^3.5 — a star twice the Sun's mass is ~11× more luminous.</p>"
    "<h4>Lifetime</h4>"
    "<p>t ∝ M/L ∝ M^(−2.5). More massive stars burn fuel faster → shorter lives. A 10 M☉ star lives ~20 million years; the Sun ~10 billion years; a 0.1 M☉ red dwarf ~trillions of years.</p>",
    [("Main Sequence","Evolutionary phase where stars fuse hydrogen; longest phase of a star's life (~90%)."),
     ("Mass-Luminosity Relation","L ∝ M^3.5 for main sequence stars; higher mass = dramatically higher luminosity."),
     ("Stellar Lifetime","Time on the main sequence; t ∝ M/L ∝ M^−2.5; massive stars live shorter lives."),
     ("Red Dwarf","Low-mass (< 0.5 M☉), cool M-type main sequence star; extremely long-lived and most common star type."),
     ("Hydrostatic Equilibrium","Balance between gravity (inward) and radiation/gas pressure (outward) in a stable star.")],
    [("Stars spend approximately _____ of their total lives on the main sequence.",["10%","50%","*~90%","100%"],"Longest evolutionary phase."),
     ("On the main sequence, a star's mass determines its:",["Nothing","*Temperature, luminosity, color, size, and lifetime","Only color","Only distance"],"Mass is the key parameter."),
     ("Using L ∝ M^3.5, a star with 2 M☉ has a luminosity of approximately:",["2 L☉","4 L☉","*~11.3 L☉ (2^3.5 ≈ 11.3)","100 L☉"],"Rapid increase with mass."),
     ("A main-sequence star with 10 M☉ has a luminosity of approximately:",["10 L☉","100 L☉","*~3,162 L☉ (10^3.5)","1 million L☉"],"Very luminous."),
     ("The Sun's main-sequence lifetime is approximately:",["1 million years","100 million years","*~10 billion years","1 trillion years"],"~4.6 Gyr old, ~5 Gyr remaining."),
     ("A 10 M☉ star's main-sequence lifetime is approximately:",["10 billion years","1 billion years","*~20 million years","1 million years"],"Burns fuel fast despite having more."),
     ("A 0.1 M☉ red dwarf's lifetime is:",["10 billion years","100 billion years","*Trillions of years (much longer than the current age of the universe)","1 million years"],"Extremely efficient fuel use."),
     ("Red dwarfs are the most common type of star in the galaxy because:",["They're the hottest","*Low-mass stars form far more frequently (IMF) and live extremely long","They're the brightest","They're the biggest"],"Abundant and long-lived."),
     ("Hydrostatic equilibrium means:",["Stars are falling apart","*Gravitational compression is balanced by outward pressure from fusion energy","Stars don't move","Stars are getting bigger"],"Stable balance."),
     ("If fusion in a main sequence star's core decreases, the star:",["Stays the same","*Contracts (gravity wins temporarily until core heats up and fusion rate adjusts)","Explodes immediately","Becomes a black hole"],"Self-regulating process."),
     ("The main sequence is really a _____ sequence.",["Color","Size","*Mass (mass determines position on the MS)","Age"],"Fundamental parameter."),
     ("Proxima Centauri (nearest star to the Sun) is a:",["Blue giant","*Red dwarf (M-type, ~0.12 M☉)","White dwarf","Neutron star"],"Common star type."),
     ("Sirius A is a main-sequence star of type:",["M","G","*A (~2 M☉, blue-white)","O"],"Brightest star in the night sky."),
     ("Massive main-sequence stars are _____ common and _____ lived.",["Very; long","*Rare; short (burn through hydrogen quickly)","Common; short","Rare; long"],"Few and brief."),
     ("The zero-age main sequence (ZAMS) is:",["Where stars die","*The position on the HR diagram where stars first begin hydrogen fusion","The oldest stars","A type of galaxy"],"Starting line for main sequence life."),
     ("Main-sequence stars convert hydrogen to helium via:",["The p-p chain only","The CNO cycle only","*The p-p chain (low mass) or CNO cycle (high mass), or both","Fission"],"Depending on core temperature."),
     ("A main-sequence star gradually becomes _____ luminous over its MS lifetime because:",["Less","*Slightly more (core becomes denser with He ash, temperature rises to maintain equilibrium)","Exactly the same","Infinitely"],"Slow increase in luminosity."),
     ("When a main-sequence star exhausts core hydrogen, it:",["Stays on the MS","*Evolves off the main sequence (expands to become a red giant)","Becomes a white dwarf immediately","Disappears"],"Post-main-sequence evolution begins."),
     ("Studying main-sequence stars is important because:",["Nothing useful","*They are the basis for understanding stellar structure, evolution, and the HR diagram","Only for naming","Only for navigation"],"Foundation of stellar astrophysics."),
     ("The Sun will remain on the main sequence for approximately _____ more years.",["100 million","1 billion","*~5 billion","10 billion"],"Total ~10 Gyr lifetime, currently ~4.6 Gyr.")]
)
lessons[k]=v

# 5.5
k,v = build_lesson(5,5,"Red Giants & White Dwarfs",
    "<h3>Red Giants &amp; White Dwarfs</h3>"
    "<h4>Red Giant Phase</h4>"
    "<p>After core H is exhausted: core contracts → heats → H-shell burning begins → outer layers expand and cool → red giant. Core may reach ~100 million K → helium flash → helium fusion begins (triple-alpha process: 3 He → C).</p>"
    "<h4>White Dwarfs</h4>"
    "<p>End state for low/medium-mass stars (<8 M☉). After losing outer layers (planetary nebula), the hot, dense core remains. Supported by electron degeneracy pressure. Chandrasekhar limit: 1.4 M☉ max.</p>",
    [("Red Giant","Post-main-sequence star with expanded, cooled outer layers and a contracting, hot core."),
     ("Helium Flash","Explosive onset of He fusion in the degenerate core of a low-mass red giant."),
     ("Triple-Alpha Process","Fusion of three helium-4 nuclei into carbon-12; occurs in red giant cores."),
     ("Planetary Nebula","Shell of gas expelled by a dying low-mass star; reveals the hot white dwarf core."),
     ("Chandrasekhar Limit","Maximum mass of a white dwarf (~1.4 M☉); above this, electron degeneracy cannot support it.")],
    [("A star becomes a red giant when:",["It runs out of all fuel","*Core hydrogen is exhausted; hydrogen shell burning begins and outer layers expand","It fuses iron","It collides with another star"],"Shell burning drives expansion."),
     ("In a red giant, the core is _____ while the outer layers are _____.",["Cool; hot","*Hot and contracting; cool and expanding","Both cool","Both hot"],"Opposite behaviors."),
     ("The helium flash occurs in low-mass stars because:",["Helium fuses gradually","*Helium fusion ignites explosively in a degenerate core (doesn't expand to regulate itself)","The core cools","Nothing special happens"],"Degeneracy prevents self-regulation."),
     ("The triple-alpha process fuses:",["Hydrogen to helium","*Three helium-4 nuclei into carbon-12","Carbon to oxygen","Iron to gold"],"Named for 3 alpha particles (He nuclei)."),
     ("After helium burning, a low-mass star's core is primarily:",["Hydrogen","Helium","*Carbon and oxygen","Iron"],"C/O core."),
     ("A planetary nebula is produced when:",["A planet explodes","*A dying low-mass star's outer layers are expelled, revealing the hot core","A supernova occurs","A galaxy collapses"],"Misleading name (no planets involved)."),
     ("The Ring Nebula (M57) is an example of:",["A galaxy","*A planetary nebula","A supernova remnant","A molecular cloud"],"Beautiful expelled shell."),
     ("A white dwarf is supported against gravity by:",["Nuclear fusion","Thermal pressure","*Electron degeneracy pressure (Pauli exclusion principle)","Magnetic fields"],"Quantum mechanical support."),
     ("The Chandrasekhar limit is approximately:",["0.5 M☉","*1.4 M☉","3 M☉","10 M☉"],"Maximum white dwarf mass."),
     ("A typical white dwarf has a size comparable to:",["The Sun","Jupiter","*Earth (but with ~1 M☉)","A city"],"Incredibly dense."),
     ("White dwarf density is approximately:",["1 g/cm³","*~10⁶ g/cm³ (1 million g/cm³)","10 g/cm³","10¹⁵ g/cm³"],"Extremely compact."),
     ("White dwarfs cool over time because:",["They fuse hydrogen","*They have no energy source (no fusion); they slowly radiate stored thermal energy","They absorb energy","They grow"],"Cooling remnants."),
     ("A nova occurs when:",["A star is born","*A white dwarf in a binary system accretes material from a companion; surface fusion eruption occurs","A star dies","Two galaxies merge"],"Thermonuclear explosion on the surface."),
     ("A Type Ia supernova occurs when a white dwarf:",["Cools down","*Exceeds the Chandrasekhar limit (accretion from companion) → catastrophic thermonuclear explosion","Becomes a black hole","Fuses helium"],"Standardizable candle."),
     ("Type Ia supernovae are important in cosmology as:",["Random events","*Standard candles for measuring cosmic distances (uniform peak brightness)","Useless","Only theoretical"],"Key distance indicator."),
     ("The Sun will eventually become:",["A black hole","A neutron star","*A white dwarf (after red giant and planetary nebula phases)","A supergiant"],"Not massive enough for other fates."),
     ("Sirius B is a famous:",["Red giant","Main sequence star","*White dwarf (companion to Sirius A)","Neutron star"],"First white dwarf discovered."),
     ("Asymptotic giant branch (AGB) stars are:",["Young stars","*Late-stage red giants undergoing thermal pulses before becoming planetary nebulae","White dwarfs","Main sequence stars"],"Final red giant phase."),
     ("The fate of a star is primarily determined by its:",["Color","Distance","*Initial mass","Temperature only"],"Mass dictates evolution."),
     ("Understanding red giants and white dwarfs is important for:",["Nothing","*Tracing stellar evolution, understanding element production, and calibrating cosmic distances","Only naming stars","Only pretty nebulae"],"Core stellar astrophysics.")]
)
lessons[k]=v

# 5.6
k,v = build_lesson(5,6,"Supernovae & Neutron Stars",
    "<h3>Supernovae &amp; Neutron Stars</h3>"
    "<h4>Core-Collapse Supernova (Type II)</h4>"
    "<p>Massive stars (>8 M☉) → fusion builds up iron core → iron cannot release energy via fusion → core collapses in milliseconds → rebounds → supernova explosion. Peak luminosity = entire galaxy. Creates elements heavier than iron (r-process nucleosynthesis).</p>"
    "<h4>Neutron Stars</h4>"
    "<p>Remnant core 1.4–3 M☉; ~20 km diameter; density ~10¹⁴ g/cm³. Supported by neutron degeneracy pressure. Pulsars: rapidly rotating neutron stars emitting radio beams.</p>",
    [("Core-Collapse Supernova","Explosion of a massive star (>8 M☉) when its iron core collapses; Type II supernova."),
     ("Neutron Star","Ultra-dense remnant of a supernova; ~20 km; supported by neutron degeneracy pressure."),
     ("Pulsar","Rotating neutron star emitting beams of radiation; observed as periodic pulses."),
     ("r-Process Nucleosynthesis","Rapid neutron capture in supernovae/mergers; creates heavy elements like gold, platinum, uranium."),
     ("Supernova Remnant","Expanding shell of gas and dust from a supernova explosion (e.g., Crab Nebula).")],
    [("A core-collapse supernova occurs in stars with initial mass greater than:",["1 M☉","5 M☉","*~8 M☉","50 M☉"],"Threshold for iron core formation."),
     ("Iron is the end of the fusion chain because:",["It's too heavy","*Fusing iron absorbs energy rather than releasing it (no net energy gain)","It's too light","It's not abundant"],"Binding energy per nucleon peaks at iron."),
     ("The core collapse takes approximately:",["Years","*Milliseconds (fraction of a second)","Hours","Days"],"Catastrophically fast."),
     ("At peak brightness, a supernova can outshine:",["A few stars","*An entire galaxy (billions of stars)","Only one star","Nothing"],"Extraordinarily luminous."),
     ("Elements heavier than iron are primarily created in:",["Normal fusion","*Supernovae and neutron star mergers (r-process nucleosynthesis)","The Big Bang","Planet cores"],"Extreme conditions needed."),
     ("After a Type II supernova, the core remnant can become:",["A white dwarf","*A neutron star (1.4–3 M☉) or a black hole (>3 M☉)","Nothing","A new star"],"Depends on remnant mass."),
     ("A neutron star has a diameter of approximately:",["1,000 km","100 km","*~20 km","1 km"],"City-sized."),
     ("Neutron star density is approximately:",["10⁶ g/cm³","*~10¹⁴ g/cm³ (nuclear density)","1 g/cm³","10²⁰ g/cm³"],"A teaspoon weighs ~10¹² kg."),
     ("Neutron stars are supported by:",["Electron degeneracy pressure","Thermal pressure","*Neutron degeneracy pressure","Magnetic fields"],"Stronger than electron degeneracy."),
     ("A pulsar is a neutron star that:",["Doesn't rotate","*Rotates rapidly and emits beams of radio waves that sweep past Earth like a lighthouse","Absorbs all light","Is invisible"],"Lighthouse model."),
     ("The Crab Nebula is the remnant of a supernova observed in:",["1900","*1054 AD (recorded by Chinese astronomers)","1610","500 BC"],"Historic supernova."),
     ("The Crab Pulsar at the center of the Crab Nebula rotates approximately:",["Once per hour","Once per minute","*~30 times per second","Once per year"],"Very fast rotation."),
     ("Millisecond pulsars rotate hundreds of times per second due to:",["Original rotation","*Accretion spin-up from a binary companion ('recycled' pulsars)","Magnetic fields","Explosions"],"Spun up by mass transfer."),
     ("SN 1987A was significant because:",["It was the first supernova","*It was the closest supernova in ~400 years (in the Large Magellanic Cloud) and neutrinos were detected","It created a black hole for sure","It was in our galaxy"],"First neutrino detection from a supernova."),
     ("Nucleosynthesis in supernovae seeded the universe with:",["Only hydrogen","*Heavy elements (carbon, oxygen, iron, gold, uranium) that form planets and life","Only helium","Nothing"],"'We are star stuff' — Carl Sagan."),
     ("Neutron star mergers have been detected via:",["Only light","*Both gravitational waves and electromagnetic radiation (GW170817 in 2017)","Only sound","Only X-rays"],"Multi-messenger astronomy breakthrough."),
     ("GW170817 confirmed that neutron star mergers produce:",["Only gravitational waves","*Heavy elements via r-process nucleosynthesis (including gold and platinum)","Only light","Nothing"],"Kilonova observation."),
     ("Magnetars are neutron stars with:",["Weak magnetic fields","*Extremely strong magnetic fields (~10⁹–10¹¹ T, strongest in the universe)","No magnetic field","Normal fields"],"Extraordinary field strength."),
     ("Supernova remnants enrich the interstellar medium with:",["Only gas","*Heavy elements that are incorporated into new stars, planets, and eventually life","Only dust","Nothing"],"Chemical enrichment cycle."),
     ("Understanding supernovae and neutron stars is crucial for:",["Nothing","*Explaining element origins, gravitational wave sources, and extreme physics","Only history","Only theory"],"Foundational astrophysics.")]
)
lessons[k]=v

# 5.7
k,v = build_lesson(5,7,"Black Holes",
    "<h3>Black Holes</h3>"
    "<h4>Formation</h4>"
    "<p>When a stellar remnant exceeds ~3 M☉ (Tolman-Oppenheimer-Volkoff limit), nothing can halt collapse → singularity. Event horizon: boundary beyond which nothing (not even light) can escape. Schwarzschild radius: r_s = 2GM/c².</p>"
    "<h4>Types</h4>"
    "<ul><li><b>Stellar:</b> 3–100 M☉; from massive star collapse.</li>"
    "<li><b>Supermassive:</b> 10⁶–10¹⁰ M☉; centers of galaxies (Sgr A* in Milky Way ≈ 4 million M☉).</li>"
    "<li><b>Intermediate:</b> 10²–10⁵ M☉; evidence growing.</li></ul>",
    [("Event Horizon","Boundary around a black hole beyond which escape is impossible; the 'point of no return.'"),
     ("Schwarzschild Radius","Radius of the event horizon: r_s = 2GM/c²; defines the size of a non-rotating black hole."),
     ("Singularity","Point of theoretically infinite density at the center of a black hole (classical GR prediction)."),
     ("Accretion Disk","Disk of infalling matter spiraling around a black hole; heats up and emits X-rays."),
     ("Sagittarius A* (Sgr A*)","Supermassive black hole at the Milky Way's center; ~4 million M☉; imaged by the EHT.")],
    [("A stellar black hole forms from stars with remnant masses greater than:",["1.4 M☉","*~3 M☉ (Tolman-Oppenheimer-Volkoff limit)","10 M☉","100 M☉"],"Above this, neutron degeneracy fails."),
     ("The event horizon is:",["The center of a black hole","*The boundary beyond which nothing can escape (not even light)","The accretion disk","A galaxy boundary"],"Point of no return."),
     ("The Schwarzschild radius for a black hole is given by:",["r = GM/c","*r_s = 2GM/c²","r = mc²","r = G/c"],"Event horizon radius."),
     ("For a 10 M☉ black hole, the Schwarzschild radius is approximately:",["1 km","*~30 km","1,000 km","1 AU"],"~3 km per solar mass."),
     ("Light cannot escape from within the event horizon because:",["The black hole absorbs it","*Escape velocity exceeds the speed of light inside the event horizon","It's too dark","The black hole is solid"],"v_esc > c."),
     ("Accretion disks around black holes emit:",["Visible light only","*Intense X-rays (matter heated to millions of degrees by friction and compression)","Radio only","Nothing"],"X-ray binary sources."),
     ("Supermassive black holes (SMBHs) are found:",["In empty space","Orbiting stars","*At the centers of most galaxies","Only in the Milky Way"],"Nearly universal in galaxy centers."),
     ("Sagittarius A* (Sgr A*) has a mass of approximately:",["1 M☉","1,000 M☉","*~4 million M☉","1 billion M☉"],"Milky Way's central SMBH."),
     ("The Event Horizon Telescope (EHT) achieved the first image of:",["A star","*A black hole's shadow (M87* in 2019, Sgr A* in 2022)","A planet","A nebula"],"Historic achievement."),
     ("The EHT works by:",["Using one telescope","*Combining radio telescopes worldwide to form an Earth-sized virtual telescope (VLBI)","Using Hubble","Only infrared"],"Very Long Baseline Interferometry."),
     ("Hawking radiation is:",["Light from accretion disks","*Theoretical radiation emitted by black holes due to quantum effects near the event horizon","Sound from black holes","Not a real concept"],"Black holes slowly evaporate (over vast timescales)."),
     ("Gravitational time dilation near a black hole means:",["Time speeds up","*Time passes slower near the event horizon as observed from far away","Time stops everywhere","Nothing happens to time"],"General relativity prediction."),
     ("Spaghettification is:",["A cooking term","*The stretching of objects by extreme tidal forces near a black hole","A type of galaxy","A spectral line"],"Tidal forces stretch you like spaghetti."),
     ("Quasars are powered by:",["Stars","*Supermassive black holes actively accreting material at galaxy centers (Active Galactic Nuclei)","Nuclear bombs","Dark matter"],"Most luminous objects in the universe."),
     ("Gravitational waves from merging black holes were first detected by:",["Hubble","*LIGO (Laser Interferometer Gravitational-Wave Observatory) in 2015 (GW150914)","Chandra","Radio telescopes"],"Nobel Prize discovery."),
     ("Intermediate-mass black holes (10²–10⁵ M☉) are:",["Well-understood","*Still being studied; evidence is growing but fewer confirmed detections","Nonexistent","Everywhere"],"Filling the gap between stellar and supermassive."),
     ("Black holes do NOT:",["Have gravity","Bend light","Exist","* 'Suck' everything in — objects at a safe distance orbit normally, just as around any mass"],"Only dangerous inside the event horizon."),
     ("Information paradox refers to:",["Lost data on computers","*The question of whether information falling into a black hole is truly destroyed (challenges quantum mechanics)","Nothing important","A coding problem"],"Major unsolved problem in physics."),
     ("Binary black hole mergers produce:",["Only light","*Gravitational waves (ripples in spacetime) that LIGO/Virgo can detect","Only heat","Nothing"],"Gravitational-wave astronomy."),
     ("Black holes connect:",["Nothing","*General relativity, quantum mechanics, galaxy evolution, and fundamental physics","Only astronomy","Only mathematics"],"At the intersection of major physics questions.")]
)
lessons[k]=v

# 5.8
k,v = build_lesson(5,8,"Case Studies in Stellar Observation",
    "<h3>Case Studies in Stellar Observation</h3>"
    "<h4>Betelgeuse's Great Dimming (2019–2020)</h4>"
    "<p>Red supergiant in Orion dimmed significantly. Cause: likely a dust cloud ejected by the star partially blocking light. Shows variable behavior of evolved massive stars.</p>"
    "<h4>TRAPPIST-1</h4>"
    "<p>Ultra-cool red dwarf with 7 Earth-sized planets, 3 in habitable zone. Discovered using transit method. Key target for JWST atmospheric studies.</p>"
    "<h4>GW170817</h4>"
    "<p>First observation of a neutron star merger via both gravitational waves and electromagnetic radiation → 'multi-messenger astronomy.'</p>",
    [("Betelgeuse","Red supergiant in Orion, ~700 light-years away; candidate for a future supernova."),
     ("TRAPPIST-1","Ultra-cool red dwarf with 7 Earth-sized planets; key target for habitability studies."),
     ("GW170817","First neutron star merger detected by LIGO/Virgo AND observed electromagnetically; confirmed r-process nucleosynthesis."),
     ("Multi-Messenger Astronomy","Observing cosmic events using multiple signals: light, gravitational waves, neutrinos, cosmic rays."),
     ("Transit Method","Detection of exoplanets by measuring the dimming of a star as a planet passes in front of it.")],
    [("Betelgeuse's great dimming (2019–2020) was most likely caused by:",["An approaching supernova","*A dust cloud ejected from the star partially obscuring it","A planet transit","Instrument error"],"Surface mass ejection → dust formation."),
     ("Betelgeuse is classified as a:",["Main sequence star","White dwarf","*Red supergiant","Neutron star"],"One of the largest known stars."),
     ("If Betelgeuse exploded as a supernova, it would:",["Destroy Earth","*Be visible in daylight for weeks but at ~700 light-years, would not harm Earth","Not be noticed","Turn into a planet"],"Safe distance."),
     ("TRAPPIST-1 is a:",["G-type star","*Ultra-cool M-type red dwarf","Blue supergiant","White dwarf"],"Very cool and small."),
     ("TRAPPIST-1 has _____ known planets.",["2","4","*7","10"],"All roughly Earth-sized."),
     ("The transit method detects exoplanets by measuring:",["Wobble of the star","*Periodic dimming of the star as a planet crosses in front of it","Color changes","Sound waves"],"Light curve dips."),
     ("TRAPPIST-1 is a prime target for JWST because:",["It's close to the Sun","*Its small size makes planet transits deeper and easier to study with transit spectroscopy","It's the largest star","It's a pulsar"],"Favorable star-to-planet size ratio."),
     ("GW170817 was groundbreaking because it was the first event observed with both:",["Light and sound","*Gravitational waves AND electromagnetic radiation (multi-messenger)","Telescopes and naked eye","Only gravitational waves"],"Multi-messenger astronomy milestone."),
     ("The electromagnetic counterpart of GW170817 was called a:",["Supernova","*Kilonova (relatively faint thermal emission from r-process nucleosynthesis)","Nova","Quasar"],"Heavy element formation visible."),
     ("GW170817 confirmed that neutron star mergers produce:",["Only energy","*Heavy elements like gold and platinum via the r-process","Only gravitational waves","Only light"],"Origin of heavy elements confirmed."),
     ("Eta Carinae is interesting because:",["It's a red dwarf","*It's a massive, unstable star that had a major eruption in the 1840s and may become a supernova","It's a white dwarf","It's the closest star"],"Luminous Blue Variable."),
     ("Tabby's Star (KIC 8462852) attracted attention due to:",["Its explosion","*Unusual, irregular dimming patterns initially unexplained (likely dust/comets)","Its proximity","Its pulses"],"Once speculated to be alien megastructures (not supported)."),
     ("The first exoplanet confirmed around a Sun-like star was:",["TRAPPIST-1b","*51 Pegasi b (1995, a hot Jupiter)","Earth","Kepler-442b"],"Nobel Prize awarded to Mayor and Queloz."),
     ("Cepheid variable stars are used as distance indicators because:",["They're always the same distance","*Their pulsation period is directly related to their luminosity (period-luminosity relation)","They're always the same color","They don't vary"],"Henrietta Leavitt's discovery."),
     ("RR Lyrae variables are similar to Cepheids but found in:",["Young star clusters","*Globular clusters and old stellar populations","Only galaxies","Only nebulae"],"Used for distances to old populations."),
     ("The radial velocity (Doppler wobble) method detects exoplanets by:",["Direct imaging","*Measuring the tiny shift in a star's spectrum caused by gravitational tugging from an orbiting planet","Transit dimming","Parallax"],"Complementary to transit method."),
     ("Direct imaging of exoplanets is:",["Easy","*Extremely challenging because planets are much fainter than their host stars","Impossible","Routine"],"Requires coronagraphs and advanced techniques."),
     ("Gaia (ESA) is mapping over a billion stars, providing:",["Only images","*Precise positions, distances (parallax), motions, and properties for a 3D map of the Milky Way","Only names","Only colors"],"Transformative survey mission."),
     ("These case studies show that modern astronomy is:",["Static","*A dynamic, rapidly advancing field with new discoveries transforming our understanding","Finished","Only theoretical"],"Active and exciting."),
     ("Stellar case studies connect to broader themes of:",["Nothing","*Stellar evolution, exoplanet science, fundamental physics, and the search for life","Only naming","Only observation"],"Rich interdisciplinary connections.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Astronomy Unit 5: wrote {len(lessons)} lessons")
