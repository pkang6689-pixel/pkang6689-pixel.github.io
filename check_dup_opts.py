import json
COURSES=['algebra_1','algebra_2','anatomy','astronomy','biology','chemistry','earth_science','environmental_science','financial_math','geometry','integrated_science','linear_algebra','marine_science','physics','precalculus','statistics','trigonometry']
count = 0
for c in COURSES:
    d = json.load(open(f'content_data/{c}_lessons.json','r',encoding='utf-8'))
    for lid in sorted(d):
        for qi,q in enumerate(d[lid].get('quiz_questions',[])):
            opts = q.get('options',[])
            texts = [o.get('text','').strip().lower() for o in opts if isinstance(o,dict)]
            if len(texts) != len(set(texts)):
                count += 1
                if count <= 20:
                    qt = q.get('question_text','')[:60]
                    print(f"\n{c} {lid} q{qi}: {qt}")
                    for oi,o in enumerate(opts):
                        cor = '*' if o.get('is_correct') else ' '
                        print(f"  {cor} [{oi}] {o['text']}")
print(f"\nTotal duplicate-option questions: {count}")
