#!/usr/bin/env python3
"""
Final Batch Translation System - Batches 31-40
Completing full coverage with specific problem instances and detailed solutions
"""
import re

class FinalBatchTranslationEngine:
    def __init__(self):
        self.trans_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
    
    def create_batch_31_specific_quadratic_solutions(self):
        """BATCH 31: Specific quadratic problem solutions"""
        mapping = {
            "Subtract 5: x² - 2x - 8 = 0.": "减去5：x² - 2x - 8 = 0。",
            "Take square root: x - 1 = ±2.": "开平方：x - 1 = ±2。",
            "Divide by 2: x² - 5x + 1 = 0.": "除以2：x² - 5x + 1 = 0。",
            "Quadratic formula: x = (-b ± √(b²-4ac))/(2a).": "二次公式：x = (-b ± √(b²-4ac))/(2a)。",
            "Two integers that multiply to 6 and add to 5: 2 and 3.": "两个整数，乘积为6，和为5：2和3。",
            "Discriminant = 0, one repeated root.": "判别式= 0，一个重根。",
            "Discriminant < 0, no real solutions.": "判别式< 0，无实数解。",
            "Discriminant > 0, two distinct real solutions.": "判别式> 0，两个不同的实数解。",
        }
        return mapping
    
    def create_batch_32_specific_exponential_logarithmic(self):
        """BATCH 32: Specific exponential and logarithmic solutions"""
        mapping = {
            "Take log of both sides: log(2ˣ) = log(100).": "两边取对数：log(2ˣ) = log(100)。",
            "Use power rule: x·log(2) = log(100).": "使用幂法则：x·log(2) = log(100)。",
            "Solve for x: x = log(100)/log(2).": "解出x：x = log(100)/log(2)。",
            "Natural log: ln(e²ˣ) = ln(50).": "自然对数：ln(e²ˣ) = ln(50)。",
            "Exponential form: 2³ = 8.": "指数形式：2³ = 8。",
            "Logarithmic form: log₂(8) = 3.": "对数形式：log₂(8) = 3。",
            "Add exponents: aᵐ · aⁿ = aᵐ⁺ⁿ.": "指数相加：aᵐ · aⁿ = aᵐ⁺ⁿ。",
            "Subtract exponents: aᵐ / aⁿ = aᵐ⁻ⁿ.": "指数相减：aᵐ / aⁿ = aᵐ⁻ⁿ。",
        }
        return mapping
    
    def create_batch_33_polynomial_division_solutions(self):
        """BATCH 33: Polynomial division and remainder solutions"""
        mapping = {
            "Divide 2x³ by x: 2x².": "将2x³除以x：2x²。",
            "Multiply back: 2x²(x-2) = 2x³ - 4x².": "乘回：2x²(x-2) = 2x³ - 4x²。",
            "Subtract from dividend to get new dividend.": "从被除数减去得到新被除数。",
            "Continue until degree of remainder < degree of divisor.": "继续直到余数的次数<除数的次数。",
            "Quotient + remainder/divisor = final answer.": "商+余数/除数=最终答案。",
            "Remainder = 0: Divisor is a factor.": "余数= 0：除数是因数。",
            "Remainder ≠ 0: Divisor is not a factor.": "余数≠ 0：除数不是因数。",
            "Synthetic division is faster for linear divisors.": "综合除法对线性除数更快。",
        }
        return mapping
    
    def create_batch_34_rational_expression_solutions(self):
        """BATCH 34: Rational expression simplification"""
        mapping = {
            "Find common denominator before adding/subtracting.": "相加/相减前找到公分母。",
            "Multiply numerators and denominators.": "数值和分母相乘。",
            "For division: multiply by reciprocal.": "对于除法：乘以倒数。",
            "Cancel common factors only.": "仅约去公因数。",
            "Reduced form: No common factors remain.": "最简形式：没有公因数。",
            "Excluded values: Where denominator = 0.": "排除的值：分母= 0的地方。",
            "Undefined at x = 2 (denominator zero).": "在x = 2处未定义（分母为零）。",
            "Simplify by factoring numerator and denominator first.": "先对分子和分母因式分解来简化。",
        }
        return mapping
    
    def create_batch_35_trig_equation_solutions(self):
        """BATCH 35: Trigonometric equation solutions"""
        mapping = {
            "sin(x) = 1/2 at x = π/6, 5π/6 in [0, 2π).": "sin(x) = 1/2在x = π/6, 5π/6（在[0, 2π)中）。",
            "cos(x) = √3/2 at x = π/6, 11π/6.": "cos(x) = √3/2在x = π/6, 11π/6。",
            "tan(x) = √3 at x = π/3, 4π/3.": "tan(x) = √3在x = π/3, 4π/3。",
            "General solutions add 2πk or πk (for tangent).": "一般解加2πk或πk（对于正切）。",
            "Check for extraneous solutions when squaring.": "平方时检查增根。",
            "Use inverse trig: sin⁻¹, cos⁻¹, tan⁻¹.": "使用反三角函数：sin⁻¹, cos⁻¹, tan⁻¹。",
            "Verify solution in original equation.": "在原方程中验证解。",
            "Domain of inverse: sin⁻¹ and cos⁻¹ are [-π/2, π/2].": "反函数定义域：sin⁻¹和cos⁻¹是[-π/2, π/2]。",
        }
        return mapping
    
    def create_batch_36_matrix_properties(self):
        """BATCH 36: Matrix properties and operations"""
        mapping = {
            "Identity matrix I: AI = IA = A.": "单位矩阵I：AI = IA = A。",
            "Zero matrix O: A + O = A, AO = O.": "零矩阵O：A + O = A，AO = O。",
            "Transpose Aᵀ: Rows become columns.": "转置Aᵀ：行变为列。",
            "Symmetric: A = Aᵀ.": "对称的：A = Aᵀ。",
            "(AB)ᵀ = BᵀAᵀ.": "(AB)ᵀ = BᵀAᵀ。",
            "Orthogonal: AAᵀ = I.": "正交的：AAᵀ = I。",
            "Inverse exists: det(A) ≠ 0.": "逆矩阵存在：det(A) ≠ 0。",
            "Singular: det(A) = 0, no inverse.": "奇异的：det(A) = 0，无逆矩阵。",
        }
        return mapping
    
    def create_batch_37_word_problems_specific(self):
        """BATCH 37: Specific word problem solutions"""
        mapping = {
            "Let x = hours worked. Then hourly pay = total/x.": "设x =工作小时数。那么小时工资=总计/x。",
            "Set up equation: Distance = Rate × Time.": "建立方程：距离=速率×时间。",
            "Slower speed: Let x = speed, x+10 = faster speed.": "较慢速度：设x =速度，x+10 =较快速度。",
            "Interest problem: Principal × Rate × Time = Interest.": "利息问题：本金×利率×时间=利息。",
            "Mixture: Amount₁ × Percent₁ + Amount₂ × Percent₂ = Total.": "混合：数量₁×百分比₁+数量₂×百分比₂=总计。",
            "Check answer in original problem (not just equation).": "在原始问题中检查答案（不仅仅是方程）。",
            "Watch units: Ensure consistent units throughout.": "注意单位：确保始终单位一致。",
            "Reasonableness: Does answer make sense contextually?": "合理性：答案在问题背景下是否有意义？",
        }
        return mapping
    
    def create_batch_38_conic_focus_directrix(self):
        """BATCH 38: Conic section focus and directrix properties"""
        mapping = {
            "Circle: c = 0, all points equidistant from center.": "圆：c = 0，所有点到圆心等距。",
            "Ellipse: c² = a² - b². Foci: (h±c, k) or (h, k±c).": "椭圆：c² = a² - b²。焦点：(h±c, k)或(h, k±c)。",
            "Hyperbola: c² = a² + b². Foci: (h±c, k) or (h, k±c).": "双曲线：c² = a² + b²。焦点：(h±c, k)或(h, k±c)。",
            "Parabola: Focus and directrix equidistant from curve point.": "抛物线：焦点和准线到曲线点的距离相等。",
            "Eccentricity e < 1: Ellipse. e = 1: Parabola.": "离心率e < 1：椭圆。e = 1：抛物线。",
            "Eccentricity e > 1: Hyperbola.": "离心率e > 1：双曲线。",
            "Directrix of parabola: x = h - p (opens right).": "抛物线的准线：x = h - p（开口向右）。",
            "For vertical: y = k - p (opens up).": "对于竖直的：y = k - p（开口向上）。",
        }
        return mapping
    
    def create_batch_39_recursion_and_series_convergence(self):
        """BATCH 39: Recursion and series convergence tests"""
        mapping = {
            "Recursive formula: aₙ defined in terms of previous terms.": "递归公式：aₙ用前面项定义。",
            "nth-term test: If lim(aₙ) ≠ 0, series diverges.": "第n项测试：如果lim(aₙ) ≠ 0，级数发散。",
            "Geometric series test: |r| < 1 converges.": "几何级数测试：|r| < 1收敛。",
            "Ratio test: lim|aₙ₊₁/aₙ| < 1 converges.": "比值测试：lim|aₙ₊₁/aₙ| < 1收敛。",
            "Root test: lim ⁿ√|aₙ| < 1 converges.": "根测试：lim ⁿ√|aₙ| < 1收敛。",
            "Integral test: If ∫f(x)dx converges, series converges.": "积分测试：如果∫f(x)dx收敛，级数收敛。",
            "Comparison test: Compare to known convergent/divergent series.": "比较测试：与已知的收敛/发散级数比较。",
            "Alternating series: Converges if terms decrease and approach 0.": "交替级数：如果项递减并接近0则收敛。",
        }
        return mapping
    
    def create_batch_40_complex_problem_synthesis(self):
        """BATCH 40: Complex problem synthesis and multi-step solutions"""
        mapping = {
            "Read problem carefully twice. Identify what's given and what's needed.": 
                "仔细读两次问题。识别已知和需要的。",
            "Draw diagram if applicable. Label known and unknown quantities.": 
                "绘制图表（如适用）。标记已知和未知的量。",
            "Translate words to mathematical expressions or equations.": 
                "将单词翻译为数学表达式或方程。",
             "Solve the equation or system systematically, showing all steps.": 
                "系统地解方程或方程组，显示所有步骤。",
            "Check solution: Substitute back into original equation.": 
                "检查解：代入原始方程。",
            "Verify answer is reasonable in original context.": 
                "验证答案在原始背景中合理。",
            "Multiple approaches: Try different methods, verify same result.": 
                "多种方法：尝试不同方法，验证相同结果。",
            "Explain reasoning: Show why each step is valid and necessary.": 
                "解释推理：显示为什么每一步有效和必要。",
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
    
    def add_batch_to_file(self, batch_name, batch_dict):
        """Add batch to file"""
        existing = self.get_existing_translations()
        to_add = {k: v for k, v in batch_dict.items() if k not in existing}
        
        if not to_add:
            print(f"  {batch_name}: All translations already exist, skipping")
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
    
    def run_all_batches(self):
        """Execute batches 31-40"""
        print("=" * 80)
        print("ALGEBRA 2 FINAL BATCH TRANSLATION SYSTEM - BATCHES 31-40")
        print("=" * 80)
        print()
        
        batches = [
            ("Batch 31: Specific Quadratic Solutions (8 items)", self.create_batch_31_specific_quadratic_solutions()),
            ("Batch 32: Specific Exp/Log Solutions (8 items)", self.create_batch_32_specific_exponential_logarithmic()),
            ("Batch 33: Polynomial Division (8 items)", self.create_batch_33_polynomial_division_solutions()),
            ("Batch 34: Rational Expression Solutions (8 items)", self.create_batch_34_rational_expression_solutions()),
            ("Batch 35: Trigonometric Equations (8 items)", self.create_batch_35_trig_equation_solutions()),
            ("Batch 36: Matrix Properties (8 items)", self.create_batch_36_matrix_properties()),
            ("Batch 37: Specific Word Problems (8 items)", self.create_batch_37_word_problems_specific()),
            ("Batch 38: Conic Focus/Directrix (8 items)", self.create_batch_38_conic_focus_directrix()),
            ("Batch 39: Recursion & Convergence (8 items)", self.create_batch_39_recursion_and_series_convergence()),
            ("Batch 40: Complex Problem Synthesis (8 items)", self.create_batch_40_complex_problem_synthesis()),
        ]
        
        total_added = 0
        for batch_name, batch_dict in batches:
            print(f"Processing {batch_name}...")
            added = self.add_batch_to_file(batch_name, batch_dict)
            if added > 0:
                print(f"  ✓ Added {added} translations")
                total_added += added
            print()
        
        print("=" * 80)
        print(f"TOTAL TRANSLATIONS ADDED (BATCHES 31-40): {total_added}")
        print(f"CUMULATIVE TOTAL (BATCHES 1-40): {total_added + 256}")
        print("=" * 80)
        
        return total_added

if __name__ == '__main__':
    engine = FinalBatchTranslationEngine()
    engine.run_all_batches()
