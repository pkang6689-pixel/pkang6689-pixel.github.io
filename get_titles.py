import json, os
base = 'content_data/AstronomyLessons'
for u in range(4, 11):
    udir = os.path.join(base, f'Unit{u}')
    for f in sorted(os.listdir(udir)):
        if f.endswith('_Quiz.json'):
            d = json.load(open(os.path.join(udir, f), encoding='utf-8'))
            title = d.get('title', '?')
            print(f'Unit{u}/{f}: {title}')
    print()
