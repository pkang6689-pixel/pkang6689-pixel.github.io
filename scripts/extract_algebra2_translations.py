#!/usr/bin/env python3
import os
import re
import json
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_content = []
        self.in_script = False
        self.in_style = False
    
    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.in_script = True
        elif tag == 'style':
            self.in_style = True
    
    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False
        elif tag == 'style':
            self.in_style = False
    
    def handle_data(self, data):
        if not self.in_script and not self.in_style:
            text = data.strip()
            if text and len(text) > 3:  # Only meaningful text
                self.text_content.append(text)

def extract_text_from_html(file_path):
    """Extract all text from an HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        parser = TextExtractor()
        parser.feed(content)
        return parser.text_content
    except:
        return []

def extract_flashcards(file_path):
    """Extract flashcard content"""
    cards = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r'window\.lessonFlashcards\s*=\s*\[(.*?)\];', content, re.DOTALL)
        if match:
            flashcard_text = match.group(1)
            card_pattern = r'"question":\s*"([^"]*(?:\\"[^"]*)*)",\s*"answer":\s*"([^"]*(?:\\"[^"]*)*)"'
            for m in re.finditer(card_pattern, flashcard_text):
                q = m.group(1).replace('\\"', '"')
                a = m.group(2).replace('\\"', '"')
                cards.append((q, a))
    except:
        pass
    return cards

def extract_quiz_questions(file_path):
    """Extract quiz questions"""
    questions = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all quiz questions
        q_pattern = r'<p[^>]*>(\d+\.\s*[^<]+)</p>'
        for match in re.finditer(q_pattern, content):
            q = match.group(1).strip()
            if q:
                questions.append(q)
    except:
        pass
    return questions

def collect_algebra2_content():
    """Collect all Algebra2 content for translation"""
    base_path = '/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons'
    all_content = {}
    
    for unit_num in range(1, 10):
        unit_dir = os.path.join(base_path, f'Unit{unit_num}')
        if not os.path.exists(unit_dir):
            continue
        
        unit_content = {
            'summaries': [],
            'flashcards': [],
            'quiz_questions': []
        }
        
        # Get all lesson files
        files = [f for f in os.listdir(unit_dir) if f.endswith('.html')]
        
        for fname in files:
            fpath = os.path.join(unit_dir, fname)
            
            if '_Summary.html' in fname:
                texts = extract_text_from_html(fpath)
                unit_content['summaries'].extend(texts)
            
            if '_Practice.html' in fname:
                cards = extract_flashcards(fpath)
                unit_content['flashcards'].extend(cards)
            
            if '_Quiz.html' in fname:
                questions = extract_quiz_questions(fpath)
                unit_content['quiz_questions'].extend(questions)
        
        all_content[f'Unit {unit_num}'] = unit_content
    
    return all_content

# Sample Chinese translations mapping for common Algebra 2 terms
ALGEBRA2_TRANSLATIONS = {
    # Unit 1: Functions
    "Review of Functions & Notation": "函数与记号复习",
    "Functions": "函数",
    "Function Notation": "函数记号",
    "Domain and Range": "定义域与值域",
    "Operations with Functions": "函数的运算",
    "If f(x) = 2x + 3, what is f(5)?": "如果f(x) = 2x + 3，f(5)是多少？",
    "f(5) = 13": "f(5) = 13",
    "What is the domain of f(x) = √(x - 4)?": "f(x) = √(x - 4)的定义域是什么？",
    "x ≥ 4": "x ≥ 4",
    "Composition of functions": "函数复合",
    "(f ∘ g)(x) = f(g(x))": "(f ∘ g)(x) = f(g(x))",
    "Inverse functions": "反函数",
    "One-to-one functions": "一一对应函数",
    
    # Unit 2: Quadratic Functions
    "Quadratic Functions": "二次函数",
    "Graphing Quadratics": "二次函数作图",
    "Vertex Form": "顶点式",
    "Standard Form": "一般式",
    "Factored Form": "因式分解式",
    "Discriminant": "判别式",
    "Real Solutions": "实数解",
    "Complex Solutions": "复数解",
    
    # Unit 3: Polynomial & Rational Functions
    "Polynomial Functions": "多项式函数",
    "Rational Functions": "有理函数",
    "End Behavior": "端行为",
    "Zeros": "零点",
    "Multiplicity": "重数",
    "Asymptotes": "渐近线",
    "Vertical Asymptotes": "竖直渐近线",
    "Horizontal Asymptotes": "水平渐近线",
    
    # Unit 4: Exponential & Logarithmic Functions
    "Exponential Functions": "指数函数",
    "Growth": "增长",
    "Decay": "衰减",
    "Half-life": "半衰期",
    "Logarithmic Functions": "对数函数",
    "Natural Logarithm": "自然对数",
    
    # Unit 5: Sequence & Series
    "Sequences": "数列",
    "Series": "级数",
    "Arithmetic Sequences": "等差数列",
    "Geometric Sequences": "等比数列",
    "Common Difference": "公差",
    "Common Ratio": "公比",
    
    # Unit 6: Trigonometry
    "Trigonometric Functions": "三角函数",
    "Sine": "正弦",
    "Cosine": "余弦",
    "Tangent": "正切",
    "Unit Circle": "单位圆",
    "Radians": "弧度",
    "Degrees": "度",
    
    # Unit 7: Systems
    "Systems of Equations": "方程组",
    "Linear Systems": "线性系统",
    "Nonlinear Systems": "非线性系统",
    "Substitution": "代入法",
    "Elimination": "消元法",
    
    # Unit 8: Matrices
    "Matrices": "矩阵",
    "Matrix Operations": "矩阵运算",
    "Determinant": "行列式",
    "Inverse Matrix": "逆矩阵",
    
    # Unit 9: Conic Sections
    "Conic Sections": "圆锥曲线",
    "Circle": "圆",
    "Parabola": "抛物线",
    "Ellipse": "椭圆",
    "Hyperbola": "双曲线",
}

def generate_translations():
    """Generate translation additions for global_translations.js"""
    content = collect_algebra2_content()
    
    translations_dict = {}
    
    # Add known translations
    for eng, chin in ALGEBRA2_TRANSLATIONS.items():
        translations_dict[eng] = chin
    
    # Collect all unique strings from content
    all_strings = set()
    
    for unit, data in content.items():
        all_strings.update(data['summaries'])
        for q, a in data['flashcards']:
            all_strings.add(q)
            all_strings.add(a)
        all_strings.update(data['quiz_questions'])
    
    # Print coverage
    covered = sum(1 for s in all_strings if s in ALGEBRA2_TRANSLATIONS or s.replace('f(x)', 'f(x)') in ALGEBRA2_TRANSLATIONS)
    print(f"Total unique strings to translate: {len(all_strings)}")
    print(f"Already have translations for: {covered}")
    print(f"Need translations for: {len(all_strings) - covered}")
    
    # Return translations for addition to global file
    return translations_dict, all_strings

if __name__ == '__main__':
    trans_dict, all_strs = generate_translations()
    
    # Output a sample of what needs translation
    print("\nSample strings that need translation:")
    count = 0
    for s in all_strs:
        if s not in trans_dict and count < 20:
            print(f"  '{s}'")
            count += 1
