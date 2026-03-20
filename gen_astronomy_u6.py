#!/usr/bin/env python3
"""Astronomy Unit 6 – Galaxies & Cosmology (7 lessons)."""
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

# 6.1
k,v = build_lesson(6,1,"Types of Galaxies (Spiral, Elliptical, Irregular)",
    "<h3>Types of Galaxies</h3>"
    "<h4>Hubble's Classification (Tuning Fork)</h4>"
    "<ul><li><b>Spiral (S, SB):</b> Flat disk with spiral arms, central bulge, active star formation. Barred spirals (SB) have a central bar. Milky Way is SBbc.</li>"
    "<li><b>Elliptical (E0–E7):</b> Smooth, featureless, ellipsoidal. Older (red) stars; little gas/dust; minimal star formation. Range from nearly spherical (E0) to highly elongated (E7).</li>"
    "<li><b>Irregular (Irr):</b> No defined shape. Often rich in gas and active star formation. Examples: Large & Small Magellanic Clouds.</li></ul>",
    [("Spiral Galaxy","Disk-shaped galaxy with spiral arms, central bulge, and active star formation (e.g., Milky Way, Andromeda)."),
     ("Elliptical Galaxy","Smooth, featureless galaxy of mostly old red stars; little gas or star formation; E0–E7."),
     ("Irregular Galaxy","Galaxy with no definite shape; often gas-rich with active star formation (e.g., Magellanic Clouds)."),
     ("Barred Spiral","Spiral galaxy with a bar-shaped structure through its center; Milky Way is a barred spiral."),
     ("Hubble Tuning Fork","Classification diagram for galaxies: ellipticals on left, spirals branching right (normal and barred).")],
    [("The three main types of galaxies are:",["Stars, planets, moons","*Spiral, elliptical, and irregular","Large, medium, small","Old, new, and dying"],"Hubble classification."),
     ("Spiral galaxies are characterized by:",["Smooth, featureless appearance","*A flat disk with spiral arms, central bulge, and active star formation","No defined shape","Only old stars"],"Arms contain young blue stars and gas."),
     ("The Milky Way is classified as a:",["Regular spiral","Elliptical","*Barred spiral (SBbc)","Irregular"],"Bar structure confirmed."),
     ("Elliptical galaxies contain mostly:",["Young blue stars","Gas and dust","*Older red/yellow stars with little gas or dust","Spiral arms"],"Minimal star formation."),
     ("Elliptical galaxies range in shape from:",["Flat to irregular","*Nearly spherical (E0) to highly elongated (E7)","Only spherical","Only flat"],"Numerical suffix indicates elongation."),
     ("Irregular galaxies have:",["Spiral arms","Ellipsoidal shape","*No well-defined shape; often gas-rich with active star formation","Only old stars"],"Messy morphology."),
     ("The Large and Small Magellanic Clouds are examples of:",["Spiral galaxies","Elliptical galaxies","*Irregular galaxies (satellite galaxies of the Milky Way)","Planetary nebulae"],"Visible from the Southern Hemisphere."),
     ("The Hubble Tuning Fork diagram classifies galaxies by:",["Color only","*Morphology (shape): ellipticals on left, spirals branching right","Distance only","Mass only"],"Classic classification scheme."),
     ("Barred spiral galaxies differ from regular spirals by having:",["More stars","*A bar-shaped structure of stars through the center","No spiral arms","Fewer stars"],"Bar = different matter distribution."),
     ("Spiral arms are regions of:",["Old stars only","*Enhanced star formation (density waves compress gas → new stars)","Empty space","Dark matter only"],"Density wave theory."),
     ("The largest galaxies in the universe are typically:",["Spirals","Irregulars","*Giant ellipticals (can contain trillions of stars)","Dwarf galaxies"],"Supergiant ellipticals at cluster centers."),
     ("The Andromeda Galaxy (M31) is a:",["Dwarf irregular","*Large spiral galaxy (nearest major galaxy to the Milky Way, ~2.5 million ly away)","Elliptical galaxy","Quasar"],"Approaching the Milky Way."),
     ("Dwarf galaxies are:",["The rarest type","*Small galaxies with fewer stars; most common galaxy type by number","The largest","Only theoretical"],"Many orbit larger galaxies."),
     ("Lenticular galaxies (S0) are:",["Spirals with extra arms","*Intermediate between elliptical and spiral: disk shape but no spiral arms","Irregular","Not real"],"Transition type."),
     ("Galaxy mergers can transform:",["Nothing","*Spiral galaxies into elliptical galaxies through gravitational interactions","Ellipticals into irregulars only","Stars into planets"],"Mergers disrupt spiral structure."),
     ("Active star formation is found most commonly in:",["Elliptical galaxies","*Spiral and irregular galaxies (which are gas-rich)","Only dwarf galaxies","Only the Milky Way"],"Gas = fuel for new stars."),
     ("Edwin Hubble's galaxy classification system was introduced in:",["1800","*1926","1960","2000"],"Early 20th century galaxy taxonomy."),
     ("Galaxy morphology depends on:",["Only distance","*Formation history, gas content, mergers, and environment","Only color","Only age"],"Multiple factors."),
     ("Studying galaxy types helps us understand:",["Nothing","*Galaxy formation, evolution, and the large-scale structure of the universe","Only pretty pictures","Only the Milky Way"],"Fundamental extragalactic astronomy."),
     ("The Milky Way and Andromeda will merge in approximately:",["1 million years","*~4.5 billion years","100 billion years","They won't merge"],"'Milkomeda' or 'Milkdromeda.'")]
)
lessons[k]=v

# 6.2
k,v = build_lesson(6,2,"Milky Way Structure",
    "<h3>Milky Way Structure</h3>"
    "<p>Our galaxy is a <b>barred spiral</b> ~100,000 light-years in diameter with ~200–400 billion stars.</p>"
    "<h4>Components</h4>"
    "<ul><li><b>Disk:</b> Spiral arms with young stars, gas, dust. Sun is ~26,000 ly from center in the Orion Arm.</li>"
    "<li><b>Bulge:</b> Central region with older yellow/red stars and Sgr A* (supermassive black hole, ~4 million M☉).</li>"
    "<li><b>Halo:</b> Spherical region with old stars, globular clusters, and dark matter.</li>"
    "<li><b>Dark matter halo:</b> Extends far beyond visible stars; ~85% of total mass.</li></ul>",
    [("Disk","Thin, flat region of the Milky Way containing spiral arms, young stars, gas, and dust."),
     ("Galactic Bulge","Central region of the Milky Way; older stars, bar structure, and the supermassive black hole Sgr A*."),
     ("Galactic Halo","Spherical region surrounding the disk; contains old stars, globular clusters, and dark matter."),
     ("Orion Arm","The spiral arm of the Milky Way where the Sun is located; a minor arm (spur)."),
     ("Globular Cluster","Dense, spherical cluster of ~100,000–1 million old stars orbiting in the galactic halo.")],
    [("The Milky Way is approximately _____ light-years in diameter.",["1,000","10,000","*~100,000","1 million"],"Large barred spiral."),
     ("The Milky Way contains approximately:",["1 million stars","*200–400 billion stars","10 billion stars","A trillion stars"],"Enormous number."),
     ("The Sun is located approximately _____ from the galactic center.",["1,000 ly","*~26,000 ly","50,000 ly","100 ly"],"In the Orion (or Local) Arm."),
     ("The galactic center contains:",["Nothing special","*Sagittarius A* (Sgr A*), a supermassive black hole of ~4 million M☉","A giant star","A nebula"],"Confirmed by star orbits and EHT imaging."),
     ("The galactic disk contains:",["Only old stars","*Young stars, gas, dust, and spiral arms","Only dark matter","Only the bulge"],"Active star formation region."),
     ("The galactic bulge contains mostly:",["Young blue stars","*Older yellow/red stars and the central bar structure","Gas clouds","Planets"],"Old stellar population."),
     ("The galactic halo contains:",["Young stars and gas","*Old stars, globular clusters, and dark matter","Only dust","Only spiral arms"],"Old, metal-poor population."),
     ("Dark matter makes up approximately _____ of the Milky Way's total mass.",["10%","50%","*~85%","0%"],"Dominant mass component."),
     ("We know dark matter exists in the Milky Way because:",["We can see it","*Star orbital velocities don't decrease with distance from center as expected (flat rotation curve)","It emits light","Einstein predicted it must"],"Rotation curve evidence."),
     ("The Sun orbits the galactic center in approximately:",["1 million years","*~225–250 million years (a galactic year)","1 billion years","1,000 years"],"One galactic year."),
     ("The Sun's orbital speed around the galactic center is approximately:",["10 km/s","*~230 km/s","1,000 km/s","Speed of light"],"Quite fast."),
     ("Globular clusters in the halo are:",["Young","Gas-rich","*Old (~10–13 billion years), dense, and spherical","Spiral-shaped"],"Among the oldest objects in the galaxy."),
     ("The Milky Way's spiral arms are named after:",["Scientists","*Constellations they pass through (e.g., Perseus, Sagittarius, Orion)","Planets","Greek gods"],"Directional naming."),
     ("The thick disk vs thin disk of the Milky Way differ in:",["Nothing","*Age and composition — thick disk is older with metal-poorer stars; thin disk has younger, metal-rich stars","Color only","Temperature only"],"Two stellar populations in the disk."),
     ("The Milky Way's bar was confirmed by observations from:",["Hubble","*Spitzer Space Telescope (infrared can see through dust)","Only ground telescopes","Naked eye"],"Infrared penetrates dust."),
     ("The Local Group includes:",["Only the Milky Way","*The Milky Way, Andromeda, Triangulum, and ~80 smaller galaxies","Only spiral galaxies","Millions of galaxies"],"Our small galaxy cluster."),
     ("Mapping the Milky Way is challenging because:",["It's small","*We are inside it and dust blocks visible light in the galactic plane","It's too far","It moves too fast"],"Must use infrared, radio, and other wavelengths."),
     ("21-cm radio emission from neutral hydrogen is useful for mapping because:",["It's loud","*It penetrates dust and reveals the distribution of gas in the spiral arms","It's visible","It comes from stars"],"Radio wavelength passes through dust."),
     ("The Milky Way is part of the _____ supercluster.",["Coma","*Laniakea","Perseus","Hydra"],"Laniakea = 'immense heaven' in Hawaiian."),
     ("Understanding the Milky Way's structure helps us:",["Not at all","*Contextualize our place in the universe and understand galaxy formation/evolution","Only navigate","Only name stars"],"Fundamental galactic astronomy.")]
)
lessons[k]=v

# 6.3
k,v = build_lesson(6,3,"Galaxy Clusters",
    "<h3>Galaxy Clusters &amp; Large-Scale Structure</h3>"
    "<p><b>Galaxy groups:</b> ~50 galaxies (Local Group). <b>Galaxy clusters:</b> 100s–1,000s of galaxies bound by gravity (e.g., Virgo Cluster, Coma Cluster). <b>Superclusters:</b> clusters of clusters.</p>"
    "<h4>Large-Scale Structure</h4>"
    "<p>The universe has a <b>cosmic web</b> of filaments, walls, and voids. Galaxy clusters sit at intersections of filaments. Voids are vast, nearly empty regions.</p>",
    [("Galaxy Cluster","Gravitationally bound collection of hundreds to thousands of galaxies; contain hot intracluster gas and dark matter."),
     ("Local Group","The galaxy group containing the Milky Way, Andromeda, Triangulum, and ~80 smaller galaxies."),
     ("Supercluster","Large-scale agglomeration of galaxy clusters and groups (e.g., Laniakea Supercluster)."),
     ("Cosmic Web","The large-scale structure of the universe: filaments, walls, and voids forming a web-like pattern."),
     ("Void","Vast, nearly empty region of space between filaments in the cosmic web; can be hundreds of Mly across.")],
    [("The Local Group contains approximately:",["2 galaxies","*~80+ galaxies (dominated by Milky Way and Andromeda)","1,000 galaxies","1 million galaxies"],"Small galaxy group."),
     ("Galaxy clusters contain:",["1–10 galaxies","*Hundreds to thousands of galaxies","Only one galaxy","Millions of galaxies"],"Larger than groups."),
     ("The nearest large galaxy cluster to us is the:",["Coma Cluster","*Virgo Cluster (~54 million ly away)","Perseus Cluster","Hercules Cluster"],"Center of the Local Supercluster."),
     ("Superclusters are:",["Smaller than clusters","*Large structures composed of multiple galaxy clusters and groups","Single galaxies","Stars"],"Largest gravitationally connected structures."),
     ("The cosmic web is:",["A theory only","*The observed large-scale structure of the universe: filaments, walls, and voids","A type of galaxy","A spider web in space"],"Confirmed by galaxy surveys."),
     ("Galaxy clusters sit at:",["Random locations","*Intersections and nodes of filaments in the cosmic web","Void centers","The universe's edge"],"Density peaks."),
     ("Voids in the cosmic web are:",["Full of stars","*Vast, nearly empty regions that can span hundreds of millions of light-years","Very small","Full of dark matter only"],"Almost no galaxies."),
     ("Intracluster gas in galaxy clusters is:",["Cold","*Extremely hot (10⁷–10⁸ K) and emits X-rays","Invisible","Nonexistent"],"X-ray luminous."),
     ("Most of the mass in galaxy clusters is:",["In stars","In gas","*In dark matter (~80–85%)","In planets"],"Dark matter dominates."),
     ("Gravitational lensing by galaxy clusters demonstrates:",["Nothing","*The presence of dark matter (bending light from background objects)","The absence of gravity","Only star positions"],"Einstein's prediction confirmed."),
     ("The Bullet Cluster provides evidence for dark matter because:",["Nothing special","*The separation of visible matter (gas) from the gravitational mass (dark matter) during a cluster collision","It's the largest cluster","It contains no gas"],"Dark matter passed through while gas collided."),
     ("Galaxy clusters grow by:",["Shrinking","*Merging with other clusters and accreting matter along cosmic web filaments","Losing galaxies","Not changing"],"Hierarchical structure formation."),
     ("The Sloan Digital Sky Survey (SDSS) mapped:",["Only the Moon","*Millions of galaxies, revealing the cosmic web structure","Only the Sun","Only nearby stars"],"Landmark galaxy survey."),
     ("Redshift surveys reveal the 3D distribution of galaxies by:",["Only imaging","*Using redshift (Hubble's law) to estimate galaxy distances","Only counting","Only parallax"],"Distance from recession velocity."),
     ("The largest known structures in the universe are:",["Galaxy clusters","Superclusters","*Galaxy filaments and walls in the cosmic web (hundreds of Mly)","Individual galaxies"],"Enormous scale."),
     ("The cosmological principle states that on large scales, the universe is:",["Clumpy and asymmetric","*Homogeneous and isotropic (the same everywhere and in every direction)","Flat only","Only expanding"],"Fundamental assumption."),
     ("Dark energy affects large-scale structure by:",["Compressing it","*Accelerating the expansion of the universe, counteracting gravitational clustering on the largest scales","Not affecting it","Creating structure"],"Limits future structure growth."),
     ("Galaxy cluster surveys help constrain:",["Nothing","*Cosmological parameters (dark matter amount, dark energy, and universe geometry)","Only galaxy colors","Only star counts"],"Powerful cosmological probes."),
     ("The CMB (Cosmic Microwave Background) shows seeds of the cosmic web from:",["Yesterday","*~380,000 years after the Big Bang (tiny density fluctuations)","1 billion years ago","Now"],"Earliest observable structure."),
     ("Studying large-scale structure connects galaxy formation to:",["Nothing","*Cosmology, dark matter, dark energy, and the origin and fate of the universe","Only nearby stars","Only individual galaxies"],"Grand unification of astronomy.")]
)
lessons[k]=v

# 6.4
k,v = build_lesson(6,4,"Dark Matter & Dark Energy",
    "<h3>Dark Matter &amp; Dark Energy</h3>"
    "<h4>Dark Matter (~27% of universe)</h4>"
    "<p>Does not emit/absorb light. Evidence: galaxy rotation curves (flat instead of Keplerian decline), gravitational lensing, galaxy cluster dynamics, CMB anisotropies. Candidates: WIMPs, axions.</p>"
    "<h4>Dark Energy (~68% of universe)</h4>"
    "<p>Mysterious force accelerating the universe's expansion. Discovered 1998 via Type Ia supernovae (dimmer than expected at high redshift). Possible explanation: cosmological constant (Λ).</p>",
    [("Dark Matter","Invisible mass (~27% of universe) that doesn't emit or absorb light; detected through gravitational effects."),
     ("Dark Energy","Mysterious component (~68%) driving the accelerated expansion of the universe."),
     ("Rotation Curve","Plot of orbital velocity vs distance from galactic center; flat curves imply dark matter halos."),
     ("Gravitational Lensing","Bending of light from distant objects by massive foreground structures; reveals dark matter distribution."),
     ("Cosmological Constant (Λ)","Einstein's term representing a constant energy density filling space; a candidate for dark energy.")],
    [("Dark matter makes up approximately _____ of the universe's total mass-energy.",["5%","*~27%","68%","100%"],"Intermediate fraction."),
     ("Dark energy makes up approximately _____ of the universe's total mass-energy.",["5%","27%","*~68%","0%"],"Dominant component."),
     ("Ordinary (baryonic) matter makes up approximately _____ of the universe.",["27%","68%","*~5%","50%"],"Only a small fraction!"),
     ("Evidence for dark matter includes:",["Only theory","*Galaxy rotation curves, gravitational lensing, cluster dynamics, and CMB patterns","Only rotation curves","Only mathematical models"],"Multiple independent lines of evidence."),
     ("Galaxy rotation curves show that stars far from the center orbit:",["Slower than expected","*At roughly the same speed as closer stars (flat curve), implying extra unseen mass","Faster than expected","Not at all"],"Don't follow Keplerian decline."),
     ("Gravitational lensing reveals dark matter by:",["Emitting light","*Bending light from background objects, mapping the invisible mass distribution","Absorbing light","Reflecting light"],"Einstein's prediction."),
     ("Leading dark matter candidates include:",["Regular atoms","*WIMPs (Weakly Interacting Massive Particles) and axions","Photons","Neutrinos alone"],"Hypothetical particles."),
     ("Dark matter has been directly detected in labs:",["Yes, confirmed","*Not yet — only indirect gravitational evidence exists","No one is trying","It was detected in 2020"],"Major ongoing experimental effort."),
     ("The accelerating expansion of the universe was discovered in:",["1950","1980","*1998 (by Riess, Schmidt, Perlmutter using Type Ia supernovae)","2020"],"Nobel Prize 2011."),
     ("Type Ia supernovae revealed acceleration because distant ones appeared:",["Brighter than expected","*Dimmer than expected (farther away → expansion accelerating)","The same brightness","Invisible"],"Dimmer = farther = acceleration."),
     ("The cosmological constant (Λ) was originally proposed by:",["Hubble","*Einstein (to allow a static universe; later abandoned but revived as dark energy)","Newton","Hawking"],"Einstein's 'biggest blunder' became relevant."),
     ("If dark energy continues to dominate, the universe will:",["Collapse","*Continue expanding forever, increasingly faster (eventual 'heat death' or 'Big Freeze')","Stop expanding","Oscillate"],"Accelerating expansion."),
     ("The Big Rip scenario proposes that dark energy could:",["Weaken","*Increase to the point that it tears apart galaxies, stars, atoms, and spacetime itself","Disappear","Stay constant"],"Extreme (less favored) scenario."),
     ("Modified Newtonian Dynamics (MOND) is:",["The leading theory","*An alternative to dark matter that modifies gravity at low accelerations (not widely accepted)","A proven theory","A type of dark energy"],"Alternative, but doesn't explain all evidence."),
     ("The CMB provides evidence for dark matter through:",["Its color","*Acoustic oscillations (patterns of density fluctuations match models with dark matter)","Its temperature","Nothing"],"CMB power spectrum."),
     ("The Planck satellite precisely measured:",["Only galaxy positions","*CMB temperature fluctuations, determining the composition of the universe","Only star temperatures","Only distances"],"5% normal, 27% dark matter, 68% dark energy."),
     ("Dark matter and dark energy together comprise:",["50% of the universe","*~95% of the universe's total mass-energy content","10%","100%"],"We understand only ~5%."),
     ("The nature of dark energy is:",["Well understood","*One of the biggest unsolved problems in physics","Solved","Not important"],"Fundamental mystery."),
     ("Experiments like LUX-ZEPLIN (LZ) and XENONnT are searching for:",["Dark energy","*Dark matter particles directly (underground detectors for WIMP interactions)","New elements","New stars"],"Direct detection experiments."),
     ("Understanding dark matter and dark energy is essential for:",["Nothing","*Comprehending the composition, structure, and ultimate fate of the universe","Only cosmologists","Only particle physicists"],"Central to modern physics.")]
)
lessons[k]=v

# 6.5
k,v = build_lesson(6,5,"Expansion of the Universe",
    "<h3>Expansion of the Universe</h3>"
    "<h4>Hubble's Discovery (1929)</h4>"
    "<p>Edwin Hubble showed that galaxies are receding from us, with velocity proportional to distance: <b>v = H₀ × d</b> (Hubble's law). Current H₀ ≈ 70 km/s/Mpc (debated 'Hubble tension').</p>"
    "<h4>Big Bang</h4>"
    "<p>Extrapolating expansion backward → the universe began ~13.8 billion years ago from a hot, dense state. Key evidence: CMB (Cosmic Microwave Background, ~2.7 K), Big Bang nucleosynthesis (predicted H/He ratios), and Hubble expansion.</p>",
    [("Hubble's Law","v = H₀d; recession velocity of a galaxy is proportional to its distance; describes the expanding universe."),
     ("Hubble Constant (H₀)","Rate of expansion; currently ~70 km/s/Mpc; exact value debated ('Hubble tension')."),
     ("Big Bang","The event ~13.8 billion years ago from which the universe expanded from a hot, dense state."),
     ("Cosmic Microwave Background","Relic radiation from ~380,000 years after the Big Bang; observed as ~2.7 K microwave radiation filling all of space."),
     ("Big Bang Nucleosynthesis","Prediction that the early universe produced ~75% H and ~25% He (by mass); matches observations.")],
    [("Hubble's law states that v = H₀d, meaning:",["Closer galaxies move faster","*More distant galaxies recede faster (recession velocity proportional to distance)","All galaxies are stationary","Only nearby galaxies move"],"Linear relationship."),
     ("The Hubble constant (H₀) is approximately:",["10 km/s/Mpc","*~70 km/s/Mpc","700 km/s/Mpc","1,000 km/s/Mpc"],"Debated value."),
     ("The 'Hubble tension' refers to:",["Stress on the telescope","*The discrepancy between H₀ measured from the CMB (~67.4) and from local methods (~73)","Nothing","A broken instrument"],"Major open question in cosmology."),
     ("The expansion of the universe means:",["Galaxies are moving through space","Everything is getting bigger","*Space itself is expanding, carrying galaxies apart","Galaxies are exploding"],"Space expands, not galaxies moving through fixed space."),
     ("Redshift of distant galaxies is evidence of expansion because:",["Galaxies are red","*Light is stretched to longer (redder) wavelengths as space expands","Galaxies are moving toward us","Telescopes add red"],"Cosmological redshift."),
     ("The Big Bang occurred approximately:",["1 billion years ago","*~13.8 billion years ago","100 billion years ago","1 million years ago"],"Age of the universe."),
     ("The Cosmic Microwave Background (CMB) was discovered accidentally in:",["1920","*1965 (by Penzias and Wilson)","2000","1800"],"Radio noise from all directions."),
     ("The CMB has a temperature of approximately:",["100 K","0 K","*~2.7 K (2.725 K)","1,000 K"],"Cooled from ~3,000 K due to expansion."),
     ("The CMB is significant because it:",["Only makes noise","*Provides direct evidence of the Big Bang — the afterglow of the early universe","Proves dark matter","Comes from galaxies"],"Relic radiation."),
     ("Big Bang nucleosynthesis correctly predicted:",["Heavy element abundances","*The primordial hydrogen (~75%) and helium (~25%) mass ratio","Only hydrogen","Only carbon"],"Matches observed abundances."),
     ("The universe is expanding everywhere, meaning:",["Only at the edges","*Every point sees galaxies receding — there is no center of expansion","Only in one direction","There's a central explosion point"],"Expansion is uniform (no center)."),
     ("Olbers' paradox asks why the night sky is dark if the universe has infinite stars:",["It shouldn't be dark","*Resolved because the universe has a finite age, finite expansion, and light from distant stars hasn't reached us yet","Stars are too dim","There aren't enough stars"],"Finite age + expansion."),
     ("The scale factor a(t) describes:",["Galaxy sizes","*How much the universe has expanded at time t relative to now","Star brightness","Nothing"],"a = 1 now; smaller in the past."),
     ("The lookback time of an object at z = 1 (redshift) is approximately:",["1 billion years","*~7.7 billion years","13 billion years","1 million years"],"We see it as it was ~7.7 Gyr ago."),
     ("The observable universe has a radius of approximately:",["1 million ly","*~46.5 billion light-years (due to expansion, farther than 13.8 Gly)","13.8 billion ly exactly","Infinite"],"Larger than age × speed of light due to expansion."),
     ("Inflation theory proposes that in the first fraction of a second, the universe:",["Shrank","*Expanded exponentially fast (solving the horizon and flatness problems)","Stayed the same","Collapsed"],"~10⁻³⁶ to ~10⁻³² s after the Big Bang."),
     ("The flatness problem asks why the universe's geometry is so close to:",["Spherical","*Flat (Euclidean) — which requires precise initial conditions","Hyperbolic","Irregular"],"Inflation explains this fine-tuning."),
     ("The horizon problem asks why the CMB is so:",["Cold","Hot","*Uniform in temperature in all directions (regions that shouldn't have been in contact)","Variable"],"Inflation connected all regions early on."),
     ("Evidence for the Big Bang includes:",["Only expansion","*Hubble expansion, CMB, element abundances, and the evolution of large-scale structure","Only the CMB","Only math"],"Multiple converging lines."),
     ("Understanding the expansion of the universe is foundational for:",["Nothing","*Cosmology — the study of the origin, evolution, and fate of the universe","Only physics","Only philosophy"],"Central to modern science.")]
)
lessons[k]=v

# 6.6
k,v = build_lesson(6,6,"Case Studies in Cosmology",
    "<h3>Case Studies in Cosmology</h3>"
    "<h4>The Hubble Deep Fields</h4>"
    "<p>HST pointed at 'empty' patches of sky for days → revealed thousands of galaxies in tiny areas, showing galaxies at all stages of evolution out to >13 billion light-years.</p>"
    "<h4>JWST's First Deep Field (2022)</h4>"
    "<p>Deepest infrared image ever; revealed galaxies from just 600 million years after the Big Bang. Unexpectedly massive early galaxies challenge formation models.</p>"
    "<h4>Gravitational Wave Cosmology</h4>"
    "<p>LIGO/Virgo detections of merging compact objects provide an independent way to measure the Hubble constant ('standard sirens').</p>",
    [("Hubble Deep Field","Long-exposure HST images of 'empty' sky revealing thousands of distant galaxies; showed galaxy evolution."),
     ("JWST Deep Field","Deepest infrared image (2022); revealed extremely distant, unexpectedly massive early galaxies."),
     ("Standard Siren","Gravitational-wave source whose distance can be inferred from the signal; independent H₀ measurement."),
     ("Galaxy Evolution","How galaxies form, grow, merge, and change over cosmic time."),
     ("Cosmic Dawn","The period when the first stars and galaxies formed, ~100–500 million years after the Big Bang.")],
    [("The Hubble Deep Field (1995) was created by:",["A quick snapshot","*Pointing HST at an apparently empty patch of sky for ~10 days of continuous exposure","Combining all Hubble images","Looking at the Moon"],"Revealed ~3,000 galaxies in a tiny area."),
     ("The Hubble Deep Fields demonstrated that:",["Space is empty","*The universe is filled with galaxies at all distances and evolutionary stages","Only nearby galaxies exist","Only stars exist"],"Profoundly changed our view."),
     ("JWST's first deep field image (SMACS 0723) showed galaxies from:",["1 billion years ago","*As early as ~600 million years after the Big Bang","Only recently","100 billion years ago"],"Extremely early galaxies."),
     ("JWST surprised astronomers by finding:",["Few galaxies","*Unexpectedly massive and mature galaxies in the very early universe","Empty space","Only stars"],"Challenges formation models."),
     ("JWST observes primarily in _____, which is ideal for seeing distant galaxies.",["Visible light","X-rays","*Infrared (light from early galaxies is redshifted to IR)","Radio waves"],"Redshift moves light to longer wavelengths."),
     ("Gravitational-wave 'standard sirens' can measure:",["Galaxy colors","*The Hubble constant independently (distance from GW signal, redshift from EM counterpart)","Star temperatures","Planet sizes"],"GW170817 provided the first measurement."),
     ("The Hubble tension might be resolved by:",["Ignoring it","*New physics, better measurements, or systematic error correction — still an active research area","Only one measurement","Changing the speed of light"],"Open question."),
     ("Galaxy evolution shows that early galaxies were:",["Just like modern ones","*Generally smaller, bluer, more irregular, and forming stars more actively","Non-existent","Perfectly ordered"],"Galaxies grow and evolve."),
     ("The Cosmic Dawn is the period when:",["The Sun formed","*The first stars and galaxies formed (~100–500 Myr after the Big Bang)","The Earth formed","Nothing happened"],"Epoch of first light sources."),
     ("The 'epoch of reionization' was when:",["Stars stopped forming","*UV light from the first stars and galaxies ionized the neutral hydrogen filling the universe","The CMB was produced","Galaxies merged"],"Universe became transparent to UV."),
     ("The Wilkinson Microwave Anisotropy Probe (WMAP) measured:",["Galaxy positions","*CMB temperature fluctuations with high precision, constraining cosmological parameters","Only star temperatures","Only dark energy"],"Pre-Planck CMB mission."),
     ("The Planck satellite improved on WMAP by:",["Not much","*Higher resolution and sensitivity, refining the age, composition, and geometry of the universe","Only confirming WMAP","Being cheaper"],"ESA mission."),
     ("Galaxy surveys like SDSS and DESI map the cosmic web by:",["Taking pictures","*Measuring redshifts of millions of galaxies to build 3D maps of large-scale structure","Only counting galaxies","Only naming galaxies"],"Spectroscopic surveys."),
     ("The DESI (Dark Energy Spectroscopic Instrument) aims to:",["Find aliens","*Map 40+ million galaxies to study dark energy and the expansion history","Only observe stars","Only study the Moon"],"Next-generation survey."),
     ("Simulations like Illustris and EAGLE:",["Are video games","*Model galaxy formation and evolution, comparing to observations to test theories","Only theoretical exercise","Only for fun"],"Computational astrophysics."),
     ("Studying galaxy formation requires understanding:",["Only gravity","*Gravity, gas physics, star formation, black hole feedback, dark matter, and dark energy","Only light","Only names"],"Complex multi-physics problem."),
     ("Baryon acoustic oscillations (BAO) are:",["Sound waves now","*Fossil' imprints of sound waves in the early universe, visible in galaxy distributions; used as a cosmic ruler","Galaxy explosions","Star vibrations"],"Standard ruler for cosmology."),
     ("These case studies demonstrate that cosmology is:",["Finished","*A rapidly advancing field with new observations constantly refining (and challenging) our understanding","Only theoretical","Only mathematical"],"Exciting and dynamic."),
     ("Understanding cosmic history from Big Bang to present involves:",["Only one field","*Particle physics, nuclear physics, thermodynamics, GR, and observational astronomy","Only cosmology","Only philosophy"],"Grand synthesis."),
     ("Students should appreciate that many cosmological questions remain:",["All answered","*Open and actively researched (dark matter nature, dark energy, H₀ tension, early galaxy formation)","Impossible to study","Not important"],"Frontier science.")]
)
lessons[k]=v

# 6.7
k,v = build_lesson(6,7,"AP Prep: Hubble's Law",
    "<h3>AP Prep: Hubble's Law</h3>"
    "<h4>Calculations</h4>"
    "<ul><li><b>v = H₀ × d:</b> v in km/s, d in Mpc, H₀ ≈ 70 km/s/Mpc.</li>"
    "<li><b>Distance:</b> d = v/H₀. If v = 2,100 km/s → d = 2100/70 = 30 Mpc.</li>"
    "<li><b>Redshift:</b> z = Δλ/λ₀ = v/c (for v ≪ c). Higher z = greater distance = looking farther back in time.</li>"
    "<li><b>Age estimate:</b> t ≈ 1/H₀ ≈ 14 billion years (rough upper bound).</li></ul>",
    [("Hubble's Law","v = H₀d; recession velocity = Hubble constant × distance; describes universal expansion."),
     ("Redshift (z)","z = Δλ/λ₀; shift of spectral lines to longer wavelengths due to recession velocity/expansion."),
     ("Megaparsec (Mpc)","1 million parsecs (~3.26 million light-years); standard distance unit in extragalactic astronomy."),
     ("Recession Velocity","Speed at which a galaxy appears to move away due to the expansion of space."),
     ("Lookback Time","Time since light left a distant object; higher redshift → longer lookback time → seeing the past.")],
    [("Using Hubble's law, a galaxy receding at 7,000 km/s is at a distance of:",["10 Mpc","70 Mpc","*100 Mpc (d = 7000/70)","1,000 Mpc"],"d = v/H₀."),
     ("A galaxy at a distance of 50 Mpc has a recession velocity of:",["50 km/s","500 km/s","*3,500 km/s (v = 70 × 50)","7,000 km/s"],"v = H₀ × d."),
     ("The Hubble constant H₀ has units of:",["km/s","Mpc","*km/s/Mpc","years"],"Velocity per unit distance."),
     ("Redshift z = 0.01 means the galaxy's wavelengths are shifted by:",["10%","0.001%","*1%","50%"],"z = Δλ/λ₀ = 0.01 = 1%."),
     ("For low-redshift galaxies, z ≈ v/c. If z = 0.1, v ≈:",["3,000 km/s","*30,000 km/s (0.1 × 300,000 km/s)","300 km/s","300,000 km/s"],"v = z × c."),
     ("A rough estimate of the age of the universe from H₀ is:",["1 billion years","*~1/H₀ ≈ 14 billion years","100 billion years","1 million years"],"Hubble time."),
     ("Higher redshift means:",["The galaxy is closer","*The galaxy is farther away and we see it further back in time","The galaxy is blue","Nothing"],"Distance and lookback time increase with z."),
     ("1 Megaparsec (Mpc) equals approximately:",["1 light-year","*3.26 million light-years","1 million km","100 light-years"],"Standard extragalactic unit."),
     ("If a galaxy's Hα line (rest: 656.3 nm) is observed at 662.9 nm, its redshift z is:",["0.1","*~0.01 (z = 6.6/656.3 ≈ 0.01)","1.0","0.001"],"z = Δλ/λ₀ = (662.9−656.3)/656.3."),
     ("Using that z, the galaxy's recession velocity is approximately:",["300 km/s","*~3,000 km/s (z × c = 0.01 × 300,000)","30,000 km/s","300,000 km/s"],"v = zc."),
     ("Its distance from Earth is therefore approximately:",["1 Mpc","10 Mpc","*~43 Mpc (d = 3000/70 ≈ 42.9)","100 Mpc"],"d = v/H₀."),
     ("Hubble's law breaks down for:",["All galaxies","Nearby galaxies","*Very distant galaxies (where relativistic effects and the expansion history matter)","No galaxies"],"At high z, need cosmological models."),
     ("Galaxies within the Local Group do not obey Hubble's law because:",["They're too hot","*They are gravitationally bound and their motions are dominated by gravity, not cosmic expansion","They don't exist","They're moving toward us"],"Bound systems don't expand."),
     ("Andromeda is actually:",["Moving away","Stationary","*Moving toward us (blueshifted); it will merge with the Milky Way)","Invisible"],"Gravitational attraction overcomes expansion."),
     ("The distance ladder uses multiple methods because:",["One method works for everything","*No single method works at all distances; each method calibrates the next","Scientists disagree","It's tradition"],"Parallax → Cepheids → Type Ia SNe."),
     ("Cepheid variables serve as distance indicators because:",["They're always the same distance","*Their pulsation period correlates with luminosity (period-luminosity relation)","They're always the same color","They don't pulsate"],"Henrietta Leavitt's discovery."),
     ("Type Ia supernovae serve as standard candles because:",["They occur frequently","*They have a calibratable peak luminosity (brighter-slower relation)","They're always the same color","Only 1 type exists"],"Distance ladder rung."),
     ("The Tully-Fisher relation connects a spiral galaxy's:",["Color and size","*Rotational velocity and luminosity (faster rotation → more luminous)","Nothing","Distance and temperature"],"Alternative distance indicator."),
     ("For AP exams, students should be able to:",["Only define Hubble's law","*Calculate distances, velocities, and redshifts using Hubble's law formulas","Only describe expansion","Only name galaxies"],"Quantitative skills."),
     ("Hubble's law demonstrates that the universe is:",["Static","Contracting","*Expanding (galaxies recede with velocity proportional to distance)","Oscillating"],"Pillar of modern cosmology.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Astronomy Unit 6: wrote {len(lessons)} lessons")
