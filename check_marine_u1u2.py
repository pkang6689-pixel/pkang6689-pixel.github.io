import json
d = json.load(open('content_data/marine_science_lessons.json', 'r', encoding='utf-8'))
for u in range(1, 3):
    prefix = f"u{u}_l{u}."
    for k in sorted(d.keys()):
        if k.startswith(prefix):
            qs = d[k]["quiz_questions"]
            placeholders = sum(1 for q in qs if "Sample" in q["question_text"])
            print(f"{k}: {len(qs)} qs, {placeholders} placeholders — {qs[0]['question_text'][:60]}")
