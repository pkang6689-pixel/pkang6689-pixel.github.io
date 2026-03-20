#!/usr/bin/env python3
"""Anatomy Unit 1 – Foundations of Anatomy & Physiology (7 lessons)."""
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

# 1.1
k, v = build_lesson(1, 1, "Levels of Organization (Cells → Tissues → Organs → Systems)",
    "<h3>Levels of Structural Organization</h3>"
    "<p>The human body is organized from the smallest to largest levels:</p>"
    "<ul><li><b>Chemical level:</b> Atoms combine into molecules (e.g., H₂O, DNA).</li>"
    "<li><b>Cellular level:</b> Cells are the basic units of life (e.g., neurons, muscle cells).</li>"
    "<li><b>Tissue level:</b> Groups of similar cells (4 types: epithelial, connective, muscle, nervous).</li>"
    "<li><b>Organ level:</b> Two or more tissues form a functional unit (e.g., heart, liver).</li>"
    "<li><b>Organ system level:</b> Organs work together (11 major systems).</li>"
    "<li><b>Organismal level:</b> All systems cooperate to maintain life.</li></ul>",
    [
        ("Chemical Level", "Atoms and molecules; the simplest structural level of the body."),
        ("Cell", "The basic living unit of all organisms; performs all life functions."),
        ("Tissue", "A group of similar cells performing a common function (4 types)."),
        ("Organ", "A structure composed of two or more tissue types that performs a specific function."),
        ("Organ System", "A group of organs that work together to accomplish a common purpose (e.g., cardiovascular system)."),
    ],
    [
        ("The smallest living structural level of the body is the:", ["Tissue", "*Cell", "Organ", "Molecule"],
         "Cells are the basic living units; molecules are not alive."),
        ("How many major tissue types are there?", ["2", "3", "*4", "6"],
         "Epithelial, connective, muscle, and nervous."),
        ("An organ consists of:", ["One tissue type", "*Two or more tissue types", "Only cells", "Only molecules"],
         "By definition, an organ contains at least two tissue types."),
        ("Which sequence is correct from simplest to most complex?", ["Organ → Tissue → Cell → System", "*Cell → Tissue → Organ → Organ System → Organism", "Tissue → Cell → Organ → System", "Atom → Organ → Cell → Tissue"],
         "Standard hierarchy of organization."),
        ("The cardiovascular system includes the heart and:", ["Lungs only", "Kidneys", "*Blood vessels and blood", "Bones"],
         "Heart, blood vessels, and blood make up the cardiovascular system."),
        ("Which is at the chemical level?", ["Neuron", "Stomach", "Heart", "*Water molecule (H₂O)"],
         "Molecules like H₂O are at the chemical level."),
        ("How many organ systems are typically recognized?", ["8", "*11", "5", "15"],
         "11 major organ systems in the human body."),
        ("DNA is found at which level?", ["Tissue", "*Chemical (molecular)", "Organ", "System"],
         "DNA is a molecule."),
        ("Epithelial tissue is an example of which level?", ["Chemical", "Cellular", "*Tissue", "Organ"],
         "Epithelial is one of the four tissue types."),
        ("The stomach is an example of:", ["A cell", "A tissue", "*An organ", "An organ system"],
         "The stomach is composed of multiple tissue types performing digestion."),
        ("Which level describes the entire human body functioning together?", ["Organ system", "*Organismal", "Tissue", "Cellular"],
         "The organismal level is the highest."),
        ("Muscle cells grouped together form:", ["An organ", "*Muscle tissue", "A system", "A molecule"],
         "Similar cells grouped = tissue."),
        ("The digestive system is at the _____ level.", ["Organ", "*Organ system", "Tissue", "Chemical"],
         "A system consists of multiple organs working together."),
        ("Which tissue type transmits electrical signals?", ["Epithelial", "Connective", "*Nervous", "Muscle"],
         "Nervous tissue specializes in signal transmission."),
        ("Red blood cells belong to the _____ level.", ["Chemical", "*Cellular", "Tissue", "Organ"],
         "Individual cells, even in blood, are at the cellular level."),
        ("An atom of oxygen is at the:", ["*Chemical level", "Cellular level", "Tissue level", "Organ level"],
         "Atoms and molecules = chemical level."),
        ("Which is NOT one of the four tissue types?", ["Epithelial", "Connective", "Muscle", "*Skeletal"],
         "Skeletal is a type of muscle tissue, not a main category."),
        ("The liver is composed of:", ["Only one cell type", "*Multiple tissue types (epithelial, connective, etc.)", "Only connective tissue", "No tissues"],
         "As an organ, the liver has several tissue types."),
        ("Organ systems work together to maintain:", ["Only movement", "Only digestion", "*Homeostasis and life", "Only circulation"],
         "All systems cooperate for homeostasis."),
        ("Connective tissue includes:", ["Neurons", "Skin cells only", "*Bone, blood, cartilage, fat", "Muscle fibers only"],
         "Connective tissue is the most diverse: bone, blood, cartilage, adipose, etc."),
    ]
)
lessons[k] = v

# 1.2
k, v = build_lesson(1, 2, "Anatomical Terminology (Planes, Directions, Cavities)",
    "<h3>Anatomical Terminology</h3>"
    "<h4>Anatomical Position</h4>"
    "<p>Standing erect, feet forward, palms facing anteriorly. All directional terms reference this position.</p>"
    "<h4>Directional Terms</h4>"
    "<ul><li><b>Superior/Inferior:</b> Above/below.</li>"
    "<li><b>Anterior (ventral)/Posterior (dorsal):</b> Front/back.</li>"
    "<li><b>Medial/Lateral:</b> Toward/away from the midline.</li>"
    "<li><b>Proximal/Distal:</b> Closer/farther from the trunk (for limbs).</li>"
    "<li><b>Superficial/Deep:</b> Toward/away from the body surface.</li></ul>"
    "<h4>Body Planes</h4>"
    "<ul><li><b>Sagittal:</b> Divides left/right. Midsagittal = equal halves.</li>"
    "<li><b>Frontal (coronal):</b> Divides anterior/posterior.</li>"
    "<li><b>Transverse (horizontal):</b> Divides superior/inferior (cross-section).</li></ul>"
    "<h4>Body Cavities</h4>"
    "<p>Dorsal cavity (cranial + vertebral) and ventral cavity (thoracic + abdominopelvic).</p>",
    [
        ("Anatomical Position", "Standing erect, feet forward, arms at sides, palms facing anteriorly."),
        ("Sagittal Plane", "Divides the body into left and right portions; midsagittal = equal halves."),
        ("Frontal (Coronal) Plane", "Divides the body into anterior (front) and posterior (back) portions."),
        ("Transverse Plane", "Divides the body into superior (upper) and inferior (lower) portions."),
        ("Medial vs. Lateral", "Medial = toward the midline; lateral = away from the midline."),
    ],
    [
        ("In anatomical position, the palms face:", ["Posteriorly", "*Anteriorly", "Medially", "Inferiorly"],
         "Palms face forward (anteriorly) in anatomical position."),
        ("The sagittal plane divides the body into:", ["Front and back", "*Left and right", "Upper and lower", "Inside and outside"],
         "Sagittal = left/right division."),
        ("The frontal (coronal) plane divides:", ["Left and right", "*Anterior and posterior", "Upper and lower", "Medial and lateral"],
         "Front and back halves."),
        ("The transverse plane creates a:", ["Longitudinal section", "*Cross-section (upper/lower)", "Sagittal section", "Frontal section"],
         "Horizontal cut = cross-section."),
        ("The elbow is _____ to the wrist.", ["Distal", "*Proximal", "Inferior", "Lateral"],
         "The elbow is closer to the trunk."),
        ("The nose is _____ to the ears.", ["Lateral", "*Medial", "Distal", "Superior"],
         "The nose is nearer the midline."),
        ("The skin is _____ to the muscles.", ["Deep", "*Superficial", "Inferior", "Proximal"],
         "The skin is closer to the body surface."),
        ("Superior means:", ["Below", "In front", "*Above", "Behind"],
         "Superior = toward the head/above."),
        ("Anterior is the same as:", ["Dorsal", "*Ventral", "Superior", "Inferior"],
         "Anterior = ventral = front of the body."),
        ("The cranial cavity houses the:", ["Heart", "Lungs", "*Brain", "Stomach"],
         "The cranial cavity is the bony skull enclosing the brain."),
        ("The thoracic cavity contains:", ["Brain and spinal cord", "Stomach only", "*Heart and lungs", "Reproductive organs"],
         "Heart and lungs are in the thorax."),
        ("The abdominopelvic cavity is divided into:", ["*Abdominal and pelvic cavities", "Thoracic and pelvic cavities", "Cranial and vertebral cavities", "Dorsal and ventral cavities"],
         "The two sub-regions of the ventral cavity below the diaphragm."),
        ("The vertebral cavity protects the:", ["Brain", "*Spinal cord", "Heart", "Kidneys"],
         "Vertebral (spinal) cavity houses the spinal cord."),
        ("Dorsal cavity includes:", ["*Cranial and vertebral cavities", "Thoracic and abdominal cavities", "Pelvic only", "Abdominopelvic only"],
         "Dorsal = back = cranial + vertebral."),
        ("The knee is _____ to the hip.", ["Proximal", "Superior", "*Distal", "Medial"],
         "The knee is farther from the trunk along the limb."),
        ("A midsagittal plane divides the body into:", ["Unequal left and right", "*Equal left and right halves", "Front and back", "Top and bottom"],
         "Midsagittal = exactly at the midline."),
        ("The heart is _____ to the lungs.", ["Lateral", "*Medial", "Superior", "Inferior"],
         "The heart is between the lungs, closer to the midline."),
        ("Which cavity is separated from the abdominal cavity by the diaphragm?", ["Cranial", "Vertebral", "*Thoracic", "Pelvic"],
         "The diaphragm separates the thoracic and abdominal cavities."),
        ("Prone position means lying:", ["On the back", "*Face down", "On the side", "Standing"],
         "Prone = face down; supine = face up."),
        ("Why is standardized terminology important?", ["It's not important", "*It eliminates ambiguity in medical communication", "Only for textbooks", "Tradition only"],
         "Precise language prevents errors in healthcare."),
    ]
)
lessons[k] = v

# 1.3
k, v = build_lesson(1, 3, "Homeostasis & Feedback Mechanisms",
    "<h3>Homeostasis &amp; Feedback</h3>"
    "<p><b>Homeostasis:</b> The body's ability to maintain a relatively stable internal environment despite external changes.</p>"
    "<h4>Components of a Feedback Loop</h4>"
    "<ul><li><b>Receptor (sensor):</b> Detects a stimulus/change.</li>"
    "<li><b>Control center (integrator):</b> Processes the signal, determines the response (often the brain).</li>"
    "<li><b>Effector:</b> Carries out the response (muscles, glands).</li></ul>"
    "<h4>Types</h4>"
    "<ul><li><b>Negative feedback:</b> Reverses the change (most common). Example: thermoregulation.</li>"
    "<li><b>Positive feedback:</b> Amplifies the change until the process completes. Example: childbirth (oxytocin).</li></ul>",
    [
        ("Homeostasis", "Maintenance of a stable internal environment (temperature, pH, blood glucose, etc.)."),
        ("Negative Feedback", "A response that reverses (reduces) the initial stimulus; most common feedback type."),
        ("Positive Feedback", "A response that amplifies the stimulus until the process is complete."),
        ("Receptor", "The sensor that detects a change in the internal or external environment."),
        ("Effector", "The organ/tissue that carries out the corrective response (e.g., muscle, gland)."),
    ],
    [
        ("Homeostasis refers to:", ["Constant change", "*Maintenance of stable internal conditions", "Growth", "Disease"],
         "Stable internal environment despite external changes."),
        ("Most feedback loops in the body are:", ["Positive", "*Negative", "Neutral", "Absent"],
         "Negative feedback is the most common regulatory mechanism."),
        ("Negative feedback _____ the stimulus.", ["Amplifies", "*Reverses/reduces", "Ignores", "Doubles"],
         "It works to reverse the change."),
        ("Positive feedback _____ the stimulus.", ["*Amplifies until completion", "Reverses", "Eliminates", "Reduces slowly"],
         "Positive feedback enhances the change."),
        ("An example of negative feedback:", ["Blood clotting", "Childbirth", "*Body temperature regulation", "Labor contractions"],
         "When you get hot, you sweat to cool down (reverse)."),
        ("Blood clotting is an example of:", ["Negative feedback", "*Positive feedback", "No feedback", "Homeostasis failure"],
         "Each step amplifies clotting until the wound is sealed."),
        ("The receptor in a feedback loop:", ["Causes the response", "Processes the information", "*Detects the stimulus", "Is always in the brain"],
         "The receptor (sensor) detects changes."),
        ("The control center usually is the:", ["Muscle", "Gland", "*Brain or endocrine gland", "Skin"],
         "The brain or an endocrine gland processes information and sends commands."),
        ("The effector:", ["Detects the change", "Processes information", "*Carries out the response", "Creates the stimulus"],
         "Effectors (muscles, glands) execute the corrective action."),
        ("Normal body temperature is about:", ["40°C", "35°C", "*37°C (98.6°F)", "42°C"],
         "37°C is the homeostatic set point for temperature."),
        ("When body temp rises, sweat glands activate. The sweat gland is the:", ["Receptor", "Control center", "*Effector", "Stimulus"],
         "Sweat glands carry out the cooling response."),
        ("Blood glucose regulation involves:", ["Only the brain", "*Negative feedback loops involving insulin and glucagon", "Positive feedback only", "No feedback"],
         "Insulin lowers glucose; glucagon raises it — classic negative feedback."),
        ("Insulin is released when blood glucose is:", ["Low", "*High", "Normal", "Absent"],
         "High glucose triggers insulin release, which lowers glucose."),
        ("Glucagon is released when blood glucose is:", ["High", "*Low", "Normal", "Absent"],
         "Low glucose triggers glucagon, which raises glucose."),
        ("Oxytocin during labor is an example of:", ["Negative feedback", "*Positive feedback (contractions increase until birth)", "No feedback", "Homeostasis maintenance"],
         "Contractions release more oxytocin, which causes more contractions."),
        ("If homeostasis fails, the result can be:", ["Nothing", "Improved health", "*Disease or death", "Stronger feedback"],
         "Failure of homeostasis leads to pathology."),
        ("The set point is:", ["Always changing", "*The normal target value the body maintains (e.g., 37°C)", "Only for temperature", "Irrelevant"],
         "The set point is the ideal value the body regulates around."),
        ("Fever represents:", ["Homeostasis working perfectly", "*An adjusted set point (the body raises its thermostat)", "Positive feedback", "No regulation"],
         "During fever, the hypothalamus raises the temperature set point."),
        ("Which is NOT part of a feedback loop?", ["Receptor", "Effector", "Control center", "*Mitosis"],
         "Mitosis is cell division, not a feedback component."),
        ("Feedback loops are critical for _____ in all organ systems.", ["Growth only", "Movement only", "*Maintaining homeostasis", "Reproduction only"],
         "All organ systems use feedback to maintain stable conditions."),
    ]
)
lessons[k] = v

# 1.4
k, v = build_lesson(1, 4, "Basic Histology (Tissue Types)",
    "<h3>Basic Histology — The Four Tissue Types</h3>"
    "<h4>1. Epithelial Tissue</h4>"
    "<ul><li>Covers body surfaces, lines cavities, forms glands.</li>"
    "<li>Classified by layers (simple vs. stratified) and cell shape (squamous, cuboidal, columnar).</li></ul>"
    "<h4>2. Connective Tissue</h4>"
    "<ul><li>Supports, protects, binds. Contains cells in an extracellular matrix.</li>"
    "<li>Types: loose (areolar), dense (tendons), cartilage, bone, blood.</li></ul>"
    "<h4>3. Muscle Tissue</h4>"
    "<ul><li>Generates force. Three types: skeletal (voluntary, striated), cardiac (involuntary, striated), smooth (involuntary, nonstriated).</li></ul>"
    "<h4>4. Nervous Tissue</h4>"
    "<ul><li>Transmits electrical signals. Neurons + supporting neuroglia (glial cells).</li></ul>",
    [
        ("Epithelial Tissue", "Lines and covers surfaces; classified by cell shape and layer number."),
        ("Connective Tissue", "Supports and binds structures; most abundant and diverse tissue type."),
        ("Skeletal Muscle", "Voluntary, striated, attached to bones; responsible for movement."),
        ("Cardiac Muscle", "Involuntary, striated, found only in the heart; self-exciting."),
        ("Smooth Muscle", "Involuntary, nonstriated; found in walls of hollow organs."),
    ],
    [
        ("How many basic tissue types are there?", ["2", "3", "*4", "6"],
         "Epithelial, connective, muscle, nervous."),
        ("Epithelial tissue functions include:", ["Support only", "*Covering, lining, and secretion", "Movement", "Signal transmission"],
         "Epithelial = covering/lining + glands (secretion)."),
        ("Simple squamous epithelium is found in:", ["Skin surface", "*Alveoli of lungs and blood vessel linings", "Tendons", "Brain"],
         "Thin, flat cells allow gas exchange in alveoli."),
        ("The most abundant tissue type is:", ["Epithelial", "*Connective", "Muscle", "Nervous"],
         "Connective tissue is the most widespread and varied."),
        ("Blood is classified as:", ["Epithelial tissue", "*Connective tissue", "Muscle tissue", "Nervous tissue"],
         "Blood has cells in a liquid extracellular matrix (plasma)."),
        ("Tendons are made of:", ["Loose connective tissue", "*Dense regular connective tissue", "Cartilage", "Epithelial tissue"],
         "Parallel collagen fibers = dense regular CT."),
        ("Skeletal muscle is:", ["Involuntary", "*Voluntary and striated", "Smooth", "Cardiac"],
         "Skeletal muscle is under conscious control and has striations."),
        ("Cardiac muscle is found in the:", ["Intestines", "Biceps", "*Heart", "Blood vessels"],
         "Cardiac muscle is unique to the heart wall."),
        ("Smooth muscle is found in:", ["Skeleton", "*Walls of hollow organs (stomach, blood vessels, bladder)", "Heart only", "Brain"],
         "Smooth muscle lines visceral organs."),
        ("Nervous tissue is composed of:", ["Only neurons", "*Neurons and neuroglia (glial cells)", "Only glia", "Red blood cells"],
         "Both neurons (signal-carrying) and glia (support)."),
        ("Stratified squamous epithelium is found in:", ["Alveoli", "*Skin, mouth, esophagus (areas of friction)", "Bones", "Heart"],
         "Multiple layers protect against abrasion."),
        ("Cartilage is a type of:", ["Epithelial tissue", "*Connective tissue", "Muscle tissue", "Nervous tissue"],
         "Cartilage has cells in a firm matrix — connective tissue."),
        ("Bone (osseous tissue) is:", ["Epithelial", "*A connective tissue with a hard mineralized matrix", "Nervous", "Muscle"],
         "Bone has osteocytes in a calcified matrix."),
        ("What distinguishes connective tissue from others?", ["Cell shape", "*Abundant extracellular matrix between cells", "No blood supply", "No cells at all"],
         "CT is characterized by its matrix (ground substance + fibers)."),
        ("Striated means:", ["Smooth appearance", "*Having visible cross-stripes (bands of sarcomeres)", "No nuclei", "Multiple layers"],
         "Striations come from organized actin/myosin filaments."),
        ("Which muscle type has intercalated discs?", ["Skeletal", "Smooth", "*Cardiac", "All types"],
         "Intercalated discs are gap junctions unique to cardiac muscle."),
        ("Neuroglia function to:", ["Contract", "Secrete hormones", "*Support and protect neurons", "Digest food"],
         "Glial cells provide support, insulation, and nourishment to neurons."),
        ("Adipose tissue is classified as:", ["Epithelial", "*Connective tissue (fat)", "Muscle", "Nervous"],
         "Fat cells in a matrix = connective tissue."),
        ("Histology is the study of:", ["Organs", "Systems", "*Tissues (microscopic anatomy)", "Genes"],
         "Histo- = tissue; -logy = study of."),
        ("Glandular epithelium forms:", ["Bones", "Muscles", "*Glands (endocrine and exocrine)", "Neurons"],
         "Glands are specialized epithelial tissue."),
    ]
)
lessons[k] = v

# 1.5
k, v = build_lesson(1, 5, "Medical Imaging Techniques",
    "<h3>Medical Imaging Techniques</h3>"
    "<h4>X-Ray</h4>"
    "<p>Uses ionizing radiation. Best for bones and detecting fractures. Low cost, fast.</p>"
    "<h4>CT (Computed Tomography)</h4>"
    "<p>Multiple X-ray images processed by computer to create cross-sectional slices. Good for soft tissue and bone.</p>"
    "<h4>MRI (Magnetic Resonance Imaging)</h4>"
    "<p>Uses strong magnets and radio waves. Superior soft-tissue contrast. No ionizing radiation.</p>"
    "<h4>Ultrasound</h4>"
    "<p>Uses sound waves. No radiation. Common for fetal imaging, heart (echocardiogram), and abdominal organs.</p>"
    "<h4>PET (Positron Emission Tomography)</h4>"
    "<p>Uses radioactive tracers to detect metabolic activity. Used in cancer diagnosis and brain studies.</p>",
    [
        ("X-Ray", "Ionizing radiation technique; best for bone structures and fractures."),
        ("CT Scan", "Computed Tomography; multiple X-ray slices assembled into cross-sectional images."),
        ("MRI", "Magnetic Resonance Imaging; uses magnetic fields for excellent soft-tissue detail, no radiation."),
        ("Ultrasound", "Uses sound waves; safe (no radiation), commonly used for fetal imaging."),
        ("PET Scan", "Positron Emission Tomography; radioactive tracers reveal metabolic activity (cancer, brain)."),
    ],
    [
        ("X-rays are best for imaging:", ["Soft tissue", "*Bones and fractures", "Brain activity", "Blood flow"],
         "X-rays pass through soft tissue but are absorbed by dense bone."),
        ("CT scans produce:", ["Single images", "*Cross-sectional (slice) images", "Sound images", "Magnetic images"],
         "CT = computed tomography creates cross-sections."),
        ("MRI uses:", ["X-rays", "Radioactive tracers", "*Magnetic fields and radio waves", "Sound waves"],
         "MRI uses strong magnets — no ionizing radiation."),
        ("MRI is best for imaging:", ["Bones", "*Soft tissues (brain, joints, muscles)", "Only fractures", "Lungs"],
         "MRI provides superior soft-tissue contrast."),
        ("Ultrasound uses:", ["X-rays", "Magnets", "Radioactive tracers", "*High-frequency sound waves"],
         "Sound waves reflect off structures to form images."),
        ("Which imaging technique is safest during pregnancy?", ["X-ray", "CT", "PET", "*Ultrasound"],
         "Ultrasound uses no radiation — safe for fetal monitoring."),
        ("PET scans detect:", ["Bone density", "Fractures", "*Metabolic activity (using radioactive tracers)", "Sound echoes"],
         "PET uses radioactive glucose to find metabolically active areas."),
        ("CT scans use _____ to create images.", ["Magnets", "*X-rays (multiple angles processed by computer)", "Sound waves", "No energy"],
         "CT is based on X-ray technology."),
        ("Which technique involves no ionizing radiation?", ["X-ray", "CT", "*MRI", "PET"],
         "MRI uses magnets, not radiation."),
        ("Echocardiogram uses which technique?", ["X-ray", "MRI", "*Ultrasound", "PET"],
         "Echo = sound; an echocardiogram uses ultrasound to image the heart."),
        ("PET scans are especially useful for:", ["*Detecting cancer and studying brain function", "Viewing fractures", "Pregnancy monitoring", "Routine physicals"],
         "Cancer cells are metabolically active and take up more tracer."),
        ("The main disadvantage of X-rays is:", ["High cost", "*Exposure to ionizing radiation (small cancer risk)", "Takes too long", "Poor bone images"],
         "Ionizing radiation carries a small risk with repeated exposure."),
        ("CT scans provide more detail than standard X-rays because:", ["They use magnets", "*They combine many X-ray slices into 3D cross-sections", "They use sound", "They are cheaper"],
         "Computer processing of multiple angles gives far more detail."),
        ("MRI is contraindicated (shouldn't be used) in patients with:", ["Hearing aids", "*Certain metal implants (pacemakers, metal clips)", "Plastic casts", "Contact lenses"],
         "Strong magnets can move or heat metal implants."),
        ("Fluoroscopy is a type of:", ["*Real-time X-ray imaging (e.g., barium swallow)", "MRI", "Ultrasound", "PET"],
         "Fluoroscopy uses continuous X-rays to view motion."),
        ("Doppler ultrasound specifically measures:", ["Bone density", "Tissue composition", "*Blood flow velocity", "Brain activity"],
         "Doppler detects movement of blood cells."),
        ("A mammogram is a specialized:", ["MRI", "CT scan", "*X-ray of breast tissue", "PET scan"],
         "Mammography uses low-dose X-rays."),
        ("DEXA scan measures:", ["Brain function", "*Bone mineral density (osteoporosis screening)", "Heart function", "Liver size"],
         "Dual-energy X-ray absorptiometry assesses bone density."),
        ("Which imaging method is most expensive?", ["X-ray", "Ultrasound", "*MRI or PET", "All cost the same"],
         "MRI and PET are the most costly due to equipment."),
        ("Why is understanding imaging important for anatomy students?", ["It's not", "*It shows how anatomical knowledge guides clinical diagnosis", "Only for doctors", "Just for passing exams"],
         "Anatomical knowledge is essential for interpreting medical images."),
    ]
)
lessons[k] = v

# 1.6
k, v = build_lesson(1, 6, "Case Studies in Homeostasis",
    "<h3>Case Studies in Homeostasis</h3>"
    "<h4>Case 1 — Dehydration</h4>"
    "<p>A runner loses excessive water through sweat. Osmoreceptors detect increased blood osmolarity → hypothalamus signals ADH release → kidneys reabsorb more water → blood osmolarity returns to normal.</p>"
    "<h4>Case 2 — Diabetes (Type 1)</h4>"
    "<p>Autoimmune destruction of beta cells → no insulin → blood glucose stays elevated → homeostatic failure without treatment.</p>"
    "<h4>Case 3 — Heatstroke</h4>"
    "<p>Body's cooling mechanisms overwhelmed → core temp rises above 40°C → positive feedback cycle (enzyme dysfunction worsens temp control) → medical emergency.</p>",
    [
        ("Dehydration", "Excess water loss triggers ADH release, increasing kidney water reabsorption."),
        ("ADH (Antidiuretic Hormone)", "Released by posterior pituitary; causes kidneys to reabsorb water."),
        ("Type 1 Diabetes", "Autoimmune destruction of insulin-producing beta cells → chronic hyperglycemia."),
        ("Heatstroke", "Failure of thermoregulatory homeostasis; core temp > 40°C; medical emergency."),
        ("Homeostatic Imbalance", "When the body cannot maintain stable conditions; leads to disease or death."),
    ],
    [
        ("In the dehydration case, the receptor is:", ["Kidneys", "Sweat glands", "*Osmoreceptors (in hypothalamus)", "Skin"],
         "Osmoreceptors detect changes in blood concentration."),
        ("ADH acts on the:", ["Heart", "Liver", "*Kidneys (collecting ducts)", "Brain"],
         "ADH increases water reabsorption in the kidneys."),
        ("The dehydration response is an example of:", ["Positive feedback", "*Negative feedback", "No feedback", "Homeostatic failure"],
         "The response (water retention) reverses the stimulus (dehydration)."),
        ("In Type 1 diabetes, which cells are destroyed?", ["Alpha cells", "*Beta cells of the pancreas", "White blood cells", "Red blood cells"],
         "Autoimmune attack on insulin-producing beta cells."),
        ("Without insulin, blood glucose:", ["Drops", "Stays normal", "*Remains dangerously high (hyperglycemia)", "Disappears"],
         "Insulin is needed to transport glucose into cells."),
        ("Type 1 diabetes represents:", ["Working negative feedback", "*Failure of homeostasis (glucose regulation)", "Positive feedback", "Normal physiology"],
         "A broken feedback loop."),
        ("Heatstroke occurs when:", ["You exercise mildly", "*The body's cooling mechanisms are overwhelmed", "It's cold", "You drink too much water"],
         "The thermoregulatory system fails at extreme heat."),
        ("Heatstroke involves a dangerous _____ feedback loop.", ["Negative", "*Positive (breakdown accelerates the problem)", "Neutral", "No feedback"],
         "Rising temperature impairs enzymes → worsens temperature control."),
        ("Core body temperature in heatstroke exceeds:", ["35°C", "37°C", "*40°C (104°F)", "45°C"],
         "Above 40°C is the threshold for heatstroke."),
        ("ADH is released by the:", ["Kidneys", "Thyroid", "*Posterior pituitary gland (signaled by hypothalamus)", "Adrenal gland"],
         "The hypothalamus controls ADH release from the posterior pituitary."),
        ("A person in heatstroke needs:", ["Rest only", "More exercise", "*Immediate cooling and emergency medical treatment", "No intervention"],
         "Heatstroke is a medical emergency."),
        ("Which organ produces insulin?", ["Liver", "Kidney", "*Pancreas", "Brain"],
         "Beta cells of the pancreatic islets produce insulin."),
        ("Hypo- means:", ["High", "*Low/below normal", "Normal", "Absent"],
         "Hypothermia = low temperature, hypoglycemia = low glucose."),
        ("Hyper- means:", ["Low", "*High/above normal", "Normal", "Half"],
         "Hyperglycemia = high blood glucose."),
        ("Untreated Type 1 diabetes can lead to:", ["Perfect health", "*Diabetic ketoacidosis (DKA) — life-threatening", "Improved glucose control", "Weight gain only"],
         "Without insulin, the body uses fat for energy, producing ketone acids."),
        ("In a healthy person, after eating a sweet meal:", ["Blood glucose drops", "*Blood glucose rises → insulin released → glucose enters cells → levels return to normal", "Nothing happens", "Glucagon is released"],
         "Classic negative feedback cycle."),
        ("Blood loss triggers which homeostatic response?", ["Vasodilation", "*Vasoconstriction and increased heart rate to maintain blood pressure", "Sweating", "Insulin release"],
         "The cardiovascular system compensates to maintain BP."),
        ("Fever is:", ["Heatstroke", "*A regulated increase in the body's temperature set point", "Loss of homeostasis", "Positive feedback"],
         "The hypothalamus resets the thermostat higher during infection."),
        ("Clinical case studies help anatomy students by:", ["Adding difficulty", "*Connecting theoretical concepts to real patient scenarios", "Testing memorization only", "Being unnecessary"],
         "Application of knowledge to clinical situations deepens understanding."),
        ("The common theme in all homeostatic failures is:", ["Too much exercise", "*The feedback mechanism is disrupted, overwhelmed, or absent", "Aging", "Genetics only"],
         "Any breakdown in the receptor-CC-effector pathway can cause imbalance."),
    ]
)
lessons[k] = v

# 1.7
k, v = build_lesson(1, 7, "AP Prep: Anatomical Terminology",
    "<h3>AP Prep: Anatomical Terminology</h3>"
    "<p>This lesson reviews high-yield anatomical terms and concepts that frequently appear on standardized exams.</p>"
    "<h4>Key AP Review Points</h4>"
    "<ul><li>Know all directional terms relative to anatomical position.</li>"
    "<li>Identify body regions: cranial, cervical, thoracic, abdominal, pelvic, upper/lower extremities.</li>"
    "<li>Serous membranes: parietal (lines wall), visceral (covers organ). Examples: pleura, pericardium, peritoneum.</li>"
    "<li>Abdominopelvic quadrants: RUQ, LUQ, RLQ, LLQ.</li></ul>",
    [
        ("Parietal Membrane", "The layer of a serous membrane that lines the wall of a body cavity."),
        ("Visceral Membrane", "The layer that directly covers an organ (e.g., visceral pleura covers the lung)."),
        ("Pleura", "Serous membrane surrounding the lungs (visceral + parietal layers)."),
        ("Pericardium", "Serous membrane surrounding the heart."),
        ("Peritoneum", "Serous membrane lining the abdominopelvic cavity and covering abdominal organs."),
    ],
    [
        ("RUQ stands for:", ["Right Upper Quadricep", "*Right Upper Quadrant", "Right Under Quarter", "Right Upper Quarter"],
         "Abdominopelvic quadrant: right upper quadrant."),
        ("The liver is primarily in which quadrant?", ["LUQ", "RLQ", "*RUQ", "LLQ"],
         "The liver occupies most of the right upper quadrant."),
        ("The appendix is in the:", ["RUQ", "LUQ", "*RLQ", "LLQ"],
         "Right lower quadrant — appendicitis pain localizes here."),
        ("Serous membranes produce:", ["Blood", "Mucus", "*Serous fluid (reduces friction)", "Bile"],
         "Serous fluid lubricates organs to reduce friction during movement."),
        ("The visceral pericardium:", ["Lines the chest wall", "*Directly covers the heart surface", "Surrounds the lungs", "Lines the abdomen"],
         "Visceral = adhered to the organ itself."),
        ("The parietal pleura:", ["Covers the lung surface", "*Lines the wall of the thoracic cavity", "Covers the heart", "Lines the abdomen"],
         "Parietal = attached to the body wall."),
        ("The cervical region refers to the:", ["Chest", "Abdomen", "*Neck", "Head"],
         "Cervical = neck region."),
        ("The lumbar region is the:", ["Chest", "*Lower back", "Hip", "Upper back"],
         "Lumbar = lower back area."),
        ("The brachial region refers to the:", ["Forearm", "*Upper arm", "Hand", "Shoulder"],
         "Brachial = arm (between shoulder and elbow)."),
        ("The femoral region is the:", ["*Thigh", "Foot", "Knee", "Hip"],
         "Femoral = thigh region."),
        ("Ipsilateral means:", ["Opposite side", "*Same side of the body", "Above", "Below"],
         "Ipsi = same; lateral = side."),
        ("Contralateral means:", ["Same side", "*Opposite side of the body", "Behind", "In front"],
         "Contra = opposite; lateral = side."),
        ("A sagittal section through the eye would divide it into:", ["Top and bottom", "*Left and right portions", "Front and back", "Inside and outside"],
         "Sagittal = left/right."),
        ("The peritoneum covers:", ["Lungs", "Heart", "*Abdominal organs", "Brain"],
         "Peritoneum = serous membrane of the abdominopelvic cavity."),
        ("The patellar region is the:", ["*Knee (front)", "Ankle", "Elbow", "Hip"],
         "Patella = kneecap."),
        ("The plantar region is the:", ["Palm", "Back of hand", "Knee", "*Sole of the foot"],
         "Plantar surface = bottom of the foot."),
        ("The gluteal region is the:", ["Chest", "Thigh", "*Buttock", "Groin"],
         "Gluteal = buttock region."),
        ("On the AP exam, you may be shown an image and asked to identify:", ["Only bones", "*Directional relationships and body regions", "Only organs", "Microscope slides only"],
         "Directional term application is a high-yield AP topic."),
        ("The antecubital region is:", ["Behind the knee", "*In front of the elbow (where blood is drawn)", "The wrist", "The ankle"],
         "Antecubital fossa = front of elbow."),
        ("Knowing body regions and directional terms is essential because:", ["It's tradition", "*Precise communication is critical in healthcare and anatomy study", "It's not essential", "Only for surgeons"],
         "Accurate terminology prevents miscommunication in all medical settings."),
    ]
)
lessons[k] = v

# 1.8 (extra — the JSON has u1_l1.1 through u1_l1.7, so we have 7 lessons)

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Anatomy Unit 1: wrote {len(lessons)} lessons")
