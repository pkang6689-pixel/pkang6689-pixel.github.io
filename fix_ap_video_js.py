from pathlib import Path

base = Path(r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\CourseFiles')
files = list(base.rglob('*_Video.html'))

script_tag = '<script src="../../../../scripts/lesson_video.js"></script>'
fixed = 0
for f in files:
    txt = f.read_text(encoding='utf-8', errors='ignore')
    if 'lesson_video.js' not in txt and 'side-buttons' in txt and f.parts[-4] == 'APLessons':
        if '</body>' in txt:
            new_txt = txt.replace('</body>', script_tag + '\n</body>')
            f.write_text(new_txt, encoding='utf-8')
            fixed += 1

print(f'Fixed: {fixed}')
