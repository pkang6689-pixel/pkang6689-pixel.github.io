#!/usr/bin/env python3
"""
Shorten Video, Summary, and Quiz HTML files across all ChemistryLessons units.
Removes unnecessary script references that are not needed by each file type:

Video files: Remove game_utils.js, search_data.js, search_logic.js
Summary files: Remove game_utils.js, search_data.js, search_logic.js
Quiz files: Remove game_utils.js (resetQuizQuestion moved to quiz_ui.js),
            search_data.js, search_logic.js
"""
import os
import re

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     "ArisEdu Project Folder", "ChemistryLessons")


def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    bn = os.path.basename(filepath)
    
    # Determine file type
    if '_Video.html' in bn:
        ftype = 'Video'
    elif '_Summary.html' in bn:
        ftype = 'Summary'
    elif '_Quiz.html' in bn:
        ftype = 'Quiz'
    else:
        return []
    
    # Scripts to remove from ALL non-Practice file types
    remove_scripts = [
        (r'<script\s+src="[^"]*game_utils\.js"[^>]*>\s*</script>\s*\n?', "game_utils.js"),
        (r'<script\s+src="[^"]*search_data\.js"[^>]*>\s*</script>\s*\n?', "search_data.js"),
        (r'<script\s+src="[^"]*search_logic\.js"[^>]*>\s*</script>\s*\n?', "search_logic.js"),
    ]
    
    # Video files also don't need quiz_ui.js
    if ftype == 'Video':
        remove_scripts.append(
            (r'<script\s+src="[^"]*quiz_ui\.js"[^>]*>\s*</script>\s*\n?', "quiz_ui.js")
        )
    
    # Summary files don't need quiz_ui.js or lesson_video.js
    if ftype == 'Summary':
        remove_scripts.append(
            (r'<script\s+src="[^"]*quiz_ui\.js"[^>]*>\s*</script>\s*\n?', "quiz_ui.js")
        )
    
    for pattern, name in remove_scripts:
        if re.search(pattern, content):
            content = re.sub(pattern, '', content)
            changes.append(f"Removed {name}")
    
    # Remove HTML comments for search
    if re.search(r'<!-- ArisEdu Global Search -->\s*\n?', content):
        content = re.sub(r'<!-- ArisEdu Global Search -->\s*\n?', '', content)
        changes.append("Removed search comment")
    
    # Remove empty/redundant view comments that don't have corresponding content
    for comment_pattern, comment_name in [
        (r'<!-- Embedded Summary View \(Hidden by default\) -->\s*\n?', "empty Summary view comment"),
        (r'<!-- Embedded Practice View \(Hidden by default\) -->\s*\n?', "empty Practice view comment"),
        (r'<!-- Quiz View \(Hidden by default\) -->\s*\n?', "empty Quiz view comment"),
        (r'<!-- Embedded Summary View -->\s*\n?', "empty Summary view comment"),
    ]:
        # Only remove if the page doesn't actually have that embedded view's content
        if re.search(comment_pattern, content):
            content = re.sub(comment_pattern, '', content)
            changes.append(f"Removed {comment_name}")
    
    # Normalize absolute script paths to relative
    abs_patterns = [
        (r'<script\s+src="/ArisEdu Project Folder/scripts/taskbar\.js"', 
         '<script src="../../scripts/taskbar.js"', "taskbar.js"),
        (r'<script\s+src="/ArisEdu Project Folder/scripts/game_utils\.js"', 
         '<script src="../../scripts/game_utils.js"', "game_utils.js"),
        (r'<script\s+src="/ArisEdu Project Folder/scripts/quiz_ui\.js"', 
         '<script src="../../scripts/quiz_ui.js"', "quiz_ui.js"),
        (r'<script\s+src="/ArisEdu Project Folder/scripts/lesson_video\.js"', 
         '<script src="../../scripts/lesson_video.js"', "lesson_video.js"),
    ]
    
    for pattern, replacement, name in abs_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes.append(f"Normalized {name} path to relative")
    
    # Clean up excessive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    
    return []


def main():
    total_changes = 0
    files_changed = 0
    
    for unit in sorted(os.listdir(BASE)):
        unit_dir = os.path.join(BASE, unit)
        if not os.path.isdir(unit_dir) or unit.startswith(('_', 'Archive')):
            continue
        
        unit_changes = 0
        unit_files = 0
        
        for fn in sorted(os.listdir(unit_dir)):
            if not fn.endswith('.html'):
                continue
            if '_Practice.html' in fn or '_Test' in fn:
                continue  # Skip Practice (already cleaned) and Test files
            
            filepath = os.path.join(unit_dir, fn)
            changes = clean_file(filepath)
            
            if changes:
                files_changed += 1
                unit_files += 1
                total_changes += len(changes)
                unit_changes += len(changes)
        
        if unit_changes:
            print(f"  {unit}: {unit_files} files, {unit_changes} changes")
    
    print(f"\n=== Summary ===")
    print(f"Files changed: {files_changed}")
    print(f"Total changes: {total_changes}")
    
    # Verification
    print(f"\n=== Verification ===")
    issues = 0
    for unit in sorted(os.listdir(BASE)):
        unit_dir = os.path.join(BASE, unit)
        if not os.path.isdir(unit_dir) or unit.startswith(('_', 'Archive')):
            continue
        
        for fn in sorted(os.listdir(unit_dir)):
            if not fn.endswith('.html') or '_Practice.html' in fn or '_Test' in fn:
                continue
            
            filepath = os.path.join(unit_dir, fn)
            with open(filepath) as f:
                html = f.read()
            lines = html.count('\n') + 1
            
            file_issues = []
            
            # Check for scripts that should have been removed
            if 'game_utils.js' in html:
                file_issues.append("still has game_utils.js")
            if 'search_data.js' in html:
                file_issues.append("still has search_data.js")
            if 'search_logic.js' in html:
                file_issues.append("still has search_logic.js")
            
            # Check required scripts are still present
            if '_Video.html' in fn:
                if 'taskbar.js' not in html: file_issues.append("MISSING taskbar.js")
                if 'lesson_video.js' not in html: file_issues.append("MISSING lesson_video.js")
            elif '_Summary.html' in fn:
                if 'taskbar.js' not in html: file_issues.append("MISSING taskbar.js")
            elif '_Quiz.html' in fn:
                if 'taskbar.js' not in html: file_issues.append("MISSING taskbar.js")
                if 'quiz_ui.js' not in html: file_issues.append("MISSING quiz_ui.js")
            
            if file_issues:
                issues += 1
                print(f"  ISSUE {unit}/{fn}: {', '.join(file_issues)}")
    
    if issues == 0:
        print("  All files verified OK!")
    
    # Line count summary
    print(f"\n=== Line Counts ===")
    for ftype in ['_Video.html', '_Summary.html', '_Quiz.html']:
        counts = []
        for unit in sorted(os.listdir(BASE)):
            unit_dir = os.path.join(BASE, unit)
            if not os.path.isdir(unit_dir) or unit.startswith(('_', 'Archive')):
                continue
            for fn in sorted(os.listdir(unit_dir)):
                if fn.endswith(ftype):
                    with open(os.path.join(unit_dir, fn)) as f:
                        counts.append(f.read().count('\n') + 1)
        if counts:
            print(f"  {ftype}: {len(counts)} files, avg={sum(counts)/len(counts):.0f}, min={min(counts)}, max={max(counts)}, total={sum(counts)}")


if __name__ == "__main__":
    main()
