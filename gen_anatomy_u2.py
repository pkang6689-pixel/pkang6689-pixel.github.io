#!/usr/bin/env python3
"""Anatomy Unit 2 – Skeletal System (8 lessons)."""
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

# 2.1
k,v = build_lesson(2,1,"Bone Structure & Function",
    "<h3>Bone Structure &amp; Function</h3>"
    "<h4>Functions of Bone</h4>"
    "<ul><li>Support, protection, movement (lever for muscles), mineral storage (Ca²⁺, PO₄³⁻), blood cell formation (hematopoiesis), energy storage (yellow marrow fat).</li></ul>"
    "<h4>Gross Anatomy of a Long Bone</h4>"
    "<ul><li><b>Diaphysis:</b> Shaft; compact bone surrounding the medullary cavity (yellow marrow).</li>"
    "<li><b>Epiphysis:</b> Ends; spongy (cancellous) bone covered by articular cartilage.</li>"
    "<li><b>Epiphyseal plate/line:</b> Growth plate (cartilage in children; ossified line in adults).</li>"
    "<li><b>Periosteum:</b> Outer fibrous membrane covering bone; rich in blood vessels and nerves.</li>"
    "<li><b>Endosteum:</b> Thin membrane lining the medullary cavity.</li></ul>",
    [("Diaphysis","The shaft of a long bone; composed of compact bone surrounding the medullary cavity."),
     ("Epiphysis","The end of a long bone; contains spongy bone and articular cartilage at the joint surface."),
     ("Periosteum","Dense fibrous membrane covering the outer surface of bone (except at joints)."),
     ("Hematopoiesis","The production of blood cells, occurring in red bone marrow."),
     ("Epiphyseal Plate","Growth plate made of cartilage; allows bones to lengthen during development.")],
    [("The shaft of a long bone is called the:",["Epiphysis","*Diaphysis","Periosteum","Endosteum"],"Diaphysis = shaft."),
     ("The ends of a long bone are called:",["Diaphysis","*Epiphyses","Periosteum","Medullary cavity"],"Epiphysis = bone end."),
     ("Red bone marrow is the site of:",["Fat storage","*Hematopoiesis (blood cell formation)","Mineral storage","Nerve transmission"],"Red marrow produces blood cells."),
     ("Yellow bone marrow stores:",["Blood cells","Minerals","*Fat (energy reserve)","Water"],"Yellow marrow = adipose tissue in the medullary cavity."),
     ("The periosteum covers:",["Joint surfaces","*Outer bone surface (except joints)","Inner marrow cavity","Cartilage only"],"Periosteum: outer membrane for bone nutrition and repair."),
     ("Articular cartilage covers the:",["Diaphysis","*Joint surface of the epiphysis","Periosteum","Growth plate"],"Reduces friction at joints."),
     ("Compact bone is found primarily in the:",["Epiphysis interior","*Diaphysis (shaft)","Growth plate","Marrow cavity"],"The shaft is dense compact bone."),
     ("Spongy (cancellous) bone is found in the:",["Shaft","*Interior of the epiphysis","Periosteum","Articular cartilage"],"Spongy bone = trabecular network inside the ends."),
     ("The epiphyseal plate is important for:",["Muscle attachment","Blood cell production","*Longitudinal bone growth","Nerve transmission"],"Cartilage growth plate → bone elongation."),
     ("In adults, the epiphyseal plate becomes the:",["Periosteum","*Epiphyseal line (ossified)","Endosteum","Diaphysis"],"Once growth stops, cartilage ossifies into a line."),
     ("Bones store which minerals?",["Sodium and potassium","*Calcium and phosphorus","Iron and zinc only","No minerals"],"Bone is the body's calcium and phosphate reservoir."),
     ("Bone serves as a lever for:",["Digestion","*Muscle-driven movement","Breathing only","Hormone release"],"Muscles pull on bones to produce movement."),
     ("The endosteum lines the:",["Outer bone surface","Joint surfaces","*Medullary (marrow) cavity","Epiphyseal plate"],"Endosteum: thin inner membrane."),
     ("How many bones does the adult skeleton have?",["150","*206","300","100"],"The standard adult count is 206 bones."),
     ("Hematopoiesis occurs in:",["Yellow marrow","Compact bone","*Red bone marrow","The periosteum"],"Red marrow in spongy bone produces blood cells."),
     ("The Haversian (osteon) system is a feature of:",["Spongy bone","*Compact bone","Cartilage","Marrow"],"Osteons are the structural unit of compact bone."),
     ("Osteocytes are:",["Bone-forming cells","Bone-destroying cells","*Mature bone cells trapped in lacunae","Blood cells"],"Osteocytes maintain bone tissue."),
     ("Osteoblasts:",["Destroy bone","*Build new bone (bone-forming cells)","Are mature bone cells","Produce blood cells"],"Blast = build."),
     ("Osteoclasts:",["Build bone","Store minerals","*Break down (resorb) bone tissue","Form blood cells"],"Clast = break."),
     ("Wolff's law states that bone:",["Never changes","*Remodels in response to the stresses placed on it","Only grows in childhood","Weakens with exercise"],"Mechanical stress stimulates bone strengthening.")]
)
lessons[k]=v

# 2.2
k,v = build_lesson(2,2,"Types of Bones (Long, Short, Flat, Irregular)",
    "<h3>Classification of Bones by Shape</h3>"
    "<ul><li><b>Long bones:</b> Longer than wide; shaft + two ends. Examples: femur, humerus, phalanges.</li>"
    "<li><b>Short bones:</b> Roughly cube-shaped. Examples: carpals (wrist), tarsals (ankle).</li>"
    "<li><b>Flat bones:</b> Thin, flattened, often curved. Examples: skull bones, sternum, scapula, ribs.</li>"
    "<li><b>Irregular bones:</b> Complex shapes. Examples: vertebrae, hip bones, some facial bones.</li>"
    "<li><b>Sesamoid bones:</b> Embedded in tendons. Example: patella (kneecap).</li></ul>",
    [("Long Bone","Longer than wide, with a shaft and two ends (e.g., femur, humerus)."),
     ("Short Bone","Cube-shaped; found in wrist (carpals) and ankle (tarsals)."),
     ("Flat Bone","Thin, flattened, often curved; provides protection and broad surfaces (e.g., skull, sternum)."),
     ("Irregular Bone","Complex, non-uniform shape (e.g., vertebrae, hip bones)."),
     ("Sesamoid Bone","Small bone embedded within a tendon; the patella is the largest example.")],
    [("The femur is classified as a:",["Short","Flat","*Long","Irregular"],"The femur (thighbone) is the longest bone."),
     ("Carpals of the wrist are:",["Long","*Short","Flat","Sesamoid"],"Small, roughly cube-shaped."),
     ("The sternum is a _____ bone.",["Long","Short","*Flat","Irregular"],"The breastbone is thin and flat."),
     ("Vertebrae are classified as:",["Long","Short","Flat","*Irregular"],"Complex shape with processes and foramina."),
     ("The patella is a _____ bone.",["Long","Flat","Irregular","*Sesamoid"],"Embedded in the quadriceps tendon."),
     ("Phalanges (finger/toe bones) are:",["Short","*Long (miniature long bones)","Flat","Irregular"],"Despite being small, phalanges have a shaft and two ends — long bone structure."),
     ("The scapula (shoulder blade) is a:",["Long","Short","*Flat","Sesamoid"],"Broad, flat, triangular bone."),
     ("Ribs are classified as:",["Long","Short","*Flat","Irregular"],"Curved, flat protective bones."),
     ("Tarsals of the ankle are:",["Long","*Short","Flat","Irregular"],"Cube-like bones of the ankle."),
     ("The hip bone (os coxae) is:",["Long","Short","Flat","*Irregular"],"Complex fused bone with multiple surfaces."),
     ("Which bone type is most important for hematopoiesis?",["Long (diaphysis)","Short","*Flat bones (e.g., sternum, hip) contain red marrow","Sesamoid"],"Flat bones have significant red marrow."),
     ("Sesamoid bones develop:",["In childhood only","In utero only","*Within tendons where there is friction/stress","In cartilage only"],"They protect tendons from wear."),
     ("The mandible (jawbone) is a(n):",["Flat","*Irregular","Long","Short"],"Complex shape with multiple projections."),
     ("Flat bones of the skull protect the:",["*Brain","Heart","Lungs","Spinal cord"],"The cranial vault shields the brain."),
     ("Long bones function primarily in:",["Protection","*Leverage and movement","Mineral storage only","Hearing"],"Limb bones provide leverage for muscles."),
     ("Wormian (sutural) bones are:",["Regular","*Small irregular bones found between skull sutures","Long bones","Part of the spine"],"Extra bone pieces at skull suture lines."),
     ("The clavicle (collarbone) is classified as:",["Flat","*Long (modified)","Short","Irregular"],"It has the structure of a long bone despite its shape."),
     ("The hyoid bone in the throat is:",["*Irregular (the only bone not articulating with another bone)","Long","Short","Flat"],"The hyoid is unique — it 'floats' in the neck."),
     ("Which classification has the most bones in the body?",["Short","Flat","*Irregular","Long"],"Many skull, facial, and vertebral bones are irregular."),
     ("Understanding bone types helps clinicians because:",["It doesn't","*Different bone types fracture differently and heal at different rates","Only for anatomy exams","Tradition"],"Clinical decisions depend on bone type.")]
)
lessons[k]=v

# 2.3
k,v = build_lesson(2,3,"Axial Skeleton",
    "<h3>The Axial Skeleton</h3>"
    "<p>The axial skeleton (80 bones) forms the central axis: skull, vertebral column, thoracic cage.</p>"
    "<h4>Skull (22 bones)</h4>"
    "<ul><li>Cranial bones (8): frontal, parietal (2), temporal (2), occipital, sphenoid, ethmoid.</li>"
    "<li>Facial bones (14): mandible, maxilla (2), zygomatic (2), nasal (2), lacrimal (2), palatine (2), inferior nasal conchae (2), vomer.</li></ul>"
    "<h4>Vertebral Column (26 bones)</h4>"
    "<ul><li>Cervical (7), Thoracic (12), Lumbar (5), Sacrum (1, fused 5), Coccyx (1, fused 3–5).</li></ul>"
    "<h4>Thoracic Cage</h4>"
    "<ul><li>Sternum (manubrium, body, xiphoid), 12 pairs of ribs: true (1–7), false (8–10), floating (11–12).</li></ul>",
    [("Axial Skeleton","80 bones forming the body's central axis: skull, vertebral column, bony thorax."),
     ("Cervical Vertebrae","7 neck vertebrae (C1–C7); C1 = atlas, C2 = axis."),
     ("Thoracic Vertebrae","12 vertebrae (T1–T12) articulating with ribs."),
     ("Lumbar Vertebrae","5 lower back vertebrae (L1–L5); largest and strongest."),
     ("True Ribs vs. False Ribs","True ribs (1–7) attach directly to the sternum; false ribs (8–12) do not attach directly.")],
    [("The axial skeleton has approximately _____ bones.",["126","206","*80","60"],"80 bones in skull + vertebral column + thorax."),
     ("How many cranial bones are there?",["6","14","*8","22"],"8 cranial bones form the braincase."),
     ("How many facial bones?",["8","*14","22","6"],"14 facial bones."),
     ("The mandible is the:",["Upper jaw","*Lower jaw (only movable skull bone)","Cheekbone","Nose bone"],"The mandible is the only freely movable skull bone."),
     ("How many cervical vertebrae?",["5","12","*7","4"],"Always 7 cervical vertebrae."),
     ("C1 is called the:",["Axis","*Atlas","Cervix","Sacrum"],"Atlas supports the skull (named for the Greek Titan)."),
     ("C2 is called the:",["Atlas","*Axis","Sacrum","Coccyx"],"The axis allows rotational movement of the head."),
     ("How many thoracic vertebrae?",["7","5","*12","10"],"12 thoracic, matching the 12 pairs of ribs."),
     ("How many lumbar vertebrae?",["7","12","*5","3"],"5 lumbar vertebrae bear the most weight."),
     ("The sacrum is formed by _____ fused vertebrae.",["3","*5","7","12"],"5 fused sacral vertebrae form the sacrum."),
     ("True ribs attach directly to the sternum via:",["Muscle","*Costal cartilage","Ligaments","Bone only"],"Hyaline costal cartilage connects true ribs to the sternum."),
     ("How many pairs of true ribs?",["5","12","*7","10"],"Ribs 1–7 are true ribs."),
     ("Floating ribs are pairs:",["1–7","8–10","*11–12","All 12"],"Ribs 11 and 12 have no anterior attachment."),
     ("The sternum consists of:",["One piece","*Three parts: manubrium, body, xiphoid process","Two parts","Four parts"],"Three fused sections."),
     ("The foramen magnum is in the:",["Frontal bone","Sphenoid","*Occipital bone","Temporal bone"],"Large opening in the occipital bone for the spinal cord."),
     ("The sphenoid bone resembles a:",["Square","*Butterfly/bat","Circle","Triangle"],"Butterfly-shaped bone in the cranial floor."),
     ("The intervertebral discs serve to:",["Hold vertebrae in place only","Prevent all movement","*Absorb shock and allow flexibility","Produce blood cells"],"Fibrocartilage discs cushion between vertebrae."),
     ("Normal spinal curves include:",["No curves","*Cervical lordosis, thoracic kyphosis, lumbar lordosis, sacral kyphosis","Only kyphosis","Only lordosis"],"Alternating curves increase resilience."),
     ("Scoliosis is:",["Normal curvature","*Abnormal lateral curvature of the spine","Forward curvature","Backward curvature"],"Side-to-side deviation."),
     ("The axial skeleton primarily functions in:",["Locomotion","*Protection of vital organs and support of the body axis","Mineral storage only","Movement of limbs"],"Skull protects brain, cage protects heart/lungs, spine protects spinal cord.")]
)
lessons[k]=v

# 2.4
k,v = build_lesson(2,4,"Appendicular Skeleton",
    "<h3>The Appendicular Skeleton</h3>"
    "<p>126 bones of the limbs and girdles that attach them to the axial skeleton.</p>"
    "<h4>Pectoral (Shoulder) Girdle</h4>"
    "<ul><li>Clavicle (collarbone) + scapula (shoulder blade) on each side.</li></ul>"
    "<h4>Upper Limb (30 bones each side)</h4>"
    "<ul><li>Humerus, radius, ulna, 8 carpals, 5 metacarpals, 14 phalanges.</li></ul>"
    "<h4>Pelvic Girdle</h4>"
    "<ul><li>Each hip bone (os coxae) = ilium + ischium + pubis (fused). Two hip bones + sacrum = pelvis.</li></ul>"
    "<h4>Lower Limb (30 bones each side)</h4>"
    "<ul><li>Femur, patella, tibia, fibula, 7 tarsals, 5 metatarsals, 14 phalanges.</li></ul>",
    [("Appendicular Skeleton","126 bones: limbs plus pectoral and pelvic girdles."),
     ("Pectoral Girdle","Clavicle + scapula; attaches upper limb to the axial skeleton."),
     ("Pelvic Girdle","Two hip bones (ilium, ischium, pubis each) + sacrum; attaches lower limb."),
     ("Humerus","The single bone of the upper arm."),
     ("Femur","The thighbone; the longest and strongest bone in the body.")],
    [("The appendicular skeleton has approximately:",["80","*126","206","50"],"126 bones in limbs and girdles."),
     ("The pectoral girdle consists of the:",["Hip bones","Sternum and ribs","*Clavicle and scapula","Vertebrae"],"Shoulder girdle = clavicle + scapula."),
     ("The clavicle is commonly called the:",["Shoulder blade","*Collarbone","Breastbone","Kneecap"],"Clavicle = collarbone."),
     ("The single upper arm bone is the:",["Radius","Ulna","*Humerus","Femur"],"Humerus = upper arm."),
     ("The forearm contains:",["One bone","*Two bones: radius and ulna","Three bones","No bones"],"Radius (lateral) and ulna (medial)."),
     ("How many carpal bones in each wrist?",["5","6","*8","10"],"8 small carpal bones arranged in two rows."),
     ("The longest bone in the body is the:",["Humerus","Tibia","*Femur","Fibula"],"The femur (thighbone) is the longest."),
     ("The patella is associated with the:",["Elbow","Wrist","*Knee","Ankle"],"Patella = kneecap."),
     ("Tibia is the:",["Smaller leg bone","*Larger, weight-bearing leg bone (shin)","Thighbone","Wrist bone"],"Tibia = shinbone, bears body weight."),
     ("The fibula is:",["The shinbone","*The thin, lateral bone of the lower leg (non-weight-bearing)","A forearm bone","A foot bone"],"Fibula = lateral, mainly for muscle attachment."),
     ("Each hip bone is formed by the fusion of:",["2 bones","*3 bones: ilium, ischium, pubis","4 bones","1 bone"],"Three fused bones."),
     ("The ilium is the:",["Lower hip bone","*Large, fan-shaped upper portion of the hip bone","Anterior portion","None of these"],"Ilium = the broad superior part you feel at your hip."),
     ("How many phalanges in each hand?",["10","*14","15","20"],"2 in the thumb + 3 in each of the other 4 fingers = 14."),
     ("How many tarsal bones in each foot?",["5","8","*7","14"],"7 tarsals including the calcaneus (heel) and talus."),
     ("The calcaneus is the:",["Kneecap","Ankle bone","*Heel bone","Toe bone"],"Largest tarsal bone."),
     ("The olecranon is part of the:",["Humerus","Radius","*Ulna (forms the elbow point)","Femur"],"The bony prominence of the elbow."),
     ("Female pelvis vs. male pelvis: the female pelvis is:",["Narrower","Taller","*Wider and shallower (adapted for childbirth)","Identical"],"The female pelvis has a broader inlet for childbirth."),
     ("The acetabulum is the:",["Shoulder socket","Knee joint","*Hip socket (where femur meets hip bone)","Elbow joint"],"Cup-shaped depression that receives the femoral head."),
     ("The radius is on the _____ side of the forearm.",["Medial (pinky side)","*Lateral (thumb side)","Superior","Inferior"],"Radius = lateral = thumb side."),
     ("The appendicular skeleton is primarily responsible for:",["Protecting the brain","*Movement and manipulation of the environment","Blood cell production only","Maintaining posture only"],"Limbs allow locomotion and interaction.")]
)
lessons[k]=v

# 2.5
k,v = build_lesson(2,5,"Joints & Movement",
    "<h3>Joints (Articulations) &amp; Movement</h3>"
    "<h4>Classification by Structure</h4>"
    "<ul><li><b>Fibrous:</b> No joint cavity; bones joined by fibers (e.g., skull sutures).</li>"
    "<li><b>Cartilaginous:</b> Bones joined by cartilage (e.g., intervertebral discs, pubic symphysis).</li>"
    "<li><b>Synovial:</b> Joint cavity with synovial fluid; most movable (e.g., knee, shoulder, hip).</li></ul>"
    "<h4>Types of Synovial Joints</h4>"
    "<ul><li>Plane (gliding), Hinge (elbow), Pivot (atlas/axis), Condyloid (wrist), Saddle (thumb), Ball-and-socket (hip, shoulder).</li></ul>"
    "<h4>Movements</h4>"
    "<p>Flexion/extension, abduction/adduction, rotation, circumduction, pronation/supination.</p>",
    [("Synovial Joint","Most movable joint type; contains a joint cavity filled with synovial fluid."),
     ("Flexion","Decreasing the angle between two body parts (e.g., bending the elbow)."),
     ("Extension","Increasing the angle between two body parts (e.g., straightening the elbow)."),
     ("Abduction/Adduction","Abduction = away from midline; adduction = toward midline."),
     ("Ball-and-Socket Joint","Allows the greatest range of motion (e.g., hip, shoulder).")],
    [("The most movable joint type is:",["Fibrous","Cartilaginous","*Synovial","Sutural"],"Synovial joints have the greatest freedom of movement."),
     ("Skull sutures are examples of _____ joints.",["Synovial","Cartilaginous","*Fibrous","Hinge"],"Bones connected by fibrous tissue, immovable."),
     ("Synovial joints contain:",["Bone only","Cartilage cement","*A joint cavity with synovial fluid","Fibrous connections"],"Synovial fluid lubricates the joint."),
     ("The elbow is a _____ joint.",["Pivot","*Hinge","Ball-and-socket","Gliding"],"Hinge: flexion/extension in one plane."),
     ("The shoulder is a _____ joint.",["Hinge","Pivot","*Ball-and-socket","Saddle"],"Ball-and-socket = greatest range of motion."),
     ("The hip is a _____ joint.",["Hinge","Pivot","*Ball-and-socket","Saddle"],"Femoral head fits into the acetabulum."),
     ("Flexion is:",["Straightening","*Bending (decreasing the angle)","Rotating","Moving away from midline"],"Flexion decreases the joint angle."),
     ("Extension is:",["Bending","*Straightening (increasing the angle)","Rotating","Moving toward midline"],"Extension increases the joint angle."),
     ("Abduction moves a limb:",["Toward the midline","*Away from the midline","Forward","Backward"],"Ab- = away from."),
     ("Adduction moves a limb:",["Away from the midline","*Toward the midline","Upward","Downward"],"Ad- = toward."),
     ("Rotation is:",["Bending","*Turning a bone around its own axis","Straightening","Gliding"],"Like turning your head left to right."),
     ("Pronation of the forearm turns the palm:",["Up (forward)","*Down (backward)","Sideways","Neither"],"Pronation = palm faces posterior/downward."),
     ("Supination of the forearm turns the palm:",["Down","*Up (forward/anteriorly)","Sideways","Neither"],"Supination = anatomical position (palm forward)."),
     ("The thumb joint (1st carpometacarpal) is a _____ joint.",["Hinge","Pivot","*Saddle","Ball-and-socket"],"Saddle joints allow opposition of the thumb."),
     ("The atlas-axis (C1-C2) joint is a:",["Hinge","Saddle","*Pivot","Ball-and-socket"],"Pivot joint allows head rotation (saying 'no')."),
     ("Circumduction is:",["Straight movement","*Cone-shaped movement combining flexion, extension, abduction, adduction","Only rotation","No movement"],"Drawing a circle with a limb."),
     ("Ligaments connect:",["Muscle to bone","*Bone to bone","Muscle to muscle","Nerve to muscle"],"Ligaments stabilize joints by connecting bones."),
     ("Tendons connect:",["Bone to bone","*Muscle to bone","Nerve to nerve","Bone to cartilage"],"Tendons transmit muscle force to bone."),
     ("Arthritis involves:",["Bone breaks","*Inflammation of joints","Nerve damage only","Muscle wasting only"],"Arthritis = joint inflammation."),
     ("A sprain involves damage to:",["Bone","Muscle","*Ligaments","Nerves only"],"A sprain is a stretched or torn ligament.")]
)
lessons[k]=v

# 2.6
k,v = build_lesson(2,6,"Bone Growth & Remodeling",
    "<h3>Bone Growth &amp; Remodeling</h3>"
    "<h4>Ossification</h4>"
    "<ul><li><b>Intramembranous:</b> Bone forms directly from mesenchyme (flat bones of skull).</li>"
    "<li><b>Endochondral:</b> Bone replaces a hyaline cartilage model (most bones).</li></ul>"
    "<h4>Long Bone Growth</h4>"
    "<ul><li>Length: Epiphyseal plate cartilage proliferates → ossifies progressively.</li>"
    "<li>Width: Appositional growth — osteoblasts add bone to the periosteal surface.</li></ul>"
    "<h4>Remodeling</h4>"
    "<p>Continuous process: osteoclasts resorb old bone, osteoblasts deposit new bone. Regulated by hormones (PTH, calcitonin) and mechanical stress (Wolff's law).</p>",
    [("Intramembranous Ossification","Bone forms directly from mesenchyme without a cartilage model (e.g., skull flat bones)."),
     ("Endochondral Ossification","Bone replaces a hyaline cartilage template; how most bones develop."),
     ("Appositional Growth","Bone grows in width by adding layers on the outer surface via osteoblasts."),
     ("PTH (Parathyroid Hormone)","Stimulates osteoclasts to resorb bone, raising blood calcium levels."),
     ("Calcitonin","Hormone from the thyroid that inhibits osteoclasts, lowering blood calcium.")],
    [("Endochondral ossification involves:",["Bone forming directly from membrane","*Bone replacing a cartilage model","Cartilage remaining permanently","No growth"],"Most bones form by replacing cartilage."),
     ("Intramembranous ossification forms:",["Long bones","*Most flat bones of the skull","Limb bones","Vertebrae"],"Skull bones form directly from mesenchyme."),
     ("Bones grow in length at the:",["Periosteum","Diaphysis","*Epiphyseal plate","Endosteum"],"Cartilage at the growth plate proliferates and ossifies."),
     ("Bones grow in width by:",["Epiphyseal plate growth","*Appositional growth (osteoblasts add bone at the periosteum)","Only in childhood","They don't grow in width"],"Periosteal surface addition."),
     ("Growth hormone (GH) stimulates:",["Bone resorption","*Bone growth during childhood and adolescence","Calcium deposition only","Nothing"],"GH promotes growth plate activity."),
     ("The epiphyseal plate closes:",["At birth","*At the end of puberty (growth stops)","At age 5","Never"],"Sex hormones cause final ossification of the plate."),
     ("PTH raises blood calcium by stimulating:",["Osteoblasts","*Osteoclasts (bone resorption)","Calcitonin","Cartilage growth"],"PTH → osteoclasts break down bone → Ca²⁺ enters blood."),
     ("Calcitonin:",["Raises blood calcium","*Lowers blood calcium (inhibits osteoclasts)","Promotes bone resorption","Has no effect on bone"],"Calcitonin opposes PTH."),
     ("Wolff's law states that:",["Bones weaken with stress","*Bones adapt and strengthen in response to mechanical stress","Bones never change","Bones grow only in childhood"],"Stress → bone remodeling to resist that stress."),
     ("Exercise _____ bone density.",["Decreases","Has no effect on","*Increases","Only affects muscle, not bone"],"Weight-bearing exercise stimulates bone deposition."),
     ("A fracture heals by:",["Cartilage only","No repair","*Formation of a callus (fibrocartilage → bony callus → remodeling)","Muscle filling the gap"],"Hematoma → fibrocartilage callus → bony callus → remodeling."),
     ("Vitamin D is essential for:",["Muscle growth only","*Calcium absorption from the intestines (critical for bone mineralization)","Iron absorption","Protein synthesis only"],"Without vitamin D, calcium can't be absorbed properly."),
     ("Rickets results from:",["Excess calcium","*Vitamin D deficiency in children (soft, deformed bones)","Too much exercise","Too much protein"],"Unmineralized bone → soft, bowed bones."),
     ("Osteoporosis is:",["*Loss of bone mass making bones fragile and prone to fracture","Excess bone growth","A joint disease","A muscle disorder"],"Common in postmenopausal women."),
     ("Estrogen helps maintain bone density by:",["Stimulating osteoclasts","*Inhibiting osteoclast activity (reducing resorption)","Increasing PTH","Having no effect"],"Post-menopause estrogen drops → accelerated bone loss."),
     ("Bone remodeling occurs:",["Only during childhood","Only after fractures","*Continuously throughout life","Only once per year"],"~5-10% of the skeleton is replaced annually."),
     ("An osteocyte begins as a(n):",["Osteoclast","Chondrocyte","*Osteoblast (that became trapped in its own matrix)","Fibroblast"],"Osteoblast → surrounded by matrix → osteocyte."),
     ("Which fracture type is most common in osteoporotic patients?",["Greenstick","*Compression fracture (vertebrae) and hip fracture","Spiral","Open"],"Weakened vertebrae and femoral neck are most vulnerable."),
     ("Teeth are NOT bones because they:",["Look different","*Are made of enamel, dentin, cementum (different composition and development)","Have no calcium","Are always the same size"],"Teeth have a different structure and developmental origin."),
     ("Understanding bone growth and remodeling is clinically important for treating:",["Heart disease","*Fractures, osteoporosis, growth disorders, and metabolic bone diseases","Vision problems","Neurological disorders only"],"Bone biology is central to orthopedic and endocrine medicine.")]
)
lessons[k]=v

# 2.7
k,v = build_lesson(2,7,"Disorders of the Skeletal System",
    "<h3>Disorders of the Skeletal System</h3>"
    "<h4>Common Conditions</h4>"
    "<ul><li><b>Osteoporosis:</b> Bone mass loss → fragile bones; common in postmenopausal women.</li>"
    "<li><b>Osteoarthritis (OA):</b> Wear-and-tear degeneration of articular cartilage.</li>"
    "<li><b>Rheumatoid Arthritis (RA):</b> Autoimmune destruction of joint synovial membranes.</li>"
    "<li><b>Fractures:</b> Complete/incomplete, open/closed, stress, pathological.</li>"
    "<li><b>Osteogenesis imperfecta:</b> Genetic disorder; brittle bones (collagen defect).</li>"
    "<li><b>Paget's disease:</b> Excessive/disorganized bone remodeling.</li></ul>",
    [("Osteoporosis","Progressive loss of bone density → increased fracture risk; most common metabolic bone disease."),
     ("Osteoarthritis","Degenerative joint disease from wear and tear on articular cartilage."),
     ("Rheumatoid Arthritis","Autoimmune disorder where the immune system attacks joint linings."),
     ("Osteogenesis Imperfecta","Genetic collagen disorder resulting in extremely brittle, easily fractured bones."),
     ("Compound (Open) Fracture","A fracture where bone pierces through the skin; high infection risk.")],
    [("Osteoporosis is characterized by:",["Excess bone","*Decreased bone density and increased fracture risk","Joint inflammation","Muscle weakness only"],"Bone resorption outpaces formation."),
     ("The population most at risk for osteoporosis:",["Young men","Children","*Postmenopausal women","Teenagers"],"Estrogen loss accelerates bone loss."),
     ("Osteoarthritis affects:",["Synovial membrane","Muscles","*Articular cartilage (wear and tear)","Tendons only"],"OA is cartilage degeneration."),
     ("Rheumatoid arthritis is:",["Mechanical wear","*An autoimmune disease attacking the synovial membrane","Caused by fractures","Only in the elderly"],"RA = autoimmune inflammatory disease."),
     ("A compound (open) fracture means:",["No skin break","*Bone has pierced through the skin","A hairline crack","An incomplete break"],"Open = bone exits through skin → infection risk."),
     ("A greenstick fracture is:",["Complete break","*An incomplete break (common in children — bone bends)","An open fracture","A spiral fracture"],"Children's flexible bones bend rather than snap completely."),
     ("A stress fracture results from:",["Sudden trauma","*Repetitive, low-impact forces (common in runners)","Disease","Aging"],"Overuse → tiny cracks."),
     ("A pathological fracture occurs in:",["Healthy bone","*Bone weakened by disease (e.g., cancer, osteoporosis)","Muscle","Cartilage"],"Minimal trauma fractures diseased bone."),
     ("Osteogenesis imperfecta is caused by:",["Vitamin D deficiency","Aging","*Genetic defect in collagen production","Infection"],"Faulty collagen → extremely brittle bones."),
     ("Paget's disease involves:",["No bone activity","*Excessive and disorganized bone remodeling","Only muscle weakness","Infection"],"Chaotic osteoclast/osteoblast activity → weak, deformed bone."),
     ("Rickets in children is caused by:",["*Vitamin D and/or calcium deficiency","Excess calcium","Autoimmune disease","Trauma"],"Soft, poorly mineralized bones."),
     ("DEXA scans are used to diagnose:",["Fractures","RA","*Osteoporosis (measures bone mineral density)","Muscle injuries"],"Gold standard for bone density measurement."),
     ("Treatment for osteoporosis may include:",["Only surgery","*Bisphosphonates, calcium/vitamin D, weight-bearing exercise","Antibiotics","Blood transfusions"],"Multiple approaches to slow bone loss and prevent fractures."),
     ("Gout is caused by:",["Bacterial infection","*Uric acid crystal deposits in joints","Trauma","Cartilage wear"],"Uric acid → inflammatory crystalline arthropathy."),
     ("A herniated disc involves:",["Bone fracture","*Nucleus pulposus protruding through the annulus fibrosus","Joint dislocation","Torn ligament"],"The inner gel of the intervertebral disc bulges out."),
     ("Scoliosis is:",["Normal curvature","*Abnormal lateral curvature of the spine","Excess kyphosis","Excess lordosis"],"Side-to-side spinal deviation."),
     ("Kyphosis is:",["*Excessive posterior thoracic curvature (hunchback)","Lateral curvature","Normal curvature","Excess lordosis"],"Exaggerated thoracic curve."),
     ("Lordosis is:",["Hunchback","*Excessive anterior lumbar curvature (swayback)","Lateral curvature","Normal posture"],"Exaggerated inward lumbar curve."),
     ("A dislocation occurs when:",["Bone breaks","*Bones in a joint are forced out of alignment","Cartilage wears away","Ligaments tighten"],"The articular surfaces separate."),
     ("Prevention of skeletal disorders includes:",["Avoiding all activity","*Regular exercise, adequate calcium/vitamin D, proper body mechanics","Only medications","Rest only"],"Lifestyle factors significantly reduce risk.")]
)
lessons[k]=v

# 2.8
k,v = build_lesson(2,8,"AP Prep: Bone Identification",
    "<h3>AP Prep: Bone Identification</h3>"
    "<p>Review of high-yield bones, landmarks, and markings frequently tested on AP and standardized exams.</p>"
    "<h4>Key Bone Landmarks (Markings)</h4>"
    "<ul><li><b>Foramen:</b> Opening for blood vessels or nerves (e.g., foramen magnum).</li>"
    "<li><b>Process:</b> Bony projection (e.g., spinous process of vertebrae).</li>"
    "<li><b>Fossa:</b> Depression (e.g., glenoid fossa of scapula).</li>"
    "<li><b>Condyle:</b> Rounded articular surface (e.g., femoral condyles).</li>"
    "<li><b>Tuberosity:</b> Roughened area for muscle/ligament attachment (e.g., tibial tuberosity).</li></ul>",
    [("Foramen","A hole or opening in bone for passage of blood vessels or nerves."),
     ("Process","A bony projection or prominence."),
     ("Fossa","A shallow depression in a bone surface."),
     ("Condyle","A large, rounded articular surface for joint formation."),
     ("Tuberosity","A rough, raised area on bone for muscle or ligament attachment.")],
    [("A foramen is:",["A bump","A depression","*An opening/hole in bone","A joint surface"],"Foramen = hole for nerves/vessels."),
     ("The foramen magnum is found in the:",["Frontal bone","Sphenoid","*Occipital bone","Temporal bone"],"Large opening at the base of the skull."),
     ("A fossa is:",["A projection","An opening","*A depression/cavity","A ridge"],"Fossa = depression (e.g., glenoid fossa)."),
     ("A condyle is a:",["Flat surface","Hole","*Rounded projection for joint articulation","Sharp ridge"],"Condyles form part of a joint surface."),
     ("The glenoid cavity is on the:",["Humerus","Hip bone","*Scapula (shoulder socket)","Femur"],"Shallow socket of the shoulder joint."),
     ("The olecranon process is on the:",["Radius","Humerus","*Ulna","Femur"],"Forms the point of the elbow."),
     ("The tibial tuberosity is:",["On the femur","*A roughened area on the anterior tibia (patellar tendon attaches here)","On the fibula","Inside the knee joint"],"Attachment point for the patellar ligament."),
     ("The greater trochanter is on the:",["Humerus","*Femur (lateral projection near the hip)","Tibia","Scapula"],"Large bony prominence felt at the hip."),
     ("The mastoid process is on the:",["Frontal bone","*Temporal bone (behind the ear)","Occipital bone","Mandible"],"Bump behind the ear — attachment for neck muscles."),
     ("The acromion is on the:",["Clavicle","*Scapula (point of the shoulder)","Humerus","Sternum"],"The bony projection at the top of the shoulder."),
     ("The zygomatic arch forms the:",["Forehead","Jaw","*Cheekbone","Nose bridge"],"Zygomatic = cheek prominence."),
     ("The mental foramen is on the:",["Maxilla","*Mandible (chin area)","Temporal bone","Frontal bone"],"Opening on the lower jaw for nerves/vessels."),
     ("The deltoid tuberosity is on the:",["Ulna","*Humerus (midshaft, lateral)","Femur","Tibia"],"Where the deltoid muscle attaches."),
     ("The xiphoid process is part of the:",["Vertebra","*Sternum (inferior tip)","Scapula","Clavicle"],"The small, cartilaginous inferior portion of the sternum."),
     ("Spinous processes are found on:",["The femur","*Vertebrae (posterior projections)","The skull","The ribs"],"You can palpate them along the midline of the back."),
     ("The medial malleolus is on the:",["Femur","Fibula","*Tibia (inner ankle bump)","Humerus"],"Bony prominence on the inner side of the ankle."),
     ("The lateral malleolus is on the:",["Tibia","*Fibula (outer ankle bump)","Femur","Patella"],"Bony prominence on the outer ankle."),
     ("The obturator foramen is in the:",["Skull","Vertebra","*Hip bone (os coxae)","Sternum"],"Large opening in the hip bone."),
     ("On the AP exam, you may be given a diagram and asked to identify:",["Only muscles","*Specific bones and their landmarks","Only organ systems","Only tissues"],"Bone identification is a classic AP anatomy topic."),
     ("The best way to study bone landmarks is:",["Reading only","*Hands-on work with bone models or specimens","Memorizing lists alone","Watching videos only"],"Tactile/visual learning is most effective for bone identification.")]
)
lessons[k]=v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Anatomy Unit 2: wrote {len(lessons)} lessons")
