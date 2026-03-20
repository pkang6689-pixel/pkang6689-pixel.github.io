#!/usr/bin/env python3
"""Anatomy Unit 4 – Nervous System (8 lessons)."""
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

# 4.1
k,v = build_lesson(4,1,"Neurons & Neuroglia",
    "<h3>Neurons &amp; Neuroglia</h3>"
    "<h4>Neuron Structure</h4>"
    "<ul><li><b>Cell body (soma):</b> Contains the nucleus; integrates incoming signals.</li>"
    "<li><b>Dendrites:</b> Short, branching extensions that receive signals.</li>"
    "<li><b>Axon:</b> Single long process that conducts impulses away from the cell body.</li>"
    "<li><b>Myelin sheath:</b> Insulating lipid layer (Schwann cells in PNS, oligodendrocytes in CNS); speeds conduction.</li>"
    "<li><b>Nodes of Ranvier:</b> Gaps in myelin where saltatory (jumping) conduction occurs.</li></ul>"
    "<h4>Neuroglia (Glial Cells)</h4>"
    "<ul><li><b>Astrocytes:</b> Support neurons, blood-brain barrier. <b>Oligodendrocytes:</b> CNS myelin. <b>Schwann cells:</b> PNS myelin.</li>"
    "<li><b>Microglia:</b> Immune defense in CNS. <b>Ependymal cells:</b> Line ventricles, produce CSF.</li></ul>",
    [("Neuron","Functional unit of the nervous system; transmits electrical signals."),
     ("Dendrite","Branching extension of a neuron that receives incoming signals."),
     ("Axon","Long projection that carries nerve impulses away from the cell body."),
     ("Myelin Sheath","Insulating lipid layer around axons that speeds signal conduction."),
     ("Astrocyte","Star-shaped glial cell; supports neurons, contributes to the blood-brain barrier.")],
    [("The functional unit of the nervous system is the:",["Glial cell","Synapse","*Neuron","Brain"],"Neurons transmit signals."),
     ("Dendrites function to:",["Send signals away from the cell body","*Receive incoming signals","Produce myelin","Store neurotransmitters"],"Dendrites = input receivers."),
     ("The axon conducts impulses:",["Toward the cell body","*Away from the cell body","In both directions","Nowhere"],"Axon = output pathway."),
     ("Myelin is produced by _____ in the PNS.",["Astrocytes","Oligodendrocytes","*Schwann cells","Microglia"],"Schwann cells myelinate PNS axons."),
     ("Myelin in the CNS is produced by:",["Schwann cells","*Oligodendrocytes","Astrocytes","Ependymal cells"],"Oligos = CNS myelin."),
     ("Nodes of Ranvier allow:",["Slow continuous conduction","*Saltatory (jumping) conduction, greatly increasing speed","Signal reversal","Myelin production"],"Impulse jumps node to node."),
     ("Astrocytes function to:",["Produce myelin","Destroy pathogens","*Support neurons and help form the blood-brain barrier","Line ventricles"],"Astrocytes = structural/metabolic support."),
     ("Microglia serve as:",["Structural support","*Immune cells of the CNS (phagocytic)","Myelin producers","Signal transmitters"],"Brain's resident immune defense."),
     ("Ependymal cells:",["Myelinate axons","*Line brain ventricles and produce cerebrospinal fluid (CSF)","Transmit signals","Destroy pathogens"],"Ciliated cells lining CSF-filled cavities."),
     ("The cell body (soma) contains:",["Only dendrites","Only the axon","*The nucleus and most organelles","Only myelin"],"Soma = metabolic center of the neuron."),
     ("Sensory (afferent) neurons:",["Send signals to muscles","*Carry impulses from receptors toward the CNS","Only exist in the brain","Produce hormones"],"Afferent = arriving to CNS."),
     ("Motor (efferent) neurons:",["Receive sensory information","*Carry impulses from the CNS to effectors (muscles/glands)","Only exist in the spinal cord","Have no axon"],"Efferent = exiting CNS."),
     ("Interneurons are found:",["Only in PNS","*Entirely within the CNS (connect sensory to motor)","In muscles","In skin"],"Interneurons integrate and relay signals."),
     ("The blood-brain barrier:",["Does not exist","*Protects the brain by restricting what passes from blood into brain tissue","Blocks all nutrients","Is made of bone"],"Tight junctions and astrocyte end-feet regulate transport."),
     ("White matter in the CNS appears white because of:",["Blood","Fat storage","*Myelinated axon fibers","Bone"],"Myelin's lipid content = white color."),
     ("Gray matter consists of:",["Myelinated axons only","*Cell bodies, dendrites, and unmyelinated structures","Only glial cells","Only blood vessels"],"Gray = soma-rich regions."),
     ("Multiple sclerosis (MS) involves:",["Destruction of neurons","*Demyelination in the CNS","Loss of glial cells only","Excess myelin"],"Autoimmune attack on myelin sheaths."),
     ("How many neurons are estimated in the human brain?",["1 million","100 million","*Approximately 86 billion","1 trillion"],"~86 billion neurons."),
     ("Glial cells outnumber neurons by:",["No difference","*Roughly equal or slightly more glial cells","10:1","100:1"],"Current estimates suggest roughly equal numbers."),
     ("Understanding neuron structure is essential for:",["Nothing","*Understanding neurological diseases, drug mechanisms, and brain function","Only anatomy class","Only surgery"],"Foundation for all neuroscience and neurology.")]
)
lessons[k]=v

# 4.2
k,v = build_lesson(4,2,"Action Potentials & Synaptic Transmission",
    "<h3>Action Potentials &amp; Synaptic Transmission</h3>"
    "<h4>Resting Membrane Potential</h4>"
    "<p>At rest: −70 mV (inside negative). Maintained by Na⁺/K⁺ ATPase pump (3 Na⁺ out, 2 K⁺ in).</p>"
    "<h4>Action Potential Phases</h4>"
    "<ul><li><b>Depolarization:</b> Na⁺ channels open → Na⁺ rushes in → membrane becomes positive (~+30 mV).</li>"
    "<li><b>Repolarization:</b> Na⁺ channels close, K⁺ channels open → K⁺ exits → membrane returns to negative.</li>"
    "<li><b>Hyperpolarization:</b> Brief overshoot below −70 mV before return to rest.</li></ul>"
    "<h4>Synaptic Transmission</h4>"
    "<p>AP reaches axon terminal → Ca²⁺ enters → vesicles release neurotransmitter → binds postsynaptic receptors → excitatory or inhibitory response.</p>",
    [("Resting Membrane Potential","~−70 mV; maintained by Na⁺/K⁺ pump and ion channel leaks."),
     ("Depolarization","Na⁺ channels open; Na⁺ influx makes the interior positive."),
     ("Repolarization","K⁺ channels open; K⁺ efflux restores negative interior."),
     ("Threshold","The membrane potential (~−55 mV) that must be reached to trigger an action potential."),
     ("Synapse","Junction between two neurons where neurotransmitters transmit the signal.")],
    [("The resting membrane potential is approximately:",["0 mV","*−70 mV","+30 mV","−120 mV"],"Inside of neuron is negative at rest."),
     ("The Na⁺/K⁺ pump moves:",["3 K⁺ out, 2 Na⁺ in","*3 Na⁺ out, 2 K⁺ in","Equal amounts","No ions"],"3 sodium out, 2 potassium in per cycle."),
     ("During depolarization:",["K⁺ channels open","*Na⁺ channels open → Na⁺ rushes into the cell","The cell becomes more negative","Nothing changes"],"Na⁺ influx makes interior positive."),
     ("The threshold potential is approximately:",["−70 mV","0 mV","*−55 mV","+30 mV"],"Must reach ~−55 mV to trigger an AP."),
     ("During repolarization:",["Na⁺ continues entering","*K⁺ channels open → K⁺ leaves the cell","Ca²⁺ enters","The cell stays positive"],"K⁺ efflux restores negative potential."),
     ("Action potentials follow the all-or-none principle, meaning:",["Partial APs are possible","*Either a full AP fires or none at all","All neurons fire simultaneously","There is no threshold"],"Once threshold is reached, full AP always occurs."),
     ("Saltatory conduction occurs in:",["Unmyelinated axons","*Myelinated axons (impulse jumps between nodes of Ranvier)","Dendrites only","Cell bodies"],"Myelin enables jumping conduction."),
     ("At the synapse, the neurotransmitter is released from:",["Dendrites","*The presynaptic axon terminal (vesicles)","The postsynaptic membrane","Glial cells"],"Vesicles fuse with presynaptic membrane."),
     ("Before neurotransmitter release, _____ ions enter the axon terminal.",["Na⁺","K⁺","*Ca²⁺","Cl⁻"],"Ca²⁺ influx triggers vesicle exocytosis."),
     ("An excitatory postsynaptic potential (EPSP):",["Hyperpolarizes the membrane","*Depolarizes the membrane (makes AP more likely)","Has no effect","Destroys the synapse"],"EPSP pushes toward threshold."),
     ("An inhibitory postsynaptic potential (IPSP):",["Depolarizes the membrane","*Hyperpolarizes the membrane (makes AP less likely)","Triggers an AP","Releases Ca²⁺"],"IPSP pushes away from threshold."),
     ("Neurotransmitter is removed from the synaptic cleft by:",["Leaving permanently","*Reuptake, enzymatic degradation, or diffusion","Nothing","Electrical current"],"Multiple mechanisms terminate the signal."),
     ("The refractory period:",["Allows continuous firing","*Prevents a new AP from occurring immediately (ensures one-way propagation)","Is very long","Does not exist"],"Ensures directionality and limits firing rate."),
     ("Conduction velocity increases with:",["Smaller axon diameter","*Larger axon diameter and myelination","No myelin","Fewer nodes"],"Larger and myelinated = faster."),
     ("Common neurotransmitters include:",["Only ACh","*ACh, norepinephrine, dopamine, serotonin, GABA, glutamate","Only dopamine","Only serotonin"],"Many different neurotransmitters exist."),
     ("GABA is the main _____ neurotransmitter in the brain.",["Excitatory","*Inhibitory","Modulatory","None"],"GABA inhibits postsynaptic neurons."),
     ("Glutamate is the main _____ neurotransmitter.",["Inhibitory","*Excitatory","Modulatory","None"],"Glutamate excites postsynaptic neurons."),
     ("Drugs that affect synaptic transmission include:",["None","Only illegal drugs","*Antidepressants, anesthetics, anti-anxiety meds, and many others","Only pain relievers"],"Many drugs target neurotransmitter systems."),
     ("The absolute refractory period means:",["The neuron can fire if stimulated strongly","*No new AP can be generated regardless of stimulus strength","The neuron is dead","Normal firing"],"Na⁺ channels are inactivated."),
     ("Understanding APs and synapses is crucial for:",["Only neuroscientists","*All medicine (anesthesia, psychiatry, neurology, pharmacology)","Only anatomy class","Nothing practical"],"Foundation of neuroscience and pharmacology.")]
)
lessons[k]=v

# 4.3
k,v = build_lesson(4,3,"Central Nervous System (Brain & Spinal Cord)",
    "<h3>Central Nervous System</h3>"
    "<h4>Brain Regions</h4>"
    "<ul><li><b>Cerebrum:</b> Largest part; cerebral cortex handles higher functions (thought, memory, language, motor control). Four lobes: frontal, parietal, temporal, occipital.</li>"
    "<li><b>Cerebellum:</b> Coordination, balance, fine motor skills.</li>"
    "<li><b>Brainstem:</b> Midbrain, pons, medulla oblongata — vital functions (breathing, heart rate, sleep/wake).</li>"
    "<li><b>Diencephalon:</b> Thalamus (relay center), hypothalamus (homeostasis, hormones).</li></ul>"
    "<h4>Spinal Cord</h4>"
    "<p>31 pairs of spinal nerves. Conducts signals between brain and body; integrates reflexes.</p>",
    [("Cerebrum","Largest brain region; cerebral cortex handles thought, language, motor, sensation."),
     ("Cerebellum","'Little brain' at the posterior; coordinates movement and balance."),
     ("Brainstem","Midbrain + pons + medulla oblongata; controls vital autonomic functions."),
     ("Thalamus","Relay center for sensory information heading to the cerebral cortex."),
     ("Hypothalamus","Controls homeostasis, body temperature, hunger, thirst, and the endocrine system.")],
    [("The largest part of the brain is the:",["Cerebellum","Brainstem","*Cerebrum","Hypothalamus"],"Cerebrum makes up ~80% of brain mass."),
     ("The frontal lobe is responsible for:",["Vision","Hearing","*Voluntary motor control, decision-making, personality","Balance"],"Frontal = executive functions and motor."),
     ("The occipital lobe processes:",["Hearing","Touch","*Vision","Language"],"Visual cortex is in the occipital lobe."),
     ("The temporal lobe processes:",["Vision","*Hearing and memory (includes auditory cortex and hippocampus)","Motor control","Balance"],"Temporal = auditory + memory areas."),
     ("The parietal lobe processes:",["Vision","Hearing","*Somatosensory information (touch, pain, temperature, proprioception)","Smell"],"Parietal = body sensation."),
     ("The cerebellum coordinates:",["Thinking","*Movement, balance, and posture","Vision","Digestion"],"Cerebellum fine-tunes motor output."),
     ("The medulla oblongata controls:",["Voluntary movement","Memory","*Vital functions (heart rate, breathing, blood pressure)","Vision"],"Damage to medulla = life-threatening."),
     ("The thalamus functions as:",["A hormone producer","*A relay center for sensory information (except smell)","A motor area","A memory center"],"All senses except olfaction relay through thalamus."),
     ("The hypothalamus regulates:",["Only movement","*Homeostasis: temperature, hunger, thirst, circadian rhythms, hormone control","Only vision","Only hearing"],"Master homeostatic regulator."),
     ("The spinal cord has _____ pairs of spinal nerves.",["12","*31","24","42"],"31 pairs: 8 cervical, 12 thoracic, 5 lumbar, 5 sacral, 1 coccygeal."),
     ("The meninges are:",["Brain cells","*Three protective membranes: dura mater, arachnoid mater, pia mater","Myelin layers","Bone"],"Meninges = CNS protective coverings."),
     ("Cerebrospinal fluid (CSF) functions to:",["Feed neurons","*Cushion and protect the brain and spinal cord","Conduct signals","Produce hormones"],"CSF acts as a shock absorber."),
     ("The corpus callosum connects:",["Brain and spinal cord","*Left and right cerebral hemispheres","Cerebrum and cerebellum","Thalamus and hypothalamus"],"Large fiber bundle for interhemispheric communication."),
     ("Broca's area (usually left frontal lobe) is involved in:",["*Speech production","Comprehension","Vision","Hearing"],"Damage → difficulty producing speech."),
     ("Wernicke's area (usually left temporal/parietal) is involved in:",["Speech production","*Language comprehension","Motor control","Balance"],"Damage → difficulty understanding language."),
     ("The blood-brain barrier protects the brain by:",["Blocking all substances","*Selectively allowing nutrients while blocking toxins and pathogens","Producing CSF","Being made of bone"],"Tight junctions restrict passage."),
     ("A stroke occurs when:",["The heart stops","*Blood flow to part of the brain is interrupted (ischemic) or a vessel ruptures (hemorrhagic)","A nerve is cut","Muscles fail"],"Brain tissue dies without blood supply."),
     ("The limbic system includes structures involved in:",["Motor control only","*Emotions and memory (amygdala, hippocampus, cingulate)","Vision","Hearing"],"Emotional and memory processing center."),
     ("The hippocampus is critical for:",["*Forming new memories","Motor coordination","Visual processing","Breathing"],"Hippocampal damage → inability to form new memories."),
     ("CNS damage is particularly serious because:",["It heals quickly","*CNS neurons have very limited regenerative capacity","It never matters","PNS is more important"],"CNS repair is minimal compared to PNS.")]
)
lessons[k]=v

# 4.4
k,v = build_lesson(4,4,"Peripheral Nervous System",
    "<h3>Peripheral Nervous System (PNS)</h3>"
    "<p>All neural tissue outside the brain and spinal cord.</p>"
    "<h4>Divisions</h4>"
    "<ul><li><b>Sensory (afferent):</b> Carries information from receptors TO the CNS.</li>"
    "<li><b>Motor (efferent):</b> Carries commands FROM the CNS to effectors.</li></ul>"
    "<h4>Motor Subdivision</h4>"
    "<ul><li><b>Somatic nervous system:</b> Voluntary control of skeletal muscles.</li>"
    "<li><b>Autonomic nervous system:</b> Involuntary control of smooth muscle, cardiac muscle, glands.</li></ul>"
    "<h4>Cranial Nerves</h4>"
    "<p>12 pairs of cranial nerves (I–XII) emerge from the brain. Important examples: vagus nerve (X) — extensive autonomic functions.</p>",
    [("PNS","Peripheral Nervous System; all nerves and ganglia outside the CNS."),
     ("Afferent (Sensory) Neurons","Carry signals from sensors/receptors TO the CNS."),
     ("Efferent (Motor) Neurons","Carry signals FROM the CNS to muscles and glands."),
     ("Somatic Nervous System","Voluntary motor control of skeletal muscles."),
     ("Cranial Nerves","12 pairs emerging from the brain; serve head, neck, and (vagus) thoracic/abdominal organs.")],
    [("The PNS includes:",["Brain and spinal cord","*All nerves and ganglia outside the CNS","Only spinal nerves","Only cranial nerves"],"PNS = everything except brain and spinal cord."),
     ("Afferent neurons carry signals:",["From CNS to muscles","*From receptors to the CNS","Within the CNS only","Nowhere"],"Afferent = arriving at CNS."),
     ("Efferent neurons carry signals:",["To the CNS","*From the CNS to effectors (muscles/glands)","Within PNS only","From brain to spinal cord"],"Efferent = exiting CNS."),
     ("The somatic nervous system controls:",["Involuntary functions","*Voluntary skeletal muscle movements","Heart rate","Digestion"],"Somatic = conscious, voluntary motor."),
     ("How many pairs of cranial nerves are there?",["10","*12","31","24"],"Cranial nerves I through XII."),
     ("The vagus nerve (CN X) is important because:",["It controls vision","*It has extensive parasympathetic functions (heart, lungs, GI tract)","It only serves the tongue","It's the smallest"],"The vagus is the most widespread cranial nerve."),
     ("The optic nerve (CN II) carries:",["Motor signals to the eye","*Visual sensory information from the retina to the brain","Sound information","Pain signals"],"CN II = vision."),
     ("Ganglia in the PNS are:",["Parts of the brain","*Clusters of neuron cell bodies outside the CNS","Myelin-producing cells","Types of neurotransmitters"],"Ganglia = PNS nerve cell body clusters."),
     ("A nerve is:",["A single neuron","*A bundle of axon fibers (fascicles) wrapped in connective tissue","A ganglion","A synapse"],"Nerves = bundles of axons."),
     ("The trigeminal nerve (CN V):",["Controls hearing","*Carries sensation from the face and motor to chewing muscles","Controls vision","Controls balance"],"Largest cranial nerve; face sensation + jaw muscles."),
     ("PNS nerves CAN regenerate because:",["They don't regenerate","*Schwann cells form a regeneration tube guiding axon regrowth","Oligodendrocytes help","Neurons divide"],"PNS regeneration is possible but slow (~1 mm/day)."),
     ("Sensory receptors include:",["Motor neurons","*Mechanoreceptors, thermoreceptors, nociceptors, photoreceptors, chemoreceptors","Only pain receptors","Only touch receptors"],"Many receptor types detect different stimuli."),
     ("Nociceptors detect:",["Light","Temperature","*Pain","Sound"],"Noci- = harmful (pain receptors)."),
     ("A dermatome is:",["A type of nerve","*An area of skin supplied by a single spinal nerve","A brain region","A muscle group"],"Used clinically to assess nerve function."),
     ("Bell's palsy involves:",["Blindness","*Paralysis of facial muscles (CN VII dysfunction)","Hearing loss","Loss of smell"],"Facial nerve dysfunction → one-sided facial paralysis."),
     ("Referred pain occurs when:",["Pain is imagined","*Visceral pain is perceived as coming from a somatic area (e.g., heart → left arm)","There is no pain","Pain is blocked"],"Shared nerve pathways confuse pain localization."),
     ("The brachial plexus serves the:",["Leg","*Upper limb (shoulder, arm, forearm, hand)","Trunk","Head"],"Nerve network for the upper extremity."),
     ("Sciatica involves:",["Arm pain","*Pain along the sciatic nerve (lower back, buttock, leg)","Headache","Stomach pain"],"Compression/irritation of the sciatic nerve."),
     ("Peripheral neuropathy:",["Only affects the CNS","*Damage to peripheral nerves causing numbness, tingling, or weakness","Is always genetic","Has no treatment"],"Common in diabetes."),
     ("Understanding the PNS is essential for:",["Nothing","*Diagnosing nerve injuries, planning surgeries, treating pain, and rehabilitation","Only anatomy exams","Only research"],"Clinical neurology depends on PNS knowledge.")]
)
lessons[k]=v

# 4.5
k,v = build_lesson(4,5,"Autonomic Nervous System",
    "<h3>Autonomic Nervous System (ANS)</h3>"
    "<p>Involuntary control of internal organs, smooth muscle, cardiac muscle, and glands.</p>"
    "<h4>Two Divisions</h4>"
    "<ul><li><b>Sympathetic ('fight or flight'):</b> Increases heart rate, dilates bronchioles, redirects blood to muscles, dilates pupils, inhibits digestion.</li>"
    "<li><b>Parasympathetic ('rest and digest'):</b> Decreases heart rate, constricts bronchioles, stimulates digestion, constricts pupils.</li></ul>"
    "<h4>Dual Innervation</h4>"
    "<p>Most organs receive both sympathetic and parasympathetic input, maintaining a dynamic balance.</p>",
    [("Sympathetic Division","'Fight or flight'; prepares body for stress — ↑HR, ↑BP, dilated pupils, inhibited digestion."),
     ("Parasympathetic Division","'Rest and digest'; promotes calm functions — ↓HR, stimulated digestion, constricted pupils."),
     ("Dual Innervation","Most organs receive both sympathetic and parasympathetic signals for balanced control."),
     ("Norepinephrine","Primary neurotransmitter of the sympathetic postganglionic neurons."),
     ("Acetylcholine","Neurotransmitter used by all preganglionic neurons and parasympathetic postganglionic neurons.")],
    [("The sympathetic division is often called:",["Rest and digest","*Fight or flight","Feed and breed","Freeze and forget"],"Prepares body for emergency."),
     ("The parasympathetic division is often called:",["Fight or flight","*Rest and digest","Run and recover","Stress response"],"Promotes calm, restorative functions."),
     ("Sympathetic activation _____ heart rate.",["Decreases","*Increases","Has no effect on","Stops"],"HR increases to pump more blood."),
     ("Parasympathetic activation _____ heart rate.",["Increases","*Decreases","Has no effect on","Stops"],"Vagus nerve slows the heart."),
     ("During sympathetic activation, digestion is:",["Stimulated","*Inhibited (blood is redirected to muscles)","Unchanged","Enhanced"],"Digestion is non-essential during fight-or-flight."),
     ("During parasympathetic activation, digestion is:",["Inhibited","*Stimulated","Stopped","Unchanged"],"Rest and digest = digestive activity increases."),
     ("Sympathetic stimulation causes pupil:",["Constriction","*Dilation (to let in more light)","No change","Closure"],"Dilated pupils see better in dim/threatening situations."),
     ("The primary sympathetic neurotransmitter (postganglionic) is:",["ACh","*Norepinephrine (noradrenaline)","Dopamine","Serotonin"],"NE acts on adrenergic receptors."),
     ("All preganglionic neurons (both divisions) release:",["Norepinephrine","*Acetylcholine","Dopamine","Epinephrine"],"ACh at all preganglionic synapses."),
     ("Parasympathetic postganglionic neurons release:",["Norepinephrine","*Acetylcholine","Epinephrine","Dopamine"],"ACh acts on muscarinic receptors."),
     ("Dual innervation means:",["Only one division controls each organ","*Most organs receive both sympathetic and parasympathetic input","Organs have no nerve supply","Only the brain is innervated"],"Dynamic balance between divisions."),
     ("The adrenal medulla releases:",["Only cortisol","*Epinephrine (adrenaline) and norepinephrine into the bloodstream","Only ACh","Only insulin"],"Sympathetic stimulation → adrenaline surge."),
     ("Bronchioles during sympathetic activation:",["Constrict","*Dilate (more airflow)","Close","Collapse"],"Open airways for maximum oxygen intake."),
     ("The vagus nerve is the primary nerve of the:",["Sympathetic division","*Parasympathetic division (supplies thoracic and abdominal organs)","Somatic division","None"],"CN X has extensive parasympathetic functions."),
     ("Sympathetic preganglionic neurons originate from:",["Brain only","*Thoracolumbar spinal cord (T1-L2)","Sacral spinal cord","Cervical cord"],"Thoracolumbar outflow."),
     ("Parasympathetic preganglionic neurons originate from:",["Thoracolumbar cord","*Brainstem and sacral spinal cord (S2-S4) — craniosacral outflow","Lumbar cord only","Cervical cord only"],"Craniosacral outflow."),
     ("Beta-blockers are drugs that:",["Stimulate sympathetic activity","*Block sympathetic beta receptors (lower heart rate and blood pressure)","Block parasympathetic activity","Have no cardiovascular effect"],"Common antihypertensive medication."),
     ("Atropine blocks:",["Sympathetic receptors","*Parasympathetic muscarinic receptors (increases HR, dilates pupils)","Beta receptors","No receptors"],"Anticholinergic drug."),
     ("The ANS maintains homeostasis by:",["Only stimulating","Only inhibiting","*Balancing sympathetic and parasympathetic activity","Having no effect"],"Dynamic push-pull balance."),
     ("Understanding the ANS is critical for:",["Nothing","*Pharmacology, anesthesia, cardiac care, and stress management","Only anatomy exams","Only surgeons"],"Many drugs target the ANS.")]
)
lessons[k]=v

# 4.6
k,v = build_lesson(4,6,"Reflex Arcs",
    "<h3>Reflex Arcs</h3>"
    "<p>A reflex is a rapid, involuntary, predictable response to a stimulus.</p>"
    "<h4>Components of a Reflex Arc (5 steps)</h4>"
    "<ul><li><b>1. Receptor:</b> Detects the stimulus.</li>"
    "<li><b>2. Sensory (afferent) neuron:</b> Transmits impulse to the CNS.</li>"
    "<li><b>3. Integration center:</b> CNS processes the information (may involve interneurons).</li>"
    "<li><b>4. Motor (efferent) neuron:</b> Carries the response command.</li>"
    "<li><b>5. Effector:</b> Muscle or gland that carries out the response.</li></ul>"
    "<h4>Examples</h4>"
    "<p><b>Patellar (knee-jerk) reflex:</b> Stretch receptor → sensory neuron → spinal cord → motor neuron → quadriceps contracts. This is a monosynaptic reflex (no interneuron).</p>",
    [("Reflex Arc","Neural pathway for a reflex: receptor → sensory neuron → CNS → motor neuron → effector."),
     ("Monosynaptic Reflex","Only one synapse (sensory → motor); e.g., patellar reflex."),
     ("Polysynaptic Reflex","Multiple synapses involving interneurons; e.g., withdrawal reflex."),
     ("Patellar Reflex","Knee-jerk reflex: tapping the patellar tendon stretches the quadriceps → leg kicks."),
     ("Withdrawal Reflex","Pulling hand away from a hot surface; polysynaptic, involves interneurons.")],
    [("A reflex is:",["A voluntary action","*A rapid, involuntary, predictable response to a stimulus","A learned behavior","A conscious decision"],"Reflexes are automatic."),
     ("The correct order of a reflex arc is:",["Motor → sensory → effector → receptor → CNS","*Receptor → sensory neuron → CNS → motor neuron → effector","Effector → CNS → receptor → motor → sensory","Random order"],"Standard 5-component pathway."),
     ("The receptor in a reflex arc:",["Carries out the response","*Detects the stimulus","Processes the information","Is always in the brain"],"Receptor = sensor."),
     ("The effector in a reflex arc:",["Detects the stimulus","*Carries out the response (muscle or gland)","Transmits the signal","Processes information"],"Effector = response executor."),
     ("The patellar reflex is monosynaptic because:",["It has many synapses","*There is only one synapse (sensory to motor, no interneuron)","It involves the brain","It is voluntary"],"Simplest reflex pathway."),
     ("In the withdrawal reflex (e.g., touching a hot stove):",["Only one synapse is involved","*Multiple synapses are involved (interneurons relay the signal)","The brain processes it first","No motor neuron is used"],"Polysynaptic reflex."),
     ("The integration center for most reflexes is in the:",["Brain only","Muscle","*Spinal cord (or brainstem)","Skin"],"Most reflexes are processed at the spinal level."),
     ("Reflexes are faster than voluntary responses because:",["They use bigger neurons","*They bypass the cerebral cortex (no conscious processing needed)","They use hormones","They don't exist"],"Direct spinal cord processing = fast."),
     ("The knee-jerk reflex tests:",["Brain function","*The integrity of the spinal cord and nerves at the L2-L4 level","Muscle strength only","Pain sensation"],"Clinically tests the femoral nerve/L2-L4 segments."),
     ("An absent patellar reflex may indicate:",["Normal function","*Nerve or spinal cord damage at L2-L4","Excess strength","No medical significance"],"Reflex testing diagnoses neural pathology."),
     ("A hyperactive (exaggerated) reflex may suggest:",["Normal function","*Upper motor neuron damage (loss of inhibitory brain control)","Peripheral nerve damage","Muscle weakness"],"Uninhibited spinal reflexes = upper motor neuron lesion."),
     ("The Babinski reflex (toe fanning up on sole stimulation) is:",["Always normal in adults","*Normal in infants but abnormal in adults (suggests corticospinal tract damage)","Never tested","Voluntary"],"Babinski in adults = concerning sign."),
     ("Crossed extensor reflex:",["Only flexes one leg","*Extends the opposite leg while the injured leg flexes (maintains balance)","Is voluntary","Doesn't exist"],"Stepping on a tack: lift injured foot, push down with the other."),
     ("Somatic reflexes involve:",["Smooth muscle","Glands","*Skeletal muscle","Cardiac muscle"],"Somatic = skeletal muscle responses."),
     ("Autonomic reflexes involve:",["Skeletal muscle only","*Smooth muscle, cardiac muscle, and glands","Only the brain","No muscles"],"Autonomic reflexes regulate internal organs."),
     ("An example of an autonomic reflex:",["Knee-jerk","*Baroreceptor reflex (blood pressure regulation)","Withdrawal reflex","Patellar reflex"],"Baroreceptors detect BP changes → autonomic adjustment."),
     ("Sensory neurons in a reflex arc are also called:",["Efferent","Motor","*Afferent","Interneurons"],"Afferent = sensory = toward CNS."),
     ("Motor neurons in a reflex arc are also called:",["Afferent","Sensory","*Efferent","Association neurons"],"Efferent = motor = away from CNS."),
     ("Reflexes are important for:",["Nothing","*Protecting the body from injury and maintaining homeostasis rapidly","Only neurological exams","Only anatomy class"],"Survival mechanism."),
     ("Testing reflexes is a critical part of:",["*A neurological examination to assess nervous system integrity","Only school labs","Only physical therapy","Nothing clinical"],"Reflex testing is routine in neurological assessment.")]
)
lessons[k]=v

# 4.7
k,v = build_lesson(4,7,"Disorders of the Nervous System",
    "<h3>Disorders of the Nervous System</h3>"
    "<ul><li><b>Alzheimer's disease:</b> Progressive memory loss and cognitive decline; amyloid plaques and neurofibrillary tangles.</li>"
    "<li><b>Parkinson's disease:</b> Loss of dopamine-producing neurons in substantia nigra → tremor, rigidity, bradykinesia.</li>"
    "<li><b>Epilepsy:</b> Abnormal, excessive electrical activity → seizures.</li>"
    "<li><b>Multiple sclerosis:</b> Autoimmune demyelination in the CNS.</li>"
    "<li><b>Stroke:</b> Ischemic (blockage) or hemorrhagic (bleed) → sudden neurological deficits.</li>"
    "<li><b>Meningitis:</b> Infection/inflammation of the meninges (bacterial or viral).</li></ul>",
    [("Alzheimer's Disease","Progressive neurodegenerative disorder; memory loss, amyloid plaques, neurofibrillary tangles."),
     ("Parkinson's Disease","Loss of dopaminergic neurons → tremor, rigidity, slow movement (bradykinesia)."),
     ("Epilepsy","Condition of recurrent seizures from abnormal brain electrical activity."),
     ("Stroke (CVA)","Cerebrovascular accident; ischemic (clot) or hemorrhagic (bleed) interrupting brain blood flow."),
     ("Meningitis","Inflammation of the meninges; can be caused by bacteria or viruses.")],
    [("Alzheimer's disease primarily affects:",["Movement","*Memory and cognitive function","Vision","Hearing"],"Progressive memory loss and dementia."),
     ("Hallmarks of Alzheimer's pathology include:",["Normal brain tissue","*Amyloid plaques and neurofibrillary tangles","Excess myelin","Too many neurons"],"Protein deposits damage neurons."),
     ("Parkinson's disease involves loss of:",["Serotonin neurons","*Dopamine-producing neurons in the substantia nigra","ACh neurons","GABA neurons"],"Dopamine deficiency → motor symptoms."),
     ("Cardinal symptoms of Parkinson's include:",["*Tremor, rigidity, bradykinesia (slow movement), postural instability","Blindness","Paralysis","Seizures"],"TRAP mnemonic."),
     ("Epilepsy is characterized by:",["Constant pain","*Recurrent seizures from abnormal electrical brain activity","Memory loss only","Paralysis"],"Seizure disorder."),
     ("An ischemic stroke is caused by:",["A bleed","*A blood clot blocking a cerebral artery","Trauma","Infection"],"~87% of strokes are ischemic."),
     ("A hemorrhagic stroke involves:",["A clot","*Rupture of a blood vessel in the brain","Infection","Dehydration"],"Bleeding into brain tissue."),
     ("Stroke symptoms include:",["No symptoms","*Sudden weakness, speech difficulty, facial drooping, confusion","Only headache","Only dizziness"],"FAST: Face, Arms, Speech, Time."),
     ("Multiple sclerosis involves:",["Muscle wasting","*Autoimmune destruction of CNS myelin","Bone loss","Liver disease"],"Demyelination slows or blocks nerve impulses."),
     ("Meningitis symptoms include:",["Joint pain only","*Severe headache, stiff neck, fever, photophobia","Muscle cramps only","Rash only"],"Classic meningitis triad."),
     ("Bacterial meningitis is a:",["Minor illness","*Medical emergency requiring immediate antibiotics","Chronic condition","Non-infectious disease"],"Can be fatal within hours without treatment."),
     ("A concussion is a:",["Fracture","*Mild traumatic brain injury (TBI)","Stroke","Seizure"],"Brain shaken within the skull."),
     ("Traumatic brain injury (TBI) can result from:",["*Falls, vehicle accidents, sports impacts, and violence","Infection only","Genetics only","Aging only"],"Physical trauma to the head."),
     ("Sciatica involves irritation of the:",["Cranial nerves","*Sciatic nerve (often from herniated disc)","Vagus nerve","Optic nerve"],"Lower back → buttock → leg pain."),
     ("Neuropathy in diabetes results from:",["*Chronic high blood sugar damaging peripheral nerves","Too much insulin","Low blood sugar","No connection"],"Diabetic neuropathy = common complication."),
     ("ALS (Lou Gehrig's disease) involves:",["Only sensory neurons","*Progressive degeneration of motor neurons","Only the brain","Only autonomic neurons"],"Motor neuron death → progressive paralysis."),
     ("Treatment for Parkinson's often includes:",["*Levodopa (L-DOPA) to increase dopamine levels","Surgery only","No treatment exists","Antibiotics"],"L-DOPA is converted to dopamine in the brain."),
     ("Neuroplasticity refers to:",["Brain rigidity","*The brain's ability to reorganize and form new neural connections","Brain atrophy","Nerve death"],"Basis for rehabilitation after brain injury."),
     ("Prevention of neurological disorders includes:",["Nothing can be done","*Protecting the head, managing cardiovascular risk factors, staying active, and early detection","Only genetics determine outcomes","Only medication"],"Lifestyle factors significantly affect neurological health."),
     ("Why is understanding neurological disorders important?",["It's not","*They are among the leading causes of disability worldwide","Only for neurologists","Only for research"],"Neurological conditions affect millions globally.")]
)
lessons[k]=v

# 4.8
k,v = build_lesson(4,8,"AP Prep: Neurophysiology",
    "<h3>AP Prep: Neurophysiology</h3>"
    "<h4>Key Topics for Exam</h4>"
    "<ul><li>Resting potential, action potential phases, ion channels.</li>"
    "<li>Synaptic transmission: neurotransmitter release, receptor binding, signal termination.</li>"
    "<li>Reflex arc components and clinical testing.</li>"
    "<li>ANS: sympathetic vs. parasympathetic effects on target organs.</li>"
    "<li>Brain regions and their functions.</li></ul>",
    [("Graded Potentials","Local, decremental signals (EPSPs/IPSPs) that can summate to reach threshold."),
     ("Summation","Temporal (rapid stimuli from one source) or spatial (simultaneous stimuli from multiple sources)."),
     ("Threshold","~−55 mV; the critical depolarization level that triggers a full action potential."),
     ("Absolute vs. Relative Refractory","Absolute: no AP possible. Relative: stronger-than-normal stimulus can trigger AP."),
     ("Neuroplasticity","The brain's ability to reorganize connections; basis of learning, memory, and recovery.")],
    [("Graded potentials are:",["All-or-none like APs","*Local, decremental potentials that can be excitatory or inhibitory","Only inhibitory","Found only in muscle"],"EPSPs and IPSPs are graded."),
     ("Temporal summation occurs when:",["Many neurons fire at once","*One neuron fires rapidly, signals overlap","No signals arrive","Muscles contract"],"Rapid successive stimuli from the same source."),
     ("Spatial summation occurs when:",["One neuron fires repeatedly","*Multiple neurons stimulate the same postsynaptic cell simultaneously","Muscles contract","No stimuli arrive"],"Convergence of signals from different sources."),
     ("An EPSP _____ the chance of an AP.",["Decreases","*Increases (depolarizes toward threshold)","Eliminates","Has no effect on"],"Excitatory = moves toward threshold."),
     ("An IPSP _____ the chance of an AP.",["Increases","*Decreases (hyperpolarizes away from threshold)","Eliminates","Has no effect on"],"Inhibitory = moves away from threshold."),
     ("During the absolute refractory period:",["A normal stimulus triggers an AP","*No AP can be generated, regardless of stimulus strength","The neuron is at rest","The neuron is dead"],"Na⁺ channels are inactivated."),
     ("The relative refractory period:",["No AP is possible","*A stronger-than-normal stimulus can trigger an AP","Is the same as the absolute","Does not exist"],"Some Na⁺ channels have recovered."),
     ("Sympathetic stimulation of the heart:",["Decreases HR","*Increases heart rate and contractility","Has no effect","Stops the heart"],"β₁ receptors → ↑HR, ↑force."),
     ("Parasympathetic stimulation of the GI tract:",["Inhibits motility","*Increases motility and secretion (digestion)","Has no effect","Causes pain"],"Rest and digest."),
     ("The neurotransmitter for the somatic NMJ is always:",["Norepinephrine","*Acetylcholine","Dopamine","Serotonin"],"ACh at all skeletal NMJs."),
     ("Serotonin is involved in regulating:",["Only motor function","*Mood, sleep, appetite, and pain","Only digestion","Only vision"],"Low serotonin linked to depression."),
     ("Dopamine pathways are involved in:",["Only Parkinson's","*Reward, motivation, motor control, and addiction","Only sleep","Only vision"],"Multiple brain functions."),
     ("The hypothalamus connects the nervous and endocrine systems by:",["Having no connection","*Controlling the pituitary gland (the 'master' endocrine gland)","Being a muscle","Producing CSF"],"Hypothalamus-pituitary axis."),
     ("A nerve impulse travels fastest in:",["Small, unmyelinated fibers","*Large, myelinated fibers","Dendrites","Cell bodies"],"Diameter and myelin both increase speed."),
     ("In clinical practice, EEG measures:",["Heart activity","*Brain electrical activity (useful for diagnosing epilepsy, sleep disorders)","Muscle activity","Nerve speed"],"Electroencephalogram."),
     ("Nerve conduction studies test:",["Brain waves","*The speed and strength of electrical signals in peripheral nerves","Heart rhythm","Muscle size"],"Useful for diagnosing neuropathy."),
     ("A key concept for the AP exam: the Na⁺/K⁺ pump is:",["Passive transport","*Active transport (uses ATP to maintain the resting potential)","Channel-mediated","Not energy-requiring"],"3 Na⁺ out, 2 K⁺ in — requires ATP."),
     ("The direction of an AP along an axon is determined by:",["Random chance","*The refractory period (prevents backward propagation)","The myelin sheath direction","Gravity"],"Refractory zones ensure one-way travel."),
     ("If all Na⁺ channels were blocked:",["Normal function","*No action potentials could be generated (nerve block)","Faster conduction","Stronger signals"],"Local anesthetics block Na⁺ channels."),
     ("Neurophysiology connects to all body systems because:",["It doesn't","*The nervous system controls and coordinates virtually every body function","Only muscles matter","Only hormones matter"],"The nervous system is the master coordinator.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Anatomy Unit 4: wrote {len(lessons)} lessons")
