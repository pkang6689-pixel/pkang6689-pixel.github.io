import json
data=json.load(open('content_data/biology_lessons.json','r',encoding='utf-8'))
for k in sorted(data.keys(), key=lambda x: (data[x]['unit'], x)):
    v=data[k]
    qc=len(v.get('quiz_questions',[]))
    if qc<20:
        print(f"{k}: U{v['unit']} - {v['title']} ({qc}q)")
