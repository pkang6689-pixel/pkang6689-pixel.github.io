
import re

LOG_FILE = "ArisEdu Project Folder/scripts/global_translations.js"

with open(LOG_FILE, 'r') as f:
    lines = f.readlines()

definitions_start = -1
definitions_end = -1

brace_count = 0
found_start = False

for i, line in enumerate(lines):
    if "const translations = {" in line:
        definitions_start = i
        brace_count = 1
        found_start = True
        continue
    
    if found_start:
        brace_count += line.count('{')
        brace_count -= line.count('}')
        
        if brace_count == 0:
            definitions_end = i
            break

print(f"Start: {definitions_start}, End: {definitions_end}")
print(f"Line at End: {lines[definitions_end].strip()}")
