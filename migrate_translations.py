"""
migrate_translations.py
========================
Migrates all HTML files from the old monolithic translation scripts
to the new translation_loader.js system.

Replaces:
    <script src="...global_translations.js..."></script>
    <script src="...spanish_translations.js..."></script>
    <script src="...hindi_translations.js..."></script>

With:
    <script src="...translation_loader.js" data-section="SECTION" data-base="...translations"></script>

Also removes the manual DOMContentLoaded/applyTranslations boilerplate
since the loader handles it automatically.

Run from repo root:
    python migrate_translations.py
"""

import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
ARIS_DIR = os.path.join(REPO_ROOT, "ArisEdu Project Folder")

# Map folder names to section slugs
FOLDER_TO_SECTION = {
    "Algebra1Lessons":              "algebra1",
    "Algebra2Lessons":              "algebra2",
    "AnatomyLessons":               "anatomy",
    "APLessons":                    "ap",
    "AP_Unit_Tests":                "ap",
    "AstronomyLessons":             "astronomy",
    "BiologyLessons":               "biology",
    "ChemistryLessons":             "chemistry",
    "EarthScienceLessons":          "earth_science",
    "EnvironmentalScienceLessons":  "environmental_science",
    "FinancialMathLessons":         "financial_math",
    "GeometryLessons":              "geometry",
    "LinearAlgebraLessons":         "linear_algebra",
    "MarineScienceLessons":         "marine_science",
    "MS_Algebra1Lessons":           "ms_algebra1",
    "MS_Algebra2Lessons":           "ms_algebra2",
    "MS_BiologyLessons":            "ms_biology",
    "MS_ChemistryLessons":          "ms_chemistry",
    "MS_GeometryLessons":           "ms_geometry",
    "MS_PhysicsLessons":            "ms_physics",
    "PhysicsLessons":               "physics",
    "PrecalculusLessons":           "precalculus",
    "StatisticsLessons":            "statistics",
    "TrigonometryLessons":          "trigonometry",
}

# Map CourseHomepage filenames to section slugs
HOMEPAGE_TO_SECTION = {
    "algebra1.html":                "algebra1",
    "algebra2.html":                "algebra2",
    "anatomy.html":                 "anatomy",
    "ap_biology.html":              "ap_biology",
    "ap_calculus.html":             "ap_calculus",
    "ap_chemistry.html":            "ap_chemistry",
    "ap_environmental_science.html":"ap_environmental_science",
    "ap_hug.html":                  "ap_hug",
    "ap_physics1.html":             "ap_physics1",
    "ap_physics2.html":             "ap_physics2",
    "ap_physics_mechanics.html":    "ap_physics_mechanics",
    "ap_statistics.html":           "ap_statistics",
    "astronomy.html":               "astronomy",
    "bio.html":                     "biology",
    "chem.html":                    "chemistry",
    "earth_science.html":           "earth_science",
    "environmental_science.html":   "environmental_science",
    "financial_math.html":          "financial_math",
    "geometry.html":                "geometry",
    "linear_algebra.html":          "linear_algebra",
    "marine_science.html":          "marine_science",
    "ms_algebra1.html":             "ms_algebra1",
    "ms_algebra2.html":             "ms_algebra2",
    "ms_bio.html":                  "ms_biology",
    "ms_chem.html":                 "ms_chemistry",
    "ms_geometry.html":             "ms_geometry",
    "ms_physics.html":              "ms_physics",
    "physics.html":                 "physics",
    "precalculus.html":             "precalculus",
    "statistics.html":              "statistics",
    "trigonometry.html":            "trigonometry",
}


def detect_section(filepath):
    """Determine the section slug based on the file's location."""
    rel = os.path.relpath(filepath, ARIS_DIR).replace("\\", "/")
    parts = rel.split("/")

    # CourseFiles/{CourseLessons}/...
    if parts[0] == "CourseFiles" and len(parts) >= 2:
        folder = parts[1]
        return FOLDER_TO_SECTION.get(folder, "common")

    # CourseHomepage/{course}.html
    if parts[0] == "CourseHomepage" and len(parts) >= 2:
        return HOMEPAGE_TO_SECTION.get(parts[1], "common")

    # Top-level pages (Dashboard, Courses, etc.) or games
    return "common"


def compute_relative_path(html_path, target_dir):
    """Compute relative path from the HTML file to the target directory."""
    html_dir = os.path.dirname(html_path)
    rel = os.path.relpath(target_dir, html_dir).replace("\\", "/")
    return rel


def migrate_file(filepath):
    """Migrate a single HTML file. Returns True if modified."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Check if this file references old translation scripts
    if "global_translations" not in content and \
       "spanish_translations" not in content and \
       "hindi_translations" not in content:
        return False

    # Already migrated?
    if "translation_loader.js" in content:
        return False

    section = detect_section(filepath)
    scripts_dir = os.path.join(ARIS_DIR, "scripts")
    translations_dir = os.path.join(ARIS_DIR, "translations")

    loader_path = compute_relative_path(filepath, scripts_dir) + "/translation_loader.js"
    base_path = compute_relative_path(filepath, translations_dir)

    # Build new script tag
    if section == "common":
        new_tag = f'<script src="{loader_path}" data-base="{base_path}"></script>'
    else:
        new_tag = f'<script src="{loader_path}" data-section="{section}" data-base="{base_path}"></script>'

    # Remove old script tags (various version patterns)
    # Match: <script src="...global_translations.js..."></script>
    patterns_to_remove = [
        r'<script\s+src="[^"]*global_translations\.js[^"]*"\s*>\s*</script>\s*\n?',
        r'<script\s+src="[^"]*spanish_translations\.js[^"]*"\s*>\s*</script>\s*\n?',
        r'<script\s+src="[^"]*hindi_translations\.js[^"]*"\s*>\s*</script>\s*\n?',
    ]

    # Replace the first old script tag with the new loader, remove the rest
    first_replaced = False
    for pat in patterns_to_remove:
        if not first_replaced and re.search(pat, content):
            content = re.sub(pat, new_tag + "\n", content, count=1)
            first_replaced = True
        else:
            content = re.sub(pat, "", content)

    # Remove the manual DOMContentLoaded/applyTranslations boilerplate
    # Pattern: <script> ... applyTranslations ... </script>
    boilerplate_pattern = (
        r'\s*<script>\s*\n?'
        r'\s*//\s*Apply translations when DOM is ready\s*\n?'
        r'\s*document\.addEventListener\([\'"]DOMContentLoaded[\'"],\s*function\(\)\s*\{\s*\n?'
        r'\s*if\s*\(window\.applyTranslations\)\s*\{\s*\n?'
        r'\s*setTimeout\(function\(\)\s*\{\s*\n?'
        r'\s*window\.applyTranslations\(\);\s*\n?'
        r'\s*\},\s*50\);\s*\n?'
        r'\s*\}\s*\n?'
        r'\s*\}\);\s*\n?'
        r'\s*</script>\s*\n?'
    )
    content = re.sub(boilerplate_pattern, "\n", content)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    log_path = os.path.join(REPO_ROOT, "migration_output.txt")
    log = open(log_path, "w", encoding="utf-8")

    def out(msg=""):
        log.write(msg + "\n")
        log.flush()

    out("=" * 60)
    out("ArisEdu Translation Migration")
    out("=" * 60)

    # Find all HTML files
    html_files = glob.glob(os.path.join(ARIS_DIR, "**", "*.html"), recursive=True)
    html_files.sort()

    out(f"\nScanning {len(html_files)} HTML files...\n")

    migrated = 0
    skipped = 0

    for f in html_files:
        rel = os.path.relpath(f, REPO_ROOT).replace("\\", "/")
        if migrate_file(f):
            section = detect_section(f)
            out(f"  MIGRATED  [{section:25s}]  {rel}")
            migrated += 1
        else:
            skipped += 1

    out(f"\n{'=' * 60}")
    out(f"Done! {migrated} files migrated, {skipped} skipped (no old scripts).")
    out(f"{'=' * 60}")
    log.close()
    print(f"Done! See {log_path}")


if __name__ == "__main__":
    main()
