#!/usr/bin/env python3
"""
Add unit test support to AP course files.
Each unit will have an extra item for the unit test, linking to AP_Unit_Tests folder.
"""

import os
from pathlib import Path
import re

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

def fix_ap_course(file_path: Path, course_name: str) -> bool:
    """Fix a single AP course file to include unit tests"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Store original for comparison
        original_content = content
        
        # 1. Update generateUnitSVG function to include unit test
        # Find and replace the generateUnitSVG function
        old_generate_function = r'''function generateUnitSVG\(unitNum, lessonCount\) \{
    let segments = '';
    const actualLessonCount = lessonCount;
    
    // Calculate height based on total available space \(30 units\) divided by lesson count
    const totalSpace = 30; // Available SVG space from y=3 to y=33
    const rectHeight = \(totalSpace / actualLessonCount\)\.toFixed\(3\);
    
    for \(let lessonNum = 1; lessonNum <= actualLessonCount; lessonNum\+\+\) \{
      // Y position: lessons positioned from bottom \(high lesson #\) to top \(lesson 1\)
      const yPos = \(3 \+ totalSpace - \(lessonNum \* rectHeight\)\)\.toFixed\(3\);
      const folderPath = courseConfig\.folder\.replace\(/\\s\+/g, '%20'\);
      const unitText = `Unit \$\{unitNum\}`\.replace\(/\\s\+/g, '%20'\);
      const lessonText = `Lesson\$\{unitNum\}\.\$\{lessonNum\}_Practice\.html`;
      const topicName = courseConfig\.lessonNames\?\.\[unitNum\]\?\.\[lessonNum\];
      const lessonName = topicName \? `⭐ Lesson \$\{unitNum\}\.\$\{lessonNum\}: \$\{topicName\}` : `Lesson \$\{unitNum\}\.\$\{lessonNum\}`;
      
      const href = `APLessons/\$\{folderPath\}/\$\{unitText\}/\$\{lessonText\}`;
      segments \+= `<g onclick="markLessonStarted\(\$\{unitNum\}, \$\{lessonNum\}\); window\.location\.href='\$\{href\}';" style="cursor: pointer;">
    <rect id="u\$\{unitNum\}-l\$\{lessonNum\}" stroke="none" x="3" y="\$\{yPos\}" width="18" height="\$\{rectHeight\}" fill="white" fill-opacity="0\.25" pointer-events="auto" onmouseenter="showLessonPopup\(event, '\$\{lessonName\}'\)" onmousemove="moveLessonPopup\(event\)" onmouseleave="hideLessonPopup\(\)"></rect></g>
  <line x1="3" y1="\$\{yPos\}" x2="21" y2="\$\{yPos\}" stroke="currentColor" stroke-width="0\.08" stroke-opacity="0\.3" pointer-events="none" />`;
    \}'''

        new_generate_function = '''function generateUnitSVG(unitNum, lessonCount) {
    let segments = '';
    const actualLessonCount = lessonCount + 1; // +1 for unit test
    
    // Calculate height based on total available space (30 units) divided by lesson count
    const totalSpace = 30; // Available SVG space from y=3 to y=33
    const rectHeight = (totalSpace / actualLessonCount).toFixed(3);
    
    // Regular lessons
    for (let lessonNum = 1; lessonNum <= lessonCount; lessonNum++) {
      // Y position: lessons positioned from bottom (high lesson #) to top (lesson 1)
      const yPos = (3 + totalSpace - (lessonNum * rectHeight)).toFixed(3);
      const folderPath = courseConfig.folder.replace(/\\s+/g, '%20');
      const unitText = `Unit ${unitNum}`.replace(/\\s+/g, '%20');
      const lessonText = `Lesson${unitNum}.${lessonNum}_Practice.html`;
      const topicName = courseConfig.lessonNames?.[unitNum]?.[lessonNum];
      const lessonName = topicName ? `⭐ Lesson ${unitNum}.${lessonNum}: ${topicName}` : `Lesson ${unitNum}.${lessonNum}`;
      
      const href = `APLessons/${folderPath}/${unitText}/${lessonText}`;
      segments += `<g onclick="markLessonStarted(${unitNum}, ${lessonNum}); window.location.href='${href}';" style="cursor: pointer;">
    <rect id="u${unitNum}-l${lessonNum}" stroke="none" x="3" y="${yPos}" width="18" height="${rectHeight}" fill="white" fill-opacity="0.25" pointer-events="auto" onmouseenter="showLessonPopup(event, '${lessonName}')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect></g>
  <line x1="3" y1="${yPos}" x2="21" y2="${yPos}" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />`;
    }
    
    // Unit Test
    const testYPos = (3 + totalSpace - ((lessonCount + 1) * rectHeight)).toFixed(3);
    const testHref = `AP_Unit_Tests/${courseConfig.folder}/Unit${unitNum}/unit_tests.html`;
    const testName = `Unit ${unitNum} Test`;
    segments += `<g onclick="markLessonStarted(${unitNum}, 99); window.location.href='${testHref}';" style="cursor: pointer;">
    <rect id="u${unitNum}-l99" stroke="none" x="3" y="${testYPos}" width="18" height="${rectHeight}" fill="white" fill-opacity="0.25" pointer-events="auto" onmouseenter="showLessonPopup(event, '${testName}')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect></g>
  <line x1="3" y1="${testYPos}" x2="21" y2="${testYPos}" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />`;'''

        # Replace the function
        content = re.sub(
            r'function generateUnitSVG\(unitNum, lessonCount\) \{[\s\S]*?return `<div',
            new_generate_function + '\n    \n    return `<div',
            content,
            count=1
        )
        
        # 2. Update applyProgressColors to handle unit tests
        old_progress_function = r'function applyProgressColors\(\) \{[\s\S]*?\}\s*\}'
        
        new_progress_function = '''function applyProgressColors() { 
    for (let u = 1; u <= courseConfig.numUnits; u++) { 
      const maxLessons = courseConfig.units[u] || 0;
      // Apply colors to regular lessons
      for (let l = 1; l <= maxLessons; l++) { 
        const segment = document.getElementById(`u${u}-l${l}`); 
        if (segment) { 
          const isCompleted = localStorage.getItem(`ap_chem_u${u}_l${l}_completed`) === 'true'; 
          const isStarted = localStorage.getItem(`ap_chem_u${u}_l${l}_started`) === 'true'; 
          if (isCompleted) { 
            segment.setAttribute('fill', '#16a34a'); 
            segment.setAttribute('fill-opacity', '0.7'); 
          } else if (isStarted) { 
            segment.setAttribute('fill', '#f97316'); 
            segment.setAttribute('fill-opacity', '0.6'); } 
        } 
      }
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
        
        # A bit tricky - replace just the function body
        content = re.sub(
            r'function applyProgressColors\(\) \{ \n    for \(let u = 1; u <= courseConfig\.numUnits; u\+\+\) \{ \n      const maxLessons = courseConfig\.units\[u\] \|\| 0;[\s\S]*?}\s*]}',
            new_progress_function,
            content
        )
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            # If complex regex didn't work, try a simpler approach
            return fix_ap_course_simple(file_path, lessonCount)
            
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        import traceback
        traceback.print_exc()
        return False

def fix_ap_course_simple(file_path: Path, course_name: str) -> bool:
    """Simpler approach using string replacement"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Make specific replacements
        # 1. Change actualLessonCount calculation
        content = content.replace(
            'const actualLessonCount = lessonCount;',
            'const actualLessonCount = lessonCount + 1; // +1 for unit test'
        )
        
        # 2. Add unit test segment after the loop
        old_loop_end = '''    }
    
    return `<div'''
        
        new_loop_end = '''    }
    
    // Unit Test
    const testYPos = (3 + totalSpace - ((lessonCount + 1) * rectHeight)).toFixed(3);
    const testHref = `AP_Unit_Tests/${courseConfig.folder}/Unit${unitNum}/unit_tests.html`;
    const testName = `Unit ${unitNum} Test`;
    segments += `<g onclick="markLessonStarted(${unitNum}, 99); window.location.href='${testHref}';" style="cursor: pointer;">
    <rect id="u${unitNum}-l99" stroke="none" x="3" y="${testYPos}" width="18" height="${rectHeight}" fill="white" fill-opacity="0.25" pointer-events="auto" onmouseenter="showLessonPopup(event, '${testName}')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect></g>
  <line x1="3" y1="${testYPos}" x2="21" y2="${testYPos}" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />`;
    
    return `<div'''
        
        content = content.replace(old_loop_end, new_loop_end)
        
        # 3. Update applyProgressColors - add unit test handling
        old_apply_colors_end = '''      } 
    } 
  }'''
        
        new_apply_colors_end = '''      }
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
        
        content = content.replace(old_apply_colors_end, new_apply_colors_end)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error in simple fix for {file_path}: {e}")
        return False

def main():
    workspace_root = Path(__file__).parent / "ArisEdu Project Folder"
    
    total = 0
    fixed = 0
    
    for filename, course_name in AP_COURSES:
        file_path = workspace_root / filename
        if file_path.exists():
            total += 1
            print(f"Fixing {course_name}... ", end='')
            if fix_ap_course_simple(file_path, course_name):
                fixed += 1
                print("OK")
            else:
                print("ERROR")
        else:
            print(f"File not found: {file_path}")
    
    print(f"\n{'='*50}")
    print(f"Fixed {fixed}/{total} AP course files")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
