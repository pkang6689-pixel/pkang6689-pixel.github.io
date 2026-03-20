#!/usr/bin/env python3
"""Anatomy Unit 5 – Endocrine System (7 lessons)."""
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

# 5.1
k,v = build_lesson(5,1,"Hormones & Chemical Signaling",
    "<h3>Hormones &amp; Chemical Signaling</h3>"
    "<h4>What Are Hormones?</h4>"
    "<p>Chemical messengers secreted by endocrine glands into the bloodstream; they act on distant target cells.</p>"
    "<h4>Types of Hormones</h4>"
    "<ul><li><b>Amino acid-derived:</b> Thyroid hormones, catecholamines (epinephrine, norepinephrine).</li>"
    "<li><b>Peptide/protein:</b> Insulin, growth hormone, ADH, oxytocin.</li>"
    "<li><b>Steroid:</b> Cortisol, estrogen, testosterone, aldosterone (derived from cholesterol).</li></ul>"
    "<h4>Mechanisms of Action</h4>"
    "<ul><li>Water-soluble hormones → bind surface receptors → second messenger (e.g., cAMP).</li>"
    "<li>Lipid-soluble (steroid/thyroid) → pass through membrane → bind intracellular/nuclear receptors → alter gene expression.</li></ul>",
    [("Hormone","Chemical messenger produced by endocrine glands; travels via blood to target cells."),
     ("Endocrine Gland","Ductless gland that secretes hormones directly into the bloodstream."),
     ("Target Cell","A cell with specific receptors for a particular hormone."),
     ("Second Messenger","Intracellular molecule (e.g., cAMP) that relays the signal from a surface receptor."),
     ("Steroid Hormone","Lipid-soluble hormone derived from cholesterol; crosses membrane to bind nuclear receptors.")],
    [("Hormones are:",["Nerve impulses","*Chemical messengers secreted into the bloodstream","Enzymes","Structural proteins"],"Hormones travel through blood to targets."),
     ("Endocrine glands are 'ductless' because they:",["Have no products","*Secrete hormones directly into the blood (no ducts)","Secrete into body cavities","Are not real glands"],"Ductless = directly into bloodstream."),
     ("Steroid hormones are derived from:",["Amino acids","*Cholesterol","Glucose","ATP"],"Cholesterol backbone → steroid ring."),
     ("Insulin is a _____ hormone.",["Steroid","*Peptide (protein)","Amino acid-derived","Lipid"],"51 amino acid peptide."),
     ("Water-soluble hormones (peptides):",["Cross the membrane directly","*Bind cell surface receptors and use second messengers","Enter the nucleus","Are always steroids"],"Can't cross lipid bilayer → need surface receptors."),
     ("Steroid hormones:",["Can't enter cells","*Cross the cell membrane and bind intracellular/nuclear receptors","Use cAMP","Bind surface receptors only"],"Lipid-soluble → enter cells directly."),
     ("cAMP is an example of a:",["Hormone","*Second messenger","Receptor","Steroid"],"Cyclic AMP relays the signal intracellularly."),
     ("The hypothalamus connects the nervous and endocrine systems by:",["Having no role","*Producing releasing/inhibiting hormones that control the pituitary gland","Being a muscle","Only processing sensory info"],"Neuroendocrine link."),
     ("Hormone specificity depends on:",["Blood type","*The presence of specific receptors on target cells","Hormone concentration only","The size of the gland"],"No receptor = no response."),
     ("Up-regulation of receptors means:",["Fewer receptors","*Increased receptor number (increased sensitivity)","Receptor destruction","No change"],"Cell becomes more responsive."),
     ("Down-regulation of receptors means:",["More receptors","*Decreased receptor number (decreased sensitivity)","Receptor creation","Improved response"],"Prolonged hormone exposure → reduced sensitivity."),
     ("Catecholamines (epinephrine, norepinephrine) are:",["Steroid hormones","*Amino acid-derived hormones (from tyrosine)","Peptide hormones","Lipids"],"Tyrosine → dopamine → NE → epinephrine."),
     ("Thyroid hormones (T3/T4) are:",["Steroids","*Amino acid-derived (from tyrosine + iodine)","Peptides","Carbohydrates"],"Iodinated tyrosine residues."),
     ("Prostaglandins are:",["True hormones","*Local chemical mediators (paracrines) derived from lipids","Steroids","Proteins"],"Act locally, not always through bloodstream."),
     ("Hormones are typically present in the blood at:",["Very high concentrations","*Very low (nanomolar) concentrations","Equal to glucose","Unmeasurable levels"],"Tiny amounts have large effects."),
     ("Half-life of a hormone refers to:",["When it was made","*The time it takes for half the hormone to be broken down","Its potency","Its receptor count"],"Determines how long effects last."),
     ("The endocrine system works _____ compared to the nervous system.",["Faster","*More slowly but with longer-lasting effects","At the same speed","Not at all"],"Hormones = slow onset, long duration vs. fast neural signals."),
     ("Hormone levels are regulated primarily by:",["Random secretion","*Negative feedback loops","Positive feedback only","No regulation"],"Negative feedback maintains homeostasis."),
     ("An example of positive feedback in the endocrine system:",["Insulin regulation","*Oxytocin during labor (contractions increase oxytocin release)","Thyroid regulation","Cortisol regulation"],"Rare: positive feedback amplifies until completion."),
     ("Why is understanding hormone signaling important?",["Only for endocrinologists","*It underlies diabetes, thyroid disease, growth disorders, reproductive health, and many more","Only for the exam","It isn't"],"Endocrine dysfunction = widespread clinical impact.")]
)
lessons[k]=v

# 5.2
k,v = build_lesson(5,2,"Major Endocrine Glands",
    "<h3>Major Endocrine Glands</h3>"
    "<ul><li><b>Pituitary (hypophysis):</b> 'Master gland'; anterior (GH, TSH, ACTH, FSH, LH, prolactin), posterior (ADH, oxytocin — made in hypothalamus).</li>"
    "<li><b>Thyroid:</b> T3, T4 (metabolism); calcitonin (lowers blood Ca²⁺).</li>"
    "<li><b>Parathyroids (4):</b> PTH — raises blood Ca²⁺.</li>"
    "<li><b>Adrenals:</b> Cortex (cortisol, aldosterone, androgens); Medulla (epinephrine, norepinephrine).</li>"
    "<li><b>Pancreas (endocrine):</b> Islets of Langerhans — β-cells (insulin↓glucose), α-cells (glucagon↑glucose).</li>"
    "<li><b>Gonads:</b> Ovaries (estrogen, progesterone); Testes (testosterone).</li>"
    "<li><b>Pineal gland:</b> Melatonin (circadian rhythm).</li>"
    "<li><b>Thymus:</b> Thymosin (T-cell maturation).</li></ul>",
    [("Pituitary Gland","'Master gland'; anterior lobe produces GH, TSH, ACTH, FSH, LH, prolactin; posterior stores ADH, oxytocin."),
     ("Thyroid Gland","Produces T3/T4 (regulate metabolism) and calcitonin (lowers blood calcium)."),
     ("Adrenal Glands","Cortex: cortisol, aldosterone. Medulla: epinephrine, norepinephrine."),
     ("Pancreatic Islets","β-cells secrete insulin (↓glucose); α-cells secrete glucagon (↑glucose)."),
     ("Parathyroid Glands","Four small glands; secrete PTH which raises blood calcium levels.")],
    [("The 'master gland' is the:",["Thyroid","Adrenal","*Pituitary","Pineal"],"Pituitary controls many other endocrine glands."),
     ("Growth hormone (GH) is produced by the:",["Thyroid","*Anterior pituitary","Posterior pituitary","Adrenal gland"],"Somatotrophs in the anterior pituitary."),
     ("ADH and oxytocin are stored in the:",["Anterior pituitary","*Posterior pituitary (made in hypothalamus)","Thyroid","Adrenals"],"Hypothalamus makes them; posterior pituitary releases them."),
     ("T3 and T4 regulate:",["Blood pressure only","*Metabolism (energy production, heat generation)","Blood clotting","Reproduction only"],"Thyroid hormones set basal metabolic rate."),
     ("Calcitonin is produced by the _____ and _____ blood calcium.",["Parathyroid; raises","*Thyroid; lowers","Pituitary; raises","Adrenal; lowers"],"Calcitonin = tones down calcium."),
     ("PTH is produced by the _____ and _____ blood calcium.",["Thyroid; lowers","*Parathyroids; raises","Adrenals; lowers","Pituitary; raises"],"PTH mobilizes Ca²⁺ from bone, increases reabsorption."),
     ("Cortisol is produced by the:",["Adrenal medulla","*Adrenal cortex","Thyroid","Pituitary"],"Zona fasciculata of the adrenal cortex."),
     ("Epinephrine is produced by the:",["Adrenal cortex","*Adrenal medulla","Thyroid","Pancreas"],"Medulla = modified sympathetic ganglion."),
     ("Insulin is produced by _____ cells in the pancreas.",["Alpha","*Beta","Delta","Gamma"],"β-cells of the islets of Langerhans."),
     ("Glucagon is produced by _____ cells in the pancreas.",["Beta","*Alpha","Delta","Gamma"],"α-cells raise blood glucose."),
     ("Insulin _____ blood glucose.",["Raises","*Lowers (promotes glucose uptake by cells)","Has no effect on","Eliminates"],"Insulin = key that opens cells to glucose."),
     ("Glucagon _____ blood glucose.",["Lowers","*Raises (stimulates glycogenolysis and gluconeogenesis in liver)","Has no effect on","Eliminates"],"Counter-regulatory to insulin."),
     ("Melatonin is produced by the _____ gland.",["Pituitary","Thyroid","*Pineal","Adrenal"],"Pineal gland regulates sleep-wake cycles."),
     ("The thymus produces thymosin, which is important for:",["Digestion","*T-cell maturation and immune function","Metabolism","Heart function"],"Critical in childhood immunity."),
     ("Aldosterone regulates:",["Blood sugar","*Sodium and potassium balance (and blood pressure)","Calcium","Thyroid function"],"Aldosterone = Na⁺ retention, K⁺ excretion."),
     ("TSH (thyroid-stimulating hormone) is produced by:",["Thyroid","*Anterior pituitary","Hypothalamus","Adrenals"],"TSH stimulates T3/T4 production."),
     ("ACTH stimulates the:",["Thyroid","*Adrenal cortex (to produce cortisol)","Gonads","Pancreas"],"Adrenocorticotropic hormone → cortisol release."),
     ("FSH and LH are involved in:",["Metabolism","Blood pressure","*Reproductive function (gamete production and sex hormone secretion)","Digestion"],"Gonadotropins regulate the gonads."),
     ("Prolactin stimulates:",["Growth","*Milk production in mammary glands","Thyroid activity","Muscle contraction"],"Prolactin = pro-lactation."),
     ("The endocrine glands work together as a coordinated system to:",["Function independently","*Maintain homeostasis through interconnected feedback loops","Oppose each other always","Compete for resources"],"Integrated hormonal regulation.")]
)
lessons[k]=v

# 5.3
k,v = build_lesson(5,3,"Hormonal Regulation of Homeostasis",
    "<h3>Hormonal Regulation of Homeostasis</h3>"
    "<h4>Blood Glucose Regulation</h4>"
    "<p>High glucose → β-cells release insulin → cells absorb glucose → blood glucose drops. Low glucose → α-cells release glucagon → liver releases glucose → blood glucose rises.</p>"
    "<h4>Calcium Homeostasis</h4>"
    "<p>High Ca²⁺ → calcitonin → Ca²⁺ into bone. Low Ca²⁺ → PTH → Ca²⁺ out of bone + ↑intestinal absorption + ↑renal reabsorption.</p>"
    "<h4>Water Balance</h4>"
    "<p>Dehydration → hypothalamus detects ↑osmolarity → ADH released → kidneys reabsorb more water.</p>",
    [("Blood Glucose Homeostasis","Insulin (↓glucose) and glucagon (↑glucose) maintain blood sugar within a narrow range."),
     ("Calcium Homeostasis","PTH raises Ca²⁺; calcitonin lowers Ca²⁺; vitamin D aids absorption."),
     ("ADH (Antidiuretic Hormone)","Released when dehydrated; causes kidneys to reabsorb more water, concentrating urine."),
     ("Negative Feedback","Response reduces the original stimulus; primary mechanism for hormonal regulation."),
     ("Homeostasis","Maintenance of stable internal conditions despite external changes.")],
    [("When blood glucose is high, the pancreas releases:",["Glucagon","*Insulin","Cortisol","Epinephrine"],"Insulin lowers glucose."),
     ("When blood glucose is low, the pancreas releases:",["Insulin","*Glucagon","Calcitonin","ADH"],"Glucagon raises glucose."),
     ("Diabetes mellitus type 1 involves:",["Insulin resistance","*Autoimmune destruction of β-cells (no insulin production)","Excess insulin","Excess glucagon"],"T1D = absolute insulin deficiency."),
     ("Diabetes mellitus type 2 involves:",["No β-cells","*Insulin resistance (cells don't respond properly to insulin)","Excess calcitonin","Low glucagon"],"T2D = relative insulin insufficiency."),
     ("PTH increases blood calcium by:",["Storing Ca²⁺ in bone","*Releasing Ca²⁺ from bone, increasing renal reabsorption, and activating vitamin D","Excreting Ca²⁺","Blocking absorption"],"Multiple mechanisms raise Ca²⁺."),
     ("Calcitonin decreases blood calcium by:",["Releasing Ca²⁺ from bone","*Promoting Ca²⁺ deposition into bone and reducing renal reabsorption","Destroying Ca²⁺","Blocking PTH completely"],"Calcitonin = calcium toned down."),
     ("ADH is released when:",["Blood is dilute","*Blood osmolarity is high (dehydration)","Blood pressure is very high","Calcium is low"],"Osmoreceptors in hypothalamus detect concentration."),
     ("ADH causes the kidneys to:",["Excrete more water","*Reabsorb more water (producing concentrated urine)","Produce more urine","Excrete sodium"],"Anti-diuretic = less urine."),
     ("Aldosterone helps regulate blood pressure by:",["Excreting sodium","*Causing kidneys to retain sodium (water follows → ↑blood volume → ↑BP)","Dilating vessels","Lowering heart rate"],"Na⁺ retention → water retention → ↑BP."),
     ("Cortisol is important during stress because it:",["Lowers blood sugar","*Increases blood glucose, suppresses inflammation, and mobilizes energy reserves","Has no effect","Only affects mood"],"Cortisol prepares body for prolonged stress."),
     ("Negative feedback means:",["The response amplifies the stimulus","*The response opposes (reduces) the original stimulus","There is no response","Positive only"],"Most hormonal regulation uses negative feedback."),
     ("An example of hormonal negative feedback:",["*High T3/T4 → inhibits TSH release → less thyroid stimulation","Oxytocin during labor","Blood clotting cascade","Fever increasing"],"Classic negative feedback loop."),
     ("Hyperthyroidism (excess thyroid hormone) causes:",["Slow metabolism","*↑Metabolism, weight loss, rapid heart rate, heat intolerance","No symptoms","Hypothermia"],"Overactive thyroid = hypermetabolic state."),
     ("Hypothyroidism (low thyroid hormone) causes:",["Fast metabolism","*↓Metabolism, weight gain, fatigue, cold intolerance","Hyperactivity","No symptoms"],"Underactive thyroid = hypometabolic state."),
     ("Addison's disease involves:",["Excess cortisol","*Insufficient adrenal cortex hormones (cortisol, aldosterone)","Excess insulin","Excess GH"],"Adrenal insufficiency."),
     ("Cushing's syndrome involves:",["Low cortisol","*Excess cortisol (moon face, buffalo hump, weight gain)","Low aldosterone","High insulin"],"Chronic cortisol excess."),
     ("Vitamin D acts as a hormone that:",["Lowers calcium","*Promotes intestinal calcium absorption (works with PTH)","Blocks PTH","Has no role in calcium"],"Vitamin D is essential for Ca²⁺ balance."),
     ("The renin-angiotensin-aldosterone system (RAAS) is activated by:",["High blood pressure","*Low blood pressure (kidneys release renin)","High calcium","High glucose"],"Low BP → renin → angiotensin II → aldosterone → ↑BP."),
     ("Erythropoietin (EPO) is released by the kidneys when:",["O₂ is high","*O₂ levels are low (stimulates red blood cell production)","BP is high","Glucose is high"],"EPO → bone marrow → more RBCs."),
     ("Hormonal homeostasis failure underlies:",["No diseases","*Many diseases: diabetes, thyroid disorders, adrenal disorders, reproductive issues","Only rare conditions","Only one disease"],"Endocrine dysfunction = many clinical conditions.")]
)
lessons[k]=v

# 5.4
k,v = build_lesson(5,4,"Feedback Loops in the Endocrine System",
    "<h3>Feedback Loops in the Endocrine System</h3>"
    "<h4>Negative Feedback (Most Common)</h4>"
    "<p>Output reduces the stimulus. Example: ↑cortisol → inhibits hypothalamus (CRH) and anterior pituitary (ACTH) → less cortisol produced.</p>"
    "<h4>Positive Feedback (Rare)</h4>"
    "<p>Output amplifies the stimulus. Examples: oxytocin during labor (uterine contractions ↑ → more oxytocin → stronger contractions until delivery) and LH surge triggering ovulation.</p>"
    "<h4>Hypothalamic-Pituitary Axes</h4>"
    "<p>HPT axis (thyroid), HPA axis (adrenal), HPG axis (gonadal) — all use negative feedback to maintain set points.</p>",
    [("Negative Feedback Loop","The dominant control mechanism; the product inhibits further production to maintain a set point."),
     ("Positive Feedback Loop","Rare; the product amplifies the stimulus (e.g., oxytocin in labor, LH surge)."),
     ("HPA Axis","Hypothalamic-Pituitary-Adrenal axis: CRH → ACTH → cortisol; cortisol inhibits CRH and ACTH."),
     ("HPT Axis","Hypothalamic-Pituitary-Thyroid axis: TRH → TSH → T3/T4; T3/T4 inhibit TRH and TSH."),
     ("HPG Axis","Hypothalamic-Pituitary-Gonadal axis: GnRH → FSH/LH → sex hormones; sex hormones feed back.")],
    [("Most endocrine regulation uses:",["Positive feedback","*Negative feedback","No feedback","Random secretion"],"Negative feedback = primary mechanism."),
     ("In negative feedback, the product:",["Amplifies the stimulus","*Inhibits the stimulus (reduces further production)","Has no effect","Destroys the gland"],"Product shuts off its own production."),
     ("The hypothalamic-pituitary-thyroid (HPT) axis: high T3/T4:",["Stimulates more TSH","*Inhibits TRH and TSH (reducing thyroid stimulation)","Has no effect","Stimulates the thyroid directly"],"Classic negative feedback."),
     ("The hypothalamic-pituitary-adrenal (HPA) axis: high cortisol:",["Stimulates more CRH","*Inhibits CRH and ACTH (reducing cortisol production)","Destroys the adrenals","Has no effect"],"Cortisol feeds back to inhibit its own axis."),
     ("An example of positive feedback is:",["Insulin reducing blood glucose","*Oxytocin during labor (contractions → more oxytocin → stronger contractions)","TSH regulation","Cortisol regulation"],"Amplification until the event is complete."),
     ("The LH surge that triggers ovulation is an example of:",["Negative feedback","*Positive feedback (rising estrogen triggers an LH spike)","No feedback","Constant secretion"],"Estrogen positive feedback → LH surge → ovulation."),
     ("Positive feedback loops end when:",["They never end","*The stimulus is removed (e.g., baby is delivered, stopping oxytocin loop)","They reverse automatically","Negative feedback takes over permanently"],"Event completion removes the stimulus."),
     ("In the HPG axis, testosterone in males:",["Stimulates more GnRH","*Inhibits GnRH and LH (negative feedback)","Has no feedback effect","Only stimulates FSH"],"Testosterone reduces its own production signal."),
     ("If the thyroid is removed, TSH levels would:",["Drop","*Rise (no T3/T4 to provide negative feedback, so pituitary produces more TSH)","Stay the same","Disappear"],"Loss of inhibition → TSH increase."),
     ("Chronic stress keeps the HPA axis active, resulting in:",["Low cortisol","*Chronically elevated cortisol (harmful: weight gain, immune suppression, anxiety)","Normal cortisol","No cortisol"],"Persistent stress overrides normal feedback."),
     ("A pituitary tumor producing excess ACTH causes:",["Addison's disease","*Cushing's disease (excess cortisol from adrenal stimulation)","Hypothyroidism","Diabetes"],"ACTH-secreting tumor → cortisol excess."),
     ("Set point in homeostasis refers to:",["A random value","*The ideal physiological value the body maintains (e.g., 37°C, ~100 mg/dL glucose)","A maximum only","A minimum only"],"Feedback loops maintain the set point."),
     ("Hormonal rhythms (e.g., cortisol highest in morning) are called:",["Random","*Circadian rhythms","Monthly rhythms only","No pattern"],"24-hour biological clock patterns."),
     ("The hypothalamus releases _____ hormones to control the anterior pituitary.",["No","*Releasing and inhibiting","Only releasing","Only inhibiting"],"Both releasing and inhibiting hormones exist."),
     ("TRH stands for:",["Thyroid receptor hormone","*Thyrotropin-releasing hormone","Total thyroid hormone","Thyroid resistance hormone"],"TRH → TSH → T3/T4."),
     ("CRH stands for:",["Cortisol-receptor hormone","*Corticotropin-releasing hormone","Central regulatory hormone","Calcium-related hormone"],"CRH → ACTH → cortisol."),
     ("GnRH stands for:",["Growth-releasing hormone","*Gonadotropin-releasing hormone","Glucose-regulating hormone","General neuroendocrine hormone"],"GnRH → FSH/LH → sex hormones."),
     ("Feedback loops are clinically important because:",["They are simple","*Many endocrine disorders result from feedback loop disruption","They never fail","They are theoretical only"],"Understanding feedback → diagnosing and treating disease."),
     ("Exogenous steroid use can suppress the HPA axis because:",["Steroids have no effect","*External cortisol provides negative feedback, reducing natural cortisol production","They stimulate CRH","They are not absorbed"],"Why sudden steroid withdrawal is dangerous."),
     ("Understanding feedback loops is essential for:",["Nothing","*Diagnosing endocrine disorders, managing hormone therapies, and predicting drug effects","Only academic purposes","Only one specialty"],"Foundation of endocrine medicine.")]
)
lessons[k]=v

# 5.5
k,v = build_lesson(5,5,"Disorders of the Endocrine System",
    "<h3>Disorders of the Endocrine System</h3>"
    "<ul><li><b>Diabetes mellitus:</b> Type 1 (autoimmune β-cell destruction) and Type 2 (insulin resistance). Hyperglycemia → complications (neuropathy, retinopathy, nephropathy).</li>"
    "<li><b>Hyperthyroidism:</b> Graves' disease (autoimmune → excess T3/T4). Symptoms: weight loss, tachycardia, exophthalmos.</li>"
    "<li><b>Hypothyroidism:</b> Hashimoto's (autoimmune thyroid destruction). Symptoms: fatigue, weight gain, cold intolerance.</li>"
    "<li><b>Cushing's syndrome:</b> Excess cortisol. <b>Addison's disease:</b> Adrenal insufficiency.</li>"
    "<li><b>Gigantism/Acromegaly:</b> Excess GH before/after bone growth plate closure.</li></ul>",
    [("Diabetes Mellitus","Chronic hyperglycemia; Type 1 (no insulin) vs. Type 2 (insulin resistance)."),
     ("Graves' Disease","Autoimmune hyperthyroidism; antibodies stimulate the thyroid."),
     ("Hashimoto's Thyroiditis","Autoimmune hypothyroidism; gradual thyroid destruction."),
     ("Cushing's Syndrome","Chronic excess cortisol causing moon face, central obesity, and metabolic issues."),
     ("Acromegaly","Excess GH in adults; enlarged hands, feet, and facial features.")],
    [("Type 1 diabetes results from:",["Overeating","*Autoimmune destruction of pancreatic β-cells","Excess insulin","Lack of exercise only"],"T1D = absolute insulin deficiency."),
     ("Type 2 diabetes involves:",["No β-cells","*Insulin resistance and relative insulin deficiency","Autoimmune attack","Too much glucagon only"],"Cells don't respond properly to insulin."),
     ("A major long-term complication of uncontrolled diabetes:",["None","*Neuropathy, retinopathy, nephropathy, cardiovascular disease","Only weight gain","Only fatigue"],"Chronic hyperglycemia damages blood vessels and nerves."),
     ("Graves' disease is a form of:",["Hypothyroidism","*Hyperthyroidism (autoimmune stimulation of thyroid)","Diabetes","Adrenal disease"],"Antibodies mimic TSH → overstimulate thyroid."),
     ("Exophthalmos (bulging eyes) is associated with:",["Hypothyroidism","*Graves' disease (hyperthyroidism)","Diabetes","Cushing's"],"Autoimmune inflammation behind the eyes."),
     ("Hashimoto's thyroiditis causes:",["Hyperthyroidism","*Hypothyroidism (gradual thyroid destruction)","Diabetes","Adrenal insufficiency"],"Most common cause of hypothyroidism in iodine-sufficient areas."),
     ("Goiter is:",["A normal thyroid","*An enlarged thyroid gland (can occur in hyper- or hypothyroidism)","A tumor","An adrenal disorder"],"Thyroid enlargement from various causes."),
     ("Cushing's syndrome features include:",["Weight loss","*Moon face, buffalo hump, central obesity, easy bruising, hyperglycemia","Low cortisol","Hypotension"],"Chronic cortisol excess effects."),
     ("Addison's disease is:",["Excess cortisol","*Adrenal insufficiency (low cortisol and aldosterone)","Excess aldosterone","A thyroid disorder"],"Can cause hypotension, hyperpigmentation, fatigue."),
     ("Gigantism occurs when excess GH is produced:",["After puberty","*Before the growth plates close (childhood)","At any age","Never"],"Excessive linear growth in children."),
     ("Acromegaly occurs when excess GH is produced:",["Before puberty","*After the growth plates close (adulthood) — enlarges extremities","In infants only","Never"],"Can't grow taller, but bones/soft tissue enlarge."),
     ("Dwarfism can result from:",["Excess GH","*GH deficiency during childhood","Excess thyroid hormone","Excess cortisol"],"Pituitary dwarfism = lack of GH."),
     ("Diabetes insipidus involves:",["High blood sugar","*ADH deficiency or resistance → excessive dilute urine and extreme thirst","High insulin","Low glucagon"],"Not related to blood sugar; related to water balance."),
     ("Conn's syndrome (primary hyperaldosteronism) causes:",["Low blood pressure","*Hypertension, hypokalemia (excess aldosterone)","Low sodium","Hypotension"],"Too much aldosterone → Na⁺ retention → ↑BP."),
     ("Pheochromocytoma is a tumor of the:",["Thyroid","*Adrenal medulla (excess catecholamines: episodic hypertension, palpitations)","Pituitary","Pancreas"],"Catecholamine-secreting tumor."),
     ("SIADH (Syndrome of Inappropriate ADH) causes:",["Dehydration","*Excess water retention, hyponatremia (dilutional)","Diabetes","Hypernatremia"],"Too much ADH → too much water retained."),
     ("Cretinism results from:",["Excess thyroid hormone in infants","*Severe thyroid deficiency during fetal/infant development → intellectual disability, growth failure","Normal thyroid","Excess GH"],"Congenital hypothyroidism."),
     ("Polycystic ovary syndrome (PCOS) involves:",["Only ovarian cysts","*Hormonal imbalance (excess androgens), irregular periods, insulin resistance","Only weight gain","Only infertility"],"Complex endocrine disorder affecting many women."),
     ("Treatment for hypothyroidism typically involves:",["Surgery only","*Levothyroxine (synthetic T4) replacement","Radioactive iodine","No treatment"],"Daily oral T4 replacement."),
     ("Early detection of endocrine disorders is important because:",["They are untreatable","*Many are manageable with medication, and untreated cases lead to serious complications","They resolve on their own","They are rare"],"Early treatment prevents complications.")]
)
lessons[k]=v

# 5.6
k,v = build_lesson(5,6,"Case Studies in Endocrinology",
    "<h3>Case Studies in Endocrinology</h3>"
    "<h4>Case 1: A Patient with Uncontrolled Blood Sugar</h4>"
    "<p>A 45-year-old presents with polyuria, polydipsia, and weight loss despite increased appetite. Fasting glucose 280 mg/dL, HbA1c 10.5%. Diagnosis: Type 2 diabetes mellitus. Management: lifestyle changes + metformin + monitoring.</p>"
    "<h4>Case 2: Thyroid Dysfunction</h4>"
    "<p>A 30-year-old female with weight gain, fatigue, constipation, cold intolerance. TSH elevated, T4 low. Anti-TPO antibodies positive. Diagnosis: Hashimoto's thyroiditis. Treatment: levothyroxine.</p>"
    "<h4>Case 3: Adrenal Crisis</h4>"
    "<p>A patient on chronic prednisone suddenly stops medication → collapse, hypotension, hypoglycemia. Adrenal crisis due to HPA axis suppression. Treatment: IV hydrocortisone, fluid resuscitation.</p>",
    [("Polyuria/Polydipsia/Polyphagia","The 'three Ps' of diabetes: excessive urination, thirst, and hunger."),
     ("HbA1c","Glycated hemoglobin; reflects average blood glucose over ~3 months."),
     ("Anti-TPO Antibodies","Antibodies against thyroid peroxidase; marker for Hashimoto's thyroiditis."),
     ("Adrenal Crisis","Life-threatening cortisol deficiency; can occur with sudden steroid withdrawal."),
     ("Metformin","First-line oral medication for Type 2 diabetes; reduces hepatic glucose production.")],
    [("The 'three Ps' of diabetes are:",["Pain, pressure, pallor","*Polyuria, polydipsia, polyphagia","Palpitations, perspiration, pallor","Paresthesia, paralysis, pain"],"Classic diabetic symptoms."),
     ("HbA1c measures:",["Fasting glucose","*Average blood glucose over approximately 3 months","Insulin levels","Glucagon levels"],"Glycated hemoglobin reflects chronic glucose control."),
     ("A normal HbA1c is below:",["10%","8%","*5.7%","3%"],"<5.7% normal; 5.7-6.4% prediabetes; ≥6.5% diabetes."),
     ("In the thyroid case, elevated TSH with low T4 indicates:",["Hyperthyroidism","*Primary hypothyroidism (thyroid failing, pituitary compensating)","Normal function","Pituitary tumor"],"Pituitary tries to stimulate failing thyroid → ↑TSH."),
     ("Anti-TPO antibodies confirm:",["Graves' disease","*Hashimoto's thyroiditis (autoimmune thyroid destruction)","Normal thyroid","Diabetes"],"Autoimmune marker for Hashimoto's."),
     ("Adrenal crisis occurs because:",["The adrenals produce too much","*Chronic steroid use suppresses the HPA axis; sudden withdrawal → no cortisol","Steroids are always safe","The thyroid fails"],"Dependency → sudden withdrawal = crisis."),
     ("Treatment for adrenal crisis includes:",["Oral medication only","*IV hydrocortisone and fluid resuscitation (emergency)","Insulin","Thyroid hormone"],"Life-threatening emergency requiring IV steroids."),
     ("Fasting glucose of 280 mg/dL is:",["Normal","*Severely elevated (normal is <100 mg/dL)","Slightly high","Low"],">126 = diabetic. 280 = very high."),
     ("Metformin works by:",["Increasing insulin production","*Reducing hepatic glucose production and improving insulin sensitivity","Blocking glucagon","Destroying β-cells"],"First-line drug for T2DM."),
     ("Why is the physical exam + labs important in endocrine cases?",["They're not","*Symptoms alone can overlap; specific labs (hormone levels, antibodies) confirm the diagnosis","Only imaging matters","Symptoms are enough"],"Lab confirmation is essential."),
     ("If a patient has low TSH and high T3/T4, the diagnosis is:",["Hypothyroidism","*Hyperthyroidism (e.g., Graves' disease — negative feedback suppresses TSH)","Normal","Diabetes"],"Low TSH + high T3/T4 = hyperthyroid."),
     ("Diabetic ketoacidosis (DKA) is more common in:",["Type 2 diabetes","*Type 1 diabetes (absolute insulin lack → fat breakdown → ketone production)","Thyroid disease","Adrenal disease"],"DKA = medical emergency in T1D."),
     ("A thyroid storm is:",["A minor issue","*A life-threatening exacerbation of hyperthyroidism (very high T3/T4, fever, tachycardia)","A type of hypothyroidism","An adrenal emergency"],"Requires emergency treatment."),
     ("Lifestyle modifications for T2DM include:",["Medication only","*Diet changes, regular exercise, weight management, and blood glucose monitoring","Bed rest","No changes needed"],"Lifestyle is fundamental to T2DM management."),
     ("When tapering steroids, the dose should be:",["Stopped abruptly","*Reduced gradually to allow HPA axis recovery","Doubled","Kept constant"],"Gradual taper prevents adrenal crisis."),
     ("Case studies integrate knowledge of:",["One organ system only","*Multiple concepts (anatomy, physiology, pathology, pharmacology) for clinical reasoning","Only drug names","Only lab values"],"Clinical reasoning requires integrated knowledge."),
     ("A patient with a pituitary tumor may present with:",["*Visual field defects (optic chiasm compression), headaches, and hormonal abnormalities","Only headache","No symptoms","Joint pain only"],"Pituitary tumors can affect nearby structures."),
     ("Monitoring treatment in endocrine disorders involves regular:",["Nothing","*Blood tests (hormone levels, HbA1c, electrolytes) and symptom assessment","Imaging only","Surgery"],"Ongoing monitoring optimizes treatment."),
     ("The importance of patient education in endocrine disorders:",["Minimal","*Critical — patients manage daily (medication, diet, monitoring), and understanding improves outcomes","Only for healthcare providers","Not needed"],"Chronic disease management requires informed patients."),
     ("These case studies demonstrate that endocrine disorders:",["Are rare","*Are common, interconnected, and manageable with proper diagnosis and treatment","Always require surgery","Cannot be treated"],"Endocrine disease is prevalent and treatable.")]
)
lessons[k]=v

# 5.7
k,v = build_lesson(5,7,"AP Prep: Hormone Pathways",
    "<h3>AP Prep: Hormone Pathways</h3>"
    "<h4>Essential Pathways for the Exam</h4>"
    "<ul><li><b>HPT axis:</b> Hypothalamus (TRH) → Anterior pituitary (TSH) → Thyroid (T3/T4) → Negative feedback to hypothalamus/pituitary.</li>"
    "<li><b>HPA axis:</b> Hypothalamus (CRH) → Anterior pituitary (ACTH) → Adrenal cortex (cortisol) → Negative feedback.</li>"
    "<li><b>HPG axis:</b> Hypothalamus (GnRH) → Anterior pituitary (FSH/LH) → Gonads (estrogen/testosterone) → Negative feedback.</li>"
    "<li><b>Blood glucose:</b> Insulin/glucagon antagonism.</li>"
    "<li><b>Calcium:</b> PTH/calcitonin/vitamin D interplay.</li></ul>",
    [("HPT Axis","TRH → TSH → T3/T4; negative feedback from thyroid hormones."),
     ("HPA Axis","CRH → ACTH → cortisol; stress axis; negative feedback from cortisol."),
     ("HPG Axis","GnRH → FSH/LH → sex hormones; reproductive regulation."),
     ("Tropic Hormone","A hormone that stimulates another endocrine gland (e.g., TSH, ACTH, FSH, LH)."),
     ("Permissive Effect","One hormone enhances the effect of another (e.g., thyroid hormones potentiate catecholamine effects).")],
    [("In the HPT axis, TRH is released by the:",["Thyroid","Pituitary","*Hypothalamus","Adrenal gland"],"TRH = thyrotropin-releasing hormone from hypothalamus."),
     ("TSH acts on the:",["Adrenals","*Thyroid gland to produce T3/T4","Pancreas","Gonads"],"TSH stimulates thyroid hormone production."),
     ("Negative feedback in the HPT axis: high T3/T4 inhibits:",["The thyroid directly","*TRH (hypothalamus) and TSH (anterior pituitary)","The gonads","The adrenals"],"Long and short loop feedback."),
     ("In the HPA axis, ACTH acts on the:",["Thyroid","*Adrenal cortex to produce cortisol","Medulla","Pancreas"],"ACTH → cortisol (zona fasciculata)."),
     ("CRH release increases during:",["Sleep","*Stress (physical, emotional, or physiological)","Relaxation","Low cortisol only"],"Stress activates the HPA axis."),
     ("In the HPG axis, FSH stimulates:",["Cortisol production","*Follicle development (females) and spermatogenesis (males)","Thyroid activity","Calcium release"],"FSH = follicle-stimulating hormone."),
     ("LH triggers:",["Thyroid function","*Ovulation (females) and testosterone production (males)","Cortisol release","Calcium reabsorption"],"Luteinizing hormone."),
     ("A tropic hormone is one that:",["Acts on muscles","*Stimulates another endocrine gland to secrete its hormone","Is always a steroid","Is produced by the gonads"],"TSH, ACTH, FSH, LH are tropic."),
     ("The permissive effect means:",["Hormones block each other","*One hormone makes target cells more responsive to another (e.g., thyroid potentiates catecholamines)","No interaction","Hormones are identical"],"Thyroid hormones enable catecholamine effects."),
     ("Antagonistic hormones:",["Work together","*Oppose each other (e.g., insulin ↓glucose vs. glucagon ↑glucose)","Are identical","Don't exist"],"Opposing effects maintain balance."),
     ("Synergistic hormones:",["Oppose each other","*Work together to produce a greater combined effect","Cancel each other","Don't exist"],"Combined effect > individual effects."),
     ("If the anterior pituitary is destroyed, which would increase?",["TSH","ACTH","*None of the anterior pituitary hormones would increase; all would drop","FSH"],"No pituitary = no tropic hormones."),
     ("A patient with primary hypothyroidism has:",["Low TSH","*High TSH, low T3/T4","Normal labs","Low ACTH"],"Pituitary compensates by raising TSH."),
     ("A patient with secondary hypothyroidism (pituitary failure) has:",["High TSH","*Low TSH, low T3/T4","High T4","Normal labs"],"Pituitary can't produce TSH."),
     ("Identifying primary vs. secondary endocrine failure is important for:",["Nothing","*Determining the location of the problem and guiding treatment","Only research","Only surgery"],"Primary = gland failure. Secondary = pituitary. Tertiary = hypothalamus."),
     ("Water-soluble hormones have a _____ half-life compared to steroids.",["Longer","*Shorter","Equal","No half-life"],"Peptides degrade faster than steroids."),
     ("Steroid hormones affect gene expression by:",["Using cAMP","*Binding intracellular receptors that act as transcription factors","Binding surface receptors","Being enzymes"],"Steroid-receptor complex → alters DNA transcription."),
     ("For the AP exam, you should be able to:",["Only memorize gland names","*Trace complete hormone pathways, predict effects of disruptions, and interpret clinical data","Only name hormones","Only identify glands"],"Application-level understanding required."),
     ("A question asks: 'What happens if the adrenal glands are removed?' The answer involves:",["Nothing","*Loss of cortisol, aldosterone, adrenal androgens → adrenal crisis without replacement","Only testosterone loss","Only epinephrine loss"],"Cortisol and aldosterone are life-essential."),
     ("Integrating endocrine pathways is essential because:",["Systems are isolated","*The endocrine system interacts with every other body system","Only nerves matter","Only muscles matter"],"Hormones regulate nearly all physiological processes.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Anatomy Unit 5: wrote {len(lessons)} lessons")
