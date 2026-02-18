import json
import re
import os

translation_file = "../ArisEdu Project Folder/scripts/global_translations.js"

# Taskbar and Course Keys
new_translations = {
    # Taskbar specific full strings (with emojis if needed, though usually regex handles parts)
    "\u2190 Back to Summary": "← 返回总结",
    "\u2190 Back to Lesson": "← 返回课程",
    "\u2190 Back to Practice": "← 返回练习",
    "\u2190 Back to Unit": "← 返回单元",
    "\u2190 Back to Physics": "← 返回物理",
    "\u2190 Back to Course": "← 返回课程",
    "\u2190 Back to Courses": "← 返回课程列表",
    "Search": "搜索", # Already exists likely
    "Homepage": "首页", 
    "Courses": "课程",
    "Settings": "设置",
    "Login/Signup": "登录/注册",
    "Dev: Clear Progress": "开发: 清除进度",
    
    # Course Page Headers
    "High School: Chemistry": "高中：化学",
    "High School: Physics": "高中：物理",
    "High School: Biology": "高中：生物",
    "High School: Algebra 1": "高中：代数 1",
    "High School: Algebra 2": "高中：代数 2",
    "High School: Geometry": "高中：几何",
    
    # Course Map Keys might appear in titles too
    "ChemistryLessons": "化学课程",
    "PhysicsLessons": "物理课程",
    "BiologyLessons": "生物课程",
    "Algebra1Lessons": "代数 1 课程",
    "Algebra2Lessons": "代数 2 课程",
    "GeometryLessons": "几何课程"
}

try:
    with open(translation_file, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'const translations\s*=\s*({[\s\S]*?});', content) or             re.search(r'window\.globalTranslations\s*=\s*({[\s\S]*?});', content)
            
    if not match:
        print("Error: Could not find translation object")
        exit(1)
        
    json_str = match.group(1)
    
    # Loose parse
    try:
        data = json.loads(json_str)
    except:
        json_str_fixed = re.sub(r',\s*}', '}', json_str)
        data = json.loads(json_str_fixed)

    added = 0
    for k, v in new_translations.items():
        if k not in data:
            data[k] = v
            added += 1
            
    print(f"Added {added} new translations.")
    
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1), new_json_str)
    
    with open(translation_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
except Exception as e:
    print(f"Error: {e}")
