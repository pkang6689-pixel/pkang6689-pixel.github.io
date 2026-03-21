import json
d = json.load(open("content_data/integrated_science_lessons.json", "r", encoding="utf-8"))
qs = d["u3_l3.1"]["quiz_questions"][:3]
for q in qs:
    print(q["question_text"])
    for o in q["options"]:
        mark = "*" if o["is_correct"] else " "
        print(f"  [{mark}] {o['text']}")
    print(f"  Expl: {q.get('explanation','')}")
    print()
