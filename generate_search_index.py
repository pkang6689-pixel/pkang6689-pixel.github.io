"""
Generate search_data.js from actual course files on disk.
Scans CourseFiles/, CourseHomepage/, and content_data/ to produce
a comprehensive, filterable search index with category and type fields.

Usage:  python generate_search_index.py
Output: search_data.js (overwritten in place)
"""

import os, re, json, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
ARISEDU = os.path.join(ROOT, "ArisEdu Project Folder")
COURSE_FILES = os.path.join(ARISEDU, "CourseFiles")
COURSE_HOMEPAGE = os.path.join(ARISEDU, "CourseHomepage")
CONTENT_DATA = os.path.join(ROOT, "content_data")

# ── Mapping helpers ──────────────────────────────────────────────────

# folder name  →  (display name, subject group)
FOLDER_TO_COURSE = {
    "Algebra1Lessons":              ("Algebra 1",               "Math"),
    "Algebra2Lessons":              ("Algebra 2",               "Math"),
    "GeometryLessons":              ("Geometry",                "Math"),
    "PrecalculusLessons":           ("Precalculus",             "Math"),
    "TrigonometryLessons":          ("Trigonometry",            "Math"),
    "StatisticsLessons":            ("Statistics",              "Math"),
    "FinancialMathLessons":         ("Financial Math",          "Math"),
    "LinearAlgebraLessons":         ("Linear Algebra",          "Math"),
    "ChemistryLessons":             ("Chemistry",               "Science"),
    "PhysicsLessons":               ("Physics",                 "Science"),
    "BiologyLessons":               ("Biology",                 "Science"),
    "AnatomyLessons":               ("Anatomy",                 "Science"),
    "AstronomyLessons":             ("Astronomy",               "Science"),
    "EarthScienceLessons":          ("Earth Science",           "Science"),
    "EnvironmentalScienceLessons":  ("Environmental Science",   "Science"),
    "IntegratedScienceLessons":     ("Integrated Science",      "Science"),
    "MarineScienceLessons":         ("Marine Science",          "Science"),
    "MS_Algebra1Lessons":           ("MS Algebra 1",            "Middle School"),
    "MS_Algebra2Lessons":           ("MS Algebra 2",            "Middle School"),
    "MS_GeometryLessons":           ("MS Geometry",             "Middle School"),
    "MS_BiologyLessons":            ("MS Biology",              "Middle School"),
    "MS_ChemistryLessons":          ("MS Chemistry",            "Middle School"),
    "MS_PhysicsLessons":            ("MS Physics",              "Middle School"),
}

# AP subfolder  →  display name
AP_FOLDER_TO_COURSE = {
    "AP Biology":              "AP Biology",
    "AP Calculus AB":          "AP Calculus AB",
    "AP Chemistry":            "AP Chemistry",
    "AP Environmental Science":"AP Environmental Science",
    "AP Human Geography":      "AP Human Geography",
    "AP Physics 2":            "AP Physics 2",
    "AP Physics C - Mechanics":"AP Physics C: Mechanics",
    "AP Statistics":           "AP Statistics",
}

# content_data JSON filename → course display name
CONTENT_JSON_MAP = {
    "algebra_1_lessons.json":            "Algebra 1",
    "algebra_2_lessons.json":            "Algebra 2",
    "geometry_lessons.json":             "Geometry",
    "precalculus_lessons.json":          "Precalculus",
    "trigonometry_lessons.json":         "Trigonometry",
    "statistics_lessons.json":           "Statistics",
    "financial_math_lessons.json":       "Financial Math",
    "linear_algebra_lessons.json":       "Linear Algebra",
    "chemistry_lessons.json":            "Chemistry",
    "physics_lessons.json":              "Physics",
    "biology_lessons.json":              "Biology",
    "anatomy_lessons.json":              "Anatomy",
    "astronomy_lessons.json":            "Astronomy",
    "earth_science_lessons.json":        "Earth Science",
    "environmental_science_lessons.json":"Environmental Science",
    "integrated_science_lessons.json":   "Integrated Science",
    "marine_science_lessons.json":       "Marine Science",
}

# Course homepage filename → display name
HOMEPAGE_MAP = {
    "algebra1.html":                ("Algebra 1",               "Math"),
    "algebra2.html":                ("Algebra 2",               "Math"),
    "geometry.html":                ("Geometry",                "Math"),
    "precalculus.html":             ("Precalculus",             "Math"),
    "trigonometry.html":            ("Trigonometry",            "Math"),
    "statistics.html":              ("Statistics",              "Math"),
    "financial_math.html":          ("Financial Math",          "Math"),
    "linear_algebra.html":          ("Linear Algebra",          "Math"),
    "chem.html":                    ("Chemistry",               "Science"),
    "physics.html":                 ("Physics",                 "Science"),
    "bio.html":                     ("Biology",                 "Science"),
    "anatomy.html":                 ("Anatomy",                 "Science"),
    "astronomy.html":               ("Astronomy",               "Science"),
    "earth_science.html":           ("Earth Science",           "Science"),
    "environmental_science.html":   ("Environmental Science",   "Science"),
    "integrated_science.html":      ("Integrated Science",      "Science"),
    "marine_science.html":          ("Marine Science",          "Science"),
    "ms_algebra1.html":             ("MS Algebra 1",            "Middle School"),
    "ms_algebra2.html":             ("MS Algebra 2",            "Middle School"),
    "ms_geometry.html":             ("MS Geometry",             "Middle School"),
    "ms_bio.html":                  ("MS Biology",              "Middle School"),
    "ms_chem.html":                 ("MS Chemistry",            "Middle School"),
    "ms_physics.html":              ("MS Physics",              "Middle School"),
    "ap_biology.html":              ("AP Biology",              "AP"),
    "ap_calculus.html":             ("AP Calculus AB",          "AP"),
    "ap_chemistry.html":            ("AP Chemistry",            "AP"),
    "ap_environmental_science.html":("AP Environmental Science","AP"),
    "ap_hug.html":                  ("AP Human Geography",      "AP"),
    "ap_physics1.html":             ("AP Physics 1",            "AP"),
    "ap_physics2.html":             ("AP Physics 2",            "AP"),
    "ap_physics_mechanics.html":    ("AP Physics C: Mechanics", "AP"),
    "ap_statistics.html":           ("AP Statistics",           "AP"),
}


def to_web_path(abs_path):
    """Convert absolute path to web-root-relative URL."""
    rel = os.path.relpath(abs_path, ROOT).replace("\\", "/")
    return "/" + rel


# ── Load lesson titles from content_data JSONs ──────────────────────

# key = (course_display_name, lesson_number)  →  title string
_lesson_titles = {}

def load_content_data():
    for fname, course_name in CONTENT_JSON_MAP.items():
        fpath = os.path.join(CONTENT_DATA, fname)
        if not os.path.isfile(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                continue
        for key, val in data.items():
            ln = val.get("lesson_number", "")
            title = val.get("title", "")
            if ln and title:
                _lesson_titles[(course_name, str(ln))] = title

    # Also load AP content_data
    ap_dir = os.path.join(CONTENT_DATA, "AP_Courses")
    if os.path.isdir(ap_dir):
        for fname in os.listdir(ap_dir):
            if not fname.endswith(".json"):
                continue
            fpath = os.path.join(ap_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    continue
            # try to detect course name from the first entry or filename
            course_name = None
            for key, val in data.items():
                c = val.get("course", "")
                if c:
                    course_name = c
                    break
            if not course_name:
                # derive from filename: ap_chemistry_lessons.json -> AP Chemistry
                base = fname.replace("_lessons.json", "").replace("_", " ").title()
                if not base.startswith("Ap "):
                    base = "AP " + base
                else:
                    base = "AP " + base[3:]
                course_name = base
            for key, val in data.items():
                ln = val.get("lesson_number", "")
                title = val.get("title", "")
                if ln and title:
                    _lesson_titles[(course_name, str(ln))] = title


def get_lesson_title(course_name, lesson_number):
    return _lesson_titles.get((course_name, str(lesson_number)), "")


# ── Detect content type from filename ────────────────────────────────

def classify_file(filename):
    """Return (lesson_number, content_type) or None for non-lesson files."""
    # Match patterns like "Lesson1.1_Summary.html" or "Lesson 1.1_Summary.html"
    m = re.match(r"Lesson\s*(\d+\.\d+)_(\w+)\.html$", filename, re.IGNORECASE)
    if m:
        return m.group(1), m.group(2)  # e.g. ("1.1", "Summary")
    return None


def classify_test(filename):
    """Return (unit_num, test_type) for unit test files."""
    m = re.match(r"Unit(\d+)_Test(?:_Practice)?\.html$", filename, re.IGNORECASE)
    if m:
        is_practice = "_Practice" in filename
        return int(m.group(1)), "Test Practice" if is_practice else "Test"
    # AP unit tests
    if filename.lower() == "unit_tests.html":
        return None, "Test"
    return None


# ── Build index ──────────────────────────────────────────────────────

def build_index():
    load_content_data()
    entries = []
    seen_urls = set()

    def add(title, subtitle, url, content, category, content_type):
        if url in seen_urls:
            return
        seen_urls.add(url)
        entries.append({
            "title": title,
            "subtitle": subtitle,
            "url": url,
            "content": content,
            "category": category,
            "type": content_type,
        })

    # ── 1. Static pages ──────────────────────────────────────────────
    add("ArisEdu Home", "Homepage", "/index.html",
        "ArisEdu educational platform homepage", "General", "Page")
    add("Our Courses", "All courses", "/ArisEdu Project Folder/Courses.html",
        "Browse all ArisEdu Mathematics and Science courses", "General", "Page")

    # ── 2. Course homepages ──────────────────────────────────────────
    for fname, (display, group) in HOMEPAGE_MAP.items():
        fpath = os.path.join(COURSE_HOMEPAGE, fname)
        if not os.path.isfile(fpath):
            continue
        url = to_web_path(fpath)
        add(display, f"{group} Course", url,
            f"{display} course homepage", display, "Course")

    # ── 3. Regular course lessons ────────────────────────────────────
    for folder_name, (course_name, group) in FOLDER_TO_COURSE.items():
        folder = os.path.join(COURSE_FILES, folder_name)
        if not os.path.isdir(folder):
            continue

        for unit_dir in sorted(os.listdir(folder)):
            unit_path = os.path.join(folder, unit_dir)
            if not os.path.isdir(unit_path):
                continue
            unit_m = re.match(r"Unit(\d+)", unit_dir)
            if not unit_m:
                continue
            unit_num = int(unit_m.group(1))

            for fname in sorted(os.listdir(unit_path)):
                if not fname.endswith(".html"):
                    continue

                fpath = os.path.join(unit_path, fname)
                url = to_web_path(fpath)

                # Lesson files
                result = classify_file(fname)
                if result:
                    lesson_num, ctype = result
                    lesson_title = get_lesson_title(course_name, lesson_num)
                    display_title = f"Lesson {lesson_num}: {lesson_title}" if lesson_title else f"Lesson {lesson_num}"
                    if ctype != "Summary":
                        display_title += f" - {ctype}"
                    subtitle = f"{course_name} - Unit {unit_num}, Lesson {lesson_num.split('.')[1]} ({ctype})"
                    content_text = f"{course_name} {subtitle}"
                    add(display_title, subtitle, url, content_text, course_name, ctype)
                    continue

                # Unit tests
                test_result = classify_test(fname)
                if test_result and test_result[0] is not None:
                    t_unit, t_type = test_result
                    display_title = f"Unit {t_unit} {t_type}"
                    subtitle = f"{course_name} - Unit {t_unit}"
                    add(display_title, subtitle, url,
                        f"{course_name} Unit {t_unit} {t_type}", course_name, t_type)

    # ── 4. AP course lessons ─────────────────────────────────────────
    ap_root = os.path.join(COURSE_FILES, "APLessons")
    if os.path.isdir(ap_root):
        for ap_folder in sorted(os.listdir(ap_root)):
            ap_path = os.path.join(ap_root, ap_folder)
            if not os.path.isdir(ap_path):
                continue
            course_name = AP_FOLDER_TO_COURSE.get(ap_folder, ap_folder)

            # Practice exam at subject level
            practice_exam = os.path.join(ap_path, "practice_exam.html")
            if os.path.isfile(practice_exam):
                url = to_web_path(practice_exam)
                add(f"{course_name} Practice Exam", f"{course_name}",
                    url, f"{course_name} AP Practice Exam", course_name, "Practice Exam")

            for unit_dir in sorted(os.listdir(ap_path)):
                unit_path = os.path.join(ap_path, unit_dir)
                if not os.path.isdir(unit_path):
                    continue
                unit_m = re.match(r"Unit(\d+)", unit_dir)
                if not unit_m:
                    continue
                unit_num = int(unit_m.group(1))

                for fname in sorted(os.listdir(unit_path)):
                    if not fname.endswith(".html"):
                        continue
                    fpath = os.path.join(unit_path, fname)
                    url = to_web_path(fpath)

                    result = classify_file(fname)
                    if result:
                        lesson_num, ctype = result
                        lesson_title = get_lesson_title(course_name, lesson_num)
                        display_title = f"Lesson {lesson_num}: {lesson_title}" if lesson_title else f"Lesson {lesson_num}"
                        if ctype != "Summary":
                            display_title += f" - {ctype}"
                        subtitle = f"{course_name} - Unit {unit_num}, Lesson {lesson_num.split('.')[1]} ({ctype})"
                        content_text = f"{course_name} {subtitle}"
                        add(display_title, subtitle, url, content_text, course_name, ctype)
                        continue

                    # unit_tests.html
                    if fname.lower() == "unit_tests.html":
                        add(f"Unit {unit_num} Test", f"{course_name} - Unit {unit_num}",
                            url, f"{course_name} Unit {unit_num} Test", course_name, "Test")

    # ── 5. AP Unit Tests folder ──────────────────────────────────────
    ap_tests = os.path.join(COURSE_FILES, "AP_Unit_Tests")
    if os.path.isdir(ap_tests):
        for fname in sorted(os.listdir(ap_tests)):
            if not fname.endswith(".html"):
                continue
            fpath = os.path.join(ap_tests, fname)
            url = to_web_path(fpath)
            display = fname.replace("_", " ").replace(".html", "")
            add(display, "AP Unit Tests", url, f"AP Unit Test: {display}", "AP", "Test")

    return entries


# ── Write output ─────────────────────────────────────────────────────

def main():
    entries = build_index()
    out_path = os.path.join(ROOT, "search_data.js")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("const ARIS_EDU_SEARCH_INDEX = ")
        json.dump(entries, f, indent=2, ensure_ascii=False)
        f.write(";\n")
    print(f"✓ Generated {len(entries)} search entries → search_data.js")

    # Stats
    cats = {}
    types = {}
    for e in entries:
        cats[e["category"]] = cats.get(e["category"], 0) + 1
        types[e["type"]] = types.get(e["type"], 0) + 1
    print("\nBy category:")
    for k in sorted(cats):
        print(f"  {k}: {cats[k]}")
    print("\nBy type:")
    for k in sorted(types):
        print(f"  {k}: {types[k]}")


if __name__ == "__main__":
    main()
