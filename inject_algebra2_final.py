#!/usr/bin/env python3
"""
Inject all 1536 Algebra 2 translations into global_translations.js.
Inserts new entries right before the closing }; of the translations object.
Skips any entries that already exist as keys.
"""
import json, re

TRANS_FILE = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"

# Load translated strings
with open("/workspaces/ArisEdu/algebra2_full_translations.json", "r", encoding="utf-8") as f:
    new_translations = json.load(f)

# Read the file
with open(TRANS_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Extract existing keys to avoid duplicates
existing_keys = set()
for m in re.finditer(r'^\s*"(.+?)"\s*:', content, re.MULTILINE):
    existing_keys.add(m.group(1))

print(f"Existing keys: {len(existing_keys)}")
print(f"New translations: {len(new_translations)}")

# Filter out already-existing keys
to_add = {}
for key, val in new_translations.items():
    if key not in existing_keys:
        to_add[key] = val

print(f"After dedup: {len(to_add)} new entries to add")

if not to_add:
    print("Nothing to add!")
    exit(0)

# Build the insertion text
lines = []
for key, val in sorted(to_add.items()):
    # Escape quotes in key and value for JS
    k_escaped = key.replace('\\', '\\\\').replace('"', '\\"')
    v_escaped = val.replace('\\', '\\\\').replace('"', '\\"')
    lines.append(f'    "{k_escaped}": "{v_escaped}",')

insertion = '\n'.join(lines)

# Find the closing }; of the translations object (line after last key-value pair)
# Pattern: last translation entry followed by };
# We look for the pattern: "...": "...",\n}; or "...": "...",\n    };
match = re.search(r'("≈ 3 × 10⁸ m/s\.": "≈ 3 × 10⁸ m/s\.",?\n)(};)', content)
if not match:
    # Try a more general approach - find }; that follows translation entries
    match = re.search(r'(\n)(};)\s*\n\s*// ── Simplified Chinese', content)

if match:
    pos = match.start(2)
    new_content = content[:pos] + insertion + '\n' + content[pos:]
    
    with open(TRANS_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Successfully injected {len(to_add)} translations")
    
    # Verify
    with open(TRANS_FILE, "r", encoding="utf-8") as f:
        verify = f.read()
    new_key_count = len(re.findall(r'^\s*".*?":', verify, re.MULTILINE))
    print(f"Total translation keys now: {new_key_count}")
    print(f"File size: {len(verify.splitlines())} lines")
else:
    print("ERROR: Could not find injection point!")
    # Try line-based approach
    lines_all = content.split('\n')
    # Find the }; after the last "..." line
    last_entry_line = None
    for i, line in enumerate(lines_all):
        if re.match(r'^\s*".*?"\s*:', line):
            last_entry_line = i
    
    if last_entry_line is not None:
        # Find the next }; after last entry
        for i in range(last_entry_line + 1, len(lines_all)):
            if lines_all[i].strip() == '};':
                print("Found closing brace at line", i+1)
                # Insert before this line
                new_lines = lines_all[:i] + insertion.split('\n') + lines_all[i:]
                with open(TRANS_FILE, "w", encoding="utf-8") as f:
                    f.write('\n'.join(new_lines))
                print("Injected", len(to_add), "translations at line", i+1)
                
                with open(TRANS_FILE, "r", encoding="utf-8") as f:
                    verify = f.read()
                print(f"Total file: {len(verify.splitlines())} lines")
                break
        else:
            print("FATAL: Could not find closing brace after last entry")
