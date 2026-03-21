import json

with open("content_data/linear_algebra_lessons.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for k in sorted(data.keys()):
    v = data[k]
    if isinstance(v, dict) and "quiz_questions" in v:
        qs = v["quiz_questions"]
        placeholders = sum(1 for q in qs if "Sample question" in q.get("question_text", "") or "Option A" in str(q.get("options", [])))
        title = v.get("title", "?")[:55]
        print(f"{k}: {len(qs)}q, {placeholders} placeholder, {title}")
