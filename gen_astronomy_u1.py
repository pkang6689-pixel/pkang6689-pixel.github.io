#!/usr/bin/env python3
"""Astronomy Unit 1 – Introduction to Astronomy (7 lessons)."""
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

# 1.1
k,v = build_lesson(1,1,"History of Astronomy",
    "<h3>History of Astronomy</h3>"
    "<h4>Ancient Astronomy</h4>"
    "<ul><li><b>Babylonians:</b> Recorded star positions, predicted eclipses.</li>"
    "<li><b>Greeks:</b> Aristotle (geocentric model, Earth is a sphere), Aristarchus (heliocentric idea), Eratosthenes (measured Earth's circumference).</li>"
    "<li><b>Ptolemy:</b> Geocentric model with epicycles — dominant for 1,400 years.</li></ul>"
    "<h4>The Scientific Revolution</h4>"
    "<ul><li><b>Copernicus:</b> Heliocentric model (1543). <b>Galileo:</b> Telescopic observations (moons of Jupiter, Venus phases).</li>"
    "<li><b>Tycho Brahe:</b> Precise observations. <b>Kepler:</b> Laws of planetary motion (elliptical orbits).</li>"
    "<li><b>Newton:</b> Universal gravitation — unified celestial and terrestrial mechanics.</li></ul>",
    [("Geocentric Model","Earth-centered model of the universe championed by Ptolemy; dominated for ~1,400 years."),
     ("Heliocentric Model","Sun-centered model proposed by Copernicus; confirmed by Galileo's observations."),
     ("Kepler's Laws","Three laws describing planetary motion: elliptical orbits, equal areas, period-distance relationship."),
     ("Newton's Law of Gravitation","Every mass attracts every other mass; F = G·m₁·m₂/r²; explains orbital mechanics."),
     ("Galileo Galilei","First to use a telescope for astronomy; observed Jupiter's moons, Venus phases, and lunar craters.")],
    [("The geocentric model placed _____ at the center of the universe.",["The Sun","*The Earth","The Moon","Jupiter"],"Ptolemaic system."),
     ("Copernicus proposed a _____ model.",["Geocentric","*Heliocentric (Sun-centered)","Lunar-centric","Star-centered"],"Published in 1543."),
     ("Galileo's telescopic observations included:",["Only comets","*Moons of Jupiter, phases of Venus, craters on the Moon","Only the Sun","Only stars"],"Evidence supporting heliocentrism."),
     ("Kepler showed that planetary orbits are:",["Circular","*Elliptical (with the Sun at one focus)","Square","Random"],"Kepler's first law."),
     ("Newton's universal gravitation states that:",["Only large objects have gravity","*Every mass attracts every other mass with a force proportional to both masses and inversely proportional to distance squared","Gravity only works on Earth","Gravity decreases linearly"],"F = Gm₁m₂/r²."),
     ("Eratosthenes estimated:",["The mass of the Sun","*Earth's circumference (remarkably accurately using shadow angles)","The distance to stars","The Moon's mass"],"~240 BCE, using geometry in Egypt."),
     ("Ptolemy's model used _____ to explain retrograde motion.",["Heliocentric orbits","*Epicycles (small circles within larger orbital circles)","Gravity","Telescopes"],"Complex but wrong system."),
     ("Tycho Brahe contributed by:",["Using a telescope","*Making the most precise naked-eye astronomical observations of his era","Proposing heliocentrism","Discovering gravity"],"His data enabled Kepler's laws."),
     ("Aristarchus of Samos proposed that:",["Earth is flat","*The Sun is at the center (early heliocentric idea, ~250 BCE)","The Moon produces its own light","Stars are fixed"],"Ahead of his time by 1,800 years."),
     ("The ancient Babylonians contributed to astronomy by:",["Inventing telescopes","*Recording star positions and predicting eclipses","Proposing heliocentrism","Measuring gravity"],"Earliest systematic sky records."),
     ("Which observation by Galileo most strongly supported heliocentrism?",["Sunspots","*Phases of Venus (full cycle only possible if Venus orbits the Sun)","Lunar craters","Star clusters"],"Venus phases prove it orbits the Sun."),
     ("Newton unified astronomy and physics by showing that:",["Gravity only exists in space","*The same laws of gravity govern falling apples and orbiting planets","Planets move randomly","Stars don't attract each other"],"Universal gravitation."),
     ("The Scientific Revolution in astronomy occurred during the:",["Ancient era","*16th-17th centuries","20th century","1st century"],"Copernicus → Galileo → Kepler → Newton."),
     ("Retrograde motion is:",["Planets moving backward in space","*The apparent backward movement of planets as seen from Earth (due to relative orbital speeds)","Stars moving","Comets approaching"],"Geometric illusion."),
     ("The Copernican Revolution refers to:",["A political event","*The paradigm shift from geocentric to heliocentric understanding of the solar system","A type of orbit","A Greek invention"],"Fundamental change in worldview."),
     ("Kepler's second law states that:",["Orbits are circular","*A line from the Sun to a planet sweeps equal areas in equal times (planets move faster near the Sun)","Gravity is constant","Planets don't accelerate"],"Equal area law."),
     ("Kepler's third law relates:",["Mass and distance","*A planet's orbital period squared to its semi-major axis cubed (T² ∝ a³)","Speed and mass","Distance and brightness"],"Period-distance relationship."),
     ("Ancient Greek astronomy was significant because:",["They had telescopes","*They applied reason and geometry to understand celestial phenomena","They only recorded dates","They focused on astrology only"],"Philosophy + mathematics = early science."),
     ("The shift from geocentrism to heliocentrism demonstrates:",["Science never changes","*How scientific understanding evolves through observation, evidence, and critical thinking","Ancient people were wrong about everything","Heliocentrism was always obvious"],"Science is self-correcting."),
     ("Studying the history of astronomy is important because:",["It's not relevant today","*It shows how scientific methods developed and how our understanding of the universe evolved","Only for historians","Only for ancient languages"],"Foundation of modern science.")]
)
lessons[k]=v

# 1.2
k,v = build_lesson(1,2,"Tools of Astronomy (Telescopes, Satellites)",
    "<h3>Tools of Astronomy</h3>"
    "<h4>Telescopes</h4>"
    "<ul><li><b>Refracting:</b> Uses lenses; limited by chromatic aberration and lens size.</li>"
    "<li><b>Reflecting:</b> Uses mirrors (parabolic); larger apertures possible. Newton invented the first.</li>"
    "<li><b>Radio telescopes:</b> Detect radio waves; large dish antennas; can operate day/night, through clouds.</li></ul>"
    "<h4>Space-Based Instruments</h4>"
    "<ul><li><b>Hubble Space Telescope:</b> Optical/UV/IR, above atmosphere → sharp images.</li>"
    "<li><b>James Webb Space Telescope (JWST):</b> Infrared, 6.5 m mirror, L2 orbit → early universe studies.</li>"
    "<li><b>Satellites &amp; probes:</b> Chandra (X-ray), Spitzer (IR), Voyager (interstellar), New Horizons (Pluto).</li></ul>",
    [("Refracting Telescope","Uses lenses to gather and focus light; suffers from chromatic aberration for large sizes."),
     ("Reflecting Telescope","Uses mirrors to gather light; avoids chromatic aberration; can be built much larger than refractors."),
     ("Radio Telescope","Detects radio-wavelength emissions from space; works through clouds and daylight."),
     ("Hubble Space Telescope","Optical/UV/IR space telescope launched 1990; above atmospheric distortion for clear images."),
     ("JWST","James Webb Space Telescope; infrared optimized, 6.5 m mirror; studies early universe, exoplanets.")],
    [("A refracting telescope uses:",["Mirrors","*Lenses","Radio waves","X-rays"],"Refraction bends light through lenses."),
     ("A reflecting telescope uses:",["Lenses","*Mirrors (typically parabolic)","Radio dishes","Prisms"],"Newton invented the first one."),
     ("Chromatic aberration is a problem primarily in:",["Reflecting telescopes","*Refracting telescopes (different wavelengths focus at different points)","Radio telescopes","Space telescopes"],"Color fringing from lens dispersion."),
     ("Radio telescopes can observe:",["Only at night","*Day and night, through clouds and dust","Only in clear weather","Only visible light"],"Radio waves penetrate atmosphere."),
     ("The Hubble Space Telescope is in space because:",["It's cheaper","*Earth's atmosphere blurs images; above it, Hubble gets much sharper observations","It needs zero gravity to work","Closer to stars"],"No atmospheric distortion."),
     ("JWST primarily observes in:",["Visible light","X-rays","*Infrared","Radio waves"],"Infrared penetrates dust and detects redshifted early-universe light."),
     ("JWST is located at Lagrange point L2, which is:",["On the Moon","*~1.5 million km from Earth, opposite the Sun — stable and cold for IR observations","In low Earth orbit","On Mars"],"Sun-Earth L2 point."),
     ("The aperture of a telescope determines:",["Its color","*Its light-gathering power and resolution (larger = more light, finer detail)","Its weight","Its price"],"Bigger aperture = better observations."),
     ("Interferometry in radio astronomy:",["Uses one dish","*Combines signals from multiple telescopes to achieve higher resolution","Reduces resolution","Only works in visible light"],"Array of dishes acts as one giant telescope."),
     ("Chandra X-ray Observatory detects:",["Radio waves","*X-rays from hot gas, black holes, supernova remnants","Visible light","Infrared"],"High-energy X-ray astronomy."),
     ("The Very Large Array (VLA) is:",["One giant telescope","*An array of 27 radio telescopes in New Mexico that work together via interferometry","A space probe","A satellite"],"Y-shaped configuration."),
     ("Adaptive optics in ground-based telescopes:",["Makes telescopes smaller","*Corrects atmospheric turbulence in real-time using deformable mirrors","Blocks radio waves","Enhances infrared"],"Sharpens ground-based images."),
     ("CCDs (charge-coupled devices) in telescopes:",["Record sound","*Convert incoming photons into electronic signals (digital imaging)","Produce light","Reflect light"],"Replaced photographic plates."),
     ("Spectrographs attached to telescopes are used to:",["Take photos only","*Split light into its spectrum to determine composition, temperature, and motion of objects","Increase magnification","Block certain wavelengths"],"Spectroscopy is fundamental."),
     ("The Arecibo telescope (before collapse) was:",["A space telescope","*A 305 m radio telescope in Puerto Rico — one of the largest single-dish radio telescopes","A refractor","An X-ray telescope"],"Iconic instrument."),
     ("Space telescopes are expensive because:",["They use gold","*Building, launching, and maintaining instruments in space is extremely technically challenging","They're large","They're decorative"],"Engineering marvels."),
     ("The electromagnetic spectrum used in astronomy includes:",["Only visible light","*Radio, microwave, infrared, visible, ultraviolet, X-ray, and gamma-ray","Only radio and light","Only X-rays"],"Multi-wavelength astronomy."),
     ("Light pollution affects:",["Only radio telescopes","*Ground-based optical telescopes (artificial light drowns out faint celestial objects)","Space telescopes","Nothing"],"Major problem for observatories."),
     ("Future telescope projects include:",["Only more Hubble mirrors","*Extremely Large Telescope (ELT), Vera Rubin Observatory, Square Kilometre Array (SKA)","Only space missions","Nothing new"],"Next-generation instruments."),
     ("Understanding astronomical tools is important because:",["Tools don't matter","*Every astronomical discovery depends on the instruments used to observe the universe","Only for engineers","Only for NASA"],"Technology drives discovery.")]
)
lessons[k]=v

# 1.3
k,v = build_lesson(1,3,"Scales of the Universe",
    "<h3>Scales of the Universe</h3>"
    "<h4>Distance Measures</h4>"
    "<ul><li><b>AU:</b> Astronomical Unit = average Earth-Sun distance ≈ 150 million km.</li>"
    "<li><b>Light-year:</b> Distance light travels in one year ≈ 9.46 × 10¹² km.</li>"
    "<li><b>Parsec:</b> Based on parallax; 1 pc ≈ 3.26 light-years.</li></ul>"
    "<h4>Cosmic Scale</h4>"
    "<ul><li>Solar system: ~0.001 ly across (to Oort cloud ~1 ly).</li>"
    "<li>Milky Way: ~100,000 ly diameter, ~200-400 billion stars.</li>"
    "<li>Observable universe: ~93 billion ly diameter, ~2 trillion galaxies.</li></ul>",
    [("Astronomical Unit (AU)","Average distance from Earth to the Sun; ~150 million km (93 million miles)."),
     ("Light-Year","Distance light travels in one year; ~9.46 × 10¹² km; used for stellar and galactic distances."),
     ("Parsec","Distance at which 1 AU subtends 1 arcsecond of parallax; ~3.26 light-years."),
     ("Observable Universe","The sphere of space from which light has had time to reach us; ~93 billion ly in diameter."),
     ("Parallax","Apparent shift in position of a nearby star against distant background stars as Earth orbits the Sun.")],
    [("One Astronomical Unit (AU) is approximately:",["The distance to the nearest star","*The average distance from Earth to the Sun (~150 million km)","1 light-year","The diameter of the Milky Way"],"The 'ruler' for the solar system."),
     ("A light-year measures:",["Time","*Distance (how far light travels in one year, ~9.46 × 10¹² km)","Speed","Mass"],"Common misconception — it's distance, not time."),
     ("1 parsec equals approximately:",["1 light-year","*3.26 light-years","10 AU","100 million km"],"Based on parallax geometry."),
     ("Stellar parallax is:",["Star brightness change","*The apparent shift of a nearby star's position due to Earth's orbital motion","A type of eclipse","Star color change"],"Closer stars show larger parallax."),
     ("The nearest star to the Sun (Proxima Centauri) is about:",["1 AU","*4.24 light-years away","100 light-years","1 parsec"],"Our closest stellar neighbor."),
     ("The Milky Way galaxy is approximately _____ in diameter.",["1,000 ly","*100,000 light-years","1 million ly","93 billion ly"],"Our home galaxy."),
     ("The observable universe has a diameter of approximately:",["100,000 ly","1 billion ly","*93 billion light-years","Infinite"],"Finite observational horizon."),
     ("The estimated number of galaxies in the observable universe is:",["1 million","100 million","*~2 trillion","10"],"Mind-boggling number."),
     ("The Milky Way contains approximately:",["1 million stars","*200–400 billion stars","1 trillion stars","10,000 stars"],"Our very average galaxy."),
     ("The cosmic distance ladder refers to:",["A physical ladder","*The series of methods used to measure increasingly larger astronomical distances","A space elevator","A constellation"],"Parallax → Cepheids → Type Ia supernovae → Hubble's law."),
     ("Cepheid variables are used as distance indicators because:",["They are bright","*Their pulsation period is directly related to their luminosity (period-luminosity relation)","They are close","They don't move"],"Standard candles."),
     ("Type Ia supernovae are 'standard candles' because:",["They are common","*They all reach approximately the same peak luminosity → distance can be calculated","They are close by","They are predictable in timing"],"Key tool for measuring cosmological distances."),
     ("The speed of light is approximately:",["300 km/s","*300,000 km/s (3 × 10⁸ m/s)","30,000 km/h","3,000 km/s"],"Fastest speed in the universe."),
     ("Looking at a galaxy 1 billion light-years away means we see it as it was:",["Now","*1 billion years ago (light travel time)","1 million years ago","Yesterday"],"Looking deep into space = looking back in time."),
     ("The solar system (to the Oort Cloud) extends approximately:",["1 AU","*~1 light-year","100 light-years","1 parsec"],"Oort Cloud = outermost boundary."),
     ("Scientific notation is essential in astronomy because:",["Numbers are small","*Astronomical distances and quantities span enormous ranges (10⁸ to 10²⁶ m)","It's simpler to write","It's a tradition"],"Practical necessity."),
     ("The Andromeda Galaxy is about _____ from the Milky Way.",["100 light-years","1,000 light-years","*2.5 million light-years","93 billion light-years"],"Nearest large galaxy; on collision course."),
     ("The Sun is located approximately _____ from the center of the Milky Way.",["At the center","*~26,000 light-years from the center","At the edge","1 AU from center"],"In the Orion Arm."),
     ("The concept of cosmic scale helps us understand:",["Nothing","*Our place in the universe and the vast distances between objects","Only math","Only measurement"],"Cosmic perspective."),
     ("Understanding astronomical scales is essential for:",["Trivia only","*Interpreting observations, calculating travel times, and comprehending the universe's structure","Only astronomers","Nothing practical"],"Foundation of astronomical reasoning.")]
)
lessons[k]=v

# 1.4
k,v = build_lesson(1,4,"Scientific Method in Astronomy",
    "<h3>Scientific Method in Astronomy</h3>"
    "<p>Astronomy uses the same scientific method as other sciences but adapts to unique constraints: objects can't be brought to the lab, experiments are largely observational, and timescales span billions of years.</p>"
    "<h4>Steps Applied to Astronomy</h4>"
    "<ul><li><b>Observation:</b> Telescopes, satellites, ground stations gather data.</li>"
    "<li><b>Hypothesis:</b> Testable explanations (e.g., 'dark matter causes rotation curves').</li>"
    "<li><b>Prediction &amp; Testing:</b> Models predict observations (e.g., CMB); computer simulations.</li>"
    "<li><b>Peer review &amp; publication:</b> Community verifies results.</li></ul>",
    [("Scientific Method","Systematic approach: observation → hypothesis → prediction → testing → conclusion → peer review."),
     ("Hypothesis","A testable, falsifiable explanation for an observed phenomenon."),
     ("Observational Science","Gathering data from natural phenomena without experimental manipulation; astronomy relies heavily on this."),
     ("Peer Review","Process where other scientists evaluate research for accuracy and validity before publication."),
     ("Scientific Theory","A well-tested, broadly accepted explanation supported by extensive evidence (e.g., Big Bang theory).")],
    [("Astronomy is primarily an _____ science.",["Experimental","*Observational (we can't manipulate stars or galaxies in a lab)","Agricultural","Social"],"We observe rather than experiment."),
     ("A scientific hypothesis must be:",["Always correct","*Testable and falsifiable","Just an opinion","A proven fact"],"Must be capable of being disproven."),
     ("The Big Bang theory is called a 'theory' because:",["It's just a guess","*In science, a theory is a well-supported explanation backed by extensive evidence","Scientists aren't sure","It changes every year"],"Theory ≠ guess."),
     ("Computer simulations in astronomy are used to:",["Replace telescopes","*Model complex phenomena (galaxy formation, stellar evolution, climate) that can't be reproduced in labs","Only for games","Make pretty images"],"Computational astrophysics."),
     ("Peer review ensures:",["Papers are always perfect","*Research is scrutinized by other experts before publication for accuracy and validity","No mistakes ever happen","Only popular ideas are published"],"Quality control in science."),
     ("Confirmation bias in astronomy is avoided by:",["Ignoring unexpected results","*Using blind analyses, independent verification, and testing alternative hypotheses","Only publishing expected results","Not sharing data"],"Objectivity."),
     ("The Cosmic Microwave Background (CMB) was predicted by the Big Bang theory and later:",["Never found","*Detected accidentally by Penzias and Wilson (1965) → confirmed the theory","Disproved the theory","Was predicted by Ptolemy"],"Prediction confirmed by observation."),
     ("Controlled experiments are rare in astronomy because:",["Scientists are lazy","*Astronomers cannot manipulate cosmic objects; they rely on observations of natural events","They're not needed","Telescopes are enough"],"Nature runs the experiments."),
     ("Spectroscopy allows astronomers to determine:",["Only distance","*Composition, temperature, density, and radial velocity of celestial objects","Only color","Only size"],"Decoding starlight."),
     ("The principle of uniformity (uniformitarianism) means:",["Physics changes in space","*The same physical laws apply everywhere in the universe","Only Earth laws matter","Laws change over time"],"Physics is universal."),
     ("Astronomical data can be collected at wavelengths that humans cannot see, such as:",["None","*Radio, infrared, ultraviolet, X-ray, and gamma-ray","Only visible","Only radio"],"Multi-wavelength astronomy."),
     ("A null result in an experiment:",["Is a failure","*Can be just as informative as a positive result (e.g., Michelson-Morley experiment disproved the luminiferous aether)","Should be hidden","Means nothing"],"Negative results matter."),
     ("Citizen science projects like Galaxy Zoo:",["Are not useful","*Allow the public to help classify galaxies, contributing to real research","Replace professional astronomers","Only exist for education"],"Public participation in science."),
     ("Replication in astronomy means:",["Repeating an experiment","*Independent teams observing the same phenomenon to verify results","Copying data","Building identical telescopes"],"Verification by independent parties."),
     ("The scientific method is iterative, meaning:",["It's done once","*Results feed back into new questions, hypotheses, and observations","It never ends correctly","It's circular without progress"],"Continuous refinement."),
     ("Occam's razor suggests:",["The most complex explanation is best","*The simplest explanation consistent with the data is preferred","All explanations are equal","Data doesn't matter"],"Parsimony in science."),
     ("An astronomical model is useful when it:",["Looks nice","*Makes accurate, testable predictions that match observations","Is complicated","Is endorsed by one scientist"],"Predictive power = validity."),
     ("Dark matter was hypothesized because:",["It was seen directly","*Galaxy rotation curves and gravitational lensing didn't match predictions from visible matter alone","It was obvious","Telescopes detected it"],"Evidence-based hypothesis."),
     ("Long-term astronomical surveys (e.g., decades) are valuable because:",["They waste time","*Some phenomena change on long timescales (variable stars, orbits, transient events)","Short surveys are always enough","Data becomes outdated"],"Time-domain astronomy."),
     ("Applying the scientific method to astronomy has led to:",["No discoveries","*Understanding stellar evolution, the expanding universe, exoplanets, and the Big Bang","Only theoretical knowledge","Only technology"],"Transformative discoveries.")]
)
lessons[k]=v

# 1.5
k,v = build_lesson(1,5,"Observational Techniques",
    "<h3>Observational Techniques</h3>"
    "<h4>Photometry</h4><p>Measuring the brightness (flux) of celestial objects. Apparent magnitude vs. absolute magnitude.</p>"
    "<h4>Spectroscopy</h4><p>Splitting light into a spectrum to identify composition (absorption/emission lines), temperature, and radial velocity (Doppler shift).</p>"
    "<h4>Astrometry</h4><p>Precise measurement of positions and motions of stars. Used for parallax distances and detecting exoplanets.</p>"
    "<h4>Imaging</h4><p>CCD cameras, filters (UBVRI), and image processing. Multi-wavelength imaging reveals different structures.</p>",
    [("Photometry","Measurement of the brightness (flux) of celestial objects; uses apparent and absolute magnitudes."),
     ("Spectroscopy","Analysis of light spectra to determine composition, temperature, density, and velocity."),
     ("Astrometry","Precise measurement of star positions and proper motions; key for parallax and exoplanet detection."),
     ("Doppler Shift","Change in observed wavelength due to relative motion: blueshift (approaching) or redshift (receding)."),
     ("Apparent Magnitude","How bright a star appears from Earth; depends on luminosity and distance.")],
    [("Photometry measures:",["Star positions","*Brightness (flux) of celestial objects","Star composition","Star distance only"],"Quantity of light received."),
     ("Apparent magnitude describes:",["A star's true brightness","*How bright a star appears from Earth","A star's distance","A star's mass"],"Depends on both luminosity and distance."),
     ("Absolute magnitude indicates:",["Apparent brightness","*A star's true (intrinsic) luminosity measured at a standard distance of 10 parsecs","Distance from Earth","Temperature"],"Removes distance from the comparison."),
     ("The magnitude scale is _____ — a lower number means _____.",["Linear; dimmer","*Logarithmic; brighter","Linear; brighter","Logarithmic; dimmer"],"Mag 1 is brighter than mag 6."),
     ("Spectroscopy reveals a star's:",["Only color","*Composition, temperature, density, and radial velocity","Only brightness","Only position"],"Decoding the message in light."),
     ("Absorption lines in a spectrum occur when:",["Stars emit light","*Cooler gas absorbs specific wavelengths from a continuous spectrum (dark lines)","Light is reflected","Stars are moving away"],"Each element has unique absorption lines."),
     ("Emission lines occur when:",["Light is absorbed","*Hot, low-density gas emits specific wavelengths (bright lines)","Stars are cold","Stars are far away"],"Characteristic wavelengths per element."),
     ("The Doppler effect causes _____ when a star moves toward us.",["Redshift","*Blueshift (shorter wavelengths, higher frequency)","No change","Brightness increase"],"Approaching → blue; receding → red."),
     ("Redshift indicates that an object is:",["Approaching","*Moving away from the observer","Stationary","Getting hotter"],"Wavelengths stretch as source recedes."),
     ("Astrometry measures:",["Brightness","Composition","*Precise positions and motions of stars","Temperature"],"Positional astronomy."),
     ("The Gaia satellite is a major astrometry mission because it:",["Takes photos","*Has measured precise positions, motions, and distances for nearly 2 billion stars","Only studies the Sun","Only observes planets"],"Revolutionizing our map of the Milky Way."),
     ("CCD cameras in astronomy:",["Use film","*Convert photons into electronic signals with high sensitivity and linearity","Only take color photos","Are analog devices"],"Digital imaging revolution."),
     ("Filters (UBVRI) in photometry allow astronomers to:",["Block all light","*Observe in specific wavelength bands to measure color and temperature","Only see in visible light","Increase brightness"],"Multi-band photometry."),
     ("A star's color is related to its:",["Mass only","*Surface temperature (blue = hot, red = cool; Wien's law)","Distance","Age only"],"Wien's law: λ_max ∝ 1/T."),
     ("Proper motion is:",["A star rotating","A star's luminosity change","*A star's apparent movement across the sky over time (true space motion)","A measurement error"],"Detected via astrometry over years."),
     ("Adaptive optics corrects for:",["Lens defects","*Atmospheric turbulence (twinkling) in real-time","Light pollution","Chromatic aberration"],"Deformable mirrors compensate."),
     ("Multi-wavelength astronomy means observing in:",["Only visible light","*Multiple wavelength ranges (radio, IR, visible, UV, X-ray, gamma) to get a complete picture","Only radio","Only X-rays"],"Different wavelengths reveal different physics."),
     ("Image stacking in astrophotography:",["Decreases quality","*Combines many short exposures to reduce noise and reveal faint details","Only works for bright objects","Is outdated"],"Signal averaging."),
     ("Radial velocity measurements detect exoplanets by:",["Imaging them directly","*Measuring tiny Doppler shifts in a star's spectrum caused by an orbiting planet's gravitational tug","Measuring brightness dips","Counting moons"],"Wobble method."),
     ("Observational techniques are the foundation of astronomy because:",["Theory alone is enough","*Without observations, hypotheses cannot be tested and knowledge cannot advance","Techniques are simple","Only professionals need them"],"Data drives understanding.")]
)
lessons[k]=v

# 1.6
k,v = build_lesson(1,6,"Case Studies in Ancient Astronomy",
    "<h3>Case Studies in Ancient Astronomy</h3>"
    "<h4>Stonehenge</h4><p>Neolithic monument in England aligned with summer/winter solstice sunrise/sunset. Likely used as a solar/lunar calendar.</p>"
    "<h4>Ancient Egypt</h4><p>Aligned pyramids with cardinal directions; used the heliacal rising of Sirius to predict Nile floods and define a 365-day calendar.</p>"
    "<h4>Maya Civilization</h4><p>Sophisticated calendar systems; accurately predicted eclipses and tracked Venus. The Dresden Codex contains Venus tables.</p>"
    "<h4>Ancient China &amp; India</h4><p>Detailed eclipse records, star catalogs, and early concepts of cosmic cycles.</p>",
    [("Stonehenge","Neolithic monument aligned with solstice positions; functioned as a prehistoric astronomical calendar."),
     ("Heliacal Rising of Sirius","First visible pre-dawn rising of Sirius; used by Egyptians to predict Nile flooding seasons."),
     ("Maya Astronomy","Mesoamerican civilization with precise calendars, eclipse predictions, and Venus tracking."),
     ("Solstice","Points where the Sun reaches its highest/lowest noon altitude; longest/shortest days."),
     ("Archaeoastronomy","Study of how ancient cultures understood and used celestial phenomena.")],
    [("Stonehenge is aligned with the:",["Equator","*Summer and winter solstice sunrise/sunset","North Star only","Full Moon"],"Solar alignment."),
     ("The Egyptians used the heliacal rising of Sirius to:",["Navigate at sea","*Predict the annual flooding of the Nile and maintain their calendar","Predict earthquakes","Build pyramids"],"Agricultural timing."),
     ("The Maya Dresden Codex contains:",["Only art","*Venus tables and eclipse prediction cycles","Star maps","Solar system models"],"Sophisticated astronomical records."),
     ("The Maya calendar was:",["Simple","*Extremely sophisticated, including a 365-day solar calendar and a 260-day ritual calendar","Based on Ptolemy","Only lunar"],"Multiple interlocking calendar systems."),
     ("Chinese astronomers contributed by:",["Ignoring eclipses","*Recording detailed eclipse records, supernovae (1054 CE), and compiling star catalogs","Only astrology","Nothing significant"],"1054 supernova → Crab Nebula."),
     ("The Great Pyramid of Giza is aligned:",["Randomly","*With remarkable precision to true north (cardinal directions)","With the equator","With Sirius only"],"Precise astronomical surveying."),
     ("Archaeoastronomy is the study of:",["Modern telescopes","*How ancient cultures observed and used celestial events","Only Greek astronomy","Space exploration"],"Interdisciplinary field."),
     ("Ancient astronomy was often linked to:",["Nothing","*Agriculture, religion, calendar-keeping, and navigation","Only entertainment","Only warfare"],"Practical and cultural significance."),
     ("The Antikythera mechanism is:",["A modern computer","*An ancient Greek analog computer (~100 BCE) that predicted eclipses and planetary positions","A type of telescope","A Roman sundial"],"Earliest known astronomical calculator."),
     ("Ancient Polynesian navigators used:",["GPS","*Star positions, wave patterns, and bird migration to navigate vast Pacific Ocean distances","Only compasses","Only maps"],"Celestial navigation expertise."),
     ("These case studies demonstrate that:",["Ancient people were ignorant of the sky","*Humans across all cultures have observed and used celestial patterns for thousands of years","Only Europeans did astronomy","Astronomy is modern only"],"Universal human endeavor."),
     ("The 365-day calendar originated with:",["The Romans","*The Egyptians (based on Sirius cycle and the Nile flood)","The Greeks","The Maya"],"Egyptian civil calendar."),
     ("Solstices occur when:",["The Sun is closest to Earth","*The Sun's declination reaches its maximum north or south position","The Moon crosses the Sun","Day and night are equal"],"Longest/shortest days."),
     ("Equinoxes occur when:",["The Sun is at maximum declination","*The Sun crosses the celestial equator; day and night are approximately equal","The Moon is full","Tides are highest"],"Vernal and autumnal."),
     ("Ancient Indian astronomy included contributions like:",["Nothing","*The concept of a heliocentric model (Aryabhata), precise planetary calculations, and the number zero","Only religious texts","Only calendars"],"Advanced mathematical astronomy."),
     ("The significance of eclipse prediction in ancient cultures was:",["Entertainment only","*Often religious and political — eclipses were seen as omens; predicting them conveyed power","Scientific only","Nothing"],"Cultural and political importance."),
     ("Megalithic structures (like passage graves in Ireland) aligned with:",["Random directions","*Specific astronomical events like the winter solstice sunrise","Only the Moon","Only north"],"Newgrange illuminated at winter solstice."),
     ("The Babylonian sexagesimal (base-60) system gave us:",["Nothing","*60 minutes in an hour, 60 seconds in a minute, and 360 degrees in a circle","Only arithmetic","Only calendars"],"Still used today in timekeeping and angles."),
     ("The study of ancient astronomy matters because:",["Ancient people had telescopes","*It reveals the universal human drive to understand the cosmos and the origins of science","It's only historical","It's not relevant today"],"Roots of modern science."),
     ("Comparing astronomical knowledge across cultures shows:",["Only one culture was right","*Independent development of astronomical understanding across the globe","Ancient cultures copied each other","Astronomy was unimportant"],"Convergent discovery.")]
)
lessons[k]=v

# 1.7
k,v = build_lesson(1,7,"AP Prep: Measurement & Units",
    "<h3>AP Prep: Measurement &amp; Units</h3>"
    "<h4>Key Units</h4>"
    "<ul><li><b>Distance:</b> AU, light-year, parsec, km, m.</li>"
    "<li><b>Mass:</b> kg, solar masses (M☉ = 1.989 × 10³⁰ kg).</li>"
    "<li><b>Temperature:</b> Kelvin (absolute); K = °C + 273.15.</li>"
    "<li><b>Luminosity:</b> Watts; solar luminosity L☉ = 3.828 × 10²⁶ W.</li></ul>"
    "<h4>Key Conversions &amp; Formulas</h4>"
    "<ul><li>d = 1/p (parsec, where p is parallax in arcseconds).</li>"
    "<li>m − M = 5 log₁₀(d/10) (distance modulus).</li>"
    "<li>Wien's law: λ_max = 2.898 × 10⁶ / T (nm, K).</li>"
    "<li>Stefan-Boltzmann: L = 4πR²σT⁴.</li></ul>",
    [("Solar Mass (M☉)","Mass of the Sun; ≈ 1.989 × 10³⁰ kg; used as a standard unit for stellar masses."),
     ("Solar Luminosity (L☉)","Luminosity of the Sun; ≈ 3.828 × 10²⁶ Watts; standard for comparing star brightnesses."),
     ("Distance Modulus","m − M = 5 log₁₀(d/10); relates apparent magnitude, absolute magnitude, and distance in parsecs."),
     ("Wien's Law","λ_max = b/T; hotter objects peak at shorter (bluer) wavelengths; b ≈ 2.898 × 10⁶ nm·K."),
     ("Stefan-Boltzmann Law","L = 4πR²σT⁴; luminosity depends on radius squared and surface temperature to the fourth power.")],
    [("1 AU is approximately:",["1 light-year","*150 million km","1 parsec","10 km"],"Earth-Sun distance."),
     ("1 parsec is approximately:",["1 light-year","*3.26 light-years","1 AU","150 million km"],"Parallax-based distance unit."),
     ("The Kelvin temperature scale starts at:",["0°C","100°C","*Absolute zero (0 K = −273.15°C)","−100°C"],"No negative Kelvin values."),
     ("A star with parallax angle p = 0.1 arcseconds is at a distance of:",["0.1 pc","*10 parsecs","1 pc","100 pc"],"d = 1/p = 1/0.1 = 10 pc."),
     ("Wien's law states that a hotter star has its peak emission at:",["Longer wavelengths","*Shorter wavelengths (bluer light)","The same wavelength","No peak"],"λ_max ∝ 1/T."),
     ("A star with T = 5,800 K (like the Sun) has peak emission at approximately:",["100 nm","*~500 nm (visible, yellow-green)","1,000 nm","10,000 nm"],"λ_max = 2.898×10⁶/5800 ≈ 500 nm."),
     ("The Stefan-Boltzmann law says luminosity depends on:",["Only temperature","Only radius","*Both radius squared AND temperature to the fourth power (L = 4πR²σT⁴)","Only mass"],"Both size and temperature matter."),
     ("If you double a star's temperature (keeping radius the same), luminosity increases by a factor of:",["2","4","8","*16 (2⁴ = 16)"],"L ∝ T⁴."),
     ("If you double a star's radius (keeping temperature the same), luminosity increases by a factor of:",["2","*4 (2² = 4)","16","8"],"L ∝ R²."),
     ("The distance modulus (m − M) = 0 means the star is at:",["100 pc","1 pc","*10 parsecs","1 light-year"],"m − M = 5 log(d/10); if d=10 pc, m−M=0."),
     ("Scientific notation 3 × 10⁸ m/s represents:",["Sound speed","*The speed of light","Earth's orbital speed","The speed of gravity"],"c ≈ 3 × 10⁸ m/s."),
     ("The inverse-square law means light intensity decreases with:",["Distance linearly","*The square of the distance (I ∝ 1/d²)","The cube of the distance","No decrease"],"Double distance = 1/4 brightness."),
     ("Solar luminosity (L☉) is approximately:",["3.828 W","*3.828 × 10²⁶ W","3.828 × 10¹⁰ W","3.828 × 10⁴⁰ W"],"Enormous energy output."),
     ("Solar mass (M☉) is approximately:",["2 × 10²⁰ kg","*~2 × 10³⁰ kg","2 × 10⁴⁰ kg","2 × 10¹⁰ kg"],"~330,000 Earth masses."),
     ("To convert °C to Kelvin:",["Subtract 273","*Add 273.15","Multiply by 1.8","Divide by 2"],"K = °C + 273.15."),
     ("Dimensional analysis helps in astronomy by:",["Making math harder","*Ensuring equations have correct units and catching errors","Only for simple problems","Not being useful"],"Always check units."),
     ("Significant figures are important because:",["They look nice","*They indicate the precision of a measurement","They're just convention","They don't matter in astronomy"],"Precision matters."),
     ("The flux (brightness) received from a star depends on:",["Only luminosity","*Both luminosity and distance (F = L / 4πd²)","Only distance","Only temperature"],"Distance dims light."),
     ("For AP exams, students should be able to:",["Only memorize formulas","*Use formulas to solve problems, interpret data, and apply to real astronomical scenarios","Only define terms","Only convert units"],"Application is key."),
     ("Practice with units and calculations is essential because:",["Math isn't used in astronomy","*Quantitative reasoning is fundamental to astronomical discovery","Only for tests","Only for professionals"],"Astronomy is a quantitative science.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Astronomy Unit 1: wrote {len(lessons)} lessons")
