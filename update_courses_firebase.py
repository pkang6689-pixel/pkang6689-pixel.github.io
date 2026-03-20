#!/usr/bin/env python3
"""
Update all course homepage files to import Firebase auth
"""
import os
from pathlib import Path

course_folder = Path(r"C:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\CourseHomepage")

# List of course files
courses = [
    "algebra2.html", "anatomy.html", "ap_biology.html", "ap_calculus.html",
    "ap_chemistry.html", "ap_environmental_science.html", "ap_hug.html",
    "ap_physics1.html", "ap_physics2.html", "ap_physics_mechanics.html",
    "ap_statistics.html", "astronomy.html", "bio.html", "chem.html",
    "earth_science.html", "environmental_science.html", "financial_math.html",
    "geometry.html", "integrated_science.html", "linear_algebra.html",
    "marine_science.html", "ms_algebra1.html", "ms_algebra2.html",
    "ms_bio.html", "ms_chem.html", "ms_geometry.html", "ms_physics.html",
    "physics.html", "precalculus.html", "statistics.html", "trigonometry.html"
]

firebase_import = '''  <script type="module">
    // Import Firebase config and make auth available to analytics
    import { auth } from '../firebase-config.js';
    window.auth = auth;
  </script>
<script src="../scripts/analytics-helper.js"></script>'''

for course in courses:
    file_path = course_folder / course
    if not file_path.exists():
        print(f"❌ {course} - NOT FOUND")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has the import
    if 'import { auth } from' in content:
        print(f"✅ {course} - Already has Firebase import")
        continue
    
    # Find and replace
    if '<script src="../scripts/analytics-helper.js"></script>' not in content:
        print(f"⚠️  {course} - No analytics-helper script tag found")
        continue
    
    # Replace the old analytics-helper tag with our new import + tag
    old_pattern = '<script src="../scripts/analytics-helper.js"></script>'
    new_content = content.replace(old_pattern, firebase_import)
    
    if new_content == content:
        print(f"❌ {course} - Replacement failed")
        continue
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ {course} - Updated successfully")

print("\n✅ All course homepages updated!")
