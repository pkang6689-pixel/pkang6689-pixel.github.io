"""Add flashcards to all 73 Physics lessons."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "physics_lessons.json")

FC = {
    # ── Unit 1: Measurement & Units ─────────────────────────────────
    "u1_l1.1": [
        ("Physical Quantity", "A measurable property of a physical system (e.g., mass, length, time)."),
        ("Base Quantity", "One of the seven fundamental quantities in SI: length, mass, time, current, temperature, amount of substance, luminous intensity."),
        ("Derived Quantity", "A quantity formed from combinations of base quantities (e.g., velocity = length/time)."),
        ("Unit", "A standard used to measure a physical quantity (e.g., meter, kilogram, second)."),
        ("Measurement", "The process of comparing a physical quantity to a standard unit."),
    ],
    "u1_l1.2": [
        ("SI System", "The International System of Units — the globally accepted metric system with seven base units."),
        ("Prefix", "A multiplier attached to a unit (e.g., kilo- = 10³, milli- = 10⁻³, nano- = 10⁻⁹)."),
        ("Meter (m)", "The SI base unit of length."),
        ("Kilogram (kg)", "The SI base unit of mass."),
        ("Second (s)", "The SI base unit of time."),
    ],
    "u1_l1.3": [
        ("Scalar", "A quantity with magnitude only (e.g., speed, mass, temperature)."),
        ("Vector", "A quantity with both magnitude and direction (e.g., velocity, force, displacement)."),
        ("Magnitude", "The size or amount of a quantity."),
        ("Resultant Vector", "The single vector that has the same effect as two or more vectors combined."),
        ("Vector Addition", "Vectors are added tip-to-tail; the resultant goes from the start of the first to the end of the last."),
    ],
    "u1_l1.4": [
        ("Accuracy", "How close a measurement is to the true value."),
        ("Precision", "How close repeated measurements are to each other."),
        ("Significant Figures", "All reliably known digits plus one estimated digit in a measurement."),
        ("Systematic Error", "A consistent error in one direction; affects accuracy."),
        ("Random Error", "Irregular fluctuations in measurements; affects precision."),
    ],
    "u1_l1.5": [
        ("Dimensional Analysis", "Using units to check equations and convert between unit systems."),
        ("Dimension", "The physical nature of a quantity expressed in terms of base quantities (e.g., [L], [M], [T])."),
        ("Conversion Factor", "A ratio equal to 1 used to convert units (e.g., 1 km / 1000 m)."),
        ("Dimensional Consistency", "Both sides of an equation must have the same dimensions."),
        ("Unit Cancellation", "Multiplying by conversion factors so unwanted units cancel."),
    ],
    "u1_l1.6": [
        ("Absolute Uncertainty", "The margin of error in a measurement, in the same units as the measurement."),
        ("Relative (Percentage) Uncertainty", "(absolute uncertainty / measured value) × 100%."),
        ("Propagation of Uncertainty", "Rules for combining uncertainties: add for sums/differences; add percentages for products/quotients."),
        ("Error Analysis", "Evaluating how measurement uncertainties affect calculated results."),
        ("Percent Error", "|experimental − accepted| / accepted × 100%."),
    ],

    # ── Unit 2: Kinematics ──────────────────────────────────────────
    "u2_l2.1": [
        ("Distance", "The total path length traveled; a scalar quantity."),
        ("Displacement", "The straight-line change in position from start to end; a vector."),
        ("Speed", "The rate of distance traveled: speed = distance / time; a scalar."),
        ("Velocity", "The rate of displacement: v = Δx / Δt; a vector."),
        ("Average vs Instantaneous", "Average is over an interval; instantaneous is at a specific moment."),
    ],
    "u2_l2.2": [
        ("Acceleration", "The rate of change of velocity: a = Δv / Δt; a vector (m/s²)."),
        ("Uniform Acceleration", "Constant acceleration — velocity changes at a steady rate."),
        ("Deceleration", "Acceleration opposite to the direction of motion (slowing down)."),
        ("Direction of Acceleration", "Points in the direction of the change in velocity."),
        ("Instantaneous Acceleration", "Acceleration at a specific instant; slope of v-t graph at a point."),
    ],
    "u2_l2.3": [
        ("Position-Time Graph", "Slope = velocity. Straight line = constant velocity; curve = acceleration."),
        ("Velocity-Time Graph", "Slope = acceleration. Area under curve = displacement."),
        ("Acceleration-Time Graph", "Area under curve = change in velocity."),
        ("Uniform Motion", "Horizontal line on v-t graph; straight diagonal on x-t graph."),
        ("Non-Uniform Motion", "Curved lines on x-t or v-t graphs indicate changing velocity or acceleration."),
    ],
    "u2_l2.4": [
        ("v = v₀ + at", "Final velocity = initial velocity + (acceleration × time)."),
        ("x = v₀t + ½at²", "Displacement = initial velocity × time + half acceleration × time²."),
        ("v² = v₀² + 2ax", "Relates velocity, acceleration, and displacement without time."),
        ("x = ½(v₀ + v)t", "Displacement = average velocity × time."),
        ("Constant Acceleration", "These kinematic equations only apply when acceleration is constant."),
    ],
    "u2_l2.5": [
        ("Free Fall", "Motion under gravity alone; a = g ≈ 9.8 m/s² downward."),
        ("Projectile Motion", "Motion in two dimensions under gravity: horizontal (constant v) and vertical (free fall)."),
        ("Range", "The horizontal distance a projectile travels; max at 45° launch angle."),
        ("Trajectory", "The parabolic path of a projectile (ignoring air resistance)."),
        ("Independence of Axes", "Horizontal and vertical motions are analyzed independently."),
    ],
    "u2_l2.6": [
        ("Reference Frame", "A coordinate system used to describe motion; can be stationary or moving."),
        ("Relative Velocity", "The velocity of one object as observed from another: v_AB = v_A − v_B."),
        ("Inertial Frame", "A reference frame not accelerating — Newton's laws hold in their simplest form."),
        ("Non-Inertial Frame", "An accelerating reference frame where fictitious forces appear."),
        ("Galilean Transformation", "Position and velocity transformations between frames moving at constant relative velocity."),
    ],

    # ── Unit 3: Forces & Newton's Laws ──────────────────────────────
    "u3_l3.1": [
        ("Force", "A push or pull on an object; a vector measured in newtons (N)."),
        ("Contact Force", "A force requiring physical contact (normal, friction, tension, applied)."),
        ("Field Force", "A force acting at a distance (gravity, electric, magnetic)."),
        ("Net Force", "The vector sum of all forces acting on an object; determines acceleration."),
        ("Free-Body Diagram", "A diagram showing all forces acting on a single object as vectors."),
    ],
    "u3_l3.2": [
        ("Newton's First Law", "An object at rest stays at rest, and an object in motion stays in motion at constant velocity, unless acted on by a net force."),
        ("Inertia", "The tendency of an object to resist changes in its motion; proportional to mass."),
        ("Equilibrium", "Net force = 0; object is at rest or moving at constant velocity."),
        ("Mass", "A measure of inertia; the quantity of matter in an object (kg)."),
        ("Balanced Forces", "Forces that are equal in magnitude and opposite in direction; produce no acceleration."),
    ],
    "u3_l3.3": [
        ("Newton's Second Law", "F_net = ma; acceleration is proportional to net force and inversely proportional to mass."),
        ("Newton (N)", "The SI unit of force: 1 N = 1 kg · m/s²."),
        ("Weight", "The gravitational force on an object: W = mg."),
        ("Mass vs Weight", "Mass is intrinsic (kg); weight depends on gravitational field (N)."),
        ("Acceleration Direction", "Always in the direction of the net force."),
    ],
    "u3_l3.4": [
        ("Newton's Third Law", "For every action force, there is an equal and opposite reaction force."),
        ("Action-Reaction Pair", "Two forces that are equal, opposite, and act on different objects."),
        ("Normal Force", "The perpendicular contact force a surface exerts on an object."),
        ("Third-Law Pairs", "Action and reaction forces never cancel because they act on different objects."),
        ("Application", "Walking: foot pushes ground backward, ground pushes foot forward."),
    ],
    "u3_l3.5": [
        ("Friction", "A force opposing the relative motion or tendency of motion between surfaces."),
        ("Static Friction", "Prevents motion; f_s ≤ μ_s N (up to a maximum value)."),
        ("Kinetic Friction", "Opposes sliding motion; f_k = μ_k N (constant)."),
        ("Coefficient of Friction (μ)", "A dimensionless ratio depending on the surfaces; μ_s > μ_k."),
        ("Tension", "The pulling force transmitted through a string, rope, or cable."),
    ],
    "u3_l3.6": [
        ("Normal Force", "Perpendicular to the surface; balances the component of weight into the surface."),
        ("Inclined Plane", "A flat surface tilted at angle θ; weight splits into parallel (mg sin θ) and perpendicular (mg cos θ) components."),
        ("Component of Weight Parallel", "mg sin θ — pulls the object down the ramp."),
        ("Component of Weight Perpendicular", "mg cos θ — pushes the object into the surface; equals normal force."),
        ("Equilibrium on a Ramp", "Object is static when friction ≥ mg sin θ."),
    ],
    "u3_l3.7": [
        ("Circular Motion", "Motion along a circular path at constant speed; direction constantly changes."),
        ("Centripetal Acceleration", "a_c = v²/r; directed toward the center of the circle."),
        ("Centripetal Force", "F_c = mv²/r; the net inward force causing circular motion."),
        ("Period (T)", "Time for one complete revolution: T = 2πr/v."),
        ("Banked Curve", "A tilted road surface that provides a component of normal force for centripetal acceleration."),
    ],
    "u3_l3.8": [
        ("Non-Inertial Frame", "An accelerating reference frame where Newton's laws require fictitious forces."),
        ("Pseudo-Force", "A fictitious force (e.g., centrifugal) that appears in a non-inertial frame to account for acceleration."),
        ("Centrifugal Force", "The outward pseudo-force in a rotating frame; equals mv²/r directed away from center."),
        ("Coriolis Force", "A pseudo-force that deflects moving objects in a rotating reference frame (e.g., Earth)."),
        ("Application", "Weather patterns, Foucault pendulum, apparent forces in elevators."),
    ],

    # ── Unit 4: Work & Energy ───────────────────────────────────────
    "u4_l4.1": [
        ("Work", "W = Fd cos θ; energy transferred by a force acting over a displacement."),
        ("Joule (J)", "The SI unit of work/energy: 1 J = 1 N·m."),
        ("Positive Work", "Force has a component in the direction of displacement (energy added)."),
        ("Negative Work", "Force opposes displacement (energy removed, e.g., friction)."),
        ("Zero Work", "Force is perpendicular to displacement (cos 90° = 0)."),
    ],
    "u4_l4.2": [
        ("Kinetic Energy", "KE = ½mv²; energy of motion."),
        ("Gravitational Potential Energy", "PE = mgh; energy due to position in a gravitational field."),
        ("Elastic Potential Energy", "PE = ½kx²; energy stored in a stretched or compressed spring."),
        ("Mechanical Energy", "The sum of kinetic and potential energy: E = KE + PE."),
        ("Reference Level", "The position where gravitational PE is defined as zero."),
    ],
    "u4_l4.3": [
        ("Conservation of Energy", "Energy cannot be created or destroyed, only transformed."),
        ("Conservation of Mechanical Energy", "KE₁ + PE₁ = KE₂ + PE₂ (when only conservative forces act)."),
        ("Energy Transformation", "Conversion between forms (PE ↔ KE, chemical → thermal, etc.)."),
        ("Dissipative Forces", "Non-conservative forces (friction) that convert mechanical energy to thermal energy."),
        ("Application", "Roller coasters, pendulums, falling objects."),
    ],
    "u4_l4.4": [
        ("Power", "P = W/t = Fv; the rate of doing work or transferring energy."),
        ("Watt (W)", "The SI unit of power: 1 W = 1 J/s."),
        ("Efficiency", "η = (useful output / total input) × 100%; always less than 100% due to losses."),
        ("Horsepower", "1 hp ≈ 746 W; a non-SI unit of power."),
        ("Application", "Comparing engines, motors, and energy use rates."),
    ],
    "u4_l4.5": [
        ("Work-Energy Theorem", "W_net = ΔKE = ½mv² − ½mv₀²; net work equals the change in kinetic energy."),
        ("Net Work", "The total work done by all forces on an object."),
        ("Application", "If net work is positive, KE increases (object speeds up); if negative, KE decreases."),
        ("Graphical Interpretation", "Work = area under the force-displacement graph."),
        ("Variable Force", "For non-constant forces, integrate F·dx or use area under F-x graph."),
    ],
    "u4_l4.6": [
        ("Conservative Force", "A force where work is path-independent (gravity, spring); energy is recoverable."),
        ("Non-Conservative Force", "A force where work depends on the path (friction, air resistance); energy is dissipated."),
        ("Potential Energy Defined", "Only conservative forces have associated potential energy functions."),
        ("Path Independence", "Work done by a conservative force between two points is the same regardless of path."),
        ("Closed Loop", "Work done by a conservative force around a closed path is zero."),
    ],

    # ── Unit 5: Momentum ────────────────────────────────────────────
    "u5_l5.1": [
        ("Linear Momentum", "p = mv; a vector quantity equal to mass × velocity."),
        ("SI Unit of Momentum", "kg·m/s."),
        ("Momentum Direction", "Same direction as velocity."),
        ("Relationship to Force", "F = dp/dt; force is the rate of change of momentum."),
        ("Large Momentum", "Requires large mass, large velocity, or both."),
    ],
    "u5_l5.2": [
        ("Impulse", "J = FΔt = Δp; the product of force and time interval, equal to the change in momentum."),
        ("Impulse-Momentum Theorem", "The impulse on an object equals the change in its momentum."),
        ("Extending Impact Time", "Longer collision time reduces the average force (airbags, crumple zones)."),
        ("Area Under F-t Graph", "Equals impulse."),
        ("Units", "Impulse has units of N·s = kg·m/s."),
    ],
    "u5_l5.3": [
        ("Conservation of Momentum", "In an isolated system, total momentum before = total momentum after."),
        ("Isolated System", "No external forces act on the system."),
        ("Before and After", "Σp_before = Σp_after."),
        ("Vector Nature", "Momentum is conserved in each direction independently."),
        ("Application", "Collisions, explosions, recoil."),
    ],
    "u5_l5.4": [
        ("Elastic Collision", "Both momentum and kinetic energy are conserved; objects bounce apart."),
        ("Inelastic Collision", "Momentum is conserved but kinetic energy is not; some KE is lost to heat/deformation."),
        ("Perfectly Inelastic", "Objects stick together after collision; maximum KE loss."),
        ("Coefficient of Restitution", "e = (separation speed) / (approach speed); e = 1 elastic, e = 0 perfectly inelastic."),
        ("1D vs 2D Collisions", "In 2D, conserve momentum separately in x and y directions."),
    ],
    "u5_l5.5": [
        ("Center of Mass", "The average position of all mass in a system: x_cm = Σmᵢxᵢ / Σmᵢ."),
        ("Motion of Center of Mass", "Moves as if all mass were concentrated there with all external forces applied."),
        ("Symmetric Objects", "Center of mass is at the geometric center for uniform, symmetric objects."),
        ("Internal Forces", "Do not affect the motion of the center of mass."),
        ("Application", "Thrown wrench rotates around its center of mass while flying through the air."),
    ],
    "u5_l5.6": [
        ("Rocket Propulsion", "Thrust comes from expelling mass (exhaust) — conservation of momentum."),
        ("Tsiolkovsky Equation", "Δv = v_e · ln(m₀/m_f); relates speed change to exhaust velocity and mass ratio."),
        ("Thrust", "F = v_e · (dm/dt); force equals exhaust velocity × mass flow rate."),
        ("Mass Ratio", "m₀/m_f; ratio of initial to final mass — larger ratio means greater Δv."),
        ("Application", "Space travel: no air to push against, so momentum of exhaust provides thrust."),
    ],

    # ── Unit 6: Gravitation ─────────────────────────────────────────
    "u6_l6.1": [
        ("Newton's Law of Gravitation", "F = Gm₁m₂/r²; the gravitational force between two masses."),
        ("Gravitational Constant", "G ≈ 6.674 × 10⁻¹¹ N·m²/kg²."),
        ("Inverse-Square Law", "Gravitational force decreases with the square of distance."),
        ("Universal", "Gravity acts between all objects with mass."),
        ("Superposition", "Gravitational forces from multiple sources add as vectors."),
    ],
    "u6_l6.2": [
        ("Gravitational Field", "g = F/m = GM/r²; the force per unit mass at a point in space."),
        ("Field Lines", "Point toward the mass; density indicates field strength."),
        ("Surface Gravity", "g = GM/R² where R is the planet's radius; ≈ 9.8 m/s² on Earth."),
        ("Field Inside a Shell", "Zero inside a uniform spherical shell (Shell Theorem)."),
        ("Variation of g", "Decreases with altitude; differs slightly across Earth's surface."),
    ],
    "u6_l6.3": [
        ("Orbital Motion", "An object in free fall around a massive body; gravity provides centripetal force."),
        ("Orbital Velocity", "v = √(GM/r); speed for a circular orbit at distance r."),
        ("Orbital Period", "T = 2πr/v = 2π√(r³/GM)."),
        ("Weightlessness", "In orbit, objects are in free fall together — no normal force, apparent weight = 0."),
        ("Geostationary Orbit", "Orbit with T = 24 hours, directly above the equator at ~35,786 km altitude."),
    ],
    "u6_l6.4": [
        ("Satellite", "An object orbiting a larger body due to gravity."),
        ("Low Earth Orbit (LEO)", "Altitude ~200–2,000 km; period ~90 minutes."),
        ("Geostationary Orbit", "Fixed position above the equator; used for communications."),
        ("Polar Orbit", "Passes over both poles; used for Earth observation."),
        ("Orbital Energy", "E_total = −GMm/(2r); negative for bound orbits."),
    ],
    "u6_l6.5": [
        ("Escape Velocity", "v_e = √(2GM/R); minimum speed to escape a gravitational field."),
        ("Independent of Mass", "Escape velocity doesn't depend on the mass of the escaping object."),
        ("Earth's Escape Velocity", "≈ 11.2 km/s from the surface."),
        ("Gravitational Potential Energy", "U = −GMm/r; zero at infinity, negative when bound."),
        ("Bound vs Unbound", "Total energy < 0: bound orbit. Total energy ≥ 0: escapes."),
    ],
    "u6_l6.6": [
        ("Kepler's First Law", "Planets orbit in ellipses with the Sun at one focus."),
        ("Kepler's Second Law", "A line from Sun to planet sweeps equal areas in equal times (faster near Sun)."),
        ("Kepler's Third Law", "T² ∝ r³; for the Sun's planets: T² = (4π²/GM)r³."),
        ("Ellipse", "An oval shape with two foci; eccentricity measures elongation."),
        ("Perihelion / Aphelion", "Closest / farthest point to the Sun in an orbit."),
    ],

    # ── Unit 7: Oscillations & Waves ────────────────────────────────
    "u7_l7.1": [
        ("Simple Harmonic Motion (SHM)", "Oscillation where the restoring force is proportional to displacement: F = −kx."),
        ("Restoring Force", "A force directed toward the equilibrium position."),
        ("Equilibrium Position", "The position where the net force is zero."),
        ("Oscillation", "Repetitive back-and-forth motion about an equilibrium."),
        ("Spring-Mass System", "A classic SHM example: mass on a spring with F = −kx."),
    ],
    "u7_l7.2": [
        ("Period (T)", "Time for one complete oscillation; measured in seconds."),
        ("Frequency (f)", "Number of oscillations per second: f = 1/T; measured in hertz (Hz)."),
        ("Amplitude (A)", "Maximum displacement from equilibrium."),
        ("Angular Frequency", "ω = 2πf = 2π/T; measured in rad/s."),
        ("Period of a Pendulum", "T = 2π√(L/g); depends on length and gravity, not mass."),
    ],
    "u7_l7.3": [
        ("Energy in SHM", "Total energy E = ½kA²; constant, alternating between KE and PE."),
        ("At Equilibrium", "KE is maximum, PE is zero, speed is maximum."),
        ("At Maximum Displacement", "PE is maximum, KE is zero, speed is zero."),
        ("Energy Conservation in SHM", "½kx² + ½mv² = ½kA² at every point."),
        ("Damped Oscillation", "SHM with friction — amplitude gradually decreases over time."),
    ],
    "u7_l7.4": [
        ("Wave", "A disturbance that transfers energy without transferring matter."),
        ("Wavelength (λ)", "The distance between consecutive identical points on a wave (e.g., crest to crest)."),
        ("Wave Speed", "v = fλ; frequency × wavelength."),
        ("Transverse Wave", "Particle displacement is perpendicular to wave direction (e.g., light, string waves)."),
        ("Longitudinal Wave", "Particle displacement is parallel to wave direction (e.g., sound)."),
    ],
    "u7_l7.5": [
        ("Superposition Principle", "When waves overlap, the resultant displacement is the sum of individual displacements."),
        ("Constructive Interference", "Waves combine in phase — amplitudes add; larger resultant."),
        ("Destructive Interference", "Waves combine out of phase — amplitudes subtract; smaller or zero resultant."),
        ("Path Difference", "The difference in distance traveled by two waves; determines constructive or destructive."),
        ("Phase", "The position in a wave cycle; in phase = same point in cycle."),
    ],
    "u7_l7.6": [
        ("Standing Wave", "A wave pattern that appears stationary, formed by superposition of two traveling waves."),
        ("Node", "A point of zero displacement in a standing wave."),
        ("Antinode", "A point of maximum displacement in a standing wave."),
        ("Resonance", "Occurs when a driving frequency matches a natural frequency — maximum amplitude."),
        ("Harmonics", "Integer multiples of the fundamental frequency: fₙ = nf₁."),
    ],
    "u7_l7.7": [
        ("Doppler Effect", "The apparent change in frequency of a wave due to relative motion between source and observer."),
        ("Approaching Source", "Frequency increases (higher pitch for sound, blueshift for light)."),
        ("Receding Source", "Frequency decreases (lower pitch, redshift)."),
        ("Doppler Formula (sound)", "f' = f × (v ± v_o) / (v ∓ v_s); signs depend on motion direction."),
        ("Application", "Radar guns, medical ultrasound, redshift of galaxies."),
    ],
    "u7_l7.8": [
        ("Wave-Particle Duality", "Light and matter exhibit both wave and particle properties."),
        ("Photon", "A quantum (packet) of light energy: E = hf."),
        ("de Broglie Wavelength", "λ = h/p = h/(mv); wavelength associated with a moving particle."),
        ("Planck's Constant", "h ≈ 6.626 × 10⁻³⁴ J·s; fundamental constant linking energy and frequency."),
        ("Double-Slit Experiment", "Demonstrates wave-like interference for light and even electrons."),
    ],

    # ── Unit 8: Sound ───────────────────────────────────────────────
    "u8_l8.1": [
        ("Sound Wave", "A longitudinal mechanical wave that travels through a medium."),
        ("Compression", "A region of high pressure in a sound wave."),
        ("Rarefaction", "A region of low pressure in a sound wave."),
        ("Medium", "Sound requires a medium (solid, liquid, or gas) — cannot travel through a vacuum."),
        ("Mechanical Wave", "A wave that requires matter to propagate."),
    ],
    "u8_l8.2": [
        ("Speed of Sound in Air", "≈ 343 m/s at 20°C; increases with temperature."),
        ("Speed Depends on Medium", "Fastest in solids, slowest in gases (denser, stiffer media → faster)."),
        ("Temperature Dependence", "v ≈ 331 + 0.6T (m/s) where T is in °C."),
        ("Mach Number", "Ratio of object's speed to speed of sound: Mach 1 = speed of sound."),
        ("Sonic Boom", "Shock wave produced when an object exceeds the speed of sound."),
    ],
    "u8_l8.3": [
        ("Intensity", "Power per unit area: I = P/A; measured in W/m²."),
        ("Loudness", "The perceived volume of sound; related to intensity (subjective)."),
        ("Decibel (dB)", "Sound level: β = 10 log(I/I₀); I₀ = 10⁻¹² W/m² (threshold of hearing)."),
        ("Inverse-Square Law", "Sound intensity decreases as 1/r² with distance from the source."),
        ("Threshold of Pain", "≈ 120 dB; the intensity at which sound becomes painful."),
    ],
    "u8_l8.4": [
        ("Pitch", "The perceived highness or lowness of a sound; determined by frequency."),
        ("Frequency Range of Hearing", "Humans hear approximately 20 Hz – 20,000 Hz."),
        ("Infrasound", "Frequencies below 20 Hz; below human hearing range."),
        ("Ultrasound", "Frequencies above 20,000 Hz; used in medical imaging."),
        ("Fundamental Frequency", "The lowest natural frequency of a vibrating object."),
    ],
    "u8_l8.5": [
        ("Resonance in Air Columns", "Standing waves form in pipes; resonant frequencies depend on pipe length."),
        ("Open Pipe", "Both ends open; all harmonics present. fₙ = nv/(2L)."),
        ("Closed Pipe", "One end closed; only odd harmonics. fₙ = nv/(4L), n = 1,3,5,..."),
        ("Node and Antinode", "Closed end = node; open end = antinode."),
        ("Application", "Musical instruments: flutes, organs, brass instruments."),
    ],
    "u8_l8.6": [
        ("Beats", "Periodic fluctuations in loudness when two close frequencies interfere."),
        ("Beat Frequency", "f_beat = |f₁ − f₂|."),
        ("Harmonics", "Integer multiples of the fundamental: 1st harmonic = fundamental, 2nd = first overtone."),
        ("Overtone", "Any resonant frequency above the fundamental."),
        ("Timbre", "The quality of sound determined by the mix of harmonics (distinguishes instruments)."),
    ],

    # ── Unit 9: Optics ──────────────────────────────────────────────
    "u9_l9.1": [
        ("Reflection", "Light bounces off a surface; angle of incidence = angle of reflection."),
        ("Refraction", "Light bends when passing between media with different optical densities."),
        ("Snell's Law", "n₁ sin θ₁ = n₂ sin θ₂; relates angles and indices of refraction."),
        ("Index of Refraction", "n = c/v; ratio of light speed in vacuum to speed in the medium."),
        ("Normal Line", "A line perpendicular to the surface at the point of incidence."),
    ],
    "u9_l9.2": [
        ("Concave Mirror", "Converges light; produces real or virtual images depending on object distance."),
        ("Convex Mirror", "Diverges light; always produces virtual, upright, reduced images."),
        ("Converging Lens", "Thicker in the middle; converges light to a focal point."),
        ("Diverging Lens", "Thinner in the middle; diverges light away from the focal axis."),
        ("Mirror/Lens Equation", "1/f = 1/d_o + 1/d_i; relates focal length, object distance, and image distance."),
    ],
    "u9_l9.3": [
        ("Total Internal Reflection", "Light reflects entirely within a medium when the angle exceeds the critical angle."),
        ("Critical Angle", "θ_c = sin⁻¹(n₂/n₁); exists only when light moves to a less dense medium."),
        ("Fiber Optics", "Uses total internal reflection to transmit light through thin glass fibers."),
        ("Diamond Brilliance", "High index of refraction → small critical angle → many internal reflections."),
        ("Application", "Telecommunications, endoscopy, decorative lighting."),
    ],
    "u9_l9.4": [
        ("Microscope", "Uses two converging lenses to magnify small objects."),
        ("Telescope", "Uses lenses or mirrors to view distant objects."),
        ("Magnification", "The ratio of image size to object size: M = −d_i/d_o."),
        ("Camera", "A converging lens forms a real image on film or a sensor."),
        ("Human Eye", "A lens system that focuses images on the retina; accommodates by changing lens shape."),
    ],
    "u9_l9.5": [
        ("Diffraction", "The bending of light around obstacles or through narrow openings."),
        ("Single-Slit Diffraction", "Central bright maximum with smaller maxima on either side."),
        ("Double-Slit Interference", "Produces alternating bright and dark fringes: dsinθ = mλ."),
        ("Diffraction Grating", "Many slits that produce sharp, bright fringes for precise wavelength measurement."),
        ("Thin-Film Interference", "Colorful patterns from constructive/destructive interference in thin layers."),
    ],
    "u9_l9.6": [
        ("Polarization", "Restricting light oscillation to one plane."),
        ("Unpolarized Light", "Light vibrating in all directions perpendicular to propagation."),
        ("Polarizer", "A filter that transmits light oscillating in one direction."),
        ("Malus's Law", "I = I₀ cos²θ; intensity after passing through a second polarizer at angle θ."),
        ("Polarization by Reflection", "At Brewster's angle, reflected light is fully polarized."),
    ],

    # ── Unit 10: Electricity & Magnetism ────────────────────────────
    "u10_l10.1": [
        ("Electric Charge", "A fundamental property of matter; positive (+) or negative (−)."),
        ("Coulomb's Law", "F = kq₁q₂/r²; force between two point charges."),
        ("Elementary Charge", "e = 1.6 × 10⁻¹⁹ C; charge of a proton (electron = −e)."),
        ("Charging Methods", "Friction, conduction, and induction."),
        ("Conservation of Charge", "Total charge in an isolated system remains constant."),
    ],
    "u10_l10.2": [
        ("Electric Field", "E = F/q = kQ/r²; force per unit positive charge."),
        ("Field Lines", "Point from positive to negative; density indicates field strength."),
        ("Electric Potential (Voltage)", "V = kQ/r; energy per unit charge. Units: volts (V = J/C)."),
        ("Potential Difference", "ΔV = W/q; work done per unit charge to move between two points."),
        ("Equipotential Lines", "Lines of constant potential; perpendicular to field lines."),
    ],
    "u10_l10.3": [
        ("Capacitance", "C = Q/V; ability to store charge. Units: farads (F)."),
        ("Parallel Plate Capacitor", "C = ε₀A/d; capacitance depends on area, distance, and dielectric."),
        ("Dielectric", "Insulating material between plates that increases capacitance."),
        ("Energy Stored", "U = ½CV² = ½QV = Q²/(2C)."),
        ("Capacitors in Series/Parallel", "Series: 1/C_total = Σ(1/Cᵢ). Parallel: C_total = ΣCᵢ."),
    ],
    "u10_l10.4": [
        ("Current", "I = Q/t; flow of charge per unit time. Units: amperes (A)."),
        ("Resistance", "R = V/I; opposition to current flow. Units: ohms (Ω)."),
        ("Ohm's Law", "V = IR; voltage equals current × resistance."),
        ("Resistivity", "ρ; a material property. R = ρL/A."),
        ("Conductors vs Insulators", "Conductors: low resistance (metals). Insulators: high resistance (rubber, glass)."),
    ],
    "u10_l10.5": [
        ("Series Circuit", "Components connected end-to-end; same current through all. R_total = ΣRᵢ."),
        ("Parallel Circuit", "Components connected across each other; same voltage. 1/R_total = Σ(1/Rᵢ)."),
        ("Kirchhoff's Current Law", "Total current into a junction = total current out (conservation of charge)."),
        ("Kirchhoff's Voltage Law", "Sum of voltage gains and drops around any closed loop = 0."),
        ("Power Dissipated", "P = IV = I²R = V²/R."),
    ],
    "u10_l10.6": [
        ("Magnetic Field (B)", "A field produced by moving charges or magnets; units: tesla (T)."),
        ("Force on Moving Charge", "F = qvB sin θ; perpendicular to both v and B."),
        ("Force on Current-Carrying Wire", "F = BIL sin θ."),
        ("Right-Hand Rule", "Fingers point in current direction, curl toward B → thumb gives force direction."),
        ("Magnetic Field of a Wire", "B = μ₀I/(2πr); circles around the wire."),
    ],
    "u10_l10.7": [
        ("Electromagnetic Induction", "A changing magnetic flux induces an EMF (voltage) in a conductor."),
        ("Faraday's Law", "EMF = −dΦ_B/dt; induced EMF equals the rate of change of magnetic flux."),
        ("Magnetic Flux", "Φ_B = BA cos θ; the product of field, area, and the cosine of the angle."),
        ("Lenz's Law", "The induced current flows in a direction to oppose the change in flux."),
        ("Application", "Generators, transformers, induction cooktops."),
    ],
    "u10_l10.8": [
        ("Alternating Current (AC)", "Current that periodically reverses direction; V = V₀ sin(ωt)."),
        ("RMS Values", "V_rms = V₀/√2, I_rms = I₀/√2; effective values for power calculations."),
        ("Transformer", "Transfers AC between circuits; V₁/V₂ = N₁/N₂ (turns ratio)."),
        ("Impedance", "The total opposition to AC; combines resistance, capacitive, and inductive reactance."),
        ("Resonant Frequency", "f₀ = 1/(2π√(LC)); where impedance is minimized in an RLC circuit."),
    ],
    "u10_l10.9": [
        ("Maxwell's Equations", "Four fundamental equations unifying electricity, magnetism, and light."),
        ("Gauss's Law (Electric)", "∮E·dA = Q_enc/ε₀; electric flux through a closed surface ∝ enclosed charge."),
        ("Gauss's Law (Magnetic)", "∮B·dA = 0; no magnetic monopoles — field lines form closed loops."),
        ("Faraday's Law (Integral)", "∮E·dl = −dΦ_B/dt; changing magnetic flux creates an electric field."),
        ("Electromagnetic Wave", "Self-propagating oscillation of electric and magnetic fields; speed = c."),
    ],

    # ── Unit 11: Modern Physics ─────────────────────────────────────
    "u11_l11.1": [
        ("Photoelectric Effect", "Electrons are emitted from a metal surface when struck by light of sufficient frequency."),
        ("Photon Energy", "E = hf; energy of a photon depends on frequency, not intensity."),
        ("Work Function (φ)", "Minimum energy needed to eject an electron from a surface."),
        ("Threshold Frequency", "Minimum frequency for photoemission: f₀ = φ/h."),
        ("Einstein's Equation", "KE_max = hf − φ; kinetic energy of emitted electrons."),
    ],
    "u11_l11.2": [
        ("Thomson Model", "'Plum pudding' — positive charge with electrons embedded."),
        ("Rutherford Model", "Dense positive nucleus with electrons orbiting (discovered via gold foil experiment)."),
        ("Bohr Model", "Electrons orbit in quantized energy levels; emit photons when jumping down."),
        ("Energy Levels", "Eₙ = −13.6/n² eV for hydrogen; quantized, discrete values."),
        ("Emission Spectrum", "Discrete wavelengths emitted by excited atoms — unique to each element."),
    ],
    "u11_l11.3": [
        ("Radioactive Decay", "Unstable nuclei emit radiation (alpha, beta, or gamma) to become more stable."),
        ("Half-Life", "Time for half the atoms in a sample to decay: N = N₀(½)^(t/t₁/₂)."),
        ("Nuclear Fission", "A heavy nucleus splits into lighter nuclei, releasing energy (e.g., uranium-235)."),
        ("Nuclear Fusion", "Light nuclei combine to form a heavier nucleus, releasing energy (e.g., hydrogen → helium)."),
        ("Mass-Energy Equivalence", "E = mc²; mass can be converted to energy."),
    ],
    "u11_l11.4": [
        ("Special Relativity", "Einstein's theory: laws of physics are the same in all inertial frames; c is constant."),
        ("Time Dilation", "Moving clocks run slower: Δt = γΔt₀ where γ = 1/√(1 − v²/c²)."),
        ("Length Contraction", "Moving objects are shorter in the direction of motion: L = L₀/γ."),
        ("Lorentz Factor (γ)", "γ = 1/√(1 − v²/c²); approaches infinity as v → c."),
        ("Twin Paradox", "A traveling twin ages less than the stationary twin due to time dilation."),
    ],
    "u11_l11.5": [
        ("Wave Function (ψ)", "A mathematical function describing the quantum state of a particle."),
        ("Heisenberg Uncertainty Principle", "Δx · Δp ≥ ℏ/2; position and momentum cannot both be precisely known."),
        ("Probability Density", "|ψ|² gives the probability of finding a particle at a particular location."),
        ("Quantization", "Energy, angular momentum, and other quantities come in discrete packets."),
        ("Schrödinger Equation", "The fundamental equation governing quantum mechanics; predicts wave functions."),
    ],
    "u11_l11.6": [
        ("Standard Model", "The theory classifying all known fundamental particles and three of four forces."),
        ("Quarks", "Fundamental particles that make up protons and neutrons (6 flavors: up, down, charm, strange, top, bottom)."),
        ("Leptons", "Fundamental particles including electrons, muons, taus, and their neutrinos."),
        ("Bosons", "Force-carrying particles: photon (EM), gluon (strong), W/Z (weak), Higgs."),
        ("Antimatter", "Particles with the same mass but opposite charge; annihilate with matter releasing energy."),
    ],
}

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for key, cards in FC.items():
    if key in data:
        data[key]["flashcards"] = [{"term": t, "definition": d} for t, d in cards]
        count += 1

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added flashcards to {count} Physics lessons")
