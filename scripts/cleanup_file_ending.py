#!/usr/bin/env python3
"""
Clean up duplicate closing at end of file
"""

filepath = "ArisEdu Project Folder/scripts/global_translations.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove any duplicate closing
content = content.rstrip()
if content.endswith('})();\n});'):
    content = content[:-5] + '\n'
elif content.endswith('})()});'):
    content = content[:-6] + ')();\n'
elif content.count('});') > 0:
    # Find and remove duplicate
    lines = content.split('\n')
    while lines and lines[-1] in ['})();', '});', '']:
        lines.pop()
    content = '\n'.join(lines) + '\n})();\n'

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Cleaned up file ending")
