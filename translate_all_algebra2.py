#!/usr/bin/env python3
"""
Translate ALL missing Algebra 2 strings to Chinese.
Handles: quiz questions, test questions, lesson titles, summary text,
video labels, and math expression labels.
"""
import json, re

with open("/workspaces/ArisEdu/algebra2_all_missing.json", "r", encoding="utf-8") as f:
    missing = json.load(f)

print(f"Total missing strings to translate: {len(missing)}")

# ═══════════════════════════════════════════════════════════════════════
# COMPREHENSIVE WORD / PHRASE DICTIONARY
# ═══════════════════════════════════════════════════════════════════════

# Longer phrases first for proper replacement order
phrase_dict = {
    # ── General / UI ──
    "Submit Answer": "提交答案",
    "Try Again": "重试",
    "View other videos": "查看其他视频",
    "Next Up: Summary": "下一步：总结",
    "Next Up: Practice": "下一步：练习",
    "Next Up: Quiz": "下一步：测验",
    "videos": "视频",
    "Rubric": "评分标准",
    "TBD": "待定",
    
    # ── Lesson titles / topic phrases ──
    "Review of Functions & Notation": "函数与符号复习",
    "Advanced Linear Applications": "高级线性应用",
    "Quadratic Inequalities": "二次不等式",
    "Higher-Degree Polynomials": "高次多项式",
    "Applications of Rational Functions": "有理函数的应用",
    "Natural Logarithms & e": "自然对数与e",
    "Applications & Mathematical Induction": "应用与数学归纳法",
    "Mathematical Induction": "数学归纳法",
    "Correlation & Linear Regression": "相关性与线性回归",
    "Linear Regression": "线性回归",
    "Applications of Trigonometry": "三角学的应用",
    "Trigonometric Identities": "三角恒等式",
    "Trigonometric Equations": "三角方程",
    "Trigonometric Functions": "三角函数",
    "Trigonometry": "三角学",
    "Conic Sections": "圆锥曲线",
    "Sequences and Series": "数列与级数",
    "Sequences & Series": "数列与级数",
    "Probability & Statistics": "概率与统计",
    "Probability": "概率",
    "Statistics": "统计",
    "Systems of Equations": "方程组",
    "Linear Programming": "线性规划",
    "Rational Expressions": "有理表达式",
    "Rational Functions": "有理函数",
    "Exponential Functions": "指数函数",
    "Logarithmic Functions": "对数函数",
    "Polynomial Functions": "多项式函数",
    "Quadratic Functions": "二次函数",
    "Linear Functions": "线性函数",
    "Inverse Functions": "反函数",
    "Composite Functions": "复合函数",
    "Piecewise Functions": "分段函数",
    "Parent Functions": "基本函数",
    "Domain and Range": "定义域与值域",
    "Function Notation": "函数符号",
    "Function Transformations": "函数变换",
    "Arithmetic Sequences": "等差数列",
    "Geometric Sequences": "等比数列",
    "Parametric Equations": "参数方程",
    "Polar Coordinates": "极坐标",
    "Complex Numbers": "复数",
    "Matrices": "矩阵",
    "Determinants": "行列式",

    # ── Math vocabulary (longer phrases first) ──
    "no horizontal asymptote": "无水平渐近线",
    "horizontal asymptote": "水平渐近线",
    "vertical asymptote": "垂直渐近线",
    "oblique asymptote": "斜渐近线",
    "removable discontinuity": "可去间断点",
    "point discontinuity": "点间断点",
    "standard position": "标准位置",
    "linear programming": "线性规划",
    "objective function": "目标函数",
    "constraint": "约束条件",
    "feasible region": "可行域",
    "Henderson-Hasselbalch equation": "亨德森-哈塞尔巴尔赫方程",
    "best fits": "最佳拟合",
    "line of best fit": "最佳拟合线",
    "linear reg line": "线性回归线",
    "linear regression": "线性回归",
    "correlation coefficient": "相关系数",
    "strong positive": "强正相关",
    "strong negative": "强负相关",
    "no correlation": "无相关性",
    "scatter plot": "散点图",
    "residual": "残差",
    "half-life model": "半衰期模型",
    "half-life": "半衰期",
    "exponential growth": "指数增长",
    "exponential decay": "指数衰减",
    "compound interest": "复利",
    "continuously compounded": "连续复利",
    "continuous compounding": "连续复利",
    "binomial probability": "二项概率",
    "binomial expansion": "二项展开",
    "binomial theorem": "二项式定理",
    "Pascal's Triangle": "帕斯卡三角",
    "normal distribution": "正态分布",
    "standard deviation": "标准差",
    "margin of error": "误差范围",
    "margin error": "误差范围",
    "confidence interval": "置信区间",
    "sample size": "样本量",
    "population": "总体",
    "sample": "样本",
    "z-score": "z分数",
    "Law of Sines": "正弦定律",
    "Law of Cosines": "余弦定律",
    "law of sines": "正弦定律",
    "law of cosines": "余弦定律",
    "unit circle": "单位圆",
    "reference angle": "参考角",
    "coterminal angle": "同终边角",
    "radian measure": "弧度制",
    "degree measure": "角度制",
    "amplitude": "振幅",
    "angular speed": "角速度",
    "linear speed": "线速度",
    "angular velocity": "角速度",
    "arc length": "弧长",
    "sector area": "扇形面积",
    "phase shift": "相移",
    "vertical shift": "垂直平移",
    "period": "周期",
    "frequency": "频率",
    "midline": "中线",
    "ambiguous case": "模糊情况",
    "oblique triangle": "斜三角形",
    "right triangle": "直角三角形",
    "Heron's formula": "海伦公式",
    "completing the square": "配方法",
    "complete the square": "配方",
    "quadratic formula": "求根公式",
    "discriminant": "判别式",
    "vertex form": "顶点式",
    "standard form": "标准式",
    "factored form": "因式分解式",
    "intercept form": "截距式",
    "point-slope form": "点斜式",
    "slope-intercept form": "斜截式",
    "axis of symmetry": "对称轴",
    "end behavior": "末端行为",
    "leading coefficient": "首项系数",
    "turning point": "转折点",
    "multiplicity": "重数",
    "synthetic division": "综合除法",
    "long division": "长除法",
    "polynomial division": "多项式除法",
    "Remainder Theorem": "余数定理",
    "remainder theorem": "余数定理",
    "Factor Theorem": "因式定理",
    "Rational Root Theorem": "有理根定理",
    "Descartes' Rule": "笛卡尔法则",
    "Fundamental Theorem of Algebra": "代数基本定理",
    "complex conjugate": "共轭复数",
    "imaginary unit": "虚数单位",
    "sum of cubes": "立方和",
    "difference of cubes": "立方差",
    "difference of squares": "平方差",
    "perfect square trinomial": "完全平方三项式",
    "common factor": "公因式",
    "greatest common factor": "最大公因式",
    "least common denominator": "最小公分母",
    "least common multiple": "最小公倍数",
    "extraneous solution": "增根",
    "partial fractions": "部分分式",
    "partial fraction": "部分分式",
    "cross multiply": "交叉相乘",
    "cross-multiply": "交叉相乘",
    "direct variation": "正比例",
    "inverse variation": "反比例",
    "joint variation": "联合变化",
    "combined variation": "复合变化",
    "hole in graph": "图形中的洞",
    "slant asymptote": "斜渐近线",
    "change of base": "换底公式",
    "change-of-base": "换底公式",
    "one-to-one": "一对一",
    "common logarithm": "常用对数",
    "natural logarithm": "自然对数",
    "power rule": "幂法则",
    "product rule": "乘法法则",
    "quotient rule": "商法则",
    "logarithm": "对数",
    "logarithms": "对数",
    "exponential": "指数",
    "inverse": "反",
    "composition": "复合",
    "transformation": "变换",
    "translation": "平移",
    "reflection": "反射",
    "dilation": "缩放",
    "rotation": "旋转",
    "even function": "偶函数",
    "odd function": "奇函数",
    "neither": "两者都不是",
    "continuous": "连续的",
    "discontinuous": "不连续的",
    "increasing": "递增",
    "decreasing": "递减",
    "bounded": "有界",
    "unbounded": "无界",
    "absolute maximum": "绝对最大值",
    "absolute minimum": "绝对最小值",
    "relative maximum": "相对最大值",
    "relative minimum": "相对最小值",
    "local maximum": "局部最大值",
    "local minimum": "局部最小值",
    "maximum": "最大值",
    "minimum": "最小值",
    "zeros": "零点",
    "roots": "根",
    "x-intercept": "x截距",
    "y-intercept": "y截距",
    "intercept": "截距",
    "asymptote": "渐近线",
    "domain": "定义域",
    "range": "值域",
    "interval": "区间",
    "interval notation": "区间表示法",
    "set notation": "集合表示法",
    "inequality": "不等式",
    "system": "方程组",
    "matrix": "矩阵",
    "determinant": "行列式",
    "series": "级数",
    "sequence": "数列",
    "arithmetic": "等差",
    "geometric": "等比",
    "convergent": "收敛",
    "divergent": "发散",
    "infinite series": "无穷级数",
    "finite series": "有限级数",
    "partial sum": "部分和",
    "sigma notation": "求和符号",
    "summation": "求和",
    "recursive": "递归",
    "explicit": "显式",
    "common ratio": "公比",
    "common difference": "公差",
    "term": "项",
    "permutation": "排列",
    "combination": "组合",
    "factorial": "阶乘",
    "independent events": "独立事件",
    "dependent events": "相关事件",
    "mutually exclusive": "互斥",
    "complementary": "互补的",
    "supplementary": "互余的",
    "conditional probability": "条件概率",
    "expected value": "期望值",
    "variance": "方差",
    "mean": "均值",
    "median": "中位数",
    "mode": "众数",
    "quartile": "四分位数",
    "percentile": "百分位数",
    "outlier": "异常值",
    "box plot": "箱线图",
    "histogram": "直方图",
    "stem-and-leaf": "茎叶图",
    "circle": "圆",
    "ellipse": "椭圆",
    "parabola": "抛物线",
    "hyperbola": "双曲线",
    "conic": "圆锥曲线",
    "focus": "焦点",
    "foci": "焦点",
    "directrix": "准线",
    "eccentricity": "离心率",
    "major axis": "长轴",
    "minor axis": "短轴",
    "semi-major": "半长轴",
    "semi-minor": "半短轴",
    "center": "中心",
    "radius": "半径",
    "diameter": "直径",
    "tangent line": "切线",
    "secant line": "割线",
    "normal line": "法线",
    "perpendicular": "垂直",
    "parallel": "平行",
    "intersect": "相交",
    "collinear": "共线",
    "midpoint": "中点",
    "distance formula": "距离公式",
    "midpoint formula": "中点公式",
    "parametric": "参数",
    "parameter": "参数",
    "eliminate": "消去",
    "elimination": "消元法",
    "substitution": "代入法",
    "substitute": "代入",
    "graphing": "图形法",
    "solve by elimination": "用消元法求解",
    "solve by substitution": "用代入法求解",
    "solve by graphing": "用图形法求解",
    
    # ── Question words / phrases ──
    "Question about": "关于…的问题",
    "What is the": "什么是",
    "What is": "什么是",
    "Which represents": "哪个表示",
    "Which step": "哪个步骤",
    "Which": "哪个",
    "Find the": "求",
    "Find": "求",
    "Evaluate": "求值",
    "Solve": "求解",
    "Graph": "图形",
    "Convert": "转换",
    "Simplify": "化简",
    "Factor": "因式分解",
    "Expand": "展开",
    "Divide": "除",
    "Multiply": "乘",
    "Add": "加",
    "Subtract": "减",
    "Combine": "合并",
    "Complete": "完成",
    "Classify": "分类",
    "Identify": "识别",
    "Determine": "确定",
    "Express": "表示",
    "Describe": "描述",
    "Explain": "解释",
    "Compare": "比较",
    "Prove": "证明",
    "Verify": "验证",
    "Show that": "证明",
    "How many": "多少",
    "How long": "多长时间",
    "How far": "多远",
    "How fast": "多快",
    "How much": "多少",

    # ── Common answer/option words ──
    "all real numbers": "所有实数",
    "all real x": "所有实数x",
    "no solution": "无解",
    "no real solution": "无实数解",
    "infinitely many solutions": "无穷多解",
    "infinite solutions": "无穷多解",
    "one solution": "一个解",
    "two solutions": "两个解",
    "unique solution": "唯一解",
    "consistent": "一致的",
    "inconsistent": "不一致的",
    "dependent": "相关的",
    "independent": "独立的",
    "positive": "正",
    "negative": "负",
    "undefined": "未定义",
    "does not exist": "不存在",
    "true": "真",
    "false": "假",
    "always": "总是",
    "sometimes": "有时",
    "never": "从不",
    "identity": "恒等式",
    "equation": "方程",
    "expression": "表达式",
    "function": "函数",
    "relation": "关系",
    "slope": "斜率",
    "rate": "速率",
    "speed": "速度",
    "time": "时间",
    "distance": "距离",
    "height": "高度",
    "width": "宽度",
    "length": "长度",
    "area": "面积",
    "volume": "体积",
    "perimeter": "周长",
    "circumference": "圆周",
    "angle": "角",
    "degree": "度",
    "radian": "弧度",
    "radians": "弧度",
    "degrees": "度",
    
    # ── Work/rate/mixture problem words ──
    "per day": "每天",
    "per hour": "每小时",
    "per minute": "每分钟",
    "mph": "英里/小时",
    "downstream": "顺流",
    "upstream": "逆流",
    "current": "水流",
    "boat": "船",
    "train": "火车",
    "worker": "工人",
    "workers": "工人",
    "combined": "合计",
    "together": "一起",
    "alone": "独自",
    "fills": "填满",
    "pool": "游泳池",
    "tank": "水箱",
    "pipe": "管道",
    "job": "工作",
    "profit": "利润",
    "cost": "成本",
    "revenue": "收入",
    "interest": "利息",
    "principal": "本金",
    "total": "总计",
    "annually": "每年",
    "quarterly": "每季度",
    "monthly": "每月",
    "years": "年",
    "coins": "硬币",
    "quarters": "25美分硬币",
    "dimes": "10美分硬币",
    "nickels": "5美分硬币",
    "pennies": "1美分硬币",
    "age": "年龄",
    "mixture": "混合物",
    "solution": "解/溶液",
    "concentration": "浓度",
    "grow": "增长",
    "decay": "衰减",
    "double": "翻倍",
    "triple": "三倍",
    "after": "之后",
    "before": "之前",
    "remaining": "剩余",
    
    # ── Trig-specific ──
    "sin": "sin",
    "cos": "cos",
    "tan": "tan",
    "csc": "csc",
    "sec": "sec",
    "cot": "cot",
    "arcsin": "arcsin",
    "arccos": "arccos",
    "arctan": "arctan",
    
    # ── Direction / position words ──
    "translate": "平移",
    "Standard position": "标准位置",
    "opening up": "开口朝上",
    "opening down": "开口朝下",
    "opening left": "开口朝左",
    "opening right": "开口朝右",
    "vertical line": "垂直线",
    "horizontal line": "水平线",
    "comes first in": "首先进行",
    "subject to": "满足条件",
    "in terms of": "用…表示",
    "same line": "同一直线",
    "Perpendicular to": "垂直于",
    "has slope": "斜率为",
    "through": "经过",
    "between": "之间",
    "from": "从",
    "to": "到",
    
    # ── Connectors ──
    "and": "和",
    "or": "或",
    "then": "那么",
}

# For full-sentence / pattern-based translations
sentence_translations = {
    # Lesson titles
    "Lesson 1.9: Advanced Linear Applications": "课程 1.9：高级线性应用",
    "Lesson 2.7: Quadratic Inequalities": "课程 2.7：二次不等式",
    "Lesson 3.7: Higher-Degree Polynomials": "课程 3.7：高次多项式",
    "Lesson 4.6: Applications of Rational Functions": "课程 4.6：有理函数的应用",
    "Lesson 5.7: Natural Logarithms & e": "课程 5.7：自然对数与e",
    "Lesson 6.5: Applications & Mathematical Induction": "课程 6.5：应用与数学归纳法",
    "Lesson 7.7: Correlation & Linear Regression": "课程 7.7：相关性与线性回归",
    "Lesson 8.6: Applications of Trigonometry": "课程 8.6：三角学的应用",
    
    # Video panel labels
    "Lesson 1.8 videos": "课程 1.8 视频",
    "Lesson 1.9 videos": "课程 1.9 视频",
    "Lesson 8.5 videos": "课程 8.5 视频",
    "Lesson 8.6 videos": "课程 8.6 视频",
    "Lesson 9.7 videos": "课程 9.7 视频",
}

# ────────────────────────────────────────────────────────────────────────
# Build FULL quiz/test question translations
# These are specific numbered questions and answers
# ────────────────────────────────────────────────────────────────────────
quiz_translations = {
    # ── Unit 1: Functions ──
    "1. If f(x) = 2x + 3, find f(-2)": "1. 若 f(x) = 2x + 3，求 f(-2)",
    "2. What is the domain of f(x) = √(x - 4)?": "2. f(x) = √(x - 4) 的定义域是什么？",
    "3. Which represents a function?": "3. 哪个表示函数？",
    "4. If f(x) = x², find f(3) + f(−3)": "4. 若 f(x) = x²，求 f(3) + f(−3)",
    "5. What is (f ∘ g)(x) if f(x) = x + 1 and g(x) = 2x?": "5. 若 f(x) = x + 1 且 g(x) = 2x，(f ∘ g)(x) 是什么？",
    "6. Is f(x) = 3x² even, odd, or neither?": "6. f(x) = 3x² 是偶函数、奇函数还是两者都不是？",
    "7. Piecewise: f(x)={2x if x<0, x² if x≥0}. f(−1)?": "7. 分段函数：f(x)={2x 若 x<0, x² 若 x≥0}。f(−1)?",
    "circle": "圆",
    "parabola opening left": "开口朝左的抛物线",
    "parabola opening up": "开口朝上的抛物线",
    "vertical line": "垂直线",
    "even": "偶函数",
    "odd": "奇函数",
    "even, odd, or neither": "偶函数、奇函数还是两者都不是",
    
    # ── Unit 1 Lesson topics ──
    "1. Find slope between (2, 5) and (4, 11)": "1. 求 (2, 5) 和 (4, 11) 之间的斜率",
    "2. What is the y-intercept of 2x + 3y = 6?": "2. 2x + 3y = 6 的y截距是什么？",
    "3. Point-slope form through (1, 2) slope 3?": "3. 经过 (1, 2) 斜率为 3 的点斜式？",
    "4. Perpendicular to y = 2x + 1 has slope?": "4. 垂直于 y = 2x + 1 的斜率是？",
    "5. Equation through (1, 3) with slope 4?": "5. 经过 (1, 3) 斜率为 4 的方程？",
    "6. Parallel to y = −x + 5 through (2, 1)?": "6. 平行于 y = −x + 5 经过 (2, 1)？",
    "7. Midpoint of (1,3) and (5,7)?": "7. (1,3) 和 (5,7) 的中点？",
    "8. Find slope between (2, 5) and (4, 11)": "8. 求 (2, 5) 和 (4, 11) 之间的斜率",
    "9. What is the y-intercept of 2x + 3y = 6?": "9. 2x + 3y = 6 的y截距是什么？",
    "10. Point-slope through (1,2) slope 3?": "10. 经过 (1,2) 斜率为 3 的点斜式？",
    "11. Perpendicular to y = 2x + 1 has slope?": "11. 垂直于 y = 2x + 1 的斜率是？",
    "12. Equation through (1, 3) with slope 4?": "12. 经过 (1, 3) 斜率为 4 的方程？",
    "13. Distance between (1,2) and (4,6)?": "13. (1,2) 和 (4,6) 之间的距离？",
    "14. Line y = 2x + b through (3, 10). b = ?": "14. 直线 y = 2x + b 经过 (3, 10)。b = ？",
    
    # ── Systems of Equations (Unit 1.9) ──
    "1. Solve by elimination: 2x + y = 5 and x − y = 1": "1. 用消元法求解：2x + y = 5 且 x − y = 1",
    "2. From y = 3x − 1, substitute into 2x + y = 5": "2. 将 y = 3x − 1 代入 2x + y = 5",
    "3. System: x + y = 7, x − y = 3. Solve.": "3. 方程组：x + y = 7, x − y = 3。求解。",
    "4. Express x in terms of y from 2x + 3y = 6": "4. 从 2x + 3y = 6 用 y 表示 x",
    "5. Solve by graphing: y = −x + 2 and y = x": "5. 用图形法求解：y = −x + 2 且 y = x",
    "6. Which step comes first in substitution?": "6. 代入法中哪个步骤先进行？",
    "7. Two equations, same line = ? solutions": "7. 两个方程，同一直线 = ？个解",
    "8. No intersection means ? solutions": "8. 没有交点意味着？个解",
    "9. Add equations: x + y = 5 and x − y = 3": "9. 方程相加：x + y = 5 且 x − y = 3",
    "5. Add equations: x + y = 5 and x − y = 3": "5. 方程相加：x + y = 5 且 x − y = 3",
    "6. Two equations, same line = ? solutions": "6. 两个方程，同一直线 = ？个解",
    "7. No intersection means ? solutions": "7. 没有交点意味着？个解",
    "15. System: x + y = 7, x − y = 3. Solve.": "15. 方程组：x + y = 7, x − y = 3。求解。",
    "16. Classify: x + y = 3 and 2x + 2y = 6": "16. 分类：x + y = 3 和 2x + 2y = 6",
    "17. Classify: x + y = 3 and x + y = 5": "17. 分类：x + y = 3 和 x + y = 5",
    "18. Solve by substitution: y = x+1, x+y = 5": "18. 用代入法求解：y = x+1, x+y = 5",
    "19. Solve by graphing: y = −x + 2 and y = x": "19. 用图形法求解：y = −x + 2 且 y = x",
    "20. Two equations, same line = ? solutions": "20. 两个方程，同一直线 = ？个解",
    "21. If 2x+y=5 and x−y=1, find x": "21. 若 2x+y=5 且 x−y=1，求 x",
    "22. Solution type: x+y=3 and x+y=5": "22. 解的类型：x+y=3 和 x+y=5",
    "23. From y = 3x − 1, substitute into 2x + y = 5": "23. 将 y = 3x − 1 代入 2x + y = 5",
    "24. System: x + y = 10, x − y = 2. Solve.": "24. 方程组：x + y = 10, x − y = 2。求解。",
    "25. Express x in terms of y from 2x + 3y = 6": "25. 从 2x + 3y = 6 用 y 表示 x",
    "26. Add: 3x + 2y = 7 and −3x + y = 2": "26. 相加：3x + 2y = 7 和 −3x + y = 2",
    "27. Which step comes first in substitution?": "27. 代入法中哪个步骤先进行？",
    
    # ── Word problems ──
    "1. Work: A does 1/5, B does 1/4 per day. Combined?": "1. 工作：A每天做1/5，B每天做1/4。合计？",
    "2. Profit P(x) = −2x² + 100x − 1000. Max?": "2. 利润 P(x) = −2x² + 100x − 1000。最大值？",
    "3. Speed ratio 60 mph vs 40 mph, 30 mi. Time diff?": "3. 速度比 60英里/时 vs 40英里/时，30英里。时间差？",
    "4. $5000 at 6% and 8%, total interest $380. At 8%?": "4. $5000分别以6%和8%投资，总利息$380。8%投资多少？",
    "5. Pool A fills in 5 hrs, B in 3 hrs. Combined?": "5. 泳池A需5小时填满，B需3小时。合计？",
    "6. 25 coins (quarters/dimes), $5.05 total. Quarters?": "6. 25枚硬币（25美分和10美分），共$5.05。25美分多少枚？",
    "7. Boat 20 mph, current 5 mph, 100 mi downstream. Time?": "7. 船速20英里/时，水流5英里/时，顺流100英里。时间？",
    "5. Two workers complete 1 job: x days A, y days B": "5. 两个工人完成一项工作：A用x天，B用y天",
    "3. Trains 50&60 mph apart, when 275 apart?": "3. 火车速度50和60英里/时，何时相距275英里？",
    "2. Age: A = 3B, in 10 years A = 2B. Current A?": "2. 年龄：A = 3B，10年后A = 2B。目前A多大？",
    "6. Population 1000, grow 5% annually. After?": "6. 人口1000，年增长5%。之后？",
    "2. Multiply first equation by what: x + 2y = 7 and 3x − y = 4": "2. 第一个方程乘以什么：x + 2y = 7 和 3x − y = 4",
    "6. Multiply second by −1 then add eliminates x: 2x + y = 3 and 2x − 3y = 7": "6. 第二个方程乘以−1再相加消去x：2x + y = 3 和 2x − 3y = 7",
    
    # ── Quadratic ──
    "1. Factor x² + 5x + 6": "1. 因式分解 x² + 5x + 6",
    "1. Complete: x² + 6x + ?": "1. 配方：x² + 6x + ?",
    "1. Height h(t) = −16t² + 80t + 5. Max?": "1. 高度 h(t) = −16t² + 80t + 5。最大值？",
    
    # ── Polynomial Division ──
    "1. Divide x³−6x²+11x−6 by x−1": "1. 将 x³−6x²+11x−6 除以 x−1",
    
    # ── Exponential/Log ──
    "1. Evaluate f(x)=2^x at x=3": "1. 求 f(x)=2^x 在 x=3 时的值",
    "1. Half-life model M(t)=500(0.5)^(t/10)": "1. 半衰期模型 M(t)=500(0.5)^(t/10)",
    "1. Question about Natural Logarithms & e?": "1. 关于自然对数与e的问题？",
    
    # ── Sequences/Series ──
    "1. Find 5th term: 2, 5, 8, 11, ...": "1. 求第5项：2, 5, 8, 11, ...",
    "1. Geometric: 1, 2, 4, 8. Ratio r = ?": "1. 等比数列：1, 2, 4, 8。公比 r = ?",
    
    # ── Conics ──
    "1. Conic x²/4 + y²/9 = 1": "1. 圆锥曲线 x²/4 + y²/9 = 1",
    "1. Circle center (2,3), r=5 equation": "1. 圆心 (2,3)，r=5 的方程",
    "3. Center/radius from x² + y² − 6x + 8y = 0": "3. 从 x² + y² − 6x + 8y = 0 求圆心和半径",
    
    # ── Trig ──
    "1. Convert 120° to radians": "1. 将 120° 转换为弧度",
    "1. Graph y = sin x period": "1. y = sin x 的周期图",
    "1. Law of Sines a/sin A = ?": "1. 正弦定律 a/sin A = ?",
    
    # ── Stats ──
    "1. Linear reg line best fits": "1. 线性回归线最佳拟合",
    "1. Margin error E = ?": "1. 误差范围 E = ?",
    "1. Binomial P(X=k) = ?": "1. 二项概率 P(X=k) = ?",
    
    # ── Parametric ──
    "1. Parametric x = 3t, y = t², eliminate t": "1. 参数方程 x = 3t, y = t²，消去 t",
    "15. Parametric x = 3t, y = t², eliminate t": "15. 参数方程 x = 3t, y = t²，消去 t",
    
    # ── Linear Programming ──
    "1. Max P = 2x + 3y subject to x≥0, y≥0, x+y≤5": "1. 最大化 P = 2x + 3y 满足 x≥0, y≥0, x+y≤5",
    "4. Linear programming objective example": "4. 线性规划目标函数示例",
    "1. Question about Applications & Mathematical Induction?": "1. 关于应用与数学归纳法的问题？",
    
    # ── Rational functions ──
    "1. Asymptote of (2x+1)/(x−3)": "1. (2x+1)/(x−3) 的渐近线",
    "1. Combine (x+1)/(x²−4) + 3/(x−2)": "1. 合并 (x+1)/(x²−4) + 3/(x−2)",
    "1. Inequality 1/x > 0 solution?": "1. 不等式 1/x > 0 的解？",
    "2. Vertical asymptote f(x)=(x+1)/(x²−9)": "2. f(x)=(x+1)/(x²−9) 的垂直渐近线",
    "3. Horizontal asymptote (3x²−1)/(2x²+5)": "3. (3x²−1)/(2x²+5) 的水平渐近线",
    "7. Removable discontinuity (x²−1)/(x−1)": "7. (x²−1)/(x−1) 的可去间断点",
    "10. Horizontal asymptote (3x²−1)/(2x²+5)": "10. (3x²−1)/(2x²+5) 的水平渐近线",
    "14. Removable discontinuity (x²−1)/(x−1)": "14. (x²−1)/(x−1) 的可去间断点",
    "14. Standard position (h,k) → translate": "14. 标准位置 (h,k) → 平移",
    
    # ── Common answer options ──
    "isolate a variable": "分离一个变量",
    "Isolate a variable": "分离一个变量",
    "solve for x": "求解x",
    "solve for y": "求解y",
    "eliminate a variable": "消去一个变量",
    "graph both lines": "画出两条线",
    "multiply equations": "方程相乘",
    "add equations": "方程相加",
    "subtract equations": "方程相减",
    "one unique solution": "一个唯一解",
    "no solutions": "无解",
    "infinite": "无穷",
    "exactly one": "恰好一个",
    "exactly two": "恰好两个",
    "consistent and independent": "一致且独立",
    "consistent and dependent": "一致且相关",
    "inconsistent": "不一致",
    
    # ── Summary content ──
    "denominator degree: no horizontal asymptote.": "分母次数：无水平渐近线。",
    "b (two rays), or a": "b（两条射线），或a",
    "c) = 1 - P(X ≤ c).": "c) = 1 - P(X ≤ c)。",
    "7 is basic. Henderson-Hasselbalch equation uses logarithms.": "7是碱性的。亨德森-哈塞尔巴尔赫方程使用对数。",

    # ── Misc answer choices ──
    "$1500": "$1500",
    "$2000": "$2000",
    "$2500": "$2500",
    "$3000": "$3000",
    "0.5 hrs": "0.5 小时",
    "0.75 hrs": "0.75 小时",
    "1 hr": "1 小时",
    "0 to 1": "0 到 1",
    "0 to 4": "0 到 4",
    "0 to 100": "0 到 100",
    "1 to ∞": "1 到 ∞",
    "0, 1, or 2 solns": "0、1或2个解",
    "1 or 2": "1 或 2",
    "1, 3, or 5": "1、3或5",
}


def translate_string(text):
    """Translate a string using dictionary + pattern-based approach."""
    
    # 1. Check exact matches first
    if text in sentence_translations:
        return sentence_translations[text]
    if text in quiz_translations:
        return quiz_translations[text]
    
    # 2. Check if it's pure math (no translatable English)
    if not re.search(r'[a-zA-Z]{2,}', text):
        # Pure math/numbers - keep as is (still add to translations for completeness)
        return text
    
    # 3. Pattern-based translation for numbered questions
    # Match "N. <question text>"
    m = re.match(r'^(\d+)\.\s+(.+)$', text, re.DOTALL)
    if m:
        num = m.group(1)
        body = m.group(2)
        translated_body = translate_body(body)
        if translated_body != body:
            return f"{num}. {translated_body}"
    
    # 4. General phrase replacement
    result = translate_body(text)
    return result


def translate_body(text):
    """Translate the body of a string using phrase dictionary."""
    result = text
    
    # Sort phrases by length (longest first) to avoid partial replacements
    sorted_phrases = sorted(phrase_dict.items(), key=lambda x: len(x[0]), reverse=True)
    
    for eng, chn in sorted_phrases:
        # Use word boundary matching for short words to avoid partial matches
        if len(eng) <= 3:
            pattern = r'\b' + re.escape(eng) + r'\b'
        else:
            pattern = re.escape(eng)
        
        result = re.sub(pattern, chn, result, flags=re.IGNORECASE)
    
    return result


# ═══════════════════════════════════════════════════════════════════════
# Process all missing strings
# ═══════════════════════════════════════════════════════════════════════
translations = {}
unchanged = []

for text in missing:
    translated = translate_string(text)
    translations[text] = translated
    if translated == text and re.search(r'[a-zA-Z]{3,}', text):
        unchanged.append(text)

print(f"\nTranslated: {len(translations)}")
print(f"Unchanged (still has English 3+ letters): {len(unchanged)}")

if unchanged:
    print("\n=== Still untranslated (first 30) ===")
    for s in sorted(unchanged, key=len, reverse=True)[:30]:
        print(f"  [{len(s):>4}] {s[:150]}")

# Save
with open("/workspaces/ArisEdu/algebra2_full_translations.json", "w", encoding="utf-8") as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\nSaved to algebra2_full_translations.json")
