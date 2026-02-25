#!/usr/bin/env python3
"""
Extended Batch Translation System - Batches 16-30
Covering specific problem types, edge cases, and detailed solutions
"""
import re
from pathlib import Path

class ExtendedBatchTranslationEngine:
    def __init__(self):
        self.trans_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
    
    def create_batch_16_function_analysis(self):
        """BATCH 16: Function analysis and properties"""
        mapping = {
            "Even function: f(-x) = f(x). Graph symmetric about y-axis.":
                "偶函数：f(-x) = f(x)。图像关于y轴对称。",
            "Odd function: f(-x) = -f(x). Graph symmetric about origin.":
                "奇函数：f(-x) = -f(x)。图像关于原点对称。",
            "One-to-one: Each y-value has exactly one x-value.":
                "一一对应：每个y值恰好对应一个x值。",
            "Onto: Every y-value in codomain has at least one x-value.":
                "映上：陪域中的每个y值至少有一个x值。",
            "Continuous at a: lim(x→a⁻) f(x) = lim(x→a⁺) f(x) = f(a).":
                "在a处连续：lim(x→a⁻) f(x) = lim(x→a⁺) f(x) = f(a)。",
            "Jump discontinuity: Left and right limits exist but not equal.":
                "跳跃间断：左右极限存在但不相等。",
            "Removable discontinuity: Hole at point, limit exists.":
                "可去间断：点处有洞，极限存在。",
            "Infinite discontinuity: Vertical asymptote present.":
                "无穷间断：存在竖直渐近线。",
        }
        return mapping
    
    def create_batch_17_transformation_patterns(self):
        """BATCH 17: Function transformations and shifts"""
        mapping = {
            "Horizontal shift right by c: f(x) → f(x-c).":
                "向右水平移动c：f(x) → f(x-c)。",
            "Horizontal shift left by c: f(x) → f(x+c).":
                "向左水平移动c：f(x) → f(x+c)。",
            "Vertical shift up by c: f(x) → f(x) + c.":
                "向上垂直移动c：f(x) → f(x) + c。",
            "Vertical shift down by c: f(x) → f(x) - c.":
                "向下垂直移动c：f(x) → f(x) - c。",
            "Vertical stretch by factor a: f(x) → a·f(x).":
                "垂直拉伸因子a：f(x) → a·f(x)。",
            "Vertical compression by factor 1/a: f(x) → f(x)/a.":
                "垂直压缩因子1/a：f(x) → f(x)/a。",
            "Horizontal stretch by factor 1/b: f(x) → f(x/b).":
                "水平拉伸因子1/b：f(x) → f(x/b)。",
            "Horizontal compression by factor b: f(x) → f(bx).":
                "水平压缩因子b：f(x) → f(bx)。",
            "Reflect about x-axis: f(x) → -f(x).":
                "关于x轴反射：f(x) → -f(x)。",
            "Reflect about y-axis: f(x) → f(-x).":
                "关于y轴反射：f(x) → f(-x)。",
        }
        return mapping
    
    def create_batch_18_rational_function_details(self):
        """BATCH 18: Rational function specific solutions"""
        mapping = {
            "Simplify before analyzing, cancel common factors.":
                "在分析前简化，约去公因数。",
            "Vertical asymptote: Set denominator = 0, solve for x.":
                "竖直渐近线：令分母= 0，解出x。",
            "Hole (removable discontinuity): Factor and cancel.":
                "洞（可去间断）：因式分解并约去。",
            "Degree of numerator = degree of denominator: y = leading coeff ratio.":
                "分子次数=分母次数：y =主导系数比。",
            "Degree of numerator > degree of denominator: No horizontal asymptote.":
                "分子次数>分母次数：没有水平渐近线。",
            "Degree of numerator < degree of denominator: y = 0 asymptote.":
                "分子次数<分母次数：y = 0渐近线。",
            "Oblique asymptote: Numerator degree = denominator degree + 1.":
                "斜渐近线：分子次数=分母次数+ 1。",
            "Sign analysis: Test values in each interval.":
                "符号分析：在每个区间测试值。",
        }
        return mapping
    
    def create_batch_19_exponential_growth_decay(self):
        """BATCH 19: Exponential growth and decay models"""
        mapping = {
            "Exponential growth model: A(t) = A₀(1 + r)ᵗ.":
                "指数增长模型：A(t) = A₀(1 + r)ᵗ。",
            "Exponential decay model: A(t) = A₀(1 - r)ᵗ.":
                "指数衰减模型：A(t) = A₀(1 - r)ᵗ。",
            "Continuous growth: A(t) = A₀eᵏᵗ.":
                "连续增长：A(t) = A₀eᵏᵗ。",
            "Half-life: Amount = Initial × (1/2)^(t/half-life).":
                "半衰期：数量=初始× (1/2)^(t/半衰期)。",
            "Doubling time: A(t) = A₀ × 2^(t/doubling time).":
                "倍增时间：A(t) = A₀ × 2^(t/倍增时间)。",
            "Compound interest: A = P(1 + r/n)^(nt).":
                "复利：A = P(1 + r/n)^(nt)。",
            "Continuous compound: A = Pe^(rt).":
                "连续复利：A = Pe^(rt)。",
            "Annual percentage yield: APY = (1 + r/n)^n - 1.":
                "年百分比收益率：APY = (1 + r/n)^n - 1。",
        }
        return mapping
    
    def create_batch_20_logarithmic_equations(self):
        """BATCH 20: Logarithmic equations and properties"""
        mapping = {
            "Product rule: log(ab) = log(a) + log(b).":
                "乘法法则：log(ab) = log(a) + log(b)。",
            "Quotient rule: log(a/b) = log(a) - log(b).":
                "商法则：log(a/b) = log(a) - log(b)。",
            "Power rule: log(aᵇ) = b·log(a).":
                "幂法则：log(aᵇ) = b·log(a)。",
            "Change of base: logₐ(b) = log(b)/log(a).":
                "换底：logₐ(b) = log(b)/log(a)。",
            "Inverse of exponent: If bˣ = a, then x = logₐ(b).":
                "指数的反：如果bˣ = a，那么x = logₐ(b)。",
            "Domain of log: Argument must be positive.":
                "对数的定义域：参数必须为正。",
            "One-to-one property: logₐ(m) = logₐ(n) ⟹ m = n.":
                "一一对应性：logₐ(m) = logₐ(n) ⟹ m = n。",
            "Expand: log(2x³√y) = log(2) + 3log(x) + (1/2)log(y).":
                "展开：log(2x³√y) = log(2) + 3log(x) + (1/2)log(y)。",
        }
        return mapping
    
    def create_batch_21_trigonometric_identities_solutions(self):
        """BATCH 21: Trigonometric identity solutions"""
        mapping = {
            "Pythagorean identity: sin²θ + cos²θ = 1.":
                "勾股恒等式：sin²θ + cos²θ = 1。",
            "Reciprocal: csc(θ) = 1/sin(θ), sec(θ) = 1/cos(θ).":
                "倒数：csc(θ) = 1/sin(θ)，sec(θ) = 1/cos(θ)。",
            "Quotient: tan(θ) = sin(θ)/cos(θ).":
                "商：tan(θ) = sin(θ)/cos(θ)。",
            "Sum identity: sin(α±β) = sin(α)cos(β) ± cos(α)sin(β).":
                "和恒等式：sin(α±β) = sin(α)cos(β) ± cos(α)sin(β)。",
            "Double angle: sin(2θ) = 2sin(θ)cos(θ).":
                "二倍角：sin(2θ) = 2sin(θ)cos(θ)。",
            "Half angle: sin(θ/2) = ±√((1-cos(θ))/2).":
                "半角：sin(θ/2) = ±√((1-cos(θ))/2)。",
            "Cofunction: sin(π/2 - θ) = cos(θ).":
                "辅角：sin(π/2 - θ) = cos(θ)。",
            "Even-odd: cos(-θ) = cos(θ), sin(-θ) = -sin(θ).":
                "偶奇：cos(-θ) = cos(θ)，sin(-θ) = -sin(θ)。",
        }
        return mapping
    
    def create_batch_22_unit_circle_solutions(self):
        """BATCH 22: Unit circle and radian measure"""
        mapping = {
            "radian = (degrees × π)/180.":
                "弧度= (度数× π)/180。",
            "degrees = (radians × 180)/π.":
                "度数= (弧度× 180)/π。",
            "Unit circle: x² + y² = 1, (cos(θ), sin(θ)).":
                "单位圆：x² + y² = 1，(cos(θ)，sin(θ))。",
            "Quadrant I: All positive. Quadrant II: sin positive.":
                "第一象限：全正。第二象限：sin正。",
            "Quadrant III: tan positive. Quadrant IV: cos positive.":
                "第三象限：tan正。第四象限：cos正。",
            "Reference angle: Acute angle to x-axis in standard position.":
                "参考角：标准位置到x轴的锐角。",
            "Coterminal: Add or subtract 2π to get same angle.":
                "终边相同的角：加或减2π得到相同的角。",
            "Period of sin/cos: 2π. Period of tan: π.":
                "sin/cos周期：2π。tan周期：π。",
        }
        return mapping
    
    def create_batch_23_system_solving_methods(self):
        """BATCH 23: System solving techniques"""
        mapping = {
            "Substitution: Solve for one variable in one equation, substitute in other.":
                "代入法：在一个方程中解出一个变量，代入另一个方程。",
            "Elimination: Multiply equations to make coefficients equal, subtract.":
                "消元法：相乘方程使系数相等，相减。",
            "Graphical: Find intersection points of graphs.":
                "图形法：找到图形的交点。",
            "Matrix (Gaussian): Row reduce augmented matrix to RREF.":
                "矩阵（高斯）：将增广矩阵行化为简化阶跃形式。",
            "Cramer's Rule: x = det(A_x)/det(A), y = det(A_y)/det(A).":
                "克莱姆法则：x = det(A_x)/det(A)，y = det(A_y)/det(A)。",
            "Number solution: Unique solution (intersecting lines).":
                "唯一解：唯一解（相交的直线）。",
            "No solution: Parallel lines (same slope, different intercept).":
                "无解：平行线（相同斜率，不同截距）。",
            "Infinitely many: Same line (all points in common).":
                "无穷多解：同一直线（所有点共同）。",
        }
        return mapping
    
    def create_batch_24_combination_permutation(self):
        """BATCH 24: Combinations and permutations"""
        mapping = {
            "Permutation: P(n,r) = n!/(n-r)!. Order matters.":
                "排列：P(n,r) = n!/(n-r)!。顺序重要。",
            "Combination: C(n,r) = n!/(r!(n-r)!). Order doesn't matter.":
                "组合：C(n,r) = n!/(r!(n-r)!)。顺序不重要。",
            "Factorial: n! = n × (n-1) × (n-2) × ... × 1.":
                "阶乘：n! = n × (n-1) × (n-2) × ... × 1。",
            "Circular permutation: (n-1)! ways to arrange n objects in circle.":
                "圆形排列：安排n个对象在圆形中的(n-1)!方式。",
            "With repetition allowed: nʳ ways for r selections from n items.":
                "允许重复：n个项中r个选择的nʳ种方式。",
            "Without repetition: P(n,r) or C(n,r) depending on order.":
                "不允许重复：根据顺序使用P(n,r)或C(n,r)。",
            "Binomial coefficient: C(n,k) = n choose k.":
                "二项式系数：C(n,k) = n选k。",
            "Expanding (a+b)ⁿ: Use C(n,k) for coefficients.":
                "展开(a+b)ⁿ：使用C(n,k)作为系数。",
        }
        return mapping
    
    def create_batch_25_polar_coordinates(self):
        """BATCH 25: Polar coordinates and complex numbers"""
        mapping = {
            "Polar to rectangular: x = r cos(θ), y = r sin(θ).":
                "极坐标转直角：x = r cos(θ)，y = r sin(θ)。",
            "Rectangular to polar: r = √(x² + y²), tan(θ) = y/x.":
                "直角转极坐标：r = √(x² + y²)，tan(θ) = y/x。",
            "Complex number: z = a + bi in rectangular, z = r(cos(θ) + i sin(θ)) in polar.":
                "复数：z = a + bi（直角），z = r(cos(θ) + i sin(θ))（极坐标）。",
            "Modulus: |z| = √(a² + b²) = r.":
                "模：|z| = √(a² + b²) = r。",
            "Argument: θ = arctan(b/a), adjusted for quadrant.":
                "幅角：θ = arctan(b/a)，根据象限调整。",
            "Euler's formula: e^(iθ) = cos(θ) + i sin(θ).":
                "欧拉公式：e^(iθ) = cos(θ) + i sin(θ)。",
            "Multiplication in polar: (r₁∠θ₁)(r₂∠θ₂) = r₁r₂∠(θ₁+θ₂).":
                "极坐标相乘：(r₁∠θ₁)(r₂∠θ₂) = r₁r₂∠(θ₁+θ₂)。",
            "Division in polar: (r₁∠θ₁)/(r₂∠θ₂) = (r₁/r₂)∠(θ₁-θ₂).":
                "极坐标相除：(r₁∠θ₁)/(r₂∠θ₂) = (r₁/r₂)∠(θ₁-θ₂)。",
        }
        return mapping
    
    def create_batch_26_vector_operations(self):
        """BATCH 26: Vector operations and properties"""
        mapping = {
            "Vector magnitude: |⟨a,b⟩| = √(a² + b²).":
                "向量大小：|⟨a,b⟩| = √(a² + b²)。",
            "Unit vector: û = u/|u|.":
                "单位向量：û = u/|u|。",
            "Dot product: u·v = u₁v₁ + u₂v₂ = |u||v|cos(θ).":
                "点积：u·v = u₁v₁ + u₂v₂ = |u||v|cos(θ)。",
            "Orthogonal vectors: u·v = 0.":
                "正交向量：u·v = 0。",
            "Angle between vectors: cos(θ) = (u·v)/(|u||v|).":
                "向量间夹角：cos(θ) = (u·v)/(|u||v|)。",
            "Vector projection: proj_u(v) = ((v·u)/(u·u))u.":
                "向量投影：proj_u(v) = ((v·u)/(u·u))u。",
            "Component of v in direction of u: (v·u)/|u|.":
                "v在u方向的分量：(v·u)/|u|。",
            "Linear combination: c₁u + c₂v (adding vectors).":
                "线性组合：c₁u + c₂v（向量相加）。",
        }
        return mapping
    
    def create_batch_27_parametric_equations(self):
        """BATCH 27: Parametric equations"""
        mapping = {
            "Parametric form: x = f(t), y = g(t) for parameter t.":
                "参数形式：x = f(t)，y = g(t)，参数为t。",
            "Eliminate parameter: Solve one equation for t, substitute in other.":
                "消去参数：从一个方程解出t，代入另一个。",
            "Projectile motion: x = v₀t cos(θ), y = v₀t sin(θ) - (1/2)gt².":
                "抛体运动：x = v₀t cos(θ)，y = v₀t sin(θ) - (1/2)gt²。",
            "Cycloid: x = r(t - sin(t)), y = r(1 - cos(t)).":
                "摆线：x = r(t - sin(t))，y = r(1 - cos(t))。",
            "Line segment: x = x₁ + t(x₂-x₁), y = y₁ + t(y₂-y₁), 0≤t≤1.":
                "线段：x = x₁ + t(x₂-x₁)，y = y₁ + t(y₂-y₁)，0≤t≤1。",
            "Derivative: dy/dx = (dy/dt)/(dx/dt).":
                "导数：dy/dx = (dy/dt)/(dx/dt)。",
            "Slope at t: Find dy/dx by using parametric derivative formula.":
                "t处斜率：使用参数导数公式求dy/dx。",
            "Arc length: L = ∫√((dx/dt)² + (dy/dt)²) dt.":
                "弧长：L = ∫√((dx/dt)² + (dy/dt)²) dt。",
        }
        return mapping
    
    def create_batch_28_conic_transformations(self):
        """BATCH 28: Conic section transformations and rotations"""
        mapping = {
            "Standard position: Axes aligned with coordinate axes.":
                "标准位置：轴与坐标轴对齐。",
            "Translated conic: (x-h)²/a² ± (y-k)²/b² = 1.":
                "平移圆锥：(x-h)²/a² ± (y-k)²/b² = 1。",
            "Rotation of axes: x = x' cos(θ) - y' sin(θ).":
                "轴旋转：x = x' cos(θ) - y' sin(θ)。",
            "Eliminate xy term: Rotate by angle θ = (1/2)arctan(B/(A-C)).":
                "消去xy项：旋转角度θ = (1/2)arctan(B/(A-C))。",
            "Eccentricity for ellipse: 0 < e < 1, e = c/a.":
                "椭圆离心率：0 < e < 1，e = c/a。",
            "Eccentricity for hyperbola: e > 1, e = c/a.":
                "双曲线离心率：e > 1，e = c/a。",
            "Eccentricity for parabola: e = 1.":
                "抛物线离心率：e = 1。",
            "Focus-directrix definition: e = distance to focus / distance to directrix.":
                "焦点-准线定义：e =焦点距离/准线距离。",
        }
        return mapping
    
    def create_batch_29_advanced_factoring(self):
        """BATCH 29: Advanced factoring techniques"""
        mapping = {
            "Factor by grouping: Group and find common factors.":
                "分组因式分解：分组并找到公因数。",
            "Difference of squares: a² - b² = (a-b)(a+b).":
                "平方差：a² - b² = (a-b)(a+b)。",
            "Sum of cubes: a³ + b³ = (a+b)(a² - ab + b²).":
                "立方和：a³ + b³ = (a+b)(a² - ab + b²)。",
            "Difference of cubes: a³ - b³ = (a-b)(a² + ab + b²).":
                "立方差：a³ - b³ = (a-b)(a² + ab + b²)。",
            "Perfect square trinomial: a² + 2ab + b² = (a+b)².":
                "完全平方三项式：a² + 2ab + b² = (a+b)²。",
            "AC method: Find factors of AC that add to B.":
                "AC法：找AC的因数，相加等于B。",
            "Rational root test: Possible roots = ±(factors of c)/(factors of a).":
                "有理根定理：可能的根= ±(c的因数)/(a的因数)。",
            "Upper/lower bound: If synthetic division shows all positive/negative, bound found.":
                "上/下界：如果综合除法显示全正/全负，找到界。",
        }
        return mapping
    
    def create_batch_30_convergence_and_limits(self):
        """BATCH 30: Convergence, limits, and asymptotic behavior"""
        mapping = {
            "Limit exists: Function approaches specific value as x approaches point.":
                "极限存在：当x接近点时，函数接近特定值。",
            "Limit notation: lim(x→a) f(x) = L means for any ε > 0, ∃δ > 0.":
                "极限记号：lim(x→a) f(x) = L表示对任何ε > 0，∃δ > 0。",
            "Infinite limit: lim(x→a) f(x) = ∞ means function grows unbounded.":
                "无穷极限：lim(x→a) f(x) = ∞表示函数无限增长。",
            "Limit at infinity: lim(x→∞) f(x) = L means horizontal asymptote y = L.":
                "无穷处的极限：lim(x→∞) f(x) = L表示水平渐近线y = L。",
            "Convergent sequence: Approaches single limit value.":
                "收敛数列：接近单个极限值。",
            "Divergent sequence: Does not approach limit or oscillates.":
                "发散数列：不接近极限或振荡。",
            "Absolute convergence: Σ|aₙ| converges.":
                "绝对收敛：Σ|aₙ|收敛。",
            "Conditional convergence: Σaₙ converges but Σ|aₙ| diverges.":
                "条件收敛：Σaₙ收敛但Σ|aₙ|发散。",
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
        """Add batch translations to file"""
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
        """Execute batches 16-30"""
        print("=" * 80)
        print("ALGEBRA 2 EXTENDED BATCH TRANSLATION SYSTEM - BATCHES 16-30")
        print("=" * 80)
        print()
        
        batches = [
            ("Batch 16: Function Analysis (8 items)", self.create_batch_16_function_analysis()),
            ("Batch 17: Transformation Patterns (10 items)", self.create_batch_17_transformation_patterns()),
            ("Batch 18: Rational Function Details (8 items)", self.create_batch_18_rational_function_details()),
            ("Batch 19: Exponential Growth/Decay (8 items)", self.create_batch_19_exponential_growth_decay()),
            ("Batch 20: Logarithmic Equations (8 items)", self.create_batch_20_logarithmic_equations()),
            ("Batch 21: Trigonometric Identities (8 items)", self.create_batch_21_trigonometric_identities_solutions()),
            ("Batch 22: Unit Circle Solutions (8 items)", self.create_batch_22_unit_circle_solutions()),
            ("Batch 23: System Solving Methods (8 items)", self.create_batch_23_system_solving_methods()),
            ("Batch 24: Combination/Permutation (8 items)", self.create_batch_24_combination_permutation()),
            ("Batch 25: Polar Coordinates (8 items)", self.create_batch_25_polar_coordinates()),
            ("Batch 26: Vector Operations (8 items)", self.create_batch_26_vector_operations()),
            ("Batch 27: Parametric Equations (8 items)", self.create_batch_27_parametric_equations()),
            ("Batch 28: Conic Transformations (8 items)", self.create_batch_28_conic_transformations()),
            ("Batch 29: Advanced Factoring (8 items)", self.create_batch_29_advanced_factoring()),
            ("Batch 30: Convergence & Limits (8 items)", self.create_batch_30_convergence_and_limits()),
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
        print(f"TOTAL TRANSLATIONS ADDED (BATCHES 16-30): {total_added}")
        print("=" * 80)
        
        return total_added

if __name__ == '__main__':
    engine = ExtendedBatchTranslationEngine()
    engine.run_all_batches()
