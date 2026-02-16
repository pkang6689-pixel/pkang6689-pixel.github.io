
import os
import re

# Define the lesson plan
units = {
    2: {
        "title": "Kinematics",
        "lessons": [
            "2.1 Distance, Displacement, Speed, Velocity",
            "2.2 Acceleration",
            "2.3 Graphical Analysis of Motion",
            "2.4 Equations of Motion (constant acceleration)",
            "2.5 Free Fall & Projectile Motion",
            "2.6 ⭐ Relative Motion & Reference Frames"
        ]
    },
    3: {
        "title": "Dynamics",
        "lessons": [
            "3.1 Force & Interaction",
            "3.2 Newton’s First Law",
            "3.3 Newton’s Second Law (F = ma)",
            "3.4 Newton’s Third Law",
            "3.5 Friction & Tension",
            "3.6 Normal Force & Inclined Planes",
            "3.7 ⭐ Circular Motion & Centripetal Force",
            "3.8 ⭐ Non-Inertial Frames & Pseudo-Forces"
        ]
    },
    4: {
        "title": "Work, Energy, & Power",
        "lessons": [
            "4.1 Work & Energy Transfer",
            "4.2 Kinetic Energy & Potential Energy",
            "4.3 Conservation of Energy",
            "4.4 Power & Efficiency",
            "4.5 ⭐ Work-Energy Theorem",
            "4.6 ⭐ Conservative vs. Non-Conservative Forces"
        ]
    },
    5: {
        "title": "Momentum & Collisions",
        "lessons": [
            "5.1 Linear Momentum",
            "5.2 Impulse",
            "5.3 Conservation of Momentum",
            "5.4 Elastic & Inelastic Collisions",
            "5.5 ⭐ Center of Mass",
            "5.6 ⭐ Rocket Propulsion"
        ]
    },
    6: {
        "title": "Gravitation",
        "lessons": [
            "6.1 Newton’s Law of Gravitation",
            "6.2 Gravitational Field Strength",
            "6.3 Orbital Motion",
            "6.4 ⭐ Satellite Motion",
            "6.5 ⭐ Escape Velocity",
            "6.6 ⭐ Kepler’s Laws"
        ]
    },
    7: {
        "title": "Oscillations & Waves",
        "lessons": [
            "7.1 Simple Harmonic Motion (SHM)",
            "7.2 Period, Frequency, Amplitude",
            "7.3 Energy in SHM",
            "7.4 Wave Properties (wavelength, speed, frequency)",
            "7.5 ⭐ Wave Superposition & Interference",
            "7.6 Standing Waves & Resonance",
            "7.7 ⭐ Doppler Effect",
            "7.8 ⭐ Wave-Particle Duality (introductory)"
        ]
    },
    8: {
        "title": "Sound",
        "lessons": [
            "8.1 Nature of Sound Waves",
            "8.2 Speed of Sound",
            "8.3 Intensity & Loudness",
            "8.4 Pitch & Frequency",
            "8.5 Resonance in Air Columns",
            "8.6 ⭐ Beats & Harmonics"
        ]
    },
    9: {
        "title": "Light & Optics",
        "lessons": [
            "9.1 Reflection & Refraction",
            "9.2 Lenses & Mirrors",
            "9.3 Total Internal Reflection",
            "9.4 Optical Instruments",
            "9.5 ⭐ Diffraction & Interference",
            "9.6 ⭐ Polarization"
        ]
    },
    10: {
        "title": "Electricity & Magnetism",
        "lessons": [
            "10.1 Electric Charge & Coulomb’s Law",
            "10.2 Electric Field & Potential",
            "10.3 ⭐ Capacitance",
            "10.4 Current, Resistance, & Ohm’s Law",
            "10.5 DC Circuits & Kirchhoff’s Laws",
            "10.6 Magnetic Fields & Forces",
            "10.7 Electromagnetic Induction",
            "10.8 ⭐ Alternating Current (AC) Circuits",
            "10.9 ⭐ Maxwell’s Equations (introductory)"
        ]
    },
    11: {
        "title": "Modern Physics",
        "lessons": [
            "11.1 ⭐ Photoelectric Effect",
            "11.2 ⭐ Atomic Models",
            "11.3 ⭐ Nuclear Physics (fission, fusion, decay)",
            "11.4 ⭐ Relativity (special relativity basics)",
            "11.5 ⭐ Quantum Mechanics (wavefunctions, uncertainty principle)",
            "11.6 ⭐ Particle Physics & Standard Model"
        ]
    }
}

base_path = "/workspaces/ArisEdu/ArisEdu Project Folder/PhysicsLessons"

def get_filename(unit_num, lesson_str):
    # Extract lesson number (e.g. "1.1")
    match = re.search(r'(\d+\.\d+)', lesson_str)
    if not match:
        return None
    lesson_num = match.group(1)
    
    # Extract Title (remove "Lesson X.Y ", special chars)
    # 1. Remove "Lesson X.Y" prefix
    title_part = re.sub(r'Lesson\s+\d+\.\d+\s*', '', lesson_str)
    # 2. Remove stars
    title_part = title_part.replace('⭐', '').strip()
    # 3. CamelCase conversion
    # Remove special chars except spaces first
    clean_title = re.sub(r'[^\w\s]', '', title_part)
    # Split by space and capitalize
    camel_title = "".join([word.capitalize() for word in clean_title.split()])
    
    # Expected filename
    filename = foo = f"PhysicsLesson{lesson_num}{camel_title}.html"
    
    # Verify existence (approximate search if needed)
    unit_dir = os.path.join(base_path, f"Unit{unit_num}")
    full_path = os.path.join(unit_dir, filename)
    
    if os.path.exists(full_path):
        return f"PhysicsLessons/Unit{unit_num}/{filename}"
    
    # Fallback: exact search in dir
    if os.path.exists(unit_dir):
        files = os.listdir(unit_dir)
        # Try to find file starting with PhysicsLesson{lesson_num}
        for f in files:
            if f.startswith(f"PhysicsLesson{lesson_num}") and f.endswith(".html") and "Summary" not in f:
                return f"PhysicsLessons/Unit{unit_num}/{f}"
                
    return f"PhysicsLessons/PhysicsUnit{unit_num}.html" # Safety fallback

html_output = ""

for unit_num in range(2, 12):
    unit_data = units[unit_num]
    title = unit_data['title']
    lessons = unit_data['lessons']
    total_lessons = len(lessons)
    
    # Calculate segment height
    # Available height in bulb rect area approx: y=2 to y=17 (height 15)
    # We stack from bottom (y=17 up to y=2)
    # Actually checking Unit 1:
    # L1.1 at bottom: y=14.5, h=2.5
    # L1.6 at top: y=2, h=2.5
    # Top Y = 2
    # Bottom Y = 17
    # Total H = 15
    
    svg_height = 15.0
    segment_height = svg_height / total_lessons
    
    lesson_svgs = []
    
    # Process from top to bottom for list order, but SVG y coordinates grow downwards
    # Actually typically we want Lesson 1 at the bottom.
    # So reverse lessons list?
    # Unit 1 logic:
    # L1.6 (Top) y=2
    # L1.1 (Bottom) y=14.5
    
    # We will iterate reversed (Lesson X.1 at bottom)
    
    # Correct order: Top to Bottom in code determines render order, but calculating Y:
    # Lesson N (Last) -> Top (y = 2)
    # Lesson 1 (First) -> Bottom (y = 17 - segment_height)
    
    reversed_lessons = list(reversed(lessons)) # Now index 0 is User's Last Lesson (Top)
    
    html_output += f"""
        <!-- Unit {unit_num}: {title} -->
        <div style="position: relative; display: flex; align-items: flex-end; justify-content: center; height: 100%;">
             <svg viewBox="0 0 24 36" fill="none" class="bulb-bg" stroke="currentColor" stroke-width="0.4" stroke-linecap="round" stroke-linejoin="round" style="width: 130%; height: 130%; max-height: 45rem; color: #fbbf24;">
                <defs>
                  <clipPath id="bulb-clip-u{unit_num}">
                    <path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17H9v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7z" />
                  </clipPath>
                </defs>
                
                <path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17H9v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7z" stroke-width="0.5" />
                
                <g clip-path="url(#bulb-clip-u{unit_num})" stroke="none">
                    <path fill="#fbbf24" fill-opacity="0.1" d="M0 0 H24 V24 H0 Z"></path>
                    <path fill="#fbbf24" fill-opacity="0.2" id="liquid-unit-{unit_num}">
                        <animate attributeName="d" dur="{3 + (unit_num % 3)}s" repeatCount="indefinite" values="M4 17 Q12 {16 + (unit_num % 2)} 20 17 V24 H4 Z; M4 17 Q12 {18 - (unit_num % 2)} 20 17 V24 H4 Z; M4 17 Q12 {16 + (unit_num % 2)} 20 17 V24 H4 Z" />
                    </path>
                </g>

                <g id="segments-unit-{unit_num}" clip-path="url(#bulb-clip-u{unit_num})">
    """
    
    current_y = 2.0 # Start at top
    
    # Iterate normal lessons list (Top to Bottom visually in Unit 1 example was Last Lesson first)
    # Unit 1: L1.6 x=5 y=2
    # So we want the Last Lesson at the Top
    
    last_lesson_idx = len(lessons) 
    
    for i, lesson_str in enumerate(reversed(lessons)):
        # i=0 -> Last Lesson -> Top
        lesson_idx = last_lesson_idx - i
        
        # Get Clean Title
        clean_title = lesson_str.replace('Lesson', '').strip()
        
        # Get Link
        link = get_filename(unit_num, lesson_str)
        
        # Determine Star
        is_starred = '⭐' in lesson_str
        
        rect_id = f"u{unit_num}-l{lesson_idx}"
        
        html_output += f"""
                    <!-- {clean_title} -->
                    <a href="{link}" onclick="markLessonStarted('{unit_num}', {lesson_idx})">
                        <rect id="{rect_id}" x="5" y="{current_y:.1f}" width="14" height="{segment_height:.1f}" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(event, '{clean_title}')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"/>
                    </a>
        """
        
        # Add separator line unless it's the last one (bottom)
        if i < total_lessons - 1:
            line_y = current_y + segment_height
            html_output += f"""            <line x1="5" y1="{line_y:.1f}" x2="19" y2="{line_y:.1f}" stroke="white" stroke-width="0.04" stroke-opacity="0.6" />
"""
        
        current_y += segment_height

    html_output += f"""
                </g>

                <line x1="9" y1="19" x2="15" y2="19" /><line x1="10" y1="21" x2="14" y2="21" />
                <text x="12" y="24" text-anchor="middle" fill="currentColor" stroke="none" font-size="2.5" font-family="Orbitron, sans-serif" font-weight="700" style="pointer-events: none;">Unit {unit_num}</text>
             </svg>
        </div>
    """

with open("temp_physics_grid.html", "w") as f:
    f.write(html_output)

print("Generated HTML grid.")
