#!/usr/bin/env python3
"""Anatomy Unit 3 – Muscular System (8 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "anatomy_lessons.json")
COURSE = "Human Anatomy & Physiology"

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

# 3.1
k,v = build_lesson(3,1,"Muscle Tissue Types (Skeletal, Cardiac, Smooth)",
    "<h3>Three Types of Muscle Tissue</h3>"
    "<ul><li><b>Skeletal muscle:</b> Voluntary, striated, multinucleated; attached to bones for movement.</li>"
    "<li><b>Cardiac muscle:</b> Involuntary, striated, branching cells with intercalated discs; found only in the heart.</li>"
    "<li><b>Smooth muscle:</b> Involuntary, nonstriated, spindle-shaped; found in walls of hollow organs (GI tract, blood vessels, bladder).</li></ul>"
    "<h4>Key Differences</h4>"
    "<p>Skeletal is the only type under conscious control. Cardiac muscle is self-exciting (autorhythmicity). Smooth muscle sustains long, slow contractions.</p>",
    [("Skeletal Muscle","Voluntary, striated, multinucleated; moves the skeleton."),
     ("Cardiac Muscle","Involuntary, striated, branching; has intercalated discs; found only in the heart."),
     ("Smooth Muscle","Involuntary, nonstriated, spindle-shaped; lines hollow organs."),
     ("Intercalated Discs","Gap junctions between cardiac muscle cells allowing synchronized contraction."),
     ("Autorhythmicity","The ability of cardiac muscle to generate its own electrical impulses.")],
    [("Which muscle type is voluntary?",["Cardiac","Smooth","*Skeletal","All three"],"Only skeletal muscle is under conscious control."),
     ("Cardiac muscle is found:",["In the intestines","In the arms","*Only in the heart","In blood vessel walls"],"Exclusive to the heart wall."),
     ("Smooth muscle is found in:",["Bones","*Walls of hollow organs (stomach, blood vessels, bladder)","The heart","Skeletal attachments"],"Visceral organs contain smooth muscle."),
     ("Intercalated discs are unique to:",["Skeletal muscle","Smooth muscle","*Cardiac muscle","All muscle types"],"Specialized junctions for cardiac cell communication."),
     ("Striated muscle includes:",["Only skeletal","Only cardiac","*Both skeletal and cardiac","Only smooth"],"Both have visible striations from organized sarcomeres."),
     ("Which muscle type is spindle-shaped with a single nucleus?",["Skeletal","Cardiac","*Smooth","All three"],"Smooth muscle cells are fusiform (spindle)."),
     ("Skeletal muscle cells are:",["Small and round","*Long, cylindrical, and multinucleated","Branching with one nucleus","Spindle-shaped"],"Skeletal fibers are very long and have many nuclei."),
     ("Autorhythmicity describes:",["Skeletal muscle","*Cardiac muscle's ability to self-excite","Smooth muscle contraction","Nerve impulses"],"Cardiac pacemaker cells generate rhythmic impulses."),
     ("Which muscle type contracts most slowly?",["Skeletal","Cardiac","*Smooth","All contract equally"],"Smooth muscle sustains slow, prolonged contractions."),
     ("Peristalsis in the GI tract is performed by:",["Skeletal muscle","Cardiac muscle","*Smooth muscle","Tendons"],"Smooth muscle waves push food through the digestive tract."),
     ("Cardiac muscle fatigue is:",["Common","*Extremely rare (it contracts continuously for life)","Impossible","Frequent during exercise"],"Cardiac muscle has abundant mitochondria and blood supply."),
     ("Skeletal muscle is controlled by:",["Hormones only","*Somatic (voluntary) motor neurons","Autonomic neurons only","No nerves"],"Somatic nervous system controls voluntary movement."),
     ("Smooth and cardiac muscle are regulated by:",["Somatic nerves","*Autonomic nervous system and hormones","Only hormones","Conscious thought"],"Involuntary control."),
     ("The 'striations' in skeletal and cardiac muscle come from:",["Nuclei arrangement","*The organized pattern of actin and myosin filaments (sarcomeres)","Cell membranes","Mitochondria"],"Regular sarcomere banding produces the striated appearance."),
     ("Muscle tissue makes up approximately _____ of body mass.",["10%","25%","*40-50%","75%"],"Skeletal muscle alone is ~40% of body weight."),
     ("Blood vessels contain which muscle type?",["Skeletal","Cardiac","*Smooth","No muscle"],"Vascular smooth muscle controls vessel diameter."),
     ("A cramp in your calf involves:",["Smooth muscle","Cardiac muscle","*Skeletal muscle","No muscle"],"Calf muscles (gastrocnemius, soleus) are skeletal."),
     ("Which has the fastest contraction speed?",["Smooth","Cardiac","*Skeletal","All equal"],"Skeletal muscle can contract very rapidly."),
     ("All three muscle types share the property of:",["Being voluntary","Being striated","*Excitability and contractility","Having intercalated discs"],"All muscle can respond to stimuli and generate force."),
     ("The study of muscles is called:",["Osteology","*Myology","Neurology","Histology"],"Myo- = muscle.")]
)
lessons[k]=v

# 3.2
k,v = build_lesson(3,2,"Muscle Anatomy & Physiology",
    "<h3>Skeletal Muscle Anatomy</h3>"
    "<h4>Organizational Hierarchy</h4>"
    "<ul><li><b>Muscle → Fascicle → Muscle fiber (cell) → Myofibril → Sarcomere</b></li>"
    "<li>Each muscle fiber is a single multinucleated cell wrapped in sarcolemma (cell membrane).</li>"
    "<li>Sarcoplasmic reticulum (SR) stores Ca²⁺ ions.</li></ul>"
    "<h4>Connective Tissue Wrappings</h4>"
    "<ul><li><b>Endomysium:</b> Around each fiber. <b>Perimysium:</b> Around each fascicle. <b>Epimysium:</b> Around the entire muscle.</li></ul>"
    "<h4>Neuromuscular Junction (NMJ)</h4>"
    "<p>Motor neuron meets muscle fiber → acetylcholine (ACh) released → triggers contraction.</p>",
    [("Sarcomere","The basic contractile unit of striated muscle; A band + I band + Z lines."),
     ("Myofibril","A thread-like organelle within a muscle fiber composed of repeating sarcomeres."),
     ("Sarcoplasmic Reticulum","Specialized smooth ER in muscle that stores and releases calcium ions."),
     ("Neuromuscular Junction","The synapse between a motor neuron and a skeletal muscle fiber."),
     ("Acetylcholine (ACh)","Neurotransmitter released at the NMJ that triggers muscle contraction.")],
    [("The basic contractile unit of skeletal muscle is the:",["Myofibril","Fascicle","*Sarcomere","Muscle fiber"],"Sarcomeres are the smallest functional unit."),
     ("The hierarchy from largest to smallest is:",["Sarcomere → Myofibril → Fiber → Fascicle","*Muscle → Fascicle → Fiber → Myofibril → Sarcomere","Fiber → Fascicle → Muscle → Sarcomere","Myofibril → Fiber → Muscle → Fascicle"],"Correct organizational order."),
     ("The sarcolemma is the:",["Cell nucleus","*Plasma membrane of the muscle fiber","Sarcoplasmic reticulum","Connective tissue around a fascicle"],"Sarcolemma = muscle fiber cell membrane."),
     ("The sarcoplasmic reticulum stores:",["ATP","Proteins","*Calcium ions (Ca²⁺)","Sodium"],"SR releases Ca²⁺ to initiate contraction."),
     ("Endomysium wraps around:",["The whole muscle","A fascicle","*A single muscle fiber","A myofibril"],"Endo = within; individual fiber level."),
     ("Perimysium wraps around:",["A single fiber","The whole muscle","*A fascicle (bundle of fibers)","A sarcomere"],"Peri = around; fascicle level."),
     ("Epimysium wraps around:",["A fiber","A fascicle","*The entire muscle","A myofibril"],"Epi = upon; whole muscle level."),
     ("At the NMJ, the neurotransmitter released is:",["Epinephrine","Dopamine","*Acetylcholine (ACh)","Serotonin"],"ACh is the NMJ neurotransmitter."),
     ("ACh binds to receptors on the:",["Nerve terminal","*Sarcolemma (motor end plate)","Sarcoplasmic reticulum","Myofibril"],"ACh activates receptors on the muscle fiber membrane."),
     ("T-tubules function to:",["Store calcium","*Conduct the action potential deep into the muscle fiber","Produce ATP","Remove waste"],"T-tubules carry the signal inward."),
     ("A motor unit consists of:",["One muscle","*One motor neuron and all the muscle fibers it innervates","One sarcomere","The whole nervous system"],"Smallest functional unit of motor control."),
     ("Fine movements (e.g., eye muscles) have motor units with:",["Many fibers","*Few fibers per neuron","No motor units","Only one",""],"Small motor units = precise control."),
     ("The A band of a sarcomere contains:",["Only actin (thin)","*Both actin and myosin (the overlap zone)","Only myosin (thick)","No filaments"],"A band = All of myosin's length, including overlap with actin."),
     ("The I band contains:",["Only myosin","Both actin and myosin","*Only actin (thin filaments, no overlap with myosin)","Connective tissue"],"I band = actin only (no myosin overlap)."),
     ("Z lines (discs) define:",["A band boundaries","*The boundaries of one sarcomere","I band boundaries","The NMJ location"],"Sarcomere = Z line to Z line."),
     ("During contraction, which bands shorten?",["A band","*I band and H zone (Z lines move closer)","Neither","All bands equally"],"A band stays the same; I band and H zone narrow."),
     ("The H zone contains:",["Only actin","*Only myosin (thick filaments, center of the sarcomere)","Both","Calcium"],"Central zone with thick filaments only."),
     ("Acetylcholinesterase:",["Produces ACh","Stores ACh","*Breaks down ACh (terminates the signal)","Releases calcium"],"Enzyme that degrades ACh in the synaptic cleft."),
     ("The 'all-or-none' principle states that:",["Muscles always contract maximally","*A single muscle fiber either contracts fully or not at all (once threshold is reached)","Nerves don't stimulate muscles","All fibers contract simultaneously"],"Individual fibers fully contract or don't."),
     ("Muscle physiology knowledge is essential for understanding:",["Only exercise","*Movement disorders, anesthesia, cardiac function, and athletic performance","Nothing clinical","Only anatomy"],"Broad clinical implications.")]
)
lessons[k]=v

# 3.3
k,v = build_lesson(3,3,"Sliding Filament Theory",
    "<h3>The Sliding Filament Theory</h3>"
    "<p>Muscle contraction occurs when thin filaments (actin) slide over thick filaments (myosin), shortening the sarcomere.</p>"
    "<h4>Steps of the Cross-Bridge Cycle</h4>"
    "<ul><li><b>1.</b> Ca²⁺ released from SR binds to troponin → tropomyosin shifts → exposes binding sites on actin.</li>"
    "<li><b>2.</b> Myosin head (already energized by ATP hydrolysis) binds actin → cross-bridge forms.</li>"
    "<li><b>3.</b> Power stroke: myosin head pivots, pulling actin toward the center (ADP + Pᵢ released).</li>"
    "<li><b>4.</b> New ATP binds myosin → detachment from actin.</li>"
    "<li><b>5.</b> ATP hydrolyzed → myosin re-cocks. Cycle repeats as long as Ca²⁺ is present.</li></ul>",
    [("Sliding Filament Theory","Actin (thin) filaments slide past myosin (thick) filaments, shortening the sarcomere."),
     ("Cross-Bridge Cycle","Myosin heads attach to actin, pivot (power stroke), detach, re-cock — repeating cycle."),
     ("Troponin","Regulatory protein on actin that binds Ca²⁺ and moves tropomyosin off the binding sites."),
     ("Tropomyosin","Protein covering actin binding sites at rest; moves when Ca²⁺ binds troponin."),
     ("Power Stroke","The pivoting of the myosin head that pulls actin, generating force.")],
    [("The sliding filament theory states that:",["Filaments shorten","*Thin filaments slide over thick filaments, shortening the sarcomere","Muscles grow","Sarcomeres break"],"Filaments slide; they don't shorten themselves."),
     ("Thick filaments are made of:",["Actin","Troponin","*Myosin","Tropomyosin"],"Myosin = thick filament."),
     ("Thin filaments are primarily:",["Myosin","*Actin (with troponin and tropomyosin)","Collagen","Elastin"],"Actin + regulatory proteins."),
     ("Contraction begins when Ca²⁺ binds to:",["Myosin","Actin directly","*Troponin","Tropomyosin"],"Ca²⁺ → troponin → conformational change."),
     ("Troponin-Ca²⁺ binding causes:",["Actin to shorten","Myosin to dissolve","*Tropomyosin to shift, exposing actin binding sites","ATP production"],"Removing the tropomyosin block."),
     ("The cross-bridge forms when:",["ATP binds myosin","Ca²⁺ leaves the fiber","*Myosin head binds to the exposed actin site","Tropomyosin covers actin"],"Cross-bridge = myosin-actin attachment."),
     ("The power stroke is powered by:",["New ATP binding","Calcium directly","*Energy stored in the myosin head (from prior ATP hydrolysis)","Sodium ions"],"ATP was already hydrolyzed to 'cock' the head."),
     ("During the power stroke, _____ are released.",["ATP","Ca²⁺","*ADP and Pᵢ (inorganic phosphate)","Troponin"],"Products of the previous ATP hydrolysis."),
     ("Detachment of myosin from actin requires:",["Ca²⁺","ADP","*A new ATP molecule binding to the myosin head","Nothing"],"Without ATP, myosin stays locked (rigor)."),
     ("Rigor mortis occurs because:",["Muscles relax after death","*No ATP is available to detach myosin from actin → muscles stiffen","Ca²⁺ is absent","Muscles contract faster"],"ATP depletion → permanent cross-bridges."),
     ("Ca²⁺ is released from the:",["Mitochondria","Nucleus","*Sarcoplasmic reticulum (SR)","Golgi apparatus"],"SR stores and releases Ca²⁺."),
     ("Ca²⁺ is pumped back into the SR by:",["Passive diffusion","Myosin","*Ca²⁺-ATPase pumps (requires ATP)","Gravity"],"Active transport returns Ca²⁺ → relaxation."),
     ("When Ca²⁺ is pumped back, the muscle:",["Contracts harder","*Relaxes (tropomyosin re-covers actin binding sites)","Dies","Stays contracted"],"Removing Ca²⁺ ends contraction."),
     ("ATP is needed for:",["Contraction only","Relaxation only","*Both contraction (cocking myosin) and relaxation (detachment and Ca²⁺ removal)","Neither"],"ATP powers multiple steps."),
     ("The cross-bridge cycle repeats as long as:",["Myosin is present","ATP runs out","*Ca²⁺ is available and ATP is supplied","The nerve fires once"],"Sustained Ca²⁺ and ATP keep the cycle going."),
     ("How many times can a myosin head cycle per second?",["Once","*About 5 times","100 times","1,000 times"],"Approximately 5 cycles per second during contraction."),
     ("The sarcomere shortens because:",["I bands expand","A bands lengthen","*Z lines are pulled closer together as actin slides inward","Myosin shortens"],"Actin slides → Z lines approach each other."),
     ("During maximal contraction, the H zone:",["Widens","Stays the same","*Disappears (actin filaments overlap in the center)","Doubles"],"Thin filaments completely overlap the thick."),
     ("A muscle cramp may result from:",["Too much ATP","*Failure to pump Ca²⁺ back into the SR (sustained contraction)","Too much relaxation","No nerve signal"],"Prolonged Ca²⁺ in cytoplasm → continuous contraction."),
     ("Understanding the sliding filament theory is key to:",["Only anatomy class","*Understanding muscle diseases, pharmacology, exercise physiology, and cardiac function","Nothing practical","Only sports"],"Foundation for all clinical muscle science.")]
)
lessons[k]=v

# 3.4
k,v = build_lesson(3,4,"Muscle Contraction & Energy Use",
    "<h3>Muscle Contraction &amp; Energy Systems</h3>"
    "<h4>Types of Contraction</h4>"
    "<ul><li><b>Isotonic:</b> Muscle changes length (concentric = shortening, eccentric = lengthening).</li>"
    "<li><b>Isometric:</b> Muscle generates force without changing length (holding a weight still).</li></ul>"
    "<h4>Energy Sources</h4>"
    "<ul><li><b>Immediate:</b> ATP (2–3 sec) → Creatine phosphate (5–8 sec).</li>"
    "<li><b>Short-term:</b> Anaerobic glycolysis (30–60 sec) — glucose → lactic acid + 2 ATP.</li>"
    "<li><b>Long-term:</b> Aerobic (oxidative) metabolism — glucose/fat + O₂ → 36 ATP (sustains long activity).</li></ul>"
    "<h4>Muscle Fatigue</h4>"
    "<p>Decline in force due to ATP depletion, lactic acid buildup, and electrolyte imbalance.</p>",
    [("Isotonic Contraction","Muscle changes length; concentric (shortens) or eccentric (lengthens under load)."),
     ("Isometric Contraction","Muscle generates force without changing length (e.g., holding a wall push)."),
     ("Creatine Phosphate","Immediate energy reserve; donates phosphate to ADP → ATP (lasts ~8 seconds)."),
     ("Anaerobic Glycolysis","Glucose broken down without oxygen; yields 2 ATP + lactic acid."),
     ("Aerobic Metabolism","O₂-dependent breakdown of glucose/fat; yields ~36 ATP per glucose.")],
    [("In a concentric contraction, the muscle:",["Lengthens","Stays the same","*Shortens","Tears"],"Concentric = shortening under load."),
     ("In an eccentric contraction, the muscle:",["Shortens","Stays the same","*Lengthens while under tension","Relaxes completely"],"Lowering a weight slowly = eccentric."),
     ("Isometric contraction means:",["Movement occurs","*Force is generated but no change in muscle length","The muscle relaxes","No force produced"],"Like pushing against a wall."),
     ("The immediate energy source for contraction is:",["Glucose","Fat","*ATP already in the fiber","Oxygen"],"ATP on hand is used first (~2–3 seconds worth)."),
     ("Creatine phosphate provides energy for approximately:",["30 minutes","1 second","*5–8 seconds","5 minutes"],"Quick phosphate transfer to regenerate ATP."),
     ("Anaerobic glycolysis produces:",["36 ATP","0 ATP","*2 ATP (plus lactic acid)","100 ATP"],"Fast but inefficient: 2 net ATP."),
     ("Aerobic metabolism produces approximately:",["2 ATP","*36 ATP per glucose molecule","5 ATP","100 ATP"],"Much more efficient but requires oxygen."),
     ("Aerobic metabolism requires:",["No oxygen","Only fat","*Oxygen (O₂)","Lactic acid"],"Aero- = air/oxygen."),
     ("Lactic acid buildup is associated with:",["Aerobic exercise","*Anaerobic glycolysis (intense short-term exercise)","Rest","Fat metabolism"],"Glycolysis without O₂ produces lactic acid."),
     ("Muscle fatigue results from:",["Too much rest","*ATP depletion, lactic acid accumulation, and electrolyte changes","Strong bones","Excess oxygen"],"Multiple factors contribute to fatigue."),
     ("During a marathon, the primary energy source is:",["Creatine phosphate","Anaerobic glycolysis","*Aerobic metabolism (oxidative phosphorylation)","ATP stores only"],"Long-duration = aerobic (fat + glucose + O₂)."),
     ("A 100-meter sprint primarily uses:",["Aerobic metabolism","Fat only","*ATP stores, creatine phosphate, and anaerobic glycolysis","Protein"],"Short, intense = immediate and anaerobic systems."),
     ("Oxygen debt refers to:",["Needing no oxygen","*Extra O₂ consumed after exercise to restore ATP, creatine phosphate, and remove lactic acid","An inability to breathe","Muscle damage"],"Recovery requires elevated O₂ consumption."),
     ("Which type of muscle fiber is best for endurance?",["Fast-twitch (Type II)","*Slow-twitch (Type I)","Both equally","Neither"],"Type I fibers: slow, oxidative, fatigue-resistant."),
     ("Fast-twitch (Type II) fibers are best for:",["Marathons","Posture","*Short, powerful bursts (sprinting, jumping)","Sleeping"],"Fast, glycolytic, fatigue quickly."),
     ("Which fuel is most energy-dense for muscles?",["Glucose","Protein","*Fat (9 kcal/g vs. 4 kcal/g for carbs)","Water"],"Fat provides the most energy per gram."),
     ("A twitch is:",["A sustained contraction","*A single, brief contraction-relaxation cycle from one stimulus","Relaxation only","Muscle death"],"The simplest muscle response."),
     ("Tetanus (fused) contraction occurs when:",["The muscle relaxes","*Stimuli arrive so rapidly the fiber doesn't relax between twitches","ATP runs out","One stimulus occurs"],"Sustained smooth contraction."),
     ("Muscle tone refers to:",["Maximum contraction","No tension","*Constant, low-level involuntary contractions that keep muscles firm and ready","Only during exercise"],"Tone = baseline tension even at rest."),
     ("Understanding energy metabolism is important for:",["Nothing","*Exercise science, treating metabolic disorders, and nutrition","Only athletes","Only diabetics"],"Energy systems underpin all muscle function and clinical conditions.")]
)
lessons[k]=v

# 3.5
k,v = build_lesson(3,5,"Major Muscle Groups",
    "<h3>Major Muscle Groups</h3>"
    "<h4>Upper Body</h4>"
    "<ul><li><b>Deltoid:</b> Shoulder abduction. <b>Biceps brachii:</b> Elbow flexion/forearm supination. <b>Triceps brachii:</b> Elbow extension.</li>"
    "<li><b>Pectoralis major:</b> Arm flexion/adduction/medial rotation. <b>Latissimus dorsi:</b> Arm extension/adduction.</li></ul>"
    "<h4>Core</h4>"
    "<ul><li><b>Rectus abdominis:</b> Trunk flexion. <b>External/internal obliques:</b> Trunk rotation.</li>"
    "<li><b>Erector spinae:</b> Back extension and posture.</li></ul>"
    "<h4>Lower Body</h4>"
    "<ul><li><b>Quadriceps femoris:</b> Knee extension. <b>Hamstrings:</b> Knee flexion/hip extension. <b>Gluteus maximus:</b> Hip extension. <b>Gastrocnemius:</b> Plantar flexion (calf).</li></ul>",
    [("Biceps Brachii","Anterior upper arm; flexes elbow and supinates forearm."),
     ("Triceps Brachii","Posterior upper arm; extends the elbow."),
     ("Quadriceps Femoris","Four muscles on the anterior thigh; extends the knee."),
     ("Hamstrings","Three posterior thigh muscles; flex the knee and extend the hip."),
     ("Gluteus Maximus","Largest muscle in the body; extends and laterally rotates the hip.")],
    [("The deltoid muscle performs:",["Knee extension","*Shoulder abduction (raising arm to the side)","Elbow flexion","Trunk flexion"],"Deltoid caps the shoulder."),
     ("The biceps brachii primarily:",["Extends the elbow","*Flexes the elbow and supinates the forearm","Extends the knee","Rotates the trunk"],"Bi- = two heads; flexes at the elbow."),
     ("The triceps brachii:",["Flexes the elbow","*Extends the elbow","Flexes the knee","Extends the hip"],"Tri- = three heads; the antagonist of the biceps."),
     ("The pectoralis major is located:",["In the back","*Across the anterior chest","In the leg","In the abdomen"],"Pec major = large chest muscle."),
     ("The latissimus dorsi is in the:",["Anterior chest","*Posterior trunk (back)","Thigh","Neck"],"Lat = broad back muscle."),
     ("The quadriceps group includes:",["2 muscles","3 muscles","*4 muscles (rectus femoris, vastus lateralis, medialis, intermedius)","5 muscles"],"Quad- = four."),
     ("Quadriceps primarily:",["Flex the knee","*Extend the knee","Flex the hip only","Rotate the trunk"],"Knee extension = quads."),
     ("The hamstrings include:",["Quadriceps muscles","*Biceps femoris, semimembranosus, semitendinosus","Rectus abdominis","Gluteus muscles"],"Three muscles on the posterior thigh."),
     ("Hamstrings primarily:",["Extend the knee","*Flex the knee and extend the hip","Extend the knee only","Plantar flex the ankle"],"Antagonists to the quadriceps."),
     ("The gluteus maximus:",["Flexes the hip","*Extends the hip (climbing stairs, standing from a squat)","Extends the knee","Dorsiflexes the ankle"],"The most powerful hip extensor."),
     ("The gastrocnemius performs:",["Knee extension","Dorsiflexion","*Plantar flexion (pointing toes / calf raise)","Hip flexion"],"Calf muscle for pushing off ground."),
     ("The rectus abdominis performs:",["Back extension","*Trunk flexion (sit-ups/crunches)","Arm flexion","Knee extension"],"'Six-pack' muscle flexes the spine."),
     ("The erector spinae:",["Flexes the trunk","*Extends the spine (posture and back extension)","Rotates the hip","Flexes the knee"],"Back extensors maintain upright posture."),
     ("An agonist is:",["A muscle that opposes an action","*The primary mover for a given action","A stabilizer","A synergist"],"The muscle that produces the desired movement."),
     ("An antagonist:",["Assists the agonist","*Opposes the action of the agonist","Stabilizes","Is the same as the agonist"],"E.g., triceps oppose biceps."),
     ("The origin of a muscle is on the:",["*Stationary bone (less movable attachment)","Moving bone","Tendon only","Skin"],"Origin = fixed; insertion = movable."),
     ("The insertion is on the:",["Stationary bone","*Moving bone (the bone that moves when the muscle contracts)","Midpoint","Neither bone"],"Insertion moves toward origin."),
     ("The diaphragm is the primary muscle of:",["*Breathing (inspiration)","Digestion","Circulation","Movement"],"Contracts to pull air into the lungs."),
     ("The sternocleidomastoid muscle:",["Extends the knee","*Flexes and rotates the neck/head","Raises the arm","Flexes the trunk"],"SCM turns and tilts the head."),
     ("Knowing major muscle groups is essential for:",["Nothing practical","*Physical therapy, exercise prescription, surgery, and understanding movement disorders","Only athletes","Only bodybuilders"],"Clinical and practical applications throughout medicine.")]
)
lessons[k]=v

# 3.6
k,v = build_lesson(3,6,"Disorders of the Muscular System",
    "<h3>Disorders of the Muscular System</h3>"
    "<ul><li><b>Muscular dystrophy (MD):</b> Genetic; progressive muscle degeneration. Duchenne MD is the most common childhood form (dystrophin gene mutation).</li>"
    "<li><b>Myasthenia gravis:</b> Autoimmune; antibodies attack ACh receptors at the NMJ → progressive weakness.</li>"
    "<li><b>Fibromyalgia:</b> Chronic widespread muscle pain; cause unknown.</li>"
    "<li><b>Rhabdomyolysis:</b> Rapid muscle breakdown releasing myoglobin → kidney damage.</li>"
    "<li><b>Strains:</b> Overstretched or torn muscle fibers (different from sprains, which involve ligaments).</li></ul>",
    [("Muscular Dystrophy","Genetic disorders causing progressive muscle weakness and degeneration."),
     ("Myasthenia Gravis","Autoimmune disease where antibodies destroy ACh receptors → muscle weakness."),
     ("Fibromyalgia","Chronic condition with widespread musculoskeletal pain and fatigue."),
     ("Rhabdomyolysis","Rapid skeletal muscle destruction releasing myoglobin; can cause kidney failure."),
     ("Strain","Injury to a muscle or tendon (overstretching/tearing).")],
    [("Duchenne muscular dystrophy is caused by:",["Vitamin deficiency","Infection","*A genetic mutation in the dystrophin gene","Overuse"],"X-linked recessive dystrophin gene mutation."),
     ("Myasthenia gravis affects the:",["Bones","Heart","*Neuromuscular junction (ACh receptors)","Intestines"],"Autoantibodies destroy ACh receptors."),
     ("Myasthenia gravis is classified as a(n):",["Genetic disorder","Infectious disease","*Autoimmune disorder","Nutritional deficiency"],"The immune system attacks self-tissues."),
     ("Fibromyalgia is characterized by:",["Muscle wasting","*Chronic widespread pain and fatigue","Joint destruction","Bone loss"],"Pain without identifiable tissue damage."),
     ("Rhabdomyolysis can cause:",["Improved strength","*Acute kidney failure (from myoglobin release)","Better endurance","No complications"],"Myoglobin clogs kidney tubules."),
     ("A muscle strain involves:",["Bone fracture","Ligament tear","*Overstretched or torn muscle fibers/tendons","Joint dislocation"],"Strain = muscle/tendon injury."),
     ("Duchenne MD primarily affects:",["Girls","Adults","*Boys (X-linked recessive)","The elderly"],"Males are primarily affected."),
     ("A common symptom of muscular dystrophy is:",["Increased strength","*Progressive muscle weakness and loss of function","Better coordination","No symptoms"],"Muscles gradually weaken over time."),
     ("DOMS (Delayed Onset Muscle Soreness) occurs:",["During exercise","*24-72 hours after unaccustomed or intense exercise","Only in athletes","Never"],"Microtrauma and inflammation cause delayed soreness."),
     ("Tetanus (the disease) causes:",["Muscle wasting","*Sustained muscle contraction/spasm (lockjaw)","Muscle relaxation","No effect"],"Clostridium tetani toxin prevents relaxation."),
     ("A torn ACL is classified as a:",["Strain","*Sprain (ligament injury, not muscle)","Fracture","Dislocation"],"ACL = ligament → sprain, not strain."),
     ("Compartment syndrome involves:",["Bone fracture","*Increased pressure in a muscle compartment cutting off blood flow","Joint infection","Nerve disease"],"Swelling within a fascial compartment → tissue ischemia."),
     ("Treatment for mild strains includes:",["Surgery immediately","*RICE: Rest, Ice, Compression, Elevation","Vigorous exercise","Ignore it"],"RICE protocol for acute muscle injuries."),
     ("Botulinum toxin (Botox) works by:",["Stimulating ACh release","*Blocking ACh release at the NMJ → muscle paralysis","Strengthening muscles","Producing ACh"],"Prevents neurotransmitter release → relaxation."),
     ("Atrophy refers to:",["Muscle growth","*Decrease in muscle size from disuse, denervation, or disease","Normal tone","Hypertrophy"],"Muscles shrink without stimulation."),
     ("Hypertrophy refers to:",["Muscle shrinkage","*Increase in muscle size (from exercise/use)","Cell multiplication","Fat gain"],"Individual fibers get larger with training."),
     ("Cramps are involuntary:",["Relaxations","*Sustained, painful contractions","Bone movements","Nerve signals only"],"Involuntary tetanic-like contraction."),
     ("Multiple sclerosis (MS) causes muscle weakness because:",["Muscles are diseased","*The immune system destroys myelin on motor nerves → impaired signal transmission","Bones weaken","The heart fails"],"Demyelination slows or blocks nerve impulses."),
     ("Prevention of muscle injuries includes:",["No warm-up","*Proper warm-up, stretching, gradual progression, and adequate hydration","Maximal effort immediately","Skipping rest days"],"Preparation reduces injury risk."),
     ("Understanding muscular disorders helps in:",["Nothing","*Diagnosis, treatment, rehabilitation, and prevention","Only surgery","Only research"],"Clinical knowledge for comprehensive patient care.")]
)
lessons[k]=v

# 3.7
k,v = build_lesson(3,7,"Case Studies in Sports Medicine",
    "<h3>Case Studies in Sports Medicine</h3>"
    "<h4>Case 1: ACL Tear</h4>"
    "<p>A basketball player lands awkwardly → knee gives out. Diagnosis: Anterior cruciate ligament (ACL) tear. Treatment: surgery (graft) + physical therapy rehabilitation.</p>"
    "<h4>Case 2: Rotator Cuff Injury</h4>"
    "<p>A swimmer experiences shoulder pain with overhead motion. Rotator cuff muscles (supraspinatus, infraspinatus, teres minor, subscapularis) stabilize the shoulder.</p>"
    "<h4>Case 3: Achilles Tendon Rupture</h4>"
    "<p>Sudden calf pain during sprinting → unable to plantar flex. The Achilles tendon (calcaneal tendon) connects gastrocnemius/soleus to the calcaneus.</p>",
    [("ACL (Anterior Cruciate Ligament)","Key knee stabilizer preventing anterior tibial translation; common sports injury."),
     ("Rotator Cuff","Four muscles (SITS: supraspinatus, infraspinatus, teres minor, subscapularis) stabilizing the shoulder."),
     ("Achilles Tendon","Thickest and strongest tendon; connects calf muscles to the heel bone (calcaneus)."),
     ("Concussion","Mild traumatic brain injury from a blow to the head; requires careful management."),
     ("CTE","Chronic Traumatic Encephalopathy; degenerative brain disease from repeated head impacts.")],
    [("The ACL prevents:",["Lateral knee movement","*Anterior (forward) translation of the tibia relative to the femur","Posterior knee movement","Hip rotation"],"ACL = anterior cruciate ligament."),
     ("ACL injuries are most common in:",["Swimming","*Cutting/pivoting sports (basketball, soccer, football)","Walking","Sleeping"],"Sudden direction changes stress the ACL."),
     ("The rotator cuff consists of:",["2 muscles","*4 muscles: supraspinatus, infraspinatus, teres minor, subscapularis (SITS)","6 muscles","1 muscle"],"SITS mnemonic."),
     ("Rotator cuff injuries commonly occur in:",["Runners","*Overhead athletes (swimmers, baseball pitchers, tennis players)","Cyclists only","Non-athletes only"],"Repetitive overhead motion stresses the cuff."),
     ("The Achilles tendon attaches to the:",["Tibia","Fibula","*Calcaneus (heel bone)","Patella"],"The thickest tendon inserts on the heel."),
     ("An Achilles tendon rupture results in inability to:",["Flex the knee","*Plantar flex the foot (push off / stand on toes)","Extend the hip","Flex the elbow"],"Loss of calf muscle force transmission."),
     ("RICE stands for:",["Run, Ice, Contract, Elevate","*Rest, Ice, Compression, Elevation","Rehab, Inject, Compress, Exercise","Rest, Inject, Cool, Eat"],"Acute injury management."),
     ("Concussions should be managed by:",["Returning to play immediately","*Removing the athlete from play and following a gradual return-to-play protocol","Ignoring symptoms","Only taking painkillers"],"Brain rest and stepwise return is critical."),
     ("CTE is associated with:",["A single concussion","*Repeated head impacts over time (common in football, boxing)","Knee injuries","Muscle strains"],"Cumulative brain trauma."),
     ("Physical therapy after ACL surgery focuses on:",["Immediate full activity","*Gradually rebuilding strength, range of motion, and proprioception","Bed rest only","Only medication"],"Progressive rehabilitation."),
     ("The PCL (posterior cruciate ligament) prevents:",["*Posterior translation of the tibia","Anterior translation","Medial collapsing","Rotation only"],"PCL opposes the ACL."),
     ("Meniscus tears involve:",["Ligaments","*Cartilage pads in the knee joint","Tendons","Bones"],"Medial/lateral menisci are fibrocartilage shock absorbers."),
     ("Shin splints typically affect:",["The thigh","*The anterior tibial area (front of the lower leg)","The forearm","The shoulder"],"Medial tibial stress syndrome."),
     ("Tennis elbow (lateral epicondylitis) involves:",["The knee","*Inflammation of the lateral elbow tendons from repetitive wrist extension","The shoulder","The ankle"],"Overuse injury of the forearm extensors."),
     ("Hamstring strains are common in:",["Swimmers","*Sprinters and athletes requiring rapid acceleration","Cyclists only","Golfers only"],"Rapid stretch during sprinting tears hamstring fibers."),
     ("What imaging is best for soft tissue injuries?",["X-ray","*MRI","CT scan","PET scan"],"MRI provides excellent soft tissue contrast."),
     ("Performance-enhancing drugs (anabolic steroids) carry risks including:",["No risks","*Liver damage, heart disease, hormonal imbalance, and psychological effects","Only positive effects","Improved health"],"Serious health consequences."),
     ("Proper sports injury prevention includes:",["Extreme training without rest","*Warm-up, conditioning, proper technique, equipment, and rest","Only talent","Avoiding all activity"],"Comprehensive prevention approach."),
     ("Sports medicine integrates knowledge of:",["Only muscles","*Anatomy, physiology, biomechanics, nutrition, and psychology","Only bones","Only surgery"],"A multidisciplinary field."),
     ("Why are case studies valuable in anatomy?",["They're not","*They connect theoretical knowledge to real clinical scenarios","Only for entertainment","They replace textbooks"],"Application deepens understanding and retention.")]
)
lessons[k]=v

# 3.8
k,v = build_lesson(3,8,"AP Prep: Muscle Physiology",
    "<h3>AP Prep: Muscle Physiology</h3>"
    "<p>High-yield review of concepts commonly tested on AP and standardized anatomy exams.</p>"
    "<h4>Must-Know Concepts</h4>"
    "<ul><li>Sliding filament mechanism and the role of Ca²⁺, ATP, actin, myosin.</li>"
    "<li>NMJ: ACh release → depolarization → Ca²⁺ release from SR → contraction.</li>"
    "<li>Muscle fiber types: Type I (slow oxidative) vs. Type IIa/IIb (fast glycolytic).</li>"
    "<li>Length-tension relationship: maximal force at optimal sarcomere overlap.</li>"
    "<li>Graded responses: recruitment, frequency summation, tetanus.</li></ul>",
    [("Motor Unit Recruitment","Activating more motor units to increase force; small units first (size principle)."),
     ("Frequency Summation","Increasing stimulation frequency → increased force → tetanus."),
     ("Length-Tension Relationship","Maximal force is generated when sarcomeres are at optimal actin-myosin overlap."),
     ("Type I Fibers","Slow-twitch, oxidative, fatigue-resistant; endurance activities."),
     ("Type II Fibers","Fast-twitch, glycolytic, fatigue quickly; powerful, rapid movements.")],
    [("The sequence of events at the NMJ is:",["Ca²⁺ → ACh → contraction → AP","*AP arrives → ACh released → binds receptors → muscle AP → Ca²⁺ released → contraction","Contraction → ACh → Ca²⁺","Random"],"Standard NMJ → contraction chain."),
     ("Ca²⁺ in muscle contraction is released from the:",["Mitochondria","Nerve terminal","*Sarcoplasmic reticulum","T-tubules"],"SR is the Ca²⁺ store."),
     ("The size principle of motor unit recruitment states:",["Large units fire first","*Smaller motor units are recruited first; larger ones as more force is needed","All fire simultaneously","Random recruitment"],"Orderly recruitment from small to large."),
     ("Tetanus (physiological) results from:",["Single stimuli","*Rapid, repeated stimuli preventing relaxation between contractions","Muscle disease","Bacterial infection"],"Fused tetanus = smooth, sustained contraction."),
     ("The length-tension relationship shows that maximum force occurs when:",["*Sarcomeres are at optimal actin-myosin overlap","Muscle is fully stretched","Muscle is completely contracted","There is no overlap"],"Too stretched or too compressed = less force."),
     ("Type I (slow-twitch) fibers are rich in:",["Glycogen only","*Mitochondria and myoglobin (red fibers)","Fast glycolytic enzymes","No special features"],"Aerobic machinery for endurance."),
     ("Type IIb fibers are best for:",["Marathons","Posture","*Short, explosive bursts of power","Swimming long distances"],"Fast glycolytic fibers fatigue quickly."),
     ("Wave summation occurs when a second stimulus arrives:",["During relaxation","*Before the muscle fully relaxes from the first stimulus","Hours later","The next day"],"Overlapping twitches = increased force."),
     ("Treppe (staircase effect) is:",["Muscle fatigue","*Progressive increase in contraction force with repeated stimuli (warm-up)","Immediate maximal force","Relaxation"],"Successive twitches become stronger."),
     ("Complete tetanus vs. incomplete tetanus:",["No difference","*Complete = smooth sustained contraction; incomplete = partial relaxation between stimuli","Complete is weaker","Incomplete involves no contraction"],"Frequency determines which type."),
     ("Muscle produces maximum force at:",["Full stretch","Full compression","*Optimal resting length (about 2.0-2.6 μm sarcomere length)","Zero length"],"Where actin-myosin overlap is optimal."),
     ("If a sarcomere is overstretched:",["Force increases","*Force decreases because fewer cross-bridges can form","No change","Muscle tears"],"Less overlap = fewer cross-bridges."),
     ("Acetylcholinesterase is important because it:",["Produces force","*Quickly degrades ACh to prevent continuous stimulation","Releases Ca²⁺","Stores ATP"],"Without it, muscles would stay contracted."),
     ("Curare blocks ACh receptors, causing:",["Increased contraction","*Muscle paralysis (especially respiratory muscles)","No effect","Spasms"],"Competitive inhibitor at the NMJ."),
     ("Succinylcholine causes:",["Permanent paralysis","*Initial depolarization then desensitization (used in surgical anesthesia)","No effect","Increased strength"],"Depolarizing neuromuscular blocker."),
     ("The power stroke is the _____ step of the cross-bridge cycle.",["First","Second","*Third (myosin pivots, pulling actin)","Last"],"After attachment, the head pivots."),
     ("During rigor mortis:",["Muscles are relaxed","*Myosin stays bound to actin because no ATP is available to break the bond","ATP is abundant","Only smooth muscle is affected"],"ATP depletion → locked cross-bridges."),
     ("AP exam free-response may ask you to:",["Only label diagrams","*Explain the mechanism of contraction, energy systems, or neuromuscular signaling","Only define terms","Only list muscles"],"Expect mechanism-based questions."),
     ("Integration question: If Ca²⁺ cannot be released from the SR, what happens?",["Normal contraction","*No contraction (troponin remains blocking binding sites)","Constant contraction","Muscle death"],"Ca²⁺ is the trigger for exposing actin binding sites."),
     ("Quick review: the correct order is:",["ACh → Ca²⁺ → cross-bridge → AP","*Nerve AP → ACh → muscle AP → Ca²⁺ → cross-bridge → contraction","Ca²⁺ → ACh → AP → contraction","Cross-bridge → AP → ACh → Ca²⁺"],"Complete signaling pathway.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Anatomy Unit 3: wrote {len(lessons)} lessons")
