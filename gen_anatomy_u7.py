#!/usr/bin/env python3
"""Anatomy Unit 7 – Respiratory System (8 lessons)."""
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

# 7.1
k,v = build_lesson(7,1,"Anatomy of the Respiratory System",
    "<h3>Anatomy of the Respiratory System</h3>"
    "<h4>Upper Respiratory Tract</h4>"
    "<ul><li><b>Nose/nasal cavity:</b> Warms, moistens, filters air. <b>Pharynx:</b> Throat; shared with digestive tract.</li>"
    "<li><b>Larynx:</b> Voice box; epiglottis prevents food from entering the trachea.</li></ul>"
    "<h4>Lower Respiratory Tract</h4>"
    "<ul><li><b>Trachea:</b> Windpipe; C-shaped cartilage rings.</li>"
    "<li><b>Bronchi → bronchioles → terminal bronchioles → respiratory bronchioles → alveolar ducts → alveoli.</b></li>"
    "<li><b>Alveoli:</b> ~300 million; thin-walled sacs where gas exchange occurs.</li>"
    "<li><b>Lungs:</b> Right (3 lobes), left (2 lobes). <b>Pleura:</b> Serous membrane lining.</li></ul>",
    [("Alveoli","Tiny air sacs (~300 million) in the lungs where O₂/CO₂ exchange occurs with capillaries."),
     ("Trachea","Windpipe; supported by C-shaped cartilage rings; leads to the bronchi."),
     ("Larynx","Voice box; contains vocal cords; epiglottis guards the airway during swallowing."),
     ("Bronchi","Two main branches of the trachea (right and left); carry air into each lung."),
     ("Pleura","Double-layered serous membrane (visceral + parietal) surrounding each lung.")],
    [("The primary function of the respiratory system is:",["Digestion","*Gas exchange (O₂ in, CO₂ out)","Blood filtration","Hormone production"],"Ventilation and gas exchange."),
     ("Air is warmed, humidified, and filtered in the:",["Alveoli","*Nasal cavity","Bronchi","Trachea"],"Nasal mucosa and turbinates condition air."),
     ("The epiglottis prevents:",["Breathing","*Food from entering the trachea during swallowing","Speech","Coughing"],"Flaps over larynx during swallowing."),
     ("The trachea is kept open by:",["Muscle only","*C-shaped cartilage rings","Bone","Ligaments"],"Cartilage prevents collapse."),
     ("The trachea divides into:",["4 bronchi","*2 main (primary) bronchi (left and right)","6 bronchi","No branches"],"One to each lung."),
     ("The right lung has _____ lobes.",["2","*3","4","1"],"Right = 3 lobes (superior, middle, inferior)."),
     ("The left lung has _____ lobes.",["3","*2","4","1"],"Left = 2 lobes (superior, inferior) — cardiac notch."),
     ("Alveoli are the site of:",["Air filtration","*Gas exchange (O₂ into blood, CO₂ out of blood)","Mucus production","Voice production"],"Thin walls allow diffusion."),
     ("Approximately how many alveoli are in both lungs?",["1 million","10 million","*~300 million","1 billion"],"Enormous surface area for gas exchange."),
     ("The respiratory membrane consists of:",["Thick layers of muscle","*Alveolar epithelium + capillary endothelium (very thin for diffusion)","Cartilage","Only epithelium"],"~0.5 µm thick."),
     ("Type I alveolar cells:",["Produce surfactant","*Are thin squamous cells forming most of the gas exchange surface","Are immune cells","Produce mucus"],"Thin = optimized for diffusion."),
     ("Type II alveolar cells produce:",["Mucus","*Surfactant (reduces surface tension, prevents alveolar collapse)","Hemoglobin","Hormones"],"Surfactant is essential for lung compliance."),
     ("The pleura has two layers: visceral (on lung) and parietal (on chest wall). Between them is:",["Air","*A thin layer of serous fluid (reduces friction during breathing)","Blood","Nothing"],"Pleural fluid lubricates."),
     ("Pneumothorax is:",["Excess fluid in the lungs","*Air in the pleural space → lung collapse","A lung infection","A blood clot"],"Collapsed lung."),
     ("The bronchial tree progressively _____ in diameter.",["Increases","*Decreases (bronchi → bronchioles → terminal bronchioles)","Stays the same","Varies randomly"],"Gets smaller with each branching."),
     ("Cilia in the respiratory tract:",["Absorb oxygen","*Move mucus (with trapped particles) upward toward the throat (mucociliary escalator)","Produce surfactant","Generate sound"],"Clears debris from airways."),
     ("Smoking damages cilia, leading to:",["Better breathing","*Impaired mucus clearance → increased infections and chronic bronchitis","Stronger lungs","No effect"],"Paralyzed cilia = mucus accumulation."),
     ("The diaphragm is the primary muscle of:",["Digestion","*Respiration (contraction = inhalation)","Circulation","Excretion"],"Dome-shaped muscle below the lungs."),
     ("The hilum of the lung is where:",["Gas exchange occurs","*Bronchi, blood vessels, lymphatics, and nerves enter and exit the lung","The diaphragm attaches","Pleural fluid collects"],"Root of the lung."),
     ("Understanding respiratory anatomy is essential for:",["Nothing","*Diagnosing and treating asthma, pneumonia, COPD, lung cancer, and more","Only anatomy class","Only surgeons"],"Foundation for pulmonary medicine.")]
)
lessons[k]=v

# 7.2
k,v = build_lesson(7,2,"Mechanics of Breathing",
    "<h3>Mechanics of Breathing</h3>"
    "<h4>Inspiration (Inhalation)</h4>"
    "<p>Diaphragm contracts (flattens) + external intercostals lift ribs → thoracic volume increases → intrapulmonary pressure drops below atmospheric → air flows in.</p>"
    "<h4>Expiration (Exhalation)</h4>"
    "<p>Passive at rest: diaphragm relaxes (domes up) + elastic recoil of lungs → thoracic volume decreases → pressure increases → air flows out. Forced expiration uses internal intercostals and abdominal muscles.</p>"
    "<h4>Lung Volumes</h4>"
    "<p>Tidal volume (~500 mL), vital capacity, residual volume, total lung capacity. Spirometry measures these.</p>",
    [("Inspiration","Active process; diaphragm contracts, thoracic volume increases, pressure drops, air flows in."),
     ("Expiration","Passive at rest (elastic recoil); forced expiration uses internal intercostals and abdominals."),
     ("Tidal Volume","Volume of air inhaled/exhaled in a normal breath (~500 mL)."),
     ("Vital Capacity","Maximum air exhaled after maximum inhalation (~4.8 L)."),
     ("Residual Volume","Air remaining in lungs after maximum exhalation (~1.2 L); prevents alveolar collapse.")],
    [("During inspiration, the diaphragm:",["Relaxes and moves up","*Contracts and flattens (moves down), increasing thoracic volume","Does not move","Moves laterally"],"Diaphragm contraction = inhalation."),
     ("During inspiration, intrapulmonary pressure:",["Increases above atmospheric","*Drops below atmospheric pressure → air flows in","Stays equal to atmospheric","Reaches zero"],"Boyle's law: ↑volume → ↓pressure."),
     ("Quiet expiration at rest is:",["Active (muscular)","*Passive (elastic recoil of lungs and relaxation of diaphragm)","Impossible","Voluntary only"],"No muscle effort needed at rest."),
     ("Forced expiration uses:",["Only the diaphragm","*Internal intercostals and abdominal muscles","Only external intercostals","No muscles"],"Active contraction compresses thorax."),
     ("Tidal volume is approximately:",["100 mL","*500 mL","2000 mL","5000 mL"],"Normal resting breath volume."),
     ("Vital capacity is:",["Same as tidal volume","*The maximum amount of air exhaled after a maximum inhalation","The total lung capacity","The residual volume"],"VC = IRV + TV + ERV."),
     ("Residual volume is:",["The normal breath volume","*Air that remains in the lungs and cannot be exhaled (prevents alveolar collapse)","The maximum breath","Zero in healthy lungs"],"~1.2 L always remains."),
     ("Total lung capacity (TLC) = ",["*Vital capacity + residual volume (~6 L)","Tidal volume × rate","Only vital capacity","Only residual volume"],"VC + RV = TLC."),
     ("Spirometry measures:",["Blood pressure","*Lung volumes and airflow rates","Heart function","Blood gases"],"Key pulmonary function test."),
     ("Boyle's law states that pressure and volume are:",["Directly proportional","*Inversely proportional (↑volume → ↓pressure)","Unrelated","Equal"],"Basis of breathing mechanics."),
     ("The external intercostals assist inspiration by:",["Lowering the ribs","*Elevating the ribs (increasing thoracic diameter)","Compressing the abdomen","Relaxing the diaphragm"],"Bucket-handle motion expands chest."),
     ("Pulmonary compliance refers to:",["Airway resistance","*How easily the lungs expand (stretchability)","Lung volume","Breathing rate"],"High compliance = easy expansion."),
     ("Surfactant increases compliance by:",["Increasing surface tension","*Reducing surface tension in alveoli (preventing collapse)","Thickening alveolar walls","Producing mucus"],"Without surfactant, alveoli collapse."),
     ("Premature infants may lack surfactant, causing:",["No problems","*Respiratory distress syndrome (RDS) — difficulty expanding alveoli","Excess breathing","Strong lungs"],"Surfactant production matures late in fetal development."),
     ("Airway resistance is highest in the:",["Alveoli","*Medium-sized bronchi (total cross-sectional area is relatively small here)","Trachea","Nose"],"Individual bronchi are narrower; total resistance peaks there."),
     ("In asthma, airway resistance _____ due to bronchospasm.",["Decreases","*Increases (narrowed airways → harder to breathe, especially exhale)","Stays the same","Disappears"],"Asthma = obstructive disease."),
     ("Minute ventilation = ",["*Tidal volume × respiratory rate","Vital capacity × rate","Residual volume × rate","Total lung capacity / rate"],"MV = TV × RR. Normal: 500 mL × 12 = 6 L/min."),
     ("Dead space refers to:",["The alveoli","*Volume of air in conducting airways that does not participate in gas exchange (~150 mL)","The total lung volume","Air in the pleura"],"Anatomical dead space."),
     ("A pneumothorax impairs breathing because:",["Muscles fail","*Air in the pleural space breaks the negative pressure → lung collapses","Blood enters the lungs","Mucus blocks airways"],"Loss of intrapleural negative pressure."),
     ("Understanding breathing mechanics is essential for:",["Nothing","*Managing COPD, asthma, respiratory failure, and ventilator settings in critical care","Only anatomy class","Only exercise science"],"Fundamental to pulmonary and critical care medicine.")]
)
lessons[k]=v

# 7.3
k,v = build_lesson(7,3,"Gas Exchange in the Alveoli",
    "<h3>Gas Exchange in the Alveoli</h3>"
    "<h4>Principles</h4>"
    "<p>Gas exchange occurs by simple diffusion across the respiratory membrane. O₂ diffuses from alveoli (high PO₂ ~104 mmHg) into pulmonary capillary blood (low PO₂ ~40 mmHg). CO₂ diffuses from blood (PCO₂ ~45 mmHg) into alveoli (PCO₂ ~40 mmHg).</p>"
    "<h4>Factors Affecting Exchange</h4>"
    "<ul><li><b>Surface area:</b> ~70 m²; reduced in emphysema.</li>"
    "<li><b>Membrane thickness:</b> Thickened in fibrosis → impaired diffusion.</li>"
    "<li><b>Ventilation-perfusion (V/Q) matching:</b> Adequate airflow matched with blood flow for efficient exchange.</li></ul>",
    [("Partial Pressure","The pressure exerted by a single gas in a mixture; drives diffusion."),
     ("Respiratory Membrane","Alveolar epithelium + capillary endothelium; ~0.5 µm; where gas exchange occurs."),
     ("Ventilation-Perfusion (V/Q) Matching","Ideal ratio of alveolar airflow to capillary blood flow for efficient gas exchange."),
     ("Emphysema","Destructive lung disease that reduces alveolar surface area → impaired gas exchange."),
     ("Pulmonary Fibrosis","Thickening/scarring of lung tissue increasing diffusion distance → impaired gas exchange.")],
    [("Gas exchange in the alveoli occurs by:",["Active transport","*Simple diffusion (down partial pressure gradients)","Osmosis","Exocytosis"],"Passive process driven by pressure gradients."),
     ("O₂ moves from the alveoli into the blood because:",["Blood has higher PO₂","*Alveolar PO₂ (104 mmHg) is higher than blood PO₂ (40 mmHg)","It's actively pumped","Hemoglobin pushes it"],"O₂ follows its gradient into blood."),
     ("CO₂ moves from blood into the alveoli because:",["Alveolar PCO₂ is higher","*Blood PCO₂ (45 mmHg) is higher than alveolar PCO₂ (40 mmHg)","CO₂ is pumped","Carbonic anhydrase pulls it"],"CO₂ follows its gradient into alveoli."),
     ("The respiratory membrane is approximately _____ thick.",["5 mm","1 mm","*0.5 µm (very thin)","10 µm"],"Extremely thin for rapid diffusion."),
     ("The total surface area for gas exchange in the lungs is approximately:",["10 m²","*70 m² (about the size of a tennis court)","1 m²","200 m²"],"300 million alveoli = huge area."),
     ("In emphysema, gas exchange is impaired because:",["Airways constrict","*Alveolar walls are destroyed → reduced surface area","Mucus blocks gases","Surfactant is excessive"],"Less surface = less exchange."),
     ("In pulmonary fibrosis, gas exchange is impaired because:",["Surface area is large","*The respiratory membrane is thickened → increased diffusion distance","Alveoli collapse","Blood flow stops"],"Thicker barrier slows diffusion."),
     ("Ventilation-perfusion (V/Q) matching means:",["All alveoli get equal air","*Airflow (ventilation) is matched with blood flow (perfusion) for efficient exchange","Only one lung works","V and Q are always equal"],"Mismatch → wasted ventilation or wasted perfusion."),
     ("A V/Q mismatch where an alveolus has airflow but no blood flow is called:",["*Dead space ventilation (wasted ventilation)","Shunt","Normal","Atelectasis"],"Ventilated but not perfused."),
     ("A V/Q mismatch where blood flows past an unventilated alveolus is called:",["Dead space","*Shunt (blood is not oxygenated)","Normal V/Q","Hyperventilation"],"Perfused but not ventilated."),
     ("Dalton's law of partial pressures states:",["Total P is from one gas","*Total gas pressure = sum of individual gas partial pressures","Pressure is constant","Volume determines pressure alone"],"Each gas exerts its own pressure."),
     ("Henry's law states that gas solubility in liquid depends on:",["Temperature only","Surface area only","*Partial pressure of the gas and its solubility coefficient","Volume only"],"Higher PP → more gas dissolves."),
     ("At high altitude, PO₂ is _____, making gas exchange _____.",["Higher; easier","*Lower; more difficult (less O₂ available)","The same; unchanged","Higher; harder"],"Lower atmospheric P → lower PO₂."),
     ("Supplemental oxygen helps patients by:",["Replacing all air","*Increasing alveolar PO₂ → steeper gradient → more O₂ into blood","Cooling the lungs","Removing CO₂"],"Higher FiO₂ improves oxygenation."),
     ("Pulmonary edema impairs gas exchange because:",["It reduces blood flow","*Fluid in the alveoli increases diffusion distance and reduces surface area","It increases ventilation","It destroys surfactant"],"Fluid barrier between air and blood."),
     ("CO₂ is about _____ times more soluble in blood than O₂.",["The same","*20 times more","5 times less","100 times more"],"CO₂ diffuses easily even with small gradients."),
     ("ABG (arterial blood gas) analysis measures:",["Only pH","*pH, PaO₂, PaCO₂, HCO₃⁻, and O₂ saturation","Only O₂","Only CO₂"],"Comprehensive assessment of gas exchange and acid-base."),
     ("Hypoxemia is defined as:",["High blood O₂","*Low arterial O₂ (PaO₂ <60 mmHg)","Low CO₂","High CO₂"],"Insufficient oxygen in arterial blood."),
     ("Hypercapnia is defined as:",["Low CO₂","Low O₂","*High arterial CO₂ (PaCO₂ >45 mmHg)","High O₂"],"CO₂ retention."),
     ("Understanding gas exchange is critical because:",["Only for respiratory therapists","*Impaired exchange underlies respiratory failure, COPD, pneumonia, ARDS, and many emergencies","It's only theoretical","It doesn't change in disease"],"Core concept in pulmonary and critical care medicine.")]
)
lessons[k]=v

# 7.4
k,v = build_lesson(7,4,"Transport of O₂ & CO₂",
    "<h3>Transport of O₂ &amp; CO₂</h3>"
    "<h4>Oxygen Transport</h4>"
    "<ul><li>~98.5% bound to hemoglobin (Hb) → oxyhemoglobin (HbO₂).</li>"
    "<li>~1.5% dissolved in plasma.</li>"
    "<li><b>O₂-Hb dissociation curve:</b> Sigmoidal; right shift (↑temp, ↓pH, ↑CO₂, ↑2,3-BPG) → easier O₂ release to tissues.</li></ul>"
    "<h4>CO₂ Transport</h4>"
    "<ul><li>~70% as bicarbonate (HCO₃⁻) via carbonic anhydrase: CO₂ + H₂O → H₂CO₃ → H⁺ + HCO₃⁻.</li>"
    "<li>~23% bound to Hb (carbaminohemoglobin). ~7% dissolved.</li></ul>",
    [("Oxyhemoglobin","Hemoglobin bound to O₂ (HbO₂); forms in the lungs, releases O₂ in tissues."),
     ("O₂-Hb Dissociation Curve","Sigmoidal curve showing Hb's O₂ saturation vs. PO₂; right shift = easier O₂ unloading."),
     ("Bicarbonate (HCO₃⁻)","Primary form of CO₂ transport in blood (~70%); formed by carbonic anhydrase in RBCs."),
     ("Carbonic Anhydrase","Enzyme in RBCs catalyzing CO₂ + H₂O ↔ H₂CO₃ ↔ H⁺ + HCO₃⁻."),
     ("Bohr Effect","Increased H⁺ or CO₂ decreases Hb's affinity for O₂ → promotes O₂ release in active tissues.")],
    [("Most O₂ in blood is transported:",["Dissolved in plasma","*Bound to hemoglobin (~98.5% as oxyhemoglobin)","As bicarbonate","Bound to albumin"],"Hb carries almost all O₂."),
     ("Each hemoglobin molecule can bind up to _____ O₂ molecules.",["1","2","*4","8"],"4 heme groups = 4 O₂."),
     ("The O₂-Hb dissociation curve is:",["Linear","*Sigmoidal (S-shaped)","Exponential","Flat"],"Cooperative binding."),
     ("A right shift of the O₂-Hb curve means:",["Hb holds O₂ tighter","*Hb releases O₂ more easily (beneficial for active tissues)","No change","Hb can't bind O₂"],"More O₂ delivered to working muscles."),
     ("Factors causing a right shift include:",["↓Temp, ↑pH","*↑Temperature, ↓pH (↑H⁺), ↑CO₂, ↑2,3-BPG","↓CO₂ only","Cold temperature only"],"Active tissue conditions promote O₂ release."),
     ("The Bohr effect describes:",["O₂ binding improving","*↑CO₂ and ↓pH reducing Hb's affinity for O₂ (promoting O₂ release to tissues)","CO₂ transport only","Hb production"],"Active tissues produce CO₂ and acid → more O₂ delivered."),
     ("Most CO₂ (~70%) is transported as:",["Dissolved gas","Carbaminohemoglobin","*Bicarbonate ions (HCO₃⁻) in plasma","Bound to albumin"],"Carbonic anhydrase converts CO₂ in RBCs."),
     ("Carbonic anhydrase catalyzes:",["O₂ binding to Hb","*CO₂ + H₂O → H₂CO₃ → H⁺ + HCO₃⁻","Hemoglobin synthesis","Surfactant production"],"Rapid conversion in red blood cells."),
     ("About 23% of CO₂ is carried as:",["Bicarbonate","*Carbaminohemoglobin (bound to Hb's amino groups)","Dissolved CO₂","Carboxyhemoglobin"],"CO₂ binds to globin protein, not heme."),
     ("About 7% of CO₂ is:",["Bound to Hb","Bicarbonate","*Dissolved directly in plasma","Converted to O₂"],"Small fraction dissolved in plasma."),
     ("Carbon monoxide (CO) poisoning is dangerous because:",["CO is acidic","*CO binds Hb ~200× more tightly than O₂, blocking O₂ transport","CO destroys Hb","CO is a nutrient"],"Carboxyhemoglobin can't carry O₂."),
     ("Pulse oximetry measures:",["Blood pressure","*Oxygen saturation (SpO₂) of hemoglobin (normal ≥95%)","Heart rate only","CO₂ levels"],"Non-invasive O₂ monitoring."),
     ("Cyanosis (bluish skin) indicates:",["Normal oxygenation","*Significant deoxygenation of hemoglobin","High O₂","CO poisoning always"],"Deoxyhemoglobin = bluish color."),
     ("Fetal hemoglobin (HbF) has a _____ affinity for O₂ than adult Hb.",["Lower","*Higher (left-shifted curve) — allows fetus to extract O₂ from maternal blood","Same","No"],"HbF pulls O₂ from maternal Hb."),
     ("In the chloride shift:",["Chloride enters RBCs as HCO₃⁻ exits → maintains electrical neutrality","*Cl⁻ moves into RBC as HCO₃⁻ moves out","Chloride is destroyed","No ions move"],"Maintains electron balance."),
     ("At the tissue level, Hb:",["Picks up O₂","*Releases O₂ (low PO₂, high PCO₂, low pH promote unloading)","Picks up CO₂ only","Does nothing"],"Tissue conditions favor O₂ release."),
     ("At the lungs, Hb:",["Releases all O₂","*Picks up O₂ (high PO₂) and releases CO₂","Picks up CO₂","Decomposes"],"Lung conditions favor O₂ loading."),
     ("2,3-BPG is produced by:",["The lungs","*Red blood cells during glycolysis","The liver","White blood cells"],"2,3-bisphosphoglycerate promotes O₂ release."),
     ("Anemia reduces O₂ transport because:",["Lungs fail","*Fewer RBCs or less Hb means less O₂-carrying capacity","Hb changes structure","CO₂ increases"],"Less Hb = less O₂ carried."),
     ("Understanding O₂/CO₂ transport is critical for:",["Nothing practical","*Managing respiratory failure, anemia, CO poisoning, blood transfusions, and exercise physiology","Only chemists","Only lab workers"],"Core physiology for clinical medicine.")]
)
lessons[k]=v

# 7.5
k,v = build_lesson(7,5,"Regulation of Breathing",
    "<h3>Regulation of Breathing</h3>"
    "<h4>Neural Control</h4>"
    "<ul><li><b>Medullary respiratory center:</b> Sets the basic rhythm — dorsal respiratory group (inspiration), ventral respiratory group (forced breathing).</li>"
    "<li><b>Pontine respiratory group:</b> Smooths transitions between inspiration and expiration.</li></ul>"
    "<h4>Chemical Control</h4>"
    "<ul><li><b>Central chemoreceptors (medulla):</b> Detect ↑CO₂ (via ↑H⁺ in CSF) — primary driver of ventilation.</li>"
    "<li><b>Peripheral chemoreceptors (carotid/aortic bodies):</b> Detect ↓O₂, ↑CO₂, ↓pH.</li></ul>",
    [("Medullary Respiratory Center","Brainstem region that generates the basic rhythm of breathing."),
     ("Central Chemoreceptors","In the medulla; primarily sense ↑CO₂ (via H⁺ in CSF) to increase ventilation."),
     ("Peripheral Chemoreceptors","In carotid/aortic bodies; detect low O₂, high CO₂, low pH."),
     ("Hering-Breuer Reflex","Stretch receptors in lungs prevent overinflation by inhibiting inspiration."),
     ("Hypercapnic Drive","Normal stimulus to breathe: rising CO₂ detected by chemoreceptors → increased ventilation.")],
    [("The primary respiratory control center is in the:",["Cerebrum","Cerebellum","*Medulla oblongata","Spinal cord"],"Medulla generates basic breathing rhythm."),
     ("The primary chemical stimulus for breathing is:",["Low O₂","*High CO₂ (detected as H⁺ by central chemoreceptors)","Low CO₂","High O₂"],"CO₂ is the primary respiratory drive."),
     ("Central chemoreceptors detect CO₂ by sensing:",["CO₂ directly","*H⁺ ions (CO₂ crosses BBB → converts to H⁺ in CSF)","O₂ levels","Bicarbonate only"],"CO₂ → H₂CO₃ → H⁺ in CSF."),
     ("Peripheral chemoreceptors are located in the:",["Brain","*Carotid and aortic bodies","Lungs","Spinal cord"],"Detect O₂, CO₂, and pH changes in blood."),
     ("Peripheral chemoreceptors respond primarily to:",["*Significant decreases in blood O₂ (PaO₂ <60 mmHg)","Normal O₂ ranges","High O₂","Low CO₂"],"O₂ must drop significantly to trigger these."),
     ("The Hering-Breuer reflex:",["Stimulates inspiration","*Prevents lung overinflation by inhibiting inspiration when lungs are stretched","Promotes coughing","Regulates blood pressure"],"Stretch receptors in lung tissue."),
     ("Hyperventilation causes:",["*↓CO₂ (hypocapnia) → respiratory alkalosis → lightheadedness/tingling","↑CO₂","No change","↑O₂ dramatically"],"Blowing off too much CO₂."),
     ("Hypoventilation causes:",["↓CO₂","*↑CO₂ (hypercapnia) → respiratory acidosis","No change","↓O₂ only"],"Not enough CO₂ removed."),
     ("In chronic COPD, some patients rely on a 'hypoxic drive' because:",["Normal","*Chronically elevated CO₂ has desensitized central chemoreceptors; low O₂ becomes the stimulus","They don't breathe","They have no medulla"],"Hypoxic drive = backup mechanism."),
     ("The pontine respiratory group:",["Generates the basic rhythm","*Modifies and smooths transitions between inspiration and expiration","Is not involved in breathing","Only controls forced breathing"],"Fine-tunes the medullary rhythm."),
     ("Voluntary control of breathing involves the:",["Medulla only","*Cerebral cortex (can temporarily override automatic breathing)","Cerebellum","Pons only"],"You can consciously hold your breath."),
     ("You cannot voluntarily hold your breath until you die because:",["You are too weak","*Rising CO₂ and falling O₂ eventually override voluntary control","The heart stops","The diaphragm is voluntary"],"Involuntary drive forces breathing."),
     ("During exercise, ventilation increases because of:",["Only low O₂","*↑CO₂ production, ↓pH, ↑body temperature, and neural input from muscles","Only conscious effort","No change"],"Multiple factors increase ventilation."),
     ("Apnea means:",["Fast breathing","Normal breathing","*Temporary cessation of breathing","Deep breathing"],"A- = without, -pnea = breathing."),
     ("Sleep apnea is:",["Normal sleep","*Repeated episodes of breathing cessation during sleep (obstructive or central)","Insomnia","A heart problem"],"Obstructive: airway collapse; Central: brain signal failure."),
     ("Cheyne-Stokes respiration is:",["Normal breathing","*An abnormal pattern: crescendo-decrescendo breathing alternating with apnea","Fast breathing","Slow breathing"],"Seen in heart failure, brain injury."),
     ("Respiratory acidosis results from:",["Hyperventilation","*Hypoventilation (CO₂ retention → ↓pH)","Low CO₂","High O₂"],"CO₂ retention = acid accumulation."),
     ("Respiratory alkalosis results from:",["Hypoventilation","*Hyperventilation (excess CO₂ loss → ↑pH)","High CO₂","Low O₂"],"Blowing off CO₂ = pH rises."),
     ("Mechanical ventilation in ICU:",["Is simple","*Assists or replaces breathing; settings must match the patient's physiology","Is never used","Only provides O₂"],"Life-saving for respiratory failure."),
     ("Understanding breathing regulation is essential for:",["Nothing","*Managing respiratory failure, COPD, sleep apnea, acid-base disorders, and critical care","Only anatomy","Only researchers"],"Core to pulmonary and emergency medicine.")]
)
lessons[k]=v

# 7.6
k,v = build_lesson(7,6,"Disorders of the Respiratory System",
    "<h3>Disorders of the Respiratory System</h3>"
    "<ul><li><b>Asthma:</b> Chronic airway inflammation with reversible bronchospasm → wheezing, dyspnea. Treated with bronchodilators and inhaled corticosteroids.</li>"
    "<li><b>COPD:</b> Chronic bronchitis (excess mucus) + emphysema (alveolar destruction). Mostly from smoking. Irreversible airflow limitation.</li>"
    "<li><b>Pneumonia:</b> Infection (bacterial, viral, fungal) filling alveoli with fluid/pus → impaired gas exchange.</li>"
    "<li><b>Tuberculosis (TB):</b> Mycobacterium tuberculosis; granuloma formation.</li>"
    "<li><b>Lung cancer:</b> Leading cancer killer; strong association with smoking.</li></ul>",
    [("Asthma","Chronic inflammatory airway disease with reversible bronchospasm; wheezing, dyspnea."),
     ("COPD","Chronic Obstructive Pulmonary Disease; chronic bronchitis + emphysema; usually from smoking."),
     ("Pneumonia","Lung infection causing alveolar fluid/pus accumulation → impaired gas exchange."),
     ("Emphysema","Destruction of alveolar walls reducing surface area; irreversible; component of COPD."),
     ("Pulmonary Embolism","Blood clot (usually from DVT) blocking a pulmonary artery; life-threatening.")],
    [("Asthma is characterized by:",["Permanent airway narrowing","*Reversible airway inflammation and bronchospasm","Alveolar destruction","Lung fibrosis"],"Key feature: reversibility."),
     ("The primary treatment for asthma includes:",["Antibiotics","*Inhaled bronchodilators (e.g., albuterol) and corticosteroids","Surgery","Only oxygen"],"Bronchodilators for acute relief; steroids for control."),
     ("COPD is most commonly caused by:",["Genetics alone","*Chronic cigarette smoking","Allergies","Infection"],"Smoking is the #1 cause."),
     ("Emphysema involves:",["Excess mucus","*Destruction of alveolar walls → reduced surface area for gas exchange","Fluid in alveoli","Bronchospasm"],"Irreversible alveolar damage."),
     ("Chronic bronchitis involves:",["Alveolar destruction","*Chronic inflammation with excess mucus production in bronchi","Fibrosis","Pleural effusion"],"Productive cough most days for ≥3 months in 2 consecutive years."),
     ("Pneumonia is caused by:",["Only bacteria","*Bacteria, viruses, or fungi infecting the lung parenchyma","Allergies","Smoking"],"Multiple infectious agents."),
     ("In pneumonia, gas exchange is impaired because:",["Airways constrict","*Alveoli fill with fluid and inflammatory exudate","Surface area decreases permanently","Blood flow stops"],"Fluid blocks O₂/CO₂ diffusion."),
     ("Tuberculosis (TB) is caused by:",["A virus","*Mycobacterium tuberculosis (bacterial)","A fungus","A parasite"],"Acid-fast bacillus."),
     ("A pulmonary embolism most often originates from:",["The lungs","The brain","*Deep vein thrombosis (DVT) in the legs","The heart"],"Clot breaks free → travels to pulmonary artery."),
     ("Symptoms of a PE include:",["No symptoms","*Sudden dyspnea, chest pain, tachycardia, possible hemoptysis","Only cough","Only fever"],"PE can be rapidly fatal."),
     ("Lung cancer is strongly associated with:",["Exercise","*Cigarette smoking (but also occurs in non-smokers)","Healthy diet","Cold weather"],"Smoking = #1 risk factor."),
     ("ARDS (Acute Respiratory Distress Syndrome) involves:",["Mild inflammation","*Severe, diffuse lung inflammation → bilateral pulmonary edema → respiratory failure","Slow onset","Only in smokers"],"Life-threatening; requires ICU care."),
     ("Cystic fibrosis is:",["Infectious","*A genetic disorder causing thick mucus in lungs and other organs","An allergy","Caused by smoking"],"CFTR gene mutation."),
     ("Pleural effusion is:",["Air in pleural space","*Excess fluid in the pleural space","A lung infection","An airway obstruction"],"Can compress lung tissue."),
     ("A chest X-ray is valuable for diagnosing:",["Heart disease only","*Pneumonia, TB, pleural effusion, pneumothorax, lung masses","Only fractures","Only heart size"],"First-line imaging for lung disease."),
     ("Pulse oximetry below _____ generally indicates concerning hypoxemia.",["99%","97%","*90%","80%"],"SpO₂ < 90% ≈ PaO₂ < 60 mmHg."),
     ("Smoking cessation:",["Has no benefit after starting","*Is the single most important intervention for preventing respiratory disease","Only helps young people","Doesn't reduce cancer risk"],"Benefits at any age."),
     ("Influenza can lead to respiratory complications including:",["Only fatigue","*Viral pneumonia, secondary bacterial pneumonia, and ARDS in severe cases","Only runny nose","No respiratory complications"],"Flu can be fatal, especially in vulnerable populations."),
     ("COVID-19 can cause:",["No lung involvement","*Pneumonia, ARDS, and long-term respiratory impairment in some patients","Only cold symptoms","Only sore throat"],"SARS-CoV-2 primarily targets the respiratory system."),
     ("Understanding respiratory disorders is essential because:",["They are rare","*They are among the leading causes of morbidity and mortality worldwide","Only for pulmonologists","Only in hospitals"],"Respiratory disease = massive global burden.")]
)
lessons[k]=v

# 7.7
k,v = build_lesson(7,7,"Case Studies in Pulmonology",
    "<h3>Case Studies in Pulmonology</h3>"
    "<h4>Case 1: Acute Asthma Exacerbation</h4>"
    "<p>A 22-year-old with wheezing, dyspnea, and prolonged expiratory phase after allergen exposure. Peak flow 50% of predicted. Treatment: nebulized albuterol + systemic corticosteroids. Improvement within hours.</p>"
    "<h4>Case 2: Community-Acquired Pneumonia</h4>"
    "<p>A 68-year-old with fever, productive cough (rusty sputum), dyspnea. CXR: right lower lobe consolidation. WBC elevated. Treatment: antibiotics (empiric then targeted).</p>"
    "<h4>Case 3: COPD Exacerbation</h4>"
    "<p>A 65-year-old smoker with worsening dyspnea, increased sputum, and hypoxemia. ABG: PaO₂ 55, PaCO₂ 60 (respiratory acidosis). Treatment: controlled O₂, bronchodilators, antibiotics, systemic steroids.</p>",
    [("Peak Flow","Measures maximum airflow during forced exhalation; reduced in asthma/COPD."),
     ("Consolidation","Solid-appearing area on CXR where alveoli are filled with fluid/pus (e.g., pneumonia)."),
     ("Rusty Sputum","Blood-tinged sputum characteristic of Streptococcus pneumoniae pneumonia."),
     ("Controlled Oxygen","In COPD, O₂ is given at low flow to avoid suppressing the hypoxic drive."),
     ("Respiratory Acidosis","pH < 7.35 with PaCO₂ > 45 mmHg; caused by hypoventilation/CO₂ retention.")],
    [("In acute asthma, the primary treatment is:",["Antibiotics","*Inhaled bronchodilators (albuterol) and systemic corticosteroids","Surgery","Only oxygen"],"Open airways + reduce inflammation."),
     ("Peak flow in the asthma case at 50% predicted indicates:",["Normal function","*Moderate-to-severe obstruction","Mild disease","No obstruction"],"<50% = significant airflow limitation."),
     ("Rusty sputum in the pneumonia case suggests:",["Viral infection","*Streptococcus pneumoniae (pneumococcal pneumonia)","Normal mucus","Tuberculosis"],"Classic finding."),
     ("Right lower lobe consolidation on CXR means:",["Normal lung","*Fluid/pus filling alveoli in that lobe (pneumonia)","A collapsed lung","A tumor"],"Consolidated = solidified lung tissue."),
     ("In the COPD case, PaCO₂ of 60 mmHg indicates:",["Normal","*Hypercapnia (CO₂ retention) — respiratory acidosis","Hypocapnia","Alkalosis"],"Normal is 35-45; 60 = significantly elevated."),
     ("Controlled O₂ in COPD means:",["High-flow O₂","*Low-flow O₂ (target SpO₂ 88-92%) to avoid suppressing the hypoxic drive","No oxygen","Only room air"],"Too much O₂ can reduce respiratory drive in COPD."),
     ("ABG showing pH <7.35 and PaCO₂ >45 is:",["Metabolic acidosis","*Respiratory acidosis","Respiratory alkalosis","Metabolic alkalosis"],"CO₂ retention → acid accumulation."),
     ("Empiric antibiotic therapy means:",["Waiting for culture results","*Starting antibiotics based on most likely pathogens before culture results are available","No antibiotics","Only IV fluids"],"Treat now, adjust later with culture data."),
     ("Asthma is classified as _____ lung disease.",["Restrictive","*Obstructive (difficulty exhaling due to airway narrowing)","Mixed","Neither"],"Obstructive = increased airway resistance."),
     ("COPD is classified as _____ lung disease.",["Restrictive","*Obstructive (irreversible airflow limitation)","Neither","Only restrictive"],"Chronic, progressive obstruction."),
     ("Pulmonary fibrosis is classified as _____ lung disease.",["Obstructive","*Restrictive (stiff lungs, difficulty expanding)","Neither","Only obstructive"],"Restrictive = reduced compliance."),
     ("Spirometry in obstructive disease shows:",["Normal FEV₁/FVC","*Reduced FEV₁/FVC ratio (<70%)","Increased FVC","Normal everything"],"Can't exhale quickly."),
     ("Spirometry in restrictive disease shows:",["Reduced FEV₁/FVC","*Reduced FVC with normal or increased FEV₁/FVC ratio","Increased total lung capacity","No abnormalities"],"Can't expand fully but can empty quickly."),
     ("The asthma case demonstrates the importance of:",["Ignoring symptoms","*Identifying triggers, having an action plan, and seeking early treatment","Only using medications","Not exercising"],"Prevention + early intervention."),
     ("In pneumonia, sputum culture helps determine:",["Nothing","*The specific pathogen and antibiotic sensitivity","Blood type","Lung capacity"],"Guides targeted antibiotic therapy."),
     ("A COPD exacerbation is often triggered by:",["Exercise","*Respiratory infections or environmental irritants","Eating","Sleeping"],"Infection = most common trigger."),
     ("These case studies show that respiratory emergencies:",["Are simple","*Require rapid assessment (history, exam, labs, imaging) and targeted treatment","Always self-resolve","Only need rest"],"Time-sensitive clinical decisions."),
     ("Long-term management of COPD includes:",["Only acute treatment","*Smoking cessation, inhaled bronchodilators/steroids, pulmonary rehabilitation, flu/pneumonia vaccines","Nothing","Only surgery"],"Comprehensive long-term plan."),
     ("Vaccinations prevent respiratory disease by:",["Nothing","*Reducing the risk of influenza and pneumococcal pneumonia (especially in high-risk groups)","Curing asthma","Reversing COPD"],"Prevention is key."),
     ("Clinical reasoning in pulmonology integrates:",["One skill only","*History, physical exam, spirometry, ABG, imaging, and microbiology for accurate diagnosis","Only CXR","Only ABG"],"Multiple data sources for the best clinical decisions.")]
)
lessons[k]=v

# 7.8
k,v = build_lesson(7,8,"AP Prep: Respiratory Physiology",
    "<h3>AP Prep: Respiratory Physiology</h3>"
    "<h4>Key Topics for Exam</h4>"
    "<ul><li>Breathing mechanics: Boyle's law, diaphragm, intrapulmonary vs. intrapleural pressure.</li>"
    "<li>Gas laws: Dalton's (partial pressures), Henry's (gas solubility).</li>"
    "<li>O₂ transport: Hb saturation curve, Bohr effect, factors shifting curve.</li>"
    "<li>CO₂ transport: bicarbonate, carbaminohemoglobin, dissolved.</li>"
    "<li>Regulation: chemoreceptors (central vs. peripheral), respiratory centers.</li>"
    "<li>Acid-base: respiratory acidosis/alkalosis, compensation.</li></ul>",
    [("Boyle's Law","P₁V₁ = P₂V₂; as volume increases, pressure decreases (and vice versa)."),
     ("Dalton's Law","Total pressure of a gas mixture = sum of each gas's partial pressure."),
     ("Henry's Law","Amount of gas dissolved in liquid is proportional to its partial pressure."),
     ("Respiratory Acidosis","pH < 7.35, PaCO₂ > 45 mmHg; caused by hypoventilation."),
     ("Respiratory Alkalosis","pH > 7.45, PaCO₂ < 35 mmHg; caused by hyperventilation.")],
    [("Boyle's law explains breathing because:",["Gases are hot","*As thoracic volume increases (inspiration), pressure decreases, drawing air in","Pressure stays constant","Volume doesn't change"],"Volume-pressure relationship drives ventilation."),
     ("Intrapleural pressure is normally:",["Positive","Zero","*Negative (subatmospheric) — keeps lungs expanded","Equal to intrapulmonary"],"Negative pressure prevents lung collapse."),
     ("If intrapleural pressure becomes equal to atmospheric (e.g., chest wound):",["Nothing happens","*The lung collapses (pneumothorax)","Breathing improves","Pressure normalizes"],"Loss of negative pressure = collapse."),
     ("Dalton's law is important because:",["Gases don't mix","*Individual gas partial pressures drive diffusion (each gas moves independently)","Total pressure is irrelevant","Only O₂ matters"],"Partial pressures determine gas exchange."),
     ("At sea level, atmospheric pressure is _____ mmHg.",["*760","650","860","500"],"Standard atmospheric pressure."),
     ("PO₂ of inspired air at sea level is approximately:",["760 mmHg","21 mmHg","*159 mmHg (21% of 760)","104 mmHg"],"21% of atmospheric pressure."),
     ("Henry's law explains why:",["*More gas dissolves in blood at higher partial pressures","Gases don't dissolve","Temperature doesn't matter","All gases dissolve equally"],"Solubility = f(PP, solubility coefficient)."),
     ("The oxygen-hemoglobin dissociation curve shows that Hb is _____ saturated at normal arterial PO₂ (~100 mmHg).",["50%","75%","*~97-99%","100%"],"Nearly fully saturated in the lungs."),
     ("At a PO₂ of ~40 mmHg (venous blood), Hb saturation is approximately:",["97%","90%","*75%","50%"],"Hb releases ~25% of its O₂ to tissues."),
     ("The P50 is the PO₂ at which Hb is _____ saturated.",["100%","75%","*50%","25%"],"Normal P50 ≈ 26.6 mmHg."),
     ("A right shift (increased P50) means the tissue gets:",["Less O₂","*More O₂ (Hb releases O₂ more readily)","No O₂","The same amount"],"Active tissues benefit from right shift."),
     ("Respiratory acidosis is compensated by the kidneys, which:",["Excrete HCO₃⁻","*Retain HCO₃⁻ and excrete H⁺ (renal compensation takes hours-days)","Excrete CO₂","Produce more acid"],"Kidneys balance pH by adjusting bicarbonate."),
     ("Respiratory alkalosis is compensated by the kidneys, which:",["Retain HCO₃⁻","*Excrete HCO₃⁻ and retain H⁺","Produce more CO₂","Excrete nothing"],"Kidneys lower bicarb to lower pH."),
     ("An ABG showing pH 7.30, PaCO₂ 55, HCO₃⁻ 24 indicates:",["Metabolic acidosis","*Uncompensated respiratory acidosis","Respiratory alkalosis","Normal"],"Low pH + high CO₂ + normal bicarb = uncompensated."),
     ("An ABG showing pH 7.48, PaCO₂ 28, HCO₃⁻ 24 indicates:",["Metabolic alkalosis","Respiratory acidosis","*Uncompensated respiratory alkalosis","Normal"],"High pH + low CO₂ + normal bicarb."),
     ("Oxygen therapy increases:",["CO₂","*Alveolar and arterial PO₂ → improved oxygenation","Acid production","Bicarbonate"],"Higher FiO₂ raises PaO₂."),
     ("Mechanical ventilation can correct respiratory acidosis by:",["Reducing O₂","*Increasing ventilation → blowing off excess CO₂","Adding bicarbonate","Reducing blood flow"],"Ventilator increases minute ventilation."),
     ("For the AP exam, students should be able to interpret:",["Only diagrams","*ABG values, spirometry results, and O₂-Hb curves in clinical scenarios","Only definitions","Only anatomy"],"Application and analysis required."),
     ("The relationship between ventilation and acid-base balance is:",["Unrelated","*Directly linked (ventilation adjusts CO₂ → adjusts pH)","Inverse","Only during exercise"],"Breathing is a rapid pH regulator."),
     ("Respiratory physiology integrates with:",["Nothing else","*Cardiovascular, renal, and metabolic systems for whole-body homeostasis","Only the nervous system","Only the immune system"],"No system works in isolation.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Anatomy Unit 7: wrote {len(lessons)} lessons")
