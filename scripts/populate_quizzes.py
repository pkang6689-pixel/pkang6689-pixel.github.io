"""
Replace placeholder quiz content in all 73 Physics Quiz.html files
with actual lesson-specific multiple-choice questions (7 per lesson).
Also fixes:
  - "Back to Chemistry" → "Back to Physics" with correct link
  - "Next Lesson: 1.2" → correct next lesson with proper filename
"""
import os, re, glob

# ── Ordered lesson list for "Next Lesson" navigation ──────────────────
LESSON_ORDER = [
    "1.1","1.2","1.3","1.4","1.5","1.6",
    "2.1","2.2","2.3","2.4","2.5","2.6",
    "3.1","3.2","3.3","3.4","3.5","3.6","3.7","3.8",
    "4.1","4.2","4.3","4.4","4.5","4.6",
    "5.1","5.2","5.3","5.4","5.5","5.6",
    "6.1","6.2","6.3","6.4","6.5","6.6",
    "7.1","7.2","7.3","7.4","7.5","7.6","7.7","7.8",
    "8.1","8.2","8.3","8.4","8.5","8.6",
    "9.1","9.2","9.3","9.4","9.5","9.6",
    "10.1","10.2","10.3","10.4","10.5","10.6","10.7","10.8","10.9",
    "11.1","11.2","11.3","11.4","11.5","11.6",
]

def get_next_lesson(current):
    idx = LESSON_ORDER.index(current)
    if idx + 1 < len(LESSON_ORDER):
        return LESSON_ORDER[idx + 1]
    return None  # last lesson

# ── Quiz content: list of (question, correct, [wrong1, wrong2, wrong3]) ──
QUIZZES = {
"1.1": [
    ("What is a physical quantity?", "A property that can be measured with a number and a unit", ["A property that can only be observed", "A mathematical constant", "An abstract concept with no measurement"]),
    ("How many SI base quantities are there?", "Seven", ["Five", "Ten", "Three"]),
    ("What is the SI base unit for mass?", "Kilogram (kg)", ["Gram (g)", "Pound (lb)", "Newton (N)"]),
    ("What is a derived quantity?", "A quantity formed by combining base quantities", ["A quantity that cannot be measured", "A base unit of the SI system", "A unit with no physical meaning"]),
    ("What is the SI base unit for time?", "Second (s)", ["Minute (min)", "Hour (hr)", "Millisecond (ms)"]),
    ("What happens when you add two values with different units?", "The result is meaningless", ["The units cancel out", "You always get the larger unit", "The result takes the first unit"]),
    ("Which of the following is a derived unit?", "Newton (N)", ["Kilogram (kg)", "Second (s)", "Meter (m)"]),
],
"1.2": [
    ("What does the prefix 'kilo' mean?", "10³ (one thousand)", ["10⁶ (one million)", "10⁻³ (one thousandth)", "10² (one hundred)"]),
    ("What does the prefix 'milli' mean?", "10⁻³ (one thousandth)", ["10⁻⁶ (one millionth)", "10³ (one thousand)", "10⁻² (one hundredth)"]),
    ("Convert 5.2 km to meters.", "5200 m", ["52 m", "520 m", "0.52 m"]),
    ("What does the prefix 'mega' mean?", "10⁶ (one million)", ["10³ (one thousand)", "10⁹ (one billion)", "10⁻⁶ (one millionth)"]),
    ("What does the prefix 'nano' mean?", "10⁻⁹ (one billionth)", ["10⁻⁶ (one millionth)", "10⁻³ (one thousandth)", "10⁻¹² (one trillionth)"]),
    ("Convert 350 mg to grams.", "0.35 g", ["3.5 g", "35 g", "0.035 g"]),
    ("What does the prefix 'centi' mean?", "10⁻² (one hundredth)", ["10⁻³ (one thousandth)", "10⁻¹ (one tenth)", "10² (one hundred)"]),
],
"1.3": [
    ("What is a scalar quantity?", "A quantity with only magnitude", ["A quantity with magnitude and direction", "A quantity with no units", "A quantity that only describes direction"]),
    ("Which of the following is a vector quantity?", "Displacement", ["Speed", "Mass", "Temperature"]),
    ("Is speed a scalar or vector?", "Scalar", ["Vector", "Both", "Neither"]),
    ("Is velocity a scalar or vector?", "Vector", ["Scalar", "Both", "Neither"]),
    ("How are vectors added?", "Using vector addition (tip-to-tail or component method)", ["By simple arithmetic addition", "By multiplying their magnitudes", "By subtracting the smaller from the larger"]),
    ("Which of the following is a scalar quantity?", "Temperature", ["Force", "Velocity", "Displacement"]),
    ("Can the resultant of two vectors be less than either vector's magnitude?", "Yes, when the vectors partially cancel each other", ["No, the resultant is always larger", "Only if the vectors are equal", "Only for perpendicular vectors"]),
],
"1.4": [
    ("What is accuracy?", "How close a measurement is to the true value", ["How close repeated measurements are to each other", "The number of significant figures", "The smallest division on a scale"]),
    ("What is precision?", "How close repeated measurements are to each other", ["How close a measurement is to the true value", "The number of decimal places", "The range of the instrument"]),
    ("How many significant figures does 0.0045 have?", "Two", ["Four", "Three", "One"]),
    ("What is the sig fig rule for multiplication?", "Result has the same number of sig figs as the least precise factor", ["Result has the most sig figs of any factor", "Always round to 2 sig figs", "Add the sig figs of all factors"]),
    ("Can a measurement be precise but not accurate?", "Yes — consistently giving the same wrong value", ["No — precision guarantees accuracy", "Only for digital instruments", "Only for very large values"]),
    ("Are leading zeros significant?", "No", ["Yes", "Only in scientific notation", "Only after a decimal point"]),
    ("How many significant figures does 2.50 have?", "Three", ["Two", "Four", "One"]),
],
"1.5": [
    ("What is dimensional analysis?", "A technique using dimensions to check equations and convert units", ["A way to draw 3D graphs", "A method for calculating mass", "A type of laboratory experiment"]),
    ("What must be true for a physics equation to be valid dimensionally?", "Both sides must have the same dimensions", ["Both sides must have the same numbers", "The left side must be larger", "Units don't matter in equations"]),
    ("What are the dimensions of velocity?", "[L][T]⁻¹", ["[M][L][T]⁻²", "[L]²[T]⁻¹", "[M][T]⁻¹"]),
    ("What are the dimensions of force?", "[M][L][T]⁻²", ["[M][L][T]⁻¹", "[L][T]⁻²", "[M][L]²[T]⁻²"]),
    ("Can dimensional analysis determine dimensionless constants?", "No", ["Yes, always", "Only for simple equations", "Only for constants greater than 1"]),
    ("What is a conversion factor?", "A fraction equal to 1 used to convert between units", ["A number that changes the laws of physics", "A constant that appears in every equation", "The ratio of two different physical quantities"]),
    ("What are the dimensions of energy?", "[M][L]²[T]⁻²", ["[M][L][T]⁻²", "[L][T]⁻¹", "[M][L]²[T]⁻¹"]),
],
"1.6": [
    ("What is a systematic error?", "A consistent error that shifts all measurements in the same direction", ["A random fluctuation in measurements", "An error caused by the observer", "An error that averages out over many trials"]),
    ("Random errors affect which property?", "Precision", ["Accuracy", "Units", "Dimensions"]),
    ("How do you calculate percentage uncertainty?", "(Absolute uncertainty / measured value) × 100%", ["(Measured value / absolute uncertainty) × 100%", "Absolute uncertainty × measured value", "Absolute uncertainty − measured value"]),
    ("How do uncertainties combine in addition?", "Add the absolute uncertainties", ["Add the percentage uncertainties", "Multiply the uncertainties", "Take the larger uncertainty"]),
    ("How do uncertainties combine in multiplication?", "Add the percentage uncertainties", ["Add the absolute uncertainties", "Multiply the absolute uncertainties", "Subtract the uncertainties"]),
    ("If x has 2% uncertainty, what is the uncertainty in x³?", "6%", ["2%", "8%", "3%"]),
    ("Systematic errors affect which property?", "Accuracy", ["Precision", "Significant figures", "Sample size"]),
],
"2.1": [
    ("What is the difference between distance and displacement?", "Distance is total path length (scalar); displacement is straight-line with direction (vector)", ["They are the same thing", "Distance has direction; displacement does not", "Displacement is always larger than distance"]),
    ("What is velocity?", "Rate of change of displacement", ["Rate of change of distance", "Rate of change of acceleration", "Distance traveled per unit mass"]),
    ("On a position-time graph, what does the slope represent?", "Velocity", ["Acceleration", "Distance", "Force"]),
    ("Can average velocity equal zero for a moving object?", "Yes — if it returns to its starting position", ["No, never", "Only if it moves in a circle", "Only at very high speeds"]),
    ("What is instantaneous velocity?", "Velocity at a specific instant in time", ["The average of all velocities", "The maximum velocity reached", "Velocity measured over one hour"]),
    ("How is average speed calculated?", "Total distance divided by total time", ["Displacement divided by time", "Final speed minus initial speed", "Distance times time"]),
    ("Is it possible for speed to be constant while velocity changes?", "Yes — for example, in circular motion", ["No, speed and velocity are the same", "Only at the speed of light", "Only when acceleration is zero"]),
],
"2.2": [
    ("What is acceleration?", "The rate of change of velocity with respect to time", ["The rate of change of distance", "The speed of an object", "The total displacement"]),
    ("What is the SI unit of acceleration?", "m/s²", ["m/s", "N", "kg·m/s"]),
    ("What does the slope of a velocity-time graph represent?", "Acceleration", ["Velocity", "Displacement", "Force"]),
    ("What does the area under a velocity-time graph represent?", "Displacement", ["Acceleration", "Speed", "Force"]),
    ("Can an object have zero velocity but nonzero acceleration?", "Yes — like a ball at the top of its trajectory", ["No, that is impossible", "Only in outer space", "Only for very heavy objects"]),
    ("If you double the net force on an object (constant mass), acceleration:", "Doubles", ["Halves", "Stays the same", "Quadruples"]),
    ("Is acceleration a scalar or a vector?", "Vector", ["Scalar", "Both", "Neither"]),
],
"2.3": [
    ("On a position-time graph, what does a horizontal line mean?", "The object is at rest", ["The object has constant velocity", "The object is accelerating", "The object is decelerating"]),
    ("On a v-t graph, what does a horizontal line mean?", "Constant velocity (zero acceleration)", ["The object is at rest", "Constant acceleration", "The object is decelerating"]),
    ("What shape does constant acceleration produce on a position-time graph?", "A parabola", ["A straight line", "A horizontal line", "A circle"]),
    ("How do you go from an x-t graph to a v-t graph?", "Take the slope (differentiate)", ["Take the area (integrate)", "Multiply by time", "Add a constant"]),
    ("On an a-t graph, what does the area under the curve represent?", "Change in velocity (Δv)", ["Displacement", "Acceleration", "Force"]),
    ("On a position-time graph, what does a curved line mean?", "Changing velocity (acceleration)", ["Constant velocity", "The object is at rest", "The object is moving backward"]),
    ("How do you go from a v-t graph to an x-t graph?", "Take the area (integrate)", ["Take the slope", "Divide by time", "Square the values"]),
],
"2.4": [
    ("Which equation is v = u + at?", "A kinematic (SUVAT) equation for constant acceleration", ["Newton's Second Law", "The work-energy theorem", "The impulse-momentum theorem"]),
    ("When do the kinematic equations apply?", "Only when acceleration is constant", ["Always", "Only in free fall", "Only for objects at rest"]),
    ("How many SUVAT knowns do you need to solve a problem?", "Three", ["Two", "Four", "Five"]),
    ("A car starts from rest. What is u?", "0 m/s", ["9.8 m/s", "Unknown", "Equal to v"]),
    ("What is the formula s = ut + ½at²  used for?", "Finding displacement given initial velocity, acceleration, and time", ["Finding force", "Finding energy", "Finding momentum"]),
    ("What does v² = u² + 2as allow you to find without knowing?", "Time", ["Mass", "Force", "Distance"]),
    ("What is the acceleration due to gravity (g)?", "9.8 m/s² downward", ["9.8 m/s upward", "10 N/kg", "3 × 10⁸ m/s²"]),
],
"2.5": [
    ("What is free fall?", "Motion under gravity alone with no air resistance", ["Falling with a parachute", "Any downward motion", "Motion at terminal velocity"]),
    ("In projectile motion, horizontal acceleration is:", "Zero", ["9.8 m/s²", "Equal to vertical acceleration", "Depends on launch angle"]),
    ("At what launch angle is the range of a projectile maximized?", "45°", ["30°", "60°", "90°"]),
    ("What shape does a projectile's path trace?", "A parabola", ["A straight line", "A circle", "An ellipse"]),
    ("At the top of a projectile's path, what is the vertical velocity?", "Zero", ["Maximum", "Equal to horizontal velocity", "9.8 m/s"]),
    ("Do heavier objects fall faster in free fall (no air resistance)?", "No — all objects accelerate at g", ["Yes, heavier objects fall faster", "Only near Earth's surface", "It depends on their shape"]),
    ("What is the formula for time of flight of a projectile?", "T = 2v₀ sin θ / g", ["T = v₀ / g", "T = v₀ cos θ / g", "T = 2v₀ / g"]),
],
"2.6": [
    ("What is a reference frame?", "A coordinate system used to measure position and motion", ["A type of laboratory equipment", "A fixed point in space", "A unit of measurement"]),
    ("How do you find the velocity of A relative to B?", "v_AB = v_A − v_B", ["v_AB = v_A + v_B", "v_AB = v_A × v_B", "v_AB = v_A / v_B"]),
    ("Two cars moving at 60 and 40 km/h in the same direction: relative velocity?", "20 km/h", ["100 km/h", "50 km/h", "2400 km/h"]),
    ("What is an inertial frame?", "A non-accelerating frame where Newton's laws apply directly", ["Any frame attached to Earth", "A rotating frame", "A frame moving faster than light"]),
    ("When does Galilean relativity break down?", "At speeds close to the speed of light", ["At very low speeds", "Only in water", "Never"]),
    ("Why does rain appear angled when you run?", "Your motion changes the rain's velocity relative to you", ["The wind always blows horizontally", "Rain never falls straight", "It's an optical illusion"]),
    ("In a river crossing, the boat's ground velocity is found by:", "Vector sum of boat velocity relative to water and water velocity relative to ground", ["Subtracting all velocities", "Using only the boat's speed", "Dividing boat speed by current speed"]),
],
"3.1": [
    ("What is the SI unit of force?", "Newton (N)", ["Joule (J)", "Watt (W)", "Pascal (Pa)"]),
    ("What is a free-body diagram?", "A diagram showing all forces on a single object as arrows", ["A diagram of an object in free fall", "A graph of force vs. time", "A picture of an object with no forces"]),
    ("What is the net force?", "The vector sum of all forces acting on an object", ["The largest force acting on an object", "The force of gravity", "Any single force on the object"]),
    ("What happens when the net force on an object is zero?", "The object is in equilibrium — no acceleration", ["The object must be at rest", "The object must be moving", "The object accelerates"]),
    ("Is force a scalar or vector?", "Vector", ["Scalar", "Both", "Neither"]),
    ("What is a contact force?", "A force requiring physical touch", ["A force acting at a distance", "A force from gravity", "An electromagnetic force"]),
    ("What is 1 Newton in base units?", "1 kg·m/s²", ["1 kg·m/s", "1 kg·m²/s²", "1 kg/m·s²"]),
],
"3.2": [
    ("What is Newton's First Law also called?", "The Law of Inertia", ["The Law of Acceleration", "The Law of Action-Reaction", "The Law of Gravity"]),
    ("What is inertia?", "The resistance of an object to changes in its state of motion", ["The force needed to move an object", "The speed of an object", "The weight of an object"]),
    ("If no net force acts on a moving object, it will:", "Continue at constant velocity", ["Slow down and stop", "Speed up", "Change direction"]),
    ("What is static equilibrium?", "An object at rest with ΣF = 0", ["An object accelerating", "An object moving at constant speed", "An object in free fall"]),
    ("A bus brakes suddenly. Why do passengers lurch forward?", "Their bodies' inertia keeps them moving forward", ["The bus pushes them forward", "Gravity pulls them forward", "Air resistance pushes them"]),
    ("What determines how much inertia an object has?", "Its mass", ["Its speed", "Its color", "Its temperature"]),
    ("Can an object be in equilibrium while moving?", "Yes — this is called dynamic equilibrium", ["No, equilibrium requires rest", "Only in space", "Only at very low speeds"]),
],
"3.3": [
    ("State Newton's Second Law.", "ΣF = ma", ["F = mv", "F = mgh", "F = kx"]),
    ("If you double the net force on an object (mass constant), acceleration:", "Doubles", ["Halves", "Stays the same", "Quadruples"]),
    ("What is the weight of a 70 kg person on Earth?", "About 686 N", ["70 N", "700 kg", "7 N"]),
    ("What is the difference between mass and weight?", "Mass is amount of matter (kg); weight is gravitational force (N)", ["They are the same thing", "Mass is measured in Newtons", "Weight is measured in kilograms"]),
    ("Does mass change with location?", "No — mass is constant", ["Yes — mass changes with gravity", "Only on the Moon", "Only in space"]),
    ("A 5 kg object accelerates at 3 m/s². What is the net force?", "15 N", ["8 N", "1.67 N", "150 N"]),
    ("Acceleration is always in which direction relative to net force?", "The same direction", ["The opposite direction", "Perpendicular", "It varies"]),
],
"3.4": [
    ("State Newton's Third Law.", "For every action there is an equal and opposite reaction", ["Objects at rest stay at rest", "F = ma", "Energy is conserved"]),
    ("Action-reaction pairs act on how many objects?", "Two different objects", ["The same object", "Three objects", "It depends on the situation"]),
    ("Why don't action-reaction pairs cancel each other?", "Because they act on different objects", ["Because one is always larger", "They do cancel", "Because of friction"]),
    ("If a truck hits a small car, which experiences the greater force?", "Both experience the same force", ["The truck", "The car", "Neither — no force occurs"]),
    ("How does a rocket propel itself in space?", "It expels exhaust gases backward; the gases push the rocket forward", ["It pushes against the air", "It uses magnetic fields", "Solar wind pushes it"]),
    ("Does Newton's Third Law have exceptions?", "No — it always applies", ["Yes, not in space", "Yes, not for gravity", "Yes, not at high speeds"]),
    ("You push a wall. What is the reaction force?", "The wall pushes back on you with equal and opposite force", ["Gravity pulls you down", "Friction pushes you sideways", "Nothing — walls cannot exert force"]),
],
"3.5": [
    ("Which is larger: static or kinetic friction coefficient?", "Static friction coefficient (μₛ)", ["Kinetic friction coefficient (μₖ)", "They are always equal", "It depends on the surface"]),
    ("What is the normal force?", "The perpendicular contact force a surface exerts on an object", ["The force of gravity", "The friction force", "The applied force"]),
    ("What is tension?", "The pulling force transmitted through a string, rope, or cable", ["A pushing force", "The force of gravity", "Air resistance"]),
    ("If N = 50 N and μₖ = 0.3, what is the kinetic friction force?", "15 N", ["50 N", "150 N", "0.006 N"]),
    ("Why does it take more force to start an object moving than to keep it moving?", "Static friction (max) is greater than kinetic friction", ["Gravity increases at rest", "Kinetic friction is larger", "Objects gain mass at rest"]),
    ("In an ideal pulley, what happens to tension?", "It changes direction but not magnitude", ["It doubles", "It halves", "It becomes zero"]),
    ("For connected objects with a taut string, what do they share?", "The same acceleration", ["The same mass", "The same velocity always", "The same force"]),
],
"3.6": [
    ("What is the component of weight parallel to an incline?", "mg sin θ", ["mg cos θ", "mg tan θ", "mg/sin θ"]),
    ("What is the normal force on an inclined plane?", "N = mg cos θ", ["N = mg", "N = mg sin θ", "N = mg tan θ"]),
    ("On a frictionless incline, what is the acceleration?", "g sin θ", ["g cos θ", "g", "g tan θ"]),
    ("What is the angle of repose?", "The steepest angle at which an object stays stationary", ["The angle of a ramp in a lab", "45 degrees", "The angle at which friction disappears"]),
    ("Does the normal force always equal mg?", "No — only on flat horizontal surfaces", ["Yes, always", "Only on inclines", "Only in free fall"]),
    ("Why do we decompose forces on an inclined plane?", "To separate motion along the slope from motion perpendicular to it", ["To make the math harder", "Forces cannot act on inclines", "To eliminate gravity"]),
    ("On a steeper incline, the component of gravity along the slope:", "Increases", ["Decreases", "Stays the same", "Becomes zero"]),
],
"3.7": [
    ("What is centripetal acceleration?", "Acceleration directed toward the center of circular motion: a_c = v²/r", ["Acceleration away from the center", "Acceleration along the tangent", "Acceleration due to gravity"]),
    ("Is centripetal force a new type of force?", "No — it is provided by existing forces", ["Yes — it only appears in circular motion", "Yes — it is a fundamental force", "Yes — it is a quantum effect"]),
    ("What provides centripetal force for a car turning on a road?", "Friction between tires and road", ["Gravity", "The engine", "Air resistance"]),
    ("In uniform circular motion, is speed constant?", "Yes, but velocity changes direction", ["No, speed varies", "Yes, and velocity is also constant", "Speed is zero"]),
    ("What is the formula for period of circular motion?", "T = 2πr/v", ["T = πr²/v", "T = v/(2πr)", "T = 2πv/r"]),
    ("What is the relationship between period and frequency?", "f = 1/T", ["f = T", "f = 2T", "f = T²"]),
    ("Write centripetal force in terms of angular velocity.", "F_c = mω²r", ["F_c = mωr", "F_c = mω²/r", "F_c = mω/r²"]),
],
"3.8": [
    ("What is a pseudo-force?", "A fictitious force added in a non-inertial frame to make F = ma work", ["A real contact force", "A gravitational force", "An electromagnetic force"]),
    ("Is centrifugal force a real force?", "No — it is a fictitious force in a rotating frame", ["Yes — it is a fundamental force", "Yes — it is a contact force", "Yes — it acts in all frames"]),
    ("In which direction does the Coriolis force deflect objects in the Northern Hemisphere?", "To the right", ["To the left", "Downward", "Upward"]),
    ("Do pseudo-forces have action-reaction pairs?", "No", ["Yes, always", "Only in rotating frames", "Only at high speeds"]),
    ("Why do you feel pushed backward when a car accelerates forward?", "Pseudo-force in the non-inertial frame of the car", ["The seat pushes you back", "Gravity increases", "Air resistance pushes you"]),
    ("What is a non-inertial reference frame?", "A frame that is accelerating", ["Any frame at rest", "Any frame moving at constant velocity", "A frame attached to Earth"]),
    ("What must you add to apply Newton's laws in an accelerating frame?", "Pseudo-forces (fictitious forces)", ["Real forces", "More mass", "Extra dimensions"]),
],
"4.1": [
    ("What is the formula for work?", "W = Fd cos θ", ["W = Fd sin θ", "W = mv²", "W = mgh"]),
    ("What is the SI unit of work?", "Joule (J)", ["Watt (W)", "Newton (N)", "Pascal (Pa)"]),
    ("When is work zero?", "When force is perpendicular to displacement", ["When force equals displacement", "When the object moves", "When there is no friction"]),
    ("What does negative work do to an object?", "Removes energy (slows it down)", ["Adds energy", "Has no effect", "Changes its direction without changing speed"]),
    ("If you push a box 5 m with 20 N in the same direction, work done is:", "100 J", ["25 J", "4 J", "200 J"]),
    ("Does gravity do work when you carry a box horizontally?", "No — gravity is perpendicular to the horizontal displacement", ["Yes, gravity always does work", "Only if the box is heavy", "Only if you walk fast"]),
    ("When is work positive?", "When force and displacement are in the same direction", ["When force and displacement are perpendicular", "When force and displacement are opposite", "Work is always positive"]),
],
"4.2": [
    ("What is the formula for kinetic energy?", "KE = ½mv²", ["KE = mv", "KE = mgh", "KE = ½kx²"]),
    ("If speed doubles, what happens to kinetic energy?", "It quadruples", ["It doubles", "It halves", "It stays the same"]),
    ("What is gravitational potential energy near Earth's surface?", "PE = mgh", ["PE = ½mv²", "PE = ½kx²", "PE = GMm/r"]),
    ("Can kinetic energy be negative?", "No — it is always positive or zero", ["Yes, when moving backward", "Yes, at very low temperatures", "Yes, in space"]),
    ("What is elastic potential energy?", "PE = ½kx²", ["PE = mgh", "PE = ½mv²", "PE = Fd"]),
    ("As a ball falls, PE converts to:", "Kinetic energy", ["Thermal energy only", "Potential energy increases", "Nothing"]),
    ("What is the KE of a 2 kg object moving at 3 m/s?", "9 J", ["6 J", "3 J", "18 J"]),
],
"4.3": [
    ("When is mechanical energy conserved?", "When only conservative forces act", ["Always", "Never", "Only in collisions"]),
    ("At the lowest point of a pendulum, which energy is maximum?", "Kinetic energy", ["Potential energy", "Thermal energy", "Elastic energy"]),
    ("State the law of conservation of energy.", "Energy cannot be created or destroyed — only transformed", ["Energy can be created from nothing", "Energy is always lost", "Energy only exists as heat"]),
    ("On a roller coaster, where is speed greatest?", "At the lowest point", ["At the highest point", "At the middle", "Speed is constant"]),
    ("What happens to mechanical energy when friction is present?", "Some is converted to thermal energy", ["It increases", "It stays the same", "It disappears"]),
    ("Write the conservation of mechanical energy equation.", "KE₁ + PE₁ = KE₂ + PE₂", ["KE₁ = PE₂", "KE = PE always", "F = ma"]),
    ("Is total energy (all forms) always conserved in an isolated system?", "Yes", ["No", "Only in theory", "Only at low speeds"]),
],
"4.4": [
    ("What is power?", "The rate of doing work: P = W/t", ["The total energy used", "Force times distance", "Mass times acceleration"]),
    ("What is the SI unit of power?", "Watt (W)", ["Joule (J)", "Newton (N)", "Horsepower (hp)"]),
    ("What is an alternative formula for power?", "P = Fv", ["P = Fd", "P = mgh", "P = ½mv²"]),
    ("Can efficiency exceed 100%?", "No", ["Yes, with advanced technology", "Yes, in quantum mechanics", "Yes, with renewable energy"]),
    ("What is efficiency?", "Useful energy output / total energy input × 100%", ["Total output / useful input × 100%", "Input / output × 100%", "Work done / force applied"]),
    ("How much power is needed to lift 100 N by 2 m in 4 s?", "50 W", ["200 W", "800 W", "25 W"]),
    ("1 horsepower is approximately:", "746 W", ["1000 W", "100 W", "500 W"]),
],
"4.5": [
    ("State the work-energy theorem.", "The net work on an object equals its change in kinetic energy", ["Work equals force times distance", "Energy is always conserved", "Power equals work divided by time"]),
    ("If net work is positive, what happens to speed?", "The object speeds up", ["The object slows down", "Speed stays the same", "The object stops"]),
    ("If net work is zero, what happens to speed?", "Speed stays the same", ["The object speeds up", "The object slows down", "The object stops"]),
    ("Write the work-energy theorem formula.", "W_net = ½mv² − ½mu²", ["W = Fd", "W = mgh", "W = ½kx²"]),
    ("A 10 N net force moves an object 5 m. Change in KE?", "50 J", ["2 J", "15 J", "500 J"]),
    ("For a variable force, what gives the net work?", "Area under the F-x graph", ["Slope of the F-x graph", "Height of the F-x graph", "The maximum force value"]),
    ("How does the work-energy theorem relate to Newton's Second Law?", "It is derived from F = ma combined with kinematics", ["They are unrelated", "It replaces Newton's laws", "It only applies to light objects"]),
],
"4.6": [
    ("What is a conservative force?", "A force whose work is independent of path", ["A force that always opposes motion", "A force with variable magnitude", "Any friction force"]),
    ("Which of these is a non-conservative force?", "Friction", ["Gravity", "Elastic spring force", "Electrostatic force"]),
    ("What is the work done by a conservative force in a closed loop?", "Zero", ["Maximum", "Equal to the total energy", "Depends on speed"]),
    ("Which type of force is associated with potential energy?", "Conservative forces", ["Non-conservative forces", "All forces", "Only gravity"]),
    ("Does friction do positive or negative work?", "Always negative", ["Always positive", "It depends on direction", "Zero"]),
    ("What does friction convert mechanical energy into?", "Thermal energy (heat)", ["Kinetic energy", "Potential energy", "Nuclear energy"]),
    ("If only conservative forces act, ΔKE + ΔPE equals:", "Zero", ["The total work done", "The initial KE", "Infinity"]),
],
"5.1": [
    ("What is linear momentum?", "p = mv", ["p = ma", "p = Ft", "p = ½mv²"]),
    ("What is the SI unit of momentum?", "kg·m/s", ["N·m", "J/s", "kg·m/s²"]),
    ("Is momentum a scalar or vector?", "Vector", ["Scalar", "Both", "Neither"]),
    ("When is total momentum conserved?", "In an isolated system with no net external force", ["Always", "Never", "Only in elastic collisions"]),
    ("State Newton's Second Law in terms of momentum.", "F = dp/dt", ["F = mv", "F = ma only", "F = p/t"]),
    ("A 2 kg object moves at 5 m/s. Its momentum is:", "10 kg·m/s", ["2.5 kg·m/s", "7 kg·m/s", "50 kg·m/s"]),
    ("In an explosion from rest, total momentum after is:", "Zero", ["Maximum", "Equal to the energy released", "It depends on the fragments"]),
],
"5.2": [
    ("What is impulse?", "The product of force and time: J = FΔt", ["Force divided by time", "Mass times velocity", "Energy times time"]),
    ("State the impulse-momentum theorem.", "FΔt = Δp", ["Ft = mv", "F = ma", "Impulse = KE"]),
    ("How do car airbags reduce injury?", "They extend collision time, reducing average force", ["They make the car lighter", "They absorb all the energy", "They increase the force on the body"]),
    ("For a variable force, how do you find impulse?", "Area under the F-t graph", ["Slope of the F-t graph", "Peak of the F-t graph", "The average time"]),
    ("Can impulse be negative?", "Yes — if the force is in the negative direction", ["No, impulse is always positive", "Only in explosions", "Only for light objects"]),
    ("Why do you bend your knees when landing a jump?", "It increases stopping time, reducing force", ["It makes you heavier", "It increases the force", "It reduces your momentum"]),
    ("What is the SI unit of impulse?", "N·s (same as kg·m/s)", ["J", "W", "Pa·s"]),
],
"5.3": [
    ("State the law of conservation of momentum.", "Total momentum before = total momentum after in an isolated system", ["Momentum always increases", "Momentum is only conserved in elastic collisions", "Momentum equals energy"]),
    ("Is momentum conserved in explosions?", "Yes", ["No", "Only for symmetric explosions", "Only at low speeds"]),
    ("Write the conservation equation for two objects.", "m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂", ["m₁u₁ = m₂v₂", "m₁v₁ = m₂v₂", "m₁ + m₂ = m₁v₁ + m₂v₂"]),
    ("In a gun recoil, bullet and gun momenta are:", "Equal in magnitude and opposite in direction", ["Equal in every way", "The bullet has more momentum", "The gun has more momentum"]),
    ("Is momentum conserved in all types of collisions?", "Yes", ["Only elastic", "Only inelastic", "No"]),
    ("Does conservation apply separately to x and y components?", "Yes", ["No — only to the total magnitude", "Only in 1D problems", "Only for elastic collisions"]),
    ("A 5 kg object at 4 m/s collides and sticks to a 5 kg object at rest. Final velocity?", "2 m/s", ["4 m/s", "0 m/s", "8 m/s"]),
],
"5.4": [
    ("What is an elastic collision?", "One where both momentum and KE are conserved", ["One where objects stick together", "One where momentum is not conserved", "Any collision"]),
    ("What is a perfectly inelastic collision?", "Objects stick together — maximum KE lost", ["All energy is conserved", "Objects bounce apart", "No collision occurs"]),
    ("Which type of collision loses the most kinetic energy?", "Perfectly inelastic", ["Elastic", "Superelastic", "They all lose the same"]),
    ("In an elastic head-on collision of equal masses, what happens?", "They exchange velocities", ["They stop", "They both reverse", "They stick together"]),
    ("Where does lost KE go in inelastic collisions?", "Heat, sound, or deformation", ["It disappears", "Into momentum", "Into mass"]),
    ("Are most real-world collisions elastic or inelastic?", "Inelastic", ["Elastic", "Perfectly elastic", "Superelastic"]),
    ("What is conserved in ALL types of collisions?", "Momentum", ["Kinetic energy", "Speed", "Force"]),
],
"5.5": [
    ("What is the center of mass?", "The average position of all mass, weighted by mass", ["The geometric center always", "The heaviest point", "The point farthest from all edges"]),
    ("Where is the COM of a uniform symmetric object?", "At its geometric center", ["At one edge", "Outside the object", "At the heaviest atom"]),
    ("How does the COM move if no external forces act?", "At constant velocity", ["It accelerates", "It stops", "It spirals"]),
    ("Can the center of mass be outside the physical object?", "Yes — like the center of a ring", ["No, it must be inside", "Only for gases", "Only in 2D"]),
    ("If two equal masses are 10 m apart, where is the COM?", "At the midpoint (5 m from each)", ["At mass 1", "At mass 2", "10 m from both"]),
    ("State Newton's second law for the center of mass.", "F_ext = Ma_cm", ["F = mv", "F = kx", "F_ext = mv_cm"]),
    ("After an explosion, the center of mass:", "Continues on the same path as before", ["Stops", "Moves to the largest fragment", "Moves randomly"]),
],
"5.6": [
    ("How do rockets propel themselves?", "By expelling exhaust gases — conservation of momentum", ["By pushing against air", "By magnetic repulsion", "By heating the surrounding space"]),
    ("Do rockets need air to push against?", "No — they work in the vacuum of space", ["Yes, they need atmosphere", "Only for takeoff", "Only above 10 km"]),
    ("What is the formula for rocket thrust?", "Thrust = v_e × (dm/dt)", ["Thrust = ma only", "Thrust = mg", "Thrust = Fd"]),
    ("For liftoff, thrust must exceed:", "The rocket's weight (mg)", ["The rocket's mass", "The exhaust velocity", "The speed of sound"]),
    ("Which Newton's law explains rocket propulsion?", "Newton's Third Law", ["Newton's First Law", "Newton's Second Law only", "Kepler's Law"]),
    ("What is staging in rocketry?", "Discarding empty fuel tanks to reduce mass", ["Adding more fuel", "Splitting the payload", "Orbiting in stages"]),
    ("What does the Tsiolkovsky rocket equation relate?", "Δv to exhaust velocity and mass ratio", ["Force to mass", "Energy to time", "Thrust to altitude"]),
],
"6.1": [
    ("State Newton's Law of Universal Gravitation.", "F = GMm/r²", ["F = mg only", "F = kx", "F = mv²/r"]),
    ("What is G?", "The gravitational constant: 6.674 × 10⁻¹¹ N·m²/kg²", ["Acceleration due to gravity", "The weight of 1 kg", "The gravitational field strength"]),
    ("What happens to gravitational force if you double the distance?", "It decreases by a factor of 4", ["It halves", "It doubles", "It quadruples"]),
    ("Is gravitational force attractive or repulsive?", "Always attractive", ["Always repulsive", "Sometimes repulsive", "Neither"]),
    ("What is g at Earth's surface in terms of G, M, and R?", "g = GM/R²", ["g = GM/R", "g = G/MR²", "g = GMR²"]),
    ("What is r in the gravitational formula?", "Distance between the centers of the two masses", ["Radius of the smaller object", "Radius of the larger object", "The surface distance"]),
    ("What type of law is the gravitational force law?", "An inverse-square law", ["A linear law", "An exponential law", "A direct-proportion law"]),
],
"6.2": [
    ("What is gravitational field strength?", "Force per unit mass: g = F/m = GM/r²", ["Total force on an object", "Mass per unit volume", "Energy per unit time"]),
    ("What are the units of gravitational field strength?", "N/kg or m/s²", ["N·m", "kg/m³", "J/kg"]),
    ("Which direction do gravitational field lines point?", "Toward the mass", ["Away from the mass", "In circles", "Random directions"]),
    ("What is the general formula for gravitational PE?", "PE = −GMm/r", ["PE = mgh always", "PE = ½mv²", "PE = GMm/r²"]),
    ("Why is gravitational PE negative?", "Because PE = 0 at infinity by convention, and work must be done to reach infinity", ["It's a calculation error", "Gravity repels at close range", "Energy is always negative"]),
    ("What do closer field lines indicate?", "A stronger gravitational field", ["A weaker field", "No field", "Constant field"]),
    ("Near Earth's surface, field lines are approximately:", "Parallel (uniform field)", ["Radial", "Circular", "Random"]),
],
"6.3": [
    ("What provides centripetal force for an orbit?", "Gravity", ["Rocket engines", "Momentum", "Inertia"]),
    ("Does orbital speed depend on the orbiting object's mass?", "No — only on M and r", ["Yes, heavier objects orbit faster", "Yes, lighter objects orbit faster", "It depends on the altitude only"]),
    ("What is the formula for orbital speed?", "v = √(GM/r)", ["v = GM/r", "v = √(GM·r)", "v = 2πr/GM"]),
    ("Higher orbit: faster or slower speed?", "Slower speed", ["Faster speed", "Same speed", "Speed is zero"]),
    ("What is a geostationary orbit?", "An orbit with T = 24 hours staying above the same point", ["Any orbit around Earth", "An orbit at the equator surface", "Any satellite with zero velocity"]),
    ("What shape can orbits be?", "Circular or elliptical", ["Only circular", "Only elliptical", "Any polygon"]),
    ("In a circular orbit, is speed constant?", "Yes", ["No", "Only at high altitudes", "Only for heavy satellites"]),
],
"6.4": [
    ("Why do satellites stay in orbit?", "Gravity provides centripetal force — continuous free fall", ["Rockets keep pushing them", "There is no gravity in space", "They move too slowly to fall"]),
    ("What is the altitude of LEO?", "200–2,000 km", ["0–100 km", "35,000–40,000 km", "100,000+ km"]),
    ("What is the period of a geostationary satellite?", "24 hours", ["90 minutes", "1 year", "12 hours"]),
    ("Why do astronauts on the ISS feel weightless?", "They and the station are in free fall together", ["There is no gravity at that altitude", "The ISS has antigravity", "Air resistance cancels gravity"]),
    ("What is g at the ISS altitude (~400 km)?", "About 8.7 m/s²", ["0 m/s²", "9.8 m/s²", "1.6 m/s²"]),
    ("Geostationary satellites are used for:", "Communications and weather monitoring", ["GPS navigation (MEO)", "Space tourism", "Mining asteroids"]),
    ("Does orbital period depend on satellite mass?", "No", ["Yes", "Only for heavy satellites", "Only near Earth"]),
],
"6.5": [
    ("What is escape velocity?", "Minimum speed to leave a gravitational field without further propulsion", ["Maximum speed in orbit", "The speed of light", "Terminal velocity in atmosphere"]),
    ("What is the formula for escape velocity?", "v_esc = √(2GM/r)", ["v_esc = √(GM/r)", "v_esc = 2GM/r", "v_esc = GM/r²"]),
    ("What is Earth's escape velocity?", "About 11.2 km/s", ["About 7.9 km/s", "About 3 km/s", "About 30 km/s"]),
    ("Does escape velocity depend on the escaping object's mass?", "No", ["Yes", "Only for rockets", "Only for heavy objects"]),
    ("How does escape velocity relate to orbital velocity?", "Escape velocity = √2 × orbital velocity", ["They are equal", "Escape = 2 × orbital", "Escape = orbital / 2"]),
    ("Total energy at escape velocity is:", "Zero", ["Positive", "Negative", "Infinite"]),
    ("At escape velocity, speed at infinity is:", "Zero", ["Equal to c", "Equal to escape velocity", "Infinite"]),
],
"6.6": [
    ("State Kepler's First Law.", "Planets orbit in ellipses with the Sun at one focus", ["Planets orbit in circles", "All orbits have the same period", "Planets move at constant speed"]),
    ("State Kepler's Second Law.", "A line from Sun to planet sweeps equal areas in equal times", ["Planets move at constant speed", "Closer planets orbit faster", "All orbits are circular"]),
    ("State Kepler's Third Law.", "T² ∝ r³", ["T ∝ r", "T² ∝ r²", "T ∝ r²"]),
    ("When is a planet fastest in its orbit?", "At perihelion (closest to Sun)", ["At aphelion (farthest from Sun)", "At all points equally", "At the halfway point"]),
    ("What is perihelion?", "The closest point to the Sun in an orbit", ["The farthest point from the Sun", "The midpoint of an orbit", "The point of zero velocity"]),
    ("If a planet's orbital radius doubles, the period increases by:", "A factor of 2√2", ["A factor of 2", "A factor of 4", "A factor of 8"]),
    ("Kepler's Third Law as an equation:", "T² = (4π²/GM)r³", ["T = 2πr", "T² = GMr", "T = 4π²r³"]),
],
"7.1": [
    ("What is simple harmonic motion (SHM)?", "Periodic motion with restoring force proportional to displacement: F = −kx", ["Any periodic motion", "Motion in a circle", "Motion at constant speed"]),
    ("What is the period of a mass-spring system?", "T = 2π√(m/k)", ["T = 2π√(k/m)", "T = mk", "T = 2πmk"]),
    ("Where is maximum speed in SHM?", "At the equilibrium position", ["At the extremes", "At the midpoint of one half", "Speed is constant"]),
    ("Where is maximum acceleration in SHM?", "At the extremes (x = ±A)", ["At equilibrium", "It's constant everywhere", "At the midpoint"]),
    ("What is the period of a simple pendulum?", "T = 2π√(L/g)", ["T = 2π√(g/L)", "T = 2πLg", "T = L/g"]),
    ("What direction does acceleration point in SHM?", "Always toward equilibrium", ["Always away from equilibrium", "In the direction of motion", "Perpendicular to motion"]),
    ("What is the maximum speed in SHM?", "v_max = Aω", ["v_max = A/ω", "v_max = Aω²", "v_max = ω/A"]),
],
"7.2": [
    ("What is the period (T) of an oscillation?", "The time for one complete cycle", ["The number of cycles per second", "The maximum displacement", "The speed of the oscillation"]),
    ("What is the SI unit of frequency?", "Hertz (Hz)", ["Second (s)", "Radian (rad)", "Newton (N)"]),
    ("Does amplitude affect the period of ideal SHM?", "No", ["Yes, larger amplitude means longer period", "Yes, larger amplitude means shorter period", "Only for springs"]),
    ("What is angular frequency?", "ω = 2πf = 2π/T", ["ω = f/2π", "ω = T/2π", "ω = πf"]),
    ("Does the period of a pendulum depend on mass?", "No — only on L and g", ["Yes — heavier means longer period", "Yes — lighter means longer period", "Only for very heavy pendulums"]),
    ("If T = 0.5 s, what is f?", "2 Hz", ["0.5 Hz", "1 Hz", "4 Hz"]),
    ("What determines the energy in a spring SHM?", "E = ½kA² (depends on amplitude)", ["E = ½mv only", "E = kA", "E = mg"]),
],
"7.3": [
    ("What is the total energy in undamped SHM?", "E = ½kA² (constant)", ["E = ½mv²", "E = mgh", "E varies continuously"]),
    ("At equilibrium (x = 0), what is the energy distribution?", "All kinetic, zero potential", ["All potential, zero kinetic", "Equal KE and PE", "Zero total energy"]),
    ("At the extremes (x = ±A), the energy is:", "All potential, zero kinetic", ["All kinetic, zero potential", "Equal KE and PE", "Zero total"]),
    ("If amplitude doubles, total energy:", "Quadruples", ["Doubles", "Stays the same", "Halves"]),
    ("On an energy-time graph, total energy looks like:", "A horizontal line (constant)", ["A sine wave", "An increasing line", "A decreasing line"]),
    ("KE and PE oscillate at what frequency compared to the motion?", "Twice the frequency", ["Same frequency", "Half the frequency", "Three times"]),
    ("When KE is at its peak, PE is at its:", "Minimum (zero)", ["Maximum", "Half of total", "Equal to KE"]),
],
"7.4": [
    ("What is a wave?", "A disturbance that transfers energy without transferring matter", ["A movement of matter", "A type of force", "A form of temperature"]),
    ("What is a transverse wave?", "Oscillation perpendicular to wave direction", ["Oscillation parallel to wave direction", "A wave that doesn't move", "A wave in a circle"]),
    ("State the wave equation.", "v = fλ", ["v = f/λ", "v = λ/f", "v = f²λ"]),
    ("Give an example of a longitudinal wave.", "Sound", ["Light", "Water surface waves", "Radio waves"]),
    ("Does wave speed depend on amplitude?", "No — it depends on the medium", ["Yes — larger amplitude means faster", "Yes — smaller amplitude means faster", "It depends on frequency"]),
    ("If frequency doubles but speed stays the same, wavelength:", "Halves", ["Doubles", "Stays the same", "Quadruples"]),
    ("What is wavelength (λ)?", "Distance between consecutive identical points", ["The height of a wave", "The speed of a wave", "The time for one cycle"]),
],
"7.5": [
    ("State the principle of superposition.", "The resultant displacement is the sum of individual displacements", ["Waves always cancel", "Waves always amplify", "Waves pass through each other unchanged"]),
    ("What is constructive interference?", "Waves in phase combine to produce larger amplitude", ["Waves cancel each other", "Waves slow down", "Waves change direction"]),
    ("What path difference gives constructive interference?", "nλ (0, λ, 2λ, ...)", ["(n+½)λ", "nλ/2", "Random"]),
    ("What path difference gives destructive interference?", "(n+½)λ", ["nλ", "2nλ", "0"]),
    ("Which experiment demonstrated light interference?", "Young's double-slit experiment", ["Newton's prism experiment", "Rutherford's scattering", "Michelson-Morley"]),
    ("How do noise-canceling headphones work?", "Destructive interference", ["Constructive interference", "Reflection", "Refraction"]),
    ("In complete destructive interference (equal amplitudes), the result is:", "Zero amplitude", ["Double amplitude", "Half amplitude", "Random amplitude"]),
],
"7.6": [
    ("How is a standing wave formed?", "Two identical waves traveling in opposite directions interfere", ["A single wave reflects", "Waves of different frequencies combine", "A wave slows down"]),
    ("What are nodes?", "Points of zero displacement", ["Points of maximum displacement", "The frequency of the wave", "The wavelength"]),
    ("What are antinodes?", "Points of maximum displacement", ["Points of zero displacement", "The speed of the wave", "The period of the wave"]),
    ("Does energy propagate in a standing wave?", "No — the pattern stands still", ["Yes — all waves carry energy", "Only at nodes", "Only at antinodes"]),
    ("What is resonance?", "When a system is driven at its natural frequency, amplitude increases dramatically", ["When waves cancel", "When frequency approaches zero", "When amplitude decreases"]),
    ("In the nth harmonic of a fixed string, how many nodes?", "n + 1", ["n", "n − 1", "2n"]),
    ("Fundamental frequency for a string fixed at both ends: L = ?", "λ/2", ["λ", "2λ", "λ/4"]),
],
"7.7": [
    ("What is the Doppler effect?", "Change in observed frequency due to relative motion", ["Change in amplitude due to distance", "Change in wavelength due to temperature", "Change in speed of sound"]),
    ("If a sound source approaches, pitch:", "Increases", ["Decreases", "Stays the same", "Becomes inaudible"]),
    ("What is red shift?", "Light from a receding object shifts to longer wavelength", ["Light becomes red in color", "Light speeds up", "Light reflects off red objects"]),
    ("What evidence does red shift provide?", "The universe is expanding", ["The Sun is cooling", "Stars are made of iron", "Light has mass"]),
    ("Does the Doppler effect apply to all types of waves?", "Yes", ["Only sound", "Only light", "Only water waves"]),
    ("When a source approaches, wavelength is:", "Compressed", ["Stretched", "Unchanged", "Doubled"]),
    ("What is blue shift?", "Light from an approaching object shifts to shorter wavelength", ["Light becomes blue", "Light slows down", "Light refracts through water"]),
],
"7.8": [
    ("What is wave-particle duality?", "Light and matter exhibit both wave and particle behavior", ["Light is only a wave", "Light is only a particle", "Matter cannot behave as a wave"]),
    ("What experiment showed light as a particle?", "The photoelectric effect", ["Double-slit experiment", "Michelson-Morley experiment", "Rutherford scattering"]),
    ("What is the energy of a photon?", "E = hf", ["E = mc²", "E = ½mv²", "E = mgh"]),
    ("What is the de Broglie wavelength?", "λ = h/p = h/(mv)", ["λ = mc/h", "λ = hv/c", "λ = mv/h"]),
    ("What confirmed that particles behave as waves?", "Electron diffraction experiments", ["The photoelectric effect", "Rutherford's experiment", "Newton's prism"]),
    ("What is h called?", "Planck's constant", ["Boltzmann's constant", "Coulomb's constant", "The gravitational constant"]),
    ("Do electrons exhibit interference patterns?", "Yes", ["No", "Only at high temperatures", "Only in metals"]),
],
"8.1": [
    ("What type of wave is sound?", "A longitudinal mechanical wave", ["A transverse electromagnetic wave", "A transverse mechanical wave", "A longitudinal electromagnetic wave"]),
    ("Can sound travel through a vacuum?", "No — it requires a medium", ["Yes", "Only very loud sounds", "Only ultrasound"]),
    ("What produces sound?", "Vibrating objects", ["Static objects", "Light sources", "Magnetic fields"]),
    ("What is the human hearing range?", "Approximately 20 Hz to 20,000 Hz", ["1 Hz to 1,000 Hz", "100 Hz to 100,000 Hz", "0 to 10,000 Hz"]),
    ("What are compressions in a sound wave?", "High-pressure regions", ["Low-pressure regions", "Transverse peaks", "Points of zero pressure"]),
    ("What is ultrasound?", "Sound above 20,000 Hz", ["Sound below 20 Hz", "Very loud sound", "Sound from a tuning fork"]),
    ("Can sound be diffracted?", "Yes — it bends around obstacles", ["No", "Only at very high frequencies", "Only in liquids"]),
],
"8.2": [
    ("What is the speed of sound in air at 20°C?", "Approximately 343 m/s", ["Approximately 1500 m/s", "Approximately 100 m/s", "Approximately 3 × 10⁸ m/s"]),
    ("In which state of matter is sound fastest?", "Solids", ["Gases", "Liquids", "Sound speed is the same in all media"]),
    ("How does temperature affect the speed of sound?", "Speed increases with temperature", ["Speed decreases with temperature", "Temperature has no effect", "Speed doubles every 10°C"]),
    ("When sound enters a denser medium, what stays the same?", "Frequency", ["Wavelength", "Speed", "Amplitude"]),
    ("Give the formula for speed of sound vs. temperature.", "v ≈ 331 + 0.6T", ["v = 343T", "v = 331T", "v = 300 + T"]),
    ("Why is sound faster in solids than gases?", "Solids are denser and stiffer, allowing faster energy transfer", ["Solids have more air", "Gases absorb sound", "Sound doesn't exist in solids"]),
    ("Speed of sound in water is approximately:", "1,500 m/s", ["343 m/s", "5,000 m/s", "100 m/s"]),
],
"8.3": [
    ("What is sound intensity?", "Power per unit area: I = P/A", ["Frequency of the sound", "Amplitude of the sound wave", "Speed of sound squared"]),
    ("How does intensity vary with distance from a point source?", "Inverse-square law: I ∝ 1/r²", ["Linearly: I ∝ 1/r", "It doesn't vary", "Exponentially"]),
    ("What is the threshold of hearing?", "~10⁻¹² W/m²", ["~10⁻⁶ W/m²", "~1 W/m²", "~10⁻³ W/m²"]),
    ("An increase of 10 dB means intensity increases by:", "A factor of 10", ["A factor of 2", "A factor of 100", "A factor of 5"]),
    ("What is the formula for sound level in decibels?", "β = 10 log₁₀(I/I₀)", ["β = 20 log₁₀(I/I₀)", "β = I/I₀", "β = ln(I/I₀)"]),
    ("At what dB level can prolonged exposure cause hearing damage?", "About 85 dB", ["About 60 dB", "About 120 dB", "About 30 dB"]),
    ("What is normal conversation approximately?", "About 60 dB", ["About 30 dB", "About 90 dB", "About 120 dB"]),
],
"8.4": [
    ("What determines pitch?", "Frequency", ["Amplitude", "Wavelength", "Speed"]),
    ("What frequency is concert A (A4)?", "440 Hz", ["262 Hz", "880 Hz", "1000 Hz"]),
    ("What is an octave?", "A doubling of frequency", ["A halving of frequency", "An increase of 100 Hz", "A change in amplitude"]),
    ("What is timbre?", "The tone quality distinguishing different instruments", ["The volume of a sound", "The pitch of a note", "The speed of sound"]),
    ("What determines timbre?", "The mix of harmonics in the sound", ["Only the fundamental frequency", "Only the amplitude", "The speed of the wave"]),
    ("How does the ear perceive frequency?", "Logarithmically", ["Linearly", "Exponentially", "It doesn't perceive frequency"]),
    ("A4 is 440 Hz. What is A5?", "880 Hz", ["440 Hz", "220 Hz", "660 Hz"]),
],
"8.5": [
    ("In an open tube, what are at both ends?", "Antinodes", ["Nodes", "One node and one antinode", "Neither"]),
    ("What harmonics does a closed tube support?", "Only odd harmonics", ["All harmonics", "Only even harmonics", "No harmonics"]),
    ("Formula for resonant frequencies of an open tube?", "f_n = nv/(2L)", ["f_n = nv/(4L)", "f_n = 2nv/L", "f_n = v/(nL)"]),
    ("What is the fundamental wavelength for a closed tube?", "λ₁ = 4L", ["λ₁ = 2L", "λ₁ = L", "λ₁ = L/2"]),
    ("Is a flute an open or closed tube?", "Open", ["Closed", "Both", "Neither"]),
    ("In a closed tube, what is at the closed end?", "A node", ["An antinode", "Nothing", "Both"]),
    ("What harmonics does an open tube support?", "All harmonics", ["Only odd", "Only even", "None"]),
],
"8.6": [
    ("What are beats?", "Periodic loudness variations when two close frequencies interfere", ["A musical rhythm", "Sound reflections", "Standing waves in air"]),
    ("What is beat frequency?", "f_beat = |f₁ − f₂|", ["f_beat = f₁ + f₂", "f_beat = f₁ × f₂", "f_beat = f₁ / f₂"]),
    ("How are beats used in tuning instruments?", "Beats disappear when frequencies match", ["Beats increase when in tune", "Beats are unrelated to tuning", "By counting beats per minute"]),
    ("The 2nd harmonic is also called the:", "1st overtone", ["Fundamental", "2nd overtone", "3rd overtone"]),
    ("Closed tubes produce what harmonics?", "Only odd harmonics", ["All harmonics", "Only even harmonics", "No harmonics"]),
    ("What gives each instrument its unique sound?", "The mix of harmonics (timbre)", ["Only the fundamental frequency", "The volume", "The material of the room"]),
    ("If two tuning forks have frequencies 440 and 444 Hz, beat frequency?", "4 Hz", ["884 Hz", "442 Hz", "2 Hz"]),
],
"9.1": [
    ("State the law of reflection.", "Angle of incidence = angle of reflection", ["Angle of incidence × 2 = angle of reflection", "Light always reflects at 45°", "Reflection doesn't follow laws"]),
    ("State Snell's Law.", "n₁ sin θ₁ = n₂ sin θ₂", ["n₁ cos θ₁ = n₂ cos θ₂", "n₁ θ₁ = n₂ θ₂", "n₁/sin θ₁ = n₂/sin θ₂"]),
    ("What is the refractive index?", "n = c/v", ["n = v/c", "n = c·v", "n = c + v"]),
    ("When light enters a denser medium, it bends:", "Toward the normal", ["Away from the normal", "Not at all", "Parallel to the surface"]),
    ("Does frequency change during refraction?", "No — wavelength changes", ["Yes — frequency changes", "Both change", "Neither changes"]),
    ("What is specular reflection?", "Reflection from a smooth surface", ["Reflection from a rough surface", "Reflection at 90°", "No reflection"]),
    ("Angles of incidence and reflection are measured from:", "The normal", ["The surface", "The horizontal", "The vertical"]),
],
"9.2": [
    ("What type of image does a convex mirror always form?", "Virtual, upright, and diminished", ["Real and inverted", "Virtual and enlarged", "Real and upright"]),
    ("State the mirror/lens equation.", "1/f = 1/d_o + 1/d_i", ["f = d_o + d_i", "f = d_o × d_i", "1/f = 1/d_o − 1/d_i"]),
    ("What is the magnification formula?", "m = −d_i/d_o", ["m = d_i + d_o", "m = f/d_o", "m = d_o/d_i"]),
    ("If |m| > 1, the image is:", "Enlarged", ["Diminished", "Same size", "Virtual"]),
    ("A diverging lens always forms:", "Virtual, upright, diminished image", ["Real, inverted, enlarged image", "Real, upright image", "Virtual, inverted image"]),
    ("A convex (converging) lens has what kind of focal length?", "Positive", ["Negative", "Zero", "Infinite"]),
    ("If m is negative, the image is:", "Inverted", ["Upright", "Virtual", "Larger"]),
],
"9.3": [
    ("What is total internal reflection (TIR)?", "All light reflected when hitting boundary above the critical angle", ["Light passing through all materials", "Light absorbed at a boundary", "Partial reflection only"]),
    ("When does TIR occur?", "Light goes from denser to less dense medium above critical angle", ["Light goes from less dense to denser medium", "At any angle", "Only in vacuum"]),
    ("What is the formula for the critical angle?", "sin θ_c = n₂/n₁ (where n₁ > n₂)", ["sin θ_c = n₁/n₂", "cos θ_c = n₂/n₁", "tan θ_c = n₂/n₁"]),
    ("How do optical fibers use TIR?", "Light bounces along the fiber by total internal reflection", ["Light passes straight through", "Light is absorbed", "Light diffracts inside"]),
    ("Why do diamonds sparkle?", "Very low critical angle causes maximum internal reflection", ["They emit light", "They are transparent", "They absorb all colors"]),
    ("Can TIR occur going from air to glass?", "No — only from denser to less dense medium", ["Yes, at any angle", "Yes, above 42°", "Yes, but only for red light"]),
    ("Name a medical application of optical fibers.", "Endoscopes", ["X-ray machines", "MRI scanners", "Stethoscopes"]),
],
"9.4": [
    ("What type of lens does the human eye use?", "A converging lens", ["A diverging lens", "A flat lens", "A prism"]),
    ("What corrects myopia (nearsightedness)?", "Diverging (concave) lens", ["Converging (convex) lens", "A prism", "A mirror"]),
    ("What corrects hyperopia (farsightedness)?", "Converging (convex) lens", ["Diverging (concave) lens", "A flat lens", "A pinhole"]),
    ("What is the near point of a normal eye?", "About 25 cm", ["About 1 m", "About 10 cm", "About 50 cm"]),
    ("In a telescope, which lens has the larger focal length?", "The objective lens", ["The eyepiece", "Both are equal", "Neither — telescopes use mirrors only"]),
    ("Where does the eye focus incoming light?", "On the retina", ["On the cornea", "On the iris", "On the pupil"]),
    ("What is the total magnification of a compound microscope?", "M_objective × M_eyepiece", ["M_objective + M_eyepiece", "M_objective / M_eyepiece", "M_objective − M_eyepiece"]),
],
"9.5": [
    ("What is diffraction?", "Bending and spreading of waves around obstacles or through openings", ["Reflection of light", "Absorption of light", "Polarization of light"]),
    ("When is diffraction most significant?", "When the opening is comparable to the wavelength", ["When the opening is very large", "At very high frequencies", "In a vacuum"]),
    ("Condition for bright fringes in Young's double slit:", "d sin θ = nλ", ["d sin θ = (n+½)λ", "d cos θ = nλ", "d = nλ"]),
    ("What is a diffraction grating?", "A device with many parallel slits producing sharp bright maxima", ["A single slit", "A type of mirror", "A filter for colors"]),
    ("In single-slit diffraction, which maximum is brightest?", "The central maximum", ["The first side maximum", "They are all equal", "The edges"]),
    ("What is the formula for fringe spacing?", "Δy = λL/d", ["Δy = dL/λ", "Δy = d/(λL)", "Δy = λd/L"]),
    ("What must two sources be for interference to occur?", "Coherent", ["Incoherent", "Very bright", "The same color only"]),
],
"9.6": [
    ("What is polarization?", "Restricting oscillation of a transverse wave to a single plane", ["Increasing the speed of light", "Changing the color of light", "Bending light around obstacles"]),
    ("Can longitudinal waves be polarized?", "No — only transverse waves", ["Yes", "Only in certain media", "Only at high frequencies"]),
    ("What does polarization prove about light?", "That light is a transverse wave", ["That light is longitudinal", "That light has mass", "That light is a particle"]),
    ("At θ = 90° (crossed polarizers), what fraction of light passes?", "0%", ["100%", "50%", "25%"]),
    ("How do polarizing sunglasses work?", "They block horizontally polarized light (glare)", ["They block all light equally", "They change light color", "They increase brightness"]),
    ("State Malus's Law.", "I = I₀ cos² θ", ["I = I₀ sin² θ", "I = I₀ cos θ", "I = I₀/cos² θ"]),
    ("Name three methods of polarization.", "Filters, reflection, and scattering", ["Refraction, diffraction, absorption", "Gravity, magnetism, friction", "Only filters can polarize"]),
],
"10.1": [
    ("State Coulomb's Law.", "F = kq₁q₂/r²", ["F = kq₁q₂/r", "F = kq₁q₂r²", "F = q₁q₂/r²"]),
    ("What is the elementary charge?", "1.6 × 10⁻¹⁹ C", ["1.6 × 10⁻¹⁹ kg", "9.8 N", "6.67 × 10⁻¹¹ C"]),
    ("Like charges:", "Repel", ["Attract", "Have no interaction", "Cancel each other"]),
    ("Is charge conserved?", "Yes", ["No", "Only in conductors", "Only at low temperatures"]),
    ("What happens if distance between charges doubles?", "Force decreases by a factor of 4", ["Force halves", "Force doubles", "Force quadruples"]),
    ("Is charge quantized?", "Yes — in multiples of e", ["No — charge is continuous", "Only for electrons", "Only in metals"]),
    ("What is Coulomb's constant k?", "8.99 × 10⁹ N·m²/C²", ["6.67 × 10⁻¹¹ N·m²/C²", "9.8 N/C", "1.6 × 10⁻¹⁹ N·m²/C²"]),
],
"10.2": [
    ("What is an electric field?", "A region where a charged particle experiences a force", ["A region with no charges", "A magnetic field around a wire", "The space inside a capacitor only"]),
    ("What is the formula for electric field?", "E = F/q = kQ/r²", ["E = Fq", "E = kQ/r", "E = FR²/q"]),
    ("Field lines point away from:", "Positive charges", ["Negative charges", "Both equally", "Neither"]),
    ("What is electric potential?", "Energy per unit charge: V = U/q", ["Force per unit charge", "Charge per unit energy", "Current per unit time"]),
    ("Equipotential lines are perpendicular to:", "Electric field lines", ["Magnetic field lines", "The surface", "Nothing"]),
    ("What are the units of electric field?", "N/C or V/m", ["J/C", "C/m", "W/A"]),
    ("What is the unit of electric potential?", "Volt (V) = J/C", ["Ampere (A)", "Ohm (Ω)", "Farad (F)"]),
],
"10.3": [
    ("What does a capacitor store?", "Electrical energy in an electric field", ["Magnetic energy", "Charge only", "Current"]),
    ("What is capacitance?", "C = Q/V", ["C = V/Q", "C = QV", "C = Q²/V"]),
    ("What is the SI unit of capacitance?", "Farad (F)", ["Coulomb (C)", "Volt (V)", "Henry (H)"]),
    ("How does inserting a dielectric affect capacitance?", "Increases it", ["Decreases it", "No effect", "Makes it zero"]),
    ("How do capacitors combine in parallel?", "C_total = C₁ + C₂", ["1/C_total = 1/C₁ + 1/C₂", "C_total = C₁ × C₂", "C_total = C₁ − C₂"]),
    ("Energy stored in a capacitor:", "E = ½CV²", ["E = CV", "E = C²V", "E = 2CV²"]),
    ("If plate separation d is halved, capacitance:", "Doubles", ["Halves", "Stays the same", "Quadruples"]),
],
"10.4": [
    ("What is electric current?", "Rate of flow of charge: I = Q/t", ["Charge times time", "Voltage divided by power", "Resistance times voltage"]),
    ("State Ohm's Law.", "V = IR", ["V = I/R", "V = I²R", "V = IR²"]),
    ("What is the SI unit of resistance?", "Ohm (Ω)", ["Volt (V)", "Ampere (A)", "Watt (W)"]),
    ("Conventional current flows from:", "Positive to negative", ["Negative to positive", "It doesn't flow", "Both directions equally"]),
    ("What is the formula for electrical power?", "P = IV", ["P = I/V", "P = V/I", "P = IR"]),
    ("What factors affect resistance of a wire?", "Material, length, and cross-sectional area", ["Only length", "Only material", "Only temperature"]),
    ("What is a non-ohmic device?", "One whose resistance changes with current (e.g., diode)", ["One that follows Ohm's Law", "Any battery", "A perfect conductor"]),
],
"10.5": [
    ("In a series circuit, what stays the same?", "Current", ["Voltage", "Resistance", "Power"]),
    ("In a parallel circuit, what stays the same?", "Voltage across all branches", ["Current through all branches", "Resistance", "Power"]),
    ("Resistances in series:", "R_total = R₁ + R₂", ["1/R_total = 1/R₁ + 1/R₂", "R_total = R₁ × R₂", "R_total = R₁ − R₂"]),
    ("State Kirchhoff's Junction Rule (KCL).", "Current in = current out", ["Voltage in = voltage out", "Resistance in = resistance out", "Power in = power out"]),
    ("KCL represents conservation of:", "Charge", ["Energy", "Momentum", "Mass"]),
    ("KVL represents conservation of:", "Energy", ["Charge", "Momentum", "Mass"]),
    ("In parallel, currents combine as:", "I_total = I₁ + I₂", ["I_total = I₁ × I₂", "1/I_total = 1/I₁ + 1/I₂", "I_total = I₁ − I₂"]),
],
"10.6": [
    ("What produces magnetic fields?", "Moving charges (currents) and permanent magnets", ["Static charges only", "Gravity", "Sound waves"]),
    ("What is the SI unit of magnetic field?", "Tesla (T)", ["Newton (N)", "Henry (H)", "Weber (Wb)"]),
    ("Does a stationary charge experience a magnetic force?", "No", ["Yes", "Only in strong fields", "Only near magnets"]),
    ("What is the force on a moving charge in a B field?", "F = qvB sin θ", ["F = qvB cos θ", "F = qB/v", "F = qv/B"]),
    ("Does the magnetic force do work on a moving charge?", "No — it changes direction only", ["Yes", "Only at high speeds", "Only for electrons"]),
    ("The magnetic force is perpendicular to:", "Both v and B", ["Only v", "Only B", "Neither"]),
    ("Magnetic field lines outside a magnet go from:", "North to South", ["South to North", "East to West", "They don't have direction"]),
],
"10.7": [
    ("State Faraday's Law.", "EMF = −dΦ/dt", ["EMF = Φ/t", "EMF = BIL", "EMF = IR"]),
    ("What is magnetic flux?", "Φ = BA cos θ", ["Φ = BA sin θ", "Φ = B/A", "Φ = BA²"]),
    ("State Lenz's Law.", "Induced current opposes the change in flux that caused it", ["Induced current aids the change in flux", "There is no induced current", "Current always flows clockwise"]),
    ("Does a constant magnetic flux induce an EMF?", "No — flux must be changing", ["Yes", "Only in superconductors", "Only in coils"]),
    ("What does a generator convert?", "Mechanical energy to electrical energy", ["Electrical to mechanical", "Heat to light", "Chemical to kinetic"]),
    ("Name two applications of electromagnetic induction.", "Generators and transformers", ["Batteries and resistors", "Capacitors and inductors", "Magnets and compasses"]),
    ("Why is there a negative sign in Faraday's Law?", "Lenz's Law — the induced EMF opposes the change", ["It's a mathematical convention only", "EMF is always negative", "Flux is always negative"]),
],
"10.8": [
    ("What is alternating current (AC)?", "Current and voltage that vary sinusoidally", ["Constant current", "Current that only flows one way", "Direct current"]),
    ("What are RMS values?", "Equivalent DC values for calculating power", ["Maximum values", "Minimum values", "Average values"]),
    ("In a resistor, voltage and current are:", "In phase", ["90° out of phase", "180° out of phase", "45° out of phase"]),
    ("In a capacitor, current:", "Leads voltage by 90°", ["Lags voltage by 90°", "Is in phase with voltage", "Leads voltage by 180°"]),
    ("What is impedance?", "Total opposition to AC current", ["DC resistance only", "Capacitive reactance only", "Inductive reactance only"]),
    ("At resonance in an RLC circuit:", "Impedance is minimum (Z = R), current is maximum", ["Impedance is maximum", "Current is zero", "Voltage is zero"]),
    ("A step-up transformer:", "Increases voltage (N₂ > N₁)", ["Decreases voltage", "Increases current", "Has no effect"]),
],
"10.9": [
    ("How many equations are in Maxwell's set?", "Four", ["Three", "Five", "Two"]),
    ("What does Gauss's Law (Magnetic) tell us?", "No magnetic monopoles exist", ["Magnetic charges exist", "Electric fields are zero", "Gravity determines magnetism"]),
    ("What did Maxwell predict from his equations?", "Electromagnetic waves traveling at speed c", ["Gravitational waves", "Sound waves in vacuum", "Magnetic monopoles"]),
    ("What is the speed of electromagnetic waves?", "c ≈ 3 × 10⁸ m/s", ["c ≈ 343 m/s", "c ≈ 1500 m/s", "c ≈ 3 × 10⁶ m/s"]),
    ("What is light, according to Maxwell?", "An electromagnetic wave", ["A sound wave", "A mechanical wave", "A gravitational wave"]),
    ("Who confirmed Maxwell's prediction experimentally?", "Heinrich Hertz", ["Isaac Newton", "Albert Einstein", "Michael Faraday"]),
    ("What unification did Maxwell achieve?", "He unified electricity and magnetism", ["He unified gravity and light", "He unified mass and energy", "He unified sound and heat"]),
],
"11.1": [
    ("What is the photoelectric effect?", "Light ejects electrons from a metal surface", ["Light heats up metal", "Electrons create light", "Metal absorbs all light"]),
    ("What increases the maximum KE of photoelectrons?", "Increasing the frequency of light", ["Increasing the intensity below threshold", "Decreasing the frequency", "Making the metal thicker"]),
    ("What is Einstein's photoelectric equation?", "KE_max = hf − φ", ["KE = ½mv²", "E = mc²", "KE = hf + φ"]),
    ("What is the work function (φ)?", "Minimum energy to free an electron from the surface", ["Maximum energy of an electron", "The speed of light", "Planck's constant"]),
    ("Is emission of photoelectrons instantaneous?", "Yes — no time delay", ["No — there is always a delay", "Only for intense light", "Only for UV light"]),
    ("Why couldn't classical wave theory explain the photoelectric effect?", "It predicted any frequency would work with enough intensity", ["It predicted the correct results", "Classical theory doesn't discuss light", "It predicted electrons are waves"]),
    ("Does increasing intensity below threshold frequency eject electrons?", "No", ["Yes", "Only with enough time", "Only at low temperatures"]),
],
"11.2": [
    ("What experiment led to Rutherford's model?", "The gold foil experiment", ["The double-slit experiment", "The photoelectric effect", "Thomson's cathode ray experiment"]),
    ("What did Rutherford discover?", "Most of the atom is empty space with a tiny dense nucleus", ["Atoms are solid spheres", "Electrons orbit randomly", "Atoms have no nucleus"]),
    ("In the Bohr model, electrons move in:", "Fixed energy levels", ["Random paths", "Straight lines", "Spirals into the nucleus"]),
    ("Energy of the nth level in hydrogen:", "E_n = −13.6/n² eV", ["E_n = −13.6n² eV", "E_n = 13.6/n eV", "E_n = n × 13.6 eV"]),
    ("What is an emission spectrum?", "Bright lines from electrons dropping to lower levels", ["Dark lines in a continuous spectrum", "A continuous rainbow", "X-ray radiation"]),
    ("What describes electrons in the quantum mechanical model?", "Probability clouds (orbitals)", ["Definite circular orbits", "Straight line paths", "Fixed positions"]),
    ("Spectral lines are evidence of:", "Quantized energy levels", ["Continuous energy", "Classical orbits", "Wave-particle duality"]),
],
"11.3": [
    ("What are the two types of particles in a nucleus?", "Protons and neutrons", ["Electrons and protons", "Quarks and leptons", "Photons and neutrons"]),
    ("What is the atomic number Z?", "The number of protons", ["The number of neutrons", "The total nucleons", "The number of electrons in an ion"]),
    ("What are isotopes?", "Atoms with the same Z but different neutrons", ["Atoms with different Z", "Atoms with no neutrons", "Different elements with same mass"]),
    ("What is alpha decay?", "Emission of a ⁴₂He nucleus; Z decreases by 2, A by 4", ["Emission of an electron", "Emission of a photon", "Emission of a neutron"]),
    ("What is half-life?", "Time for half the radioactive nuclei to decay", ["Time for all nuclei to decay", "Time for one nucleus to form", "Time for radiation to stop"]),
    ("What is nuclear fission?", "A heavy nucleus splitting into lighter nuclei", ["Light nuclei combining", "Any nuclear reaction", "Radioactive decay only"]),
    ("What is nuclear fusion?", "Light nuclei combining into a heavier nucleus", ["Heavy nuclei splitting", "Chemical bonding", "Electron capture"]),
],
"11.4": [
    ("State Einstein's second postulate of special relativity.", "The speed of light is the same for all observers", ["Mass increases with speed", "Time runs faster for moving observers", "Nothing can move"]),
    ("What is time dilation?", "Moving clocks run slow: t = γt₀", ["Moving clocks run fast", "Time stops for all observers", "Time only exists at rest"]),
    ("What is the Lorentz factor (γ)?", "γ = 1/√(1 − v²/c²)", ["γ = v/c", "γ = mc²", "γ = 1 − v/c"]),
    ("What is the mass-energy equivalence?", "E = mc²", ["E = mv²", "E = mgh", "E = ½mv²"]),
    ("What happens to γ as v → c?", "γ → infinity", ["γ → 0", "γ → 1", "γ → c"]),
    ("What is length contraction?", "Moving objects are shorter in the direction of motion", ["Moving objects are longer", "Objects don't change length", "Length only changes at rest"]),
    ("At everyday speeds, γ is approximately:", "1", ["0", "Infinity", "c"]),
],
"11.5": [
    ("What is the Heisenberg Uncertainty Principle?", "Cannot simultaneously know exact position and momentum: Δx·Δp ≥ ℏ/2", ["Position and momentum can be known exactly", "Only momentum is uncertain", "It applies only to photons"]),
    ("What does |ψ|² represent?", "Probability density of finding the particle", ["Energy of the particle", "Velocity of the particle", "Charge of the particle"]),
    ("What is quantum tunneling?", "A particle passes through a barrier even when energy is less than the barrier", ["A particle bounces off all barriers", "A particle gains energy from nothing", "A particle loses all energy"]),
    ("What is the de Broglie wavelength?", "λ = h/p", ["λ = p/h", "λ = hv", "λ = mc"]),
    ("Is the uncertainty principle a measurement limitation?", "No — it is a fundamental property of nature", ["Yes — better instruments would fix it", "Only for small particles", "It's just a theory"]),
    ("What equation governs the wavefunction's evolution?", "The Schrödinger equation", ["Newton's equation", "Maxwell's equation", "Einstein's field equation"]),
    ("Why don't we observe quantum effects in everyday life?", "Macroscopic objects have incredibly tiny de Broglie wavelengths", ["Quantum effects don't exist", "Only atoms have wavefunctions", "Gravity cancels quantum effects"]),
],
"11.6": [
    ("What are the two families of fundamental particles?", "Quarks and leptons", ["Protons and neutrons", "Electrons and photons", "Bosons and fermions only"]),
    ("How many types of quarks are there?", "Six", ["Three", "Four", "Eight"]),
    ("What mediates the electromagnetic force?", "Photons", ["Gluons", "W and Z bosons", "Gravitons"]),
    ("What is the Higgs boson?", "The particle giving mass to fundamental particles via the Higgs field", ["The heaviest quark", "A type of lepton", "The carrier of gravity"]),
    ("When was the Higgs boson discovered?", "2012, at CERN", ["2000, at Fermilab", "1998, at CERN", "2020, at CERN"]),
    ("What is antimatter?", "Particles with same mass but opposite charge", ["Particles with no mass", "Dark matter", "Particles moving backward in time"]),
    ("What happens when a particle meets its antiparticle?", "Annihilation — converting to pure energy", ["They pass through each other", "They form a nucleus", "Nothing happens"]),
],
}


def build_quiz_html(questions, lesson_num):
    """Build quiz form HTML from question list."""
    html_parts = []
    for i, (q_text, correct, wrongs) in enumerate(questions, 1):
        name = f"q{i}"
        # Build all 4 options: correct first, then wrongs
        options = [(correct, "correct")] + [(w, "wrong") for w in wrongs]

        labels = []
        for text, val in options:
            labels.append(f'''                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="{name}" value="{val}"> {text}
                </label>''')

        labels_html = "\n                \n".join(labels)

        html_parts.append(f'''            <div class="quiz-question" style="margin-bottom: 2rem;" data-attempts="2">
                <p style="font-weight: 700; font-size: 1.45rem; margin-bottom: 1rem;">{i}. {q_text}</p>
            
{labels_html}
                
                <div class="attempts-indicator"></div>
                <div style="margin-top:1.5rem;">
                    <button type="button" class="action-button" onclick="window.checkQuizAnswer('{name}', 'correct', this)">Submit Answer</button>
                    <button type="button" class="nav-button" onclick="window.resetQuizQuestion(this)" style="margin-left:0.5rem;">Try Again</button>
                </div>
            </div>''')

    return "\n            \n".join(html_parts)


def build_nav_buttons(lesson_num):
    """Build correct navigation buttons."""
    next_lesson = get_next_lesson(lesson_num)
    back_btn = '''<button type="button" class="side-button" onclick="window.location.href='../../physics.html'">Back to Physics</button>'''

    if next_lesson:
        unit = next_lesson.split('.')[0]
        current_unit = lesson_num.split('.')[0]
        # If next lesson is in a different unit, need to navigate to that unit folder
        if unit != current_unit:
            href = f"../Unit{unit}/Lesson{next_lesson}_Video.html"
        else:
            href = f"Lesson{next_lesson}_Video.html"
        next_btn = f'''<button type="button" class="side-button" onclick="window.location.href='{href}'">Next Lesson: {next_lesson}</button>'''
    else:
        next_btn = '''<button type="button" class="side-button" onclick="window.location.href='../../physics.html'">🎉 Course Complete!</button>'''

    return f"""{back_btn}
{next_btn}"""


# ── Main ──────────────────────────────────────────────────────────────

base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                        "ArisEdu Project Folder", "PhysicsLessons")

quiz_files = glob.glob(os.path.join(base_dir, "Unit*", "Lesson*_Quiz.html"))
print(f"Found {len(quiz_files)} Quiz files\n")

# Pattern to match entire quiz form content (between <form id="quiz-form"> and </form>)
form_pattern = re.compile(
    r'(<form id="quiz-form">)\s*\n.*?\n(\s*</form>)',
    re.DOTALL
)

# Pattern for navigation buttons
nav_pattern = re.compile(
    r'<div class="summary-actions"[^>]*>.*?</div>',
    re.DOTALL
)

modified = 0
skipped = 0

for filepath in sorted(quiz_files):
    filename = os.path.basename(filepath)
    m = re.match(r'Lesson(\d+\.\d+)_Quiz\.html', filename)
    if not m:
        continue
    lesson_num = m.group(1)

    if lesson_num not in QUIZZES:
        print(f"  SKIP (no content): {filename}")
        skipped += 1
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Replace quiz form content
    quiz_html = build_quiz_html(QUIZZES[lesson_num], lesson_num)
    content = form_pattern.sub(
        r'\1\n\n' + quiz_html + '\n            \n\\2',
        content
    )

    # 2. Replace navigation buttons
    nav_html = build_nav_buttons(lesson_num)
    new_nav = f'''<div class="summary-actions" style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
{nav_html}
</div>'''
    content = nav_pattern.sub(new_nav, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        modified += 1
        print(f"  OK: {filename} ({len(QUIZZES[lesson_num])} questions)")
    else:
        print(f"  UNCHANGED: {filename}")

print(f"\nModified: {modified}/{len(quiz_files)} files")
if skipped:
    print(f"Skipped: {skipped} (no content defined)")
