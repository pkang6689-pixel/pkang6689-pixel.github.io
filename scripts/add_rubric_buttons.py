import os
import re

root_dir = "/workspaces/ArisEdu/ArisEdu Project Folder"

css_block = """
    /* Rubric Info Button Styles */
    .rubric-hover-wrap {
      position: absolute;
      top: 0;
      right: 0;
      z-index: 20;
    }

    .rubric-hover-dot {
      scale: 1.5; /* Reduced scale to fit better in box */
      width: 1.4rem;
      height: 1.4rem;
      border-radius: 999px;
      margin-right: 0.5rem; /* Adjusted margin */
      margin-top: 0.5rem; /* Adjusted margin to be inside top-right */
      border: 2px solid #1f2937;
      background: #0f172a;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.35);
      cursor: pointer;
      position: relative;
      z-index: 21;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.9rem;
      font-weight: 700;
    }

    .rubric-hover-dot span {
      font-family: 'Playfair Display', 'Poppins', serif;
      background: linear-gradient(135deg, #3b82f6 0%, #10b981 50%, #8b5cf6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      color: transparent;
    }

    .rubric-hover-panel {
      position: absolute;
      margin-right: 1.5rem;
      scale: 1.2; /* Adjusted scale */
      right: 0;
      bottom: 100%; /* Position above the dot */
      width: 10rem;
      min-height: 3rem;
      background: #0f172a;
      border: 2px solid #334155;
      border-radius: 0.75rem;
      opacity: 0;
      visibility: hidden;
      transform: translateY(-0.5rem);
      transition: opacity 0.15s ease, transform 0.15s ease, visibility 0.15s;
      z-index: 30;
      pointer-events: none; /* Prevent interfering with hover on dot if overlapping */
      padding: 0.5rem;
    }

    .rubric-hover-panel p {
      font-size: 0.7rem;
      line-height: 1.2;
      margin: 0.25rem 0;
      color: #cbd5e1;
    }

    .rubric-hover-wrap:hover .rubric-hover-panel {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
      pointer-events: auto;
    }
    
    .course-box {
        position: relative !important;
    }
"""

html_snippet = """
              <div class="rubric-hover-wrap">
                <div class="rubric-hover-dot" aria-hidden="true"><span>i</span></div>
                <div class="rubric-hover-panel" aria-hidden="true">
                  <p>Difficulty (How hard it is to understand)</p>
                  <p>Detail (Depth of lessons)</p>
                  <p>Speed (How long the video is)</p>
                  <p>Pace (How fast detail is covered)</p>
                </div>
              </div>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Heuristic: must have courses-grid
    if 'class="courses-grid"' not in content:
        return False

    modified = False

    # 1. Add CSS if missing
    if '.rubric-hover-wrap' not in content:
        # insert before </style> if exists, else before </head>
        if '</style>' in content:
            # find the last </style>
            idx = content.rfind('</style>')
            content = content[:idx] + css_block + content[idx:]
            modified = True
            print(f"Added CSS to {filepath}")
        elif '</head>' in content:
            content = content.replace('</head>', f'<style>{css_block}</style></head>')
            modified = True
            print(f"Added CSS block to {filepath}")

    # 2. Find course-box divs with stars and inject HTML
    # Using a simple state machine or splitting to avoid robust parsing issues
    
    parts = content.split('<div class="course-box">')
    # parts[0] is everything before the first course-box
    # parts[1..n] starts with the content of the course-box
    
    new_parts = [parts[0]]
    for i in range(1, len(parts)):
        part = parts[i]
        
        # Find the first closing div which should close the course-box
        close_div_idx = part.find('</div>')
        
        should_prepend = False
        
        if close_div_idx != -1:
             content_inside_box = part[:close_div_idx]
             if '⭐' in content_inside_box:
                 if 'rubric-hover-wrap' not in content_inside_box:
                     should_prepend = True
        
        if should_prepend:
             part = html_snippet + part
             modified = True
             # Only print if not already processed by previous run (though redundant check above helps)
             print(f"  Added rubric to starred lesson in {filepath}")
        
        new_parts.append(part)
        
    if modified:
        final_content = '<div class="course-box">'.join(new_parts)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        return True
        
    return False

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".html"):
            process_file(os.path.join(dirpath, filename))
