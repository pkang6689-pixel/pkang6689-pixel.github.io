"""
Remove difficult/advanced lessons from Middle School course homepages.
For each MS course page:
  1. Parse SVG units and their lesson links
  2. Remove specified advanced lessons
  3. Recalculate SVG y-positions and heights
  4. Renumber lesson IDs and onclick indices
"""

import re
import os

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"

# ============================================================
# LESSONS TO REMOVE — matched by substring of popup title
# (titles may have prefixes like "Lesson 3.5: " or "3.5 ")
# Use the core topic name as it appears in the attribute.
# The `&` in HTML attributes is literal `&`, not `&amp;`.
# ============================================================

REMOVE = {
    "ms_chem.html": [
        # Unit 3 — advanced atomic physics
        "Radioactivity & Stability",
        "Radioactivity &amp; Stability",
        "Isotopes & Radioisotopes",
        "Isotopes &amp; Radioisotopes",
        # Unit 4 — advanced electron topics
        "Electron Configuration",
        "Periodic Trends",
        # Unit 5A — advanced nomenclature
        "Crisscross Method",
        "Polyatomic Ions",
        "Common Exceptions",
        # Unit 5B — advanced bonding
        "Organic Compounds",
        "Mixed Nomenclature Practice",
        # Unit 6 — advanced reactions
        "Redox Reactions",
        "Balancing Equations",
        "Chemical Equilibrium",
        # Unit 7 — advanced stoichiometry
        "Molar Mass",
        "Avogadro",
        "Molar Conversions",
        "Stoichiometric Calculations",
    ],
    "ms_bio.html": [
        # Unit 4 — advanced evolution
        "Population Dynamics",
        # Unit 5 — advanced classification
        "Cladistics",
        "Phylogenetic Trees",
        # Unit 6 — advanced cell biology
        "Cell Communication",
        # Unit 7 — advanced respiration
        "Glycolysis",
        "Fermentation",
        # Unit 8 — advanced photosynthesis
        "Chloroplast Structure",
        "Light-Dependent Reactions",
    ],
    "ms_physics.html": [
        # Unit 1 — advanced measurement
        "Dimensional Analysis",
        "Measurement Uncertainty",
        # Unit 2 — advanced kinematics
        "Equations of Motion",
        "Free Fall",
        # Unit 3 — advanced forces
        "Friction & Tension",
        "Friction &amp; Tension",
        "Normal Force",
        "Inclined Planes",
        # Unit 4 — advanced energy
        "Power & Efficiency",
        "Power &amp; Efficiency",
        # Unit 5 — advanced momentum
        "Conservation of Momentum",
        "Elastic & Inelastic",
        "Elastic &amp; Inelastic",
    ],
    "ms_algebra1.html": [
        # Unit 2 — advanced equations
        "Literal Equations",
        "Compound Inequalities",
        # Unit 3 — advanced statistics
        "Residuals",
        "Association in Categorical Data",
        # Unit 4 — advanced functions
        "Arithmetic Sequences",
        # Unit 5 — advanced exponential
        "Exponential vs",
        "Geometric Sequences",
        # Unit 6 — advanced quadratics
        "Vertex Form",
        "Transformations of Quadratic",
        # Unit 7 — advanced factoring
        "Special Products",
    ],
    "ms_algebra2.html": [
        # Unit 1 — advanced linear systems
        "Applications of Linear Systems",
        "Inequalities & System",
        "Inequalities &amp; System",
        # Unit 2 — advanced quadratics
        "Completing the Square",
        "Quadratic Formula",
        # Unit 3 — advanced polynomials
        "Synthetic Division",
        "Polynomial Graphs",
    ],
    "ms_geometry.html": [
        # Unit 2 — all proofs (too advanced for MS)
        "Conditional Statements",
        "Postulates",
        "Paragraph Proofs",
        "Algebraic Proof",
        "Proving Segment Relationships",
        "Proving Angle Relationships",
        # Unit 3 — advanced parallel line proofs
        "Proving Lines Parallel",
        "Perpendiculars and Distance",
        # Unit 4 — advanced proofs
        "Proving Congruence: SSS",
        "Proving Congruence: ASA",
        "Congruence Transformations",
        # Unit 5 — advanced triangle properties
        "Medians and Altitudes",
        "Inequalities in One Triangle",
        "Triangle Inequality",
        "Inequalities in Two Triangles",
        # Unit 6 — advanced quadrilateral proofs
        "Tests for Parallelograms",
        "Kites and Trapezoids",
        # Unit 7 — advanced similarity
        "Proportional Parts",
        "Parts of Similar Triangles",
        "Similarity Transformations",
        # Unit 8 — advanced trig
        "Geometric Mean",
        "Angles of Elevation",
    ],
}


def extract_popup_title(a_html):
    """Extract the lesson popup title from the onmouseenter attribute."""
    m = re.search(r"showLessonPopup\(event,\s*'([^']+)'\)", a_html)
    return m.group(1) if m else None


def should_remove(title, remove_titles):
    """Check if a lesson title matches any removal pattern (substring match)."""
    if not title:
        return False
    for pattern in remove_titles:
        if pattern in title:
            return True
    return False


def process_unit(unit_html, remove_titles):
    """
    Given the HTML of a <g id="segments-unit-X">...</g> block,
    remove lessons whose titles match remove_titles,
    recalculate positions, and renumber.
    Returns (new_html, removed_count).
    """
    # Extract all lesson blocks: each is <a>...</a> followed by <line .../>
    # Pattern: <a href=...>...<rect ...></rect>\n</a>\n  <line .../> 
    lesson_pattern = re.compile(
        r'(<a\s+href="[^"]*"[^>]*>.*?</a>)\s*\n\s*(<line[^/]*/\s*>)',
        re.DOTALL
    )
    
    lessons = list(lesson_pattern.finditer(unit_html))
    if not lessons:
        return unit_html, 0
    
    # Determine which to keep
    keep = []
    removed = 0
    for match in lessons:
        a_html = match.group(1)
        title = extract_popup_title(a_html)
        if should_remove(title, remove_titles):
            removed += 1
        else:
            keep.append(match)
    
    if removed == 0:
        return unit_html, 0
    
    N = len(keep)  # new total lessons
    if N == 0:
        return unit_html, removed
    
    # SVG geometry: lessons in rect y=3 to y=33, total height=30
    TOP_Y = 3.0
    TOTAL_H = 30.0
    seg_h = TOTAL_H / N
    
    # Rebuild the segments block
    # First, get the opening tag
    open_match = re.match(r'(.*?<g\s+id="segments-unit-[^"]*">)\s*\n', unit_html, re.DOTALL)
    if not open_match:
        return unit_html, 0
    
    header = open_match.group(1)
    
    # Build new lessons from bottom (lesson 1) to top (lesson N)
    new_lines = [header]
    
    for i, match in enumerate(keep):
        lesson_idx = i + 1  # 1-indexed from bottom
        a_html = match.group(1)
        
        # Calculate new y and height
        y = TOP_Y + TOTAL_H - lesson_idx * seg_h
        h = seg_h
        
        # Extract the unit number from the rect id
        rect_id_match = re.search(r'id="u(\w+)-l\d+"', a_html)
        unit_id = rect_id_match.group(1) if rect_id_match else "?"
        
        # Update rect attributes: id, y, height
        new_a = re.sub(
            r'id="u\w+-l\d+"',
            f'id="u{unit_id}-l{lesson_idx}"',
            a_html
        )
        new_a = re.sub(
            r'y="[\d.]+"(\s+width="18"\s+height=")[\d.]+"',
            lambda m: f'y="{y:.3f}"{m.group(1)}{h:.3f}"',
            new_a
        )
        
        # Update onclick markLessonStarted index
        new_a = re.sub(
            r"markLessonStarted\('[^']+',\s*\d+\)",
            f"markLessonStarted('{unit_id}', {lesson_idx})",
            new_a
        )
        
        new_lines.append(new_a)
        
        # Add separator line
        line_y = y
        new_lines.append(
            f'  <line x1="3" y1="{line_y:.3f}" x2="21" y2="{line_y:.3f}" '
            f'stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />'
        )
    
    # Close the group
    new_lines.append("    </g>")
    
    return "\n".join(new_lines), removed


def process_file(filename, remove_titles):
    filepath = os.path.join(BASE, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    remove_set = set(remove_titles)
    total_removed = 0
    
    # Find each unit's segment group
    unit_pattern = re.compile(
        r'(<g\s+id="segments-unit-[^"]*">)(.*?)(</g>)',
        re.DOTALL
    )
    
    def replace_unit(m):
        nonlocal total_removed
        full = m.group(1) + m.group(2) + m.group(3)
        new_html, removed = process_unit(full, remove_set)
        total_removed += removed
        return new_html
    
    new_html = unit_pattern.sub(replace_unit, html)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_html)
    
    return total_removed


if __name__ == "__main__":
    grand_total = 0
    for filename, titles in REMOVE.items():
        removed = process_file(filename, titles)
        grand_total += removed
        print(f"  {filename}: removed {removed} lessons")
    print(f"\nTotal lessons removed: {grand_total}")
