import json
data = json.load(open("content_data/marine_science_lessons.json", "r", encoding="utf-8"))
for k in sorted(data, key=lambda x: (int(x.split('_')[0][1:]), float(x.split('l')[1]) if 'l' in x else 0)):
    title = data[k].get("title", "?")
    qs = data[k].get("quiz_questions", [])
    ph = sum(1 for q in qs if "Sample question" in q.get("question_text", ""))
    print(f"{k}: {title}  ({len(qs)} qs, {ph} ph)")
