import os, json

base = r'c:\Users\Peter\pkang6689-pixel.github.io\content_data'
results = {}

for subject in sorted(os.listdir(base)):
    subj_path = os.path.join(base, subject)
    if not os.path.isdir(subj_path):
        continue
    lessons = []
    for unit in sorted(os.listdir(subj_path)):
        unit_path = os.path.join(subj_path, unit)
        if not os.path.isdir(unit_path):
            continue
        for fname in sorted(os.listdir(unit_path)):
            if not fname.endswith('.json'):
                continue
            lesson_id = fname[:-5]
            fpath = os.path.join(unit_path, fname)
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                title = (data.get('title') or data.get('name') or
                         data.get('lessonName') or data.get('lesson_title') or
                         data.get('lessonTitle') or '')
                lessons.append((lesson_id, title))
            except Exception as e:
                lessons.append((lesson_id, f'ERROR: {e}'))
    results[subject] = lessons

import re
out_path = r'c:\Users\Peter\pkang6689-pixel.github.io\_lessons_output.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    for subj, lessons in results.items():
        # Deduplicate: strip _Practice/_Quiz/_Summary suffix
        seen = {}
        for lid, title in lessons:
            base = re.sub(r'_(Practice|Quiz|Summary)$', '', lid)
            if base not in seen:
                seen[base] = title
        out.write(f'\n=== {subj} ===\n')
        for base_id, title in seen.items():
            out.write(f'  {base_id}: {title}\n')
print('Done. Written to', out_path)
