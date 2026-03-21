import json
d = json.load(open("content_data/integrated_science_lessons.json", "r", encoding="utf-8"))
# Check U1 question quality
qs = d["u1_l1.1"]["quiz_questions"][:2]
print("=== U1 L1.1 ===")
for q in qs:
    print(q["question_text"])
    for o in q["options"]:
        mark = "*" if o["is_correct"] else " "
        print(f"  [{mark}] {o['text']}")
    print(f"  Expl: {q.get('explanation','')}")
    print()

# Check U2 question quality
qs2 = d["u2_l2.1"]["quiz_questions"][:2]
print("=== U2 L2.1 ===")
for q in qs2:
    print(q["question_text"])
    for o in q["options"]:
        mark = "*" if o["is_correct"] else " "
        print(f"  [{mark}] {o['text']}")
    print(f"  Expl: {q.get('explanation','')}")
    print()
