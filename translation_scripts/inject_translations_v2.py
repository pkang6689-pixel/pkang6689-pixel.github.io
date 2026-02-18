import json
import re

translation_file = "../ArisEdu Project Folder/scripts/global_translations.js"

new_translations = {
    # Courses.html
    "Our Courses": "我们的课程",
    "Mathematics": "数学",
    "Science": "科学",
    "High School Algebra 1(WIP)": "高中代数 1 (进行中)",
    "High School Algebra 2(WIP)": "高中代数 2 (进行中)",
    "High School Geometry (WIP)": "高中几何 (进行中)",
    "High School Geometry(WIP)": "高中几何 (进行中)", 
    "High School Biology (WIP)": "高中生物 (进行中)",
    "High School Chemistry": "高中化学",
    "High School Physics": "高中物理",
    
    # Practice Games Logic (practice_games.js)
    "Correct! Great job.": "正确！做得好。",
    "Incorrect. The correct answer was option": "不正确。正确答案是选项",
    "Incorrect. Try again!": "不正确。请重试！",
    "Attempts left:": "剩余尝试次数：",
    
    # Common Game UI
    "Ready to Fly?": "准备好起飞了吗？",
    "Use spacebar or tap to fly": "使用空格键或点击屏幕飞行",
    "Fuel Bar": "燃料条",
    "Start Flying": "开始飞行",
    "Game Over": "游戏结束",
    "Score": "分数",
    "High Score": "最高分",
    "Restart": "重新开始",
    "Shuffle": "洗牌",
    "Previous Lesson": "上一课",
    "Next Lesson": "下一课",
    "Check Answer": "检查答案",
    "Try Again": "重试",
    "Go Back": "返回",
    
    # Climb Game Specifics
    "You ran out of fuel!": "燃料耗尽！",
    "You hit an obstacle!": "你撞到了障碍物！",
    
    # Login / Panel
    "Login": "登录",
    "Sign Up": "注册",
    "Progress": "进度",
    "Community": "社区",
    "Settings": "设置", 
    "Logout": "登出"
}

try:
    with open(translation_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for the object definition: const translations = { ... };
    # We will assume it ends with }; and starts after 'const translations ='
    match = re.search(r'const translations\s*=\s*({[\s\S]*?});', content)
    
    if not match:
        # Fallback to window.globalTranslations = { ... } if format changed
        match = re.search(r'window\.globalTranslations\s*=\s*({[\s\S]*?});', content)
        
    if not match:
        print("Error: Could not find translation object in file")
        exit(1)
        
    json_str = match.group(1)
    
    # Try parsing
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        print("Warning: JSON decode error. Attempting to fix trailing commas.")
        # Remove trailing commas
        json_str_fixed = re.sub(r',\s*}', '}', json_str)
        try:
             data = json.loads(json_str_fixed)
        except:
             print("Fatal: Cannot parse JSON even after fixing trailing commas.")
             exit(1)

    # Update data
    added_count = 0
    for key, value in new_translations.items():
        if key not in data:
            data[key] = value
            added_count += 1
            
    print(f"Added {added_count} new translations.")
    
    # Serialize
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    
    # Replace in content
    # We replace the matched group 1 (the object) with new json
    # Use string replacement on the exact match string to be safe
    new_content = content.replace(match.group(1), new_json_str)
    
    with open(translation_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully updated global_translations.js with new keys.")

except Exception as e:
    print(f"An error occurred: {e}")
    import traceback
    traceback.print_exc()
