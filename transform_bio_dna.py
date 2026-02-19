"""Transform bio.html lightbulbs to DNA helix shapes."""
import re

with open("ArisEdu Project Folder/bio.html", 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the header icon (lightbulb → DNA helix)
old_header_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #22c55e; margin-right: 15px;">
          <defs>
            <clipPath id="bulb-clip">
              <path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17H9v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7z" />
            </clipPath>
          </defs>
          <path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17H9v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7z" stroke="currentColor" stroke-width="2"></path>
          
          <g clip-path="url(#bulb-clip)" stroke="none">
             <!-- Liquid Wave Animation inside Bulb -->
             <path fill="#22c55e" fill-opacity="0.2" d="M0 0 H24 V24 H0 Z"></path> 
             <path fill="#22c55e">
                <animate attributeName="d" dur="3s" repeatCount="indefinite" 
                 values="M4 8 Q12 4 20 8 V24 H4 Z; 
                         M4 8 Q12 12 20 8 V24 H4 Z; 
                         M4 8 Q12 4 20 8 V24 H4 Z" />
             </path>
             <!-- Rising Bubbles -->
             <circle cx="10" cy="18" r="1.5" fill="rgba(255,255,255,0.6)">
                <animate attributeName="cy" values="18;4" dur="3s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite" />
             </circle>
             <circle cx="14" cy="20" r="1" fill="rgba(255,255,255,0.6)">
                <animate attributeName="cy" values="20;6" dur="4s" begin="1s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0;1;0" dur="4s" begin="1s" repeatCount="indefinite" />
             </circle>
             <circle cx="12" cy="19" r="0.8" fill="rgba(255,255,255,0.6)">
                <animate attributeName="cy" values="19;5" dur="2.5s" begin="0.5s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0;1;0" dur="2.5s" begin="0.5s" repeatCount="indefinite" />
             </circle>
          </g>

          <!-- Bulb Bottom Threads -->
          <line x1="9" y1="21" x2="15" y2="21"></line>
          <line x1="9" y1="19" x2="15" y2="19"></line>
        </svg>'''

new_header_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #22c55e; margin-right: 15px;">
          <!-- DNA Double Helix Icon -->
          <!-- Left strand -->
          <path d="M4 3 Q12 6 4 9 Q-4 12 4 15 Q12 18 4 21" stroke="#22c55e" stroke-width="2" fill="none">
            <animate attributeName="d" dur="3s" repeatCount="indefinite" 
              values="M4 3 Q12 6 4 9 Q-4 12 4 15 Q12 18 4 21;
                      M4 3 Q-4 6 4 9 Q12 12 4 15 Q-4 18 4 21;
                      M4 3 Q12 6 4 9 Q-4 12 4 15 Q12 18 4 21"/>
          </path>
          <!-- Right strand -->
          <path d="M20 3 Q12 6 20 9 Q28 12 20 15 Q12 18 20 21" stroke="#22c55e" stroke-width="2" fill="none">
            <animate attributeName="d" dur="3s" repeatCount="indefinite" 
              values="M20 3 Q12 6 20 9 Q28 12 20 15 Q12 18 20 21;
                      M20 3 Q28 6 20 9 Q12 12 20 15 Q28 18 20 21;
                      M20 3 Q12 6 20 9 Q28 12 20 15 Q12 18 20 21"/>
          </path>
          <!-- Base pairs (horizontal rungs) -->
          <line x1="6" y1="5" x2="18" y2="5" stroke="#22c55e" stroke-width="1.5" opacity="0.7">
            <animate attributeName="opacity" values="0.7;1;0.7" dur="1.5s" repeatCount="indefinite"/>
          </line>
          <line x1="4" y1="9" x2="20" y2="9" stroke="#22c55e" stroke-width="1.5" opacity="0.7">
            <animate attributeName="opacity" values="1;0.7;1" dur="1.5s" repeatCount="indefinite"/>
          </line>
          <line x1="6" y1="13" x2="18" y2="13" stroke="#22c55e" stroke-width="1.5" opacity="0.7">
            <animate attributeName="opacity" values="0.7;1;0.7" dur="1.5s" repeatCount="indefinite"/>
          </line>
          <line x1="4" y1="17" x2="20" y2="17" stroke="#22c55e" stroke-width="1.5" opacity="0.7">
            <animate attributeName="opacity" values="1;0.7;1" dur="1.5s" repeatCount="indefinite"/>
          </line>
          <!-- Small dots at connection points -->
          <circle cx="6" cy="5" r="1" fill="#22c55e"/>
          <circle cx="18" cy="5" r="1" fill="#22c55e"/>
          <circle cx="4" cy="9" r="1" fill="#22c55e"/>
          <circle cx="20" cy="9" r="1" fill="#22c55e"/>
          <circle cx="6" cy="13" r="1" fill="#22c55e"/>
          <circle cx="18" cy="13" r="1" fill="#22c55e"/>
          <circle cx="4" cy="17" r="1" fill="#22c55e"/>
          <circle cx="20" cy="17" r="1" fill="#22c55e"/>
        </svg>'''

html = html.replace(old_header_svg, new_header_svg)

# Function to create a DNA helix SVG for a unit
def create_dna_helix_unit(unit_num, lessons_content):
    """Create DNA helix SVG structure for a unit."""
    return f'''<svg viewBox="0 0 30 60" fill="none" class="dna-helix-bg" stroke="currentColor" stroke-width="0.3" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: 100%; max-height: 45rem; color: #22c55e;">
                <defs>
                  <clipPath id="dna-clip-u{unit_num}">
                    <rect x="3" y="2" width="24" height="52" rx="2"/>
                  </clipPath>
                  <linearGradient id="dna-grad-u{unit_num}" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:#22c55e;stop-opacity:0.1"/>
                    <stop offset="100%" style="stop-color:#22c55e;stop-opacity:0.3"/>
                  </linearGradient>
                </defs>
                
                <!-- DNA helix background structure -->
                <rect x="3" y="2" width="24" height="52" rx="2" fill="url(#dna-grad-u{unit_num})" fill-opacity="0.1" stroke="#22c55e" stroke-width="0.3"/>
                
                <!-- Left helix strand -->
                <path d="M5 2 Q20 8 5 14 Q-10 20 5 26 Q20 32 5 38 Q-10 44 5 50 Q20 56 5 62" stroke="#22c55e" stroke-width="0.4" fill="none" opacity="0.5">
                  <animate attributeName="d" dur="6s" repeatCount="indefinite" 
                    values="M5 2 Q20 8 5 14 Q-10 20 5 26 Q20 32 5 38 Q-10 44 5 50 Q20 56 5 62;
                            M5 2 Q-10 8 5 14 Q20 20 5 26 Q-10 32 5 38 Q20 44 5 50 Q-10 56 5 62;
                            M5 2 Q20 8 5 14 Q-10 20 5 26 Q20 32 5 38 Q-10 44 5 50 Q20 56 5 62"/>
                </path>
                <!-- Right helix strand -->
                <path d="M25 2 Q10 8 25 14 Q40 20 25 26 Q10 32 25 38 Q40 44 25 50 Q10 56 25 62" stroke="#22c55e" stroke-width="0.4" fill="none" opacity="0.5">
                  <animate attributeName="d" dur="6s" repeatCount="indefinite" 
                    values="M25 2 Q10 8 25 14 Q40 20 25 26 Q10 32 25 38 Q40 44 25 50 Q10 56 25 62;
                            M25 2 Q40 8 25 14 Q10 20 25 26 Q40 32 25 38 Q10 44 25 50 Q40 56 25 62;
                            M25 2 Q10 8 25 14 Q40 20 25 26 Q10 32 25 38 Q40 44 25 50 Q10 56 25 62"/>
                </path>
                
                <!-- Base pairs (rungs) - decorative -->
                <line x1="7" y1="8" x2="23" y2="8" stroke="#22c55e" stroke-width="0.2" opacity="0.3"/>
                <line x1="5" y1="14" x2="25" y2="14" stroke="#22c55e" stroke-width="0.2" opacity="0.3"/>
                <line x1="7" y1="20" x2="23" y2="20" stroke="#22c55e" stroke-width="0.2" opacity="0.3"/>
                <line x1="5" y1="26" x2="25" y2="26" stroke="#22c55e" stroke-width="0.2" opacity="0.3"/>
                <line x1="7" y1="32" x2="23" y2="32" stroke="#22c55e" stroke-width="0.2" opacity="0.3"/>
                <line x1="5" y1="38" x2="25" y2="38" stroke="#22c55e" stroke-width="0.2" opacity="0.3"/>
                <line x1="7" y1="44" x2="23" y2="44" stroke="#22c55e" stroke-width="0.2" opacity="0.3"/>
                <line x1="5" y1="50" x2="25" y2="50" stroke="#22c55e" stroke-width="0.2" opacity="0.3"/>

                <g id="segments-unit-{unit_num}" clip-path="url(#dna-clip-u{unit_num})">
{lessons_content}
                </g>

                <text x="15" y="58" text-anchor="middle" fill="currentColor" stroke="none" font-size="3" font-family="Orbitron, sans-serif" font-weight="700" style="pointer-events: none;">Unit {unit_num}</text>
             </svg>'''

# Parse and transform each unit's bulb SVG
# Use regex to find each unit section and extract lessons, then rebuild with DNA structure

# Pattern to find unit sections with their content
unit_pattern = re.compile(
    r'<!-- Unit (\d+):.*?-->\s*<div style="position: relative; display: flex.*?>\s*<svg viewBox="0 0 24 36".*?>.*?</svg>\s*</div>',
    re.DOTALL
)

# First, let's extract the lesson links for each unit
def extract_lessons_from_svg(svg_content, unit_num):
    """Extract lesson <a> and <line> elements from the original SVG."""
    # Find the segments group content
    segments_match = re.search(r'<g id="segments-unit-\d+"[^>]*>(.*?)</g>\s*<line', svg_content, re.DOTALL)
    if segments_match:
        return segments_match.group(1)
    return ""

# Read the whole file and transform it
# For simplicity, let's do search/replace on the key SVG structures

# Replace the bulb SVG defs and path with DNA helix for each unit
# Pattern for bulb structure
bulb_svg_start = re.compile(
    r'<svg viewBox="0 0 24 36" fill="none" class="bulb-bg"[^>]*>',
    re.DOTALL
)

# Replace class name
html = re.sub(r'class="bulb-bg"', 'class="dna-helix-bg"', html)

# Replace the bulb shape path with DNA helix rect
bulb_path = r'<path d="M12 2a7 7 0 0 1 7 7c0 2\.38-1\.19 4\.47-3 5\.74V17H9v-2\.26C6\.19 13\.47 5 11\.38 5 9a7 7 0 0 1 7-7z" stroke-width="0\.5" />'
dna_rect = '<rect x="5" y="2" width="14" height="15" rx="1" fill="none" stroke-width="0.3"/>'
html = re.sub(bulb_path, dna_rect, html)

# Replace bulb clip paths with rectangular clip paths
for i in range(1, 13):
    old_clip = f'''<clipPath id="bulb-clip-u{i}">
                    <path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17H9v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7z" />
                  </clipPath>'''
    new_clip = f'''<clipPath id="dna-clip-u{i}">
                    <rect x="5" y="2" width="14" height="15" rx="0.5"/>
                  </clipPath>'''
    html = html.replace(old_clip, new_clip)
    
    # Update clip-path references
    html = html.replace(f'url(#bulb-clip-u{i})', f'url(#dna-clip-u{i})')

# Replace the bulb bottom threads with DNA base pair lines
old_threads = r'<line x1="9" y1="19" x2="15" y2="19" /><line x1="10" y1="21" x2="14" y2="21" />'
new_basepairs = '''<!-- DNA base pairs decoration -->
                <line x1="6" y1="18.5" x2="18" y2="18.5" stroke="#22c55e" stroke-width="0.15" opacity="0.4"/>
                <line x1="7" y1="19.5" x2="17" y2="19.5" stroke="#22c55e" stroke-width="0.15" opacity="0.4"/>
                <line x1="6" y1="20.5" x2="18" y2="20.5" stroke="#22c55e" stroke-width="0.15" opacity="0.4"/>'''
html = re.sub(old_threads, new_basepairs, html)

# Add DNA helix strands around each unit container
# Insert decorative helix strands inside the fill area
old_liquid = r'<g clip-path="url\(#dna-clip-u(\d+)\)" stroke="none">\s*<path fill="#22c55e" fill-opacity="0\.1" d="M0 0 H24 V24 H0 Z"></path>\s*<path fill="#22c55e" fill-opacity="0\.2" id="liquid-unit-\1">.*?</path>\s*</g>'

def create_helix_animation(match):
    unit = match.group(1)
    return f'''<g clip-path="url(#dna-clip-u{unit})" stroke="none">
                    <!-- DNA helix fill effect -->
                    <rect x="5" y="2" width="14" height="15" fill="#22c55e" fill-opacity="0.05"/>
                    <!-- Left helix strand -->
                    <path d="M5 2 Q12 5 5 8 Q-2 11 5 14 Q12 17 5 20" stroke="#22c55e" stroke-width="0.25" fill="none" opacity="0.4">
                      <animate attributeName="d" dur="4s" repeatCount="indefinite" 
                        values="M5 2 Q12 5 5 8 Q-2 11 5 14 Q12 17 5 20;
                                M5 2 Q-2 5 5 8 Q12 11 5 14 Q-2 17 5 20;
                                M5 2 Q12 5 5 8 Q-2 11 5 14 Q12 17 5 20"/>
                    </path>
                    <!-- Right helix strand -->
                    <path d="M19 2 Q12 5 19 8 Q26 11 19 14 Q12 17 19 20" stroke="#22c55e" stroke-width="0.25" fill="none" opacity="0.4">
                      <animate attributeName="d" dur="4s" repeatCount="indefinite" 
                        values="M19 2 Q12 5 19 8 Q26 11 19 14 Q12 17 19 20;
                                M19 2 Q26 5 19 8 Q12 11 19 14 Q26 17 19 20;
                                M19 2 Q12 5 19 8 Q26 11 19 14 Q12 17 19 20"/>
                    </path>
                    <!-- Base pair rungs -->
                    <line x1="6" y1="5" x2="18" y2="5" stroke="#22c55e" stroke-width="0.1" opacity="0.2"/>
                    <line x1="5" y1="8" x2="19" y2="8" stroke="#22c55e" stroke-width="0.1" opacity="0.2"/>
                    <line x1="6" y1="11" x2="18" y2="11" stroke="#22c55e" stroke-width="0.1" opacity="0.2"/>
                    <line x1="5" y1="14" x2="19" y2="14" stroke="#22c55e" stroke-width="0.1" opacity="0.2"/>
                </g>'''

html = re.sub(old_liquid, create_helix_animation, html, flags=re.DOTALL)

# Write the transformed file
with open("ArisEdu Project Folder/bio.html", 'w', encoding='utf-8') as f:
    f.write(html)

print("Transformed bio.html: lightbulbs replaced with DNA helix shapes")
