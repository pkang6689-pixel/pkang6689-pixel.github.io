import re
import os

base_dir = "ArisEdu Project Folder"
chem_html_path = os.path.join(base_dir, "chem.html")

def get_lessons_from_dir(unit_num):
    unit_rel_path = f"ChemistryLessons/Unit{unit_num}"
    full_path = os.path.join(base_dir, unit_rel_path)
    
    if not os.path.exists(full_path):
        print(f"Warning: Directory not found: {full_path}")
        return []
    
    files = os.listdir(full_path)
    # Filter for Lesson files
    # Pattern: Lesson X.Y Name.html
    lesson_files = []
    
    for f in files:
        if f.lower().startswith("lesson") and f.lower().endswith(".html"):
            lesson_files.append(f)
            
    # Sort them. Ideally numerically by lesson number.
    # Assumption: Filename is like "Lesson 1.1 ... .html"
    def sort_key(filename):
        # Extract the second number "1.1" -> 1.1
        match = re.search(r'Lesson\s*\d+\.(\d+)', filename, re.IGNORECASE)
        if match:
            return int(match.group(1))
        return 999 
    
    lesson_files.sort(key=sort_key)
    
    lessons = []
    for filename in lesson_files:
        # Title derivation: Remove extension, replace underscores with spaces
        name_part = os.path.splitext(filename)[0]
        # Clean up "Lesson 1.1" prefix if present
        # But wait, existing logic in generate_segments handles "Lesson X.Y:" stripping
        # Let's clean underscores at least
        title = name_part.replace('_', ' ')
        lessons.append((filename, title))
        
    return lessons

def generate_segments_and_links(lessons, unit_num):
    count = len(lessons)
    if count == 0:
        return ""
    
    # Liquid geometry
    # Fill to the top of the flask (y=3)
    top_y = 3.0
    bottom_y = 33.0
    height = bottom_y - top_y
    width = 6.0 # x from 9 to 15
    flask_x = 9.0
    
    segment_height = height / count
    
    lines = []
    lines.append(f'<g id="segments-unit-{unit_num}">')
    
    # Generate segments from bottom (Lesson 1) to top
    for i, (lesson_href, lesson_title) in enumerate(lessons):
        rect_y = bottom_y - ((i + 1) * segment_height)
        rect_height = segment_height
        
        link_href = f"ChemistryLessons/Unit{unit_num}/{lesson_href}"
        
        # Format title logic
        match = re.match(r'Lesson\s*\d+\s*[:\.]?\s*(.*)', lesson_title, re.IGNORECASE)
        clean_name = match.group(1) if match else lesson_title
        
        new_title = f"Lesson {unit_num}.{i+1}: {clean_name}"

        # We add event listeners to the rect instead of a title tag.
        # onmousemove is used to track mouse position for the popup
        
        # Escape quotes in title
        safe_title = new_title.replace("'", "\\'")

        # Added onclick handler to track progress (now per lesson)
        # Note: We move the ID to the rect so we can change its fill
        lines.append(f'  <a href="{link_href}" onclick="markLessonStarted({unit_num}, {i+1})">')
        # Removed <title> tag. Added mouse event handlers.
        lines.append(f'    <rect id="u{unit_num}-l{i+1}" x="{flask_x}" y="{rect_y:.3f}" width="{width}" height="{rect_height:.3f}" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(evt, \'{safe_title}\')" onmousemove="moveLessonPopup(evt)" onmouseleave="hideLessonPopup()">')
        lines.append(f'    </rect>')
        lines.append(f'  </a>')
        
        if i < count - 1:
            line_y = rect_y
            # Used updated thinner stroke width
            lines.append(f'  <line x1="{flask_x}" y1="{line_y:.3f}" x2="{flask_x + width}" y2="{line_y:.3f}" stroke="white" stroke-width="0.04" stroke-opacity="0.6" stroke-linecap="round" pointer-events="none" />')
            
    lines.append('</g>')
    return "\n".join(lines)

def main():
    with open(chem_html_path, 'r', encoding='utf-8') as f:
        chem_content = f.read()

    replacements = {}
    
    for unit_num in range(1, 13):
        lessons = get_lessons_from_dir(unit_num)
        print(f"Unit {unit_num}: {len(lessons)} lessons found in directory.")

        svg_block = generate_segments_and_links(lessons, unit_num)
        replacements[str(unit_num)] = svg_block

    new_content = chem_content

    for unit_num, svg_code in replacements.items():
        pattern_group = re.compile(
            rf'<g id="segments-unit-{unit_num}"[^>]*>.*?</g>', 
            re.DOTALL
        )
        
        match = pattern_group.search(new_content)
        if match:
            new_content = pattern_group.sub(svg_code, new_content)
        else:
            text_tag_pattern = re.compile(f'(<text [^>]*>Unit {unit_num}</text>)')
            if text_tag_pattern.search(new_content):
                new_content = text_tag_pattern.sub(f'{svg_code}\n\\1', new_content)
            else:
                print(f"Could not find insert position for Unit {unit_num}")

    with open(chem_html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Done updating chem.html with lesson titles.")

if __name__ == "__main__":
    main()
