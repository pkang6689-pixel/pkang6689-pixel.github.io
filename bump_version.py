import os
count = 0
for root, dirs, files in os.walk('ArisEdu Project Folder'):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
            new_content = content.replace('global_translations.js?v=4.2', 'global_translations.js?v=5.0')
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(new_content)
                count += 1

# Also fix index.html
path = 'index.html'
with open(path, 'r', encoding='utf-8') as fh:
    content = fh.read()
new_content = content.replace('global_translations.js?v=4.2', 'global_translations.js?v=5.0')
if new_content != content:
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(new_content)
    count += 1

print(f'Updated {count} HTML files to v=5.0')
