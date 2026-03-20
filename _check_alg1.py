import json, os
PATH = os.path.join("content_data", "algebra_1_lessons.json")
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
keys = sorted(data.keys(), key=lambda k: [float(x) for x in k.replace("u","").replace("l","").split("_") if x])
for k in keys:
    n = len(data[k].get("quiz_questions", []))
    title = ""
    ss = data[k].get("summary_sections", [])
    if ss:
        t = ss[0].get("title","")
        title = t[:60]
    print(f"{k:20s}  q={n:2d}  {title}")
