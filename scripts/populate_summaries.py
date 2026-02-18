"""
Replace placeholder summary content in all 73 Physics Summary.html files
with actual educational content based on each lesson's topic.
"""
import os, re, glob

# Canonical lesson content for each lesson number
# Each entry: { "heading": "...", "body": "..." }
# body is raw HTML that goes inside <div class="lesson-notes">

CONTENT = {
"1.1": {
"heading": "Key Concepts: Physical Quantities &amp; Units",
"body": """<p><b>Physical Quantities</b></p>
<p>A physical quantity is any property of a material or system that can be measured. Every measurement has two parts: a <b>numerical value</b> and a <b>unit</b>.</p>
<ul>
<li><b>Base Quantities</b>: The seven fundamental quantities defined by the SI system — length (m), mass (kg), time (s), electric current (A), temperature (K), amount of substance (mol), and luminous intensity (cd).</li>
<li><b>Derived Quantities</b>: Quantities formed by combining base quantities through multiplication or division — e.g., speed (m/s), force (kg·m/s² = N), energy (kg·m²/s² = J).</li>
</ul>
<p><b>Why Units Matter</b></p>
<ul>
<li>Units ensure measurements are <b>meaningful and comparable</b>. A number without a unit (e.g., "5") has no physical meaning.</li>
<li>Consistent units prevent errors in calculations — always convert to SI before computing.</li>
<li>Unit analysis can help verify that an equation is dimensionally correct.</li>
</ul>"""
},
"1.2": {
"heading": "Key Concepts: SI System &amp; Prefixes",
"body": """<p><b>The International System of Units (SI)</b></p>
<p>The SI system is the globally adopted standard for scientific measurement. It defines seven base units from which all other units are derived.</p>
<ul>
<li><b>Meter (m)</b> — length</li>
<li><b>Kilogram (kg)</b> — mass</li>
<li><b>Second (s)</b> — time</li>
<li><b>Ampere (A)</b> — electric current</li>
<li><b>Kelvin (K)</b> — temperature</li>
<li><b>Mole (mol)</b> — amount of substance</li>
<li><b>Candela (cd)</b> — luminous intensity</li>
</ul>
<p><b>SI Prefixes</b></p>
<p>Prefixes scale units by powers of 10 for convenience:</p>
<ul>
<li><b>Giga (G)</b> = 10⁹, <b>Mega (M)</b> = 10⁶, <b>Kilo (k)</b> = 10³</li>
<li><b>Centi (c)</b> = 10⁻², <b>Milli (m)</b> = 10⁻³, <b>Micro (μ)</b> = 10⁻⁶, <b>Nano (n)</b> = 10⁻⁹</li>
</ul>
<p>Example: 5.2 km = 5.2 × 10³ m = 5200 m</p>"""
},
"1.3": {
"heading": "Key Concepts: Scalars vs Vectors",
"body": """<p><b>Scalar Quantities</b></p>
<p>Scalars have only <b>magnitude</b> (size). They are fully described by a number and a unit.</p>
<ul>
<li>Examples: mass (5 kg), temperature (300 K), speed (10 m/s), energy (50 J), time (3 s).</li>
</ul>
<p><b>Vector Quantities</b></p>
<p>Vectors have both <b>magnitude and direction</b>. They are represented by arrows.</p>
<ul>
<li>Examples: displacement (5 m east), velocity (10 m/s north), force (20 N downward), acceleration (9.8 m/s² down).</li>
</ul>
<p><b>Key Differences</b></p>
<ul>
<li>Scalars are added arithmetically: 3 kg + 2 kg = 5 kg.</li>
<li>Vectors must be added using <b>vector addition</b> (tip-to-tail or component method). Two 3 N forces at right angles give √(9+9) = 3√2 ≈ 4.24 N, not 6 N.</li>
<li>Distance is a scalar; displacement is a vector. Speed is a scalar; velocity is a vector.</li>
</ul>"""
},
"1.4": {
"heading": "Key Concepts: Accuracy, Precision, &amp; Significant Figures",
"body": """<p><b>Accuracy vs Precision</b></p>
<ul>
<li><b>Accuracy</b>: How close a measurement is to the <b>true (accepted) value</b>. High accuracy = small systematic error.</li>
<li><b>Precision</b>: How close repeated measurements are <b>to each other</b>. High precision = small random error.</li>
<li>A measurement can be precise but not accurate (consistently wrong), or accurate but not precise (scattered around the true value).</li>
</ul>
<p><b>Significant Figures</b></p>
<ul>
<li>All nonzero digits are significant: 123 has 3 sig figs.</li>
<li>Zeros between nonzero digits are significant: 1002 has 4 sig figs.</li>
<li>Leading zeros are NOT significant: 0.0045 has 2 sig figs.</li>
<li>Trailing zeros after a decimal point ARE significant: 2.50 has 3 sig figs.</li>
</ul>
<p><b>Rules for Calculations</b></p>
<ul>
<li><b>Multiplication/Division</b>: Result has the same number of sig figs as the factor with the fewest.</li>
<li><b>Addition/Subtraction</b>: Result is rounded to the same decimal place as the least precise input.</li>
</ul>"""
},
"1.5": {
"heading": "Key Concepts: Dimensional Analysis",
"body": """<p><b>What is Dimensional Analysis?</b></p>
<p>Dimensional analysis is a technique that uses the <b>dimensions</b> (units) of physical quantities to check equations, convert units, and derive relationships.</p>
<ul>
<li>Every term in a valid physics equation must have the <b>same dimensions</b> on both sides.</li>
<li>The three fundamental dimensions are: <b>[M]</b> (mass), <b>[L]</b> (length), <b>[T]</b> (time).</li>
</ul>
<p><b>Using Dimensional Analysis</b></p>
<ul>
<li><b>Checking equations</b>: Verify that F = ma is dimensionally correct → [M][L][T]⁻² = [M] · [L][T]⁻² ✓</li>
<li><b>Unit conversion</b>: Use conversion factors as fractions equal to 1. E.g., 60 mph × (1609 m / 1 mi) × (1 hr / 3600 s) ≈ 26.8 m/s.</li>
<li><b>Deriving formulas</b>: If the period T of a pendulum depends on length L and g, then T ∝ √(L/g) by dimensional reasoning.</li>
</ul>
<p><b>Limitations</b>: Dimensional analysis cannot determine dimensionless constants (like 2π) or distinguish between quantities with the same dimensions (work vs torque).</p>"""
},
"1.6": {
"heading": "Key Concepts: Measurement Uncertainty &amp; Error Analysis",
"body": """<p><b>Types of Errors</b></p>
<ul>
<li><b>Systematic Errors</b>: Consistent, repeatable errors that shift all measurements in the same direction. Caused by faulty equipment, calibration issues, or flawed technique. They affect <b>accuracy</b>.</li>
<li><b>Random Errors</b>: Unpredictable fluctuations that cause measurements to scatter around the true value. Caused by limitations of the instrument or observer. They affect <b>precision</b>.</li>
</ul>
<p><b>Expressing Uncertainty</b></p>
<ul>
<li><b>Absolute Uncertainty</b>: The ± range of a measurement. E.g., 5.0 ± 0.1 cm.</li>
<li><b>Percentage Uncertainty</b>: (absolute uncertainty / measured value) × 100%. E.g., (0.1/5.0) × 100% = 2%.</li>
</ul>
<p><b>Propagation of Uncertainties</b></p>
<ul>
<li><b>Addition/Subtraction</b>: Add absolute uncertainties. If A = 5.0 ± 0.1 and B = 3.0 ± 0.2, then A + B = 8.0 ± 0.3.</li>
<li><b>Multiplication/Division</b>: Add percentage uncertainties.</li>
<li><b>Powers</b>: Multiply the percentage uncertainty by the power. If x has 2% uncertainty, x³ has 6% uncertainty.</li>
</ul>"""
},
"2.1": {
"heading": "Key Concepts: Distance, Displacement, Speed, Velocity",
"body": """<p><b>Distance vs Displacement</b></p>
<ul>
<li><b>Distance</b> (scalar): Total path length traveled, regardless of direction. Always positive or zero.</li>
<li><b>Displacement</b> (vector): Straight-line distance from start to finish, with direction. Can be positive, negative, or zero.</li>
</ul>
<p><b>Speed vs Velocity</b></p>
<ul>
<li><b>Speed</b> (scalar): Rate of change of distance. Average speed = total distance / total time.</li>
<li><b>Velocity</b> (vector): Rate of change of displacement. Average velocity = displacement / time.</li>
<li><b>Instantaneous velocity</b>: Velocity at a specific instant, found as the limit of Δx/Δt as Δt → 0.</li>
</ul>
<p><b>Key Relationships</b></p>
<ul>
<li>An object moving in a circle at constant speed has <b>changing velocity</b> because direction changes.</li>
<li>Average speed ≥ |average velocity| (equality only for straight-line, one-direction motion).</li>
<li>On a position-time graph, velocity = slope of the curve.</li>
</ul>"""
},
"2.2": {
"heading": "Key Concepts: Acceleration",
"body": """<p><b>What is Acceleration?</b></p>
<p>Acceleration is the rate of change of velocity with respect to time.</p>
<ul>
<li><b>a</b> = Δv / Δt = (v_f − v_i) / t</li>
<li>SI unit: m/s² (meters per second squared).</li>
<li>Acceleration is a <b>vector</b> — it has magnitude and direction.</li>
</ul>
<p><b>Key Ideas</b></p>
<ul>
<li><b>Positive acceleration</b>: Velocity is increasing (speeding up in the positive direction, or slowing down in the negative direction).</li>
<li><b>Negative acceleration</b>: Velocity is decreasing in the positive direction (deceleration).</li>
<li>An object can have <b>zero velocity but nonzero acceleration</b> (e.g., a ball at the top of its trajectory).</li>
<li><b>Uniform acceleration</b>: Acceleration is constant — produces a straight line on a v-t graph.</li>
</ul>
<p><b>Graphical Interpretation</b></p>
<ul>
<li>On a velocity-time graph: acceleration = slope. Area under the curve = displacement.</li>
<li>On a position-time graph: acceleration causes the curve to bend (parabola for constant acceleration).</li>
</ul>"""
},
"2.3": {
"heading": "Key Concepts: Graphical Analysis of Motion",
"body": """<p><b>Position-Time (x-t) Graphs</b></p>
<ul>
<li><b>Slope</b> = velocity. A steeper slope means faster motion.</li>
<li>Straight line = constant velocity. Curved line = changing velocity (acceleration).</li>
<li>Horizontal line = object at rest.</li>
</ul>
<p><b>Velocity-Time (v-t) Graphs</b></p>
<ul>
<li><b>Slope</b> = acceleration. Positive slope = speeding up; negative slope = slowing down.</li>
<li><b>Area under the curve</b> = displacement. Area above the time axis is positive; below is negative.</li>
<li>Horizontal line = constant velocity (zero acceleration).</li>
</ul>
<p><b>Acceleration-Time (a-t) Graphs</b></p>
<ul>
<li><b>Area under the curve</b> = change in velocity (Δv).</li>
<li>Horizontal line = constant (uniform) acceleration.</li>
</ul>
<p><b>Converting Between Graphs</b></p>
<ul>
<li>Differentiate x-t → v-t → a-t (take slopes).</li>
<li>Integrate a-t → v-t → x-t (take areas).</li>
</ul>"""
},
"2.4": {
"heading": "Key Concepts: Equations of Motion (Constant Acceleration)",
"body": """<p><b>The Kinematic Equations</b> (SUVAT)</p>
<p>These equations apply when acceleration <b>a</b> is constant. The five variables are: s (displacement), u (initial velocity), v (final velocity), a (acceleration), t (time).</p>
<ul>
<li><b>v = u + at</b> — final velocity from initial velocity and acceleration.</li>
<li><b>s = ut + ½at²</b> — displacement from initial velocity, acceleration, and time.</li>
<li><b>v² = u² + 2as</b> — relates velocities to displacement (no time needed).</li>
<li><b>s = ½(u + v)t</b> — displacement from average velocity.</li>
</ul>
<p><b>Using the Equations</b></p>
<ul>
<li>Identify what you know (3 of 5 variables) and what you want to find.</li>
<li>Choose the equation that contains your known variables and the unknown.</li>
<li>Be consistent with signs: pick a positive direction and stick with it.</li>
</ul>
<p><b>Important Notes</b></p>
<ul>
<li>These equations assume <b>constant acceleration</b> — they fail if acceleration changes.</li>
<li>For free fall, use a = g = 9.8 m/s² (downward).</li>
</ul>"""
},
"2.5": {
"heading": "Key Concepts: Free Fall &amp; Projectile Motion",
"body": """<p><b>Free Fall</b></p>
<ul>
<li>Free fall is motion under gravity alone, with no air resistance.</li>
<li>All objects in free fall accelerate at <b>g ≈ 9.8 m/s²</b> downward, regardless of mass.</li>
<li>Use kinematic equations with a = −g (taking upward as positive).</li>
</ul>
<p><b>Projectile Motion</b></p>
<ul>
<li>A projectile moves in two dimensions: <b>horizontal</b> (constant velocity) and <b>vertical</b> (free fall).</li>
<li>Horizontal: x = v₀ₓ · t (no acceleration).</li>
<li>Vertical: y = v₀ᵧ · t − ½gt² (acceleration = −g).</li>
<li>The path traces a <b>parabola</b>.</li>
</ul>
<p><b>Key Formulas</b></p>
<ul>
<li>Range (horizontal distance): R = (v₀² sin 2θ) / g.</li>
<li>Maximum height: H = (v₀ sin θ)² / (2g).</li>
<li>Time of flight: T = 2v₀ sin θ / g.</li>
<li>Maximum range occurs at θ = 45°.</li>
</ul>"""
},
"2.6": {
"heading": "Key Concepts: Relative Motion &amp; Reference Frames",
"body": """<p><b>Reference Frames</b></p>
<ul>
<li>A reference frame is a coordinate system used to measure position and motion. All motion is <b>relative</b> to a chosen frame.</li>
<li><b>Inertial frame</b>: A frame not accelerating (Newton's laws hold directly).</li>
<li><b>Non-inertial frame</b>: An accelerating frame where fictitious forces appear.</li>
</ul>
<p><b>Relative Velocity</b></p>
<ul>
<li>The velocity of object A relative to object B: <b>v_AB = v_A − v_B</b>.</li>
<li>If two cars move in the same direction at 60 and 40 km/h, relative velocity = 20 km/h.</li>
<li>If moving toward each other, relative velocity = sum of speeds.</li>
</ul>
<p><b>Applications</b></p>
<ul>
<li><b>River crossing</b>: A boat's velocity relative to ground = boat velocity relative to water + water velocity relative to ground.</li>
<li><b>Rain problems</b>: The apparent direction of rain changes when you move.</li>
<li>The Galilean velocity addition formula applies at speeds much less than the speed of light.</li>
</ul>"""
},
"3.1": {
"heading": "Key Concepts: Force &amp; Interaction",
"body": """<p><b>What is Force?</b></p>
<ul>
<li>A force is a <b>push or pull</b> that can change an object's velocity (speed and/or direction).</li>
<li>Force is a <b>vector</b> quantity — it has magnitude and direction. SI unit: Newton (N).</li>
<li>1 N = 1 kg · m/s² — the force needed to accelerate 1 kg by 1 m/s².</li>
</ul>
<p><b>Types of Forces</b></p>
<ul>
<li><b>Contact forces</b>: Require physical touch — friction, tension, normal force, applied force, air resistance.</li>
<li><b>Non-contact (field) forces</b>: Act at a distance — gravity, electromagnetic force, nuclear forces.</li>
</ul>
<p><b>Free-Body Diagrams</b></p>
<ul>
<li>A free-body diagram shows <b>all forces acting on a single object</b> as arrows from its center of mass.</li>
<li>Arrow length represents magnitude; direction represents the direction of the force.</li>
<li>The <b>net force</b> (ΣF) is the vector sum of all forces. If ΣF = 0, the object is in equilibrium (no acceleration).</li>
</ul>"""
},
"3.2": {
"heading": "Key Concepts: Newton\u2019s First Law",
"body": """<p><b>Newton's First Law (Law of Inertia)</b></p>
<p>An object at rest stays at rest, and an object in motion stays in motion <b>with the same speed and direction</b>, unless acted upon by a net external force.</p>
<ul>
<li><b>Inertia</b>: The resistance of an object to changes in its state of motion. More mass = more inertia.</li>
<li>If the net force on an object is <b>zero</b>, its velocity does not change (it either stays still or moves at constant velocity).</li>
</ul>
<p><b>Equilibrium</b></p>
<ul>
<li><b>Static equilibrium</b>: Object is at rest and ΣF = 0.</li>
<li><b>Dynamic equilibrium</b>: Object moves at constant velocity and ΣF = 0.</li>
</ul>
<p><b>Everyday Examples</b></p>
<ul>
<li>A passenger lurches forward when a bus brakes suddenly — their body's inertia keeps them moving forward.</li>
<li>A hockey puck slides on ice (very low friction) and barely slows down.</li>
<li>Objects in deep space, far from gravitational influences, travel in straight lines at constant speeds indefinitely.</li>
</ul>"""
},
"3.3": {
"heading": "Key Concepts: Newton\u2019s Second Law (F = ma)",
"body": """<p><b>Newton's Second Law</b></p>
<p>The net force on an object equals its mass times its acceleration:</p>
<p style="text-align:center; font-size:1.2rem;"><b>ΣF = ma</b></p>
<ul>
<li>Greater force → greater acceleration (for the same mass).</li>
<li>Greater mass → less acceleration (for the same force).</li>
<li>Acceleration is always in the <b>same direction</b> as the net force.</li>
</ul>
<p><b>Weight vs Mass</b></p>
<ul>
<li><b>Mass</b> (kg): Amount of matter; does not change with location.</li>
<li><b>Weight</b> (N): The gravitational force on an object. W = mg, where g ≈ 9.8 m/s² on Earth.</li>
<li>A 70 kg person weighs about 686 N on Earth but only ~114 N on the Moon.</li>
</ul>
<p><b>Problem-Solving</b></p>
<ul>
<li>Draw a free-body diagram.</li>
<li>Choose a coordinate system.</li>
<li>Write ΣF = ma for each axis.</li>
<li>Solve for the unknown.</li>
</ul>"""
},
"3.4": {
"heading": "Key Concepts: Newton\u2019s Third Law",
"body": """<p><b>Newton's Third Law</b></p>
<p>For every action, there is an <b>equal and opposite reaction</b>.</p>
<ul>
<li>If object A exerts a force on object B, then B exerts a force on A that is <b>equal in magnitude</b> and <b>opposite in direction</b>.</li>
<li>Action-reaction pairs act on <b>different objects</b> — they never cancel each other.</li>
</ul>
<p><b>Examples</b></p>
<ul>
<li>You push a wall → the wall pushes you back with equal force.</li>
<li>Earth pulls you down (gravity) → you pull Earth up with the same force (but Earth barely moves due to its huge mass).</li>
<li>A rocket expels exhaust gases downward → the gases push the rocket upward.</li>
</ul>
<p><b>Common Misconceptions</b></p>
<ul>
<li>Action-reaction pairs do NOT cancel because they act on <b>different objects</b>.</li>
<li>The "heavier" object accelerates less because a = F/m (same F, bigger m).</li>
<li>Newton's third law always applies — there are no exceptions.</li>
</ul>"""
},
"3.5": {
"heading": "Key Concepts: Friction &amp; Tension",
"body": """<p><b>Friction</b></p>
<ul>
<li><b>Static friction (fₛ)</b>: Prevents an object from starting to move. fₛ ≤ μₛN (up to a maximum).</li>
<li><b>Kinetic friction (fₖ)</b>: Acts on a sliding object. fₖ = μₖN (constant).</li>
<li>μₛ > μₖ — it takes more force to start motion than to maintain it.</li>
<li><b>N</b> = normal force; <b>μ</b> = coefficient of friction (dimensionless, depends on surfaces).</li>
</ul>
<p><b>Tension</b></p>
<ul>
<li>Tension is the pulling force transmitted through a string, rope, or cable.</li>
<li>In an ideal (massless, inextensible) string, tension is the <b>same throughout</b>.</li>
<li>A pulley changes the <b>direction</b> of tension but not its magnitude (ideal pulley).</li>
</ul>
<p><b>Solving Problems</b></p>
<ul>
<li>Draw a free-body diagram for each object.</li>
<li>Apply ΣF = ma to each object separately.</li>
<li>For connected objects, they share the same acceleration (if the string is taut).</li>
</ul>"""
},
"3.6": {
"heading": "Key Concepts: Normal Force &amp; Inclined Planes",
"body": """<p><b>Normal Force</b></p>
<ul>
<li>The normal force (N) is the <b>perpendicular contact force</b> a surface exerts on an object.</li>
<li>On a flat surface: N = mg (weight). On an incline: N = mg cos θ.</li>
<li>The normal force adjusts to prevent objects from passing through surfaces.</li>
</ul>
<p><b>Inclined Planes</b></p>
<ul>
<li>Decompose weight into two components: <b>parallel</b> (mg sin θ, down the slope) and <b>perpendicular</b> (mg cos θ, into the surface).</li>
<li>Without friction, acceleration down the slope = g sin θ.</li>
<li>With friction: a = g sin θ − μₖg cos θ (down the slope).</li>
</ul>
<p><b>Key Angles</b></p>
<ul>
<li>The <b>angle of repose</b> is the steepest angle at which an object stays stationary: tan θ = μₛ.</li>
<li>At steeper angles, the object slides; at shallower angles, static friction holds it.</li>
</ul>"""
},
"3.7": {
"heading": "Key Concepts: Circular Motion &amp; Centripetal Force",
"body": """<p><b>Uniform Circular Motion</b></p>
<ul>
<li>An object moving in a circle at constant speed is always <b>accelerating</b> because its direction changes.</li>
<li>The acceleration points toward the <b>center</b> of the circle — called <b>centripetal acceleration</b>.</li>
<li>a_c = v²/r, where v is speed and r is radius.</li>
</ul>
<p><b>Centripetal Force</b></p>
<ul>
<li>The net inward force causing circular motion: <b>F_c = mv²/r = mω²r</b>.</li>
<li>Centripetal force is not a new type of force — it's provided by existing forces (tension, gravity, friction, normal force).</li>
</ul>
<p><b>Examples</b></p>
<ul>
<li>A car turning on a road: friction provides centripetal force.</li>
<li>A ball on a string: tension provides centripetal force.</li>
<li>The Moon orbiting Earth: gravity provides centripetal force.</li>
</ul>
<p><b>Period and Frequency</b>: T = 2πr/v, f = 1/T, ω = 2πf.</p>"""
},
"3.8": {
"heading": "Key Concepts: Non-Inertial Frames &amp; Pseudo-Forces",
"body": """<p><b>Non-Inertial Reference Frames</b></p>
<ul>
<li>A non-inertial frame is one that is <b>accelerating</b>. Newton's laws don't directly apply without modifications.</li>
<li>To use F = ma in a non-inertial frame, we introduce <b>pseudo-forces</b> (fictitious forces).</li>
</ul>
<p><b>Common Pseudo-Forces</b></p>
<ul>
<li><b>Pseudo-force in a linearly accelerating frame</b>: F_pseudo = −ma_frame. You feel pushed backward when a car accelerates forward.</li>
<li><b>Centrifugal force</b>: An outward pseudo-force felt in a rotating frame. F = mω²r (outward). It's not a real force — it's the result of inertia in a rotating reference frame.</li>
<li><b>Coriolis force</b>: Affects moving objects in a rotating frame. It deflects winds on Earth (right in the Northern Hemisphere, left in the Southern).</li>
</ul>
<p><b>Key Point</b></p>
<ul>
<li>Pseudo-forces are mathematical tools — they have no real physical source (no action-reaction pair).</li>
<li>In an inertial frame, the same phenomena are explained by the absence of centripetal force, not by centrifugal force.</li>
</ul>"""
},
"4.1": {
"heading": "Key Concepts: Work &amp; Energy Transfer",
"body": """<p><b>Work</b></p>
<ul>
<li>Work is done when a force causes displacement: <b>W = Fd cos θ</b>, where θ is the angle between the force and displacement.</li>
<li>SI unit: Joule (J). 1 J = 1 N·m.</li>
<li>Work is <b>positive</b> if force and displacement are in the same direction, <b>negative</b> if opposite, and <b>zero</b> if perpendicular (θ = 90°).</li>
</ul>
<p><b>Energy Transfer</b></p>
<ul>
<li>Work is the <b>mechanism for transferring energy</b> between objects or systems.</li>
<li>Positive work → energy is added to the object (it speeds up).</li>
<li>Negative work → energy is removed from the object (it slows down).</li>
</ul>
<p><b>Examples</b></p>
<ul>
<li>Pushing a box across the floor: you do positive work; friction does negative work.</li>
<li>Carrying a box horizontally at constant height: gravity does zero work (force perpendicular to displacement).</li>
<li>Lifting a box: you do positive work against gravity; gravity does negative work on the box.</li>
</ul>"""
},
"4.2": {
"heading": "Key Concepts: Kinetic Energy &amp; Potential Energy",
"body": """<p><b>Kinetic Energy (KE)</b></p>
<ul>
<li>The energy of motion: <b>KE = ½mv²</b>.</li>
<li>Doubles when speed doubles? No — <b>quadruples</b> (KE ∝ v²). Doubling speed quadruples the energy.</li>
<li>Always positive or zero (never negative).</li>
</ul>
<p><b>Potential Energy (PE)</b></p>
<ul>
<li><b>Gravitational PE</b>: Energy due to position in a gravitational field. PE = mgh (near Earth's surface).</li>
<li><b>Elastic PE</b>: Energy stored in a deformed elastic object. PE = ½kx² (spring).</li>
<li>Potential energy depends on a <b>reference point</b> — only changes in PE are physically meaningful.</li>
</ul>
<p><b>Mechanical Energy</b></p>
<ul>
<li>Total mechanical energy = KE + PE.</li>
<li>When only conservative forces act, mechanical energy is conserved: KE₁ + PE₁ = KE₂ + PE₂.</li>
<li>A falling ball converts PE to KE. A rising ball converts KE to PE.</li>
</ul>"""
},
"4.3": {
"heading": "Key Concepts: Conservation of Energy",
"body": """<p><b>The Law of Conservation of Energy</b></p>
<p>Energy cannot be created or destroyed — it can only be <b>transformed</b> from one form to another or <b>transferred</b> between objects.</p>
<ul>
<li>Total energy of an isolated system remains constant.</li>
<li>Energy forms include: kinetic, potential (gravitational, elastic, electric), thermal, chemical, nuclear, radiant.</li>
</ul>
<p><b>Conservation of Mechanical Energy</b></p>
<ul>
<li>When only <b>conservative forces</b> (gravity, springs) act: KE₁ + PE₁ = KE₂ + PE₂.</li>
<li>A pendulum swings back and forth converting KE ↔ PE continuously.</li>
<li>A roller coaster: highest point = max PE, lowest point = max KE.</li>
</ul>
<p><b>With Non-Conservative Forces</b></p>
<ul>
<li>Friction converts mechanical energy to <b>thermal energy</b>.</li>
<li>Modified equation: KE₁ + PE₁ = KE₂ + PE₂ + W_friction.</li>
<li>The total energy (all forms) is still conserved.</li>
</ul>"""
},
"4.4": {
"heading": "Key Concepts: Power &amp; Efficiency",
"body": """<p><b>Power</b></p>
<ul>
<li>Power is the <b>rate of doing work</b> or the rate of energy transfer: <b>P = W/t = ΔE/t</b>.</li>
<li>SI unit: Watt (W). 1 W = 1 J/s.</li>
<li>Alternative formula: <b>P = Fv</b> (force × velocity) for constant force along the direction of motion.</li>
</ul>
<p><b>Efficiency</b></p>
<ul>
<li>Efficiency measures how much input energy is converted to <b>useful output</b>:</li>
<li><b>η = (useful energy output / total energy input) × 100%</b>.</li>
<li>Efficiency is always ≤ 100%. No real machine is 100% efficient due to friction, heat loss, etc.</li>
</ul>
<p><b>Examples</b></p>
<ul>
<li>A 60 W light bulb converts 60 J of electrical energy every second (mostly to heat in incandescent bulbs).</li>
<li>A car engine might be 25% efficient — only 25% of fuel energy becomes motion; the rest is lost as heat.</li>
<li>LED bulbs are ~90% efficient at converting electrical energy to light.</li>
</ul>"""
},
"4.5": {
"heading": "Key Concepts: Work-Energy Theorem",
"body": """<p><b>The Work-Energy Theorem</b></p>
<p>The net work done on an object equals the change in its kinetic energy:</p>
<p style="text-align:center; font-size:1.2rem;"><b>W_net = ΔKE = ½mv² − ½mu²</b></p>
<ul>
<li>If net work is positive → object speeds up (KE increases).</li>
<li>If net work is negative → object slows down (KE decreases).</li>
<li>If net work is zero → speed doesn't change.</li>
</ul>
<p><b>Relationship to Newton's Second Law</b></p>
<ul>
<li>The theorem follows directly from F = ma and kinematics (v² = u² + 2as).</li>
<li>W_net = Fd = mad = m(v² − u²)/2 = ΔKE.</li>
</ul>
<p><b>Applications</b></p>
<ul>
<li>Finding braking distance: KE → 0 through friction. W_friction = ΔKE → μmgd = ½mv² → d = v²/(2μg).</li>
<li>Determining how much work a variable force does over a distance (area under F-x curve).</li>
</ul>"""
},
"4.6": {
"heading": "Key Concepts: Conservative vs. Non-Conservative Forces",
"body": """<p><b>Conservative Forces</b></p>
<ul>
<li>A force is conservative if the work done is <b>independent of the path</b> — it depends only on start and end positions.</li>
<li>Examples: gravity, elastic spring force, electrostatic force.</li>
<li>Work done in a closed loop by a conservative force = <b>0</b>.</li>
<li>Associated with <b>potential energy</b>: W = −ΔPE.</li>
</ul>
<p><b>Non-Conservative Forces</b></p>
<ul>
<li>Work done depends on the path taken.</li>
<li>Examples: friction, air resistance, tension (applied by a person), propulsion force.</li>
<li>Friction always does <b>negative work</b> — it converts mechanical energy to thermal energy.</li>
</ul>
<p><b>Energy Conservation with Both</b></p>
<ul>
<li>ΔKE + ΔPE = W_non-conservative.</li>
<li>If only conservative forces act: ΔKE + ΔPE = 0 (mechanical energy conserved).</li>
<li>If friction is present: some mechanical energy is lost as heat.</li>
</ul>"""
},
"5.1": {
"heading": "Key Concepts: Linear Momentum",
"body": """<p><b>Momentum</b></p>
<ul>
<li>Linear momentum is the product of mass and velocity: <b>p = mv</b>.</li>
<li>SI unit: kg·m/s. Momentum is a <b>vector</b> in the same direction as velocity.</li>
<li>A heavy slow object and a light fast object can have the same momentum.</li>
</ul>
<p><b>Newton's Second Law (Momentum Form)</b></p>
<ul>
<li><b>F = dp/dt</b> — Force equals the rate of change of momentum.</li>
<li>For constant mass: F = m(dv/dt) = ma (the familiar form).</li>
</ul>
<p><b>Conservation of Momentum</b></p>
<ul>
<li>In an <b>isolated system</b> (no external forces), total momentum before = total momentum after any interaction.</li>
<li>This applies to collisions, explosions, and any internal interaction.</li>
</ul>"""
},
"5.2": {
"heading": "Key Concepts: Impulse",
"body": """<p><b>What is Impulse?</b></p>
<ul>
<li>Impulse is the product of force and the time it acts: <b>J = FΔt</b>.</li>
<li>SI unit: N·s = kg·m/s (same as momentum).</li>
<li>Impulse equals the <b>change in momentum</b>: J = Δp = mv_f − mv_i.</li>
</ul>
<p><b>Impulse-Momentum Theorem</b></p>
<p style="text-align:center; font-size:1.1rem;"><b>FΔt = Δp</b></p>
<ul>
<li>A large force over a short time produces the same momentum change as a small force over a long time.</li>
<li>For variable force: impulse = area under the F-t graph.</li>
</ul>
<p><b>Applications</b></p>
<ul>
<li><b>Car airbags</b>: Extend the collision time → reduce the force on the passenger.</li>
<li><b>Catching a ball</b>: Moving your hand back extends contact time → less force on your hand.</li>
<li><b>Crumple zones</b>: Car structures designed to deform slowly, increasing Δt and reducing F.</li>
</ul>"""
},
"5.3": {
"heading": "Key Concepts: Conservation of Momentum",
"body": """<p><b>The Law of Conservation of Momentum</b></p>
<p>In an <b>isolated system</b> (no net external force), the total momentum remains constant:</p>
<p style="text-align:center; font-size:1.1rem;"><b>Σp_before = Σp_after</b></p>
<ul>
<li>m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂ (for two objects).</li>
<li>Applies in <b>all directions</b> independently (conserve x-momentum and y-momentum separately).</li>
</ul>
<p><b>Applications</b></p>
<ul>
<li><b>Collisions</b>: Momentum is conserved in all types (elastic, inelastic, perfectly inelastic).</li>
<li><b>Explosions</b>: Total momentum is zero before → total is still zero after (pieces fly in opposite directions).</li>
<li><b>Recoil</b>: When a gun fires, bullet and gun have equal and opposite momenta.</li>
</ul>
<p><b>Conditions</b></p>
<ul>
<li>External forces (friction, gravity) can break conservation — but during <b>short collisions</b>, their effect is often negligible.</li>
</ul>"""
},
"5.4": {
"heading": "Key Concepts: Elastic &amp; Inelastic Collisions",
"body": """<p><b>Elastic Collisions</b></p>
<ul>
<li>Both <b>momentum and kinetic energy</b> are conserved.</li>
<li>Objects bounce off each other. No permanent deformation or heat generated.</li>
<li>Example: billiard ball collisions (approximately), atomic/molecular collisions.</li>
</ul>
<p><b>Inelastic Collisions</b></p>
<ul>
<li><b>Momentum is conserved</b>, but kinetic energy is NOT — some KE is converted to heat, sound, or deformation.</li>
<li>Most real-world collisions are inelastic.</li>
</ul>
<p><b>Perfectly Inelastic Collisions</b></p>
<ul>
<li>Objects <b>stick together</b> after the collision. Maximum KE is lost.</li>
<li>m₁u₁ + m₂u₂ = (m₁ + m₂)v_f → v_f = (m₁u₁ + m₂u₂)/(m₁ + m₂).</li>
</ul>
<p><b>Comparing Collision Types</b></p>
<ul>
<li>Elastic: KE conserved, objects separate.</li>
<li>Inelastic: KE lost, objects separate.</li>
<li>Perfectly inelastic: Maximum KE lost, objects stick.</li>
</ul>"""
},
"5.5": {
"heading": "Key Concepts: Center of Mass",
"body": """<p><b>What is the Center of Mass?</b></p>
<ul>
<li>The center of mass (COM) is the average position of all mass in a system, weighted by mass.</li>
<li>For two particles: x_cm = (m₁x₁ + m₂x₂)/(m₁ + m₂).</li>
<li>The COM of a symmetric, uniform object is at its geometric center.</li>
</ul>
<p><b>Motion of the Center of Mass</b></p>
<ul>
<li>The COM moves as if all external forces were applied to a single particle of total mass M at that point.</li>
<li><b>F_ext = Ma_cm</b> — Newton's second law for the center of mass.</li>
<li>If no external forces act, the COM moves at constant velocity (or stays at rest).</li>
</ul>
<p><b>Applications</b></p>
<ul>
<li>In an explosion, individual pieces fly apart, but the COM follows the same parabolic path as before the explosion.</li>
<li>A high jumper arches their back so their COM passes <b>under</b> the bar even though their body clears it.</li>
</ul>"""
},
"5.6": {
"heading": "Key Concepts: Rocket Propulsion",
"body": """<p><b>How Rockets Work</b></p>
<ul>
<li>Rockets propel themselves by <b>expelling mass (exhaust gases) at high velocity</b> — conservation of momentum in action.</li>
<li>No external medium is needed — rockets work in the vacuum of space.</li>
</ul>
<p><b>The Rocket Equation (Tsiolkovsky)</b></p>
<ul>
<li><b>Δv = v_e · ln(m₀/m_f)</b>, where v_e is exhaust velocity, m₀ is initial mass, and m_f is final mass.</li>
<li>Higher exhaust velocity and larger mass ratio → greater speed change.</li>
</ul>
<p><b>Thrust</b></p>
<ul>
<li>Thrust = v_e · (dm/dt) — the exhaust velocity times the rate of mass ejection.</li>
<li>To lift off, thrust must exceed the rocket's weight (mg).</li>
</ul>
<p><b>Staging</b></p>
<ul>
<li>Multi-stage rockets discard empty fuel tanks to reduce mass, dramatically improving efficiency and achievable Δv.</li>
</ul>"""
},
"6.1": {
"heading": "Key Concepts: Newton\u2019s Law of Gravitation",
"body": """<p><b>Newton's Law of Universal Gravitation</b></p>
<p>Every mass attracts every other mass with a force:</p>
<p style="text-align:center; font-size:1.2rem;"><b>F = GMm/r²</b></p>
<ul>
<li><b>G</b> = 6.674 × 10⁻¹¹ N·m²/kg² (gravitational constant).</li>
<li>F is the force between masses M and m separated by distance r (center to center).</li>
<li>The force is always <b>attractive</b> and follows an <b>inverse-square law</b>.</li>
</ul>
<p><b>Key Points</b></p>
<ul>
<li>Double the distance → force decreases by a factor of 4.</li>
<li>The force acts equally on both objects (Newton's third law).</li>
<li>Near Earth's surface: F = mg, where g = GM/R² ≈ 9.8 m/s².</li>
</ul>"""
},
"6.2": {
"heading": "Key Concepts: Gravitational Field Strength",
"body": """<p><b>Gravitational Field</b></p>
<ul>
<li>A gravitational field exists around every mass. Any other mass placed in the field experiences a force.</li>
<li><b>Gravitational field strength (g)</b>: Force per unit mass at a point in the field.</li>
<li><b>g = F/m = GM/r²</b> — units: N/kg or m/s².</li>
</ul>
<p><b>Field Lines</b></p>
<ul>
<li>Field lines point <b>toward</b> the mass (gravity is attractive).</li>
<li>Closer lines = stronger field. Lines are radial around a point mass.</li>
<li>Near Earth's surface, field lines are approximately parallel (uniform field).</li>
</ul>
<p><b>Gravitational Potential Energy</b></p>
<ul>
<li>Near surface: PE = mgh.</li>
<li>General: PE = −GMm/r (negative because work must be done against gravity to move mass to infinity).</li>
<li>PE = 0 at infinite separation (by convention).</li>
</ul>"""
},
"6.3": {
"heading": "Key Concepts: Orbital Motion",
"body": """<p><b>Orbits</b></p>
<ul>
<li>An orbit occurs when gravity provides exactly the centripetal force needed for circular motion: <b>GMm/r² = mv²/r</b>.</li>
<li>Orbital speed: <b>v = √(GM/r)</b> — depends on the central mass M and orbital radius r, not on the orbiting mass.</li>
</ul>
<p><b>Orbital Period</b></p>
<ul>
<li>T = 2πr/v = 2π√(r³/GM).</li>
<li>Higher orbit → slower speed but longer period.</li>
</ul>
<p><b>Types of Orbits</b></p>
<ul>
<li><b>Circular orbit</b>: Constant radius, constant speed.</li>
<li><b>Elliptical orbit</b>: Varying radius and speed (Kepler's first law).</li>
<li><b>Geostationary orbit</b>: T = 24 hours, stays above the same point on Earth. r ≈ 42,164 km from Earth's center.</li>
</ul>"""
},
"6.4": {
"heading": "Key Concepts: Satellite Motion",
"body": """<p><b>Satellite Fundamentals</b></p>
<ul>
<li>A satellite stays in orbit because gravity provides centripetal force — it's in continuous <b>free fall</b> around Earth.</li>
<li>Orbital speed and period depend only on altitude and the mass of the central body.</li>
</ul>
<p><b>Types of Satellite Orbits</b></p>
<ul>
<li><b>Low Earth Orbit (LEO)</b>: 200–2,000 km altitude. T ≈ 90 min. Used for ISS, imaging.</li>
<li><b>Medium Earth Orbit (MEO)</b>: 2,000–35,786 km. Used for GPS satellites.</li>
<li><b>Geostationary Orbit (GEO)</b>: 35,786 km altitude. T = 24 hours. Used for communications and weather.</li>
</ul>
<p><b>Weightlessness</b></p>
<ul>
<li>Astronauts on the ISS feel weightless not because there's no gravity, but because they and the station are in <b>free fall together</b>.</li>
<li>At ISS altitude (~400 km), g ≈ 8.7 m/s² (about 89% of surface gravity).</li>
</ul>"""
},
"6.5": {
"heading": "Key Concepts: Escape Velocity",
"body": """<p><b>What is Escape Velocity?</b></p>
<ul>
<li>The minimum speed an object needs to <b>escape</b> a gravitational field without further propulsion.</li>
<li>At escape velocity, the object reaches infinity with zero speed (KE → 0 as PE → 0).</li>
</ul>
<p><b>Formula</b></p>
<p style="text-align:center; font-size:1.2rem;"><b>v_esc = √(2GM/r)</b></p>
<ul>
<li>From Earth's surface: v_esc ≈ 11.2 km/s.</li>
<li>Independent of the escaping object's mass.</li>
<li>Depends on the mass M and radius r of the body you're escaping from.</li>
</ul>
<p><b>Derivation</b></p>
<ul>
<li>Set total energy = 0 (just barely escaping): ½mv² − GMm/r = 0 → v = √(2GM/r).</li>
</ul>
<p><b>Comparison</b></p>
<ul>
<li>Escape velocity = √2 × orbital velocity at the same radius.</li>
<li>Moon: ~2.4 km/s. Jupiter: ~60 km/s. Sun: ~618 km/s.</li>
</ul>"""
},
"6.6": {
"heading": "Key Concepts: Kepler\u2019s Laws",
"body": """<p><b>Kepler's Three Laws of Planetary Motion</b></p>
<p><b>1. Law of Ellipses</b></p>
<ul>
<li>Every planet orbits the Sun in an <b>ellipse</b>, with the Sun at one <b>focus</b>.</li>
<li>Most planetary orbits are nearly circular (low eccentricity).</li>
</ul>
<p><b>2. Law of Equal Areas</b></p>
<ul>
<li>A line from the Sun to a planet sweeps out <b>equal areas in equal times</b>.</li>
<li>Planets move <b>faster</b> when closer to the Sun (perihelion) and <b>slower</b> when farther (aphelion).</li>
</ul>
<p><b>3. Law of Periods (Harmonic Law)</b></p>
<ul>
<li><b>T² ∝ r³</b> — the square of the orbital period is proportional to the cube of the semi-major axis.</li>
<li>T² = (4π²/GM) r³. This allows calculating one quantity from the other.</li>
</ul>
<p><b>Applications</b>: Kepler's third law is used to determine the masses of stars and planets, and to predict orbital parameters of satellites.</p>"""
},
"7.1": {
"heading": "Key Concepts: Simple Harmonic Motion (SHM)",
"body": """<p><b>What is SHM?</b></p>
<ul>
<li>A type of periodic motion where the <b>restoring force is proportional to displacement</b>: F = −kx.</li>
<li>The motion repeats in a sinusoidal pattern — described by sine or cosine functions.</li>
</ul>
<p><b>Key Equations</b></p>
<ul>
<li>Position: x(t) = A cos(ωt + φ).</li>
<li>Velocity: v(t) = −Aω sin(ωt + φ). Maximum speed = Aω (at equilibrium).</li>
<li>Acceleration: a(t) = −Aω² cos(ωt + φ) = −ω²x. Maximum acceleration = Aω² (at extremes).</li>
</ul>
<p><b>Examples of SHM</b></p>
<ul>
<li><b>Mass on a spring</b>: ω = √(k/m), T = 2π√(m/k).</li>
<li><b>Simple pendulum</b> (small angles): ω = √(g/L), T = 2π√(L/g).</li>
</ul>
<p><b>Important Properties</b></p>
<ul>
<li>Acceleration is always directed toward the <b>equilibrium position</b>.</li>
<li>Maximum displacement from equilibrium = <b>amplitude (A)</b>.</li>
</ul>"""
},
"7.2": {
"heading": "Key Concepts: Period, Frequency, Amplitude",
"body": """<p><b>Period (T)</b></p>
<ul>
<li>The time for one complete cycle of oscillation. SI unit: second (s).</li>
<li>For a pendulum: T = 2π√(L/g). For a mass-spring: T = 2π√(m/k).</li>
</ul>
<p><b>Frequency (f)</b></p>
<ul>
<li>The number of complete cycles per second: <b>f = 1/T</b>.</li>
<li>SI unit: Hertz (Hz). 1 Hz = 1 cycle per second.</li>
<li>Angular frequency: <b>ω = 2πf = 2π/T</b> (rad/s).</li>
</ul>
<p><b>Amplitude (A)</b></p>
<ul>
<li>The <b>maximum displacement</b> from the equilibrium position.</li>
<li>Amplitude determines the energy stored: E = ½kA² (spring). Greater amplitude = more energy.</li>
<li>Amplitude does NOT affect the period or frequency (in ideal SHM).</li>
</ul>
<p><b>Relationships</b></p>
<ul>
<li>Higher frequency = shorter period = more oscillations per second.</li>
<li>Amplitude is independent of frequency/period in SHM.</li>
</ul>"""
},
"7.3": {
"heading": "Key Concepts: Energy in SHM",
"body": """<p><b>Energy in Simple Harmonic Motion</b></p>
<ul>
<li>In SHM, energy continuously converts between <b>kinetic energy</b> and <b>potential energy</b>.</li>
<li>Total mechanical energy: <b>E = ½kA²</b> (constant, if no damping).</li>
</ul>
<p><b>At Key Positions</b></p>
<ul>
<li><b>Equilibrium (x = 0)</b>: PE = 0, KE = maximum = ½kA². Speed is maximum.</li>
<li><b>Extremes (x = ±A)</b>: KE = 0, PE = maximum = ½kA². Speed is zero.</li>
<li>At any position: KE + PE = ½kA² → ½mv² + ½kx² = ½kA².</li>
</ul>
<p><b>Graphs</b></p>
<ul>
<li>KE and PE are both sinusoidal and oscillate at <b>twice the frequency</b> of the motion.</li>
<li>When KE is at its peak, PE is at its minimum, and vice versa.</li>
<li>Total energy is a horizontal line on an Energy vs. Time graph.</li>
</ul>"""
},
"7.4": {
"heading": "Key Concepts: Wave Properties",
"body": """<p><b>What is a Wave?</b></p>
<ul>
<li>A wave is a disturbance that transfers <b>energy</b> through a medium (or space) without transferring matter.</li>
<li><b>Transverse waves</b>: Oscillation perpendicular to wave direction (light, water surface waves).</li>
<li><b>Longitudinal waves</b>: Oscillation parallel to wave direction (sound, compression springs).</li>
</ul>
<p><b>Key Properties</b></p>
<ul>
<li><b>Wavelength (λ)</b>: Distance between consecutive identical points (crest to crest). Unit: meters.</li>
<li><b>Frequency (f)</b>: Number of waves passing a point per second. Unit: Hz.</li>
<li><b>Speed (v)</b>: How fast the wave pattern moves. <b>v = fλ</b>.</li>
<li><b>Amplitude (A)</b>: Maximum displacement from rest — determines energy and intensity.</li>
</ul>
<p><b>The Wave Equation</b></p>
<ul>
<li><b>v = fλ</b> — the fundamental relationship between speed, frequency, and wavelength.</li>
<li>Wave speed depends on the <b>medium</b>, not on frequency or amplitude.</li>
</ul>"""
},
"7.5": {
"heading": "Key Concepts: Wave Superposition &amp; Interference",
"body": """<p><b>Principle of Superposition</b></p>
<ul>
<li>When two or more waves overlap, the resultant displacement at any point is the <b>sum</b> of the individual displacements.</li>
</ul>
<p><b>Constructive Interference</b></p>
<ul>
<li>Occurs when waves are <b>in phase</b> (crests align with crests).</li>
<li>Resultant amplitude = sum of amplitudes.</li>
<li>Path difference = 0, λ, 2λ, ... (nλ).</li>
</ul>
<p><b>Destructive Interference</b></p>
<ul>
<li>Occurs when waves are <b>out of phase</b> (crests align with troughs).</li>
<li>Resultant amplitude = difference of amplitudes. Complete cancellation if amplitudes are equal.</li>
<li>Path difference = λ/2, 3λ/2, ... ((n + ½)λ).</li>
</ul>
<p><b>Applications</b></p>
<ul>
<li>Young's double-slit experiment shows interference fringes (bright and dark bands).</li>
<li>Noise-canceling headphones use destructive interference.</li>
</ul>"""
},
"7.6": {
"heading": "Key Concepts: Standing Waves &amp; Resonance",
"body": """<p><b>Standing Waves</b></p>
<ul>
<li>Formed when two identical waves travel in <b>opposite directions</b> and interfere.</li>
<li>They have <b>nodes</b> (zero displacement) and <b>antinodes</b> (maximum displacement) at fixed positions.</li>
<li>Energy oscillates between kinetic and potential forms but does <b>not propagate</b> — the wave pattern stands still.</li>
</ul>
<p><b>Harmonics</b></p>
<ul>
<li><b>Fundamental (1st harmonic)</b>: Lowest frequency; L = λ/2 (string fixed at both ends).</li>
<li><b>2nd harmonic</b>: L = λ. <b>nth harmonic</b>: L = nλ/2.</li>
<li>f_n = nf₁ = nv/(2L) for a string fixed at both ends.</li>
</ul>
<p><b>Resonance</b></p>
<ul>
<li>Resonance occurs when a system is driven at its <b>natural frequency</b> — amplitude increases dramatically.</li>
<li>Examples: pushing a swing at the right frequency, a wine glass shattering from a matching sound wave.</li>
</ul>"""
},
"7.7": {
"heading": "Key Concepts: Doppler Effect",
"body": """<p><b>The Doppler Effect</b></p>
<ul>
<li>The change in observed frequency (and wavelength) due to <b>relative motion</b> between a source and observer.</li>
</ul>
<p><b>For Sound</b></p>
<ul>
<li><b>Source approaching</b>: Wavelength compressed → higher frequency (higher pitch).</li>
<li><b>Source receding</b>: Wavelength stretched → lower frequency (lower pitch).</li>
<li>Formula: f' = f × (v ± v_o)/(v ∓ v_s), where v is speed of sound, v_o is observer speed, v_s is source speed.</li>
</ul>
<p><b>For Light</b></p>
<ul>
<li><b>Blue shift</b>: Light from approaching objects has shorter wavelength (shifted blue).</li>
<li><b>Red shift</b>: Light from receding objects has longer wavelength (shifted red).</li>
<li>Astronomical red shift provides evidence that the universe is expanding.</li>
</ul>
<p><b>Applications</b>: Radar/speed guns, medical ultrasound, measuring stellar velocities.</p>"""
},
"7.8": {
"heading": "Key Concepts: Wave-Particle Duality",
"body": """<p><b>Wave-Particle Duality</b></p>
<ul>
<li>Light and matter exhibit both <b>wave-like</b> and <b>particle-like</b> behavior, depending on the experiment.</li>
</ul>
<p><b>Light as a Wave</b></p>
<ul>
<li>Interference, diffraction, and polarization are explained by wave theory.</li>
<li>Young's double-slit experiment showed light forms interference fringes — a wave property.</li>
</ul>
<p><b>Light as a Particle (Photon)</b></p>
<ul>
<li>The photoelectric effect showed light ejects electrons as if it were discrete packets (photons).</li>
<li>Photon energy: <b>E = hf</b>, where h = 6.63 × 10⁻³⁴ J·s (Planck's constant).</li>
</ul>
<p><b>Matter Waves (de Broglie)</b></p>
<ul>
<li>All particles have an associated wavelength: <b>λ = h/p = h/(mv)</b>.</li>
<li>For macroscopic objects, λ is incredibly tiny (undetectable). For electrons, λ is measurable and significant.</li>
<li>Electron diffraction confirmed that particles can behave as waves.</li>
</ul>"""
},
"8.1": {
"heading": "Key Concepts: Nature of Sound Waves",
"body": """<p><b>What is Sound?</b></p>
<ul>
<li>Sound is a <b>longitudinal mechanical wave</b> — it requires a medium (solid, liquid, or gas) to travel.</li>
<li>Sound cannot travel through a vacuum.</li>
<li>Sound waves consist of <b>compressions</b> (high pressure) and <b>rarefactions</b> (low pressure).</li>
</ul>
<p><b>Production and Detection</b></p>
<ul>
<li>Sound is produced by <b>vibrating objects</b> (vocal cords, speakers, tuning forks).</li>
<li>Detected by the ear (eardrum vibrates) or by microphones (diaphragm vibrates).</li>
</ul>
<p><b>Properties</b></p>
<ul>
<li>Sound waves can be reflected (echoes), refracted, diffracted, and can interfere.</li>
<li>Human hearing range: approximately <b>20 Hz to 20,000 Hz</b>.</li>
<li>Below 20 Hz: <b>infrasound</b>. Above 20,000 Hz: <b>ultrasound</b>.</li>
</ul>"""
},
"8.2": {
"heading": "Key Concepts: Speed of Sound",
"body": """<p><b>Speed of Sound</b></p>
<ul>
<li>In air at 20°C: approximately <b>343 m/s</b>.</li>
<li>Faster in liquids (~1,500 m/s in water) and fastest in solids (~5,000 m/s in steel).</li>
<li>Sound travels faster in denser, stiffer media.</li>
</ul>
<p><b>Factors Affecting Speed</b></p>
<ul>
<li><b>Temperature</b>: Speed increases with temperature. v ≈ 331 + 0.6T (T in °C).</li>
<li><b>Medium</b>: Solids > liquids > gases (generally).</li>
<li><b>Humidity</b>: Moist air carries sound slightly faster than dry air.</li>
</ul>
<p><b>The Wave Equation for Sound</b></p>
<ul>
<li><b>v = fλ</b> applies. If frequency increases, wavelength decreases (for a given medium).</li>
<li>When sound enters a different medium, speed and wavelength change, but <b>frequency stays the same</b>.</li>
</ul>"""
},
"8.3": {
"heading": "Key Concepts: Intensity &amp; Loudness",
"body": """<p><b>Sound Intensity</b></p>
<ul>
<li>Intensity is the <b>power per unit area</b>: I = P/A. SI unit: W/m².</li>
<li>Intensity follows an inverse-square law: <b>I ∝ 1/r²</b> (for a point source).</li>
<li>Threshold of hearing: ~10⁻¹² W/m². Threshold of pain: ~1 W/m².</li>
</ul>
<p><b>Decibel Scale</b></p>
<ul>
<li>Sound level in decibels: <b>β = 10 log₁₀(I/I₀)</b>, where I₀ = 10⁻¹² W/m².</li>
<li>Every increase of <b>10 dB</b> = 10× intensity. Every increase of <b>3 dB</b> ≈ 2× intensity.</li>
<li>Normal conversation: ~60 dB. Rock concert: ~110 dB. Damage threshold: ~85 dB (prolonged).</li>
</ul>
<p><b>Loudness vs Intensity</b></p>
<ul>
<li><b>Intensity</b> is a physical measurement (objective).</li>
<li><b>Loudness</b> is a perception (subjective) — depends on frequency, duration, and the listener's hearing.</li>
</ul>"""
},
"8.4": {
"heading": "Key Concepts: Pitch &amp; Frequency",
"body": """<p><b>Pitch</b></p>
<ul>
<li>Pitch is the <b>perceived frequency</b> of a sound — higher frequency = higher pitch.</li>
<li>Musical notes correspond to specific frequencies. Middle C ≈ 262 Hz. A4 = 440 Hz.</li>
</ul>
<p><b>Frequency and Musical Scales</b></p>
<ul>
<li>An <b>octave</b> = doubling of frequency. A4 = 440 Hz → A5 = 880 Hz.</li>
<li>The human ear perceives frequency logarithmically — equal ratios sound like equal intervals.</li>
</ul>
<p><b>Timbre (Tone Quality)</b></p>
<ul>
<li>Two instruments playing the same note sound different because of their <b>harmonic content</b> (overtones).</li>
<li>A pure tone is a single frequency (sine wave). Real sounds are combinations of harmonics.</li>
<li>The <b>fundamental frequency</b> determines pitch; higher harmonics determine timbre.</li>
</ul>"""
},
"8.5": {
"heading": "Key Concepts: Resonance in Air Columns",
"body": """<p><b>Resonance in Tubes</b></p>
<p>Sound waves in tubes create standing waves at specific resonant frequencies.</p>
<p><b>Open Tube (both ends open)</b></p>
<ul>
<li>Antinodes at both ends. Supports <b>all harmonics</b>.</li>
<li>f_n = nv/(2L), where n = 1, 2, 3, ...</li>
<li>Fundamental wavelength: λ₁ = 2L.</li>
</ul>
<p><b>Closed Tube (one end closed)</b></p>
<ul>
<li>Node at closed end, antinode at open end. Supports only <b>odd harmonics</b>.</li>
<li>f_n = nv/(4L), where n = 1, 3, 5, ...</li>
<li>Fundamental wavelength: λ₁ = 4L.</li>
</ul>
<p><b>Applications</b></p>
<ul>
<li>Musical instruments: flutes (open), clarinets (effectively closed).</li>
<li>Organ pipes produce different pitches based on length and whether they're open or closed.</li>
</ul>"""
},
"8.6": {
"heading": "Key Concepts: Beats &amp; Harmonics",
"body": """<p><b>Beats</b></p>
<ul>
<li>Beats occur when two waves with <b>slightly different frequencies</b> interfere.</li>
<li>The result is a periodic variation in loudness (throbbing sound).</li>
<li>Beat frequency: <b>f_beat = |f₁ − f₂|</b>.</li>
<li>Used in tuning instruments — beats disappear when frequencies match.</li>
</ul>
<p><b>Harmonics</b></p>
<ul>
<li>Harmonics are integer multiples of the fundamental frequency: f₁, 2f₁, 3f₁, ...</li>
<li>The <b>1st harmonic</b> = fundamental. <b>2nd harmonic</b> = 1st overtone. <b>3rd harmonic</b> = 2nd overtone.</li>
</ul>
<p><b>Harmonic Series</b></p>
<ul>
<li>Strings and open tubes produce <b>all harmonics</b>.</li>
<li>Closed tubes produce only <b>odd harmonics</b> (1st, 3rd, 5th, ...).</li>
<li>The mix of harmonics gives each instrument its unique <b>timbre</b>.</li>
</ul>"""
},
"9.1": {
"heading": "Key Concepts: Reflection &amp; Refraction",
"body": """<p><b>Reflection</b></p>
<ul>
<li><b>Law of Reflection</b>: Angle of incidence = angle of reflection (measured from the normal).</li>
<li><b>Specular reflection</b>: From smooth surfaces (mirrors) — clear image.</li>
<li><b>Diffuse reflection</b>: From rough surfaces — scattered in many directions.</li>
</ul>
<p><b>Refraction</b></p>
<ul>
<li>Light bends when it passes from one medium to another due to a change in speed.</li>
<li><b>Snell's Law</b>: n₁ sin θ₁ = n₂ sin θ₂.</li>
<li><b>Refractive index</b>: n = c/v (ratio of speed of light in vacuum to speed in the medium).</li>
</ul>
<p><b>Key Points</b></p>
<ul>
<li>Light bends <b>toward</b> the normal when entering a denser medium (n₂ > n₁).</li>
<li>Light bends <b>away</b> from the normal when entering a less dense medium.</li>
<li>Frequency is unchanged during refraction; wavelength changes.</li>
</ul>"""
},
"9.2": {
"heading": "Key Concepts: Lenses &amp; Mirrors",
"body": """<p><b>Mirrors</b></p>
<ul>
<li><b>Concave mirror</b>: Converging — forms real (inverted) or virtual (upright, magnified) images.</li>
<li><b>Convex mirror</b>: Diverging — always forms virtual, upright, diminished images.</li>
<li>Mirror equation: <b>1/f = 1/d_o + 1/d_i</b>.</li>
</ul>
<p><b>Lenses</b></p>
<ul>
<li><b>Convex (converging) lens</b>: Positive focal length. Can form real or virtual images.</li>
<li><b>Concave (diverging) lens</b>: Negative focal length. Always forms virtual, upright, diminished images.</li>
<li>Thin lens equation: <b>1/f = 1/d_o + 1/d_i</b> (same form as mirror equation).</li>
</ul>
<p><b>Magnification</b></p>
<ul>
<li>m = −d_i/d_o = h_i/h_o.</li>
<li>|m| > 1: enlarged. |m| < 1: diminished. Negative m: inverted.</li>
</ul>"""
},
"9.3": {
"heading": "Key Concepts: Total Internal Reflection",
"body": """<p><b>Total Internal Reflection (TIR)</b></p>
<ul>
<li>Occurs when light travels from a <b>denser to a less dense medium</b> at an angle greater than the <b>critical angle</b>.</li>
<li>All light is reflected back — none is refracted.</li>
</ul>
<p><b>Critical Angle</b></p>
<ul>
<li>sin θ_c = n₂/n₁ (where n₁ > n₂).</li>
<li>Glass to air: θ_c ≈ 42°. Water to air: θ_c ≈ 49°.</li>
<li>At exactly θ_c, the refracted ray travels along the boundary (θ₂ = 90°).</li>
</ul>
<p><b>Applications</b></p>
<ul>
<li><b>Optical fibers</b>: Light bounces along the fiber by TIR — used in telecommunications and medical endoscopes.</li>
<li><b>Prisms</b>: Binoculars use TIR prisms instead of mirrors for light reflection.</li>
<li><b>Diamonds</b>: Very low critical angle (~24°) causes maximum internal reflection → sparkle.</li>
</ul>"""
},
"9.4": {
"heading": "Key Concepts: Optical Instruments",
"body": """<p><b>The Human Eye</b></p>
<ul>
<li>The eye uses a <b>converging lens</b> to focus light on the retina.</li>
<li><b>Near point</b>: ~25 cm (closest clear focus). <b>Far point</b>: infinity (for normal vision).</li>
<li><b>Myopia</b> (nearsightedness): Corrected with diverging lens. <b>Hyperopia</b> (farsightedness): Corrected with converging lens.</li>
</ul>
<p><b>Magnifying Glass</b></p>
<ul>
<li>A converging lens held closer than its focal length produces a magnified, virtual, upright image.</li>
<li>Angular magnification ≈ 25 cm / f.</li>
</ul>
<p><b>Microscope</b></p>
<ul>
<li>Uses <b>two converging lenses</b>: objective (short f, near object) and eyepiece (longer f).</li>
<li>Total magnification = M_objective × M_eyepiece.</li>
</ul>
<p><b>Telescope</b></p>
<ul>
<li>Uses two lenses to view distant objects: objective (large f) creates an image at the focal point of the eyepiece.</li>
<li>Angular magnification ≈ f_objective / f_eyepiece.</li>
</ul>"""
},
"9.5": {
"heading": "Key Concepts: Diffraction &amp; Interference",
"body": """<p><b>Diffraction</b></p>
<ul>
<li>The bending and spreading of waves around obstacles or through openings.</li>
<li>Most significant when the opening/obstacle size is <b>comparable to the wavelength</b>.</li>
<li>Single-slit diffraction produces a central bright maximum with weaker secondary maxima.</li>
</ul>
<p><b>Double-Slit Interference (Young's Experiment)</b></p>
<ul>
<li>Two coherent sources produce an <b>interference pattern</b> of bright and dark fringes.</li>
<li>Bright fringes: d sin θ = nλ (constructive, n = 0, 1, 2, ...).</li>
<li>Dark fringes: d sin θ = (n + ½)λ (destructive).</li>
<li>Fringe spacing: Δy = λL/d.</li>
</ul>
<p><b>Diffraction Gratings</b></p>
<ul>
<li>Many parallel slits produce very sharp, bright maxima at d sin θ = nλ.</li>
<li>Used in spectrometers to separate light into its component wavelengths.</li>
</ul>"""
},
"9.6": {
"heading": "Key Concepts: Polarization",
"body": """<p><b>What is Polarization?</b></p>
<ul>
<li>Polarization restricts the <b>oscillation direction</b> of a transverse wave to a single plane.</li>
<li>Only <b>transverse waves</b> can be polarized — this confirms light is a transverse wave.</li>
<li>Unpolarized light oscillates in all directions perpendicular to propagation.</li>
</ul>
<p><b>Methods of Polarization</b></p>
<ul>
<li><b>Polarizing filters</b>: Absorb one component — only aligned vibrations pass (e.g., Polaroid sunglasses).</li>
<li><b>Reflection</b>: Reflected light is partially polarized. At <b>Brewster's angle</b>, reflected light is fully polarized.</li>
<li><b>Scattering</b>: Scattered light (blue sky) is partially polarized.</li>
</ul>
<p><b>Malus's Law</b></p>
<ul>
<li>When polarized light passes through a second polarizer (analyzer) at angle θ:</li>
<li><b>I = I₀ cos² θ</b>.</li>
<li>At θ = 0°: full transmission. At θ = 90°: zero transmission (crossed polarizers).</li>
</ul>"""
},
"10.1": {
"heading": "Key Concepts: Electric Charge &amp; Coulomb\u2019s Law",
"body": """<p><b>Electric Charge</b></p>
<ul>
<li>Two types: <b>positive</b> (protons) and <b>negative</b> (electrons). Like charges repel; unlike attract.</li>
<li>Charge is <b>quantized</b>: comes in multiples of e = 1.6 × 10⁻¹⁹ C.</li>
<li>Charge is <b>conserved</b>: total charge in an isolated system stays constant.</li>
</ul>
<p><b>Coulomb's Law</b></p>
<p style="text-align:center; font-size:1.2rem;"><b>F = kq₁q₂/r²</b></p>
<ul>
<li>k = 8.99 × 10⁹ N·m²/C² (Coulomb's constant).</li>
<li>Force is along the line joining the charges.</li>
<li>Inverse-square law: double the distance → force becomes ¼.</li>
</ul>
<p><b>Charging Methods</b></p>
<ul>
<li><b>Friction</b>: Rubbing transfers electrons between materials.</li>
<li><b>Conduction</b>: Direct contact with a charged object.</li>
<li><b>Induction</b>: Rearranging charges by bringing a charged object nearby without contact.</li>
</ul>"""
},
"10.2": {
"heading": "Key Concepts: Electric Field &amp; Potential",
"body": """<p><b>Electric Field</b></p>
<ul>
<li>A region where a charged particle experiences a force. <b>E = F/q = kQ/r²</b>.</li>
<li>Direction: away from positive charges, toward negative charges.</li>
<li>Unit: N/C or V/m.</li>
</ul>
<p><b>Electric Potential (Voltage)</b></p>
<ul>
<li>Electric potential is the <b>energy per unit charge</b>: V = U/q = kQ/r.</li>
<li>Potential difference (voltage): ΔV = W/q — work done per unit charge moving between two points.</li>
<li>Unit: Volt (V). 1 V = 1 J/C.</li>
</ul>
<p><b>Equipotential Lines</b></p>
<ul>
<li>Lines connecting points of equal potential. Always <b>perpendicular</b> to field lines.</li>
<li>No work is done moving a charge along an equipotential.</li>
</ul>
<p><b>Relationship</b>: E = −dV/dr. The field points in the direction of decreasing potential.</p>"""
},
"10.3": {
"heading": "Key Concepts: Capacitance",
"body": """<p><b>Capacitors</b></p>
<ul>
<li>A capacitor stores <b>electrical energy</b> in an electric field between two conductors (plates).</li>
<li><b>Capacitance</b>: C = Q/V — the ratio of charge stored to voltage applied. Unit: Farad (F).</li>
</ul>
<p><b>Parallel Plate Capacitor</b></p>
<ul>
<li>C = ε₀A/d, where A = plate area, d = plate separation, ε₀ = 8.85 × 10⁻¹² F/m.</li>
<li>Inserting a dielectric material (κ) between plates increases capacitance: C = κε₀A/d.</li>
</ul>
<p><b>Energy Stored</b></p>
<ul>
<li>E = ½CV² = ½QV = Q²/(2C).</li>
</ul>
<p><b>Combinations</b></p>
<ul>
<li><b>Parallel</b>: C_total = C₁ + C₂ + ... (add directly).</li>
<li><b>Series</b>: 1/C_total = 1/C₁ + 1/C₂ + ... (reciprocals add).</li>
</ul>"""
},
"10.4": {
"heading": "Key Concepts: Current, Resistance, &amp; Ohm\u2019s Law",
"body": """<p><b>Electric Current</b></p>
<ul>
<li>Current is the rate of flow of charge: <b>I = Q/t</b>. Unit: Ampere (A). 1 A = 1 C/s.</li>
<li>Conventional current flows from + to − (opposite to electron flow).</li>
</ul>
<p><b>Resistance</b></p>
<ul>
<li>Resistance opposes current flow: <b>R = ρL/A</b>, where ρ = resistivity, L = length, A = cross-sectional area.</li>
<li>Unit: Ohm (Ω). Resistivity depends on material and temperature.</li>
</ul>
<p><b>Ohm's Law</b></p>
<p style="text-align:center; font-size:1.2rem;"><b>V = IR</b></p>
<ul>
<li>The voltage across a resistor equals current times resistance.</li>
<li>Ohm's law applies to <b>ohmic</b> materials — those with constant resistance (e.g., metals at constant temperature).</li>
<li>Non-ohmic: diodes, filament bulbs (resistance changes with current/temperature).</li>
</ul>
<p><b>Power</b>: P = IV = I²R = V²/R.</p>"""
},
"10.5": {
"heading": "Key Concepts: DC Circuits &amp; Kirchhoff\u2019s Laws",
"body": """<p><b>Series Circuits</b></p>
<ul>
<li>Same current through all components: I_total = I₁ = I₂.</li>
<li>Voltages add: V_total = V₁ + V₂.</li>
<li>Resistances add: R_total = R₁ + R₂.</li>
</ul>
<p><b>Parallel Circuits</b></p>
<ul>
<li>Same voltage across all branches: V_total = V₁ = V₂.</li>
<li>Currents add: I_total = I₁ + I₂.</li>
<li>1/R_total = 1/R₁ + 1/R₂.</li>
</ul>
<p><b>Kirchhoff's Laws</b></p>
<ul>
<li><b>Junction Rule (KCL)</b>: Total current into a junction = total current out. (Conservation of charge.)</li>
<li><b>Loop Rule (KVL)</b>: The sum of all voltage gains and drops around any closed loop = 0. (Conservation of energy.)</li>
</ul>
<p><b>Problem-Solving</b></p>
<ul>
<li>Assign current directions (guess if needed — a negative answer means opposite direction).</li>
<li>Write KCL for junctions and KVL for loops. Solve the system of equations.</li>
</ul>"""
},
"10.6": {
"heading": "Key Concepts: Magnetic Fields &amp; Forces",
"body": """<p><b>Magnetic Fields</b></p>
<ul>
<li>Produced by moving charges (currents) and permanent magnets.</li>
<li>Field lines go from <b>North to South</b> outside the magnet.</li>
<li>Unit: Tesla (T). Earth's field ≈ 5 × 10⁻⁵ T.</li>
</ul>
<p><b>Force on a Moving Charge</b></p>
<ul>
<li><b>F = qvB sin θ</b> — force is perpendicular to both velocity and field (use right-hand rule).</li>
<li>A stationary charge experiences no magnetic force.</li>
<li>The magnetic force does no work (it changes direction, not speed).</li>
</ul>
<p><b>Force on a Current-Carrying Wire</b></p>
<ul>
<li><b>F = BIL sin θ</b> — force on a wire of length L carrying current I in field B.</li>
</ul>
<p><b>Right-Hand Rule</b>: Point fingers in the direction of velocity (or current), curl toward B — thumb points in the direction of force (for positive charges).</p>"""
},
"10.7": {
"heading": "Key Concepts: Electromagnetic Induction",
"body": """<p><b>Faraday's Law</b></p>
<ul>
<li>A changing magnetic flux through a loop induces an <b>EMF (voltage)</b>.</li>
<li><b>EMF = −dΦ/dt</b> (Faraday's law). Φ = BA cos θ (magnetic flux).</li>
<li>The induced EMF drives a current in a closed circuit.</li>
</ul>
<p><b>Lenz's Law</b></p>
<ul>
<li>The induced current flows in a direction that <b>opposes</b> the change in flux that caused it.</li>
<li>This is the reason for the negative sign in Faraday's law — it ensures energy conservation.</li>
</ul>
<p><b>Ways to Induce EMF</b></p>
<ul>
<li>Change the magnetic field strength (B).</li>
<li>Change the area of the loop (A).</li>
<li>Change the angle between the loop and the field (θ).</li>
<li>Move a conductor through a magnetic field.</li>
</ul>
<p><b>Applications</b>: Generators, transformers, induction cooktops, wireless charging.</p>"""
},
"10.8": {
"heading": "Key Concepts: Alternating Current (AC) Circuits",
"body": """<p><b>Alternating Current</b></p>
<ul>
<li>AC current and voltage vary sinusoidally: V = V₀ sin(ωt), I = I₀ sin(ωt).</li>
<li><b>RMS values</b>: V_rms = V₀/√2, I_rms = I₀/√2. These are the equivalent DC values for power calculations.</li>
</ul>
<p><b>AC Circuit Components</b></p>
<ul>
<li><b>Resistor</b>: V and I are in phase. P = I²R.</li>
<li><b>Capacitor</b>: Current leads voltage by 90°. Reactance: X_C = 1/(ωC).</li>
<li><b>Inductor</b>: Voltage leads current by 90°. Reactance: X_L = ωL.</li>
</ul>
<p><b>Impedance</b></p>
<ul>
<li>Z = √(R² + (X_L − X_C)²) — total opposition to AC.</li>
<li><b>Resonance</b>: When X_L = X_C (ω = 1/√(LC)), impedance is minimum (Z = R) and current is maximum.</li>
</ul>
<p><b>Transformers</b>: V₂/V₁ = N₂/N₁. Step-up (N₂ > N₁) increases voltage; step-down decreases it.</p>"""
},
"10.9": {
"heading": "Key Concepts: Maxwell\u2019s Equations (Introductory)",
"body": """<p><b>Maxwell's Four Equations</b></p>
<p>These equations unify electricity and magnetism and predict electromagnetic waves.</p>
<ul>
<li><b>Gauss's Law (Electric)</b>: Electric flux through a closed surface ∝ enclosed charge. ∮E·dA = Q/ε₀.</li>
<li><b>Gauss's Law (Magnetic)</b>: No magnetic monopoles exist. ∮B·dA = 0 (field lines always form closed loops).</li>
<li><b>Faraday's Law</b>: A changing magnetic field induces an electric field. ∮E·dl = −dΦ_B/dt.</li>
<li><b>Ampère-Maxwell Law</b>: Magnetic fields are produced by currents and by changing electric fields. ∮B·dl = μ₀I + μ₀ε₀(dΦ_E/dt).</li>
</ul>
<p><b>Electromagnetic Waves</b></p>
<ul>
<li>Maxwell showed that changing E and B fields propagate as waves at speed <b>c = 1/√(μ₀ε₀)</b> ≈ 3 × 10⁸ m/s.</li>
<li>This predicted that light is an electromagnetic wave — later confirmed by Hertz.</li>
</ul>"""
},
"11.1": {
"heading": "Key Concepts: Photoelectric Effect",
"body": """<p><b>The Photoelectric Effect</b></p>
<ul>
<li>Light shining on a metal surface can eject electrons — these are called <b>photoelectrons</b>.</li>
<li>This effect could not be explained by classical wave theory.</li>
</ul>
<p><b>Key Observations</b></p>
<ul>
<li>There is a <b>threshold frequency</b> (f₀) below which no electrons are emitted, regardless of intensity.</li>
<li>Above f₀, increasing intensity increases the <b>number</b> of electrons but not their maximum KE.</li>
<li>Increasing frequency increases the <b>maximum KE</b> of emitted electrons.</li>
<li>Emission is <b>instantaneous</b> — no time delay.</li>
</ul>
<p><b>Einstein's Explanation</b></p>
<ul>
<li>Light consists of <b>photons</b>, each with energy E = hf.</li>
<li><b>KE_max = hf − φ</b>, where φ = hf₀ is the work function (minimum energy to free an electron).</li>
<li>Below the threshold frequency, no single photon has enough energy to eject an electron.</li>
</ul>"""
},
"11.2": {
"heading": "Key Concepts: Atomic Models",
"body": """<p><b>Historical Atomic Models</b></p>
<ul>
<li><b>Thomson's "Plum Pudding"</b>: Positive charge spread uniformly with electrons embedded in it.</li>
<li><b>Rutherford's Nuclear Model</b>: Most of the atom is empty space; mass and positive charge concentrated in a tiny <b>nucleus</b>. Discovered via gold foil experiment.</li>
<li><b>Bohr Model</b>: Electrons orbit the nucleus in fixed energy levels (n = 1, 2, 3...). Electrons can only gain or lose energy by jumping between levels.</li>
<li><b>Quantum Mechanical Model</b>: Electrons exist in probability clouds (orbitals), not definite paths.</li>
</ul>
<p><b>Bohr Model Details</b></p>
<ul>
<li>Energy levels: E_n = −13.6/n² eV (for hydrogen).</li>
<li>Photon emission: ΔE = hf = E_upper − E_lower.</li>
<li>Spectral lines correspond to transitions between specific energy levels.</li>
</ul>
<p><b>Line Spectra</b></p>
<ul>
<li><b>Emission spectrum</b>: Bright lines from hot gas — electrons dropping to lower levels.</li>
<li><b>Absorption spectrum</b>: Dark lines where light is absorbed — electrons jumping to higher levels.</li>
</ul>"""
},
"11.3": {
"heading": "Key Concepts: Nuclear Physics",
"body": """<p><b>Nuclear Structure</b></p>
<ul>
<li>Nucleus contains <b>protons</b> (positive) and <b>neutrons</b> (neutral), collectively called <b>nucleons</b>.</li>
<li>Atomic number Z = number of protons. Mass number A = protons + neutrons.</li>
<li><b>Isotopes</b>: Same Z, different number of neutrons.</li>
</ul>
<p><b>Radioactive Decay</b></p>
<ul>
<li><b>Alpha (α)</b>: Emits ⁴₂He. Z decreases by 2, A decreases by 4.</li>
<li><b>Beta (β⁻)</b>: A neutron → proton + electron + antineutrino. Z increases by 1.</li>
<li><b>Gamma (γ)</b>: Emission of a high-energy photon. No change in Z or A.</li>
<li>Half-life: Time for half the nuclei to decay. N = N₀(½)^(t/t½).</li>
</ul>
<p><b>Nuclear Reactions</b></p>
<ul>
<li><b>Fission</b>: A heavy nucleus splits into lighter nuclei, releasing energy (nuclear reactors, atomic bombs).</li>
<li><b>Fusion</b>: Light nuclei combine to form a heavier nucleus, releasing energy (stars, hydrogen bombs).</li>
<li>Both release energy due to <b>mass defect</b>: E = Δmc² (Einstein's mass-energy equivalence).</li>
</ul>"""
},
"11.4": {
"heading": "Key Concepts: Special Relativity",
"body": """<p><b>Einstein's Two Postulates</b></p>
<ul>
<li><b>1.</b> The laws of physics are the same in all inertial reference frames.</li>
<li><b>2.</b> The speed of light in vacuum (c ≈ 3 × 10⁸ m/s) is the same for all observers, regardless of their motion.</li>
</ul>
<p><b>Key Consequences</b></p>
<ul>
<li><b>Time Dilation</b>: Moving clocks run slow. t = γt₀, where γ = 1/√(1 − v²/c²).</li>
<li><b>Length Contraction</b>: Moving objects are shorter in the direction of motion. L = L₀/γ.</li>
<li><b>Mass-Energy Equivalence</b>: E = mc². A small amount of mass corresponds to a huge amount of energy.</li>
</ul>
<p><b>The Lorentz Factor (γ)</b></p>
<ul>
<li>γ = 1 at v = 0 (no relativistic effects).</li>
<li>γ → ∞ as v → c (effects become extreme).</li>
<li>At everyday speeds, γ ≈ 1 and effects are negligible.</li>
</ul>
<p><b>Relativistic Energy</b>: E² = (pc)² + (mc²)². For a photon (m = 0): E = pc.</p>"""
},
"11.5": {
"heading": "Key Concepts: Quantum Mechanics",
"body": """<p><b>Key Principles</b></p>
<ul>
<li><b>Wave-Particle Duality</b>: All matter exhibits both wave and particle properties. λ = h/p.</li>
<li><b>Quantization</b>: Energy, angular momentum, and other properties come in discrete amounts.</li>
</ul>
<p><b>The Wavefunction (ψ)</b></p>
<ul>
<li>The wavefunction describes the quantum state of a particle.</li>
<li><b>|ψ|²</b> gives the probability density of finding the particle at a given position.</li>
<li>The wavefunction evolves according to the <b>Schrödinger equation</b>.</li>
</ul>
<p><b>Heisenberg's Uncertainty Principle</b></p>
<ul>
<li>It is impossible to simultaneously know both the exact position and momentum of a particle:</li>
<li><b>Δx · Δp ≥ ℏ/2</b> (where ℏ = h/2π).</li>
<li>This is not a measurement limitation — it's a fundamental property of nature.</li>
</ul>
<p><b>Quantum Tunneling</b>: A particle can pass through a potential barrier even if its energy is less than the barrier height — there is a nonzero probability of being found on the other side.</p>"""
},
"11.6": {
"heading": "Key Concepts: Particle Physics &amp; Standard Model",
"body": """<p><b>Fundamental Particles</b></p>
<ul>
<li>Matter is made of <b>quarks</b> (make up protons/neutrons) and <b>leptons</b> (electrons, neutrinos).</li>
<li>There are <b>6 quarks</b>: up, down, charm, strange, top, bottom.</li>
<li>There are <b>6 leptons</b>: electron, muon, tau, and their corresponding neutrinos.</li>
</ul>
<p><b>The Four Fundamental Forces</b></p>
<ul>
<li><b>Strong Nuclear Force</b>: Holds quarks together inside protons/neutrons. Mediated by gluons.</li>
<li><b>Electromagnetic Force</b>: Between charged particles. Mediated by photons.</li>
<li><b>Weak Nuclear Force</b>: Responsible for radioactive beta decay. Mediated by W and Z bosons.</li>
<li><b>Gravitational Force</b>: Between masses. Hypothetically mediated by gravitons (unconfirmed).</li>
</ul>
<p><b>The Higgs Boson</b></p>
<ul>
<li>The Higgs field gives mass to fundamental particles. The Higgs boson was discovered in 2012 at CERN.</li>
</ul>
<p><b>Antimatter</b>: Every particle has an antiparticle (same mass, opposite charge). When they meet: <b>annihilation</b> → pure energy.</p>"""
},
}

base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                        "ArisEdu Project Folder", "PhysicsLessons")

summary_files = glob.glob(os.path.join(base_dir, "Unit*", "Lesson*_Summary.html"))
print(f"Found {len(summary_files)} Summary files\n")

modified = 0
skipped = 0

for filepath in sorted(summary_files):
    filename = os.path.basename(filepath)
    m = re.match(r'Lesson(\d+\.\d+)_Summary\.html', filename)
    if not m:
        continue
    lesson_num = m.group(1)

    if lesson_num not in CONTENT:
        print(f"  SKIP (no content): {filename}")
        skipped += 1
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    heading = CONTENT[lesson_num]["heading"]
    body = CONTENT[lesson_num]["body"]

    # Build the new lesson-notes inner HTML
    new_notes = f'<h3>{heading}</h3>\n{body}'

    # Replace the lesson-notes content
    # Pattern: <div class="lesson-notes">...anything...</div>
    # followed by the summary-actions div
    pattern = r'(<div class="lesson-notes">).*?(</div>\s*<div class="summary-actions">)'
    replacement = r'\1\n' + new_notes + r'\n\2'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified += 1
        print(f"  OK: {filename}")
    else:
        print(f"  UNCHANGED: {filename}")

print(f"\nModified: {modified}/{len(summary_files)} files")
if skipped:
    print(f"Skipped: {skipped} (no content defined)")
