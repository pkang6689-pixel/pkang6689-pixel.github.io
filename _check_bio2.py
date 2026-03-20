import json
data=json.load(open('content_data/biology_lessons.json','r',encoding='utf-8'))
for k in sorted(data.keys(), key=lambda x: (data[x]['unit'], x)):
    v=data[k]
    qc=len(v.get('quiz_questions',[]))
    if qc<20:
        # Get topic from first quiz question or flashcard
        hint = ""
        if v.get('quiz_questions'):
            hint = v['quiz_questions'][0].get('question_text','')[:80]
        elif v.get('flashcards'):
            hint = v['flashcards'][0].get('term','')
        sc = ""
        if v.get('summary_sections') and v['summary_sections']:
            sc = v['summary_sections'][0].get('title','')[:60]
        print(f"{k}: U{v['unit']} | title='{v.get('title','')}' | sec='{sc}' | q1='{hint}'")
