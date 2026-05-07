"""Convert the 5 special homepages (bio, chem, geometry, physics, ap_physics1)
to use the same horizontal-bar layout as the standard pages, by parsing the
existing hardcoded SVG markup to extract lesson hrefs and tooltip names.

The original visual treatment (DNA helix, flask, etc.) is replaced with the
uniform 2-col horizontal bar layout — matching the user's request.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent / "ArisEdu Project Folder" / "CourseHomepage"

SPECIAL = ["bio", "chem", "geometry", "physics", "ap_physics1"]


# Per-file overrides where parsing is ambiguous
COURSE_DEFAULTS = {
    "bio":         {"title": "High School: Biology",   "prefix": "bio",     "section": "biology"},
    "chem":        {"title": "High School: Chemistry", "prefix": "chem",    "section": "chemistry"},
    "geometry":    {"title": "High School: Geometry",  "prefix": "geom",    "section": "geometry"},
    "physics":     {"title": "High School: Physics",   "prefix": "phys",    "section": "physics"},
    "ap_physics1": {"title": "AP Physics 1: Algebra-Based", "prefix": "apphys1", "section": "ap_physics1"},
}


def detect_prefix(text: str, fallback: str) -> str:
    m = re.search(r"localStorage\.\w+\(\s*[`'\"]([a-zA-Z0-9_]+)_u\$\{", text)
    if m:
        return m.group(1)
    m = re.search(r"localStorage\.\w+\(\s*[`'\"]([a-zA-Z0-9_]+)_u['\"]\s*\+", text)
    if m:
        return m.group(1)
    return fallback


def detect_title(text: str, fallback: str) -> str:
    m = re.search(r"<title>([^<]+)</title>", text)
    return m.group(1).strip() if m else fallback


# --- Extraction --------------------------------------------------------
RECT_RE = re.compile(
    r'id="u(?P<u>\d+)-l(?P<l>\d+)"',
)

# Find an anchor or onclick href adjacent to a u{u}-l{l} rect, plus tooltip
HREF_BLOCK_RE = re.compile(
    r'<a\s+href="(?P<href>[^"]+)"[^>]*>\s*<rect[^>]*id="u(?P<u>\d+)-l(?P<l>\d+)"[^>]*onmouseenter="showLessonPopup\(event,\s*\'(?P<tip>[^\']*)\''
)

ONCLICK_BLOCK_RE = re.compile(
    r"window\.location\.href='(?P<href>[^']+)';[^>]*>\s*<rect[^>]*id=\"u(?P<u>\d+)-l(?P<l>\d+)\"[^>]*onmouseenter=\"showLessonPopup\(event,\s*'(?P<tip>[^']*)'"
)


def extract_units(text: str):
    """Return {unitNum: [(lessonNum, href, tooltip), ...]} parsed from raw SVG.
    Element-agnostic: matches any tag (rect, path, etc.) with id="u{u}-l{l}",
    then finds the nearest preceding href (in <a> or onclick) and tooltip
    inside the same element opening tag.
    """
    units: dict[int, list[tuple[int, str, str]]] = {}

    id_re = re.compile(r'id="u(\d+)-l(\d+)"')
    # We need to find: surrounding href + tooltip inside this opening tag
    href_a_re = re.compile(r'<a\s+href="([^"]+)"[^>]*>\s*$', re.S)
    href_onclick_re = re.compile(r"window\.location\.href='([^']+)'")
    tooltip_re = re.compile(r"showLessonPopup\(\s*event\s*,\s*'([^']*)'")

    for m in id_re.finditer(text):
        u = int(m.group(1))
        l = int(m.group(2))
        # Locate opening of this element: nearest '<' before id position
        tag_open = text.rfind('<', 0, m.start())
        tag_close = text.find('>', m.end())
        if tag_open == -1 or tag_close == -1:
            continue
        element_open = text[tag_open:tag_close + 1]
        # tooltip is inside element opening tag
        tip_m = tooltip_re.search(element_open)
        tip = tip_m.group(1) if tip_m else f"Lesson {u}.{l}"

        # Look for href: try preceding <a href="..."> within ~400 chars
        prelude = text[max(0, tag_open - 600):tag_open]
        href_m = list(href_a_re.finditer(prelude))
        href = None
        if href_m:
            href = href_m[-1].group(1)
        else:
            # Try onclick="...window.location.href='...'..." within parent <a>/<g>
            parent_open = text.rfind('<a ', 0, tag_open)
            if parent_open == -1:
                parent_open = text.rfind('<g ', 0, tag_open)
            if parent_open != -1:
                parent_close = text.find('>', parent_open)
                hm = href_onclick_re.search(text[parent_open:parent_close + 1] if parent_close != -1 else '')
                if hm:
                    href = hm.group(1)
            if href is None:
                # search element_open itself for onclick href
                hm = href_onclick_re.search(element_open)
                if hm:
                    href = hm.group(1)
        if not href:
            continue
        units.setdefault(u, []).append((l, href, tip))

    # de-duplicate per (u, l): keep first occurrence
    for u in list(units.keys()):
        seen = {}
        for l, h, t in units[u]:
            seen.setdefault(l, (h, t))
        units[u] = sorted([(l, *v) for l, v in seen.items()], key=lambda x: x[0])
    return units


def derive_course_data(units):
    """From the parsed lessons, build numUnits, units count map, lessonNames,
    detect course folder, and detect test href pattern."""
    lessonNames = {}
    unitsCounts = {}
    folder = None
    test_href_template = None
    lesson_href_template = None
    for u in sorted(units.keys()):
        items = units[u]
        names = []
        for (l, href, tip) in items:
            # The last item is conventionally the unit test (highest l value).
            # We detect by href containing "_Test" or being the max l with no Lesson{n}.{m} pattern.
            is_test = ("_Test" in href) or ("Test_Practice" in href) or l == len(items)
            if is_test and l == max(it[0] for it in items):
                if test_href_template is None:
                    test_href_template = href
                continue
            # Extract human-readable lesson name from tooltip
            name = re.sub(r"^\s*(?:Lesson\s+)?\d+\.\d+[\s:]*", "", tip).strip()
            # Some tooltips include the lesson number prefix
            if not name:
                name = tip
            names.append(name)
            if folder is None:
                m = re.search(r"([A-Za-z0-9_]+Lessons|APPhys1_Lessons)", href)
                if m:
                    folder = m.group(1)
            # Prefer the FIRST (smallest u, l) lesson href as the template
            if lesson_href_template is None:
                lesson_href_template = href
        lessonNames[u] = names
        unitsCounts[u] = len(items)  # includes test (if present)
    return {
        "folder": folder or "",
        "lesson_href_template": lesson_href_template or "",
        "test_href_template": test_href_template or "",
        "units": unitsCounts,
        "lessonNames": lessonNames,
        "numUnits": max(unitsCounts.keys()) if unitsCounts else 0,
    }


# --- Page generation ---------------------------------------------------

PAGE_TEMPLATE = r"""<!doctype html>
<html lang="en" class="h-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>__TITLE__</title>
  <script src="/_sdk/element_sdk.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
  <script src="../theme_manager.js"></script>
  <script type="module">
    import { auth, db } from '../firebase-config.js';
    window.auth = auth;
    window.db = db;
  </script>
<script src="../scripts/analytics-helper.js"></script>
<script src="../scripts/translation_loader.js" data-section="__SECTION__" data-base="../translations"></script>
</head>
<body class="dark-mode h-full">
<script src="../scripts/taskbar.js"></script>
  <main class="main-container">
    <div class="logo-title-wrapper" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
      <h1 id="company-name" class="logo-font page-title" style="font-size: 3rem; margin-bottom: 0;">__TITLE__</h1>
    </div>
    <div id="courses-container" class="courses-container" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.25rem 2rem; padding: 1rem;"></div>
  </main>

  <script src="../../search_data.js"></script>
  <script src="../../search_logic.js"></script>

<style>
  rect[id^="u"], path[id^="u"] { transform-box: fill-box; transform-origin: center; transition: transform 0.2s ease; }
  #lesson-tooltip { position: fixed; background: rgba(15, 23, 42, 0.95); backdrop-filter: blur(8px); color: white; padding: 0.75rem 1rem; border-radius: 0.75rem; font-size: 0.95rem; font-weight: 600; pointer-events: none; z-index: 10000; opacity: 0; transition: opacity 0.15s ease; display: none; max-width: 250px; }
  #lesson-tooltip[data-visible="true"] { opacity: 1; display: block; }
</style>

<script>
  const courseConfig = __COURSECONFIG__;
  const COURSE_PREFIX = '__PREFIX__';

  function lessonHref(unitNum, itemNum) {
    return __LESSON_HREF_FN__;
  }
  function testHref(unitNum) {
    return __TEST_HREF_FN__;
  }

  function generateUnitSVG(unitNum, lessonCount) {
    const totalItems = lessonCount;
    const realLessons = lessonCount - 1;
    const _barX = 12, _barY = 2, _barW = 86, _barH = 8;
    const spacing = _barW / totalItems;
    let segments = '';
    for (let itemNum = 1; itemNum <= totalItems; itemNum++) {
      const xPos = (_barX + (itemNum - 1) * spacing).toFixed(3);
      const segW = spacing.toFixed(3);
      let href, tooltipName;
      if (itemNum <= realLessons) {
        href = lessonHref(unitNum, itemNum);
        const name = (courseConfig.lessonNames && courseConfig.lessonNames[unitNum]) ? courseConfig.lessonNames[unitNum][itemNum - 1] : '';
        tooltipName = name ? `${unitNum}.${itemNum} ${name}` : `Lesson ${unitNum}.${itemNum}`;
      } else {
        href = testHref(unitNum);
        tooltipName = `Unit ${unitNum} Test`;
      }
      segments += `<a href="${href}" onclick="markLessonStarted('${unitNum}', ${itemNum})">
    <rect id="u${unitNum}-l${itemNum}" stroke="none" x="${xPos}" y="${_barY}" width="${segW}" height="${_barH}" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(event, '${tooltipName.replace(/\'/g, "&#39;")}', ${unitNum}, ${itemNum})" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect></a>
  <line x1="${xPos}" y1="${_barY}" x2="${xPos}" y2="${_barY + _barH}" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />`;
    }
    return `<div style="position: relative; width: 100%;"><svg viewBox="0 0 100 12" fill="none" stroke="currentColor" stroke-width="0.2" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: auto; color: inherit;"><text x="${_barX - 2}" y="${_barY + _barH / 2 + 1}" text-anchor="end" fill="currentColor" stroke="none" font-size="2.6" font-family="ui-sans-serif, system-ui, sans-serif" font-weight="600" style="pointer-events: none;">Unit ${unitNum}</text><rect x="${_barX}" y="${_barY}" width="${_barW}" height="${_barH}" rx="1" ry="1" fill="none" stroke="currentColor" stroke-width="0.3" /><rect id="fill-unit-${unitNum}" x="${_barX}" y="${_barY}" width="${_barW}" height="${_barH}" rx="1" ry="1" fill="#9ca3af" fill-opacity="0.15" stroke="none" /><g id="segments-unit-${unitNum}">
${segments}</g></svg></div>`;
  }

  function populateGrid() {
    const container = document.getElementById('courses-container');
    for (const [unitNum, lessonCount] of Object.entries(courseConfig.units)) {
      container.innerHTML += generateUnitSVG(parseInt(unitNum), lessonCount);
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    populateGrid();
    applyProgressColors();
    if (typeof StudentAnalytics !== 'undefined') {
      try {
        const analytics = new StudentAnalytics();
        analytics.trackLessonView('__SECTION__', 0, 0);
        analytics.updateLearningStreak();
      } catch (e) { console.warn('Analytics init failed:', e); }
    }
  });

  let tooltipEl = null;
  function getOrCreateTooltip() { if (!tooltipEl) { tooltipEl = document.createElement('div'); tooltipEl.id = 'lesson-tooltip'; document.body.appendChild(tooltipEl); } return tooltipEl; }
  function showLessonPopup(event, lessonTitle, unitNum, lessonNum) {
    const tooltip = getOrCreateTooltip();
    let status = '';
    const isCompleted = localStorage.getItem(`${COURSE_PREFIX}_u${unitNum}_l${lessonNum}_completed`) === 'true';
    const isStarted = localStorage.getItem(`${COURSE_PREFIX}_u${unitNum}_l${lessonNum}_started`) === 'true';
    if (isCompleted) status = '✅ COMPLETED\n';
    else if (isStarted) status = '⌛ IN PROGRESS\n';
    tooltip.textContent = status + lessonTitle;
    tooltip.setAttribute('data-visible', 'true');
  }
  function moveLessonPopup(event) { const tooltip = getOrCreateTooltip(); tooltip.style.left = (event.pageX + 12) + 'px'; tooltip.style.top = (event.pageY + 12) + 'px'; }
  function hideLessonPopup() { const tooltip = getOrCreateTooltip(); tooltip.setAttribute('data-visible', 'false'); }
  function markLessonStarted(unit, lesson) { localStorage.setItem(`${COURSE_PREFIX}_u${unit}_l${lesson}_started`, 'true'); applyProgressColors(); }
  function applyProgressColors() {
    for (const [u, count] of Object.entries(courseConfig.units)) {
      for (let l = 1; l <= count; l++) {
        const segment = document.getElementById(`u${u}-l${l}`);
        if (segment) {
          const isCompleted = localStorage.getItem(`${COURSE_PREFIX}_u${u}_l${l}_completed`) === 'true';
          const isStarted = localStorage.getItem(`${COURSE_PREFIX}_u${u}_l${l}_started`) === 'true';
          if (isCompleted) { segment.setAttribute('fill', '#16a34a'); segment.setAttribute('fill-opacity', '0.7'); }
          else if (isStarted) { segment.setAttribute('fill', '#f97316'); segment.setAttribute('fill-opacity', '0.6'); }
        }
      }
    }
  }
  window.addEventListener('storage', function(e) {
    if (e.key && e.key.startsWith(COURSE_PREFIX + '_u')) applyProgressColors();
  });
</script>
<script src="../scripts/dev_tools.js"></script>
<script>
  if (window._isDevUser && window._isDevUser()) {
    var dcb = document.getElementById('dev-clear-btn');
    if (dcb) dcb.style.display = '';
  }
</script>
</body>
</html>
"""


def js_dict(d: dict) -> str:
    """Render a Python dict as a JSON-ish JS literal (keys are numbers)."""
    parts = []
    for k, v in sorted(d.items(), key=lambda kv: int(kv[0])):
        if isinstance(v, list):
            inner = ", ".join(json_string(s) for s in v)
            parts.append(f"      {k}: [{inner}]")
        else:
            parts.append(f"      {k}: {v}")
    return "{\n" + ",\n".join(parts) + "\n    }"


def json_string(s: str) -> str:
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"


def build_lesson_href_fn(template: str, units: dict) -> str:
    """Convert an example lesson href into a JS template-literal expression
    parameterized by unitNum and itemNum."""
    if not template:
        return "''"
    # Find the unit and lesson numbers in this template; we need to know which
    # unit/lesson it represents to substitute correctly.
    # Look for patterns like "/Unit{u}/" and "Lesson(?:\s|%20)?{u}.{l}_Video"
    expr = template
    m = re.search(r"/Unit(\d+)/", expr)
    if not m:
        return f"`{expr}`"
    u_seen = m.group(1)
    # Find lesson tail
    lm = re.search(rf"Lesson(\s|%20)?{u_seen}\.(\d+)_Video\.html", expr)
    if not lm:
        # try numerics other format
        lm = re.search(r"Lesson(\s|%20)?(\d+)\.(\d+)_Video\.html", expr)
        if not lm:
            return f"`{expr}`"
    sep = lm.group(1) or ""
    # Replace /Unit{u_seen}/ with /Unit${unitNum}/
    expr = re.sub(rf"/Unit{u_seen}/", "/Unit${unitNum}/", expr, count=1)
    # Replace Lesson{sep}{u}.{l}_Video.html with Lesson{sep}${unitNum}.${itemNum}_Video.html
    expr = re.sub(
        rf"Lesson(\s|%20)?{u_seen}\.\d+_Video\.html",
        f"Lesson{sep}${{unitNum}}.${{itemNum}}_Video.html",
        expr, count=1,
    )
    return f"`{expr}`"


def build_test_href_fn(template: str, lesson_href_template: str, units: dict) -> str:
    """Build JS expr for unit test href."""
    if template:
        expr = template
        # Find the unit number embedded and replace with ${unitNum}
        m = re.search(r"/Unit(\d+)/", expr)
        if m:
            u_seen = m.group(1)
            expr = re.sub(rf"/Unit{u_seen}/", "/Unit${unitNum}/", expr, count=1)
            expr = re.sub(rf"Unit{u_seen}_Test", "Unit${unitNum}_Test", expr, count=1)
        return f"`{expr}`"
    if lesson_href_template:
        # Derive: replace LessonX.Y_Video.html (URL-encoded or not) with UnitX_Test_Practice.html
        candidate = lesson_href_template
        m = re.search(r"/Unit(\d+)/", candidate)
        if m:
            u_seen = m.group(1)
            candidate = re.sub(
                rf"Lesson(?:\s|%20)?{u_seen}\.\d+_Video\.html",
                f"Unit{u_seen}_Test_Practice.html",
                candidate, count=1,
            )
            candidate = re.sub(rf"/Unit{u_seen}/", "/Unit${unitNum}/", candidate, count=1)
            candidate = re.sub(rf"Unit{u_seen}_Test", "Unit${unitNum}_Test", candidate, count=1)
        return f"`{candidate}`"
    return "''"


def render_course_config(data) -> str:
    return (
        "{\n"
        f"    title: 'High School',\n"
        f"    folder: '{data['folder']}',\n"
        f"    numUnits: {data['numUnits']},\n"
        f"    units: " + js_dict(data["units"]) + ",\n"
        f"    lessonNames: " + js_dict(data["lessonNames"]) + "\n"
        "  }"
    )


def process(name: str) -> bool:
    fp = ROOT / f"{name}.html"
    text = fp.read_text(encoding="utf-8")
    units = extract_units(text)
    if not units:
        print(f"  [SKIP] {name}: no rects parsed")
        return False
    data = derive_course_data(units)
    defaults = COURSE_DEFAULTS[name]
    title = detect_title(text, defaults["title"])
    prefix = detect_prefix(text, defaults["prefix"])

    course_config = render_course_config(data)
    lesson_href_fn = build_lesson_href_fn(data["lesson_href_template"], data["units"])
    test_href_fn = build_test_href_fn(data["test_href_template"], data["lesson_href_template"], data["units"])

    out = (PAGE_TEMPLATE
           .replace("__TITLE__", title)
           .replace("__SECTION__", defaults["section"])
           .replace("__PREFIX__", prefix)
           .replace("__COURSECONFIG__", course_config)
           .replace("__LESSON_HREF_FN__", lesson_href_fn)
           .replace("__TEST_HREF_FN__", test_href_fn))

    fp.write_text(out, encoding="utf-8")
    print(f"  [OK ] {name}: prefix={prefix} folder={data['folder']} units={data['numUnits']}")
    return True


if __name__ == "__main__":
    for name in SPECIAL:
        process(name)
