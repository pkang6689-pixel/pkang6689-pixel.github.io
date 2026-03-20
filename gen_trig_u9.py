#!/usr/bin/env python3
"""Generate real content for Trigonometry Unit 9: Vectors (7 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "trigonometry_lessons.json")
COURSE = "Trigonometry"

def build_lesson(unit, idx, title, summary_html, flashcards, quiz):
    key = f"u{unit}_l{unit}.{idx}"
    fc = [{"term": t, "definition": d} for t, d in flashcards]
    qs = []
    for qi, (qt, opts, exp) in enumerate(quiz, 1):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        qs.append({"question_number": qi, "question_text": qt, "attempted": 2, "data_i18n": None, "options": options, "explanation": exp})
    return key, {
        "unit": unit, "lesson_number": f"{unit}.{idx}", "title": title, "course": COURSE,
        "summary_sections": [{"title": f"Key Concepts: {title}", "content_html": summary_html, "data_i18n": None}],
        "flashcards": fc, "quiz_questions": qs
    }

lessons = {}

# ── 9.1 Vector Basics ──
k, v = build_lesson(9, 1, "Introduction to Vectors",
    "<h3>Introduction to Vectors</h3>"
    "<p>A <b>vector</b> has both magnitude and direction, unlike a scalar which has magnitude only.</p>"
    "<h4>Notation</h4>"
    "<ul><li>Bold <b>v</b> or arrow notation v⃗.</li>"
    "<li>Component form: <b>v</b> = ⟨v₁, v₂⟩ (2D) or ⟨v₁, v₂, v₃⟩ (3D).</li>"
    "<li>Magnitude: |<b>v</b>| = √(v₁² + v₂²).</li></ul>"
    "<h4>Position vs. Free Vectors</h4>"
    "<p>A free vector is defined only by magnitude and direction; it can be placed anywhere.</p>",
    [
        ("Vector", "A quantity with both magnitude and direction, e.g., velocity, force."),
        ("Scalar", "A quantity with magnitude only, e.g., speed, temperature."),
        ("Component Form", "v = ⟨v₁, v₂⟩; the horizontal and vertical components."),
        ("Magnitude", "|v| = √(v₁² + v₂²); the length of the vector."),
        ("Unit Vector", "A vector of magnitude 1; v̂ = v / |v|."),
    ],
    [
        ("A vector has:", ["Magnitude only", "*Both magnitude and direction", "Direction only", "Neither"],
         "Vectors have both magnitude and direction."),
        ("The magnitude of v = ⟨3, 4⟩:", ["7", "1", "*5", "12"],
         "|v| = √(9 + 16) = 5."),
        ("The magnitude of v = ⟨−6, 8⟩:", ["−6", "8", "14", "*10"],
         "√(36 + 64) = √100 = 10."),
        ("A unit vector has magnitude:", ["0", "*1", "Any value", "Undefined"],
         "By definition, |û| = 1."),
        ("The unit vector in the direction of v = ⟨3, 4⟩:", ["⟨3, 4⟩", "*⟨3/5, 4/5⟩", "⟨1, 1⟩", "⟨0.3, 0.4⟩"],
         "v̂ = ⟨3/5, 4/5⟩."),
        ("i⃗ and j⃗ are:", ["Real numbers", "*The standard unit vectors ⟨1,0⟩ and ⟨0,1⟩", "Imaginary numbers", "Scalars"],
         "Standard basis vectors."),
        ("v = 3i⃗ + 4j⃗ is the same as:", ["⟨4, 3⟩", "*⟨3, 4⟩", "⟨3, 3⟩", "⟨7, 0⟩"],
         "3 in the x-direction, 4 in the y-direction."),
        ("A scalar times a vector changes:", ["Only direction", "*The magnitude (and possibly reverses direction if negative)", "Nothing", "Only the components' signs"],
         "cv scales the length; if c < 0, it also reverses direction."),
        ("3⟨2, −1⟩ =", ["⟨5, 2⟩", "*⟨6, −3⟩", "⟨2, −3⟩", "⟨6, 3⟩"],
         "Multiply each component by 3."),
        ("The zero vector ⟨0, 0⟩ has magnitude:", ["1", "*0", "Undefined", "∞"],
         "√(0²+0²) = 0."),
        ("Velocity is a vector because:", ["It has magnitude only", "*It has both speed (magnitude) and direction", "It's always positive", "It has no units"],
         "Speed + direction = velocity."),
        ("Speed is:", ["A vector", "*A scalar (magnitude of velocity)", "Zero", "A direction"],
         "Speed = |velocity|."),
        ("Two vectors are equal iff:", ["They have the same magnitude", "They have the same direction", "*They have the same magnitude AND direction (same components)", "They start at the same point"],
         "Both components must match."),
        ("The direction angle of v = ⟨1, √3⟩:", ["30°", "*60° (arctan(√3/1) = 60°)", "45°", "90°"],
         "θ = arctan(√3/1) = 60°."),
        ("If |v| = 10 and θ = 45°, v in component form:", ["⟨10, 10⟩", "*⟨10cos45°, 10sin45°⟩ = ⟨5√2, 5√2⟩", "⟨5, 5⟩", "⟨10, 0⟩"],
         "v = |v|⟨cosθ, sinθ⟩."),
        ("The opposite of v = ⟨2, −3⟩ is:", ["⟨2, 3⟩", "*⟨−2, 3⟩", "⟨−2, −3⟩", "⟨3, −2⟩"],
         "−v = ⟨−2, 3⟩."),
        ("Vectors are used in physics to represent:", ["Only position", "*Force, velocity, acceleration, displacement, etc.", "Only temperature", "Only mass"],
         "Many physical quantities are vectors."),
        ("In 3D, v = ⟨1, 2, 3⟩ has magnitude:", ["6", "√6", "*√14", "14"],
         "|v| = √(1+4+9) = √14."),
        ("A displacement from (1, 2) to (4, 6) is the vector:", ["⟨1, 2⟩", "⟨4, 6⟩", "*⟨3, 4⟩", "⟨5, 8⟩"],
         "⟨4−1, 6−2⟩ = ⟨3, 4⟩."),
        ("Vectors are essential in:", ["*Physics, engineering, computer graphics, navigation", "Only pure math", "Only geography", "Nothing practical"],
         "Vectors are everywhere in STEM applications."),
    ]
)
lessons[k] = v

# ── 9.2 Vector Operations ──
k, v = build_lesson(9, 2, "Vector Operations",
    "<h3>Vector Addition, Subtraction &amp; Scalar Multiplication</h3>"
    "<h4>Addition</h4>"
    "<p><b>u + v</b> = ⟨u₁+v₁, u₂+v₂⟩. Geometrically: place tail of v at head of u (tip-to-tail).</p>"
    "<h4>Subtraction</h4>"
    "<p><b>u − v</b> = ⟨u₁−v₁, u₂−v₂⟩. Geometrically: the vector from the tip of v to the tip of u.</p>"
    "<h4>Scalar Multiplication</h4>"
    "<p><b>cv</b> = ⟨cv₁, cv₂⟩. Scales the length; reverses direction when c < 0.</p>",
    [
        ("Vector Addition", "u + v = ⟨u₁+v₁, u₂+v₂⟩; tip-to-tail or parallelogram rule."),
        ("Vector Subtraction", "u − v = u + (−v) = ⟨u₁−v₁, u₂−v₂⟩."),
        ("Scalar Multiplication", "cv = ⟨cv₁, cv₂⟩; changes magnitude (and direction if c < 0)."),
        ("Parallelogram Rule", "Place u and v tail-to-tail; the diagonal of the parallelogram is u + v."),
        ("Triangle Inequality", "|u + v| ≤ |u| + |v|; the sum's magnitude ≤ sum of magnitudes."),
    ],
    [
        ("⟨2, 3⟩ + ⟨4, 1⟩ =", ["⟨6, 3⟩", "*⟨6, 4⟩", "⟨2, 4⟩", "⟨8, 3⟩"],
         "⟨2+4, 3+1⟩ = ⟨6, 4⟩."),
        ("⟨5, −2⟩ − ⟨3, 1⟩ =", ["⟨8, −1⟩", "*⟨2, −3⟩", "⟨−2, 3⟩", "⟨2, 3⟩"],
         "⟨5−3, −2−1⟩ = ⟨2, −3⟩."),
        ("−2⟨3, −4⟩ =", ["⟨6, 8⟩", "*⟨−6, 8⟩", "⟨−6, −8⟩", "⟨6, −8⟩"],
         "⟨−2(3), −2(−4)⟩ = ⟨−6, 8⟩."),
        ("Vector addition is commutative:", ["No", "*Yes: u + v = v + u", "Sometimes", "Only in 3D"],
         "Components add in any order."),
        ("Vector addition is associative:", ["No", "*Yes: (u + v) + w = u + (v + w)", "Sometimes", "Only for unit vectors"],
         "Standard algebraic property."),
        ("The parallelogram rule places u and v:", ["Tip-to-tip", "*Tail-to-tail; the diagonal is u + v", "Head-to-head", "Randomly"],
         "Draw both from the same point; diagonal = sum."),
        ("The tip-to-tail method:", ["*Place tail of second vector at head of first; resultant goes from start to end", "Place them side by side", "Is the same as parallelogram", "Doesn't exist"],
         "Sequential chain: start of first to end of last."),
        ("If u = ⟨1, 0⟩ and v = ⟨0, 1⟩, then u + v =", ["⟨0, 0⟩", "*⟨1, 1⟩", "⟨1, 0⟩", "⟨0, 1⟩"],
         "⟨1+0, 0+1⟩ = ⟨1, 1⟩."),
        ("|u + v| with u = ⟨1, 0⟩, v = ⟨0, 1⟩:", ["2", "*√2", "1", "0"],
         "|⟨1, 1⟩| = √2."),
        ("Is |u + v| always equal to |u| + |v|?", ["Yes", "*No (only if u and v are in the same direction)", "Never", "Only in 2D"],
         "Triangle inequality: |u+v| ≤ |u| + |v|, with equality when parallel and same direction."),
        ("3u − 2v where u = ⟨1, 2⟩, v = ⟨3, −1⟩:", ["⟨−3, 8⟩", "*⟨3−6, 6+2⟩ = ⟨−3, 8⟩", "⟨9, 4⟩", "⟨−3, −8⟩"],
         "3⟨1,2⟩ − 2⟨3,−1⟩ = ⟨3,6⟩ − ⟨6,−2⟩ = ⟨−3, 8⟩."),
        ("The resultant of forces F₁ = ⟨100, 0⟩ N and F₂ = ⟨0, 100⟩ N:", ["⟨100, 0⟩", "*⟨100, 100⟩ with magnitude 100√2 ≈ 141.4 N", "⟨200, 0⟩", "⟨0, 200⟩"],
         "Add the vectors: ⟨100, 100⟩, |F| = 100√2."),
        ("A boat travels ⟨3, 4⟩ km/h in still water and the current is ⟨−1, 2⟩ km/h. Effective velocity:", ["⟨3, 4⟩", "⟨4, 2⟩", "*⟨2, 6⟩", "⟨−3, −4⟩"],
         "⟨3−1, 4+2⟩ = ⟨2, 6⟩."),
        ("|⟨2, 6⟩| =", ["8", "4", "*√40 = 2√10 ≈ 6.32 km/h", "√8"],
         "√(4+36) = √40."),
        ("u − u =", ["u", "2u", "*⟨0, 0⟩ (the zero vector)", "Undefined"],
         "Any vector minus itself = zero vector."),
        ("u + 0⃗ =", ["0⃗", "*u", "−u", "Undefined"],
         "Adding the zero vector leaves u unchanged."),
        ("Linear combination: 2i⃗ + 5j⃗ =", ["⟨5, 2⟩", "*⟨2, 5⟩", "⟨7, 0⟩", "⟨0, 7⟩"],
         "2⟨1,0⟩ + 5⟨0,1⟩ = ⟨2, 5⟩."),
        ("If F₁ and F₂ are equal and opposite, the net force is:", ["F₁", "F₂", "*Zero vector (equilibrium)", "2F₁"],
         "F₁ + (−F₁) = 0⃗."),
        ("Vector operations obey the same rules as:", ["Matrix multiplication (no)", "*Real number arithmetic (with component-wise extension)", "Complex conjugation", "Division"],
         "Addition, subtraction, scalar multiplication follow familiar algebraic rules."),
        ("In 3D, ⟨1, 2, 3⟩ + ⟨4, 5, 6⟩ =", ["⟨5, 7, 3⟩", "*⟨5, 7, 9⟩", "⟨4, 10, 18⟩", "⟨3, 3, 3⟩"],
         "Add component-wise: ⟨1+4, 2+5, 3+6⟩."),
    ]
)
lessons[k] = v

# ── 9.3 Dot Product ──
k, v = build_lesson(9, 3, "The Dot Product",
    "<h3>The Dot Product</h3>"
    "<p><b>u · v = u₁v₁ + u₂v₂</b> (component formula)</p>"
    "<p><b>u · v = |u||v| cos θ</b> (geometric formula)</p>"
    "<h4>Properties</h4>"
    "<ul><li>u · v = 0 ⟺ u ⊥ v (perpendicular).</li>"
    "<li>u · u = |u|².</li>"
    "<li>Commutative: u · v = v · u.</li></ul>"
    "<h4>Projection</h4>"
    "<p>proj_u v = (v · u / |u|²) u — the component of v along u.</p>",
    [
        ("Dot Product (Algebraic)", "u · v = u₁v₁ + u₂v₂; a scalar result."),
        ("Dot Product (Geometric)", "u · v = |u||v| cos θ; relates to the angle between vectors."),
        ("Orthogonal Vectors", "u ⊥ v ⟺ u · v = 0."),
        ("Scalar Projection", "comp_u v = (v · u) / |u|; the signed length of v along u."),
        ("Vector Projection", "proj_u v = (v · u / |u|²) u; the vector component of v along u."),
    ],
    [
        ("⟨2, 3⟩ · ⟨4, −1⟩ =", ["11", "*5", "−5", "14"],
         "2(4) + 3(−1) = 8 − 3 = 5."),
        ("The dot product gives a:", ["Vector", "*Scalar", "Matrix", "Complex number"],
         "The result is a single number (scalar)."),
        ("⟨1, 0⟩ · ⟨0, 1⟩ =", ["1", "*0", "√2", "−1"],
         "1(0) + 0(1) = 0. They are perpendicular."),
        ("If u · v = 0 and neither is the zero vector, then:", ["They're parallel", "*They're perpendicular", "They're equal", "One is zero"],
         "Zero dot product ↔ orthogonal."),
        ("u · u = |u|². So ⟨3, 4⟩ · ⟨3, 4⟩ =", ["7", "12", "*25", "49"],
         "9 + 16 = 25 = 5²."),
        ("The angle between u = ⟨1, 0⟩ and v = ⟨1, 1⟩:", ["0°", "*45°", "90°", "60°"],
         "cos θ = u·v/(|u||v|) = 1/(1·√2) = 1/√2 → θ = 45°."),
        ("cos θ = u · v / (|u||v|). If u · v < 0, θ is:", ["Acute", "*Obtuse", "Right", "Zero"],
         "Negative dot product → angle > 90°."),
        ("⟨1, 1⟩ · ⟨−1, 1⟩ =", ["2", "*0", "−2", "1"],
         "1(−1) + 1(1) = 0. Perpendicular!"),
        ("The dot product is commutative:", ["No", "*Yes: u · v = v · u", "Sometimes", "Only for unit vectors"],
         "u₁v₁ + u₂v₂ = v₁u₁ + v₂u₂."),
        ("The dot product is distributive:", ["No", "*Yes: u · (v + w) = u · v + u · w", "Sometimes", "Only in 2D"],
         "Standard algebraic property."),
        ("Find the angle between u = ⟨3, 4⟩ and v = ⟨4, −3⟩:", ["0°", "45°", "*90°", "180°"],
         "u · v = 12 − 12 = 0 → perpendicular."),
        ("Work = F · d (force dot displacement). If F = ⟨5, 3⟩ N and d = ⟨4, 0⟩ m:", ["8 J", "*20 J", "32 J", "15 J"],
         "W = 5(4) + 3(0) = 20 J."),
        ("The scalar projection of v onto u (comp_u v) is:", ["v · u", "*v · u / |u|", "|v| cos θ", "v × u"],
         "comp_u v = (v · u)/|u|."),
        ("The vector projection of v = ⟨4, 3⟩ onto u = ⟨1, 0⟩:", ["⟨4, 3⟩", "*⟨4, 0⟩", "⟨0, 3⟩", "⟨3, 4⟩"],
         "proj_u v = (v·u/|u|²)u = (4/1)⟨1,0⟩ = ⟨4, 0⟩."),
        ("If θ = 0° between u and v, then u · v =", ["|u| − |v|", "0", "*|u||v|", "−|u||v|"],
         "cos 0° = 1 → u·v = |u||v|."),
        ("If θ = 180°, then u · v =", ["|u||v|", "0", "*−|u||v|", "Undefined"],
         "cos 180° = −1."),
        ("⟨2, 5⟩ · ⟨−5, 2⟩ =", ["0", "*0 (perpendicular!)", "−5", "20"],
         "2(−5) + 5(2) = −10 + 10 = 0."),
        ("In 3D: ⟨1, 2, 3⟩ · ⟨4, −5, 6⟩ =", ["−3", "*12", "5", "26"],
         "4 − 10 + 18 = 12."),
        ("The dot product is used to calculate:", ["*Work, angles between vectors, projections", "Only area", "Only cross products", "Only unit vectors"],
         "Work, angle, and projection are the main applications."),
        ("If u · v = |u||v|, then the vectors are:", ["Perpendicular", "*Parallel and same direction", "Opposite", "Zero"],
         "cos θ = 1 → θ = 0° → same direction."),
    ]
)
lessons[k] = v

# ── 9.4 Cross Product (Introduction) ──
k, v = build_lesson(9, 4, "Introduction to the Cross Product",
    "<h3>Introduction to the Cross Product</h3>"
    "<p>The cross product is defined in 3D: <b>u × v</b> produces a <b>vector</b> perpendicular to both u and v.</p>"
    "<h4>Formula</h4>"
    "<p>u × v = ⟨u₂v₃−u₃v₂, u₃v₁−u₁v₃, u₁v₂−u₂v₁⟩</p>"
    "<h4>Key Properties</h4>"
    "<ul><li>|u × v| = |u||v| sin θ (magnitude = area of parallelogram).</li>"
    "<li>Direction: right-hand rule.</li>"
    "<li>Anti-commutative: u × v = −(v × u).</li></ul>",
    [
        ("Cross Product", "u × v; a vector perpendicular to both u and v (3D only)."),
        ("Anti-commutativity", "u × v = −(v × u); reversing the order negates the result."),
        ("|u × v|", "= |u||v| sin θ; the area of the parallelogram formed by u and v."),
        ("Right-Hand Rule", "Curl fingers from u toward v; thumb points in direction of u × v."),
        ("Parallel Vectors", "u × v = 0⃗ iff u ∥ v (since sin 0° = 0)."),
    ],
    [
        ("The cross product produces:", ["A scalar", "*A vector", "A matrix", "A complex number"],
         "Unlike dot product, cross product gives a vector."),
        ("u × v is perpendicular to:", ["u only", "v only", "*Both u and v", "Neither"],
         "The cross product is orthogonal to the plane containing u and v."),
        ("u × v = −(v × u) means the cross product is:", ["Commutative", "*Anti-commutative", "Associative", "Zero"],
         "Reversing order negates the result."),
        ("i⃗ × j⃗ =", ["i⃗", "j⃗", "*k⃗", "−k⃗"],
         "Right-hand rule: i × j = k."),
        ("j⃗ × i⃗ =", ["k⃗", "j⃗", "*−k⃗", "i⃗"],
         "Anti-commutative: j × i = −(i × j) = −k."),
        ("|u × v| represents:", ["The dot product", "*The area of the parallelogram formed by u and v", "The perimeter", "The volume"],
         "|u||v|sinθ = parallelogram area."),
        ("If u ∥ v, then u × v =", ["u + v", "|u||v|", "*0⃗ (the zero vector)", "Undefined"],
         "sin 0° = 0 → cross product is zero."),
        ("If u ⊥ v, then |u × v| =", ["0", "*|u||v|", "|u| + |v|", "|u| − |v|"],
         "sin 90° = 1 → |u||v|."),
        ("⟨1, 0, 0⟩ × ⟨0, 1, 0⟩ =", ["⟨1, 1, 0⟩", "*⟨0, 0, 1⟩", "⟨0, 0, −1⟩", "⟨1, 0, 1⟩"],
         "i × j = k = ⟨0, 0, 1⟩."),
        ("⟨1, 2, 3⟩ × ⟨4, 5, 6⟩ = :", ["⟨4, 10, 18⟩", "*⟨2·6−3·5, 3·4−1·6, 1·5−2·4⟩ = ⟨−3, 6, −3⟩", "⟨3, −6, 3⟩", "⟨0, 0, 0⟩"],
         "⟨12−15, 12−6, 5−8⟩ = ⟨−3, 6, −3⟩."),
        ("The cross product is defined only in:", ["1D and 2D", "2D only", "*3D (and 7D, but typically only 3D)", "All dimensions"],
         "Standard cross product is a 3D operation."),
        ("Torque τ = r × F. This is a:", ["Scalar", "*Vector (perpendicular to the plane of r and F)", "Matrix", "Number"],
         "Torque is a cross-product vector."),
        ("The area of a triangle with sides u and v is:", ["|u × v|", "*½|u × v|", "2|u × v|", "|u · v|"],
         "Triangle area = half the parallelogram area."),
        ("u × u =", ["u", "|u|²", "*0⃗", "2u"],
         "A vector crossed with itself is zero (sin 0° = 0)."),
        ("The right-hand rule determines:", ["Magnitude", "*The direction of u × v", "The angle", "The scalar"],
         "Curl fingers from u to v; thumb points in direction of result."),
        ("Angular momentum L = r × p uses the cross product because:", ["It's simpler", "*Angular momentum is perpendicular to the plane of motion", "It gives a scalar", "Convention"],
         "L is perp to r and p."),
        ("c(u × v) = (cu) × v. This means:", ["Cross product ignores scalars", "*Scalar multiplication distributes across the cross product", "Scalars are irrelevant", "Cross product is linear"],
         "Scalar multiple can be pulled out."),
        ("u × (v + w) = u × v + u × w. The cross product is:", ["Commutative", "*Distributive over addition", "Associative", "None of these"],
         "Cross product distributes."),
        ("The cross product is NOT:", ["Anti-commutative", "Distributive", "*Associative: a × (b × c) ≠ (a × b) × c in general", "Defined in 3D"],
         "Cross product is not associative."),
        ("In physics, the magnetic force F = qv × B is an application of:", ["The dot product", "*The cross product", "Addition", "Subtraction"],
         "Lorentz force uses cross product."),
    ]
)
lessons[k] = v

# ── 9.5 Physics & Engineering Applications ──
k, v = build_lesson(9, 5, "Physics & Engineering Applications of Vectors",
    "<h3>Physics &amp; Engineering Applications</h3>"
    "<h4>Statics: Equilibrium</h4>"
    "<p>For an object in equilibrium: ΣF = 0⃗ (all forces sum to zero).</p>"
    "<h4>Work &amp; Energy</h4>"
    "<p>W = F · d = |F||d| cos θ.</p>"
    "<h4>Torque &amp; Rotation</h4>"
    "<p>τ = r × F; magnitude = |r||F| sin θ.</p>",
    [
        ("Equilibrium", "Net force = 0⃗; the object is stationary or moving at constant velocity."),
        ("Work (W)", "W = F · d; the dot product of force and displacement."),
        ("Torque (τ)", "τ = r × F; the cross product of position vector and force."),
        ("Component Resolution", "Breaking a vector into perpendicular components along chosen axes."),
        ("Resultant Force", "The vector sum of all forces acting on an object."),
    ],
    [
        ("An object in static equilibrium has:", ["Large forces", "*Net force ΣF = 0⃗", "Only one force", "Acceleration"],
         "Equilibrium: all forces balance."),
        ("A 50 N force at 60° to horizontal. Horizontal component:", ["50 N", "*50 cos 60° = 25 N", "50 sin 60° ≈ 43.3 N", "0"],
         "Fₓ = F cos θ."),
        ("Same force: vertical component:", ["25 N", "*50 sin 60° ≈ 43.3 N", "50 N", "0"],
         "Fy = F sin θ."),
        ("Work: F = 40 N, d = 10 m, θ = 30° between them. W =", ["400 J", "200 J", "*40(10)cos30° ≈ 346.4 J", "40(10)sin30° = 200 J"],
         "W = Fd cos θ."),
        ("If force is perpendicular to motion (θ = 90°), work done:", ["Maximum", "*Zero", "Negative", "F × d"],
         "cos 90° = 0 → no work."),
        ("A wrench applies 30 N force at 0.5 m from the bolt. Maximum torque:", ["15", "*15 N·m (when F ⊥ r, sin90° = 1)", "30 N·m", "60 N·m"],
         "|τ| = rF sinθ. Max when θ = 90°: 0.5 × 30 = 15 N·m."),
        ("If the force is along the wrench (θ = 0°), torque:", ["15 N·m", "*0 (sin0° = 0: no rotation)", "30 N·m", "∞"],
         "No torque if force is along r."),
        ("Three forces in equilibrium: F₁ + F₂ + F₃ = 0⃗ means:", ["All forces are equal", "*The third force equals the negative of the sum of the other two", "One force is zero", "All parallel"],
         "F₃ = −(F₁ + F₂)."),
        ("A plane flies at 300 km/h heading north; crosswind is 50 km/h east. Actual speed:", ["350 km/h", "250 km/h", "*√(300²+50²) ≈ 304.1 km/h", "300 km/h"],
         "Pythagorean sum."),
        ("Direction of the plane's actual velocity:", ["Due north", "*Slightly east of north: arctan(50/300) ≈ 9.5° east of north", "Due east", "45° NE"],
         "tan θ = 50/300."),
        ("An inclined plane at angle α: gravity component along the plane:", ["mg cos α", "*mg sin α", "mg", "0"],
         "The component parallel to the slope is mg sin α."),
        ("Gravity component perpendicular to the plane:", ["mg sin α", "*mg cos α", "mg", "mg tan α"],
         "Normal: mg cos α."),
        ("Two ropes hold a 100 N weight in equilibrium. The tensions:", ["Both 50 N always", "*Depend on the angles of the ropes (solve ΣFₓ=0, ΣFy=0)", "Both 100 N", "Both 0"],
         "Use equilibrium equations with the angles."),
        ("Work done against gravity lifting 5 kg by 3 m: W =", ["15 J", "50 J", "*5(9.8)(3) = 147 J", "5(3) = 15 J"],
         "W = mgh = 5 × 9.8 × 3."),
        ("The dot product gives a scalar result, which is appropriate for work because:", ["Convention", "*Work is a scalar quantity (energy)", "It's easier", "No reason"],
         "Energy is a scalar → dot product is the right operation."),
        ("Torque is a vector because:", ["Convention", "*The axis of rotation has a direction", "It's easier", "It equals force times distance"],
         "Torque has both magnitude and direction (axis of rotation)."),
        ("In bridge design, engineers resolve forces in trusses using:", ["Only arithmetic", "*Vector decomposition along member directions", "Only estimation", "No math"],
         "Each truss member carries a force along its direction."),
        ("Resultant of 5 N east and 12 N north:", ["17 N", "*13 N (5-12-13 triangle)", "7 N", "60 N"],
         "√(25 + 144) = √169 = 13."),
        ("In fluid dynamics, the velocity field is a:", ["Scalar field", "*Vector field", "Matrix", "Constant"],
         "At each point, the fluid has a velocity vector."),
        ("Vectors in engineering often use component form because:", ["It's traditional", "*Components align with coordinate axes, simplifying calculations", "It looks nice", "No advantage"],
         "Component form enables systematic algebraic computation."),
    ]
)
lessons[k] = v

# ── 9.6 Computer Graphics Applications ──
k, v = build_lesson(9, 6, "Computer Graphics Applications",
    "<h3>Vectors in Computer Graphics</h3>"
    "<h4>Transformations</h4>"
    "<ul><li><b>Translation:</b> Add a displacement vector to every point.</li>"
    "<li><b>Scaling:</b> Multiply by a scalar (or scale factors per axis).</li>"
    "<li><b>Rotation:</b> Apply rotation matrix using cos/sin.</li></ul>"
    "<h4>Normal Vectors &amp; Lighting</h4>"
    "<p>Surface normal vectors determine how light reflects — using the dot product to compute brightness.</p>",
    [
        ("Translation", "Moving every point by adding a displacement vector."),
        ("Rotation Matrix (2D)", "[[cosθ, −sinθ], [sinθ, cosθ]]; rotates a vector by angle θ CCW."),
        ("Normal Vector", "A vector perpendicular to a surface; used for lighting calculations."),
        ("Diffuse Lighting", "Brightness ∝ max(0, n̂ · L̂); dot product of surface normal and light direction."),
        ("Dot Product in Graphics", "Used for shading, reflections, visibility testing, and angle computations."),
    ],
    [
        ("Translating a point (2, 3) by vector ⟨4, −1⟩:", ["(6, 4)", "*(6, 2)", "(2, 3)", "(−2, 4)"],
         "(2+4, 3+(−1)) = (6, 2)."),
        ("Scaling ⟨3, 5⟩ by factor 2:", ["⟨5, 7⟩", "*⟨6, 10⟩", "⟨3, 5⟩", "⟨1.5, 2.5⟩"],
         "2⟨3, 5⟩ = ⟨6, 10⟩."),
        ("A 90° CCW rotation of ⟨1, 0⟩:", ["⟨1, 0⟩", "⟨−1, 0⟩", "*⟨0, 1⟩", "⟨0, −1⟩"],
         "Rotation matrix: [cos90,−sin90; sin90,cos90]⟨1,0⟩ = ⟨0, 1⟩."),
        ("A 90° CCW rotation of ⟨0, 1⟩:", ["⟨0, 1⟩", "⟨1, 0⟩", "*⟨−1, 0⟩", "⟨0, −1⟩"],
         "[0,−1; 1,0]⟨0,1⟩ = ⟨−1, 0⟩."),
        ("In 3D graphics, the surface normal is used for:", ["Coloring only", "*Lighting/shading calculations", "Sound", "Motion"],
         "Normal determines how light hits the surface."),
        ("Diffuse (Lambertian) lighting uses:", ["Cross product", "*Dot product: brightness ∝ n̂ · L̂", "Subtraction", "Division"],
         "n̂ · L̂ = cos(angle between normal and light)."),
        ("If n̂ · L̂ = 0, the surface is:", ["Fully lit", "*Edge-on to the light (no illumination)", "Bright", "Overexposed"],
         "cos 90° = 0 → perpendicular to light → dark."),
        ("If n̂ · L̂ < 0, the surface faces:", ["Toward the light", "*Away from the light (backface, no illumination)", "Up", "Down"],
         "Negative dot product → facing away; clamped to 0."),
        ("Reflection of light: r = 2(n̂ · L̂)n̂ − L̂. This formula uses:", ["Only subtraction", "*Dot product and vector operations", "Cross product", "Only addition"],
         "Specular reflection formula."),
        ("The cross product in 3D graphics computes:", ["Colors", "*Surface normals from two edge vectors of a polygon", "Speed", "Textures"],
         "n = e₁ × e₂ gives the normal to the polygon."),
        ("Homogeneous coordinates add a 4th coordinate to allow:", ["Colors", "*Translation as matrix multiplication", "Z-buffering", "Textures"],
         "Translation can be represented as a 4×4 matrix in homogeneous coords."),
        ("A game character moves at velocity v = ⟨5, 0, 3⟩ m/s. After 2 seconds, displacement:", ["⟨5, 0, 3⟩", "*⟨10, 0, 6⟩", "⟨3, 0, 5⟩", "⟨2.5, 0, 1.5⟩"],
         "d = vt = 2⟨5,0,3⟩ = ⟨10, 0, 6⟩."),
        ("Back-face culling uses the dot product of the surface normal and:", ["A random vector", "*The view direction (camera vector)", "The up vector", "The x-axis"],
         "If n · view < 0, the face points away → skip rendering."),
        ("In ray tracing, the direction of a reflected ray depends on:", ["Only the surface color", "*The incident ray direction and the surface normal (dot product)", "Random chance", "Screen resolution"],
         "Reflection uses r = d − 2(d · n̂)n̂."),
        ("Interpolating normals across a polygon face is called:", ["Flat shading", "*Smooth/Phong shading", "Wireframe rendering", "Culling"],
         "Phong shading interpolates normals for smooth lighting."),
        ("Matrix transformations in graphics are composed by:", ["Adding matrices", "*Multiplying matrices (composition = multiplication)", "Inverting matrices", "Subtracting matrices"],
         "Combined transformations = product of individual matrices."),
        ("The order of transformations:", ["Doesn't matter", "*Matters! (matrix multiplication is not commutative)", "Only matters in 2D", "Is always the same"],
         "Rotate then translate ≠ translate then rotate."),
        ("A perspective projection uses:", ["Only addition", "*Division by depth (z) to create the illusion of 3D", "Cross products", "Only dot products"],
         "Perspective divide: x/z and y/z."),
        ("Vectors are fundamental to all modern computer graphics because:", ["Historical reasons", "*All positions, directions, normals, and transformations are vector operations", "Marketing", "They're simple"],
         "Everything in 3D graphics is built on vector math."),
        ("GPU hardware is optimized for:", ["String processing", "*Massively parallel vector/matrix operations", "Sorting", "Text rendering"],
         "GPUs process millions of vector operations simultaneously."),
    ]
)
lessons[k] = v

# ── 9.7 AP Calculus & Preview Applications ──
k, v = build_lesson(9, 7, "AP Calculus Connections",
    "<h3>Vectors and AP Calculus Preview</h3>"
    "<h4>Vector-Valued Functions</h4>"
    "<p>r(t) = ⟨x(t), y(t)⟩ traces a curve. The derivative r'(t) = ⟨x'(t), y'(t)⟩ is the <b>velocity vector</b>, tangent to the curve.</p>"
    "<h4>Parametric Equations</h4>"
    "<p>x = f(t), y = g(t). Eliminating t gives the Cartesian equation.</p>"
    "<h4>Arc Length</h4>"
    "<p>Arc length = ∫|r'(t)| dt = ∫√(x'(t)² + y'(t)²) dt.</p>",
    [
        ("Vector-Valued Function", "r(t) = ⟨x(t), y(t)⟩; maps a parameter t to a position vector."),
        ("Velocity Vector", "r'(t) = ⟨x'(t), y'(t)⟩; tangent to the curve at time t."),
        ("Speed", "|r'(t)| = √(x'² + y'²); the magnitude of velocity."),
        ("Parametric Equations", "x = f(t), y = g(t) define a curve in terms of a parameter."),
        ("Arc Length", "L = ∫ₐᵇ √(x'² + y'²) dt; total distance traveled along the curve."),
    ],
    [
        ("A vector-valued function r(t) = ⟨cos t, sin t⟩ traces:", ["A line", "*A unit circle", "A parabola", "An ellipse"],
         "x² + y² = cos²t + sin²t = 1."),
        ("r'(t) for ⟨cos t, sin t⟩:", ["⟨cos t, sin t⟩", "*⟨−sin t, cos t⟩", "⟨sin t, −cos t⟩", "⟨1, 0⟩"],
         "Differentiate each component."),
        ("Is r'(t) perpendicular to r(t) for the unit circle?", ["No", "*Yes: r · r' = −sincos + sincos = 0", "Sometimes", "Only at t = 0"],
         "The velocity on a circle is always tangent (perp to radius)."),
        ("|r'(t)| for ⟨cos t, sin t⟩:", ["0", "*1 (constant speed)", "2π", "t"],
         "√(sin²t + cos²t) = 1."),
        ("The parametric equations x = 2t, y = t² describe:", ["A circle", "A line", "*A parabola", "An ellipse"],
         "t = x/2 → y = (x/2)² = x²/4."),
        ("The velocity vector for x = 2t, y = t² at t = 3:", ["⟨2, 3⟩", "*⟨2, 6⟩ (x'=2, y'=2t=6)", "⟨6, 2⟩", "⟨3, 9⟩"],
         "r'(t) = ⟨2, 2t⟩. At t = 3: ⟨2, 6⟩."),
        ("Speed at t = 3:", ["8", "*√(4 + 36) = √40 = 2√10 ≈ 6.32", "6", "40"],
         "|⟨2, 6⟩| = √40."),
        ("Arc length from t = 0 to t = 1 for r(t) = ⟨t, t²⟩:", ["1", "*∫₀¹ √(1 + 4t²) dt (requires integration techniques)", "2", "√2"],
         "x' = 1, y' = 2t; L = ∫√(1 + 4t²) dt."),
        ("r(t) = ⟨3cos t, 3sin t⟩ is a circle of radius:", ["1", "*3", "9", "6"],
         "x² + y² = 9."),
        ("Acceleration a(t) = r''(t) for ⟨t², t³⟩:", ["⟨2, 3⟩", "*⟨2, 6t⟩", "⟨t, t²⟩", "⟨2t, 3t²⟩"],
         "r'(t) = ⟨2t, 3t²⟩, r''(t) = ⟨2, 6t⟩."),
        ("Parametric curves on the AP Calculus BC exam include:", ["Only circles", "*Derivatives, arc length, speed, and area under parametric curves", "Only lines", "No vectors"],
         "Key BC topics."),
        ("The parameter t often represents:", ["x", "*Time", "Area", "Slope"],
         "In physics applications, t is usually time."),
        ("To eliminate the parameter from x = t + 1, y = t − 1:", ["*Add: x + y = 2t, subtract: x − y = 2 → y = x − 2", "Multiply: xy = t² − 1", "Can't eliminate", "t = x − 1 → y = (x−1) − 1 = x − 2"],
         "t = x − 1 → y = (x − 1) − 1 = x − 2."),
        ("Projectile motion: r(t) = ⟨v₀cos α · t, v₀sin α · t − ½gt²⟩. This is:", ["A circle", "*A parabola", "A line", "An ellipse"],
         "Parametric parabola."),
        ("The maximum height of a projectile occurs when:", ["x'(t) = 0", "*y'(t) = 0 (vertical velocity = 0)", "t = 0", "x(t) = 0"],
         "Vertical component of velocity = 0 at the peak."),
        ("dy/dx for parametric curves:", ["y' + x'", "*dy/dx = (dy/dt) / (dx/dt)", "dx/dt + dy/dt", "Undefined"],
         "Chain rule: dy/dx = y'/x'."),
        ("For r(t) = ⟨t², t³⟩: dy/dx =", ["2t/3t²", "*3t²/(2t) = 3t/2", "t", "6t"],
         "dy/dx = y'/x' = 3t²/(2t) = 3t/2."),
        ("The tangent line at a point uses:", ["Only the position", "*The position r(t₀) and the direction r'(t₀)", "Only the acceleration", "Only the speed"],
         "Position + velocity direction = tangent line."),
        ("Vectors connect to calculus through:", ["Nothing", "*Parametric curves, motion, fields, and multivariable calculus", "Only AP exam requirements", "Only theory"],
         "Vectors are the foundation of multivariable and vector calculus."),
        ("On the AP exam, always include units when describing:", ["Only position", "*Velocity (m/s), acceleration (m/s²), and speed", "Only speed", "Nothing"],
         "AP requires proper units."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Trigonometry Unit 9: wrote {len(lessons)} lessons")
