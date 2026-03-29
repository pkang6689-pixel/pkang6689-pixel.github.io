import json, os, glob

base = 'content_data/AnatomyLessons'

replacements = {
    # UNIT 4
    ("Unit4/Lesson4.3_Quiz.json", 7): {
        "Only hearing and balance": "Only hearing and balance processes within the inner ear and auditory cortex",
        "Only visual processing": "Only visual processing within the retina, optic nerve, and occipital cortex",
        "Only voluntary movement": "Only voluntary skeletal movement coordinated through the motor cortex and cerebellum",
    },
    ("Unit4/Lesson4.5_Quiz.json", 5): {
        "Acetylcholine": "Acetylcholine (cholinergic transmitter)",
        "Serotonin": "Serotonin (5-hydroxytryptamine)",
        "Dopamine": "Dopamine (catecholamine precursor)",
    },
    ("Unit4/Lesson4.5_Quiz.json", 8): {
        "Only insulin": "Only insulin secreted into the portal circulation",
        "Only cortisol": "Only cortisol released from the adrenal cortex",
        "Only acetylcholine": "Only acetylcholine from parasympathetic nerve endings",
    },
    ("Unit4/Lesson4.6_Quiz.json", 24): {
        "The infant's spinal cord is located lower than the adult's": "The infant's spinal cord terminates at a lower vertebral level than the adult's, resulting in more reflex pathways passing through the lumbar region and producing the upgoing toe response",
        "Infants have more pain receptors in their feet than adults": "Infants have a significantly higher density of pain and touch receptors in the plantar surface of their feet than adults, making them hypersensitive to the plantar stimulation",
        "Infants have weaker foot muscles that cannot resist the stimulus": "Infants have weaker intrinsic foot muscles that cannot resist the stroking stimulus, so the toes fan out passively rather than curling, and this resolves as foot muscles strengthen with age",
    },
    ("Unit4/Lesson4.7_Quiz.json", 16): {
        "A migraine headache with visual disturbances": "A migraine headache with visual disturbances such as aura, photophobia, and scintillating scotomas that typically last several hours before resolving",
        "A permanent stroke with lasting brain damage": "A permanent ischemic stroke with lasting brain damage caused by complete occlusion of a cerebral artery resulting in irreversible neuronal death",
        "A type of seizure that occurs during sleep": "A type of nocturnal seizure that occurs exclusively during sleep, involving repetitive abnormal electrical discharges in the temporal lobe cortex",
    },
    ("Unit4/Lesson4.7_Quiz.json", 18): {
        "Spinal cord damage caused by insulin injections": "Spinal cord damage caused by insulin injections near the vertebral column, leading to progressive myelopathy and lower extremity motor deficits",
        "An autoimmune condition where diabetes triggers MS": "An autoimmune condition where chronically elevated blood glucose in diabetes triggers the immune system to attack myelin sheaths, causing multiple sclerosis",
        "A condition where diabetes causes brain tumors": "A condition where chronic hyperglycemia from diabetes stimulates abnormal glial cell proliferation in the central nervous system, leading to brain tumors",
    },
    ("Unit4/Lesson4.7_Quiz.json", 21): {
        "Epilepsy; seizures have destroyed the hippocampus": "Epilepsy; repeated temporal lobe seizures have progressively destroyed hippocampal neurons through excitotoxicity, causing both anterograde and retrograde memory loss",
        "Multiple sclerosis; demyelination has shrunk the hippocampus": "Multiple sclerosis; progressive demyelination of hippocampal white matter tracts has caused significant hippocampal atrophy, leading to the gradual short-term memory deficits observed",
        "Parkinson's disease; the hippocampus controls motor coordination": "Parkinson's disease; the hippocampus is a major center for motor coordination and balance, and dopamine depletion in this region causes the progressive motor and memory symptoms observed",
    },
    ("Unit4/Lesson4.8_Quiz.json", 21): {
        "Hyperpolarization, threshold, repolarization, depolarization, resting": "Hyperpolarization (K+ efflux to -80 mV), threshold (-55 mV), repolarization (Na+ influx), depolarization (K+ efflux to +30 mV), then return to resting potential at -70 mV",
        "Depolarization only; the other changes are artifact": "Depolarization (Na+ influx to +30 mV) is the only real phase; the apparent repolarization and hyperpolarization seen on recordings are electrical artifacts from the equipment",
        "Repolarization, depolarization, resting potential, hyperpolarization": "Repolarization (K+ efflux from +30 mV back to -70 mV), depolarization (Na+ influx to +30 mV), resting potential (-70 mV steady state), hyperpolarization (K+ undershoot to -80 mV)",
    },
    ("Unit4/Lesson4.8_Quiz.json", 25): {
        "Neostigmine stops the autoimmune attack on ACh receptors": "Neostigmine stops the autoimmune attack on ACh receptors by suppressing the production of anti-acetylcholine receptor antibodies at the immune cell level",
        "Neostigmine increases the number of ACh receptors on the muscle": "Neostigmine increases the number of ACh receptors on the muscle end plate by stimulating the synthesis and insertion of new nicotinic receptors into the membrane",
        "Neostigmine directly stimulates the muscle fibers without needing ACh": "Neostigmine directly stimulates the muscle fibers by binding to nicotinic receptors itself and mimicking the depolarizing effect of ACh",
    },
    ("Unit4/Lesson4.8_Quiz.json", 28): {
        "The neuron would depolarize to +30 mV and stay there": "The neuron would depolarize to +30 mV and stay permanently depolarized because the K+ channels would be unable to repolarize the membrane",
        "The neuron would fire action potentials continuously": "The neuron would fire action potentials continuously and without any refractory period because the sustained K+ efflux would keep resetting the membrane",
        "There would be no effect on the action potential": "There would be no effect on the action potential because K+ channels are not involved in establishing or maintaining the resting membrane potential",
    },
    # UNIT 5
    ("Unit5/Lesson5.1_Quiz.json", 27): {
        "The endocrine system only functions during sleep": "The endocrine system only functions during sleep when the brain enters a parasympathetic state, and all hormone secretion ceases entirely during waking hours",
        "Insulin is a steroid hormone and all steroids act slowly": "Insulin is a steroid hormone derived from cholesterol, and all steroid hormones act slowly because they must diffuse through the cell membrane and bind intracellular receptors",
        "The nervous system uses hormones that work faster than endocrine hormones": "The nervous system uses specialized neurosecretory hormones that are structurally different from endocrine hormones and travel through dedicated neural channels much faster than blood",
    },
    ("Unit5/Lesson5.2_Quiz.json", 15): {
        "A pancreatic hormone that regulates blood sugar": "A pancreatic hormone that regulates blood sugar by promoting glucose uptake into cells and stimulating glycogen synthesis in the liver and skeletal muscles",
        "A hormone from the thyroid that lowers blood calcium": "A hormone produced by the parafollicular C cells of the thyroid gland that lowers blood calcium by inhibiting osteoclast activity and promoting calcium deposition in bone",
        "A pituitary hormone that controls growth": "A pituitary hormone that controls longitudinal bone growth and overall somatic development by stimulating hepatic production of insulin-like growth factors",
    },
    ("Unit5/Lesson5.2_Quiz.json", 17): {
        "A part of the adrenal gland": "A part of the adrenal gland that secretes catecholamines, located deep within the adrenal medulla superior to the kidneys",
        "An endocrine gland that produces thyroid hormones": "An endocrine gland that produces thyroid hormones T3 and T4 in the anterior neck, regulated by TSH from the anterior pituitary",
        "A gland located in the neck that regulates calcium": "A gland located on the posterior surface of the thyroid in the neck that regulates calcium homeostasis through parathyroid hormone",
    },
    ("Unit5/Lesson5.3_Quiz.json", 17): {
        "The autoimmune destruction of pancreatic beta cells": "The autoimmune destruction of pancreatic beta cells by T lymphocytes, resulting in absolute insulin deficiency that requires lifelong exogenous insulin replacement therapy",
        "An allergy to insulin injections": "An allergic hypersensitivity reaction to exogenous insulin injections, causing localized inflammation and tissue necrosis at the injection site",
        "A condition where the pancreas produces too much insulin": "A condition where the pancreatic beta cells produce excessive amounts of insulin, leading to chronic hypoglycemia and recurrent episodes of confusion and unconsciousness",
    },
    ("Unit5/Lesson5.3_Quiz.json", 20): {
        "A hormone that regulates blood glucose levels": "A hormone that regulates blood glucose levels by promoting cellular uptake and hepatic storage of glucose in response to elevated postprandial blood sugar concentrations",
        "A type of bone cell that stores minerals": "A type of bone cell embedded in the mineralized matrix that stores calcium and phosphate and helps maintain the structural integrity of the skeletal system",
        "A vitamin that helps absorb minerals from the intestine": "A fat-soluble vitamin that enhances the intestinal absorption of dietary calcium and phosphate, working synergistically with parathyroid hormone to maintain mineral homeostasis",
    },
    ("Unit5/Lesson5.5_Quiz.json", 8): {
        "It never occurs in adults": "It never occurs in adults because growth hormone secretion ceases entirely after puberty",
        "During fetal development only": "During fetal development only, when growth hormone receptors are most abundant",
        "During infancy exclusively": "During infancy exclusively, before the pituitary gland fully matures",
    },
    ("Unit5/Lesson5.5_Quiz.json", 10): {
        "Pancreatic islets": "Pancreatic islets secreting excess insulin causing recurrent hypoglycemic episodes",
        "Anterior pituitary gland": "Anterior pituitary gland producing excess prolactin causing galactorrhea",
        "Thyroid gland": "Thyroid gland producing excess T3 and T4 causing metabolic acceleration",
    },
    ("Unit5/Lesson5.5_Quiz.json", 12): {
        "A tumor growing behind the eye": "A tumor growing behind the eye within the orbital cavity that mechanically pushes the globe forward, often associated with pituitary adenomas",
        "Blurred vision caused by diabetes": "Blurred vision caused by diabetic retinopathy, where chronically elevated blood glucose damages the retinal microvasculature and causes macular edema",
        "A condition of sunken eyes due to hypothyroidism": "A condition of sunken and recessed eyes due to hypothyroidism, where decreased metabolic activity causes orbital fat wasting and periorbital tissue atrophy",
    },
    ("Unit5/Lesson5.5_Quiz.json", 16): {
        "A form of pituitary dwarfism in teenagers": "A form of pituitary dwarfism in teenagers caused by growth hormone deficiency, resulting in proportionally short stature but normal cognitive development",
        "Excess thyroid hormone in adults causing weight loss": "Excess thyroid hormone production in adults causing significant weight loss, heat intolerance, tachycardia, and increased basal metabolic rate",
        "An adrenal tumor found in newborns": "An adrenal tumor found in newborns that secretes excess cortisol, causing premature bone maturation and early closure of growth plates",
    },
    ("Unit5/Lesson5.5_Quiz.json", 18): {
        "A type of kidney cancer": "A type of kidney cancer originating in the renal tubular epithelium that disrupts normal fluid reabsorption and causes electrolyte imbalances and polyuria",
        "A condition caused by excess insulin leading to low blood sugar": "A condition caused by excess insulin secretion from a pancreatic insulinoma, leading to chronic low blood sugar, confusion, diaphoresis, and recurrent hypoglycemic episodes",
        "A form of diabetes caused by insulin deficiency": "A form of diabetes mellitus caused by absolute insulin deficiency from autoimmune beta cell destruction, leading to hyperglycemia, ketosis, and metabolic acidosis",
    },
    ("Unit5/Lesson5.5_Quiz.json", 19): {
        "A condition of abnormally low thyroid hormone levels": "A condition of abnormally low thyroid hormone levels causing decreased metabolism, weight gain, fatigue, cold intolerance, and myxedema",
        "An enlarged thyroid gland with normal function": "An enlarged thyroid gland (goiter) with normal hormone production and function, caused by iodine deficiency or benign nodular hyperplasia",
        "A normal state of thyroid function": "A normal euthyroid state in which the thyroid gland produces adequate T3 and T4 within the reference range for healthy metabolism",
    },
    ("Unit5/Lesson5.5_Quiz.json", 20): {
        "An autoimmune condition attacking the pituitary gland": "An autoimmune condition in which antibodies attack the anterior pituitary gland, progressively destroying hormone-secreting cells and causing panhypopituitarism",
        "Growth hormone deficiency in children causing short stature": "Growth hormone deficiency in children causing proportional short stature, delayed bone age, and reduced growth velocity despite adequate nutrition",
        "A calcium disorder causing bone loss": "A calcium metabolism disorder caused by hyperparathyroidism that accelerates osteoclast-mediated bone resorption, leading to progressive bone density loss",
    },
    ("Unit5/Lesson5.5_Quiz.json", 25): {
        "Osteoporosis causing bone remodeling": "Osteoporosis causing excessive bone remodeling and resorption, resulting in progressive skeletal enlargement of the hands, feet, and jaw",
        "Gigantism from excess GH during childhood": "Gigantism from excess growth hormone during childhood before epiphyseal plate closure, causing proportional overgrowth of all skeletal elements",
        "Pituitary dwarfism from GH deficiency": "Pituitary dwarfism from growth hormone deficiency during childhood, causing proportionally reduced skeletal growth and short stature",
    },
    ("Unit5/Lesson5.5_Quiz.json", 26): {
        "Graves' disease, which will resolve on its own": "Graves' disease, an autoimmune hyperthyroid condition that typically resolves spontaneously in infants and requires only monitoring and supportive care",
        "Normal developmental variation that needs no intervention": "Normal developmental variation that needs no intervention, as some infants naturally display temporary lethargy, feeding difficulty, and delayed milestones that resolve by age two",
        "Type 1 diabetes requiring insulin treatment": "Type 1 diabetes requiring immediate insulin treatment, as autoimmune pancreatic beta cell destruction in infancy causes severe hyperglycemia and growth failure",
    },
    ("Unit5/Lesson5.5_Quiz.json", 27): {
        "Pheochromocytoma from excess catecholamines": "Pheochromocytoma from an adrenal medulla tumor producing excess catecholamines, causing episodic hypertension, headaches, palpitations, and diaphoresis",
        "Cushing's syndrome from excess cortisol": "Cushing's syndrome from excess cortisol produced by an adrenal adenoma, causing central obesity, moon face, proximal muscle weakness, and hypertension",
        "Addison's disease from adrenal insufficiency": "Addison's disease from primary adrenal insufficiency causing inadequate cortisol and aldosterone production, leading to hypotension, fatigue, and hyperpigmentation",
    },
    ("Unit5/Lesson5.5_Quiz.json", 28): {
        "Type 2 diabetes from insulin resistance": "Type 2 diabetes from insulin resistance at the cellular level, causing chronic hyperglycemia, polyuria, polydipsia, and gradual peripheral nerve damage",
        "Conn's syndrome from excess aldosterone": "Conn's syndrome from excess aldosterone secreted by an adrenal adenoma, causing sodium retention, potassium wasting, metabolic alkalosis, and hypertension",
        "Addison's disease from adrenal cortex failure": "Addison's disease from autoimmune adrenal cortex failure causing deficient cortisol and aldosterone production, resulting in hypotension, fatigue, and salt craving",
    },
    ("Unit5/Lesson5.6_Quiz.json", 7): {
        "Thyroid disease": "Thyroid disease affecting T3/T4 metabolism and energy balance",
        "Type 2 diabetes": "Type 2 diabetes involving chronic peripheral insulin resistance",
        "Adrenal disease": "Adrenal disease affecting cortisol and aldosterone secretion",
    },
    ("Unit5/Lesson5.6_Quiz.json", 11): {
        "A measure of hemoglobin's oxygen-carrying capacity": "A measure of hemoglobin's oxygen-carrying capacity, indicating how effectively red blood cells transport oxygen from the lungs to peripheral tissues",
        "A type of white blood cell involved in immune defense": "A type of white blood cell involved in adaptive immune defense, specifically responsible for producing antibodies against foreign antigens in the bloodstream",
        "A liver enzyme used to assess liver function": "A liver enzyme used to assess hepatocyte integrity and liver function, with elevated levels indicating hepatocellular damage or cholestatic disease",
    },
    ("Unit5/Lesson5.6_Quiz.json", 12): {
        "A condition of low blood sugar from too much insulin": "A condition of dangerously low blood sugar caused by excessive insulin administration, leading to neuroglycopenia, confusion, diaphoresis, and potential loss of consciousness",
        "A chronic condition of slow glucose metabolism": "A chronic condition of abnormally slow glucose metabolism in the liver and peripheral tissues, causing gradual accumulation of glycogen deposits and progressive hepatomegaly",
        "An allergic reaction to diabetes medication": "An allergic hypersensitivity reaction to oral diabetes medication, causing urticaria, angioedema, and potentially life-threatening anaphylaxis requiring immediate epinephrine",
    },
    ("Unit5/Lesson5.6_Quiz.json", 13): {
        "A gradual worsening of hypothyroidism over months": "A gradual worsening of hypothyroidism over several months, characterized by progressive fatigue, weight gain, cold intolerance, bradycardia, and eventual myxedema coma if untreated",
        "A type of thyroid surgery": "A type of thyroid surgery involving subtotal or complete removal of the thyroid gland, performed under general anesthesia to treat refractory hyperthyroidism or thyroid malignancy",
        "A weather pattern that affects thyroid function": "A seasonal weather pattern that affects thyroid function by altering hypothalamic thermoregulatory signals, causing cyclical fluctuations in TSH and thyroid hormone production",
    },
    ("Unit5/Lesson5.6_Quiz.json", 14): {
        "Antibodies that the thyroid produces against foreign organisms": "Antibodies that the thyroid gland itself produces against foreign organisms and pathogens, serving as a localized immune defense mechanism within the cervical endocrine tissue",
        "Antibodies that protect the thyroid from infection": "Antibodies that protect the thyroid gland from bacterial and viral infection by forming a localized immune barrier around the follicular cells and colloid-filled lumen",
        "A medication given to patients with thyroid cancer": "A medication given to patients with thyroid cancer that mimics the structure of thyroid peroxidase to competitively inhibit remaining malignant thyroid cells from synthesizing hormones",
    },
    ("Unit5/Lesson5.6_Quiz.json", 18): {
        "A test that measures how quickly the stomach digests food": "A test that measures how quickly the stomach digests food by tracking a radiolabeled meal through the gastrointestinal tract and calculating gastric emptying time over four hours",
        "A urine test for glucose performed at home": "A urine test for glucose performed at home using reagent dipsticks that detect glycosuria, providing a rough estimate of blood glucose when direct measurement is unavailable",
        "A test that measures insulin levels after fasting overnight": "A test that measures fasting insulin levels after an overnight twelve-hour fast, assessing pancreatic beta cell function and the degree of peripheral insulin resistance",
    },
    ("Unit5/Lesson5.6_Quiz.json", 23): {
        "Lower doses would cause the infection to worsen by stimulating bacterial growth": "Lower doses of prednisone would cause the infection to worsen by directly stimulating bacterial growth, as cortisol at low concentrations provides a nutritive substrate that promotes pathogen proliferation",
        "Higher steroids directly fight the infection by killing bacteria": "Higher doses of steroids directly fight the infection by killing bacteria through a direct bactericidal mechanism, as cortisol at pharmacological doses disrupts bacterial cell membranes and inhibits replication",
        "Prednisone acts as an antibiotic at higher doses": "Prednisone acts as a broad-spectrum antibiotic at higher doses, directly inhibiting bacterial protein synthesis through a mechanism similar to macrolide antibiotics like azithromycin",
    },
    ("Unit5/Lesson5.6_Quiz.json", 24): {
        "Fasting glucose tests are always inaccurate": "Fasting glucose tests are always inaccurate because they only capture a single moment in time and are affected by stress hormones, recent exercise, and normal diurnal cortisol fluctuations",
        "Fasting glucose only measures glucagon levels, not actual glucose": "Fasting glucose only measures glucagon levels released by pancreatic alpha cells during the fasting state, not the actual glucose concentration circulating in the blood",
        "HbA1c is easier to perform in a lab than fasting glucose": "HbA1c is technically easier to perform in a clinical laboratory than fasting glucose because it does not require the patient to fast, uses a simpler assay, and has fewer preanalytical variables",
    },
    ("Unit5/Lesson5.6_Quiz.json", 26): {
        "Hypothyroidism secondary to diabetes": "Hypothyroidism secondary to diabetes, where chronic hyperglycemia suppresses thyroid-stimulating hormone production and leads to progressive thyroid gland atrophy",
        "Diabetic nephropathy causing kidney failure": "Diabetic nephropathy causing progressive kidney failure, where chronic hyperglycemia damages the glomerular capillaries and leads to proteinuria and declining filtration",
        "Diabetic retinopathy affecting the eyes": "Diabetic retinopathy affecting the eyes, where chronic hyperglycemia damages the retinal microvasculature causing hemorrhages, exudates, and progressive vision loss",
    },
    ("Unit5/Lesson5.6_Quiz.json", 30): {
        "Monitoring is only necessary when the patient feels sick": "Monitoring blood glucose is only necessary when the patient feels symptomatic or acutely ill, because subjective symptoms reliably correlate with actual blood glucose concentrations",
        "Monitoring is required by law for all diabetic patients": "Monitoring blood glucose is legally required for all diabetic patients as a public health mandate, and failure to maintain records can result in penalties and loss of prescription access",
        "Symptoms always appear before blood sugar reaches dangerous levels": "Symptoms of hyperglycemia and hypoglycemia always appear well before blood sugar reaches dangerous levels, giving patients ample warning to self-correct with medication or dietary changes",
    },
    ("Unit5/Lesson5.7_Quiz.json", 14): {
        "Failure of the hypothalamus to produce releasing hormones": "Failure of the hypothalamus to produce adequate releasing hormones, resulting in diminished pituitary tropic hormone secretion and downstream target gland hypofunction",
        "Failure of hormone receptors on target tissues": "Failure of hormone receptors on target tissues to respond to circulating hormones, resulting in end-organ resistance despite normal or elevated hormone levels",
        "The first endocrine disease a patient ever develops": "The first endocrine disease that a patient ever develops in their lifetime, regardless of the anatomical origin of the hormonal dysfunction or the gland involved",
    },
    ("Unit5/Lesson5.7_Quiz.json", 16): {
        "The third endocrine disease diagnosed in a patient": "The third endocrine disease sequentially diagnosed in a patient, following primary and secondary disorders, regardless of the anatomical level of dysfunction",
        "The mildest form of any endocrine disorder": "The mildest form of any endocrine disorder, characterized by minimal hormonal imbalance and subtle clinical symptoms that rarely require medical intervention",
        "A condition that only occurs in the third decade of life": "A condition that only occurs in the third decade of life due to age-related changes in hypothalamic sensitivity to feedback signals from peripheral endocrine glands",
    },
    ("Unit5/Lesson5.7_Quiz.json", 18): {
        "An enzyme that destroys hormones after they bind to receptors": "An enzyme that destroys hormones after they bind to receptors by cleaving the hormone-receptor complex, terminating the signal and preventing prolonged gene activation",
        "A cell-surface receptor for water-soluble hormones": "A cell-surface receptor for water-soluble hormones that activates intracellular second messenger cascades such as cAMP or IP3 when bound by peptide hormones",
        "A second messenger molecule like cAMP": "A second messenger molecule like cAMP that relays the hormonal signal from the cell surface receptor to intracellular protein kinases and downstream effectors",
    },
    ("Unit5/Lesson5.7_Quiz.json", 19): {
        "The general systemic blood circulation throughout the body": "The general systemic blood circulation throughout the body that carries hormones from all endocrine glands to every tissue without any specialized vascular connections",
        "A nerve pathway from the brain to the pituitary": "A direct nerve pathway from the cerebral cortex to the anterior pituitary that transmits electrical signals rather than hormonal signals to regulate gland function",
        "A portal vein connecting the intestines to the liver": "A portal vein connecting the intestines to the liver that carries absorbed nutrients and gut hormones for first-pass hepatic metabolism before systemic distribution",
    },
    ("Unit5/Lesson5.7_Quiz.json", 21): {
        "Primary hypothyroidism, because both values are low": "Primary hypothyroidism, because both TSH and T4 are low, indicating the thyroid gland itself has failed to produce adequate hormone and the pituitary is also unable to compensate",
        "Hyperthyroidism, because TSH is suppressed": "Hyperthyroidism, because the suppressed TSH indicates excessive negative feedback from high circulating thyroid hormones, even though the T4 level appears paradoxically low",
        "Normal thyroid function with a lab error": "Normal thyroid function with a laboratory error, because simultaneous low TSH and low T4 values are physiologically impossible and must represent a specimen collection or assay problem",
    },
    ("Unit5/Lesson5.7_Quiz.json", 24): {
        "All three are elevated equally": "TRH high, TSH high, T4 high: all three are elevated equally because the autoantibodies stimulate every level of the hypothalamic-pituitary-thyroid axis simultaneously",
        "TRH low, TSH high, T4 low": "TRH low, TSH high, T4 low: the high TSH reflects pituitary compensation for low thyroid output, while TRH decreases because the hypothalamus senses elevated TSH",
        "TRH high, TSH high, T4 high": "TRH high, TSH high, T4 high: the autoantibodies stimulate the thyroid while the hypothalamus and pituitary both increase output because they cannot detect the autoimmune stimulus",
    },
    ("Unit5/Lesson5.7_Quiz.json", 25): {
        "ACTH would be normal in both cases": "ACTH would be normal in both cases because the hypothalamus compensates by adjusting CRH output to maintain ACTH at baseline regardless of adrenal or pituitary status",
        "ACTH would be low in both cases": "ACTH would be low in both cases because the loss of either the adrenal glands or the pituitary gland eliminates the positive feedback loop that sustains ACTH secretion",
        "ACTH would be high in both cases": "ACTH would be high in both cases because the stress of surgery triggers a maximal hypothalamic CRH response that overrides any negative feedback mechanisms",
    },
    ("Unit5/Lesson5.7_Quiz.json", 26): {
        "Synergism between insulin and thyroid hormones": "Synergism between insulin and thyroid hormones, where both work together to amplify glucose uptake into cells, and the loss of thyroid hormones also impairs insulin signaling",
        "Antagonism between thyroid hormones and catecholamines": "Antagonism between thyroid hormones and catecholamines, where thyroid hormones normally suppress catecholamine production and low thyroid levels lead to catecholamine excess",
        "Positive feedback between low thyroid and low catecholamines": "Positive feedback between low thyroid hormone levels and low catecholamine activity, where each decrease amplifies the other in a downward spiral of hormonal insufficiency",
    },
    ("Unit5/Lesson5.7_Quiz.json", 27): {
        "Insulin, glucagon, and cortisol all lower blood glucose together": "Insulin, glucagon, and cortisol all lower blood glucose together through complementary mechanisms: insulin promotes cellular uptake, glucagon inhibits hepatic output, and cortisol enhances peripheral utilization",
        "Calcitonin, PTH, and ADH regulate glucose through calcium signaling": "Calcitonin, PTH, and ADH regulate blood glucose through calcium signaling pathways: calcium ions serve as second messengers that modulate insulin secretion and glucose transporter activity",
        "Only glucagon raises blood glucose; no other hormones are involved": "Only glucagon raises blood glucose through hepatic glycogenolysis; no other hormones are involved in the counter-regulatory response, and cortisol and epinephrine have no effect on glucose metabolism",
    },
    ("Unit5/Lesson5.7_Quiz.json", 28): {
        "Steroid hormones are always more potent than peptide hormones": "Steroid hormones are always more potent than peptide hormones at any given concentration because they directly alter gene expression, making dosing differences irrelevant in clinical practice",
        "All hormones have the same half-life once they reach the bloodstream": "All hormones have the same half-life once they reach the bloodstream because hepatic and renal clearance mechanisms process all hormone types at the same rate regardless of structure",
        "There is no clinical significance to half-life differences": "There is no clinical significance to half-life differences between hormone types, and all replacement therapies can be administered on the same once-daily schedule regardless of hormone class",
    },
    ("Unit5/Lesson5.7_Quiz.json", 29): {
        "Low BP activates the thyroid to produce T3 which increases heart rate": "Low BP activates the thyroid to produce T3 which increases heart rate and cardiac output, while simultaneously stimulating aldosterone secretion from the adrenal cortex to retain sodium",
        "Low BP triggers the posterior pituitary to release oxytocin, which constricts blood vessels": "Low BP triggers the posterior pituitary to release oxytocin, which constricts peripheral blood vessels and stimulates the kidneys to retain water, directly restoring blood volume and pressure",
        "Low BP activates the adrenal medulla to release cortisol, which retains water": "Low BP activates the adrenal medulla to release cortisol, which acts on the kidneys to retain sodium and water while simultaneously constricting the peripheral vasculature to raise pressure",
    },
    ("Unit5/Lesson5.7_Quiz.json", 30): {
        "GnRH and LH increase to balance the extra testosterone, maintaining normal sperm production": "GnRH and LH increase to balance the extra testosterone through a positive feedback mechanism, maintaining normal intratesticular testosterone levels and preserving normal sperm production",
        "All hormone levels increase proportionally with the exogenous testosterone": "All hormone levels increase proportionally with the exogenous testosterone because the hypothalamic-pituitary-gonadal axis amplifies the signal through positive feedback at every level",
        "Only FSH decreases while all other hormones remain normal": "Only FSH decreases while GnRH, LH, and testosterone all remain normal because FSH is the only gonadotropin sensitive to circulating testosterone levels through selective negative feedback",
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

# Verify both units
for unit in ['Unit4', 'Unit5']:
    files = sorted(glob.glob(os.path.join(base, unit, '*Quiz*.json')))
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
            cl = len(correct_text)
            awl = sum(len(w) for w in wrong_texts) / len(wrong_texts)
            if awl > 0 and cl / awl >= 3.0:
                still_flagged += 1
                print(f'STILL FLAGGED: {unit}/{os.path.basename(f)} Q{q["question_number"]}: ratio={cl/awl:.1f}')
    if still_flagged == 0:
        print(f"{unit}: ALL CLEAR!")
    else:
        print(f"{unit}: {still_flagged} still flagged")
