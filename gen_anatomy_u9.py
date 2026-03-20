#!/usr/bin/env python3
"""Anatomy Unit 9 – Urinary & Reproductive Systems (8 lessons)."""
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

# 9.1
k,v = build_lesson(9,1,"Anatomy of the Urinary System",
    "<h3>Anatomy of the Urinary System</h3>"
    "<h4>Components</h4>"
    "<ul><li><b>Kidneys (2):</b> Bean-shaped, retroperitoneal. Cortex (outer), medulla (inner pyramids), pelvis (collects urine).</li>"
    "<li><b>Ureters:</b> Transport urine from kidneys to bladder via peristalsis.</li>"
    "<li><b>Urinary Bladder:</b> Stores urine; detrusor muscle; trigone (triangle between two ureteral openings and internal urethral orifice).</li>"
    "<li><b>Urethra:</b> Carries urine from bladder to exterior. Female ~4 cm; male ~20 cm (passes through prostate).</li></ul>"
    "<h4>Nephron — Functional Unit</h4>"
    "<p>~1 million per kidney. Parts: glomerulus (Bowman's capsule), PCT, loop of Henle, DCT, collecting duct.</p>",
    [("Nephron","Functional unit of the kidney; filters blood and produces urine (~1 million per kidney)."),
     ("Glomerulus","Capillary tuft inside Bowman's capsule; site of blood filtration."),
     ("Renal Cortex","Outer region of the kidney containing glomeruli and convoluted tubules."),
     ("Renal Medulla","Inner region of the kidney containing loops of Henle and collecting ducts (pyramids)."),
     ("Detrusor Muscle","Smooth muscle of the urinary bladder wall; contracts during urination.")],
    [("The functional unit of the kidney is the:",["Glomerulus only","Collecting duct","*Nephron","Renal pelvis"],"Nephron = complete filtration and reabsorption unit."),
     ("Each kidney contains approximately:",["100 nephrons","10,000 nephrons","*1 million nephrons","10 million nephrons"],"~1 million per kidney."),
     ("The kidneys are located:",["In the peritoneal cavity","*Retroperitoneally (behind the peritoneum) in the posterior abdominal wall","In the pelvic cavity","In the thoracic cavity"],"Retroperitoneal position."),
     ("The renal cortex contains:",["Only blood vessels","*Glomeruli, proximal and distal convoluted tubules","Only collecting ducts","Renal pelvis"],"Cortex = outer filtering structures."),
     ("The renal medulla contains:",["Glomeruli","*Loops of Henle, collecting ducts, and vasa recta (arranged in pyramids)","Only the pelvis","PCT and DCT"],"Medulla = concentration gradient region."),
     ("The renal pelvis:",["Filters blood","*Collects urine from the collecting ducts and funnels it to the ureter","Produces hormones","Contains glomeruli"],"Funnel that drains the kidney."),
     ("Ureters transport urine via:",["Gravity only","*Peristalsis (smooth muscle contractions)","Voluntary control","Cilia"],"Active transport of urine."),
     ("The trigone of the bladder is:",["A muscle","*A triangular area formed by the two ureteral openings and the internal urethral orifice","A nerve plexus","The bladder neck"],"Clinically significant; common site of infection."),
     ("The female urethra is approximately:",["20 cm","*4 cm","10 cm","1 cm"],"Shorter → higher UTI risk in females."),
     ("The male urethra passes through the:",["Uterus","*Prostate gland (prostatic urethra)","Kidneys","Ovaries"],"Prostatic enlargement can obstruct urine flow."),
     ("Bowman's capsule:",["Produces urine","*Surrounds the glomerular capillaries and collects filtrate","Reabsorbs all water","Is in the medulla"],"First step of urine formation."),
     ("The proximal convoluted tubule (PCT):",["Does nothing","*Reabsorbs ~65% of filtered water, glucose, amino acids, and Na⁺","Only secretes waste","Concentrates urine"],"Primary reabsorption site."),
     ("The loop of Henle creates a:",["Uniform concentration","*Concentration gradient in the medulla (countercurrent multiplier)","Dilute cortex","Acid environment"],"Essential for concentrating urine."),
     ("The distal convoluted tubule (DCT):",["Is not regulated","*Is regulated by aldosterone (Na⁺ reabsorption) and PTH (Ca²⁺ reabsorption)","Only excretes K⁺","Only reabsorbs water"],"Fine-tuning of electrolytes."),
     ("The collecting duct is regulated by:",["Gastrin","*ADH (antidiuretic hormone) — controls water reabsorption","Insulin","Cortisol"],"ADH → aquaporins → water retention."),
     ("The juxtaglomerular apparatus (JGA):",["Produces urine","*Monitors blood pressure and NaCl; releases renin to activate the RAAS","Is only structural","Is in the bladder"],"Critical for BP regulation."),
     ("Afferent arterioles:",["Carry filtered blood away","*Bring blood TO the glomerulus","Carry urine","Are veins"],"Afferent = arriving."),
     ("Efferent arterioles:",["Bring blood to the glomerulus","*Carry blood AWAY from the glomerulus (to peritubular capillaries)","Are veins","Carry urine"],"Efferent = exiting."),
     ("The kidneys also produce:",["Only urine","*Erythropoietin (EPO), renin, and active vitamin D (calcitriol)","Only renin","Only hormones"],"Endocrine functions of the kidney."),
     ("Understanding urinary anatomy is essential for diagnosing:",["Only kidney stones","*UTIs, kidney stones, renal failure, and urinary obstruction","Only bladder cancer","Only infections"],"Common urinary conditions.")]
)
lessons[k]=v

# 9.2
k,v = build_lesson(9,2,"Kidney Function & Filtration",
    "<h3>Kidney Function &amp; Filtration</h3>"
    "<h4>Three Processes of Urine Formation</h4>"
    "<ul><li><b>Glomerular filtration:</b> Passive, pressure-driven. GFR ~125 mL/min = ~180 L/day. Filters water, ions, glucose, amino acids, urea; retains proteins and cells.</li>"
    "<li><b>Tubular reabsorption:</b> PCT (65% of filtrate), loop of Henle (water & ions), DCT & collecting duct (hormone-regulated). >99% of filtrate reabsorbed.</li>"
    "<li><b>Tubular secretion:</b> H⁺, K⁺, drugs, toxins secreted from blood into tubular fluid.</li></ul>"
    "<h4>RAAS</h4>"
    "<p>Low BP → renin → angiotensinogen → angiotensin I → (ACE) → angiotensin II → vasoconstriction + aldosterone → Na⁺/H₂O retention → BP ↑.</p>",
    [("GFR (Glomerular Filtration Rate)","Volume of filtrate formed per minute (~125 mL/min); key measure of kidney function."),
     ("Tubular Reabsorption","Process of moving useful substances (glucose, water, ions) from tubular filtrate back to blood."),
     ("Tubular Secretion","Process of moving substances (H⁺, K⁺, drugs) from blood into tubular fluid for excretion."),
     ("RAAS","Renin-Angiotensin-Aldosterone System; regulates blood pressure and fluid balance."),
     ("ADH (Antidiuretic Hormone)","Released from posterior pituitary; increases water reabsorption in collecting ducts.")],
    [("The GFR is approximately:",["10 mL/min","*125 mL/min (~180 L/day)","500 mL/min","1 L/min"],"Most is reabsorbed; ~1-2 L urine/day."),
     ("Glomerular filtration is driven by:",["Active transport","*Hydrostatic blood pressure (passive, pressure-driven)","Osmosis only","Hormones only"],"Net filtration pressure."),
     ("The filtrate initially contains:",["Only urea","*Water, ions, glucose, amino acids, urea — NOT proteins or blood cells","Proteins and cells","Only water"],"Glomerular filter retains large molecules."),
     ("The PCT reabsorbs approximately _____ of the filtrate.",["10%","25%","*65%","99%"],"Most reabsorption occurs here."),
     ("More than _____ of the filtrate is reabsorbed back into the blood.",["50%","75%","90%","*99%"],"Only 1-2 L becomes urine."),
     ("Glucose is normally completely reabsorbed in the:",["Loop of Henle","DCT","*PCT (via SGLT transporters)","Collecting duct"],"All glucose reabsorbed unless blood glucose is very high (diabetes)."),
     ("In uncontrolled diabetes, glucose appears in urine because:",["The kidneys fail","*Blood glucose exceeds the renal threshold; transporters are saturated","Glucose is toxic","The PCT is missing"],"Glucosuria = glucose in urine."),
     ("The descending limb of the loop of Henle is permeable to:",["Na⁺ only","*Water (but NOT NaCl)","Both water and NaCl equally","Nothing"],"Water leaves → filtrate concentrates."),
     ("The ascending limb of the loop of Henle:",["Reabsorbs water","*Actively pumps out NaCl but is impermeable to water","Does nothing","Secretes urea"],"Dilutes the filtrate; concentrates the medulla."),
     ("Aldosterone acts on the DCT and collecting duct to:",["Excrete Na⁺","*Reabsorb Na⁺ (and water follows) and secrete K⁺","Block ADH","Produce renin"],"Aldosterone = sodium retention."),
     ("ADH increases water reabsorption by:",["Opening Na⁺ channels","*Inserting aquaporin channels in the collecting duct","Increasing GFR","Constricting arterioles"],"ADH = water retention → concentrated urine."),
     ("Renin is released when:",["Blood pressure is high","*Blood pressure (or NaCl) is low → activates RAAS","Urine is dilute","Glucose is high"],"JGA detects low perfusion."),
     ("ACE (angiotensin-converting enzyme) converts:",["Renin to angiotensin","*Angiotensin I to angiotensin II (in the lungs)","Aldosterone to cortisol","ADH to oxytocin"],"ACE inhibitors are used to treat hypertension."),
     ("Angiotensin II causes:",["Vasodilation","*Vasoconstriction + aldosterone release + ADH release → ↑ BP","Decreased BP","Diuresis"],"Powerful vasoconstrictor."),
     ("ANP (atrial natriuretic peptide) opposes RAAS by:",["Increasing renin","*Promoting Na⁺ and water excretion → ↓ blood volume and BP","Constricting blood vessels","Nothing"],"ANP = natural diuretic."),
     ("Creatinine clearance is used to estimate:",["Liver function","*GFR (kidney function)","Heart function","Lung function"],"Clinical measure of kidney filtration."),
     ("A normal urine output is approximately:",["100 mL/day","*1-2 L/day","10 L/day","50 mL/day"],"About 1% of filtrate becomes urine."),
     ("Oliguria means:",["Excess urine","*Abnormally low urine output (<400 mL/day)","Normal urine","No urine"],"Sign of kidney dysfunction or dehydration."),
     ("Diuretics treat hypertension by:",["Increasing blood volume","*Promoting urine output → reducing blood volume → lowering BP","Blocking aldosterone only","Constricting arteries"],"Various classes target different nephron segments."),
     ("Understanding kidney function is critical for:",["Only nephrologists","*Managing hypertension, diabetes, kidney disease, electrolyte disorders, and drug dosing","Only urologists","Nothing"],"Kidneys affect nearly every organ system.")]
)
lessons[k]=v

# 9.3
k,v = build_lesson(9,3,"Fluid & Electrolyte Balance",
    "<h3>Fluid &amp; Electrolyte Balance</h3>"
    "<h4>Body Fluid Compartments</h4>"
    "<p>Total body water ~60% of body weight. ICF (intracellular fluid) ~2/3; ECF (extracellular fluid) ~1/3 (plasma + interstitial).</p>"
    "<h4>Key Electrolytes</h4>"
    "<ul><li><b>Na⁺:</b> Major ECF cation; regulates osmolarity and fluid volume.</li>"
    "<li><b>K⁺:</b> Major ICF cation; essential for membrane potential, cardiac function.</li>"
    "<li><b>Ca²⁺:</b> Muscle contraction, nerve signaling, clotting, bone.</li>"
    "<li><b>Acid-base:</b> pH 7.35–7.45. Buffers (bicarbonate), lungs (CO₂), kidneys (H⁺/HCO₃⁻).</li></ul>",
    [("ICF","Intracellular fluid; ~2/3 of total body water; K⁺ is the major cation."),
     ("ECF","Extracellular fluid (~1/3 of TBW); includes plasma and interstitial fluid; Na⁺ is the major cation."),
     ("Hypernatremia","Abnormally high blood sodium; usually from water deficit → dehydration."),
     ("Hypokalemia","Low blood potassium; can cause dangerous cardiac arrhythmias."),
     ("Metabolic Acidosis","Arterial pH < 7.35 due to HCO₃⁻ loss or acid gain; kidneys excrete H⁺, retain HCO₃⁻.")],
    [("Total body water is approximately _____ of body weight.",["40%","50%","*60%","80%"],"The '60% rule.'"),
     ("The intracellular fluid (ICF) compartment holds about:",["1/3 of TBW","*2/3 of TBW","1/2 of TBW","All of TBW"],"Most water is inside cells."),
     ("The major cation of the ECF is:",["K⁺","Ca²⁺","*Na⁺","Mg²⁺"],"Na⁺ drives ECF volume."),
     ("The major cation of the ICF is:",["Na⁺","*K⁺","Ca²⁺","Cl⁻"],"K⁺ is primary intracellular cation."),
     ("Hypernatremia most commonly results from:",["Too much Na⁺ intake","*Water deficit (dehydration)","Low aldosterone","Excess ADH"],"Concentrated Na⁺ from water loss."),
     ("Hyponatremia can be caused by:",["Dehydration only","*Excess water intake, SIADH, or Na⁺ loss","Too much salt","High aldosterone only"],"Dilution or depletion."),
     ("Hypokalemia is dangerous because it can cause:",["Only fatigue","*Cardiac arrhythmias (ventricular fibrillation), muscle weakness","Only cramps","No problems"],"K⁺ critical for cardiac conduction."),
     ("Hyperkalemia is dangerous because:",["It causes nothing","*It can cause fatal cardiac arrhythmias (tall T waves on ECG, cardiac arrest)","It only causes muscle pain","It causes dehydration"],"Emergency if K⁺ > 6.0 mEq/L."),
     ("Calcium is important for:",["Only bones","*Muscle contraction, nerve signaling, blood clotting, and bone structure","Only teeth","Only clotting"],"Multi-system roles."),
     ("Hypocalcemia can cause:",["High blood pressure","*Tetany (muscle spasms), numbness, Trousseau's and Chvostek's signs","Weight gain","No symptoms"],"Excitable nerves and muscles."),
     ("Normal blood pH is:",["7.0","7.2","*7.35–7.45","7.8"],"Narrow range; deviations are life-threatening."),
     ("The bicarbonate buffer system:",["Is irrelevant","*H₂CO₃ ⇌ H⁺ + HCO₃⁻; most important ECF buffer","Only works in the lungs","Only works in kidneys"],"Immediate buffer."),
     ("The lungs regulate pH by:",["Retaining H⁺","*Adjusting CO₂ exhalation (hyperventilation → ↓CO₂ → ↑pH)","Producing bicarbonate","Absorbing acid"],"Respiratory compensation."),
     ("The kidneys regulate pH by:",["Adjusting CO₂","*Excreting H⁺ and reabsorbing/generating HCO₃⁻","Only filtering waste","Only making urine"],"Metabolic compensation (slower but more complete)."),
     ("Metabolic acidosis (pH < 7.35) can result from:",["Hyperventilation","*Diabetic ketoacidosis, renal failure, or severe diarrhea (loss of HCO₃⁻)","Vomiting","Anxiety"],"Acid accumulation or bicarb loss."),
     ("Respiratory acidosis results from:",["Excess HCO₃⁻","*Hypoventilation → CO₂ retention → ↓ pH","Diarrhea","Vomiting"],"CO₂ + H₂O → carbonic acid."),
     ("Metabolic alkalosis can result from:",["Diarrhea","*Prolonged vomiting (loss of HCl) or excess antacids","Hypoventilation","Renal failure"],"Loss of acid."),
     ("Edema (fluid accumulation in tissues) can result from:",["Dehydration","*Low albumin (decreased oncotic pressure), heart failure, or lymphatic obstruction","High BP only","Excess exercise"],"Multiple causes of fluid shift."),
     ("IV fluid therapy (e.g., normal saline, lactated Ringer's) is used to:",["Replace food","*Restore fluid volume, correct electrolyte imbalances, and maintain hydration","Only deliver drugs","Only during surgery"],"Critical in many clinical scenarios."),
     ("Understanding fluid and electrolyte balance is essential for:",["Only anesthesiologists","*Managing dehydration, shock, heart failure, kidney disease, and nearly all medical conditions","Only surgeons","Only nephrologists"],"Foundational to all medicine.")]
)
lessons[k]=v

# 9.4
k,v = build_lesson(9,4,"Male Reproductive System",
    "<h3>Male Reproductive System</h3>"
    "<h4>Anatomy</h4>"
    "<ul><li><b>Testes:</b> Produce sperm (seminiferous tubules) and testosterone (Leydig cells). Located in scrotum (cooler temperature).</li>"
    "<li><b>Epididymis:</b> Sperm maturation and storage.</li>"
    "<li><b>Vas deferens → ejaculatory duct → urethra:</b> Sperm transport pathway.</li>"
    "<li><b>Accessory glands:</b> Seminal vesicles (fructose, prostaglandins), prostate (alkaline fluid), bulbourethral glands (pre-ejaculate).</li></ul>"
    "<h4>Spermatogenesis</h4>"
    "<p>Spermatogonia (2n) → primary spermatocyte → meiosis I → secondary → meiosis II → spermatids → spermatozoa. ~74 days. FSH + testosterone drive the process.</p>",
    [("Spermatogenesis","Formation of sperm from spermatogonia through meiosis; occurs in seminiferous tubules (~74 days)."),
     ("Leydig Cells","Interstitial cells that produce testosterone in response to LH."),
     ("Sertoli Cells","'Nurse cells' in seminiferous tubules; support, nourish, and protect developing sperm; form blood-testis barrier."),
     ("Testosterone","Primary male sex hormone; produced by Leydig cells; drives secondary sex characteristics, spermatogenesis, and libido."),
     ("Vas Deferens","Muscular duct that transports sperm from the epididymis to the ejaculatory duct.")],
    [("Sperm are produced in the:",["Prostate","Epididymis","*Seminiferous tubules of the testes","Vas deferens"],"Seminiferous tubules = sperm factory."),
     ("Leydig (interstitial) cells produce:",["Sperm","*Testosterone (in response to LH)","Estrogen","FSH"],"Endocrine function of the testis."),
     ("Sertoli cells:",["Produce testosterone","*Support, nourish, and protect developing sperm; form the blood-testis barrier","Are found in the epididymis","Produce semen"],"Nurse cells of the testis."),
     ("The scrotum keeps the testes at a temperature that is:",["Higher than body temp","*Slightly lower than core body temperature (~2–3°C below)","The same as body temp","Much colder"],"Optimal for spermatogenesis."),
     ("Spermatogenesis takes approximately:",["7 days","*74 days (about 2.5 months)","1 month","1 year"],"Continuous process from puberty onward."),
     ("During spermatogenesis, meiosis produces:",["Diploid cells","*Haploid (n) spermatids from diploid (2n) spermatogonia","Tetraploid cells","Identical cells"],"Meiosis halves chromosome number."),
     ("FSH stimulates:",["Testosterone production","*Sertoli cells to support spermatogenesis","Leydig cells","Prostate growth"],"FSH acts on Sertoli cells."),
     ("LH stimulates:",["Sertoli cells","*Leydig cells to produce testosterone","Sperm maturation","Prostate secretion"],"LH acts on Leydig cells."),
     ("Sperm mature and are stored in the:",["Seminiferous tubules","*Epididymis","Prostate","Seminal vesicles"],"Epididymis = maturation + storage."),
     ("The vas deferens connects the:",["Testis to scrotum","*Epididymis to the ejaculatory duct","Bladder to urethra","Kidney to bladder"],"Sperm transport duct."),
     ("A vasectomy involves:",["Removing the testes","*Cutting and sealing the vas deferens (male sterilization)","Removing the prostate","Blocking the urethra"],"Prevents sperm from reaching semen."),
     ("The seminal vesicles contribute:",["Sperm","*~60-70% of semen volume (fructose for energy, prostaglandins)","Only water","Testosterone"],"Fructose = sperm fuel."),
     ("The prostate gland produces:",["Sperm","*Alkaline fluid (neutralizes vaginal acidity, contains enzymes)","Testosterone","Fructose"],"Protects sperm in the vaginal environment."),
     ("Benign prostatic hyperplasia (BPH):",["Is cancer","*Is non-cancerous prostate enlargement — common in older men → urinary obstruction","Is rare","Affects only young men"],"Very common age-related condition."),
     ("Prostate cancer is:",["Rare","*One of the most common cancers in men; screened with PSA test","Only in elderly","Always fatal"],"Early detection improves outcomes."),
     ("Testosterone drives:",["Only muscle growth","*Secondary sex characteristics (facial hair, deep voice, muscle mass), spermatogenesis, and libido","Only sperm production","Only bone growth"],"Wide-ranging androgenic effects."),
     ("Erectile dysfunction (ED) can be caused by:",["Only aging","*Vascular disease, diabetes, neurological disorders, medications, or psychological factors","Only stress","Only low testosterone"],"Multifactorial etiology."),
     ("Inhibin from Sertoli cells:",["Stimulates FSH","*Inhibits FSH release (negative feedback to the pituitary)","Stimulates LH","Produces sperm"],"Negative feedback regulation."),
     ("Cryptorchidism is:",["Normal","*Undescended testis (failure to descend into scrotum); increases cancer risk if untreated","A type of infection","A hormone disorder"],"Requires surgical correction (orchiopexy)."),
     ("Understanding male reproductive anatomy is essential for:",["Nothing","*Diagnosing infertility, BPH, prostate cancer, STIs, and hormonal disorders","Only urology","Only fertility specialists"],"Common clinical conditions.")]
)
lessons[k]=v

# 9.5
k,v = build_lesson(9,5,"Female Reproductive System",
    "<h3>Female Reproductive System</h3>"
    "<h4>Anatomy</h4>"
    "<ul><li><b>Ovaries:</b> Produce oocytes and hormones (estrogen, progesterone). Oogenesis begins prenatally.</li>"
    "<li><b>Uterine (fallopian) tubes:</b> Site of fertilization; fimbriae sweep oocyte in.</li>"
    "<li><b>Uterus:</b> Endometrium (inner lining, sheds during menstruation), myometrium (smooth muscle).</li>"
    "<li><b>Vagina:</b> Birth canal, receives penis.</li></ul>"
    "<h4>Menstrual Cycle (~28 days)</h4>"
    "<p>Follicular phase (FSH → follicle growth → estrogen ↑) → LH surge → ovulation → luteal phase (corpus luteum → progesterone ↑) → if no fertilization → corpus luteum degenerates → menstruation.</p>",
    [("Oogenesis","Formation of oocytes; begins prenatally, arrested at prophase I; resumes at puberty with each cycle."),
     ("Ovulation","Release of a secondary oocyte from the ovary at mid-cycle (~day 14), triggered by LH surge."),
     ("Corpus Luteum","Structure formed from the ruptured follicle post-ovulation; secretes progesterone and estrogen."),
     ("Endometrium","Inner lining of the uterus; thickens each cycle for implantation; sheds during menstruation."),
     ("Estrogen","Primary female hormone; promotes endometrial growth, secondary sex characteristics, and bone density.")],
    [("Oogenesis begins:",["At puberty","*Prenatally (before birth); arrested at prophase I until puberty","At menopause","At age 5"],"Females are born with all primary oocytes."),
     ("Fertilization typically occurs in the:",["Uterus","Ovary","*Uterine (fallopian) tube","Vagina"],"Sperm meets egg in the tube."),
     ("The fimbriae:",["Are in the uterus","*Are finger-like projections that sweep the released oocyte into the fallopian tube","Produce hormones","Are part of the ovary"],"Capture the oocyte at ovulation."),
     ("The endometrium:",["Never changes","*Thickens under estrogen/progesterone influence; sheds if implantation doesn't occur (menstruation)","Is muscle only","Is only vaginal tissue"],"Cyclical changes drive menstruation."),
     ("The myometrium is:",["Endometrial lining","*The thick smooth muscle layer of the uterus (contracts during labor)","The ovarian cortex","The cervix"],"Powerful contractions during delivery."),
     ("The follicular phase is dominated by:",["Progesterone","*FSH and estrogen (follicle growth and endometrial proliferation)","LH only","Testosterone"],"Days 1-14 approximately."),
     ("Ovulation is triggered by:",["Estrogen decline","*A surge in LH (and FSH) at mid-cycle","Progesterone","Low FSH"],"LH surge = ovulation trigger."),
     ("The corpus luteum secretes:",["Only estrogen","*Progesterone (primarily) and estrogen","FSH","LH"],"Maintains endometrium for implantation."),
     ("If fertilization does not occur:",["Progesterone rises","*The corpus luteum degenerates → progesterone drops → menstruation","Estrogen keeps rising","LH surges again"],"Corpus luteum → corpus albicans."),
     ("hCG (human chorionic gonadotropin) in early pregnancy:",["Causes menstruation","*Maintains the corpus luteum (preventing menstruation) until the placenta takes over","Is produced by the ovary","Triggers ovulation"],"hCG is the basis of pregnancy tests."),
     ("Estrogen promotes:",["Bone loss","*Endometrial growth, secondary sex characteristics (breast development), and bone density","Menstruation directly","Progesterone decline"],"Wide-ranging effects."),
     ("Progesterone's main role is to:",["Trigger ovulation","*Prepare and maintain the endometrium for implantation; maintain pregnancy","Cause menstruation","Stimulate follicle growth"],"Progesterone = pro-gestation."),
     ("Polycystic ovary syndrome (PCOS):",["Is rare","*Is a common hormonal disorder causing irregular cycles, excess androgens, and ovarian cysts","Only affects fertility","Is a type of cancer"],"Affects ~10% of women of reproductive age."),
     ("Endometriosis is:",["Normal tissue growth","*Growth of endometrial tissue outside the uterus → pain, infertility","A type of cancer","A bladder disease"],"Can implant on ovaries, tubes, peritoneum."),
     ("Cervical cancer screening (Pap smear) detects:",["Ovarian cancer","*Precancerous or cancerous cells on the cervix (often caused by HPV)","Uterine cancer","Endometriosis"],"Early detection saves lives."),
     ("Menopause is:",["A disease","*The permanent cessation of menstruation (average age ~51); ovarian function declines","Reversible","Caused by stress"],"Natural end of reproductive years."),
     ("Ectopic pregnancy occurs when:",["Implantation is in the uterus","*The embryo implants outside the uterus (most commonly in the fallopian tube)","The baby is large","Menstruation continues"],"Medical emergency if tube ruptures."),
     ("Oral contraceptives work primarily by:",["Killing sperm","*Suppressing ovulation (inhibiting FSH/LH surge via synthetic estrogen and progesterone)","Thickening endometrium","Destroying oocytes"],"Multiple mechanisms; ovulation suppression is primary."),
     ("IVF (in vitro fertilization) involves:",["Natural conception","*Fertilizing oocytes with sperm in a lab, then transferring embryos to the uterus","Only hormone therapy","Only surgery"],"Assisted reproductive technology."),
     ("Understanding female reproductive anatomy is essential for:",["Nothing","*Managing menstrual disorders, infertility, pregnancy, contraception, and gynecological cancers","Only OB/GYN","Only women"],"Fundamental to health care.")]
)
lessons[k]=v

# 9.6
k,v = build_lesson(9,6,"Hormonal Regulation of Reproduction",
    "<h3>Hormonal Regulation of Reproduction</h3>"
    "<h4>Hypothalamic-Pituitary-Gonadal (HPG) Axis</h4>"
    "<p>GnRH (hypothalamus) → FSH + LH (anterior pituitary) → Gonads (testes/ovaries) → sex hormones → negative feedback to hypothalamus/pituitary.</p>"
    "<h4>Males</h4>"
    "<p>GnRH → LH → testosterone (Leydig); GnRH → FSH → spermatogenesis (Sertoli). Testosterone + inhibin = negative feedback.</p>"
    "<h4>Females</h4>"
    "<p>GnRH → FSH → follicle growth → estrogen. Mid-cycle: estrogen surge → positive feedback → LH surge → ovulation. Luteal: progesterone → negative feedback.</p>",
    [("GnRH","Gonadotropin-releasing hormone from the hypothalamus; stimulates FSH and LH release."),
     ("FSH","Follicle-stimulating hormone; stimulates follicle growth (females) or spermatogenesis (males)."),
     ("LH","Luteinizing hormone; triggers ovulation (females) or testosterone production (males)."),
     ("HPG Axis","Hypothalamic-Pituitary-Gonadal axis; the hormonal control system for reproduction."),
     ("Positive Feedback (LH Surge)","High estrogen in the late follicular phase triggers a positive feedback loop → LH surge → ovulation.")],
    [("GnRH is released from the:",["Pituitary","*Hypothalamus","Ovary","Adrenal gland"],"Hypothalamic pulse generator."),
     ("GnRH stimulates the anterior pituitary to release:",["Estrogen and progesterone","*FSH and LH","ADH and oxytocin","Testosterone and inhibin"],"Gonadotropins."),
     ("In males, LH stimulates:",["Sertoli cells","*Leydig cells to produce testosterone","Sperm directly","FSH release"],"LH → Leydig → testosterone."),
     ("In males, FSH stimulates:",["Leydig cells","*Sertoli cells to support spermatogenesis","Testosterone production","LH release"],"FSH → Sertoli → sperm support."),
     ("Testosterone provides negative feedback to:",["Only the testes","*Both the hypothalamus and anterior pituitary (↓ GnRH, FSH, LH)","Only the ovaries","Only FSH"],"Negative feedback loop."),
     ("In females, FSH stimulates:",["Testosterone production","*Ovarian follicle growth and estrogen production","Ovulation directly","Progesterone production"],"Follicular phase hormone."),
     ("The LH surge is triggered by:",["Low estrogen","*High estrogen levels in the late follicular phase (positive feedback)","Progesterone","Low FSH"],"Unique positive feedback moment."),
     ("After ovulation, the corpus luteum produces:",["Only estrogen","*Progesterone (primarily) and estrogen","FSH","LH"],"Supports potential pregnancy."),
     ("If pregnancy occurs, _____ maintains the corpus luteum.",["LH","*hCG (human chorionic gonadotropin from the embryo)","FSH","Progesterone alone"],"hCG prevents corpus luteum degeneration."),
     ("The placenta eventually takes over hormone production around:",["Week 1","*Week 10-12 of pregnancy","Week 30","At birth"],"Progesterone and estrogen from placenta."),
     ("Oral contraceptives containing estrogen/progesterone work by:",["Enhancing ovulation","*Suppressing GnRH → ↓ FSH/LH → no ovulation","Increasing LH","Only thickening cervical mucus"],"Hormonal suppression of the HPG axis."),
     ("Clomiphene (fertility drug) works by:",["Suppressing ovulation","*Blocking estrogen receptors at the hypothalamus/pituitary → ↑ FSH/LH → stimulates ovulation","Producing testosterone","Inhibiting sperm"],"Tricks the brain into making more gonadotropins."),
     ("Inhibin from the testes/ovaries:",["Stimulates FSH","*Selectively inhibits FSH release from the anterior pituitary","Stimulates LH","Inhibits GnRH only"],"Fine-tuning of FSH."),
     ("GnRH is released in a _____ pattern.",["Continuous","*Pulsatile (intermittent pulses are essential for normal FSH/LH secretion)","Random","Only at night"],"Continuous GnRH actually suppresses gonadotropins."),
     ("Puberty is initiated by:",["High testosterone at birth","*Increased GnRH pulsatile secretion from the hypothalamus","Decreased body weight","Adrenal hormones only"],"HPG axis activation."),
     ("Precocious puberty is:",["Normal","*Abnormally early onset of puberty (before age 8 in girls, 9 in boys)","Late puberty","A type of infertility"],"Can be central (GnRH-dependent) or peripheral."),
     ("Hypogonadism refers to:",["Excess hormone production","*Underactive gonads → low sex hormones → delayed puberty, infertility","Normal function","Overactive pituitary"],"Can be primary (gonadal) or secondary (pituitary/hypothalamic)."),
     ("Testosterone replacement therapy may be used for:",["Women only","*Men with hypogonadism (low testosterone with symptoms)","Children routinely","Weight loss"],"Clinical indication for TRT."),
     ("The HPG axis has clinical relevance in:",["Nothing","*Infertility, contraception, puberty disorders, menopause, and hormonal cancers","Only research","Only endocrinology"],"Core reproductive endocrinology."),
     ("Understanding hormonal regulation is essential for:",["Only endocrinologists","*Managing reproductive health, fertility treatments, contraception, and hormonal disorders","Only pharmacists","Nothing"],"Fundamental to reproductive medicine.")]
)
lessons[k]=v

# 9.7
k,v = build_lesson(9,7,"Disorders of the Urinary & Reproductive Systems",
    "<h3>Disorders of the Urinary &amp; Reproductive Systems</h3>"
    "<h4>Urinary Disorders</h4>"
    "<ul><li><b>UTI:</b> Bacterial infection (often E. coli); more common in females (shorter urethra).</li>"
    "<li><b>Kidney stones (nephrolithiasis):</b> Calcium oxalate most common. Severe flank pain (renal colic).</li>"
    "<li><b>Acute kidney injury (AKI):</b> Sudden loss of function (prerenal, intrarenal, postrenal). Oliguria, ↑ creatinine/BUN.</li>"
    "<li><b>Chronic kidney disease (CKD):</b> Progressive loss of nephrons; stages 1-5; stage 5 = end-stage → dialysis or transplant.</li></ul>"
    "<h4>Reproductive Disorders</h4>"
    "<ul><li><b>STIs:</b> Chlamydia, gonorrhea, syphilis, HPV, HIV, herpes.</li>"
    "<li><b>Infertility:</b> ~15% of couples; multifactorial.</li></ul>",
    [("UTI","Urinary tract infection; bacterial (commonly E. coli); presents with dysuria, frequency, urgency."),
     ("Nephrolithiasis","Kidney stones; calcium oxalate most common; cause severe renal colic."),
     ("CKD","Chronic kidney disease; progressive nephron loss; Stage 5 (GFR <15) requires dialysis or transplant."),
     ("Dialysis","Treatment that filters blood when kidneys fail; hemodialysis or peritoneal dialysis."),
     ("STI","Sexually transmitted infection; includes chlamydia, gonorrhea, syphilis, HPV, HIV, herpes.")],
    [("The most common cause of UTIs is:",["Virus","Fungus","*E. coli (Escherichia coli)","Parasite"],"E. coli from GI tract ascends the urethra."),
     ("UTIs are more common in females because:",["They have weaker immunity","*The female urethra is shorter (~4 cm), allowing easier bacterial ascent","They drink less water","Their kidneys are smaller"],"Anatomical risk factor."),
     ("UTI symptoms include:",["Only fever","*Dysuria (painful urination), frequency, urgency, and sometimes hematuria","Only back pain","No symptoms"],"Classic triad: dysuria, frequency, urgency."),
     ("The most common type of kidney stone is:",["Uric acid","*Calcium oxalate","Struvite","Cystine"],"~80% are calcium-based."),
     ("Renal colic (kidney stone pain) is typically:",["Mild","*Severe, colicky flank pain that may radiate to the groin","Only in the back","Only during urination"],"One of the most severe pains known."),
     ("Prevention of kidney stones includes:",["Reduced water intake","*Adequate hydration, dietary modifications (reduce oxalate, moderate calcium)","Only medication","Surgery only"],"Hydration is the most important preventive measure."),
     ("AKI (acute kidney injury) is characterized by:",["Gradual onset","*Sudden decline in kidney function (↑ creatinine, ↑ BUN, ± oliguria)","Only dehydration","Only stones"],"Medical emergency."),
     ("CKD Stage 5 (GFR < 15 mL/min) is called:",["Mild kidney disease","*End-stage renal disease (ESRD) — requires dialysis or transplant","Stage 1","Acute kidney injury"],"Kidneys are failing."),
     ("Hemodialysis works by:",["Transplanting kidneys","*Filtering the patient's blood through an external dialyzer machine","Only removing water","Nothing"],"3× per week typically."),
     ("Glomerulonephritis is:",["A stone disease","*Inflammation of the glomeruli (can be caused by infections, autoimmunity)","A bladder infection","A reproductive disorder"],"Can be acute or chronic."),
     ("Chlamydia is:",["Always symptomatic","*The most common bacterial STI; often asymptomatic; can cause PID and infertility if untreated","A viral infection","Not treatable"],"Silent STI."),
     ("HPV (human papillomavirus) is significant because:",["It's harmless","*Certain strains cause cervical, oropharyngeal, and other cancers; vaccine available","It only causes warts","It's untreatable"],"HPV vaccine prevents cancer."),
     ("HIV attacks:",["Red blood cells","*CD4+ T-helper cells (weakening the immune system)","Liver cells","Neurons"],"Progressive immunodeficiency → AIDS."),
     ("Testicular torsion is:",["A mild condition","*A surgical emergency: twisting of the spermatic cord → ischemia → requires urgent surgery","Common and benign","Only in elderly men"],"Must be treated within hours to save the testis."),
     ("Polycystic kidney disease (PKD) is:",["An infection","*A genetic disorder causing multiple fluid-filled cysts in the kidneys → progressive renal failure","Caused by diet","Only in children"],"Autosomal dominant (most common genetic kidney disease)."),
     ("Urinary incontinence types include:",["Only one type","*Stress (sneezing/coughing), urge (overactive bladder), overflow, and functional","Only stress type","It's not a medical condition"],"Common and treatable."),
     ("Pyelonephritis is:",["A bladder infection","*A kidney infection (upper UTI); presents with fever, flank pain, and CVA tenderness","A stone disease","A liver disease"],"More serious than lower UTI."),
     ("Syphilis is caused by:",["A virus","*Treponema pallidum (a spirochete bacterium)","A fungus","A parasite"],"Treated with penicillin."),
     ("Infertility affects approximately _____ of couples.",["<1%","5%","*~15%","50%"],"Both male and female factors involved."),
     ("Understanding these disorders is critical because:",["They are rare","*Urinary and reproductive conditions are among the most common and impactful health issues globally","Only for specialists","They're not important"],"High prevalence and significant morbidity.")]
)
lessons[k]=v

# 9.8
k,v = build_lesson(9,8,"AP Prep: Renal Physiology",
    "<h3>AP Prep: Renal Physiology</h3>"
    "<h4>Exam Focus Areas</h4>"
    "<ul><li>Nephron structure and function (filtration, reabsorption, secretion).</li>"
    "<li>GFR regulation: myogenic mechanism, tubuloglomerular feedback, RAAS.</li>"
    "<li>Countercurrent multiplier and concentrating mechanism.</li>"
    "<li>Hormonal regulation: ADH, aldosterone, ANP, PTH.</li>"
    "<li>Acid-base balance: respiratory vs. metabolic; compensation.</li>"
    "<li>Urinalysis interpretation.</li></ul>",
    [("Countercurrent Multiplier","Loop of Henle mechanism creating a medullary concentration gradient for water reabsorption."),
     ("Myogenic Mechanism","Intrinsic renal autoregulation: afferent arteriole constricts when stretched by high BP to maintain constant GFR."),
     ("Tubuloglomerular Feedback","Macula densa senses NaCl in DCT; signals JGA to adjust afferent arteriole tone and renin release."),
     ("Clearance","Volume of plasma completely cleared of a substance per unit time; used to estimate GFR."),
     ("Urinalysis","Laboratory analysis of urine; screens for glucose, protein, blood, bacteria, pH, and specific gravity.")],
    [("The countercurrent multiplier operates in the:",["PCT","DCT","*Loop of Henle (descending and ascending limbs)","Collecting duct"],"Creates medullary osmotic gradient."),
     ("The descending limb of the loop of Henle is permeable to _____ but not _____.",["NaCl; water","*Water; NaCl (water leaves, concentrating the tubular fluid)","Both equally","Neither"],"Water exits → filtrate concentrates."),
     ("The thick ascending limb actively pumps out:",["Water","*NaCl (via the Na⁺/K⁺/2Cl⁻ cotransporter) — impermeable to water","Glucose","Protein"],"Creates dilute tubular fluid and hypertonic medulla."),
     ("Loop diuretics (e.g., furosemide) inhibit the:",["PCT transporters","*Na⁺/K⁺/2Cl⁻ cotransporter in the thick ascending limb","Collecting duct aquaporins","Glomerular filtration"],"Blocks NaCl reabsorption → massive diuresis."),
     ("ADH acts on the _____ to increase water reabsorption.",["PCT","Loop of Henle","DCT","*Collecting duct (inserts aquaporin-2 channels)"],"Concentrates the urine."),
     ("Without ADH, urine is:",["Very concentrated","*Dilute (large volume) — diabetes insipidus","Normal","Absent"],"ADH absence → can't concentrate urine."),
     ("Aldosterone promotes:",["K⁺ reabsorption","*Na⁺ reabsorption (and K⁺/H⁺ secretion) in the DCT/collecting duct","Water loss","Decreased BP"],"Mineralocorticoid effect."),
     ("ANP (atrial natriuretic peptide) is released when:",["BP is low","*Atrial walls are stretched (volume overload) → promotes Na⁺ and water excretion","K⁺ is low","ADH is high"],"Opposes RAAS; lowers blood volume."),
     ("PTH affects the kidney by:",["Inhibiting Ca²⁺ reabsorption","*Increasing Ca²⁺ reabsorption in the DCT and activating vitamin D","Decreasing phosphate excretion","Producing bicarbonate"],"PTH raises serum calcium."),
     ("Inulin clearance measures:",["Liver function","*GFR accurately (freely filtered, not reabsorbed or secreted)","Urine volume","Blood pressure"],"Gold standard marker."),
     ("PAH (para-aminohippuric acid) clearance estimates:",["GFR","*Renal plasma flow (RPF); PAH is filtered AND secreted","Blood volume","Cardiac output"],"~90% cleared in one pass."),
     ("Plasma creatinine is inversely related to:",["Blood pressure","*GFR (as GFR ↓, creatinine ↑)","Heart rate","Urine volume"],"Clinical GFR estimator."),
     ("BUN (blood urea nitrogen) rises in:",["Exercise","*Renal failure, dehydration, high protein diet, and GI bleeding","Liver disease only","Normal health"],"Non-specific but useful."),
     ("Respiratory compensation for metabolic acidosis involves:",["Hypoventilation","*Hyperventilation (to blow off CO₂ and raise pH)","No change in breathing","Increased H⁺ secretion"],"Kussmaul breathing in DKA."),
     ("Renal compensation for respiratory acidosis involves:",["Excreting HCO₃⁻","*Retaining HCO₃⁻ and excreting H⁺","Increasing CO₂","Decreasing GFR"],"Slower but more complete compensation."),
     ("Normal urine specific gravity is:",["1.000","*1.001–1.035","1.100","2.000"],"Reflects urine concentration."),
     ("Proteinuria (protein in urine) suggests:",["Normal function","*Glomerular damage (allowing protein to leak into filtrate)","Excess protein intake only","Dehydration only"],"Healthy glomeruli don't filter protein."),
     ("Glycosuria (glucose in urine) in the absence of diabetes may indicate:",["Normal variation","*Renal tubular defects (failure to reabsorb glucose) or very high blood glucose","Kidney stones","UTI"],"Exceeded transport maximum."),
     ("For the AP exam, understand the sequence:",["Secretion → filtration → reabsorption","*Filtration → reabsorption → secretion → excretion","Excretion → filtration → absorption","Random order"],"The three steps of urine formation."),
     ("Renal physiology integrates with:",["No other systems","*Cardiovascular (BP), endocrine (hormones), respiratory (acid-base), and nervous systems","Only the GI system","Only the lungs"],"Whole-body homeostasis.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Anatomy Unit 9: wrote {len(lessons)} lessons")
