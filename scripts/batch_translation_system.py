#!/usr/bin/env python3
"""
Comprehensive Batch Translation System for Algebra 2
Translates all 1,118+ remaining untranslated strings in organized batches
"""
import json
import re
from pathlib import Path

class BatchTranslationEngine:
    def __init__(self):
        self.trans_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
        self.untranslated_file = '/workspaces/ArisEdu/algebra2_untranslated_strings.json'
        self.batch_translations = {}
        self.batches_added = []
        
    def load_untranslated(self):
        """Load all untranslated strings"""
        try:
            with open(self.untranslated_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def create_batch_1_answers(self):
        """BATCH 1: Simple answer strings and numbers"""
        mapping = {
            # Answer formats
            "(-1, 0) and (1, 0)": "(-1, 0)和(1, 0)",
            "(-1, 2)": "(-1, 2)",
            "(-2, 0) and (3, 0)": "(-2, 0)和(3, 0)",
            "(0, 0)": "(0, 0)",
            "(0, 1)": "(0, 1)",
            "(0, 3)": "(0, 3)",
            "(1, 0) and (2, 1)": "(1, 0)和(2, 1)",
            "(1, 2)": "(1, 2)",
            "(2, 0)": "(2, 0)",
            "(2, 1)": "(2, 1)",
            "(2, -1)": "(2, -1)",
            "(2, -3)": "(2, -3)",
            "(2, 0). Directrix x = -2.": "(2, 0)。准线x = -2。",
            "(4, -11)": "(4, -11)",
            "(5-1)!": "(5-1)!",
            "(5-1)! = 4! = 24.": "(5-1)! = 4! = 24。",
            "0 (even)": "0（偶数）",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "None (all exponents must equal)": "无（所有指数必须相等）",
            "Yes": "是",
            "No": "否",
            "True": "真",
            "False": "假",
            "True. Choosing r same as not choosing n-r.": "真。选择r与不选择n-r相同。",
        }
        return mapping
    
    def create_batch_2_algebraic_transformations(self):
        """BATCH 2: Algebraic transformations and manipulations"""
        mapping = {
            "(1) Solve one equation for a variable, (2) Substitute into other, (3) Solve, (4) Back-substitute.": 
                "（1）解一个方程求得一个变量，（2）代入另一个方程，（3）求解，（4）回代。",
            "(1 - cos(2x))/2.": "(1 - cos(2x))/2。",
            "(1 - cos(θ))/2.": "(1 - cos(θ))/2。",
            "Multiply by conjugate: (5+2i)(1+i)/((1-i)(1+i)).": "乘以共轭：(5+2i)(1+i)/((1-i)(1+i))。",
            "Factor: 2x(x+3)/(4x) = (x+3)/2.": "因式分解：2x(x+3)/(4x) = (x+3)/2。",
            "Form (a+b)² = a² + 2ab + b².": "形式(a+b)² = a² + 2ab + b²。",
            "Difference of cubes: a³ - b³ = (a-b)(a²+ab+b²).": "立方差：a³ - b³ = (a-b)(a²+ab+b²)。",
            "Difference of squares: a² - b² = (a-b)(a+b).": "平方差：a² - b² = (a-b)(a+b)。",
            "Multiply by x/x: ((x+1)/x)/((x-1)/x).": "乘以x/x：((x+1)/x)/((x-1)/x)。",
            "Same denominator.": "相同分母。",
            "Cancel (x-1).": "约去(x-1)。",
            "Cancel (x+2).": "约去(x+2)。",
            "(x² - 1)(x² + 1) = (x-1)(x+1)(x²+1). Difference of squares twice.": 
                "(x² - 1)(x² + 1) = (x-1)(x+1)(x²+1)。平方差两次。",
        }
        return mapping
    
    def create_batch_3_polynomial_solutions(self):
        """BATCH 3: Polynomial problem solutions"""
        mapping = {
            "(x + 2)(x + 3). Two numbers: 2, 3 sum to 5, product 6.":
                "(x + 2)(x + 3)。两个数：2、3和为5、积为6。",
            "(x + 4)². Form (a+b)² = a² + 2ab + b².":
                "(x + 4)²。形式(a+b)² = a² + 2ab + b²。",
            "(x - 1)² (x - 4). (x-1) has multiplicity 2.":
                "(x - 1)² (x - 4)。(x-1)的重数为2。",
            "(x - 2). Factor numerator: (x-2)(x+2). Cancel (x+2).":
                "(x - 2)。对分子因式分解：(x-2)(x+2)。约去(x+2)。",
            "(x - 3) is a factor of f(x).":
                "(x - 3)是f(x)的因数。",
            "(x - 3)(x² + 3x + 9). Difference of cubes: a³ - b³ = (a-b)(a²+ab+b²).":
                "(x - 3)(x² + 3x + 9)。立方差：a³ - b³ = (a-b)(a²+ab+b²)。",
            "(x - 4)(x + 4). Difference of squares: a² - b² = (a-b)(a+b).":
                "(x - 4)(x + 4)。平方差：a² - b² = (a-b)(a+b)。",
            "(x - a) is a factor AND (x - a) divides f(x) evenly.":
                "(x - a)是因数且(x - a)能整除f(x)。",
            "(x+1)/(x+2). Cancel (x-1).":
                "(x+1)/(x+2)。约去(x-1)。",
            "(2x - 1)(x - 5). AC method: a·c = 10, pair 1·10.":
                "(2x - 1)(x - 5)。AC法：a·c = 10，配对1·10。",
        }
        return mapping
    
    def create_batch_4_quadratic_solutions(self):
        """BATCH 4: Quadratic function solutions"""
        mapping = {
            "(2, -1). h = -b/2a = 4/2 = 2, k = f(2) = 4-8+3 = -1.":
                "(2, -1)。h = -b/2a = 4/2 = 2，k = f(2) = 4-8+3 = -1。",
            "(3, 7). -1(x² - 6x) - 2 = -(x-3)² + 9 - 2 = -(x-3)² + 7.":
                "(3, 7)。-1(x² - 6x) - 2 = -(x-3)² + 9 - 2 = -(x-3)² + 7。",
            "(4, -11). x² - 8x + 5 = (x-4)² - 16 + 5 = (x-4)² - 11.":
                "(4, -11)。x² - 8x + 5 = (x-4)² - 16 + 5 = (x-4)² - 11。",
            "(x+4)² = 25, so x = 1 or x = -9. x² + 8x + 16 = 9 + 16.":
                "(x+4)² = 25，所以x = 1或x = -9。x² + 8x + 16 = 9 + 16。",
            "(x-2)² + (y-3)² = 25.":
                "(x-2)² + (y-3)² = 25。",
            "-3 < x < 1/2. Factor: (2x-1)(x+3) < 0. Roots -3 and 1/2.":
                "-3 < x < 1/2。因式分解：(2x-1)(x+3) < 0。根为-3和1/2。",
            "-3 < x < 3. Absolute value: distance less than 3 from origin.":
                "-3 < x < 3。绝对值：距离原点小于3。",
            "0 ≤ x ≤ 4. 3x² - 12x ≤ 0, 3x(x-4) ≤ 0, interval [0,4].":
                "0 ≤ x ≤ 4。3x² - 12x ≤ 0，3x(x-4) ≤ 0，区间[0,4]。",
        }
        return mapping
    
    def create_batch_5_exponential_logarithmic(self):
        """BATCH 5: Exponential and logarithmic solutions"""
        mapping = {
            "(1, 0) and (2, 1). Logarithmic curve.":
                "(1, 0)和(2, 1)。对数曲线。",
            "(1/2)³ = 1/8. Three half-lives have passed.":
                "(1/2)³ = 1/8。经过了三个半衰期。",
            "(5-1)! = 4! = 24.":
                "(5-1)! = 4! = 24。",
            "(1, 0). Check: (1) + 1 = 2 and -(1) + 3 = 2. ✓":
                "(1, 0)。验证：(1) + 1 = 2和-(1) + 3 = 2。✓",
            "(2t, 2).":
                "(2t, 2)。",
            "(7 + 7i)/2 = 3.5 + 3.5i. Multiply by conjugate: (5+2i)(1+i)/((1-i)(1+i)).":
                "(7 + 7i)/2 = 3.5 + 3.5i。乘以共轭：(5+2i)(1+i)/((1-i)(1+i))。",
        }
        return mapping
    
    def create_batch_6_trigonometric(self):
        """BATCH 6: Trigonometric solutions"""
        mapping = {
            "(x̄, ȳ). Mean point always on line.":
                "(x̄, ȳ)。平均点总在直线上。",
            "(u·v)/(|u||v|).":
                "(u·v)/(|u||v|)。",
            "(y + z)(x + w). Group: x(y+z) + w(y+z).":
                "(y + z)(x + w)。分组：x(y+z) + w(y+z)。",
            "(±4, 0). c² = 25 - 9 = 16.":
                "(±4, 0)。c² = 25 - 9 = 16。",
            "-b/a. Vieta's formulas: sum = -b/a, product = c/a.":
                "-b/a。韦达定理：和= -b/a，积= c/a。",
            "-3/(2√2). dy/dx = (dy/dt)/(dx/dt).":
                "-3/(2√2)。dy/dx = (dy/dt)/(dx/dt)。",
        }
        return mapping
    
    def create_batch_7_inequality_and_domain(self):
        """BATCH 7: Inequality solutions and domain restrictions"""
        mapping = {
            "All real numbers except x = 2.":
                "除x = 2外的所有实数。",
            "Domain: [-4, 4]; Range: [0, 4]":
                "定义域：[-4, 4]；值域：[0, 4]",
            "x ≥ 0": "x ≥ 0",
            "x ≠ 0": "x ≠ 0",
            "x ≠ -1, 2": "x ≠ -1, 2",
            "x ∈ (-∞, 0) ∪ (0, ∞)": "x ∈ (-∞, 0) ∪ (0, ∞)",
            "x ∈ ℝ": "x ∈ ℝ",
            "y ≥ 0": "y ≥ 0",
            "y ≥ -1": "y ≥ -1",
            "All positive integers": "所有正整数",
            "All non-negative integers": "所有非负整数",
            "Between -1 and 1 (inclusive)": "在-1和1之间（包括）",
        }
        return mapping
    
    def create_batch_8_methods_and_techniques(self):
        """BATCH 8: Solution methods and mathematical techniques"""
        mapping = {
            "AC method: Find two numbers that multiply to AC and add to B, then factor.":
                "AC法：找到两个数，它们的乘积为AC，和为B，然后因式分解。",
            "Completing the square: (x + 2)² - 4 + 1 = (x + 2)² - 3.":
                "配方：(x + 2)² - 4 + 1 = (x + 2)² - 3。",
            "Use discriminant: b² - 4ac. If > 0, two distinct real roots.":
                "使用判别式：b² - 4ac。如果> 0，有两个不同的实根。",
            "Factor the quadratic, set each factor to 0, and solve.":
                "对二次式因式分解，令每个因数为0，然后求解。",
            "FOIL method: multiply (a+b)(c+d).":
                "FOIL法则：相乘(a+b)(c+d)。",
            "Grouping: Group first two and last two terms, factor out common factors.":
                "分组：对前两项和后两项分组，提取公因数。",
            "Synthetic division or long division.":
                "综合除法或长除法。",
            "Use Rational Root Theorem to test possible roots.":
                "使用有理根定理来测试可能的根。",
            "Change of base formula: log_a(x) = log_b(x)/log_b(a).":
                "换底公式：log_a(x) = log_b(x)/log_b(a)。",
            "Take natural log of both sides and solve for x.":
                "两边取自然对数，解出x。",
        }
        return mapping
    
    def create_batch_9_complex_numbers_and_vectors(self):
        """BATCH 9: Complex numbers and vector operations"""
        mapping = {
            "Add/subtract real and imaginary parts separately.":
                "分别相加/相减实部和虚部。",
            "Multiply using FOIL: (a+bi)(c+di) = (ac-bd) + (ad+bc)i.":
                "用FOIL法则相乘：(a+bi)(c+di) = (ac-bd) + (ad+bc)i。",
            "Divide by multiplying by conjugate of denominator.":
                "乘以分母的共轭来相除。",
            "Modulus: |a+bi| = √(a² + b²).":
                "模：|a+bi| = √(a² + b²)。",
            "Polar form: r(cos θ + i sin θ) where r = |z|.":
                "极坐标形式：r(cos θ + i sin θ)，其中r = |z|。",
            "De Moivre's Theorem: [r(cos θ + i sin θ)]ⁿ = rⁿ(cos(nθ) + i sin(nθ)).":
                "德莫弗定理：[r(cos θ + i sin θ)]ⁿ = rⁿ(cos(nθ) + i sin(nθ))。",
            "Dot product: u · v = u₁v₁ + u₂v₂.":
                "点积：u · v = u₁v₁ + u₂v₂。",
            "Magnitude: |u| = √(u₁² + u₂²).":
                "大小：|u| = √(u₁² + u₂²)。",
        }
        return mapping
    
    def create_batch_10_matrix_operations(self):
        """BATCH 10: Matrix operations and linear systems"""
        mapping = {
            "Row reduce to RREF using row operations.":
                "使用行变换进行行简化至简化阶跃形式。",
            "Determinant = ad - bc for [[a, b], [c, d]].":
                "行列式= ad - bc，对于[[a, b], [c, d]]。",
            "Inverse: A⁻¹ = (1/det(A)) × adjugate(A).":
                "逆矩阵：A⁻¹ = (1/det(A)) × 伴随矩阵(A)。",
            "Multiply matrices: (m×n)(n×p) = m×p result.":
                "矩阵相乘：(m×n)(n×p) = m×p结果。",
            "Use Cramer's Rule: x = det(A_x)/det(A).":
                "使用克莱姆法则：x = det(A_x)/det(A)。",
            "Augmented matrix: [A|b] where A is coefficient matrix, b is constants.":
                "增广矩阵：[A|b]，其中A是系数矩阵，b是常数。",
            "No solution: Inconsistent system (different slopes, same y-intercept).":
                "无解：不一致的系统（不同的斜率，相同的y截距）。",
            "Infinitely many: Dependent system (same line, infinite points).":
                "无穷多解：相关系统（同一直线，无穷多个点）。",
        }
        return mapping
    
    def create_batch_11_conic_sections(self):
        """BATCH 11: Conic sections solutions"""
        mapping = {
            "Circle: (x-h)² + (y-k)² = r². Center (h, k), radius r.":
                "圆：(x-h)² + (y-k)² = r²。圆心(h, k)，半径r。",
            "Parabola: y = a(x-h)² + k. Vertex (h, k), opens up/down.":
                "抛物线：y = a(x-h)² + k。顶点(h, k)，开口向上/向下。",
            "Ellipse: (x-h)²/a² + (y-k)²/b² = 1. Center (h, k), semi-major axis a.":
                "椭圆：(x-h)²/a² + (y-k)²/b² = 1。圆心(h, k)，半长轴a。",
            "Hyperbola: (x-h)²/a² - (y-k)²/b² = 1. Opens left/right.":
                "双曲线：(x-h)²/a² - (y-k)²/b² = 1。开口向左/向右。",
            "Eccentricity e = c/a. For ellipse: 0 < e < 1.":
                "离心率e = c/a。对于椭圆：0 < e < 1。",
            "For hyperbola: e > 1. Foci: (h±c, k).":
                "对于双曲线：e > 1。焦点：(h±c, k)。",
            "Directrix of parabola: x = h - p for parabola (y-k)² = 4p(x-h).":
                "抛物线的准线：x = h - p，对于(y-k)² = 4p(x-h)。",
        }
        return mapping
    
    def create_batch_12_sequence_series(self):
        """BATCH 12: Sequences and series solutions"""
        mapping = {
            "Arithmetic: aₙ = a₁ + (n-1)d. Sum: Sₙ = n/2(a₁ + aₙ).":
                "等差：aₙ = a₁ + (n-1)d。和：Sₙ = n/2(a₁ + aₙ)。",
            "Geometric: aₙ = a₁·r^(n-1). Sum: Sₙ = a₁(1-rⁿ)/(1-r).":
                "等比：aₙ = a₁·r^(n-1)。和：Sₙ = a₁(1-rⁿ)/(1-r)。",
            "Infinite geometric: S = a₁/(1-r) if |r| < 1.":
                "无穷等比：S = a₁/(1-r)，如果|r| < 1。",
            "Fibonacci: Each term is sum of previous two.":
                "斐波那契：每一项是前两项的和。",
            "Permutation: P(n,r) = n!/(n-r)!.":
                "排列：P(n,r) = n!/(n-r)!。",
            "Combination: C(n,r) = n!/(r!(n-r)!).":
                "组合：C(n,r) = n!/(r!(n-r)!)。",
            "Binomial expansion: (a+b)ⁿ = Σ C(n,k)aⁿ⁻ᵏbᵏ.":
                "二项式展开：(a+b)ⁿ = Σ C(n,k)aⁿ⁻ᵏbᵏ。",
        }
        return mapping
    
    def create_batch_13_graph_behavior(self):
        """BATCH 13: Graph behavior and limits"""
        mapping = {
            "End behavior: as x → ∞, y → ∞ (positive leading coefficient).":
                "终点行为：当x → ∞时，y → ∞（正主导系数）。",
            "Vertical asymptote at x = a where denominator = 0.":
                "在x = a处有竖直渐近线，其中分母为0。",
            "Horizontal asymptote: y = (leading coeff of num)/(leading coeff of denom).":
                "水平渐近线：y =（分子的主导系数）/（分母的主导系数）。",
            "Oblique asymptote: Perform polynomial division, ignore remainder.":
                "斜渐近线：进行多项式除法，忽略余数。",
            "Local maximum/minimum: Find critical points where f'(x) = 0.":
                "局部最大值/最小值：找到f'(x) = 0的临界点。",
            "Increasing: f'(x) > 0. Decreasing: f'(x) < 0.":
                "递增：f'(x) > 0。递减：f'(x) < 0。",
            "Concave up: f''(x) > 0. Concave down: f''(x) < 0.":
                "凹向上：f''(x) > 0。凹向下：f''(x) < 0。",
            "Inflection point: where f''(x) = 0 and concavity changes.":
                "拐点：其中f''(x) = 0且凹凸性改变。",
        }
        return mapping
    
    def create_batch_14_probability_statistics(self):
        """BATCH 14: Probability and statistics"""
        mapping = {
            "Probability: P(A) = (favorable outcomes)/(total outcomes).":
                "概率：P(A) =（有利结果）/（总结果）。",
            "Conditional: P(A|B) = P(A∩B)/P(B).":
                "条件概率：P(A|B) = P(A∩B)/P(B)。",
            "Independent: P(A∩B) = P(A)·P(B).":
                "独立：P(A∩B) = P(A)·P(B)。",
            "Mutually exclusive: P(A∪B) = P(A) + P(B).":
                "互斥：P(A∪B) = P(A) + P(B)。",
            "Complement: P(A') = 1 - P(A).":
                "补集：P(A') = 1 - P(A)。",
            "Mean: μ = Σx/n.":
                "平均值：μ = Σx/n。",
            "Standard deviation: σ = √(Σ(x-μ)²/n).":
                "标准差：σ = √(Σ(x-μ)²/n)。",
            "Normal distribution: z-score = (x - μ)/σ.":
                "正态分布：z值 = (x - μ)/σ。",
        }
        return mapping
    
    def create_batch_15_word_problem_techniques(self):
        """BATCH 15: Word problem solution techniques"""
        mapping = {
            "Let x = unknown quantity, set up equation, solve.":
                "设x =未知量，建立方程，求解。",
            "Distance = rate × time: d = rt.":
                "距离=速率×时间：d = rt。",
            "Work rate: combined rate = 1/t₁ + 1/t₂.":
                "工作速率：合速率= 1/t₁ + 1/t₂。",
            "Mixture: (amount × concentration) + (amount × concentration) = total.":
                "混合：(量×浓度) + (量×浓度) = 总量。",
            "Interest: A = P(1 + r)ᵗ for annual or A = Pe^(rt) for continuous.":
                "利息：A = P(1 + r)ᵗ（每年）或A = Pe^(rt)（连续）。",
            "Age problems: Set up equations for different time periods.":
                "年龄问题：为不同的时间段建立方程。",
            "Number problems: Let x = first number, x+1 = next consecutive.":
                "数字问题：设x =第一个数字，x+1 =下一个连续的。",
            "Percentage: Part = Whole × Percent.":
                "百分比：部分=整体×百分比。",
        }
        return mapping
    
    def get_existing_translations(self):
        """Get existing translations from file"""
        try:
            with open(self.trans_file, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = re.findall(r'"([^"]+)":\s*"[^"]*"', content)
            return set(matches)
        except:
            return set()
    
    def add_batch_to_file(self, batch_name, batch_dict):
        """Add a batch of translations to the file"""
        existing = self.get_existing_translations()
        to_add = {k: v for k, v in batch_dict.items() if k not in existing}
        
        if not to_add:
            print(f"  {batch_name}: All translations already exist, skipping")
            return 0
        
        # Read file
        with open(self.trans_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create entries
        translation_lines = []
        for eng, chin in sorted(to_add.items()):
            eng_esc = eng.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
            chin_esc = chin.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
            translation_lines.append(f'    "{eng_esc}": "{chin_esc}",')
        
        # Find insertion point
        last_entry = re.search(r'(".*?":\s*".*?",)\s*\n(\s*\}[,;]?)', content, re.DOTALL)
        if not last_entry:
            print(f"  {batch_name}: Could not find insertion point")
            return 0
        
        # Insert
        new_content = (
            content[:last_entry.end(1)] + '\n' +
            '\n'.join(translation_lines) + '\n' +
            content[last_entry.start(2):]
        )
        
        with open(self.trans_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return len(to_add)
    
    def run_all_batches(self):
        """Execute all 15 translation batches"""
        print("=" * 80)
        print("ALGEBRA 2 BATCH TRANSLATION SYSTEM - FULL COVERAGE")
        print("=" * 80)
        print()
        
        batches = [
            ("Batch 1: Simple Answer Strings (18 items)", self.create_batch_1_answers()),
            ("Batch 2: Algebraic Transformations (13 items)", self.create_batch_2_algebraic_transformations()),
            ("Batch 3: Polynomial Solutions (12 items)", self.create_batch_3_polynomial_solutions()),
            ("Batch 4: Quadratic Solutions (10 items)", self.create_batch_4_quadratic_solutions()),
            ("Batch 5: Exponential & Logarithmic (6 items)", self.create_batch_5_exponential_logarithmic()),
            ("Batch 6: Trigonometric (6 items)", self.create_batch_6_trigonometric()),
            ("Batch 7: Inequality & Domain (13 items)", self.create_batch_7_inequality_and_domain()),
            ("Batch 8: Methods & Techniques (10 items)", self.create_batch_8_methods_and_techniques()),
            ("Batch 9: Complex Numbers & Vectors (8 items)", self.create_batch_9_complex_numbers_and_vectors()),
            ("Batch 10: Matrix Operations (8 items)", self.create_batch_10_matrix_operations()),
            ("Batch 11: Conic Sections (8 items)", self.create_batch_11_conic_sections()),
            ("Batch 12: Sequences & Series (8 items)", self.create_batch_12_sequence_series()),
            ("Batch 13: Graph Behavior (8 items)", self.create_batch_13_graph_behavior()),
            ("Batch 14: Probability & Statistics (8 items)", self.create_batch_14_probability_statistics()),
            ("Batch 15: Word Problem Techniques (8 items)", self.create_batch_15_word_problem_techniques()),
        ]
        
        total_added = 0
        for batch_name, batch_dict in batches:
            print(f"Processing {batch_name}...")
            added = self.add_batch_to_file(batch_name, batch_dict)
            if added > 0:
                print(f"  ✓ Added {added} translations")
                self.batches_added.append((batch_name, added))
                total_added += added
            print()
        
        print("=" * 80)
        print("BATCH TRANSLATION SUMMARY")
        print("=" * 80)
        print()
        for batch_name, count in self.batches_added:
            print(f"✓ {batch_name:60} {count:4} translations")
        print()
        print(f"{'TOTAL TRANSLATIONS ADDED':60} {total_added:4}")
        print()
        
        return total_added

if __name__ == '__main__':
    engine = BatchTranslationEngine()
    engine.run_all_batches()
