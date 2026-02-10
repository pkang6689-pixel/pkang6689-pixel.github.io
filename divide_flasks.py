import re
import os

base_dir = "ArisEdu Project Folder"
chem_html_path = os.path.join(base_dir, "chem.html")

def get_lesson_count(unit_rel_path):
    full_path = os.path.join(base_dir, unit_rel_path)
    if not os.path.exists(full_path):
        print(f"Warning: File not found: {full_path}")
        return 0
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Count links appearing to be lessons. 
        # Pattern: href="Lesson" or similar.
        matches = re.findall(r'href=["\']Lesson', content)
        return len(matches)

def generate_segments_svg(count, unit_num):
    if count <= 1:
        return ""
    
    # Liquid goes from y=6 to y=33 (height 27)
    # x goes from 9 to 15
    top_y = 6.0
    bottom_y = 33.0
    height = bottom_y - top_y
    segment_height = height / count
    
    lines = []
    lines.append(f'<g id="segments-unit-{unit_num}" pointer-events="none">')
    for i in range(1, count):
        y = top_y + (i * segment_height)
        # Add a white line
        lines.append(f'<line x1="9" y1="{y:.2f}" x2="15" y2="{y:.2f}" stroke="white" stroke-width="0.15" stroke-opacity="0.6" stroke-linecap="round" />')
    lines.append('</g>')
    return "\n".join(lines)

with open(chem_html_path, 'r', encoding='utf-8') as f:
    chem_content = f.read()

# Find unit links and numbers
# Matches: href="ChemistryLessons/..." ... >Unit 1: ...
# Regex: href="([^"]+)">Unit (\d+):
unit_links = re.findall(r'href="([^"]+)">Unit (\d+):', chem_content)

replacements = {}

print(f"Found {len(unit_links)} units.")

for path, unit_num in unit_links:
    count = get_lesson_count(path)
    print(f"Unit {unit_num}: {count} lessons found in {path}")
    
    svg_segment_code = generate_segments_svg(count, unit_num)
    replacements[unit_num] = svg_segment_code

new_content = chem_content

for unit_num, svg_code in replacements.items():
    # Remove existing group if present (for idempotency)
    pattern_remove = re.compile(f'<g id="segments-unit-{unit_num}".*?</g>', re.DOTALL)
    new_content = pattern_remove.sub('', new_content)
    
    # Insert new code before the text tag
    # Look for <text ...>Unit X</text>
    # We use a pattern that allows for attributes in the text tag
    text_tag_pattern = re.compile(f'(<text [^>]*>Unit {unit_num}</text>)')
    
    if text_tag_pattern.search(new_content):
         new_content = text_tag_pattern.sub(f'{svg_code}\n\\1', new_content)
    else:
        print(f"Error: Could not find text tag for Unit {unit_num}")

with open(chem_html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Finished updating chem.html")
