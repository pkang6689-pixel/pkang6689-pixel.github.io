#!/usr/bin/env python3
"""Add quiz questions to Algebra 2 lessons (→20 each). Units 1-5."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "algebra_2_lessons.json")

def mq(qt, opts, exp):
    options = []
    for o in opts:
        c = o.startswith("*")
        options.append({"text": o.lstrip("*"), "is_correct": c, "data_i18n": None})
    return {"question_number": 0, "question_text": qt, "attempted": 2,
            "data_i18n": None, "options": options, "explanation": exp}

EXTRA = {}

# ── U1 L1.1 Review of Functions & Notation ──
EXTRA["u1_l1.1"] = [
    ("If f(x) = 3x − 2, what is f(5)?",["11","15","*13","17"],"f(5)=3(5)−2=13."),
    ("Which of the following is NOT a function?",["y = 2x + 1","y = x²","*x² + y² = 9","y = |x|"],"A circle fails the vertical line test."),
    ("The domain of f(x) = 1/(x − 4) excludes:",["x = 0","x = 1","*x = 4","x = −4"],"Denominator ≠ 0."),
    ("If g(x) = x² + 1, what is g(−3)?",["−8","8","*10","−10"],"(−3)²+1=10."),
    ("The range of f(x) = x² is:",["All real numbers","x ≥ 0","*y ≥ 0","y ≤ 0"],"Squares are non-negative."),
    ("(f ∘ g)(x) means:",["f(x) · g(x)","f(x) + g(x)","*f(g(x))","g(f(x))"],"Composition."),
    ("If f(x) = 2x and g(x) = x + 3, what is (f ∘ g)(4)?",["11","8","*14","16"],"g(4)=7, f(7)=14."),
    ("A function is one-to-one if:",["It passes the vertical line test","*It passes the horizontal line test (each y-value has exactly one x-value)","Its domain is all reals","It has no intercepts"],"Horizontal line test."),
    ("The vertical line test determines if a graph represents:",["An equation","A relation","*A function","A polynomial"],"Function test."),
    ("If f(x) = √(x − 1), the domain is:",["All real numbers","x > 1","*x ≥ 1","x ≤ 1"],"Radicand ≥ 0."),
    ("The notation f⁻¹(x) represents the:",["Negative of f","Reciprocal 1/f(x)","*Inverse function of f","Derivative of f"],"Inverse notation."),
    ("If f(2) = 7, then f⁻¹(7) = ?",["7","−2","*2","1/7"],"Inverse reverses input/output."),
    ("Which relation is a function: {(1,2),(3,4),(1,5)} or {(1,2),(3,4),(5,6)}?",["The first","Both","*The second (the first has two outputs for x=1)","Neither"],"Unique outputs."),
]

# ── U1 L1.2 Linear Equations & Graphing ──
EXTRA["u1_l1.2"] = [
    ("The slope-intercept form of a line is:",["ax + by = c","*y = mx + b","y − y₁ = m(x − x₁)","x = my + b"],"y = mx + b."),
    ("What is the slope of the line 2x + 3y = 6?",["2/3","2","*−2/3","3/2"],"Solve for y: y = −2x/3 + 2."),
    ("Two parallel lines have:",["Perpendicular slopes","*The same slope","Opposite slopes","No slopes"],"Equal slopes."),
    ("Two perpendicular lines have slopes that are:",["Equal","*Negative reciprocals of each other","Both zero","Both undefined"],"m₁ · m₂ = −1."),
    ("The slope of a horizontal line is:",["Undefined","1","*0","−1"],"No rise."),
    ("The slope of a vertical line is:",["0","1","*Undefined","−1"],"No run."),
    ("What is the y-intercept of y = 4x − 7?",["4","7","*−7","−4"],"b = −7."),
    ("The line through (2, 3) and (6, 11) has slope:",["1","4","*2","3"],"(11−3)/(6−2)=8/4=2."),
    ("Point-slope form is:",["y = mx + b","ax + by = c","*y − y₁ = m(x − x₁)","y = b + mx"],"Point-slope formula."),
    ("The x-intercept is where:",["x = 0","*y = 0","slope = 0","y = x"],"Crosses x-axis."),
    ("If a line passes through the origin, its y-intercept is:",["1","*0","Undefined","−1"],"Origin means b=0."),
    ("The standard form of a linear equation is:",["y = mx + b","*Ax + By = C (A, B, C integers)","y − y₁ = m(x − x₁)","y = C"],"Standard form."),
    ("A line with slope 3 passing through (1,5) has equation:",["y = 3x + 5","*y = 3x + 2","y = 5x + 3","y = 3x − 2"],"y−5=3(x−1) → y=3x+2."),
]

# ── U1 L1.3 Systems of Linear Equations ──
EXTRA["u1_l1.3"] = [
    ("A system of linear equations can have:",["Only one solution","Only no solution","*One solution, no solution, or infinitely many solutions","Exactly two solutions"],"Three possibilities."),
    ("Graphically, the solution to a system is the:",["y-intercept","*Point of intersection","Slope","x-intercept"],"Where lines cross."),
    ("Parallel lines in a system mean the system is:",["Consistent","*Inconsistent (no solution — the lines never intersect)","Dependent","Independent"],"No intersection."),
    ("If two equations describe the same line, the system has:",["No solution","One solution","*Infinitely many solutions (the lines overlap completely)","Two solutions"],"Coincident lines."),
    ("The system y = 2x + 1 and y = 2x − 3 has:",["One solution","Infinitely many","*No solution (same slope, different intercepts — parallel)","Two solutions"],"Parallel lines."),
    ("Solve: y = x + 2 and y = −x + 4. The solution is:",["(2, 2)","(0, 2)","*(1, 3)","(3, 1)"],"x+2=−x+4 → 2x=2 → x=1, y=3."),
    ("A consistent and independent system has:",["No solution","*Exactly one solution","Infinitely many solutions","Two solutions"],"One intersection."),
    ("A consistent and dependent system has:",["No solution","Exactly one solution","*Infinitely many solutions","Two solutions"],"Same line."),
    ("The solution to 2x + y = 5 and x − y = 1 is:",["(1, 3)","(3, 1)","*(2, 1)","(1, 2)"],"Add: 3x=6→x=2, y=1."),
    ("When graphing a system, two intersecting lines represent:",["Inconsistent system","*Consistent independent system (one unique solution)","Dependent system","No system"],"One solution."),
    ("Which system has no solution?",["y = x, y = −x","*y = 3x + 1, y = 3x − 2","y = 2x, y = x","y = x + 1, y = −x + 1"],"Same slope, different b."),
    ("A system of 3 variables needs at least ___ equations to potentially have a unique solution.",["1","2","*3","4"],"Same number as variables."),
    ("If a system has a solution of (−1, 4), then substituting x = −1 into both equations should give:",["Different values","0 for both","*y = 4 for both","x = 4"],"Verification."),
]

# ── U1 L1.4 Solving Systems by Substitution ──
EXTRA["u1_l1.4"] = [
    ("The first step in substitution is to:",["Add the equations","Graph both equations","*Solve one equation for one variable","Multiply by a constant"],"Isolate a variable."),
    ("Solve by substitution: y = 2x and x + y = 9.",["(2, 4)","(4, 5)","*(3, 6)","(6, 3)"],"x+2x=9→3x=9→x=3,y=6."),
    ("Substitution is most efficient when:",["Both equations are in standard form","*One variable is already isolated or has a coefficient of 1","The coefficients are large","Neither variable is isolated"],"Easy isolation."),
    ("Solve: x = 3y − 1 and 2x + y = 5.",["(2, 1)","*(2, 1)","(1, 2)","(3, −1)"],"2(3y−1)+y=5→7y=7→y=1,x=2."),
    ("After substituting, if you get 0 = 0, the system has:",["No solution","*Infinitely many solutions (same line)","One solution","An error"],"Identity → dependent."),
    ("After substituting, if you get 0 = 5, the system has:",["Infinitely many solutions","One solution","*No solution (contradiction → parallel lines)","An error"],"Contradiction."),
    ("Solve: y = x − 1 and 3x − 2y = 5.",["(2, 1)","*(3, 2)","(1, 0)","(4, 3)"],"3x−2(x−1)=5→x+2=5→x=3,y=2."),
    ("In substitution, you replace a variable with:",["A number always","*An equivalent expression from the other equation","Zero","The slope"],"Expression substitution."),
    ("Solve: 2x + y = 8 and y = x + 2.",["(3, 5)","*(2, 4)","(4, 2)","(1, 3)"],"2x+(x+2)=8→3x=6→x=2,y=4."),
    ("Which system is easiest to solve by substitution?",["3x+2y=7, 5x−3y=1","*y=4x−1, 2x+3y=11","4x+5y=20, 3x−2y=1","7x+8y=3, 5x+6y=2"],"y already isolated."),
    ("Solve: x + 2y = 10 and x − y = 1.",["(2, 4)","*(4, 3)","(3, 4)","(5, 2.5)"],"x=1+y→(1+y)+2y=10→3y=9→y=3,x=4."),
    ("When using substitution with fractions, it helps to:",["Ignore fractions","*Multiply through to clear fractions before solving","Only use decimals","Guess and check"],"Clear denominators."),
    ("Solve: a = 2b + 3 and 3a − 4b = 13.",["(3, 0)","(1, −1)","*(5, 1)","(7, 2)"],"3(2b+3)−4b=13→2b=4→b=1,a=5."),
]

# ── U1 L1.5 Solving Systems by Elimination ──
EXTRA["u1_l1.5"] = [
    ("In elimination, the goal is to _____ one variable by adding or subtracting equations.",["Isolate","Square","*Eliminate (cancel out)","Double"],"Cancel a variable."),
    ("Solve by elimination: x + y = 7 and x − y = 3.",["(3, 4)","*(5, 2)","(4, 3)","(2, 5)"],"Add: 2x=10→x=5,y=2."),
    ("To eliminate y from 2x + 3y = 12 and 4x − 3y = 6, you should:",["Subtract","*Add the equations (3y and −3y cancel)","Multiply first","Divide"],"Opposite coefficients."),
    ("Solve: 3x + 2y = 16 and x + 2y = 10.",["(2, 5)","*(3, 3.5)","(4, 2)","(1, 6.5)"],"Subtract: 2x=6→x=3, y=3.5."),
    ("To eliminate x from x + 3y = 7 and 2x + y = 4, multiply the first equation by:",["3","1","*−2","2"],"−2x−6y=−14, add to 2x+y=4."),
    ("If elimination gives 0 = 0, the system is:",["Inconsistent","*Dependent (infinitely many solutions)","Independent","Undefined"],"Same line."),
    ("If elimination gives 0 = 8, the system is:",["Dependent","*Inconsistent (no solution)","Independent","Undefined"],"Contradiction."),
    ("Solve: 5x − 2y = 1 and 3x + 2y = 15.",["(3, 2)","(1, 2)","*(2, 4.5)","(4, 1.5)"],"Add:8x=16→x=2, y=4.5."),
    ("Elimination is often preferred over substitution when:",["One variable is isolated","*Both equations are in standard form with convenient coefficients","Only one equation is given","Variables are already solved"],"Standard form advantage."),
    ("To solve 2x + 5y = 21 and 3x − 2y = −2, multiply equations by what to eliminate y?",["*2 and 5 (to get ±10y)","3 and 2","1 and 1","Nothing"],"LCM of coefficients."),
    ("Solve: 4x + y = 11 and 2x + 3y = 13.",["(3, −1)","*(2, 3)","(1, 7)","(0, 11)"],"Multiply 1st by −3: −12x−3y=−33, add: −10x=−20→x=2,y=3."),
    ("Which method would be most efficient for x − y = 5 and x + y = 9?",["Substitution","Graphing","*Elimination (add to eliminate y directly)","Matrix"],"Direct elimination."),
    ("Solve by elimination: 6x − 5y = −4 and 3x + 5y = 31.",["(2, 5)","*(3, 22/5)","(4, 3)","(5, 2)"],"Add: 9x=27→x=3, 18−5y=−4→y=22/5."),
]

# ── U1 L1.6 Applications of Linear Systems ──
EXTRA["u1_l1.6"] = [
    ("A movie ticket costs $8 for adults and $5 for children. 200 tickets sold for $1,300. How many adult tickets?",["80","*100","120","150"],"8a+5c=1300, a+c=200→a=100."),
    ("Two numbers sum to 20 and their difference is 6. The larger number is:",["10","8","*13","15"],"x+y=20, x−y=6→x=13."),
    ("A boat travels 30 km/h with the current and 20 km/h against it. The current speed is:",["10","*5","15","25"],"b+c=30, b−c=20→c=5."),
    ("A mixture problem: How many liters of 40% acid and 70% acid to make 30L of 50% acid?",["*20L of 40% and 10L of 70%","10L of 40% and 20L of 70%","15L each","25L and 5L"],"0.4x+0.7(30−x)=15→x=20."),
    ("A phone plan charges $30/month plus $0.10/text. Another charges $40/month with free texts. They cost the same at ___ texts.",["50","*100","150","200"],"30+0.1t=40→t=100."),
    ("If the sum of two numbers is 50 and one is 3 times the other, the numbers are:",["15, 35","*12.5, 37.5","10, 40","20, 30"],"x+3x=50→x=12.5."),
    ("Break-even point is where:",["Revenue > cost","Revenue < cost","*Revenue = cost","Cost = 0"],"No profit, no loss."),
    ("A store sells bags for $25,  spending $10 to make each plus $450 fixed costs. Break-even quantity is:",["25","*30","35","45"],"25q=10q+450→15q=450→q=30."),
    ("Two cars leave the same point in opposite directions at 50 and 70 km/h. They're 360 km apart after:",["2 hrs","*3 hrs","4 hrs","5 hrs"],"120t=360→t=3."),
    ("A cashier has $5 and $10 bills totaling $180 with 24 bills. Number of $10 bills:",["8","10","*12","14"],"5x+10y=180, x+y=24→y=12."),
    ("Investment problem: $10,000 split between 5% and 8% accounts earning $680 total. Amount at 8%:",["$4,000","*$6,000","$7,000","$3,000"],"0.05x+0.08(10000−x)=680→x=4000, so 8%=6000."),
    ("A supply-demand equilibrium occurs where the supply and demand _____ are equal.",["slopes","*quantities (and prices — the intersection of supply and demand curves)","intercepts","none"],"Market equilibrium."),
    ("In a word problem, 'sum' translates to _____ and 'difference' translates to _____.",["×, ÷","÷, ×","*+, −","−, +"],"Key vocabulary."),
]

# ── U1 L1.7 Inequalities & System of Inequalities ──
EXTRA["u1_l1.7"] = [
    ("When you multiply or divide an inequality by a negative number, you must:",["Keep the sign","Remove the sign","*Flip the inequality sign","Square both sides"],"Sign reversal rule."),
    ("The solution to 2x − 3 > 7 is:",["x > 2","x < 5","*x > 5","x > 7"],"2x>10→x>5."),
    ("The graph of y ≤ 2x + 1 is shaded:",["Above the line","*Below the line (solid line because ≤ includes equality)","On the line only","Nowhere"],"Below, solid."),
    ("A dashed boundary line means the inequality is:",["≤ or ≥","*< or > (boundary NOT included)","= only","Always solid"],"Strict inequality."),
    ("The solution region of a system of inequalities is:",["Any shaded region","The union of all regions","*The intersection (overlap) of all shaded regions","No region"],"Overlap region."),
    ("Solve: −3x + 6 ≥ 0.",["x ≥ 2","x > 2","*x ≤ 2","x < 2"],"−3x≥−6→x≤2 (flip sign)."),
    ("Which point satisfies y > x + 1 and y < 4?",["(0, 0)","(3, 5)","*(0, 3)","(5, 5)"],"3>0+1✓ and 3<4✓."),
    ("In compound inequality 1 < 2x + 3 < 9, x is between:",["−2 and 4","0 and 6","*−1 and 3","1 and 3"],"−2<2x<6→−1<x<3."),
    ("The graph of |x| < 3 is:",["x > 3 or x < −3","x = 3","*−3 < x < 3","x ≥ 3"],"Between −3 and 3."),
    ("Which inequality has no solution?",["x + 1 > 0","x² ≥ 0","*x + 2 > x + 5","2x < 10"],"Simplifies to 2>5, false."),
    ("To graph y ≥ −x + 2, start by drawing a _____ line.",["Dashed","Dotted","*Solid (≥ includes the boundary)","No"],"Solid for ≥."),
    ("A feasible region in linear programming is bounded by:",["One line","*A system of inequalities (the polygon formed by their intersection)","A circle","A parabola"],"Constraint region."),
    ("The solution to 5 − 2x > 11 is:",["x > −3","x > 3","*x < −3","x < 3"],"−2x>6→x<−3."),
]

# ── U1 L1.8 Linear Programming ──
EXTRA["u1_l1.8"] = [
    ("Linear programming is used to:",["Graph lines","*Optimize (maximize or minimize) a linear objective function subject to constraints","Solve equations","Factor polynomials"],"Optimization."),
    ("The objective function in linear programming is the function to be:",["Graphed","*Maximized or minimized","Factored","Integrated"],"Goal function."),
    ("Constraints in linear programming are expressed as:",["Equations only","*Linear inequalities","Quadratic equations","Limits"],"Inequality constraints."),
    ("The optimal solution always occurs at:",["The origin","The center of the feasible region","*A vertex (corner point) of the feasible region","Any point inside"],"Corner point theorem."),
    ("If the feasible region is empty, the problem has:",["Infinite solutions","One solution","*No solution (constraints are contradictory)","Multiple optimal"],"No feasible region."),
    ("Maximize P = 3x + 2y subject to x ≤ 4, y ≤ 3, x ≥ 0, y ≥ 0. The maximum P is:",["12","14","*18","20"],"At (4,3): P=12+6=18."),
    ("In a manufacturing problem, constraints often represent:",["Profit","*Resource limitations (labor, materials, machine time)","Revenue only","Cost only"],"Limited resources."),
    ("If the objective function is parallel to a constraint boundary, there may be:",["No solution","*Multiple optimal solutions (infinitely many along that edge)","Exactly one","Zero solutions"],"Edge optimality."),
    ("The feasible region is the set of all points that satisfy:",["Only one constraint","*All constraints simultaneously","The objective function","No constraints"],"All satisfied."),
    ("Minimize C = 5x + 4y. Corner points: (0,8), (2,3), (6,0). The minimum is at:",["(0,8)","*(2,3) — C=22","(6,0)","All equal"],"C: 32, 22, 30."),
    ("In linear programming, x ≥ 0 and y ≥ 0 are called:",["Objective constraints","*Non-negativity constraints","Equality constraints","Goal constraints"],"Non-negative variables."),
    ("A bounded feasible region:",["Extends infinitely","*Is enclosed (a polygon with finite area)","Has no solution","Has exactly one vertex"],"Finite region."),
    ("Linear programming was developed in the 1940s primarily for:",["Education","Entertainment","*Military logistics and resource allocation (George Dantzig's simplex method)","Art"],"Historical origin."),
]

# ── U1 L1.9 Advanced Linear Applications ──
EXTRA["u1_l1.9"] = [
    ("A 3×3 system of equations can be solved using:",["Only graphing","*Matrices, elimination, or Cramer's rule","Only substitution","Only factoring"],"Multiple methods."),
    ("A matrix is a rectangular array of:",["Variables only","*Numbers (arranged in rows and columns)","Letters only","Graphs"],"Number array."),
    ("In an augmented matrix for a system, each row represents:",["A variable","*An equation","A solution","A graph"],"Row = equation."),
    ("Row reduction aims to get the matrix in _____ form.",["Standard","*Row echelon (or reduced row echelon) form","Factored","Graphical"],"Echelon form."),
    ("Cramer's Rule uses _____ to solve systems of equations.",["Addition","Substitution","*Determinants","Graphing"],"Determinant method."),
    ("The determinant of [[a,b],[c,d]] is:",["ab + cd","ab − cd","*ad − bc","ac − bd"],"2×2 determinant."),
    ("If the determinant of the coefficient matrix is 0, the system:",["Has one solution","*Has no unique solution (either no solution or infinitely many)","Has two solutions","Cannot be determined"],"Singular matrix."),
    ("A system of 3 equations in 3 unknowns can be written as AX = B where A is:",["3×1","1×3","*3×3","3×2"],"Square coefficient matrix."),
    ("The identity matrix I has:",["All zeros","All ones","*1s on the main diagonal and 0s elsewhere","Random values"],"Identity."),
    ("If AB = I, then B is the _____ of A.",["Transpose","Negative","*Inverse (A⁻¹)","Double"],"Matrix inverse."),
    ("Gaussian elimination uses _____ operations on rows.",["Random","*Elementary row operations (swap, multiply, add multiples)","Column","Diagonal"],"Systematic solving."),
    ("Solving nutrient mix problems with 3 ingredients typically requires:",["1 equation","2 equations","*3 equations (one for each constraint/nutrient)","4 equations"],"Equations match unknowns."),
    ("A break-even analysis with fixed costs $2000, variable cost $15/unit, price $25/unit: break-even is _____ units.",["100","150","*200","250"],"25q=15q+2000→10q=2000→q=200."),
]

# ── U2 L2.1 Quadratic Functions & Parabolas ──
EXTRA["u2_l2.1"] = [
    ("The standard form of a quadratic function is:",["y = a(x−h)² + k","*y = ax² + bx + c","y = mx + b","y = a(x−p)(x−q)"],"Standard form."),
    ("The vertex form of a quadratic is:",["y = ax² + bx + c","*y = a(x − h)² + k where (h,k) is the vertex","y = mx + b","y = a(x−p)(x−q)"],"Vertex form."),
    ("If a > 0 in y = ax² + bx + c, the parabola opens:",["Down","Left","*Up","Right"],"Positive = up."),
    ("The axis of symmetry for y = ax² + bx + c is x = :",["−b/a","b/2a","*−b/(2a)","b/a"],"Symmetry formula."),
    ("The vertex of y = x² − 6x + 8 is at:",["(6, 8)","(−3, −1)","*(3, −1)","(3, 1)"],"x=6/2=3, y=9−18+8=−1."),
    ("The y-intercept of y = 2x² + 3x − 5 is:",["2","3","*−5","5"],"Set x=0: y=c=−5."),
    ("A parabola that opens downward has a:",["Minimum","*Maximum","Neither","Both"],"Vertex is the top."),
    ("In y = 3(x − 2)² + 5, the vertex is:",["(−2, 5)","(2, −5)","*(2, 5)","(−2, −5)"],"(h,k)=(2,5)."),
    ("The parabola y = −x² has its vertex at:",["(1, −1)","(−1, 1)","*(0, 0)","(0, 1)"],"Origin, opens down."),
    ("How many x-intercepts can a parabola have?",["Only 2","Only 1","*0, 1, or 2","Always 2"],"Depends on discriminant."),
    ("If the vertex is below the x-axis and a > 0, the parabola has:",["0 x-intercepts","1 x-intercept","*2 x-intercepts","Cannot determine"],"Opens up, vertex below → crosses x-axis twice."),
    ("The factored form y = 2(x−1)(x−3) has x-intercepts at:",["x = −1, −3","*x = 1, 3","x = 2, 6","x = −1, 3"],"Set each factor to 0."),
    ("The minimum value of y = x² − 4x + 7 is:",["7","4","*3","−3"],"Vertex: x=2, y=4−8+7=3."),
]

# ── U2 L2.2 Transformations of Quadratics ──
EXTRA["u2_l2.2"] = [
    ("Compared to y = x², the graph of y = x² + 3 is shifted:",["Down 3","Left 3","*Up 3","Right 3"],"Vertical shift."),
    ("Compared to y = x², the graph of y = (x − 4)² is shifted:",["Left 4","Up 4","*Right 4","Down 4"],"Horizontal shift."),
    ("The graph of y = −x² is a _____ of y = x² over the x-axis.",["Translation","Stretch","*Reflection","Compression"],"Flip over x-axis."),
    ("The graph of y = 3x² compared to y = x² is:",["Wider","The same","*Narrower (vertical stretch by factor 3)","Reflected"],"Steeper."),
    ("The graph of y = (1/2)x² compared to y = x² is:",["Narrower","The same","*Wider (vertical compression by factor 1/2)","Reflected"],"Flatter."),
    ("y = −2(x + 1)² − 3 has vertex at:",["(1, −3)","(−1, 3)","*(−1, −3)","(1, 3)"],"(h,k)=(−1,−3), opens down."),
    ("A horizontal shift right by 5 replaces x with:",["x + 5","x − 3","*(x − 5)","x/5"],"Inside the function."),
    ("y = (x − 2)² + 1 opens ___ with vertex at ___.",["Down, (2,1)","Up, (−2,1)","*Up, (2,1)","Down, (−2,1)"],"a=1>0."),
    ("Reflecting y = x² over the y-axis gives:",["y = −x²","*y = x² (same graph because x² = (−x)²)","y = −x² + 1","y = x"],"Symmetric about y-axis."),
    ("What transformation converts y = x² to y = (x + 3)² − 2?",["Right 3, up 2","Left 3, up 2","*Left 3, down 2","Right 3, down 2"],"h=−3, k=−2."),
    ("The order of transformations: horizontal shift, then vertical stretch, then vertical shift is:",["Always wrong","*A standard approach (though order matters mainly for shifts with stretches)","The only order","Not a valid order"],"Transformation sequence."),
    ("y = −(1/3)(x − 1)² + 4 is _____, _____, shifted right 1, up 4.",["Narrower, reflected","*Wider (compressed by 1/3), reflected (negative)","Narrower, not reflected","Wider, not reflected"],"Multiple transformations."),
    ("Which graph is the widest? y=5x², y=x², y=(1/4)x², y=2x²",["y = 5x²","y = x²","*y = (1/4)x²","y = 2x²"],"Smallest |a| = widest."),
]

# ── U2 L2.3 Completing the Square ──
EXTRA["u2_l2.3"] = [
    ("Completing the square converts standard form to:",["Factored form","*Vertex form y = a(x − h)² + k","Slope form","General form"],"Goal of CTS."),
    ("To complete the square for x² + 6x, add:",["3","9","*9 (half of 6, squared = 9)","36"],"(b/2)²=9."),
    ("x² + 6x + 9 = (x + ___)²",["6","9","*3","−3"],"Perfect square trinomial."),
    ("Convert y = x² − 8x + 10 to vertex form:",["y = (x − 4)² + 10","*y = (x − 4)² − 6","y = (x + 4)² − 6","y = (x − 8)² + 10"],"(−8/2)²=16, y=(x−4)²−16+10."),
    ("Complete the square: x² − 10x + __ = (x − __)²",["5, 5","10, 10","*25, 5","100, 10"],"(−10/2)²=25."),
    ("For 2x² + 8x + 3, factor out the 2 first: 2(x² + 4x) + 3. Add/subtract what inside?",["2","8","*4 (add 2·4=8, subtract 8)","16"],"(4/2)²=4, but multiply by 2."),
    ("The vertex of y = x² + 2x − 5 (by completing the square) is:",["(1, −4)","(−2, −5)","*(−1, −6)","(2, −1)"],"y=(x+1)²−1−5=(x+1)²−6."),
    ("Solve x² + 4x − 5 = 0 by completing the square:",["x = −5, 1","*x = 1, −5","x = 5, −1","x = 2, −3"],"(x+2)²=9→x+2=±3."),
    ("The vertex of y = 3x² − 12x + 7 is at:",["(2, −5)","(−2, 7)","*(2, −5)","(4, 7)"],"3(x²−4x)+7=3(x−2)²−12+7."),
    ("Completing the square is essential for deriving the:",["Slope formula","Distance formula","*Quadratic formula","Midpoint formula"],"Derivation basis."),
    ("x² + bx + (b/2)² is always a _____ square trinomial.",["Difference of","Imperfect","*Perfect","Sum of"],"Always factors as (x+b/2)²."),
    ("Solve by completing the square: x² − 2x − 3 = 0",["x = −1, 3","*x = 3, −1","x = 2, −2","x = 1, −3"],"(x−1)²=4→x=3,−1."),
    ("For which quadratic is completing the square most useful?",["Already factored ones","*Equations not easily factored (irrational or complex roots)","Linear equations","Cubic equations"],"When factoring fails."),
]

# ── U2 L2.4 Quadratic Formula & Discriminant ──
EXTRA["u2_l2.4"] = [
    ("The quadratic formula is x = :",["(−b ± b²−4ac)/2a","*[−b ± √(b²−4ac)]/(2a)","(b ± √(b²−4ac))/2a","−b/2a"],"Standard formula."),
    ("The discriminant is:",["2a","−b","*b² − 4ac","√(b² − 4ac)"],"Under the radical."),
    ("If the discriminant > 0, the equation has:",["No real solutions","One real solution","*Two distinct real solutions","Complex solutions only"],"Two real roots."),
    ("If the discriminant = 0, the equation has:",["No real solutions","*Exactly one real (repeated) solution","Two real solutions","Complex solutions"],"Double root."),
    ("If the discriminant < 0, the equation has:",["Two real solutions","One real solution","*No real solutions (two complex conjugate solutions)","Infinitely many"],"Complex roots."),
    ("For 2x² − 3x + 1 = 0, the discriminant is:",["−1","0","*1","3"],"9−8=1."),
    ("Solve x² − 5x + 6 = 0 using the quadratic formula:",["x = 1, 6","x = −2, −3","*x = 2, 3","x = −2, 3"],"x=(5±√1)/2=(5±1)/2."),
    ("For x² + 4 = 0, the discriminant is:",["4","0","*−16","16"],"0−16=−16, no real roots."),
    ("The quadratic formula works for _____ quadratic equation.",["Only factorable","Only integer","*Every (any ax²+bx+c=0 with a≠0)","Only positive"],"Universal method."),
    ("If b²−4ac = 49, the roots are:",["Complex","Repeated","*Two distinct real (and rational, since √49=7)","None"],"Perfect square discriminant."),
    ("Solve 3x² + 2x − 1 = 0:",["x = 1, −1/3","*x = 1/3, −1","x = −1/3, 1","x = 3, −1"],"x=(−2±√16)/6=(−2±4)/6."),
    ("The sum of the roots of ax² + bx + c = 0 is:",["b/a","c/a","*−b/a","−c/a"],"Vieta's formula."),
    ("The product of the roots of ax² + bx + c = 0 is:",["−b/a","b/a","*c/a","−c/a"],"Vieta's formula."),
]

# ── U2 L2.5 Graphing Quadratic Functions ──
EXTRA["u2_l2.5"] = [
    ("The first step to graph y = ax² + bx + c is usually finding the:",["y-intercept only","End behavior","*Vertex (using x = −b/2a)","Slope"],"Start with vertex."),
    ("The axis of symmetry of y = 2x² − 8x + 3 is:",["x = −2","x = 8","*x = 2","x = 4"],"x = 8/4 = 2."),
    ("The y-intercept of any quadratic y = ax² + bx + c is the point:",["(a, 0)","(b, 0)","*(0, c)","(c, 0)"],"Set x = 0."),
    ("To find x-intercepts, set y = 0 and solve using:",["Slope formula","*Factoring, completing the square, or quadratic formula","Only graphing","Only the vertex"],"Three algebraic methods."),
    ("The graph of y = −2x² + 4x + 1 opens _____ and has a _____.",["Up, minimum","*Down, maximum","Up, maximum","Down, minimum"],"a < 0→ down, maximum."),
    ("If the vertex is (3, 5) and a = 1, then the point symmetric to (1, 9) is:",["(3, 9)","(1, 5)","*(5, 9)","(7, 9)"],"Distance from axis: 3−1=2, so 3+2=5."),
    ("For y = x² − 4x + 3, the x-intercepts are:",["x = −1, −3","*x = 1, 3","x = −1, 3","x = 4, 3"],"Factor: (x−1)(x−3)=0."),
    ("The domain of any quadratic function is:",["y ≥ 0","*All real numbers","x ≥ 0","Depends on a"],"Always all reals."),
    ("The range of y = −(x−2)² + 5 is:",["y ≥ 5","All reals","*y ≤ 5","y ≥ −5"],"Opens down, max at 5."),
    ("End behavior of y = 3x²: as x→±∞, y→:",["−∞","0","*+∞","Undefined"],"Both arms go up."),
    ("A parabola with vertex at (−1, 4) and a < 0 has range:",["y ≥ 4","y ≥ −1","*y ≤ 4","All reals"],"Max at 4."),
    ("To graph more accurately, find additional points by choosing x-values on _____ of the axis.",["One side only","*Both sides (symmetric about the axis)","Neither side","Random sides"],"Symmetry."),
    ("The width of the parabola is determined by |a|: larger |a| means:",["Wider","Same width","*Narrower","Flatter"],"Steeper."),
]

# ── U2 L2.6 Applications of Quadratics ──
EXTRA["u2_l2.6"] = [
    ("The height of a projectile is modeled by h(t) = −16t² + v₀t + h₀. The −16 comes from:",["Air resistance","Mass","*Gravity (half of g ≈ 32 ft/s²)","Wind"],"Gravity constant."),
    ("A ball thrown upward reaches maximum height at t = :",["0","v₀","*v₀/(2·16) = v₀/32 seconds","h₀/v₀"],"t = −b/2a."),
    ("If h(t) = −16t² + 64t, the maximum height is:",["64 ft","16 ft","*64 ft (at t=2)","128 ft"],"h(2)=−64+128=64."),
    ("A rectangle with perimeter 40 has maximum area when:",["Length = 20","*Length = Width = 10 (square)","Length = 15","Length = 30"],"Square maximizes area."),
    ("If revenue R(x) = −2x² + 100x, the price x that maximizes revenue is:",["50","*25","100","10"],"x = −100/−4 = 25."),
    ("The profit function is:",["Revenue × Cost","Cost − Revenue","*Revenue − Cost","Revenue + Cost"],"P = R − C."),
    ("An object hits the ground when h(t) = :",["Its maximum","t = 0","*0 (solve for t > 0)","1"],"Height = 0."),
    ("The dimensions of maximum area for a fence along a wall with 60 m of fencing: width × length =",["10 × 40","20 × 20","*15 × 30","12 × 36"],"A=x(60−2x), max at x=15."),
    ("Two numbers with a sum of 20 have maximum product when they are:",["1 and 19","5 and 15","*10 and 10","2 and 18"],"Equal numbers maximize."),
    ("A ball is thrown from 48 ft at 32 ft/s. When does it hit the ground?",["t = 1","t = 2","*t = 3","t = 4"],"−16t²+32t+48=0→t²−2t−3=0→t=3."),
    ("In the equation h = −4.9t² + v₀t + h₀, the −4.9 represents gravity in _____ units.",["Feet","Inches","*Meters (half of g ≈ 9.8 m/s²)","Miles"],"Metric gravity."),
    ("If a company's cost is C(x) = x² + 10x + 50 and revenue is R(x) = 50x, profit is maximized at x = :",["10","*20","30","50"],"P=−x²+40x−50, x=20."),
    ("The trajectory of a projectile forms what shape?",["Circle","Line","*Parabola","Ellipse"],"Quadratic path."),
]

# ── U2 L2.7 Quadratic Inequalities ──
EXTRA["u2_l2.7"] = [
    ("To solve x² − 5x + 6 > 0, first find the:",["Vertex","y-intercept","*Zeros (roots): x = 2 and x = 3","Slope"],"Factor first."),
    ("x² − 5x + 6 > 0 factors as (x−2)(x−3) > 0. The solution is:",["2 < x < 3","x < 2","*x < 2 or x > 3","x = 2 or x = 3"],"Positive outside roots."),
    ("x² − 4 ≤ 0 factors as (x−2)(x+2) ≤ 0. The solution is:",["x ≤ −2 or x ≥ 2","*−2 ≤ x ≤ 2","x < 0","x > 0"],"Between roots."),
    ("A sign chart helps determine where the quadratic is:",["Zero only","*Positive or negative in each interval","Undefined","Maximum"],"Sign analysis."),
    ("For a parabola opening upward (a > 0), the quadratic is negative:",["Everywhere","Nowhere","*Between the roots (if they exist)","Outside the roots"],"Below x-axis between roots."),
    ("Solve: x² + 2x − 8 < 0",["x < −4 or x > 2","*−4 < x < 2","x > 2","x < −4"],"(x+4)(x−2)<0, between roots."),
    ("Solve: −x² + 4 > 0",["x > 2 or x < −2","*−2 < x < 2","x > 2","All reals"],"x²<4 → |x|<2."),
    ("If x² + 1 > 0, the solution is:",["No solution","x > 1","*All real numbers (x² + 1 is always positive)","x > 0"],"Always true."),
    ("If x² + 1 < 0, the solution is:",["All reals","x < 0","*No solution (x² + 1 is always positive, never negative)","x < −1"],"Never true."),
    ("The solution to (x−1)² ≥ 0 is:",["x ≥ 1","x ≤ 1","*All real numbers (a square is always ≥ 0)","No solution"],"Always non-negative."),
    ("When testing intervals, choose a _____ from each interval.",["Boundary point","*Test point (any value in the interval)","Vertex","Asymptote"],"Test a value."),
    ("Solve: 2x² − x − 6 ≥ 0. Roots are x = 2, x = −3/2. Solution:",["−3/2 ≤ x ≤ 2","*x ≤ −3/2 or x ≥ 2","x > 2","x < −3/2"],"a>0, positive outside."),
    ("Graphically, x² − 9 < 0 means the parabola y = x² − 9 is:",["Above the x-axis","*Below the x-axis (between x = −3 and x = 3)","On the x-axis","At the vertex"],"Below zero."),
]

# ── U3 L3.1 Polynomial Operations ──
EXTRA["u3_l3.1"] = [
    ("A polynomial of degree 3 is called a:",["Quadratic","*Cubic","Quartic","Linear"],"Degree 3."),
    ("The leading coefficient of 4x³ − 2x² + x − 7 is:",["−7","1","−2","*4"],"Highest degree term's coefficient."),
    ("(2x² + 3x − 1) + (x² − 5x + 4) = ",["3x² + 2x + 3","3x² − 8x + 3","*3x² − 2x + 3","2x² − 2x + 3"],"Combine like terms."),
    ("(5x³ − 2x) − (3x³ + x² − 4) = ",["2x³ + x² − 2x + 4","*2x³ − x² − 2x + 4","8x³ − x² − 2x − 4","2x³ − x² − 2x − 4"],"Distribute the negative."),
    ("(x + 3)(x − 2) = ",["x² + x − 6","x² − x + 6","*x² + x − 6","x² − 5x − 6"],"FOIL: x²−2x+3x−6."),
    ("(2x − 1)(3x + 4) = ",["6x² + 5x − 4","6x² − 5x − 4","*6x² + 5x − 4","6x² + 8x − 4"],"6x²+8x−3x−4."),
    ("(x + 2)³ = ",["x³ + 8","*x³ + 6x² + 12x + 8","x³ + 2x² + 4x + 8","x³ + 4x² + 6x + 8"],"Binomial expansion."),
    ("The degree of (3x²)(4x³) is:",["5","6","*5","15"],"2+3=5 (degree adds when multiplying)."),
    ("The product of two polynomials of degrees 2 and 3 has degree:",["2","3","*5","6"],"Degrees add."),
    ("(a + b)² = ",["a² + b²","a² − 2ab + b²","*a² + 2ab + b²","2a² + 2b²"],"Perfect square."),
    ("(a − b)(a + b) = ",["a² + b²","a² + 2ab + b²","*a² − b²","a² − 2ab + b²"],"Difference of squares."),
    ("Subtract 2x³ − x from 5x³ + 3x − 2:",["7x³ + 2x − 2","*3x³ + 4x − 2","−3x³ + 4x − 2","3x³ − 4x − 2"],"(5x³+3x−2)−(2x³−x)."),
    ("The constant term in (x − 3)(x + 5)(x − 1) is:",["15","−15","*15","3"],"(−3)(5)(−1)=15."),
]

# ── U3 L3.2 Factoring Polynomials ──
EXTRA["u3_l3.2"] = [
    ("Factor GCF from 6x³ + 9x²:",["3x(2x² + 3x)","*3x²(2x + 3)","6x(x² + 9)","9x(6x + 1)"],"GCF = 3x²."),
    ("Factor x² − 9:",["(x − 3)²","(x + 3)²","*(x − 3)(x + 3)","(x − 9)(x + 1)"],"Difference of squares."),
    ("Factor x² + 5x + 6:",["(x + 1)(x + 6)","*(x + 2)(x + 3)","(x − 2)(x − 3)","(x + 1)(x + 5)"],"Factors of 6 summing to 5."),
    ("Factor 2x² + 7x + 3:",["(2x + 3)(x + 1)","*(2x + 1)(x + 3)","(2x − 1)(x − 3)","(x + 1)(2x + 3)"],"AC method: 2·3=6, factors 1,6 sum 7."),
    ("x³ − 8 is a _____ and factors as:",["Sum of cubes; (x+2)(x²−2x+4)","*Difference of cubes; (x − 2)(x² + 2x + 4)","Cannot be factored","Difference of squares"],"a³−b³=(a−b)(a²+ab+b²)."),
    ("x³ + 27 factors as:",["(x + 3)³","*(x + 3)(x² − 3x + 9)","(x − 3)(x² + 3x + 9)","Cannot factor"],"Sum of cubes."),
    ("Factor by grouping: x³ + 2x² + 3x + 6",["(x + 2)(x + 3)","*(x² + 3)(x + 2)","(x + 1)(x² + 6)","Cannot factor"],"Group: x²(x+2)+3(x+2)."),
    ("Factor completely: 3x³ − 12x",["3x(x² − 4)","*3x(x − 2)(x + 2)","3(x³ − 4x)","x(3x² − 12)"],"GCF then diff of squares."),
    ("A perfect square trinomial x² − 10x + 25 factors as:",["(x − 5)(x + 5)","*(x − 5)²","(x + 5)²","(x − 25)²"],"(x−5)²."),
    ("Factor 4x² − 25:",["(2x − 5)²","*(2x − 5)(2x + 5)","(4x − 5)(x + 5)","Cannot factor"],"Difference of squares."),
    ("If x² + bx + c factors as (x + p)(x + q), then b = _____ and c = _____.",["pq, p+q","*p + q, pq","p − q, pq","pq, p − q"],"Sum and product."),
    ("Factor: x⁴ − 16",["(x² − 4)²","*(x² − 4)(x² + 4) = (x−2)(x+2)(x²+4)","(x − 2)⁴","Cannot factor"],"Difference of squares twice."),
    ("The sum of squares x² + 4 is _____ over the reals.",["Factorable","A perfect square","*Not factorable (prime)","Zero"],"Cannot factor with reals."),
]

# ── U3 L3.3 Synthetic Division ──
EXTRA["u3_l3.3"] = [
    ("Synthetic division is a shortcut for dividing a polynomial by:",["Any polynomial","A quadratic","*A linear divisor of the form (x − c)","A constant"],"Only linear divisors."),
    ("When dividing by (x − 3), the value used in synthetic division is:",["−3","0","*3","1/3"],"Use c, not −c."),
    ("When dividing by (x + 2), the value used in synthetic division is:",["2","0","*−2","1/2"],"x+2 = x−(−2), so c=−2."),
    ("(x³ − 4x² + 5x − 2) ÷ (x − 1) gives quotient:",["x² − 3x + 2 R 1","*x² − 3x + 2 R 0","x² − 5x + 2","x² + 3x − 2"],"Remainder 0 → (x−1) is a factor."),
    ("If the remainder is 0 in synthetic division, then the divisor is:",["Not a factor","*A factor of the polynomial","The quotient","The derivative"],"Zero remainder = factor."),
    ("For missing degree terms in synthetic division, use:",["Nothing","1","*0 as a placeholder coefficient","The previous coefficient"],"Placeholder zeros."),
    ("Dividing 2x³ + 0x² − 5x + 3 by (x − 1) using synthetic division starts with coefficients:",["2, −5, 3","*2, 0, −5, 3","2, 5, 3","1, 0, −5, 3"],"Include the 0x² term."),
    ("The degree of the quotient when dividing a degree-4 polynomial by (x − c) is:",["4","2","*3","1"],"Degree drops by 1."),
    ("Synthetic division can verify that x = 2 is a root of x³ − 6x + 4 = 0 if the remainder is:",["2","−2","*0","4"],"Root → remainder = 0."),
    ("Compared to long division, synthetic division is:",["Less efficient","More flexible","*Faster for linear divisors","Usable for all divisors"],"Speed advantage."),
    ("(2x⁴ − 3x³ + x − 5) ÷ (x + 1): the coefficients used are:",["2, −3, 1, −5","*2, −3, 0, 1, −5","2, 3, 0, 1, 5","−2, 3, 0, −1, 5"],"Include 0 for missing x²."),
    ("If you get remainders consistently, you should try another potential root from the:",["Random numbers","*Rational Root Theorem (±factors of constant / ±factors of leading coeff)","Graph only","Decimals"],"Systematic root finding."),
    ("Synthetic division helps in:",["Only dividing","*Finding roots, factoring, and evaluating polynomials efficiently","Only graphing","Only multiplying"],"Multiple uses."),
]

# ── U3 L3.4 Polynomial Graphs & Zeros ──
EXTRA["u3_l3.4"] = [
    ("A polynomial of degree n has at most _____ real zeros.",["n + 1","n − 1","*n","2n"],"Degree bounds zeros."),
    ("A polynomial of degree n has at most _____ turning points.",["n","*n − 1","n + 1","2n"],"One less than degree."),
    ("The end behavior of a polynomial with odd degree and positive leading coefficient: as x→+∞, y→___; as x→−∞, y→___.",["+∞, +∞","−∞, −∞","*+∞, −∞","−∞, +∞"],"Odd degree, positive LC."),
    ("The end behavior of an even-degree polynomial with negative leading coefficient goes to:",["Up on both ends","*Down on both ends","Up-left, down-right","Down-left, up-right"],"Even, negative: both down."),
    ("A zero with multiplicity 2 means the graph _____ the x-axis.",["Crosses","*Touches (bounces off) without crossing","Doesn't reach","Goes through twice"],"Even multiplicity = touch."),
    ("A zero with multiplicity 1 (or any odd multiplicity) means the graph _____ the x-axis.",["Touches only","*Crosses","Doesn't reach","Bounces"],"Odd multiplicity = cross."),
    ("f(x) = (x−1)²(x+3) has zeros at:",["x = 1 only","x = −3 only","*x = 1 (mult 2) and x = −3 (mult 1)","x = −1 and x = 3"],"Set each factor = 0."),
    ("The Intermediate Value Theorem says if f(a) and f(b) have opposite signs, there's a:",["Maximum","Minimum","*Real zero between a and b","No zero"],"Sign change = root."),
    ("f(x) = x⁴ − 1 has degree 4, so its end behavior is:",["Opposite ends","*Both ends go to +∞ (even degree, positive leading coefficient)","Both to −∞","One up, one down"],"Even, positive LC."),
    ("How many turning points does f(x) = x³ − 3x have?",["3","1","*2 (at most n−1 = 2)","0"],"Cubic has at most 2 turns."),
    ("The graph of f(x) = x⁵ _____ the x-axis at the origin.",["Touches","*Crosses (odd multiplicity = cross)","Doesn't touch","Bounces"],"Mult 5 is odd."),
    ("To sketch a polynomial, find: zeros, y-intercept, end behavior, and:",["Area","Slope","*Multiplicity of zeros (to know cross vs. touch)","Domain"],"Key features."),
    ("f(x) = −2x³ + 6x: as x→+∞, f(x)→ ___ and as x→−∞, f(x)→ ___.",["−∞, +∞","*−∞, +∞","+∞, −∞","−∞, −∞"],"Odd degree, negative LC."),
]

# ── U3 L3.5 Remainder & Factor Theorems ──
EXTRA["u3_l3.5"] = [
    ("The Remainder Theorem states that f(c) equals the remainder when f(x) is divided by:",["x + c","xc","*(x − c)","c − x"],"f(c) = remainder."),
    ("By the Remainder Theorem, f(2) for f(x) = x³ − 4x + 1 equals:",["−5","5","*1","3"],"8−8+1=1."),
    ("The Factor Theorem: (x − c) is a factor of f(x) if and only if f(c) = :",["1","c","*0","−c"],"Zero remainder."),
    ("If f(3) = 0, then _____ is a factor of f(x).",["(x + 3)","3x","*(x − 3)","(x − 1)"],"Factor Theorem."),
    ("Is (x − 2) a factor of x³ − 3x² + 4? Check: f(2) = :",["2","−2","*0","4"],"8−12+4=0. Yes, it's a factor."),
    ("If (x + 1) is a factor of x² + 3x + 2, then f(−1) should equal:",["1","−1","*0","2"],"Factor test."),
    ("The Rational Root Theorem: possible rational roots of f(x) are ±(factors of constant)/(factors of _____).",["Degree","Middle coefficient","*Leading coefficient","x"],"p/q candidates."),
    ("For f(x) = 2x³ − x² − 5x + 3, possible rational roots include:",["Only integers","*±1, ±3, ±1/2, ±3/2","±1, ±2, ±3","Only positive"],"Factors of 3 / factors of 2."),
    ("The Remainder Theorem lets us evaluate polynomials efficiently using:",["Graphing","*Synthetic division (remainder = f(c))","Long division only","Factoring"],"Quick evaluation."),
    ("If f(x) = x⁴ − 1 and we divide by (x − 1), the remainder is:",["1","−1","*0 (since f(1) = 0)","2"],"1−1=0."),
    ("After finding one root r, we can factor f(x) as (x − r) · q(x) and find remaining roots from:",["f(x) again","The original","*q(x) (the reduced quotient polynomial)","r"],"Reduce degree."),
    ("Finding all zeros of a polynomial often requires combining the Rational Root Theorem with:",["Only graphing","*Synthetic division and the Factor Theorem repeatedly","Only guessing","Nothing else"],"Systematic approach."),
    ("If a polynomial has no rational roots among the candidates, the roots may be:",["Nonexistent","*Irrational or complex (use quadratic formula on the quotient if possible)","Rational but missed","Integers"],"Other root types."),
]

# ── U3 L3.6 Complex Numbers & Polynomial Roots ──
EXTRA["u3_l3.6"] = [
    ("The imaginary unit i is defined as:",["−1","1","*√(−1)","0"],"i² = −1."),
    ("i² = ",["1","i","*−1","−i"],"By definition."),
    ("A complex number has the form:",["a + b","a × b","*a + bi (where a, b are real)","Only real numbers"],"Standard form."),
    ("The complex conjugate of 3 + 2i is:",["3 + 2i","−3 − 2i","*3 − 2i","−3 + 2i"],"Change sign of imaginary."),
    ("(2 + 3i)(2 − 3i) = ",["4 − 9","4 + 9i","*13","4 − 9i²"],"4 − 9i² = 4 + 9 = 13."),
    ("Complex roots of polynomials with real coefficients come in:",["Singles","Triples","*Conjugate pairs (a + bi and a − bi)","Random arrangements"],"Conjugate Root Theorem."),
    ("If 2 + i is a root of a polynomial with real coefficients, then _____ is also a root.",["−2 + i","2 + 2i","*2 − i","−2 − i"],"Conjugate pair."),
    ("Simplify: (4 + 3i) + (2 − 5i) = ",["6 + 8i","6 − 8i","*6 − 2i","2 + 8i"],"Add real and imaginary parts."),
    ("Simplify: (1 + i)² = ",["2","0","*2i","1 + 2i"],"1+2i+i²=1+2i−1=2i."),
    ("The Fundamental Theorem of Algebra states that a degree-n polynomial has exactly _____ roots (counting multiplicity, over ℂ).",["n − 1","2n","*n","1"],"n roots in ℂ."),
    ("i³ = ",["1","i","*−i","−1"],"i³ = i²·i = −i."),
    ("i⁴ = ",["i","−1","*1","−i"],"i⁴ = (i²)² = 1."),
    ("To divide complex numbers, multiply by the _____ of the denominator.",["Opposite","Same number","*Conjugate","Reciprocal"],"Rationalize."),
]

# ── U3 L3.7 Higher-Degree Polynomials ──
EXTRA["u3_l3.7"] = [
    ("A degree-4 polynomial is called a:",["Cubic","*Quartic","Quintic","Sextic"],"Fourth degree."),
    ("A quartic can have at most _____ real zeros.",["3","*4","5","8"],"Degree = max real zeros."),
    ("Descartes' Rule of Signs counts _____ to estimate positive real zeros.",["Coefficients","Degree","*Sign changes in f(x)","Roots"],"Positive root estimate."),
    ("For negative real zeros, apply Descartes' Rule to:",["f(x)","f(−x) only for odd terms","*f(−x)","−f(x)"],"Substitute −x."),
    ("f(x) = x⁴ − 3x³ + x − 5 has sign changes: +, −, +, −. That's ___ sign changes → at most ___ positive real roots.",["2, 2","*3, 3 (or 1)","4, 4","1, 1"],"3 or 1 positive roots."),
    ("A degree-5 polynomial must have at least _____ real zero(s).",["0","2","*1 (odd degree → at least one real root)","5"],"Odd degree guarantee."),
    ("Upper Bound Theorem: if synthetic division by (x − c) with c > 0 gives all non-negative values in the last row, then:",["c is a root","*There are no real zeros greater than c","All roots are positive","c is the largest root"],"Upper bound."),
    ("Graphing technology helps find approximate roots of higher-degree polynomials by identifying:",["Asymptotes","*X-intercepts (where the graph crosses or touches the x-axis)","Y-intercepts only","Slopes"],"Visual root finding."),
    ("Factor x⁴ − 5x² + 4 by treating it as a quadratic in x²:",["Cannot factor","(x²−4)(x²+1)","*(x² − 1)(x² − 4) = (x−1)(x+1)(x−2)(x+2)","(x − 4)(x − 1)"],"Quadratic substitution."),
    ("A polynomial that cannot be factored over the reals is called:",["Zero","Simple","*Irreducible (over the reals)","Prime only"],"No real factors."),
    ("The graph of a degree-6 polynomial with positive leading coefficient goes to _____ on both ends.",["−∞","One up, one down","*+∞","0"],"Even degree, positive LC."),
    ("Finding all roots of x⁵ − 2x⁴ − x + 2 = 0: first try rational roots, then:",["Stop","*Use synthetic division to reduce degree, repeat until all roots found","Guess","Only graph"],"Iterative reduction."),
    ("A polynomial identity means the equation is true for:",["One value","Two values","*All values of the variable","No values"],"Always true."),
]

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for key, tuples in EXTRA.items():
    if key not in data:
        print(f"⚠️  {key} not found"); continue
    existing = data[key].get("quiz_questions", [])
    start = len(existing) + 1
    for i, (qt, opts, exp) in enumerate(tuples):
        q = mq(qt, opts, exp)
        q["question_number"] = start + i
        existing.append(q)
    data[key]["quiz_questions"] = existing
    count += 1

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Algebra 2 U1-U3: added questions to {count} lessons")
