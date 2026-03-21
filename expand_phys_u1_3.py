#!/usr/bin/env python3
"""Expand Physics U1-U3 quizzes from 7 to 20 questions each (20 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "physics_lessons.json")

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

# ── U1: Measurements & Units ──

k, q = add_qs("u1_l1.1", [
    ("A physical quantity is a property that can be:", ["Only estimated", "*Measured and expressed with a number and unit", "Only observed qualitatively", "Described in words only"], "Quantitative measurement."),
    ("Which is a base quantity in physics?", ["Velocity", "Force", "*Mass", "Energy"], "Mass is fundamental; the others are derived."),
    ("The SI unit of time is the:", ["Hour", "Minute", "*Second", "Day"], "Second (s) is the SI base unit."),
    ("Temperature in SI is measured in:", ["Fahrenheit", "Celsius", "*Kelvin", "Rankine"], "Kelvin is the SI base unit."),
    ("Which quantity is derived?", ["Length", "Mass", "*Force (kg·m/s²)", "Time"], "Force = mass × acceleration."),
    ("Luminous intensity is measured in:", ["Lumens", "*Candela", "Watts", "Lux"], "Candela is the base unit."),
    ("The amount of substance is measured in:", ["Grams", "*Moles", "Atoms", "Liters"], "Mole is the SI base."),
    ("A quantity without a direction is a:", ["Vector", "*Scalar", "Tensor", "Unit"], "Scalars have magnitude only."),
    ("The dimensions of velocity are:", ["[M L T⁻¹]", "*[L T⁻¹]", "[L² T⁻¹]", "[L T⁻²]"], "Length/time."),
    ("Which pair has the same dimensions?", ["Work and force", "*Work and energy", "Velocity and acceleration", "Mass and weight"], "Both are kg·m²/s²."),
    ("Area has dimensions of:", ["[L]", "*[L²]", "[L³]", "[L T⁻¹]"], "Length squared."),
    ("The SI unit of energy is the:", ["Calorie", "Electron-volt", "*Joule", "Watt"], "Joule = kg·m²/s²."),
    ("Density has SI units of:", ["kg/m", "kg·m³", "*kg/m³", "g/cm³"], "Mass per volume."),
])
all_new[k] = q

k, q = add_qs("u1_l1.2", [
    ("The SI system is based on _____ base units.", ["5", "6", "*7", "10"], "Seven base units."),
    ("The prefix 'kilo' means:", ["10", "100", "*1000 (10³)", "1 000 000"], "10³."),
    ("The prefix 'milli' means:", ["10⁻²", "*10⁻³", "10⁻⁶", "10⁻¹"], "One-thousandth."),
    ("The prefix 'micro' (μ) means:", ["10⁻³", "*10⁻⁶", "10⁻⁹", "10⁻²"], "One-millionth."),
    ("The prefix 'nano' means:", ["10⁻⁶", "*10⁻⁹", "10⁻¹²", "10⁻³"], "One-billionth."),
    ("The prefix 'mega' means:", ["10³", "*10⁶", "10⁹", "10²"], "One million."),
    ("The prefix 'giga' means:", ["10⁶", "*10⁹", "10¹²", "10³"], "One billion."),
    ("5 km = _____ m.", ["50", "500", "*5000", "50 000"], "5 × 1000 = 5000."),
    ("3.2 mg = _____ g.", ["3200", "32", "*0.0032", "0.32"], "3.2 × 10⁻³."),
    ("200 ns = _____ s.", ["2 × 10⁻⁵", "2 × 10⁻⁶", "*2 × 10⁻⁷", "2 × 10⁻⁸"], "200 × 10⁻⁹ = 2 × 10⁻⁷."),
    ("The prefix 'centi' means:", ["10⁻¹", "*10⁻²", "10⁻³", "10²"], "One-hundredth."),
    ("Which is the largest? 1 Mm, 1 Gm, 1 km, 1 Tm:", ["1 Mm", "1 Gm", "1 km", "*1 Tm (10¹²)"], "Tera > Giga > Mega > kilo."),
    ("4.5 × 10⁶ μm = _____ m.", ["4500", "45", "*4.5", "0.45"], "4.5×10⁶ × 10⁻⁶ = 4.5 m."),
])
all_new[k] = q

k, q = add_qs("u1_l1.3", [
    ("A scalar quantity has:", ["Magnitude and direction", "*Magnitude only", "Direction only", "Neither"], "Magnitude only."),
    ("A vector quantity has:", ["Magnitude only", "*Magnitude and direction", "Direction only", "Neither"], "Both magnitude and direction."),
    ("Which is a vector?", ["Temperature", "Mass", "Speed", "*Velocity"], "Velocity has direction."),
    ("Which is a scalar?", ["Force", "Acceleration", "*Energy", "Displacement"], "Energy is scalar."),
    ("Speed is the _____ of velocity.", ["Direction", "Vector", "*Magnitude (scalar part)", "Inverse"], "Speed = |velocity|."),
    ("Distance is scalar; _____ is a vector.", ["Speed", "Mass", "*Displacement", "Time"], "Displacement has direction."),
    ("Vectors are added using the _____ rule.", ["Subtraction", "*Tip-to-tail (or parallelogram)", "Multiplication", "Division"], "Tip-to-tail addition."),
    ("The resultant of two perpendicular vectors of 3 N and 4 N is:", ["7 N", "1 N", "*5 N", "12 N"], "√(9+16) = 5."),
    ("A vector can be resolved into _____ components.", ["One", "*Two (or more orthogonal components)", "Only three", "None"], "Component decomposition."),
    ("The x-component of a vector F at angle θ to the x-axis: Fₓ =", ["F sin θ", "*F cos θ", "F tan θ", "F/cos θ"], "Adjacent side."),
    ("The y-component: Fᵧ =", ["F cos θ", "*F sin θ", "F tan θ", "F/sin θ"], "Opposite side."),
    ("Two antiparallel vectors of magnitudes 10 and 6 have resultant:", ["16", "*4 (in the direction of the larger)", "60", "8"], "10 - 6 = 4."),
    ("The zero vector has magnitude:", ["1", "Undefined", "*0", "Infinity"], "Zero magnitude."),
])
all_new[k] = q

k, q = add_qs("u1_l1.4", [
    ("Accuracy refers to how close a measurement is to the:", ["Average value", "*True (accepted) value", "Standard deviation", "Median"], "Closeness to true value."),
    ("Precision refers to how close repeated measurements are to:", ["The true value", "*Each other", "Zero", "The average only"], "Reproducibility."),
    ("A measurement can be precise but not accurate if there is a:", ["Random error only", "*Systematic error (consistent bias)", "No error", "Large uncertainty"], "Systematic bias."),
    ("The number 0.00340 has _____ significant figures.", ["2", "*3", "4", "5"], "3,4,0 are significant."),
    ("The number 5000 (no decimal) has _____ significant figure(s) (ambiguous, usually).", ["4", "3", "*1 (ambiguously, or 4 if all digits are measured — context matters)", "2"], "Trailing zeros ambiguous without decimal."),
    ("5.00 × 10³ has _____ significant figures.", ["1", "2", "*3", "4"], "5, 0, 0 are significant."),
    ("When multiplying, the result should have sig figs equal to the _____ of the inputs.", ["Sum", "*Fewest (least number of sig figs)", "Greatest", "Average"], "Fewest sig figs rule."),
    ("When adding, the result is rounded to the _____ decimal place of the inputs.", ["Least", "*Fewest (least precise decimal place)", "Most", "Average"], "Least precise decimal."),
    ("2.5 × 3.42 = 8.55, rounded to correct sig figs:", ["8.55", "*8.6 (2 sig figs)", "9", "8.550"], "2 sig figs from 2.5."),
    ("12.11 + 0.3 = 12.41, rounded correctly:", ["12.41", "12.4", "*12.4 (one decimal place from 0.3)", "12"], "One decimal place."),
    ("Percent error = |measured - true| / true × 100%. If true = 10.0, measured = 9.6:", ["6%", "0.4%", "*4%", "40%"], "|9.6-10|/10=0.04=4%."),
    ("Random errors cause measurements to scatter _____ the mean.", ["All above", "All below", "*Around (above and below)", "Away from"], "Random fluctuation."),
    ("Systematic errors shift all measurements in _____ direction.", ["Random", "*The same", "No", "Two"], "Consistent offset."),
])
all_new[k] = q

k, q = add_qs("u1_l1.5", [
    ("Dimensional analysis checks whether an equation is _____ consistent.", ["Numerically", "*Dimensionally", "Algebraically", "Graphically"], "Checking dimensions."),
    ("The dimensions of force [MLT⁻²] come from F = ma:", ["[M][LT⁻¹]", "*[M][LT⁻²]", "[ML²T⁻²]", "[MLT⁻¹]"], "mass × acceleration."),
    ("Energy has dimensions:", ["[MLT⁻¹]", "[MLT⁻²]", "*[ML²T⁻²]", "[ML²T⁻³]"], "Force × distance."),
    ("Power has dimensions:", ["[ML²T⁻²]", "*[ML²T⁻³]", "[MLT⁻²]", "[MLT⁻¹]"], "Energy / time."),
    ("Pressure has dimensions:", ["[MLT⁻²]", "*[ML⁻¹T⁻²]", "[ML²T⁻²]", "[ML⁻²T⁻²]"], "Force / area."),
    ("If an equation yields [MLT⁻²] on the left and [ML²T⁻²] on the right, the equation is:", ["Correct", "*Dimensionally incorrect", "Approximately correct", "Unitless"], "Mismatch means wrong."),
    ("Dimensional analysis can reveal _____ but cannot verify numerical constants.", ["Nothing", "*Whether an equation could be correct", "Exact values", "Directions"], "Checks form, not constants."),
    ("The dimensionless quantity:", ["Velocity", "Force", "*Angle in radians", "Momentum"], "Radians = length/length."),
    ("To convert 60 mph to m/s: 60 × (1609 m/mile) / (3600 s/hr) ≈", ["60 m/s", "100 m/s", "*26.8 m/s", "16.1 m/s"], "60×1609/3600 ≈ 26.8."),
    ("Using dimensional analysis, the period of a pendulum T can depend on length L and g. T ∝ √(L/g) because:", ["[T] = [L]", "[T] = [LT⁻²]", "*[T] = √([L]/[LT⁻²]) = √([T²]) = [T]", "[T] = [L][T⁻²]"], "Dimensions match."),
    ("If v² = u² + 2as, check dimensions: [LT⁻¹]² = [LT⁻¹]² + 2[LT⁻²][L]:", ["[L²T⁻²] ≠ [L²T⁻²]", "*[L²T⁻²] = [L²T⁻²] — dimensionally correct", "[LT⁻¹] = [L²T⁻²]", "Cannot check"], "All terms are [L²T⁻²]."),
    ("A dimensionally correct equation:", ["Must be physically correct", "*May or may not be physically correct (but a dimensionally wrong one is definitely wrong)", "Is always wrong", "Has no constants"], "Necessary but not sufficient."),
    ("The fine structure constant α ≈ 1/137 is:", ["A vector", "*Dimensionless", "Measured in meters", "A base unit"], "Pure number."),
])
all_new[k] = q

k, q = add_qs("u1_l1.6", [
    ("Measurement uncertainty indicates the _____ of a measured value.", ["Exactness", "*Range of doubt (possible error)", "Precision only", "True value"], "Range of possible error."),
    ("Absolute uncertainty is expressed in the:", ["Percentage only", "*Same units as the measurement", "Ratio form", "No units"], "Same units."),
    ("Relative (fractional) uncertainty = absolute uncertainty ÷ _____.", ["True value", "*Measured value", "Standard deviation", "100"], "Fraction of measured value."),
    ("Percent uncertainty = relative uncertainty × 100%. If measurement = 50±2, percent uncertainty =", ["2%", "*4%", "50%", "1%"], "2/50 = 0.04 = 4%."),
    ("When adding or subtracting, absolute uncertainties are:", ["Multiplied", "*Added", "Subtracted", "Squared and added"], "Add absolute uncertainties."),
    ("When multiplying or dividing, _____ uncertainties are added.", ["Absolute", "*Relative (or percentage)", "No", "Standard"], "Add relative uncertainties."),
    ("If A = 5.0 ± 0.2 and B = 3.0 ± 0.1, A + B =", ["8.0 ± 0.1", "*8.0 ± 0.3", "8.0 ± 0.2", "8.0 ± 0.02"], "0.2 + 0.1 = 0.3."),
    ("If A = 5.0 ± 0.2 and B = 3.0 ± 0.1, A × B = 15.0 ± ?. Use relative: 0.2/5 + 0.1/3 = 0.04+0.033 ≈ 0.073, so ±", ["0.3", "0.1", "*1.1 (0.073 × 15 ≈ 1.1)", "15"], "≈ 1.1."),
    ("For a quantity raised to power n: relative uncertainty is multiplied by:", ["1", "n²", "*|n|", "1/n"], "|n| × relative uncertainty."),
    ("If r = 3.0 ± 0.1 cm, and A = πr², the relative uncertainty in A is:", ["0.1/3", "*2 × (0.1/3) ≈ 6.7%", "0.1/9", "0.01/3"], "Power of 2 doubles relative uncertainty."),
    ("Systematic errors _____ be reduced by averaging many measurements.", ["Can", "*Cannot (averaging reduces random errors, not systematic)", "Always", "Sometimes"], "Only random errors reduce."),
    ("The standard deviation measures the _____ of repeated measurements.", ["Accuracy", "*Spread (precision)", "Systematic error", "True value"], "Spread around mean."),
    ("Error bars on a graph represent:", ["Exact values", "*Uncertainty ranges", "True values", "Scale factors"], "Visual uncertainty."),
])
all_new[k] = q

# ── U2: Kinematics ──

k, q = add_qs("u2_l2.1", [
    ("Distance is a _____ quantity.", ["Vector", "*Scalar", "Negative", "Unit"], "No direction."),
    ("Displacement is a _____ quantity.", ["Scalar", "*Vector", "Dimensionless", "Constant"], "Has direction."),
    ("Speed = distance ÷ _____.", ["Distance", "*Time", "Acceleration", "Mass"], "Rate of distance."),
    ("Velocity = displacement ÷ _____.", ["Distance", "*Time", "Mass", "Area"], "Rate of displacement."),
    ("A car travels 100 m north then 60 m south. Distance =", ["40 m", "*160 m", "100 m", "60 m"], "Total path."),
    ("Displacement of that car:", ["160 m north", "*40 m north", "60 m south", "0 m"], "100 − 60 = 40 m north."),
    ("Average speed = total distance / total time. 200 m in 10 s:", ["2 m/s", "10 m/s", "*20 m/s", "200 m/s"], "200/10=20."),
    ("Average velocity can be _____ if displacement is zero (round trip).", ["Infinite", "Negative only", "*Zero", "Equal to speed"], "Zero displacement = zero avg velocity."),
    ("Instantaneous speed is the speed at a _____ moment.", ["Long", "*Single (specific)", "Average", "Final"], "One instant."),
    ("On a position-time graph, velocity is the _____ of the curve.", ["Area", "*Slope", "Intercept", "Curvature"], "Slope = velocity."),
    ("A horizontal line on a position-time graph means:", ["Constant velocity", "*Zero velocity (stationary)", "Constant acceleration", "Increasing speed"], "No change in position."),
    ("A straight line with positive slope on x-t graph means:", ["Decelerating", "*Constant positive velocity", "Zero velocity", "Accelerating"], "Constant rate of change."),
    ("SI unit of velocity is:", ["km/h", "mph", "*m/s", "cm/s"], "Meters per second."),
])
all_new[k] = q

k, q = add_qs("u2_l2.2", [
    ("Acceleration is the rate of change of:", ["Distance", "Position", "*Velocity", "Displacement"], "Δv/Δt."),
    ("SI unit of acceleration:", ["m/s", "*m/s²", "m²/s", "s/m"], "Meters per second squared."),
    ("A car goes from 0 to 20 m/s in 5 s. Acceleration =", ["100 m/s²", "*4 m/s²", "5 m/s²", "20 m/s²"], "20/5 = 4."),
    ("Negative acceleration (in the direction of motion) is called:", ["Speeding up", "*Deceleration (retardation)", "Uniform motion", "Free fall"], "Slowing down."),
    ("On a velocity-time graph, acceleration is the:", ["Area", "Intercept", "*Slope", "Zero line"], "Slope of v-t graph."),
    ("The area under a v-t graph gives:", ["Acceleration", "*Displacement", "Velocity", "Force"], "Area = displacement."),
    ("A horizontal line on a v-t graph indicates:", ["Accelerating", "*Constant velocity (zero acceleration)", "Stationary", "Decelerating"], "No change in velocity."),
    ("A straight line with positive slope on v-t graph means:", ["Constant velocity", "*Constant (uniform) acceleration", "Deceleration", "Zero motion"], "Constant positive acceleration."),
    ("If acceleration is constant, the motion is called:", ["Non-uniform", "*Uniformly accelerated", "Random", "Circular"], "Uniform acceleration."),
    ("An object decelerating from 30 m/s at 5 m/s² stops after:", ["3 s", "*6 s", "5 s", "30 s"], "30/5 = 6 s."),
    ("A negative velocity and negative acceleration means the object is:", ["Slowing down", "*Speeding up in the negative direction", "Stationary", "Changing direction"], "Both negative = speed increases."),
    ("Average acceleration = (v - u) / t. If u=10, v=30, t=4:", ["10", "*5 m/s²", "20", "40"], "(30-10)/4 = 5."),
    ("Instantaneous acceleration is the acceleration at a:", ["Large interval", "*Single instant", "Average point", "Final time"], "One moment."),
])
all_new[k] = q

k, q = add_qs("u2_l2.3", [
    ("A position-time graph with a curve (concave up) indicates:", ["Constant velocity", "*Increasing velocity (acceleration)", "Zero velocity", "Constant position"], "Curving up = accelerating."),
    ("The slope of a position-time graph gives:", ["Acceleration", "*Velocity", "Force", "Distance traveled"], "Slope of x-t = velocity."),
    ("The slope of a velocity-time graph gives:", ["Velocity", "Position", "*Acceleration", "Force"], "Slope of v-t = acceleration."),
    ("The area under a velocity-time graph gives:", ["Velocity", "*Displacement", "Acceleration", "Speed"], "Area = ∫v dt = displacement."),
    ("The area under an acceleration-time graph gives:", ["Displacement", "Position", "*Change in velocity", "Force"], "∫a dt = Δv."),
    ("A v-t graph that starts at zero and rises linearly represents:", ["Constant velocity", "*Constant acceleration from rest", "Deceleration", "No motion"], "Linear v-t from origin."),
    ("A position-time graph that is a straight line with zero slope means:", ["Uniform velocity", "*The object is at rest", "Uniform acceleration", "Deceleration"], "No change in position."),
    ("Negative slope on a position-time graph means:", ["Speeding up", "At rest", "*Moving in the negative direction", "Accelerating"], "Moving backward."),
    ("On a v-t graph, the object changes direction when velocity:", ["Is maximum", "*Crosses zero (changes sign)", "Is constant", "Equals acceleration"], "Sign change in velocity."),
    ("Two objects with the same v-t graph line have:", ["Different accelerations", "*The same velocity at every time (same motion)", "Different positions always", "Nothing in common"], "Same velocity-time behavior."),
    ("A parabolic position-time graph implies:", ["Constant velocity", "Zero velocity", "*Constant acceleration", "Constant jerk"], "x ∝ t² means constant a."),
    ("On a v-t graph, displacement from t=0 to t=5 with constant v=4 m/s equals:", ["4 m", "*20 m (area = 4 × 5)", "9 m", "1.25 m"], "Area of rectangle."),
    ("The instantaneous velocity at a point on an x-t graph is the slope of the:", ["Secant line", "*Tangent line at that point", "Average", "Chord"], "Tangent slope."),
])
all_new[k] = q

k, q = add_qs("u2_l2.4", [
    ("The kinematic equation v = u + at relates:", ["Position and time", "*Final velocity, initial velocity, acceleration, and time", "Force and mass", "Energy and work"], "Four variables."),
    ("s = ut + ½at² gives _____ as a function of time.", ["Velocity", "*Displacement", "Acceleration", "Force"], "Position equation."),
    ("v² = u² + 2as relates velocity to _____ without time.", ["Mass", "Force", "*Displacement", "Power"], "Eliminates time."),
    ("s = ½(u + v)t is useful when _____ is not given.", ["Time", "Velocity", "*Acceleration", "Displacement"], "No acceleration needed."),
    ("A ball starts from rest (u=0) and accelerates at 3 m/s² for 4 s. v =", ["3 m/s", "*12 m/s", "7 m/s", "0.75 m/s"], "v = 0 + 3(4) = 12."),
    ("Displacement in that case: s = 0 + ½(3)(16) =", ["48 m", "12 m", "*24 m", "6 m"], "½(3)(16) = 24."),
    ("A car traveling at 20 m/s brakes at −4 m/s². Distance to stop:", ["100 m", "80 m", "*50 m (v²=u²+2as → 0=400−8s → s=50)", "25 m"], "s = 400/8 = 50."),
    ("These equations assume _____ acceleration.", ["Variable", "Zero", "*Constant (uniform)", "Infinite"], "Constant acceleration only."),
    ("If u = 10, a = 2, t = 3: s = 10(3) + ½(2)(9) =", ["30", "39", "*39 (30 + 9)", "21"], "30 + 9 = 39 m."),
    ("If v = 25, u = 5, a = 2: time t = (v−u)/a =", ["15 s", "*10 s", "12.5 s", "5 s"], "(25−5)/2 = 10."),
    ("The sign of acceleration determines the direction of the:", ["Speed", "*Change in velocity", "Mass", "Distance"], "Direction of Δv."),
    ("u = 0, s = 100 m, a = 2 m/s²: v =", ["10 m/s", "*20 m/s (v² = 0 + 2(2)(100) = 400)", "200 m/s", "14.1 m/s"], "v = √400 = 20."),
    ("The equations of motion were formalized by:", ["Einstein", "*Galileo and Newton (classical mechanics)", "Bohr", "Faraday"], "Classical kinematics."),
])
all_new[k] = q

k, q = add_qs("u2_l2.5", [
    ("In free fall, the only force acting is:", ["Air resistance", "Friction", "*Gravity", "Normal force"], "Gravity only."),
    ("The acceleration due to gravity near Earth's surface is approximately:", ["8.9 m/s²", "10.8 m/s²", "*9.8 m/s² (≈ 10 m/s²)", "6.7 m/s²"], "g ≈ 9.8 m/s²."),
    ("In free fall, all objects accelerate at the same rate regardless of:", ["Shape", "*Mass (in a vacuum)", "Color", "Temperature"], "Galileo's insight."),
    ("A ball dropped from rest falls for 3 s. Distance = ½(9.8)(9) ≈", ["14.7 m", "29.4 m", "*44.1 m", "88.2 m"], "½(9.8)(9) = 44.1 m."),
    ("Its speed after 3 s: v = gt =", ["3 m/s", "19.6 m/s", "*29.4 m/s", "44.1 m/s"], "9.8 × 3 = 29.4 m/s."),
    ("A ball thrown upward with v₀ = 20 m/s reaches max height after:", ["1 s", "*≈ 2.04 s (20/9.8)", "3 s", "4 s"], "t = v₀/g."),
    ("Max height = v₀²/(2g) = 400/19.6 ≈", ["10.2 m", "*20.4 m", "40.8 m", "5.1 m"], "≈ 20.4 m."),
    ("At maximum height, the velocity is:", ["Maximum", "g", "*Zero", "Negative"], "Momentarily zero."),
    ("A projectile has _____ acceleration in the horizontal direction (ignoring air resistance).", ["g", "2g", "*Zero", "Variable"], "No horizontal force."),
    ("The horizontal velocity of a projectile remains:", ["Increasing", "*Constant", "Decreasing", "Zero"], "No horizontal acceleration."),
    ("The time of flight for a projectile launched horizontally from height h:", ["h/g", "*√(2h/g)", "2h/g", "h²/g"], "From s = ½gt²."),
    ("The range of a projectile launched at angle θ: R = v₀²sin(2θ)/g. Maximum range occurs at θ =", ["30°", "*45°", "60°", "90°"], "sin(90°) = 1 maximum."),
    ("A projectile's path is a:", ["Circle", "*Parabola", "Straight line", "Hyperbola"], "Parabolic trajectory."),
])
all_new[k] = q

k, q = add_qs("u2_l2.6", [
    ("Relative velocity is the velocity of one object as observed from:", ["A fixed point always", "*Another moving object (reference frame)", "Outer space", "The ground only"], "Different reference frames."),
    ("If car A moves at 60 km/h east and car B at 40 km/h east, the velocity of A relative to B is:", ["100 km/h east", "*20 km/h east", "20 km/h west", "40 km/h"], "60 − 40 = 20."),
    ("If they move in opposite directions (A east at 60, B west at 40), relative velocity of A w.r.t. B:", ["20 km/h", "*100 km/h east", "100 km/h west", "60 km/h"], "60 + 40 = 100."),
    ("A boat crossing a river must account for the river's:", ["Depth", "Width", "*Current velocity", "Temperature"], "Vector addition."),
    ("If a plane flies north at 200 m/s and wind blows east at 50 m/s, resultant speed:", ["250 m/s", "150 m/s", "*≈ 206 m/s (√(200²+50²))", "200 m/s"], "Pythagorean theorem."),
    ("A reference frame is:", ["Always at rest", "*A coordinate system from which motion is observed", "Only the ground", "Always inertial"], "Observer's coordinate system."),
    ("An inertial frame is one that:", ["Accelerates", "*Moves at constant velocity (no acceleration)", "Rotates", "Is always at rest"], "Non-accelerating frame."),
    ("Newton's laws hold in _____ reference frames.", ["All", "Rotating", "*Inertial", "Only one specific"], "Inertial frames."),
    ("The velocity of A relative to B: v_AB = v_A − v_B. If v_A = 30 m/s and v_B = −10 m/s:", ["20 m/s", "*40 m/s", "−40 m/s", "10 m/s"], "30 − (−10) = 40."),
    ("In 2D, relative velocity is found by _____ subtraction.", ["Scalar", "*Vector", "Matrix", "No"], "Vector difference."),
    ("A passenger on a train moving at 20 m/s throws a ball at 10 m/s forward. Ball's speed relative to ground:", ["10 m/s", "20 m/s", "*30 m/s", "200 m/s"], "20 + 10 = 30."),
    ("Galilean relativity applies when speeds are much less than:", ["Sound speed", "*Speed of light", "Earth's speed", "Mach 1"], "v << c."),
    ("If two frames move at constant velocity relative to each other, physics laws are:", ["Different", "*The same (principle of relativity)", "Invalid", "Reversed"], "Galilean relativity principle."),
])
all_new[k] = q

# ── U3: Forces & Newton's Laws ──

k, q = add_qs("u3_l3.1", [
    ("A force is a _____ that can change an object's state of motion.", ["Scalar", "*Push or pull (vector quantity)", "Energy", "Position"], "Force changes motion."),
    ("The SI unit of force is the:", ["Pound", "Dyne", "*Newton (N)", "Kilogram"], "1 N = 1 kg·m/s²."),
    ("1 Newton equals:", ["1 kg·m/s", "*1 kg·m/s²", "1 g·cm/s²", "1 kg²·m/s²"], "Definition."),
    ("A contact force requires:", ["Gravity", "*Physical contact between objects", "Magnetism", "Electric charge"], "Objects must touch."),
    ("A field (non-contact) force acts at a:", ["Short range only", "*Distance (without direct contact)", "Fixed point", "Zero range"], "Action at a distance."),
    ("Examples of contact forces include:", ["Gravity and magnetism", "*Friction, tension, normal force", "Electric and gravitational", "Nuclear and gravitational"], "Physical contact needed."),
    ("Examples of non-contact forces include:", ["Friction and tension", "*Gravity, electric, and magnetic forces", "Normal and air resistance", "Tension and spring"], "Act across distance."),
    ("A free-body diagram shows:", ["The object's shape", "*All forces acting on a single object", "All objects in the scene", "Only gravity"], "Force diagram."),
    ("In a free-body diagram, forces are drawn as arrows from the:", ["Ground", "*Object (center or surface)", "Sky", "Another object"], "Arrows from the body."),
    ("The net force is the _____ sum of all forces.", ["Scalar", "*Vector", "Algebraic (ignoring direction)", "Average"], "Vector addition."),
    ("If two forces of 5 N and 3 N act in the same direction, net force =", ["2 N", "15 N", "*8 N", "1.67 N"], "5 + 3 = 8 N."),
    ("If they act in opposite directions, net force =", ["8 N", "*2 N (in the direction of the larger force)", "15 N", "0 N"], "5 − 3 = 2 N."),
    ("When net force = 0, the object is in:", ["Motion always", "*Equilibrium (at rest or constant velocity)", "Free fall", "Acceleration"], "Zero net force = equilibrium."),
])
all_new[k] = q

k, q = add_qs("u3_l3.2", [
    ("Newton's First Law is also called the law of:", ["Acceleration", "*Inertia", "Action-reaction", "Gravitation"], "Law of inertia."),
    ("An object at rest stays at rest unless acted on by a:", ["Balanced force", "*Net (unbalanced) external force", "Contact force only", "Gravitational force only"], "Unbalanced force needed."),
    ("An object in motion continues at constant velocity unless:", ["Friction always stops it", "*A net external force acts on it", "It runs out of energy", "It reaches a boundary"], "Needs net force to change."),
    ("Inertia is the tendency of an object to resist changes in:", ["Shape", "Size", "*Motion (velocity)", "Color"], "Resist velocity change."),
    ("Mass is a measure of:", ["Weight", "Volume", "*Inertia", "Density"], "More mass = more inertia."),
    ("A heavier object has _____ inertia.", ["Less", "*More (greater)", "The same", "Zero"], "Mass ∝ inertia."),
    ("In deep space (no gravity, no friction), a pushed object:", ["Slows down", "Speeds up forever", "*Moves at constant velocity indefinitely", "Stops immediately"], "No force to change it."),
    ("A passenger lurches forward when a bus brakes because of:", ["Gravity", "*Inertia (body tends to keep moving)", "Magnetism", "Buoyancy"], "Body resists velocity change."),
    ("Newton's First Law applies in _____ reference frames.", ["Rotating", "Accelerating", "*Inertial (non-accelerating)", "All"], "Only inertial frames."),
    ("If all forces on an object are balanced, acceleration =", ["g", "9.8", "*0", "Varies"], "No net force, no acceleration."),
    ("A book on a table stays at rest because:", ["Gravity is zero", "*Normal force balances gravity (net force = 0)", "It has no mass", "It is glued"], "Forces balanced."),
    ("Galileo's thought experiment involved a frictionless surface showing that motion continues:", ["Only with force", "*Indefinitely without friction", "For a limited time", "In circles"], "No friction = eternal motion."),
    ("The First Law is a special case of the Second Law when F_net =", ["ma", "mg", "*0", "∞"], "F=0 → a=0."),
])
all_new[k] = q

k, q = add_qs("u3_l3.3", [
    ("Newton's Second Law: F = ma. Force is proportional to:", ["Velocity", "*Acceleration (for constant mass)", "Position", "Time"], "F ∝ a."),
    ("If mass doubles and force stays the same, acceleration:", ["Doubles", "*Halves", "Stays the same", "Quadruples"], "a = F/m."),
    ("A 5 kg object with net force 20 N: acceleration =", ["100 m/s²", "4 m/s²", "*4 m/s² (20/5)", "25 m/s²"], "F/m = 4."),
    ("To accelerate a 2 kg mass at 3 m/s², force needed =", ["1.5 N", "5 N", "*6 N", "0.67 N"], "2 × 3 = 6 N."),
    ("Weight W = mg. A 70 kg person weighs:", ["70 N", "7 N", "*686 N (70 × 9.8)", "700 N"], "70 × 9.8 = 686 N."),
    ("Mass is measured in _____, weight in _____.", ["Newtons, kg", "*kg, Newtons", "Newtons, Newtons", "kg, kg"], "Mass=kg, weight=N."),
    ("On the Moon (g ≈ 1.6 m/s²), a 70 kg person weighs:", ["686 N", "70 N", "*112 N", "11.2 N"], "70 × 1.6 = 112 N."),
    ("F = ma applies to the _____ force on an object.", ["Largest", "Smallest", "*Net (resultant)", "Only gravitational"], "Net force."),
    ("A 10 kg object on a frictionless surface with 50 N applied: a =", ["500 m/s²", "*5 m/s²", "0.2 m/s²", "10 m/s²"], "50/10 = 5."),
    ("A 1000 kg car accelerates at 2 m/s². The net force is:", ["500 N", "2000 N", "*2000 N (1000 × 2)", "200 N"], "1000 × 2 = 2000 N."),
    ("F = ma can also be written as F = dp/dt where p is:", ["Position", "Power", "*Momentum (the more general form)", "Pressure"], "General form."),
    ("If two forces F₁=10 N right and F₂=4 N left act on a 3 kg mass: a =", ["14/3 m/s²", "*2 m/s² right (6/3)", "4.67 m/s²", "10/3 m/s²"], "Net = 6 N, a = 2."),
    ("An object in free fall has a = g because the only force is _____ = mg.", ["Friction", "Normal force", "*Gravity (weight)", "Tension"], "Gravity alone."),
])
all_new[k] = q

k, q = add_qs("u3_l3.4", [
    ("Newton's Third Law: For every action, there is an equal and _____ reaction.", ["Parallel", "Identical", "*Opposite", "Delayed"], "Equal and opposite."),
    ("Action-reaction forces act on _____ objects.", ["The same", "*Different", "No", "Three"], "Different objects."),
    ("When you push a wall, the wall pushes _____ on you.", ["Harder", "Not at all", "*Equally hard in the opposite direction", "Softer"], "Equal and opposite."),
    ("A book on a table: gravity pulls the book down. The reaction to this force is:", ["Normal force on book", "*Book pulling Earth upward", "Friction on book", "Table pushing floor"], "Book pulls Earth up."),
    ("The normal force on the book is NOT the reaction to gravity because:", ["It's stronger", "*Both act on the same object (the book) — action-reaction pairs act on different objects", "It's a contact force", "It acts upward"], "Same object ≠ action-reaction pair."),
    ("When you jump, you push the ground down and the ground pushes you:", ["Down", "*Up (allowing you to rise)", "Sideways", "Not at all"], "Ground pushes you up."),
    ("A rocket propels forward by pushing exhaust:", ["Forward", "*Backward (and exhaust pushes rocket forward)", "Upward", "Not at all"], "Third law propulsion."),
    ("Action-reaction forces are always:", ["Unbalanced on the same object", "*Equal in magnitude", "Different in magnitude", "In the same direction"], "Always equal."),
    ("Why don't action-reaction forces cancel? Because they act on:", ["The same point", "*Different objects", "The same object", "Nothing"], "Different objects."),
    ("A horse pulls a cart. The cart pulls the horse backward with equal force. The cart moves because:", ["The forces are unequal", "*The horse also pushes the ground, and the ground pushes the horse forward (net force on the horse is forward)", "Newton's Third Law is wrong", "The cart is light"], "Consider forces ON the horse from ground."),
    ("Tension in a rope is a Third Law pair between:", ["Two ropes", "*The rope and each object it's attached to", "Gravity and the rope", "The floor and the object"], "Each end-pair."),
    ("If you push a 10 kg box with 50 N, the box pushes you with:", ["0 N", "10 N", "*50 N", "100 N"], "Equal and opposite."),
    ("Newton's Third Law is valid:", ["Only at rest", "Only during motion", "*Always (at rest and in motion)", "Only in a vacuum"], "Universal law."),
])
all_new[k] = q

k, q = add_qs("u3_l3.5", [
    ("Friction is a force that _____ relative motion between surfaces.", ["Increases", "*Opposes (or tends to oppose)", "Is perpendicular to", "Has no effect on"], "Opposes relative motion."),
    ("Static friction acts when surfaces are _____ relative to each other.", ["Moving", "*Not moving (no sliding)", "Accelerating always", "In free fall"], "No relative motion."),
    ("Kinetic friction acts when surfaces are:", ["At rest", "*Sliding against each other", "Not touching", "In equilibrium only"], "Sliding contact."),
    ("The maximum static friction: fₛ(max) = μₛN, where N is the:", ["Weight", "Mass", "*Normal force", "Tension"], "Normal force."),
    ("Kinetic friction: fₖ = μₖN. Usually μₖ is _____ μₛ.", ["Greater than", "Equal to", "*Less than", "Unrelated to"], "μₖ < μₛ typically."),
    ("A 10 kg box on a surface with μₖ = 0.3. Normal force = mg = 98 N. Friction =", ["30 N", "*29.4 N (0.3 × 98)", "9.8 N", "3 N"], "0.3 × 98 = 29.4 N."),
    ("Friction does NOT depend on:", ["Normal force", "Surface roughness", "*Contact area (for most cases)", "Materials"], "Independent of area."),
    ("Tension in a rope is a _____ force.", ["Compressive", "*Pulling (tensile)", "Rotational", "Gravitational"], "Rope pulls."),
    ("For an ideal (massless) rope, tension is _____ throughout.", ["Variable", "*The same (constant)", "Zero", "Maximum at the center"], "Uniform tension."),
    ("If you pull a 5 kg block with 30 N on a frictionless surface, tension in the rope =", ["5 N", "35 N", "*30 N", "0 N"], "The applied force."),
    ("On an Atwood machine with masses m₁ > m₂, the heavier mass accelerates:", ["Upward", "*Downward", "Sideways", "Not at all"], "Heavier goes down."),
    ("The coefficient of friction is:", ["A force", "*A dimensionless ratio", "Measured in Newtons", "Always greater than 1"], "No units."),
    ("Air resistance is a type of:", ["Static friction", "Tension", "*Fluid friction (drag)", "Normal force"], "Drag force."),
])
all_new[k] = q

k, q = add_qs("u3_l3.6", [
    ("The normal force is _____ to the surface.", ["Parallel", "*Perpendicular", "At 45°", "Tangent"], "Always perpendicular."),
    ("On a flat horizontal surface, normal force equals:", ["Mass", "*Weight (mg) when no other vertical forces act", "Friction", "Zero"], "N = mg."),
    ("On an inclined plane at angle θ, the component of gravity along the plane:", ["mg cos θ", "*mg sin θ", "mg", "mg tan θ"], "Parallel component."),
    ("The component of gravity perpendicular to the incline:", ["mg sin θ", "*mg cos θ", "mg", "mg tan θ"], "Normal component."),
    ("Normal force on an incline = _____.", ["mg", "mg sin θ", "*mg cos θ", "mg tan θ"], "Balances perpendicular gravity."),
    ("An object slides down a frictionless incline at angle θ with acceleration:", ["g", "g cos θ", "*g sin θ", "g tan θ"], "a = g sin θ."),
    ("If friction is present on an incline, acceleration = g sin θ − _____.", ["g cos θ", "*μₖg cos θ", "mg sin θ", "μₖg sin θ"], "Friction = μₖN = μₖmg cos θ."),
    ("A box on a 30° incline (no friction): a = g sin 30° = 9.8 × 0.5 =", ["9.8 m/s²", "*4.9 m/s²", "2.45 m/s²", "0 m/s²"], "4.9 m/s²."),
    ("If an extra force pushes down on the box on a flat surface, normal force:", ["Decreases", "*Increases (N = mg + F_push)", "Stays the same", "Becomes zero"], "More force into surface."),
    ("If a force pulls up on the box (on a flat surface), normal force:", ["Increases", "*Decreases (N = mg − F_pull)", "Stays the same", "Doubles"], "Less force into surface."),
    ("The normal force can be zero if the object:", ["Is heavy", "*Leaves the surface (airborne)", "Is at rest", "Has high friction"], "No contact = no normal force."),
    ("On a steep enough incline, an object starts sliding when mg sin θ exceeds:", ["mg cos θ", "*μₛ mg cos θ (maximum static friction)", "The normal force alone", "Zero"], "Overcome friction."),
    ("The angle at which sliding begins is called the angle of _____.", ["Elevation", "*Repose", "Incidence", "Reflection"], "Angle of repose."),
])
all_new[k] = q

k, q = add_qs("u3_l3.7", [
    ("Circular motion at constant speed is called:", ["Linear motion", "*Uniform circular motion", "Projectile motion", "Random motion"], "Constant speed in a circle."),
    ("In uniform circular motion, the direction of velocity _____ changes.", ["Never", "*Constantly (it's always tangent to the circle)", "Rarely", "Only at the top"], "Always changing direction."),
    ("Centripetal acceleration points toward the:", ["Outside", "*Center of the circle", "Tangent", "Velocity direction"], "Center-seeking."),
    ("Centripetal acceleration ac = v²/r. If v = 10 m/s and r = 5 m:", ["2 m/s²", "50 m/s²", "*20 m/s²", "0.5 m/s²"], "100/5 = 20."),
    ("Centripetal force Fc = mv²/r is provided by:", ["A new type of force", "*Whatever force directs toward the center (gravity, tension, friction, etc.)", "Only gravity", "Only tension"], "Not a new force."),
    ("A car turning on a flat road: centripetal force is provided by:", ["Gravity", "Normal force", "*Friction", "Air resistance"], "Friction toward center."),
    ("A satellite in orbit: centripetal force is provided by:", ["Engines", "Friction", "*Gravity", "Tension"], "Gravity."),
    ("A ball on a string in horizontal circle: centripetal force from:", ["Gravity", "*Tension in the string", "Weight", "Air resistance"], "String tension."),
    ("Period T = time for one revolution. For T = 2 s and r = 3 m, speed v = 2πr/T =", ["6π m/s", "*3π m/s", "2π m/s", "π m/s"], "2π(3)/2 = 3π."),
    ("Frequency f = 1/T. If T = 0.5 s, f =", ["0.5 Hz", "*2 Hz", "1 Hz", "5 Hz"], "1/0.5 = 2."),
    ("Angular velocity ω = 2π/T = 2πf. Units:", ["m/s", "*rad/s", "Hz", "m/s²"], "Radians per second."),
    ("If the string breaks, the ball flies off:", ["Toward the center", "In a spiral", "*Tangent to the circle (in a straight line)", "Outward radially"], "Tangent direction."),
    ("On a banked curve, the _____ component of the normal force provides centripetal force.", ["Vertical", "*Horizontal", "Tangential", "Frictional"], "Horizontal component."),
])
all_new[k] = q

k, q = add_qs("u3_l3.8", [
    ("A non-inertial frame is one that:", ["Moves at constant velocity", "*Accelerates (including rotating)", "Is always at rest", "Is in deep space"], "Accelerating frame."),
    ("In a non-inertial frame, Newton's laws don't directly apply without adding:", ["More mass", "*Pseudo-forces (fictitious forces)", "Real forces", "Energy"], "Fictitious forces needed."),
    ("A pseudo-force is:", ["A real interaction", "*Not caused by any physical interaction — appears due to the acceleration of the frame", "Gravity", "Friction"], "Apparent, not real."),
    ("If you're in an accelerating car braking suddenly, you feel pushed:", ["Backward", "*Forward (the pseudo-force is opposite to the frame's acceleration)", "Upward", "Downward"], "Forward pseudo-force."),
    ("In a rotating frame, the outward pseudo-force is called:", ["Coriolis force", "*Centrifugal force", "Gravity", "Tension"], "Outward apparent force."),
    ("Centrifugal force is:", ["A real force", "*A fictitious force in a rotating frame", "Always present", "Only in gravity"], "Not a real interaction."),
    ("The Coriolis force affects objects moving in a:", ["Non-rotating frame", "*Rotating frame (like Earth)", "Linear frame only", "Vacuum only"], "Rotating reference frame."),
    ("The Coriolis effect causes large-scale deflection of wind and ocean currents on:", ["The Moon", "Mars", "*Earth", "The Sun"], "Earth's rotation."),
    ("In the Northern Hemisphere, the Coriolis effect deflects moving objects to the:", ["Left", "*Right", "Straight ahead", "Backward"], "Right deflection."),
    ("The Coriolis force is proportional to:", ["Position", "Acceleration of the object", "*The object's velocity and the angular velocity of the frame", "Mass only"], "F_cor ∝ v × ω."),
    ("In an elevator accelerating upward, you feel:", ["Lighter", "*Heavier (apparent weight increases)", "Normal", "Weightless"], "Greater apparent weight."),
    ("In an elevator in free fall, apparent weight =", ["mg", "2mg", "*0 (weightlessness)", "mg/2"], "Zero apparent weight."),
    ("Pseudo-forces are essential for solving problems in _____ frames.", ["Inertial", "*Non-inertial (accelerating)", "All", "No"], "Non-inertial frame analysis."),
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

print(f"✅ Physics U1-U3: expanded {len(all_new)} lessons")
