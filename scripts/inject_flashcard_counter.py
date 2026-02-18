"""Inject the flashcard-counter span into all physics Practice files."""
import glob

old = '              Shuffle\n            </button>\n</div>\n</div>'
counter_span = '<span id="flashcard-counter" style="display:flex;align-items:center;font-weight:600;font-size:1rem;color:#64748b;white-space:nowrap;"></span>'
new = '              Shuffle\n            </button>\n' + counter_span + '\n</div>\n</div>'

files = glob.glob('ArisEdu Project Folder/PhysicsLessons/Unit*/Lesson*_Practice.html')
count = 0
for f in sorted(files):
    with open(f, encoding='utf-8') as fh:
        content = fh.read()
    if old in content:
        content = content.replace(old, new, 1)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        count += 1
        print(f"  OK: {f}")
    else:
        print(f"  SKIP: {f}")
print(f"\nUpdated: {count}/{len(files)}")
