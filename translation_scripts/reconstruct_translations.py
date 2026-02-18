
import json
import os
import re

# Manual list of UI Strings typically found in your translations
initial_ui_translations = {
  "Settings": "设置",
  "Appearance": "外观",
  "Account": "账户",
  "Notifications": "通知",
  "Search": "搜索",
  "Homepage": "首页",
  "Courses": "课程",
  "Play": "玩",
  "Preferences": "偏好设置",
  "Dark Mode": "深色模式",
  "Enable Dark Mode": "启用深色模式",
  "Language:": "语言:",
  "Color Theme:": "主题颜色:",
  "Email:": "邮箱:",
  "Password:": "密码:",
  "Notification Settings": "通知设置",
  "Email Notifications": "邮件通知",
  "Push Notifications": "推送通知",
  "Lesson": "课",
  "Summary": "总结",
  "Game": "游戏",
  "Unit": "单元",
  "Login/Signup": "登录/注册",
  "Account Settings": "账户设置",
  "Appearance Settings": "外观设置",
  "Email": "邮箱",
  "Password": "密码",
  "Push": "推送",
  "Math & Science": "数学与科学",
  "About Our Platform": "关于我们的平台",
  "ArisEdu is a website dedicated to providing its users with free educational resources in stem subjects.": "ArisEdu 是一个致力于为用户提供免费 STEM 学科教育资源的网站。",
  "ArisEdu aims to assist all students in learning, regardless of their background or skill level.": "ArisEdu 旨在帮助所有学生学习，无论他们的背景或技能水平如何。",
  "Please note that ArisEdu is a project still in development, and we plan on expanding development with more courses and features.": "请注意，ArisEdu 仍处于开发阶段，我们计划通过更多课程和功能扩展开发。",
  "Mathematics": "数学",
  "We offer most high school level math courses that use interactive tools and visual aids to enhance learning intuitively.": "我们提供大多数高中水平的数学课程，使用交互式工具和视觉辅助工具来直观地增强学习。",
  "Algebra 1 & 2": "代数 1 & 2",
  "Geometry & Trigonometry": "几何与三角学",
  "Science": "科学",
  "We offer high school level science courses, with interactive diagrams, practice questions, and even fun games to elevate the scientific learning process, aimed at making science a enjoyable and engaging subject for all students.": "我们提供高中水平的科学课程，包含交互式图表、练习题，甚至有趣的游戏，以提升科学学习过程，旨在让科学成为所有学生愉快和引人入胜的学科。",
  "Physics & Mechanics": "物理与力学",
  "Chemistry & Molecular Science": "化学与分子科学",
  "Biology": "生物学",
  "Welcome Back": "欢迎回来",
  "We're glad to see you again": "很高兴再次见到您",
  "Continue Learning": "继续学习",
  "Continue to Courses": "继续课程",
  "Dismiss": "关闭",
  "Logout": "登出",
  "Log out": "登出",
  "Chemistry": "化学",
  "Physics": "物理",
  "Algebra": "代数",
  "Geometry": "几何",
  "Trigonometry": "三角学",
  "Next Lesson": "下一课",
  "Previous Lesson": "上一课",
  "Start Quiz": "开始测验",
  "Submit": "提交",
  "Retry": "重试",
  "Explanation": "解释",
  "Correct!": "正确！",
  "Incorrect.": "错误。",
  "Login": "登录",
  "Signup": "注册",
  "Sign Up": "注册",
  "Sign In": "登录",
  "Forgot Password?": "忘记密码？",
  "Don't have an account?": "没有账户？",
  "Already have an account?": "已有账户？",
  "Create Account": "创建账户",
  "Physics Course": "物理课程",
  "Chemistry Course": "化学课程",
  "Biology Course": "生物课程",
  "Algebra 1": "代数 1",
  "Algebra 2": "代数 2",
  "Unit 1 Test": "第一单元测试",
  "Unit 2 Test": "第二单元测试",
  "Unit 3 Test": "第三单元测试",
  "Unit 4 Test": "第四单元测试",
  "Unit 5 Test": "第五单元测试",
  "Unit 6 Test": "第六单元测试",
  "Unit 7 Test": "第七单元测试",
  "Unit 8 Test": "第八单元测试",
  "Unit 9 Test": "第九单元测试",
  "Unit 10 Test": "第十单元测试",
  "Unit 11 Test": "第十一单元测试",
  "Unit 12 Test": "第十二单元测试",
  "Practice": "练习",
  "Topic": "主题",
  "Description": "描述",
  "Video": "视频",
  "Quiz": "测验",
  "High School Physics": "高中物理",
  "High School Chemistry": "高中化学",
  "Our Courses": "我们的课程"
}

def extract_from_file(filepath, pattern_start="translations = {"):
    found = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # simple dirty extraction if pattern matches
            # Look for variable assignment
            match = re.search(r'(\w+)\s*=\s*{', content)
            if match:
                # We found a dictionary start. Let's try to parse the content more robustly or just use regex for "k": "v"
                # Regex for "key": "value"
                pairs = re.findall(r'"([^"]+)"\s*:\s*"([^"]+)"', content)
                for k, v in pairs:
                    found[k] = v
    except Exception as e:
        print(f"Skipping {filepath}: {e}")
    return found

def main():
    merged = initial_ui_translations.copy()
    
    # 1. Recover from generate_translations.py (Flashcards?)
    gen_trans = extract_from_file('generate_translations.py')
    if gen_trans:
        print(f"Recovered {len(gen_trans)} terms from generate_translations.py")
        merged.update(gen_trans)

    # 2. Recover from generate_summary_translations.py (Summaries)
    sum_trans = extract_from_file('generate_summary_translations.py')
    if sum_trans:
        print(f"Recovered {len(sum_trans)} terms from generate_summary_translations.py")
        merged.update(sum_trans)
        
    # 3. Recover from inject_translations.py (Topics)
    inj_trans = extract_from_file('inject_translations_chemistry.py')
    if inj_trans:
        print(f"Recovered {len(inj_trans)} terms from inject_translations.py")
        merged.update(inj_trans)

    # 4. Generate JavaScript Content with Safe JSON injection
    js_content = """/* Global Translations for ArisEdu */
(function() {
    const translations = %JSON_CONTENT%;

    function translateNode(node) {
        if (node.nodeType === 3) { // Text node
             var originalText = node.nodeValue;
             if (!originalText || !originalText.trim()) return;

             // Exact match (fastest path)
             var trimmed = originalText.trim();
             if (translations[trimmed] && translations[trimmed] !== trimmed) {
                 var newVal = originalText.replace(trimmed, translations[trimmed]);
                 if (newVal !== originalText) node.nodeValue = newVal;
                 return;
             }

             // Check if text contains any ASCII letters — skip if it's all non-Latin
             if (!/[A-Za-z]/.test(originalText)) return;

             // Sorted-key replacement setup
             // We do this lazily or once? Usually once is better for perf, but here 
             // we accept dynamic. Actually let's just do partial string logical replacements if needed.
             // For now, let's stick to exact matches or simple phrases to avoid breaking DOM text.
             
             // If we really want partial replacement:
             // (Logic omitted for simplicity unless user requested advanced matching)
        } else if (node.nodeType === 1) { // Element node
            var tag = node.tagName.toLowerCase();
            if (tag === 'script' || tag === 'style' || tag === 'textarea' || tag === 'input') return;

            // Translate attributes
            if (node.hasAttribute('placeholder')) {
                let ph = node.getAttribute('placeholder');
                if (translations[ph]) {
                    node.setAttribute('placeholder', translations[ph]);
                }
            }
            if (node.hasAttribute('title')) {
                 let t = node.getAttribute('title');
                 if (translations[t]) {
                     node.setAttribute('title', translations[t]);
                 }
            }

            node.childNodes.forEach(translateNode);
        }
    }

    window.applyTranslations = function() {
        if (localStorage.getItem("arisEduLanguage") === "chinese") {
            isTranslating = true;
            try {
                translateNode(document.body);
            } finally {
                isTranslating = false;
            }
            document.documentElement.lang = 'zh';
        }
    };

    // Auto-run
    if (document.readyState === 'loading') {
        window.addEventListener("DOMContentLoaded", window.applyTranslations);
    } else {
        window.applyTranslations();
    }

    // Observer 
    var isTranslating = false;
    var observer = new MutationObserver(function(mutations) {
        if (isTranslating) return;
        if (localStorage.getItem("arisEduLanguage") !== "chinese") return;

        isTranslating = true;
        try {
            mutations.forEach(function(mutation) {
                mutation.addedNodes.forEach(function(node) {
                    translateNode(node);
                });
                if (mutation.type === 'characterData' && mutation.target.nodeValue && 
                    /[A-Za-z]/.test(mutation.target.nodeValue)) {
                    translateNode(mutation.target);
                }
            });
        } finally {
            isTranslating = false;
        }
    });

    window.addEventListener('load', function() {
        if (document.body) {
            observer.observe(document.body, { childList: true, subtree: true, characterData: true });
        }
    });

})();
"""
    
    json_str = json.dumps(merged, ensure_ascii=False, indent=2)
    final_js = js_content.replace('%JSON_CONTENT%', json_str)
    
    output_path = '../ArisEdu Project Folder/scripts/global_translations.js'
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_js)
    
    print(f"Successfully reconstructed global_translations.js at {output_path} with {len(merged)} entries.")

if __name__ == "__main__":
    main()
