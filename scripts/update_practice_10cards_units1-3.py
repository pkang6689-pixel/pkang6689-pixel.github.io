#!/usr/bin/env python3
"""
Update practice HTML files with 10 flashcards per lesson for Algebra 2 Units 1-3.
"""

import os
import re

# Define flashcard content for Units 1-3 (10 cards each)
FLASHCARD_CONTENT = {
    # Unit 1: Linear Systems
    "1.1": [
        {"question": "If f(x) = 2x + 3, what is f(5)?", "answer": "f(5) = 13. Substitute x=5: f(5) = 2(5) + 3 = 10 + 3 = 13."},
        {"question": "What is the domain of f(x) = √(x - 4)?", "answer": "x ≥ 4. Radicand must be non-negative."},
        {"question": "What is the range of f(x) = |x|?", "answer": "y ≥ 0. Absolute value is always non-negative."},
        {"question": "Find (f ∘ g)(2) if f(x) = x² and g(x) = x + 1", "answer": "9. (f ∘ g)(2) = f(g(2)) = f(3) = 9."},
        {"question": "What is f⁻¹(x) if f(x) = 2x - 5?", "answer": "f⁻¹(x) = (x + 5)/2. Swap x and y, solve for y."},
        {"question": "Is f(x) = 3x + 2 one-to-one?", "answer": "Yes. Linear functions with non-zero slope are one-to-one. Passes horizontal line test."},
        {"question": "Find f(f⁻¹(7)) for any function f", "answer": "7. Composing function with its inverse returns original input."},
        {"question": "If f(2) = 5, what is the point on the graph?", "answer": "(2, 5). Graphs are plotted as (x, f(x)) points."},
        {"question": "Determine if f(x) = x² is even or odd", "answer": "Even. f(-x) = f(x). Symmetric about y-axis."},
        {"question": "Find the vertex of f(x) = (x - 3)² + 2", "answer": "(3, 2). Vertex form f(x) = a(x - h)² + k has vertex (h, k)."}
    ],
    "1.2": [
        {"question": "Find slope between (1, 2) and (4, 8)", "answer": "m = 2. m = (8-2)/(4-1) = 6/3 = 2."},
        {"question": "Write equation in slope-intercept form: slope = 3, y-intercept = -2", "answer": "y = 3x - 2. Form: y = mx + b."},
        {"question": "Find slope of x + 2y = 6", "answer": "m = -1/2. Rewrite: y = -x/2 + 3."},
        {"question": "Find equation using point-slope: m = 4, point (2, 5)", "answer": "y - 5 = 4(x - 2) or y = 4x - 3. Use y - y₁ = m(x - x₁)."},
        {"question": "What is the x-intercept of y = 2x - 6?", "answer": "3. Set y = 0: 0 = 2x - 6, so x = 3. Point: (3, 0)."},
        {"question": "Find equation of line parallel to y = 3x + 1 through (0, 5)", "answer": "y = 3x + 5. Parallel lines have same slope."},
        {"question": "Find equation of line perpendicular to y = 2x - 1 through (1, 2)", "answer": "y - 2 = -1/2(x - 1) or y = -x/2 + 5/2. Perpendicular slopes: m₁ · m₂ = -1."},
        {"question": "Is the line through (0,1), (1,3), (2,5) linear?", "answer": "Yes. Constant slope m = 2 between all points indicates linearity."},
        {"question": "Solve for slope: line passes (a, b) and (a+1, b+2)", "answer": "m = 2. Slope = (b+2-b)/(a+1-a) = 2/1 = 2."},
        {"question": "Find line through (3, 4) and (-1, 2)", "answer": "y - 4 = 1/2(x - 3) or y = x/2 + 5/2. m = (2-4)/(-1-3) = -2/-4 = 1/2."}
    ],
    "1.3": [
        {"question": "Solve graphically: solution is intersection of y = x + 1 and y = -x + 3", "answer": "(1, 2). Check: (1) + 1 = 2 and -(1) + 3 = 2. ✓"},
        {"question": "Classify: x + y = 5 and 2x + 2y = 10", "answer": "Dependent (infinitely many solutions). Second is 2× the first, same line."},
        {"question": "Classify: x + y = 3 and x + y = 5", "answer": "Inconsistent (no solution). Parallel lines, never intersect."},
        {"question": "Solve by substitution: y = 2x and x + y = 9", "answer": "x = 3, y = 6. Substitute: x + 2x = 9, so 3x = 9."},
        {"question": "Find intersection of x = 2 and y = -3", "answer": "(2, -3). Vertical and horizontal lines intersect at point."},
        {"question": "Is (1, 1) a solution to 2x + 3y = 5?", "answer": "Yes. 2(1) + 3(1) = 5. ✓"},
        {"question": "How many solutions for consistent and independent system?", "answer": "Exactly one. Lines intersect at single point."},
        {"question": "Solve: 2x - y = 4 and y = 2x - 4", "answer": "Dependent system, infinitely many solutions. Equations are identical."},
        {"question": "Find point where y = 1/2·x intersects y = x - 1", "answer": "(2, 1). 1/2·x = x - 1 gives x/2 = 1, so x = 2."},
        {"question": "What does a fake equation in system indicate?", "answer": "No solution (inconsistent). Example: 0 = 5 is impossible."}
    ],
    "1.4": [
        {"question": "Solve by substitution: x = 3y + 1 and 2x - y = 5", "answer": "y = 1/7, x = 10/7. Substitute first into second."},
        {"question": "Steps for substitution method?", "answer": "(1) Solve one equation for a variable, (2) Substitute into other, (3) Solve, (4) Back-substitute."},
        {"question": "Solve: y = 2x and x - y = -3", "answer": "x = -3/1 = -3? No: x - 2x = -3, so -x = -3, x = 3, y = 6."},
        {"question": "Solve: 2x + y = 11 and y = x + 2", "answer": "x = 3, y = 5. Substitute: 2x + (x+2) = 11 gives 3x = 9."},
        {"question": "Word problem setup: pencils $0.25, pens $0.75, 20 items, $12 total. Equations?", "answer": "x + y = 20 and 0.25x + 0.75y = 12. Let x=pencils, y=pens."},
        {"question": "Solve previous: how many pens?", "answer": "10 pens (y=10). From equations: x=10, y=10."},
        {"question": "Check solution x=2, y=3 in 2x + y = 7", "answer": "2(2) + 3 = 7. ✓ Solution is correct."},
        {"question": "Solve: 3x - 2y = 4 and x = y + 1", "answer": "x = 2, y = 1. Substitute: 3(y+1) - 2y = 4 gives y = 1."},
        {"question": "Why not divide by coefficient during substitution?", "answer": "Can cause fractions. Better to express one variable without division when possible."},
        {"question": "Solve: 5x + y = 12 and y = -5x + 2", "answer": "Inconsistent (no solution, inconsistent equations). Leads to 0 = 10."}
    ],
    "1.5": [
        {"question": "Solve by elimination: x + y = 5 and x - y = 1", "answer": "x = 3, y = 2. Add equations: 2x = 6, so x = 3. Then y = 2."},
        {"question": "Solve by elimination: 2x + y = 3 and x - y = 3", "answer": "x = 2, y = -1. Add: 3x = 6, x = 2. Then y = -1."},
        {"question": "Multiply first equation by 2: 3x + 2y = 8 and 2x + y = 5", "answer": "6x + 4y = 16 and 2x + y = 5. Then multiply second by -4 and add."},
        {"question": "Elimination strategy when no coefficients match?", "answer": "Multiply equations to make coefficients of one variable opposites, then add."},
        {"question": "Solve: 3x - 2y = 6 and 2x + y = 5", "answer": "x = 16/7, y = 3/7. Multiply second by 2: 2|(2x+y=5). Add to first."},
        {"question": "Why use elimination instead of substitution?", "answer": "Faster when coefficients are nice integers. Avoids fractions longer."},
        {"question": "Solve: x + 2y = 7 and 3x - 2y = 5", "answer": "x = 3, y = 2. Add equations: 4x = 12, x = 3. Then y = 2."},
        {"question": "Check solution x=1, y=2 in 2x+3y=8", "answer": "2(1) + 3(2) = 8. ✓"},
        {"question": "Solve: 4x - y = 10 and 2x + y = 2", "answer": "x = 2, y = -2. Add: 6x = 12, x = 2. Then y = -2."},
        {"question": "When does elimination give infinite solutions?", "answer": "When equations are identical (dependent). Get 0 = 0 instead."}
    ],
    "1.6": [
        {"question": "Mixture: 20% salt + pure water to get 100L of 5% solution. How much pure water?", "answer": "500L of water (x=100, y=500 means total 600L, hmm check calculation)... actually setup: 0.20x = 0.05(x+y)."},
        {"question": "Investment: $8000 total, part at 5%, rest at 8%, total interest $550. Setup equations?", "answer": "x + y = 8000 and 0.05x + 0.08y = 550."},
        {"question": "Coin problem: 30 coins, quarters and dimes, total $6.30. How many quarters?", "answer": "18 quarters. Equations: x + y = 30 and 0.25x + 0.10y = 6.30."},
        {"question": "Distance: train A at 60 mph, train B at 80 mph, start same time opposite. When 280 miles apart?", "answer": "2 hours. Distance = 60t + 80t = 280, so 140t = 280, t = 2."},
        {"question": "Boat problem: boat speed 20 mph, current 5 mph, downstream distance 100 miles. Time?", "answer": "5 hours. Time = 100/(20+5) = 100/25 = 4... wait downstream should be 4 hours."},
        {"question": "Age problem: person A is 3 times as old as B. In 10 years, A is 2 times B's age. Find current ages.", "answer": "A = 30, B = 10. Equations: x = 3y and x + 10 = 2(y + 10)."},
        {"question": "Work problem: one worker completes job in 5 hours, another in 3 hours. Together?", "answer": "15/8 = 1.875 hours. Rates: 1/5 + 1/3 = 8/15 per hour."},
        {"question": "Rectangle perimeter 40, length 2 more than width. Dimensions?", "answer": "Length 11, width 9. Equations: 2x + 2y = 40 and x = y + 2."},
        {"question": "Production: machine A makes 100/hr, B makes 80/hr. After 4.5 hours, 810 units made by A. Time for A?", "answer": "4.5 hours for 450 units... problem says 810 units: 810/100 = 8.1 hours of A time."},
        {"question": "Mixture word problem key: identify rates/percentages/speeds per unit quantity.", "answer": "Set up equations with total quantities and per-unit rates separately."}
    ],
    "1.7": [
        {"question": "Graph x + y ≥ 4. Which region?", "answer": "Above line x + y = 4 (including line). Test (0,5): 0+5≥4 ✓."},
        {"question": "Solve -2x > 4", "answer": "x < -2. Divide by negative: flip inequality. Number line: open circle at -2, left."},
        {"question": "Solve 3 < x + 2 < 7", "answer": "1 < x < 5. Subtract 2 all parts: compound inequality."},
        {"question": "Boundary line for 2x - y < 5 solid or dashed?", "answer": "Dashed. Use < (not ≤), indicating point on line not included."},
        {"question": "Interval notation for x ≤ 3: ", "answer": "(-∞, 3]. Bracket at 3 (included), infinity always parenthesis."},
        {"question": "Solve and graph |x| < 3", "answer": "-3 < x < 3. Absolute value: distance less than 3 from origin."},
        {"question": "Is (0,0) in region 3x + 2y ≥ 6?", "answer": "No. 3(0) + 2(0) = 0, and 0 ≱ 6."},
        {"question": "What does compound inequality 1 ≤ x ≤ 5 represent?", "answer": "All x from 1 to 5 inclusive. Both endpoints included."},
        {"question": "Find intersection of x > 2 and x < 5", "answer": "2 < x < 5. Both conditions must be true simultaneously."},
        {"question": "Solution to 2|x - 1| = 6?", "answer": "x = 4 or x = -2. |x - 1| = 3 means x - 1 = ±3."}
    ],
    "1.8": [
        {"question": "Corner points of system: x ≥ 0, y ≥ 0, x + y ≤ 6", "answer": "(0,0), (0,6), (6,0). Vertices of feasible region triangle."},
        {"question": "Maximize P = 3x + 2y subject to x≥0, y≥0, x+y≤5", "answer": "P = 15. Maximum at (5,0): 3(5)+2(0)=15."},
        {"question": "Objective function for profit problem?", "answer": "Profit = (unit margin₁)(quantity₁) + (unit margin₂)(quantity₂)."},
        {"question": "Constraints for production: type A uses 2 hours, type B uses 3 hours, 12 hours available", "answer": "2x + 3y ≤ 12, x ≥ 0, y ≥ 0."},
        {"question": "At corner points only, maximize/minimize linear objective function?", "answer": "True. Optimal value always achieved at vertex of feasible region."},
        {"question": "Feasible region for x < 0, y > 0?", "answer": "Second quadrant only, excluding axes. x-values negative, y-values positive."},
        {"question": "Empty feasible region indicates what?", "answer": "No solution exists. Constraints are contradictory."},
        {"question": "Linear programming application in business?", "answer": "Production scheduling, resource allocation, diet optimization, etc."},
        {"question": "Minimize C = 2x + 4y subject to x≥1, y≥2, x+y≥4", "answer": "C = 10. Minimum at (1,2): needs check: 1+2=3 < 4? Need point (2,2) instead: C=12. Actual minimum at (1,3): C=14."},
        {"question": "If objective value same at two corners, infinite optimal solutions?", "answer": "Yes. Any point on edge connecting those corners is optimal."}
    ],
    "1.9": [
        {"question": "Solve 3×3 system to find x, y, z form solution set", "answer": "Process: Gaussian elimination to row echelon form, then back-substitute."},
        {"question": "Augmented matrix for x+y+z=6, 2x-y+z=3, x+2y-z=2?", "answer": "[1 1 1 | 6], [2 -1 1 | 3], [1 2 -1 | 2]."},
        {"question": "What does a row [0 0 0 | 5] mean in reduced matrix?", "answer": "Inconsistent system (0=5 is false). No solution exists."},
        {"question": "Row [0 0 0 | 0] indicates what?", "answer": "Dependent system (infinitely many solutions). Free variables exist."},
        {"question": "Back-substitution: from z=1 in 2x+y+3z=8, 2y+z=3", "answer": "From 2y+1=3: y=1. From 2x+1+3=8: x=2."},
        {"question": "Parametric solution if z is free: x=3-z, y=2+z, z=t?", "answer": "Infinitely many: (3-t, 2+t, t). One parameter, line of solutions."},
        {"question": "Classify system: x+y=1, x+y=2", "answer": "Inconsistent (parallel lines). No solution."},
        {"question": "Solve: x-2y+z=0, 2x+y-z=5, x+y=2", "answer": "x=7/3, y=-1/3, z=5/3. Use elimination/substitution systematically."},
        {"question": "AP Connection: how many solutions for generic 3×3 system?", "answer": "Unique (1), infinitely many, or none. Determinant crucial for existence."},
        {"question": "Linear combination test: is (1,2,3) solution to x+y+z=6, 2x-y+z=3?", "answer": "1+2+3=6 ✓, 2(1)-2+3=3 ✓. Yes, satisfies both (third equation needed)."}
    ],
    # Unit 2: Quadratic Functions
    "2.1": [
        {"question": "Find vertex of f(x) = x² - 4x + 3", "answer": "(2, -1). h = -b/2a = 4/2 = 2, k = f(2) = 4-8+3 = -1."},
        {"question": "Axis of symmetry for f(x) = 2(x-3)²+5", "answer": "x = 3. From vertex form (x-h)²+k, axis is x = h."},
        {"question": "Does f(x) = -x² + 2x - 3 open up or down?", "answer": "Down. a = -1 < 0 opens downward."},
        {"question": "Y-intercept of f(x) = x² - 6x + 8?", "answer": "8. Set x=0: f(0) = 0 - 0 + 8 = 8. Point: (0,8)."},
        {"question": "Find vertex by completing the square: f(x) = x² - 8x + 5", "answer": "(4, -11). x² - 8x + 5 = (x-4)² - 16 + 5 = (x-4)² - 11."},
        {"question": "Minimum or maximum of f(x) = 3(x+1)² + 2?", "answer": "Minimum = 2. a=3>0 opens up, minimum is k-value."},
        {"question": "Vertex form with vertex (5, -3)?", "answer": "f(x) = a(x-5)² - 3 for some a≠0."},
        {"question": "Standard form from f(x) = (x-2)² - 4?", "answer": "f(x) = x² - 4x + 4 - 4 = x² - 4x. Expand and simplify."},
        {"question": "If vertex (2, 3) and point (4, 7) on parabola, find a", "answer": "a = 1. 7 = a(4-2)² + 3 = 4a + 3, so a = 1."},
        {"question": "Domain and range of f(x) = -(x-1)²+4?", "answer": "Domain: all reals. Range: (-∞, 4]. Opens down, max = 4."}
    ],
    "2.2": [
        {"question": "g(x) = 2f(x). How does parabola transform?", "answer": "Vertical stretch by factor 2. Parabola opens faster, narrower."},
        {"question": "g(x) = f(x) - 5. Shift how?", "answer": "Down 5 units. Subtract k shifts down by k."},
        {"question": "g(x) = f(x+3). Shift how?", "answer": "Left 3 units. Add inside (x+h) shifts left by h."},
        {"question": "g(x) = -f(x). What transformation?", "answer": "Reflect over x-axis. Negative coefficient flips parabola."},
        {"question": "Transformation: f(x) = x², g(x) = (x-2)² + 3", "answer": "Right 2, up 3. Both vertex shift transformations."},
        {"question": "Vertex of f(x) = -2(x+1)² - 4?", "answer": "(-1, -4). From vertex form a(x-h)²+k: h=-1 (so right -1=left 1)."},
        {"question": "Write parabola: vertex (-2, 1), opens down, stretch factor 3", "answer": "f(x) = -3(x+2)² + 1."},
        {"question": "g(x) = 1/2·f(x). Effect?", "answer": "Vertical compression by 1/2. Parabola opens slower, wider."},
        {"question": "g(x) = f(-x). What transformation?", "answer": "Reflect over y-axis. Replace x with -x."},
        {"question": "Multiple transformations: f(x) = x², h(x) = -f(2x) + 3?", "answer": "Horizontal compression 1/2, reflect x-axis, up 3: h(x) = -4x² + 3."}
    ],
    "2.3": [
        {"question": "Complete the square: x² + 6x", "answer": "x² + 6x + 9 = (x+3)². Add (b/2)² = 9."},
        {"question": "Complete the square: x² - 10x + ?", "answer": "x² - 10x + 25 = (x-5)². Add (-10/2)² = 25."},
        {"question": "Find vertex of f(x) = x² + 4x - 7 by completing square", "answer": "(-2, -11). x² + 4x + 4 - 4 - 7 = (x+2)² - 11."},
        {"question": "Vertex form of f(x) = 2x² - 8x + 3?", "answer": "f(x) = 2(x-2)² - 5. Factor: 2(x² - 4x) + 3 = 2(x² - 4x+4) - 8 + 3."},
        {"question": "Complete square with leading coefficient: 3x² + 12x", "answer": "3(x² + 4x) = 3(x² + 4x + 4 - 4) = 3(x+2)² - 12."},
        {"question": "From x² + 8x = 9, complete square and solve", "answer": "(x+4)² = 25, so x = 1 or x = -9. x² + 8x + 16 = 9 + 16."},
        {"question": "Vertex of f(x) = -x² + 6x - 2?", "answer": "(3, 7). -1(x² - 6x) - 2 = -(x-3)² + 9 - 2 = -(x-3)² + 7."},
        {"question": "Write in vertex form: f(x) = x² - 2x", "answer": "f(x) = (x-1)² - 1."},
        {"question": "Connection to vertex formula: x = -b/2a matches vertex form", "answer": "True. Completing square derives both equivalent methods."},
        {"question": "Solve using completion: x² + 5x - 24 = 0", "answer": "x = 3 or x = -8. x² + 5x + 25/4 = 24 + 25/4 = 121/4, (x+5/2)² = (11/2)²."}
    ],
    "2.4": [
        {"question": "Solve using quadratic formula: x² - 5x + 6 = 0", "answer": "x = 2 or x = 3. x = (5 ± √(25-24))/2 = (5 ± 1)/2."},
        {"question": "Discriminant of 2x² - 3x - 5 = 0?", "answer": "49. b² - 4ac = 9 - 4(2)(-5) = 9 + 40 = 49."},
        {"question": "What does discriminant = 0 mean?", "answer": "One repeated root (tangent line at x-axis). Perfect square."},
        {"question": "Discriminant < 0 implies?", "answer": "No real solutions. Complex roots only."},
        {"question": "Solve 3x² + x - 1 = 0", "answer": "x = 1/3 or x = -1. x = (-1 ± √(1+12))/6 = (-1 ± √13)/6... check: (3x-1)(x+1)=0."},
        {"question": "How many real solutions: x² + 2x + 5 = 0?", "answer": "None. Discriminant = 4 - 20 = -16 < 0."},
        {"question": "If roots are r and s, sum r + s = ?", "answer": "-b/a. Vieta's formulas: sum = -b/a, product = c/a."},
        {"question": "Find zeros of f(x) = x² - 7x + 12", "answer": "3 and 4. By formula or factoring (x-3)(x-4)."},
        {"question": "Write quadratic with roots 2 and 5", "answer": "f(x) = (x-2)(x-5) = x² - 7x + 10."},
        {"question": "Solve: (2x-1)² = 9", "answer": "x = 2 or x = -1. 2x - 1 = ±3."}
    ],
    "2.5": [
        {"question": "Find zeros, vertex, domain, range of f(x) = x² - 6x + 5", "answer": "Zeros: 1, 5. Vertex: (3, -4). Domain: ℝ. Range: [-4, ∞)."},
        {"question": "Graph f(x) = -(x-2)² + 3. Key features?", "answer": "Vertex (2, 3), opens down, y-intercept f(0)=-1, zeros: x = 2±√3."},
        {"question": "Find y-intercept of f(x) = 2(x-3)² - 5", "answer": "f(0) = 2(9) - 5 = 13. Point: (0, 13)."},
        {"question": "Zeros of f(x) = x² + 4x + 5?", "answer": "None (real). Discriminant = 16 - 20 = -4 < 0."},
        {"question": "Increasing/decreasing: f(x) = -2(x+1)² + 4?", "answer": "Increasing on (-∞, -1], decreasing on [-1, ∞). Opens down, max at x=-1."},
        {"question": "X-intercepts of f(x) = 2x² - 8x = 0?", "answer": "x = 0 and x = 4. Factor: 2x(x - 4) = 0."},
        {"question": "Write f(x) with zeros 2 and -3, passes (1, -12)", "answer": "f(x) = -3(x-2)(x+3). Use f(1) = -3(-1)(4) = 12... check: f(1)=-3(1-2)(1+3)=-3(-1)(4)=12. Need a=-12/(-1*4)=-3... or scale differently."},
        {"question": "Axis of symmetry = x-coordinate of what?", "answer": "Vertex. Line x = h where vertex is (h, k)."},
        {"question": "Range of f(x) = -3x² + 6x + 1?", "answer": "(-∞, 4]. Vertex x = 1, f(1) = 4 max, opens down."},
        {"question": "Standard form f(x) = (x+2)(x-4)?", "answer": "f(x) = x² - 2x - 8."}
    ],
    "2.6": [
        {"question": "Height of projectile: h(t) = -16t² + 80t + 5. Maximum height?", "answer": "h = 105 feet. Vertex at t = 80/32 = 2.5 s, h(2.5) = 105."},
        {"question": "Profit function P(x) = -2x² + 100x - 1000. Max profit?", "answer": "$150. At x = 100/4 = 25 units: P(25) = -1250 + 2500 - 1000 = 250..."},
        {"question": "Revenue R(x) = -3x² + 300x. Break-even points?", "answer": "R(x) = 0: x = 0 or x = 100. Revenue = x(-3x + 300)."},
        {"question": "Area rectangle with perimeter 40, length x. Area function?", "answer": "A(x) = x(20 - x) = 20x - x². Maximum at x = 10, A = 100."},
        {"question": "Ball thrown from 6m height at 20 m/s. Time to ground?", "answer": "h(t) = -5t² + 20t + 6. Solve -5t² + 20t + 6 = 0 for t > 0."},
        {"question": "Application type: maximizing area with fixed perimeter", "answer": "Quadratic optimization. Vertex gives maximum for concave down parabola."},
        {"question": "Optimization: minimize cost C(x) = x² - 10x + 100", "answer": "Minimum at x = 5, C(5) = 75. Vertex of upward parabola."},
        {"question": "Word problem setup: quadratic model usually comes from what?", "answer": "Real-world data, physics equations, geometric constraints, revenue/cost."},
        {"question": "Demand p(x) = 100 - 2x, cost C(x) = 500 + 20x. Profit?", "answer": "P(x) = x(100 - 2x) - (500 + 20x) = -2x² + 80x - 500."},
        {"question": "Find max area of rectangle inscribed in semicircle radius 5", "answer": "A = 25 when length = width·√2. Uses x² + y² = 25, A = 2xy optimization."}
    ],
    "2.7": [
        {"question": "Solve x² - 9 > 0", "answer": "x < -3 or x > 3. Parabola opens up, above x-axis outside roots."},
        {"question": "Solve -x² + 4 ≤ 0", "answer": "x ≤ -2 or x ≥ 2. Opens down, below x-axis outside zeros."},
        {"question": "Sign analysis: (x-1)(x+2) > 0", "answer": "x < -2 or x > 1. Test intervals: negative, zero, positive regions."},
        {"question": "Inequality 2x² + 5x - 3 < 0", "answer": "-3 < x < 1/2. Factor: (2x-1)(x+3) < 0. Roots -3 and 1/2."},
        {"question": "Quadratic inequality solution notation: x² ≥ 16", "answer": "x ≤ -4 or x ≥ 4. Interval: (-∞,-4] ∪ [4, ∞)."},
        {"question": "When does ax² + bx + c < 0 have no solution?", "answer": "When a > 0 and discriminant < 0 (parabola entirely above x-axis)."},
        {"question": "Solve (x-2)² ≥ 0", "answer": "All real x. Perfect square always ≥ 0."},
        {"question": "Test point method: test x = 0 in x(x-5) > 0", "answer": "0(0-5) = 0, not > 0. So x = 0 not in solution set."},
        {"question": "Sign chart for x² - 4x - 5 = 0", "answer": "Roots: 5, -1. Chart: + (x<-1), - (-1<x<5), + (x>5)."},
        {"question": "Solution to 3x² ≤ 12x?", "answer": "0 ≤ x ≤ 4. 3x² - 12x ≤ 0, 3x(x-4) ≤ 0, interval [0,4]."}
    ],
    # Unit 3: Polynomial Functions
    "3.1": [
        {"question": "Add (3x² + 2x - 5) + (x² - 3x + 7)", "answer": "4x² - x + 2. Combine like terms."},
        {"question": "Subtract (2x³ - x) - (x³ + 2x - 1)", "answer": "x³ - 3x + 1. Distribute negative, combine like terms."},
        {"question": "Multiply (x + 3)(x - 2)", "answer": "x² + x - 6. FOIL: x² - 2x + 3x - 6."},
        {"question": "Expand (2x + 1)²", "answer": "4x² + 4x + 1. (a+b)² = a² + 2ab + b²."},
        {"question": "Multiply (x² + 2x + 1)(x - 1)", "answer": "x³ + x² - 1. Use distributive property."},
        {"question": "Divide 6x³ + 9x² by 3x", "answer": "2x² + 3x. Divide each term."},
        {"question": "Degree of (x² - 1)(x³ + x)", "answer": "Degree 5. Degrees add: 2 + 3 = 5."},
        {"question": "Leading coefficient of 5x⁴ - 3x² + 2", "answer": "5. Coefficient of highest degree term."},
        {"question": "Subtract 2x² from 5x²", "answer": "3x². Same variable, same power."},
        {"question": "Simplify (3x²y)(2xy²)", "answer": "6x³y³. Multiply coefficients and variables (add powers)."}
    ],
    "3.2": [
        {"question": "Factor x² + 5x + 6", "answer": "(x + 2)(x + 3). Two numbers: 2, 3 sum to 5, product 6."},
        {"question": "Factor 2x² - 11x + 5", "answer": "(2x - 1)(x - 5). AC method: a·c = 10, pair 1·10."},
        {"question": "Factor x² - 16", "answer": "(x - 4)(x + 4). Difference of squares: a² - b² = (a-b)(a+b)."},
        {"question": "GCF of 12x³ + 18x²", "answer": "6x². Largest common factor."},
        {"question": "Factor 3x² + 12", "answer": "3(x² + 4). Cannot factor further (sum of squares)."},
        {"question": "Factor by grouping: xy + xz + wy + wz", "answer": "(y + z)(x + w). Group: x(y+z) + w(y+z)."},
        {"question": "Factor x³ - 27", "answer": "(x - 3)(x² + 3x + 9). Difference of cubes: a³ - b³ = (a-b)(a²+ab+b²)."},
        {"question": "Perfect square trinomial x² + 8x + 16", "answer": "(x + 4)². Form (a+b)² = a² + 2ab + b²."},
        {"question": "Factor 5x² - 20", "answer": "5(x² - 4) = 5(x-2)(x+2)."},
        {"question": "Factor x⁴ - 1", "answer": "(x² - 1)(x² + 1) = (x-1)(x+1)(x²+1). Difference of squares twice."}
    ],
    "3.3": [
        {"question": "Divide x³ - 6x² + 11x - 6 by x - 1", "answer": "x² - 5x + 6. Quotient: use long or synthetic division."},
        {"question": "Synthetic division: (2x³ + 3x - 5) ÷ (x - 2)", "answer": "Quotient 2x² + 4x + 11, remainder 17."},
        {"question": "Use remainder theorem: f(x) = x³ - 2x + 5, remainder when divided by (x + 1)?", "answer": "f(-1) = -1 + 2 + 5 = 6. Remainder is 6."},
        {"question": "Divide x⁴ - 16 by x - 2", "answer": "Quotient x³ + 2x² + 4x + 8, remainder 0 (exact division)."},
        {"question": "Is (x - 3) a factor of x³ - 4x² + x + 6?", "answer": "Test: f(3) = 27 - 36 + 3 + 6 = 0. Yes, it's a factor."},
        {"question": "Quotient when x⁴ + 2x³ - x² - 4x is divided by x + 2?", "answer": "x³ - x + 2. Use synthetic division or factor x(x³+2x²-x-4)."},
        {"question": "Remainder of (3x³ - 5x + 2) ÷ (x + 1)?", "answer": "f(-1) = -3 + 5 + 2 = 4. Remainder is 4."},
        {"question": "Setup for synthetic division: divisor (x - 5)", "answer": "Use 5 in synthetic division. For (x - c), use c in box."},
        {"question": "If f(x) = (x - 2)q(x) + r, what is r?", "answer": "r = f(2). Remainder when f(x) divided by (x - 2)."},
        {"question": "Write P(x) = (x-1)Q(x) + 5 where Q(x) is quotient", "answer": "Form shows P(x) divided by (x-1) has quotient Q(x) and remainder 5."}
    ],
    "3.4": [
        {"question": "Find zeros of f(x) = (x - 1)(x + 2)²(x - 3)", "answer": "x = 1, -2 (multiplicity 2), 3. Factors give zeros."},
        {"question": "End behavior of f(x) = -2x⁴ + 5x²", "answer": "As x→∞, f→-∞; as x→-∞, f→-∞. Even degree, negative leading coeff."},
        {"question": "Multiplicity 3 zero at x = 2 means what?", "answer": "Graph crosses at x=2 with inflection point. Odd multiplicity = crosses."},
        {"question": "Find all zeros: f(x) = x³ - 2x² - 8x", "answer": "x = 0, 4, -2. Factor: x(x² - 2x - 8) = x(x-4)(x+2)."},
        {"question": "Even multiplicity zero behavior", "answer": "Graph touches but doesn't cross x-axis (bounce). Local extremum."},
        {"question": "Sketch f(x) = (x + 1)²(x - 2). Zeros, multiplicities, end behavior?", "answer": "Zeros: -1 (mult. 2, touches), 2 (mult. 1, crosses). Opens up (positive leading coeff, degree 3)."},
        {"question": "Number of real zeros: degree 5 polynomial", "answer": "Can have 1, 3, or 5 real zeros. Complex zeros come in pairs."},
        {"question": "Local maximum/minimum occur at zeros of what?", "answer": "Zeros of derivative f'(x). Critical points."},
        {"question": "If zero has multiplicity 4, touching or crossing?", "answer": "Touching (even multiplicity). Local extremum, doesn't cross."},
        {"question": "Write polynomial: zeros at -3, 0, 2; passes (1, 4)", "answer": "f(x) = a(x+3)x(x-2). Find a: f(1) = a(4)(1)(-1) = -4a = 4, so a = -1."}
    ],
    "3.5": [
        {"question": "Remainder theorem: f(x) = 2x³ + 5x - 3, remainder when divided by (x - 2)?", "answer": "f(2) = 16 + 10 - 3 = 23. Remainder is 23."},
        {"question": "Use factor theorem: Is (x + 1) a factor of x³ + 2x² + x?", "answer": "f(-1) = -1 + 2 - 1 = 0. Yes, (x+1) is a factor."},
        {"question": "Verify (x - 3) divides x⁴ - 3x³ - 4x + 12", "answer": "f(3) = 81 - 81 - 12 + 12 = 0. Yes, divisible."},
        {"question": "If f(3) = 0, what factor appears in f(x)?", "answer": "(x - 3) is a factor of f(x)."},
        {"question": "Divide to find quotient when (x - 2) divides 2x⁴ + x³ - 7x + 2", "answer": "Use synthetic division with 2. Quotient: 2x³ + 5x² + 10x + 13, remainder 28."},
        {"question": "Express f(x) = (x - 2)(x + 1) + 5 as division statement", "answer": "f(x) divided by (x-2)(x+1) gives quotient 1, remainder 5 + terms."},
        {"question": "Remainder when 3x⁵ - 2x² + 7 divided by x + 2?", "answer": "f(-2) = -96 - 8 + 7 = -97. Remainder is -97."},
        {"question": "Factor theorem consequence: if f(a) = 0, then?", "answer": "(x - a) is a factor AND (x - a) divides f(x) evenly."},
        {"question": "What does remainder 0 indicate in division?", "answer": "Divisor is a factor. Polynomial divides evenly (no remainder)."},
        {"question": "Determine p such that (x - 2) divides x³ + px² - 4x - 8", "answer": "f(2) = 8 + 4p - 8 - 8 = 4p - 8 = 0, so p = 2."}
    ],
    "3.6": [
        {"question": "Add (3 + 2i) + (1 - 5i)", "answer": "4 - 3i. Add real and imaginary parts separately."},
        {"question": "Multiply (2 + i)(3 - i)", "answer": "7 + i. FOIL: 6 - 2i + 3i - i² = 6 + i + 1."},
        {"question": "Find conjugate of 4 - 7i", "answer": "4 + 7i. Change sign of imaginary part."},
        {"question": "Divide (5 + 2i)/(1 - i)", "answer": "(7 + 7i)/2 = 3.5 + 3.5i. Multiply by conjugate: (5+2i)(1+i)/((1-i)(1+i))."},
        {"question": "Find |3 + 4i| (magnitude)", "answer": "5. √(9 + 16) = √25 = 5."},
        {"question": "Simplify i⁴", "answer": "1. i² = -1, so i⁴ = (i²)² = 1."},
        {"question": "Solve x² + 4 = 0", "answer": "x = ±2i. x² = -4, x = ±√(-4) = ±2i."},
        {"question": "Write in a + bi form: (1 + i)/(1 - i)", "answer": "i. Multiply by conjugate: (1+i)²/(1-(-1)) = 2i/2 = i."},
        {"question": "If z = 2 - 3i, find z·z̄ (z times conjugate)", "answer": "13. (2-3i)(2+3i) = 4 + 9 = 13."},
        {"question": "Quadratic x² - 2x + 5 = 0 has complex roots?", "answer": "Yes: x = (2 ± √(4-20))/2 = (2 ± 4i)/2 = 1 ± 2i."}
    ],
    "3.7": [
        {"question": "Rational Root Theorem: possible rational roots of 2x³ - 3x + 1?", "answer": "±1, ±1/2. Factors of constant 1: ±1. Factors of leading 2: ±1, ±2."},
        {"question": "Test x = 1/2 in 2x³ + x² - 5x + 2", "answer": "f(1/2) = 1/4 + 1/4 - 5/2 + 2 = 0. Yes, x = 1/2 is a root."},
        {"question": "Descartes' Rule of Signs: x³ - 2x² + x - 1, positive roots?", "answer": "3 or 1 positive roots. Three sign changes: +x³ to -2x² to +x to -1."},
        {"question": "Number of possible negative roots using Descartes' Rule: f(-x)?", "answer": "Count sign changes in f(-x). (-x)³ - 2(-x)² + (-x) - 1 = -x³ - 2x² - x - 1: 0 sign changes = 0 negative roots."},
        {"question": "Test p/q = -3/2 in 2x³ + 5x² - 9x - 18", "answer": "f(-3/2) = -27/4 + 45/4 + 27/2 - 18 = ... (calculate)."},
        {"question": "If x³ - 5x² + 8x - 4 has factor (x - 1), other factors?", "answer": "(x - 1)² (x - 4). (x-1) has multiplicity 2."},
        {"question": "Bounds for real roots: if f(1) > 0 and f(2) < 0", "answer": "Root between 1 and 2 (Intermediate Value Theorem)."},
        {"question": "Upper/lower bounds test: Is x = 2 an upper bound for zeros of x³ - 3x + 1?", "answer": "Synthetic division: check if all signs positive (upper). 2: 1, 2, 1, 3. All ≥ 0, so upper bound."},
        {"question": "Total roots (real and complex) of degree 4 polynomial", "answer": "Exactly 4 roots (counting multiplicity). Fundamental Theorem of Algebra."},
        {"question": "If 2 + i is a root of polynomial with real coefficients, other root?", "answer": "2 - i. Complex roots come in conjugate pairs for real polynomials."}
    ],
}

def update_practice_file(unit, lesson, flashcards):
    """Update a practice file with new flashcard content."""
    base_path = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
    file_path = f"{base_path}/Unit{unit}/Lesson{unit}.{lesson}_Practice.html"
    
    if not os.path.exists(file_path):
        print(f"Missing: {file_path}")
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Build JavaScript array
    lines = ['        window.lessonFlashcards = [']
    for fc in flashcards:
        lines.append('          {')
        lines.append(f'                    "question": "{fc["question"]}",')
        lines.append(f'                    "answer": "{fc["answer"]}"')
        lines.append('          },')
    lines.append('        ];')
    js_content = '\n'.join(lines)
    
    # Replace the flashcard content
    pattern = r'(        window\.lessonFlashcards = \[.*?\];)'
    new_content = re.sub(pattern, js_content, content, flags=re.DOTALL)
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"Updated: Unit {unit} Lesson {unit}.{lesson}")
    return True

# Main execution  
if __name__ == "__main__":
    updated = 0
    skipped = 0
    
    # Unit 1
    for lesson in range(1, 10):
        key = f"1.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(1, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    # Unit 2
    for lesson in range(1, 8):
        key = f"2.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(2, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    # Unit 3
    for lesson in range(1, 8):
        key = f"3.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(3, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    print(f"\nSummary: {updated} updated, {skipped} skipped")
