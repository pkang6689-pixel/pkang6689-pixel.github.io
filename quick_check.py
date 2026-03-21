import json, os
from collections import Counter

COURSES = [
    "algebra_1", "algebra_2", "anatomy", "astronomy", "biology",
    "chemistry", "earth_science", "environmental_science", "financial_math",
    "geometry", "integrated_science", "linear_algebra", "marine_science",
    "physics", "precalculus", "statistics", "trigonometry"
]

for c in COURSES:
    path = os.path.join("content_data", f"{c}_lessons.json")
    d = json.load(open(path, "r", encoding="utf-8"))
    pos = Counter()
    total = 0
    longest_correct = 0
    no_correct = 0
    dup_in = 0
    empty_expl = 0
    for lid in sorted(d.keys()):
        seen = set()
        for q in d[lid].get("quiz_questions", []):
            opts = q.get("options", [])
            # position
            found_correct = False
            for oi, o in enumerate(opts):
                if isinstance(o, dict) and o.get("is_correct"):
                    pos[oi] += 1
                    total += 1
                    found_correct = True
            if not found_correct and len(opts) == 4:
                no_correct += 1
            # longest = correct
            if len(opts) == 4:
                correct_opt = next((o for o in opts if isinstance(o, dict) and o.get("is_correct")), None)
                if correct_opt:
                    cl = len(correct_opt["text"])
                    ml = max((len(o["text"]) for o in opts if isinstance(o, dict) and not o.get("is_correct")), default=0)
                    if cl > ml:
                        longest_correct += 1
            # dup
            qt = q.get("question_text", "").strip().lower()
            if qt in seen:
                dup_in += 1
            seen.add(qt)
            # explanation
            expl = q.get("explanation", "")
            if not expl or len(expl.strip()) < 10:
                empty_expl += 1

    dist = " ".join(f"[{i}]:{pos[i]*100//total}%" for i in range(4)) if total else "none"
    lc_pct = longest_correct * 100 // total if total else 0
    flags = []
    if no_correct: flags.append(f"no_correct={no_correct}")
    if dup_in: flags.append(f"dup_in={dup_in}")
    if empty_expl: flags.append(f"empty_expl={empty_expl}")
    extra = " | " + ", ".join(flags) if flags else ""
    print(f"{c:<25} {total:>5} qs | pos: {dist} | longest=correct: {lc_pct}%{extra}")
