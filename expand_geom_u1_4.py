#!/usr/bin/env python3
"""Expand Geometry U1-U4 quizzes from 7 to 20 questions each (31 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "geometry_lessons.json")

def add_qs(key, new_questions):
    """Return (key, list-of-question-dicts) to append."""
    qs = []
    for qi, (qt, opts, exp) in enumerate(new_questions, 8):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        qs.append({"question_number": qi, "question_text": qt, "attempted": 2,
                    "data_i18n": None, "options": options, "explanation": exp})
    return key, qs

all_new = {}

# ── U1 ──
k, q = add_qs("u1_l1.1", [
    ("A point has:", ["Length only", "Width only", "*No dimensions — it represents a location", "Three dimensions"], "Points are dimensionless."),
    ("Two points determine exactly:", ["A plane", "*A line", "A ray", "A segment"], "Two points define a unique line."),
    ("Three noncollinear points determine:", ["A line", "*A plane", "A point", "A ray"], "Three noncollinear points define a plane."),
    ("Collinear points are points that:", ["Form a triangle", "*Lie on the same line", "Lie on the same plane", "Are equidistant"], "Collinear = same line."),
    ("Coplanar points all lie on the same:", ["Line", "Segment", "*Plane", "Circle"], "Coplanar = same plane."),
    ("The intersection of two distinct lines is:", ["A line", "*A point", "A plane", "A segment"], "Two lines meet at a point."),
    ("The intersection of two distinct planes is:", ["A point", "*A line", "A plane", "A segment"], "Two planes intersect in a line."),
    ("How many lines can pass through a single point?", ["1", "2", "3", "*Infinitely many"], "Infinite lines through any point."),
    ("A line extends:", ["In one direction", "*In two directions infinitely", "To a fixed length", "In three directions"], "Lines extend infinitely both ways."),
    ("A ray has:", ["Two endpoints", "*One endpoint and extends infinitely in one direction", "No endpoints", "A fixed length"], "Ray definition."),
    ("Points A, B, C are collinear with B between A and C. Then AB + BC =", ["*AC", "2AC", "AB", "BC"], "Segment Addition Postulate."),
    ("Opposite rays share:", ["No points", "*A common endpoint and form a line", "Two endpoints", "A midpoint"], "Opposite rays form a line."),
    ("A postulate is:", ["A proven statement", "*An accepted statement without proof", "A definition", "A theorem"], "Postulates are assumed true."),
])
all_new[k] = q

k, q = add_qs("u1_l1.2", [
    ("A line segment has:", ["No endpoints", "*Two endpoints", "One endpoint", "Infinite length"], "Segment = two endpoints."),
    ("Precision in measurement depends on:", ["The object", "*The smallest unit on the measuring tool", "The measurer", "The calculation"], "Precision relates to tool markings."),
    ("If AB = 5 and BC = 8, and B is between A and C, then AC =", ["3", "8", "*13", "40"], "5 + 8 = 13."),
    ("Congruent segments have:", ["The same slope", "The same midpoint", "*The same length", "The same endpoints"], "Congruent = equal length."),
    ("The symbol for congruence is:", ["=", ">", "*≅", "~"], "≅ means congruent."),
    ("If PQ ≅ RS and RS = 12, then PQ =", ["6", "24", "*12", "Cannot determine"], "Congruent segments are equal."),
    ("The Ruler Postulate states that points on a line can be:", ["Named randomly", "*Put in one-to-one correspondence with real numbers", "Ordered alphabetically", "Counted finitely"], "Ruler Postulate."),
    ("Absolute value is used in distance because distance is always:", ["Negative", "Zero", "*Non-negative", "Imaginary"], "Distance is never negative."),
    ("If the coordinate of A is 3 and B is -5, then AB =", ["2", "-8", "*8", "15"], "|3 - (-5)| = 8."),
    ("Between means the point lies _____ two other points on a segment.", ["Outside", "Above", "*On the segment, strictly between", "At an endpoint of"], "Betweenness."),
    ("A construction uses _____ and a straightedge.", ["A ruler", "*A compass", "A protractor", "A calculator"], "Classical construction tools."),
    ("If M is the midpoint of AB and AM = 7, then AB =", ["7", "*14", "3.5", "21"], "AM = MB = 7, so AB = 14."),
    ("Measurement error is the difference between:", ["Two measurements", "*A measured value and the true value", "Two estimates", "Two units"], "Error = measured - true."),
])
all_new[k] = q

k, q = add_qs("u1_l1.3", [
    ("The distance between (1,2) and (4,6) is:", ["5", "3", "*5", "7"], "sqrt(9+16)=5."),
    ("The midpoint of (2,8) and (6,4) is:", ["(2,4)", "(6,8)", "*(4,6)", "(8,12)"], "((2+6)/2,(8+4)/2)=(4,6)."),
    ("The midpoint formula is:", ["(x1-x2, y1-y2)", "*(((x1+x2)/2, (y1+y2)/2))", "(x1*x2, y1*y2)", "((x2-x1), (y2-y1))"], "Average the coordinates."),
    ("If the midpoint of AB is (5,3) and A is (2,1), then B is:", ["(3,2)", "(7,4)", "*(8,5)", "(3.5,2)"], "(2+x)/2=5 => x=8; (1+y)/2=3 => y=5."),
    ("The distance formula is derived from:", ["The midpoint formula", "*The Pythagorean Theorem", "Slope formula", "Area formula"], "Distance formula comes from a^2+b^2=c^2."),
    ("Distance between (-3,4) and (0,0) is:", ["3", "4", "*5", "7"], "sqrt(9+16)=5."),
    ("A segment bisector passes through the:", ["Endpoint", "*Midpoint", "Origin", "Vertex"], "Bisectors go through midpoints."),
    ("If AB = 10 and M is the midpoint, then AM =", ["10", "*5", "20", "2.5"], "Half the segment."),
    ("The Number Line Distance between -7 and 5 is:", ["2", "-12", "*12", "7"], "|-7-5|=12."),
    ("A perpendicular bisector is _____ to the segment at its midpoint.", ["Parallel", "*Perpendicular", "Skew", "Collinear"], "Definition."),
    ("If (x,y) is equidistant from (0,0) and (6,0), then x =", ["0", "6", "*3", "2"], "Perpendicular bisector at x=3."),
    ("Midpoint of (a,b) and (c,d):", ["(a+c, b+d)", "*(((a+c)/2, (b+d)/2))", "(ac, bd)", "((c-a)/2,(d-b)/2)"], "Average coordinates."),
    ("The distance between (1,1) and (1,5) is:", ["2", "3", "*4", "6"], "|5-1|=4, vertical segment."),
])
all_new[k] = q

k, q = add_qs("u1_l1.4", [
    ("An angle is formed by:", ["One ray", "*Two rays with a common endpoint (vertex)", "Two parallel lines", "A line and a plane"], "Two rays, shared vertex."),
    ("A right angle measures:", ["180°", "45°", "*90°", "360°"], "Right = 90."),
    ("An acute angle measures:", ["90° to 180°", "*Less than 90°", "Exactly 90°", "More than 180°"], "Acute is less than 90."),
    ("An obtuse angle measures:", ["Less than 90°", "Exactly 90°", "*Between 90° and 180°", "Exactly 180°"], "Obtuse is between 90 and 180."),
    ("A straight angle measures:", ["90°", "270°", "*180°", "360°"], "Straight = 180."),
    ("The Protractor Postulate allows us to:", ["Measure segments", "*Assign degree measures to angles using a protractor", "Bisect segments", "Construct circles"], "Protractor postulate."),
    ("An angle bisector divides an angle into:", ["Unequal parts", "*Two congruent angles", "Three equal parts", "A line and a ray"], "Bisector = two equal angles."),
    ("If ray OB bisects angle AOC and angle AOC = 80°, then angle AOB =", ["80°", "20°", "*40°", "160°"], "80/2=40."),
    ("Adjacent angles share:", ["Only a vertex", "*A common vertex and a common side, with no common interior points", "Nothing", "Both sides"], "Adjacent angle definition."),
    ("Angle addition postulate: if D is in the interior of angle ABC, then angle ABD + angle DBC =", ["angle ABD", "*angle ABC", "180°", "90°"], "Angle addition."),
    ("A reflex angle measures:", ["0° to 90°", "90° to 180°", "*More than 180° but less than 360°", "Exactly 360°"], "Reflex is 180-360."),
    ("Congruent angles have:", ["Equal sides", "*Equal measures", "Equal perimeters", "The same vertex"], "Same measure."),
    ("Two angles measuring 45° each are:", ["Supplementary", "Complementary", "*Congruent (and complementary)", "Neither"], "Both 45 means congruent and complementary."),
])
all_new[k] = q

k, q = add_qs("u1_l1.5", [
    ("Vertical angles are:", ["Adjacent", "*Formed by two intersecting lines and are congruent", "Supplementary only", "Complementary"], "Vertical angles are congruent."),
    ("Complementary angles sum to:", ["180°", "*90°", "360°", "270°"], "Complementary = 90."),
    ("Supplementary angles sum to:", ["90°", "*180°", "360°", "45°"], "Supplementary = 180."),
    ("If angle A = 35°, its complement is:", ["145°", "35°", "*55°", "325°"], "90-35=55."),
    ("If angle B = 110°, its supplement is:", ["*70°", "110°", "250°", "80°"], "180-110=70."),
    ("A linear pair of angles is always:", ["Complementary", "*Supplementary (they sum to 180° and are adjacent)", "Congruent", "Vertical"], "Linear pair = supplementary."),
    ("If two angles are both congruent and supplementary, each measures:", ["45°", "*90°", "60°", "180°"], "x+x=180, x=90."),
    ("Perpendicular lines form:", ["Acute angles", "Obtuse angles", "*Four right angles", "One right angle"], "Perpendicular = 4 right angles."),
    ("If angles A and B are vertical and angle A = 3x + 10, angle B = 5x - 20, then x =", ["10", "*15", "20", "5"], "3x+10=5x-20 => 30=2x => x=15."),
    ("The angles in a linear pair are _____ angles.", ["Vertical", "*Adjacent supplementary", "Complementary", "Congruent"], "Linear pair."),
    ("If angle 1 and angle 2 are complementary and angle 1 = 2x, angle 2 = x + 30, then x =", ["*20", "30", "10", "15"], "2x+x+30=90 => 3x=60 => x=20."),
    ("Vertical angles are _____ congruent.", ["Sometimes", "Never", "*Always", "Rarely"], "Always congruent."),
    ("If two supplementary angles have a ratio of 2:3, the larger angle is:", ["72°", "*108°", "120°", "90°"], "2x+3x=180, x=36, larger=108."),
])
all_new[k] = q

k, q = add_qs("u1_l1.6", [
    ("A polygon is a closed figure formed by:", ["Curved lines", "*Three or more line segments (sides)", "Two segments", "One segment"], "Polygon definition."),
    ("A convex polygon has all interior angles:", ["Greater than 180°", "*Less than 180°", "Equal to 90°", "Equal to 180°"], "Convex = all angles < 180."),
    ("A regular polygon has:", ["Equal sides only", "Equal angles only", "*Both equal sides and equal angles", "No symmetry"], "Regular = equilateral + equiangular."),
    ("The number of diagonals of an n-sided polygon is:", ["n", "n-1", "*n(n-3)/2", "n(n-1)/2"], "Diagonal formula."),
    ("A hexagon has _____ sides.", ["5", "*6", "7", "8"], "Hex = 6."),
    ("A decagon has _____ sides.", ["8", "9", "*10", "12"], "Deca = 10."),
    ("The perimeter of a polygon is:", ["Its area", "*The sum of all side lengths", "The longest side", "Half the diagonal"], "Perimeter = sum of sides."),
    ("A concave polygon has at least one:", ["Right angle", "*Interior angle greater than 180°", "Side of length 0", "Parallel side"], "Concave = reflex angle."),
    ("An octagon has:", ["6 sides", "7 sides", "*8 sides", "10 sides"], "Octa = 8."),
    ("The sum of interior angles of a quadrilateral is:", ["180°", "270°", "*360°", "540°"], "(4-2)×180=360."),
    ("A triangle is the polygon with the fewest:", ["Angles", "Vertices", "*Sides (3)", "Diagonals"], "Minimum polygon = 3 sides."),
    ("Each interior angle of a regular hexagon measures:", ["90°", "108°", "*120°", "135°"], "(6-2)×180/6=120."),
    ("A polygon with all sides equal is called:", ["Equiangular", "*Equilateral", "Regular", "Congruent"], "Equal sides = equilateral."),
])
all_new[k] = q

k, q = add_qs("u1_l1.7", [
    ("A polyhedron is a 3D figure with:", ["Curved faces", "*Flat polygonal faces", "No vertices", "Only one face"], "Polyhedron = flat faces."),
    ("A prism has:", ["One base", "*Two congruent parallel bases", "No bases", "A curved surface"], "Prism = 2 parallel bases."),
    ("A pyramid has:", ["Two bases", "*One base and triangular lateral faces meeting at an apex", "Curved surfaces only", "No vertex"], "Pyramid definition."),
    ("A cylinder has:", ["Flat faces only", "*Two circular bases and a curved lateral surface", "One base", "No curved surface"], "Cylinder definition."),
    ("A cone has:", ["Two bases", "*One circular base and a curved surface meeting at a vertex", "Flat faces only", "No vertex"], "Cone definition."),
    ("A sphere has:", ["Faces and edges", "*No faces, edges, or vertices", "One face", "Two faces"], "Sphere is a curved surface."),
    ("Euler's formula for polyhedra: V - E + F =", ["0", "1", "*2", "3"], "V - E + F = 2."),
    ("A rectangular prism has _____ faces.", ["4", "5", "*6", "8"], "6 faces."),
    ("A triangular pyramid (tetrahedron) has _____ faces.", ["3", "*4", "5", "6"], "4 triangular faces."),
    ("A cube has _____ edges.", ["6", "8", "*12", "24"], "12 edges."),
    ("A cross section is:", ["A 3D shape", "*The 2D figure formed when a plane intersects a solid", "A rotation", "A reflection"], "Plane cuts solid."),
    ("A net is:", ["A 3D model", "*A 2D pattern that folds into a 3D figure", "A cross section", "A projection"], "Net folds into solid."),
    ("An oblique prism has lateral edges that are:", ["Perpendicular to the bases", "*Not perpendicular to the bases (tilted)", "Parallel to the bases", "Curved"], "Oblique = tilted."),
])
all_new[k] = q

# ── U2 ──
k, q = add_qs("u2_l2.1", [
    ("A conjecture is:", ["A proven fact", "*An unproven statement based on observations", "A definition", "A postulate"], "Conjecture = educated guess."),
    ("Finding a pattern in 2,4,8,16,... and predicting 32 is:", ["Deductive", "*Inductive reasoning", "Proof", "A theorem"], "Pattern recognition = inductive."),
    ("A counterexample:", ["Proves a conjecture", "*Disproves a conjecture with one example", "Supports a conjecture", "Is irrelevant"], "One counterexample disproves."),
    ("Conjecture: All prime numbers are odd. Counterexample:", ["3", "5", "*2", "7"], "2 is prime and even."),
    ("The next term in 1,4,9,16,... is:", ["20", "24", "*25", "32"], "Perfect squares: 5^2=25."),
    ("Inductive reasoning moves from:", ["General to specific", "*Specific observations to general conclusions", "Proof to theorem", "Hypothesis to law"], "Specific to general."),
    ("The sequence 3,6,12,24,... has rule:", ["Add 3", "*Multiply by 2", "Add 6", "Multiply by 3"], "Each term doubles."),
    ("A conjecture may be:", ["Always true", "Always false", "*True or false — it's unproven until demonstrated", "Neither true nor false"], "Unproven status."),
    ("Looking at data to make a generalization is:", ["Proof", "*Inductive reasoning", "Deductive reasoning", "Construction"], "Inductive = observations to generalizations."),
    ("If the pattern 1,1,2,3,5,8,... continues, the next term is:", ["10", "11", "*13", "15"], "Fibonacci: 5+8=13."),
    ("Conjecture: The product of two odd numbers is odd. This is:", ["False", "*True", "Sometimes true", "Unprovable"], "Odd × odd = odd always."),
    ("To test a conjecture, mathematicians look for:", ["More examples", "Agreement", "*Counterexamples", "Popularity"], "Try to disprove."),
    ("The scientific method uses inductive reasoning to form:", ["Proofs", "*Hypotheses", "Theorems", "Axioms"], "Hypotheses from observations."),
])
all_new[k] = q

k, q = add_qs("u2_l2.2", [
    ("A statement in logic is a sentence that is:", ["A question", "*Either true or false, but not both", "Always true", "An opinion"], "Statement = truth value."),
    ("The negation of 'It is raining' is:", ["It is sunny", "*It is not raining", "It might rain", "It will rain"], "Negation = not p."),
    ("A conjunction (p AND q) is true when:", ["Either is true", "*Both p and q are true", "Neither is true", "One is false"], "AND requires both true."),
    ("A disjunction (p OR q) is false when:", ["Either is false", "Both are true", "*Both p and q are false", "One is true"], "OR is false only when both false."),
    ("The truth value of 'Triangles have 3 sides AND squares have 5 sides' is:", ["True", "*False (second part is false)", "Unknown", "Both"], "AND: one false makes it false."),
    ("If p is true and q is false, p OR q is:", ["False", "*True", "Unknown", "Neither"], "OR: one true is enough."),
    ("A compound statement combines:", ["One statement", "*Two or more statements using logical connectives", "No statements", "Only negations"], "Compound = multiple statements."),
    ("The symbol for AND (conjunction) is:", ["∨", "*∧", "~", "→"], "∧ = AND."),
    ("The symbol for OR (disjunction) is:", ["∧", "*∨", "~", "→"], "∨ = OR."),
    ("~p means:", ["p is true", "*The negation of p", "p and q", "p or q"], "~ = not."),
    ("A truth table shows:", ["Only true values", "*All possible truth values of a compound statement", "Only false values", "Definitions"], "All combinations."),
    ("How many rows does a truth table for two variables have?", ["2", "*4", "6", "8"], "2^2 = 4 rows."),
    ("The statement '2 + 2 = 5' has truth value:", ["True", "*False", "Unknown", "Neither"], "Simply false."),
])
all_new[k] = q

k, q = add_qs("u2_l2.3", [
    ("A conditional statement has the form:", ["p and q", "*If p, then q", "p or q", "Not p"], "If-then."),
    ("The converse of 'If p, then q' is:", ["If not p, then not q", "*If q, then p", "If not q, then not p", "p and q"], "Swap hypothesis/conclusion."),
    ("The inverse of 'If p, then q' is:", ["If q, then p", "*If not p, then not q", "If not q, then not p", "p or q"], "Negate both parts."),
    ("The contrapositive of 'If p, then q' is:", ["If q, then p", "If not p, then not q", "*If not q, then not p", "p and q"], "Swap AND negate."),
    ("A conditional and its contrapositive are:", ["Never equivalent", "*Always logically equivalent", "Sometimes equivalent", "Opposites"], "Same truth value."),
    ("The converse and inverse are:", ["Equivalent to the original", "*Logically equivalent to each other", "Always true", "Always false"], "Converse and inverse match."),
    ("A biconditional (p if and only if q) is true when:", ["Only when p is true", "*When p and q have the same truth value (both true or both false)", "Only when q is true", "Always"], "Iff = same truth values."),
    ("'If a figure is a square, then it is a rectangle.' The converse is:", ["True", "*False (a rectangle is not necessarily a square)", "Always true", "Unknown"], "Rectangle ≠ square."),
    ("A counterexample to a conditional shows:", ["The conclusion is true", "*The hypothesis is true but conclusion is false", "Both are true", "Both are false"], "p true, q false."),
    ("The symbol for 'if and only if' is:", ["→", "*↔", "∧", "∨"], "↔ = biconditional."),
    ("'If a number is divisible by 4, then it is even.' This is:", ["*True", "False", "Sometimes true", "A biconditional"], "Divisible by 4 implies even."),
    ("To write a good definition, use a:", ["Conditional", "*Biconditional (if and only if)", "Disjunction", "Negation"], "Definitions are biconditionals."),
    ("The hypothesis is the _____ part of a conditional.", ["Then", "*If", "Only if", "Conclusion"], "Hypothesis follows 'if'."),
])
all_new[k] = q

k, q = add_qs("u2_l2.4", [
    ("Deductive reasoning uses:", ["Specific examples", "*General rules/laws to reach specific conclusions", "Patterns", "Guesses"], "General to specific."),
    ("The Law of Detachment states: If p→q is true and p is true, then:", ["p is false", "q is false", "*q is true", "Nothing follows"], "Modus ponens."),
    ("The Law of Syllogism states: If p→q and q→r, then:", ["r→p", "*p→r", "p→q", "q→p"], "Chain reasoning."),
    ("If 'All dogs are mammals' and 'Buddy is a dog,' then:", ["Buddy might be a mammal", "*Buddy is a mammal (Law of Detachment)", "Nothing can be concluded", "Dogs are Buddies"], "Deductive conclusion."),
    ("If a→b and b→c and a is true, then c is:", ["False", "Unknown", "*True (by Law of Syllogism + Detachment)", "Maybe true"], "Chain deduction."),
    ("Deductive reasoning is _____ if the premises are true.", ["Usually valid", "*Always valid (guaranteed true conclusion)", "Sometimes valid", "Never reliable"], "Deduction guarantees."),
    ("Given: If it rains, the ground is wet. The ground is wet. Can we conclude it rained?", ["Yes", "*No (affirming the consequent is a fallacy — sprinklers could wet the ground)", "Always", "Maybe"], "Converse error."),
    ("Valid deductive reasoning can have a false conclusion if:", ["The logic is wrong", "*One or more premises are false", "Nothing — it's always right", "The conclusion is complex"], "False premises can give false conclusions."),
    ("If 'angle A is 90°' and 'right angles equal 90°,' then angle A is:", ["Acute", "Obtuse", "*A right angle", "Straight"], "Law of Detachment."),
    ("Inductive reasoning gives _____ conclusions; deductive gives _____ conclusions.", ["Certain, probable", "*Probable, certain", "Certain, certain", "Probable, probable"], "Inductive=probable, deductive=certain."),
    ("A valid argument:", ["Must have true premises", "*Has a logical structure where if premises are true, the conclusion must be true", "Is always true", "Uses only examples"], "Validity = structure."),
    ("Deductive reasoning is used in:", ["Guessing patterns", "*Mathematical proofs", "Making conjectures", "Collecting data"], "Proofs are deductive."),
    ("The conclusion in deductive reasoning follows:", ["From specific cases", "*Necessarily from the given premises (if they are true)", "From intuition", "From probability"], "Necessary logical consequence."),
])
all_new[k] = q

k, q = add_qs("u2_l2.5", [
    ("A theorem is:", ["Accepted without proof", "*A statement that has been proven", "An assumption", "A conjecture"], "Theorem = proven."),
    ("A proof is:", ["An opinion", "*A logical argument that shows a statement is true", "A guess", "A definition"], "Logical argument."),
    ("A paragraph proof presents the argument in:", ["Two columns", "*Paragraph (sentence) form", "A diagram only", "A flowchart"], "Written as sentences."),
    ("The given information in a proof is:", ["What you prove", "*What you start with (the premises/facts assumed true)", "The conclusion", "A conjecture"], "Starting facts."),
    ("Through any two points there exists:", ["No lines", "*Exactly one line", "Two lines", "Infinitely many lines"], "Two-point postulate."),
    ("If two lines intersect, they intersect at:", ["Two points", "*Exactly one point", "No points", "A plane"], "Line intersection postulate."),
    ("A plane contains at least:", ["One point", "Two points", "*Three noncollinear points", "Four points"], "Plane postulate."),
    ("If two points lie in a plane, the line containing them:", ["Leaves the plane", "*Also lies in the plane", "Is perpendicular to the plane", "Is parallel to the plane"], "Flatness postulate."),
    ("The difference between a postulate and a theorem:", ["No difference", "*Postulates are accepted; theorems are proven", "Theorems are accepted; postulates are proven", "Both must be proven"], "Postulate=assumed, theorem=proved."),
    ("In a paragraph proof, each statement must be:", ["An opinion", "*Justified by a definition, postulate, theorem, or given information", "A guess", "Restated multiple times"], "Every step needs justification."),
    ("The Ruler Postulate establishes:", ["Angle measurement", "*A one-to-one correspondence between points on a line and real numbers", "Area calculation", "Volume measurement"], "Points correspond to numbers."),
    ("The Segment Addition Postulate: If B is between A and C, then:", ["AB = AC", "BC = AC", "*AB + BC = AC", "AB - BC = AC"], "Parts sum to whole."),
    ("A proof begins with _____ and ends with _____.", ["Conclusion, given", "*Given information, the statement to be proved", "Theorem, postulate", "Question, answer"], "Start with given, end with QED."),
])
all_new[k] = q

k, q = add_qs("u2_l2.6", [
    ("The Addition Property of Equality: if a = b, then a + c =", ["a", "*b + c", "c", "a - c"], "Add same to both sides."),
    ("The Subtraction Property of Equality: if a = b, then a - c =", ["a", "*b - c", "c", "a + c"], "Subtract same from both sides."),
    ("The Multiplication Property: if a = b, then ac =", ["a", "*bc", "c", "a/c"], "Multiply both sides."),
    ("The Division Property: if a = b and c ≠ 0, then a/c =", ["a", "*b/c", "c", "ac"], "Divide both sides."),
    ("The Reflexive Property: a =", ["b", "0", "*a", "1"], "Anything equals itself."),
    ("The Symmetric Property: if a = b, then b =", ["0", "*a", "c", "b"], "Swap sides."),
    ("The Transitive Property: if a = b and b = c, then a =", ["b", "*c", "0", "b + c"], "Chain of equality."),
    ("The Substitution Property: if a = b, then a can replace b in:", ["Nothing", "Only equations", "*Any expression or equation", "Only numbers"], "Substitute equals."),
    ("The Distributive Property: a(b + c) =", ["ab + c", "*ab + ac", "a + bc", "abc"], "Distribute."),
    ("In an algebraic proof, if 2x + 5 = 13, then 2x = 8 by:", ["Addition Property", "*Subtraction Property", "Division Property", "Reflexive Property"], "Subtract 5."),
    ("Continuing: 2x = 8, so x = 4 by:", ["Subtraction Property", "*Division Property", "Addition Property", "Transitive Property"], "Divide by 2."),
    ("Justifying each step in an algebraic proof requires:", ["No explanation", "*Naming the property used (Addition Property, etc.)", "Only the final answer", "A paragraph"], "Name the property."),
    ("If m∠A = m∠B and m∠B = m∠C, then m∠A = m∠C by:", ["Reflexive", "Symmetric", "*Transitive Property", "Substitution"], "Chain: A=B=C means A=C."),
])
all_new[k] = q

k, q = add_qs("u2_l2.7", [
    ("Segment congruence is reflexive: AB ≅", ["CD", "*AB", "BA", "0"], "A segment is congruent to itself."),
    ("If AB ≅ CD, then CD ≅ AB by:", ["Transitive Property", "*Symmetric Property of Congruence", "Reflexive Property", "Addition Property"], "Symmetric."),
    ("If AB ≅ CD and CD ≅ EF, then AB ≅ EF by:", ["Symmetric Property", "*Transitive Property of Congruence", "Reflexive Property", "Substitution"], "Transitive."),
    ("To prove segments congruent, you often show their _____ are equal.", ["Positions", "*Lengths (measures)", "Colors", "Names"], "Congruent = equal measures."),
    ("The Segment Addition Postulate is used to prove:", ["Angle relationships", "*That the sum of parts equals the whole segment", "Parallel lines", "Perpendicular lines"], "Part + part = whole."),
    ("In a two-column proof, the left column contains:", ["Only given info", "*Statements", "Only reasons", "Diagrams"], "Statements on left."),
    ("The right column of a two-column proof contains:", ["Statements", "*Reasons (justifications)", "Diagrams", "Calculations"], "Reasons on right."),
    ("If M is the midpoint of AB, then AM ≅ MB by:", ["Segment Addition", "*Definition of midpoint", "Transitive Property", "Reflexive Property"], "Midpoint definition."),
    ("A bisector creates two _____ parts.", ["Unequal", "*Congruent (equal)", "Parallel", "Perpendicular"], "Bisect = divide equally."),
    ("Given: AC = BD, AB = CD. Prove: AB = CD uses:", ["Only given", "*Segment Addition and Subtraction", "Angle properties", "Parallel lines"], "Algebraic segment proof."),
    ("In proving segment relationships, we move between congruence (≅) and equality (=) using:", ["Guessing", "*Definition of congruent segments", "Symmetric Property", "Addition Property"], "Congruent ↔ equal."),
    ("The word 'CPCTC' means:", ["Circles Prove Congruent Triangles Circular", "*Corresponding Parts of Congruent Triangles are Congruent", "Central Points Create Two Circles", "Cannot Prove Congruence Through Calculation"], "Common proof abbreviation."),
    ("Two-column proofs organize logic into:", ["Paragraphs", "*Matched statement-reason pairs", "Flowcharts", "Diagrams only"], "Statement | Reason format."),
])
all_new[k] = q

k, q = add_qs("u2_l2.8", [
    ("If two angles are vertical, they are:", ["Supplementary", "Complementary", "*Congruent", "Adjacent"], "Vertical angles theorem."),
    ("If two angles form a linear pair, they are:", ["Congruent", "Complementary", "*Supplementary", "Vertical"], "Linear pair = supplementary."),
    ("If two angles are supplements of the same angle, they are:", ["Supplementary", "*Congruent", "Complementary", "Vertical"], "Same supplement theorem."),
    ("If two angles are complements of the same angle, they are:", ["Supplementary", "*Congruent", "Complementary", "Right angles"], "Same complement theorem."),
    ("All right angles are:", ["Supplementary", "*Congruent", "Complementary", "Acute"], "All right angles = 90° = congruent."),
    ("Angle congruence is reflexive: angle A ≅", ["angle B", "*angle A", "angle C", "0°"], "Reflexive."),
    ("If angle 1 ≅ angle 2, then angle 2 ≅ angle 1 by:", ["Transitive", "*Symmetric Property", "Reflexive", "Vertical Angles"], "Symmetric."),
    ("Two perpendicular lines form _____ right angles.", ["1", "2", "*4", "8"], "Four right angles."),
    ("If angle A and angle B are supplementary and angle A = 3x + 10, angle B = 2x + 20, then x =", ["20", "25", "*30", "35"], "3x+10+2x+20=180, 5x+30=180, x=30."),
    ("Proving angle relationships often begins with:", ["The conclusion", "*The given information and a diagram", "A guess", "The last step"], "Start with given."),
    ("If angles 1 and 3 are vertical and angle 1 = 75°, then angle 3 =", ["105°", "15°", "*75°", "150°"], "Vertical = congruent."),
    ("If angles 1 and 2 form a linear pair and angle 1 = 75°, then angle 2 =", ["75°", "15°", "*105°", "85°"], "Linear pair: 180-75=105."),
    ("A flowchart proof uses:", ["Only paragraphs", "*Boxes and arrows to show logical flow", "Only two columns", "No justifications"], "Visual proof format."),
])
all_new[k] = q

k, q = add_qs("u2_l2.9", [
    ("A coordinate proof uses:", ["Only words", "*The coordinate plane to prove geometric properties algebraically", "Only constructions", "Only diagrams"], "Coordinate proof definition."),
    ("To prove a quadrilateral is a parallelogram using coordinates, show:", ["All angles are 90°", "*Opposite sides have equal slopes (parallel) or midpoints of diagonals are the same", "Diagonals are equal", "All sides are perpendicular"], "Parallelogram tests."),
    ("The slope formula m = (y2-y1)/(x2-x1) helps prove lines are:", ["Congruent", "*Parallel (equal slopes) or perpendicular (negative reciprocal slopes)", "Equal", "Bisected"], "Slope relationships."),
    ("To prove a triangle is isosceles, show:", ["All sides equal", "*At least two sides have equal lengths using the distance formula", "All angles equal", "No sides equal"], "Two equal sides."),
    ("Placing a figure at the origin in a coordinate proof:", ["Is required", "*Simplifies calculations (fewer variables)", "Changes the proof", "Is incorrect"], "Strategic placement."),
    ("For a right triangle coordinate proof, place the right angle at:", ["Any vertex", "*(0,0) for simplification (legs along axes)", "The hypotenuse", "The longest side"], "Origin placement."),
    ("To prove a quadrilateral is a rectangle, show it's a parallelogram with:", ["Equal sides", "*Right angles (perpendicular adjacent sides — slopes are negative reciprocals)", "Equal diagonals only", "Parallel diagonals"], "Rectangle = parallelogram + right angles."),
    ("The midpoint formula in coordinate proofs helps show:", ["Parallel lines", "*That a point bisects a segment or diagonals bisect each other", "Right angles", "Congruent angles"], "Midpoint applications."),
    ("If two segments have the same length (by distance formula), they are:", ["Similar", "*Congruent", "Parallel", "Perpendicular"], "Equal length = congruent."),
    ("To prove a triangle is equilateral with coordinates:", ["Only check angles", "*Show all three sides have equal lengths using the distance formula", "Only check one side", "Check parallel sides"], "All sides equal."),
    ("Variables in coordinate proofs represent:", ["Specific numbers", "*General coordinates (making the proof universal)", "Unknown quantities to solve", "Random points"], "Generality."),
    ("Coordinate proofs can verify results from:", ["Only coordinate geometry", "*Both synthetic (traditional) and analytic geometry", "Only algebra", "Only trigonometry"], "Bridge between approaches."),
    ("The distance formula is: d =", ["(x2-x1) + (y2-y1)", "*sqrt((x2-x1)^2 + (y2-y1)^2)", "(x2+x1)/2", "(y2-y1)/(x2-x1)"], "Pythagorean-based distance."),
])
all_new[k] = q

# ── U3 ──
k, q = add_qs("u3_l3.1", [
    ("A transversal is a line that:", ["Is parallel to two lines", "*Intersects two or more lines at different points", "Is perpendicular to one line", "Bisects an angle"], "Transversal definition."),
    ("Corresponding angles are on the _____ side of the transversal and in _____ positions.", ["Same, same", "*Same, matching (one interior, one exterior)", "Opposite, same", "Opposite, opposite"], "Corresponding position."),
    ("Alternate interior angles are on _____ sides of the transversal.", ["The same", "*Opposite", "Neither", "Both"], "Alternate = opposite sides."),
    ("Alternate exterior angles are on _____ sides and _____ the parallel lines.", ["Same, between", "*Opposite, outside", "Same, outside", "Opposite, between"], "Alternate exterior position."),
    ("Co-interior (same-side interior) angles are on the _____ side and between the parallel lines.", ["Opposite", "*Same", "Neither", "Alternating"], "Same-side interior."),
    ("When a transversal crosses parallel lines, it creates _____ angles.", ["4", "6", "*8", "12"], "Two intersection points, 4 angles each."),
    ("If two parallel lines are cut by a transversal, corresponding angles are:", ["Supplementary", "*Congruent", "Complementary", "Vertical"], "Corresponding Angles Postulate."),
    ("Skew lines are lines that:", ["Intersect", "Are parallel", "*Do not intersect and are not in the same plane", "Are perpendicular"], "Skew = non-intersecting, non-parallel."),
    ("Parallel lines have the same:", ["Length", "*Direction (slope)", "Midpoint", "Endpoints"], "Same slope."),
    ("The symbol for parallel is:", ["⊥", "*∥", "≅", "~"], "∥ means parallel."),
    ("A transversal cutting two lines creates _____ pairs of corresponding angles.", ["2", "3", "*4", "8"], "4 pairs of corresponding angles."),
    ("Interior angles are _____ the two lines cut by a transversal.", ["Outside", "*Between", "On", "Above"], "Interior = between the lines."),
    ("If parallel lines are cut by a transversal, alternate interior angles are:", ["Supplementary", "*Congruent", "Complementary", "Unrelated"], "Alt. Int. Angles Theorem."),
])
all_new[k] = q

k, q = add_qs("u3_l3.2", [
    ("If corresponding angles are congruent when two lines are cut by a transversal, the lines are:", ["Perpendicular", "*Parallel", "Skew", "Intersecting"], "Converse of Corresponding Angles."),
    ("Alternate interior angles formed by parallel lines and a transversal are:", ["Supplementary", "*Congruent", "Complementary", "Unrelated"], "AIA Theorem."),
    ("Co-interior (consecutive interior / same-side interior) angles are:", ["Congruent", "*Supplementary (sum to 180°)", "Complementary", "Vertical"], "Same-side = supplementary."),
    ("If angle 1 = 70° and angle 1 and angle 2 are alternate interior angles (parallel lines), then angle 2 =", ["110°", "*70°", "20°", "140°"], "AIA are congruent."),
    ("If angle 3 = 115° and angle 4 is co-interior with angle 3, then angle 4 =", ["115°", "*65°", "25°", "180°"], "Co-interior: 180-115=65."),
    ("Alternate exterior angles formed by parallel lines are:", ["Supplementary", "*Congruent", "Complementary", "Right angles"], "AEA Theorem."),
    ("If lines are NOT parallel, alternate interior angles are:", ["Still congruent", "*Not necessarily congruent", "Always 90°", "Supplementary"], "Parallel required."),
    ("Two angles that are both supplementary to the same angle are:", ["Supplementary", "*Congruent", "Complementary", "Vertical"], "Same-supplement theorem."),
    ("If angle 5 = 3x + 10 and its corresponding angle = 5x - 30 (parallel lines), then x =", ["10", "*20", "30", "15"], "3x+10=5x-30, 40=2x, x=20."),
    ("Perpendicular transversal theorem: if a transversal is perpendicular to one of two parallel lines, it is _____ to the other.", ["Parallel", "*Perpendicular", "Skew", "Oblique"], "Perp stays perp."),
    ("If two lines are cut by a transversal and same-side interior angles are supplementary, the lines are:", ["Perpendicular", "*Parallel", "Skew", "Coincident"], "Converse of co-interior theorem."),
    ("In a diagram with parallel lines cut by a transversal, how many distinct angle measures are there?", ["1", "*2 (each angle is either the acute or obtuse measure)", "4", "8"], "Only two distinct values."),
    ("An exterior angle is located _____ the two lines.", ["Between", "*Outside", "On", "At the intersection of"], "Exterior = outside."),
])
all_new[k] = q

k, q = add_qs("u3_l3.3", [
    ("Slope measures a line's:", ["Length", "*Steepness (rate of change)", "Midpoint", "Intersection"], "Slope = steepness."),
    ("Slope = (y2 - y1) / (x2 - x1). For (2,3) and (5,9), slope =", ["1", "*2", "3", "6"], "(9-3)/(5-2)=6/3=2."),
    ("A horizontal line has slope:", ["Undefined", "1", "*0", "Infinity"], "No rise = 0."),
    ("A vertical line has slope:", ["0", "1", "*Undefined", "-1"], "No run = undefined."),
    ("Parallel lines have:", ["Perpendicular slopes", "*Equal slopes", "Opposite slopes", "No slopes"], "Parallel = same slope."),
    ("Perpendicular lines have slopes that are:", ["Equal", "*Negative reciprocals", "Both zero", "Both undefined"], "Perpendicular = negative reciprocal."),
    ("If line 1 has slope 3, a perpendicular line has slope:", ["3", "-3", "1/3", "*-1/3"], "Negative reciprocal of 3."),
    ("If line 1 has slope -2/5, a parallel line has slope:", ["2/5", "5/2", "*-2/5", "-5/2"], "Same slope for parallel."),
    ("A line going from lower-left to upper-right has _____ slope.", ["Negative", "*Positive", "Zero", "Undefined"], "Rising = positive."),
    ("A line going from upper-left to lower-right has _____ slope.", ["Positive", "*Negative", "Zero", "Undefined"], "Falling = negative."),
    ("The slope of a line through (0,0) and (4,4) is:", ["0", "4", "*1", "8"], "(4-0)/(4-0)=1."),
    ("If slope of AB = 3/4 and slope of CD = 3/4, then AB and CD are:", ["Perpendicular", "*Parallel (or the same line)", "Intersecting at 90°", "Skew"], "Equal slopes = parallel."),
    ("Rate of change in real-world context is the same as:", ["Y-intercept", "*Slope", "X-intercept", "Origin"], "Slope = rate of change."),
])
all_new[k] = q

k, q = add_qs("u3_l3.4", [
    ("Slope-intercept form is y =", ["ax + b", "*mx + b", "Ax + By + C", "y1 = m(x - x1)"], "y = mx + b."),
    ("In y = mx + b, m is the:", ["y-intercept", "*Slope", "x-intercept", "Constant"], "m = slope."),
    ("In y = mx + b, b is the:", ["Slope", "*y-intercept", "x-intercept", "Origin"], "b = y-intercept."),
    ("Point-slope form is:", ["y = mx + b", "*y - y1 = m(x - x1)", "Ax + By = C", "x = a"], "Point-slope form."),
    ("Standard form of a linear equation is:", ["y = mx + b", "y - y1 = m(x - x1)", "*Ax + By = C (A, B, C are integers, A ≥ 0)", "y = ax^2 + bx + c"], "Standard form."),
    ("The equation of a horizontal line through (3,5) is:", ["x = 3", "x = 5", "y = 3", "*y = 5"], "Horizontal = y = constant."),
    ("The equation of a vertical line through (3,5) is:", ["y = 5", "y = 3", "*x = 3", "x = 5"], "Vertical = x = constant."),
    ("A line with slope 2 through (1,3): y - 3 = 2(x - 1), which simplifies to:", ["y = 2x + 3", "*y = 2x + 1", "y = x + 2", "y = 3x - 1"], "y = 2x - 2 + 3 = 2x + 1."),
    ("Convert y = -3x + 6 to standard form:", ["y + 3x = 6", "*3x + y = 6", "-3x - y = -6", "x + y = 3"], "3x + y = 6."),
    ("The x-intercept of y = 2x - 8 is:", ["(0,-8)", "(-4,0)", "*(4,0)", "(8,0)"], "0=2x-8, x=4."),
    ("Two lines with the same slope and different y-intercepts are:", ["The same line", "*Parallel (never intersect)", "Perpendicular", "Intersecting"], "Parallel."),
    ("The equation of a line through (0,0) with slope 5 is:", ["y = x + 5", "*y = 5x", "x = 5y", "y = 5"], "Through origin: y = 5x."),
    ("Parallel to y = 4x - 1 through (2,3): y =", ["4x - 1", "*4x - 5", "4x + 3", "-x/4 + 3"], "m=4: y-3=4(x-2), y=4x-5."),
])
all_new[k] = q

k, q = add_qs("u3_l3.5", [
    ("If corresponding angles are congruent, the lines are:", ["Perpendicular", "*Parallel", "Skew", "Coincident"], "Corresponding angles converse."),
    ("If alternate interior angles are congruent, the lines are:", ["Perpendicular", "*Parallel", "Intersecting", "Skew"], "AIA converse."),
    ("If co-interior angles are supplementary, the lines are:", ["Perpendicular", "*Parallel", "Intersecting", "Skew"], "Same-side interior converse."),
    ("If alternate exterior angles are congruent, the lines are:", ["Perpendicular", "*Parallel", "Skew", "Coincident"], "AEA converse."),
    ("To prove lines parallel using slope, show:", ["Slopes are negative reciprocals", "*Slopes are equal", "Slopes multiply to -1", "One slope is zero"], "Equal slopes = parallel."),
    ("Given: angle 1 ≅ angle 5 (corresponding). Conclusion:", ["Lines are perpendicular", "*Lines are parallel", "Angles are vertical", "Lines intersect"], "Corresponding angles converse."),
    ("In a two-column proof of parallel lines, the final reason is often:", ["Definition of congruent", "*Converse of Corresponding Angles Postulate (or similar)", "Vertical Angles Theorem", "Linear Pair Postulate"], "Parallel line converse."),
    ("If two lines are both perpendicular to the same transversal, they are:", ["Perpendicular to each other", "*Parallel to each other", "Skew", "Intersecting"], "Both perp to same line = parallel."),
    ("To prove lines parallel, you need to show a relationship between angles formed by:", ["Any two lines", "*The two lines and a transversal", "Parallel lines only", "Perpendicular lines"], "Transversal angle relationships."),
    ("Angle 3 = 2x + 15 and angle 5 = 4x - 5 are alternate interior angles. For parallel lines, x =", ["5", "*10", "15", "20"], "2x+15=4x-5, 20=2x, x=10."),
    ("If two coplanar lines are not parallel, they:", ["Are skew", "*Intersect at exactly one point", "Never meet", "Are perpendicular"], "Coplanar non-parallel lines intersect."),
    ("The Parallel Postulate states through a point not on a line, there is:", ["No parallel line", "*Exactly one line parallel to the given line", "Two parallel lines", "Infinitely many parallels"], "Euclid's parallel postulate."),
    ("In a flow proof, arrows show:", ["Time sequence", "*Logical connections between statements and reasons", "Direction of lines", "Angle measures"], "Flow proof structure."),
])
all_new[k] = q

k, q = add_qs("u3_l3.6", [
    ("Perpendicular lines intersect at:", ["Any angle", "*90° angles", "45° angles", "180°"], "Perpendicular = 90°."),
    ("The shortest distance from a point to a line is measured along a _____ from the point to the line.", ["Parallel", "*Perpendicular segment", "Diagonal", "Tangent"], "Perpendicular = shortest distance."),
    ("The distance between two parallel lines is measured along a:", ["Diagonal", "Transversal", "*Common perpendicular", "Secant"], "Perpendicular distance."),
    ("If the distance from point P to line l is 5 units, every point on line l is _____ from P.", ["Exactly 5 units", "*At least 5 units", "More than 5 units", "Less than 5 units"], "Perpendicular is the minimum."),
    ("The perpendicular from point (3,4) to the x-axis has length:", ["3", "*4", "5", "7"], "Distance to x-axis = |y| = 4."),
    ("The perpendicular from point (3,4) to the y-axis has length:", ["4", "*3", "5", "1"], "Distance to y-axis = |x| = 3."),
    ("Two parallel lines are everywhere:", ["Getting closer", "*Equidistant (the same distance apart)", "Getting farther apart", "Touching"], "Parallel = equidistant."),
    ("The distance from a point to a line can be found using:", ["Only measurement", "*The distance formula applied to the perpendicular segment, or a formula", "Slope only", "Midpoint formula"], "Perpendicular distance calculation."),
    ("If line l has equation y = 2x + 3 and line m has equation y = 2x - 1, the distance between them is:", ["4", "2", "*4/sqrt(5)", "1"], "Distance formula for parallel lines: |c1-c2|/sqrt(a^2+b^2)."),
    ("A perpendicular bisector is both perpendicular to a segment and passes through its:", ["Endpoint", "*Midpoint", "Any point", "Neither endpoint"], "Two conditions."),
    ("Every point on a perpendicular bisector is _____ from the endpoints of the segment.", ["Closer to one", "*Equidistant", "Farther from both", "At different distances"], "Perpendicular bisector equidistance."),
    ("The symbol for perpendicular is:", ["∥", "*⊥", "≅", "∠"], "⊥ means perpendicular."),
    ("In a coordinate plane, lines with slopes m and -1/m are:", ["Parallel", "*Perpendicular", "Skew", "The same line"], "Negative reciprocal = perpendicular."),
])
all_new[k] = q

k, q = add_qs("u3_l3.7", [
    ("Analytic geometry combines:", ["Only algebra", "Only geometry", "*Algebra and geometry using coordinate systems", "Only trigonometry"], "Algebra + geometry."),
    ("To prove a quadrilateral is a rectangle, show it has:", ["4 right angles only", "*4 right angles (or is a parallelogram with one right angle)", "Equal diagonals only", "4 equal sides"], "Rectangle proof."),
    ("To prove a quadrilateral is a rhombus using coordinates, show:", ["Right angles", "Equal diagonals", "*All four sides are equal length", "Parallel sides only"], "Rhombus = all sides equal."),
    ("The distance formula applied to all sides of a figure determines:", ["Angle measures", "*Side lengths (to check for congruence/equality)", "Slopes", "Midpoints"], "Side length calculation."),
    ("To verify a right angle at coordinates, check that adjacent sides have:", ["Equal slopes", "*Slopes that are negative reciprocals", "Zero slopes", "Undefined slopes"], "Perpendicular check."),
    ("Using coordinates, the diagonals of a rectangle are:", ["Perpendicular", "*Equal in length", "Parallel", "Different lengths"], "Rectangle diagonal property."),
    ("The centroid of a triangle with vertices (x1,y1), (x2,y2), (x3,y3) is:", ["(x1+x2, y1+y2)", "*((x1+x2+x3)/3, (y1+y2+y3)/3)", "(x1*x2*x3, y1*y2*y3)", "(x2-x1, y2-y1)"], "Average of vertices."),
    ("To prove a figure is a square, show it is a _____ with _____.", ["Rectangle, parallel sides", "*Rhombus with a right angle (or rectangle with equal sides)", "Triangle, equal sides", "Parallelogram, equal diagonals"], "Square proof."),
    ("Coordinate geometry lets us prove properties:", ["Approximately", "*Exactly, using algebraic calculations", "By estimation", "By visual inspection"], "Exact proofs."),
    ("The diagonals of a parallelogram _____ each other.", ["Are perpendicular to", "*Bisect (share the same midpoint)", "Are parallel to", "Avoid"], "Diagonal bisection."),
    ("A figure has vertices A(0,0), B(4,0), C(4,3), D(0,3). This is a:", ["Square", "*Rectangle", "Rhombus", "Trapezoid"], "Right angles, unequal adjacent sides (4 and 3)."),
    ("ABCD is a parallelogram if midpoint of AC = midpoint of BD because:", ["Sides are parallel", "*Diagonals bisect each other (midpoint test for parallelogram)", "All sides are equal", "All angles are equal"], "Midpoint diagonal test."),
    ("Analytic geometry was developed by:", ["Euclid", "Pythagoras", "*Rene Descartes (Cartesian coordinate system)", "Isaac Newton"], "Descartes' contribution."),
])
all_new[k] = q

# ── U4 ──
k, q = add_qs("u4_l4.1", [
    ("A scalene triangle has:", ["Two equal sides", "Three equal sides", "*No equal sides", "One right angle"], "Scalene = all different."),
    ("An equilateral triangle has:", ["No equal sides", "Two equal sides", "*Three equal sides", "One obtuse angle"], "Equilateral = all equal."),
    ("An isosceles triangle has:", ["No equal sides", "*At least two equal sides", "All different angles", "One straight angle"], "Isosceles = at least 2 equal."),
    ("A triangle with angles 60°, 60°, 60° is:", ["Right", "Obtuse", "*Equiangular (and equilateral)", "Isosceles only"], "All angles 60 = equiangular."),
    ("A right triangle has one angle of:", ["180°", "45°", "*90°", "120°"], "Right = 90 degree angle."),
    ("An obtuse triangle has one angle that is:", ["Less than 90°", "Exactly 90°", "*Greater than 90°", "Exactly 180°"], "Obtuse angle > 90."),
    ("An acute triangle has:", ["One angle > 90°", "One angle = 90°", "*All angles < 90°", "One angle = 180°"], "All angles acute."),
    ("Can a triangle be both right and obtuse?", ["Yes", "*No (right = 90° exactly, obtuse = more than 90° — the other two angles wouldn't sum correctly)", "Sometimes", "Always"], "Mutually exclusive."),
    ("The sides of a triangle with lengths 3, 4, 5 form a _____ triangle.", ["Equilateral", "Isosceles", "*Right (3² + 4² = 5²)", "Obtuse"], "Pythagorean triple."),
    ("An equilateral triangle is always:", ["Right", "Obtuse", "*Acute (60° angles are all acute)", "Scalene"], "Equilateral = always acute."),
    ("By side classification, the three types are:", ["Right, acute, obtuse", "*Scalene, isosceles, equilateral", "Large, medium, small", "Concave, convex, regular"], "Side classification."),
    ("By angle classification, the three types are:", ["Scalene, isosceles, equilateral", "*Acute, right, obtuse", "Small, medium, large", "Regular, irregular, convex"], "Angle classification."),
    ("A triangle with sides 5, 5, 8 is:", ["Equilateral", "*Isosceles", "Scalene", "Right"], "Two equal sides."),
])
all_new[k] = q

k, q = add_qs("u4_l4.2", [
    ("The sum of angles in a triangle is:", ["90°", "*180°", "270°", "360°"], "Triangle Angle Sum."),
    ("If two angles of a triangle are 45° and 65°, the third is:", ["110°", "*70°", "45°", "135°"], "180-45-65=70."),
    ("An exterior angle of a triangle equals:", ["One remote interior angle", "*The sum of the two non-adjacent (remote) interior angles", "180° minus all three angles", "90°"], "Exterior Angle Theorem."),
    ("If an exterior angle is 120° and one remote interior angle is 50°, the other remote interior angle is:", ["*70°", "120°", "130°", "60°"], "120-50=70."),
    ("A triangle with angles 30°, 60°, 90° has _____ degrees total.", ["160°", "*180°", "200°", "270°"], "Always 180."),
    ("The acute angles in a right triangle sum to:", ["180°", "*90°", "45°", "270°"], "90+x+y=180, so x+y=90."),
    ("Each angle of an equilateral triangle measures:", ["90°", "45°", "*60°", "120°"], "180/3=60."),
    ("If a triangle has angles x, 2x, and 3x, then x =", ["20°", "*30°", "45°", "60°"], "x+2x+3x=180, 6x=180, x=30."),
    ("An exterior angle is always _____ than either remote interior angle.", ["Smaller", "Equal", "*Greater", "Less or equal"], "Sum of two positive numbers > either."),
    ("A triangle can have at most _____ obtuse angle(s).", ["0", "*1", "2", "3"], "Two obtuse angles would exceed 180°."),
    ("A triangle can have at most _____ right angle(s).", ["0", "*1", "2", "3"], "Two right angles = 180° with nothing left."),
    ("The Exterior Angle Inequality states an exterior angle is greater than:", ["The adjacent interior angle", "*Each non-adjacent interior angle", "All three interior angles", "No other angle"], "Greater than each remote interior."),
    ("If angles in a triangle are (2x+10)°, (3x-5)°, and (x+25)°, then x =", ["20", "*25", "30", "15"], "2x+10+3x-5+x+25=180, 6x+30=180, x=25."),
])
all_new[k] = q

k, q = add_qs("u4_l4.3", [
    ("Two triangles are congruent if:", ["They look the same", "*All corresponding sides and angles are congruent (six pairs total)", "They have the same area", "They have one equal side"], "Full congruence."),
    ("CPCTC stands for:", ["Common Parts Create Two Circles", "*Corresponding Parts of Congruent Triangles are Congruent", "Congruent Pairs Come Through Calculation", "Central Points Create Triangular Congruence"], "Proof abbreviation."),
    ("If triangle ABC ≅ triangle DEF, then angle A ≅", ["angle D", "*angle D", "angle E", "angle F"], "A corresponds to D."),
    ("If triangle ABC ≅ triangle DEF, then side AB ≅", ["EF", "DF", "*DE", "BC"], "AB corresponds to DE."),
    ("The order of vertices in a congruence statement matters because:", ["It looks better", "*It shows which vertices/parts correspond", "It doesn't matter", "Alphabetical order is required"], "Order = correspondence."),
    ("Congruent figures have the same:", ["Color", "*Shape and size", "Location", "Orientation"], "Same shape AND size."),
    ("If triangle PQR ≅ triangle XYZ, then QR ≅", ["XY", "*YZ", "XZ", "PQ"], "QR corresponds to YZ."),
    ("To prove triangles congruent, you typically need to show:", ["All 6 pairs of parts congruent", "*A minimum of 3 specific pairs (using SSS, SAS, ASA, AAS, or HL)", "Just 1 pair of sides", "Just 1 pair of angles"], "Shortcut theorems."),
    ("After proving triangles congruent, CPCTC lets you conclude:", ["The triangles are similar", "*Any remaining corresponding parts are also congruent", "The triangles are equal in area only", "Nothing further"], "CPCTC application."),
    ("If two triangles share a common side, that side is congruent to itself by:", ["CPCTC", "*Reflexive Property", "Symmetric Property", "Transitive Property"], "Shared side = reflexive."),
    ("Third Angles Theorem: If two angles of one triangle are congruent to two angles of another, the third angles are:", ["Supplementary", "*Congruent (since all must sum to 180°)", "Complementary", "Unrelated"], "Third Angles Theorem."),
    ("Corresponding parts are in the _____ position in congruent figures.", ["Random", "*Matching/corresponding", "Opposite", "Adjacent"], "Matching position."),
    ("A rigid motion (isometry) preserves:", ["Only angles", "Only distances", "*Both distances and angles — producing congruent figures", "Neither"], "Isometry = congruence."),
])
all_new[k] = q

k, q = add_qs("u4_l4.4", [
    ("SSS Congruence requires:", ["Two sides and an angle", "*Three pairs of congruent sides", "Three angles", "Two angles and a side"], "Side-Side-Side."),
    ("SAS Congruence requires:", ["Three sides", "*Two sides and the included angle congruent", "Two angles and a side", "Three angles"], "Side-Angle-Side."),
    ("The 'included angle' in SAS is:", ["Any angle", "*The angle formed between the two given sides", "The largest angle", "An exterior angle"], "Between the two sides."),
    ("Can SSA (two sides and a non-included angle) prove congruence?", ["Always", "*No — it's the ambiguous case (can produce 0, 1, or 2 triangles)", "Sometimes valid", "Only for right triangles"], "SSA is ambiguous."),
    ("To use SSS, you must show _____ pairs of sides are congruent.", ["1", "2", "*3", "4"], "All three pairs."),
    ("In SAS, if the angle is NOT between the two sides, the theorem:", ["Still works", "*Does NOT apply (it must be the included angle)", "Works sometimes", "Applies to right triangles only"], "Must be included angle."),
    ("If AB ≅ DE, BC ≅ EF, and CA ≅ FD, the triangles are congruent by:", ["SAS", "*SSS", "ASA", "AAS"], "Three sides = SSS."),
    ("If AB ≅ DE, angle B ≅ angle E, and BC ≅ EF, the triangles are congruent by:", ["SSS", "*SAS (angle B is included between AB and BC)", "ASA", "AAS"], "Two sides + included angle = SAS."),
    ("A shared side (common side) between two triangles is congruent to itself by:", ["CPCTC", "SSS", "*Reflexive Property", "Midpoint Theorem"], "Reflexive."),
    ("Given: AB ≅ CB and D is the midpoint of AC. Why is triangle ABD ≅ triangle CBD?", ["ASA", "AAS", "*SSS (AB≅CB, AD≅CD by midpoint, BD≅BD by reflexive)", "SAS"], "All three sides congruent."),
    ("In a proof, after establishing SSS or SAS, you write:", ["QED", "Therefore the angles are equal", "*Therefore triangle ___ ≅ triangle ___ by SSS (or SAS)", "Nothing more needed"], "State the conclusion."),
    ("SSS and SAS are _____ for proving triangle congruence.", ["Insufficient", "*Sufficient (either one alone is enough)", "Necessary only", "Rare"], "Either is sufficient."),
    ("AAA (three angles congruent) proves:", ["Congruence", "*Similarity only (not congruence — triangles can be different sizes)", "Nothing", "Perpendicularity"], "AAA = similar, not congruent."),
])
all_new[k] = q

k, q = add_qs("u4_l4.5", [
    ("ASA Congruence requires:", ["Two sides and included angle", "*Two angles and the included side", "Three angles", "Three sides"], "Angle-Side-Angle."),
    ("AAS Congruence requires:", ["Two sides and a non-included angle", "*Two angles and a non-included side", "Three angles", "Two sides and included angle"], "Angle-Angle-Side."),
    ("The 'included side' in ASA is:", ["Any side", "*The side between the two given angles", "The longest side", "The shortest side"], "Between the two angles."),
    ("If angle A ≅ angle D, AB ≅ DE, and angle B ≅ angle E, the triangles are congruent by:", ["SAS", "SSS", "*ASA (AB is the included side)", "AAS"], "Two angles + included side = ASA."),
    ("If angle A ≅ angle D, angle B ≅ angle E, and BC ≅ EF, the triangles are congruent by:", ["ASA", "SSS", "*AAS (BC is not included between the two angles)", "SAS"], "Two angles + non-included side = AAS."),
    ("AAS works because if two angles are known, the third angle is:", ["Unknown", "*Determined (by Triangle Angle Sum = 180°)", "Variable", "Always 90°"], "Third angle is fixed."),
    ("HL (Hypotenuse-Leg) works only for:", ["Any triangle", "Obtuse triangles", "*Right triangles", "Equilateral triangles"], "HL is for right triangles only."),
    ("HL requires the hypotenuse and one _____ to be congruent.", ["Angle", "*Leg", "Median", "Altitude"], "Hypotenuse + leg."),
    ("If angle A ≅ angle D and angle C ≅ angle F, then angle B ≅ angle E by:", ["CPCTC", "*Third Angles Theorem", "Vertical Angles", "AAS"], "Remaining angles must be equal."),
    ("The five triangle congruence shortcuts are:", ["SSS, SAS, SSA, AAA, HL", "*SSS, SAS, ASA, AAS, HL", "SSS, ASA, AAA, HL, SAS", "SSS, SAS, ASA, AAS, AAA"], "Five valid methods."),
    ("AAA and SSA are NOT valid because:", ["They're too complex", "*AAA gives similarity not congruence; SSA is ambiguous (can make different triangles)", "They involve too many parts", "They only work for right triangles"], "Invalid methods."),
    ("After proving congruence by ASA, remaining parts are congruent by:", ["ASA again", "*CPCTC", "SSS", "Definition"], "CPCTC for remaining parts."),
    ("To decide which congruence theorem to use, identify the _____ congruent parts first.", ["Largest", "*Given (known)", "Smallest", "All"], "Use what's given."),
])
all_new[k] = q

k, q = add_qs("u4_l4.6", [
    ("In an isosceles triangle, the base angles are:", ["Different", "*Congruent", "Supplementary", "Complementary"], "Base Angles Theorem."),
    ("The converse: If two angles of a triangle are congruent, the sides opposite them are:", ["Different", "*Congruent (the triangle is isosceles)", "Perpendicular", "Parallel"], "Converse of Base Angles Theorem."),
    ("An equilateral triangle has _____ congruent angles.", ["0", "2", "*3", "1"], "All three = 60°."),
    ("Each angle of an equilateral triangle measures:", ["90°", "45°", "*60°", "120°"], "180/3 = 60°."),
    ("If an isosceles triangle has base angles of 50° each, the vertex angle is:", ["50°", "100°", "*80°", "130°"], "180-50-50=80."),
    ("If the vertex angle of an isosceles triangle is 40°, each base angle is:", ["40°", "80°", "*70°", "140°"], "(180-40)/2=70."),
    ("The legs of an isosceles triangle are the _____ sides.", ["Unequal", "*Two congruent", "Three", "Base"], "Legs = equal sides."),
    ("The base of an isosceles triangle is:", ["Always the longest side", "Always the shortest side", "*The side between the two base angles (may be longer or shorter than the legs)", "Always horizontal"], "Base connects base angles."),
    ("An equilateral triangle is a special case of _____ triangle.", ["Scalene", "Right", "*Isosceles", "Obtuse"], "Equilateral is always isosceles."),
    ("If a triangle has sides 6, 6, and 6, each angle measures:", ["90°", "45°", "*60°", "120°"], "Equilateral = equiangular."),
    ("The altitude from the vertex angle of an isosceles triangle _____ the base.", ["Is parallel to", "*Bisects (is also the perpendicular bisector and median)", "Misses", "Extends beyond"], "Altitude = bisector in isosceles."),
    ("If an equilateral triangle has side length 10, its perimeter is:", ["20", "25", "*30", "100"], "3 × 10 = 30."),
    ("A corollary of the Base Angles Theorem: A triangle is equilateral if and only if it is:", ["Right", "*Equiangular", "Obtuse", "Scalene"], "Equilateral ↔ equiangular."),
])
all_new[k] = q

k, q = add_qs("u4_l4.7", [
    ("A congruence transformation preserves:", ["Only shape", "Only size", "*Both shape and size (distance and angle measure)", "Neither"], "Isometry."),
    ("The three types of congruence transformations (isometries) are:", ["Dilation, rotation, translation", "*Reflection, rotation, translation", "Shear, stretch, rotate", "Scale, flip, slide"], "Reflection, rotation, translation."),
    ("A translation moves every point:", ["In different directions", "*The same distance in the same direction", "Toward a center", "Around a point"], "Slide."),
    ("A reflection flips a figure across a:", ["Point", "*Line (line of reflection)", "Circle", "Vertex"], "Line of reflection."),
    ("A rotation turns a figure around a:", ["Line", "*Fixed point (center of rotation)", "Plane", "Vertex"], "Center of rotation."),
    ("All three isometries produce figures that are _____ to the original.", ["Similar", "*Congruent", "Parallel", "Perpendicular"], "Isometries preserve congruence."),
    ("A dilation is NOT an isometry because it changes:", ["Angles", "*Size (distances are multiplied by the scale factor)", "Shape", "Orientation"], "Dilation changes size."),
    ("Reflecting a figure twice across parallel lines is equivalent to a:", ["Rotation", "*Translation", "Dilation", "Single reflection"], "Double reflection = translation."),
    ("Reflecting a figure twice across intersecting lines is equivalent to a:", ["Translation", "*Rotation", "Dilation", "Single reflection"], "Double reflection = rotation."),
    ("A glide reflection is a combination of:", ["Two rotations", "*A translation followed by a reflection", "A rotation and dilation", "Two dilations"], "Slide then flip."),
    ("Isometries preserve:", ["Area only", "Perimeter only", "*Distance, angle measure, area, and perimeter", "Nothing"], "All measurements preserved."),
    ("The image is the figure _____ the transformation.", ["Before", "*After", "During", "Instead of"], "Image = result."),
    ("The pre-image is the figure _____ the transformation.", ["After", "*Before", "During", "Instead of"], "Pre-image = original."),
])
all_new[k] = q

k, q = add_qs("u4_l4.8", [
    ("In a coordinate proof for triangles, you assign coordinates to:", ["Only one vertex", "*All three vertices (choosing strategically to simplify)", "Only the midpoint", "No points"], "All vertices get coordinates."),
    ("A common strategy places one vertex at:", ["(1,1)", "*(0,0) (the origin)", "(5,5)", "Any point"], "Origin simplifies calculations."),
    ("For a right triangle, place the right angle at the origin with legs along:", ["Diagonals", "*The x-axis and y-axis", "Random lines", "Parallel lines"], "Axes alignment."),
    ("For an isosceles triangle, align the axis of symmetry with:", ["The x-axis", "*The y-axis (placing the base along the x-axis)", "A diagonal", "No axis"], "Symmetry along y-axis."),
    ("Using variables (a, b) instead of specific numbers makes the proof:", ["Specific to one triangle", "*General (applies to all triangles of that type)", "More complex", "Invalid"], "Generality."),
    ("The midpoint of segment from (0,0) to (2a,0) is:", ["(a,a)", "*(a,0)", "(2a,0)", "(0,a)"], "(0+2a)/2=a, (0+0)/2=0."),
    ("To prove a property of isosceles triangles, place vertices at:", ["Random locations", "*(-a,0), (a,0), (0,b) — using symmetry", "(0,0), (1,0), (0,1)", "(1,1), (2,2), (3,3)"], "Symmetric placement."),
    ("The distance from (-a,0) to (0,b) equals the distance from (a,0) to (0,b) because:", ["a = b", "*sqrt(a² + b²) = sqrt(a² + b²) — the formula gives the same result", "Both are on the y-axis", "They're adjacent"], "Symmetric distance."),
    ("In a coordinate proof, 'show' means:", ["Draw a picture", "*Use formulas (distance, slope, midpoint) to demonstrate algebraically", "Estimate", "Guess"], "Algebraic demonstration."),
    ("To prove a median bisects a side, show the endpoint of the median is the:", ["Vertex", "Origin", "*Midpoint of the opposite side", "Centroid"], "Median endpoint = midpoint."),
    ("A coordinate proof of the Triangle Midsegment Theorem shows the midsegment is _____ to the third side.", ["Perpendicular", "*Parallel (same slope) and half the length", "Equal", "Congruent"], "Midsegment properties."),
    ("Why use a coordinate proof instead of a synthetic proof?", ["It's always easier", "*Algebra and formulas can verify geometric relationships precisely", "It's required", "It's the only valid method"], "Algebraic precision."),
    ("After placing a triangle for a coordinate proof, the next step is usually:", ["Draw a picture", "*Calculate distances, slopes, or midpoints as needed", "Guess the result", "Estimate"], "Computation."),
])
all_new[k] = q

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

for key, new_qs in all_new.items():
    if key in data:
        data[key]["quiz_questions"].extend(new_qs)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Geometry U1-U4: expanded {len(all_new)} lessons")
