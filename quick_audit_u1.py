import json
d = json.load(open("content_data/integrated_science_lessons.json", "r", encoding="utf-8"))
total = lc = ph = 0
for key in sorted(k for k in d if k.startswith("u1_")):
    qs = d[key].get("quiz_questions", [])
    for q in qs:
        total += 1
        opts = q.get("options", [])
        if not opts: continue
        lengths = [len(o["text"]) for o in opts]
        correct_lens = [len(o["text"]) for o in opts if o.get("is_correct")]
        if correct_lens and correct_lens[0] == max(lengths):
            lc += 1
        if any("(" in o["text"] for o in opts if o.get("is_correct")):
            ph += 1
print(f"U1: {total} qs | longest=correct: {lc} ({lc/total*100:.0f}%) | paren hints: {ph} ({ph/total*100:.0f}%)")
