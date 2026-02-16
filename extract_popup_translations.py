import re
import os

files = ["ArisEdu Project Folder/chem.html", "ArisEdu Project Folder/bio.html", "ArisEdu Project Folder/physics.html", "ArisEdu Project Folder/algebra1.html", "ArisEdu Project Folder/algebra2.html", "ArisEdu Project Folder/geometry.html"]
translations = set()

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            # onmouseenter="showLessonPopup(event, 'Some String')"
            matches = re.findall(r"showLessonPopup\s*\(\s*event\s*,\s*['\"]([^'\"]+)['\"]\s*\)", content)
            for m in matches:
                translations.add(m)

print(f"Found {len(translations)} unique popup strings.")
# Generate JSON output for review/injection
import json
print(json.dumps(list(translations)))
