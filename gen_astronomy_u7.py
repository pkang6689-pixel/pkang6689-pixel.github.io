#!/usr/bin/env python3
"""Astronomy Unit 7 – Space Exploration (7 lessons)."""
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

# 7.1
k,v = build_lesson(7,1,"History of Space Missions",
    "<h3>History of Space Missions</h3>"
    "<h4>Milestones</h4>"
    "<ul><li><b>1957:</b> Sputnik (first satellite, USSR).</li>"
    "<li><b>1961:</b> Yuri Gagarin (first human in space); Alan Shepard (first American).</li>"
    "<li><b>1969:</b> Apollo 11 — Neil Armstrong and Buzz Aldrin walk on the Moon.</li>"
    "<li><b>1971:</b> Salyut 1 (first space station, USSR).</li>"
    "<li><b>1981–2011:</b> Space Shuttle program (135 missions).</li>"
    "<li><b>1998–present:</b> International Space Station (ISS).</li>"
    "<li><b>2020s:</b> Artemis program (return to the Moon); commercial spaceflight (SpaceX, Blue Origin).</li></ul>",
    [("Sputnik","First artificial satellite; launched by the USSR on October 4, 1957; started the Space Age."),
     ("Apollo 11","First crewed Moon landing (July 20, 1969); Neil Armstrong and Buzz Aldrin walked on the Moon."),
     ("Space Shuttle","NASA's reusable spacecraft (1981–2011); 135 missions; launched and serviced satellites, built the ISS."),
     ("ISS","International Space Station; collaborative orbiting lab (1998–present); 5 space agencies."),
     ("Artemis Program","NASA program to return humans to the Moon and establish sustainable presence for future Mars missions.")],
    [("The first artificial satellite, Sputnik, was launched in:",["1945","*1957","1969","1980"],"Start of the Space Age."),
     ("The first human in space was:",["Neil Armstrong","John Glenn","*Yuri Gagarin (1961, USSR)","Alan Shepard"],"Orbited Earth in Vostok 1."),
     ("Apollo 11 landed on the Moon on:",["January 1, 1970","*July 20, 1969","December 25, 1968","October 4, 1957"],"'One small step for man…'"),
     ("The Space Shuttle program ran from:",["1969–2000","*1981–2011 (135 missions)","1990–2020","1957–1975"],"Reusable spacecraft era."),
     ("The ISS has been continuously occupied since:",["1990","*2000 (November 2000)","2010","1998"],"Longest continuous human presence in space."),
     ("The Space Race was primarily between:",["US and China","*The United States and the Soviet Union","Europe and Japan","US and India"],"Cold War competition."),
     ("The Challenger disaster occurred in:",["1969","*1986 (crew of 7 lost 73 seconds after launch)","2003","1975"],"O-ring failure."),
     ("The Columbia disaster occurred in:",["1986","*2003 (crew of 7 lost during re-entry)","1969","2011"],"Damaged heat shield."),
     ("The Artemis program aims to:",["Replace the ISS","*Return humans to the Moon and prepare for Mars","Only launch satellites","Only study the Sun"],"NASA's next big mission."),
     ("Mercury, Gemini, and Apollo were:",["Space stations","*Sequential NASA programs leading to the Moon landing","European missions","Soviet programs"],"Progressive capability building."),
     ("The first American in space was:",["John Glenn","Buzz Aldrin","*Alan Shepard (May 5, 1961, suborbital flight)","Neil Armstrong"],"Freedom 7 mission."),
     ("John Glenn was the first American to:",["Walk on the Moon","*Orbit Earth (February 20, 1962)","Walk in space","Launch a satellite"],"Friendship 7, three orbits."),
     ("The first spacewalk (EVA) was performed by:",["Neil Armstrong","*Alexei Leonov (1965, USSR)","Buzz Aldrin","John Glenn"],"12 minutes outside Voskhod 2."),
     ("Apollo 13 is famous for:",["Landing on the Moon","*A near-disaster ('Houston, we've had a problem') — safe crew return despite oxygen tank explosion","The first spacewalk","A new speed record"],"'Successful failure.'"),
     ("The total number of people who have walked on the Moon is:",["2","*12 (Apollo 11, 12, 14, 15, 16, 17)","6","24"],"All between 1969–1972."),
     ("Commercial spaceflight companies include:",["Only NASA","*SpaceX, Blue Origin, Virgin Galactic, and others","Only European companies","Only the Russian space program"],"Growing private sector."),
     ("SpaceX's Falcon 9 is notable for:",["Being expendable","*Successfully landing and reusing first-stage boosters, dramatically reducing launch costs","Only launching satellites","Being the largest rocket"],"Reusability revolution."),
     ("The Hubble Space Telescope was deployed by:",["Apollo","A Russian rocket","*The Space Shuttle Discovery (STS-31, 1990)","A commercial rocket"],"Serviced by shuttle astronauts 5 times."),
     ("International cooperation in space includes:",["Only NASA and ESA","*NASA, Roscosmos, ESA, JAXA, and CSA on the ISS, plus many bilateral partnerships","No cooperation","Only US and Russia"],"Global effort."),
     ("Understanding space exploration history is important because:",["It's only trivia","*It shows the evolution of technology, international cooperation, and humanity's expanding capabilities","It's not","Only for historians"],"Context for current and future missions.")]
)
lessons[k]=v

# 7.2
k,v = build_lesson(7,2,"Satellites & Space Probes",
    "<h3>Satellites &amp; Space Probes</h3>"
    "<h4>Satellites</h4>"
    "<p>LEO (~200–2,000 km): Hubble, ISS, Earth observation. MEO (~2,000–35,786 km): GPS, navigation. GEO (~35,786 km): Weather satellites, communications (stationary over one point).</p>"
    "<h4>Space Probes</h4>"
    "<p>Robotic explorers sent to other worlds: Voyager (outer solar system), Cassini (Saturn), New Horizons (Pluto), Mars rovers, Juno (Jupiter). Use gravity assists to change trajectory.</p>",
    [("LEO","Low Earth Orbit (~200–2,000 km); used by ISS, Hubble, Earth observation satellites."),
     ("GEO","Geostationary Earth Orbit (~35,786 km); satellite stays over one point; used for weather, communications."),
     ("Gravity Assist","Using a planet's gravity to accelerate or redirect a spacecraft without using fuel."),
     ("Space Probe","Unmanned robotic spacecraft sent to explore other celestial bodies."),
     ("GPS","Global Positioning System; ~31 satellites in MEO providing precise location data worldwide.")],
    [("The International Space Station orbits in:",["GEO","*LEO (Low Earth Orbit, ~400 km altitude)","MEO","Deep space"],"~90-minute orbital period."),
     ("Geostationary orbit (GEO) altitude is approximately:",["200 km","2,000 km","*~35,786 km","100,000 km"],"24-hour orbital period matches Earth's rotation."),
     ("GPS satellites orbit in:",["LEO","GEO","*MEO (Medium Earth Orbit, ~20,200 km)","Deep space"],"~12-hour orbital period."),
     ("A gravity assist allows a spacecraft to:",["Slow down only","*Change speed and/or direction using a planet's gravitational field — no fuel required","Land on a planet","Create gravity"],"Free momentum boost."),
     ("Voyager 2 used gravity assists from:",["Only Jupiter","*Jupiter, Saturn, Uranus, and Neptune (grand tour trajectory)","Only Mars","No gravity assists"],"Unique alignment exploited."),
     ("Communication satellites are typically in GEO because:",["It's easier to reach","*They remain stationary over one point, providing continuous coverage to ground stations","They're cheaper","They're closer"],"Fixed position relative to Earth."),
     ("Earth observation satellites like Landsat operate in:",["GEO","*LEO (low altitude for high-resolution imaging)","MEO","Solar orbit"],"Close to the surface for detail."),
     ("The Hubble Space Telescope orbits at approximately:",["35,786 km","*~547 km (LEO)","20,000 km","1 million km"],"Low Earth Orbit."),
     ("Space probes are _____ spacecraft.",["Crewed","*Uncrewed (robotic)","Always orbiting Earth","Never launched"],"No humans aboard."),
     ("The James Webb Space Telescope orbits at:",["LEO","GEO","*The Sun-Earth L2 Lagrange point (~1.5 million km from Earth)","The Moon"],"Stable, cold location."),
     ("CubeSats are:",["Large space stations","*Small, standardized satellites (10 cm × 10 cm × 10 cm units) — low-cost and increasingly capable","Cubes on Earth","Movie props"],"Democratizing space access."),
     ("Starlink is SpaceX's constellation of _____ in LEO.",["Weather satellites","GPS satellites","*Internet communication satellites (thousands deployed)","Spy satellites"],"Global broadband internet."),
     ("Space debris is a growing problem because:",["It's not a problem","*Thousands of defunct satellites and fragments in orbit risk collisions (Kessler syndrome)","There's no debris","It falls to Earth"],"Cascading collision risk."),
     ("The Kessler syndrome describes:",["A medical condition","*A scenario where cascading collisions generate so much debris that certain orbits become unusable","A financial problem","A type of orbit"],"Proposed by Donald Kessler in 1978."),
     ("Solar sails propel spacecraft using:",["Rocket fuel","*Radiation pressure from sunlight pushing on large, reflective surfaces","Solar wind","Nuclear energy"],"No fuel needed."),
     ("Ion propulsion engines provide:",["Enormous thrust","*Very low thrust but extremely high efficiency (specific impulse), useful for long missions","No thrust","Only attitude control"],"Dawn spacecraft used ion engines."),
     ("The Parker Solar Probe uses Venus gravity assists to:",["Speed up","*Gradually shrink its orbit closer to the Sun","Slow down","Change direction only"],"Multiple Venus flybys."),
     ("Satellite constellations for Earth observation help monitor:",["Nothing","*Climate change, deforestation, agriculture, natural disasters, and ocean health","Only weather","Only military targets"],"Wide-ranging applications."),
     ("Deep Space Network (DSN) is:",["A TV network","*NASA's system of large radio antennas worldwide for communicating with distant spacecraft","A social network","A type of satellite"],"Three sites: California, Spain, Australia."),
     ("The future of satellites and probes includes:",["Declining activity","*Increasing numbers, smaller sizes, AI autonomy, and missions to asteroids, Europa, Titan, and beyond","Only Earth orbit","Only military use"],"Exciting future.")]
)
lessons[k]=v

# 7.3
k,v = build_lesson(7,3,"Human Spaceflight",
    "<h3>Human Spaceflight</h3>"
    "<h4>Challenges</h4>"
    "<ul><li><b>Microgravity effects:</b> Bone loss (~1–2%/month), muscle atrophy, fluid shift, vision changes.</li>"
    "<li><b>Radiation:</b> Cosmic rays and solar particle events; increased cancer risk.</li>"
    "<li><b>Psychological:</b> Isolation, confinement, communication delay (Mars: 4–24 min one-way).</li>"
    "<li><b>Life support:</b> Oxygen, water recycling, food, waste management.</li></ul>"
    "<p>Exercise (2+ hours/day on ISS), pharmacological countermeasures, and research into artificial gravity are ongoing.</p>",
    [("Microgravity","Near-weightlessness experienced in orbit; causes physiological changes (bone loss, muscle atrophy)."),
     ("Space Radiation","Galactic cosmic rays and solar particle events; major health risk for astronauts beyond LEO."),
     ("ECLSS","Environmental Control and Life Support System; provides air, water, temperature control on spacecraft."),
     ("Astronaut Bone Loss","~1–2% bone density loss per month in microgravity; similar to severe osteoporosis."),
     ("Communication Delay","Signal travel time between Earth and distant spacecraft; Mars: 4–24 minutes one-way.")],
    [("Astronauts on the ISS exercise about _____ per day to counteract microgravity effects.",["15 minutes","30 minutes","*~2+ hours","Only when they feel like it"],"Critical countermeasure."),
     ("Bone loss in microgravity occurs at about:",["0.1% per year","*1–2% per month","10% per year","No loss occurs"],"Rapid without exercise."),
     ("Space radiation is dangerous because:",["It's not","*Cosmic rays and solar particles can damage DNA, increasing cancer risk","It only affects equipment","It only affects the skin"],"Major long-duration concern."),
     ("On a Mars mission, communication delay would be:",["Instantaneous","*4–24 minutes one-way (depending on orbital positions)","1 hour","1 day"],"No real-time communication."),
     ("The ISS's water recycling system recovers water from:",["Only stored supplies","*Humidity, urine, and other sources; recycles ~90% of water","Only rain collection","Nothing"],"Critical resource conservation."),
     ("Psychological challenges of long-duration spaceflight include:",["None","*Isolation, confinement, crew conflicts, sleep disruption, and communication delay","Only boredom","Only fear"],"Mental health is crucial."),
     ("The longest continuous spaceflight was _____ by cosmonaut Valeri Polyakov.",["30 days","6 months","*~437 days (1994–1995, aboard Mir)","1,000 days"],"Record single mission."),
     ("Artificial gravity could be created by:",["Wishing","*Rotating a spacecraft (centrifugal force simulates gravity)","Magnets","Turning off the engines"],"Concept studied but not yet implemented."),
     ("Spacesuits (EMUs) provide:",["Only appearance","*Pressurized atmosphere, oxygen, temperature regulation, and protection from radiation and micrometeoroids","Only warmth","Only communication"],"Mini spacecraft."),
     ("Space food has evolved from:",["Always being normal food","*Squeeze tubes and freeze-dried meals to more varied, nutritious options","Only pills","Only liquids"],"Improved over decades."),
     ("Vision changes in astronauts (SANS — Spaceflight Associated Neuro-ocular Syndrome) involve:",["Improved vision","*Swelling of optic nerves and flattening of eyeballs due to fluid shifts","No changes","Only color blindness"],"Active area of research."),
     ("The Orion spacecraft is designed for:",["LEO only","*Deep-space missions (Moon, Mars) — part of the Artemis program","Only cargo","Only satellites"],"Human exploration beyond LEO."),
     ("SpaceX's Dragon capsule:",["Has never flown","*Has carried astronauts to and from the ISS since 2020 (Crew Dragon)","Only carries cargo","Only orbits the Moon"],"Commercial crew program."),
     ("The twin study (Scott and Mark Kelly) showed:",["No differences","*Measurable genetic, physiological, and cognitive changes in the space-based twin vs the ground-based twin","Identical results","Only weight changes"],"Landmark study (2015–2016)."),
     ("ISS experiments include research on:",["Nothing","*Crystal growth, fluid dynamics, human physiology, plant biology, and materials science in microgravity","Only exercise","Only food"],"Unique research environment."),
     ("Space tourism is becoming reality through companies like:",["Only NASA","*SpaceX (Inspiration4), Blue Origin, Virgin Galactic, and Axiom Space","No companies","Only military"],"Private citizens in space."),
     ("Mars human missions face the challenge of:",["Only distance","*Distance, radiation, communication delay, landing, in-situ resource utilization, and mission duration (~2–3 years)","Only cost","Nothing significant"],"Multi-faceted challenge."),
     ("In-Situ Resource Utilization (ISRU) on Mars means:",["Bringing everything from Earth","*Using Martian resources (e.g., extracting oxygen from CO₂ atmosphere, using ice for water)","Leaving nothing behind","Mining gold"],"MOXIE tested on Mars."),
     ("NASA's MOXIE experiment on Mars successfully:",["Failed","*Produced oxygen from Mars's CO₂ atmosphere","Found water","Found life"],"Technology demonstration on Perseverance."),
     ("Understanding human spaceflight challenges is important for:",["Nothing","*Planning future Moon and Mars missions and ensuring astronaut health and safety","Only NASA employees","Only doctors"],"Practical space engineering and medicine.")]
)
lessons[k]=v

# 7.4
k,v = build_lesson(7,4,"International Space Station",
    "<h3>International Space Station (ISS)</h3>"
    "<p>Orbits at ~400 km (LEO); ~109 m wide (solar arrays); ~420,000 kg. Collaborative effort: NASA, Roscosmos, ESA, JAXA, CSA. Continuously occupied since November 2000.</p>"
    "<h4>Research</h4>"
    "<p>Microgravity research in biology, physics, materials science, Earth observation, and technology. Over 3,000 experiments conducted. Plans for deorbit by ~2031; commercial stations to follow.</p>",
    [("ISS","International Space Station; orbiting laboratory at ~400 km; 5 agency cooperation; occupied since 2000."),
     ("Microgravity Research","Experiments conducted in near-weightlessness; unique conditions impossible to replicate on Earth."),
     ("Expedition","Standard crew rotation on the ISS; typically 6 months; numbered sequentially."),
     ("Canadarm2","Robotic arm on the ISS (CSA); used for station maintenance, moving modules, and capturing spacecraft."),
     ("Commercial Crew Program","NASA program using private spacecraft (SpaceX Dragon, Boeing Starliner) to ferry astronauts to the ISS.")],
    [("The ISS orbits at approximately:",["100 km","*~400 km (LEO)","35,786 km","1,000 km"],"Low Earth Orbit."),
     ("The ISS has been continuously occupied since:",["1990","*November 2, 2000","2010","1998"],"Over 20 years of continuous habitation."),
     ("The five space agencies operating the ISS are:",["Only NASA","*NASA, Roscosmos, ESA, JAXA, and CSA","Only NASA and ESA","Only US and Russia"],"International partnership."),
     ("The ISS completes one orbit approximately every:",["24 hours","12 hours","*~92 minutes","1 week"],"16 sunrises per day."),
     ("Over _____ experiments have been conducted on the ISS.",["100","*3,000+","50","10"],"Extensive research program."),
     ("Canadarm2 is:",["A weapon","*A robotic arm (CSA) used for station maintenance, cargo capture, and EVA support","A communication system","A solar panel"],"Essential station tool."),
     ("The ISS is approximately _____ wide (solar array span).",["10 m","50 m","*~109 m (about a football field)","500 m"],"Visible from Earth with the naked eye."),
     ("ISS crew members typically stay for:",["1 week","1 month","*~6 months","1 year"],"Standard expedition duration."),
     ("The Commercial Crew Program uses spacecraft including:",["Only Soyuz","*SpaceX Crew Dragon and Boeing Starliner","Only space shuttles","Only Chinese spacecraft"],"Private-public partnership."),
     ("Microgravity on the ISS enables research that:",["Is the same as on Earth","*Cannot be conducted on Earth due to gravity's effects on experiments","Only military research","Only involves plants"],"Unique research conditions."),
     ("Examples of ISS research include:",["Only exercise","*Crystal growth, protein structure, combustion physics, plant growth, and human physiology","Only photography","Only communication tests"],"Wide range of science."),
     ("The ISS is planned for deorbit around:",["2025","*~2031","2050","Never"],"Commercial stations to succeed it."),
     ("Commercial space stations from companies like Axiom are planned to:",["Replace the ISS entirely immediately","*Gradually take over as research and commercial platforms in LEO","Never launch","Only serve tourists"],"ISS successor."),
     ("Astronauts on the ISS perform EVAs (spacewalks) for:",["Fun","*Maintenance, repairs, and installing new equipment","Only exercise","Only photography"],"Essential station upkeep."),
     ("The ISS recycles about _____ of its water.",["10%","50%","*~90%","100%"],"Critical for sustainability."),
     ("Soyuz spacecraft (Russia) have been transporting crews to the ISS since:",["1969","*2000 (and have been the sole crew vehicle during 2011–2020)","2020","1990"],"Reliable crew transport."),
     ("The ISS travels at approximately:",["1,000 km/h","*~28,000 km/h (7.66 km/s)","100 km/h","Speed of light"],"Orbital velocity."),
     ("International cooperation on the ISS has:",["Failed","*Demonstrated that rival nations can collaborate productively in space","Had no impact","Only benefited the US"],"Model for cooperation."),
     ("The ISS serves as a testbed for:",["Nothing useful","*Technologies needed for future Moon and Mars missions (life support, radiation shielding, crew health)","Only Earth observation","Only communication"],"Stepping stone."),
     ("The ISS can be seen from the ground as a:",["Flashing light","*Bright, steady dot moving across the sky (reflecting sunlight)","Red star","It's invisible"],"Visible to the naked eye.")]
)
lessons[k]=v

# 7.5
k,v = build_lesson(7,5,"Future of Space Travel (Mars & Beyond)",
    "<h3>Future of Space Travel</h3>"
    "<h4>Moon (Artemis)</h4>"
    "<p>Artemis program: return astronauts to the Moon, establish Gateway (lunar orbital station), and build a sustainable presence using lunar resources (ice at poles).</p>"
    "<h4>Mars</h4>"
    "<p>SpaceX Starship designed for Mars transit. Challenges: ~6–9 month journey, radiation, landing, ISRU, communication delay. Target: 2030s–2040s.</p>"
    "<h4>Beyond</h4>"
    "<ul><li>Asteroid mining, Jupiter's moons (Europa Clipper), Titan exploration, interstellar missions (Breakthrough Starshot concept).</li></ul>",
    [("Artemis Gateway","Planned small space station in lunar orbit; staging point for Moon surface missions and Mars preparation."),
     ("Starship","SpaceX's fully reusable super heavy-lift launch vehicle; designed for Moon and Mars missions."),
     ("ISRU","In-Situ Resource Utilization; using local resources (lunar ice, Martian CO₂) to produce fuel, water, oxygen."),
     ("Europa Clipper","NASA mission to study Jupiter's moon Europa's subsurface ocean and habitability (launch ~2024)."),
     ("Breakthrough Starshot","Proposed interstellar mission using light sails accelerated by lasers to reach Alpha Centauri.")],
    [("The Artemis program's primary goals include:",["Only building a space station","*Returning humans to the Moon, establishing sustainable presence, and preparing for Mars","Only studying the Sun","Only launching satellites"],"Multi-phase program."),
     ("The Gateway is:",["A constellation of satellites","*A planned small space station in lunar orbit — staging point for surface missions","A Mars habitat","A communication system"],"Lunar orbital platform."),
     ("Lunar south pole ice deposits are valuable because:",["They're pretty","*Water ice can be used for drinking, oxygen, and rocket fuel (hydrogen/oxygen)","They contain gold","They prove aliens exist"],"ISRU on the Moon."),
     ("SpaceX's Starship is designed to be:",["Expendable","*Fully reusable (both stages), dramatically reducing launch costs","Only for cargo","Only for LEO"],"Revolutionary if achieved."),
     ("A Mars transit takes approximately:",["1 week","1 month","*6–9 months (depending on trajectory)","5 years"],"Using minimum-energy Hohmann transfer."),
     ("Major challenges for Mars missions include:",["Only cost","*Radiation, communication delay, landing, duration (~2–3 years), and life support","Only distance","Only politics"],"Multi-faceted challenges."),
     ("ISRU on Mars could produce:",["Nothing useful","*Oxygen (from CO₂), water (from ice), and potentially rocket fuel (methane)","Only energy","Only building materials"],"Critical for sustaining a presence."),
     ("Europa Clipper will investigate:",["Mars","*Jupiter's moon Europa — its subsurface ocean, ice shell, and potential habitability","Saturn's rings","The Sun"],"Astrobiology target."),
     ("Titan is interesting for future exploration because:",["It's close","*It has a thick atmosphere, liquid methane lakes, and complex organic chemistry","It's hot","It has oxygen"],"Unique environment."),
     ("Asteroid mining could provide:",["Nothing","*Valuable metals (platinum, rare earths), water, and construction materials","Only scientific data","Only entertainment"],"Economic potential."),
     ("Breakthrough Starshot proposes reaching Alpha Centauri using:",["Rocket engines","*Tiny light sails accelerated by powerful ground-based lasers to ~20% speed of light","Warp drive","Solar wind"],"~20-year travel time at 0.2c."),
     ("The Space Launch System (SLS) is:",["A commercial rocket","*NASA's super heavy-lift rocket for Artemis Moon missions","A Space Shuttle replacement name","Cancelled"],"Launched Artemis I in 2022."),
     ("Nuclear thermal propulsion could benefit Mars missions by:",["Doing nothing","*Reducing transit time (higher specific impulse than chemical rockets)","Being dangerous only","Providing electricity only"],"Faster travel = less radiation exposure."),
     ("The Dragonfly mission (NASA) will send a drone to:",["Mars","Europa","*Titan (Saturn's moon) to study prebiotic chemistry","The Moon"],"Rotorcraft lander."),
     ("3D printing in space could enable:",["Nothing","*Manufacturing of tools, spare parts, and even habitats using local materials","Only art","Only food"],"Reduces need to launch from Earth."),
     ("Space elevators conceptually would:",["Be impossible","*Transport cargo from Earth's surface to orbit along a tethered cable — reducing launch costs","Only go down","Only go to the Moon"],"Theoretical but technically challenging."),
     ("Lagrange points are useful for space missions because:",["They don't exist","*Objects placed there require minimal fuel to stay in position relative to two large bodies","They're always near Earth","They have gravity"],"JWST orbits L2."),
     ("International Mars missions are being discussed between:",["No agencies","*NASA, ESA, CNSA, SpaceX, and other agencies/companies","Only SpaceX","Only NASA"],"Global interest."),
     ("The search for life beyond Earth drives exploration of:",["Only Mars","*Mars, Europa, Enceladus, Titan, and exoplanets","Only the Moon","Only asteroids"],"Astrobiology missions."),
     ("Understanding future space travel is important for appreciating:",["Nothing","*The direction of human achievement, technological innovation, and our expanding horizons","Only science fiction","Only budgets"],"Inspiring next generation.")]
)
lessons[k]=v

# 7.6
k,v = build_lesson(7,6,"Case Studies in Space Technology",
    "<h3>Case Studies in Space Technology</h3>"
    "<h4>Reusable Rockets (SpaceX)</h4>"
    "<p>Falcon 9 first-stage landing (2015) revolutionized launch economics. Over 200 booster landings. Starship aims for full reusability.</p>"
    "<h4>James Webb Space Telescope (2021)</h4>"
    "<p>Largest space telescope; 6.5 m primary mirror; infrared; deployed at L2. Studying exoplanet atmospheres, early galaxies, star formation. Cost ~$10 billion over 25 years.</p>"
    "<h4>Mars Helicopter Ingenuity</h4>"
    "<p>First powered flight on another planet (April 19, 2021). Originally planned for 5 flights; completed 72 flights before retirement.</p>",
    [("Falcon 9","SpaceX reusable rocket; first-stage booster lands and is reflown; >200 landings by 2024."),
     ("JWST","James Webb Space Telescope; 6.5 m infrared telescope at L2; studying the earliest galaxies, exoplanet atmospheres, and star formation."),
     ("Ingenuity","Mars helicopter; first powered flight on another planet; completed 72 flights (2021–2024)."),
     ("Reusability","Ability to reflown rocket components; dramatically reduces launch costs (SpaceX pioneered orbital-class reuse)."),
     ("Sunshield","JWST's tennis-court-sized, 5-layer sunshield that keeps instruments at ~-233°C.")],
    [("SpaceX's Falcon 9 first successfully landed a booster in:",["2010","*December 2015","2020","2000"],"Revolutionary achievement."),
     ("Reusable rockets reduce launch costs by:",["A small amount","*Up to ~10× (reuse expensive hardware instead of discarding it)","Nothing","Making them more expensive"],"Economics of reuse."),
     ("JWST's primary mirror is _____ in diameter.",["2 m","*~6.5 m","10 m","1 m"],"Largest space telescope mirror."),
     ("JWST primarily observes in:",["Visible light","X-rays","*Infrared (to see through dust and detect redshifted light from the early universe)","Radio waves"],"Optimized for IR."),
     ("JWST's sunshield is about the size of:",["A car","*A tennis court (5 layers of Kapton)","A football field","A house"],"Keeps instruments extremely cold."),
     ("JWST is located at:",["LEO","GEO","*Sun-Earth L2 Lagrange point (~1.5 million km from Earth)","The Moon"],"Thermally stable, always in Earth's shadow."),
     ("Mars helicopter Ingenuity was designed for _____ flights but completed _____.",["1; 5","*5; 72","50; 50","100; 100"],"Far exceeded expectations."),
     ("Ingenuity demonstrated that powered flight is possible on Mars despite:",["Thick atmosphere","*Mars's extremely thin atmosphere (~1% of Earth's surface pressure)","Strong gravity","No challenges"],"Blades spin ~5× faster than Earth helicopters."),
     ("JWST has revealed unexpectedly _____ galaxies in the early universe.",["Few","Small","*Massive and mature (challenging existing models of galaxy formation)","None"],"Major discoveries."),
     ("JWST's transit spectroscopy has detected _____ in exoplanet atmospheres.",["Nothing","*Water vapor, CO₂, and other molecules","Only hydrogen","Only helium"],"Atmospheric characterization."),
     ("The cost of JWST was approximately:",["$100 million","$1 billion","*~$10 billion (over ~25 years of development)","$100 billion"],"Expensive but transformative."),
     ("SpaceX's Starship aims for:",["Only Earth orbit","*Full reusability of both stages + deep-space capability (Moon, Mars)","Only satellite launches","Single use"],"Next generation."),
     ("Rocket Lab's Electron is an example of:",["A large rocket","*A small launch vehicle designed for dedicated small satellite missions","A space station","A missile"],"Small-sat market."),
     ("3D-printed rocket engines are being developed by:",["No one","*Relativity Space, SpaceX, and others — reducing manufacturing time and cost","Only universities","Only NASA"],"Advanced manufacturing."),
     ("The Perseverance rover's MOXIE instrument:",["Failed","*Successfully produced oxygen from Mars's CO₂ atmosphere","Found water","Found methane"],"ISRU technology demonstration."),
     ("CubeSat technology has enabled:",["Nothing","*Low-cost space missions for universities, startups, and agencies worldwide","Only military use","Only communication"],"Democratized space access."),
     ("Space technology spin-offs to everyday life include:",["Nothing","*Memory foam, water purification, camera phones, scratch-resistant lenses, and many more","Only Tang","Only Velcro"],"Broader societal benefits."),
     ("The Artemis I mission (2022) tested:",["A Mars vehicle","*The SLS rocket and Orion spacecraft on an uncrewed flight around the Moon","A lunar rover","A space station"],"First Artemis flight."),
     ("Studying these case studies shows that space technology:",["Is stagnant","*Is advancing rapidly through innovation, reusability, miniaturization, and international/commercial partnerships","Only changes slowly","Is declining"],"Dynamic field."),
     ("Future technology challenges include:",["Nothing","*Radiation shielding, closed-loop life support, nuclear propulsion, and in-space manufacturing","Only funding","Only politics"],"Engineering frontiers.")]
)
lessons[k]=v

# 7.7
k,v = build_lesson(7,7,"AP Prep: Rocket Science Basics",
    "<h3>AP Prep: Rocket Science Basics</h3>"
    "<h4>Key Principles</h4>"
    "<ul><li><b>Newton's 3rd Law:</b> Exhaust gas exits backward → rocket moves forward.</li>"
    "<li><b>Tsiolkovsky Rocket Equation:</b> Δv = v_e × ln(m₀/m_f). Δv = change in velocity; v_e = exhaust velocity; m₀/m_f = initial/final mass ratio.</li>"
    "<li><b>Specific Impulse (I_sp):</b> Measure of engine efficiency; I_sp = v_e/g₀ (seconds). Higher I_sp = more efficient.</li>"
    "<li><b>Orbital Mechanics:</b> Δv required for orbit changes determined by vis-viva equation and Hohmann transfer calculations.</li></ul>",
    [("Tsiolkovsky Rocket Equation","Δv = v_e × ln(m₀/m_f); relates change in velocity to exhaust velocity and mass ratio."),
     ("Specific Impulse (I_sp)","Measure of rocket engine efficiency; I_sp = v_e/g₀ (seconds); higher = more efficient."),
     ("Thrust","Force produced by a rocket engine: F = ṁ × v_e (mass flow rate × exhaust velocity)."),
     ("Delta-v (Δv)","Total change in velocity a spacecraft can achieve; determines what missions are possible."),
     ("Mass Ratio","m₀/m_f = initial mass / final mass (after fuel burn); higher ratio → more Δv.")],
    [("Rockets work based on Newton's _____ law of motion.",["1st","2nd","*3rd (action-reaction: exhaust goes one way, rocket goes the other)","None"],"Every action has an equal and opposite reaction."),
     ("The Tsiolkovsky rocket equation is Δv = v_e × ln(m₀/m_f). If v_e = 3 km/s and mass ratio = e (≈2.718), then Δv =:",["3 km/s as well","*~3 km/s (ln(e) = 1, so Δv = 3×1 = 3 km/s)","6 km/s","9 km/s"],"ln(e) = 1."),
     ("Specific impulse (I_sp) measures:",["Thrust only","*Engine efficiency: how much Δv per unit of propellant consumed (I_sp = v_e/g₀)","Speed only","Mass only"],"Higher I_sp = less fuel needed."),
     ("Chemical rockets have I_sp of approximately:",["10 s","*~250–450 s","5,000 s","100,000 s"],"Relatively low efficiency but high thrust."),
     ("Ion engines have I_sp of approximately:",["100 s","*~1,500–10,000 s (very efficient but very low thrust)","50 s","10 s"],"High efficiency, low thrust."),
     ("The 'tyranny of the rocket equation' means:",["Rockets are always fast","*Exponentially more fuel is needed for proportionally more Δv (mass ratio grows exponentially)","Rockets are cheap","Fuel is free"],"Most of a rocket's mass is fuel."),
     ("Staging (multi-stage rockets) helps because:",["It looks cool","*Discarding empty stages reduces mass, allowing remaining fuel to accelerate a lighter vehicle","It's tradition","No benefit"],"Shed dead weight."),
     ("To reach LEO from Earth requires approximately:",["1 km/s","*~9.4 km/s of Δv (including gravity and drag losses)","100 km/s","0.1 km/s"],"Substantial Δv budget."),
     ("Escape velocity from Earth's surface is:",["1 km/s","*~11.2 km/s","100 km/s","30 km/s"],"Δv needed to leave Earth entirely."),
     ("A Hohmann transfer orbit is the most _____ way to transfer between two circular orbits.",["Fastest","*Fuel-efficient (minimum Δv, but slowest)","Expensive","Random"],"Two-burn maneuver."),
     ("To transfer from LEO to GEO requires a Δv of approximately:",["1 km/s","*~3.9 km/s","10 km/s","0.1 km/s"],"Two burns."),
     ("A Mars mission from LEO requires a Δv of approximately _____ for trans-Mars injection.",["0.5 km/s","*~3.6 km/s","20 km/s","100 km/s"],"Then more for capture and landing."),
     ("Thrust is calculated as F = ṁ × v_e, where ṁ is:",["Mass alone","*Mass flow rate (kg/s) — how fast propellant is expelled","Volume","Temperature"],"More propellant per second = more thrust."),
     ("For AP-level problems, students should understand that Δv budgets determine:",["Nothing","*What missions are possible given a rocket's propellant and engine performance","Only launch dates","Only cost"],"Δv = mission currency."),
     ("Nuclear thermal propulsion offers better I_sp than chemical rockets because:",["It's nuclear","*It heats hydrogen to higher exhaust velocities (~900 s vs ~450 s)","It's cheaper","It's smaller"],"Higher v_e = higher I_sp."),
     ("A spacecraft in orbit is in 'free fall' because:",["Engines are on","*It's continuously falling toward Earth while moving forward fast enough to keep missing it","Gravity is off","It's weightless"],"Orbit = perpetual free fall."),
     ("The Saturn V rocket had a mass ratio allowing it to achieve:",["LEO only","*Enough Δv to send Apollo capsules to the Moon (~12 km/s total Δv)","Only 1 km/s","Escape from the solar system"],"Massive 3-stage rocket."),
     ("Gravity turn launch trajectories are used to:",["Go straight up","*Gradually pitch the rocket sideways during ascent to efficiently enter orbit","Land","Slow down"],"Efficient trajectory."),
     ("Understanding rocket science is essential for:",["Nothing practical","*Space mission planning, evaluating feasibility, and fundamental engineering physics","Only NASA","Only SpaceX"],"Core applied physics."),
     ("The fundamental limitation of rockets in space is:",["Speed of light","Gravity","*The exponential relationship between Δv and propellant mass (rocket equation)","Nothing"],"Most mass must be fuel for large Δv.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Astronomy Unit 7: wrote {len(lessons)} lessons")
