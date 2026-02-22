import os
import re

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\GeometryLessons"

# All flashcard content for Units 9-13
FLASHCARDS = {
    # ===== UNIT 9: Transformations =====
    "9.1": [
        {"q": "What is a reflection?", "a": "A transformation that flips a figure over a line (line of reflection), creating a mirror image"},
        {"q": "What is the line of reflection?", "a": "The line over which a figure is reflected; every point and its image are equidistant from this line"},
        {"q": "How do you reflect a point over the x-axis?", "a": "(x, y) becomes (x, -y)"},
        {"q": "How do you reflect a point over the y-axis?", "a": "(x, y) becomes (-x, y)"},
        {"q": "How do you reflect a point over the line y = x?", "a": "(x, y) becomes (y, x)"},
        {"q": "What is preserved in a reflection?", "a": "Distance (segment lengths), angle measures, and shape — reflections are rigid motions (isometries)"},
        {"q": "What changes in a reflection?", "a": "Orientation — the order of vertices reverses (e.g., clockwise becomes counterclockwise)"},
        {"q": "How do you reflect over the line y = -x?", "a": "(x, y) becomes (-y, -x)"},
        {"q": "What is a rigid motion?", "a": "A transformation that preserves distance and angle measures — also called an isometry"},
        {"q": "What is the image?", "a": "The resulting figure after a transformation is applied; labeled with prime notation (A becomes A prime)"},
    ],
    "9.2": [
        {"q": "What is a translation?", "a": "A transformation that slides every point of a figure the same distance in the same direction"},
        {"q": "How is a translation described?", "a": "By a translation vector (a, b) which moves every point x units horizontally and y units vertically"},
        {"q": "What is the coordinate rule for a translation?", "a": "(x, y) maps to (x + a, y + b) where (a, b) is the translation vector"},
        {"q": "Is a translation a rigid motion?", "a": "Yes — it preserves distances, angles, and orientation"},
        {"q": "What does a translation preserve?", "a": "Distance, angle measures, parallelism, collinearity, and orientation"},
        {"q": "What is a translation vector?", "a": "A directed line segment that describes the direction and magnitude of the translation"},
        {"q": "How do you describe a translation from A(1,3) to A prime(4,7)?", "a": "Translation vector is (3, 4) — moved 3 right and 4 up"},
        {"q": "Can a translation change the size of a figure?", "a": "No — translations are isometries and always produce congruent figures"},
        {"q": "What is a composition of translations?", "a": "Performing two or more translations in sequence; the result is equivalent to a single translation"},
        {"q": "If you translate by (2,3) then by (1,-5), what single translation is equivalent?", "a": "Translation by (3, -2) — add the vectors component-wise"},
    ],
    "9.3": [
        {"q": "What is a rotation?", "a": "A transformation that turns a figure around a fixed point (center of rotation) by a given angle"},
        {"q": "What is the center of rotation?", "a": "The fixed point around which a figure rotates"},
        {"q": "What is the rule for a 90-degree counterclockwise rotation about the origin?", "a": "(x, y) becomes (-y, x)"},
        {"q": "What is the rule for a 180-degree rotation about the origin?", "a": "(x, y) becomes (-x, -y)"},
        {"q": "What is the rule for a 270-degree counterclockwise rotation about the origin?", "a": "(x, y) becomes (y, -x)"},
        {"q": "Is a rotation a rigid motion?", "a": "Yes — it preserves distances and angle measures"},
        {"q": "Does a rotation preserve orientation?", "a": "Yes — unlike reflections, rotations preserve orientation"},
        {"q": "What is the angle of rotation?", "a": "The number of degrees a figure is rotated; positive is counterclockwise, negative is clockwise"},
        {"q": "A 90-degree clockwise rotation is the same as what counterclockwise rotation?", "a": "A 270-degree counterclockwise rotation"},
        {"q": "What stays the same after a rotation?", "a": "Shape, size, angle measures, and the distance from each point to the center of rotation"},
    ],
    "9.4": [
        {"q": "What is a composition of transformations?", "a": "Performing two or more transformations in sequence on a figure"},
        {"q": "What is a glide reflection?", "a": "A composition of a translation (glide) followed by a reflection over a line parallel to the direction of translation"},
        {"q": "Is the order of transformations important in a composition?", "a": "Yes — different orders can produce different results (transformations are generally not commutative)"},
        {"q": "What is the result of two reflections over parallel lines?", "a": "A translation — the distance is twice the distance between the parallel lines"},
        {"q": "What is the result of two reflections over intersecting lines?", "a": "A rotation — the angle is twice the angle between the intersecting lines"},
        {"q": "Is a glide reflection a rigid motion?", "a": "Yes — it preserves distances and angle measures"},
        {"q": "Does a glide reflection preserve orientation?", "a": "No — it reverses orientation (like a single reflection)"},
        {"q": "What transformation is equivalent to three reflections?", "a": "A glide reflection (or a single reflection if the three lines are concurrent)"},
        {"q": "What is the identity transformation?", "a": "A transformation that maps every point to itself — performing a transformation and its inverse gives the identity"},
        {"q": "How do you notate a composition?", "a": "Using the circle symbol — T2 ∘ T1 means apply T1 first, then T2"},
    ],
    "9.5": [
        {"q": "What is symmetry?", "a": "A figure has symmetry if there is a rigid motion that maps the figure onto itself"},
        {"q": "What is line symmetry?", "a": "A figure has line symmetry if it can be reflected over a line and map onto itself; that line is the line of symmetry"},
        {"q": "What is rotational symmetry?", "a": "A figure has rotational symmetry if it can be rotated less than 360 degrees about its center and map onto itself"},
        {"q": "What is the order of rotational symmetry?", "a": "The number of times a figure maps onto itself during a full 360-degree rotation"},
        {"q": "What is the magnitude of rotational symmetry?", "a": "The smallest angle of rotation that maps the figure onto itself; equals 360 divided by the order"},
        {"q": "How many lines of symmetry does a regular n-gon have?", "a": "n lines of symmetry"},
        {"q": "What is the order of rotational symmetry for a regular hexagon?", "a": "6 — it maps onto itself every 60 degrees"},
        {"q": "Does a parallelogram have line symmetry?", "a": "No — but it has rotational symmetry of order 2 (180-degree rotation)"},
        {"q": "What is point symmetry?", "a": "A figure has point symmetry if it has rotational symmetry of order 2 (maps onto itself after a 180-degree rotation)"},
        {"q": "How many lines of symmetry does a circle have?", "a": "Infinitely many — every line through the center is a line of symmetry"},
    ],
    "9.6": [
        {"q": "What is a dilation?", "a": "A transformation that changes the size of a figure by a scale factor relative to a fixed center point"},
        {"q": "Is a dilation a rigid motion?", "a": "No — dilations change size, so they are not isometries (except when scale factor is 1 or -1)"},
        {"q": "What is the scale factor of a dilation?", "a": "The ratio of a length in the image to the corresponding length in the pre-image"},
        {"q": "What happens when the scale factor is greater than 1?", "a": "The image is an enlargement — larger than the original"},
        {"q": "What happens when the scale factor is between 0 and 1?", "a": "The image is a reduction — smaller than the original"},
        {"q": "What is the coordinate rule for a dilation centered at the origin with scale factor k?", "a": "(x, y) maps to (kx, ky)"},
        {"q": "What does a dilation preserve?", "a": "Angle measures, shape, and the ratio of corresponding lengths — but NOT actual distances (unless k = 1)"},
        {"q": "What type of figures does a dilation produce?", "a": "Similar figures — same shape but possibly different size"},
        {"q": "What is the center of dilation?", "a": "The fixed point from which all points are scaled; it does not move during the dilation"},
        {"q": "If the scale factor is negative, what happens?", "a": "The image is on the opposite side of the center of dilation and the figure is also flipped"},
    ],
    "9.7": [
        {"q": "How do you describe a reflection over the x-axis using coordinates?", "a": "(x, y) maps to (x, -y)"},
        {"q": "How do you describe a 90-degree CCW rotation using coordinates?", "a": "(x, y) maps to (-y, x)"},
        {"q": "How do you describe a translation using coordinates?", "a": "(x, y) maps to (x + a, y + b) for translation vector (a, b)"},
        {"q": "How do you describe a dilation centered at origin using coordinates?", "a": "(x, y) maps to (kx, ky) where k is the scale factor"},
        {"q": "What is a similarity transformation?", "a": "A composition of rigid motions and dilations — produces similar figures"},
        {"q": "How do you determine if a transformation is rigid from coordinates?", "a": "Check if distances between all pairs of points are preserved"},
        {"q": "What coordinate rule represents a reflection over y = x?", "a": "(x, y) maps to (y, x)"},
        {"q": "How do you find the center of rotation from a pre-image and image?", "a": "Find the perpendicular bisectors of segments connecting corresponding points; their intersection is the center"},
        {"q": "What is the relationship between congruence and rigid motions?", "a": "Two figures are congruent if and only if one can be mapped to the other by a sequence of rigid motions"},
        {"q": "What is the relationship between similarity and transformations?", "a": "Two figures are similar if and only if one can be mapped to the other by a similarity transformation"},
    ],

    # ===== UNIT 10: Circles =====
    "10.1": [
        {"q": "What is a circle?", "a": "The set of all points in a plane that are a given distance (radius) from a given point (center)"},
        {"q": "What is the radius?", "a": "A segment from the center of a circle to any point on the circle"},
        {"q": "What is a diameter?", "a": "A chord that passes through the center of the circle; its length is twice the radius"},
        {"q": "What is the circumference?", "a": "The distance around a circle; C = 2 pi r or C = pi d"},
        {"q": "What is a chord?", "a": "A segment whose endpoints are both on the circle"},
        {"q": "What is a secant?", "a": "A line that intersects a circle at exactly two points"},
        {"q": "What is a tangent?", "a": "A line that intersects a circle at exactly one point (the point of tangency)"},
        {"q": "What is pi?", "a": "The ratio of a circle circumference to its diameter; approximately 3.14159"},
        {"q": "Are all circles similar?", "a": "Yes — all circles are similar because any circle can be mapped to any other by a dilation"},
        {"q": "What are concentric circles?", "a": "Circles that share the same center but have different radii"},
    ],
    "10.2": [
        {"q": "What is a central angle?", "a": "An angle whose vertex is at the center of the circle"},
        {"q": "What is an arc?", "a": "A portion of a circle between two points"},
        {"q": "What is a minor arc?", "a": "An arc that measures less than 180 degrees; named by its two endpoints"},
        {"q": "What is a major arc?", "a": "An arc that measures greater than 180 degrees; named by three points"},
        {"q": "What is a semicircle?", "a": "An arc that measures exactly 180 degrees — half the circle"},
        {"q": "How is the measure of a minor arc related to its central angle?", "a": "The measure of a minor arc equals the measure of its central angle"},
        {"q": "What is the Arc Addition Postulate?", "a": "The measure of an arc formed by two adjacent arcs equals the sum of the measures of the two arcs"},
        {"q": "What are congruent arcs?", "a": "Arcs that have the same measure and are in the same circle or congruent circles"},
        {"q": "How many degrees are in a full circle?", "a": "360 degrees"},
        {"q": "What is arc length?", "a": "The linear distance along an arc; arc length = (central angle / 360) times 2 pi r"},
    ],
    "10.3": [
        {"q": "What theorem relates congruent chords to congruent arcs?", "a": "In a circle, two chords are congruent if and only if their corresponding arcs are congruent"},
        {"q": "What happens when a diameter is perpendicular to a chord?", "a": "It bisects the chord and its arc"},
        {"q": "What is the relationship between distance from center and chord length?", "a": "Two chords are congruent if and only if they are equidistant from the center"},
        {"q": "If two chords intersect inside a circle, what is true?", "a": "The products of their segments are equal: AE times EB equals CE times ED"},
        {"q": "What is the perpendicular bisector of a chord?", "a": "It passes through the center of the circle"},
        {"q": "How can you find the center of a circle using chords?", "a": "Find the perpendicular bisectors of two non-parallel chords; their intersection is the center"},
        {"q": "Are congruent chords equidistant from the center?", "a": "Yes — in the same circle or congruent circles, congruent chords are equidistant from the center"},
        {"q": "What happens when two chords are equidistant from center?", "a": "They are congruent"},
        {"q": "If a chord is a diameter, what can you say about the arcs?", "a": "A diameter divides the circle into two semicircles of 180 degrees each"},
        {"q": "What is the longest chord in a circle?", "a": "The diameter"},
    ],
    "10.4": [
        {"q": "What is an inscribed angle?", "a": "An angle formed by two chords that share an endpoint on the circle"},
        {"q": "What is the Inscribed Angle Theorem?", "a": "An inscribed angle is half the measure of its intercepted arc"},
        {"q": "What is an intercepted arc?", "a": "The arc that lies between the two sides of an inscribed angle"},
        {"q": "If two inscribed angles intercept the same arc, what is true?", "a": "They are congruent"},
        {"q": "What is the measure of an inscribed angle that intercepts a semicircle?", "a": "90 degrees — it is a right angle"},
        {"q": "What is an inscribed polygon?", "a": "A polygon whose vertices all lie on a circle"},
        {"q": "What is a circumscribed circle?", "a": "A circle that passes through all vertices of an inscribed polygon"},
        {"q": "If a quadrilateral is inscribed in a circle, what is true about opposite angles?", "a": "Opposite angles are supplementary (sum to 180 degrees)"},
        {"q": "What is the relationship between a central angle and an inscribed angle intercepting the same arc?", "a": "The central angle is twice the inscribed angle"},
        {"q": "Can a right triangle be inscribed in a semicircle?", "a": "Yes — Thales theorem states that any triangle inscribed in a semicircle with the diameter as one side is a right triangle"},
    ],
    "10.5": [
        {"q": "What is a tangent line to a circle?", "a": "A line in the plane of a circle that intersects the circle at exactly one point"},
        {"q": "What is the point of tangency?", "a": "The single point where a tangent line touches the circle"},
        {"q": "What is the relationship between a tangent and a radius at the point of tangency?", "a": "They are perpendicular"},
        {"q": "What are tangent segments from an external point?", "a": "Two tangent segments drawn from the same external point to a circle are congruent"},
        {"q": "What is a circumscribed polygon?", "a": "A polygon whose sides are all tangent to a circle"},
        {"q": "What is an inscribed circle?", "a": "A circle that is tangent to every side of a polygon"},
        {"q": "How do you determine if a line is tangent to a circle?", "a": "Test if the line is perpendicular to the radius at the point of intersection and touches the circle at exactly one point"},
        {"q": "What is a common tangent?", "a": "A line that is tangent to two circles"},
        {"q": "What is a common internal tangent?", "a": "A common tangent that intersects the segment connecting the centers of two circles"},
        {"q": "What is a common external tangent?", "a": "A common tangent that does not intersect the segment connecting the centers of two circles"},
    ],
    "10.6": [
        {"q": "What is the angle formed by two secants from an external point?", "a": "Half the difference of the intercepted arcs"},
        {"q": "What is the angle formed by a secant and a tangent from an external point?", "a": "Half the difference of the intercepted arcs"},
        {"q": "What is the angle formed by two tangents from an external point?", "a": "Half the difference of the intercepted arcs (major minus minor)"},
        {"q": "What is the angle formed by two chords intersecting inside a circle?", "a": "Half the sum of the intercepted arcs"},
        {"q": "What is the angle formed by a tangent and a chord?", "a": "Half the measure of the intercepted arc"},
        {"q": "If two secants intersect inside a circle, how do you find the angle?", "a": "Angle equals half the sum of the two intercepted arcs"},
        {"q": "If two secants intersect outside a circle, how do you find the angle?", "a": "Angle equals half the absolute difference of the two intercepted arcs"},
        {"q": "What is the angle formed by a tangent-tangent angle from outside?", "a": "Half the difference of the major arc and minor arc"},
        {"q": "If a tangent and secant form a 35-degree angle, and the near arc is 40 degrees, what is the far arc?", "a": "110 degrees — since 35 = (far - near)/2, so 70 = far - 40, far = 110"},
        {"q": "What angle does a tangent make with the diameter at the point of tangency?", "a": "90 degrees"},
    ],
    "10.7": [
        {"q": "What is the Intersecting Chords theorem?", "a": "If two chords intersect inside a circle, the products of their segments are equal: AE times EB = CE times ED"},
        {"q": "What is the Secant-Secant theorem for external points?", "a": "If two secants are drawn from an external point, then (whole)(external) = (whole)(external) for each secant"},
        {"q": "What is the Secant-Tangent theorem?", "a": "If a secant and tangent are drawn from an external point, then tangent squared = (whole secant)(external segment)"},
        {"q": "What is the Power of a Point theorem?", "a": "A unified theorem: for any line through a point and a circle, the product of signed distances to the intersection points is constant"},
        {"q": "Two chords intersect inside a circle. One has segments 3 and 8. The other has a segment of 4. What is the missing segment?", "a": "6 — because 3 times 8 = 4 times x, so x = 6"},
        {"q": "A tangent from point P has length 6. A secant from P has external segment 3. What is the whole secant?", "a": "12 — because 6 squared = 3 times whole, so whole = 36/3 = 12"},
        {"q": "What is the external segment of a secant?", "a": "The part of the secant that lies outside the circle, from the external point to the nearer intersection"},
        {"q": "What is a secant segment?", "a": "The entire segment from the external point through the circle — it includes both the external segment and the chord portion"},
        {"q": "How do you find the length of a tangent from an external point?", "a": "Use the Pythagorean theorem with the radius and the distance from the external point to the center"},
        {"q": "Can the Power of a Point be negative?", "a": "It can be considered signed: negative when the point is inside the circle, positive when outside, and zero when on the circle"},
    ],
    "10.8": [
        {"q": "What is the standard form equation of a circle?", "a": "(x - h) squared + (y - k) squared = r squared, where (h, k) is the center and r is the radius"},
        {"q": "What is the equation of a circle centered at the origin?", "a": "x squared + y squared = r squared"},
        {"q": "How do you find the center and radius from (x - 3) squared + (y + 2) squared = 25?", "a": "Center is (3, -2) and radius is 5"},
        {"q": "What is the general form of a circle equation?", "a": "x squared + y squared + Dx + Ey + F = 0"},
        {"q": "How do you convert general form to standard form?", "a": "Complete the square for both x and y terms"},
        {"q": "How do you write the equation of a circle given the center (2, -1) and radius 4?", "a": "(x - 2) squared + (y + 1) squared = 16"},
        {"q": "How do you find the equation of a circle given a diameter with endpoints (1, 3) and (5, 7)?", "a": "Center is the midpoint (3, 5), radius is half the diameter length; find distance and divide by 2"},
        {"q": "What is completing the square?", "a": "A method to rewrite a quadratic expression as a perfect square plus a constant — used to convert circle equations"},
        {"q": "If a point satisfies the circle equation, where is it?", "a": "On the circle"},
        {"q": "If (x - h) squared + (y - k) squared is less than r squared, where is the point?", "a": "Inside the circle"},
    ],
    "10.9": [
        {"q": "What are conic sections?", "a": "Curves formed by the intersection of a plane with a double-napped cone: circles, ellipses, parabolas, and hyperbolas"},
        {"q": "What is an ellipse?", "a": "The set of all points such that the sum of distances from two fixed points (foci) is constant"},
        {"q": "What is a parabola?", "a": "The set of all points equidistant from a fixed point (focus) and a fixed line (directrix)"},
        {"q": "What is a hyperbola?", "a": "The set of all points such that the absolute difference of distances from two foci is constant"},
        {"q": "How is a circle a special case of an ellipse?", "a": "A circle is an ellipse where both foci coincide at the center (eccentricity = 0)"},
        {"q": "What determines which conic section is formed?", "a": "The angle at which the plane intersects the cone"},
        {"q": "What is the eccentricity of a circle?", "a": "0 — a circle has no elongation"},
        {"q": "What is the eccentricity of a parabola?", "a": "Exactly 1"},
        {"q": "What is the standard form of an ellipse centered at the origin?", "a": "x squared over a squared plus y squared over b squared equals 1"},
        {"q": "What is the standard form of a parabola opening upward?", "a": "x squared = 4py, where p is the distance from vertex to focus"},
    ],

    # ===== UNIT 11: Area =====
    "11.1": [
        {"q": "What is the formula for the area of a parallelogram?", "a": "A = bh, where b is the base and h is the height (perpendicular distance between bases)"},
        {"q": "What is the formula for the area of a triangle?", "a": "A = (1/2)bh, where b is the base and h is the height"},
        {"q": "Why is the area of a triangle half the area of a parallelogram?", "a": "A diagonal of a parallelogram divides it into two congruent triangles"},
        {"q": "What is the height of a parallelogram?", "a": "The perpendicular distance between the two parallel bases — NOT the slant side"},
        {"q": "Can any side of a triangle be used as the base?", "a": "Yes — the height is the perpendicular distance from the opposite vertex to the chosen base (or its extension)"},
        {"q": "What is the area of a triangle with base 10 and height 6?", "a": "30 square units — A = (1/2)(10)(6)"},
        {"q": "What is the area formula using two sides and included angle?", "a": "A = (1/2)ab sin C, where a and b are side lengths and C is the included angle"},
        {"q": "What units are used for area?", "a": "Square units (square cm, square m, square ft, etc.)"},
        {"q": "What is the area of a parallelogram with base 8 and height 5?", "a": "40 square units — A = 8 times 5"},
        {"q": "How do you find the height of a triangle given its area and base?", "a": "h = 2A / b"},
    ],
    "11.2": [
        {"q": "What is the formula for the area of a trapezoid?", "a": "A = (1/2)(b1 + b2)h, where b1 and b2 are the parallel bases and h is the height"},
        {"q": "What is the formula for the area of a rhombus?", "a": "A = (1/2)d1 times d2, where d1 and d2 are the diagonals"},
        {"q": "What is the formula for the area of a kite?", "a": "A = (1/2)d1 times d2, where d1 and d2 are the diagonals"},
        {"q": "Why do rhombi and kites use the same area formula?", "a": "Both have perpendicular diagonals, so the area formula based on diagonals applies to both"},
        {"q": "What are the bases of a trapezoid?", "a": "The two parallel sides"},
        {"q": "What is the height of a trapezoid?", "a": "The perpendicular distance between the two parallel bases"},
        {"q": "Find the area of a trapezoid with bases 6 and 10, height 4.", "a": "32 square units — A = (1/2)(6 + 10)(4)"},
        {"q": "Find the area of a rhombus with diagonals 8 and 12.", "a": "48 square units — A = (1/2)(8)(12)"},
        {"q": "What is the median of a trapezoid?", "a": "A segment connecting the midpoints of the non-parallel sides; its length is the average of the two bases"},
        {"q": "How can you compute a trapezoid area using the median?", "a": "Area = median times height, since median = (b1 + b2)/2"},
    ],
    "11.3": [
        {"q": "What is the formula for the area of a circle?", "a": "A = pi r squared"},
        {"q": "What is a sector?", "a": "A region bounded by two radii and an arc of the circle — like a slice of pie"},
        {"q": "What is the formula for the area of a sector?", "a": "A = (central angle / 360) times pi r squared"},
        {"q": "What is arc length?", "a": "The linear distance along an arc; L = (central angle / 360) times 2 pi r"},
        {"q": "What is a segment of a circle?", "a": "The region between a chord and its intercepted arc"},
        {"q": "How do you find the area of a segment?", "a": "Area of the sector minus the area of the triangle formed by the two radii and the chord"},
        {"q": "What is the area of a circle with radius 7?", "a": "49 pi or approximately 153.94 square units"},
        {"q": "Find the area of a sector with central angle 90 degrees and radius 10.", "a": "25 pi or approximately 78.54 square units"},
        {"q": "What is the area of a semicircle with diameter 12?", "a": "18 pi or approximately 56.55 square units (radius = 6, area = pi(36)/2)"},
        {"q": "What fraction of a circle area is a 60-degree sector?", "a": "1/6 of the total area"},
    ],
    "11.4": [
        {"q": "What is a regular polygon?", "a": "A polygon that is both equilateral (all sides equal) and equiangular (all angles equal)"},
        {"q": "What is the apothem?", "a": "The perpendicular distance from the center of a regular polygon to the midpoint of a side"},
        {"q": "What is the formula for the area of a regular polygon?", "a": "A = (1/2)aP, where a is the apothem and P is the perimeter"},
        {"q": "What is a composite figure?", "a": "A figure made up of two or more simpler geometric shapes"},
        {"q": "How do you find the area of a composite figure?", "a": "Break it into non-overlapping simple shapes, find each area, and add (or subtract) them"},
        {"q": "What is the central angle of a regular n-gon?", "a": "360/n degrees"},
        {"q": "How do you find the apothem of a regular hexagon with side 6?", "a": "a = 3 times the square root of 3, approximately 5.196 — using 30-60-90 triangle properties"},
        {"q": "Find the area of a regular hexagon with side length 4.", "a": "24 times the square root of 3, approximately 41.57 square units"},
        {"q": "What is the interior angle of a regular pentagon?", "a": "108 degrees — from the formula (n-2)(180)/n = (3)(180)/5"},
        {"q": "How does increasing the number of sides of a regular polygon affect its shape?", "a": "It becomes closer and closer to a circle"},
    ],
    "11.5": [
        {"q": "How are the areas of similar figures related?", "a": "The ratio of their areas is the square of the scale factor"},
        {"q": "If the scale factor of two similar figures is 3, what is the ratio of their areas?", "a": "9 (which is 3 squared)"},
        {"q": "If two similar triangles have areas 8 and 32, what is the scale factor?", "a": "1 to 2 — since 32/8 = 4, and the square root of 4 is 2"},
        {"q": "If corresponding sides are in ratio 2:5, what is the area ratio?", "a": "4:25"},
        {"q": "A rectangle is 3 by 5. A similar rectangle has a scale factor of 4. What is the area of the larger?", "a": "240 square units — original area 15 times 4 squared = 15 times 16"},
        {"q": "How are the perimeters of similar figures related?", "a": "The ratio of their perimeters equals the scale factor (linear, not squared)"},
        {"q": "If the area ratio of two similar pentagons is 9:49, what is their scale factor?", "a": "3:7 — take the square root of the area ratio"},
        {"q": "Does the area ratio apply to all similar figures, not just triangles?", "a": "Yes — the area ratio equals the square of the scale factor for any pair of similar figures"},
        {"q": "If one triangle has sides twice as long as another similar triangle, how do the areas compare?", "a": "The larger triangle area is 4 times the smaller (2 squared = 4)"},
        {"q": "How do you find a missing side given areas of similar figures?", "a": "Find the area ratio, take the square root to get the scale factor, then multiply"},
    ],
    "11.6": [
        {"q": "What is integration in the context of area?", "a": "A calculus technique that sums infinitely thin slices to find the exact area under a curve or of an irregular region"},
        {"q": "How does integration relate to geometry?", "a": "It generalizes area formulas to curved boundaries — the area under y = f(x) from a to b is the integral of f(x) dx"},
        {"q": "What is a Riemann sum?", "a": "An approximation of area using rectangles of finite width; as width approaches zero, it approaches the integral"},
        {"q": "How can you approximate the area of an irregular shape without calculus?", "a": "Use a grid overlay and count squares, or break the shape into triangles and other known shapes"},
        {"q": "What is the trapezoidal rule?", "a": "An approximation method that uses trapezoids instead of rectangles for better accuracy"},
        {"q": "How does doubling the number of rectangles in a Riemann sum affect accuracy?", "a": "It generally improves the approximation and brings it closer to the true area"},
        {"q": "What is the area under y = x from x = 0 to x = 4?", "a": "8 square units — the region is a triangle with base 4 and height 4, area = (1/2)(4)(4)"},
        {"q": "What is the connection between pi and integration?", "a": "The area formula A = pi r squared can be derived by integrating the area of infinitely thin circular rings"},
        {"q": "What does the fundamental theorem of calculus state about area?", "a": "The definite integral of a function gives the net signed area between the function and the x-axis"},
        {"q": "What is Cavalieri Principle for area?", "a": "If two regions have the same cross-sectional length at every height, they have the same area"},
    ],

    # ===== UNIT 12: Surface Area and Volume =====
    "12.1": [
        {"q": "What is a polyhedron?", "a": "A three-dimensional solid with flat polygon faces, straight edges, and vertices"},
        {"q": "What is a cross section?", "a": "The intersection of a solid and a plane — the 2D shape you see when you slice through a 3D object"},
        {"q": "What is an orthographic projection?", "a": "A 2D representation showing front, top, and side views of a 3D object"},
        {"q": "What is an isometric drawing?", "a": "A 3D representation on a 2D surface using three axes at 120-degree angles to show depth"},
        {"q": "What is a net?", "a": "A two-dimensional pattern that can be folded to form a three-dimensional solid"},
        {"q": "What are the possible cross sections of a cube?", "a": "Square, rectangle, triangle, trapezoid, pentagon, and regular hexagon"},
        {"q": "What is Euler formula for polyhedra?", "a": "V - E + F = 2, where V = vertices, E = edges, F = faces"},
        {"q": "What cross section do you get when you cut a cylinder parallel to its base?", "a": "A circle"},
        {"q": "What cross section do you get when you cut a cone perpendicular to its base through the apex?", "a": "A triangle (specifically an isosceles triangle)"},
        {"q": "What is the difference between a prism and a pyramid?", "a": "A prism has two congruent parallel bases; a pyramid has one base and an apex"},
    ],
    "12.2": [
        {"q": "What is the surface area of a prism?", "a": "SA = 2B + Ph, where B is the base area, P is the base perimeter, and h is the height"},
        {"q": "What is the lateral surface area of a prism?", "a": "LA = Ph, where P is the base perimeter and h is the height"},
        {"q": "What is the surface area of a cylinder?", "a": "SA = 2 pi r squared + 2 pi r h"},
        {"q": "What is the lateral surface area of a cylinder?", "a": "LA = 2 pi r h — the rectangle you get when you unroll the curved surface"},
        {"q": "What is a right prism?", "a": "A prism where the lateral faces are rectangles perpendicular to the bases"},
        {"q": "What is an oblique prism?", "a": "A prism where the lateral faces are parallelograms and are not perpendicular to the bases"},
        {"q": "Find the surface area of a cylinder with radius 3 and height 10.", "a": "78 pi or approximately 245.04 sq units — SA = 2 pi(9) + 2 pi(3)(10)"},
        {"q": "Find the lateral area of a rectangular prism 4 by 5 by 6.", "a": "148 sq units — wait, LA = P times h. If base is 4 by 5, P = 18, h = 6, LA = 108. Total SA = 2(20) + 108 = 148"},
        {"q": "What shape is the lateral surface of a cylinder when unrolled?", "a": "A rectangle with width equal to the circumference and height equal to the cylinder height"},
        {"q": "What is the difference between surface area and lateral area?", "a": "Surface area includes all faces; lateral area excludes the bases"},
    ],
    "12.3": [
        {"q": "What is the surface area of a pyramid?", "a": "SA = B + (1/2)Pl, where B is the base area, P is the base perimeter, and l is the slant height"},
        {"q": "What is the lateral surface area of a pyramid?", "a": "LA = (1/2)Pl, where P is the base perimeter and l is the slant height"},
        {"q": "What is the surface area of a cone?", "a": "SA = pi r squared + pi r l, where r is the radius and l is the slant height"},
        {"q": "What is the lateral surface area of a cone?", "a": "LA = pi r l"},
        {"q": "What is the slant height?", "a": "The distance from the apex to the midpoint of a base edge (pyramid) or to a point on the base circle (cone)"},
        {"q": "How do you find slant height from height and radius of a cone?", "a": "Using the Pythagorean theorem: l = square root of (r squared + h squared)"},
        {"q": "What is a regular pyramid?", "a": "A pyramid whose base is a regular polygon and whose lateral faces are congruent isosceles triangles"},
        {"q": "Find the lateral area of a cone with radius 5 and slant height 13.", "a": "65 pi or approximately 204.2 square units"},
        {"q": "What is the apex of a pyramid or cone?", "a": "The single vertex point at the top, opposite the base"},
        {"q": "What shape does the lateral surface of a cone form when unrolled?", "a": "A sector of a circle"},
    ],
    "12.4": [
        {"q": "What is the formula for the volume of a prism?", "a": "V = Bh, where B is the area of the base and h is the height"},
        {"q": "What is the formula for the volume of a cylinder?", "a": "V = pi r squared h"},
        {"q": "What does volume measure?", "a": "The amount of space a three-dimensional figure occupies, measured in cubic units"},
        {"q": "What is the volume of a rectangular prism 3 by 4 by 5?", "a": "60 cubic units — V = 3 times 4 times 5"},
        {"q": "What is the volume of a cylinder with radius 6 and height 10?", "a": "360 pi or approximately 1130.97 cubic units"},
        {"q": "Does the volume formula for prisms work for oblique prisms?", "a": "Yes — by Cavalieri Principle, oblique and right prisms with equal bases and heights have the same volume"},
        {"q": "What units are used for volume?", "a": "Cubic units (cubic cm, cubic m, cubic ft, etc.)"},
        {"q": "How do you find the height of a cylinder given volume and radius?", "a": "h = V / (pi r squared)"},
        {"q": "If you double the radius of a cylinder, what happens to the volume?", "a": "The volume quadruples (multiplied by 4) because radius is squared in the formula"},
        {"q": "If you double the height of a prism, what happens to the volume?", "a": "The volume doubles"},
    ],
    "12.5": [
        {"q": "What is the formula for the volume of a pyramid?", "a": "V = (1/3)Bh, where B is the area of the base and h is the height"},
        {"q": "What is the formula for the volume of a cone?", "a": "V = (1/3) pi r squared h"},
        {"q": "Why is the volume of a pyramid one-third the volume of a prism with the same base and height?", "a": "Three pyramids of the same base and height can be fitted together to form a prism"},
        {"q": "What is the volume of a cone with radius 3 and height 7?", "a": "21 pi or approximately 65.97 cubic units"},
        {"q": "What is the volume of a square pyramid with base side 6 and height 9?", "a": "108 cubic units — V = (1/3)(36)(9)"},
        {"q": "How do you find the height of a cone given volume and radius?", "a": "h = 3V / (pi r squared)"},
        {"q": "If the radius and height of a cone are both doubled, how does the volume change?", "a": "The volume is multiplied by 8 (2 squared times 2 = 8)"},
        {"q": "What is a right cone?", "a": "A cone where the apex is directly above the center of the circular base"},
        {"q": "Does the 1/3 factor apply to oblique pyramids and cones?", "a": "Yes — Cavalieri Principle ensures the volume formula works for oblique versions too"},
        {"q": "How does a pyramid volume compare to a cube with the same base and height?", "a": "The pyramid volume is exactly one-third the cube volume"},
    ],
    "12.6": [
        {"q": "What is the surface area of a sphere?", "a": "SA = 4 pi r squared"},
        {"q": "What is the volume of a sphere?", "a": "V = (4/3) pi r cubed"},
        {"q": "What is a great circle?", "a": "A cross section of a sphere that passes through its center — the largest possible circle on the sphere"},
        {"q": "What is a hemisphere?", "a": "Half of a sphere, divided by a great circle"},
        {"q": "What is the volume of a hemisphere?", "a": "(2/3) pi r cubed"},
        {"q": "What is the surface area of a hemisphere including the base?", "a": "3 pi r squared — curved surface (2 pi r squared) plus the flat base (pi r squared)"},
        {"q": "Find the volume of a sphere with radius 6.", "a": "288 pi or approximately 904.78 cubic units"},
        {"q": "Find the surface area of a sphere with radius 5.", "a": "100 pi or approximately 314.16 square units"},
        {"q": "If the radius of a sphere triples, how does the volume change?", "a": "The volume is multiplied by 27 (3 cubed)"},
        {"q": "How does the surface area of a sphere relate to the area of a great circle?", "a": "The surface area is exactly 4 times the area of a great circle"},
    ],
    "12.7": [
        {"q": "What is spherical geometry?", "a": "Geometry on the surface of a sphere, where lines are great circles and many Euclidean postulates do not hold"},
        {"q": "What replaces lines in spherical geometry?", "a": "Great circles — they are the shortest paths (geodesics) between two points on a sphere"},
        {"q": "Do parallel lines exist in spherical geometry?", "a": "No — any two great circles on a sphere always intersect at exactly two points"},
        {"q": "What is the sum of angles in a spherical triangle?", "a": "Greater than 180 degrees and less than 540 degrees"},
        {"q": "What is a geodesic?", "a": "The shortest path between two points on a curved surface — on a sphere, geodesics are arcs of great circles"},
        {"q": "How does spherical geometry differ from Euclidean geometry?", "a": "Parallel postulate fails, angle sums differ, and lines (great circles) always intersect"},
        {"q": "What is the spherical excess?", "a": "The amount by which the angle sum of a spherical triangle exceeds 180 degrees"},
        {"q": "What is a lune?", "a": "A region on a sphere bounded by two great semicircles — shaped like a lens"},
        {"q": "What is the area of a spherical triangle?", "a": "A = R squared times E, where E is the spherical excess in radians and R is the sphere radius"},
        {"q": "Where is spherical geometry used in real life?", "a": "Navigation, astronomy, GPS, and mapping the Earth surface — Earth is approximately a sphere"},
    ],
    "12.8": [
        {"q": "When are two solids congruent?", "a": "When they have exactly the same shape and size — all corresponding measurements are equal"},
        {"q": "When are two solids similar?", "a": "When they have the same shape but possibly different sizes — corresponding linear measurements are proportional"},
        {"q": "If two similar solids have scale factor k, what is the ratio of their surface areas?", "a": "k squared"},
        {"q": "If two similar solids have scale factor k, what is the ratio of their volumes?", "a": "k cubed"},
        {"q": "Two similar cylinders have radii 2 and 6. What is the ratio of their volumes?", "a": "1:27 — scale factor is 1:3, so volume ratio is 1:27"},
        {"q": "Two similar prisms have surface areas 50 and 200. What is the scale factor?", "a": "1:2 — area ratio is 1:4, so scale factor is square root = 1:2"},
        {"q": "If a model car is 1/24 scale, how does its volume compare to the real car?", "a": "The volume is 1/13824 of the real car (24 cubed = 13824)"},
        {"q": "How do you find the scale factor from a volume ratio?", "a": "Take the cube root of the volume ratio"},
        {"q": "How do you find the scale factor from a surface area ratio?", "a": "Take the square root of the surface area ratio"},
        {"q": "If two similar cones have heights 5 and 15, what is the ratio of their surface areas?", "a": "1:9 — scale factor is 1:3, surface area ratio is (1:3) squared = 1:9"},
    ],
    "12.9": [
        {"q": "What is Cavalieri Principle?", "a": "If two solids have the same height and the same cross-sectional area at every level, they have the same volume"},
        {"q": "How does Cavalieri Principle prove the volume of an oblique cylinder?", "a": "An oblique cylinder has the same cross-sections as a right cylinder at every height, so they have equal volumes"},
        {"q": "What is a practical example of Cavalieri Principle?", "a": "A stack of coins — tilting the stack does not change the total volume"},
        {"q": "How does Cavalieri Principle relate to the volume of a sphere?", "a": "By comparing cross-sections of a sphere with those of a cylinder minus a cone, we can derive V = (4/3) pi r cubed"},
        {"q": "What is the key condition for Cavalieri Principle?", "a": "Equal cross-sectional areas at every corresponding height between the two solids"},
        {"q": "Can Cavalieri Principle be used in 2D?", "a": "Yes — if two 2D regions have equal widths at every height, they have the same area"},
        {"q": "How do you use Cavalieri Principle to compare a prism and an oblique prism?", "a": "Both have identical cross-sections at every height, so they have equal volumes regardless of tilt"},
        {"q": "What is the method of disks in calculus?", "a": "A technique that uses Cavalieri Principle by summing the volumes of infinitely thin circular cross-sections"},
        {"q": "How does Cavalieri Principle help with pyramids?", "a": "Two pyramids with the same base area and height have equal volumes because their cross-sections at each height are proportional"},
        {"q": "Who was Cavalieri?", "a": "Bonaventura Cavalieri, a 17th-century Italian mathematician who formalized the principle before integral calculus was developed"},
    ],

    # ===== UNIT 13: Probability and Statistics in Geometry =====
    "13.1": [
        {"q": "What is a sample space?", "a": "The set of all possible outcomes of an experiment"},
        {"q": "How can you represent a sample space?", "a": "Using lists, tables, tree diagrams, or organized counting methods"},
        {"q": "What is an outcome?", "a": "A single result from an experiment"},
        {"q": "What is an event?", "a": "A subset of the sample space — one or more outcomes"},
        {"q": "What is a tree diagram?", "a": "A branching diagram that shows all possible outcomes of sequential events"},
        {"q": "What is the Fundamental Counting Principle?", "a": "If event A has m outcomes and event B has n outcomes, then A followed by B has m times n outcomes"},
        {"q": "How many outcomes are there when flipping 3 coins?", "a": "8 — since 2 times 2 times 2 = 8"},
        {"q": "What is the sample space for rolling two dice?", "a": "36 ordered pairs — (1,1), (1,2), ..., (6,6)"},
        {"q": "What is a uniform sample space?", "a": "One where all outcomes are equally likely"},
        {"q": "What is a compound event?", "a": "An event that consists of two or more simple events"},
    ],
    "13.2": [
        {"q": "What is a permutation?", "a": "An arrangement of objects in a specific order — order matters"},
        {"q": "What is a combination?", "a": "A selection of objects where order does not matter"},
        {"q": "What is the formula for permutations?", "a": "P(n, r) = n! / (n - r)!"},
        {"q": "What is the formula for combinations?", "a": "C(n, r) = n! / [r!(n - r)!]"},
        {"q": "What is n factorial (n!)?", "a": "The product of all positive integers from 1 to n; for example, 5! = 120"},
        {"q": "What is 0 factorial?", "a": "1 — by definition, 0! = 1"},
        {"q": "How many ways can 5 books be arranged on a shelf?", "a": "120 — this is 5! = 5 times 4 times 3 times 2 times 1"},
        {"q": "How many ways can a committee of 3 be chosen from 10 people?", "a": "120 — C(10,3) = 10! / (3! times 7!) = 120"},
        {"q": "When do you use permutations vs combinations?", "a": "Permutations when order matters (rankings, arrangements); combinations when order does not (selections, groups)"},
        {"q": "What is P(6, 2)?", "a": "30 — P(6,2) = 6! / 4! = 6 times 5 = 30"},
    ],
    "13.3": [
        {"q": "What is geometric probability?", "a": "Probability determined by comparing geometric measures (lengths, areas, volumes) rather than counting outcomes"},
        {"q": "How do you find geometric probability using lengths?", "a": "P = favorable length / total length"},
        {"q": "How do you find geometric probability using areas?", "a": "P = favorable area / total area"},
        {"q": "A dart is thrown randomly at a square board with side 10. A circle of radius 3 is inside. What is P(hitting the circle)?", "a": "9 pi / 100, approximately 0.283 or 28.3 percent"},
        {"q": "What is the probability of landing on a specific sector of a spinner?", "a": "The central angle of the sector divided by 360 degrees"},
        {"q": "A bus arrives randomly between 3:00 and 3:30. You arrive at 3:10. P(waiting less than 5 min)?", "a": "5/20 = 1/4 or 25 percent (favorable = 5 min window out of remaining 20 min)"},
        {"q": "How does geometric probability differ from classical probability?", "a": "Classical probability counts discrete outcomes; geometric probability measures continuous regions"},
        {"q": "What assumption underlies geometric probability?", "a": "Points are equally likely to land anywhere in the total region (uniform distribution)"},
        {"q": "Can geometric probability use volumes?", "a": "Yes — for 3D situations, P = favorable volume / total volume"},
        {"q": "A target has 3 concentric rings with radii 1, 2, 3. What is P(hitting the innermost ring)?", "a": "pi(1) squared / pi(3) squared = 1/9, approximately 11.1 percent"},
    ],
    "13.4": [
        {"q": "What is a simulation?", "a": "A model of a real-world situation used to estimate probabilities when theoretical calculation is difficult"},
        {"q": "What is a random number generator?", "a": "A tool that produces numbers with no predictable pattern, used to model random events in simulations"},
        {"q": "How do you design a simulation?", "a": "Define the problem, assign numbers to outcomes, run many trials, and analyze the results"},
        {"q": "What is a trial in a simulation?", "a": "One complete run of the simulated experiment"},
        {"q": "Why are simulations useful?", "a": "They can estimate probabilities for complex situations where theoretical calculation is impractical"},
        {"q": "How does increasing the number of trials affect a simulation?", "a": "Results become more reliable and closer to the theoretical probability (Law of Large Numbers)"},
        {"q": "What is the Law of Large Numbers?", "a": "As the number of trials increases, the experimental probability approaches the theoretical probability"},
        {"q": "How can you simulate flipping a coin?", "a": "Use odd/even random numbers, or 0/1 from a random number generator"},
        {"q": "How can you simulate rolling a die?", "a": "Generate random integers from 1 to 6"},
        {"q": "What is experimental probability?", "a": "The ratio of the number of times an event occurs to the total number of trials performed"},
    ],
    "13.5": [
        {"q": "What are independent events?", "a": "Events where the occurrence of one does not affect the probability of the other"},
        {"q": "What are dependent events?", "a": "Events where the occurrence of one changes the probability of the other"},
        {"q": "What is the formula for P(A and B) for independent events?", "a": "P(A and B) = P(A) times P(B)"},
        {"q": "What is the formula for P(A and B) for dependent events?", "a": "P(A and B) = P(A) times P(B given A)"},
        {"q": "What is conditional probability?", "a": "The probability of event B occurring given that event A has already occurred: P(B|A)"},
        {"q": "Are drawing cards with replacement independent or dependent?", "a": "Independent — the probabilities do not change between draws"},
        {"q": "Are drawing cards without replacement independent or dependent?", "a": "Dependent — the probabilities change after each draw"},
        {"q": "P(red card) from a standard deck on two draws with replacement?", "a": "(26/52) times (26/52) = 1/4"},
        {"q": "What is the multiplication rule?", "a": "P(A and B) = P(A) times P(B|A) for any events; simplifies to P(A) times P(B) when independent"},
        {"q": "How do you test if events are independent?", "a": "Check if P(A and B) = P(A) times P(B)"},
    ],
    "13.6": [
        {"q": "What are mutually exclusive events?", "a": "Events that cannot occur at the same time — their intersection is empty"},
        {"q": "What is the Addition Rule for mutually exclusive events?", "a": "P(A or B) = P(A) + P(B)"},
        {"q": "What is the Addition Rule for non-mutually exclusive events?", "a": "P(A or B) = P(A) + P(B) - P(A and B)"},
        {"q": "Are rolling a 3 and rolling a 5 on one die mutually exclusive?", "a": "Yes — you cannot roll both at the same time"},
        {"q": "Are drawing a king and drawing a heart mutually exclusive?", "a": "No — the king of hearts is both a king and a heart"},
        {"q": "What is the complement of an event?", "a": "All outcomes in the sample space that are NOT in the event; P(A complement) = 1 - P(A)"},
        {"q": "P(rolling a 2 or a 5) on a standard die?", "a": "2/6 = 1/3 — mutually exclusive, so add: 1/6 + 1/6"},
        {"q": "P(king or heart) from a standard deck?", "a": "16/52 = 4/13 — P(king) + P(heart) - P(king of hearts) = 4/52 + 13/52 - 1/52"},
        {"q": "What does the word OR mean in probability?", "a": "Union — at least one of the events occurs"},
        {"q": "If P(A) = 0.3, P(B) = 0.5, and P(A and B) = 0.15, what is P(A or B)?", "a": "0.65 — using addition rule: 0.3 + 0.5 - 0.15"},
    ],
    "13.7": [
        {"q": "What are Monte Carlo methods?", "a": "Computational algorithms that use repeated random sampling to estimate mathematical results"},
        {"q": "How can Monte Carlo methods estimate pi?", "a": "Randomly throw points in a square containing a quarter circle; pi approximately equals 4 times (points in circle / total points)"},
        {"q": "What is the key idea behind Monte Carlo simulation?", "a": "Using random sampling to approximate solutions to problems that may be deterministic in principle"},
        {"q": "How does Monte Carlo relate to geometric probability?", "a": "Monte Carlo uses random point placement in geometric regions, which is the foundation of geometric probability"},
        {"q": "What is the advantage of Monte Carlo methods?", "a": "They can solve very complex problems that have no known analytical solution"},
        {"q": "How does sample size affect Monte Carlo accuracy?", "a": "Larger sample sizes produce more accurate estimates — accuracy improves proportionally to the square root of the number of samples"},
        {"q": "How can you estimate the area of an irregular shape using Monte Carlo?", "a": "Enclose it in a rectangle, randomly generate points, and calculate (points inside shape / total points) times rectangle area"},
        {"q": "What is a random walk?", "a": "A mathematical model of a path consisting of random steps — used in Monte Carlo simulations"},
        {"q": "Who is Monte Carlo named after?", "a": "The Monte Carlo Casino in Monaco — referencing the element of chance and randomness"},
        {"q": "Where are Monte Carlo methods used in real life?", "a": "Finance (risk analysis), physics (particle simulations), engineering (reliability testing), and computer graphics (ray tracing)"},
    ],
}


def inject_flashcards(lesson_id, flashcards):
    """Inject flashcard data into the practice file."""
    unit_num = lesson_id.split('.')[0]
    filepath = os.path.join(BASE, f"Unit{unit_num}", f"Lesson{lesson_id}_Practice.html")
    
    if not os.path.exists(filepath):
        print(f"  SKIP: {filepath} does not exist")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if flashcards already exist
    if 'lessonFlashcards' in content:
        print(f"  SKIP: {filepath} already has flashcards")
        return False
    
    # Build the flashcard JS
    fc_items = []
    for fc in flashcards:
        q = fc['q'].replace("'", "\\'")
        a = fc['a'].replace("'", "\\'")
        fc_items.append(f"          {{ question: '{q}', answer: '{a}' }}")
    
    fc_js = "    <script>\n        window.lessonFlashcards = [\n" + ",\n".join(fc_items) + "\n      ];\n    </script>\n"
    
    # Insert before <script src="../../scripts/practice_games.js">
    target = '<script src="../../scripts/practice_games.js">'
    if target in content:
        content = content.replace(target, fc_js + "    " + target)
    else:
        # Try alternative: insert before </body>
        content = content.replace('</body>', fc_js + '</body>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  OK: {filepath}")
    return True


def main():
    count = 0
    for lesson_id, flashcards in FLASHCARDS.items():
        if inject_flashcards(lesson_id, flashcards):
            count += 1
    print(f"\nDone! Injected flashcards into {count} files.")


if __name__ == '__main__':
    main()
