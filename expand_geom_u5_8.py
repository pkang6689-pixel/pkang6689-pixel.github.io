#!/usr/bin/env python3
"""Expand Geometry U5-U8 quizzes from 7 to 20 questions each (29 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "geometry_lessons.json")

def add_qs(key, new_questions):
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

# ── U5: Triangle Inequalities & Special Segments ──

k, q = add_qs("u5_l5.1", [
    ("The perpendicular bisector of a segment passes through the segment's:", ["Endpoint", "*Midpoint at a 90° angle", "Vertex", "Centroid"], "Perpendicular bisector = midpoint + 90°."),
    ("Any point on the perpendicular bisector of a segment is:", ["Closer to one endpoint", "*Equidistant from both endpoints", "At the midpoint", "On the segment"], "Equidistance theorem."),
    ("The converse: if a point is equidistant from both endpoints, it lies on the:", ["Segment", "*Perpendicular bisector", "Angle bisector", "Median"], "Converse of equidistance."),
    ("An angle bisector divides an angle into:", ["Unequal parts", "*Two congruent angles", "Three parts", "Complementary angles"], "Bisector = equal halves."),
    ("Any point on an angle bisector is equidistant from:", ["The vertex", "*The two sides of the angle", "The endpoints of the angle", "The opposite side"], "Angle Bisector Equidistance."),
    ("The circumcenter of a triangle is where the three _____ meet.", ["Angle bisectors", "*Perpendicular bisectors", "Medians", "Altitudes"], "Circumcenter = perp bisectors."),
    ("The circumcenter is equidistant from the triangle's three:", ["Sides", "*Vertices", "Midpoints", "Altitudes"], "Equidistant from vertices."),
    ("The incenter of a triangle is where the three _____ meet.", ["Perpendicular bisectors", "*Angle bisectors", "Medians", "Altitudes"], "Incenter = angle bisectors."),
    ("The incenter is equidistant from the triangle's three:", ["Vertices", "*Sides", "Midpoints", "Medians"], "Equidistant from sides."),
    ("The circumscribed circle (circumcircle) has its center at the:", ["Incenter", "*Circumcenter", "Centroid", "Orthocenter"], "Circumcircle centered at circumcenter."),
    ("The inscribed circle (incircle) has its center at the:", ["Circumcenter", "*Incenter", "Centroid", "Orthocenter"], "Incircle centered at incenter."),
    ("For an acute triangle, the circumcenter lies:", ["Outside the triangle", "*Inside the triangle", "On a side", "At a vertex"], "Acute = circumcenter inside."),
    ("For a right triangle, the circumcenter lies:", ["Inside the triangle", "*On the hypotenuse (at its midpoint)", "Outside the triangle", "At the right angle vertex"], "Right = circumcenter on hypotenuse."),
])
all_new[k] = q

k, q = add_qs("u5_l5.2", [
    ("A median of a triangle connects a vertex to the:", ["Foot of the altitude", "*Midpoint of the opposite side", "Circumcenter", "Incenter"], "Median definition."),
    ("An altitude of a triangle is a perpendicular segment from a vertex to the:", ["Midpoint of the opposite side", "*Line containing the opposite side", "Adjacent side", "Median"], "Altitude definition."),
    ("The centroid is the intersection of the three:", ["Altitudes", "Angle bisectors", "*Medians", "Perpendicular bisectors"], "Centroid = medians."),
    ("The centroid divides each median in a ratio of:", ["1:1", "*2:1 (from vertex to midpoint)", "3:1", "1:2"], "2 parts from vertex, 1 from midpoint."),
    ("The centroid is also called the:", ["Circumcenter", "*Center of gravity (balance point)", "Incenter", "Orthocenter"], "Balance point."),
    ("The orthocenter is the intersection of the three:", ["Medians", "Perpendicular bisectors", "*Altitudes", "Angle bisectors"], "Orthocenter = altitudes."),
    ("For an obtuse triangle, the orthocenter lies:", ["Inside the triangle", "*Outside the triangle", "On the hypotenuse", "At a vertex"], "Obtuse = orthocenter outside."),
    ("For a right triangle, the orthocenter is at the:", ["Circumcenter", "Centroid", "*Vertex of the right angle", "Midpoint of hypotenuse"], "Right angle vertex."),
    ("A midsegment of a triangle connects:", ["Two vertices", "*The midpoints of two sides", "A vertex and midpoint", "Two altitudes"], "Midsegment definition."),
    ("A midsegment is parallel to the third side and _____ its length.", ["Equal to", "*Half", "Double", "One-third"], "Midsegment theorem."),
    ("The four special points (circumcenter, incenter, centroid, orthocenter) all coincide in a(n):", ["Right triangle", "Isosceles triangle", "*Equilateral triangle", "Scalene triangle"], "All four coincide in equilateral."),
    ("In a coordinate plane, the centroid of vertices (x1,y1), (x2,y2), (x3,y3) is:", ["((x1+x2)/2, (y1+y2)/2)", "*((x1+x2+x3)/3, (y1+y2+y3)/3)", "(x1*x2*x3, y1*y2*y3)", "((x2-x1), (y2-y1))"], "Average of coordinates."),
    ("Euler's Line passes through the:", ["Incenter, centroid, circumcenter", "*Circumcenter, centroid, orthocenter", "All four centers", "Only the centroid"], "Euler's Line: circumcenter, centroid, orthocenter."),
])
all_new[k] = q

k, q = add_qs("u5_l5.3", [
    ("In a triangle, the longest side is opposite the:", ["Smallest angle", "*Largest angle", "Middle angle", "Right angle only"], "Larger angle = longer opposite side."),
    ("In a triangle, the largest angle is opposite the:", ["Shortest side", "*Longest side", "Middle side", "Equal sides"], "Longer side = larger opposite angle."),
    ("In triangle ABC, if AB > BC > CA, then:", ["angle A > angle B > angle C", "angle C > angle A > angle B", "*angle C > angle A > angle B", "angle B > angle C > angle A"], "C is opposite AB (longest), so C is largest."),
    ("If angle P = 40°, angle Q = 60°, angle R = 80° in triangle PQR, the longest side is:", ["PQ", "QR", "*PQ (opposite R, the largest angle)", "PR"], "Opposite the largest angle."),
    ("The Exterior Angle Inequality: an exterior angle is greater than:", ["The adjacent interior angle", "*Each non-adjacent (remote) interior angle", "All interior angles", "No other angle"], "Greater than each remote interior."),
    ("If two sides of a triangle are 5 and 8, the third side must be:", ["Exactly 3", "Exactly 13", "*Greater than 3 and less than 13", "Any positive number"], "Triangle Inequality."),
    ("In a triangle with sides 7, 10, and x, which inequality must hold?", ["x > 17", "*3 < x < 17", "x = 3", "x < 3"], "|7-10| < x < 7+10."),
    ("If two sides of a triangle are equal, the angles opposite them are:", ["Different", "*Equal (Isosceles Triangle Theorem)", "Supplementary", "Complementary"], "Isosceles base angles equal."),
    ("The angle-side relationship is a direct consequence of the:", ["Pythagorean Theorem", "*Properties of triangles (larger angle 'opens' wider to a longer side)", "Circle theorems", "Parallel postulate"], "Geometric reasoning."),
    ("In an equilateral triangle, all sides are equal so all angles are:", ["90°", "*60° (equal)", "45°", "120°"], "Equilateral = equiangular."),
    ("If angle A > angle B in a triangle, then:", ["Side a < side b", "*Side a > side b (the side opposite the larger angle is longer)", "Side a = side b", "Cannot determine"], "Larger angle = longer opposite side."),
    ("Comparing two sides helps determine the:", ["Area", "*Relative sizes of opposite angles", "Perimeter", "Type of triangle only"], "Side-angle relationship."),
    ("The shortest distance from a vertex to the opposite side is the:", ["Median", "*Altitude", "Angle bisector", "Perpendicular bisector"], "Altitude is perpendicular (shortest)."),
])
all_new[k] = q

k, q = add_qs("u5_l5.4", [
    ("An indirect proof starts by:", ["Assuming the conclusion is true", "*Assuming the opposite of what you want to prove (negation of the conclusion)", "Proving the converse", "Drawing a diagram"], "Assume the negation."),
    ("Another name for indirect proof is:", ["Direct proof", "*Proof by contradiction", "Two-column proof", "Coordinate proof"], "Proof by contradiction."),
    ("In an indirect proof, you derive a:", ["Tautology", "*Contradiction (showing the assumption leads to something false)", "True statement", "Postulate"], "Contradiction ends the proof."),
    ("The contradiction shows the original assumption was:", ["True", "*False (so the desired conclusion must be true)", "Irrelevant", "Incomplete"], "Negation is false, so conclusion is true."),
    ("Indirect proof is useful when:", ["Direct proof is easy", "*It's hard to prove the statement directly", "The statement is false", "There's no theorem to apply"], "When direct proof is difficult."),
    ("Step 1 of indirect proof: Assume _____ is true.", ["The conclusion", "*The negation of the conclusion", "The hypothesis", "A theorem"], "Negate what you want to prove."),
    ("Step 2 of indirect proof: Use the assumption and given info to reach a:", ["Proof", "Diagram", "*Contradiction (a false or impossible statement)", "Conjecture"], "Derive contradiction."),
    ("Step 3 of indirect proof: Conclude the assumption was false, so the _____ is true.", ["Hypothesis", "*Original conclusion (what you wanted to prove)", "Assumption", "Converse"], "Original statement is true."),
    ("To indirectly prove 'x is not 5,' assume:", ["x is not 5", "*x is 5, then show this leads to a contradiction", "x > 5", "x < 5"], "Assume the negation."),
    ("Indirect proof is a form of:", ["Inductive reasoning", "*Deductive reasoning", "Guessing", "Estimation"], "Logical deduction."),
    ("A famous indirect proof shows that the square root of 2 is:", ["Rational", "*Irrational (by showing a rational assumption leads to contradiction)", "An integer", "Undefined"], "Classic proof by contradiction."),
    ("In geometry, indirect proof often shows something _____ exist or _____ happen.", ["Can, can", "*Cannot, cannot (impossibility)", "Will, will", "Might, might"], "Proving impossibility."),
    ("The key logical principle behind indirect proof: a statement and its negation cannot both be:", ["False", "*True at the same time", "Related", "Proven"], "Law of non-contradiction."),
])
all_new[k] = q

k, q = add_qs("u5_l5.5", [
    ("The Triangle Inequality Theorem states that the sum of any two sides must be:", ["Equal to the third", "Less than the third", "*Greater than the third side", "Less than or equal to the third"], "Sum > third side."),
    ("Can a triangle have sides 3, 4, and 8?", ["Yes", "*No (3 + 4 = 7 < 8)", "Sometimes", "Only if right"], "Fails triangle inequality."),
    ("Can a triangle have sides 5, 7, and 11?", ["*Yes (5+7=12 > 11, 5+11=16 > 7, 7+11=18 > 5)", "No", "Only if isosceles", "Only if equilateral"], "All three inequalities hold."),
    ("The triangle inequality must hold for _____ pair(s) of sides.", ["One", "Two", "*All three", "None"], "Check all three combinations."),
    ("If sides are a, b, c, the three inequalities are: a+b > c, a+c > b, and:", ["a+b > a", "*b+c > a", "a-b < c", "a*b > c"], "Third inequality."),
    ("The range of the third side when two sides are 6 and 10 is:", ["4 to 16 (inclusive)", "*Greater than 4 and less than 16", "6 to 10", "0 to 16"], "|6-10| < x < 6+10."),
    ("The shortest path between two points is a:", ["Curved line", "Zigzag", "*Straight line (which relates to triangle inequality)", "Circle"], "Straight line is shortest."),
    ("If a+b = c, the 'triangle' is actually a:", ["Valid triangle", "*Degenerate case (three collinear points forming a line segment)", "Right triangle", "Circle"], "Collinear = degenerate."),
    ("Three segments of equal length can ALWAYS form a(n):", ["Right triangle", "*Equilateral triangle", "Obtuse triangle", "Impossible figure"], "Equal sides = equilateral."),
    ("Can a triangle have sides 1, 1, and 2?", ["Yes", "*No (1 + 1 = 2, not greater than 2)", "Only right triangle", "Only isosceles"], "Fails: 1+1 is not > 2."),
    ("The triangle inequality is related to the fact that:", ["All triangles are right", "Angles sum to 180°", "*A straight line is the shortest distance between two points", "Side lengths must be positive"], "Shortest path principle."),
    ("For sides 8, 15, and x, x could be:", ["0", "23", "*10 (since 7 < x < 23)", "7"], "7 < x < 23; only 10 is in range."),
    ("If you're given three lengths and need to check if they form a triangle, test:", ["Only the two largest", "*Whether the two smallest sides sum to more than the largest", "All products", "All differences"], "Sufficient to check smallest pair vs largest."),
])
all_new[k] = q

k, q = add_qs("u5_l5.6", [
    ("The Hinge Theorem (SAS Inequality) compares two triangles that share:", ["All three sides", "*Two pairs of congruent sides but different included angles", "All three angles", "One side only"], "Two sides equal, different included angle."),
    ("In the Hinge Theorem: if two sides of one triangle are congruent to two sides of another, the triangle with the larger included angle has the:", ["Shorter third side", "*Longer third side", "Same third side", "Smaller perimeter"], "Larger angle = longer opposite side."),
    ("The converse of the Hinge Theorem: if two sides are congruent and one third side is longer, the angle opposite the longer side is:", ["Smaller", "*Larger", "Equal", "A right angle"], "Longer third side = larger included angle."),
    ("The Hinge Theorem is sometimes called the:", ["SSS Inequality", "*SAS Inequality Theorem", "ASA Inequality", "Triangle Inequality"], "SAS Inequality."),
    ("If triangle ABC has AB = DE, BC = EF, and angle B > angle E, then:", ["AC < DF", "AC = DF", "*AC > DF", "Cannot determine"], "Hinge Theorem."),
    ("The Hinge Theorem extends the idea that in a single triangle:", ["All sides are equal", "*A larger angle is opposite a longer side", "All angles are equal", "Angles don't affect sides"], "Angle-side relationship across triangles."),
    ("If two alligator jaws open at different angles but have the same jaw length, the wider jaw has a _____ opening.", ["Smaller", "*Larger (greater distance between jaw tips)", "Same", "Narrower"], "Physical analogy for Hinge Theorem."),
    ("To apply the Hinge Theorem, you need _____ pairs of congruent sides.", ["1", "*2", "3", "0"], "Two sides must match."),
    ("The Hinge Theorem does NOT apply when:", ["Two sides are congruent", "Included angles differ", "*The two congruent side pairs don't match (SAS condition not met)", "The angles are known"], "Must have SAS structure."),
    ("If triangle 1 and triangle 2 share sides of 5 and 7, and included angles are 50° and 70°, which has the longer third side?", ["Triangle 1 (50°)", "*Triangle 2 (70° — larger included angle means longer third side)", "They're equal", "Cannot determine"], "Hinge Theorem: larger angle = longer side."),
    ("The Hinge Theorem can be proven using:", ["Only construction", "*The Triangle Inequality and angle/side relationships", "Only algebra", "Coordinate geometry only"], "Proof method."),
    ("An everyday example: a door opened wider has a _____ gap between the edge and the frame.", ["Smaller", "*Larger", "Same", "Zero"], "Wider angle = larger opening."),
    ("The Hinge Theorem gives an inequality, not an exact:", ["Angle", "Side", "*Measurement (it says 'greater than,' not 'equals')", "Proof"], "Inequality relationship."),
])
all_new[k] = q

# ── U6: Quadrilaterals ──

k, q = add_qs("u6_l6.1", [
    ("The sum of interior angles of an n-sided polygon is:", ["180n", "360°", "*(n-2) × 180°", "n × 90°"], "(n-2)×180."),
    ("The sum of interior angles of a pentagon (5 sides) is:", ["360°", "720°", "*540°", "900°"], "(5-2)×180=540."),
    ("The sum of interior angles of a hexagon is:", ["540°", "*720°", "900°", "1080°"], "(6-2)×180=720."),
    ("Each interior angle of a regular n-gon is:", ["180/n", "*(n-2)×180/n", "360/n", "n×90"], "(n-2)×180/n."),
    ("Each interior angle of a regular octagon is:", ["120°", "*135°", "144°", "150°"], "(8-2)×180/8=135."),
    ("The sum of exterior angles of ANY convex polygon is:", ["180°", "540°", "*360°", "720°"], "Always 360°."),
    ("Each exterior angle of a regular n-gon is:", ["(n-2)×180/n", "*360/n", "180/n", "n×360"], "360/n."),
    ("Each exterior angle of a regular hexagon is:", ["*60°", "90°", "120°", "45°"], "360/6=60."),
    ("An interior angle and its corresponding exterior angle are:", ["Complementary", "*Supplementary (sum to 180°)", "Congruent", "Vertical"], "Interior + exterior = 180."),
    ("A triangle has interior angle sum:", ["360°", "*180°", "270°", "540°"], "(3-2)×180=180."),
    ("The number of triangles formed by diagonals from one vertex of an n-gon is:", ["n", "n-1", "*n-2", "n-3"], "n-2 triangles."),
    ("A regular polygon has all _____ and all _____ congruent.", ["Vertices, diagonals", "*Sides, angles", "Diagonals, medians", "Faces, edges"], "Regular = equal sides + equal angles."),
    ("If each exterior angle of a regular polygon is 20°, the polygon has _____ sides.", ["10", "15", "*18", "20"], "360/20=18."),
])
all_new[k] = q

k, q = add_qs("u6_l6.2", [
    ("A parallelogram has:", ["One pair of parallel sides", "*Two pairs of parallel sides", "No parallel sides", "Four right angles"], "Parallelogram = 2 pairs parallel."),
    ("Opposite sides of a parallelogram are:", ["Perpendicular", "*Congruent and parallel", "Only parallel", "Only congruent"], "Both congruent and parallel."),
    ("Opposite angles of a parallelogram are:", ["Supplementary", "*Congruent", "Complementary", "Right angles"], "Opposite angles are equal."),
    ("Consecutive angles of a parallelogram are:", ["Congruent", "*Supplementary (sum to 180°)", "Complementary", "Vertical"], "Consecutive = supplementary."),
    ("The diagonals of a parallelogram:", ["Are congruent", "Are perpendicular", "*Bisect each other", "Don't intersect"], "Diagonals bisect each other."),
    ("If ABCD is a parallelogram and angle A = 70°, then angle B =", ["70°", "*110°", "140°", "90°"], "Consecutive: 180-70=110."),
    ("If ABCD is a parallelogram and angle A = 70°, then angle C =", ["110°", "*70° (opposite angles are congruent)", "140°", "90°"], "Opposite: same measure."),
    ("If the diagonals of parallelogram ABCD intersect at E, then AE ≅", ["BD", "CD", "*CE (diagonals bisect each other)", "AB"], "Bisect means AE = CE."),
    ("AB ∥ CD and AD ∥ BC describes a:", ["Trapezoid", "*Parallelogram", "Kite", "Regular polygon"], "Two pairs parallel."),
    ("The perimeter of a parallelogram with sides 5 and 8 is:", ["13", "40", "*26", "80"], "2(5+8)=26."),
    ("A parallelogram with side lengths a and b has perimeter:", ["ab", "a+b", "*2(a+b)", "4a"], "2a+2b."),
    ("If one side of a parallelogram is 12, the opposite side is:", ["6", "24", "*12", "Cannot tell"], "Opposite sides are congruent."),
    ("Each diagonal divides a parallelogram into:", ["Four congruent triangles", "*Two congruent triangles", "Two similar triangles", "Unequal parts"], "Diagonal creates two congruent triangles."),
])
all_new[k] = q

k, q = add_qs("u6_l6.3", [
    ("To prove a quadrilateral is a parallelogram, show both pairs of opposite sides are:", ["Perpendicular", "*Parallel (or congruent)", "Adjacent", "Unequal"], "Both pairs parallel or congruent."),
    ("If both pairs of opposite sides are congruent, the quadrilateral is a:", ["Kite", "*Parallelogram", "Trapezoid", "Rectangle only"], "Test for parallelogram."),
    ("If one pair of opposite sides is both parallel and congruent, it's a:", ["Trapezoid", "*Parallelogram", "Kite", "Rhombus only"], "One pair: parallel + congruent = enough."),
    ("If the diagonals bisect each other, the quadrilateral is a:", ["Kite", "*Parallelogram", "Trapezoid", "Regular polygon"], "Diagonal bisection test."),
    ("If both pairs of opposite angles are congruent, it's a:", ["Trapezoid", "*Parallelogram", "Kite", "Regular polygon"], "Opposite angles congruent test."),
    ("How many tests exist for proving a parallelogram?", ["2", "3", "*5 (both opposite sides parallel; both opposite sides congruent; one pair both parallel and congruent; diagonals bisect; both opposite angles congruent)", "1"], "Five tests."),
    ("To prove ABCD is a parallelogram using slopes, show:", ["All slopes are equal", "*Slope AB = slope CD AND slope BC = slope AD (opposite sides parallel)", "Adjacent slopes are equal", "Slopes multiply to -1"], "Parallel = equal slopes."),
    ("To prove using midpoints: the diagonals have the same _____ (they bisect each other).", ["Length", "*Midpoint", "Slope", "Endpoint"], "Same midpoint = bisect."),
    ("If consecutive angles are supplementary, the figure is a:", ["Triangle", "*Parallelogram", "Kite", "Pentagon"], "Supplementary consecutive angles."),
    ("A quadrilateral with vertices A(0,0), B(4,0), C(6,3), D(2,3): slopes AB = 0, CD = 0 (parallel), AD = 3/2, BC = 3/2 (parallel). It's a:", ["Trapezoid", "*Parallelogram", "Kite", "Rectangle"], "Both pairs parallel."),
    ("NOT sufficient to prove a parallelogram: one pair of sides is _____ and the other pair is _____.", ["Parallel, equal", "*One pair parallel, one pair congruent (but not the same pair)", "Both parallel", "Both congruent"], "Different pairs: not sufficient."),
    ("Using distance formula: if AB = CD and BC = AD, then ABCD is a:", ["Only a quadrilateral", "*Parallelogram", "Only a rectangle", "Only a rhombus"], "Both opposite pairs congruent."),
    ("The coordinate methods for testing parallelogram properties use:", ["Only angles", "*Slope (for parallel), distance (for congruent), midpoint (for bisection)", "Only area", "Only perimeter"], "Three formulas."),
])
all_new[k] = q

k, q = add_qs("u6_l6.4", [
    ("A rectangle is a parallelogram with:", ["All sides equal", "*Four right angles", "Perpendicular diagonals", "No parallel sides"], "Rectangle = 4 right angles."),
    ("The diagonals of a rectangle are:", ["Perpendicular", "*Congruent (equal in length)", "Parallel", "Unequal"], "Rectangle diagonals are equal."),
    ("If ABCD is a rectangle and AC = 10, then BD =", ["5", "20", "*10", "Cannot tell"], "Diagonals are congruent."),
    ("If the diagonals of a parallelogram are congruent, it's a:", ["Rhombus", "*Rectangle", "Kite", "Trapezoid"], "Congruent diagonals test for rectangle."),
    ("A rectangle has all the properties of a parallelogram plus:", ["Perpendicular diagonals", "*Right angles and congruent diagonals", "All sides equal", "Only one pair of parallel sides"], "Additional rectangle properties."),
    ("The area of a rectangle with length 8 and width 5 is:", ["13", "26", "*40", "80"], "A = l × w = 40."),
    ("Every square is a rectangle, but not every rectangle is a:", ["Parallelogram", "Quadrilateral", "*Square", "Polygon"], "Square is a special rectangle."),
    ("If one angle of a parallelogram is 90°, all angles are 90° and it's a:", ["Rhombus", "Kite", "*Rectangle", "Trapezoid"], "One right angle + parallelogram = all right angles."),
    ("The diagonals of a rectangle bisect each other because it's a:", ["Rectangle", "*Parallelogram (rectangles inherit all parallelogram properties)", "Square", "Rhombus"], "Parallelogram property."),
    ("To prove a quadrilateral is a rectangle, first show it's a parallelogram, then show:", ["All sides equal", "*One angle is 90° (or diagonals are congruent)", "Diagonals are perpendicular", "It has an altitude"], "Parallelogram + right angle = rectangle."),
    ("The diagonal of a rectangle with sides a and b has length:", ["a + b", "ab", "*sqrt(a² + b²)", "2(a+b)"], "Pythagorean theorem."),
    ("A rectangle has _____ lines of symmetry.", ["0", "1", "*2", "4"], "Two lines of symmetry."),
    ("In coordinate geometry, a rectangle has all adjacent sides with slopes that are:", ["Equal", "*Negative reciprocals (perpendicular)", "Zero", "Undefined"], "Right angles = perpendicular sides."),
])
all_new[k] = q

k, q = add_qs("u6_l6.5", [
    ("A rhombus is a parallelogram with:", ["Four right angles", "*All four sides congruent", "Congruent diagonals", "No parallel sides"], "All sides equal."),
    ("The diagonals of a rhombus are:", ["Congruent", "*Perpendicular bisectors of each other", "Parallel", "Equal in length"], "Diagonals are perpendicular."),
    ("A square is both a _____ and a _____.", ["Triangle and circle", "*Rectangle and rhombus", "Kite and trapezoid", "Pentagon and hexagon"], "Square = rectangle + rhombus."),
    ("Each diagonal of a rhombus bisects a pair of:", ["Sides", "*Opposite angles", "Adjacent angles", "Diagonals"], "Diagonal bisects vertex angles."),
    ("If the diagonals of a parallelogram are perpendicular, it's a:", ["Rectangle", "*Rhombus", "Trapezoid", "Kite"], "Perpendicular diagonals test for rhombus."),
    ("If a side of a rhombus is 6, the perimeter is:", ["12", "18", "*24", "36"], "4 × 6 = 24."),
    ("The area of a rhombus with diagonals d1 and d2 is:", ["d1 + d2", "d1 × d2", "*(d1 × d2)/2", "2(d1 + d2)"], "Half the product of diagonals."),
    ("A rhombus has _____ lines of symmetry.", ["0", "1", "*2", "4"], "Two: along each diagonal."),
    ("A square has _____ lines of symmetry.", ["2", "3", "*4", "8"], "4 lines of symmetry."),
    ("All squares are rhombi, but not all rhombi are:", ["Parallelograms", "*Squares (rhombi don't necessarily have right angles)", "Quadrilaterals", "Polygons"], "Squares need right angles too."),
    ("If one angle of a rhombus is 60°, the consecutive angle is:", ["60°", "*120°", "90°", "30°"], "Consecutive: 180-60=120."),
    ("To prove a parallelogram is a rhombus, show:", ["Diagonals are congruent", "*Two consecutive sides are congruent (or diagonals are perpendicular)", "All angles are 90°", "It has 4 sides"], "Consecutive sides equal or perp diagonals."),
    ("The diagonals of a square are:", ["Only perpendicular", "Only congruent", "*Both perpendicular and congruent", "Neither"], "Square: both properties."),
])
all_new[k] = q

k, q = add_qs("u6_l6.6", [
    ("A trapezoid has exactly:", ["No parallel sides", "Two pairs of parallel sides", "*One pair of parallel sides", "Three parallel sides"], "Trapezoid = one pair parallel."),
    ("The parallel sides of a trapezoid are called:", ["Legs", "*Bases", "Diagonals", "Medians"], "Bases are parallel."),
    ("The non-parallel sides of a trapezoid are called:", ["Bases", "*Legs", "Diagonals", "Altitudes"], "Legs = non-parallel sides."),
    ("An isosceles trapezoid has:", ["All sides equal", "Parallel legs", "*Congruent legs", "Perpendicular diagonals"], "Isosceles = legs congruent."),
    ("The base angles of an isosceles trapezoid are:", ["Supplementary", "*Congruent (each pair of base angles)", "Complementary", "Vertical"], "Isosceles trap base angles equal."),
    ("The diagonals of an isosceles trapezoid are:", ["Perpendicular", "*Congruent", "Parallel", "Bisecting each other"], "Isosceles trap diagonals equal."),
    ("A kite has:", ["Two pairs of parallel sides", "*Two pairs of consecutive congruent sides", "All four sides equal", "No congruent sides"], "Kite: two pairs of adjacent equal sides."),
    ("The diagonals of a kite are:", ["Congruent", "*Perpendicular (and exactly one diagonal is bisected by the other)", "Parallel", "Equal"], "Kite diagonals are perpendicular."),
    ("In a kite, the pair of opposite angles between the unequal sides are:", ["Supplementary", "*Congruent", "Right angles", "Complementary"], "Non-vertex angles are congruent."),
    ("The midsegment (median) of a trapezoid is parallel to the bases and its length is:", ["The sum of the bases", "*The average of the two bases: (b1 + b2)/2", "Half the shorter base", "Twice the longer base"], "Average of bases."),
    ("If the bases of a trapezoid are 8 and 14, the midsegment length is:", ["8", "14", "*11", "22"], "(8+14)/2=11."),
    ("A kite has _____ line(s) of symmetry.", ["0", "*1 (along the diagonal connecting the vertex angles)", "2", "4"], "One axis of symmetry."),
    ("The area of a kite with diagonals d1 and d2 is:", ["d1 + d2", "d1 × d2", "*(d1 × d2)/2", "2(d1 + d2)"], "Same formula as rhombus."),
])
all_new[k] = q

k, q = add_qs("u6_l6.7", [
    ("A regular polygon is both equilateral and:", ["Scalene", "*Equiangular", "Isosceles", "Obtuse"], "Equilateral + equiangular = regular."),
    ("A regular polygon can be inscribed in a:", ["Line", "*Circle", "Square always", "Triangle"], "Inscribed in a circle."),
    ("The center of a regular polygon is equidistant from all:", ["Sides only", "Vertices only", "*Both vertices and (perpendicular distance to) sides", "Diagonals"], "Center to vertices and to sides."),
    ("The apothem of a regular polygon is the distance from the center to:", ["A vertex", "*The midpoint of a side (perpendicular distance)", "A diagonal", "An exterior point"], "Apothem = perpendicular to side."),
    ("The area of a regular polygon is: A =", ["s²", "πr²", "*½ × apothem × perimeter", "base × height"], "A = ½aP."),
    ("Rotational symmetry means the figure maps onto itself after a:", ["Reflection", "*Rotation of less than 360°", "Translation", "Dilation"], "Rotation < 360° maps to itself."),
    ("A regular n-gon has rotational symmetry of order:", ["1", "*n (it maps onto itself n times in a full rotation)", "2", "n-1"], "Order n."),
    ("The angle of rotation for a regular n-gon is:", ["180/n", "*360/n degrees", "n degrees", "90 degrees"], "360/n."),
    ("A regular hexagon has _____ lines of symmetry.", ["3", "*6", "2", "12"], "n lines of symmetry for regular n-gon."),
    ("Line symmetry means one half is a mirror image of the other across a:", ["Point", "*Line (line of symmetry / axis of symmetry)", "Plane", "Circle"], "Reflection across a line."),
    ("A regular pentagon has rotational symmetry of:", ["90°", "60°", "*72° (360/5)", "45°"], "360/5=72."),
    ("Point symmetry means the figure looks the same after 180° rotation about:", ["Any point", "*The center point", "A vertex", "A side"], "Half-turn symmetry."),
    ("All regular polygons have both _____ and _____ symmetry.", ["Only line", "Only rotational", "*Line (reflective) and rotational", "Neither"], "Both types of symmetry."),
])
all_new[k] = q

# ── U7: Similarity ──

k, q = add_qs("u7_l7.1", [
    ("A ratio compares two quantities by:", ["Addition", "Subtraction", "*Division", "Multiplication"], "Ratio = a/b."),
    ("The ratio of 8 to 12 in simplest form is:", ["8:12", "4:6", "*2:3", "1:2"], "Divide both by 4."),
    ("A proportion is an equation stating two _____ are equal.", ["Sums", "Products", "*Ratios", "Differences"], "Proportion = equal ratios."),
    ("In a/b = c/d, the cross products are:", ["a+d and b+c", "*ad and bc (and they are equal)", "ac and bd", "a/c and b/d"], "Cross multiplication."),
    ("If 3/x = 6/10, then x =", ["6", "10", "*5", "3"], "3×10=6x, x=5."),
    ("The means in a:b = c:d are:", ["a and d", "*b and c", "a and c", "b and d"], "Means are the inner terms."),
    ("The extremes in a:b = c:d are:", ["b and c", "*a and d", "a and b", "c and d"], "Extremes are the outer terms."),
    ("Properties of proportions: if a/b = c/d, then a/c = b/d. This is the:", ["Cross product property", "*Alternation property (switching means)", "Addition property", "Inverse property"], "Alternation."),
    ("If a/b = c/d, then (a+b)/b = (c+d)/d. This is the:", ["Cross product", "*Addition property of proportions", "Subtraction property", "Alternation"], "Add denominator to numerator."),
    ("In a scale drawing, 1 inch = 10 miles. A 3.5-inch segment represents:", ["10 miles", "30 miles", "*35 miles", "100 miles"], "3.5 × 10 = 35."),
    ("The geometric mean of a and b is:", ["(a+b)/2", "a×b", "*sqrt(a×b)", "a/b"], "Geometric mean = sqrt(ab)."),
    ("The geometric mean of 4 and 16 is:", ["10", "20", "*8", "64"], "sqrt(4×16)=sqrt(64)=8."),
    ("When solving proportions, always check that the _____ is not zero.", ["Numerator", "*Denominator", "Mean", "Extreme"], "Division by zero undefined."),
])
all_new[k] = q

k, q = add_qs("u7_l7.2", [
    ("Similar polygons have the same _____ but not necessarily the same _____.", ["Size, shape", "*Shape, size", "Angles, sides", "Area, perimeter"], "Same shape, different size."),
    ("Corresponding angles of similar polygons are:", ["Supplementary", "*Congruent", "Complementary", "Proportional"], "Angles are equal."),
    ("Corresponding sides of similar polygons are:", ["Congruent", "*Proportional", "Perpendicular", "Parallel"], "Sides are proportional."),
    ("The scale factor is the ratio of:", ["Areas", "Perimeters", "*Corresponding side lengths", "Angles"], "Side ratio."),
    ("If triangle ABC ~ triangle DEF with scale factor 3:1, and AB = 12, then DE =", ["36", "12", "*4", "3"], "12 ÷ 3 = 4."),
    ("The symbol for similarity is:", ["≅", "=", "*~", "∥"], "~ means similar."),
    ("If the scale factor of two similar figures is k, the ratio of their perimeters is:", ["k²", "k³", "*k", "1/k"], "Perimeter ratio = scale factor."),
    ("If the scale factor is 2:5, and a side of the smaller figure is 6, the corresponding side of the larger is:", ["12", "2.4", "*15", "30"], "6 × (5/2) = 15."),
    ("Similar figures: the order of vertices in the similarity statement shows:", ["Size order", "*Correspondence", "Alphabetical order", "Nothing"], "Order = correspondence."),
    ("All circles are:", ["Congruent", "*Similar (to every other circle)", "Neither", "Both"], "All circles are similar."),
    ("All squares are:", ["Congruent", "*Similar", "Neither", "Only sometimes similar"], "All squares are similar."),
    ("If the scale factor of similar polygons is 1, the polygons are:", ["Only similar", "*Congruent (and similar)", "Neither", "Different sizes"], "Scale factor 1 = congruent."),
    ("Two rectangles with dimensions 3×5 and 6×10 are similar with scale factor:", ["3:6", "5:10", "*1:2 (or 3:6, simplified)", "2:3"], "3/6 = 5/10 = 1/2."),
])
all_new[k] = q

k, q = add_qs("u7_l7.3", [
    ("AA Similarity: Two triangles are similar if:", ["Two sides are proportional", "*Two angles are congruent", "One angle is congruent", "All sides are proportional"], "AA: two angles sufficient."),
    ("SSS Similarity: Two triangles are similar if:", ["All angles are congruent", "*All three pairs of corresponding sides are proportional", "Two angles and a side match", "One pair of sides is congruent"], "All sides proportional."),
    ("SAS Similarity: Two triangles are similar if:", ["Two angles and a side match", "*Two pairs of sides are proportional and the included angles are congruent", "Three sides are proportional", "One angle is congruent"], "Two proportional sides + included angle."),
    ("If two angles of one triangle equal two angles of another, the third angles are automatically:", ["Different", "*Equal (since all angles sum to 180°)", "Supplementary", "Zero"], "AA determines the third."),
    ("Triangle ABC has angles 30°, 70°, 80°. Triangle DEF has angles 30°, 70°, __. They're similar by:", ["SSS", "*AA (third angle must be 80°)", "SAS", "HL"], "Two angles match."),
    ("To use SSS Similarity, check that:", ["a/d = b/e only", "*a/d = b/e = c/f (all three ratios are equal)", "a = d", "One ratio equals 1"], "All three ratios equal."),
    ("Sides 3,4,5 and 6,8,10: similar?", ["*Yes (ratios are all 1:2)", "No", "Cannot tell", "Only if angles match"], "3/6=4/8=5/10=1/2."),
    ("Sides 3,4,5 and 6,8,11: similar?", ["Yes", "*No (5/11 ≠ 3/6)", "Cannot tell", "Only if angles match"], "Ratios not equal."),
    ("If two triangles are similar, their angles are _____ and sides are _____.", ["Proportional, congruent", "*Congruent, proportional", "Equal, equal", "Proportional, proportional"], "Angles congruent, sides proportional."),
    ("To prove two triangles similar, you need at minimum:", ["Three pairs of sides", "Three pairs of angles", "*Two pairs of congruent angles (AA)", "One pair of sides"], "AA is the minimum."),
    ("Similar triangles have the same:", ["Area", "Perimeter", "*Shape", "Size"], "Same shape."),
    ("Similarity is _____ (A~B and B~C implies A~C).", ["Reflexive only", "Symmetric only", "*Transitive (and also reflexive and symmetric)", "None of these"], "Transitivity of similarity."),
    ("Right triangles with a 30° angle are all similar because:", ["They share a side", "*They share two angles (30° and 90°, so the third is 60°) — AA", "Right angles are special", "They're congruent"], "AA similarity."),
])
all_new[k] = q

k, q = add_qs("u7_l7.4", [
    ("The Triangle Proportionality Theorem: A line parallel to one side of a triangle divides the other two sides:", ["Equally", "*Proportionally", "Perpendicularly", "Into congruent segments only if isosceles"], "Proportional division."),
    ("If DE ∥ BC in triangle ABC, then AD/DB = AE/EC. This is the:", ["Midpoint theorem", "*Triangle Proportionality Theorem (or Side-Splitter Theorem)", "Angle Bisector Theorem", "Hinge Theorem"], "Side-Splitter."),
    ("The converse: if a line divides two sides proportionally, it is _____ to the third side.", ["Perpendicular", "*Parallel", "Congruent", "Equal"], "Converse of Proportionality."),
    ("A midsegment connects midpoints of two sides and is parallel to the third side and _____ its length.", ["Equal to", "Twice", "*Half", "One-third"], "Midsegment theorem."),
    ("If three parallel lines cut two transversals, the segments are:", ["Equal", "*Proportional", "Perpendicular", "Congruent"], "Corollary of proportionality."),
    ("The Angle Bisector Theorem: An angle bisector divides the opposite side in the ratio of:", ["Equal parts", "*The other two sides (adjacent sides)", "The diagonals", "The angles"], "Ratio of adjacent sides."),
    ("In triangle ABC, if the bisector of angle A meets BC at D, then BD/DC =", ["AC/AB", "*AB/AC", "AB/BC", "AC/BC"], "Angle bisector ratio."),
    ("If DE ∥ BC and AD = 4, DB = 6, AE = 5, then EC =", ["4", "6", "*7.5", "10"], "4/6 = 5/EC, EC = 30/4 = 7.5."),
    ("Proportional segments can be used to find _____ lengths indirectly.", ["Angle", "*Missing side", "Area", "Volume"], "Solve for unknowns."),
    ("If a line is parallel to the base of a triangle and bisects one side, it _____ the other side.", ["Trisects", "*Bisects (midpoint theorem)", "Doesn't affect", "Doubles"], "Bisects = midpoint."),
    ("Three parallel lines create proportional segments on _____ transversals.", ["Only one", "*Any two (or more)", "No", "Perpendicular"], "Any transversals."),
    ("If AD/DB = 3/5 and AE = 9, then EC =", ["9", "3", "*15", "5"], "3/5 = 9/EC, EC = 45/3 = 15."),
    ("Proportionality theorems help solve real-world problems involving:", ["Only angles", "*Indirect measurement (shadows, maps, etc.)", "Only areas", "Only volumes"], "Practical measurement."),
])
all_new[k] = q

k, q = add_qs("u7_l7.5", [
    ("In similar triangles, corresponding altitudes are in the same ratio as:", ["Areas", "*Corresponding sides (the scale factor)", "Angles", "Perimeters squared"], "Altitudes are proportional."),
    ("In similar triangles, corresponding medians are proportional to:", ["Angles", "*Corresponding sides", "Areas", "Diagonals"], "Medians in scale factor ratio."),
    ("In similar triangles, corresponding angle bisector lengths are proportional to:", ["Angles", "*Corresponding sides", "Perimeters", "Areas"], "Bisectors in scale factor ratio."),
    ("The ratio of perimeters of similar figures equals:", ["The square of the scale factor", "The cube of the scale factor", "*The scale factor", "1"], "Perimeter ratio = k."),
    ("The ratio of areas of similar figures equals:", ["The scale factor", "*The square of the scale factor (k²)", "The cube", "1"], "Area ratio = k²."),
    ("If two similar triangles have a scale factor of 3:5, the ratio of their areas is:", ["3:5", "*9:25", "27:125", "6:10"], "(3/5)² = 9/25."),
    ("If corresponding altitudes of similar triangles are 4 and 6, the scale factor is:", ["4:6", "*2:3 (simplified)", "6:4", "16:36"], "4/6 = 2/3."),
    ("If the perimeters of two similar figures are 20 and 30, the scale factor is:", ["20:30", "*2:3", "4:9", "400:900"], "20/30 = 2/3."),
    ("If the areas of two similar figures are 16 and 64, the scale factor is:", ["16:64", "4:16", "*1:2 (sqrt(16/64) = sqrt(1/4) = 1/2)", "2:8"], "sqrt(16/64)=1/2."),
    ("Similar triangles with scale factor k have altitude ratio:", ["k²", "k³", "*k", "1/k"], "Same as scale factor."),
    ("An altitude in a right triangle from the right angle to the hypotenuse creates:", ["One similar triangle", "*Two triangles that are similar to each other and the original", "Two congruent triangles", "No special relationship"], "Three similar triangles."),
    ("If two similar pentagons have sides in ratio 2:7, the ratio of their perimeters is:", ["4:49", "*2:7", "2:49", "7:2"], "Perimeter ratio = scale factor."),
    ("Corresponding special segments (medians, altitudes, bisectors) of similar triangles are all in the _____ ratio.", ["Different ratios", "*Same ratio (the scale factor)", "Squared ratio", "No fixed ratio"], "All in scale factor ratio."),
])
all_new[k] = q

k, q = add_qs("u7_l7.6", [
    ("A similarity transformation maps a figure to a _____ figure.", ["Congruent", "*Similar", "Identical", "Perpendicular"], "Produces similar figure."),
    ("A dilation with scale factor k > 1 produces a(n):", ["Smaller figure", "*Larger figure (enlargement)", "Congruent figure", "Opposite figure"], "k > 1 = enlargement."),
    ("A dilation with 0 < k < 1 produces a(n):", ["Larger figure", "*Smaller figure (reduction)", "Congruent figure", "Reflected figure"], "0 < k < 1 = reduction."),
    ("A dilation with k = 1 produces a(n):", ["Larger figure", "Smaller figure", "*Congruent figure (identity)", "Reflected figure"], "k=1: no change."),
    ("The center of dilation is the _____ from which the figure is enlarged/reduced.", ["Edge", "*Fixed point", "Midpoint", "Vertex always"], "Center = fixed point."),
    ("Under a dilation with center O and scale k, the image of point P is P' where OP' =", ["OP", "*k × OP", "OP/k", "OP + k"], "Distance multiplied by k."),
    ("Dilations preserve:", ["Side lengths", "*Angle measures (and shape)", "Distance", "Area"], "Angles preserved; distances scaled."),
    ("A similarity transformation can be a dilation alone or a dilation followed by:", ["Nothing", "*An isometry (reflection, rotation, or translation)", "Another dilation", "A shear"], "Dilation + isometry."),
    ("Under a dilation centered at origin with k=3, point (2,5) maps to:", ["(5,8)", "(2/3, 5/3)", "*(6,15)", "(6,5)"], "(3×2, 3×5) = (6,15)."),
    ("Under a dilation centered at origin with k=½, point (8,4) maps to:", ["(16,8)", "*(4,2)", "(4,8)", "(8,2)"], "(4,2)."),
    ("Dilations are NOT isometries because they change:", ["Angles", "Shape", "*Size (distances are multiplied, not preserved)", "Orientation"], "Size changes."),
    ("A composition of a dilation (k=2) and a rotation produces a:", ["Congruence transformation", "*Similarity transformation", "No transformation", "Dilation only"], "Dilation + isometry = similarity."),
    ("If a figure is dilated by k=3 then k=2, the overall scale factor is:", ["5", "*6 (3 × 2)", "1", "3/2"], "Multiply scale factors."),
])
all_new[k] = q

k, q = add_qs("u7_l7.7", [
    ("A scale drawing represents a real object at a _____ size.", ["Same", "*Different (proportional)", "Random", "Unrelated"], "Proportional representation."),
    ("The scale factor of a map relates map distance to:", ["Time", "*Actual (real-world) distance", "Elevation", "Speed"], "Map to real distance."),
    ("If a map scale is 1 cm : 50 km and two cities are 3.5 cm apart on the map, the actual distance is:", ["100 km", "150 km", "*175 km", "200 km"], "3.5 × 50 = 175 km."),
    ("If a model car is built at 1:24 scale and the real car is 12 feet long, the model is:", ["2 feet", "1 foot", "*6 inches (0.5 feet)", "24 inches"], "12/24 = 0.5 feet = 6 inches."),
    ("Scale drawings preserve:", ["Actual sizes", "*Proportions (ratios of corresponding dimensions)", "Colors", "Areas exactly"], "Proportions preserved."),
    ("To enlarge a figure by scale factor 3, multiply all dimensions by:", ["1/3", "2", "*3", "9"], "Multiply by 3."),
    ("To reduce a figure by scale factor 1/4, multiply all dimensions by:", ["4", "2", "*1/4", "1/16"], "Multiply by 1/4."),
    ("If a blueprint scale is 1 in : 8 ft and a room is 15 ft long, the blueprint length is:", ["15 inches", "2 inches", "*1.875 inches (15/8)", "8 inches"], "15/8 = 1.875 in."),
    ("In a scale model, angles are:", ["Scaled too", "*Preserved (same as the original)", "Doubled", "Halved"], "Angles don't change with scale."),
    ("Scale factor = model dimension ÷:", ["Model dimension", "*Actual dimension", "Scale", "Ratio"], "model/actual."),
    ("If the area of a real room is 200 sq ft and the scale factor is 1:10, the model area is:", ["20 sq ft", "*2 sq ft (200/100)", "0.2 sq ft", "2000 sq ft"], "Area scales by k²: 200 × (1/10)² = 2."),
    ("Architects use scale drawings to represent:", ["Full-size buildings", "*Proportionally reduced floor plans and elevations", "Only heights", "Only widths"], "Practical application."),
    ("If two scale drawings of the same object have different scales, they are _____ to each other.", ["Congruent", "*Similar", "Unrelated", "Identical"], "Different scales = similar."),
])
all_new[k] = q

k, q = add_qs("u7_l7.8", [
    ("A fractal is a shape that exhibits:", ["Symmetry only", "*Self-similarity at different scales", "Only straight lines", "No pattern"], "Self-similar at all scales."),
    ("Self-similarity means parts of the figure look like:", ["Different shapes", "*Smaller copies of the whole figure", "Circles", "Random patterns"], "Part resembles whole."),
    ("The Sierpinski Triangle is created by repeatedly:", ["Enlarging a triangle", "*Removing the central triangle from each remaining triangle", "Rotating a triangle", "Reflecting a triangle"], "Iterative removal."),
    ("The Koch Snowflake is formed by adding _____ to each side at each iteration.", ["Squares", "*Equilateral triangles (on the middle third of each segment)", "Circles", "Pentagons"], "Triangles added to segments."),
    ("As fractal iterations increase, the perimeter of the Koch Snowflake:", ["Stays the same", "Decreases", "*Increases without bound (approaches infinity)", "Doubles exactly"], "Infinite perimeter."),
    ("The area of the Koch Snowflake:", ["Goes to infinity", "Is zero", "*Converges to a finite value", "Equals the perimeter"], "Finite area, infinite perimeter."),
    ("Fractal dimension can be a:", ["Whole number only", "*Non-integer (fractional) value", "Negative number", "Zero"], "Fractional dimension."),
    ("Fractals appear in nature in:", ["Nothing", "*Coastlines, trees, ferns, blood vessels, clouds", "Only crystals", "Only snowflakes"], "Many natural patterns."),
    ("Each iteration of a fractal applies the same:", ["Random change", "*Transformation rule(s) — producing scaled copies", "Rotation only", "No change"], "Iterative rules."),
    ("The Cantor Set is created by repeatedly removing the _____ third of segments.", ["First", "*Middle", "Last", "Entire"], "Remove middle thirds."),
    ("Mandelbrot Set is a famous fractal defined using:", ["Only geometry", "*Complex number iteration (z → z² + c)", "Only triangles", "Simple addition"], "Complex iteration."),
    ("The scale factor at each iteration in Sierpinski Triangle is:", ["1", "*1/2 (each smaller triangle has sides half the original)", "1/3", "2"], "Half-size copies."),
    ("Fractals demonstrate that simple rules can produce:", ["Simple shapes", "*Infinitely complex structures", "Only polygons", "Only circles"], "Complexity from simplicity."),
])
all_new[k] = q

# ── U8: Right Triangles & Trigonometry ──

k, q = add_qs("u8_l8.1", [
    ("The geometric mean of a and b is:", ["(a+b)/2", "a-b", "*sqrt(ab)", "a/b"], "sqrt(ab)."),
    ("The geometric mean of 4 and 9 is:", ["6.5", "13", "*6", "36"], "sqrt(36)=6."),
    ("In a right triangle, the altitude from the right angle to the hypotenuse creates:", ["One triangle", "*Two similar triangles (each similar to the original)", "Two congruent triangles", "No special relationship"], "Three similar triangles."),
    ("The altitude to the hypotenuse has length equal to the geometric mean of:", ["The two legs", "*The two segments of the hypotenuse (created by the altitude)", "The hypotenuse and a leg", "The two angles"], "Altitude = geometric mean of hypotenuse segments."),
    ("Each leg of the original right triangle is the geometric mean of:", ["The two segments", "*The hypotenuse and the adjacent hypotenuse segment", "The other leg and a segment", "The two altitudes"], "Leg = geometric mean of hyp and adjacent segment."),
    ("If the hypotenuse is divided into segments 4 and 9 by the altitude, the altitude length is:", ["13", "6.5", "*6 (sqrt(4×9))", "36"], "sqrt(36) = 6."),
    ("If hypotenuse = 13 and one segment = 4, the other segment =", ["4", "*9", "8", "17"], "13-4=9."),
    ("In the equation h² = p × q (altitude = geometric mean), p and q are the:", ["Legs", "*Two segments of the hypotenuse", "Hypotenuse and altitude", "Two angles"], "Hypotenuse segments."),
    ("The geometric mean is always _____ the arithmetic mean (for positive, unequal values).", ["Greater than", "Equal to", "*Less than or equal to", "Unrelated to"], "GM ≤ AM."),
    ("The geometric mean of 3 and 12 is:", ["7.5", "*6", "36", "15"], "sqrt(36)=6."),
    ("If a leg is 6 and the hypotenuse is 9, the projection of that leg on the hypotenuse is:", ["3", "*4 (6²/9 = 36/9 = 4)", "6", "9"], "leg² = hyp × projection."),
    ("The three similar triangles formed by the altitude to the hypotenuse allow us to set up:", ["Equations with unknowns", "*Proportions to find missing sides", "Only angle relationships", "No useful relationships"], "Proportions from similarity."),
    ("The geometric mean relates to right triangle altitude theorem, which is used in:", ["Trigonometry only", "*Finding missing lengths in right triangles", "Only obtuse triangles", "Circle theorems"], "Practical application."),
])
all_new[k] = q

k, q = add_qs("u8_l8.2", [
    ("The Pythagorean Theorem: a² + b² =", ["a + b", "2ab", "*(c², where c is the hypotenuse)", "ab"], "a² + b² = c²."),
    ("If a = 3 and b = 4, then c =", ["7", "12", "*5", "25"], "9+16=25, c=5."),
    ("The hypotenuse is always the _____ side of a right triangle.", ["Shortest", "*Longest", "Middle", "Adjacent"], "Longest side."),
    ("The converse: If a² + b² = c², the triangle is:", ["Obtuse", "Acute", "*Right", "Equilateral"], "Converse of Pythagorean Theorem."),
    ("If a² + b² > c², the triangle is:", ["Right", "Obtuse", "*Acute", "Not a triangle"], "Acute triangle test."),
    ("If a² + b² < c², the triangle is:", ["Right", "Acute", "*Obtuse", "Equilateral"], "Obtuse triangle test."),
    ("A Pythagorean triple is a set of three positive integers where:", ["a + b = c", "*a² + b² = c²", "a × b = c", "a - b = c"], "Integer right triangle sides."),
    ("Common Pythagorean triples include 3-4-5, 5-12-13, and:", ["6-7-8", "7-10-12", "*8-15-17", "9-10-11"], "8² + 15² = 64 + 225 = 289 = 17²."),
    ("Multiples of Pythagorean triples are also triples: 6-8-10 is a multiple of:", ["5-12-13", "*3-4-5", "7-24-25", "8-15-17"], "Multiplied by 2."),
    ("The Pythagorean Theorem applies ONLY to:", ["All triangles", "Obtuse triangles", "*Right triangles", "Isosceles triangles"], "Right triangles only."),
    ("The two shorter sides of a right triangle are called:", ["Hypotenuses", "*Legs", "Bases", "Altitudes"], "Legs."),
    ("If c = 13 and a = 5, then b =", ["8", "*12", "18", "144"], "b²=169-25=144, b=12."),
    ("The distance formula is derived from the:", ["Midpoint formula", "*Pythagorean Theorem", "Slope formula", "Area formula"], "Distance formula = Pythagorean Theorem on a coordinate plane."),
])
all_new[k] = q

k, q = add_qs("u8_l8.3", [
    ("In a 45-45-90 triangle, the legs are:", ["Different lengths", "*Congruent (equal in length)", "In ratio 1:2", "In ratio 1:sqrt(3)"], "Isosceles right triangle."),
    ("In a 45-45-90 triangle, if each leg is s, the hypotenuse is:", ["2s", "s", "*s√2", "s√3"], "Hypotenuse = s√2."),
    ("In a 30-60-90 triangle, the sides are in the ratio:", ["1:1:√2", "*1:√3:2", "1:2:3", "1:√2:√3"], "Short leg : long leg : hypotenuse."),
    ("In a 30-60-90 triangle, the side opposite 30° is:", ["The longest", "The hypotenuse", "*The shortest (half the hypotenuse)", "Equal to the hypotenuse"], "Shortest side opposite smallest angle."),
    ("In a 30-60-90 triangle with short leg = 5, the hypotenuse is:", ["5", "5√3", "*10", "5√2"], "Hypotenuse = 2 × short leg."),
    ("In a 30-60-90 triangle with short leg = 5, the long leg is:", ["10", "5", "*5√3", "5√2"], "Long leg = short leg × √3."),
    ("A 45-45-90 triangle with hypotenuse 10 has legs of length:", ["10", "5", "*5√2", "10√2"], "leg = 10/√2 = 5√2."),
    ("A 30-60-90 triangle with hypotenuse 12 has short leg:", ["12", "12√3", "*6", "6√3"], "Short leg = 12/2 = 6."),
    ("The diagonal of a square with side s creates two:", ["30-60-90 triangles", "*45-45-90 triangles", "Equilateral triangles", "Scalene triangles"], "Square diagonal = 45-45-90."),
    ("An equilateral triangle with an altitude creates two:", ["45-45-90 triangles", "*30-60-90 triangles", "Scalene triangles", "Right isosceles triangles"], "Altitude splits into 30-60-90."),
    ("The diagonal of a square with side 8 is:", ["8", "16", "*8√2", "8√3"], "d = s√2 = 8√2."),
    ("The altitude of an equilateral triangle with side 10 is:", ["10", "*5√3", "10√3", "5√2"], "Altitude = (s/2)√3 = 5√3."),
    ("These special triangles help find exact values without:", ["Rulers", "Protractors", "*A calculator (exact radical forms)", "Paper"], "Exact answers."),
])
all_new[k] = q

k, q = add_qs("u8_l8.4", [
    ("SOH-CAH-TOA stands for Sin=Opp/Hyp, Cos=Adj/Hyp, and:", ["Tan=Hyp/Adj", "*Tan=Opp/Adj", "Tan=Adj/Opp", "Tan=Opp/Hyp"], "TOA = Tan = Opposite/Adjacent."),
    ("sin(30°) =", ["√3/2", "√2/2", "*1/2", "1"], "Opposite/Hyp in 30-60-90."),
    ("cos(60°) =", ["√3/2", "√2/2", "*1/2", "1"], "Adjacent/Hyp in 30-60-90."),
    ("tan(45°) =", ["0", "√2", "1/2", "*1"], "Opposite = Adjacent in 45-45-90."),
    ("If sin(θ) = 3/5, and the triangle has hypotenuse 5, the opposite side is:", ["5", "4", "*3", "2"], "sin = opp/hyp: opp = 3."),
    ("If cos(θ) = 4/5, the adjacent side is _____ (hypotenuse = 5).", ["5", "3", "*4", "1"], "cos = adj/hyp: adj = 4."),
    ("sin²(θ) + cos²(θ) =", ["0", "2", "*1", "θ"], "Pythagorean identity."),
    ("tan(θ) = sin(θ) /", ["tan(θ)", "*cos(θ)", "sin(θ)", "1"], "tan = sin/cos."),
    ("As an angle increases from 0° to 90°, sin(θ):", ["Decreases", "*Increases (from 0 to 1)", "Stays the same", "Oscillates"], "Sin increases to 1."),
    ("cos(0°) =", ["0", "*1", "-1", "Undefined"], "cos(0°) = 1."),
    ("sin(90°) =", ["0", "*1", "-1", "Undefined"], "sin(90°) = 1."),
    ("To find an angle given a trig ratio, use the _____ function.", ["Regular trig", "*Inverse trig (e.g., sin⁻¹, cos⁻¹, tan⁻¹)", "Double", "Half"], "Inverse trig functions."),
    ("If tan(θ) = 1, then θ =", ["30°", "60°", "*45°", "90°"], "tan(45°) = 1."),
])
all_new[k] = q

k, q = add_qs("u8_l8.5", [
    ("An angle of elevation is measured from:", ["The top down", "*The horizontal up to the line of sight", "The ground to the groundlevel", "Vertical to horizontal"], "Horizontal up."),
    ("An angle of depression is measured from:", ["The ground up", "*The horizontal down to the line of sight", "The vertical down", "The line of sight up"], "Horizontal down."),
    ("Angle of elevation and angle of depression between two points are:", ["Supplementary", "*Congruent (alternate interior angles with the horizontal)", "Complementary", "Vertical"], "Equal angles."),
    ("A 6 ft person casts a 10 ft shadow. The angle of elevation to the sun is:", ["30°", "45°", "*arctan(6/10) ≈ 31°", "60°"], "tan(θ) = 6/10."),
    ("From a 50 m tower, the angle of depression to a car is 35°. The car is about _____ m away.", ["50", "35", "*71.4 (50/tan(35°))", "50tan(35°)"], "Adjacent = 50/tan(35°)."),
    ("When solving elevation/depression problems, always draw a:", ["Circle", "*Right triangle", "Parallelogram", "Number line"], "Right triangle model."),
    ("From the top of a cliff, the angle of depression to a boat is 20°. This means the angle of elevation from the boat to the cliff top is:", ["70°", "*20°", "160°", "90°"], "Alternate interior angles."),
    ("To find the height of a tree using trigonometry, you need:", ["Only the angle", "*The angle of elevation and the distance from the tree", "Only the distance", "The tree's age"], "Angle + distance."),
    ("If the angle of elevation to a kite is 60° and the string is 100 m, the kite's height is:", ["50 m", "*100sin(60°) ≈ 86.6 m", "100cos(60°)", "100tan(60°)"], "Height = hyp × sin(angle)."),
    ("Problems with two angles of depression from the same height involve:", ["One right triangle", "*Two right triangles sharing a vertical side", "No triangles", "Circles"], "Two triangles."),
    ("A ramp rises 3 ft over a horizontal distance of 12 ft. The angle of elevation is:", ["15°", "*arctan(3/12) ≈ 14°", "45°", "30°"], "tan(θ)=3/12."),
    ("Angles of elevation and depression are always measured from the:", ["Vertical", "*Horizontal", "Hypotenuse", "Ground only"], "From horizontal."),
    ("A pilot at 5000 ft sees a runway at a 3° angle of depression. The horizontal distance is about:", ["5000 ft", "*95,144 ft (5000/tan(3°))", "15000 ft", "5000 × tan(3°)"], "Large H/small angle = large distance."),
])
all_new[k] = q

k, q = add_qs("u8_l8.6", [
    ("The Law of Sines: a/sin(A) = b/sin(B) =", ["c/cos(C)", "c × sin(C)", "*c/sin(C)", "a × sin(A)"], "a/sinA = b/sinB = c/sinC."),
    ("The Law of Cosines: c² = a² + b² -", ["2ab", "ab", "*2ab·cos(C)", "2ab·sin(C)"], "c² = a² + b² − 2ab cos(C)."),
    ("Use the Law of Sines when you know:", ["Three sides", "*Two angles and a side (AAS or ASA) or two sides and an opposite angle (SSA)", "Three angles", "Only one side"], "AAS, ASA, or SSA."),
    ("Use the Law of Cosines when you know:", ["Two angles and a side", "*Three sides (SSS) or two sides and the included angle (SAS)", "Three angles", "Only one angle"], "SSS or SAS."),
    ("When angle C = 90°, the Law of Cosines simplifies to:", ["a² = b² + c²", "*c² = a² + b² (Pythagorean Theorem, since cos(90°) = 0)", "c = a + b", "c² = 2ab"], "cos(90°)=0 eliminates the last term."),
    ("The ambiguous case of the Law of Sines (SSA) can yield:", ["Exactly one triangle", "*Zero, one, or two triangles", "Always two triangles", "Always zero triangles"], "SSA is ambiguous."),
    ("To solve a triangle means to find all:", ["Sides only", "Angles only", "*Missing sides and angles", "Areas"], "All unknowns."),
    ("In triangle ABC, a = 8, angle A = 30°, angle B = 45°. Find b using Law of Sines: b =", ["8", "*8sin(45°)/sin(30°) ≈ 11.3", "8tan(45°)", "8cos(45°)/cos(30°)"], "b/sin(B) = a/sin(A)."),
    ("If a = 5, b = 7, C = 60°, then c² = 25 + 49 - 2(5)(7)cos(60°) =", ["74", "*39 (74 - 35 = 39)", "109", "4"], "70 × 0.5 = 35; 74 - 35 = 39."),
    ("The area of a triangle can be found using: Area = ½ab·sin(C). This is useful when:", ["All angles are known", "*Two sides and the included angle are known", "Only one side is known", "The triangle is right"], "SAS area formula."),
    ("If a=10, b=14, angle C=30°, the area is:", ["70", "*35 (½ × 10 × 14 × sin(30°) = ½ × 10 × 14 × 0.5)", "140", "7"], "½(10)(14)(0.5) = 35."),
    ("Heron's formula finds area using:", ["Angles", "*The three side lengths (and semi-perimeter)", "Two sides and an angle", "One side only"], "Area from three sides."),
    ("The Law of Cosines generalizes the Pythagorean Theorem for:", ["Right triangles only", "*All triangles (any angle, not just 90°)", "Obtuse triangles only", "Acute triangles only"], "Works for any triangle."),
])
all_new[k] = q

k, q = add_qs("u8_l8.7", [
    ("A vector has both:", ["Only magnitude", "Only direction", "*Magnitude and direction", "Neither"], "Two properties."),
    ("The magnitude of a vector is its:", ["Direction", "*Length (size)", "Angle", "Endpoint"], "Magnitude = length."),
    ("A vector from (0,0) to (3,4) has magnitude:", ["7", "12", "*5", "1"], "sqrt(9+16)=5."),
    ("The direction of a vector is the _____ it makes with the positive x-axis.", ["Length", "*Angle", "Magnitude", "Component"], "Direction angle."),
    ("Vector addition: (a,b) + (c,d) =", ["(ac, bd)", "(a-c, b-d)", "*(a+c, b+d)", "(ad, bc)"], "Add components."),
    ("The resultant of two vectors is their:", ["Difference", "*Sum (the combined effect)", "Product", "Quotient"], "Resultant = vector sum."),
    ("Scalar multiplication: k(a,b) =", ["(k+a, k+b)", "(a/k, b/k)", "*(ka, kb)", "(k,k)"], "Multiply each component."),
    ("Opposite vectors have the same magnitude but:", ["Same direction", "*Opposite directions", "No direction", "Perpendicular directions"], "Opposite direction."),
    ("The zero vector has magnitude:", ["1", "Undefined", "*0", "Infinity"], "Zero vector = no magnitude."),
    ("Two vectors are equal if they have the same:", ["Starting point", "*Magnitude and direction", "Ending point", "x-component only"], "Equal = same magnitude & direction."),
    ("Vectors can represent:", ["Only position", "*Force, velocity, displacement, and other quantities with magnitude and direction", "Only speed", "Only distance"], "Physical applications."),
    ("The component form of a vector from A(1,2) to B(4,6) is:", ["(1,2)", "*(3,4)", "(4,6)", "(5,8)"], "(4-1, 6-2) = (3,4)."),
    ("A unit vector has magnitude:", ["0", "*1", "Any value", "π"], "Unit = magnitude 1."),
])
all_new[k] = q

k, q = add_qs("u8_l8.8", [
    ("Polar coordinates describe a point using:", ["(x, y)", "*(r, θ) — distance from origin and angle from positive x-axis", "(a, b, c)", "(slope, intercept)"], "r and θ."),
    ("In polar coordinates, r is the:", ["Angle", "*Distance from the pole (origin)", "x-coordinate", "y-coordinate"], "Radial distance."),
    ("In polar coordinates, θ is the:", ["Distance", "*Angle from the positive x-axis (polar axis)", "Radius", "Diameter"], "Angular direction."),
    ("To convert polar (r,θ) to rectangular: x =", ["r sin(θ)", "*r cos(θ)", "r tan(θ)", "r/cos(θ)"], "x = r cos(θ)."),
    ("To convert polar (r,θ) to rectangular: y =", ["r cos(θ)", "*r sin(θ)", "r tan(θ)", "r/sin(θ)"], "y = r sin(θ)."),
    ("To convert rectangular (x,y) to polar: r =", ["x + y", "x - y", "*sqrt(x² + y²)", "x²+y²"], "Distance formula."),
    ("To find θ from rectangular (x,y): θ =", ["x/y", "y/x", "*arctan(y/x) (with quadrant adjustment)", "arcsin(x/r)"], "θ = arctan(y/x)."),
    ("The polar point (5, 60°) in rectangular form is:", ["(5, 60)", "*(2.5, 2.5√3)", "(5cos60, 5sin60)", "(5√3/2, 5/2)"], "x=5cos60=2.5, y=5sin60=2.5√3."),
    ("The rectangular point (3,3) in polar form has r =", ["3", "6", "*3√2", "9"], "sqrt(9+9) = 3√2."),
    ("Polar coordinates are especially useful for:", ["Linear equations", "*Curves with rotational symmetry (circles, spirals)", "Only squares", "Only triangles"], "Rotational symmetry."),
    ("The equation r = 5 in polar coordinates represents a:", ["Line", "*Circle of radius 5 centered at the origin", "Spiral", "Point"], "Constant r = circle."),
    ("The equation θ = π/4 represents a:", ["Circle", "*Ray from the origin at 45°", "Spiral", "Point"], "Constant θ = ray."),
    ("Multiple polar coordinates can represent the same point because:", ["r can be negative", "θ + 360° gives the same point", "*Both: adding 360° to θ or using negative r with θ + 180°", "They can't"], "Non-uniqueness of polar coords."),
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

print(f"✅ Geometry U5-U8: expanded {len(all_new)} lessons")
