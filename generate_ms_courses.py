#!/usr/bin/env python3
"""
Generate Middle School course HTML files from existing High School course files.
Removes advanced units and difficult lessons to create easier versions.
"""

import re
import os
import math

BASE_DIR = os.path.join(os.path.dirname(__file__), "ArisEdu Project Folder")

# ─────────────────────────────────────────────────────────────────
# COURSE DEFINITIONS: what to KEEP for each middle school course
# Each entry: source file, output file, new title, localStorage prefix,
#             lessons directory, and a dict of {unit_num: [lesson_names_to_keep]}
# ─────────────────────────────────────────────────────────────────

# We define units to keep and lessons to REMOVE from each kept unit.
# Lessons not in the remove list are kept.

COURSES = {
    "algebra1": {
        "source": "algebra1.html",
        "output": "ms_algebra1.html",
        "title": "Middle School: Pre-Algebra",
        "prefix": "ms_alg1",
        "lessons_dir": "Algebra1Lessons",
        "remove_units": [8, 9, 10, 11],  # Polynomials, Rational Expr, Radicals, Sequences (too advanced)
        "remove_lessons": {
            # Unit 2: remove absolute value, systems of equations/inequalities
            2: ["Absolute Value Equations &amp; Inequalities",
                "Absolute Value Equations & Inequalities",
                "Systems of Equations — Substitution &amp; Elimination",
                "Systems of Equations — Substitution & Elimination",
                "Systems of Inequalities"],
            # Unit 4: remove piecewise and transformations
            4: ["Piecewise &amp; Step Functions",
                "Piecewise & Step Functions",
                "Function Transformations"],
            # Unit 5: remove advanced exponential topics
            5: ["Compound Interest",
                "Exponential Equations from Tables &amp; Graphs",
                "Exponential Equations from Tables & Graphs",
                "Transformations of Exponential Functions",
                "Solving Exponential Equations",
                "Interpreting Exponential Models",
                "Exponential Regression"],
            # Unit 6: remove comparing models and regression
            6: ["Comparing Linear, Exponential, &amp; Quadratic Models",
                "Comparing Linear, Exponential, & Quadratic Models",
                "Quadratic Regression"],
            # Unit 7: remove advanced quadratic solving
            7: ["Completing the Square",
                "The Quadratic Formula",
                "The Discriminant",
                "Systems with Quadratics",
                "Quadratic Inequalities"],
            # Unit 12: remove advanced probability
            12: ["Conditional Probability",
                 "Probability with Combinatorics"],
        },
    },
    "algebra2": {
        "source": "algebra2.html",
        "output": "ms_algebra2.html",
        "title": "Middle School: Algebra Foundations",
        "prefix": "ms_alg2",
        "lessons_dir": "Algebra2Lessons",
        "remove_units": [4, 5, 6, 7, 8, 9],  # Rational, Exp/Log, Sequences, Stats, Trig, Conic
        "remove_lessons": {
            1: ["1.8 Linear Programming",
                "1.9 Advanced Linear Applications"],
            2: ["2.7 Quadratic Inequalities"],
            3: ["3.5 Remainder &amp; Factor Theorems",
                "3.5 Remainder & Factor Theorems",
                "3.6 Complex Numbers &amp; Polynomial Roots",
                "3.6 Complex Numbers & Polynomial Roots",
                "3.7 Higher-Degree Polynomials"],
        },
    },
    "geometry": {
        "source": "geometry.html",
        "output": "ms_geometry.html",
        "title": "Middle School: Geometry",
        "prefix": "ms_geom",
        "lessons_dir": "GeometryLessons",
        "remove_units": [9, 10, 11, 12, 13],  # Transformations coord, Circles adv, Area, 3D, Probability
        "remove_lessons": {
            # Remove all ⭐ lessons from kept units
            2: ["Lesson 2.2: Logic ⭐",
                "Logic ⭐",
                "Lesson 2.4: Deductive Reasoning ⭐",
                "Deductive Reasoning ⭐",
                "Lesson 2.9: Proofs in Coordinate Geometry ⭐",
                "Proofs in Coordinate Geometry ⭐"],
            3: ["Lesson 3.7: Analytic Geometry Applications ⭐",
                "Analytic Geometry Applications ⭐"],
            4: ["Lesson 4.8: Triangles and Coordinate Proof ⭐",
                "Triangles and Coordinate Proof ⭐"],
            5: ["Lesson 5.4: Indirect Proof ⭐",
                "Indirect Proof ⭐"],
            6: ["Lesson 6.7: Regular Polygons and Symmetry ⭐",
                "Regular Polygons and Symmetry ⭐"],
            7: ["Lesson 7.8: Fractals and Self-Similarity ⭐",
                "Fractals and Self-Similarity ⭐"],
            8: ["Lesson 8.4: Trigonometry ⭐",
                "Trigonometry ⭐",
                "Lesson 8.6: The Law of Sines and Cosines ⭐",
                "The Law of Sines and Cosines ⭐",
                "Lesson 8.7: Vectors ⭐",
                "Vectors ⭐",
                "Lesson 8.8: Polar Coordinates and Complex Numbers ⭐",
                "Polar Coordinates and Complex Numbers ⭐"],
        },
    },
    "physics": {
        "source": "physics.html",
        "output": "ms_physics.html",
        "title": "Middle School: Physical Science",
        "prefix": "ms_phys",
        "lessons_dir": "PhysicsLessons",
        "remove_units": [6, 7, 8, 9, 10, 11],  # Gravity, Waves, Sound, Light, EM, Modern
        "remove_lessons": {
            # Remove ⭐ lessons
            2: ["2.6 ⭐ Relative Motion &amp; Reference Frames",
                "2.6 ⭐ Relative Motion & Reference Frames",
                "⭐ Relative Motion &amp; Reference Frames",
                "⭐ Relative Motion & Reference Frames"],
            3: ["3.7 ⭐ Circular Motion &amp; Centripetal Force",
                "3.7 ⭐ Circular Motion & Centripetal Force",
                "⭐ Circular Motion &amp; Centripetal Force",
                "⭐ Circular Motion & Centripetal Force",
                "3.8 ⭐ Non-Inertial Frames &amp; Pseudo-Forces",
                "3.8 ⭐ Non-Inertial Frames & Pseudo-Forces",
                "⭐ Non-Inertial Frames &amp; Pseudo-Forces",
                "⭐ Non-Inertial Frames & Pseudo-Forces"],
            4: ["4.5 ⭐ Work-Energy Theorem",
                "⭐ Work-Energy Theorem",
                "4.6 ⭐ Conservative vs. Non-Conservative Forces",
                "⭐ Conservative vs. Non-Conservative Forces"],
            5: ["5.5 ⭐ Center of Mass",
                "⭐ Center of Mass",
                "5.6 ⭐ Rocket Propulsion",
                "⭐ Rocket Propulsion"],
        },
    },
    "chem": {
        "source": "chem.html",
        "output": "ms_chem.html",
        "title": "Middle School: Chemistry Foundations",
        "prefix": "ms_chem",
        "lessons_dir": "ChemistryLessons",
        "remove_units": [8, 9, 10, 11, 12],  # Gas Laws, Solutions, Acids, Thermo, Nuclear
        "remove_lessons": {
            # Remove starred/advanced lessons
            3: ["Quantum Mechanical Model &amp; Orbitals",
                "Quantum Mechanical Model & Orbitals",
                "Electromagnetic Spectrum &amp; Atomic Emission Spectra",
                "Electromagnetic Spectrum & Atomic Emission Spectra",
                "Element Synthesis"],
            4: ["VSEPR Molecule Shapes",
                "Suborbital Shapes",
                "Shielding Effect",
                "Electron Suborbitals"],
            6: ["Chemical Equilibrium &amp; Le Chatelier&#x27;s Principle",
                "Chemical Equilibrium & Le Chatelier's Principle",
                "Chemical Equilibrium &amp; Le Chatelier's Principle",
                "Reaction Rates &amp; Catalysts",
                "Reaction Rates & Catalysts"],
            7: ["Limiting Reagents",
                "Empirical vs. Molecular Formulas",
                "Percent Yield"],
        },
    },
    "bio": {
        "source": "bio.html",
        "output": "ms_bio.html",
        "title": "Middle School: Life Science",
        "prefix": "ms_bio",
        "lessons_dir": "BiologyLessons",
        "remove_units": [10, 11, 12],  # Meiosis, Genetics, DNA/Biotech
        "remove_lessons": {
            # Remove advanced ecology/evolution
            4: ["4.4 Hardy-Weinberg Equilibrium",
                "Hardy-Weinberg Equilibrium"],
            5: ["5.5 Speciation",
                "Speciation",
                "5.4 Patterns of Evolution",
                "Patterns of Evolution"],
            7: ["7.5 The Electron Transport Chain",
                "The Electron Transport Chain",
                "7.4 The Krebs Cycle",
                "The Krebs Cycle"],
            8: ["8.4 The Calvin Cycle",
                "The Calvin Cycle"],
            9: ["9.5 Cell Cycle Regulation and Cancer",
                "Cell Cycle Regulation and Cancer"],
        },
    },
}


def normalize_text(text):
    """Normalize HTML entities and special chars for comparison."""
    if not text:
        return ""
    return (text.replace("&amp;", "&")
                .replace("&#x27;", "'")
                .replace("&#39;", "'")
                .replace("&lt;", "<")
                .replace("&gt;", ">")
                .replace("\u2014", "—")
                .replace("⭐", "")
                .strip())


def should_remove_lesson(lesson_name, remove_list):
    """Check if a lesson should be removed based on the remove list."""
    if not lesson_name or not remove_list:
        return False
    norm_name = normalize_text(lesson_name)
    for pattern in remove_list:
        norm_pattern = normalize_text(pattern)
        if norm_name == norm_pattern or norm_pattern in norm_name or norm_name in norm_pattern:
            return True
    return False


def extract_all_lessons(html):
    """
    Extract all lessons from any course HTML format.
    Returns a dict: {unit_num: [(href, lesson_name, original_lesson_idx), ...]}
    Works with all SVG shapes (book, triangle, lightbulb, flask, DNA).
    """
    units = {}
    
    # Find all lesson <a> tags with markLessonStarted and showLessonPopup
    lesson_pattern = re.compile(
        r'<a\s+href="([^"]*)"[^>]*onclick="markLessonStarted\(\'([^\']*)\',\s*(\d+)\)"[^>]*>'
        r'.*?showLessonPopup\(event,\s*\'([^\']*)\'\)',
        re.DOTALL
    )
    
    for m in lesson_pattern.finditer(html):
        href = m.group(1)
        unit_id = m.group(2)  # Could be "1", "5A", "5B", etc.
        lesson_idx = int(m.group(3))
        lesson_name = m.group(4)
        
        # Normalize unit ID
        try:
            unit_key = int(unit_id)
        except ValueError:
            unit_key = unit_id  # "5A", "5B"
        
        if unit_key not in units:
            units[unit_key] = []
        units[unit_key].append((href, lesson_name, lesson_idx))
    
    # Sort lessons within each unit by their original index
    for unit_key in units:
        units[unit_key].sort(key=lambda x: x[2])
    
    return units


def rebuild_unit_svg(unit_num, lessons, new_unit_index):
    """
    Rebuild a unit SVG block with recalculated positions.
    lessons: list of (href, lesson_name, original_idx) tuples
    """
    num_lessons = len(lessons)
    if num_lessons == 0:
        return ""

    box_top = 3.0
    box_height = 30.0
    segment_height = round(box_height / num_lessons, 3)

    svg_parts = []
    svg_parts.append(f'''<div style="position: relative; display: flex; align-items: flex-start; justify-content: center; height: 100%;">
  <svg viewBox="0 0 24 38" fill="none" stroke="currentColor" stroke-width="0.4" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: 100%; max-height: 45rem; color: inherit;">
    <!-- Box outline -->
    <rect x="3" y="3" width="18" height="30" rx="1.5" ry="1.5" fill="none" stroke="currentColor" stroke-width="0.5" />
    <!-- Fill background -->
    <rect id="fill-unit-{unit_num}" x="3" y="3" width="18" height="30" rx="1.5" ry="1.5" fill="#9ca3af" fill-opacity="0.15" stroke="none" />
    <!-- Lesson segments -->
    <g id="segments-unit-{unit_num}">''')

    for i, (href, lesson_name, orig_idx) in enumerate(lessons):
        # Calculate new Y position and height
        y = round(box_top + box_height - (i + 1) * segment_height, 3)
        h = round(segment_height, 3)

        lesson_idx = i + 1
        rect_id = f"u{unit_num}-l{lesson_idx}"
        
        # Escape single quotes in lesson name for HTML attribute
        safe_name = lesson_name.replace("'", "\\'")

        svg_parts.append(f'''<a href="{href}" onclick="markLessonStarted('{unit_num}', {lesson_idx})">
    <rect id="{rect_id}" stroke="none" x="3" y="{y:.3f}" width="18" height="{h:.3f}" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(event, '{safe_name}')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect>
</a>
  <line x1="3" y1="{y:.3f}" x2="21" y2="{y:.3f}" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />''')

    svg_parts.append(f'''    </g>
    <text x="12" y="36" text-anchor="middle" fill="currentColor" stroke="none" font-size="1.8" font-family="ui-sans-serif, system-ui, sans-serif" font-weight="600" style="pointer-events: none;">Unit {unit_num}</text>
  </svg>
</div>''')

    return '\n'.join(svg_parts)


def compute_grid_dims(num_units):
    """Compute grid columns and rows for a given number of units."""
    if num_units <= 3:
        return num_units, 1
    elif num_units <= 6:
        return 3, 2
    elif num_units <= 8:
        return 4, 2
    elif num_units <= 9:
        return 3, 3
    elif num_units <= 12:
        return 4, 3
    elif num_units <= 16:
        return 4, 4
    else:
        cols = 4
        rows = math.ceil(num_units / cols)
        return cols, rows


def compute_container_height(num_units):
    """Compute the main container min-height based on unit count."""
    _, rows = compute_grid_dims(num_units)
    # 45rem per row (matches SVG max-height) + 10rem for translateY offset + label padding
    return f"{rows * 45 + 10}rem"


def generate_ms_course(course_key, config):
    """Generate a middle school course HTML file."""
    source_path = os.path.join(BASE_DIR, config["source"])
    output_path = os.path.join(BASE_DIR, config["output"])

    print(f"\n{'='*60}")
    print(f"Generating {config['title']}...")
    print(f"  Source: {config['source']}")
    print(f"  Output: {config['output']}")

    with open(source_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # ── Step 1: Extract all lessons from the HTML (works with any SVG shape) ──
    all_units = extract_all_lessons(html)
    print(f"  Found {len(all_units)} units with lessons")

    if not all_units:
        print(f"  ERROR: No units found in {config['source']}! Skipping.")
        return

    # ── Step 2: Filter units and lessons ──
    remove_units = config.get("remove_units", [])
    remove_lessons_map = config.get("remove_lessons", {})

    kept_units = []
    # Sort units numerically (handle "5A", "5B" as 5.1, 5.2)
    def unit_sort_key(k):
        s = str(k)
        if s.endswith('A'):
            return (int(s[:-1]), 0)
        elif s.endswith('B'):
            return (int(s[:-1]), 1)
        return (int(k), 0)
    
    for unit_key in sorted(all_units.keys(), key=unit_sort_key):
        if unit_key in remove_units:
            print(f"  Removing Unit {unit_key} (entire unit)")
            continue

        lessons = all_units[unit_key]
        lessons_to_remove = remove_lessons_map.get(unit_key, [])
        
        if lessons_to_remove:
            original_count = len(lessons)
            filtered = []
            for href, name, idx in lessons:
                if should_remove_lesson(name, lessons_to_remove):
                    safe = name.encode('ascii', 'replace').decode('ascii')
                    print(f"    Removing: {safe} (Unit {unit_key})")
                else:
                    filtered.append((href, name, idx))
            lessons = filtered
            print(f"  Unit {unit_key}: {original_count} -> {len(lessons)} lessons")
        else:
            print(f"  Unit {unit_key}: keeping all {len(lessons)} lessons")

        if lessons:
            kept_units.append((unit_key, lessons))

    print(f"  Keeping {len(kept_units)} units total")

    # ── Step 3: Generate new SVG unit blocks ──
    cols, rows = compute_grid_dims(len(kept_units))
    container_height = compute_container_height(len(kept_units))

    unit_svgs = []
    all_new_ids = set()
    for idx, (unit_key, lessons) in enumerate(kept_units):
        svg = rebuild_unit_svg(unit_key, lessons, idx)
        unit_svgs.append(svg)
        for i in range(len(lessons)):
            all_new_ids.add(f"u{unit_key}-l{i+1}")

    grid_html = '\n'.join(unit_svgs)

    grid_container = f'''      <div style="position: absolute; inset: 0; transform: translateY(6rem); display: grid; grid-template-columns: repeat({cols}, 1fr); grid-template-rows: repeat({rows}, 1fr); pointer-events: none; opacity: 1; z-index: 0; gap: 1rem; padding: 0 1rem;">
{grid_html}

      </div>'''

    # ── Step 4: Extract head and build new file ──
    head_match = re.search(r'(<head>.*?</head>)', html, re.DOTALL)
    head_html = head_match.group(1) if head_match else "<head></head>"
    head_html = re.sub(r'<title>[^<]*</title>', f'<title>{config["title"]}</title>', head_html)

    # Get the old localStorage prefix
    prefix_match = re.search(r'`(\w+)_u\$\{unit\}_l\$\{lesson\}_started`', html)
    old_prefix = prefix_match.group(1) if prefix_match else course_key
    new_prefix = config["prefix"]

    # Extract the script section
    script_section = ""
    search_section = ""
    
    # Try to find tooltip + progress script section
    tooltip_start = html.find("<!-- Lesson Tooltip -->")
    if tooltip_start < 0:
        tooltip_start = html.find("#lesson-tooltip")
        if tooltip_start >= 0:
            # Back up to find the <div> or <style> before it
            tooltip_start = html.rfind("<", 0, tooltip_start)

    search_start = html.find("<!-- ArisEdu Global Search -->")
    body_end = html.rfind("</body>")

    if tooltip_start >= 0 and search_start >= 0:
        script_section = html[tooltip_start:search_start]
        search_section = html[search_start:body_end]
    elif tooltip_start >= 0:
        script_section = html[tooltip_start:body_end]
    else:
        # Fallback: extract everything from the first <style> tag after </main>
        main_end = html.find("</main>")
        if main_end >= 0 and search_start >= 0:
            script_section = html[main_end + len("</main>"):search_start]
            search_section = html[search_start:body_end]
        elif main_end >= 0:
            script_section = html[main_end + len("</main>"):body_end]

    # Update localStorage prefix in script section
    script_section = script_section.replace(f"`{old_prefix}_u", f"`{new_prefix}_u")
    script_section = script_section.replace(f"'{old_prefix}_u'", f"'{new_prefix}_u'")
    script_section = script_section.replace(f'"{old_prefix}_u"', f'"{new_prefix}_u"')
    script_section = re.sub(
        r"startsWith\(\s*'" + re.escape(old_prefix) + r"_u'\s*\)",
        f"startsWith('{new_prefix}_u')",
        script_section
    )
    script_section = re.sub(
        r"startsWith\(\s*`" + re.escape(old_prefix) + r"_u",
        f"startsWith(`{new_prefix}_u",
        script_section
    )
    script_section = re.sub(
        r'/\^' + re.escape(old_prefix) + r'_u/',
        f'/^{new_prefix}_u/',
        script_section
    )

    # Filter starred IDs to only those that exist
    def filter_starred_ids(match):
        old_ids_str = match.group(1)
        old_ids = re.findall(r"'([^']+)'", old_ids_str)
        new_ids = [id for id in old_ids if id in all_new_ids]
        if not new_ids:
            return "const starredIds = []"
        return "const starredIds = [" + ", ".join(f"'{id}'" for id in new_ids) + "]"

    script_section = re.sub(
        r'const starredIds = \[([^\]]*)\]',
        filter_starred_ids,
        script_section
    )
    
    # Also update search section prefix if needed
    search_section = search_section.replace(f"`{old_prefix}_u", f"`{new_prefix}_u")
    search_section = search_section.replace(f"'{old_prefix}_u'", f"'{new_prefix}_u'")

    # Build the complete HTML
    output_html = f'''<!doctype html>
<html lang="en" class="h-full">
 {head_html}
 <body class="dark-mode h-full">
<script src="scripts/taskbar.js"></script>
  <main class="main-container">
    <div class="logo-title-wrapper" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
      <h1 id="company-name" class="logo-font page-title" style="font-size: 3rem; margin-bottom: 0;">{config["title"]}</h1>
    </div>
    <div class="courses-container" style="min-height: {container_height};">

      <!-- Unit Grid -->
{grid_container}

    </div>
  </main>

    {script_section}
    {search_section}
</body>
</html>
'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_html)

    print(f"  Written to {config['output']}")
    print(f"    Units: {len(kept_units)}, Grid: {cols}x{rows}")
    for unit_num, lessons in kept_units:
        print(f"    Unit {unit_num}: {len(lessons)} items")


def main():
    print("=" * 60)
    print("Middle School Course Generator")
    print("=" * 60)

    for key, config in COURSES.items():
        try:
            generate_ms_course(key, config)
        except Exception as e:
            print(f"  ERROR generating {key}: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 60)
    print("Generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
