import glob

games_dir = 'ArisEdu Project Folder/games'
files = glob.glob(games_dir + '/Game*.html')
tag = '<script src="../scripts/arcade_quiz_overlay.js"></script>'

changed = 0
for fp in files:
    txt = open(fp, encoding='utf-8').read()
    if tag in txt:
        continue
    if '</body>' not in txt:
        print('WARNING: no body tag in', fp)
        continue
    txt = txt.replace('</body>', tag + '\n</body>', 1)
    open(fp, 'w', encoding='utf-8').write(txt)
    changed += 1

print(f'Injected overlay script into {changed}/{len(files)} arcade games')
