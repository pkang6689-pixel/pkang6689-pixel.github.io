#!/usr/bin/env python3
"""Expand Physics U4-U6 quizzes from 7 to 20 questions each (18 lessons)."""
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

# ── U4: Work, Energy & Power ──

k, q = add_qs("u4_l4.1", [
    ("Work is done when a force causes a:", ["Vibration only", "Sound", "*Displacement in the direction of the force", "Rotation only"], "W = Fd cos θ."),
    ("The SI unit of work is the:", ["Watt", "*Joule", "Newton", "Pascal"], "1 J = 1 N·m."),
    ("W = Fd cos θ. If F = 10 N, d = 5 m, θ = 0°:", ["0 J", "25 J", "*50 J", "100 J"], "10 × 5 × 1 = 50 J."),
    ("If the force is perpendicular to displacement (θ = 90°), work =", ["Fd", "½Fd", "*0", "Fd²"], "cos 90° = 0."),
    ("Gravity does _____ work on an object moving horizontally.", ["Positive", "Negative", "*Zero (perpendicular)", "Maximum"], "Perpendicular force."),
    ("A 20 N force at 60° to the horizontal moves an object 3 m. W =", ["60 J", "*30 J (20 × 3 × cos 60° = 30)", "20 J", "10 J"], "cos 60° = 0.5."),
    ("Negative work means the force component is _____ to displacement.", ["Parallel", "*Opposite (antiparallel)", "Perpendicular", "At 45°"], "Force opposes motion."),
    ("Friction does _____ work on a sliding object.", ["Positive", "Zero", "*Negative", "Variable positive"], "Opposes displacement direction."),
    ("Work done by gravity on a falling object is:", ["Negative", "Zero", "*Positive (force and displacement same direction)", "Undefined"], "Same direction = positive."),
    ("Work is a _____ quantity.", ["Vector", "*Scalar", "Tensor", "Neither"], "No direction."),
    ("The work-energy theorem states that net work equals the change in:", ["Potential energy", "*Kinetic energy", "Momentum", "Force"], "W_net = ΔKE."),
    ("On a force-displacement graph, work equals the:", ["Slope", "*Area under the curve", "Intercept", "Maximum"], "Area under F-d graph."),
    ("If the force varies, work is found by:", ["Simple multiplication", "*Integration (or area under the F-d curve)", "Division", "Taking the slope"], "Integral of F·dx."),
])
all_new[k] = q

k, q = add_qs("u4_l4.2", [
    ("Kinetic energy (KE) = ½mv². A 2 kg object at 3 m/s:", ["3 J", "6 J", "*9 J", "18 J"], "½(2)(9) = 9 J."),
    ("If velocity doubles, KE:", ["Doubles", "*Quadruples", "Halves", "Stays the same"], "KE ∝ v²."),
    ("Gravitational potential energy PE = mgh. A 5 kg object at 4 m:", ["20 J", "49 J", "*196 J (5 × 9.8 × 4)", "9.8 J"], "5 × 9.8 × 4 = 196 J."),
    ("PE depends on the _____ above a reference point.", ["Speed", "*Height", "Mass only", "Time"], "Height-dependent."),
    ("KE is always:", ["Negative", "Zero", "*Non-negative (≥ 0)", "Equal to PE"], "½mv² ≥ 0 always."),
    ("Elastic PE in a spring: PEₛ = ½kx². If k = 200 N/m and x = 0.1 m:", ["10 J", "20 J", "*1 J", "100 J"], "½(200)(0.01) = 1 J."),
    ("KE = 0 when the object is:", ["Moving fast", "Accelerating", "*At rest (v = 0)", "At height h"], "Zero velocity."),
    ("Doubling the height doubles the:", ["KE", "*PE", "Speed", "Mass"], "PE ∝ h."),
    ("A roller coaster at the top of a hill has maximum _____ energy.", ["Kinetic", "*Potential", "Elastic", "Thermal"], "Maximum height = max PE."),
    ("At the bottom, it has maximum _____ energy.", ["Potential", "*Kinetic", "Elastic", "No"], "Maximum speed = max KE."),
    ("PE is energy of _____, KE is energy of _____.", ["Motion, position", "*Position, motion", "Heat, light", "Sound, force"], "Position vs motion."),
    ("Total mechanical energy = KE + PE. This is useful for:", ["Static problems only", "*Conservation of energy problems", "Thermodynamics only", "Optics"], "Energy conservation."),
    ("A 10 kg ball at 10 m height (at rest) has total energy:", ["100 J", "490 J", "*980 J (mgh = 10×9.8×10)", "0 J"], "All PE = 980 J."),
])
all_new[k] = q

k, q = add_qs("u4_l4.3", [
    ("The law of conservation of energy states energy cannot be _____ or _____.", ["Moved, transferred", "*Created, destroyed", "Measured, calculated", "Stored, used"], "Only transformed."),
    ("In a closed system with no non-conservative forces, KE + PE =", ["Zero", "*Constant", "Increasing", "Decreasing"], "Total ME conserved."),
    ("A ball dropped from 20 m (no air resistance): speed at ground: v = √(2gh) =", ["14 m/s", "*≈ 19.8 m/s", "20 m/s", "9.8 m/s"], "√(2×9.8×20) = √392 ≈ 19.8."),
    ("At half the height (10 m), KE = PE because:", ["They're always equal", "*Half the PE converted to KE (½mgh each)", "Conservation fails", "Speed is maximum"], "Equal split at halfway."),
    ("A pendulum converts PE to KE and back, demonstrating:", ["Newton's Third Law", "*Conservation of energy", "Friction", "Momentum"], "Energy transformation."),
    ("If friction is present, mechanical energy:", ["Increases", "Stays constant", "*Decreases (converted to thermal energy)", "Becomes negative"], "Thermal energy generated."),
    ("Energy is measured in:", ["Newtons", "kg", "*Joules", "Watts"], "SI unit of energy."),
    ("A spring compressed and released converts _____ PE to KE.", ["Gravitational", "*Elastic", "Chemical", "Nuclear"], "Spring PE → KE."),
    ("A 2 kg ball at height 5 m has PE = 98 J. If it falls to 2 m, KE =", ["98 J", "*58.8 J (PE lost = mg×3 = 58.8 J)", "39.2 J", "0 J"], "PE lost = KE gained."),
    ("In a roller coaster (no friction), speed at any point depends only on:", ["Time", "Distance traveled", "*Height change from starting point", "Shape of track"], "Height determines speed."),
    ("Conservation of energy applies to _____ energy forms, not just mechanical.", ["Only kinetic", "Only potential", "*All (including thermal, chemical, nuclear, etc.)", "None"], "Universal law."),
    ("If a ball is thrown upward at 15 m/s, max height = v²/(2g) =", ["7.5 m", "22.5 m", "*11.5 m (225/19.6)", "15 m"], "225/19.6 ≈ 11.5 m."),
    ("Energy transformations in a hydroelectric dam: gravitational PE → KE → _____.", ["Thermal", "Chemical", "*Electrical", "Nuclear"], "Water PE → turbine KE → electricity."),
])
all_new[k] = q

k, q = add_qs("u4_l4.4", [
    ("Power is the rate of doing:", ["Force", "Acceleration", "*Work (or energy transfer per unit time)", "Displacement"], "P = W/t."),
    ("SI unit of power:", ["Joule", "Newton", "*Watt (W)", "Volt"], "1 W = 1 J/s."),
    ("P = W/t. If 500 J of work in 10 s:", ["5000 W", "*50 W", "0.02 W", "510 W"], "500/10 = 50 W."),
    ("1 horsepower ≈ _____ watts.", ["500", "600", "*746", "1000"], "746 W."),
    ("P = Fv (force × velocity). If F = 100 N and v = 5 m/s:", ["20 W", "105 W", "*500 W", "2000 W"], "100 × 5 = 500 W."),
    ("Efficiency = useful output / total input × 100%. If input = 200 J and output = 150 J:", ["50%", "*75%", "133%", "25%"], "150/200 = 0.75."),
    ("No machine can be more than _____ efficient.", ["50%", "75%", "*100% (and real machines are always less)", "200%"], "100% max (2nd law prevents it for heat engines)."),
    ("A 60 W lightbulb uses 60 J of energy every:", ["60 s", "0.1 s", "*1 s", "One hour"], "60 W = 60 J/s."),
    ("kWh is a unit of:", ["Power", "*Energy", "Force", "Time"], "Kilowatt-hour = energy."),
    ("1 kWh = 3.6 × 10⁶ J because:", ["1000 kW × 1 h", "*1000 W × 3600 s = 3,600,000 J", "It's defined that way only", "1000 J × 3600 s"], "Power × time."),
    ("A machine lifts 50 kg by 4 m in 2 s. Power = mgh/t =", ["100 W", "490 W", "*980 W (50×9.8×4/2)", "1960 W"], "1960/2 = 980 W."),
    ("A more powerful engine can do the same work in _____ time.", ["More", "The same", "*Less", "Infinite"], "Higher power = faster work."),
    ("The efficiency of a real engine is limited by:", ["Newton's laws", "*Friction, heat loss, and thermodynamic limits", "Conservation of energy", "Nothing"], "Energy losses."),
])
all_new[k] = q

k, q = add_qs("u4_l4.5", [
    ("The work-energy theorem: W_net = ΔKE = _____ - _____.", ["KE_i − KE_f", "*KE_f − KE_i (½mv² − ½mu²)", "PE_f − PE_i", "F × d always"], "Change in KE."),
    ("If net work on an object is positive, its speed:", ["Decreases", "*Increases", "Stays the same", "Becomes zero"], "Positive work = gain KE."),
    ("If net work is negative, kinetic energy:", ["Increases", "*Decreases", "Is unchanged", "Doubles"], "Loses KE."),
    ("If net work = 0, the object's speed:", ["Increases", "Decreases", "*Stays the same", "Becomes infinite"], "No change in KE."),
    ("A 3 kg object accelerates from 2 m/s to 6 m/s. ΔKE =", ["24 J", "*48 J (½(3)(36) − ½(3)(4) = 54 − 6)", "6 J", "54 J"], "54 − 6 = 48 J."),
    ("The net work done on that object is:", ["54 J", "6 J", "*48 J", "60 J"], "W_net = ΔKE = 48 J."),
    ("A car (1500 kg) brakes from 20 m/s to rest. Work by brakes:", ["300,000 J", "150,000 J", "*−300,000 J (negative because KE decreases)", "0 J"], "½(1500)(400) = 300,000 J lost."),
    ("The braking distance is directly proportional to:", ["Speed", "*Speed squared (since KE ∝ v²)", "Mass only", "Time"], "Doubling speed => 4× distance."),
    ("The work-energy theorem is derived from:", ["Conservation of momentum", "*Newton's Second Law (F=ma integrated over distance)", "Kepler's laws", "Coulomb's law"], "F=ma → W=ΔKE."),
    ("If only gravity does work: W_gravity = mgh = ΔKE. This is equivalent to:", ["Momentum conservation", "*Conservation of mechanical energy", "Newton's Third Law", "Bernoulli's principle"], "Same concept."),
    ("For a variable force, W = ∫F·dx. The work-energy theorem still gives W_net = _____.", ["ΔPE", "*ΔKE", "F × d", "½Fd"], "Still ΔKE."),
    ("A 50 N force pushes a 10 kg box 4 m on a frictionless surface (from rest). Final speed:", ["10 m/s", "*√(40) ≈ 6.32 m/s", "20 m/s", "4 m/s"], "W=200=½(10)v², v²=40."),
    ("Work done by a spring (from x₁ to x₂): W = ½kx₁² − ½kx₂². This is because the spring force:", ["Is constant", "*Varies linearly with displacement", "Is zero", "Acts at 90°"], "Hooke's law: F = -kx."),
])
all_new[k] = q

k, q = add_qs("u4_l4.6", [
    ("A conservative force has work that depends only on:", ["Speed", "Time", "*Initial and final positions (path-independent)", "Acceleration"], "Path-independent."),
    ("Gravity is a _____ force.", ["Non-conservative", "*Conservative", "Fictitious", "Dissipative"], "Work depends only on Δh."),
    ("Friction is a _____ force.", ["Conservative", "*Non-conservative (path-dependent)", "Fictitious", "Central"], "Longer path = more work by friction."),
    ("For a conservative force, work in a closed loop is:", ["Maximum", "Positive", "*Zero", "Negative"], "Returns to start = zero net work."),
    ("Potential energy can be defined only for _____ forces.", ["Non-conservative", "*Conservative", "All", "Frictional"], "PE = −W by conservative force."),
    ("Examples of conservative forces: gravity, spring force, and:", ["Friction", "Air drag", "*Electrostatic force", "Viscous drag"], "Electrostatic is conservative."),
    ("Examples of non-conservative forces: friction, air resistance, and:", ["Gravity", "Spring force", "*Applied forces (like pushing)", "Electrostatic force"], "Push/pull forces (external)."),
    ("When non-conservative forces do work, mechanical energy:", ["Is conserved", "*Changes (some converts to thermal or other forms)", "Increases always", "Becomes infinite"], "ME not conserved."),
    ("W_non-conservative = ΔKE + ΔPE = _____.", ["0", "ΔKE", "*ΔME (change in total mechanical energy)", "ΔPE"], "Non-conservative changes total ME."),
    ("A block slides down a rough incline. Friction converts mechanical energy to:", ["Electrical", "Nuclear", "*Thermal (heat) energy", "Chemical energy"], "Friction → heat."),
    ("If friction does −20 J and gravity does +50 J on a falling block, ΔKE =", ["70 J", "20 J", "*30 J", "50 J"], "W_net = 50 − 20 = 30 J."),
    ("In a real system, energy is 'lost' (actually converted) through:", ["Creation", "Destruction", "*Dissipation (friction, drag, sound, heat)", "Conservation"], "Dissipative processes."),
    ("The total energy (including thermal) is always conserved, consistent with the:", ["Second Law only", "Third Law only", "*First Law of Thermodynamics (conservation of energy)", "Zero-th Law"], "Energy conservation universal."),
])
all_new[k] = q

# ── U5: Momentum ──

k, q = add_qs("u5_l5.1", [
    ("Linear momentum p = mv. SI unit:", ["N", "J", "*kg·m/s", "W"], "Mass times velocity."),
    ("A 3 kg object at 4 m/s has momentum:", ["7 kg·m/s", "*12 kg·m/s", "0.75 kg·m/s", "1.33 kg·m/s"], "3 × 4 = 12."),
    ("Momentum is a _____ quantity.", ["Scalar", "*Vector", "Dimensionless", "Unit"], "Has direction."),
    ("If velocity doubles, momentum:", ["Halves", "Quadruples", "*Doubles", "Stays the same"], "p ∝ v."),
    ("Newton's Second Law in terms of momentum: F = dp/dt. This is the _____ form.", ["Simple", "*General (more general than F=ma)", "Incorrect", "Approximate"], "General form allows variable mass."),
    ("An object at rest has momentum:", ["Infinite", "Undefined", "*Zero", "Equal to its mass"], "v=0, so p=0."),
    ("A heavy truck and a light car at the same speed: the truck has _____ momentum.", ["Less", "*More (greater mass)", "The same", "Zero"], "Greater m = greater p."),
    ("Two objects moving in opposite directions with equal |p| have total momentum:", ["2p", "*Zero (they cancel)", "p", "Undefined"], "Equal and opposite = zero net."),
    ("Momentum has dimensions:", ["[MLT⁻²]", "ML²T⁻²]", "*[MLT⁻¹]", "[MLT⁻¹]"], "kg·m/s = [MLT⁻¹]."),
    ("A lighter object can have more momentum than a heavier one if:", ["It's at rest", "*Its speed is sufficiently greater", "It has more mass", "It accelerates"], "Higher v compensates lower m."),
    ("A 0.5 kg ball at 20 m/s has the same |p| as a 10 kg object at:", ["20 m/s", "0.5 m/s", "*1 m/s", "10 m/s"], "0.5×20 = 10, so 10×v=10, v=1."),
    ("The principle of conservation of momentum follows from Newton's _____ Law.", ["First", "Second", "*Third (action-reaction forces for internal forces)", "Zeroth"], "Third law → internal forces cancel."),
    ("For a system with no external forces, total momentum is:", ["Zero always", "*Constant (conserved)", "Increasing", "Undefined"], "Conservation of momentum."),
])
all_new[k] = q

k, q = add_qs("u5_l5.2", [
    ("Impulse J = FΔt. SI unit:", ["N", "*N·s (or kg·m/s)", "J", "W"], "Force times time."),
    ("Impulse equals the change in:", ["Energy", "Position", "*Momentum (J = Δp)", "Acceleration"], "Impulse-momentum theorem."),
    ("A 10 N force for 3 s gives impulse:", ["3.33 N·s", "13 N·s", "*30 N·s", "0.3 N·s"], "10 × 3 = 30."),
    ("A large force over a short time can give the same impulse as:", ["No force", "*A small force over a long time", "Only a large force works", "Impulse is always the same"], "FΔt = constant."),
    ("A car airbag works by _____ the time of impact, reducing the force.", ["Decreasing", "*Increasing", "Maintaining", "Eliminating"], "Longer time = less force."),
    ("Catching a ball: following through increases contact time, _____ force.", ["Increasing", "*Decreasing", "Maintaining", "Doubling"], "Same impulse, more time, less force."),
    ("The area under a force-time graph equals:", ["Momentum", "Energy", "*Impulse", "Acceleration"], "Area = ∫F dt = J."),
    ("A 2 kg ball going 5 m/s is stopped. Impulse needed:", ["5 N·s", "*10 N·s", "2.5 N·s", "7 N·s"], "Δp = 2 × 5 = 10 kg·m/s."),
    ("If the ball bounces back at 5 m/s, impulse =", ["10 N·s", "*20 N·s (change = 5 − (−5) = 10, ×2 kg = 20)", "0 N·s", "5 N·s"], "Δp = 2(5−(−5)) = 20."),
    ("A baseball bat hits a ball with 1000 N for 0.01 s. Impulse:", ["100 N·s", "*10 N·s", "1 N·s", "10,000 N·s"], "1000 × 0.01 = 10 N·s."),
    ("Impulse is a _____ quantity.", ["Scalar", "*Vector (same direction as force)", "Dimensionless", "Constant"], "Same direction as average force."),
    ("Crumple zones in cars increase impact:", ["Force", "Speed", "*Time (reducing force)", "Mass"], "Longer deformation time."),
    ("If F varies, impulse = ∫F dt. For constant force, this simplifies to:", ["F/t", "*F × Δt", "Fd", "½Ft²"], "Simple product."),
])
all_new[k] = q

k, q = add_qs("u5_l5.3", [
    ("Conservation of momentum: in a closed system with no external forces, total momentum before = total momentum:", ["Lost", "*After", "Zero", "Doubled"], "p_before = p_after."),
    ("Two ice skaters push apart. If one moves right at 2 m/s (60 kg), the other (40 kg) moves:", ["Right at 2 m/s", "*Left at 3 m/s (60×2 = 40×v, v=3)", "Left at 2 m/s", "Doesn't move"], "60×2 = 40×v."),
    ("A 10 kg cart at 5 m/s collides and sticks to a 10 kg cart at rest. Final speed:", ["5 m/s", "10 m/s", "*2.5 m/s", "0 m/s"], "10(5) = 20v, v = 2.5."),
    ("Momentum is conserved in _____ collisions.", ["Only elastic", "Only inelastic", "*All types (as long as external forces are negligible)", "None"], "Universal law."),
    ("A bullet (0.01 kg at 400 m/s) embeds in a block (2 kg at rest). Speed after:", ["400 m/s", "200 m/s", "*≈ 1.99 m/s (0.01×400 = 2.01×v)", "4 m/s"], "4 = 2.01v, v ≈ 1.99."),
    ("In an explosion (one object splits into two), total momentum:", ["Increases", "Decreases", "*Stays the same (usually zero if initially at rest)", "Is undefined"], "Conserved."),
    ("A recoiling gun: gun momentum = _____ bullet momentum.", ["More than", "Less than", "*Equal and opposite to", "Unrelated to"], "Σp = 0."),
    ("Momentum conservation applies when net external force =", ["Maximum", "*Zero (or negligible)", "mg", "ma"], "No external force."),
    ("Two billiard balls collide: total momentum is conserved because:", ["Friction is zero", "*Internal forces cancel (Newton's Third Law)", "Balls are round", "Table is flat"], "Third law."),
    ("If external forces act but are small compared to collision forces:", ["Momentum is not conserved", "*Momentum is approximately conserved", "Energy is conserved", "Nothing is conserved"], "Approximately conserved."),
    ("In 2D collisions, momentum is conserved in _____ direction(s).", ["One", "*Both x and y (independently)", "Neither", "Only x"], "Component-wise conservation."),
    ("A 5 kg object at 6 m/s and a 3 kg object at -4 m/s collide and stick. Final velocity:", ["2 m/s", "1 m/s", "*2.25 m/s ((30-12)/8)", "10 m/s"], "(30-12)/8 = 2.25."),
    ("The 'system' in momentum conservation must include all objects that:", ["Are heavy", "*Interact with each other during the event", "Are moving", "Are at rest"], "All interacting objects."),
])
all_new[k] = q

k, q = add_qs("u5_l5.4", [
    ("In an elastic collision, both momentum and _____ are conserved.", ["Force", "Acceleration", "*Kinetic energy", "Potential energy"], "KE conserved in elastic."),
    ("In a perfectly inelastic collision, objects _____ and move together.", ["Bounce apart", "*Stick together", "Explode", "Stop"], "Maximum KE loss."),
    ("In any inelastic collision, some KE is converted to:", ["More KE", "Potential energy always", "*Thermal energy, sound, deformation, etc.", "Momentum"], "KE lost to other forms."),
    ("An elastic collision between equal masses where one is at rest: the moving one:", ["Continues", "*Stops, and the other moves with the initial speed", "Moves backward", "Both stop"], "Complete transfer."),
    ("Two equal masses in elastic head-on collision with equal speeds: they:", ["Stop", "*Exchange velocities (bounce back)", "Stick together", "Move in the same direction"], "Exchange velocities."),
    ("In a perfectly inelastic collision, KE lost is _____ for collisions.", ["Zero", "Small", "*Maximum (of any collision type)", "Infinite"], "Maximum loss."),
    ("In an elastic collision, relative speed of approach = relative speed of:", ["Stopping", "Approach again", "*Separation", "Zero"], "Coefficient of restitution = 1."),
    ("The coefficient of restitution e = 1 for:", ["Perfectly inelastic", "*Perfectly elastic", "All collisions", "Inelastic"], "e = 1 elastic."),
    ("e = 0 for:", ["Perfectly elastic", "*Perfectly inelastic", "All collisions", "Superelastic"], "e = 0 stick together."),
    ("A 2 kg ball at 6 m/s hits a 2 kg ball at rest (elastic). After: ball 1 speed =", ["6 m/s", "3 m/s", "*0 m/s (stops)", "−6 m/s"], "Equal masses elastic: complete transfer."),
    ("Ball 2 speed after:", ["0 m/s", "3 m/s", "*6 m/s", "12 m/s"], "Takes all the speed."),
    ("In real collisions, most are:", ["Perfectly elastic", "Perfectly inelastic", "*Somewhere in between (partially inelastic)", "None of these"], "Partial KE loss."),
    ("In a superelastic collision (e.g., explosion), KE _____ .", ["Decreases", "Is conserved", "*Increases (energy released from internal source)", "Is zero"], "Internal energy converts to KE."),
])
all_new[k] = q

k, q = add_qs("u5_l5.5", [
    ("The center of mass (CM) is the _____ position of a system.", ["Highest", "Lowest", "*Average weighted (mass-weighted average)", "Random"], "Mass-weighted average position."),
    ("For two masses m₁ at x₁ and m₂ at x₂: x_cm =", ["(x₁ + x₂)/2", "*(m₁x₁ + m₂x₂)/(m₁ + m₂)", "m₁x₁ − m₂x₂", "(m₁ + m₂)/(x₁ + x₂)"], "Weighted average."),
    ("If m₁ = 3 kg at x = 0 and m₂ = 1 kg at x = 4: x_cm =", ["2 m", "*1 m ((0+4)/(3+1)=1)", "3 m", "4 m"], "(3×0+1×4)/4 = 1."),
    ("The CM is closer to the _____ mass.", ["Lighter", "*Heavier", "Faster", "Higher"], "Weighted toward heavier."),
    ("For a uniform (symmetric) object, the CM is at the:", ["Edge", "Top", "*Geometric center", "Corner"], "Geometric center."),
    ("The velocity of the CM: v_cm = (m₁v₁ + m₂v₂)/(m₁ + m₂) = _____.", ["v₁ + v₂", "*(total momentum)/(total mass)", "v₁ - v₂", "0 always"], "p_total / M_total."),
    ("If no external forces act, the CM moves at:", ["Varying velocity", "*Constant velocity", "Rest always", "g"], "Constant by Newton's 1st."),
    ("In an explosion, the CM:", ["Moves away", "Stops", "*Continues at the same velocity as before", "Accelerates"], "No external force changes CM."),
    ("A thrown wrench rotates in the air, but its CM follows a:", ["Spiral", "*Parabolic path", "Circular path", "Random path"], "CM follows projectile path."),
    ("For a distributed mass, the CM is found by:", ["Guessing", "Finding the edge", "*Integration: x_cm = (1/M)∫x dm", "Averaging endpoints"], "Integral for continuous mass."),
    ("The total momentum of a system = M × v_cm, where M is:", ["One mass", "*Total mass of the system", "Average mass", "Reduced mass"], "P = Mv_cm."),
    ("If the CM is at rest, the total momentum is:", ["Maximum", "Undefined", "*Zero", "Equal to the largest mass"], "P = M × 0 = 0."),
    ("The CM frame is the reference frame in which total momentum =", ["Maximum", "*Zero", "M × g", "Infinite"], "Zero-momentum frame."),
])
all_new[k] = q

k, q = add_qs("u5_l5.6", [
    ("Rocket propulsion works by expelling mass (exhaust) in one direction, gaining momentum in the:", ["Same direction", "*Opposite direction", "Perpendicular direction", "No direction"], "Newton's Third Law."),
    ("The thrust of a rocket = exhaust speed × rate of mass ejection: F = v_e × (dm/dt). This is derived from:", ["Energy conservation", "*Momentum conservation (generalized Newton's 2nd law)", "Bernoulli's principle", "Kepler's Laws"], "Momentum changes."),
    ("A rocket in space (no gravity, no air resistance) accelerates because:", ["It pushes against air", "*It expels mass backward (internal action-reaction)", "Gravity pulls it", "Fuel pushes it"], "No external medium needed."),
    ("The Tsiolkovsky rocket equation relates final velocity to:", ["Thrust only", "*Exhaust velocity and mass ratio (v = v_e × ln(m₀/m_f))", "Fuel type only", "Rocket shape"], "v = v_e ln(m₀/m_f)."),
    ("If exhaust velocity = 3000 m/s and mass ratio m₀/m_f = e (≈2.718), Δv =", ["3000 m/s", "*3000 m/s (v_e × ln(e) = v_e × 1)", "6000 m/s", "1500 m/s"], "ln(e) = 1."),
    ("Higher exhaust velocity means _____ fuel efficiency.", ["Lower", "*Greater", "The same", "Zero"], "Better Δv per unit mass."),
    ("Multi-stage rockets are more efficient because:", ["They're larger", "*They discard empty stages (reducing dead mass)", "They use more fuel", "They burn longer"], "Shed mass of empty tanks."),
    ("In deep space, a rocket continues at its achieved speed when engines stop because:", ["Friction decelerates it", "It runs out of fuel", "*No force acts to slow it down (Newton's 1st Law)", "Gravity stops it"], "No friction in space."),
    ("The momentum of the rocket + exhaust system is:", ["Increasing", "Decreasing", "*Constant (if no external forces)", "Zero always"], "Conservation of momentum."),
    ("If a 100 kg astronaut throws a 2 kg tool at 10 m/s, the astronaut recoils at:", ["10 m/s", "2 m/s", "*0.2 m/s (2×10 = 100×v)", "5 m/s"], "0.2 m/s."),
    ("Ion thrusters have very high exhaust velocity but low:", ["Efficiency", "Duration", "*Thrust (low mass flow rate)", "Exhaust speed"], "Low mass ejection rate."),
    ("Chemical rockets have high thrust but relatively lower:", ["Force", "*Exhaust velocity (compared to ion engines)", "Mass flow rate", "Size"], "Lower v_e."),
    ("Jet engines differ from rockets because jets take in _____ from the environment.", ["Fuel", "*Air (oxygen for combustion)", "Water", "Nothing"], "Air-breathing engines."),
])
all_new[k] = q

# ── U6: Gravitation ──

k, q = add_qs("u6_l6.1", [
    ("Newton's Law of Gravitation: F = Gm₁m₂/r². G is the:", ["Gravitational acceleration", "*Universal gravitational constant", "Gravitational field", "Weight"], "Universal constant."),
    ("G ≈ 6.674 × 10⁻¹¹ N·m²/kg². It is very:", ["Large", "*Small (gravity is weak compared to other forces)", "Variable", "Zero"], "Weak force constant."),
    ("Gravitational force is always:", ["Repulsive", "*Attractive", "Zero", "Perpendicular"], "Gravity only attracts."),
    ("If the distance between two masses doubles, gravitational force:", ["Doubles", "Halves", "*Becomes ¼ (inverse square)", "Becomes ⅛"], "F ∝ 1/r²."),
    ("If both masses double, force:", ["Doubles", "*Quadruples", "Halves", "Stays the same"], "F ∝ m₁m₂."),
    ("The gravitational force between Earth and a 1 kg mass at Earth's surface:", ["6.674 × 10⁻¹¹ N", "*≈ 9.8 N (its weight)", "1 N", "0 N"], "F = mg ≈ 9.8 N."),
    ("Gravitational force acts along the _____ connecting the two masses.", ["Perpendicular", "*Line (radial line)", "Tangent", "Diagonal"], "Radial direction."),
    ("Newton's law of gravitation is an _____ law.", ["Approximate", "*Inverse square", "Linear", "Exponential"], "F ∝ 1/r²."),
    ("The law applies to _____ masses.", ["Only large", "Only small", "*All (every pair of masses in the universe)", "Only spherical"], "Universal."),
    ("Weight is the gravitational force exerted by Earth on an object: W =", ["mv", "½mv²", "*mg", "Gm/r"], "W = mg."),
    ("The gravitational attraction between two 1 kg masses 1 m apart is:", ["9.8 N", "1 N", "*6.674 × 10⁻¹¹ N (extremely small)", "0 N"], "Tiny for small masses."),
    ("Newton's law explained both the fall of an apple and the orbit of the:", ["Stars", "*Moon", "Sun", "Galaxy"], "Same force governs both."),
    ("Einstein's General Relativity provides a more accurate theory of gravity as curvature of:", ["Light", "Energy", "*Spacetime", "Mass"], "Spacetime curvature."),
])
all_new[k] = q

k, q = add_qs("u6_l6.2", [
    ("Gravitational field strength g = F/m = _____.", ["Gm₁m₂/r²", "*GM/r² (at distance r from mass M)", "mv²/r", "½mv²"], "Field strength formula."),
    ("g at Earth's surface ≈ 9.8 m/s² ≈ 9.8 N/kg. Both units are:", ["Different", "*Equivalent", "Incompatible", "Only m/s² is correct"], "m/s² = N/kg."),
    ("Gravitational field strength decreases with:", ["Mass", "*Increasing distance from the center (of the mass)", "Temperature", "Time"], "g ∝ 1/r² outside the mass."),
    ("Inside a uniform spherical shell, g =", ["Maximum", "g_surface", "*0 (shell theorem)", "Variable"], "No net force inside shell."),
    ("At twice Earth's radius from the center, g =", ["9.8 m/s²", "4.9 m/s²", "*2.45 m/s² (g/4)", "19.6 m/s²"], "g ∝ 1/r², so 9.8/4 ≈ 2.45."),
    ("Field lines point:", ["Away from mass", "*Toward the mass (direction of force on test mass)", "Perpendicular", "In circles"], "Toward attracting mass."),
    ("A stronger field is represented by _____ field lines.", ["Fewer", "*More closely spaced", "Wider apart", "Colored"], "Density indicates strength."),
    ("Two nearby masses: field between them may have a point where g =", ["Maximum", "*Zero (where fields cancel)", "Infinite", "Constant"], "Neutral point."),
    ("On a planet with mass 2M_E and radius 2R_E, surface g =", ["g_E", "*g_E/2 (2M/(2R)² = 2M/4R² = g/2)", "2g_E", "4g_E"], "GM/R² → 2GM_E/(4R_E²) = g_E/2."),
    ("g varies slightly on Earth's surface because Earth is:", ["A perfect sphere", "*An oblate spheroid (flattened at poles) and rotates", "Hollow", "Changing mass"], "Shape and rotation."),
    ("g is slightly larger at the _____ than at the equator.", ["Equator", "*Poles", "Summit", "Sea level only"], "Closer to center + less rotation effect."),
    ("Gravitational potential energy (near Earth): PE = -GMm/r. This is always:", ["Positive", "*Negative (with zero at infinity)", "Zero", "Undefined"], "Negative with PE=0 at ∞."),
    ("The gravitational field is a _____ field.", ["Scalar", "*Vector", "Tensor", "No"], "Has magnitude and direction."),
])
all_new[k] = q

k, q = add_qs("u6_l6.3", [
    ("Orbital motion occurs when an object has enough tangential velocity to continuously _____ around another body.", ["Accelerate", "*Fall (while maintaining altitude)", "Stop", "Oscillate"], "Continuous free fall."),
    ("For circular orbit: gravitational force = centripetal force, so GMm/r² = mv²/r, giving v =", ["GM/r", "√(GM/r²)", "*√(GM/r)", "GMr"], "v = √(GM/r)."),
    ("Orbital speed _____ as orbital radius increases.", ["Increases", "*Decreases", "Stays the same", "Doubles"], "v ∝ 1/√r."),
    ("An astronaut in orbit feels 'weightless' because:", ["Gravity is zero", "*They are in free fall (accelerating at g)", "They are far from Earth", "Air resistance holds them up"], "Free fall."),
    ("The orbital period T = 2πr/v. Combining with v: T² ∝ _____.", ["r", "r²", "*r³ (Kepler's Third Law)", "1/r"], "T² ∝ r³."),
    ("Low Earth orbit altitude is roughly:", ["36,000 km", "*200-2000 km", "1 km", "384,000 km"], "LEO range."),
    ("The ISS orbits at roughly _____ km altitude.", ["36,000", "100", "*400", "2000"], "Approximately 400 km."),
    ("LEO speed is approximately:", ["3 km/s", "*7.8 km/s", "11.2 km/s", "30 km/s"], "≈ 7.8 km/s."),
    ("In orbit, the only force (ignoring drag) is:", ["Thrust", "Normal force", "*Gravity", "Friction"], "Gravity provides centripetal force."),
    ("Orbital energy = KE + PE = -GMm/(2r). This is:", ["Positive", "*Negative (bound orbit)", "Zero", "Infinite"], "Bound orbits have negative total energy."),
    ("A higher orbit has _____ total energy (less negative).", ["Lower", "*Higher (closer to zero)", "The same", "More negative"], "Less bound."),
    ("To move to a higher orbit, a spacecraft must _____ its energy.", ["Decrease", "*Increase (fire engines to speed up)", "Keep the same", "Zero out"], "More energy needed."),
    ("Elliptical orbits: speed is greatest at _____ (closest approach).", ["Apoapsis", "*Periapsis", "The equator", "The poles"], "Fastest at closest point."),
])
all_new[k] = q

k, q = add_qs("u6_l6.4", [
    ("A geostationary satellite orbits with period:", ["90 minutes", "12 hours", "*24 hours (matches Earth's rotation)", "1 year"], "Appears stationary."),
    ("Geostationary orbit altitude ≈:", ["200 km", "2,000 km", "*35,786 km", "384,400 km"], "≈ 36,000 km."),
    ("Geostationary orbit must be directly above the:", ["Poles", "*Equator", "Tropic of Cancer", "Any latitude"], "Equatorial orbit."),
    ("GPS satellites orbit at about 20,200 km with period ≈:", ["24 hours", "*12 hours", "90 minutes", "1 year"], "12-hour period."),
    ("Polar orbits pass over the:", ["Equator only", "One hemisphere", "*Both poles (nearly)", "Geostationary point"], "Pole to pole."),
    ("The Moon is a natural satellite at about _____ km from Earth.", ["36,000", "200,000", "*384,400", "1,000,000"], "≈ 384,400 km."),
    ("Communication satellites are often geostationary so that ground dishes:", ["Rotate constantly", "*Can point at a fixed direction", "Don't need power", "Use less fuel"], "Fixed position in sky."),
    ("Satellite orbital speed depends on _____ (not on the satellite's mass).", ["The satellite's mass", "*The central body's mass and orbital radius", "The satellite's shape", "Fuel amount"], "v = √(GM/r)."),
    ("A satellite in a higher orbit moves _____ than one in a lower orbit.", ["Faster", "*Slower", "At the same speed", "Backward"], "v ∝ 1/√r."),
    ("To deorbit, a satellite must _____ its speed.", ["Increase", "*Decrease (fire retro-rockets)", "Maintain", "Double"], "Reduce speed to lower orbit."),
    ("The orbital period of a LEO satellite (≈400 km) is approximately:", ["24 hours", "12 hours", "*About 90 minutes", "1 hour"], "≈ 90 minutes."),
    ("Kepler's Third Law for satellites: T² = (4π²/GM)r³. The constant depends on:", ["The satellite mass", "*The central body mass M", "Temperature", "Orbit shape only"], "Depends on M."),
    ("A satellite's orbit decays due to:", ["Gravity weakening", "*Atmospheric drag (for low orbits)", "Solar radiation only", "Magnetic repulsion"], "Drag slows it."),
])
all_new[k] = q

k, q = add_qs("u6_l6.5", [
    ("Escape velocity is the minimum speed needed to _____ a gravitational field.", ["Orbit in", "Enter", "*Leave (reach infinity)", "Stay in"], "Escape to infinity."),
    ("Escape velocity from Earth's surface: v_e = √(2GM/R) ≈", ["7.8 km/s", "*11.2 km/s", "3.0 km/s", "30 km/s"], "≈ 11.2 km/s."),
    ("Escape velocity does not depend on the:", ["Planet mass", "Planet radius", "*Mass of the escaping object", "Gravitational constant"], "Independent of escaping mass."),
    ("At escape velocity, total mechanical energy (KE + PE) =", ["Positive", "Negative", "*Zero", "Infinite"], "Exactly enough to reach ∞."),
    ("If launched above escape velocity, the object has positive total energy and:", ["Falls back", "Orbits", "*Escapes with residual speed", "Stops"], "Moves away forever."),
    ("If launched below escape velocity:", ["It escapes", "*It falls back (or enters orbit)", "It reaches infinity", "Energy is negative"], "Not enough energy."),
    ("Escape velocity from the Moon is _____ than from Earth because the Moon has less mass.", ["Greater", "*Less (≈ 2.4 km/s)", "The same", "Zero"], "Smaller M, smaller v_e."),
    ("For a planet of mass 4M_E and radius 2R_E: v_e = √(2G(4M)/(2R)) = √(4GM/R) = 2√(GM/R). Compared to Earth's:", ["Same", "Half", "*√2 times (about 1.41×)", "Double"], "Actually v_e = √(2G×4M/(2R)) = √(4GM/R) = 2v_earth/√2 = √2 × v_earth... let me recalc: v_e = √(2GM_E/R_E) for Earth. New: √(2G(4M_E)/(2R_E)) = √(4GM_E/R_E) = √2 × √(2GM_E/R_E) = √2 × v_e."),
    ("If a planet's radius halves but mass stays the same, escape velocity:", ["Halves", "*Increases by √2", "Stays the same", "Doubles"], "v_e = √(2GM/R), smaller R = larger v_e."),
    ("The concept of escape velocity leads to the idea of:", ["Satellites", "Orbits", "*Black holes (where v_e ≥ c, the speed of light)", "Tides"], "Black hole: v_e ≥ c."),
    ("A black hole has escape velocity ≥:", ["Sound speed", "Orbital speed", "*Speed of light (c)", "Mach 3"], "Nothing can escape."),
    ("The Schwarzschild radius is the radius where escape velocity = c:", ["r = GM/c²", "*r = 2GM/c²", "r = GM/c", "r = c²/GM"], "R_s = 2GM/c²."),
    ("Escape velocity at the surface of the Sun ≈:", ["11.2 km/s", "400 m/s", "*617 km/s", "300,000 km/s"], "≈ 617 km/s."),
])
all_new[k] = q

k, q = add_qs("u6_l6.6", [
    ("Kepler's First Law: planets orbit in _____ with the Sun at one focus.", ["Circles", "*Ellipses", "Parabolas", "Hyperbolas"], "Elliptical orbits."),
    ("Kepler's Second Law: a line from planet to Sun sweeps equal _____ in equal times.", ["Distances", "*Areas", "Angles", "Speeds"], "Equal area in equal time."),
    ("Kepler's Third Law: T² ∝ _____.", ["r", "r²", "*r³ (or a³ for semi-major axis)", "1/r"], "Period squared ∝ semi-major axis cubed."),
    ("Kepler's Second Law implies a planet moves faster when it is _____ to the Sun.", ["Farther from", "*Closer to", "Perpendicular to", "At 90° from"], "Speed up near Sun."),
    ("The point of closest approach to the Sun is called:", ["Aphelion", "*Perihelion", "Perigee", "Zenith"], "Perihelion."),
    ("The farthest point from the Sun is:", ["Perihelion", "*Aphelion", "Perigee", "Nadir"], "Aphelion."),
    ("If planet A is 4 times farther from the Sun than planet B, its period is:", ["4 times longer", "16 times longer", "*8 times longer (T ∝ r^(3/2), so 4^(3/2) = 8)", "2 times longer"], "4^1.5 = 8."),
    ("Kepler's laws were empirical. Newton later derived them from:", ["Optics", "*His law of gravitation", "Thermodynamics", "Electromagnetism"], "Gravitational theory."),
    ("Earth's orbit is nearly circular but actually slightly:", ["Square", "*Elliptical (eccentricity ≈ 0.017)", "Hyperbolic", "Parabolic"], "Low eccentricity."),
    ("An orbit with eccentricity 0 is a:", ["Line", "Ellipse", "*Circle", "Parabola"], "e=0 is a circle."),
    ("An orbit with eccentricity approaching 1 is a very:", ["Circular", "*Elongated ellipse", "Short", "Symmetric"], "Highly elliptical."),
    ("The semi-major axis 'a' of an ellipse is half the:", ["Minor axis", "*Longest diameter", "Perimeter", "Focus distance"], "Half the major axis."),
    ("Kepler's Third Law exactly: T² = (4π²/GM)a³. M is the mass of the:", ["Planet", "*Central body (Sun for planets)", "Satellite", "Moon"], "Central body mass."),
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

print(f"✅ Physics U4-U6: expanded {len(all_new)} lessons")
