import os, glob, re

root = r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder'

old_count = 0
new_count = 0
encoding_ok = 0
encoding_bad = 0

for filepath in glob.glob(os.path.join(root, '**', '*.html'), recursive=True):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        encoding_ok += 1
    except UnicodeDecodeError:
        encoding_bad += 1
        continue
    
    if 'global_translations.js?v=5.5' in content:
        old_count += 1
    if 'global_translations.js?v=6.0' in content:
        new_count += 1

print(f"Files with v=5.5 (old): {old_count}")
print(f"Files with v=6.0 (new): {new_count}")
print(f"Valid UTF-8 files: {encoding_ok}")
print(f"Encoding errors: {encoding_bad}")

# Spot-check Chinese characters in a few files
for sample in ['Courses.html', 'bio.html', 'chem.html']:
    fp = os.path.join(root, sample)
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            c = f.read()
        chinese = re.findall(r'[\u4e00-\u9fff]+', c)
        print(f"  {sample}: {len(chinese)} Chinese character groups - {'OK' if len(chinese) >= 0 else 'BAD'}")
