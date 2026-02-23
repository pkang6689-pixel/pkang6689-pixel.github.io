import json, sys

with open('ArisEdu Project Folder/scripts/global_translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the translations object
start = content.index('const translations = {')
obj_start = content.index('{', start)

# Find matching closing brace
depth = 0
in_str = False
escape_next = False
obj_end = obj_start

for i in range(obj_start, len(content)):
    c = content[i]
    if escape_next:
        escape_next = False
        continue
    if c == '\\':
        escape_next = True
        continue
    if c == '"' and not escape_next:
        in_str = not in_str
        continue
    if not in_str:
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                obj_end = i + 1
                break

obj_text = content[obj_start:obj_end]
print(f"Object extracted: {len(obj_text)} chars")

try:
    d = json.loads(obj_text)
    print(f"Valid JSON with {len(d)} entries - no syntax errors in translations object")
except json.JSONDecodeError as e:
    print(f"JSON parse error: {e}")
    lines = obj_text.split('\n')
    line_num = e.lineno
    print(f"Error near line {line_num} of object:")
    for l in range(max(0, line_num - 4), min(len(lines), line_num + 3)):
        marker = " >>>" if l + 1 == line_num else "    "
        print(f"{marker} {l+1}: {lines[l][:300]}")

# Also check the overall JS structure
print("\n--- Checking JS structure ---")
# Check IIFE wrapper
if content.strip().startswith('/*') or content.strip().startswith('(function'):
    print("IIFE wrapper: OK (starts correctly)")
else:
    print("WARNING: Missing IIFE wrapper at start")

if content.strip().endswith('})();'):
    print("IIFE wrapper: OK (ends correctly)")
else:
    last_50 = content.strip()[-50:]
    print(f"WARNING: File ending: ...{repr(last_50)}")

# Check for common JS issues
lines = content.split('\n')
print(f"\nTotal lines: {len(lines)}")

# Look for unescaped quotes in strings
errors_found = 0
for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if stripped.startswith('"') and '": "' in stripped:
        # This is a translation line - check for issues
        # Count quotes (rough check)
        parts = stripped.split('": "', 1)
        if len(parts) == 2:
            value = parts[1]
            if value.endswith(','):
                value = value[:-1]
            if value.endswith('"'):
                value = value[:-1]
            # Check for unescaped quotes inside value
            j = 0
            while j < len(value):
                if value[j] == '\\':
                    j += 2
                    continue
                if value[j] == '"':
                    errors_found += 1
                    if errors_found <= 10:
                        print(f"  Possible unescaped quote at line {i}: {stripped[:150]}")
                    break
                j += 1

if errors_found == 0:
    print("No unescaped quotes found in translation values")
else:
    print(f"Found {errors_found} lines with possible unescaped quotes")
