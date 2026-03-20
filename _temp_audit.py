import json

# Biology: show title vs summary_section title for all lessons
with open('content_data/biology_lessons.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

units = {}
for k, v in data.items():
    u = v['unit']
    units.setdefault(u, [])
    st = v['summary_sections'][0]['title'] if v['summary_sections'] else 'NO SUMMARY'
    units[u].append((k, v['title'], st))

for u in sorted(units.keys()):
    ls = units[u]
    print(f'Unit {u} ({len(ls)} lessons)')
    for k, t, st in ls:
        print(f'  {k}: title="{t}" | summary_title="{st}"')
    print()
