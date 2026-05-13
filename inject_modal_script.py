import os

ROOT = os.path.join('ArisEdu Project Folder', 'CourseFiles')
OLD = '<script src="../../../scripts/practice_games.js"></script>'
NEW = '<script src="../../../scripts/practice_games.js"></script>\n<script src="../../../scripts/arcade_games_modal.js"></script>'
updated = skipped = 0
for dirpath, _, files in os.walk(ROOT):
    for f in files:
        if not f.endswith('_Practice.html'):
            continue
        fp = os.path.join(dirpath, f)
        txt = open(fp, encoding='utf-8').read()
        if 'arcade_games_modal.js' in txt:
            skipped += 1
            continue
        if OLD not in txt:
            continue
        open(fp, 'w', encoding='utf-8').write(txt.replace(OLD, NEW, 1))
        updated += 1
print(f'Updated: {updated}, Skipped: {skipped}')
