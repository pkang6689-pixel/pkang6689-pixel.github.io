"""
Master Content Extraction Script
Extracts all courses: Chemistry, Algebra 1, Algebra 2, Biology, Geometry, Physics, and all AP courses
"""

import subprocess
from pathlib import Path
import sys

# Course definitions with their paths
COURSES = {
    'Chemistry': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\ChemistryLessons',
    'Algebra 1': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\Algebra1Lessons',
    'Algebra 2': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\Algebra2Lessons',
    'Biology': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\BiologyLessons',
    'Geometry': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\GeometryLessons',
    'Physics': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\PhysicsLessons',
    'AP Biology': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\APLessons\AP Biology',
    'AP Calculus AB': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\APLessons\AP Calculus AB',
    'AP Chemistry': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\APLessons\AP Chemistry',
    'AP Environmental Science': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\APLessons\AP Environmental Science',
    'AP Human Geography': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\APLessons\AP Human Geography',
    'AP Physics 2': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\APLessons\AP Physics 2',
    'AP Physics C - Mechanics': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\APLessons\AP Physics C - Mechanics',
    'AP Statistics': r'c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\APLessons\AP Statistics',
}

OUTPUT_DIR = r'c:\Users\Peter\pkang6689-pixel.github.io\content_data'


def extract_course(course_name: str, course_path: str) -> bool:
    """Extract a single course"""
    print(f"\n{'='*60}")
    print(f"Extracting {course_name}...")
    print(f"{'='*60}")
    
    if not Path(course_path).exists():
        print(f"[ERROR] Path not found: {course_path}")
        return False
    
    try:
        result = subprocess.run(
            [sys.executable, 'extract_course_content.py', course_name, course_path, '--output-dir', OUTPUT_DIR],
            cwd=Path(__file__).parent,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"[ERROR] Timeout extracting {course_name}")
        return False
    except Exception as e:
        print(f"[ERROR] Error extracting {course_name}: {e}")
        return False


def main():
    print("\n" + "="*60)
    print("Master Content Extraction - All Courses")
    print("="*60)
    
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    
    results = {}
    for course_name, course_path in COURSES.items():
        results[course_name] = extract_course(course_name, course_path)
    
    # Summary
    print("\n" + "="*60)
    print("EXTRACTION SUMMARY")
    print("="*60)
    
    for course_name, success in results.items():
        status = "[OK]" if success else "[FAIL]"
        print(f"{course_name:20} {status}")
    
    total = len(results)
    successful = sum(1 for v in results.values() if v)
    
    print(f"\nTotal: {successful}/{total} courses extracted successfully")
    print(f"\nOutput directory: {OUTPUT_DIR}")
    
    if successful == total:
        print("\n[OK] All courses extracted successfully!")
        print("\nNext steps:")
        print("1. Review/edit content in content_data/ JSON files")
        print("2. Run: python regenerate_all_html.py")
        print("3. This will regenerate all HTML files with your changes")


if __name__ == "__main__":
    main()
