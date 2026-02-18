"""
Fix lesson titles in Summary, Practice, Quiz, and Video HTML files
to match the canonical names in global_translations.js.
"""
import os, re, glob

# Canonical lesson names (from global_translations.js lines 156-227)
CANONICAL = {
    "1.1": "Physical Quantities & Units",
    "1.2": "SI System & Prefixes",
    "1.3": "Scalars vs Vectors",
    "1.4": "Accuracy, Precision, & Significant Figures",
    "1.5": "Dimensional Analysis",
    "1.6": "Measurement Uncertainty & Error Analysis",
    "2.1": "Distance, Displacement, Speed, Velocity",
    "2.2": "Acceleration",
    "2.3": "Graphical Analysis of Motion",
    "2.4": "Equations of Motion (constant acceleration)",
    "2.5": "Free Fall & Projectile Motion",
    "2.6": "Relative Motion & Reference Frames",
    "3.1": "Force & Interaction",
    "3.2": "Newton\u2019s First Law",
    "3.3": "Newton\u2019s Second Law (F = ma)",
    "3.4": "Newton\u2019s Third Law",
    "3.5": "Friction & Tension",
    "3.6": "Normal Force & Inclined Planes",
    "3.7": "Circular Motion & Centripetal Force",
    "3.8": "Non-Inertial Frames & Pseudo-Forces",
    "4.1": "Work & Energy Transfer",
    "4.2": "Kinetic Energy & Potential Energy",
    "4.3": "Conservation of Energy",
    "4.4": "Power & Efficiency",
    "4.5": "Work-Energy Theorem",
    "4.6": "Conservative vs. Non-Conservative Forces",
    "5.1": "Linear Momentum",
    "5.2": "Impulse",
    "5.3": "Conservation of Momentum",
    "5.4": "Elastic & Inelastic Collisions",
    "5.5": "Center of Mass",
    "5.6": "Rocket Propulsion",
    "6.1": "Newton\u2019s Law of Gravitation",
    "6.2": "Gravitational Field Strength",
    "6.3": "Orbital Motion",
    "6.4": "Satellite Motion",
    "6.5": "Escape Velocity",
    "6.6": "Kepler\u2019s Laws",
    "7.1": "Simple Harmonic Motion (SHM)",
    "7.2": "Period, Frequency, Amplitude",
    "7.3": "Energy in SHM",
    "7.4": "Wave Properties (wavelength, speed, frequency)",
    "7.5": "Wave Superposition & Interference",
    "7.6": "Standing Waves & Resonance",
    "7.7": "Doppler Effect",
    "7.8": "Wave-Particle Duality (introductory)",
    "8.1": "Nature of Sound Waves",
    "8.2": "Speed of Sound",
    "8.3": "Intensity & Loudness",
    "8.4": "Pitch & Frequency",
    "8.5": "Resonance in Air Columns",
    "8.6": "Beats & Harmonics",
    "9.1": "Reflection & Refraction",
    "9.2": "Lenses & Mirrors",
    "9.3": "Total Internal Reflection",
    "9.4": "Optical Instruments",
    "9.5": "Diffraction & Interference",
    "9.6": "Polarization",
    "10.1": "Electric Charge & Coulomb\u2019s Law",
    "10.2": "Electric Field & Potential",
    "10.3": "Capacitance",
    "10.4": "Current, Resistance, & Ohm\u2019s Law",
    "10.5": "DC Circuits & Kirchhoff\u2019s Laws",
    "10.6": "Magnetic Fields & Forces",
    "10.7": "Electromagnetic Induction",
    "10.8": "Alternating Current (AC) Circuits",
    "10.9": "Maxwell\u2019s Equations (introductory)",
    "11.1": "Photoelectric Effect",
    "11.2": "Atomic Models",
    "11.3": "Nuclear Physics (fission, fusion, decay)",
    "11.4": "Relativity (special relativity basics)",
    "11.5": "Quantum Mechanics (wavefunctions, uncertainty principle)",
    "11.6": "Particle Physics & Standard Model",
}

# Suffix map for file types
SUFFIX_MAP = {
    "_Video": "",
    "_Summary": " Summary",
    "_Practice": " Practice",
    "_Quiz": ": Quiz",
}

base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                        "ArisEdu Project Folder", "PhysicsLessons")

files = glob.glob(os.path.join(base_dir, "Unit*", "Lesson*_*.html"))
print(f"Found {len(files)} lesson files\n")

fixed = 0
errors = []

for filepath in sorted(files):
    filename = os.path.basename(filepath)
    # Extract lesson number and file type
    m = re.match(r'Lesson(\d+\.\d+)_(Video|Summary|Practice|Quiz)\.html', filename)
    if not m:
        continue
    lesson_num = m.group(1)
    file_type = m.group(2)
    suffix_key = f"_{file_type}"
    
    if lesson_num not in CANONICAL:
        errors.append(f"No canonical name for {lesson_num}")
        continue
    
    canonical_name = CANONICAL[lesson_num]
    suffix = SUFFIX_MAP[suffix_key]
    
    # Build correct title with HTML entity for &
    # In page-title h2, & appears as &amp; in HTML source
    # The correct h2 content should be:
    # "Lesson X.Y: Name Suffix" with & as &amp;
    if suffix_key == "_Quiz":
        correct_title = f"Lesson {lesson_num}{suffix.replace(':', '&#58;') if False else suffix}"
        # Quiz format: "Lesson X.Y: Topic Name: Quiz"
        correct_title = f"Lesson {lesson_num}: {canonical_name}: Quiz"
    else:
        correct_title = f"Lesson {lesson_num}: {canonical_name}{suffix}"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix <h2 class="page-title">...</h2>
    # The page-title pattern
    h2_pattern = r'(<h2 class="page-title">)Lesson ' + re.escape(lesson_num) + r':\s*(.+?)(</h2>)'
    h2_match = re.search(h2_pattern, content)
    
    if h2_match:
        current_title_content = h2_match.group(2)
        # Build expected content (what should be between "Lesson X.Y: " and "</h2>")
        # In HTML, & is &amp;, ' (curly) might be rendered as-is or as entity
        if suffix_key == "_Quiz":
            expected_content = f"{canonical_name}: Quiz"
        else:
            expected_content = f"{canonical_name}{suffix}"
        
        # Convert to HTML entities for comparison
        expected_html = expected_content.replace("&", "&amp;")
        current_clean = current_title_content.strip()
        
        if current_clean != expected_html:
            new_h2 = f'{h2_match.group(1)}Lesson {lesson_num}: {expected_html}{h2_match.group(3)}'
            content = content[:h2_match.start()] + new_h2 + content[h2_match.end():]
    
    # Also fix <title> tag
    title_pattern = r'(<title>)Lesson ' + re.escape(lesson_num) + r':\s*(.+?)(</title>)'
    title_match = re.search(title_pattern, content)
    
    if title_match:
        if suffix_key == "_Quiz":
            expected_title_content = f"{canonical_name}: Quiz"
        else:
            expected_title_content = f"{canonical_name}{suffix}"
        
        # Title tag uses actual & not &amp;
        current_title = title_match.group(2).strip()
        if current_title != expected_title_content:
            new_title = f'{title_match.group(1)}Lesson {lesson_num}: {expected_title_content}{title_match.group(3)}'
            content = content[:title_match.start()] + new_title + content[title_match.end():]
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed += 1
        print(f"  FIXED: {filename}")
    # else: file already correct, skip

print(f"\nFixed: {fixed}/{len(files)} files")
if errors:
    print("\nErrors:")
    for e in errors:
        print(f"  - {e}")
