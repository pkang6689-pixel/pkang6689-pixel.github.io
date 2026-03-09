import json
with open('content_data/anatomy_lessons.json', encoding='utf-8') as f:
    d = json.load(f)
count = 0
total = len(d)
for v in d.values():
    if 'coming soon' in str(v).lower():
        count += 1
print(f'Placeholders: {count} / Total lessons: {total}')
