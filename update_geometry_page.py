import os
import re

# Same plan as before to ensure consistency
PLAN_TEXT = """
Unit 1 – Foundations of Geometry
Lesson 1.1: Points, Lines, and Planes
Lesson 1.2: Linear Measure and Precision
Lesson 1.3: Distance and Midpoints
Lesson 1.4: Angle Measure
Lesson 1.5: Angle Relationships
Lesson 1.6: Two-Dimensional Figures
Lesson 1.7: Three-Dimensional Figures

Unit 2 – Reasoning and Proof
Lesson 2.1: Inductive Reasoning and Conjecture
Lesson 2.2: Logic ⭐
Lesson 2.3: Conditional Statements
Lesson 2.4: Deductive Reasoning ⭐
Lesson 2.5: Postulates and Paragraph Proofs
Lesson 2.6: Algebraic Proof
Lesson 2.7: Proving Segment Relationships
Lesson 2.8: Proving Angle Relationships
Lesson 2.9: Proofs in Coordinate Geometry ⭐

Unit 3 – Parallel and Perpendicular Lines
Lesson 3.1: Parallel Lines and Transversals
Lesson 3.2: Angles and Parallel Lines
Lesson 3.3: Slopes of Lines
Lesson 3.4: Equations of Lines
Lesson 3.5: Proving Lines Parallel
Lesson 3.6: Perpendiculars and Distance
Lesson 3.7: Analytic Geometry Applications ⭐

Unit 4 – Triangles
Lesson 4.1: Classifying Triangles
Lesson 4.2: Angles of Triangles
Lesson 4.3: Congruent Triangles
Lesson 4.4: Proving Congruence: SSS, SAS
Lesson 4.5: Proving Congruence: ASA, AAS
Lesson 4.6: Isosceles and Equilateral Triangles
Lesson 4.7: Congruence Transformations
Lesson 4.8: Triangles and Coordinate Proof ⭐

Unit 5 – Triangle Relationships
Lesson 5.1: Bisectors of Triangles
Lesson 5.2: Medians and Altitudes of Triangles
Lesson 5.3: Inequalities in One Triangle
Lesson 5.4: Indirect Proof ⭐
Lesson 5.5: The Triangle Inequality
Lesson 5.6: Inequalities in Two Triangles

Unit 6 – Quadrilaterals and Polygons
Lesson 6.1: Angles of Polygons
Lesson 6.2: Parallelograms
Lesson 6.3: Tests for Parallelograms
Lesson 6.4: Rectangles
Lesson 6.5: Rhombi and Squares
Lesson 6.6: Kites and Trapezoids
Lesson 6.7: Regular Polygons and Symmetry ⭐

Unit 7 – Similarity
Lesson 7.1: Ratios and Proportions
Lesson 7.2: Similar Polygons
Lesson 7.3: Similar Triangles
Lesson 7.4: Parallel Lines and Proportional Parts
Lesson 7.5: Parts of Similar Triangles
Lesson 7.6: Similarity Transformations
Lesson 7.7: Scale Drawings and Models
Lesson 7.8: Fractals and Self-Similarity ⭐

Unit 8 – Right Triangles and Trigonometry
Lesson 8.1: Geometric Mean
Lesson 8.2: The Pythagorean Theorem and Its Converse
Lesson 8.3: Special Right Triangles
Lesson 8.4: Trigonometry ⭐
Lesson 8.5: Angles of Elevation and Depression
Lesson 8.6: The Law of Sines and Cosines ⭐
Lesson 8.7: Vectors ⭐
Lesson 8.8: Polar Coordinates and Complex Numbers ⭐

Unit 9 – Transformations
Lesson 9.1: Reflections
Lesson 9.2: Translations
Lesson 9.3: Rotations
Lesson 9.4: Compositions of Transformations
Lesson 9.5: Symmetry
Lesson 9.6: Dilations
Lesson 9.7: Transformations in the Coordinate Plane ⭐

Unit 10 – Circles
Lesson 10.1: Circles and Circumference
Lesson 10.2: Measuring Angles and Arcs
Lesson 10.3: Arcs and Chords
Lesson 10.4: Inscribed Angles
Lesson 10.5: Tangents
Lesson 10.6: Secants, Tangents, and Angle Measures
Lesson 10.7: Special Segments in a Circle
Lesson 10.8: Equations of Circles ⭐
Lesson 10.9: Conic Sections (intro) ⭐

Unit 11 – Area
Lesson 11.1: Areas of Parallelograms and Triangles
Lesson 11.2: Areas of Trapezoids, Rhombi, and Kites
Lesson 11.3: Areas of Circles and Sectors
Lesson 11.4: Areas of Regular Polygons and Composite Figures
Lesson 11.5: Areas of Similar Figures
Lesson 11.6: Integration in Area Calculations ⭐

Unit 12 – Surface Area and Volume
Lesson 12.1: Representations of Three-Dimensional Figures
Lesson 12.2: Surface Areas of Prisms and Cylinders
Lesson 12.3: Surface Areas of Pyramids and Cones
Lesson 12.4: Volumes of Prisms and Cylinders
Lesson 12.5: Volumes of Pyramids and Cones
Lesson 12.6: Surface Areas and Volumes of Spheres
Lesson 12.7: Spherical Geometry ⭐
Lesson 12.8: Congruent and Similar Solids
Lesson 12.9: Cavalieri’s Principle and Applications ⭐

Unit 13 – Probability and Statistics in Geometry
Lesson 13.1: Representing Sample Spaces
Lesson 13.2: Permutations and Combinations
Lesson 13.3: Geometric Probability
Lesson 13.4: Simulations
Lesson 13.5: Probabilities of Independent and Dependent Events
Lesson 13.6: Probabilities of Mutually Exclusive Events
Lesson 13.7: Monte Carlo Methods in Geometry ⭐
"""

def parse_plan(text):
    units = []
    current_unit = None
    
    lines = text.strip().split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        unit_match = re.match(r"Unit (\d+) – (.+)", line)
        if unit_match:
            if current_unit:
                units.append(current_unit)
            current_unit = {
                'number': unit_match.group(1),
                'title': unit_match.group(2),
                'lessons': []
            }
            continue
            
        lesson_match = re.match(r"Lesson (\d+\.\d+): (.+)", line)
        if lesson_match and current_unit:
            current_unit['lessons'].append({
                'id': lesson_match.group(1),
                'title': lesson_match.group(2)
            })
            
    if current_unit:
        units.append(current_unit)
    return units

def generate_svg_for_unit(unit):
    u_num = unit['number']
    lessons = unit['lessons']
    
    all_items = []
    
    # 1. Unit Test
    all_items.append({
        'id': f"u{u_num}-test",
        'title': f"Unit {u_num} Test",
        'link': f"GeometryLessons/Unit{u_num}/Unit{u_num}_Test.html",
        'type': 'test'
    })
    
    # 2. Lessons (Reversed: Last lesson is below test, First lesson is at bottom)
    for l in reversed(lessons):
        all_items.append({
            'id': f"u{u_num}-l{l['id'].split('.')[-1]}", # u1-l1
            'title': f"Lesson {l['id']}: {l['title']}",
            'link': f"GeometryLessons/Unit{u_num}/Lesson{l['id']}_Video.html",
            'type': 'lesson'
        })

    count = len(all_items)
    start_y = 2.0
    end_y = 30.0
    total_h = end_y - start_y
    segment_h = total_h / count
    
    items_svg = ""
    current_y = start_y
    
    # Generate items top to bottom (Test -> Last Lesson -> ... -> First Lesson)
    for i, item in enumerate(all_items):
        
        # Link
        items_svg += f"""
                    <a href="{item['link']}">
                        <rect x="0" y="{current_y:.3f}" width="24" height="{segment_h:.3f}" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(event, '{item['title']}')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()">
                            <title>{item['title']}</title>
                        </rect>
                    </a>
        """
        # Separator Line (bottom of this rect)
        if i < count - 1:
             line_y = current_y + segment_h
             # Changed to use userSpaceOnUse behavior by referencing a specific gradient or just ensuring it renders.
             # Issue: objectBoundingBox on a horizontal line (height=0) fails.
             # Fix 1: Use a rect instead of a line with small height.
             items_svg += f"""<rect x="0" y="{line_y:.3f}" width="24" height="0.15" fill="url(#math-grad-{u_num})" fill-opacity="0.8" />\n"""
             
        current_y += segment_h

    svg_content = f"""
        <!-- Unit {u_num} -->
        <div style="position: relative; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; height: 35rem;">
             <svg viewBox="0 0 24 36" fill="none" class="bulb-bg" stroke="currentColor" stroke-width="0.5" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: 100%; max-height: 40rem;">
                <defs>
                  <!-- Gradient Units: userSpaceOnUse ensures correct scaling across elements -->
                  <linearGradient id="math-grad-{u_num}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="24" y2="36">
                      <stop offset="0%" stop-color="var(--theme-color-1, #3b82f6)"/>
                      <stop offset="50%" stop-color="var(--theme-color-2, #10b981)"/>
                      <stop offset="100%" stop-color="var(--theme-color-3, #8b5cf6)"/>
                  </linearGradient>
                  <clipPath id="tri-clip-u{u_num}">
                    <polygon points="12,2 2,30 22,30" />
                  </clipPath>
                </defs>
                
                <!-- Main Outline - Reverted to gradient -->
                <polygon points="12,2 2,30 22,30" stroke="url(#math-grad-{u_num})" stroke-width="0.8" fill="none" />
                
                <!-- Inner Liquid/Glass Effect -->
                <g clip-path="url(#tri-clip-u{u_num})" stroke="none">
                    <path fill="url(#math-grad-{u_num})" fill-opacity="0.05" d="M0 0 H24 V36 H0 Z"></path>
                    
                     <!-- Animated Liquid Level (Decorative) -->
                    <!-- <path fill="url(#math-grad-{u_num})" fill-opacity="0.1">
                        <animate attributeName="d" dur="6s" repeatCount="indefinite" values="M0 25 Q12 23 24 25 V36 H0 Z; M0 25 Q12 27 24 25 V36 H0 Z; M0 25 Q12 23 24 25 V36 H0 Z" />
                    </path> -->
                </g>

                <!-- Interactive Segments -->
                <g id="segments-unit-{u_num}" clip-path="url(#tri-clip-u{u_num})">
                    {items_svg}
                </g>
                
                <text x="12" y="34" text-anchor="middle" fill="url(#math-grad-{u_num})" stroke="none" font-size="2" font-family="Orbitron, sans-serif" font-weight="700" style="pointer-events: none;">Unit {u_num}</text>
             </svg>
        </div>
    """
    return svg_content

def main():
    units = parse_plan(PLAN_TEXT)
    
    # Generate SVGs
    html_grids = ""
    for unit in units:
        html_grids += generate_svg_for_unit(unit)
    
    final_grid_html = f"""
        <div class="courses-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem;">
            {html_grids}
        </div>
    """

    file_path = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\geometry.html"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
            
    # Remove fixed height from .courses-container
    content = re.sub(r'(\.courses-container\s*\{[^}]*?)height:\s*32rem;([^}]*\})', r'\1min-height: 32rem; height: auto;\2', content)
    
    # 1. Remove the "Geometry Units" header if it exists.
    # The user explicitly wants to remove "the text that says Geometry Units in the box".
    # This usually refers to: <h2 class="courses-section-title">Geometry Units</h2>
    content = content.replace('<h2 class="courses-section-title">Geometry Units</h2>', '')

    # Find the section by other means or if the header was our only anchor, we must change strategy.
    # Previously we used the header as anchor. Since we remove it, we need to locate the grid differently.
    # Or, we can use the grid div itself as the anchor.
    
    # Let's find the grid div using a broader search, assuming there's only one main grid to replace or based on structure.
    # The structure is <div class="courses-grid" ...> or just <div class="courses-grid">
    
    # Regex to find <div class="courses-grid"...>
    # Note: previous run added style="..." so strictly searching for class="courses-grid" might fail if we don't account for attributes.
    # But usually class attribute is first or we can regex.
    
    idx_grid_start = content.find('<div class="courses-grid"')
    
    if idx_grid_start != -1:
        # Find the end of this div block
        cursor = idx_grid_start + 4
        depth = 1
        while depth > 0 and cursor < len(content):
            next_open = content.find('<div', cursor)
            next_close = content.find('</div>', cursor)
            
            if next_open == -1: next_open = len(content)
            if next_close == -1: next_close = len(content)
            
            if next_open < next_close:
                depth += 1
                cursor = next_open + 4
            else:
                depth -= 1
                cursor = next_close + 6
        
        idx_grid_end = cursor
        
        # Construct new content replacement
        new_content = content[:idx_grid_start] + final_grid_html + content[idx_grid_end:]
        
        # Add popup code if needed
        popup_html = """
<div id="lesson-popup" style="position: fixed; display: none; background: rgba(15, 23, 42, 0.95); color: #e2e8f0; padding: 0.5rem 1rem; border-radius: 0.5rem; border: 1px solid #3b82f6; pointer-events: none; z-index: 1000; font-size: 0.9rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);"></div>
<script>
  const popup = document.getElementById('lesson-popup');
  function showLessonPopup(e, title) {
    if(!popup) return;
    popup.textContent = title;
    popup.style.display = 'block';
    moveLessonPopup(e);
  }
  function moveLessonPopup(e) {
    if(!popup) return;
    popup.style.left = (e.clientX + 15) + 'px';
    popup.style.top = (e.clientY + 15) + 'px';
  }
  function hideLessonPopup() {
    if(!popup) return;
    popup.style.display = 'none';
  }
</script>
        """
        
        if "lesson-popup" not in new_content:
            new_content = new_content.replace('</body>', popup_html + '\n</body>')
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            print("Successfully updated geometry.html")
    else:
         print("Could not find grid div")

if __name__ == '__main__':
    main()
