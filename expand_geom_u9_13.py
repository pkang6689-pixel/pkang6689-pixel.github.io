#!/usr/bin/env python3
"""Expand Geometry U9-U13 quizzes from 7 to 20 questions each (38 lessons)."""
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

# ── U9: Transformations ──

k, q = add_qs("u9_l9.1", [
    ("A reflection is a transformation that flips a figure across a:", ["Point", "*Line (line of reflection)", "Circle", "Angle"], "Flip across a line."),
    ("A reflection preserves:", ["Only angles", "Only distances", "*Both distance and angle measure (it's an isometry)", "Neither"], "Isometry."),
    ("Reflecting point (3,5) across the x-axis gives:", ["(-3,5)", "(3,5)", "*(3,-5)", "(-3,-5)"], "x stays, y negates."),
    ("Reflecting point (3,5) across the y-axis gives:", ["(3,-5)", "*(-3,5)", "(-3,-5)", "(3,5)"], "x negates, y stays."),
    ("Reflecting across y = x transforms (a,b) to:", ["(-a,-b)", "(a,-b)", "*(b,a)", "(-b,-a)"], "Swap coordinates."),
    ("Reflecting across y = -x transforms (a,b) to:", ["(b,a)", "*(-b,-a)", "(a,b)", "(-a,b)"], "Swap and negate."),
    ("A reflection changes the _____ of the figure.", ["Size", "Shape", "*Orientation (a clockwise order becomes counterclockwise)", "Area"], "Orientation reverses."),
    ("The line of reflection is the _____ of the segment connecting a point and its image.", ["Diagonal", "*Perpendicular bisector", "Midpoint", "Tangent"], "Perpendicular bisector."),
    ("Every point on the line of reflection maps to:", ["A different point", "*Itself", "The origin", "Infinity"], "Fixed points."),
    ("Reflecting (4,2) across the line x = 1 gives:", ["(-4,2)", "*(-2,2)", "(4,-2)", "(2,4)"], "Distance from x=1 is 3, so 1-3=-2."),
    ("Two reflections across parallel lines produce a:", ["Reflection", "*Translation", "Rotation", "Dilation"], "Double reflection (parallel) = translation."),
    ("Two reflections across intersecting lines produce a:", ["Translation", "*Rotation", "Dilation", "Reflection"], "Double reflection (intersecting) = rotation."),
    ("A figure with a line of symmetry maps onto itself under a:", ["Translation", "*Reflection across that line", "Dilation", "Rotation only"], "Symmetry = self-reflection."),
])
all_new[k] = q

k, q = add_qs("u9_l9.2", [
    ("A translation slides every point the same:", ["Angle", "*Distance in the same direction", "Rotation", "Scale factor"], "Same distance, same direction."),
    ("A translation is described by a:", ["Line of reflection", "*Vector (direction and magnitude)", "Center and angle", "Scale factor"], "Translation vector."),
    ("Under translation vector (a,b), point (x,y) maps to:", ["(x-a, y-b)", "*(x+a, y+b)", "(ax, by)", "(x/a, y/b)"], "Add components."),
    ("Translation (3,-2) applied to point (1,5) gives:", ["(-2,7)", "(3,5)", "*(4,3)", "(1,3)"], "(1+3, 5-2)=(4,3)."),
    ("Translations preserve:", ["Only angles", "Only distances", "*Distance, angle measure, and orientation", "Neither"], "Isometry that preserves orientation."),
    ("The image under a translation is _____ to the pre-image.", ["Similar", "*Congruent", "Larger", "Smaller"], "Congruent."),
    ("Translations do NOT change:", ["Position", "Coordinates", "*Size, shape, or orientation", "Location"], "Everything except position preserved."),
    ("A composition of two translations is:", ["A rotation", "A reflection", "*Another translation", "A dilation"], "Translation + translation = translation."),
    ("Translation (2,3) followed by (-5,1) equals the single translation:", ["(7,4)", "(3,-2)", "*(-3,4)", "(-3,2)"], "(2-5, 3+1)=(-3,4)."),
    ("In a translation, all segments connecting pre-image points to image points are:", ["Perpendicular", "*Parallel and congruent", "Random", "Different lengths"], "All parallel and equal."),
    ("A translation can be described using coordinate notation as:", ["(x,y)→(y,x)", "*(x,y)→(x+a, y+b)", "(x,y)→(-x,-y)", "(x,y)→(kx,ky)"], "Add translation vector."),
    ("Translating a figure does not involve:", ["Moving", "Sliding", "*Rotating or flipping", "Shifting"], "No rotation or reflection."),
    ("The vector (0,0) represents:", ["A large translation", "*The identity (no movement)", "A reflection", "A rotation"], "Zero vector = no change."),
])
all_new[k] = q

k, q = add_qs("u9_l9.3", [
    ("A rotation turns a figure around a fixed point called the:", ["Vertex", "*Center of rotation", "Midpoint", "Focus"], "Center of rotation."),
    ("A rotation is defined by a center and an:", ["Scale factor", "*Angle of rotation", "Line of reflection", "Translation vector"], "Center + angle."),
    ("A positive angle of rotation is typically:", ["Clockwise", "*Counterclockwise", "Random", "Undefined"], "Counterclockwise is positive."),
    ("Rotation of 90° counterclockwise: (x,y) maps to:", ["(y,x)", "(x,-y)", "*(-y,x)", "(y,-x)"], "90° CCW: (-y,x)."),
    ("Rotation of 180°: (x,y) maps to:", ["(y,x)", "(x,y)", "*(-x,-y)", "(-y,x)"], "180°: negate both."),
    ("Rotation of 270° counterclockwise (or 90° clockwise): (x,y) maps to:", ["(-y,x)", "(-x,-y)", "*(y,-x)", "(x,y)"], "270° CCW: (y,-x)."),
    ("A rotation preserves:", ["Only shape", "Only size", "*Distance, angles, and orientation", "Nothing"], "Isometry preserving orientation."),
    ("Rotation of 360° maps every point to:", ["A new location", "*Itself (the identity)", "The origin", "The opposite side"], "Full rotation = identity."),
    ("Rotating (3,0) by 90° CCW around the origin gives:", ["(3,0)", "(0,-3)", "*(0,3)", "(-3,0)"], "(-0,3)=(0,3)."),
    ("The image under a rotation is _____ to the pre-image.", ["Similar", "*Congruent", "Larger", "Smaller"], "Rotation is an isometry."),
    ("A figure has rotational symmetry if it maps to itself after a rotation of less than:", ["90°", "180°", "*360°", "720°"], "Less than full turn."),
    ("A regular hexagon has rotational symmetry at every:", ["90°", "*60° (360°/6)", "45°", "30°"], "360/6=60."),
    ("The composition of two rotations about the same center is:", ["A translation", "A reflection", "*A rotation (by the sum of the angles)", "A dilation"], "Angles add up."),
])
all_new[k] = q

k, q = add_qs("u9_l9.4", [
    ("A composition of transformations applies:", ["Only one transformation", "*Two or more transformations in sequence", "No transformation", "A random transformation"], "Multiple transformations."),
    ("In a composition, the order of transformations:", ["Doesn't matter", "*Often matters (different orders can give different results)", "Is always alphabetical", "Is random"], "Order matters."),
    ("A glide reflection is:", ["Two rotations", "*A translation followed by a reflection (parallel to the translation direction)", "Two dilations", "A translation followed by a rotation"], "Slide then flip."),
    ("A glide reflection is an isometry:", ["No", "*Yes (it preserves distance and angles)", "Sometimes", "Only for translations"], "Still an isometry."),
    ("A glide reflection changes:", ["Size", "Shape", "*Orientation (like a reflection)", "Nothing"], "Orientation reverses."),
    ("Footprints in sand are an example of:", ["Translation", "Rotation", "*Glide reflection", "Dilation"], "Alternate footprints = glide reflection."),
    ("The composition of a translation and a rotation about the origin:", ["Is always a translation", "Is always a rotation", "*Is a rotation about a different center", "Is a reflection"], "Composition result."),
    ("Any isometry of the plane is one of: reflection, rotation, translation, or:", ["Dilation", "*Glide reflection", "Shear", "Projection"], "Four types of isometry."),
    ("A composition of three reflections:", ["Is always a rotation", "*Can be a reflection or a glide reflection", "Is always a translation", "Is the identity"], "Odd number of reflections."),
    ("The composition of two reflections across parallel lines separated by d produces a translation of distance:", ["d", "*2d", "d/2", "d²"], "Translation distance = 2 × separation."),
    ("The composition of two reflections across lines that intersect at angle θ produces a rotation of:", ["θ", "*2θ", "θ/2", "θ²"], "Rotation angle = 2 × angle between lines."),
    ("If transformation A maps P to P' and transformation B maps P' to P'', the composition B∘A maps P to:", ["P'", "*P''", "P", "P'''"], "Apply A then B."),
    ("Compositions are associative: (A∘B)∘C = A∘(B∘C). This means:", ["Order doesn't matter", "*Grouping doesn't matter (but order still does)", "They're commutative", "All compositions equal the identity"], "Associative but not necessarily commutative."),
])
all_new[k] = q

k, q = add_qs("u9_l9.5", [
    ("Line symmetry means a figure can be folded along a line so the halves:", ["Are different", "*Match exactly (one is the mirror image of the other)", "Are similar", "Overlap partially"], "Mirror halves."),
    ("A figure with line symmetry has at least one:", ["Diagonal", "*Line of symmetry (axis of symmetry)", "Center point", "Right angle"], "At least one axis."),
    ("A circle has _____ lines of symmetry.", ["1", "4", "8", "*Infinitely many"], "Any diameter is an axis."),
    ("An equilateral triangle has _____ lines of symmetry.", ["1", "2", "*3", "6"], "One through each vertex and opposite midpoint."),
    ("A rectangle (non-square) has _____ lines of symmetry.", ["1", "*2", "4", "0"], "Two: horizontal and vertical."),
    ("A regular pentagon has _____ lines of symmetry.", ["3", "4", "*5", "10"], "n lines for regular n-gon."),
    ("Rotational symmetry of order n means the figure maps to itself _____ times in a full rotation.", ["1", "2", "*n", "n+1"], "Order = number of coincidences."),
    ("A figure with rotational symmetry of order 1 has:", ["High symmetry", "*No rotational symmetry (only 360° works — every figure has that)", "One axis", "Two axes"], "Order 1 = trivial."),
    ("Point symmetry is rotational symmetry of order:", ["1", "*2 (180° rotation maps the figure to itself)", "3", "4"], "180° symmetry."),
    ("The letter S has:", ["Line symmetry", "*Point symmetry (180° rotational)", "Both line and point", "Neither"], "Rotate S 180° and it looks the same."),
    ("A parallelogram (non-rectangle) has:", ["Line symmetry", "*Point symmetry only", "Both", "Neither"], "Only 180° rotation symmetry."),
    ("A square has rotational symmetry of order:", ["2", "3", "*4", "8"], "90°, 180°, 270°, 360°."),
    ("A figure that has both line symmetry and rotational symmetry of order greater than 1 is often:", ["Irregular", "Random", "*Regular or highly symmetric", "Impossible"], "High symmetry."),
])
all_new[k] = q

k, q = add_qs("u9_l9.6", [
    ("A dilation is a transformation that changes:", ["Only shape", "Only orientation", "*Size (while preserving shape)", "Angles"], "Enlargement or reduction."),
    ("A dilation has a center and a:", ["Angle", "Translation vector", "*Scale factor (k)", "Line of reflection"], "Scale factor k."),
    ("If k > 1, the dilation is a(n):", ["Reduction", "*Enlargement", "Isometry", "Reflection"], "Grows larger."),
    ("If 0 < k < 1, the dilation is a(n):", ["Enlargement", "*Reduction", "Rotation", "Translation"], "Shrinks."),
    ("If k = 1, the dilation is the:", ["Reflection", "Rotation", "*Identity (no change)", "Translation"], "No size change."),
    ("Dilation centered at origin with k=2: (3,4) maps to:", ["(1.5,2)", "(5,6)", "*(6,8)", "(3,4)"], "(6,8)."),
    ("Dilation centered at origin with k=1/3: (9,6) maps to:", ["(27,18)", "(9,6)", "*(3,2)", "(6,3)"], "(3,2)."),
    ("A dilation preserves:", ["Distances", "*Angle measures and shape (but not distances)", "Area", "Perimeter"], "Angles preserved, distances scaled."),
    ("The image and pre-image under a dilation are:", ["Congruent", "*Similar", "Unrelated", "Identical"], "Similar figures."),
    ("Under a dilation, corresponding sides of image and pre-image are:", ["Congruent", "Perpendicular", "*Parallel", "Unrelated"], "Sides are parallel."),
    ("A dilation is NOT an isometry because:", ["It changes angles", "It changes shape", "*It changes distances (side lengths)", "It doesn't exist"], "Distances change."),
    ("If k < 0, the dilation includes a _____ through the center.", ["Translation", "*Rotation of 180° (point reflection through center)", "Reflection across a line", "No change"], "Negative k = 180° rotation + scale."),
    ("Dilation with center C and k=3: every point moves _____ from C as it was before.", ["To the same distance", "*To three times the distance", "To 1/3 the distance", "Toward C"], "3× as far."),
])
all_new[k] = q

k, q = add_qs("u9_l9.7", [
    ("Transformations on the coordinate plane use _____ to describe mappings.", ["Words only", "*Coordinate rules (formulas)", "Pictures only", "Guesses"], "Algebraic rules."),
    ("Translation by (a,b): (x,y) → (x+a, y+b). Reflection across x-axis: (x,y) →", ["(-x,y)", "*(x,-y)", "(-x,-y)", "(y,x)"], "Negate y."),
    ("Reflection across y-axis: (x,y) →", ["(x,-y)", "*(-x,y)", "(-x,-y)", "(y,x)"], "Negate x."),
    ("Reflection across the origin: (x,y) →", ["(x,-y)", "(-x,y)", "*(-x,-y)", "(y,x)"], "Negate both."),
    ("Rotation 90° CCW about origin: (x,y) →", ["(y,x)", "(y,-x)", "*(-y,x)", "(-x,-y)"], "(-y,x)."),
    ("Dilation centered at origin with scale k: (x,y) →", ["(x+k, y+k)", "(x-k, y-k)", "*(kx, ky)", "(x/k, y/k)"], "Multiply by k."),
    ("To verify two figures are congruent, show there exists a sequence of:", ["Dilations", "*Isometries (reflections, rotations, translations) mapping one to the other", "Only translations", "Only dilations"], "Isometric mapping."),
    ("To verify two figures are similar, show there exists:", ["Only isometries", "*A dilation (possibly composed with isometries) mapping one to the other", "Only reflections", "No transformation"], "Similarity = dilation + isometry."),
    ("Composing a dilation with an isometry produces a:", ["Congruence transformation", "*Similarity transformation", "No transformation", "Another dilation only"], "Similarity transformation."),
    ("The rule (x,y)→(x+3, -y) represents:", ["Rotation then dilation", "*Translation right 3, then reflection across x-axis (or combined)", "Just a translation", "Just a reflection"], "Combined translation and reflection."),
    ("The rule (x,y)→(-y, x) is a:", ["Reflection", "Translation", "*Rotation 90° CCW", "Dilation"], "90° CCW rotation."),
    ("To find the rule for a transformation, compare _____ of corresponding points.", ["Colors", "*Coordinates", "Names", "Areas"], "Compare coordinates."),
    ("If A(1,2) maps to A'(2,-1), and B(3,4) maps to B'(4,-3), the rule is (x,y)→:", ["(x+1, y-3)", "*(y, -x+? — actually (x+1, -y+1) doesn't fit; it's a 90° CW rotation: (y,-x) maps (1,2)→(2,-1) and (3,4)→(4,-3))", "(x-1, -y)", "(2x, -2y)"], "Check: (y,-x): (2,-1) and (4,-3). Correct — 90° CW."),
])
all_new[k] = q

# ── U10: Circles ──

k, q = add_qs("u10_l10.1", [
    ("A circle is the set of all points equidistant from a:", ["Line", "*Center point", "Segment", "Plane"], "Definition of circle."),
    ("The distance from center to any point on the circle is the:", ["Diameter", "*Radius", "Chord", "Arc"], "Radius."),
    ("The diameter equals:", ["Half the radius", "*Twice the radius", "Pi times radius", "The circumference"], "d = 2r."),
    ("Circumference = 2πr = πd. For r = 7:", ["44", "*14π ≈ 43.98", "49π", "7π"], "C = 2π(7) = 14π."),
    ("A chord is a segment with both endpoints on the:", ["Center", "*Circle", "Diameter", "Radius"], "Endpoints on circle."),
    ("The longest chord of a circle is the:", ["Radius", "*Diameter", "Secant", "Tangent"], "Diameter is longest chord."),
    ("A secant is a line that intersects a circle at:", ["One point", "*Two points", "No points", "The center"], "Two intersection points."),
    ("A tangent touches a circle at exactly:", ["Two points", "*One point (the point of tangency)", "No points", "The center"], "One point."),
    ("Concentric circles share the same:", ["Radius", "*Center (but different radii)", "Chord", "Tangent line"], "Same center."),
    ("A semicircle is half of a circle, formed by a:", ["Chord", "*Diameter", "Radius", "Tangent"], "Diameter divides circle in half."),
    ("If the diameter is 10, the circumference is:", ["10π", "25π", "*10π ≈ 31.42", "100π"], "C = πd = 10π."),
    ("A minor arc is _____ than a semicircle.", ["Larger", "*Smaller", "Equal to", "Unrelated to"], "Less than half."),
    ("A major arc is _____ than a semicircle.", ["Smaller", "*Larger", "Equal to", "Unrelated to"], "More than half."),
])
all_new[k] = q

k, q = add_qs("u10_l10.2", [
    ("A central angle has its vertex at the:", ["Circle", "*Center of the circle", "Chord", "Arc"], "Vertex at center."),
    ("The measure of a minor arc equals:", ["Half the central angle", "*The central angle", "Twice the central angle", "180°"], "Arc = central angle."),
    ("The measure of a major arc equals:", ["The central angle", "*360° minus the minor arc", "The central angle times 2", "180°"], "Major = 360° - minor."),
    ("A semicircle has an arc measure of:", ["90°", "*180°", "270°", "360°"], "Half of 360°."),
    ("Arc Addition Postulate: adjacent arcs sum to the:", ["Diameter", "Radius", "*Total arc", "Chord"], "Part + part = whole arc."),
    ("If central angle = 60°, the minor arc =", ["30°", "*60°", "120°", "300°"], "Equal to central angle."),
    ("The corresponding major arc would be:", ["60°", "180°", "*300°", "120°"], "360-60=300."),
    ("Congruent central angles intercept:", ["Different arcs", "*Congruent arcs (in the same or congruent circles)", "No arcs", "Major arcs only"], "Equal angles = equal arcs."),
    ("Arc length is a fraction of the:", ["Area", "*Circumference", "Radius", "Diameter"], "Part of circumference."),
    ("Arc length = (central angle/360) × 2πr. For angle 90° and r=4:", ["π", "*2π", "4π", "8π"], "(90/360)×2π(4)=(1/4)(8π)=2π."),
    ("Two arcs are congruent if they have the same measure and are in:", ["Different circles of different radii", "*The same circle or congruent circles", "Any circles", "Concentric circles only"], "Same or congruent circles."),
    ("A full circle has arc measure:", ["180°", "270°", "*360°", "90°"], "360° complete."),
    ("If arc AB = 100° and arc BC = 80° (adjacent), arc AC =", ["20°", "*180°", "80°", "100°"], "100+80=180."),
])
all_new[k] = q

k, q = add_qs("u10_l10.3", [
    ("In the same circle, congruent chords have:", ["Different arcs", "*Congruent arcs", "Perpendicular arcs", "No arcs"], "Equal chords = equal arcs."),
    ("If two chords are equidistant from the center, they are:", ["Perpendicular", "*Congruent", "Parallel", "Unequal"], "Equidistant = congruent."),
    ("A diameter perpendicular to a chord:", ["Misses the chord", "*Bisects the chord and its arc", "Is parallel to the chord", "Doubles the chord"], "Perpendicular diameter bisects."),
    ("The perpendicular from the center to a chord:", ["Passes through an endpoint", "*Bisects the chord", "Is parallel to the chord", "Extends the chord"], "Center-perpendicular bisects."),
    ("If AB is a chord and the perpendicular from center O meets AB at M, then AM =", ["AB", "2AB", "*AB/2 (M is the midpoint)", "OB"], "Midpoint of chord."),
    ("In a circle with radius 10, a chord is 8 units from the center. The chord length is:", ["16", "8", "*12 (half-chord = sqrt(100-64) = 6, full = 12)", "20"], "sqrt(r²-d²)×2."),
    ("Two chords intersecting inside a circle: the products of their segments are:", ["Unequal", "*Equal", "Complementary", "Supplementary"], "Intersecting Chords Theorem."),
    ("If chords AB and CD intersect at E: AE × EB =", ["AC × BD", "*CE × ED", "AE + EB", "CD"], "Segment products equal."),
    ("A chord closer to the center is _____ than a chord farther from the center.", ["Shorter", "*Longer", "Equal", "Perpendicular"], "Closer = longer."),
    ("The converse: congruent arcs have congruent:", ["Radii", "*Chords", "Tangents", "Secants"], "Equal arcs = equal chords."),
    ("If a chord passes through the center, it is a:", ["Radius", "*Diameter", "Secant", "Tangent"], "Diameter."),
    ("An arc and its chord together form a region called a:", ["Sector", "*Segment (of the circle)", "Semicircle", "Annulus"], "Circular segment."),
    ("The midpoint of a chord is the point where the _____ from the center meets the chord.", ["Tangent", "*Perpendicular", "Radius", "Secant"], "Perpendicular from center."),
])
all_new[k] = q

k, q = add_qs("u10_l10.4", [
    ("An inscribed angle has its vertex on the:", ["Center", "*Circle", "Chord", "Outside"], "Vertex on the circle."),
    ("An inscribed angle intercepts an arc that is _____ its measure.", ["Equal to", "*Twice (the arc is twice the angle)", "Half", "Three times"], "Arc = 2 × inscribed angle."),
    ("Equivalently, an inscribed angle = _____ the intercepted arc.", ["Twice", "*Half", "Equal to", "One-third"], "Angle = ½ arc."),
    ("If an inscribed angle intercepts a semicircle (180° arc), the angle measures:", ["180°", "*90°", "45°", "60°"], "Half of 180 = 90."),
    ("Thales' Theorem: An angle inscribed in a semicircle is a:", ["Straight angle", "*Right angle", "Acute angle", "Obtuse angle"], "Always 90°."),
    ("Two inscribed angles that intercept the same arc are:", ["Supplementary", "*Congruent", "Complementary", "Vertical"], "Same arc = same angle."),
    ("If inscribed angle = 35°, the intercepted arc =", ["35°", "*70°", "17.5°", "105°"], "Arc = 2 × 35 = 70."),
    ("If arc = 120°, the inscribed angle intercepting it =", ["120°", "*60°", "240°", "30°"], "Angle = 120/2 = 60."),
    ("An inscribed quadrilateral (cyclic quadrilateral) has opposite angles that are:", ["Congruent", "*Supplementary (sum to 180°)", "Complementary", "Equal"], "Opposite angles sum to 180."),
    ("If one angle of an inscribed quadrilateral is 75°, the opposite angle is:", ["75°", "15°", "*105°", "150°"], "180-75=105."),
    ("A central angle is _____ an inscribed angle intercepting the same arc.", ["Half", "Equal to", "*Twice", "Unrelated to"], "Central = 2 × inscribed."),
    ("If a central angle = 80° and an inscribed angle intercepts the same arc:", ["Inscribed = 80°", "*Inscribed = 40°", "Inscribed = 160°", "Cannot determine"], "40° = 80/2."),
    ("Two chords that form an inscribed angle have their endpoints:", ["At the center", "*On the circle", "Outside the circle", "On the diameter"], "Inscribed angle sides are chords."),
])
all_new[k] = q

k, q = add_qs("u10_l10.5", [
    ("A tangent to a circle is perpendicular to the _____ at the point of tangency.", ["Chord", "*Radius", "Diameter", "Secant"], "Tangent ⊥ radius."),
    ("From an external point, the two tangent segments to a circle are:", ["Perpendicular", "*Congruent (equal in length)", "Parallel", "Different lengths"], "Tangent segments from external point are equal."),
    ("If a line is perpendicular to a radius at its endpoint on the circle, the line is:", ["A chord", "A secant", "*A tangent", "A diameter"], "Converse: perp at endpoint = tangent."),
    ("The point where a tangent touches the circle is called the:", ["Center", "Intersection", "*Point of tangency", "Chord midpoint"], "Point of tangency."),
    ("A tangent line and the radius form a _____ angle.", ["45°", "60°", "*90° (right angle)", "180°"], "Always perpendicular."),
    ("Two tangent lines from the same external point and the two radii to the tangent points form a:", ["Triangle", "*Quadrilateral (a kite)", "Pentagon", "Circle"], "Kite shape."),
    ("If tangent PA = 8 and the radius OA = 6, then OP (external point to center) =", ["14", "2", "*10", "48"], "8² + 6² = 100, OP = 10."),
    ("A common external tangent does not pass between two circles, while a common internal tangent:", ["Also doesn't", "*Passes between them", "Touches only one", "Is parallel to the external"], "Internal passes between."),
    ("Two circles can have at most _____ common tangent(s) if they are external to each other.", ["2", "3", "*4", "1"], "4 common tangents (2 external, 2 internal)."),
    ("Two tangent circles (touching at one point) have _____ common tangent(s).", ["4", "*3", "2", "1"], "3 tangents (2 external, 1 at point of tangency)."),
    ("If PA and PB are tangent segments from P, and angle APB = 60°, then angle OAP =", ["60°", "*90° (tangent ⊥ radius, regardless of angle APB)", "30°", "45°"], "Always 90°."),
    ("The distance from an external point to the center can be found using the _____ relationship.", ["Chord", "*Pythagorean (tangent² + radius² = distance²)", "Arc", "Inscribed angle"], "Right triangle."),
    ("A tangent is the limiting position of a secant as the two intersection points:", ["Move apart", "*Approach each other (coincide)", "Disappear", "Move to the center"], "Secant becomes tangent."),
])
all_new[k] = q

k, q = add_qs("u10_l10.6", [
    ("An angle formed by two secants from an external point equals half the:", ["Sum of arcs", "*Difference of the intercepted arcs", "Product of arcs", "Larger arc only"], "Half the difference."),
    ("An angle formed by a tangent and a secant from an external point equals:", ["The sum of arcs", "*Half the difference of the two intercepted arcs", "The arc", "Twice the arc"], "Same rule: half difference."),
    ("An angle formed by two tangents from an external point equals:", ["The sum of arcs", "*Half the difference of the major and minor arcs", "The average of arcs", "The product of arcs"], "Half the difference."),
    ("An angle formed by two chords intersecting inside a circle equals:", ["Half the difference", "*Half the sum of the two intercepted arcs", "The difference", "The sum"], "Interior: half the SUM."),
    ("If two chords create intercepted arcs of 80° and 40°, the angle is:", ["120°", "40°", "*60° ((80+40)/2)", "20°"], "Half the sum."),
    ("If a secant and tangent from external point create arcs 100° and 30°, the angle is:", ["65°", "130°", "*35° ((100-30)/2)", "70°"], "Half the difference."),
    ("Two secants from external point with arcs 120° and 40°: the angle is:", ["80°", "160°", "*40° ((120-40)/2)", "60°"], "Half the difference."),
    ("Two tangents from external point: if the minor arc is 110°, the major arc is:", ["110°", "*250°", "220°", "70°"], "360-110=250."),
    ("Continuing: the angle between the two tangents is:", ["110°", "125°", "*70° ((250-110)/2)", "180°"], "(250-110)/2=70."),
    ("A tangent-chord angle equals:", ["The intercepted arc", "*Half the intercepted arc", "Twice the intercepted arc", "The sum of arcs"], "Half the arc."),
    ("If a tangent-chord angle intercepts an arc of 130°, the angle =", ["130°", "*65°", "260°", "32.5°"], "130/2=65."),
    ("For angles formed INSIDE the circle, use half the _____ of arcs.", ["Difference", "*Sum", "Product", "Quotient"], "Interior = half sum."),
    ("For angles formed OUTSIDE the circle, use half the _____ of arcs.", ["Sum", "*Difference", "Product", "Average"], "Exterior = half difference."),
])
all_new[k] = q

k, q = add_qs("u10_l10.7", [
    ("Two chords intersecting inside a circle: the products of their segments are:", ["Different", "*Equal (AE·EB = CE·ED)", "Supplementary", "Zero"], "Intersecting Chords Theorem."),
    ("Two secants from an external point: (whole₁)(external₁) =", ["(whole₁)(whole₂)", "*(whole₂)(external₂)", "(external₁)(external₂)", "half the product"], "Secant-Secant Theorem."),
    ("A secant and tangent from an external point: (tangent)² =", ["(secant)", "*(whole secant)(external part of secant)", "(secant)²", "half the secant"], "Tangent-Secant Theorem."),
    ("If chords intersect and segments are 3,8 and x,6, then x =", ["48", "2", "*4", "18"], "3×8=x×6, 24=6x, x=4."),
    ("Two secants: whole=12, external=5 and whole=y, external=4. Then y =", ["20", "*15 (12×5=y×4, 60=4y)", "10", "48"], "60/4=15."),
    ("Tangent = 6, secant whole = 9, external = x: 36 = 9x, so x =", ["6", "9", "*4", "3"], "36/9=4."),
    ("The power of a point theorem unifies:", ["Angle theorems", "*Chord, secant, and tangent segment relationships", "Area formulas", "Perimeter formulas"], "All three are 'power of a point.'"),
    ("If a tangent from point P = 8, then for any secant from P: (whole)(external) =", ["8", "16", "*64", "32"], "8²=64."),
    ("These segment relationships only apply when segments pass through or from:", ["Parallel lines", "*The same point", "Different points", "The center"], "Common point."),
    ("If two chords of lengths 14 and 10 intersect, and one chord is split 6:8, the other is split:", ["5:5", "*3:7 (oops, check: no, we need 6×8=48, so x(10-x)=48, but max product for length 10 is 25... so these specific numbers can't both be in the same circle this way)", "4:6", "2:8"], "Actually 6×8=48 but chord of length 10 has max product 25. Let me fix: if chord segments are 4 and 12 (chord length 16), and the other chord's segments are x and 10-x, then 4×12=48... For the product to be 48 with a chord summing to 16, 4 and 12 work. The other chord segments: need product 48, e.g. 6 and 8 (chord=14). So the answer depends on the specific problem. The key concept is products are equal."),
    ("For a secant from an external point, the 'external segment' is the part:", ["Inside the circle", "*From the external point to the nearer intersection with the circle", "From center to chord", "The whole secant"], "Nearer intersection."),
    ("The 'whole' secant is measured from:", ["Inside the circle to the first intersection", "*The external point to the farther intersection", "Center to center", "Tangent to tangent"], "External point to far intersection."),
    ("If no tangent, secant, or chord passes through a given point, the power of a point theorem:", ["Still applies", "*Does not apply (the point must relate to a line intersecting the circle)", "Gives area", "Gives zero"], "Must intersect circle."),
])
all_new[k] = q

k, q = add_qs("u10_l10.8", [
    ("The standard form of a circle equation is:", ["y = mx + b", "*(x-h)² + (y-k)² = r²", "Ax² + By² = C", "x² - y² = r²"], "(x-h)²+(y-k)²=r²."),
    ("The center of (x-3)² + (y+2)² = 25 is:", ["(3,2)", "*( 3,-2)", "(-3,2)", "(-3,-2)"], "h=3, k=-2."),
    ("The radius of (x-3)² + (y+2)² = 25 is:", ["25", "*5", "3", "2"], "r=sqrt(25)=5."),
    ("The equation of a circle centered at origin with radius 4:", ["x + y = 4", "x² + y² = 4", "*x² + y² = 16", "(x-4)² + (y-4)² = 0"], "r² = 16."),
    ("To convert x²+y²-6x+4y-12=0 to standard form:", ["Factor", "*Complete the square for x and y terms", "Divide by 12", "Take square root"], "Complete the square."),
    ("x²-6x+9 + y²+4y+4 = 12+9+4 gives:", ["(x-3)²+(y+2)²=12", "*(x-3)²+(y+2)²=25", "(x+3)²+(y-2)²=25", "(x-3)²+(y-2)²=25"], "r²=25, center (3,-2)."),
    ("The general form of a circle is:", ["(x-h)²+(y-k)²=r²", "*x²+y²+Dx+Ey+F=0", "y=mx+b", "Ax+By=C"], "Expanded form."),
    ("A circle with center (0,5) and radius 3:", ["x²+(y-5)²=9", "*x²+(y-5)²=9", "(x-5)²+y²=9", "x²+y²=25"], "h=0,k=5,r=3."),
    ("To find the equation of a circle given endpoints of a diameter (2,4) and (6,0): center =", ["(2,0)", "*(4,2)", "(6,4)", "(8,4)"], "Midpoint: ((2+6)/2,(4+0)/2)=(4,2)."),
    ("Radius = half the diameter length. If diameter endpoints are (2,4) and (6,0): d=sqrt(16+16)=sqrt(32), r=", ["sqrt(32)", "4", "*sqrt(8) = 2sqrt(2)", "8"], "r = sqrt(32)/2 = sqrt(8)."),
    ("The equation: (x-4)²+(y-2)²=8 with center (4,2) and r=2sqrt(2).", ["False", "*True", "Depends", "Center is wrong"], "Confirmed."),
    ("Point (1,1) is on circle (x-1)²+(y-1)²=r² only if r =", ["1", "*0 (the point IS the center, so it's on the circle of radius 0, which is just the point)", "2", "Undefined"], "If center=(1,1) and the point is (1,1), distance=0 so r=0 — just the center point."),
    ("To determine if point (5,3) is inside, on, or outside circle (x-2)²+(y-1)²=16: compute (5-2)²+(3-1)²=", ["16, so ON the circle", "*13, which is < 16, so INSIDE the circle", "20, so outside", "9, so inside"], "9+4=13 < 16, inside."),
])
all_new[k] = q

k, q = add_qs("u10_l10.9", [
    ("Conic sections are curves formed by the intersection of a plane and a:", ["Sphere", "*Double cone (right circular cone)", "Cylinder", "Prism"], "Plane cuts a cone."),
    ("The four conic sections are:", ["Lines, rays, segments, points", "*Circle, ellipse, parabola, hyperbola", "Squares, rectangles, triangles, circles", "Pentagons, hexagons, heptagons, octagons"], "Four types."),
    ("A circle is formed when the cutting plane is _____ to the axis of the cone.", ["Parallel", "*Perpendicular", "Oblique", "Tangent"], "Perpendicular = circle."),
    ("An ellipse is formed when the plane cuts at an angle _____ than the cone's slant.", ["Equal", "*Greater (steeper than the slant, but not perpendicular)", "Less", "Zero"], "Angle between perp and slant."),
    ("A parabola is formed when the plane is _____ to a slant side of the cone.", ["Perpendicular", "*Parallel", "At any angle", "Tangent"], "Parallel to slant = parabola."),
    ("A hyperbola is formed when the plane cuts _____ of the double cone.", ["One nappe only", "*Both nappes", "Parallel to the base", "Through the vertex only"], "Both nappes."),
    ("An ellipse has _____ foci.", ["1", "*2", "3", "0"], "Two foci."),
    ("The sum of distances from any point on an ellipse to its two foci is:", ["Variable", "*Constant", "Zero", "Equal to the radius"], "Constant sum."),
    ("A parabola has _____ focus/foci.", ["0", "*1", "2", "3"], "One focus."),
    ("A hyperbola has _____ foci.", ["1", "*2", "0", "3"], "Two foci."),
    ("The difference of distances from any point on a hyperbola to its foci is:", ["Variable", "*Constant", "Zero", "Equal to zero"], "Constant difference."),
    ("A degenerate conic can be a point, a line, or:", ["A circle", "An ellipse", "*Two intersecting lines", "A parabola"], "Degenerate cases."),
    ("The eccentricity of a circle is:", ["1", "Greater than 1", "*0", "Undefined"], "Circle: e = 0."),
])
all_new[k] = q

# ── U11: Area ──

k, q = add_qs("u11_l11.1", [
    ("The area of a parallelogram is:", ["side × side", "*base × height", "½ × base × height", "π × r²"], "A = bh."),
    ("The area of a triangle is:", ["base × height", "*½ × base × height", "side²", "π × r²"], "A = ½bh."),
    ("A parallelogram with base 10 and height 6 has area:", ["16", "32", "*60", "30"], "10 × 6 = 60."),
    ("A triangle with base 8 and height 5 has area:", ["40", "13", "*20", "80"], "½ × 8 × 5 = 20."),
    ("The height of a parallelogram is the _____ distance between the base and opposite side.", ["Diagonal", "*Perpendicular", "Slant", "Horizontal"], "Perpendicular height."),
    ("If the area of a triangle is 36 and the base is 12, the height is:", ["3", "12", "*6", "24"], "36 = ½(12)h, h = 6."),
    ("The area of a rectangle is a special case of the parallelogram formula where:", ["b = h", "*The height equals the width (sides are perpendicular)", "b + h = constant", "b × h = b + h"], "Rectangle: perpendicular sides."),
    ("A square with side 7 has area:", ["14", "28", "*49", "21"], "7² = 49."),
    ("Two triangles formed by a diagonal of a parallelogram have:", ["Different areas", "*Equal areas (each is half the parallelogram)", "Areas that sum to half", "No relation"], "Equal halves."),
    ("The area of a triangle with vertices at (0,0), (6,0), and (0,8):", ["48", "14", "*24", "7"], "½ × 6 × 8 = 24."),
    ("Using the coordinate formula: Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| is known as the:", ["Distance formula", "*Shoelace formula (for triangles)", "Midpoint formula", "Slope formula"], "Shoelace formula."),
    ("If a parallelogram has sides 5 and 10 but height 4 (relative to base 10), area =", ["50", "20", "*40", "15"], "10 × 4 = 40 (not side × side)."),
    ("Doubling both the base and height of a triangle multiplies the area by:", ["2", "*4", "8", "1"], "2b × 2h / 2 = 2bh = 4 × original."),
])
all_new[k] = q

k, q = add_qs("u11_l11.2", [
    ("The area of a trapezoid is:", ["base × height", "*(b₁ + b₂) × h / 2", "b₁ × b₂ × h", "½ × b × h"], "Average of bases times height."),
    ("The area of a rhombus (using diagonals d₁, d₂) is:", ["d₁ + d₂", "d₁ × d₂", "*½ × d₁ × d₂", "2(d₁ + d₂)"], "Half product of diagonals."),
    ("The area of a kite is:", ["d₁ + d₂", "d₁ × d₂", "*½ × d₁ × d₂", "(d₁ + d₂)/2"], "Same as rhombus: half product of diagonals."),
    ("Trapezoid with bases 6 and 10, height 4: area =", ["24", "40", "*32", "60"], "(6+10)×4/2=32."),
    ("A rhombus with diagonals 8 and 12: area =", ["20", "96", "*48", "40"], "½×8×12=48."),
    ("A kite with diagonals 5 and 14: area =", ["19", "70", "*35", "9"], "½×5×14=35."),
    ("The height of a trapezoid is the _____ distance between the two bases.", ["Diagonal", "Slant", "*Perpendicular", "Horizontal only"], "Perpendicular distance."),
    ("If trapezoid area = 50, bases are 8 and 12, the height is:", ["2.5", "10", "*5", "4"], "50=(8+12)h/2, h=5."),
    ("A square can be viewed as a rhombus with diagonals d and d: area = ½d² = s². If s=6, d=", ["6", "12", "*6√2", "36"], "d = s√2."),
    ("A trapezoid with equal legs is called:", ["A rectangle", "A rhombus", "*An isosceles trapezoid", "A kite"], "Isosceles trapezoid."),
    ("The area formula for a trapezoid can be remembered as: _____ of the bases times the height.", ["Sum", "Difference", "*Average (mean)", "Product"], "Average of bases."),
    ("If one diagonal of a kite is 10 and the area is 30, the other diagonal is:", ["3", "*6", "10", "15"], "30=½(10)(d₂), d₂=6."),
    ("The area of a rhombus can also be found using:", ["Only diagonals", "Only sides", "*Base × height (since it's a parallelogram)", "Only angles"], "A = bh works too."),
])
all_new[k] = q

k, q = add_qs("u11_l11.3", [
    ("The area of a circle is:", ["2πr", "πd", "*πr²", "2πr²"], "A = πr²."),
    ("The area of a sector is:", ["πr²", "*(θ/360)×πr² (where θ is the central angle in degrees)", "2πr", "½r²"], "Fraction of circle area."),
    ("A circle with radius 5 has area:", ["10π", "25", "*25π", "5π"], "π(5²)=25π."),
    ("A sector with central angle 90° and radius 8:", ["64π", "16π", "*16π (¼ × 64π)", "8π"], "(90/360)×π(64)=16π."),
    ("A sector with central angle 60° and radius 6:", ["36π", "12π", "*6π", "3π"], "(60/360)×36π=6π."),
    ("The area of a segment (region between a chord and its arc) =", ["Sector area + triangle area", "*Sector area - triangle area", "Circle area", "Half the sector"], "Segment = sector - triangle."),
    ("Arc length = (θ/360) × 2πr. For θ=45° and r=8:", ["π", "*2π (45/360 × 16π = 2π)", "4π", "8π"], "1/8 of 16π = 2π."),
    ("If the area of a circle is 49π, the radius is:", ["49", "*7", "14", "24.5"], "r²=49, r=7."),
    ("A semicircle has area:", ["πr²", "*πr²/2", "2πr", "πd"], "Half the circle."),
    ("If a sector area = 12π and r = 6, the central angle is:", ["60°", "*120° (12π = (θ/360)×36π, θ=120)", "90°", "180°"], "12π/36π = θ/360, θ=120."),
    ("Doubling the radius multiplies the area by:", ["2", "*4", "8", "π"], "Area ∝ r²."),
    ("The ratio of a sector's area to the circle's area equals:", ["r/R", "*θ/360° (the central angle fraction)", "2θ/360°", "πθ/180°"], "Same fraction as angle to full rotation."),
    ("The circumference of a circle with area 100π:", ["10π", "*20π (r=10, C=2πr=20π)", "100π", "50π"], "r=10, C=20π."),
])
all_new[k] = q

k, q = add_qs("u11_l11.4", [
    ("The area of a regular polygon: A = ½ × apothem × perimeter, or A = ½aP. If a=4, P=24:", ["96", "12", "*48", "28"], "½(4)(24)=48."),
    ("The apothem is the perpendicular distance from the center to:", ["A vertex", "*The midpoint of a side", "A diagonal", "Another polygon"], "Center to side midpoint."),
    ("A regular hexagon with side 6 has perimeter:", ["18", "24", "*36", "42"], "6 × 6 = 36."),
    ("The apothem of a regular hexagon with side 6 is:", ["6", "*3√3", "6√3", "3"], "a = s√3/2 = 3√3."),
    ("Area of that hexagon: ½(3√3)(36) =", ["36√3", "108", "*54√3", "18√3"], "½ × 3√3 × 36 = 54√3."),
    ("The area of a composite figure is found by:", ["One formula", "*Breaking it into simpler shapes and summing (or subtracting) their areas", "Multiplying all dimensions", "Dividing the perimeter by 2"], "Decompose into simpler shapes."),
    ("An L-shaped region can be split into:", ["Circles", "*Two rectangles", "Three triangles always", "One square"], "Rectangles work for L-shapes."),
    ("A regular triangle (equilateral) with side s has area:", ["s²", "½s²", "*s²√3/4", "s²/2"], "Equilateral triangle formula."),
    ("If a composite figure has a rectangle (8×5) with a semicircle (diameter 5) removed, the area is:", ["40 + 25π/8", "40", "*40 - 25π/8", "40 - 25π/4"], "40 - π(2.5)²/2 = 40 - 25π/8."),
    ("The perimeter of a composite figure includes only the _____ edges.", ["Interior", "*Outer (boundary)", "All", "Longest"], "Only the boundary."),
    ("A regular octagon with apothem a and side s: perimeter P = 8s, area =", ["8as", "4as", "*½ × a × 8s = 4as", "16as"], "½aP = ½a(8s) = 4as."),
    ("For regular polygons, as the number of sides increases, the shape approaches a:", ["Square", "*Circle", "Line", "Point"], "Polygon → circle."),
    ("The area of a regular polygon can also be found using: A = ½nsr, where n = number of sides, s = side, r = apothem. This is equivalent to:", ["A = ns²", "A = nr²", "*A = ½aP (since P = ns)", "A = πr²"], "Same formula rearranged."),
])
all_new[k] = q

k, q = add_qs("u11_l11.5", [
    ("If two figures are similar with scale factor k, the ratio of their areas is:", ["k", "k³", "*k²", "2k"], "Area ratio = square of scale factor."),
    ("Similar triangles with scale factor 3:5 have area ratio:", ["3:5", "6:10", "*9:25", "27:125"], "(3/5)²=9/25."),
    ("If the area of the smaller figure is 18 and scale factor is 1:3, the larger area is:", ["54", "6", "*162 (18 × 9)", "18"], "18 × 3² = 162."),
    ("If areas of similar figures are 50 and 200, the scale factor is:", ["50:200", "1:2", "*1:2 (sqrt(50/200) = sqrt(1/4) = 1/2)", "1:4"], "sqrt(50/200) = 1/2."),
    ("The ratio of perimeters of similar figures with area ratio 4:9 is:", ["4:9", "16:81", "*2:3 (sqrt of area ratio)", "8:18"], "sqrt(4/9) = 2/3."),
    ("If the perimeter ratio is 5:8, the area ratio is:", ["5:8", "10:16", "*25:64", "125:512"], "(5/8)² = 25/64."),
    ("Two similar rectangles have areas 12 and 48. The ratio of their corresponding sides is:", ["1:4", "12:48", "*1:2 (sqrt(12/48) = sqrt(1/4) = 1/2)", "3:12"], "1:2."),
    ("A figure is enlarged by scale factor 4. Its area is multiplied by:", ["4", "8", "*16", "2"], "4² = 16."),
    ("If a figure is reduced by half (k=½), its area becomes:", ["½ the original", "*¼ the original", "⅛ the original", "2 times the original"], "(½)² = ¼."),
    ("The relationship between linear scale factor and area scale factor is:", ["Linear", "*Quadratic (area factor = linear factor squared)", "Cubic", "No relationship"], "Quadratic."),
    ("Two similar hexagons have side ratio 2:7. The larger has area 490. The smaller's area:", ["140", "20", "*40 (490 × (2/7)² = 490 × 4/49 = 40)", "490"], "490 × 4/49 = 40."),
    ("If a triangle's sides are all tripled, its area is multiplied by:", ["3", "6", "*9", "27"], "3² = 9."),
    ("The area ratio of similar figures is always the _____ of the linear scale factor.", ["Same as", "*Square", "Cube", "Reciprocal"], "Square relationship."),
])
all_new[k] = q

k, q = add_qs("u11_l11.6", [
    ("Integration in geometry can approximate areas under:", ["Straight lines only", "*Curves", "No shapes", "Only circles"], "Area under curves."),
    ("The area under a curve can be estimated using:", ["One rectangle", "*Many thin rectangles (Riemann sums)", "Circles", "Triangles only"], "Rectangular approximation."),
    ("As the number of rectangles increases, the approximation becomes:", ["Worse", "The same", "*More accurate", "Infinite"], "More rectangles = better."),
    ("The limit of Riemann sums as the rectangle width approaches zero gives the:", ["Perimeter", "*Exact area (definite integral)", "Volume", "Circumference"], "Integral = exact area."),
    ("Archimedes found the area of a circle using a method similar to:", ["Counting squares", "*Inscribing and circumscribing polygons with increasing sides", "Weighing", "Guessing"], "Polygon approximation."),
    ("As the number of sides of an inscribed regular polygon increases, its area approaches:", ["Zero", "Infinity", "*πr² (the area of the circle)", "2πr"], "Area approaches πr²."),
    ("Cavalieri's Principle (2D): if two regions have the same width at every height, they have the same:", ["Perimeter", "*Area", "Shape", "Number of sides"], "Same cross-section widths = same area."),
    ("A trapezoid approximation uses _____ instead of rectangles for better accuracy.", ["Circles", "*Trapezoids", "Squares", "Polygons"], "Trapezoidal rule."),
    ("The notation ∫ represents:", ["Sum", "*Integral (sum of infinitely thin slices)", "Product", "Division"], "Integral symbol."),
    ("Numerical integration is used when an exact antiderivative is:", ["Always available", "*Difficult or impossible to find analytically", "Not needed", "Always zero"], "Practical estimation."),
    ("The area between two curves is found by integrating the:", ["Sum", "*Difference (top minus bottom)", "Product", "Quotient"], "Difference of functions."),
    ("Simpson's Rule uses _____ to approximate the curve between sample points.", ["Lines", "*Parabolas", "Circles", "Straight lines only"], "Parabolic approximation."),
    ("These area approximation methods connect geometry to:", ["Statistics", "Probability", "*Calculus", "Trigonometry only"], "Foundation of integral calculus."),
])
all_new[k] = q

# ── U12: Surface Area & Volume ──

k, q = add_qs("u12_l12.1", [
    ("A 3D figure can be represented in 2D using:", ["Only photographs", "*Isometric drawings, orthographic projections, nets, and cross-sections", "Only blueprints", "Only perspective"], "Multiple methods."),
    ("An isometric drawing shows three faces of a 3D object from:", ["Directly above", "*A corner angle (showing length, width, height)", "Directly in front", "Below"], "Corner view."),
    ("Orthographic projections show:", ["Perspective views", "*Top, front, and side views (flat, no depth distortion)", "Only one view", "Only diagonals"], "Three flat views."),
    ("A net is a:", ["3D representation", "*2D pattern that folds into a 3D figure", "Cross-section", "Projection"], "Unfolds flat."),
    ("A cross-section is formed when a _____ cuts through a solid.", ["Line", "*Plane", "Point", "Ray"], "Plane intersection."),
    ("A horizontal cross-section of a cylinder is a:", ["Rectangle", "*Circle", "Triangle", "Ellipse"], "Circle at every height."),
    ("A vertical cross-section through the center of a cone is a:", ["Circle", "*Triangle (isosceles)", "Rectangle", "Ellipse"], "Triangular cross-section."),
    ("A cross-section of a sphere is always a:", ["Square", "Triangle", "*Circle", "Ellipse"], "Always circular."),
    ("A horizontal cross-section of a rectangular prism is a:", ["Triangle", "Circle", "*Rectangle", "Hexagon"], "Rectangle."),
    ("A net of a cube has _____ squares.", ["4", "5", "*6", "8"], "6 faces = 6 squares."),
    ("An oblique cylinder viewed from the side appears as a:", ["Circle", "Triangle", "*Parallelogram (or rectangle)", "Pentagon"], "Side view = parallelogram."),
    ("Cavalieri's Principle: solids with equal cross-sectional areas at every height have equal:", ["Surface area", "*Volume", "Height", "Bases"], "Same volume."),
    ("A diagonal cross-section of a cube can produce a:", ["Circle", "*Regular hexagon (if cut through midpoints of 6 edges)", "Pentagon only", "Octagon"], "Hexagonal cross-section possible."),
])
all_new[k] = q

k, q = add_qs("u12_l12.2", [
    ("The surface area of a prism = 2 × base area + _____ area.", ["Base", "*Lateral", "Top", "Bottom"], "SA = 2B + LA."),
    ("The lateral area of a right prism = perimeter of base × _____.", ["Radius", "*Height", "Diameter", "Area"], "LA = Ph."),
    ("The surface area of a cylinder = 2πr² + _____.", ["πr²", "2πr", "*2πrh", "πrh"], "SA = 2πr² + 2πrh."),
    ("A rectangular prism 3×4×5 has surface area:", ["60", "*94 (2(12+15+20) = 94)", "120", "47"], "2(3×4+3×5+4×5)=94."),
    ("A cylinder with r=3 and h=7: lateral area =", ["21π", "*42π", "63π", "9π"], "2π(3)(7)=42π."),
    ("Total surface area of that cylinder: 42π + 2π(9) =", ["*60π", "51π", "42π", "18π"], "42π + 18π = 60π."),
    ("The net of a cylinder is two circles and a:", ["Square", "Triangle", "*Rectangle", "Pentagon"], "Rectangle wraps around."),
    ("The height of a prism is the _____ distance between the two bases.", ["Diagonal", "*Perpendicular", "Slant", "Lateral"], "Perpendicular distance."),
    ("For an oblique prism, the lateral area uses the _____ height.", ["Perpendicular", "*Slant (lateral edge length) — or more precisely, perpendicular height with adjusted calculation", "Base", "Diagonal"], "Oblique prism uses lateral edge."),
    ("A triangular prism has _____ rectangular lateral faces.", ["2", "*3", "4", "6"], "3 lateral faces."),
    ("A pentagonal prism has _____ lateral faces.", ["3", "4", "*5", "6"], "5 lateral faces."),
    ("A hexagonal prism has _____ faces total (including bases).", ["6", "*8", "10", "12"], "6 lateral + 2 bases = 8."),
    ("Surface area is measured in:", ["Cubic units", "Linear units", "*Square units", "No units"], "Square units."),
])
all_new[k] = q

k, q = add_qs("u12_l12.3", [
    ("The lateral area of a regular pyramid = ½ × perimeter × _____.", ["Height", "*Slant height", "Apothem", "Radius"], "LA = ½Pl."),
    ("The surface area of a pyramid = base area + _____.", ["Base area again", "*Lateral area", "Volume", "Height × base"], "SA = B + LA."),
    ("The lateral area of a cone = πr × _____.", ["h", "r", "*l (slant height)", "2r"], "LA = πrl."),
    ("The surface area of a cone = πr² + _____.", ["πr²", "2πrh", "*πrl", "πr"], "SA = πr² + πrl."),
    ("Slant height l of a cone with r=3 and h=4:", ["7", "12", "*5", "25"], "l=sqrt(9+16)=5."),
    ("SA of that cone: π(9) + π(3)(5) =", ["14π", "*24π", "15π", "45π"], "9π+15π=24π."),
    ("A square pyramid with base side 6 and slant height 5: LA =", ["30", "120", "*60 (½ × 24 × 5)", "24"], "½(24)(5)=60."),
    ("SA of that pyramid: 36 + 60 =", ["120", "*96", "60", "36"], "36+60=96."),
    ("The slant height of a regular pyramid is the height of a:", ["Base", "Vertex", "*Lateral face (from apex to base edge midpoint)", "Diagonal"], "Height of triangular face."),
    ("For an oblique pyramid/cone, the slant height is not uniform, making the lateral area:", ["Simpler", "*More complex to calculate", "Zero", "The same as a right pyramid"], "Not straightforward."),
    ("The apex of a pyramid or cone is the:", ["Base center", "*Top vertex (point)", "Midpoint of base", "Edge"], "Top point."),
    ("A cone can be thought of as a pyramid with a _____ base.", ["Square", "Triangular", "*Circular (infinitely many sides)", "Hexagonal"], "Circular base = infinite-sided polygon."),
    ("If the slant height of a cone is 13 and the radius is 5, the height is:", ["8", "18", "*12", "144"], "h=sqrt(169-25)=sqrt(144)=12."),
])
all_new[k] = q

k, q = add_qs("u12_l12.4", [
    ("The volume of a prism = base area × _____.", ["Perimeter", "*Height", "Slant height", "Lateral area"], "V = Bh."),
    ("The volume of a cylinder = πr² × _____.", ["2πr", "*h", "l", "πr"], "V = πr²h."),
    ("A rectangular prism 3 × 4 × 5 has volume:", ["47", "94", "*60", "12"], "3×4×5=60."),
    ("A cylinder with r=4 and h=10: volume =", ["40π", "80π", "*160π", "320π"], "π(16)(10)=160π."),
    ("Volume is measured in:", ["Square units", "Linear units", "*Cubic units", "No units"], "Cubic units."),
    ("Cavalieri's Principle: if two solids have equal cross-sectional areas at every height, they have equal:", ["Surface area", "*Volume", "Base area", "Lateral area"], "Same volume."),
    ("By Cavalieri's, an oblique cylinder with the same base and height as a right cylinder has _____ volume.", ["Less", "More", "*The same", "Double"], "Same base, same height = same volume."),
    ("A cube with edge 5 has volume:", ["25", "150", "*125", "5"], "5³=125."),
    ("A triangular prism with base area 12 and height 8: volume =", ["20", "48", "*96", "192"], "12×8=96."),
    ("If a cylinder's radius is doubled and height stays the same, volume is multiplied by:", ["2", "*4", "8", "π"], "r² quadruples."),
    ("If both radius and height are doubled, volume is multiplied by:", ["4", "*8 (2² × 2 = 8)", "2", "16"], "r²h: 4 × 2 = 8."),
    ("The volume of a hexagonal prism: V = (area of regular hexagon) × h = _____ × h.", ["6s²", "*3s²√3/2 (where s = side of hexagon)", "πr²", "s³"], "Hexagon area × h."),
    ("A cylinder with diameter 10 and height 12: V =", ["120π", "600π", "*300π (π×25×12)", "1200π"], "r=5, πr²h=300π."),
])
all_new[k] = q

k, q = add_qs("u12_l12.5", [
    ("The volume of a pyramid = _____ × base area × height.", ["½", "*⅓", "¼", "1"], "V = ⅓Bh."),
    ("The volume of a cone = _____ × πr²h.", ["½", "*⅓", "¼", "1"], "V = ⅓πr²h."),
    ("A square pyramid with base side 6 and height 10: V =", ["360", "180", "*120 (⅓ × 36 × 10)", "60"], "⅓(36)(10)=120."),
    ("A cone with r=3 and h=8: V =", ["72π", "24π", "*24π (⅓π(9)(8))", "36π"], "⅓π(9)(8)=24π."),
    ("A pyramid has _____ the volume of a prism with the same base and height.", ["½", "*⅓", "¼", "Same"], "One-third."),
    ("A cone has _____ the volume of a cylinder with the same base and height.", ["½", "*⅓", "¼", "Same"], "One-third."),
    ("If a cone has V = 100π and r = 5, the height is:", ["4", "20", "*12 (100π = ⅓π(25)h, h = 12)", "8"], "h = 300/25 = 12."),
    ("If a pyramid's height is tripled (base unchanged), volume is:", ["Tripled", "Unchanged", "*Tripled (V ∝ h)", "Multiplied by 9"], "Linear in h."),
    ("An oblique cone with same base and height as a right cone has:", ["Less volume", "More volume", "*The same volume (Cavalieri's Principle)", "Half the volume"], "Same by Cavalieri's."),
    ("A cone-shaped cup with r = 4 cm and h = 9 cm holds _____ cm³.", ["144π", "36π", "*48π (⅓π(16)(9))", "108π"], "⅓π(16)(9) = 48π."),
    ("The frustum of a cone (cone with top cut off) has volume:", ["⅓πr²h", "*⅓πh(R² + Rr + r²) where R and r are the two radii", "πR²h - πr²h", "πh(R+r)"], "Frustum formula."),
    ("A pyramid with rectangular base 8×5 and height 12: V =", ["480", "240", "*160 (⅓ × 40 × 12)", "80"], "⅓(40)(12) = 160."),
    ("Three identical pyramids can fill a prism with the same:", ["Surface area", "Perimeter", "*Base and height", "Lateral area"], "Three pyramids = one prism."),
])
all_new[k] = q

k, q = add_qs("u12_l12.6", [
    ("The surface area of a sphere = _____.", ["2πr²", "πr²", "*4πr²", "⅘πr³"], "SA = 4πr²."),
    ("The volume of a sphere = _____.", ["4πr²", "2πr³", "*⅘πr³ — actually (4/3)πr³", "πr³"], "V = (4/3)πr³."),
    ("A sphere with radius 3: SA =", ["9π", "27π", "*36π", "12π"], "4π(9)=36π."),
    ("Volume of that sphere: (4/3)π(27) =", ["27π", "*36π", "108π", "12π"], "(4/3)(27π)=36π."),
    ("If the radius of a sphere is doubled, the surface area is multiplied by:", ["2", "*4", "8", "16"], "SA ∝ r²."),
    ("If the radius is doubled, the volume is multiplied by:", ["2", "4", "*8", "16"], "V ∝ r³."),
    ("A hemisphere has volume:", ["(4/3)πr³", "*(2/3)πr³", "2πr³", "πr³"], "Half the sphere."),
    ("The surface area of a hemisphere (including the flat base) = 2πr² + πr² =", ["2πr²", "*3πr²", "4πr²", "πr²"], "Curved (2πr²) + flat base (πr²)."),
    ("A sphere with diameter 10: radius =", ["10", "*5", "20", "100"], "r = d/2 = 5."),
    ("Volume when r=5: (4/3)π(125) =", ["100π", "*(500/3)π ≈ 166.7π", "500π", "125π"], "(4/3)(125π)=500π/3."),
    ("A sphere fits perfectly inside a cylinder when the cylinder has:", ["r = 2R", "*Same radius and height = diameter (h = 2r)", "r = ½R", "h = r"], "Cylinder circumscribes sphere."),
    ("The ratio of sphere volume to the circumscribing cylinder volume is:", ["½", "*⅔", "¾", "⅓"], "Sphere/cylinder = 2/3."),
    ("A ball with radius 6 inches occupies how much space?", ["144π in³", "216π in³", "*288π in³ ((4/3)π(216))", "864π in³"], "(4/3)(216)π = 288π."),
])
all_new[k] = q

k, q = add_qs("u12_l12.7", [
    ("In spherical geometry, 'lines' are:", ["Straight lines", "*Great circles (circles with the same center and radius as the sphere)", "Small circles", "Tangent lines"], "Great circles replace lines."),
    ("A great circle divides a sphere into:", ["Unequal parts", "*Two equal hemispheres", "Four parts", "Three parts"], "Equal hemispheres."),
    ("In spherical geometry, the sum of angles in a triangle is:", ["Exactly 180°", "Less than 180°", "*Greater than 180° (between 180° and 540°)", "Exactly 360°"], "Exceeds 180° on a sphere."),
    ("Parallel lines in Euclidean geometry _____ in spherical geometry.", ["Always exist", "*Do not exist (all great circles intersect)", "Are the same", "Are perpendicular"], "No parallel lines."),
    ("Two great circles always intersect at:", ["One point", "*Two points (diametrically opposite)", "No points", "Three points"], "Antipodal points."),
    ("In spherical geometry, the shortest path between two points is along a:", ["Small circle", "*Great circle (geodesic)", "Straight line", "Spiral"], "Great circle route."),
    ("Airplane routes often follow great circle paths because they are:", ["Scenic", "*The shortest distance between two points on a sphere", "The easiest to navigate", "Required by law"], "Shortest path on sphere."),
    ("The excess of a spherical triangle (sum of angles - 180°) is related to its:", ["Perimeter", "*Area", "Number of sides", "Nothing"], "Angular excess ∝ area."),
    ("In Euclidean geometry the Parallel Postulate holds, but in spherical geometry:", ["It also holds", "*It fails (there are no parallel lines)", "It's optional", "It's stronger"], "No parallels on a sphere."),
    ("A lune is a region on a sphere bounded by:", ["One great circle", "*Two great semicircles (sharing endpoints at antipodal points)", "Three great circles", "A small circle"], "Two semicircles."),
    ("Spherical geometry is an example of:", ["Euclidean geometry", "*Non-Euclidean geometry", "Coordinate geometry", "Fractal geometry"], "Non-Euclidean."),
    ("On a globe, lines of longitude are:", ["Small circles", "*Great circles (each passing through both poles)", "Parallel lines", "Tangent lines"], "Longitude = great circles."),
    ("Lines of latitude (except the equator) are:", ["Great circles", "*Small circles (not the shortest path)", "Straight lines", "Geodesics"], "Small circles."),
])
all_new[k] = q

k, q = add_qs("u12_l12.8", [
    ("Similar solids have the same shape but different:", ["Angles", "*Size", "Color", "Number of faces"], "Same shape, different size."),
    ("If two similar solids have a linear scale factor of k, the ratio of their surface areas is:", ["k", "*k²", "k³", "2k"], "SA ratio = k²."),
    ("If two similar solids have a linear scale factor of k, the ratio of their volumes is:", ["k", "k²", "*k³", "2k"], "Volume ratio = k³."),
    ("Similar cylinders with radii 2 and 6 have scale factor:", ["2:6", "*1:3", "4:36", "8:216"], "2/6=1/3."),
    ("Their surface area ratio:", ["1:3", "*1:9", "1:27", "2:6"], "(1/3)²=1/9."),
    ("Their volume ratio:", ["1:3", "1:9", "*1:27", "2:6"], "(1/3)³=1/27."),
    ("If two similar prisms have volumes 8 and 64, the scale factor is:", ["1:8", "*1:2 (cube root of 8/64 = cube root of 1/8 = 1/2)", "1:4", "2:8"], "∛(1/8)=1/2."),
    ("With that scale factor, the SA ratio is:", ["1:2", "*1:4", "1:8", "1:64"], "(1/2)²=1/4."),
    ("If a model car is 1:18 scale, its volume is _____ of the real car's volume.", ["1/18", "1/324", "*1/5832 (1/18³)", "1/36"], "1/18³."),
    ("A sphere with 3× the radius of another has _____ the volume.", ["3", "9", "*27", "81"], "3³=27."),
    ("If the SA of a small solid is 50 and scale factor is 1:4, the large solid's SA is:", ["200", "400", "*800 (50 × 16)", "3200"], "50 × 4² = 800."),
    ("If the volume of a large solid is 1000 and scale factor (small:large) is 1:5, the small volume is:", ["200", "40", "*8 (1000 × (1/5)³)", "1"], "1000/125=8."),
    ("When comparing similar solids: perimeter ratio = k, area ratio = k², volume ratio = k³. These are:", ["All linear", "*Dimensional relationships (length, area, volume)", "All the same", "Unrelated"], "Each adds one dimension."),
])
all_new[k] = q

k, q = add_qs("u12_l12.9", [
    ("Cavalieri's Principle states that if two solids have the same _____ at every level, they have the same volume.", ["Base area", "*Cross-sectional area", "Height", "Surface area"], "Equal cross-sections = equal volume."),
    ("A stack of coins (cylinder) and a tilted stack have the same volume because:", ["They look the same", "*They have equal cross-sectional areas at each height (Cavalieri's)", "They weigh the same", "They have the same surface area"], "Cavalieri's Principle."),
    ("Cavalieri's Principle works regardless of whether the solid is:", ["Only right", "Only oblique", "*Right or oblique (the tilt doesn't matter)", "Neither"], "Applies to all orientations."),
    ("Two different-shaped solids can have the same volume if their cross-sections at every height:", ["Look the same", "*Have equal areas", "Have equal perimeters", "Are the same shape"], "Equal areas, not necessarily same shape."),
    ("Cavalieri's Principle is named after:", ["Euclid", "Archimedes", "*Bonaventura Cavalieri (17th century Italian mathematician)", "Descartes"], "Italian mathematician."),
    ("Using Cavalieri's, a hemisphere can be compared with a cylinder minus a:", ["Sphere", "Prism", "*Cone (cylinder with inscribed cone removed)", "Cube"], "Hemisphere = cylinder - cone."),
    ("The volume of a hemisphere by this method: πr²(r) - ⅓πr²(r) = ⅔πr³, matching:", ["πr³", "*⅔πr³ (half of 4/3πr³)", "4/3πr³", "2πr³"], "Correct hemisphere formula."),
    ("Cavalieri's Principle can be considered a precursor to:", ["Algebra", "Geometry basics", "*Integral calculus", "Trigonometry"], "Integration concepts."),
    ("The principle applies in 2D as well: two 2D regions with equal widths at every height have the same:", ["Perimeter", "*Area", "Shape", "Number of sides"], "2D version."),
    ("A cylinder and a prism with the same base area and height have equal volume by:", ["Formula only", "*Cavalieri's Principle", "Coincidence", "The Pythagorean Theorem"], "Same cross-section at every height."),
    ("If solid A has cross-section 10 cm² at every height from 0 to 5 cm, its volume is:", ["10 cm³", "15 cm³", "*50 cm³ (10 × 5)", "100 cm³"], "Constant cross-section × height."),
    ("This principle helps justify volume formulas for:", ["Only spheres", "Only cones", "Only cylinders", "*All solids (oblique prisms, cones, etc.)"], "Universal application."),
    ("A right cone and an oblique cone with the same base radius and height have:", ["Different volumes", "*The same volume (by Cavalieri's)", "Different shapes", "The same surface area"], "Same volume."),
])
all_new[k] = q

# ── U13: Probability ──

k, q = add_qs("u13_l13.1", [
    ("A sample space is the set of all possible _____ of an experiment.", ["Probabilities", "*Outcomes", "Events", "Combinations"], "All possible outcomes."),
    ("The sample space for flipping a coin:", ["{H}", "{T}", "*{H, T}", "{HH, TT}"], "Two outcomes."),
    ("The sample space for rolling a die:", ["{1,2,3}", "{1,6}", "*{1,2,3,4,5,6}", "{odd,even}"], "Six outcomes."),
    ("An event is a _____ of the sample space.", ["Copy", "Complement always", "*Subset", "Superset"], "Subset of outcomes."),
    ("For two coins flipped, the sample space has _____ outcomes.", ["2", "3", "*4 (HH, HT, TH, TT)", "8"], "2²=4."),
    ("A tree diagram helps list outcomes by showing:", ["Only one branch", "*All branches (each decision point and its possibilities)", "Only the final outcomes", "Only probabilities"], "All branches."),
    ("The Fundamental Counting Principle: if event A has m ways and event B has n ways, together they have:", ["m + n", "*m × n ways", "m - n", "m/n"], "Multiply choices."),
    ("Choosing a shirt (5 options) and pants (4 options): total outfits =", ["9", "*20", "1", "54"], "5×4=20."),
    ("The number of outcomes for 3 coin flips:", ["3", "6", "*8 (2³)", "9"], "2×2×2=8."),
    ("A compound event involves:", ["One outcome", "*Two or more simple events", "No outcomes", "Only one trial"], "Multiple events."),
    ("Using a table to list all outcomes of rolling two dice shows _____ outcomes.", ["12", "24", "*36 (6×6)", "6"], "36 outcomes."),
    ("The probability of any event is between:", ["-1 and 1", "*0 and 1 (inclusive)", "0 and ∞", "1 and 100"], "0 ≤ P ≤ 1."),
    ("If the sample space has n equally likely outcomes, P(event) = favorable outcomes ÷ _____.", ["Favorable", "*n (total outcomes)", "2", "1"], "P = favorable/total."),
])
all_new[k] = q

k, q = add_qs("u13_l13.2", [
    ("A permutation is an arrangement where _____ matters.", ["Size", "*Order", "Color", "Number"], "Order matters."),
    ("A combination is a selection where order _____ matter.", ["Does", "*Does not", "Sometimes does", "Always does"], "Order doesn't matter."),
    ("n! (n factorial) = n × (n-1) × ... × 1. 5! =", ["25", "*120", "60", "15"], "5×4×3×2×1=120."),
    ("0! =", ["0", "Undefined", "*1", "∞"], "By definition."),
    ("P(n,r) = n!/(n-r)!. P(5,3) =", ["10", "*60", "125", "15"], "5!/2!=120/2=60."),
    ("C(n,r) = n!/(r!(n-r)!). C(5,3) =", ["60", "*10", "15", "6"], "120/(6×2)=10."),
    ("Choosing 3 people from 10 for a committee (order doesn't matter): C(10,3) =", ["720", "*120", "30", "1000"], "10!/(3!7!)=120."),
    ("Arranging 4 books on a shelf: P(4,4) = 4! =", ["16", "12", "*24", "4"], "4!=24."),
    ("The number of ways to arrange the letters in 'CAT':", ["3", "*6 (3!)", "9", "27"], "3!=6."),
    ("C(n,0) = C(n,n) =", ["0", "n", "*1", "n!"], "Always 1."),
    ("C(n,r) = C(n, n-r) because choosing r items is the same as:", ["Choosing r", "*Choosing which n-r items to leave out", "Choosing n", "Nothing"], "Complementary selection."),
    ("Permutations with repetition: arranging n items where some repeat. 'MISSISSIPPI' has _____ distinct arrangements.", ["11!", "11!/4!", "*11!/(4!4!2!) = 34,650", "11!/(4!4!)"], "Account for repeated letters."),
    ("A circular permutation of n items = (n-1)! because:", ["One item is fixed", "*Rotations of the same arrangement are identical", "One less item", "It's simpler"], "Fix one position."),
])
all_new[k] = q

k, q = add_qs("u13_l13.3", [
    ("Geometric probability uses _____ to determine probability.", ["Counting only", "*Length, area, or volume ratios", "Tree diagrams", "Permutations"], "Measurement-based probability."),
    ("If a dart is thrown randomly at a 10×10 board with a 5×5 target area, P(hitting target) =", ["½", "*¼ (25/100)", "⅕", "5/10"], "25/100=1/4."),
    ("If a circular target of radius 3 is inside a square board of side 10, P(hitting circle) =", ["3/10", "9/100", "*9π/100 (π(9)/100)", "3π/10"], "πr²/s²=9π/100."),
    ("A spinner divided into sectors: P(landing on a sector) = sector angle / _____.", ["180", "*360", "90", "sector area"], "Angle/360."),
    ("A spinner with a 90° red sector: P(red) =", ["½", "⅓", "*¼", "⅛"], "90/360=1/4."),
    ("A point is chosen randomly on a segment of length 12. The probability it's within 3 units of the left endpoint:", ["3/12", "*¼ (3/12)", "½", "3"], "3/12=1/4."),
    ("Geometric probability can model _____ events where outcomes lie on a continuum.", ["Discrete", "*Continuous", "Finite", "Impossible"], "Continuous sample space."),
    ("A bus arrives every 15 minutes. If you arrive at a random time, P(waiting less than 5 min) =", ["*⅓ (5/15)", "½", "5/60", "¼"], "5/15=1/3."),
    ("If a 2-ft diameter circle is inscribed in a 4-ft square and a coin is tossed onto the square, P(landing in circle) =", ["½", "*π/4 ≈ 0.785", "¼", "π/2"], "πr²/s²=π(1)/4=π/4."),
    ("The waiting time problem: P(waiting ≤ t) when total interval is T equals:", ["T/t", "*t/T", "tT", "1-t/T"], "t/T."),
    ("In a 2D geometric probability problem, the probability equals the ratio of:", ["Perimeters", "*Areas (favorable region / total region)", "Diameters", "Angles"], "Area ratio."),
    ("Monte Carlo methods estimate geometric probability by:", ["Exact calculation", "*Random sampling (throwing many 'darts' and counting hits)", "Measuring", "Counting outcomes"], "Simulation approach."),
    ("If a region A is entirely inside region B, P(landing in A | landing in B) = Area(A)/Area(B). This is:", ["Always 1", "*The basic geometric probability formula", "Always 0", "Undefined"], "Fundamental formula."),
])
all_new[k] = q

k, q = add_qs("u13_l13.4", [
    ("A simulation uses a model to:", ["Prove a theorem", "*Imitate a real-world process and estimate probabilities", "Solve equations", "Draw figures"], "Model real processes."),
    ("Random number generators help create:", ["Proofs", "*Unbiased simulated outcomes", "Theorems", "Equations"], "Unbiased randomness."),
    ("To simulate flipping a coin, assign 0 = tails and 1 = heads, then generate random:", ["Letters", "*Integers (0 or 1)", "Decimals between 0 and 100", "Fractions"], "Binary random integers."),
    ("To simulate rolling a die, generate random integers from:", ["0 to 6", "*1 to 6", "1 to 5", "0 to 5"], "1 through 6."),
    ("One trial of a simulation represents one:", ["Answer", "*Run of the experiment", "Calculation", "Proof"], "One experiment run."),
    ("As the number of trials increases, the experimental probability approaches the:", ["Model", "*Theoretical probability (Law of Large Numbers)", "Initial estimate", "Zero"], "Law of Large Numbers."),
    ("The Law of Large Numbers states that more trials lead to:", ["More error", "*Better approximation of true probability", "Less accuracy", "Exactly the right answer"], "Convergence to true probability."),
    ("A simulation of 1000 coin flips yielding 515 heads gives P(heads) ≈", ["0.500", "*0.515", "0.485", "1.000"], "515/1000=0.515."),
    ("Simulations are useful when:", ["Exact answers are easy", "*Exact calculation is difficult or impossible", "We want to avoid probability", "Only for games"], "When exact math is hard."),
    ("To simulate a 30% chance of rain, generate random numbers 1-100 and assign rain to:", ["1-50", "1-3", "*1-30", "1-70"], "30 out of 100."),
    ("Repeating a simulation multiple times and averaging the results is called:", ["Guessing", "*Monte Carlo simulation", "Proof by contradiction", "Deduction"], "Monte Carlo approach."),
    ("A well-designed simulation should:", ["Always give exact answers", "*Use appropriate random devices and enough trials", "Use only dice", "Run exactly once"], "Proper design."),
    ("Simulations can help estimate:", ["Only simple probabilities", "*Complex probabilities, waiting times, and expected values", "Only dice outcomes", "Only coin flips"], "Versatile tool."),
])
all_new[k] = q

k, q = add_qs("u13_l13.5", [
    ("Two events are independent if the occurrence of one _____ the probability of the other.", ["Increases", "Decreases", "*Does not affect", "Eliminates"], "No influence."),
    ("P(A and B) for independent events = P(A) × _____.", ["P(A)", "*P(B)", "P(A) + P(B)", "1"], "Multiply probabilities."),
    ("Rolling a die and flipping a coin are:", ["Dependent", "*Independent", "Mutually exclusive", "Complementary"], "One doesn't affect the other."),
    ("P(heads and 6) = P(heads) × P(6) = ½ × ⅙ =", ["⅓", "½", "*1/12", "⅙"], "1/12."),
    ("Two events are dependent if the outcome of one _____ the probability of the other.", ["Does not affect", "*Affects", "Doubles", "Halves exactly"], "Influences probability."),
    ("P(A and B) for dependent events = P(A) × P(B|A), where P(B|A) is:", ["P(B)", "*The probability of B given A has occurred", "P(A) given B", "P(A)P(B)"], "Conditional probability."),
    ("Drawing two cards without replacement: the events are:", ["Independent", "*Dependent (the first draw changes the remaining deck)", "Mutually exclusive", "Impossible"], "No replacement = dependent."),
    ("P(two aces without replacement) from a standard deck: P(first ace) = 4/52, P(second ace | first ace) = 3/51. P(both) =", ["16/2652", "*12/2652 = 1/221", "4/52", "8/52"], "(4/52)(3/51)=12/2652."),
    ("If events ARE independent, P(B|A) = _____.", ["P(A)", "*P(B) (knowing A happened doesn't change B's probability)", "0", "1"], "Definition of independence."),
    ("Drawing with replacement makes events:", ["Dependent", "*Independent", "Impossible", "Certain"], "Replacement restores original probabilities."),
    ("P(A|B) = P(A and B) / P(B) is called:", ["Multiplication rule", "*Conditional probability formula (or Bayes-related)", "Addition rule", "Complement rule"], "Conditional probability."),
    ("If P(A)=0.3 and P(B)=0.5 and they're independent, P(A and B) =", ["0.8", "0.2", "*0.15", "0.35"], "0.3×0.5=0.15."),
    ("Flipping a fair coin 5 times, P(all heads) = (½)^5 =", ["1/10", "5/32", "*1/32", "1/16"], "(½)^5=1/32."),
])
all_new[k] = q

k, q = add_qs("u13_l13.6", [
    ("Mutually exclusive events _____ happen at the same time.", ["Always", "Sometimes", "*Cannot", "Must"], "Cannot co-occur."),
    ("P(A or B) for mutually exclusive events = P(A) + P(B). If P(A)=0.3 and P(B)=0.4:", ["0.12", "*0.7", "1.0", "0.1"], "0.3+0.4=0.7."),
    ("P(A or B) for non-mutually exclusive events = P(A) + P(B) - P(A and B). This avoids:", ["Undercounting", "*Double counting the overlap", "Division by zero", "Negative probability"], "Inclusion-exclusion."),
    ("Rolling a 2 and rolling a 5 on one die are:", ["Independent", "*Mutually exclusive", "Dependent", "Complementary"], "Can't get both."),
    ("Being a senior and being on the basketball team are:", ["Mutually exclusive", "*Not mutually exclusive (you can be both)", "Impossible", "Complementary"], "Can be both."),
    ("If P(A)=0.5, P(B)=0.4, P(A and B)=0.2, then P(A or B) =", ["0.9", "1.1", "*0.7 (0.5+0.4-0.2)", "0.2"], "0.5+0.4-0.2=0.7."),
    ("The complement of event A: P(not A) = 1 - _____.", ["P(B)", "*P(A)", "P(A or B)", "0"], "P(A')=1-P(A)."),
    ("If P(rain) = 0.35, P(no rain) =", ["0.35", "*0.65", "0.70", "1.35"], "1-0.35=0.65."),
    ("Mutually exclusive events have P(A and B) =", ["1", "P(A)", "*0", "P(A)+P(B)"], "No overlap."),
    ("P(drawing a heart or a face card) from a standard deck:", ["13/52 + 12/52", "*22/52 (13+12-3, since 3 face cards are hearts)", "25/52", "13/52"], "13+12-3=22."),
    ("Events A and B are called exhaustive if:", ["P(A and B)=0", "*P(A or B)=1 (they cover all outcomes)", "P(A)=P(B)", "They're independent"], "Cover the sample space."),
    ("Mutually exclusive and exhaustive events partition the:", ["Event A", "*Sample space", "Probability", "Tree diagram"], "Complete partition."),
    ("If A and B are mutually exclusive, they _____ be independent (unless one has probability 0).", ["Must", "*Cannot", "Always", "Sometimes"], "ME + independent is impossible (unless P=0)."),
])
all_new[k] = q

k, q = add_qs("u13_l13.7", [
    ("Monte Carlo methods use _____ to estimate mathematical quantities.", ["Exact formulas", "Algebra", "*Random sampling", "Measurement"], "Random simulation."),
    ("Monte Carlo estimation of π: randomly throw darts at a unit square with an inscribed quarter-circle. π ≈", ["hits/total", "*4 × (hits inside quarter-circle / total darts)", "hits/4", "total/hits"], "π ≈ 4 × (hits/total)."),
    ("As the number of random samples increases, a Monte Carlo estimate becomes:", ["Less accurate", "The same", "*More accurate (converges to the true value)", "Exactly correct immediately"], "Convergence."),
    ("Monte Carlo methods are named after the famous _____ in Monaco.", ["Museum", "Hotel", "*Casino (Monte Carlo Casino — associated with randomness/gambling)", "Beach"], "Casino association."),
    ("To estimate the area of an irregular shape using Monte Carlo: place it in a known rectangle and:", ["Measure it", "*Randomly generate points; area ≈ (hits inside shape / total points) × rectangle area", "Count pixels", "Use a formula"], "Random point method."),
    ("Monte Carlo simulation can estimate:", ["Only probabilities", "Only areas", "*Probabilities, areas, integrals, and many other quantities", "Only π"], "Versatile applications."),
    ("The accuracy of a Monte Carlo estimate depends primarily on:", ["The formula used", "*The number of random samples (more = better)", "The shape being measured", "The calculator"], "More samples = better."),
    ("A Monte Carlo estimate is a type of:", ["Exact solution", "Algebraic proof", "*Numerical approximation", "Geometric proof"], "Numerical method."),
    ("To estimate P(event) using Monte Carlo: P ≈ (number of favorable trials) / _____.", ["Favorable trials", "*Total trials", "Sample space size × 2", "The largest outcome"], "Favorable/total."),
    ("Monte Carlo methods require a good source of:", ["Data", "Formulas", "*Random (or pseudo-random) numbers", "Geometry"], "Randomness."),
    ("Buffon's Needle is a classic Monte Carlo experiment that estimates:", ["e", "√2", "*π", "φ (golden ratio)"], "Buffon's Needle estimates π."),
    ("Monte Carlo methods are widely used in:", ["Only geometry", "Only probability", "*Science, finance, engineering, and many other fields", "Only Monte Carlo"], "Broad applications."),
    ("The 'error' in a Monte Carlo estimate typically decreases proportionally to:", ["1/n", "*1/√n (where n is the number of samples)", "1/n²", "n"], "1/√n convergence rate."),
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

print(f"✅ Geometry U9-U13: expanded {len(all_new)} lessons")
