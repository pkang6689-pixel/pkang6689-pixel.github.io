import json
d = json.load(open('geometry_translation_dict.json', encoding='utf-8'))
print(len(d), 'total translations')
checks = ['Our Courses', 'Mathematics', 'Science', 'High School: Geometry', 
           'Unit 1', 'Unit 8 Test', 'Submit Answer', 'Back to Geometry', 'Get Started Today']
for c in checks:
    print(f'  {c}: {d.get(c, "MISSING")}')
