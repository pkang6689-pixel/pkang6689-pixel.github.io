import json, os, glob

base = 'content_data/AnatomyLessons'

replacements = {
    # Lesson3.5
    ("Unit3/Lesson3.5_Quiz.json", 1): {
        "Knee extension": "Knee extension and straightening of the lower leg",
        "Elbow flexion": "Elbow flexion and curling of the forearm upward",
        "Trunk flexion": "Trunk flexion and forward bending of the torso",
    },
    ("Unit3/Lesson3.5_Quiz.json", 4): {
        "Three": "Three (rectus femoris, vastus lateralis, and vastus medialis)",
        "Five": "Five (the four vastus muscles plus the sartorius as a fifth member)",
        "Two": "Two (the rectus femoris and a single combined vastus muscle)",
    },
    ("Unit3/Lesson3.5_Quiz.json", 8): {
        "Dorsiflexion of the ankle": "Dorsiflexion of the ankle (pulling toes upward toward the shin)",
        "Hip abduction": "Hip abduction (moving the thigh laterally away from midline)",
        "Knee extension": "Knee extension (straightening the lower leg at the knee joint)",
    },
    ("Unit3/Lesson3.5_Quiz.json", 19): {
        "An abdominal muscle that compresses the organs": "An abdominal wall muscle that compresses the internal organs, assists in forced expiration, and helps stabilize the trunk during lifting",
        "A muscle of the lower back that extends the spine": "A deep muscle of the lower back that extends and laterally flexes the vertebral column, running alongside the spinous processes from the sacrum upward",
        "A muscle of the shoulder that abducts the arm": "A triangular muscle of the shoulder that abducts the arm, originating from the clavicle and scapular spine and inserting on the deltoid tuberosity",
    },
    ("Unit3/Lesson3.5_Quiz.json", 26): {
        "Hip abduction during lateral movement": "The forceful hip abduction during lateral movement placed excessive stress on the gluteal muscles and tensor fasciae latae",
        "Knee extension during the push-off phase": "Overloading of the quadriceps during explosive knee extension in the push-off phase exceeded the tendon's tensile strength",
        "Ankle plantar flexion during toe-off": "Extreme ankle plantar flexion during the toe-off phase overstressed the gastrocnemius and soleus muscles of the posterior calf",
    },
    # Lesson3.6
    ("Unit3/Lesson3.6_Quiz.json", 4): {
        "A bone fracture": "A crack or break in the periosteum and bone matrix",
        "A ligament tear": "An overstretched or torn ligament connecting bones",
        "A joint dislocation": "A displacement of bones from their normal joint alignment",
    },
    ("Unit3/Lesson3.6_Quiz.json", 14): {
        "A fracture that damages the bone marrow compartment": "A fracture that damages the bone marrow compartment, releasing fat globules into the bloodstream that can cause a systemic fat embolism",
        "An infection within a joint space": "An infection within the joint space that spreads to surrounding tissues, causing inflammation and eventual destruction of the articular cartilage",
        "A benign condition that resolves without treatment": "A benign and self-limiting condition of mild muscle swelling that resolves spontaneously without any medical or surgical intervention needed",
    },
    ("Unit3/Lesson3.6_Quiz.json", 25): {
        "Fibromyalgia triggered by the injury": "Fibromyalgia triggered by the traumatic injury; the widespread muscle pain and tenderness are characteristic of this chronic pain condition and should be managed with analgesics and physical therapy",
        "Normal post-fracture swelling that requires only ice and elevation": "Normal post-fracture swelling that requires only ice and elevation; the pain and tightness are expected after a tibia fracture and will resolve with standard conservative management over several days",
        "A simple blood clot that can be treated with medication alone": "A deep venous thrombosis forming at the fracture site that is compressing the surrounding tissues; this can be treated with anticoagulant medication alone without any surgical intervention required",
    },
    ("Unit3/Lesson3.6_Quiz.json", 27): {
        "MS is actually a muscle disease that has been misclassified": "MS is actually a primary muscle disease that has been historically misclassified as a neurological condition; the muscle fibers themselves undergo autoimmune destruction, leading to progressive loss of contractile tissue",
        "MS directly destroys the muscle fibers themselves": "MS directly destroys the skeletal muscle fibers through an autoimmune attack on the sarcolemma, causing progressive loss of contractile protein and eventual dissolution of the affected myofibrils",
        "MS causes bones to weaken, which makes muscles appear weak": "MS causes demineralization and weakening of the bones that serve as muscle attachment sites, reducing the mechanical leverage available to muscles and making them appear functionally weak",
    },
    # Lesson3.7
    ("Unit3/Lesson3.7_Quiz.json", 5): {
        "Walking and light jogging only": "Walking, light jogging, and other low-impact linear movements",
        "Archery and golf": "Archery, golf, and other precision-based non-contact sports",
        "Swimming and cycling": "Swimming, cycling, and other non-weight-bearing endurance sports",
    },
    ("Unit3/Lesson3.7_Quiz.json", 6): {
        "Abduct the shoulder": "Abduct the shoulder (lift the arm away from the body)",
        "Extend the hip": "Extend the hip (swing the thigh posteriorly behind you)",
        "Flex the knee": "Flex the knee (bend the lower leg at the knee joint)",
    },
    ("Unit3/Lesson3.7_Quiz.json", 7): {
        "Muscle strains in the back": "Muscle strains and overuse injuries in the lower back from heavy lifting",
        "A single isolated concussion": "A single isolated concussion from one traumatic head impact event",
        "Knee injuries from running": "Knee injuries from repetitive running on hard surfaces over many years",
    },
    ("Unit3/Lesson3.7_Quiz.json", 8): {
        "Nothing; X-ray is always superior": "Nothing; X-ray is always superior for all tissue types including soft structures",
        "Only brain injuries": "Only brain injuries, and not for any other soft tissue structures in the body",
        "Bone fractures only": "Bone fractures only, as MRI cannot generate images of non-bony structures",
    },
    ("Unit3/Lesson3.7_Quiz.json", 9): {
        "A torn rotator cuff muscle": "A torn rotator cuff muscle in the shoulder from repetitive overhead movements",
        "Inflammation of the medial knee ligaments": "Inflammation of the medial collateral knee ligaments caused by repetitive lateral pivoting motions",
        "A fracture of the humerus": "A stress fracture of the humerus shaft caused by repetitive throwing or swinging",
    },
    ("Unit3/Lesson3.7_Quiz.json", 14): {
        "A fracture of the shin bone": "A complete fracture of the tibial shaft from a single traumatic impact rather than from repetitive stress",
        "A condition that only affects the forearm": "A condition affecting only the forearm extensor muscles and tendons, causing pain along the lateral radius",
        "A ligament tear in the ankle joint": "A ligament tear in the ankle joint, specifically the anterior talofibular ligament, caused by an inversion sprain",
    },
    ("Unit3/Lesson3.7_Quiz.json", 15): {
        "Only the study of muscles without any clinical application": "A narrow field focused solely on skeletal muscle anatomy without any clinical application, limited entirely to basic science laboratory research and textbook descriptions",
        "Only surgical treatment of sports injuries": "A surgical specialty that focuses exclusively on operating on sports injuries, without any involvement in prevention, rehabilitation, nutrition, or non-surgical treatment strategies",
        "Exclusively the treatment of professional athletes": "A field exclusively dedicated to the treatment and performance enhancement of professional athletes, with no relevance to recreational exercisers or the general population",
    },
    ("Unit3/Lesson3.7_Quiz.json", 16): {
        "Concussion severity": "Concussion severity, by measuring pupil dilation and reaction time after a head impact",
        "ACL tears in the knee": "ACL tears in the knee, by pulling the tibia forward and assessing anterior translation",
        "Rotator cuff tears in the shoulder": "Rotator cuff tears in the shoulder, by resisting arm abduction and checking for weakness or pain",
    },
    ("Unit3/Lesson3.7_Quiz.json", 20): {
        "The study of nutrition for athletes": "The study of nutrition for athletes, including macronutrient ratios, hydration strategies, and dietary supplementation protocols for peak performance",
        "The study of muscle cell biology only": "The study of muscle cell biology only, focusing on the molecular structure of sarcomeres, myofilaments, and the biochemistry of contraction",
        "The study of drug interactions with muscle tissue": "The study of how pharmacological drugs interact with skeletal muscle tissue, including performance-enhancing substances and their physiological effects",
    },
    ("Unit3/Lesson3.7_Quiz.json", 25): {
        "Surgical intervention is immediately required": "Surgical intervention is immediately required to repair the tibial periosteum, followed by complete restriction on weight-bearing activity for at least six months",
        "Increase training intensity immediately to 'push through' the pain": "Increase training intensity immediately and push through the pain, as the discomfort is simply muscle weakness that will resolve with higher training loads and more frequent runs",
        "Complete bed rest for 3 months with no exercise": "Complete bed rest for at least three months with absolutely no exercise, as any movement will prevent the periosteum from healing and could cause a tibial stress fracture",
    },
    ("Unit3/Lesson3.7_Quiz.json", 26): {
        "CTE can be easily diagnosed with a simple blood test": "CTE can be definitively diagnosed in living patients with a simple blood test that detects elevated tau protein levels, making post-mortem brain examination completely unnecessary",
        "A standard MRI can definitively diagnose CTE in living patients": "A standard MRI scan can definitively diagnose CTE in living patients by revealing characteristic patterns of tau protein deposits in the brain tissue, providing a reliable imaging biomarker",
        "CTE does not actually exist and is not recognized by medical science": "CTE does not actually exist as a distinct medical condition and is not recognized by any major neurological organization; the symptoms attributed to CTE are better explained by normal aging processes",
    },
    ("Unit3/Lesson3.7_Quiz.json", 27): {
        "Swimming does not involve repetitive shoulder movements": "Swimming does not actually involve repetitive shoulder movements because the water resistance and buoyancy eliminate the overhead stress that would normally occur during land-based activities",
        "The chlorine in pool water directly damages shoulder tendons": "The chlorine and other chemical disinfectants present in pool water directly penetrate the skin and chemically degrade the collagen fibers within the shoulder tendons over time",
        "Swimming primarily stresses the hip joint, not the shoulder": "Swimming primarily generates mechanical stress on the hip joint and lower extremity rather than the shoulder, since the kick phase provides most of the propulsive force",
    },
    ("Unit3/Lesson3.7_Quiz.json", 28): {
        "Tennis elbow is caused by a bone fracture at the elbow": "Tennis elbow is caused by a stress fracture at the lateral epicondyle of the humerus that develops from repeated impact forces transmitted through the racquet into the elbow joint during each stroke",
        "Tennis elbow only occurs in professional tennis players": "Tennis elbow only occurs in professional tennis players who practice many hours daily, because the tendons of recreational players are not subjected to sufficient repetitive stress to develop micro-tears",
        "The elbow joint dislocated during play": "The elbow joint partially dislocated during play, causing the common extensor tendon to sublux over the lateral epicondyle, resulting in mechanical irritation and chronic pain with gripping",
    },
    # Lesson3.8
    ("Unit3/Lesson3.8_Quiz.json", 6): {
        "Maintaining posture": "Maintaining upright posture through prolonged low-intensity contractions",
        "Long-distance swimming": "Long-distance aerobic swimming and sustained endurance efforts",
        "Marathon running": "Marathon running and other sustained oxidative endurance activities",
    },
    ("Unit3/Lesson3.8_Quiz.json", 9): {
        "Complete tetanus is weaker than incomplete tetanus": "Complete tetanus is weaker than incomplete tetanus because the sustained fusion of stimuli fatigues the available cross-bridges over time",
        "Incomplete tetanus involves no contraction at all": "Incomplete tetanus involves no meaningful contraction because the gaps between stimuli prevent any useful summation of force",
        "There is no difference between them": "There is no physiological difference between complete and incomplete tetanus; both produce the same contractile force and relaxation pattern",
    },
    ("Unit3/Lesson3.8_Quiz.json", 13): {
        "A drug that increases muscle contraction strength permanently": "A drug that permanently increases muscle contraction strength by enhancing the sensitivity of actin-myosin cross-bridges to calcium, producing larger forces with each cycle",
        "A drug that blocks calcium channels in the heart only": "A drug that selectively blocks voltage-gated calcium channels in cardiac muscle only, reducing heart rate and contraction strength without any effect on skeletal muscle",
        "A vitamin supplement that enhances nerve function": "A vitamin supplement that enhances nerve conduction velocity at the neuromuscular junction, improving the speed and reliability of signal transmission to muscle fibers",
    },
    ("Unit3/Lesson3.8_Quiz.json", 18): {
        "It pumps calcium back into the SR during relaxation": "It serves as an active calcium pump on the sarcoplasmic reticulum membrane that resequesters calcium ions during the relaxation phase of muscle contraction",
        "It breaks down acetylcholine at the NMJ": "It functions as an enzyme at the neuromuscular junction that rapidly breaks down acetylcholine after it has bound to the motor end plate receptors",
        "It forms the cross-bridge between actin and myosin": "It forms the structural cross-bridge connection between the actin thin filament and the myosin thick filament during the power stroke of contraction",
    },
    ("Unit3/Lesson3.8_Quiz.json", 20): {
        "The decrease in force during repeated contractions": "The progressive decrease in force-generating capacity during repeated contractions, caused by the accumulation of metabolic waste products in the sarcoplasm",
        "The generation of force by a single motor unit in isolation": "The generation of contractile force by a single motor unit functioning in isolation, independent of any recruitment of additional motor units or frequency changes",
        "The resting tension in a completely relaxed muscle": "The baseline resting tension present in a completely relaxed muscle due to the inherent elasticity of the connective tissue elements and passive sarcolemma resistance",
    },
    ("Unit3/Lesson3.8_Quiz.json", 22): {
        "The muscle only produces force at one exact length and produces zero force at all other lengths": "The muscle only produces force at one exact sarcomere length of 2.2 micrometers and produces zero force at all other lengths, because cross-bridges can only form at this single precise overlap distance between actin and myosin",
        "Force depends only on the number of motor units recruited, not sarcomere length": "Force depends only on the number of motor units recruited and the frequency of stimulation, not on sarcomere length, because cross-bridge formation is independent of the degree of overlap between actin and myosin",
        "At any length, the muscle produces the same force because all cross-bridges always form": "At any length, the muscle produces the same force because all available cross-bridges always form regardless of filament overlap, since myosin heads can reach actin binding sites at any distance between the thick and thin filaments",
    },
    ("Unit3/Lesson3.8_Quiz.json", 23): {
        "The muscle switches from skeletal to cardiac muscle type at high frequencies": "The muscle switches from skeletal to cardiac-type contractile behavior at high stimulation frequencies, adopting the autorhythmic properties and gap-junction-mediated conduction that are characteristic of cardiac tissue",
        "Higher stimulus frequencies create new motor units": "Higher stimulus frequencies trigger the formation of new motor units within the muscle by activating previously non-innervated muscle fibers and establishing new neuromuscular junctions",
        "The transitions occur because the muscle grows larger with each stimulus": "The transitions from twitch to tetanus occur because the muscle physically grows larger with each successive stimulus, adding new sarcomeres and myofibrils that increase force capacity",
    },
    ("Unit3/Lesson3.8_Quiz.json", 24): {
        "ACh would decrease and muscles would relax": "ACh levels in the synaptic cleft would decrease rapidly because the organophosphate stimulates acetylcholinesterase to work faster, causing muscles to relax completely due to insufficient stimulation at the motor end plate",
        "The muscle would strengthen and improve performance": "The muscle would strengthen and improve its contractile performance because the prolonged presence of ACh at the motor end plate would enhance excitation-contraction coupling efficiency and increase maximum force output",
        "Only smooth muscle would be affected": "Only smooth muscle in the walls of hollow organs would be affected because skeletal muscle at the neuromuscular junction uses a different neurotransmitter system that is not influenced by cholinesterase",
    },
    ("Unit3/Lesson3.8_Quiz.json", 25): {
        "Curare increases ACh release while botulinum toxin increases receptor sensitivity": "Curare increases the amount of ACh released from the presynaptic terminal by enhancing vesicle fusion, while botulinum toxin increases the sensitivity of postsynaptic nicotinic receptors, producing excessive stimulation",
        "Neither drug affects the NMJ; they both act directly on sarcomeres": "Neither drug affects the neuromuscular junction at all; both curare and botulinum toxin act directly on the sarcomere by binding to and inhibiting the myosin ATPase enzyme, preventing the power stroke cycle",
        "Both drugs work identically by destroying the motor neuron": "Both drugs work identically by triggering apoptosis of the motor neuron cell body, leading to irreversible denervation of the muscle fiber and permanent loss of voluntary contraction in the affected muscles",
    },
    ("Unit3/Lesson3.8_Quiz.json", 26): {
        "Rigor mortis is caused by excess calcium that cannot be removed after death": "Rigor mortis is caused solely by excess calcium flooding the sarcoplasm after death, which triggers uncontrolled cross-bridge cycling; supplying ATP would have no effect because the calcium overload is the primary problem",
        "Rigor occurs because excess ATP locks the cross-bridges; removing ATP would cause relaxation": "Rigor occurs because excess ATP production continues after death and locks the myosin heads onto actin in a permanent bound state; removing this accumulated ATP from the muscle would release the cross-bridges and allow relaxation",
        "ATP has no relationship to rigor mortis": "ATP has absolutely no relationship to rigor mortis or cross-bridge cycling; the stiffness after death is caused entirely by the denaturation of structural proteins in the sarcomere that lock the muscle into a rigid state",
    },
    ("Unit3/Lesson3.8_Quiz.json", 28): {
        "The muscle would never be able to contract at all": "The muscle would never be able to contract at all because the Ca2+-ATPase pump is required for the initial release of calcium from the sarcoplasmic reticulum, and without a functioning pump no calcium would ever reach troponin",
        "Contraction would be weaker but relaxation would be normal": "Contraction would be significantly weaker because the Ca2+-ATPase pump is needed to concentrate calcium in the SR before release, but the relaxation phase would proceed normally since it depends on passive diffusion",
        "Both contraction and relaxation would be completely normal": "Both contraction and relaxation would be completely normal because the Ca2+-ATPase pump plays only a minor supplementary role in calcium handling and other transport mechanisms would fully compensate for the reduced efficiency",
    },
    ("Unit3/Lesson3.8_Quiz.json", 29): {
        "Temperature has no effect on muscle enzyme activity": "Temperature has no effect on muscle enzyme activity because the enzymes involved in contraction, including myosin ATPase and Ca2+-ATPase, maintain constant catalytic rates regardless of tissue temperature",
        "Treppe is caused by an increase in the number of sarcomeres per fiber": "Treppe is caused by an increase in the number of sarcomeres added in series within each muscle fiber during repeated contractions, increasing the total length and force-generating capacity",
        "Treppe occurs because new muscle fibers are created during the warm-up": "Treppe occurs because entirely new muscle fibers are created through rapid mitotic division during the warm-up period, increasing the total number of contractile units available for force",
    },
    ("Unit3/Lesson3.8_Quiz.json", 30): {
        "Nerve AP, contraction, relaxation - only three steps are involved": "The process involves only three main phases: the nerve action potential reaches the muscle, the muscle contracts through an unspecified mechanism, and then the muscle relaxes when stimulation stops, with no intermediate molecular steps or calcium signaling events occurring between these broad phases",
        "The pathway differs for each individual and cannot be summarized": "The pathway from nerve signal to muscle contraction and relaxation differs for each individual person based on their unique genetics, muscle fiber type composition, and training history, making it impossible to summarize into one universal sequence",
        "ACh release, calcium binding, power stroke - only three steps with one ATP used": "The entire sequence from nerve to contraction consists of only three molecular steps: acetylcholine release from the nerve terminal, calcium binding to the contractile proteins, and a single power stroke, with just one molecule of ATP consumed during the whole cycle",
    },
}

files_modified = set()
for (rel_path, qnum), text_map in replacements.items():
    full_path = os.path.join(base, rel_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for q in data['quiz_questions']:
        if q['question_number'] == qnum:
            for opt in q['options']:
                if not opt['is_correct'] and opt['text'] in text_map:
                    opt['text'] = text_map[opt['text']]
            break

    with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    files_modified.add(full_path)

print(f"Modified {len(files_modified)} files")

# Verify
files = sorted(glob.glob(os.path.join(base, 'Unit3', '*Quiz*.json')))
still_flagged = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    for q in data['quiz_questions']:
        correct_text = ''
        wrong_texts = []
        for opt in q['options']:
            if opt['is_correct']:
                correct_text = opt['text']
            else:
                wrong_texts.append(opt['text'])
        if not wrong_texts: continue
        correct_len = len(correct_text)
        avg_wrong_len = sum(len(w) for w in wrong_texts) / len(wrong_texts)
        if avg_wrong_len > 0 and correct_len / avg_wrong_len >= 3.0:
            still_flagged += 1
            print(f'STILL FLAGGED: {os.path.basename(f)} Q{q["question_number"]}: ratio={correct_len/avg_wrong_len:.1f}')

if still_flagged == 0:
    print("Unit 3: ALL CLEAR!")
else:
    print(f"Unit 3: {still_flagged} still flagged")
