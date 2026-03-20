#!/usr/bin/env python3
"""Astronomy Unit 8 – Astrobiology & the Search for Life (7 lessons)."""
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

# 8.1
k,v = build_lesson(8,1,"Conditions for Life",
    "<h3>Conditions for Life</h3>"
    "<h4>Requirements</h4>"
    "<ul><li><b>Liquid water:</b> Universal solvent; essential for biochemistry.</li>"
    "<li><b>Energy source:</b> Sunlight, chemical energy (chemosynthesis), or geothermal.</li>"
    "<li><b>Organic molecules:</b> Carbon-based compounds (amino acids, nucleotides).</li>"
    "<li><b>Stable environment:</b> Sufficient time for evolution; protection from sterilizing events.</li></ul>"
    "<p>The <b>habitable zone</b> (Goldilocks zone) is the region around a star where liquid water could exist on a planet's surface. However, subsurface oceans (Europa, Enceladus) expand the concept of habitability.</p>",
    [("Habitable Zone","Region around a star where surface temperatures allow liquid water; also called the Goldilocks zone."),
     ("Liquid Water","Considered essential for life as we know it; excellent solvent for biochemical reactions."),
     ("Chemosynthesis","Process where organisms derive energy from chemical reactions (e.g., oxidizing hydrogen sulfide) rather than sunlight."),
     ("Organic Molecules","Carbon-based compounds (amino acids, sugars, lipids, nucleotides) — building blocks of life."),
     ("Panspermia","Hypothesis that life or its precursors could be distributed throughout the universe via meteorites or comets.")],
    [("The habitable zone is defined as the region where:",["Only plants can grow","*Liquid water can exist on a planet's surface (appropriate temperature range)","There is no radiation","Gravity is zero"],"Goldilocks zone."),
     ("Liquid water is considered essential for life because:",["It's blue","*It's an excellent solvent enabling biochemical reactions","It's cold","It's heavy"],"Universal biological solvent."),
     ("The three main requirements for life as we know it are:",["Only water","*Liquid water, energy source, and organic molecules","Only sunlight","Only oxygen"],"Basic habitability criteria."),
     ("Chemosynthesis is important because it shows that:",["Sunlight is always required","*Life can exist without sunlight, using chemical energy instead","Chemistry and life are unrelated","Only plants use it"],"Found at hydrothermal vents."),
     ("The habitable zone of a hotter star is _____ from the star compared to a cooler star.",["Closer","*Farther away","The same distance","Nonexistent"],"More luminous = zone pushed outward."),
     ("Europa and Enceladus expand our concept of habitability because:",["They have atmospheres","*They may have subsurface oceans (heated by tidal forces) — liquid water without surface sunlight","They are in the habitable zone","They have oxygen"],"Subsurface habitability."),
     ("Carbon is the basis of organic molecules because:",["It's abundant","*It can form four stable bonds with many elements, creating complex, diverse molecules","It's heavy","It's magnetic"],"Chemical versatility."),
     ("The Miller-Urey experiment (1952) demonstrated:",["Life creation","*That amino acids (precursors to life) can form from simple gases and energy (simulating early Earth conditions)","Nuclear fusion","Photosynthesis"],"Abiogenesis research."),
     ("Panspermia is the hypothesis that:",["Life exists everywhere","*Life's building blocks or microbes could travel between worlds via meteorites or comets","Only Earth has life","Life can't survive in space"],"Not proven but possible."),
     ("Extremophiles are relevant to astrobiology because:",["They're unusual","*They demonstrate life can thrive in conditions once thought impossible — expanding where we look for life","They're large","They need oxygen"],"Life in extreme conditions."),
     ("Mars is a target for life detection because:",["It's close","*It had liquid water in the past, has polar ice caps, and subsurface water may persist","It has oxygen","It's warm"],"Evidence of ancient water."),
     ("Biosignatures are:",["Photos of aliens","*Detectable signs of past or present life (certain gases, isotope ratios, chemical patterns)","Radio signals","Fossils only"],"What we search for."),
     ("Atmospheric biosignatures could include:",["Nitrogen only","*Oxygen, methane, and other gases in disequilibrium that may indicate biological activity","CO₂ only","Nothing"],"Chemical disequilibrium."),
     ("JWST can contribute to biosignature detection by:",["Landing on planets","*Analyzing exoplanet atmospheres via transit spectroscopy for potential biosignature gases","Sending probes","Visiting stars"],"Remote atmospheric analysis."),
     ("Titan is interesting for astrobiology because:",["It has oxygen","*It has complex organic chemistry, a thick atmosphere, and liquid methane/ethane — possible alternative biochemistry","It's warm","It's close to Earth"],"Different solvent possibility."),
     ("The Drake Equation estimates:",["Speed of light","*The number of communicating civilizations in the Milky Way (many uncertain variables)","Earth's age","Star brightness"],"Framework, not precise answer."),
     ("One challenge in defining 'life' for astrobiology is:",["It's easy","*We may not recognize life that uses different chemistry than Earth life","Everyone agrees","Only water-based life counts"],"Need flexible definitions."),
     ("Hydrothermal vents on the ocean floor support life through:",["Photosynthesis","*Chemosynthesis — bacteria oxidize chemicals (H₂S, methane) to produce energy","Wind power","Solar panels"],"Dark ecosystems."),
     ("The search for life focuses on 'follow the water' because:",["Water is rare","*Water is essential for all known life and its presence is the strongest habitability indicator","Water is blue","No reason"],"Primary search strategy."),
     ("Understanding conditions for life helps us:",["Nothing","*Prioritize where to search for life, design instruments, and interpret potential biosignatures","Only on Earth","Only for fun"],"Guides the search.")]
)
lessons[k]=v

# 8.2
k,v = build_lesson(8,2,"Extremophiles on Earth",
    "<h3>Extremophiles on Earth</h3>"
    "<p>Organisms thriving in extreme conditions that inform our search for extraterrestrial life:</p>"
    "<ul><li><b>Thermophiles:</b> >60°C environments (hot springs, hydrothermal vents; <i>Thermus aquaticus</i> — source of Taq polymerase for PCR).</li>"
    "<li><b>Psychrophiles:</b> Below 0°C (Antarctic ice, permafrost).</li>"
    "<li><b>Halophiles:</b> High salt concentrations (Dead Sea, salt mines).</li>"
    "<li><b>Acidophiles/Alkaliphiles:</b> Extreme pH environments.</li>"
    "<li><b>Radioresistant:</b> <i>Deinococcus radiodurans</i> survives 5,000× the lethal human dose of radiation.</li>"
    "<li><b>Endoliths:</b> Live inside rocks, kilometers underground.</li></ul>",
    [("Extremophile","Organism that thrives in physically or geochemically extreme conditions lethal to most life."),
     ("Thermophile","Organism thriving at temperatures >60°C; found in hot springs and hydrothermal vents."),
     ("Deinococcus radiodurans","Bacterium that survives extreme radiation (~5,000× human lethal dose); repairs its own DNA."),
     ("Tardigrade","Microscopic animal surviving extreme cold, heat, vacuum, radiation, and desiccation (cryptobiosis)."),
     ("Endolith","Organism living inside rocks or in pore spaces within minerals; found kilometers underground.")],
    [("Extremophiles are relevant to astrobiology because they:",["Are alien life","*Demonstrate that life can survive conditions similar to those on Mars, Europa, and Enceladus","Only exist in labs","Are extinct"],"Expands search parameters."),
     ("Thermophiles thrive at temperatures:",["Below 0°C","*Above 60°C (some above 100°C at hydrothermal vents)","Exactly 25°C","Any temperature"],"Hot-loving organisms."),
     ("Taq polymerase, used in PCR, comes from:",["Human cells","*Thermus aquaticus (a thermophile from hot springs)","Plants","Viruses"],"Biotechnology from extremophiles."),
     ("Psychrophiles thrive in:",["Hot environments","*Cold environments (below 0°C — Antarctic ice, permafrost)","Neutral environments","Dry environments"],"Cold-loving organisms."),
     ("Halophiles thrive in:",["Fresh water","*Extremely salty environments (Dead Sea, salt flats)","Pure water","Acidic environments"],"Salt-loving organisms."),
     ("Deinococcus radiodurans can withstand radiation doses that are:",["Equal to human tolerance","*~5,000 times the lethal dose for humans","Slightly above normal","Zero"],"Extreme DNA repair mechanisms."),
     ("Tardigrades (water bears) can survive:",["Only in water","*Extreme cold, heat, vacuum, radiation, desiccation, and even space exposure","Only on land","Only in the tropics"],"Remarkable resilience."),
     ("Endoliths live:",["On leaf surfaces","Only in water","*Inside rocks or in tiny pore spaces within minerals","Only in soil"],"Among the deepest life on Earth."),
     ("The discovery of extremophiles has expanded the concept of habitability to include:",["Only Earth-like planets","*Subsurface oceans, ice worlds, acidic environments, and high-radiation zones","Only hot planets","Only watery planets"],"Broadened search."),
     ("Chemolithoautotrophs obtain energy from:",["Sunlight","*Inorganic chemical reactions (oxidizing minerals, sulfur compounds, etc.)","Eating food","Wind"],"No light or organic matter needed."),
     ("Life has been found _____ km below Earth's surface.",["0.1","*Several km (~5 km or deeper in some studies)","100","Only at the surface"],"Deep biosphere."),
     ("Antarctic subglacial lakes like Lake Vostok are interesting because:",["They're warm","*They may harbor life isolated for millions of years under kilometers of ice — analog to Europa","They're empty","They're on the surface"],"Ice-covered habitats."),
     ("Acidophiles survive in pH as low as:",["7 (neutral)","5","*0 or near 0 (extremely acidic environments like acid mine drainage)","Only 6"],"Extremely acidic."),
     ("Alkaliphiles survive in pH as high as:",["7","*~12 or higher (extremely basic/alkaline environments like soda lakes)","8","Only 9"],"Extremely alkaline."),
     ("The discovery of life at deep-sea hydrothermal vents in 1977 was significant because:",["Vents are hot","*It proved complex ecosystems can thrive without sunlight, using chemosynthesis","Vents are deep","It was a coincidence"],"Paradigm shift."),
     ("Extremophile research helps design:",["Nothing","*Life-detection instruments for spacecraft and define where to look for life beyond Earth","Only medicine","Only food"],"Applied astrobiology."),
     ("Xerophiles thrive in:",["Wet environments","*Extremely dry environments (like the Atacama Desert — Mars analog)","Cold environments","Hot environments"],"Dry conditions."),
     ("The Atacama Desert is used as a Mars analog because:",["It's on Mars","*It's the driest place on Earth, with similar soil chemistry and UV exposure to Mars","It's cold","It's hot"],"Testing life-detection methods."),
     ("Barophiles (piezophiles) thrive under:",["Low pressure","*Extreme high pressure (deep ocean trenches, >1,000 atm)","Normal pressure","Vacuum"],"Pressure-loving."),
     ("Studying extremophiles teaches us that life is:",["Fragile","*Far more resilient and adaptable than once believed — it can thrive almost anywhere there's liquid water and energy","Only in oceans","Only on land"],"Life finds a way.")]
)
lessons[k]=v

# 8.3
k,v = build_lesson(8,3,"Search for Extraterrestrial Life",
    "<h3>Search for Extraterrestrial Life</h3>"
    "<h4>Strategies</h4>"
    "<ul><li><b>Mars:</b> Rovers (Curiosity, Perseverance) analyze soil, rock chemistry, and atmospheric gases. Signs of ancient water.</li>"
    "<li><b>Ocean Worlds:</b> Europa Clipper (Europa), Dragonfly (Titan), future Enceladus missions.</li>"
    "<li><b>Exoplanets:</b> JWST transit spectroscopy for biosignature gases (O₂, CH₄, H₂O, CO₂ in disequilibrium).</li>"
    "<li><b>Meteorites:</b> ALH84001 (controversial Mars meteorite); Murchison meteorite (amino acids).</li></ul>",
    [("Perseverance","NASA Mars rover (2021–present); collecting samples for future return; MOXIE and Ingenuity included."),
     ("Europa Clipper","NASA orbiter mission to study Europa's ice shell and subsurface ocean; launch 2024."),
     ("Transit Spectroscopy","Analyzing starlight filtered through a planet's atmosphere during transit to identify chemical composition."),
     ("ALH84001","Mars meteorite found in Antarctica; controversial claim of fossil microbes (1996); debated."),
     ("Murchison Meteorite","Fell in Australia (1969); contains amino acids and organic compounds — supports panspermia hypothesis.")],
    [("Mars rovers search for life by:",["Looking for animals","*Analyzing rock and soil chemistry for signs of past water, organic molecules, and habitable environments","Digging tunnels","Listening for sounds"],"Geological and chemical analysis."),
     ("Perseverance's unique mission includes:",["Only driving","*Caching samples for future Mars Sample Return mission to Earth","Only photography","Only weather monitoring"],"First step of sample return."),
     ("Europa Clipper will:",["Land on Europa","*Orbit Jupiter and make close flybys of Europa to study its ice shell, ocean, and habitability","Orbit Europa directly","Visit Mars"],"Multiple flyby approach."),
     ("JWST detects exoplanet atmospheres using:",["Cameras","*Transit spectroscopy — analyzing starlight filtered through the atmosphere","Microphones","Touch sensors"],"Spectral fingerprints."),
     ("A potential atmospheric biosignature would be:",["CO₂ alone","*Multiple gases in chemical disequilibrium (e.g., O₂ + CH₄ together)","Only nitrogen","Vacuum"],"Shouldn't coexist without replenishment."),
     ("ALH84001 is a meteorite from:",["The Moon","*Mars (found in Allan Hills, Antarctica, 1984; controversial 'microfossils' announced 1996)","Venus","Jupiter"],"Sparked debate."),
     ("The Murchison meteorite is important because:",["It's large","*It contains amino acids and complex organic molecules, showing these form in space","It's from Mars","It glows"],"Prebiotic chemistry in space."),
     ("Mars Sample Return (MSR) is significant because:",["We already have Mars samples","*Returning cached samples to Earth allows analysis with advanced lab instruments impossible on rovers","It's impossible","Only for minerals"],"Most detailed analysis possible."),
     ("Enceladus (Saturn's moon) is a target because:",["It's large","*Its geysers eject material from a subsurface ocean — spacecraft could fly through and sample it","It has atmosphere","It's warm"],"Accessible ocean material."),
     ("The Dragonfly mission will send a _____ to Titan.",["Rover","Orbiter","*Rotorcraft (drone) — sampling organic-rich surface for prebiotic chemistry","Submarine"],"Flying laboratory."),
     ("Viking landers (1976) tested for life on Mars by:",["Looking for fossils","*Conducting experiments on soil samples to detect metabolic activity (ambiguous results)","Planting seeds","Drilling deep"],"One experiment showed positive result — still debated."),
     ("Curiosity rover discovered that Gale Crater on Mars was once a:",["Desert","*Lake with habitable conditions (appropriate pH, chemistry, organic molecules present)","Volcano","Ocean"],"Ancient habitable environment."),
     ("The search for extraterrestrial life includes looking for:",["Only intelligent life","*Both microbial and intelligent life — most likely first detection will be microbial","Only large animals","Only plants"],"Microbes most probable."),
     ("Biosignatures in ancient Mars rocks might include:",["Fossils of animals","*Patterns in mineral structures, isotope ratios, or preserved organic molecules indicating biological origin","Radio signals","Written messages"],"Subtle geological evidence."),
     ("The 'follow the water' strategy for life detection means:",["Rain is needed","*Water is the strongest habitability indicator, so missions prioritize locations with past or present water","Only Earth sea","Only ice"],"Where there's water, look for life."),
     ("Phosphine detected in Venus's atmosphere (2020) was notable because:",["It's common","*On Earth, phosphine is associated with biological processes — possible (controversial) Venus biosignature","It proves life","It was a mistake"],"Still debated."),
     ("The search for life is interdisciplinary, involving:",["Only biology","*Biology, chemistry, geology, physics, engineering, and computer science","Only astronomy","Only philosophy"],"Team effort."),
     ("Life detection instruments on rovers include:",["Only cameras","*Spectrometers, mass spectrometers, X-ray analyzers, and sample caching systems","Only wheels","Only antennas"],"Sophisticated analytical tools."),
     ("If microbial life is found beyond Earth, it would:",["Be unimportant","*Be among the most significant scientific discoveries in human history","Only interest biologists","Not change anything"],"Profound implications."),
     ("Future missions may include submarines sent to:",["Mars","*Europa or Titan (to explore subsurface oceans or methane seas)","The Sun","Venus"],"Concept missions.")]
)
lessons[k]=v

# 8.4
k,v = build_lesson(8,4,"SETI & Radio Astronomy",
    "<h3>SETI &amp; Radio Astronomy</h3>"
    "<p><b>SETI</b> (Search for ExtraTerrestrial Intelligence): Listening for artificial signals from technologically advanced civilizations.</p>"
    "<ul><li><b>Water Hole:</b> Radio frequencies (1420–1720 MHz) between hydrogen and hydroxyl lines — low noise, logical for communication.</li>"
    "<li><b>WOW! Signal:</b> 1977 detection at Ohio State — strong narrowband signal; never repeated; origin unknown.</li>"
    "<li><b>Fermi Paradox:</b> If intelligent life is common, where is everybody?</li>"
    "<li><b>Drake Equation:</b> N = R* × f_p × n_e × f_l × f_i × f_c × L — framework for estimating N (communicating civilizations).</li></ul>",
    [("SETI","Search for ExtraTerrestrial Intelligence; systematic effort to detect artificial signals from alien civilizations."),
     ("Water Hole","Radio frequency band (1420–1720 MHz) considered optimal for interstellar communication (low noise)."),
     ("Fermi Paradox","Contradiction between the high probability of alien civilizations and the lack of evidence; 'Where is everybody?'"),
     ("Drake Equation","N = R* × f_p × n_e × f_l × f_i × f_c × L; estimates the number of communicating civilizations in the Milky Way."),
     ("WOW! Signal","A strong, narrowband radio signal detected in 1977 at Ohio State; never repeated; origin still unknown.")],
    [("SETI stands for:",["Space Exploration Technology Initiative","*Search for ExtraTerrestrial Intelligence","Solar Energy Transmission Institute","Stellar Examination and Testing"],"Searching for intelligent signals."),
     ("The Water Hole frequency band is between:",["100–200 MHz","*1420–1720 MHz (hydrogen and hydroxyl lines)","10–20 GHz","1–2 Hz"],"Low-noise communication window."),
     ("The Fermi Paradox asks:",["How old is the universe?","*If intelligent life is common, why haven't we detected any evidence of it?","How far are the stars?","What is dark matter?"],"Where is everybody?"),
     ("The Drake Equation estimates:",["Star brightness","*The number of communicating civilizations (N) in the Milky Way","Planet size","Our galaxy's age"],"Framework with many unknowns."),
     ("The WOW! Signal was:",["A hoax","*A strong, narrowband radio signal detected in 1977 that lasted ~72 seconds and was never repeated","A TV broadcast","Thunder"],"Most famous candidate signal."),
     ("SETI primarily uses _____ to search for signals.",["Optical telescopes","*Radio telescopes (and increasingly optical/infrared telescopes)","X-ray detectors","Spacecraft"],"Radio frequencies travel well through space."),
     ("The Allen Telescope Array is dedicated to:",["Weather observation","*SETI observations — a radio telescope array designed for continuous sky surveys","Military use","Solar observation"],"Named after Paul Allen."),
     ("One explanation for the Fermi Paradox is the 'Great Filter,' which suggests:",["Aliens are hiding","*There may be a barrier (step) in the development of intelligent life that most civilizations don't pass","Earth is special in every way","The universe is young"],"Could be ahead or behind us."),
     ("The Drake Equation variable L represents:",["Star luminosity","*The average length of time communicating civilizations survive and transmit","Light-years","Lifespan of a star"],"Most uncertain variable."),
     ("Breakthrough Listen is a modern SETI project that:",["Has ended","*Surveys ~1 million nearby stars and 100+ galaxies using world's largest radio telescopes","Only uses optical","Is government-funded"],"$100 million initiative."),
     ("Narrowband radio signals are interesting for SETI because:",["Nature produces them commonly","*Natural processes rarely produce narrowband signals — they could indicate technology","They're easy to detect","They're beautiful"],"Artificial vs. natural."),
     ("The 'zoo hypothesis' proposes that aliens:",["Don't exist","*Are aware of us but choose not to interfere (like a nature preserve)","Can't travel","Are too far"],"One Fermi Paradox explanation."),
     ("The Arecibo Message (1974) was:",["A radio station","*A coded message transmitted toward globular cluster M13 — a symbolic demonstration","An alien signal","A satellite launch"],"Won't arrive for ~25,000 years."),
     ("Technosignatures are:",["Only radio signals","*Any detectable signs of technology (radio signals, laser emissions, megastructures, pollution)","Only fossils","Only spacecraft"],"Broader than just radio."),
     ("Optical SETI searches for:",["Radio waves","*Brief, intense laser pulses that could serve as interstellar communication beacons","X-rays","Gravity waves"],"Complementary to radio."),
     ("The term 'biosignature' differs from 'technosignature' because:",["They're the same","*Biosignatures indicate any life; technosignatures indicate technology/intelligence","Technosignatures are biological","Biosignatures are technological"],"Different detection targets."),
     ("If a signal were detected, SETI protocols call for:",["Immediate response","*Verification, peer review, and international consultation before any response","Secrecy","Ignore it"],"Careful, measured approach."),
     ("Earth itself broadcasts _____ into space.",["Nothing","*Radio/TV signals, radar, and other electromagnetic emissions (detectable at limited distances)","Only light","Only heat"],"We're already broadcasting."),
     ("The Kardashev Scale classifies civilizations by:",["Population size","*Energy usage: Type I (planet), Type II (star), Type III (galaxy)","Military strength","Age"],"Measuring advancement."),
     ("Understanding SETI is important because:",["It's science fiction","*It represents a rigorous scientific effort to answer one of humanity's deepest questions: are we alone?","It's only a hobby","It has no value"],"Fundamental inquiry.")]
)
lessons[k]=v

# 8.5
k,v = build_lesson(8,5,"Exoplanets & Habitable Zones",
    "<h3>Exoplanets &amp; Habitable Zones</h3>"
    "<h4>Detection Methods</h4>"
    "<ul><li><b>Transit method:</b> Planet crosses in front of star → slight dimming (Kepler, TESS).</li>"
    "<li><b>Radial velocity:</b> Star wobbles due to orbiting planet's gravity → Doppler shift in spectrum.</li>"
    "<li><b>Direct imaging:</b> Blocking star's light to photograph the planet (coronagraph).</li></ul>"
    "<p>Over 5,500 confirmed exoplanets as of 2024. Many in habitable zones. TRAPPIST-1 system has 7 Earth-sized planets, 3 in the habitable zone.</p>",
    [("Exoplanet","Planet orbiting a star other than our Sun; over 5,500 confirmed (as of 2024)."),
     ("Transit Method","Detecting exoplanets by measuring the slight dimming of a star as a planet crosses in front."),
     ("Radial Velocity","Detecting exoplanets by measuring the Doppler shift in a star's spectrum caused by gravitational wobble."),
     ("TRAPPIST-1","Ultracool dwarf star with 7 Earth-sized planets; 3 in the habitable zone; prime JWST target."),
     ("Kepler Space Telescope","NASA mission (2009–2018) that discovered thousands of exoplanets using the transit method.")],
    [("The transit method detects exoplanets by measuring:",["Planet brightness","*The slight dimming of a star as a planet crosses in front of it","Sound","Heat"],"Light curve dip."),
     ("The radial velocity method detects:",["Planet color","*Doppler shift in the star's spectrum caused by the gravitational pull of an orbiting planet","Planet size directly","Sound"],"Star wobble."),
     ("As of 2024, approximately _____ exoplanets have been confirmed.",["100","1,000","*5,500+","100,000"],"Rapidly growing number."),
     ("The Kepler Space Telescope discovered:",["10 planets","*Thousands of exoplanets using the transit method (2009–2018)","Only Jupiter-like planets","No planets"],"Revolutionary mission."),
     ("TESS (Transiting Exoplanet Survey Satellite) focuses on:",["Distant stars","*Nearby, bright stars to find exoplanets (including Earth-sized ones) for follow-up study","Only our solar system","Only the Moon"],"Kepler's successor."),
     ("Direct imaging of exoplanets is difficult because:",["Planets are large","*Stars are millions to billions of times brighter than their planets — the glare overwhelms the planet's light","Stars are dim","Planets are dark"],"Needle next to a searchlight."),
     ("TRAPPIST-1 is notable because:",["It's a large star","*It has 7 Earth-sized planets, with 3 in the habitable zone — all close enough for atmospheric study","It's the closest star","It has no planets"],"Prime astrobiology target."),
     ("A 'hot Jupiter' is:",["A planet in our solar system","*A gas giant orbiting very close to its star (short period, high temperature)","A cool planet","An asteroid"],"Unexpected discovery."),
     ("A 'super-Earth' is:",["Earth in the future","*An exoplanet with mass larger than Earth but smaller than Neptune (~1.2–10 Earth masses)","A star","A moon"],"No solar system analog."),
     ("The habitable zone depends on:",["Only distance","*Star luminosity and temperature (brighter/hotter star → farther HZ; cooler star → closer HZ)","Only planet size","Only time"],"Star-dependent."),
     ("Atmospheric characterization via JWST can detect:",["Nothing","*Specific molecules (H₂O, CO₂, CH₄, O₃) in exoplanet atmospheres during transits","Only hydrogen","Only temperature"],"Spectroscopic fingerprints."),
     ("The Kepler mission revealed that planets are:",["Rare","*Extremely common — on average, every star in the Milky Way has at least one planet","Only around Sun-like stars","Nonexistent"],"Planets outnumber stars."),
     ("Microlensing is a detection method that uses:",["Magnets","*The gravitational bending of light from a distant star by an intervening star-planet system","Radio waves","Sound"],"Einstein's general relativity."),
     ("The Roman Space Telescope (Nancy Grace Roman) will use _____ to study exoplanets.",["Only transit","*Coronagraphy (direct imaging) and microlensing","Only radio","Only spectroscopy"],"Next-generation mission."),
     ("Proxima Centauri b is significant because:",["It's the largest planet","*It's the nearest known exoplanet (orbiting the closest star to the Sun, ~4.2 light-years away)","It's the hottest","It has rings"],"In the habitable zone."),
     ("Tidal locking means:",["The planet spins fast","*One side of the planet always faces the star (like the Moon to Earth) — common for close-in planets","The planet has tides","The planet orbits backward"],"Affects habitability."),
     ("The 'biosignature gas' oxygen on Earth is produced primarily by:",["Volcanoes","*Photosynthetic organisms (plants, algae, cyanobacteria)","Lightning","Chemical reactions"],"Biological origin on Earth."),
     ("False positives in biosignature detection could come from:",["Nothing","*Geological processes, photochemistry, or other abiotic sources that produce similar gases","Only life","Only technology"],"Need to rule out non-biological sources."),
     ("The sheer number of exoplanets suggests that:",["Life is impossible","*The potential for life elsewhere is statistically significant — many habitable-zone planets exist","Earth is unique in all ways","We're alone"],"Numbers favor the search."),
     ("Exoplanet science helps us understand:",["Nothing about Earth","*Earth's place in the universe, the diversity of planetary systems, and the potential for life elsewhere","Only physics","Only chemistry"],"Context for our home.")]
)
lessons[k]=v

# 8.6
k,v = build_lesson(8,6,"Case Studies in Astrobiology",
    "<h3>Case Studies in Astrobiology</h3>"
    "<h4>Mars — Perseverance &amp; Sample Return</h4>"
    "<p>Jezero Crater: ancient river delta. Perseverance caching rock samples with potential biosignatures for future return to Earth labs.</p>"
    "<h4>Europa &amp; Enceladus</h4>"
    "<p>Europa Clipper will assess ice thickness, ocean salinity, and surface geology. Enceladus plumes contain water, organics, and molecular hydrogen — strong habitability indicators.</p>"
    "<h4>Titan</h4>"
    "<p>Dragonfly mission: rotorcraft exploring Titan's organic-rich dunes and impact craters for prebiotic chemistry.</p>",
    [("Jezero Crater","Mars landing site for Perseverance; ancient lake/river delta — ideal for preserving biosignatures."),
     ("Mars Sample Return","Planned mission to bring Perseverance's cached samples back to Earth for advanced laboratory analysis."),
     ("Enceladus Plumes","Geysers erupting from Enceladus's south pole containing water, organic molecules, and H₂ — accessible for sampling."),
     ("Dragonfly","NASA rotorcraft mission to Titan; will explore organic-rich surface and search for prebiotic chemistry."),
     ("Habitability Indicators","Features suggesting an environment could support life: liquid water, energy, organic molecules, suitable chemistry.")],
    [("Jezero Crater was chosen for Perseverance because:",["It's flat","*It's an ancient river delta likely to preserve signs of past life in sedimentary rocks","It's warm","It's close to the equator"],"Best preservation potential."),
     ("Perseverance's sample caching system:",["Discards samples","*Seals rock cores in tubes for future retrieval and return to Earth","Only photographs","Only analyzes on-site"],"First step of MSR."),
     ("Mars Sample Return would allow:",["Nothing new","*Analysis with instruments too large/sensitive for rovers — definitive life detection capability","Only chemistry","Only dating"],"Earth labs far exceed rover instruments."),
     ("Enceladus's plumes are significant because:",["They're beautiful","*They provide direct access to subsurface ocean material without drilling through ice","They're hot","They contain only gas"],"Material ejected into space."),
     ("Enceladus's plumes contain:",["Only water","*Water, organic molecules, molecular hydrogen, silica — suggesting hydrothermal activity","Only ice","Only gas"],"Strong habitability indicators."),
     ("Europa Clipper's ice-penetrating radar will:",["Drill through ice","*Map the thickness and structure of Europa's ice shell and look for subsurface water pockets","Melt ice","Only photograph"],"Understanding the ice-ocean boundary."),
     ("Titan's organic dunes are interesting because:",["They're sand","*They contain complex carbon-based molecules that could reveal prebiotic chemistry pathways","They're boring","They're all water"],"Organic chemistry laboratory."),
     ("Dragonfly will fly on Titan because:",["It's easy","*Titan's thick atmosphere (1.5× Earth's surface pressure) and low gravity (1/7 Earth) make flight efficient","It has wings already","Wind blows it"],"Favorable flight conditions."),
     ("The Cassini mission discovered Enceladus's plumes by:",["Landing","Drilling","*Flying through them and detecting water, organics, and salts with its instruments","Radio observation"],"Unexpected discovery during Saturn tour."),
     ("Finding molecular hydrogen (H₂) in Enceladus's plumes suggests:",["Nothing","*Active hydrothermal reactions on the ocean floor — potential energy source for life","Only chemistry","Only heat"],"Similar to Earth's hydrothermal vents."),
     ("Pre-biotic chemistry refers to:",["Life already existing","*Chemical reactions that produce building blocks of life but haven't yet assembled into living organisms","Only organic chemistry","Only biology"],"Steps toward life."),
     ("Impact craters on Titan are interesting for Dragonfly because:",["They're dangerous","*Impacts may have temporarily melted water ice, mixing with organics — 'natural laboratory' for prebiotic reactions","They're smooth","They're shallow"],"Transient habitable environments."),
     ("The hypothesized ocean on Europa may be kept liquid by:",["Solar heating","*Tidal heating from Jupiter's gravitational forces flexing Europa's interior","Radioactive decay only","Geothermal only"],"Jupiter's tidal influence."),
     ("If amino acids are found in returned Mars samples, it would:",["Prove life","*Be a strong (but not definitive) indicator; must determine if they're biological or abiotic in origin","Mean nothing","Only interest chemists"],"Context matters."),
     ("Studying multiple ocean worlds (Europa, Enceladus, Titan) is important because:",["They're similar","*Comparing different environments reveals which conditions are necessary vs. sufficient for life","Only one matters","It's redundant"],"Comparative astrobiology."),
     ("The Galileo mission to Jupiter provided evidence for Europa's ocean by:",["Landing","*Detecting a magnetic field consistent with a salty, conducting subsurface ocean","Radar imaging","Drilling"],"Induced magnetic field."),
     ("A future Enceladus mission concept involves:",["Landing only","*Flying through plumes to collect and analyze material for biosignatures","Orbiting Saturn only","Only photography"],"Direct sampling."),
     ("The significance of these case studies is that:",["Only theoretical","*They represent concrete, funded missions actively searching for life — the search is happening now","Outdated","Only American effort"],"Real missions, real search."),
     ("Astrobiology case studies demonstrate that:",["Only one approach works","*Multiple independent lines of evidence from different worlds will be needed to confirm or deny extraterrestrial life","Life is everywhere","Life is nowhere"],"Converging evidence."),
     ("The overarching lesson from astrobiology research is that:",["The search is hopeless","*The universe provides many potential habitats, and we now have the technology to begin investigating them","Only Earth matters","Life is impossible elsewhere"],"Optimistic but rigorous.")]
)
lessons[k]=v

# 8.7
k,v = build_lesson(8,7,"AP Prep: Probability Models for Life",
    "<h3>AP Prep: Probability Models for Life</h3>"
    "<h4>Drake Equation</h4>"
    "<p>N = R* × f_p × n_e × f_l × f_i × f_c × L</p>"
    "<ul><li><b>R*</b> = rate of star formation (~1.5–3/yr in Milky Way)</li>"
    "<li><b>f_p</b> = fraction of stars with planets (~1, nearly all)</li>"
    "<li><b>n_e</b> = habitable planets per star (~0.2–0.5)</li>"
    "<li><b>f_l</b> = fraction developing life (?)</li>"
    "<li><b>f_i</b> = fraction developing intelligence (?)</li>"
    "<li><b>f_c</b> = fraction developing communicating technology (?)</li>"
    "<li><b>L</b> = years a civilization communicates (?)</li></ul>"
    "<p>Known factors suggest many habitable planets exist. Unknown factors (f_l through L) dominate uncertainty.</p>",
    [("Drake Equation","N = R* × f_p × n_e × f_l × f_i × f_c × L; framework for estimating communicating civilizations."),
     ("R* (Star Formation Rate)","Average rate of star formation in the Milky Way: ~1.5–3 solar masses per year."),
     ("n_e","Average number of habitable planets per star with planets; estimated 0.2–0.5 based on Kepler data."),
     ("L (Civilization Lifetime)","Average number of years a civilization remains detectable; most uncertain Drake variable."),
     ("Bayesian Analysis","Statistical method for updating probability estimates as new data is obtained; used in modern astrobiology.")],
    [("In the Drake Equation, N represents:",["Number of stars","*Number of communicating civilizations in the Milky Way","Number of planets","Number of galaxies"],"The final estimate."),
     ("R* in the Drake Equation is:",["Number of planets","*Rate of star formation in the galaxy (~1.5–3/yr for the Milky Way)","Radius of stars","Random number"],"Known parameter."),
     ("f_p (fraction of stars with planets) is now estimated at:",["0.01","0.1","*~1.0 (nearly every star has at least one planet)","Unknown"],"Kepler revolution."),
     ("n_e (habitable planets per star) is estimated at:",["0","*0.2–0.5 (based on Kepler and TESS data)","100","Unknown — no data"],"Constrained by observations."),
     ("The most uncertain variables in the Drake Equation are:",["R* and f_p","*f_l, f_i, f_c, and L (life development to civilization lifetime)","n_e","All are known"],"Biological and sociological factors."),
     ("If all Drake variables are optimistic, N could be:",["0","1","*Millions of communicating civilizations","Infinite"],"Depends entirely on assumptions."),
     ("If L (civilization lifetime) is very short, then N is:",["Large","*Small (civilizations don't overlap in time)","Infinite","Unchanged"],"L dominates the result."),
     ("The Drake Equation is best described as:",["A precise calculation","*A framework for organizing our knowledge and ignorance about extraterrestrial intelligence","Proven correct","Disproven"],"Useful thinking tool."),
     ("Kepler data has most constrained which Drake variables?",["f_l and f_i","*f_p and n_e (fraction of stars with planets, habitable planets per star)","f_c and L","R*"],"Observational advances."),
     ("For AP problems, if R*=2, f_p=1, n_e=0.3, f_l=0.1, f_i=0.01, f_c=0.1, L=10,000, then N=:",["1","*N = 2×1×0.3×0.1×0.01×0.1×10,000 = 0.6 (less than 1 civilization)","100","1,000"],"Plug and calculate."),
     ("Changing L from 100 to 10,000 increases N by:",["2×","*100× (direct proportionality)","10×","1,000×"],"N is directly proportional to L."),
     ("Bayesian analysis in astrobiology:",["Is not used","*Updates probability estimates as new evidence (exoplanet data, biosignatures) is gathered","Replaces the Drake Equation entirely","Only applies to physics"],"Modern statistical approach."),
     ("The Copernican Principle suggests:",["Earth is the center","*Earth is not special — conditions that produced life here likely exist elsewhere","Life is unique to Earth","Nothing about life"],"Philosophical assumption."),
     ("The Great Filter hypothesis proposes that:",["All civilizations survive","*Some step in the development of spacefaring civilizations is extremely improbable","Filters don't exist","Only humans can pass"],"Explains the Fermi Paradox."),
     ("If we find microbial life on Mars, it would affect the Drake Equation by:",["No effect","*Suggesting f_l (fraction of habitable planets developing life) is higher, increasing N estimates","Decreasing N","Eliminating the equation"],"Data constrains variables."),
     ("Monte Carlo simulations applied to the Drake Equation:",["Give one answer","*Run thousands of scenarios with random values within ranges to produce a probability distribution for N","Are irrelevant","Always give N=0"],"Statistical modeling."),
     ("The fraction of civilizations that develop radio technology (f_c) is important because:",["Radio is old","*Only civilizations with detectable technology can be found by SETI — radio/laser ability is necessary","It's not important","Everyone has radio"],"Detection requirement."),
     ("If every star had a habitable planet with life, but f_i = 0.0001, then:",["N would be huge","*Intelligence would still be very rare — most life would be microbial","N would be zero","Intelligence is guaranteed"],"Intelligence may be the bottleneck."),
     ("Understanding probability models in astrobiology teaches:",["Nothing useful","*How to quantify uncertainty, use frameworks for complex problems, and update estimates with new data","Only math","Only biology"],"Critical thinking skill."),
     ("The most important takeaway from the Drake Equation is that:",["We can calculate N precisely","*It highlights what we know, what we don't, and what observations could help narrow the answer","Aliens definitely exist","Aliens definitely don't exist"],"Framework for inquiry.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Astronomy Unit 8: wrote {len(lessons)} lessons")
