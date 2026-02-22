#!/usr/bin/env python3
"""
Fix geometry.html to match physics/bio/chem course pages:
1. Add main.css link to <head> (remove redundant inline styles)
2. Replace crude #lesson-popup with proper #lesson-tooltip (CSS + JS)
3. Add IDs (u1-l1, etc.) and onclick="markLessonStarted()" to all SVG rects
4. Add full JS: progress tracking, star effects, hover animations
5. Add page title SVG icon matching the triangle theme
"""

import re

FILEPATH = "ArisEdu Project Folder/geometry.html"

with open(FILEPATH, 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ============================================================
# 1. Add main.css to <head> and clean up inline styles
# ============================================================

# Add main.css link right after the Poppins font link
content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;display=swap" rel="stylesheet">\n  <link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">'
)

# Remove the huge inline <style> block (everything from the first <style> to the closing </style> before Orbitron)
# We need to keep the @view-transition style if present, but the big block needs to go
# The block starts with "<style>\n    body {" and ends with "</style>" just before Orbitron font link
inline_style_pattern = r'  <style>\s*body \{.*?\.course-box \{\s*position: relative !important;\s*\}\s*</style>'
content = re.sub(inline_style_pattern, '', content, flags=re.DOTALL)

# ============================================================
# 2. Add page title SVG icon (triangle) matching geometry theme
# ============================================================
content = content.replace(
    '''    <div class="logo-title-wrapper">
    <h1 id="company-name" class="logo-font company-title">High School: Geometry</h1>
    </div>''',
    '''    <div class="logo-title-wrapper" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
      <h1 id="company-name" class="logo-font page-title" style="font-size: 3rem; margin-bottom: 0; display: flex; align-items: center;">
        <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 15px;">
          <defs>
            <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="var(--theme-color-1, #3b82f6)"/>
              <stop offset="50%" stop-color="var(--theme-color-2, #10b981)"/>
              <stop offset="100%" stop-color="var(--theme-color-3, #8b5cf6)"/>
            </linearGradient>
          </defs>
          <polygon points="12,2 2,22 22,22" stroke="url(#title-grad)" stroke-width="2" fill="none"/>
          <circle cx="12" cy="2" r="1.5" fill="url(#title-grad)" stroke="none">
            <animate attributeName="r" values="1.5;2;1.5" dur="2s" repeatCount="indefinite"/>
          </circle>
          <circle cx="2" cy="22" r="1.5" fill="url(#title-grad)" stroke="none">
            <animate attributeName="r" values="1.5;2;1.5" dur="2s" begin="0.7s" repeatCount="indefinite"/>
          </circle>
          <circle cx="22" cy="22" r="1.5" fill="url(#title-grad)" stroke="none">
            <animate attributeName="r" values="1.5;2;1.5" dur="2s" begin="1.4s" repeatCount="indefinite"/>
          </circle>
        </svg>
        High School: Geometry
      </h1>
    </div>'''
)

# ============================================================
# 3. Add IDs and onclick to all SVG rect elements
# ============================================================

# Build a mapping of all units and their lesson counts
# We need to parse each unit's links to figure out lesson numbers

# Pattern for unit test links
# <a href="GeometryLessons/UnitX/UnitX_Test.html">
# Pattern for lesson links  
# <a href="GeometryLessons/UnitX/LessonX.Y_Video.html">

# We need to process anchor tags and add onclick, and add id to their child rect

def add_ids_and_onclick(html):
    """Add IDs and onclick handlers to all geometry lesson link rects."""
    
    # First, find all units and count their lessons
    unit_lessons = {}
    for m in re.finditer(r'<a href="GeometryLessons/Unit(\d+)/(?:Unit\d+_Test|Lesson(\d+)\.(\d+)_Video)\.html">', html):
        unit = m.group(1)
        if unit not in unit_lessons:
            unit_lessons[unit] = set()
        if m.group(2):  # It's a lesson, not a test
            unit_lessons[unit].add(int(m.group(3)))
    
    # For each unit, determine the total lesson count (lessons + 1 for test)
    for unit_num_str in unit_lessons:
        unit_lessons[unit_num_str] = max(unit_lessons[unit_num_str]) if unit_lessons[unit_num_str] else 0
    
    # Now process each link
    # Unit test: lesson index = max_lesson + 1 (the test is always at the top)
    def replace_test_link(m):
        unit = m.group(1)
        max_lesson = unit_lessons.get(unit, 7)
        test_index = max_lesson + 1
        return f'<a href="GeometryLessons/Unit{unit}/Unit{unit}_Test.html" onclick="markLessonStarted(\'{unit}\', {test_index})">'
    
    html = re.sub(
        r'<a href="GeometryLessons/Unit(\d+)/Unit\d+_Test\.html">',
        replace_test_link,
        html
    )
    
    # Lesson links
    def replace_lesson_link(m):
        unit = m.group(1)
        lesson = m.group(2)
        return f'<a href="GeometryLessons/Unit{unit}/Lesson{unit}.{lesson}_Video.html" onclick="markLessonStarted(\'{unit}\', {lesson})">'
    
    html = re.sub(
        r'<a href="GeometryLessons/Unit(\d+)/Lesson\d+\.(\d+)_Video\.html">',
        replace_lesson_link,
        html
    )
    
    # Now add IDs to the rect elements inside these links
    # The rect elements follow the <a> tag and currently have no id
    # We need to track which unit/lesson we're in
    
    # Process test rects - they come right after the test link
    # Pattern: onclick="markLessonStarted('X', N)">\n<rect x="0"
    def add_test_rect_id(m):
        unit = m.group(1)
        test_idx = m.group(2)
        rest = m.group(3)
        return f'''onclick="markLessonStarted('{unit}', {test_idx})">\n                        <rect id="u{unit}-l{test_idx}" {rest}'''
    
    html = re.sub(
        r'''onclick="markLessonStarted\('(\d+)', (\d+)\)">\s*<rect (x="0")''',
        add_test_rect_id,
        html
    )
    
    # Process lesson rects
    def add_lesson_rect_id(m):
        unit = m.group(1)
        lesson = m.group(2)
        rest = m.group(3)
        return f'''onclick="markLessonStarted('{unit}', {lesson})">\n                        <rect id="u{unit}-l{lesson}" {rest}'''
    
    html = re.sub(
        r'''onclick="markLessonStarted\('(\d+)', (\d+)\)">\s*<rect (x="0" y="\d)''',
        add_lesson_rect_id,
        html
    )
    
    return html

content = add_ids_and_onclick(content)

# ============================================================
# 4. Replace the old popup system with new tooltip system
# ============================================================

# Remove the old lesson-popup div and its script
old_popup = r'''    <div id="lesson-popup" style="position: fixed; display: none; background: rgba\(15, 23, 42, 0\.95\); color: #e2e8f0; padding: 0\.5rem 1rem; border-radius: 0\.5rem; border: 1px solid #3b82f6; pointer-events: none; z-index: 1000; font-size: 0\.9rem; box-shadow: 0 4px 6px -1px rgba\(0, 0, 0, 0\.1\);"></div>
    <script>
      const popup = document\.getElementById\('lesson-popup'\);
      function showLessonPopup\(e, title\) \{
        if\(!popup\) return;
        popup\.textContent = title;
        popup\.style\.display = 'block';
        moveLessonPopup\(e\);
      \}
      function moveLessonPopup\(e\) \{
        if\(!popup\) return;
        popup\.style\.left = \(e\.clientX \+ 15\) \+ 'px';
        popup\.style\.top = \(e\.clientY \+ 15\) \+ 'px';
      \}
      function hideLessonPopup\(\) \{
        if\(!popup\) return;
        popup\.style\.display = 'none';
      \}
    </script>'''

# Use a simpler approach - find and replace the exact text
old_popup_text = '''    <div id="lesson-popup" style="position: fixed; display: none; background: rgba(15, 23, 42, 0.95); color: #e2e8f0; padding: 0.5rem 1rem; border-radius: 0.5rem; border: 1px solid #3b82f6; pointer-events: none; z-index: 1000; font-size: 0.9rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);"></div>
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
    </script>'''

new_tooltip_and_js = '''  <!-- Popup & Game Logic Scripts -->
  <style>
      #lesson-tooltip {
          position: fixed;
          background: rgba(15, 23, 42, 0.95);
          backdrop-filter: blur(12px);
          color: #f1f5f9;
          padding: 0.75rem 1.25rem;
          border-radius: 0.75rem;
          font-size: 0.95rem;
          font-weight: 600;
          pointer-events: none;
          z-index: 10000;
          opacity: 0;
          transition: opacity 0.15s ease;
          border: 1px solid rgba(255, 255, 255, 0.15);
          box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
          white-space: nowrap;
      }
      #lesson-tooltip.visible {
          opacity: 1;
      }
      /* Hover interactions & Transitions */
      rect[id^="u"], path[id^="u"] {
          transform-box: fill-box;
          transform-origin: center;
          transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), filter 0.2s ease, stroke-width 0.2s ease;
      }
      .segment-hover {
          transform: scale(1.05);
          filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.9));
          fill-opacity: 0.15;
      }

      /* Starred Lesson Glow & Animation */
      @keyframes star-pulse {
        0%, 100% { stroke-opacity: 0.8; stroke-width: 0.12; filter: drop-shadow(0 0 2px #a78bfa); }
        50% { stroke-opacity: 1; stroke-width: 0.25; filter: drop-shadow(0 0 6px #8b5cf6); }
      }
      .starred-lesson-glow {
        stroke: #c4b5fd !important;
        stroke-dasharray: 0.3, 0.1;
        animation: star-pulse 1.5s infinite ease-in-out;
      }
      @keyframes star-twinkle {
          0%, 100% { opacity: 0.4; transform: scale(0.8); }
          50% { opacity: 1; transform: scale(1.3); }
      }
      .star-icon {
          animation: star-twinkle 2s infinite ease-in-out;
          font-family: inherit;
          pointer-events: none;
          transform-box: fill-box;
          transform-origin: center;
          font-size: 0.6px;
          user-select: none;
      }
  </style>

  <div id="lesson-tooltip"></div>
  
  <script>
    const tooltip = document.getElementById('lesson-tooltip');

    function showLessonPopup(e, title) {
      if(!title) return;
      let displayText = title;
      const target = e.target;
      
      if (target && target.id && target.id.match(/^u[\\w]+-l\\d+$/)) {
          target.classList.add('segment-hover');
      }

      // Translate title if in Chinese mode
      const lang = localStorage.getItem("arisEduLanguage");
      const isChinese = (lang === "chinese" || lang === "traditional");
      const t = window.arisEduTranslations;

      if (isChinese && t) {
          if (t[displayText]) {
              displayText = t[displayText];
          }
          if (lang === "traditional" && window.OpenCCConverter) {
              displayText = window.OpenCCConverter(displayText);
          }
      }

      // Check Progress & add status prefix
      if(target) {
           const fill = target.getAttribute('fill');
           if (fill === '#16a34a' || fill === '#16A34A') {
                if (isChinese && t) {
                    let status = t["COMPLETED"] || "已完成";
                    if (lang === "traditional" && window.OpenCCConverter) status = window.OpenCCConverter(status);
                    displayText = status + " \\u2714 " + displayText;
                } else {
                    displayText = "COMPLETED \\u2714 " + displayText;
                }
           } else if (fill === '#f97316' || fill === '#F97316') {
                if (isChinese && t) {
                    let status = t["IN PROGRESS"] || "进行中";
                    if (lang === "traditional" && window.OpenCCConverter) status = window.OpenCCConverter(status);
                    displayText = status + " " + displayText;
                } else {
                    displayText = "IN PROGRESS " + displayText;
                }
           }
      }

      tooltip.textContent = displayText;
      tooltip.classList.add('visible');
      moveLessonPopup(e);
    }

    function moveLessonPopup(e) {
      if (!tooltip.classList.contains('visible')) return;
      const offset = 15;
      let x = e.clientX + offset;
      let y = e.clientY + offset;
      
      const rect = tooltip.getBoundingClientRect();
      const winW = window.innerWidth;
      const winH = window.innerHeight;
      
      if (x + rect.width > winW) x = e.clientX - rect.width - offset;
      if (y + rect.height > winH) y = e.clientY - rect.height - offset;
      
      tooltip.style.left = x + 'px';
      tooltip.style.top = y + 'px';
    }

    function hideLessonPopup() {
      tooltip.classList.remove('visible');
      document.querySelectorAll('.segment-hover').forEach(el => el.classList.remove('segment-hover'));
    }

    function markLessonStarted(unit, lesson) {
      localStorage.setItem(`geometry_u${unit}_l${lesson}_started`, 'true');
    }

    function applyProgressColors() {
        const progressMap = {};
        for (let i = 0; i < localStorage.length; i++) {
          const key = localStorage.key(i);
          if (!key || !key.startsWith('geometry_u')) continue;
          const match = key.match(/^geometry_u(.+)_l(\\d+)_(started|completed)$/);
          if (!match) continue;
          const u = match[1], l = match[2], type = match[3];
          const mapKey = `${u}_${l}`;
          if (!progressMap[mapKey]) progressMap[mapKey] = { unit: u, lesson: l };
          if (localStorage.getItem(key) === 'true') progressMap[mapKey][type] = true;
        }

        for (const mapKey in progressMap) {
          const { unit, lesson, started, completed } = progressMap[mapKey];
          const elementId = `u${unit}-l${lesson}`;
          const el = document.getElementById(elementId);
          if(el) {
              if (completed) {
                el.setAttribute('fill', '#16a34a');
                el.setAttribute('fill-opacity', '0.7');
              } else if (started) {
                el.setAttribute('fill', '#f97316');
                el.setAttribute('fill-opacity', '0.6');
              }
          }
        }
    }

    function addStarEffects() {
        const lessons = document.querySelectorAll('rect');
        lessons.forEach(el => {
            const onmouseenter = el.getAttribute('onmouseenter');
            if (onmouseenter && onmouseenter.includes('\\u2B50')) {
                if (!el.id || !el.id.startsWith('u')) return;

                el.classList.add('starred-lesson-glow');

                const x = parseFloat(el.getAttribute('x'));
                const y = parseFloat(el.getAttribute('y'));
                const w = parseFloat(el.getAttribute('width'));
                const h = parseFloat(el.getAttribute('height'));

                if (!isNaN(x) && !isNaN(y) && !isNaN(w) && !isNaN(h)) {
                    const positions = [
                        { cx: x + w - 1.0, cy: y + 0.5, delay: '0.2s' },
                        { cx: x + 1.0, cy: y + h - 0.5, delay: '1.2s' }
                    ];

                    positions.forEach(pos => {
                        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                        text.textContent = '\\u2728';
                        text.setAttribute('x', pos.cx);
                        text.setAttribute('y', pos.cy);
                        text.setAttribute('text-anchor', 'middle');
                        text.setAttribute('dominant-baseline', 'middle');
                        text.classList.add('star-icon');
                        text.style.animationDelay = pos.delay;
                        
                        if (el.parentNode) {
                             el.parentNode.insertBefore(text, el.nextSibling);
                        }
                    });
                }
            }
        });
    }

    function clearAllProgress() {
        const keysToRemove = [];
        for (let i = 0; i < localStorage.length; i++) {
          const key = localStorage.key(i);
          if (key && key.startsWith('geometry_u')) {
            keysToRemove.push(key);
          }
        }
        keysToRemove.forEach(k => localStorage.removeItem(k));
        
        document.querySelectorAll('rect[id^="u"], path[id^="u"]').forEach(seg => {
            seg.setAttribute('fill', 'white');
            seg.setAttribute('fill-opacity', '0');
        });
    }

    document.addEventListener('DOMContentLoaded', () => {
        applyProgressColors();
        addStarEffects();
    });
  </script>'''

content = content.replace(old_popup_text, new_tooltip_and_js)

# ============================================================
# 5. Write the fixed file
# ============================================================

if content != original:
    with open(FILEPATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: geometry.html fixed!")
    
    # Verify key features
    checks = [
        ('main.css link', 'styles/main.css' in content),
        ('lesson-tooltip div', 'id="lesson-tooltip"' in content),
        ('lesson-tooltip CSS', '#lesson-tooltip {' in content),
        ('.segment-hover CSS', '.segment-hover {' in content),
        ('.starred-lesson-glow CSS', '.starred-lesson-glow {' in content),
        ('.star-icon CSS', '.star-icon {' in content),
        ('markLessonStarted function', 'function markLessonStarted' in content),
        ('applyProgressColors function', 'function applyProgressColors' in content),
        ('addStarEffects function', 'function addStarEffects' in content),
        ('clearAllProgress function', 'function clearAllProgress' in content),
        ('DOMContentLoaded', "addEventListener('DOMContentLoaded'" in content),
        ('onclick markLessonStarted', "onclick=\"markLessonStarted(" in content),
        ('rect IDs (u1-l1)', 'id="u1-l1"' in content),
        ('rect IDs (u13-l7)', 'id="u13-l7"' in content),
        ('old popup removed', 'lesson-popup' not in content),
        ('old inline styles removed', 'position: relative !important' not in content),
        ('page title with SVG', 'title-grad' in content),
        ('geometry_ localStorage prefix', "geometry_u" in content),
        ('overflow boundary check', 'rect.width > winW' in content),
        ('translation support', 'arisEduTranslations' in content),
    ]
    
    all_pass = True
    for name, result in checks:
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  {status}: {name}")
    
    if all_pass:
        print("\nAll 20 checks PASSED!")
    else:
        print("\nSome checks FAILED - review needed")
else:
    print("No changes made (unexpected)")
