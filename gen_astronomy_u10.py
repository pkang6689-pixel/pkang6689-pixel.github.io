#!/usr/bin/env python3
"""Astronomy Unit 10 – Review & AP Prep (6 lessons)."""
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

# 10.1
k,v = build_lesson(10,1,"Review of Key Concepts",
    "<h3>Review of Key Concepts</h3>"
    "<h4>Foundations (Units 1–3)</h4>"
    "<ul><li>History of astronomy from ancient observations to modern telescopes.</li>"
    "<li>Earth-Moon-Sun system: seasons, lunar phases, eclipses, tides.</li>"
    "<li>Solar system formation, planet types, Kepler's laws of planetary motion.</li></ul>"
    "<h4>Stars &amp; Galaxies (Units 4–6)</h4>"
    "<ul><li>The Sun: structure, nuclear fusion, solar activity, solar wind.</li>"
    "<li>Stars: properties, HR diagram, stellar evolution (main sequence → giant → remnant).</li>"
    "<li>Galaxies: types, Milky Way, dark matter/energy, expanding universe, Hubble's law.</li></ul>"
    "<h4>Exploration &amp; Life (Units 7–9)</h4>"
    "<ul><li>Space missions, human spaceflight, ISS, future exploration.</li>"
    "<li>Astrobiology: conditions for life, extremophiles, SETI, Drake equation, exoplanets.</li>"
    "<li>Telescopes: ground-based, space-based, radio, spectroscopy, computer modeling.</li></ul>",
    [("Kepler's Laws","Three laws of planetary motion: elliptical orbits, equal areas in equal times, P² ∝ a³."),
     ("HR Diagram","Hertzsprung-Russell diagram plotting luminosity vs. temperature; reveals stellar classification and evolution."),
     ("Hubble's Law","v = H₀d; galaxy recession velocity proportional to distance; evidence for expanding universe."),
     ("Drake Equation","N = R* × f_p × n_e × f_l × f_i × f_c × L; framework for estimating communicating civilizations."),
     ("Spectroscopy","Analyzing light by wavelength to determine composition, temperature, velocity, and other properties.")],
    [("Kepler's third law states that P² ∝ a³, meaning:",["Orbital period is constant","*The square of the orbital period is proportional to the cube of the semi-major axis","Planets orbit in circles","Speed is constant"],"Fundamental orbital relationship."),
     ("The four terrestrial planets are:",["Jupiter, Saturn, Uranus, Neptune","*Mercury, Venus, Earth, Mars","Only Earth and Mars","Mercury, Venus, Jupiter, Mars"],"Rocky, inner planets."),
     ("Nuclear fusion in the Sun converts:",["Iron to gold","*Hydrogen to helium (releasing energy via E = mc²)","Helium to carbon","Oxygen to nitrogen"],"Powers the Sun."),
     ("The main sequence on the HR diagram represents stars that:",["Are dying","*Are fusing hydrogen to helium in their cores (most of a star's lifetime)","Have no fuel","Are forming"],"Stable phase."),
     ("Seasons on Earth are caused by:",["Distance from the Sun","*Earth's 23.5° axial tilt causing varying angles of sunlight during the year","Moon phases","Solar activity"],"Tilt, not distance."),
     ("Lunar eclipses occur when:",["The Moon is between Earth and Sun","*Earth is between the Sun and Moon (Earth's shadow on the Moon)","The Sun is between Earth and Moon","Stars align"],"Full Moon alignment."),
     ("Dark matter is evidenced by:",["Photographs","*Galaxy rotation curves showing more gravitational pull than visible matter can account for","Radio signals","Temperature readings"],"Invisible mass."),
     ("The habitable zone is the region where:",["All stars exist","*Liquid water could exist on a planet's surface","Gravity is zero","There is no radiation"],"Goldilocks zone."),
     ("Transit spectroscopy reveals:",["The number of galaxies","*The chemical composition of an exoplanet's atmosphere during transit","Star size","Moon phases"],"JWST application."),
     ("Hubble's Law (v = H₀d) is evidence for:",["Static universe","*An expanding universe (more distant galaxies recede faster)","Contracting universe","Rotating universe"],"Cosmic expansion."),
     ("The ISS orbits in:",["GEO","*LEO (~400 km altitude)","MEO","Deep space"],"Low Earth Orbit."),
     ("Adaptive optics corrects:",["Mirror size","*Atmospheric turbulence in real time using deformable mirrors","Star color","Telescope weight"],"Sharper ground images."),
     ("Extremophiles demonstrate that life can thrive:",["Only in normal conditions","*In extreme heat, cold, radiation, acidity, salinity, and pressure","Only on Earth's surface","Only in water"],"Expanded habitability."),
     ("The Tsiolkovsky rocket equation relates Δv to:",["Gravity only","*Exhaust velocity and mass ratio (Δv = v_e × ln(m₀/m_f))","Distance only","Time only"],"Fundamental rocket science."),
     ("Radio astronomy can observe through:",["Nothing","*Dust and gas clouds that block visible light","Only clear skies","Only at night"],"Different wavelength advantage."),
     ("The Event Horizon Telescope imaged:",["A star","*The shadow of supermassive black holes (M87* and Sgr A*)","A planet","A nebula"],"VLBI achievement."),
     ("LIGO detected gravitational waves from:",["Planets","*Merging black holes (first detection September 14, 2015)","Stars","Galaxies colliding"],"Spacetime ripples."),
     ("The Fermi Paradox asks:",["How old is Earth?","*If intelligent life should be common, why don't we see evidence of it?","How far is Mars?","What causes tides?"],"Where is everybody?"),
     ("Wien's law relates a blackbody's peak wavelength to:",["Mass","*Temperature (λ_max = b/T; hotter → shorter peak wavelength)","Distance","Size"],"Color-temperature link."),
     ("This review connects themes across all units by emphasizing:",["Only memorization","*How physics principles (gravity, EM radiation, thermodynamics) unify our understanding from planets to galaxies","Only one topic","Only math"],"Unified framework.")]
)
lessons[k]=v

# 10.2
k,v = build_lesson(10,2,"AP Practice: Multiple Choice",
    "<h3>AP Practice: Multiple Choice</h3>"
    "<p>This lesson presents AP-style multiple-choice questions covering all major topics across the course. Focus on applying physics principles, interpreting data, and making quantitative calculations.</p>"
    "<h4>Test Strategy</h4>"
    "<ul><li>Read the question carefully; identify what's being asked.</li>"
    "<li>Eliminate obviously wrong answers first.</li>"
    "<li>For calculations, check units and order of magnitude.</li>"
    "<li>Watch for 'which is NOT' or 'EXCEPT' questions.</li></ul>",
    [("AP Test Strategy","Read carefully, eliminate wrong answers, check units, manage time, answer every question."),
     ("Process of Elimination","Removing clearly incorrect answers increases probability of selecting the correct one."),
     ("Unit Analysis","Checking that units in calculations are consistent; powerful error-detection tool."),
     ("Order of Magnitude","Rough estimation to check if an answer is reasonable (powers of 10)."),
     ("Time Management","Allocate roughly equal time per question; flag difficult ones and return later.")],
    [("A planet at 4 AU from a star takes 8 years to orbit. What is the orbital period of a planet at 1 AU? (Kepler's 3rd law: P²∝a³)",["8 years","4 years","2 years","*1 year (P²=a³ → P²=1³=1 → P=1)"],"P²/a³ is constant."),
     ("A star's spectrum peaks at 500 nm. Using Wien's law (b = 2.9×10⁶ nm·K), its surface temperature is:",["3,000 K","*~5,800 K (T = 2.9×10⁶/500 = 5,800 K)","10,000 K","50,000 K"],"Apply Wien's law."),
     ("An object has a recession velocity of 14,000 km/s. Using H₀ = 70 km/s/Mpc, its distance is:",["100 Mpc","*200 Mpc (d = v/H₀ = 14,000/70 = 200 Mpc)","70 Mpc","1,000 Mpc"],"Hubble's Law."),
     ("A star has a parallax of 0.05 arcseconds. Its distance is:",["5 pc","*20 pc (d = 1/p = 1/0.05 = 20 parsecs)","50 pc","0.05 pc"],"d = 1/p."),
     ("During a planetary transit, the star's brightness decreases by 0.01%. The ratio (R_planet/R_star)² equals:",["0.01","*0.0001 (0.01% = 0.0001)","0.1","0.001"],"R_p/R_* = √0.0001 = 0.01 = 1/100."),
     ("Which is NOT a terrestrial planet?",["Mercury","Venus","Earth","*Neptune (it's a gas/ice giant)"],"Inner rocky vs. outer giant."),
     ("The Sun generates energy primarily through:",["Fission","Chemical burning","*Proton-proton chain fusion (H → He)","Gravitational contraction"],"Nuclear fusion."),
     ("A star cooler than the Sun would appear on the HR diagram:",["Upper left","*To the right of the Sun (cooler = redder = right)","Below and left","Same spot"],"Temperature axis."),
     ("Which observation supports the Big Bang theory?",["Static galaxies","*Cosmic Microwave Background radiation — remnant heat from the early universe","Flat Earth","No redshift"],"Predicted and observed."),
     ("If the mass ratio m₀/m_f = e² (≈7.39) and v_e = 3 km/s, Δv =:",["3 km/s","*6 km/s (Δv = 3 × ln(e²) = 3 × 2 = 6 km/s)","9 km/s","12 km/s"],"Rocket equation."),
     ("The habitable zone around a cooler (M-dwarf) star is _____ than around a Sun-like star.",["Farther","*Closer (less luminosity → need to be nearer for liquid water temperatures)","The same","Nonexistent"],"Luminosity-dependent."),
     ("Spectral lines shifted toward red indicate:",["The object is approaching","*The object is receding (redshift = moving away)","The object is stationary","The object is hot"],"Doppler effect."),
     ("Gravitational waves are produced by:",["Light","*Accelerating massive objects (e.g., merging black holes or neutron stars)","Sound","Heat"],"Einstein predicted them."),
     ("The Drake Equation variable with the MOST uncertainty is:",["R* (star formation rate)","f_p (fraction with planets)","*L (civilization lifetime)","n_e (habitable planets)"],"Sociological, not astronomical."),
     ("An astronaut on the ISS experiences microgravity because:",["There's no gravity","*They're in free fall (continuously falling around Earth)","The ISS blocks gravity","They're too far from Earth"],"Orbit = free fall."),
     ("JWST observes primarily in _____ to see through dust and detect high-redshift objects.",["UV","Visible","*Infrared","X-ray"],"IR penetrates dust."),
     ("The Cepheid period-luminosity relation is used to measure:",["Temperature","*Distance (longer period = more luminous → compare to apparent brightness)","Mass","Age"],"Cosmic distance ladder."),
     ("Which detection method is most productive for finding exoplanets?",["Direct imaging","Radial velocity","*Transit method (Kepler/TESS discovered thousands)","Microlensing"],"Most detections."),
     ("Dark energy is invoked to explain:",["Galaxy rotation","*The accelerating expansion of the universe","Star formation","Planet orbits"],"~68% of the universe's energy."),
     ("Effective AP preparation requires:",["Only memorization","*Understanding underlying physics principles and their application to diverse astronomical contexts","Only reading","Only calculation"],"Conceptual and quantitative.")]
)
lessons[k]=v

# 10.3
k,v = build_lesson(10,3,"AP Practice: Case Studies",
    "<h3>AP Practice: Case Studies</h3>"
    "<p>AP-style questions based on real scenarios requiring multi-step reasoning and data interpretation.</p>"
    "<h4>Approach</h4>"
    "<ul><li>Identify relevant physics principles for each scenario.</li>"
    "<li>Extract data from the problem description.</li>"
    "<li>Show clear reasoning and justify conclusions.</li></ul>",
    [("Case Study Analysis","Applying multiple concepts to a real-world scenario; requires identifying relevant data and principles."),
     ("Multi-Step Reasoning","Breaking complex problems into sequential steps, each applying a specific principle."),
     ("Data Interpretation","Extracting meaning from graphs, spectra, light curves, or numerical data."),
     ("Scientific Justification","Supporting conclusions with evidence and physical reasoning."),
     ("Cross-Unit Integration","Connecting concepts from different units to analyze a single scenario.")],
    [("A transit light curve shows a dip every 3.5 days with depth 0.02. The planet's radius relative to the star is:",["0.02","*~0.14 (√0.02 ≈ 0.141)","0.2","0.5"],"R_p/R_* = √(depth)."),
     ("The same planet's star has a measured radial velocity wobble of 50 m/s. This data constrains the planet's:",["Color","*Minimum mass (radial velocity amplitude depends on planet mass and orbital inclination)","Temperature","Age"],"Ma with sin(i) uncertainty."),
     ("A galaxy's spectrum shows Hα at 672 nm instead of 656.3 nm. Its recession velocity is approximately:",["100 km/s","*~7,170 km/s (Δλ/λ = v/c → v = c × 15.7/656.3 ≈ 7,170 km/s)","50,000 km/s","300,000 km/s"],"Doppler formula."),
     ("Using H₀ = 70 km/s/Mpc, this galaxy's distance is:",["50 Mpc","*~102 Mpc (d = 7,170/70 ≈ 102 Mpc)","500 Mpc","10 Mpc"],"Hubble's Law application."),
     ("A Cepheid variable in a distant galaxy has a period of 30 days. Using the period-luminosity relation, this constrains:",["Its temperature","*Its absolute luminosity (and therefore distance when compared to apparent brightness)","Its color","Its mass"],"Standard candle."),
     ("Mars's thin atmosphere (1% of Earth's) makes landed missions challenging because:",["Landing is easier","*Less atmospheric braking available — spacecraft must use heat shields, parachutes, AND retrorockets","It's too thick","Wind is strong"],"Mars EDL problem."),
     ("An astronomer finds methane AND oxygen in an exoplanet's atmosphere. This is notable because:",["Both are common gases","*They should react and destroy each other — their coexistence suggests a replenishing source (possibly biological)","Neither is important","Only O₂ matters"],"Chemical disequilibrium."),
     ("A binary system shows both spectral lines shifting periodically. Measuring both shifts allows determination of:",["Color only","*The mass ratio of the two stars (and total mass with Kepler's third law)","Distance only","Age only"],"Double-lined spectroscopic binary."),
     ("Europa's induced magnetic field suggests:",["A rocky surface","*A subsurface layer of conducting fluid (salty ocean) beneath the ice shell","No ocean","Strong surface magnets"],"Galileo mission evidence."),
     ("Enceladus ejects material at its south pole. A flythrough mission could directly sample for:",["Rock types","*Organic molecules, salts, and potential biosignatures from the subsurface ocean","Magnetic fields only","Temperature only"],"Direct ocean sampling."),
     ("A star on the HR diagram at high luminosity and low temperature is classified as:",["Main sequence","White dwarf","*Red giant or supergiant","Neutron star"],"Upper-right region."),
     ("If a spacecraft needs 9.4 km/s to reach LEO and v_e = 3 km/s, the mass ratio m₀/m_f must be at least:",["3","10","*~23 (e^(9.4/3) = e^3.13 ≈ 22.9)","100"],"Rocket equation."),
     ("Adaptive optics on ground telescopes achieve near-Hubble image quality by:",["Using bigger mirrors only","*Rapidly deforming a mirror to counteract atmospheric turbulence measured 1000× per second","Pointing differently","Using radio waves"],"Real-time correction."),
     ("The TRAPPIST-1 system is ideal for atmospheric study because:",["The star is hot","*The star is small and cool — planet transits cause relatively large, detectable dips","The planets are far apart","It's near the Sun"],"Small star amplifies signal."),
     ("A neutron star merger (GW170817) was detected in both gravitational waves and light. This 'multi-messenger' approach revealed:",["Nothing new","*The creation of heavy elements, the nature of the merger, and confirmed that gravitational waves travel at light speed","Only waves","Only light"],"Multiple information channels."),
     ("The CMB's tiny temperature fluctuations (~0.00001 K) map:",["Nothing","*Density variations in the early universe that seeded the formation of galaxies and large-scale structure","Only noise","Only errors"],"Seeds of structure."),
     ("Dark energy comprises ~68% of the universe's energy. Its primary evidence comes from:",["Galaxy rotation","*Type Ia supernovae appearing dimmer than expected — the expansion is accelerating","Star formation rates","Planet orbits"],"Accelerating expansion."),
     ("A comet's two tails (ion + dust) always point:",["Toward the Sun","*Generally away from the Sun (ion tail: solar wind; dust tail: slightly curved by gravity)","Toward Jupiter","Randomly"],"Solar wind and radiation pressure."),
     ("The Great Red Spot on Jupiter is:",["A mountain","*A massive, persistent anticyclonic storm (larger than Earth)","A crater","An ocean"],"Atmospheric feature."),
     ("Analyzing case studies demonstrates that astronomy requires:",["Only one skill","*Integration of physics, chemistry, data analysis, and critical thinking across topics","Only memorization","Only observation"],"Interdisciplinary science.")]
)
lessons[k]=v

# 10.4
k,v = build_lesson(10,4,"Real-World Applications of Astronomy",
    "<h3>Real-World Applications of Astronomy</h3>"
    "<h4>Technology Spin-offs</h4>"
    "<p>GPS (relativity corrections), satellite communications, weather forecasting, medical imaging (from X-ray telescope detectors), CCDs (digital cameras), WiFi (radio astronomy signal processing).</p>"
    "<h4>Planetary Defense</h4>"
    "<p>Near-Earth object (NEO) detection and deflection: DART mission successfully altered asteroid Dimorphos's orbit (2022).</p>"
    "<h4>Climate Science</h4>"
    "<p>Understanding solar variability, Earth's energy balance, and planetary atmospheres informs climate modeling.</p>",
    [("GPS Relativity Correction","GPS satellites must account for time dilation (special + general relativity) — clocks run differently in orbit."),
     ("DART Mission","Double Asteroid Redirection Test; NASA kinetic impactor that successfully changed asteroid Dimorphos's orbit in 2022."),
     ("CCD Technology","Charge-Coupled Devices; developed for astronomy, now standard in digital cameras and smartphones."),
     ("Space Weather","Solar activity (flares, CMEs) affecting Earth's technology — power grids, satellites, communications."),
     ("Climate Modeling","Understanding planetary atmospheres and solar variability helps model and predict Earth's climate.")],
    [("GPS satellites must correct for _____ to maintain accuracy.",["Nothing","*Relativistic time dilation (clocks in orbit run differently than on Earth's surface by ~38 μs/day)","Temperature","Humidity"],"Both special and general relativity."),
     ("The DART mission demonstrated:",["Landing on an asteroid","*The ability to change an asteroid's orbit by kinetic impact (planetary defense)","Mining an asteroid","Launching from an asteroid"],"Successful deflection test."),
     ("CCD technology, now in every digital camera, was originally developed for:",["Television","*Astronomy (to capture faint light from distant objects more efficiently than film)","Military","Gaming"],"Technology transfer."),
     ("Space weather includes:",["Rain on the ISS","*Solar flares, coronal mass ejections (CMEs), and solar wind that can disrupt Earth's technology","Wind in space","Cosmic temperature"],"Sun-Earth connection."),
     ("A major solar storm could disrupt:",["Nothing","*Power grids, satellite operations, GPS, communications, and airline operations","Only astronomy","Only space stations"],"Real infrastructure risk."),
     ("Satellite remote sensing helps monitor:",["Nothing on Earth","*Deforestation, ocean temperatures, ice sheets, crop health, and natural disasters","Only space","Only weather"],"Earth observation."),
     ("WiFi technology has roots in:",["Telephone systems","*Radio astronomy signal processing techniques (CSIRO, Australia)","Television","Calculators"],"Unexpected origin."),
     ("Medical imaging technologies (like certain X-ray detectors) were developed for:",["Hospital use only","*Space-based X-ray telescopes (Chandra-type detector technology adapted for medicine)","Military","Entertainment"],"Medical spin-off."),
     ("Understanding planetary atmospheres helps climate science by:",["Being irrelevant","*Providing comparative models (Venus greenhouse effect, Mars atmosphere loss) that inform Earth's climate projections","Only theory","Only for other planets"],"Comparative planetology."),
     ("Near-Earth Objects (NEOs) are tracked because:",["They're interesting","*Some may impact Earth in the future — early detection enables deflection or evacuation","They're pretty","Only for science"],"Planetary defense."),
     ("The Carrington Event (1859) was a massive solar storm that:",["Had no effect","*Disrupted telegraph systems globally — a similar event today could cause trillions of dollars in damage","Only affected weather","Only affected the Sun"],"Historical warning."),
     ("Astronomy education develops:",["Only memorization","*Critical thinking, data analysis, mathematical reasoning, and scientific literacy applicable to many careers","Only fun","Only history knowledge"],"Transferable skills."),
     ("Commercial space activities include:",["Only launches","*Communications (satellites), remote sensing, tourism, manufacturing, and future resource extraction","Only tourism","Only military"],"Growing economy."),
     ("Understanding the Sun's energy output is critical for:",["Nothing practical","*Modeling Earth's climate and energy balance — solar variability affects temperature and weather","Only astronomy","Only space"],"Sun-Earth climate link."),
     ("Asteroid mining could provide:",["Nothing useful","*Rare metals, water (for space fuel), and materials that reduce environmental harm from terrestrial mining","Only rocks","Only iron"],"Future resource."),
     ("The ozone layer's interaction with UV radiation was better understood through:",["Chemistry alone","*Studying planetary atmospheres (Venus, Mars) and the Sun's UV output — comparative approach","Nothing","Biology alone"],"Cross-disciplinary insight."),
     ("International Space Law (Outer Space Treaty, 1967) established:",["No rules","*Space cannot be claimed by nations, weapons of mass destruction banned in orbit, and more","Only US law","Only for the Moon"],"Legal framework."),
     ("Astronomy inspires _____ in STEM fields.",["No one","*The next generation of scientists, engineers, and thinkers — one of the strongest STEM recruitment pathways","Only astronomers","Only school children"],"Inspiration."),
     ("The 'Overview Effect' experienced by astronauts is:",["A visual defect","*A profound cognitive shift — seeing Earth from space increases appreciation for its fragility and unity","A disease","Nothing"],"Perspective change."),
     ("Real-world applications show that astronomy is:",["Purely theoretical with no practical value","*Deeply practical — driving technology, protecting Earth, informing policy, and inspiring society","Only for professionals","Declining in relevance"],"Tangible benefits.")]
)
lessons[k]=v

# 10.5
k,v = build_lesson(10,5,"Capstone: Connecting Astronomy to Other Sciences",
    "<h3>Capstone: Connecting Astronomy to Other Sciences</h3>"
    "<h4>Physics</h4>"
    "<p>Gravity (Newton/Einstein), electromagnetic radiation, nuclear physics, thermodynamics, relativity, quantum mechanics (spectral lines).</p>"
    "<h4>Chemistry</h4>"
    "<p>Stellar nucleosynthesis (origin of elements), spectroscopy, molecular clouds, astrochemistry, planetary atmospheres.</p>"
    "<h4>Biology</h4>"
    "<p>Astrobiology, extremophiles, evolution of life on Earth (astronomy-influenced events like mass extinctions from impacts).</p>"
    "<h4>Earth Science</h4>"
    "<p>Plate tectonics (radioactive decay), climate (solar variability), magnetic field (solar wind protection), tides.</p>",
    [("Stellar Nucleosynthesis","Creation of elements inside stars; lighter elements in main sequence, heavier in supernovae and mergers."),
     ("Interdisciplinary Science","Astronomy connects physics, chemistry, biology, geology, engineering, and computer science."),
     ("Mass Extinction Events","Some caused by asteroid impacts (e.g., Chicxulub ~66 Mya) — astronomy-Earth connection."),
     ("Radioactive Decay","Powers Earth's interior (plate tectonics, magnetic field); elements created in stellar nucleosynthesis."),
     ("Cosmic Perspective","Understanding our place in the universe — from subatomic particles to the cosmic web.")],
    [("Every element heavier than hydrogen and helium was created in:",["The Big Bang","A laboratory","*Stars (fusion) and stellar explosions/mergers (nucleosynthesis)","Earth's core"],"We are star stuff."),
     ("Astronomy relies on physics principles including:",["Only gravity","*Gravity, electromagnetism, nuclear physics, thermodynamics, and relativity","Only optics","Only mechanics"],"Foundation."),
     ("Spectral lines are explained by:",["Classical mechanics","*Quantum mechanics (electrons transitioning between discrete energy levels)","Gravity","Thermodynamics"],"Quantum physics in stars."),
     ("The Chicxulub impact (~66 Mya) caused:",["A new continent","*Mass extinction of dinosaurs — demonstrating the astronomical threat of asteroid impacts","A new ocean","Nothing significant"],"Astronomy-Earth connection."),
     ("Earth's magnetic field, which protects us from solar wind, is powered by:",["The Sun","*Radioactive decay heating Earth's outer core, driving convection (and ultimately the dynamo)","The Moon","Wind"],"Internal heat source."),
     ("The carbon in our bodies was formed in:",["Earth's atmosphere","*Stars (carbon-12 from triple-alpha process in red giant stars)","The ocean","The Big Bang"],"Stellar origin."),
     ("Astrochemistry studies the chemistry of:",["Only Earth","*Interstellar space — molecular clouds contain amino acid precursors, alcohols, sugars, and complex organics","Only planets","Only stars"],"Space chemistry."),
     ("Evolution on Earth has been influenced by astronomical events including:",["Nothing","*Asteroid impacts (mass extinctions), solar variability, and cosmic ray flux changes","Only plate tectonics","Only climate alone"],"Cosmic influences."),
     ("General relativity is essential for understanding:",["Only GPS","*Black holes, gravitational waves, the expanding universe, and gravitational lensing","Only Mercury's orbit","Only time"],"Einstein's framework."),
     ("Computer science contributes to astronomy through:",["Nothing","*Simulations, data analysis, machine learning, telescope control, and data visualization","Only storage","Only typing"],"Computational astronomy."),
     ("Engineering is essential for:",["Only building roads","*Designing telescopes, spacecraft, instruments, launch vehicles, and space habitats","Only manufacturing","Nothing astronomical"],"Making astronomy possible."),
     ("Geology and astronomy connect through:",["Nothing","*Planetary geology (Mars, Moon, asteroids), Earth's formation, radiometric dating, and plate tectonics","Only rocks","Only earthquakes"],"Comparative planetology."),
     ("The laws of physics are the same throughout the universe, as demonstrated by:",["Nothing","*Spectra of distant galaxies showing the same elements and physics as on Earth","Only opinion","Only belief"],"Universality of physics."),
     ("Thermodynamics governs:",["Only engines","*Stellar energy generation, planetary atmospheres, heat transfer in stars, and the evolution of the universe","Only cooking","Only heating"],"Energy and entropy."),
     ("Mathematics in astronomy includes:",["Only addition","*Calculus, statistics, linear algebra, differential equations, and computational methods","Only counting","Only geometry"],"Quantitative science."),
     ("The concept of deep time connects geology and astronomy by showing that:",["Everything is young","*Earth (4.5 Gy) and the universe (13.8 Gy) evolved over immense timescales","Time doesn't matter","Only recent history counts"],"Perspective on time."),
     ("Neutrinos from the Sun confirm that:",["The Sun is cold","*Nuclear fusion is occurring in the Sun's core (detected by underground experiments)","The Sun is dying","Nothing"],"Direct evidence."),
     ("Biology on Earth is connected to astronomy because:",["It's not","*The elements, energy (sunlight), and environments for life all have astronomical origins and influences","Only through water","Only through air"],"Cosmic origins of life."),
     ("The interdisciplinary nature of astronomy prepares students for:",["Only astronomy careers","*Careers in physics, engineering, data science, medicine, policy, education, and many more","Nothing","Only academia"],"Broad preparation."),
     ("The capstone lesson demonstrates that astronomy is:",["Narrow","Disconnected from other sciences","*A unifying science that integrates nearly all STEM disciplines","Only about stars"],"The ultimate interdisciplinary field.")]
)
lessons[k]=v

# 10.6
k,v = build_lesson(10,6,"Comprehensive Review & AP Prep",
    "<h3>Comprehensive Review &amp; AP Prep</h3>"
    "<p>Final preparation covering all ten units with emphasis on:</p>"
    "<ul><li><b>Core formulas:</b> Kepler's 3rd law, Wien's law, Hubble's law, Doppler formula, rocket equation, parallax, inverse-square law, Stefan-Boltzmann law.</li>"
    "<li><b>Key diagrams:</b> HR diagram, light curves, spectra, orbital diagrams, HR evolutionary tracks.</li>"
    "<li><b>Major concepts:</b> Formation and evolution of universe → galaxies → stars → planets → life.</li>"
    "<li><b>Skills:</b> Data interpretation, calculation, scientific reasoning, and connecting concepts across units.</li></ul>",
    [("Stefan-Boltzmann Law","L = 4πR²σT⁴; luminosity depends on radius squared and temperature to the fourth power."),
     ("Inverse-Square Law","Brightness decreases with the square of distance: b = L/(4πd²)."),
     ("Parallax Formula","d(pc) = 1/p(arcsec); fundamental distance measurement for nearby stars."),
     ("Wien's Law","λ_max = b/T; peak wavelength inversely proportional to temperature (b = 2.9 × 10⁶ nm·K)."),
     ("Cosmic Evolution","Big Bang → atoms → stars → heavy elements → planets → molecules → life → intelligence.")],
    [("Stefan-Boltzmann law: if a star has 2× the Sun's temperature and the same radius, its luminosity is ___× the Sun's.",["2","4","8","*16 (L ∝ T⁴; 2⁴ = 16)"],"Fourth power of temperature."),
     ("Inverse-square law: if a star is moved to 3× its original distance, its apparent brightness becomes:",["1/3","*1/9 (brightness ∝ 1/d²; 1/3² = 1/9)","1/6","1/27"],"Brightness ∝ 1/d²."),
     ("A star with twice the Sun's radius and the same temperature has ___× the Sun's luminosity.",["2","*4 (L ∝ R²; 2² = 4)","8","16"],"Radius squared."),
     ("The sequence of cosmic evolution from the Big Bang to life is:",["Life → stars → atoms","*Big Bang → atoms → stars → heavy elements → planets → molecules → life","Stars → Big Bang → life","Random"],"13.8 billion years."),
     ("The HR diagram relates:",["Mass to distance","*Luminosity (or absolute magnitude) to temperature (or spectral class)","Distance to velocity","Size to color"],"Fundamental stellar classification tool."),
     ("Kepler's 3rd law in SI units (for solar system): P(years)² = a(AU)³. If a = 8 AU, P =:",["8 years","16 years","*~22.6 years (P² = 8³ = 512, P = √512 ≈ 22.6)","64 years"],"Apply the law."),
     ("A light curve with periodic dips of equal depth suggests:",["A supernova","*A planet transiting its star at regular intervals","A binary star","A variable star"],"Exoplanet transit."),
     ("Red, orange, yellow, white, blue ordering of star colors corresponds to _____ temperature.",["Decreasing","Random","*Increasing (red coolest → blue hottest)","Same"],"Color-temperature scale."),
     ("Evidence for the Big Bang includes:",["Nothing","*CMB, Hubble's Law (expansion), light element abundances (H, He ratios), and large-scale structure","Only redshift","Only philosophy"],"Multiple independent lines."),
     ("The cosmic distance ladder proceeds from:",["Hubble's law → parallax","*Parallax → Cepheids → Type Ia supernovae → Hubble's law (increasing distance)","Only one method","Random methods"],"Stepping stones."),
     ("The Sun will eventually become:",["A black hole","A neutron star","*A red giant, then a planetary nebula and white dwarf","A supernova"],"Medium-mass star fate."),
     ("Massive stars (>8 M☉) end their lives as:",["White dwarfs","*Supernovae, leaving neutron stars or black holes","Planetary nebulae","Main sequence stars"],"Explosive death."),
     ("The observable universe is approximately _____ billion light-years in radius.",["1","*46.5 (due to expansion — farther than 13.8 Gly because space expanded)","13.8","100"],"Expansion stretches distances."),
     ("Tides on Earth are caused primarily by:",["Wind","The Sun alone","*The Moon's gravitational pull (with solar contribution)","Earth's rotation alone"],"Differential gravity."),
     ("The four fundamental forces relevant to astronomy are:",["Only gravity","*Gravity, electromagnetism, strong nuclear, and weak nuclear","Only EM","Only two"],"All play roles."),
     ("If you observe a star's spectral lines shifted 0.1% to longer wavelengths, the star is:",["Approaching at 300 km/s","*Receding at ~300 km/s (v = c × 0.001 = 3×10⁵ × 0.001 = 300 km/s)","Stationary","Spinning"],"Doppler formula."),
     ("The most abundant element in the universe is:",["Oxygen","Carbon","Helium","*Hydrogen (~75% by mass)"],"Primordial nucleosynthesis."),
     ("A complete understanding of astronomy requires integrating knowledge from:",["Only this course","*Physics, chemistry, biology, math, computer science, and engineering — astronomy is inherently interdisciplinary","Only physics","Only one field"],"Unified science."),
     ("The key to AP success in astronomy is:",["Memorizing every fact","*Understanding core principles deeply and applying them to novel problems using quantitative reasoning","Guessing","Only reading the textbook"],"Deep understanding."),
     ("Astronomy reveals that humanity is:",["The center of everything","*Part of a vast, evolving cosmos — the atoms in our bodies were forged in stars billions of years ago","Unimportant","Alone"],"Cosmic perspective.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Astronomy Unit 10: wrote {len(lessons)} lessons")
