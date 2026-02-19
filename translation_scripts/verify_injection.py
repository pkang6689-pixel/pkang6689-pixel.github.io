import re, os

GT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ArisEdu Project Folder", "scripts", "global_translations.js")

with open(GT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

keys = set(re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"\s*:', content))
lines = content.count('\n') + 1
print(f"Total lines: {lines}")
print(f"Total keys: {len(keys)}")
print(f"Has lesson content block: {'Physics Lesson Content Translations' in content}")
print(f"Has unit test block: {'Physics Unit Test Translations' in content}")

# Check closing };
last_close = content.rfind('};')
print(f"Closing }}; at position: {last_close} / {len(content)}")

# Check the translateNode function is still intact
print(f"translateNode function present: {'function translateNode' in content}")
print(f"File size: {len(content):,} bytes")
