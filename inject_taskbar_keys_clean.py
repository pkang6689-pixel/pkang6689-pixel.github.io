import json
import re

translation_file = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"

# Taskbar Emoji Keys (Clean Unicode)
new_translations = {
    "🔍 Search": "🔍 搜索",
    "🏠 Homepage": "🏠 首页", 
    "📚 Courses": "📚 课程",
    "📝 Courses": "📝 课程", # Variant check
    "⚙️ Settings": "⚙️ 设置",
    "⚙️ Preferences": "⚙️ 偏好设置",
    "🔐 Login/Signup": "🔐 登录/注册",
    "👤": "👤", # Check loginname prefix
    
    # Headers
    "High School: Chemistry": "高中：化学",
    "High School: Physics": "高中：物理",
    "High School: Biology": "高中：生物",
    "High School: Algebra 1": "高中：代数 1",
    "High School: Algebra 2": "高中：代数 2",
    "High School: Geometry": "高中：几何",
    
    # Taskbar back buttons with arrow
    "← Back to Summary": "← 返回总结",
    "← Back to Lesson": "← 返回课程",
    "← Back to Practice": "← 返回练习",
    "← Back to Unit": "← 返回单元",
    "← Back to Physics": "← 返回物理",
    "← Back to Course": "← 返回课程",
    "← Back to Courses": "← 返回课程列表"
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
            print(f"Adding key: {k}")
            
    print(f"Added {added} new translations.")
    
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1), new_json_str)
    
    with open(translation_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
except Exception as e:
    print(f"Error: {e}")
