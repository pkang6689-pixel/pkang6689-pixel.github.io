import json
data = json.load(open("content_data/linear_algebra_lessons.json", "r", encoding="utf-8"))
for k in sorted(data):
    if k.startswith("u7_") or k.startswith("u8_"):
        qs = data[k].get("quiz_questions", [])
        ph = sum(1 for q in qs if "Sample question" in q.get("question_text", ""))
        print(f"{k}: {len(qs)} questions, {ph} placeholders")
