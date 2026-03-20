import json, os
PATH = os.path.join("content_data", "algebra_1_lessons.json")
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
keys = sorted(data.keys(), key=lambda k: [float(x) for x in k.replace("u","").replace("l","").split("_") if x])
for k in keys:
    qs = data[k].get("quiz_questions", [])
    q1 = qs[0]["question_text"][:80] if qs else "NO Q"
    print(f"{k:20s}  {q1}")
