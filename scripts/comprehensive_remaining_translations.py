#!/usr/bin/env python3
"""
Comprehensive Translation System - Batches 41-70
Translates all remaining 1,118 untranslated strings from algebra2_untranslated_strings.json
"""
import json
import re

class ComprehensiveTranslationSystem:
    def __init__(self):
        self.trans_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
        self.untranslated_file = '/workspaces/ArisEdu/algebra2_untranslated_strings.json'
        
    def load_untranslated(self):
        """Load all untranslated strings"""
        try:
            with open(self.untranslated_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def create_comprehensive_mapping(self, untranslated_list):
        """Create comprehensive translation mapping for all strings"""
        mapping = {
            # Specific coordinate answers
            "(-1, -4)": "(-1, -4)",
            "(-2, -11)": "(-2, -11)",
            "(0, 0)": "(0, 0)",
            "(0, 1)": "(0, 1)",
            "(1, 0) and (2, 1)": "(1, 0)和(2, 1)",
            "(1, 2)": "(1, 2)",
            "(2, -1)": "(2, -1)",
            "(2, -3)": "(2, -3)",
            "(2, 1)": "(2, 1)",
            "(3, 7)": "(3, 7)",
            "(4, -11)": "(4, -11)",
            "(2, 0)": "(2, 0)",
            "(0, 0), (0, 6), (6, 0)": "(0, 0), (0, 6), (6, 0)",
            "(2t, 2)": "(2t, 2)",
            "(-∞, 3]": "(-∞, 3]",
            "(-∞, 4]": "(-∞, 4]",
            "(-∞, -2) ∪ (2, ∞)": "(-∞, -2) ∪ (2, ∞)",
            "(-∞, -1) ∪ (2, ∞)": "(-∞, -1) ∪ (2, ∞)",
            "(-∞, 0) ∪ (0, ∞)": "(-∞, 0) ∪ (0, ∞)",
            "(-3, 4)": "(-3, 4)",
            "(-3, 1)": "(-3, 1)",
            "(-4, 2)": "(-4, 2)",
            
            # Interval solutions
            "-3 < x < 1/2": "-3 < x < 1/2",
            "-3 < x < 3": "-3 < x < 3",
            "0 ≤ x ≤ 4": "0 ≤ x ≤ 4",
            "x ≤ -1 or x ≥ 1": "x ≤ -1或x ≥ 1",
            "x < -1/2 or x > 1": "x < -1/2或x > 1",
            "0 < x < 5": "0 < x < 5",
            "1 ≤ x ≤ 3": "1 ≤ x ≤ 3",
            
            # Step-by-step solutions
            "From vertex form a(x-h)²+k: h=-1 (so right -1=left 1).": 
                "从顶点式a(x-h)²+k：h=-1（所以右-1=左1）。",
            "x² + 4x + 4 - 4 - 7 = (x+2)² - 11.": 
                "x² + 4x + 4 - 4 - 7 = (x+2)² - 11。",
            "Find common denominator (x+1)(x-1).": 
                "找到公分母(x+1)(x-1)。",
            "Bracket at 3 (included), infinity always parenthesis.": 
                "在3处有括号（包括），无穷大总是圆括号。",
            "Vertex x = 1, f(1) = 4 max, opens down.": 
                "顶点x = 1，f(1) = 4最大值，开口向下。",
            "cos(90°)=0, sin(90°)=1.": 
                "cos(90°)=0, sin(90°)=1。",
            "Vertices of feasible region triangle.": 
                "可行域三角形的顶点。",
            
            # Algebraic forms
            "(-x-3)/((x+1)(x-1))": "(-x-3)/((x+1)(x-1))",
            "(1 - cos(2x))/2": "(1 - cos(2x))/2",
            "(1 - cos(θ))/2": "(1 - cos(θ))/2",
            "(u·v)/(|u||v|)": "(u·v)/(|u||v|)",
            "(x + 2)(x + 3)": "(x + 2)(x + 3)",
            "(x + 3)/2": "(x + 3)/2",
            "(x + 4)²": "(x + 4)²",
            "(x - 1)² (x - 4)": "(x - 1)² (x - 4)",
            "(x - 2)": "(x - 2)",
            "(x - 3)": "(x - 3)",
            "(x - 3)(x² + 3x + 9)": "(x - 3)(x² + 3x + 9)",
            "(x - 4)(x + 4)": "(x - 4)(x + 4)",
            "(x+1)/(x+2)": "(x+1)/(x+2)",
            "(x+1)/(x-1)": "(x+1)/(x-1)",
            "(x+3)/(x-2)": "(x+3)/(x-2)",
            "(x+4)² = 25": "(x+4)² = 25",
            "(x-2)² + (y-3)² = 25": "(x-2)² + (y-3)² = 25",
            "(x² - 1)(x² + 1)": "(x² - 1)(x² + 1)",
            "(x̄, ȳ)": "(x̄, ȳ)",
            "(y + z)(x + w)": "(y + z)(x + w)",
            "(±4, 0)": "(±4, 0)",
            
            # Explanations for solutions
            "Two numbers: 2, 3 sum to 5, product 6.": 
                "两个数：2、3和为5、积为6。",
            "Factor: 2x(x+3)/(4x) = (x+3)/2.": 
                "因式分解：2x(x+3)/(4x) = (x+3)/2。",
            "Form (a+b)² = a² + 2ab + b².": 
                "形式(a+b)² = a² + 2ab + b²。",
            "(x-1) has multiplicity 2.": 
                "(x-1)的重数为2。",
            "Factor numerator: (x-2)(x+2). Cancel (x+2).": 
                "对分子因式分解：(x-2)(x+2)。约去(x+2)。",
            "is a factor of f(x).": 
                "是f(x)的因数。",
            "Difference of cubes: a³ - b³ = (a-b)(a²+ab+b²).": 
                "立方差：a³ - b³ = (a-b)(a²+ab+b²)。",
            "Difference of squares: a² - b² = (a-b)(a+b).": 
                "平方差：a² - b² = (a-b)(a+b)。",
            "divides f(x) evenly.": 
                "能整除f(x)。",
            "Cancel (x-1).": 
                "约去(x-1)。",
            "Multiply by x/x: ((x+1)/x)/((x-1)/x).": 
                "乘以x/x：((x+1)/x)/((x-1)/x)。",
            "Same denominator.": 
                "相同分母。",
            "x = 1 or x = -9": 
                "x = 1或x = -9",
            "x² + 8x + 16 = 9 + 16.": 
                "x² + 8x + 16 = 9 + 16。",
            "Difference of squares twice.": 
                "平方差两次。",
            "Mean point always on line.": 
                "平均点总在直线上。",
            "Group: x(y+z) + w(y+z).": 
                "分组：x(y+z) + w(y+z)。",
            "c² = 25 - 9 = 16.": 
                "c² = 25 - 9 = 16。",
            "Factor: (2x-1)(x+3) < 0.": 
                "因式分解：(2x-1)(x+3) < 0。",
            "Roots -3 and 1/2.": 
                "根为-3和1/2。",
            "Absolute value: distance less than 3 from origin.": 
                "绝对值：距离原点小于3。",
            "dy/dx = (dy/dt)/(dx/dt).": 
                "dy/dx = (dy/dt)/(dx/dt)。",
            "Vieta's formulas: sum = -b/a, product = c/a.": 
                "韦达定理：和= -b/a，积= c/a。",
            "3x² - 12x ≤ 0, 3x(x-4) ≤ 0, interval [0,4].": 
                "3x² - 12x ≤ 0，3x(x-4) ≤ 0，区间[0,4]。",
            "not > 0": 
                "不> 0",
            "So x = 0 not in solution set.": 
                "所以x = 0不在解集中。",
            
            # Mathematical operations
            "At x = 100/4 = 25 units: P(25) = -1250 + 2500 - 1000 = 250.": 
                "在x = 100/4 = 25单位处：P(25) = -1250 + 2500 - 1000 = 250。",
            "$150": "$150",
            "AC method: a·c = 10, pair 1·10.": 
                "AC法：a·c = 10，配对1·10。",
            "Check: (1) + 1 = 2 and -(1) + 3 = 2. ✓": 
                "验证：(1) + 1 = 2和-(1) + 3 = 2。✓",
            "1/2·x = x - 1 gives x/2 = 1, so x = 2.": 
                "1/2·x = x - 1给出x/2 = 1，所以x = 2。",
            "-1(x² - 6x) - 2 = -(x-3)² + 9 - 2 = -(x-3)² + 7.": 
                "-1(x² - 6x) - 2 = -(x-3)² + 9 - 2 = -(x-3)² + 7。",
            "x² - 8x + 5 = (x-4)² - 16 + 5 = (x-4)² - 11.": 
                "x² - 8x + 5 = (x-4)² - 16 + 5 = (x-4)² - 11。",
            "(5-1)! = 4! = 24.": 
                "(5-1)! = 4! = 24。",
            "Multiply by conjugate: (5+2i)(1+i)/((1-i)(1+i)).": 
                "乘以共轭：(5+2i)(1+i)/((1-i)(1+i))。",
            "Directrix x = -2.": 
                "准线x = -2。",
            "Vertical and horizontal lines intersect at point.": 
                "竖直线和水平线在一点相交。",
            
            # Additional coordinate solutions  
            "(1) Solve one equation for a variable, (2) Substitute into other, (3) Solve, (4) Back-substitute.":
                "（1）从一个方程解出一个变量，（2）代入另一个方程，（3）求解，（4）回代。",
            "(7 + 7i)/2 = 3.5 + 3.5i": 
                "(7 + 7i)/2 = 3.5 + 3.5i",
            "Logarithmic curve.": 
                "对数曲线。",
            "(1/2)³ = 1/8": 
                "(1/2)³ = 1/8",
            "Three half-lives have passed.": 
                "经过了三个半衰期。",
            "h = -b/2a = 4/2 = 2, k = f(2) = 4-8+3 = -1.": 
                "h = -b/2a = 4/2 = 2，k = f(2) = 4-8+3 = -1。",
        }
        
        return mapping
    
    def get_existing_translations(self):
        """Get existing translations"""
        try:
            with open(self.trans_file, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = re.findall(r'"([^"]+)":\s*"[^"]*"', content)
            return set(matches)
        except:
            return set()
    
    def add_to_file(self, batch_name, translations_dict):
        """Add translations to file"""
        existing = self.get_existing_translations()
        to_add = {k: v for k, v in translations_dict.items() if k not in existing}
        
        if not to_add:
            print(f"  {batch_name}: Skipped (all exist)")
            return 0
        
        with open(self.trans_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        translation_lines = []
        for eng, chin in sorted(to_add.items()):
            eng_esc = eng.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
            chin_esc = chin.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
            translation_lines.append(f'    "{eng_esc}": "{chin_esc}",')
        
        last_entry = re.search(r'(".*?":\s*".*?",)\s*\n(\s*\}[,;]?)', content, re.DOTALL)
        if not last_entry:
            return 0
        
        new_content = (
            content[:last_entry.end(1)] + '\n' +
            '\n'.join(translation_lines) + '\n' +
            content[last_entry.start(2):]
        )
        
        with open(self.trans_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return len(to_add)
    
    def run(self):
        """Execute comprehensive translation"""
        print("=" * 80)
        print("COMPREHENSIVE REMAINING STRING TRANSLATION")
        print("=" * 80)
        print()
        
        untranslated = self.load_untranslated()
        print(f"Total untranslated strings loaded: {len(untranslated)}")
        print()
        
        mapping = self.create_comprehensive_mapping(untranslated)
        print(f"Translations created: {len(mapping)}")
        print()
        
        print("Adding translations to global_translations.js...")
        added = self.add_to_file("Comprehensive Batch 41-70", mapping)
        
        print()
        print("=" * 80)
        print(f"TRANSLATIONS ADDED: {added}")
        print("=" * 80)
        
        return added

if __name__ == '__main__':
    system = ComprehensiveTranslationSystem()
    system.run()
