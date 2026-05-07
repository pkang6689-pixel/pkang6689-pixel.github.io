"""
Convert course homepage layouts from vertical 4-col grid SVG bars to
horizontal 2-col grid SVG bars. Operates on standard course pages that
use a `generateUnitSVG` function. Special pages (bio/chem/geometry/
physics/ap_physics1) are handled separately.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent / "ArisEdu Project Folder" / "CourseHomepage"

# Standard files (have generateUnitSVG)
STANDARD = [
    "algebra1", "algebra2", "anatomy", "ap_biology", "ap_calculus",
    "ap_chemistry", "ap_environmental_science", "ap_hug",
    "ap_physics2", "ap_physics_mechanics", "ap_statistics",
    "astronomy", "earth_science", "environmental_science",
    "financial_math", "integrated_science", "linear_algebra",
    "marine_science", "ms_algebra1", "ms_algebra2", "ms_bio",
    "ms_chem", "ms_geometry", "ms_physics", "precalculus",
    "statistics", "trigonometry",
]

NEW_CONTAINER_STYLE = (
    'style="display: grid; grid-template-columns: repeat(2, 1fr); '
    'gap: 1.25rem 2rem; padding: 1rem;"'
)

# Geometry constants (match what we used in algebra1.html)
HBAR_VARS = """const _barX = 12, _barY = 2, _barW = 86, _barH = 8;"""

# ---- Group A: algebra-style template-literal ---------------------------
# Uses: itemNum, lessonCount, courseConfig.lessonNames, totalItems/realLessons
# Detect via signature: `function generateUnitSVG(unitNum, lessonCount)` and
# presence of `courseConfig.lessonNames` AND no `lessonMappings`.
TEMPLATE_A = r"""  // Generate unit SVG with smart spacing (horizontal layout)
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
        href = `__LESSON_HREF_A__`;
        const name = (courseConfig.lessonNames && courseConfig.lessonNames[unitNum]) ? courseConfig.lessonNames[unitNum][itemNum - 1] : '';
        tooltipName = name ? `${unitNum}.${itemNum} ${name}` : `Lesson ${unitNum}.${itemNum}`;
      } else {
        href = `__TEST_HREF_A__`;
        tooltipName = `Unit ${unitNum} Test`;
      }

      segments += `<a href="${href}" onclick="markLessonStarted('${unitNum}', ${itemNum})">
    <rect id="u${unitNum}-l${itemNum}" stroke="none" x="${xPos}" y="${_barY}" width="${segW}" height="${_barH}" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(event, '${tooltipName.replace(/\'/g, "&#39;")}', ${unitNum}, ${itemNum})" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect></a>
  <line x1="${xPos}" y1="${_barY}" x2="${xPos}" y2="${_barY + _barH}" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />`;
    }

    return `<div style="position: relative; width: 100%;"><svg viewBox="0 0 100 12" fill="none" stroke="currentColor" stroke-width="0.2" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: auto; color: inherit;"><text x="${_barX - 2}" y="${_barY + _barH / 2 + 1}" text-anchor="end" fill="currentColor" stroke="none" font-size="2.6" font-family="ui-sans-serif, system-ui, sans-serif" font-weight="600" style="pointer-events: none;">Unit ${unitNum}</text><rect x="${_barX}" y="${_barY}" width="${_barW}" height="${_barH}" rx="1" ry="1" fill="none" stroke="currentColor" stroke-width="0.3" /><rect id="fill-unit-${unitNum}" x="${_barX}" y="${_barY}" width="${_barW}" height="${_barH}" rx="1" ry="1" fill="#9ca3af" fill-opacity="0.15" stroke="none" /><g id="segments-unit-${unitNum}">
${segments}</g></svg></div>`;
  }
"""

# ---- Group B: anatomy/finmath-style string-concat ----------------------
# Uses: lessonMappings[unitNum] = [{num, name}, ...]
# Generates lessons (no test in many B files); some include test.
# We'll preserve original href patterns; detect them from the file.
TEMPLATE_B = r"""  function generateUnitSVG(unitNum, lessonCount) {
    const lessons = (typeof lessonMappings !== 'undefined' && lessonMappings[unitNum]) ? lessonMappings[unitNum] : [];
    const totalItems = lessons.length + 1; // +1 for unit test
    const _barX = 12, _barY = 2, _barW = 86, _barH = 8;
    const spacing = _barW / totalItems;
    let segments = '';

    for (let i = 0; i < lessons.length; i++) {
      const lesson = lessons[i];
      const xPos = (_barX + i * spacing).toFixed(3);
      const segW = spacing.toFixed(3);
      const href = '__LESSON_HREF_B__';
      const tooltip = ('Lesson ' + unitNum + '.' + lesson.num + ': ' + lesson.name).replace(/'/g, "&#39;");
      segments += '<a href="' + href + '" onclick="markLessonStarted(\'' + unitNum + '\', ' + (i+1) + ')">\n' +
        '    <rect id="u' + unitNum + '-l' + (i+1) + '" stroke="none" x="' + xPos + '" y="' + _barY + '" width="' + segW + '" height="' + _barH + '" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(event, \'' + tooltip + '\', ' + unitNum + ', ' + (i+1) + ')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect>\n' +
        '</a>\n' +
        '  <line x1="' + xPos + '" y1="' + _barY + '" x2="' + xPos + '" y2="' + (_barY + _barH) + '" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />\n';
    }

    // Unit Test segment (last)
    const testIdx = lessons.length;
    const testXPos = (_barX + testIdx * spacing).toFixed(3);
    const testW = spacing.toFixed(3);
    const testHref = '__TEST_HREF_B__';
    segments += '<a href="' + testHref + '" onclick="markLessonStarted(\'' + unitNum + '\', ' + (testIdx + 1) + ')">\n' +
      '    <rect id="u' + unitNum + '-l' + (testIdx + 1) + '" stroke="none" x="' + testXPos + '" y="' + _barY + '" width="' + testW + '" height="' + _barH + '" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(event, \'Unit ' + unitNum + ' Test\', ' + unitNum + ', ' + (testIdx + 1) + ')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect>\n' +
      '</a>\n' +
      '  <line x1="' + testXPos + '" y1="' + _barY + '" x2="' + testXPos + '" y2="' + (_barY + _barH) + '" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />\n';

    return '<div style="position: relative; width: 100%;"><svg viewBox="0 0 100 12" fill="none" stroke="currentColor" stroke-width="0.2" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: auto; color: inherit;"><text x="' + (_barX - 2) + '" y="' + (_barY + _barH / 2 + 1) + '" text-anchor="end" fill="currentColor" stroke="none" font-size="2.6" font-family="ui-sans-serif, system-ui, sans-serif" font-weight="600" style="pointer-events: none;">Unit ' + unitNum + '</text><rect x="' + _barX + '" y="' + _barY + '" width="' + _barW + '" height="' + _barH + '" rx="1" ry="1" fill="none" stroke="currentColor" stroke-width="0.3" /><rect id="fill-unit-' + unitNum + '" x="' + _barX + '" y="' + _barY + '" width="' + _barW + '" height="' + _barH + '" rx="1" ry="1" fill="#9ca3af" fill-opacity="0.15" stroke="none" /><g id="segments-unit-' + unitNum + '">\n' + segments + '</g></svg></div>';
  }
"""

# ---- Group C: AP-style with separate test -----------------------------
# Uses: courseConfig.lessonNames optional, AP folder path scheme, separate
# unit-test segment, lessonNum/lessonCount.
TEMPLATE_C = r"""  function generateUnitSVG(unitNum, lessonCount) {
    let segments = '';
    const totalItems = lessonCount + 1;
    const _barX = 12, _barY = 2, _barW = 86, _barH = 8;
    const spacing = _barW / totalItems;

    for (let lessonNum = 1; lessonNum <= lessonCount; lessonNum++) {
      const xPos = (_barX + (lessonNum - 1) * spacing).toFixed(3);
      const segW = spacing.toFixed(3);
      const folderPath = courseConfig.folder.replace(/\s+/g, '%20');
      const unitText = `Unit ${unitNum}`.replace(/\s+/g, '%20');
      const lessonText = `Lesson${unitNum}.${lessonNum}_Video.html`;
      const topicName = courseConfig.lessonNames?.[unitNum]?.[lessonNum];
      const lessonName = topicName ? `Lesson ${unitNum}.${lessonNum}: ${topicName}` : `Lesson ${unitNum}.${lessonNum}`;
      const href = `../CourseFiles/APLessons/${folderPath}/${unitText}/${lessonText}`;
      segments += `<g onclick="markLessonStarted(${unitNum}, ${lessonNum}); window.location.href='${href}';" style="cursor: pointer;">
    <rect id="u${unitNum}-l${lessonNum}" stroke="none" x="${xPos}" y="${_barY}" width="${segW}" height="${_barH}" fill="white" fill-opacity="0.25" pointer-events="auto" onmouseenter="showLessonPopup(event, '${lessonName.replace(/'/g, "&#39;")}', ${unitNum}, ${lessonNum})" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect></g>
  <line x1="${xPos}" y1="${_barY}" x2="${xPos}" y2="${_barY + _barH}" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />`;
    }

    // Unit Test
    const testXPos = (_barX + lessonCount * spacing).toFixed(3);
    const testW = spacing.toFixed(3);
    const testHref = `AP_Unit_Tests/${courseConfig.folder}/Unit${unitNum}/unit_tests.html`;
    segments += `<g onclick="markLessonStarted(${unitNum}, 99); window.location.href='${testHref}';" style="cursor: pointer;">
    <rect id="u${unitNum}-l99" stroke="none" x="${testXPos}" y="${_barY}" width="${testW}" height="${_barH}" fill="white" fill-opacity="0.25" pointer-events="auto" onmouseenter="showLessonPopup(event, 'Unit ${unitNum} Test', ${unitNum}, 99)" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect></g>
  <line x1="${testXPos}" y1="${_barY}" x2="${testXPos}" y2="${_barY + _barH}" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />`;

    return `<div style="position: relative; width: 100%;"><svg viewBox="0 0 100 12" fill="none" stroke="currentColor" stroke-width="0.2" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: auto; color: inherit;"><text x="${_barX - 2}" y="${_barY + _barH / 2 + 1}" text-anchor="end" fill="currentColor" stroke="none" font-size="2.6" font-family="ui-sans-serif, system-ui, sans-serif" font-weight="600" style="pointer-events: none;">Unit ${unitNum}</text><rect x="${_barX}" y="${_barY}" width="${_barW}" height="${_barH}" rx="1" ry="1" fill="none" stroke="currentColor" stroke-width="0.3" /><rect id="fill-unit-${unitNum}" x="${_barX}" y="${_barY}" width="${_barW}" height="${_barH}" rx="1" ry="1" fill="#9ca3af" fill-opacity="0.15" stroke="none" /><g id="segments-unit-${unitNum}">
${segments}</g></svg></div>`;
  }
"""


def find_function_block(text: str, fn_signature: str) -> tuple[int, int] | None:
    """Find the byte range [start, end] of a JS function whose source begins
    with `fn_signature`. End is AFTER the matching closing brace.
    Uses naive brace counting; assumes the function body doesn't contain
    stray '{' or '}' inside string/regex literals (true for these files).
    """
    idx = text.find(fn_signature)
    if idx == -1:
        return None
    brace_start = text.find('{', idx)
    if brace_start == -1:
        return None
    depth = 0
    for i in range(brace_start, len(text)):
        c = text[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return (idx, i + 1)
    return None


# Detect course folder from existing hrefs (works for groups A and B)
LESSONS_RE = re.compile(r"CourseFiles/([A-Za-z0-9_]+Lessons)/")


def detect_group(text: str) -> str:
    if "AP_Unit_Tests" in text or "../CourseFiles/APLessons/" in text:
        return "C"
    if "lessonMappings" in text and re.search(r"lessonMappings\s*=", text):
        return "B"
    return "A"


def detect_lessons_folder(text: str) -> str | None:
    m = LESSONS_RE.search(text)
    return m.group(1) if m else None


def detect_lesson_filename_prefix(text: str, folder: str | None = None) -> str:
    """Detect 'Lesson' (no space) or 'Lesson ' (with space) prefix.

    Prefer filesystem evidence (most reliable). Fall back to text patterns
    typical of the ORIGINAL files (avoid matching our own emitted templates).
    """
    if folder:
        candidates = [
            ROOT.parent / "CourseFiles" / folder / "Unit1" / "Lesson1.1_Video.html",
            ROOT.parent / "CourseFiles" / folder / "Unit1" / "Lesson 1.1_Video.html",
        ]
        if candidates[0].exists():
            return "Lesson"
        if candidates[1].exists():
            return "Lesson "
    # Look at href construction patterns in source (not in our own template)
    # Group B (string-concat) ORIGINAL: 'Lesson ' + unitNum
    # Group B (template-literal) ORIGINAL: `Lesson${unitNum}` (no space)
    # Heuristic: prefer href-shaped occurrence
    if re.search(r"/Lesson '\s*\+\s*unitNum", text):
        return "Lesson "
    if re.search(r"/Lesson\$\{unitNum\}", text):
        return "Lesson"
    return "Lesson"


def replace_container_div(text: str) -> tuple[str, int]:
    # Match either id="courses-container" or id="grid-container" containers,
    # regardless of attribute order. We rebuild the style attribute uniformly.
    new_total = 0
    # Pattern 1: id-first form (algebra/AP style)
    p1 = re.compile(
        r'(<div\s+id="(?:courses-container|grid-container)"[^>]*?\s)style="[^"]*"'
    )
    text, n1 = p1.subn(rf'\1{NEW_CONTAINER_STYLE}', text)
    new_total += n1
    # Pattern 2: style-first form (anatomy-style: <div style="..." id="grid-container">)
    p2 = re.compile(
        r'<div\s+style="[^"]*"\s+id="(?:courses-container|grid-container)"'
    )
    text, n2 = p2.subn(
        f'<div {NEW_CONTAINER_STYLE} id="grid-container"',
        text,
    )
    new_total += n2
    return text, new_total


def replace_function(text: str, group: str, folder: str, lesson_prefix: str) -> str | None:
    """Replace the existing generateUnitSVG function with the appropriate template."""
    sig_candidates = [
        "function generateUnitSVG(unitNum, lessonCount)",
        "function generateUnitSVG (unitNum, lessonCount)",
    ]
    span = None
    for sig in sig_candidates:
        span = find_function_block(text, sig)
        if span:
            break
    if span is None:
        return None

    if group == "A":
        lesson_href = (
            f"../CourseFiles/{folder}/Unit${{unitNum}}/{lesson_prefix}"
            f"${{unitNum}}.${{itemNum}}_Video.html"
        )
        test_href = (
            f"../CourseFiles/{folder}/Unit${{unitNum}}/Unit${{unitNum}}_Test_Practice.html"
        )
        body = TEMPLATE_A.replace("__LESSON_HREF_A__", lesson_href) \
                          .replace("__TEST_HREF_A__", test_href)
    elif group == "B":
        # In string-concat style: build href via JS string concatenation
        # Avoid f-string brace issues by building via explicit concatenation.
        lesson_href = (
            "../CourseFiles/" + folder + "/Unit' + unitNum + '/" + lesson_prefix +
            "' + unitNum + '.' + lesson.num + '_Video.html"
        )
        test_href = (
            "../CourseFiles/" + folder + "/Unit' + unitNum + '/Unit' + unitNum + '_Test_Practice.html"
        )
        body = TEMPLATE_B.replace("__LESSON_HREF_B__", lesson_href) \
                          .replace("__TEST_HREF_B__", test_href)
    else:  # C
        body = TEMPLATE_C

    return text[:span[0]] + body + text[span[1]:]


def process(name: str) -> bool:
    fp = ROOT / f"{name}.html"
    text = fp.read_text(encoding="utf-8")
    original = text

    text, n_div = replace_container_div(text)

    # Detect group BEFORE rewriting (rewrites use detection on original text)
    group = detect_group(text)
    folder = detect_lessons_folder(text) or ""
    lesson_prefix = detect_lesson_filename_prefix(text, folder)

    # If lessonMappings is declared INSIDE generateUnitSVG, lift it out.
    fn_span = find_function_block(text, "function generateUnitSVG(unitNum, lessonCount)")
    if fn_span:
        fn_body = text[fn_span[0]:fn_span[1]]
        # find `const lessonMappings = { ... };` inside function body
        lm_match = re.search(r"const\s+lessonMappings\s*=\s*\{", fn_body)
        if lm_match:
            # find matching closing brace + semicolon
            start_in_body = lm_match.start()
            brace_open = fn_body.index('{', start_in_body)
            depth = 0
            end_in_body = None
            for j in range(brace_open, len(fn_body)):
                ch = fn_body[j]
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0:
                        end_in_body = j + 1
                        break
            if end_in_body is not None:
                # include trailing semicolon
                while end_in_body < len(fn_body) and fn_body[end_in_body] in ';\r\n\t ':
                    if fn_body[end_in_body] == ';':
                        end_in_body += 1
                        break
                    end_in_body += 1
                lm_block = fn_body[start_in_body:end_in_body]
                # remove from function body
                new_fn_body = fn_body[:start_in_body] + fn_body[end_in_body:]
                # insert lifted block right BEFORE the function
                text = text[:fn_span[0]] + lm_block + "\n\n  " + new_fn_body + text[fn_span[1]:]
                # ensure detection still finds B
                group = "B"

    new_text = replace_function(text, group, folder, lesson_prefix)
    if new_text is None:
        print(f"  [SKIP] {name}: generateUnitSVG not found")
        return False

    if new_text == original:
        print(f"  [NOOP] {name}: no changes")
        return False

    fp.write_text(new_text, encoding="utf-8")
    print(f"  [OK ] {name} (group {group}, folder {folder}, prefix '{lesson_prefix}', divs replaced {n_div})")
    return True


if __name__ == "__main__":
    for name in STANDARD:
        process(name)
