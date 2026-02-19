#!/usr/bin/env python3
"""Restructure bio.html DNA helix to have lessons split between top and bottom lobes."""

import re

def restructure_dna_helix():
    bio_path = "ArisEdu Project Folder/bio.html"
    
    with open(bio_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define the lesson data for each unit
    units = {
        1: {
            'lessons': [
                ('Unit1_Test.html', 'Unit 1 Test', 8),
                ('Lesson1.7_Video.html', '1.7 Careers in Biology', 7),
                ('Lesson1.6_Video.html', '1.6 Branches of Biology', 6),
                ('Lesson1.5_Video.html', '1.5 Levels of Biological Organization', 5),
                ('Lesson1.4_Video.html', '1.4 Characteristics of Life', 4),
                ('Lesson1.3_Video.html', '1.3 The Nature of Science', 3),
                ('Lesson1.2_Video.html', '1.2 The Science of Life', 2),
                ('Lesson1.1_Video.html', '1.1 Introduction to Biology', 1),
            ]
        },
        2: {
            'lessons': [
                ('Unit2_Test.html', 'Unit 2 Test', 8),
                ('Lesson2.7_Video.html', '2.7 Human Impact on Ecosystems', 7),
                ('Lesson2.6_Video.html', '2.6 Food Chains, Webs, and Trophic Levels', 6),
                ('Lesson2.5_Video.html', '2.5 Niches and Habitat', 5),
                ('Lesson2.4_Video.html', '2.4 Ecological Succession', 4),
                ('Lesson2.3_Video.html', '2.3 Cycling of Matter', 3),
                ('Lesson2.2_Video.html', '2.2 Flow of Energy in an Ecosystem', 2),
                ('Lesson2.1_Video.html', '2.1 Organisms and Their Relationships', 1),
            ]
        },
        3: {
            'lessons': [
                ('Unit3_Test.html', 'Unit 3 Test', 6),
                ('Lesson3.5_Video.html', '3.5 Aquatic Ecosystems', 5),
                ('Lesson3.4_Video.html', '3.4 Terrestrial Biomes', 4),
                ('Lesson3.3_Video.html', '3.3 Climate and Weather Patterns', 3),
                ('Lesson3.2_Video.html', '3.2 Biomes and Biodiversity', 2),
                ('Lesson3.1_Video.html', '3.1 Community Ecology', 1),
            ]
        },
        4: {
            'lessons': [
                ('Unit4_Test.html', 'Unit 4 Test', 7),
                ('Lesson4.6_Video.html', '4.6 Population Dynamics', 6),
                ('Lesson4.5_Video.html', '4.5 Natural Selection and Adaptation', 5),
                ('Lesson4.4_Video.html', '4.4 Hardy-Weinberg Equilibrium', 4),
                ('Lesson4.3_Video.html', '4.3 Sources of Genetic Variation', 3),
                ('Lesson4.2_Video.html', '4.2 Evidence of Evolution', 2),
                ('Lesson4.1_Video.html', '4.1 History of Evolutionary Thought', 1),
            ]
        },
        5: {
            'lessons': [
                ('Unit5_Test.html', 'Unit 5 Test', 7),
                ('Lesson5.6_Video.html', '5.6 Domains and Kingdoms of Life', 6),
                ('Lesson5.5_Video.html', '5.5 Speciation', 5),
                ('Lesson5.4_Video.html', '5.4 Patterns of Evolution', 4),
                ('Lesson5.3_Video.html', '5.3 Phylogenetic Trees', 3),
                ('Lesson5.2_Video.html', '5.2 Cladistics and Classification', 2),
                ('Lesson5.1_Video.html', '5.1 Taxonomy Basics', 1),
            ]
        },
        6: {
            'lessons': [
                ('Unit6_Test.html', 'Unit 6 Test', 7),
                ('Lesson6.6_Video.html', '6.6 Homeostasis', 6),
                ('Lesson6.5_Video.html', '6.5 Cell Communication', 5),
                ('Lesson6.4_Video.html', '6.4 Membrane Transport', 4),
                ('Lesson6.3_Video.html', '6.3 Organelles and Their Functions', 3),
                ('Lesson6.2_Video.html', '6.2 Prokaryotic vs Eukaryotic Cells', 2),
                ('Lesson6.1_Video.html', '6.1 Introduction to Cells', 1),
            ]
        },
        7: {
            'lessons': [
                ('Unit7_Test.html', 'Unit 7 Test', 7),
                ('Lesson7.6_Video.html', '7.6 Fermentation', 6),
                ('Lesson7.5_Video.html', '7.5 The Electron Transport Chain', 5),
                ('Lesson7.4_Video.html', '7.4 The Krebs Cycle', 4),
                ('Lesson7.3_Video.html', '7.3 Glycolysis', 3),
                ('Lesson7.2_Video.html', '7.2 ATP and Cellular Energy', 2),
                ('Lesson7.1_Video.html', '7.1 Overview of Cellular Respiration', 1),
            ]
        },
        8: {
            'lessons': [
                ('Unit8_Test.html', 'Unit 8 Test', 6),
                ('Lesson8.5_Video.html', '8.5 Factors Affecting Photosynthesis', 5),
                ('Lesson8.4_Video.html', '8.4 The Calvin Cycle', 4),
                ('Lesson8.3_Video.html', '8.3 Light-Dependent Reactions', 3),
                ('Lesson8.2_Video.html', '8.2 Chloroplast Structure', 2),
                ('Lesson8.1_Video.html', '8.1 Overview of Photosynthesis', 1),
            ]
        },
        9: {
            'lessons': [
                ('Unit9_Test.html', 'Unit 9 Test', 6),
                ('Lesson9.5_Video.html', '9.5 Cell Cycle Regulation and Cancer', 5),
                ('Lesson9.4_Video.html', '9.4 Cytokinesis', 4),
                ('Lesson9.3_Video.html', '9.3 Mitosis', 3),
                ('Lesson9.2_Video.html', '9.2 The Cell Cycle', 2),
                ('Lesson9.1_Video.html', '9.1 Cell Growth and Division', 1),
            ]
        },
        10: {
            'lessons': [
                ('Unit10_Test.html', 'Unit 10 Test', 7),
                ('Lesson10.6_Video.html', '10.6 Nondisjunction and Genetic Disorders', 6),
                ('Lesson10.5_Video.html', '10.5 Crossing Over and Genetic Variation', 5),
                ('Lesson10.4_Video.html', '10.4 Meiosis II', 4),
                ('Lesson10.3_Video.html', '10.3 Meiosis I', 3),
                ('Lesson10.2_Video.html', '10.2 Sexual Reproduction', 2),
                ('Lesson10.1_Video.html', '10.1 Overview of Meiosis', 1),
            ]
        },
        11: {
            'lessons': [
                ('Unit11_Test.html', 'Unit 11 Test', 7),
                ('Lesson11.6_Video.html', '11.6 Human Genetics and Pedigrees', 6),
                ('Lesson11.5_Video.html', '11.5 Polygenic and Multifactorial Traits', 5),
                ('Lesson11.4_Video.html', '11.4 Non-Mendelian Inheritance', 4),
                ('Lesson11.3_Video.html', '11.3 Dihybrid Crosses', 3),
                ('Lesson11.2_Video.html', '11.2 Monohybrid Crosses', 2),
                ('Lesson11.1_Video.html', '11.1 Mendel and the Laws of Inheritance', 1),
            ]
        },
        12: {
            'lessons': [
                ('Unit12_Test.html', 'Unit 12 Test', 7),
                ('Lesson12.6_Video.html', '12.6 Biotechnology Applications', 6),
                ('Lesson12.5_Video.html', '12.5 Genetic Engineering', 5),
                ('Lesson12.4_Video.html', '12.4 Protein Synthesis', 4),
                ('Lesson12.3_Video.html', '12.3 RNA and Transcription', 3),
                ('Lesson12.2_Video.html', '12.2 DNA Replication', 2),
                ('Lesson12.1_Video.html', '12.1 DNA Structure', 1),
            ]
        },
    }
    
    def generate_unit_svg(unit_num, lessons):
        """Generate SVG for a unit with lessons fitting inside the DNA helix shape."""
        total = len(lessons)
        
        # Split lessons between upper and lower lobes
        top_count = (total + 1) // 2  # More lessons in top if odd
        bottom_count = total - top_count
        
        top_lessons = lessons[:top_count]
        bottom_lessons = lessons[top_count:]
        
        # Calculate segment heights for each lobe
        # Top lobe spans y=2 to y=11 (height=9)
        # Bottom lobe spans y=11 to y=22 (height=11)
        top_segment_h = 9 / top_count if top_count > 0 else 0
        bottom_segment_h = 11 / bottom_count if bottom_count > 0 else 0
        
        svg = f'''
        <!-- Unit {unit_num} -->
        <div style="position: relative; display: flex; align-items: flex-end; justify-content: center; height: 40rem;">
             <svg viewBox="0 0 24 32" fill="none" class="dna-helix-bg" stroke="#22c55e" stroke-width="0.3" stroke-linecap="round" stroke-linejoin="round" style="width: 130%; height: 130%; max-height: 45rem;">
                <defs>
                  <!-- Top lobe clip (y=2 to y=11) - exact DNA strand curves -->
                  <clipPath id="dna-top-u{unit_num}">
                    <path d="M9 2 C15 5 3 8 9 11 L15 11 C21 8 9 5 15 2 Z" />
                  </clipPath>
                  <!-- Bottom lobe clip (y=11 to y=22) - exact DNA strand curves -->
                  <clipPath id="dna-bottom-u{unit_num}">
                    <path d="M9 11 C15 14 3 17 9 22 L15 22 C21 17 9 14 15 11 Z" />
                  </clipPath>
                </defs>
                
                <!-- DNA Double Helix strands -->
                <!-- Left strand -->
                <path d="M9 2 C15 5 3 8 9 11 C15 14 3 17 9 22" fill="none" opacity="0.6"/>
                <!-- Right strand -->
                <path d="M15 2 C9 5 21 8 15 11 C9 14 21 17 15 22" fill="none" opacity="0.6"/>
                
                <!-- Top lobe lesson segments -->
                <g id="segments-top-unit-{unit_num}" clip-path="url(#dna-top-u{unit_num})">'''
        
        # Add top lessons (no line after first lesson or last lesson in top lobe)
        for i, (filename, title, lesson_idx) in enumerate(top_lessons):
            y_pos = 2 + (i * top_segment_h)
            svg += f'''
                    <a href="BiologyLessons/Unit{unit_num}/{filename}" onclick="markLessonStarted('{unit_num}', {lesson_idx})">
                        <rect id="u{unit_num}-l{lesson_idx}" x="0" y="{y_pos:.3f}" width="24" height="{top_segment_h:.3f}" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(event, '{title}')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"/>
                    </a>'''
            # Add divider line, but not after first lesson (top of flask) or last lesson (bottom of top lobe)
            if i > 0 and i < top_count - 1:
                line_y = y_pos + top_segment_h
                svg += f'''
                    <line x1="0" y1="{line_y:.3f}" x2="24" y2="{line_y:.3f}" stroke="white" stroke-width="0.04" stroke-opacity="0.6" />'''
        
        svg += f'''
                </g>
                
                <!-- Bottom lobe lesson segments -->
                <g id="segments-bottom-unit-{unit_num}" clip-path="url(#dna-bottom-u{unit_num})">'''
        
        # Add bottom lessons (no line after first or last lesson in bottom lobe)
        for i, (filename, title, lesson_idx) in enumerate(bottom_lessons):
            y_pos = 11 + (i * bottom_segment_h)
            svg += f'''
                    <a href="BiologyLessons/Unit{unit_num}/{filename}" onclick="markLessonStarted('{unit_num}', {lesson_idx})">
                        <rect id="u{unit_num}-l{lesson_idx}" x="0" y="{y_pos:.3f}" width="24" height="{bottom_segment_h:.3f}" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(event, '{title}')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"/>
                    </a>'''
            # Add divider line, but not after first lesson (top of bottom lobe) or last lesson (bottom of flask)
            if i > 0 and i < bottom_count - 1:
                line_y = y_pos + bottom_segment_h
                svg += f'''
                    <line x1="0" y1="{line_y:.3f}" x2="24" y2="{line_y:.3f}" stroke="white" stroke-width="0.04" stroke-opacity="0.6" />'''
        
        svg += f'''
                </g>
                
                <text x="12" y="26" text-anchor="middle" fill="#22c55e" stroke="none" font-size="2.5" font-family="Orbitron, sans-serif" font-weight="700" style="pointer-events: none;">Unit {unit_num}</text>
             </svg>
        </div>'''
        
        return svg
    
    # Find the grid container and replace all unit content
    # Start after <div class="courses-container"...>
    courses_start = content.find('<div class="courses-container"')
    courses_div_end = content.find('>', courses_start) + 1
    
    # Find the style section that comes after the grid
    style_marker = '</main>'
    style_pos = content.find(style_marker)
    
    if style_pos == -1:
        print("Could not find main closing marker")
        return
    
    # Build new grid content
    new_grid = '''<!-- Decorative Background Grid (Interactive) -->
      <div style="position: relative; width: 100%; display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; pointer-events: none; opacity: 1; z-index: 0;">
'''
    
    for unit_num in range(1, 13):
        new_grid += generate_unit_svg(unit_num, units[unit_num]['lessons'])
        new_grid += '\n'
    
    new_grid += '''
      </div>'''
    
    # Replace everything between courses div opening and </main>
    new_content = content[:courses_div_end] + '\n      \n      ' + new_grid + '''
    </div>
  </main>''' + content[style_pos + len(style_marker):]
    
    with open(bio_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Restructured DNA helix with lessons split between top and bottom lobes")

if __name__ == "__main__":
    restructure_dna_helix()
