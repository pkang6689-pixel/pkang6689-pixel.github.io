#!/usr/bin/env python3
"""
Remove orphaned translation entries (lines 32777-32877)
"""

filepath = "ArisEdu Project Folder/scripts/global_translations.js"

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Remove lines 32777-32877 (Python is 0-indexed, so 32776-32876)
# Keep lines 0-32775 and 32877-end
keep_lines = lines[:32776] + lines[32878:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(keep_lines)

removed = len(lines) - len(keep_lines)
print(f"✅ Removed {removed} orphaned lines")
print(f"New total: {len(keep_lines)} lines")
