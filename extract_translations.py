"""
extract_translations.py
========================
Extracts translations from the monolithic JS files and splits them into
per-language, per-section JSON files.

Output structure:
    ArisEdu Project Folder/translations/{lang}/common.json
    ArisEdu Project Folder/translations/{lang}/{section}.json

Run from the repo root:
    python extract_translations.py
"""

import json
import re
import os

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(REPO_ROOT, "ArisEdu Project Folder", "scripts")
OUT_DIR = os.path.join(REPO_ROOT, "ArisEdu Project Folder", "translations")

# ── Source files ──
SOURCES = {
    "zh": os.path.join(SCRIPTS_DIR, "global_translations.js"),
    "es": os.path.join(SCRIPTS_DIR, "spanish_translations.js"),
    "hi": os.path.join(SCRIPTS_DIR, "hindi_translations.js"),
}

# ── Section detection keywords ──
# Maps a keyword/pattern found in english keys to a section slug.
# Order matters — first match wins.  Longer / more specific patterns first.
SECTION_PATTERNS = [
    # AP courses (must come before generic subjects)
    (r"\bAP\s+Biology\b|ap.bio",                        "ap_biology"),
    (r"\bAP\s+Calcul|ap.calc",                          "ap_calculus"),
    (r"\bAP\s+Chemistry\b|ap.chem",                     "ap_chemistry"),
    (r"\bAP\s+Environmental|ap.env",                     "ap_environmental_science"),
    (r"\bAP\s+Human\s+Geo|ap.hug",                      "ap_hug"),
    (r"\bAP\s+Physics\s+Mechanics|ap.phys.*mech",       "ap_physics_mechanics"),
    (r"\bAP\s+Physics\s*2|ap.phys.*2",                  "ap_physics2"),
    (r"\bAP\s+Physics\s*1|ap.phys.*1",                  "ap_physics1"),
    (r"\bAP\s+Statistics|ap.stat",                       "ap_statistics"),

    # Middle-school
    (r"\bMS.Algebra\s*1|Middle.School.Algebra\s*1",     "ms_algebra1"),
    (r"\bMS.Algebra\s*2|Middle.School.Algebra\s*2",     "ms_algebra2"),
    (r"\bMS.Biology|Middle.School.Bio",                  "ms_biology"),
    (r"\bMS.Chemistry|Middle.School.Chem",               "ms_chemistry"),
    (r"\bMS.Geometry|Middle.School.Geo",                 "ms_geometry"),
    (r"\bMS.Physics|Middle.School.Phys",                 "ms_physics"),

    # High-school courses (generic terms after AP/MS)
    (r"\bAlgebra\s*2\b",                                 "algebra2"),
    (r"\bAlgebra\s*1?\b",                                "algebra1"),
    (r"\bAnatomy\b",                                     "anatomy"),
    (r"\bAstronomy\b",                                   "astronomy"),
    (r"\bBiology\b|Biolog",                              "biology"),
    (r"\bChemistry\b|Chem\b",                            "chemistry"),
    (r"\bEarth\s*Science\b",                             "earth_science"),
    (r"\bEnvironmental\s*Science\b",                     "environmental_science"),
    (r"\bFinancial\s*Math\b",                            "financial_math"),
    (r"\bGeometry\b",                                    "geometry"),
    (r"\bLinear\s*Algebra\b",                            "linear_algebra"),
    (r"\bMarine\s*Science\b",                            "marine_science"),
    (r"\bPhysics\b",                                     "physics"),
    (r"\bPrecalculus\b|Precalc",                         "precalculus"),
    (r"\bStatistics\b",                                  "statistics"),
    (r"\bTrigonometry\b|Trig\b",                         "trigonometry"),
]

# Compile patterns once
_COMPILED = [(re.compile(pat, re.IGNORECASE), slug) for pat, slug in SECTION_PATTERNS]

# ── Course-content JSON mapping ──
# The repo has content_data/ files that list every lesson.  We can use those
# to build a set of english strings that belong to each course.
CONTENT_DATA_DIR = os.path.join(REPO_ROOT, "content_data")
CONTENT_FILE_MAP = {
    "algebra_1_lessons.json":            "algebra1",
    "algebra_2_lessons.json":            "algebra2",
    "anatomy_lessons.json":              "anatomy",
    "astronomy_lessons.json":            "astronomy",
    "biology_lessons.json":              "biology",
    "chemistry_lessons.json":            "chemistry",
    "earth_science_lessons.json":        "earth_science",
    "environmental_science_lessons.json":"environmental_science",
    "financial_math_lessons.json":       "financial_math",
    "geometry_lessons.json":             "geometry",
    "linear_algebra_lessons.json":       "linear_algebra",
    "marine_science_lessons.json":       "marine_science",
    "physics_lessons.json":              "physics",
    "precalculus_lessons.json":          "precalculus",
    "statistics_lessons.json":           "statistics",
    "trigonometry_lessons.json":         "trigonometry",
}


def load_content_strings():
    """Return dict[section] = set of english strings found in content_data JSONs."""
    mapping = {}
    for filename, section in CONTENT_FILE_MAP.items():
        path = os.path.join(CONTENT_DATA_DIR, filename)
        if not os.path.exists(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            strings = set()
            _collect_strings(data, strings)
            mapping[section] = strings
        except Exception as e:
            print(f"  Warning: could not parse {filename}: {e}")
    return mapping


def _collect_strings(obj, out):
    """Recursively collect all string values from a JSON structure."""
    if isinstance(obj, str):
        s = obj.strip()
        if s:
            out.add(s)
    elif isinstance(obj, dict):
        for v in obj.values():
            _collect_strings(v, out)
    elif isinstance(obj, list):
        for item in obj:
            _collect_strings(item, out)


def extract_dict_from_js(path):
    """
    Parse a JS file that contains a big object literal { "key": "value", ... }
    and return it as a Python dict.
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Find the first { ... } block that looks like our dictionary.
    # Strategy: find opening brace of the translations object, then match pairs.
    # The JS files have a known pattern:  var xxx = { ... };
    # We'll regex-extract all "key": "value" pairs instead of trying to parse JS.
    pairs = {}
    # Match: "english text": "translated text"
    # Also handles escaped quotes within strings.
    pattern = re.compile(
        r'"((?:[^"\\]|\\.)*)"\s*:\s*"((?:[^"\\]|\\.)*)"',
        re.DOTALL
    )
    for m in pattern.finditer(text):
        key = m.group(1).replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')
        val = m.group(2).replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')
        if key and val:
            pairs[key] = val

    return pairs


def classify_key(english_key, content_strings):
    """
    Given an english key, return the section slug it belongs to,
    or 'common' for UI/nav/shared strings.
    """
    # 1. Check content_data sets first (most reliable)
    for section, strings in content_strings.items():
        if english_key in strings:
            return section

    # 2. Check "Back to ..." patterns
    back_match = re.match(r"^Back to (.+)$", english_key, re.IGNORECASE)
    if back_match:
        target = back_match.group(1).strip()
        for pattern, slug in _COMPILED:
            if pattern.search(target):
                return slug

    # 3. Keyword-based matching
    for pattern, slug in _COMPILED:
        if pattern.search(english_key):
            # Only classify if key is long enough to be course content
            # Short keys like "Biology" are likely common nav strings
            if len(english_key) > 40:
                return slug

    # 4. Default to common
    return "common"


def main():
    print("=" * 60)
    print("ArisEdu Translation Extractor")
    print("=" * 60)

    # Load content data for classification
    print("\nLoading content_data for classification...")
    content_strings = load_content_strings()
    for sec, strings in sorted(content_strings.items()):
        print(f"  {sec}: {len(strings)} reference strings")

    # Process each language
    for lang_code, js_path in SOURCES.items():
        print(f"\n{'─' * 40}")
        print(f"Processing: {lang_code} ({os.path.basename(js_path)})")
        print(f"{'─' * 40}")

        if not os.path.exists(js_path):
            print(f"  SKIP: file not found")
            continue

        pairs = extract_dict_from_js(js_path)
        print(f"  Extracted {len(pairs)} key-value pairs")

        # Classify into sections
        buckets = {}  # section -> {key: value}
        for en_key, translated in pairs.items():
            section = classify_key(en_key, content_strings)
            if section not in buckets:
                buckets[section] = {}
            buckets[section][en_key] = translated

        # Write JSON files
        lang_dir = os.path.join(OUT_DIR, lang_code)
        os.makedirs(lang_dir, exist_ok=True)

        for section, data in sorted(buckets.items()):
            out_path = os.path.join(lang_dir, f"{section}.json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  {section}.json: {len(data)} strings")

    print(f"\n{'=' * 60}")
    print("Done! Files written to:")
    print(f"  {OUT_DIR}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
