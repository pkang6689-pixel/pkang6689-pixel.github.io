import json
d = json.load(open("content_data/integrated_science_lessons.json", "r", encoding="utf-8"))
keys = sorted([k for k in d if k.startswith("u3_")])
for k in keys:
    title = d[k]["title"]
    qs = d[k].get("quiz_questions", [])
    ph = sum(1 for q in qs if "Sample question" in q.get("question_text","") or "placeholder" in q.get("question_text","").lower())
    print(f"{k}: {title}  ({len(qs)} qs, {ph} ph)")
