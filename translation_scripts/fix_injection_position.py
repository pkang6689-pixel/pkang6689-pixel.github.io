"""
Fix the position of the Physics Lesson Content Translations block.
Move it from the wrong location (end of file) to inside the translations object (before line 9544 };).
"""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GT_PATH = os.path.join(SCRIPT_DIR, "..", "ArisEdu Project Folder", "scripts", "global_translations.js")

with open(GT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Find the marker
marker = '  /* ═══════ Physics Lesson Content Translations ═══════ */'
marker_idx = content.index(marker)

# Find the end of the lesson content block — it ends just before the last };
# The block runs from marker_idx to just before the last };
last_close = content.rfind('};')
# The block text is from marker_idx to last_close
block_text = content[marker_idx:last_close]

# Remove the block from its current position
content_without = content[:marker_idx] + content[last_close:]

# Now find where the translations dictionary ends — it's the FIRST }; in the file
# which is after the "Elastic collision" and other unit test entries
dict_close = content_without.find('};')

# Insert the block just before the dictionary closing
new_content = content_without[:dict_close] + block_text + "\n" + content_without[dict_close:]

with open(GT_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Fixed! Block moved to correct position inside translations dictionary.")

# Verify
import re
with open(GT_PATH, "r", encoding="utf-8") as f:
    verify = f.read()
    
keys = set(re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"\s*:', verify))
print(f"Total keys: {len(keys)}")
print(f"File size: {len(verify):,} bytes")
print(f"translateNode present: {'function translateNode' in verify}")

# Check structure: the marker should now appear before the first };
mkr_pos = verify.index(marker)
first_close = verify.find('};')
print(f"Marker at char {mkr_pos}, first }}; at char {first_close}")
print(f"Marker is inside dict: {mkr_pos < first_close}")
