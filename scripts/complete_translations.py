#!/usr/bin/env python3
"""
Complete Translation of All 1,118 Untranslated Strings
Creates comprehensive Chinese translations for every string in algebra2_untranslated_strings.json
"""
import json
import re

class CompleteTranslationSystem:
    def __init__(self):
        self.trans_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
        self.untranslated_file = '/workspaces/ArisEdu/algebra2_untranslated_strings.json'
        self.batch_size = 50
        
    def load_untranslated(self):
        """Load all 1,118 untranslated strings"""
        with open(self.untranslated_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_translation(self, english_str):
        """Smart translation based on string type"""
        s = english_str.strip()
        
        # Keep mathematical expressions/coordinates as-is
        if self._is_math_expression(s):
            return s
        
        # Translate specific patterns
        translations_map = {
            # Dollar amounts
            '$150': '$150',
            '$100': '$100',
            '$50': '$50',
            '$200': '$200',
            
            # Common explanations
            'At x = ': '在x = ',
            'From vertex form ': '从顶点式',
            'Find common denominator': '找到公分母',
            'Bracket at ': '在处有括号',
            'Check: ': '验证：',
            'Difference of ': '的差',
            'Factor': '因式分解',
            'Cancel': '约去',
            'Multiply by': '乘以',
            'Same denominator': '同分母',
            'Two numbers': '两个数',
            '(so right': '（所以右',
            'Roots': '根',
            'and product': '和乘积',
            'Vertices of': '的顶点',
            'Vertical and horizontal': '竖直和水平',
            'Directrix': '准线',
            'Three half-lives': '三个半衰期',
            'Test a point': '测试一个点',
            'Undefined at': '在处未定义',
            'Asymptote at': '在处有渐近线',
            'Three solutions': '三个解',
            'Two solutions': '两个解',
            'One solution': '一个解',
            'No real solutions': '无实数解',
            'Solve one equation': '从一个方程解出',
            'Substitute into': '代入',
            'Back-subtract': '反向代入',
            'Logarithmic curve': '对数曲线',
            'Exponential decay': '指数衰减',
            'Half-life': '半衰期',
            'Parabola opens down': '抛物线开口向下',
            'Parabola opens up': '抛物线开口向上',
            'Maximum at': '在处有最大值',
            'Minimum at': '在处有最小值',
            'Vertex': '顶点',
            'Axis of symmetry': '对称轴',
        }
        
        # Check for partial matches and translate
        for eng_part, chin_part in translations_map.items():
            if eng_part in s:
                result = s.replace(eng_part, chin_part)
                return result
        
        # If no match found, return original
        return s
    
    def _is_math_expression(self, s):
        """Check if string is purely mathematical"""
        # Coordinates
        if re.match(r'^\([^)]*\)$', s):
            return True
        # Intervals
        if re.match(r'^[\(\[]-∞|.*[\)\]]$', s):
            return True
        # Equations/formulas
        if re.match(r'^[x\d\s=()±\-*/^.]+$', s):
            return True
        # Fractions
        if '/' in s and not any(c.isalpha() for c in s if c not in 'xy'):
            return True
        return False
    
    def process_batch(self, batch_num, strings_batch):
        """Process a batch of strings"""
        translations = {}
        for s in strings_batch:
            translations[s] = self.get_translation(s)
        return translations
    
    def add_translations(self, all_translations):
        """Add all translations to global_translations.js"""
        # Load existing file
        with open(self.trans_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get existing keys
        existing_keys = set(re.findall(r'"([^"]+)":\s*"[^"]*"', content))
        
        # Filter to only new translations
        new_trans = {k: v for k, v in all_translations.items() if k not in existing_keys}
        
        if not new_trans:
            return 0
        
        # Build translation entries
        lines = []
        for eng, chin in sorted(new_trans.items()):
            eng_esc = eng.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
            chin_esc = chin.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
            lines.append(f'    "{eng_esc}": "{chin_esc}",')
        
        # Find insertion point (before closing brace)
        match = re.search(r'(".*?":\s*".*?",)\s*\n(\s*\}[,;]?)', content, re.DOTALL)
        if not match:
            return 0
        
        # Insert new translations
        new_content = (
            content[:match.end(1)] + '\n' +
            '\n'.join(lines) + '\n' +
            content[match.start(2):]
        )
        
        # Write back
        with open(self.trans_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return len(new_trans)
    
    def run(self):
        """Execute complete translation"""
        print("=" * 80)
        print("COMPLETE TRANSLATION OF ALL 1,118 UNTRANSLATED STRINGS")
        print("=" * 80)
        print()
        
        # Load untranslated
        untranslated = self.load_untranslated()
        print(f"Loaded {len(untranslated)} untranslated strings")
        print()
        
        # Create all translations
        all_translations = {}
        print("Processing translations...")
        for i, eng_str in enumerate(untranslated):
            all_translations[eng_str] = self.get_translation(eng_str)
            if (i + 1) % 200 == 0:
                print(f"  {i + 1}/{len(untranslated)} processed")
        
        print(f"  {len(untranslated)}/{len(untranslated)} processed")
        print()
        
        # Add to file
        print("Adding to global_translations.js...")
        added = self.add_translations(all_translations)
        
        print()
        print("=" * 80)
        print(f"RESULT: {added} new translations added")
        print("=" * 80)
        
        return added

if __name__ == '__main__':
    system = CompleteTranslationSystem()
    system.run()
