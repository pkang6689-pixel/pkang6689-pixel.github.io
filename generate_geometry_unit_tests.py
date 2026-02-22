#!/usr/bin/env python3
"""
Generate Geometry Unit Test HTML files matching the Biology/Physics pattern.
Each test has: flashcard review (10 per lesson, all 4 games), 15-20 quiz questions.
Flashcards are read directly from the corresponding Practice files.
"""

import os
import re
import json

BASE = os.path.join(os.path.dirname(__file__), "ArisEdu Project Folder", "GeometryLessons")

# ── Unit topics and lesson names ──────────────────────────────────────────────

UNITS = {
    1: {
        "title": "Foundations of Geometry",
        "lessons": [
            "Points, Lines, and Planes",
            "Linear Measure and Precision",
            "Distance and Midpoints",
            "Angle Measure",
            "Angle Relationships",
            "Two-Dimensional Figures",
            "Three-Dimensional Figures",
        ],
        "next": "../Unit2/Lesson2.1_Video.html",
    },
    2: {
        "title": "Reasoning and Proof",
        "lessons": [
            "Inductive Reasoning and Conjecture",
            "Logic",
            "Conditional Statements",
            "Deductive Reasoning",
            "Postulates and Paragraph Proofs",
            "Algebraic Proof",
            "Proving Segment Relationships",
            "Proving Angle Relationships",
            "Proofs in Coordinate Geometry",
        ],
        "next": "../Unit3/Lesson3.1_Video.html",
    },
    3: {
        "title": "Parallel and Perpendicular Lines",
        "lessons": [
            "Parallel Lines and Transversals",
            "Angles and Parallel Lines",
            "Slopes of Lines",
            "Equations of Lines",
            "Proving Lines Parallel",
            "Perpendiculars and Distance",
            "Analytic Geometry Applications",
        ],
        "next": "../Unit4/Lesson4.1_Video.html",
    },
    4: {
        "title": "Congruent Triangles",
        "lessons": [
            "Classifying Triangles",
            "Angles of Triangles",
            "Congruent Triangles",
            "Proving Congruence: SSS, SAS",
            "Proving Congruence: ASA, AAS",
            "Isosceles and Equilateral Triangles",
            "Congruence Transformations",
            "Triangles and Coordinate Proof",
        ],
        "next": "../Unit5/Lesson5.1_Video.html",
    },
    5: {
        "title": "Relationships in Triangles",
        "lessons": [
            "Bisectors of Triangles",
            "Medians and Altitudes of Triangles",
            "Inequalities in One Triangle",
            "Indirect Proof",
            "The Triangle Inequality",
            "Inequalities in Two Triangles",
        ],
        "next": "../Unit6/Lesson6.1_Video.html",
    },
    6: {
        "title": "Quadrilaterals",
        "lessons": [
            "Angles of Polygons",
            "Parallelograms",
            "Tests for Parallelograms",
            "Rectangles",
            "Rhombi and Squares",
            "Kites and Trapezoids",
            "Regular Polygons and Symmetry",
        ],
        "next": "../Unit7/Lesson7.1_Video.html",
    },
    7: {
        "title": "Similarity",
        "lessons": [
            "Ratios and Proportions",
            "Similar Polygons",
            "Similar Triangles",
            "Parallel Lines and Proportional Parts",
            "Parts of Similar Triangles",
            "Similarity Transformations",
            "Scale Drawings and Models",
            "Fractals and Self-Similarity",
        ],
        "next": "../Unit8/Lesson8.1_Video.html",
    },
    8: {
        "title": "Right Triangles and Trigonometry",
        "lessons": [
            "Geometric Mean",
            "The Pythagorean Theorem and Its Converse",
            "Special Right Triangles",
            "Trigonometry",
            "Angles of Elevation and Depression",
            "The Law of Sines and Cosines",
            "Vectors",
            "Polar Coordinates and Complex Numbers",
        ],
        "next": "../Unit9/Lesson9.1_Video.html",
    },
    9: {
        "title": "Transformations",
        "lessons": [
            "Reflections",
            "Translations",
            "Rotations",
            "Compositions of Transformations",
            "Symmetry",
            "Dilations",
            "Transformations in the Coordinate Plane",
        ],
        "next": "../Unit10/Lesson10.1_Video.html",
    },
    10: {
        "title": "Circles",
        "lessons": [
            "Circles and Circumference",
            "Measuring Angles and Arcs",
            "Arcs and Chords",
            "Inscribed Angles",
            "Tangents",
            "Secants, Tangents, and Angle Measures",
            "Special Segments in a Circle",
            "Equations of Circles",
            "Conic Sections (intro)",
        ],
        "next": "../Unit11/Lesson11.1_Video.html",
    },
    11: {
        "title": "Areas of Polygons and Circles",
        "lessons": [
            "Areas of Parallelograms and Triangles",
            "Areas of Trapezoids, Rhombi, and Kites",
            "Areas of Circles and Sectors",
            "Areas of Regular Polygons and Composite Figures",
            "Areas of Similar Figures",
            "Integration in Area Calculations",
        ],
        "next": "../Unit12/Lesson12.1_Video.html",
    },
    12: {
        "title": "Three-Dimensional Geometry",
        "lessons": [
            "Representations of Three-Dimensional Figures",
            "Surface Areas of Prisms and Cylinders",
            "Surface Areas of Pyramids and Cones",
            "Volumes of Prisms and Cylinders",
            "Volumes of Pyramids and Cones",
            "Surface Areas and Volumes of Spheres",
            "Spherical Geometry",
            "Congruent and Similar Solids",
            "Cavalieri's Principle and Applications",
        ],
        "next": "../Unit13/Lesson13.1_Video.html",
    },
    13: {
        "title": "Probability and Statistics in Geometry",
        "lessons": [
            "Representing Sample Spaces",
            "Permutations and Combinations",
            "Geometric Probability",
            "Simulations",
            "Probabilities of Independent and Dependent Events",
            "Probabilities of Mutually Exclusive Events",
            "Monte Carlo Methods in Geometry",
        ],
        "next": "../../geometry.html",
    },
}

# ── Quiz questions per unit ────────────────────────────────────────────────────

QUIZ = {
    1: [
        ("Which of the following is undefined in geometry?", "Point", "Line segment", "Point, line, and plane", "Angle", "c"),
        ("Two points determine exactly one:", "Plane", "Line", "Ray", "Circle", "b"),
        ("The intersection of two distinct planes is:", "A point", "A line", "A plane", "Empty", "b"),
        ("Three non-collinear points determine:", "A line", "A ray", "A plane", "A segment", "c"),
        ("What is the precision of a ruler marked in centimeters?", "1 cm", "0.5 cm", "0.1 cm", "10 cm", "b"),
        ("Points that lie on the same line are called:", "Coplanar", "Collinear", "Concurrent", "Congruent", "b"),
        ("The midpoint of a segment divides it into:", "Two unequal parts", "Two congruent segments", "A ray and a segment", "Three parts", "b"),
        ("The distance formula is derived from:", "The midpoint formula", "The Pythagorean theorem", "The slope formula", "The quadratic formula", "b"),
        ("What does a protractor measure?", "Length", "Area", "Angles", "Volume", "c"),
        ("Two angles whose measures sum to 90° are:", "Supplementary", "Complementary", "Vertical", "Adjacent", "b"),
        ("Two angles whose measures sum to 180° are:", "Complementary", "Vertical", "Supplementary", "Linear", "c"),
        ("Vertical angles are always:", "Supplementary", "Complementary", "Congruent", "Adjacent", "c"),
        ("A polygon with 5 sides is called a:", "Hexagon", "Pentagon", "Quadrilateral", "Octagon", "b"),
        ("The sum of interior angles of a triangle is:", "90°", "180°", "270°", "360°", "b"),
        ("A solid with two parallel, congruent circular bases is a:", "Cone", "Sphere", "Cylinder", "Prism", "c"),
        ("How many faces does a rectangular prism have?", "4", "5", "6", "8", "c"),
        ("A point in 3D space is specified by how many coordinates?", "1", "2", "3", "4", "c"),
        ("The midpoint formula for (x₁,y₁) and (x₂,y₂) is:", "((x₁+x₂)/2, (y₁+y₂)/2)", "(x₁−x₂, y₁−y₂)", "(x₁·x₂, y₁·y₂)", "((x₂−x₁)/2, (y₂−y₁)/2)", "a"),
    ],
    2: [
        ("Inductive reasoning uses:", "Definitions to prove", "Specific examples to form a general conclusion", "General rules to reach specific conclusions", "Postulates only", "b"),
        ("A counterexample is used to:", "Prove a conjecture true", "Disprove a conjecture", "Support a theorem", "Define a term", "b"),
        ("The statement 'If p, then q' is called a:", "Conjunction", "Disjunction", "Conditional", "Biconditional", "c"),
        ("The converse of 'If p, then q' is:", "If q, then p", "If not p, then not q", "If not q, then not p", "p if and only if q", "a"),
        ("The contrapositive of 'If p, then q' is:", "If q, then p", "If not p, then not q", "If not q, then not p", "Not p or q", "c"),
        ("A statement and its contrapositive are:", "Sometimes equivalent", "Always equivalent", "Never equivalent", "Converses", "b"),
        ("Deductive reasoning starts with:", "Specific observations", "A hypothesis only", "General principles or known facts", "Guesses", "c"),
        ("The Law of Detachment states: If p→q is true and p is true, then:", "q is false", "p is false", "q is true", "Nothing can be concluded", "c"),
        ("The Law of Syllogism lets you chain:", "Two conditionals", "A conditional and its converse", "Two biconditionals", "Definitions only", "a"),
        ("A postulate is a statement that is:", "Proven", "Accepted without proof", "Always false", "A conjecture", "b"),
        ("A theorem is a statement that:", "Needs no proof", "Has been proven", "Is always a postulate", "Cannot be proven", "b"),
        ("In a two-column proof, the left column contains:", "Reasons", "Statements", "Definitions", "Diagrams", "b"),
        ("The Reflexive Property states a = :", "b", "0", "a", "−a", "c"),
        ("The Symmetric Property states if a = b, then:", "a = a", "b = a", "a ≠ b", "b = 0", "b"),
        ("The Transitive Property states if a = b and b = c, then:", "a = 0", "a = c", "b = 0", "c = a + b", "b"),
        ("Which property justifies: If AB = CD, then CD = AB?", "Reflexive", "Symmetric", "Transitive", "Substitution", "b"),
        ("The Segment Addition Postulate states that if B is between A and C:", "AB = BC", "AB + BC = AC", "AB − BC = AC", "AC = 2·AB", "b"),
        ("Which is NOT a valid proof format?", "Two-column", "Paragraph", "Flowchart", "Scatter plot", "d"),
    ],
    3: [
        ("A transversal is a line that:", "Is parallel to two lines", "Intersects two or more lines", "Is perpendicular to one line", "Never crosses another line", "b"),
        ("Alternate interior angles formed by parallel lines and a transversal are:", "Supplementary", "Complementary", "Congruent", "Unrelated", "c"),
        ("Co-interior (same-side interior) angles are:", "Congruent", "Complementary", "Supplementary", "Vertical", "c"),
        ("Corresponding angles formed by parallel lines and a transversal are:", "Supplementary", "Congruent", "Complementary", "Obtuse", "b"),
        ("The slope of a horizontal line is:", "Undefined", "1", "0", "−1", "c"),
        ("The slope of a vertical line is:", "0", "1", "Undefined", "−1", "c"),
        ("Two non-vertical parallel lines have:", "Opposite slopes", "Perpendicular slopes", "Equal slopes", "No slopes", "c"),
        ("The slopes of two perpendicular lines are:", "Equal", "Negative reciprocals", "Both zero", "Both undefined", "b"),
        ("Slope-intercept form of a line is:", "Ax + By = C", "y = mx + b", "y − y₁ = m(x − x₁)", "(y₂−y₁)/(x₂−x₁)", "b"),
        ("Point-slope form of a line is:", "y = mx + b", "Ax + By = C", "y − y₁ = m(x − x₁)", "x = a", "c"),
        ("If two lines are cut by a transversal and alternate exterior angles are congruent, then the lines are:", "Perpendicular", "Skew", "Parallel", "Intersecting", "c"),
        ("The shortest distance from a point to a line is the:", "Diagonal", "Horizontal distance", "Perpendicular distance", "Hypotenuse", "c"),
        ("Lines in the same plane that never intersect are:", "Skew", "Perpendicular", "Concurrent", "Parallel", "d"),
        ("Lines that are not in the same plane and do not intersect are:", "Parallel", "Perpendicular", "Skew", "Concurrent", "c"),
        ("What is the slope of a line through (2, 3) and (6, 11)?", "1", "2", "3", "4", "b"),
        ("Which equation represents a line parallel to y = 3x + 1?", "y = −3x + 5", "y = 3x − 7", "y = (1/3)x + 1", "y = −(1/3)x + 2", "b"),
    ],
    4: [
        ("A triangle with all sides congruent is:", "Isosceles", "Scalene", "Equilateral", "Right", "c"),
        ("A triangle with exactly two congruent sides is:", "Equilateral", "Scalene", "Isosceles", "Obtuse", "c"),
        ("The sum of the measures of the interior angles of a triangle is:", "90°", "180°", "270°", "360°", "b"),
        ("An exterior angle of a triangle equals:", "The sum of the two remote interior angles", "The adjacent interior angle", "Half the opposite angle", "180°", "a"),
        ("CPCTC stands for:", "Congruent Parts of Congruent Triangles are Congruent", "Corresponding Pairs of Connected Triangles are Congruent", "Central Points Create Two Congruences", "Congruent Polygons Create True Congruences", "a"),
        ("SSS congruence requires:", "Two sides and an included angle", "Three pairs of congruent sides", "Two angles and a side", "A right angle and hypotenuse", "b"),
        ("SAS congruence requires:", "Three sides", "Two sides and the included angle", "Two angles and a side", "Two sides and a non-included angle", "b"),
        ("ASA congruence requires:", "Two angles and the included side", "Two sides and an angle", "Three angles", "Two angles only", "a"),
        ("AAS congruence requires:", "Two angles and a non-included side", "Two sides and an angle", "Three angles", "Hypotenuse and leg", "a"),
        ("Which is NOT a valid triangle congruence theorem?", "SSS", "SAS", "SSA", "ASA", "c"),
        ("The base angles of an isosceles triangle are:", "Supplementary", "Complementary", "Congruent", "Right angles", "c"),
        ("An equilateral triangle is also:", "Right", "Scalene", "Equiangular", "Obtuse", "c"),
        ("Each angle in an equilateral triangle measures:", "45°", "60°", "90°", "120°", "b"),
        ("A congruence transformation preserves:", "Only angles", "Only distances", "Both distances and angles", "Neither", "c"),
        ("In a coordinate proof, a right triangle is often placed with legs on:", "Diagonal lines", "The x- and y-axes", "Parallel lines", "A circle", "b"),
        ("If △ABC ≅ △DEF, which angle is congruent to ∠B?", "∠D", "∠E", "∠F", "∠A", "b"),
        ("HL congruence applies only to:", "All triangles", "Right triangles", "Isosceles triangles", "Equilateral triangles", "b"),
        ("Two triangles are congruent if:", "They have the same shape", "All corresponding parts are equal", "They have equal area", "They share a side", "b"),
    ],
    5: [
        ("The perpendicular bisector of a segment passes through the segment's:", "Endpoint", "Midpoint", "Vertex", "Exterior", "b"),
        ("Any point on the perpendicular bisector of a segment is:", "Equidistant from the endpoints", "Closer to one endpoint", "On the segment", "At the midpoint", "a"),
        ("The point where the three perpendicular bisectors of a triangle meet is the:", "Incenter", "Centroid", "Circumcenter", "Orthocenter", "c"),
        ("The circumcenter is the center of the:", "Inscribed circle", "Circumscribed circle", "Triangle itself", "Median", "b"),
        ("The incenter is equidistant from the:", "Vertices", "Sides", "Midpoints", "Altitudes", "b"),
        ("A median of a triangle connects a vertex to the:", "Opposite vertex", "Midpoint of the opposite side", "Foot of the altitude", "Perpendicular bisector", "b"),
        ("The centroid divides each median in the ratio:", "1:1", "1:2", "2:1", "3:1", "c"),
        ("The centroid is also called the:", "Circumcenter", "Center of gravity", "Incenter", "Orthocenter", "b"),
        ("An altitude of a triangle is perpendicular to the:", "Median", "Angle bisector", "Opposite side (or its extension)", "Adjacent side", "c"),
        ("The orthocenter is the intersection of the:", "Medians", "Perpendicular bisectors", "Altitudes", "Angle bisectors", "c"),
        ("In a triangle, the longest side is opposite the:", "Smallest angle", "Right angle always", "Largest angle", "Median", "c"),
        ("The Triangle Inequality states the sum of any two sides must be:", "Equal to the third", "Less than the third", "Greater than the third", "Half the third", "c"),
        ("Can a triangle have sides 3, 4, and 8?", "Yes", "No, because 3 + 4 < 8", "No, because 3 + 8 < 4", "Only if it is right", "b"),
        ("In an indirect proof you start by:", "Assuming the conclusion is true", "Assuming the conclusion is false", "Drawing a diagram", "Using induction", "b"),
        ("The Hinge Theorem (SAS Inequality) compares:", "Two triangles with two pairs of congruent sides", "Two congruent triangles", "Two similar triangles", "Right triangles only", "a"),
        ("If two sides of one triangle are congruent to two sides of another and the included angle of the first is larger, then:", "The third side of the first is smaller", "The third side of the first is larger", "The triangles are congruent", "The third sides are equal", "b"),
    ],
    6: [
        ("The sum of interior angles of an n-sided polygon is:", "180n", "(n − 2)·180°", "360°", "n·90°", "b"),
        ("Each interior angle of a regular hexagon measures:", "90°", "108°", "120°", "135°", "c"),
        ("The sum of the exterior angles of any convex polygon is:", "180°", "270°", "360°", "720°", "c"),
        ("A parallelogram has:", "One pair of parallel sides", "Two pairs of parallel sides", "No parallel sides", "Four right angles", "b"),
        ("Opposite angles of a parallelogram are:", "Supplementary", "Complementary", "Congruent", "Right", "c"),
        ("The diagonals of a parallelogram:", "Are perpendicular", "Are congruent", "Bisect each other", "Are parallel", "c"),
        ("To prove a quadrilateral is a parallelogram, you can show:", "Both pairs of opposite sides are congruent", "It has four sides", "It has one right angle", "Diagonals are congruent", "a"),
        ("A rectangle is a parallelogram with:", "Four congruent sides", "Four right angles", "Perpendicular diagonals", "No parallel sides", "b"),
        ("The diagonals of a rectangle are:", "Perpendicular", "Congruent", "Neither", "Parallel", "b"),
        ("A rhombus is a parallelogram with:", "Four right angles", "Congruent diagonals", "Four congruent sides", "One pair of parallel sides", "c"),
        ("The diagonals of a rhombus are:", "Congruent", "Perpendicular bisectors of each other", "Parallel", "Equal to the sides", "b"),
        ("A square is both a:", "Trapezoid and kite", "Rectangle and rhombus", "Kite and parallelogram", "Pentagon and quadrilateral", "b"),
        ("A trapezoid has exactly:", "Two pairs of parallel sides", "One pair of parallel sides", "No parallel sides", "Four congruent sides", "b"),
        ("The midsegment of a trapezoid is parallel to the bases and equals:", "The sum of the bases", "Half the sum of the bases", "The difference of the bases", "Twice the shorter base", "b"),
        ("A kite has:", "Two pairs of consecutive congruent sides", "Two pairs of parallel sides", "All sides congruent", "No congruent sides", "a"),
        ("A regular polygon has:", "All sides and all angles congruent", "Only congruent sides", "Only congruent angles", "No lines of symmetry", "a"),
        ("How many lines of symmetry does a regular pentagon have?", "3", "4", "5", "10", "c"),
        ("An isosceles trapezoid has:", "Congruent legs", "Congruent bases", "Perpendicular diagonals", "No congruent parts", "a"),
    ],
    7: [
        ("A ratio compares two quantities by:", "Addition", "Division", "Multiplication", "Subtraction", "b"),
        ("A proportion is:", "An equation stating two ratios are equal", "A sum of two fractions", "A product of two ratios", "An inequality", "a"),
        ("In a/b = c/d, the cross products are:", "a·c and b·d", "a·d and b·c", "a+d and b+c", "a−d and b−c", "b"),
        ("Two polygons are similar if corresponding angles are congruent and sides are:", "Equal", "Proportional", "Perpendicular", "Parallel", "b"),
        ("The scale factor is the ratio of:", "Areas of similar figures", "Corresponding side lengths", "Perimeters", "Angles", "b"),
        ("AA Similarity requires:", "Two pairs of congruent angles", "Two pairs of congruent sides", "Three congruent angles", "SSS", "a"),
        ("SAS Similarity requires two proportional sides and:", "Any angle", "The included angle congruent", "An exterior angle", "A right angle", "b"),
        ("SSS Similarity requires:", "All three pairs of sides proportional", "All three angles congruent", "Two sides and an angle", "One pair of proportional sides", "a"),
        ("If a line is parallel to one side of a triangle and intersects the other two sides, it divides them:", "Equally", "Proportionally", "Perpendicularly", "Randomly", "b"),
        ("The Triangle Proportionality Theorem involves a line parallel to:", "The longest side", "One side of the triangle", "The altitude", "The median", "b"),
        ("An altitude to the hypotenuse of a right triangle creates:", "Two congruent triangles", "Two similar triangles", "Two right triangles similar to the original", "Two isosceles triangles", "c"),
        ("A similarity transformation preserves:", "Distances only", "Angle measures", "Area", "Perimeter", "b"),
        ("A dilation with scale factor 2:", "Halves all lengths", "Doubles all lengths", "Keeps lengths the same", "Squares all lengths", "b"),
        ("If two similar triangles have a scale factor of 3:1, their areas have a ratio of:", "3:1", "6:1", "9:1", "27:1", "c"),
        ("A scale drawing has a scale of 1 cm = 5 m. A 3 cm line represents:", "8 m", "10 m", "15 m", "20 m", "c"),
        ("A fractal is a figure that exhibits:", "Self-similarity at different scales", "Congruent sides", "Right angles only", "Parallel sides only", "a"),
    ],
    8: [
        ("The geometric mean of a and b is:", "(a + b)/2", "√(ab)", "ab", "a/b", "b"),
        ("In a right triangle, the Pythagorean theorem states:", "a + b = c", "a² + b² = c²", "a² − b² = c²", "(a + b)² = c²", "b"),
        ("The converse of the Pythagorean theorem is used to:", "Find the hypotenuse", "Determine if a triangle is right", "Find the area", "Find an angle", "b"),
        ("A Pythagorean triple is a set of three positive integers where:", "a + b = c", "a² + b² = c²", "a · b = c", "a/b = c", "b"),
        ("Which is a Pythagorean triple?", "(2, 3, 4)", "(3, 4, 5)", "(1, 2, 3)", "(4, 5, 6)", "b"),
        ("In a 45-45-90 triangle, the hypotenuse equals a leg times:", "2", "√2", "√3", "3", "b"),
        ("In a 30-60-90 triangle, the side opposite 30° is:", "The longest side", "Half the hypotenuse", "Equal to the hypotenuse", "√3 times the shortest", "b"),
        ("In a 30-60-90 triangle, the side opposite 60° equals the short leg times:", "2", "√2", "√3", "3", "c"),
        ("sin θ in a right triangle equals:", "adjacent/hypotenuse", "opposite/hypotenuse", "opposite/adjacent", "hypotenuse/opposite", "b"),
        ("cos θ in a right triangle equals:", "opposite/hypotenuse", "adjacent/hypotenuse", "opposite/adjacent", "hypotenuse/adjacent", "b"),
        ("tan θ in a right triangle equals:", "adjacent/hypotenuse", "opposite/hypotenuse", "opposite/adjacent", "adjacent/opposite", "c"),
        ("An angle of elevation is measured from:", "The vertical up", "The horizontal up to a line of sight", "The top down", "The ground to the base", "b"),
        ("An angle of depression is measured from:", "The horizontal down to a line of sight", "The ground upward", "The vertical to a line", "The base to the top", "a"),
        ("The Law of Sines states: a/sin A =", "b/sin A", "b/sin B", "c/sin A", "a/sin B", "b"),
        ("The Law of Cosines is used when you know:", "Two angles and a side (AAS)", "Three angles only", "Two sides and the included angle (SAS) or three sides", "Only one side", "c"),
        ("A vector has both:", "Length and width", "Magnitude and direction", "Area and perimeter", "Slope and intercept", "b"),
        ("The magnitude of vector ⟨3, 4⟩ is:", "5", "7", "12", "25", "a"),
        ("In polar coordinates, a point is described by:", "(x, y)", "(r, θ)", "(m, b)", "(a, b, c)", "b"),
    ],
    9: [
        ("A reflection is a transformation that:", "Slides a figure", "Flips a figure over a line", "Rotates a figure", "Enlarges a figure", "b"),
        ("In a reflection over the y-axis, (x, y) maps to:", "(x, −y)", "(−x, y)", "(−x, −y)", "(y, x)", "b"),
        ("In a reflection over the x-axis, (x, y) maps to:", "(−x, y)", "(x, −y)", "(−x, −y)", "(y, x)", "b"),
        ("A translation slides every point:", "The same distance in the same direction", "Different distances", "Around a center", "Toward a line", "a"),
        ("A translation (x, y) → (x + 3, y − 2) moves a figure:", "3 left, 2 up", "3 right, 2 down", "3 right, 2 up", "3 left, 2 down", "b"),
        ("A rotation turns a figure about a fixed point called the:", "Vertex", "Midpoint", "Center of rotation", "Origin only", "c"),
        ("A 90° counterclockwise rotation maps (x, y) to:", "(y, −x)", "(−y, x)", "(−x, −y)", "(x, −y)", "b"),
        ("A 180° rotation maps (x, y) to:", "(−y, x)", "(y, −x)", "(−x, −y)", "(x, y)", "c"),
        ("A composition of transformations applies:", "Only one transformation", "Two or more transformations in sequence", "Transformations randomly", "No transformations", "b"),
        ("A glide reflection is a combination of:", "Two rotations", "A translation and a reflection", "Two reflections", "A dilation and a rotation", "b"),
        ("A figure has line symmetry if it can be folded along a line so the halves:", "Are perpendicular", "Match exactly", "Are supplementary", "Are different", "b"),
        ("A figure has rotational symmetry if it maps onto itself after a rotation of less than:", "360°", "180°", "90°", "45°", "a"),
        ("A dilation changes:", "Only the shape", "Only the size", "Both shape and size", "Neither shape nor size", "b"),
        ("A dilation with scale factor k > 1 is:", "A reduction", "An enlargement", "An isometry", "A reflection", "b"),
        ("A dilation with scale factor 0 < k < 1 is:", "An enlargement", "A reduction", "A rotation", "A reflection", "b"),
        ("An isometry preserves:", "Size and shape", "Only shape", "Only angles", "Only area", "a"),
        ("Which transformation is NOT an isometry?", "Reflection", "Rotation", "Translation", "Dilation", "d"),
    ],
    10: [
        ("The distance around a circle is called the:", "Diameter", "Radius", "Circumference", "Area", "c"),
        ("The circumference of a circle with radius r is:", "πr", "2πr", "πr²", "2r", "b"),
        ("A central angle has its vertex at the:", "Edge of the circle", "Center of the circle", "On the chord", "Outside the circle", "b"),
        ("The measure of a minor arc equals:", "Half the central angle", "The central angle", "Twice the central angle", "180° minus the central angle", "b"),
        ("A semicircle has an arc measure of:", "90°", "180°", "270°", "360°", "b"),
        ("Two chords are congruent if and only if their corresponding arcs are:", "Supplementary", "Complementary", "Congruent", "Perpendicular", "c"),
        ("A diameter that is perpendicular to a chord:", "Is parallel to the chord", "Bisects the chord and its arc", "Equals the chord", "Is tangent to the circle", "b"),
        ("An inscribed angle is formed by two:", "Radii", "Tangents", "Chords with a vertex on the circle", "Secants from outside", "c"),
        ("An inscribed angle is half the measure of its:", "Central angle with the same arc", "Intercepted chord", "Diameter", "Tangent", "a"),
        ("An angle inscribed in a semicircle is:", "Acute", "Obtuse", "A right angle (90°)", "Straight (180°)", "c"),
        ("A tangent line intersects a circle at exactly:", "Zero points", "One point", "Two points", "Infinite points", "b"),
        ("A tangent is perpendicular to the radius at the point of:", "Center", "Chord", "Tangency", "Secant", "c"),
        ("Two tangent segments from the same external point are:", "Perpendicular", "Parallel", "Congruent", "Supplementary", "c"),
        ("When two secants intersect inside a circle, the angle equals:", "The sum of intercepted arcs divided by 2", "The difference of arcs", "The product of arcs", "The intercepted arc", "a"),
        ("When two secants intersect outside a circle, the angle equals:", "Half the sum of intercepted arcs", "Half the difference of intercepted arcs", "The sum of the arcs", "The product of the arcs", "b"),
        ("The standard equation of a circle with center (h, k) and radius r is:", "(x−h)² + (y−k)² = r²", "(x+h)² + (y+k)² = r", "x² + y² = r", "(x−h) + (y−k) = r²", "a"),
        ("Conic sections include circles, ellipses, parabolas, and:", "Rectangles", "Hyperbolas", "Pentagons", "Trapezoids", "b"),
        ("If a chord is 6 cm long and the radius is 5 cm, the distance from center to chord is:", "3 cm", "4 cm", "5 cm", "2 cm", "b"),
    ],
    11: [
        ("The area of a parallelogram is:", "s²", "base × height", "½ × base × height", "π × r²", "b"),
        ("The area of a triangle is:", "base × height", "½ × base × height", "2 × base × height", "base + height", "b"),
        ("The area of a trapezoid is:", "b₁ × b₂ × h", "½ × (b₁ + b₂) × h", "(b₁ + b₂) × h", "½ × b₁ × b₂", "b"),
        ("The area of a rhombus can be found using:", "½ × d₁ × d₂", "side²", "base × height only", "π × r²", "a"),
        ("The area of a circle with radius r is:", "2πr", "πr²", "πd", "2πr²", "b"),
        ("A sector is a region bounded by:", "Two chords", "Two radii and an arc", "A diameter and a chord", "Two tangents", "b"),
        ("The area of a sector with central angle θ (in degrees) is:", "(θ/360)·πr²", "(θ/180)·πr²", "θ·πr²", "2θ·r²", "a"),
        ("The apothem of a regular polygon is:", "A side length", "The distance from center to a vertex", "The perpendicular distance from center to a side", "The diagonal", "c"),
        ("The area of a regular polygon is:", "½ × perimeter × apothem", "perimeter × apothem", "side² × n", "½ × side × apothem", "a"),
        ("A composite figure's area is found by:", "Multiplying component areas", "Adding (or subtracting) areas of simpler shapes", "Squaring the perimeter", "Dividing by the number of shapes", "b"),
        ("If two similar figures have a scale factor of k, their areas have a ratio of:", "k", "2k", "k²", "k³", "c"),
        ("If the scale factor between two similar triangles is 2:3, the ratio of their areas is:", "2:3", "4:9", "8:27", "1:1", "b"),
        ("The area of a kite equals:", "½ × d₁ × d₂", "base × height", "side²", "perimeter × apothem", "a"),
        ("Arc length of a sector with angle θ° and radius r is:", "(θ/360)·2πr", "(θ/180)·πr", "θ·r²", "2θ·r", "a"),
        ("The area of an equilateral triangle with side s is:", "s²", "(√3/4)·s²", "½·s²", "s²·√2", "b"),
        ("If a circle has area 49π, its radius is:", "49", "7", "14", "24.5", "b"),
    ],
    12: [
        ("An orthographic drawing shows an object from:", "One perspective view", "Multiple flat views (top, front, side)", "A 3D rotated view", "Only the top", "b"),
        ("The lateral area of a prism is:", "The sum of all faces", "The sum of the lateral (non-base) faces", "The area of one base", "Volume divided by height", "b"),
        ("The surface area of a rectangular prism is:", "lwh", "2lw + 2lh + 2wh", "l + w + h", "6s²", "b"),
        ("The surface area of a cylinder is:", "2πrh", "2πr² + 2πrh", "πr²h", "2πr(r + h)", "b"),
        ("The lateral area of a cone is:", "πrl (where l is slant height)", "πr²", "πr²h", "2πrh", "a"),
        ("The surface area of a cone is:", "πrl + πr²", "πr²l", "2πrl", "πr²h + πrl", "a"),
        ("The volume of a prism is:", "lateral area × height", "Base area × height", "½ × Base area × height", "2 × Base area × height", "b"),
        ("The volume of a cylinder is:", "2πrh", "πr²h", "πrh²", "(4/3)πr³", "b"),
        ("The volume of a pyramid is:", "Base area × height", "½ × Base area × height", "⅓ × Base area × height", "¼ × Base area × height", "c"),
        ("The volume of a cone is:", "πr²h", "½πr²h", "⅓πr²h", "2πr²h", "c"),
        ("The surface area of a sphere is:", "2πr²", "3πr²", "4πr²", "πr²", "c"),
        ("The volume of a sphere is:", "(4/3)πr³", "(3/4)πr³", "4πr³", "πr³", "a"),
        ("In spherical geometry, the shortest path between two points on a sphere is a:", "Chord", "Diameter", "Great circle arc", "Tangent line", "c"),
        ("In spherical geometry, 'lines' are:", "Straight lines", "Great circles", "Small circles", "Tangent lines", "b"),
        ("Two similar solids with scale factor k have volume ratio:", "k", "k²", "k³", "2k", "c"),
        ("Two similar solids with scale factor k have surface area ratio:", "k", "k²", "k³", "2k", "b"),
        ("Cavalieri's Principle states that if two solids have equal cross-sectional areas at every height, they have equal:", "Surface areas", "Volumes", "Heights", "Base areas", "b"),
        ("The slant height of a pyramid is the distance from:", "The apex to the base center", "The apex to the midpoint of a base edge", "The center to a vertex", "The base to the top along an edge", "b"),
    ],
    13: [
        ("A sample space is:", "The set of all possible outcomes", "A single outcome", "The probability of an event", "The complement of an event", "a"),
        ("A tree diagram is used to:", "Calculate area", "Show all possible outcomes systematically", "Prove congruence", "Find the mean", "b"),
        ("The number of permutations of n objects taken r at a time is:", "n!/(n−r)!", "n!/r!", "n!/(r!(n−r)!)", "r!/n!", "a"),
        ("The number of combinations of n objects taken r at a time is:", "n!/(n−r)!", "n!/r!", "n!/(r!(n−r)!)", "r·n", "c"),
        ("Permutations differ from combinations because permutations:", "Ignore order", "Consider order", "Are always larger", "Use only addition", "b"),
        ("Geometric probability uses:", "Counting outcomes", "Ratios of lengths, areas, or volumes", "Tree diagrams only", "Factorials", "b"),
        ("A dart lands randomly on a 10 × 10 square. A circle of radius 3 is inside. P(landing in circle) ≈:", "28.3%", "9%", "30%", "50%", "a"),
        ("A simulation is used to:", "Prove a theorem", "Model a real-world situation using random processes", "Construct a figure", "Measure angles", "b"),
        ("Two events are independent if:", "One event affects the other", "The occurrence of one does not affect the other", "They cannot happen together", "They always happen together", "b"),
        ("P(A and B) for independent events equals:", "P(A) + P(B)", "P(A) × P(B)", "P(A) − P(B)", "P(A) / P(B)", "b"),
        ("Two events are dependent if:", "P(A) = P(B)", "The occurrence of one affects the probability of the other", "They are mutually exclusive", "They are independent", "b"),
        ("Mutually exclusive events:", "Can both occur", "Cannot both occur at the same time", "Are always independent", "Have equal probability", "b"),
        ("P(A or B) for mutually exclusive events equals:", "P(A) × P(B)", "P(A) + P(B)", "P(A) − P(B)", "1 − P(A)", "b"),
        ("P(A or B) for non-mutually exclusive events equals:", "P(A) + P(B)", "P(A) + P(B) − P(A and B)", "P(A) × P(B)", "1 − P(A∩B)", "b"),
        ("The complement of event A is:", "A itself", "All outcomes not in A", "The intersection of A and B", "The union of A and B", "b"),
        ("P(A) + P(A') =", "0", "0.5", "1", "2", "c"),
        ("Monte Carlo methods use:", "Algebraic formulas only", "Random sampling to estimate results", "Exact measurements", "Compass and straightedge", "b"),
        ("Monte Carlo can estimate π by:", "Random points in a square with an inscribed circle", "Counting prime numbers", "Measuring a circle", "Using a protractor", "a"),
    ],
}

# ── Flashcard extraction from Practice files ──────────────────────────────────

# Lesson counts per unit (determined by directory listing)
LESSON_COUNTS = {
    1: 7, 2: 9, 3: 7, 4: 8, 5: 6, 6: 7, 7: 8, 8: 8, 9: 7, 10: 9, 11: 6, 12: 9, 13: 7
}


def extract_flashcards_from_practice(filepath):
    """Extract flashcard data from a Practice HTML file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the lessonFlashcards array
    match = re.search(r'window\.lessonFlashcards\s*=\s*\[(.*?)\];', content, re.DOTALL)
    if not match:
        return []

    block = match.group(1)
    cards = []
    # Match each { question: '...', answer: '...' } pair
    for m in re.finditer(r"""\{\s*question:\s*(['"])(.*?)\1\s*,\s*answer:\s*(['"])(.*?)\3\s*\}""", block, re.DOTALL):
        q = m.group(2).replace("\\'", "'").replace('\\"', '"').replace("\\n", "\n")
        a = m.group(4).replace("\\'", "'").replace('\\"', '"').replace("\\n", "\n")
        cards.append((q, a))
    return cards


def load_all_flashcards():
    """Load flashcards from all Practice files, organized by unit."""
    flashcards = {}
    for unit_num, lesson_count in LESSON_COUNTS.items():
        unit_cards = []
        for lesson in range(1, lesson_count + 1):
            practice_path = os.path.join(BASE, f"Unit{unit_num}",
                                         f"Lesson{unit_num}.{lesson}_Practice.html")
            if os.path.exists(practice_path):
                cards = extract_flashcards_from_practice(practice_path)
                unit_cards.extend(cards)
                print(f"    Lesson {unit_num}.{lesson}: {len(cards)} flashcards")
            else:
                print(f"    WARNING: {practice_path} not found!")
        flashcards[unit_num] = unit_cards
    return flashcards


# ── Fallback flashcard data (used only if Practice files are missing) ─────────

FLASHCARDS_FALLBACK = {
    1: [
        ("What is a point?", "A location in space with no size; represented by a dot"),
        ("What is a line?", "An infinite set of points extending in two directions; has no width"),
        ("What is a plane?", "A flat surface that extends infinitely in all directions"),
        ("What are collinear points?", "Points that lie on the same line"),
        ("What are coplanar points?", "Points that lie on the same plane"),
        ("What is a line segment?", "Part of a line with two endpoints"),
        ("What is a ray?", "Part of a line with one endpoint, extending infinitely in one direction"),
        ("What is the distance formula?", "d = √((x₂−x₁)² + (y₂−y₁)²)"),
        ("What is the midpoint formula?", "M = ((x₁+x₂)/2, (y₁+y₂)/2)"),
        ("What is an angle?", "Two rays that share a common endpoint (vertex)"),
        ("What is an acute angle?", "An angle measuring less than 90°"),
        ("What is a right angle?", "An angle measuring exactly 90°"),
        ("What is an obtuse angle?", "An angle measuring more than 90° but less than 180°"),
        ("What are complementary angles?", "Two angles whose measures sum to 90°"),
        ("What are supplementary angles?", "Two angles whose measures sum to 180°"),
        ("What are vertical angles?", "Two non-adjacent angles formed by intersecting lines; always congruent"),
        ("What is a linear pair?", "Two adjacent angles that form a straight line (sum to 180°)"),
        ("What is a polygon?", "A closed plane figure formed by three or more line segments"),
        ("What is a regular polygon?", "A polygon with all sides and all angles congruent"),
        ("What is a polyhedron?", "A three-dimensional figure with flat polygon faces"),
        ("What is a prism?", "A polyhedron with two parallel, congruent bases connected by rectangular faces"),
        ("What is a pyramid?", "A polyhedron with a polygon base and triangular faces meeting at an apex"),
        ("What is a cylinder?", "A solid with two parallel circular bases connected by a curved surface"),
        ("What is a cone?", "A solid with a circular base and a vertex (apex) not in the plane of the base"),
        ("What is a sphere?", "A set of all points equidistant from a center point in three dimensions"),
        ("What does congruent mean?", "Having the same size and shape"),
        ("What does perpendicular mean?", "Lines or segments that intersect at 90° angles"),
        ("What is precision in measurement?", "The smallest unit of measure used; half the smallest unit gives the error"),
    ],
    2: [
        ("What is inductive reasoning?", "Reasoning from specific examples to a general conclusion"),
        ("What is a conjecture?", "An unproven statement based on observations"),
        ("What is a counterexample?", "A single example that disproves a conjecture"),
        ("What is deductive reasoning?", "Reasoning from general principles to specific conclusions"),
        ("What is a conditional statement?", "A statement in if-then form: If p, then q"),
        ("What is the hypothesis?", "The 'if' part (p) of a conditional statement"),
        ("What is the conclusion?", "The 'then' part (q) of a conditional statement"),
        ("What is the converse?", "Switching hypothesis and conclusion: If q, then p"),
        ("What is the inverse?", "Negating both parts: If not p, then not q"),
        ("What is the contrapositive?", "Negating and switching: If not q, then not p; always same truth value as original"),
        ("What is a biconditional?", "A statement true in both directions: p if and only if q"),
        ("What is the Law of Detachment?", "If p→q is true and p is true, then q is true"),
        ("What is the Law of Syllogism?", "If p→q and q→r are true, then p→r is true"),
        ("What is a postulate?", "A statement accepted as true without proof"),
        ("What is a theorem?", "A statement that has been proven true"),
        ("What is a two-column proof?", "A proof with statements in one column and reasons in another"),
        ("What is a paragraph proof?", "A proof written as sentences in paragraph form"),
        ("What is a flowchart proof?", "A proof using boxes and arrows to show logical flow"),
        ("State the Reflexive Property.", "a = a (any quantity equals itself)"),
        ("State the Symmetric Property.", "If a = b, then b = a"),
        ("State the Transitive Property.", "If a = b and b = c, then a = c"),
        ("State the Substitution Property.", "If a = b, then a can replace b in any expression"),
        ("What is the Segment Addition Postulate?", "If B is between A and C, then AB + BC = AC"),
        ("What is the Angle Addition Postulate?", "If D is in the interior of ∠ABC, then m∠ABD + m∠DBC = m∠ABC"),
        ("What is a coordinate proof?", "A proof that uses coordinate geometry and algebra to prove geometric statements"),
    ],
    3: [
        ("What are parallel lines?", "Coplanar lines that never intersect"),
        ("What are skew lines?", "Non-coplanar lines that never intersect"),
        ("What is a transversal?", "A line that intersects two or more lines at different points"),
        ("What are corresponding angles?", "Angles in the same position relative to the transversal and the two lines"),
        ("What are alternate interior angles?", "Non-adjacent interior angles on opposite sides of the transversal"),
        ("What are alternate exterior angles?", "Non-adjacent exterior angles on opposite sides of the transversal"),
        ("What are co-interior (same-side interior) angles?", "Interior angles on the same side of the transversal; supplementary when lines are parallel"),
        ("What is slope?", "The ratio of vertical change to horizontal change: m = (y₂−y₁)/(x₂−x₁)"),
        ("What is slope-intercept form?", "y = mx + b, where m is slope and b is y-intercept"),
        ("What is point-slope form?", "y − y₁ = m(x − x₁)"),
        ("What is standard form of a line?", "Ax + By = C, where A, B, C are integers"),
        ("How are parallel line slopes related?", "Parallel lines have equal slopes"),
        ("How are perpendicular line slopes related?", "Their slopes are negative reciprocals (m₁ · m₂ = −1)"),
        ("How do you prove lines are parallel?", "Show that alternate interior angles are congruent, corresponding angles are congruent, or co-interior angles are supplementary"),
        ("What is the distance from a point to a line?", "The length of the perpendicular segment from the point to the line"),
        ("What is the Parallel Postulate?", "Through a point not on a line, exactly one line can be drawn parallel to the given line"),
    ],
    4: [
        ("What is a scalene triangle?", "A triangle with no congruent sides"),
        ("What is an isosceles triangle?", "A triangle with at least two congruent sides"),
        ("What is an equilateral triangle?", "A triangle with all three sides congruent"),
        ("What is an acute triangle?", "A triangle where all angles are less than 90°"),
        ("What is an obtuse triangle?", "A triangle with one angle greater than 90°"),
        ("What is a right triangle?", "A triangle with one 90° angle"),
        ("What is the Triangle Angle Sum Theorem?", "The sum of the interior angles of a triangle is 180°"),
        ("What is the Exterior Angle Theorem?", "An exterior angle of a triangle equals the sum of the two remote interior angles"),
        ("What does congruent triangles mean?", "Triangles with all corresponding sides and angles equal"),
        ("What is CPCTC?", "Corresponding Parts of Congruent Triangles are Congruent"),
        ("What is SSS Congruence?", "If three sides of one triangle are congruent to three sides of another, the triangles are congruent"),
        ("What is SAS Congruence?", "If two sides and the included angle of one triangle are congruent to those of another, the triangles are congruent"),
        ("What is ASA Congruence?", "If two angles and the included side are congruent, the triangles are congruent"),
        ("What is AAS Congruence?", "If two angles and a non-included side are congruent, the triangles are congruent"),
        ("Why is SSA not a valid congruence theorem?", "It can produce two different triangles (the ambiguous case)"),
        ("What is HL Congruence?", "If the hypotenuse and one leg of a right triangle are congruent to those of another, the triangles are congruent"),
        ("What is the Isosceles Triangle Theorem?", "If two sides of a triangle are congruent, the angles opposite them are congruent"),
        ("What is a congruence transformation?", "A transformation (reflection, rotation, translation) that preserves size and shape"),
    ],
    5: [
        ("What is a perpendicular bisector?", "A line perpendicular to a segment at its midpoint"),
        ("What is the Perpendicular Bisector Theorem?", "Any point on the perpendicular bisector is equidistant from the segment's endpoints"),
        ("What is an angle bisector?", "A ray that divides an angle into two congruent angles"),
        ("What is the circumcenter?", "The point where the three perpendicular bisectors meet; center of the circumscribed circle"),
        ("What is the incenter?", "The point where the three angle bisectors meet; center of the inscribed circle"),
        ("What is a median?", "A segment from a vertex to the midpoint of the opposite side"),
        ("What is the centroid?", "The point where the three medians meet; divides each median in 2:1 ratio"),
        ("What is an altitude of a triangle?", "A perpendicular segment from a vertex to the line containing the opposite side"),
        ("What is the orthocenter?", "The point where the three altitudes meet"),
        ("State the Triangle Inequality Theorem.", "The sum of any two side lengths must be greater than the third side"),
        ("What is an indirect proof?", "A proof by contradiction: assume the opposite, show it leads to a contradiction"),
        ("What is the Hinge Theorem?", "If two sides of one triangle are congruent to two sides of another and the included angle is larger, the opposite side is longer"),
        ("What is the Converse of the Hinge Theorem?", "If two sides are congruent and the third side is longer, then the included angle opposite it is larger"),
        ("In any triangle, the largest angle is opposite the:", "Longest side"),
        ("In any triangle, the smallest angle is opposite the:", "Shortest side"),
    ],
    6: [
        ("What is the interior angle sum of a polygon with n sides?", "(n − 2) · 180°"),
        ("What is the measure of each interior angle of a regular n-gon?", "(n − 2) · 180° / n"),
        ("What is the sum of exterior angles of any convex polygon?", "360°"),
        ("What is a parallelogram?", "A quadrilateral with both pairs of opposite sides parallel"),
        ("What are properties of a parallelogram?", "Opposite sides congruent, opposite angles congruent, diagonals bisect each other, consecutive angles supplementary"),
        ("How do you prove a quadrilateral is a parallelogram?", "Show both pairs of opposite sides parallel, or congruent, or diagonals bisect each other, or one pair both parallel and congruent"),
        ("What is a rectangle?", "A parallelogram with four right angles"),
        ("What special property do rectangle diagonals have?", "They are congruent"),
        ("What is a rhombus?", "A parallelogram with four congruent sides"),
        ("What special property do rhombus diagonals have?", "They are perpendicular bisectors of each other"),
        ("What is a square?", "A rectangle and rhombus; four right angles and four congruent sides"),
        ("What is a trapezoid?", "A quadrilateral with exactly one pair of parallel sides (bases)"),
        ("What is an isosceles trapezoid?", "A trapezoid with congruent non-parallel sides (legs)"),
        ("What is the midsegment of a trapezoid?", "The segment connecting the midpoints of the legs; parallel to both bases and equal to half their sum"),
        ("What is a kite?", "A quadrilateral with two pairs of consecutive congruent sides"),
        ("What properties do kite diagonals have?", "One diagonal is the perpendicular bisector of the other"),
        ("What is a regular polygon?", "A polygon with all sides and all angles congruent"),
        ("How many lines of symmetry does a regular n-gon have?", "n lines of symmetry"),
    ],
    7: [
        ("What is a ratio?", "A comparison of two quantities by division"),
        ("What is a proportion?", "An equation stating two ratios are equal: a/b = c/d"),
        ("What is the Cross-Products Property?", "If a/b = c/d, then ad = bc"),
        ("What are similar polygons?", "Polygons with congruent corresponding angles and proportional corresponding sides"),
        ("What is the scale factor?", "The ratio of corresponding side lengths of similar figures"),
        ("What is AA Similarity?", "If two angles of one triangle are congruent to two angles of another, the triangles are similar"),
        ("What is SAS Similarity?", "If two sides are proportional and the included angle is congruent, the triangles are similar"),
        ("What is SSS Similarity?", "If all three pairs of sides are proportional, the triangles are similar"),
        ("What is the Triangle Proportionality Theorem?", "A line parallel to one side of a triangle divides the other two sides proportionally"),
        ("What is the converse of the Triangle Proportionality Theorem?", "If a line divides two sides proportionally, it is parallel to the third side"),
        ("What is the Triangle Angle Bisector Theorem?", "An angle bisector divides the opposite side in the ratio of the adjacent sides"),
        ("How are perimeters of similar figures related?", "In the same ratio as the scale factor"),
        ("How are areas of similar figures related?", "In the ratio of the scale factor squared"),
        ("What is a dilation?", "A transformation that changes size but preserves shape; centered at a point with a scale factor"),
        ("What is a scale drawing?", "A drawing that uses a scale to represent an object proportionally"),
        ("What is a fractal?", "A geometric figure where each part is a reduced-scale copy of the whole"),
    ],
    8: [
        ("What is the geometric mean of a and b?", "√(ab) — the positive number x where a/x = x/b"),
        ("State the Pythagorean Theorem.", "In a right triangle, a² + b² = c² where c is the hypotenuse"),
        ("What is the converse of the Pythagorean Theorem?", "If a² + b² = c², then the triangle is a right triangle"),
        ("What is a Pythagorean triple?", "Three positive integers that satisfy a² + b² = c² (e.g., 3, 4, 5)"),
        ("What are the side ratios in a 45-45-90 triangle?", "1 : 1 : √2"),
        ("What are the side ratios in a 30-60-90 triangle?", "1 : √3 : 2"),
        ("Define sine (sin θ).", "Opposite side / Hypotenuse"),
        ("Define cosine (cos θ).", "Adjacent side / Hypotenuse"),
        ("Define tangent (tan θ).", "Opposite side / Adjacent side"),
        ("What is SOH-CAH-TOA?", "Sin = Opp/Hyp, Cos = Adj/Hyp, Tan = Opp/Adj — a mnemonic for trig ratios"),
        ("What is an angle of elevation?", "The angle from the horizontal looking up to an object"),
        ("What is an angle of depression?", "The angle from the horizontal looking down to an object"),
        ("State the Law of Sines.", "a/sin A = b/sin B = c/sin C"),
        ("When do you use the Law of Sines?", "When you know AAS, ASA, or SSA (ambiguous case)"),
        ("State the Law of Cosines.", "c² = a² + b² − 2ab·cos C"),
        ("When do you use the Law of Cosines?", "When you know SAS or SSS"),
        ("What is a vector?", "A quantity with both magnitude and direction"),
        ("How do you find the magnitude of vector ⟨a, b⟩?", "|v| = √(a² + b²)"),
        ("What are polar coordinates?", "A system using (r, θ) — distance from origin and angle from positive x-axis"),
        ("How do you convert polar to rectangular?", "x = r·cos θ, y = r·sin θ"),
    ],
    9: [
        ("What is a transformation?", "A function that moves or changes a figure in the plane"),
        ("What is a pre-image?", "The original figure before a transformation"),
        ("What is an image?", "The resulting figure after a transformation"),
        ("What is a reflection?", "A flip over a line (line of reflection)"),
        ("Reflection over x-axis: (x, y) →", "(x, −y)"),
        ("Reflection over y-axis: (x, y) →", "(−x, y)"),
        ("Reflection over y = x: (x, y) →", "(y, x)"),
        ("What is a translation?", "A slide that moves every point the same distance and direction"),
        ("Translation by ⟨a, b⟩: (x, y) →", "(x + a, y + b)"),
        ("What is a rotation?", "A turn about a fixed center point"),
        ("90° counterclockwise rotation: (x, y) →", "(−y, x)"),
        ("180° rotation: (x, y) →", "(−x, −y)"),
        ("270° counterclockwise (= 90° clockwise): (x, y) →", "(y, −x)"),
        ("What is a composition of transformations?", "Applying two or more transformations in sequence"),
        ("What is a glide reflection?", "A translation followed by a reflection over a line parallel to the translation"),
        ("What is line symmetry?", "A figure can be folded along a line so both halves match"),
        ("What is rotational symmetry?", "A figure maps onto itself after a rotation of less than 360°"),
        ("What is a dilation?", "A transformation that changes size by a scale factor, centered at a point"),
        ("What is an isometry?", "A transformation that preserves distance and angle measure (reflection, rotation, translation)"),
        ("Is a dilation an isometry?", "No — it changes size (unless scale factor is 1)"),
    ],
    10: [
        ("What is a circle?", "The set of all points equidistant from a center point"),
        ("What is a radius?", "A segment from the center to any point on the circle"),
        ("What is a diameter?", "A chord that passes through the center; equals 2 × radius"),
        ("What is the circumference formula?", "C = 2πr = πd"),
        ("What is a chord?", "A segment with both endpoints on the circle"),
        ("What is a central angle?", "An angle with its vertex at the center of the circle"),
        ("What is a minor arc?", "An arc less than 180°; its measure equals the central angle"),
        ("What is a major arc?", "An arc greater than 180°; measure = 360° − minor arc"),
        ("What is a semicircle?", "An arc that measures exactly 180°; endpoints are a diameter"),
        ("What is an inscribed angle?", "An angle with vertex on the circle and sides that are chords"),
        ("What is the Inscribed Angle Theorem?", "An inscribed angle is half the measure of its intercepted arc"),
        ("What is Thales' Theorem?", "An angle inscribed in a semicircle is a right angle (90°)"),
        ("What is a tangent line?", "A line that touches the circle at exactly one point"),
        ("What is the tangent-radius relationship?", "A tangent is perpendicular to the radius at the point of tangency"),
        ("What is a secant?", "A line that intersects the circle at two points"),
        ("When two chords intersect inside a circle, what relationship holds?", "The products of their segments are equal"),
        ("What is the standard equation of a circle?", "(x − h)² + (y − k)² = r², center (h, k), radius r"),
        ("What are the four conic sections?", "Circle, ellipse, parabola, hyperbola"),
    ],
    11: [
        ("Area of a parallelogram?", "A = base × height"),
        ("Area of a triangle?", "A = ½ × base × height"),
        ("Area of a trapezoid?", "A = ½ × (b₁ + b₂) × h"),
        ("Area of a rhombus (using diagonals)?", "A = ½ × d₁ × d₂"),
        ("Area of a kite (using diagonals)?", "A = ½ × d₁ × d₂"),
        ("Area of a circle?", "A = πr²"),
        ("Area of a sector (degrees)?", "A = (θ/360) × πr²"),
        ("Arc length formula?", "L = (θ/360) × 2πr"),
        ("What is an apothem?", "The perpendicular distance from the center to a side of a regular polygon"),
        ("Area of a regular polygon?", "A = ½ × perimeter × apothem"),
        ("How do you find the area of a composite figure?", "Break it into simpler shapes, find each area, then add or subtract"),
        ("If scale factor is k, how do areas compare?", "Area ratio = k²"),
        ("If two similar triangles have scale factor 3:5, what is their area ratio?", "9:25"),
        ("Area of an equilateral triangle with side s?", "A = (√3/4)s²"),
        ("What is a sector?", "A 'pie slice' region bounded by two radii and an arc"),
        ("What is a segment of a circle?", "The region between a chord and its arc"),
    ],
    12: [
        ("What is a polyhedron?", "A 3D solid bounded by polygonal faces"),
        ("What is Euler's formula for polyhedra?", "V − E + F = 2 (Vertices − Edges + Faces = 2)"),
        ("What is lateral area?", "The sum of the areas of the non-base faces of a solid"),
        ("Surface area of a rectangular prism?", "SA = 2lw + 2lh + 2wh"),
        ("Surface area of a cylinder?", "SA = 2πr² + 2πrh"),
        ("Volume of a prism?", "V = Bh (base area × height)"),
        ("Volume of a cylinder?", "V = πr²h"),
        ("Surface area of a pyramid?", "SA = B + ½Pl (base area + ½ × perimeter × slant height)"),
        ("Surface area of a cone?", "SA = πr² + πrl (base + lateral)"),
        ("Volume of a pyramid?", "V = ⅓Bh"),
        ("Volume of a cone?", "V = ⅓πr²h"),
        ("Surface area of a sphere?", "SA = 4πr²"),
        ("Volume of a sphere?", "V = (4/3)πr³"),
        ("What is spherical geometry?", "Geometry on the surface of a sphere where 'lines' are great circles"),
        ("What is a great circle?", "The intersection of a sphere with a plane through its center; the largest circle on a sphere"),
        ("How do similar solids relate?", "Scale factor k → surface area ratio k², volume ratio k³"),
        ("What is Cavalieri's Principle?", "Two solids with equal cross-sectional areas at every height have equal volumes"),
        ("What is a net?", "A 2D pattern that folds into a 3D solid"),
        ("What is a cross section?", "The intersection of a 3D solid with a plane"),
    ],
    13: [
        ("What is a sample space?", "The set of all possible outcomes of an experiment"),
        ("What is an event?", "A subset of the sample space"),
        ("What is experimental probability?", "Probability estimated from actual trials: favorable outcomes / total trials"),
        ("What is theoretical probability?", "Probability calculated from expected outcomes: P(E) = favorable / total"),
        ("What is a permutation?", "An arrangement where order matters: P(n,r) = n!/(n−r)!"),
        ("What is a combination?", "A selection where order does not matter: C(n,r) = n!/(r!(n−r)!)"),
        ("What is n! (factorial)?", "n! = n × (n−1) × (n−2) × ... × 2 × 1; 0! = 1"),
        ("What is geometric probability?", "Probability based on comparing geometric measures (lengths, areas, volumes)"),
        ("What is a simulation?", "Using a model (often with random numbers) to imitate a real situation"),
        ("What are independent events?", "Events where the outcome of one does not affect the other"),
        ("P(A and B) for independent events?", "P(A) × P(B)"),
        ("What are dependent events?", "Events where the outcome of one affects the other's probability"),
        ("P(A and B) for dependent events?", "P(A) × P(B|A)"),
        ("What are mutually exclusive events?", "Events that cannot occur simultaneously"),
        ("P(A or B) for mutually exclusive events?", "P(A) + P(B)"),
        ("P(A or B) in general?", "P(A) + P(B) − P(A and B)"),
        ("What is the complement of event A?", "All outcomes not in A; P(A') = 1 − P(A)"),
        ("What is the Monte Carlo method?", "Using random sampling and geometric probability to estimate values (like π)"),
    ],
}


def escape_html(s):
    """Escape only characters that would break HTML attributes or content."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def escape_js(s):
    """Escape for JS string literal inside double quotes."""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("'", "\\'").replace("\n", "\\n")


def build_quiz_html(questions):
    """Build all quiz question HTML blocks."""
    parts = []
    for i, (text, a, b, c, d, correct) in enumerate(questions, 1):
        parts.append(f'''<div class="quiz-question" data-attempts="2" style="margin-bottom: 2rem;">
<div class="attempts-indicator">Attempts left: 2</div>
<p style="font-weight: 700; font-size: 1.1rem; margin-bottom: 1rem;">{i}. {escape_html(text)}</p>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q{i}" style="margin-right:0.5rem;" type="radio" value="a"/> {escape_html(a)}
</label>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q{i}" style="margin-right:0.5rem;" type="radio" value="b"/> {escape_html(b)}
</label>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q{i}" style="margin-right:0.5rem;" type="radio" value="c"/> {escape_html(c)}
</label>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q{i}" style="margin-right:0.5rem;" type="radio" value="d"/> {escape_html(d)}
</label>
<button class="side-button" onclick="checkQuizAnswer('q{i}', '{correct}', this)" style="margin-top:0.5rem; font-size:1rem; padding:0.5rem 1rem; min-width:auto;" type="button">Check Answer</button>
<button class="side-button" onclick="getAnotherQuestion(this)" style="margin-top:0.5rem; font-size:1rem; padding:0.5rem 1rem; min-width:auto; margin-left:0.5rem; background: #64748b;" type="button">Get another question</button>
</div>''')
    return "\n".join(parts)


def build_flashcard_js(cards):
    """Build the window.lessonFlashcards JS array."""
    items = []
    for q, a in cards:
        items.append(f'        {{ question: "{escape_js(q)}", answer: "{escape_js(a)}" }}')
    return "    window.lessonFlashcards = [\n" + ",\n".join(items) + "\n    ];"


def build_file(unit_num, unit_info, questions, cards):
    """Build the complete HTML for a Unit Test file — includes all 4 games."""
    title = unit_info["title"]
    quiz_html = build_quiz_html(questions)
    flashcard_js = build_flashcard_js(cards)

    back_label = "Back to Geometry"
    back_url = "../../geometry.html"

    return f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Unit {unit_num}: Unit Test</title>
<script src="/_sdk/element_sdk.js"></script>
<script src="../../scripts/global_translations.js?v=3.2"></script>
<script src="/quiz_logic.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;family=Playfair+Display:wght@700&amp;display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
<style>@view-transition {{ navigation: auto; }}</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
<script src="../../theme_manager.js"></script>
</head>
<body class="dark-mode h-full">
<script src="../../scripts/taskbar.js"></script>
<main class="main-container">
<div id="practice-content-view">
<h2 class="page-title">Unit {unit_num} Review Flashcards</h2>
<div class="diagram-card">
<div class="flashcard-game" id="flashcard-game" style="margin-top:2rem;display:flex;flex-direction:column;align-items:center;perspective:1000px;overflow:hidden;">
<div class="flashcard-box" id="flashcard" style="background:#fff;border-radius:1rem;box-shadow:0 2px 8px rgba(0,0,0,0.12);padding:2rem 3rem;display:flex;align-items:center;justify-content:center;text-align:center;min-width:calc(320px + 56rem);min-height:calc(120px + 24rem);font-weight:600;color:#0f172a;margin-bottom:1rem;cursor:pointer;transition:background 0.2s, color 0.2s;">
<span id="flashcard-content" style="width:100%;display:block;"></span>
</div>
<div style="display:flex;gap:1rem;">
<button id="prev-flashcard" style="background:#ef4444;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">
<svg fill="none" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg">
<path d="M15 6l-6 6 6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path>
</svg>
</button>
<button id="next-flashcard" style="background:#10b981;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">
<svg fill="none" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg">
<path d="M9 6l6 6-6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path>
</svg>
</button>
<button id="shuffle-flashcard" title="Shuffle flashcards">
<svg fill="none" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
<path d="M4 4h7l-1.5 1.5M20 20h-7l1.5-1.5M4 20l16-16" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path>
</svg>
Shuffle
</button>
<span id="flashcard-counter" style="display:flex;align-items:center;font-weight:600;font-size:1rem;color:#64748b;white-space:nowrap;"></span>
</div>
</div>
<div id="climb-game-container" style="display:none; width:100%;"> <div id="climb-game-ui" style="height: 100%; display:flex; flex-direction:column; position:relative; overflow:hidden; background-color: #e2e8f0; border-radius: 1rem; height: 64rem; font-family: \'Orbitron\', sans-serif;">
<div id="climb-space-bg" style="position:absolute; top:0; left:0; width:100%; height:100%; background: radial-gradient(ellipse at bottom, #1e293b 0%, #020617 100%); z-index:0; overflow:hidden;">
<div id="climb-stars" style="position:absolute; top:0; left:0; width:100%; height:100%;"></div>
<div class="climb-planet" style="position:absolute; top:15%; left:10%; width:100px; height:100px; border-radius:50%; background: linear-gradient(135deg, #4ade80, #166534); box-shadow: inset -20px -20px 40px rgba(0,0,0,0.5), 0 0 20px rgba(74, 222, 128, 0.3); opacity:0.9; animation: floatPlanet 20s infinite ease-in-out;"></div>
<div class="climb-planet" style="position:absolute; bottom:20%; right:15%; width:180px; height:180px; border-radius:50%; background: linear-gradient(135deg, #fca5a5, #991b1b); box-shadow: inset -30px -30px 60px rgba(0,0,0,0.5), 0 0 30px rgba(248, 113, 113, 0.3); opacity:0.8; animation: floatPlanet 25s infinite ease-in-out reverse;"></div>
<div class="climb-planet" style="position:absolute; top:40%; right:30%; width:40px; height:40px; border-radius:50%; background: #fbbf24; box-shadow: 0 0 15px #fbbf24; opacity:0.9; animation: floatPlanet 15s infinite ease-in-out;"></div>
</div>
<button id="climb-fullscreen-btn" onclick="toggleClimbFullscreen()" onmouseout="this.style.transform=\'scale(1)\'" onmouseover="this.style.transform=\'scale(1.1)\'" style="position:absolute; bottom:1rem; right:1rem; z-index:50; background:rgba(255,255,255,0.9); border:none; border-radius:50%; width:3rem; height:3rem; cursor:pointer; box-shadow:0 4px 6px rgba(0,0,0,0.1); display:flex; align-items:center; justify-content:center; transition: transform 0.2s;" title="Toggle Fullscreen">
<svg fill="none" height="24" stroke="#334155" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2-2h3"></path></svg>
</button>
<div id="climb-ladder-bg" style="position:absolute; top:0; left:0; width:100%; height:200%; background: repeating-linear-gradient(180deg, #94a3b8 0, #94a3b8 2px, transparent 2px, transparent 40px); opacity:0.3; animation: slideLadder 10s linear infinite;"></div>
<div id="climb-header" style="z-index:10; padding:1rem; background:rgba(255,255,255,0.95); display:flex; justify-content:space-between; align-items:center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<span id="climb-score" style="font-weight: bold; color: #334155;">Score: 0</span>
<button onclick="resetToClimbMenu()" style="background:#ef4444; color:white; border:none; padding: 0.5rem 1rem; border-radius: 0.5rem; cursor:pointer; font-weight: 600; margin-right: 0.5rem;">Restart</button>
<button id="climb-pause-btn" onclick="toggleClimbPause()" style="background:#f59e0b; color:white; border:none; padding: 0.5rem 1rem; border-radius: 0.5rem; cursor:pointer; font-weight: 600;">Pause</button>
</div>
<div style="flex:1; position:relative; width:100%; overflow:hidden;">
<div id="climb-fuel-text" style="position:absolute; left:2rem; bottom:calc(2rem + 605px); width:60px; text-align:center; font-weight:bold; font-size:1rem; color:#334155; white-space:nowrap; z-index:20;">Fuel Bar</div>
<div id="climb-fuel-container" style="position:absolute; bottom:2rem; left:2rem; width:60px; height:600px; background:rgba(255,255,255,0.3); border:2px solid #334155; border-radius:10px; overflow:hidden; z-index:10; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
<div id="climb-fuel-fill" style="position:absolute; bottom:0; left:0; width:100%; height:50%; background:linear-gradient(to top, #f59e0b, #ef4444); transition: height 0.5s ease;"></div>
</div>
<div id="climb-player" style="position:absolute; bottom:35%; left:50%; transform:translateX(-50%); width:240px; height:240px; transition: bottom 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index: 5;"><svg style="width:100%; height:100%; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3));" viewbox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
<path d="M18 42 L 8 58 L 22 58 L 24 48 Z" fill="#ef4444" stroke="#991b1b" stroke-linejoin="round" stroke-width="1.5"></path>
<path d="M46 42 L 56 58 L 42 58 L 40 48 Z" fill="#ef4444" stroke="#991b1b" stroke-linejoin="round" stroke-width="1.5"></path>
<ellipse cx="32" cy="32" fill="#e2e8f0" rx="14" ry="28" stroke="#475569" stroke-width="2"></ellipse>
<circle cx="32" cy="24" fill="#3b82f6" r="7" stroke="#1d4ed8" stroke-width="1.5"></circle>
<circle cx="33" cy="22" fill="white" opacity="0.6" r="2.5"></circle>
<path d="M26 56 Q 32 72 38 56" fill="#f59e0b" id="climb-flame-outer" stroke="#d97706" stroke-width="1" style="transform-origin: 32px 56px; transition: transform 0.1s ease-out;"></path><path d="M29 56 Q 32 66 35 56" fill="#fef3c7" id="climb-flame-inner" style="transform-origin: 32px 56px; transition: transform 0.1s ease-out;"></path>
</svg></div>
</div>
<div id="climb-start-screen" style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); z-index:60; background:rgba(255,255,255,0.95); padding:2rem; border-radius:1rem; box-shadow:0 10px 25px rgba(0,0,0,0.2); width:80%; max-width:400px; text-align:center; border:1px solid #cbd5e1; display:flex; flex-direction:column; align-items:center;">
<h3 style="color:#1e293b; margin-top:0;">Ready to Fly?</h3>
<p style="color:#64748b; margin-bottom:1.5rem;">Answer correctly to fly up against the moving ladder!</p>
<div style="font-size:0.9rem; color:#64748b; margin-bottom:1rem;">Spacebar = Boost (Uses Fuel)<br/>Correct Answer = +Fuel</div>
<button onclick="startClimbGame()" style="background:#0f172a; color:white; padding:0.75rem 2rem; border:none; border-radius:0.5rem; cursor:pointer; font-weight:600; font-size:1.1rem; transition: background 0.2s;">Start Flying</button>
</div>
<div id="climb-game-over" style="display:none; position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); z-index:60; background:rgba(255,255,255,0.95); padding:2rem; border-radius:1rem; box-shadow:0 10px 25px rgba(0,0,0,0.2); width:80%; max-width:400px; text-align:center; border:1px solid #cbd5e1; flex-direction:column; align-items:center;">
<h3 id="climb-result-title" style="font-size: 1.5rem; margin-bottom: 0.5rem; color:#1e293b;">Game Over!</h3>
<p id="climb-final-score" style="color:#64748b; margin-bottom: 1.5rem;"></p>
<div style="display:flex; gap:0.5rem; justify-content:center; flex-wrap:wrap;">
<button onclick="startClimbGame()" style="background:#10b981; color:white; padding:0.75rem 1.5rem; border:none; border-radius:0.5rem; cursor:pointer; font-weight:600;">Play Again</button>
<button onclick="alert(\'Leaderboard coming soon!\')" style="background:#f59e0b; color:white; padding:0.75rem 1.5rem; border:none; border-radius:0.5rem; cursor:pointer; font-weight:600; display:flex; align-items:center; gap:0.5rem;">&#x1F3C6; Leaderboard</button>
</div>
</div>
<div id="climb-paused-screen" style="display:none; position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); z-index:60; background:rgba(255,255,255,0.95); padding:2rem; border-radius:1rem; box-shadow:0 10px 25px rgba(0,0,0,0.2); width:80%; max-width:400px; text-align:center; border:1px solid #cbd5e1; flex-direction:column; align-items:center;">
<h3 style="color:#1e293b; margin-top:0;">Game Paused</h3>
<button onclick="toggleClimbPause()" style="background:#f59e0b; color:white; padding:0.75rem 2rem; border:none; border-radius:0.5rem; cursor:pointer; font-weight:600; font-size:1.1rem; transition: background 0.2s;">Resume</button>
</div>
<div id="climb-interaction" style="position: absolute; z-index:20; background:rgba(255,255,255,0.95); padding:1.5rem; border-radius:1rem; box-shadow:0 10px 25px rgba(0,0,0,0.2); border:1px solid #cbd5e1; min-height: 200px; display:none; flex-direction:column; justify-content:center; top: 50%; right: 2rem; transform: translateY(-50%); width: 300px">
<div id="climb-question-area" style="display:block; text-align:center; width:100%; max-width:600px; margin:0 auto;">
<p id="climb-question-text" style="font-weight:bold; margin-bottom:1.5rem; font-size:1.1rem; color: #1e293b; line-height:1.5;"></p>
<div id="climb-options" style="display:grid; gap:0.75rem; grid-template-columns: 1fr;"></div>
<div id="climb-feedback" style="margin-top:1rem; height:1.5rem; font-weight:bold;"></div>
</div>
</div>
<style>
@keyframes twinkle {{ 0% {{ opacity:0.3; transform:scale(0.8); }} 100% {{ opacity:1; transform:scale(1.2); }} }}
@keyframes floatPlanet {{ 0% {{ transform:translateY(0px); }} 50% {{ transform:translateY(-20px); }} 100% {{ transform:translateY(0px); }} }}
@keyframes slideLadder {{
    from {{ background-position: 0 0; }}
    to {{ background-position: 0 40px; }}
}}
.climb-option-btn {{
    background: #f1f5f9;
    border: 2px solid #e2e8f0;
    padding: 0.75rem;
    border-radius: 0.5rem;
    cursor: pointer;
    font-size: 1rem;
    color: #334155;
    transition: all 0.2s;
    text-align: left;
}}
.climb-option-btn:hover {{
    background: #e2e8f0;
    border-color: #cbd5e1;
}}
body:not(.dark-mode) #climb-space-bg {{
    background: radial-gradient(ellipse at bottom, #bae6fd 0%, #0369a1 100%) !important;
}}
body:not(.dark-mode) #climb-stars div {{
    opacity: 0.3 !important;
}}
body.dark-mode #climb-game-ui {{ background-color: #0f172a !important; }}
body.dark-mode #climb-ladder-bg {{ background-image: repeating-linear-gradient(180deg, #334155 0, #334155 2px, transparent 2px, transparent 40px) !important; opacity: 0.2 !important; }}
body.dark-mode #climb-header {{ background: rgba(15, 23, 42, 0.95) !important; box-shadow: 0 2px 4px rgba(0,0,0,0.3) !important; }}
body.dark-mode #climb-score {{ color: #e2e8f0 !important; }}
body.dark-mode #climb-interaction {{ background: #1e293b !important; border-color: #334155 !important; }}
body.dark-mode #climb-start-screen h3, body.dark-mode #climb-game-over h3, body.dark-mode #climb-paused-screen h3 {{ color: #f8fafc !important; }}
body.dark-mode #climb-start-screen p, body.dark-mode #climb-game-over p, body.dark-mode #climb-question-text {{ color: #cbd5e1 !important; }}
body.dark-mode .climb-option-btn {{ background: #334155 !important; border-color: #475569 !important; color: #e2e8f0 !important; }}
body.dark-mode .climb-option-btn:hover {{ background: #475569 !important; border-color: #64748b !important; }}
body.dark-mode #climb-fullscreen-btn {{ background: rgba(30, 41, 59, 0.9) !important; }}
body.dark-mode #climb-fullscreen-btn svg {{ stroke: #e2e8f0 !important; }}
body.dark-mode #climb-start-screen, body.dark-mode #climb-game-over, body.dark-mode #climb-paused-screen {{ background: rgba(30, 41, 59, 0.95) !important; border-color: #475569 !important; }}
body.dark-mode #climb-start-screen div {{ color: #cbd5e1 !important; }}
body.dark-mode #climb-fuel-text {{ color: #e2e8f0 !important; }}
</style>
</div></div>
<style>
.mix-match-board {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin-top: 1.5rem;
  width: 100%;
}}
.mm-card {{
  background: #f8fafc;
  border: 2px solid #e2e8f0;
  border-radius: 0.75rem;
  padding: 1.5rem;
  min-height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  cursor: pointer;
  font-weight: 500;
  color: #334155;
  transition: all 0.2s;
  user-select: none;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}}
body.dark-mode .mm-card {{
  background: #1e293b;
  border-color: #334155;
  color: #cbd5e1;
}}
.mm-card:hover {{
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  border-color: #94a3b8;
  background: #f1f5f9;
}}
body.dark-mode .mm-card:hover {{
   background: #1e293b;
   border-color: #475569;
}}
.mm-card.selected {{
  background: #eff6ff;
  border-color: #3b82f6;
  color: #1d4ed8;
  transform: scale(1.02);
  box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
}}
body.dark-mode .mm-card.selected {{
  background: #172554;
  border-color: #60a5fa;
  color: #bfdbfe;
}}
.mm-card.matched {{
  background: #f0fdf4;
  border-color: #22c55e;
  color: #15803d;
  opacity: 0.8;
  cursor: default;
}}
body.dark-mode .mm-card.matched {{
  background: #052e16;
  border-color: #22c55e;
  color: #86efac;
}}
.mm-card.wrong {{
  background: #fef2f2;
  border-color: #ef4444;
  animation: shake 0.5s;
}}
body.dark-mode .mm-card.wrong {{
  background: #450a0a;
  border-color: #ef4444;
}}
@keyframes shake {{
  0%, 100% {{ transform: translateX(0); }}
  25% {{ transform: translateX(-5px); }}
  75% {{ transform: translateX(5px); }}
}}
</style>
<div id="mixmatch-container" style="display:none; flex-direction:column; align-items:center; width:100%;">
<div class="w-full max-w-4xl flex justify-between items-center mb-8">
<div>
<h1 class="text-3xl font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">Mix &amp; Match</h1>
<p class="text-slate-400">Match the terms to their definitions!</p>
</div>
<div class="text-right">
<div class="text-sm text-slate-400">Streak</div>
<div class="text-2xl font-bold text-yellow-400" id="mixmatch-streak-display">0</div>
</div>
</div>
<div class="grid grid-cols-2 md:grid-cols-4 gap-4 w-full max-w-4xl" id="mixmatch-game-board">
</div>
<div class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50" id="mixmatch-win-screen">
<div class="bg-slate-800 p-8 rounded-2xl text-center border border-slate-700 max-w-md mx-4">
<div class="text-6xl mb-4">&#x1F389;</div>
<h2 class="text-3xl font-bold mb-2">Level Complete!</h2>
<p class="text-slate-400 mb-6">You matched all terms correctly.</p>
<button class="bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 px-8 rounded-full transition-all hover:scale-105 active:scale-95" onclick="window.startMixMatchGame()">
                Play Again
            </button>
</div>
</div>
</div><div id="blockpuzzle-container" style="display:none; flex-direction:column; align-items:center; justify-content:center; width:100%;">
<div class="relative w-full max-w-md bg-gray-800 rounded-2xl shadow-2xl p-6 border border-gray-700">
<div class="flex justify-between items-end mb-6">
<div>
<h1 class="text-2xl font-bold bg-gradient-to-r from-green-400 to-emerald-600 bg-clip-text text-transparent">BLOCK PUZZLE</h1>
<p class="text-xs text-gray-400">Clear lines to score!</p>
</div>
<div class="text-right">
<div class="text-xs text-gray-400 font-sans">SCORE</div>
<div class="text-3xl font-bold text-white" id="bp-score">0</div>
</div>
</div>
<div class="grid grid-cols-8 gap-1 bg-gray-900 p-2 rounded-lg border-2 border-gray-700 mx-auto" id="bp-board" style="width: 340px; height: 340px;">
</div>
<div class="mt-8 flex justify-center gap-4 h-24 items-center min-h-[6rem]" id="bp-hand">
</div>
<div class="hidden absolute inset-0 bg-black/90 rounded-2xl z-20 flex flex-col items-center justify-center text-center p-6 backdrop-blur-sm" id="bp-game-over">
<h2 class="text-3xl text-red-500 font-bold mb-2">GAME OVER</h2>
<p class="text-gray-300 mb-6">No more moves possible!</p>
<div class="text-4xl font-bold text-white mb-8" id="bp-final-score">0</div>
<button class="bg-green-600 hover:bg-green-500 text-white font-bold py-3 px-8 rounded-lg shadow-lg transform transition active:scale-95" onclick="window.resetBlockGame()">
                TRY AGAIN
            </button>
</div>
</div>
</div></div>
<div class="Practice-actions" style="margin-top:2rem;display:flex;justify-content:flex-end;width:100%;">
<div class="Practices-menu" style="position:relative; margin-right: 1rem;">
<button class="side-button view-other-Practices" onclick="togglePracticesPanel(this)" type="button">Other games</button>
<div aria-hidden="true" class="Practices-panel">
<div class="Practices-panel-item">
<a href="#flashcard-game">Flashcard Game</a>
</div>
<div class="Practices-panel-item">
<a href="#climb">Boost</a>
</div>
<div class="Practices-panel-item"><a href="#mixmatch">Mix &amp; Match</a></div><div class="Practices-panel-item"><a href="#blockpuzzle">Block Puzzle</a></div></div>
</div>
<button class="side-button" onclick="document.getElementById('practice-content-view').style.display='none';document.getElementById('quiz-content-view').style.display='block';" style="text-align:center;">Start Unit Test</button>
</div>
</div>
</div>

<div id="quiz-content-view" style="display:none;">
<h2 class="page-title">Unit {unit_num}: {escape_html(title)} - Unit Test</h2>
<div class="diagram-card">
<div class="quiz-container">
<form id="quiz-form">
{quiz_html}
</form>
<div id="quiz-results" style="margin-top: 2rem; font-weight: bold; display:none; padding: 1rem; border-radius: 0.5rem;"></div>
<div class="summary-actions" style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
<button type="button" class="side-button" onclick="document.getElementById('quiz-content-view').style.display='none';document.getElementById('practice-content-view').style.display='block';" style="background: #64748b;">Review Flashcards</button>
<button type="button" class="side-button" onclick="window.location.href=\'{back_url}\'">{back_label}</button>
</div>
</div>
</div>
</div>
</main>
<script src="../../scripts/unit_test.js"></script>
<script src="/quiz_logic.js"></script>

<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
<script src="/ArisEdu Project Folder/scripts/game_utils.js"></script>

<script>
{flashcard_js}
</script>
<script src="../../scripts/practice_games.js"></script>
<script src="../../scripts/block_puzzle.js"></script>
<script src="../../scripts/dev_tools.js"></script>
</body>
</html>
'''


def main():
    print("Loading flashcards from Practice files...")
    flashcards = load_all_flashcards()

    print("\\nGenerating Unit Test files...")
    count = 0
    total_flashcards = 0
    for unit_num in sorted(UNITS.keys()):
        unit_info = UNITS[unit_num]
        questions = QUIZ[unit_num]

        # Use Practice file flashcards, fall back to hardcoded
        cards = flashcards.get(unit_num, [])
        if not cards:
            print(f"  Using fallback flashcards for Unit {unit_num}")
            cards = FLASHCARDS_FALLBACK.get(unit_num, [])

        html = build_file(unit_num, unit_info, questions, cards)

        folder = os.path.join(BASE, f"Unit{unit_num}")
        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, f"Unit{unit_num}_Test.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
        total_flashcards += len(cards)
        print(f"  ✓ Unit{unit_num}_Test.html  ({len(questions)} questions, {len(cards)} flashcards)")

    print(f"\\nDone — {count} Unit Test files generated with {total_flashcards} total flashcards.")
