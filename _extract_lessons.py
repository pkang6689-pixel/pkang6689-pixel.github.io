import re, os
from collections import defaultdict

base = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"

files = [
    ('chem.html', 'HS', 'chem'),
    ('bio.html', 'HS', 'bio'),
    ('physics.html', 'HS', 'physics'),
    ('algebra1.html', 'HS', 'algebra1'),
    ('algebra2.html', 'HS', 'algebra2'),
    ('geometry.html', 'HS', 'geometry'),
    ('ms_chem.html', 'MS', 'ms_chem'),
    ('ms_bio.html', 'MS', 'ms_bio'),
    ('ms_physics.html', 'MS', 'ms_physics'),
    ('ms_algebra1.html', 'MS', 'ms_algebra1'),
    ('ms_algebra2.html', 'MS', 'ms_algebra2'),
    ('ms_geometry.html', 'MS', 'ms_geometry'),
]

for fname, level, prefix in files:
    fpath = os.path.join(base, fname)
    if not os.path.exists(fpath):
        print(f'=== {fname} ({level} prefix: {prefix}) === FILE NOT FOUND')
        print()
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    all_matches = []
    
    # Strategy: find all <a> tags that contain markLessonStarted
    # Use regex with DOTALL to handle multi-line tags
    a_tag_pattern = re.compile(r'<a\s(.*?)>', re.DOTALL | re.IGNORECASE)
    
    for m in a_tag_pattern.finditer(content):
        tag_attrs = m.group(1)
        # Check if this tag has markLessonStarted
        mls = re.search(r"markLessonStarted\(['\"](\w+)['\"]\s*,\s*(\d+)\)", tag_attrs)
        if mls:
            unit = mls.group(1)
            idx = int(mls.group(2))
            # Find href
            h = re.search(r"href=['\"]([^'\"]+)['\"]", tag_attrs)
            href = h.group(1) if h else 'NO_HREF'
            all_matches.append((href, unit, idx))
    
    print(f'=== {fname} ({level} prefix: {prefix}) ===')
    
    # Group by unit
    units = defaultdict(list)
    for href, unit, idx in all_matches:
        units[unit].append((idx, href))
    
    # Sort units naturally
    def unit_sort_key(name):
        nums = re.findall(r'\d+', name)
        return int(nums[0]) if nums else 0
    
    for unit_name in sorted(units.keys(), key=unit_sort_key):
        lessons = sorted(units[unit_name], key=lambda x: x[0])
        parts = [f'l{idx}={href}' for idx, href in lessons]
        print(f'  {unit_name}: ' + ', '.join(parts))
    
    print(f'  TOTAL: {len(all_matches)} lessons')
    print()

print("=== EXTRACTION COMPLETE ===")

# Also write to file
with open(r"c:\Users\Peter\pkang6689-pixel.github.io\_lesson_mapping.txt", "w", encoding="utf-8") as out:
    for fname, level, prefix in files:
        fpath = os.path.join(base, fname)
        if not os.path.exists(fpath):
            out.write(f'=== {fname} ({level} prefix: {prefix}) === FILE NOT FOUND\n\n')
            continue
        
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        all_matches = []
        a_tag_pattern = re.compile(r'<a\s(.*?)>', re.DOTALL | re.IGNORECASE)
        for m in a_tag_pattern.finditer(content):
            tag_attrs = m.group(1)
            mls = re.search(r"markLessonStarted\(['\"](\w+)['\"]\s*,\s*(\d+)\)", tag_attrs)
            if mls:
                unit = mls.group(1)
                idx = int(mls.group(2))
                h = re.search(r"href=['\"]([^'\"]+)['\"]", tag_attrs)
                href = h.group(1) if h else 'NO_HREF'
                all_matches.append((href, unit, idx))
        
        out.write(f'=== {fname} ({level} prefix: {prefix}) ===\n')
        units2 = defaultdict(list)
        for href, unit, idx in all_matches:
            units2[unit].append((idx, href))
        
        def unit_sort_key2(name):
            nums = re.findall(r'\d+', name)
            return int(nums[0]) if nums else 0
        
        for unit_name in sorted(units2.keys(), key=unit_sort_key2):
            lessons = sorted(units2[unit_name], key=lambda x: x[0])
            parts = [f'l{idx}={href}' for idx, href in lessons]
            out.write(f'  {unit_name}: ' + ', '.join(parts) + '\n')
        
        out.write(f'  TOTAL: {len(all_matches)} lessons\n\n')
    
    out.write("=== EXTRACTION COMPLETE ===\n")
    print("Written to _lesson_mapping.txt")
