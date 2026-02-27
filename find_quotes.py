import re
with open('batch_geometry.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

results = []
for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if not stripped.startswith('("'):
        continue
    # Count unescaped double quotes
    count = 0
    j = 0
    while j < len(stripped):
        if stripped[j] == '\\' and j+1 < len(stripped) and stripped[j+1] == '"':
            j += 2  # skip escaped quote
            continue
        if stripped[j] == '"':
            count += 1
        j += 1
    if count > 6:
        results.append(f"Line {i}: {count} quotes: {stripped[:120]}")

with open('_quote_check.txt', 'w', encoding='utf-8') as f:
    f.write(f"Found {len(results)} problematic lines\n")
    for r in results:
        f.write(r + '\n')
