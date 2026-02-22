"""
Fix Geometry Video files to use the correct rubric structure matching Physics/Bio.

Issues fixed:
1. Remove broken .rubric-container (with undefined toggleRubricItem) from inside .side-buttons
2. Add "Next Up: Summary" link inside .side-buttons
3. Add proper .rubric-box as sibling inside .courses-container (after .lesson-layout)
4. Add search scripts before </body>
"""

import os
import re
import glob

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\GeometryLessons"

RUBRIC_BOX_TEMPLATE = """\
<div class="rubric-box">
<div class="rubric-hover-wrap">
<div aria-hidden="true" class="rubric-hover-dot"><span>i</span></div>
<div aria-hidden="true" class="rubric-hover-panel">
<p><strong>Difficulty:</strong> How hard topic is &amp; how well they explained it</p>
<p><strong>Detail:</strong> Depth of content covered</p>
<p><strong>Speed:</strong> How long the video is</p>
<p><strong>Pace:</strong> How fast the video runs</p>
</div>
</div>
<h2 class="page-title">Rubric</h2>
<div class="rubric-card">
<div class="rubric-grid">
<div class="rubric-item" style="background:#e2e8f0">
<div class="rubric-text">
<span class="rubric-label">Difficulty</span>
<span class="rubric-rating">TBD</span>
</div>
</div>
<div class="rubric-item" style="background:#e2e8f0">
<div class="rubric-text">
<span class="rubric-label">Detail</span>
<span class="rubric-rating">TBD</span>
</div>
</div>
<div class="rubric-item" style="background:#e2e8f0">
<div class="rubric-text">
<span class="rubric-label">Speed</span>
<span class="rubric-rating">TBD</span>
</div>
</div>
<div class="rubric-item" style="background:#e2e8f0">
<div class="rubric-text">
<span class="rubric-label">Pace</span>
<span class="rubric-rating">TBD</span>
</div>
</div>
</div>
</div>
</div>"""

SEARCH_SCRIPTS = """\
<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>"""


def get_lesson_id(filepath):
    """Extract lesson id like '9.1' from filepath."""
    basename = os.path.basename(filepath)
    m = re.search(r'Lesson(\d+\.\d+)', basename)
    return m.group(1) if m else None


def remove_rubric_container(content):
    """Remove the entire <div class='rubric-container'>...</div> block by tracking div nesting."""
    marker = '<div class="rubric-container">'
    start = content.find(marker)
    if start == -1:
        return content

    # Walk backwards to consume leading whitespace
    ws_start = start
    while ws_start > 0 and content[ws_start - 1] in ' \t\n\r':
        ws_start -= 1

    # Track nesting from the opening <div
    depth = 0
    i = start
    while i < len(content):
        if content[i:i+4] == '<div':
            depth += 1
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                end = i + 6
                # Consume trailing whitespace/newline
                while end < len(content) and content[end] in ' \t\n\r':
                    end += 1
                return content[:ws_start] + '\n' + content[end:]
        i += 1
    return content


def fix_video_file(filepath):
    """Fix a single Video file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    lesson_id = get_lesson_id(filepath)

    # Step 1: Remove the entire rubric-container block
    content = remove_rubric_container(content)

    # Step 2: Add "Next Up: Summary" link inside .side-buttons
    # Insert right before the closing </div> of .side-buttons
    # After step 1, side-buttons contains: button + videos-panel, then closes
    # We find the closing </div> of side-buttons by looking for the pattern after videos-panel
    if 'Next Up: Summary' not in content and lesson_id:
        summary_link = f'<a class="side-button" href="Lesson{lesson_id}_Summary.html">Next Up: Summary</a>'
        # Find </div> that closes side-buttons: it's after the videos-panel's last </div>
        # The structure after step 1 is:
        #   <div class="side-buttons">
        #     <button>...</button>
        #     <div class="videos-panel">(content)</div>  ← videos-panel close
        #   </div>  ← side-buttons close
        # Find the side-buttons start, then find its matching close
        sb_start = content.find('<div class="side-buttons">')
        if sb_start != -1:
            depth = 0
            i = sb_start
            sb_close = -1
            while i < len(content):
                if content[i:i+4] == '<div':
                    depth += 1
                elif content[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        sb_close = i
                        break
                i += 1
            if sb_close != -1:
                content = content[:sb_close] + summary_link + '\n' + content[sb_close:]

    # Step 3: Add rubric-box inside courses-container, after lesson-layout closes
    # Structure: <div courses-container> <div lesson-layout>...</div> [RUBRIC HERE] </div>
    if 'rubric-box' not in content:
        # Find lesson-layout, then find its closing </div>
        ll_start = content.find('<div class="lesson-layout">')
        if ll_start != -1:
            depth = 0
            i = ll_start
            ll_close_end = -1
            while i < len(content):
                if content[i:i+4] == '<div':
                    depth += 1
                elif content[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        ll_close_end = i + 6
                        break
                i += 1
            if ll_close_end != -1:
                content = content[:ll_close_end] + '\n' + RUBRIC_BOX_TEMPLATE + '\n' + content[ll_close_end:]

    # Step 4: Add search scripts before </body> if not present
    if 'search_data.js' not in content:
        content = content.replace('</body>', SEARCH_SCRIPTS + '\n</body>')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    files = glob.glob(os.path.join(BASE, "Unit*", "Lesson*_Video.html"))
    files.sort()

    fixed = 0
    errors = []

    for filepath in files:
        try:
            if fix_video_file(filepath):
                lesson_id = get_lesson_id(filepath)
                print(f"  OK: Lesson {lesson_id}")
                fixed += 1
            else:
                lesson_id = get_lesson_id(filepath)
                print(f"  SKIP: Lesson {lesson_id} (no changes needed)")
        except Exception as e:
            print(f"  ERROR: {filepath}: {e}")
            errors.append(filepath)

    print(f"\nDone! Fixed {fixed}/{len(files)} files. Errors: {len(errors)}")
    if errors:
        for e in errors:
            print(f"  - {e}")


if __name__ == '__main__':
    main()
