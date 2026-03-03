#!/usr/bin/env python3
"""
Fix AP course files to properly add unit test support in lesson selectors.
"""

import os
from pathlib import Path

AP_COURSES = [
    ("ap_biology.html", "AP Biology"),
    ("ap_calculus.html", "AP Calculus AB"),
    ("ap_chemistry.html", "AP Chemistry"),
    ("ap_environmental_science.html", "AP Environmental Science"),
    ("ap_hug.html", "AP Human Geography"),
    ("ap_physics1.html", "AP Physics 1"),
    ("ap_physics2.html", "AP Physics 2"),
    ("ap_physics_mechanics.html", "AP Physics C - Mechanics"),
    ("ap_statistics.html", "AP Statistics"),
]

def fix_ap_course_correct(file_path: Path, course_name: str) -> bool:
    """Fix AP course file with correct unit test logic"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Step 1: Fix the loop condition to only iterate through regular lessons
        old_loop = '''    for (let lessonNum = 1; lessonNum <= actualLessonCount; lessonNum++) {'''
        new_loop = '''    for (let lessonNum = 1; lessonNum <= lessonCount; lessonNum++) {'''
        content = content.replace(old_loop, new_loop)
        
        # Step 2: Ensure actualLessonCount is used for height calculation
        # (it should already be there from previous run, but check)
        if 'const actualLessonCount = lessonCount + 1' not in content:
            old_line = 'const actualLessonCount = lessonCount;'
            new_line = 'const actualLessonCount = lessonCount + 1; // +1 for unit test'
            content = content.replace(old_line, new_line)
        
        # Step 3: Ensure unit test code exists
        if 'const testYPos = (3 + totalSpace - ((lessonCount + 1)' not in content:
            # Unit test code doesn't exist, add it
            old_return = '''    }
    
    return `<div'''
            new_return = '''    }
    
    // Unit Test
    const testYPos = (3 + totalSpace - ((lessonCount + 1) * rectHeight)).toFixed(3);
    const testHref = `AP_Unit_Tests/${courseConfig.folder}/Unit${unitNum}/unit_tests.html`;
    const testName = `Unit ${unitNum} Test`;
    segments += `<g onclick="markLessonStarted(${unitNum}, 99); window.location.href='${testHref}';" style="cursor: pointer;">
    <rect id="u${unitNum}-l99" stroke="none" x="3" y="${testYPos}" width="18" height="${rectHeight}" fill="white" fill-opacity="0.25" pointer-events="auto" onmouseenter="showLessonPopup(event, '${testName}')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect></g>
  <line x1="3" y1="${testYPos}" x2="21" y2="${testYPos}" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />`;
    
    return `<div'''
            content = content.replace(old_return, new_return)
        
        # Step 4: Fix progress color function if needed
        if 'const testSegment = document.getElementById' not in content:
            old_progress_end = '''      } 
    } 
  }'''
            new_progress_end = '''      }
      // Apply colors to unit test
      const testSegment = document.getElementById(`u${u}-l99`);
      if (testSegment) {
        const isTestCompleted = localStorage.getItem(`ap_chem_u${u}_l99_completed`) === 'true';
        const isTestStarted = localStorage.getItem(`ap_chem_u${u}_l99_started`) === 'true';
        if (isTestCompleted) {
          testSegment.setAttribute('fill', '#16a34a');
          testSegment.setAttribute('fill-opacity', '0.7');
        } else if (isTestStarted) {
          testSegment.setAttribute('fill', '#f97316');
          testSegment.setAttribute('fill-opacity', '0.6');
        }
      }
    } 
  }'''
            content = content.replace(old_progress_end, new_progress_end)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    workspace_root = Path(__file__).parent / "ArisEdu Project Folder"
    
    total = 0
    fixed = 0
    
    for filename, course_name in AP_COURSES:
        file_path = workspace_root / filename
        if file_path.exists():
            total += 1
            print(f"Correcting {course_name}... ", end='', flush=True)
            if fix_ap_course_correct(file_path, course_name):
                fixed += 1
                print("OK")
            else:
                print("ERROR")
        else:
            print(f"File not found: {file_path}")
    
    print(f"\n{'='*50}")
    print(f"Corrected {fixed}/{total} AP course files")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
