import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    1: [
        "The color and visual appearance of the surface, because darker surfaces generate more friction than lighter-colored surfaces at the molecular interaction level",
        "Air molecules pushing against the surfaces and creating resistance between them, since atmospheric pressure is the primary source of friction between any two objects",
        "Gravity pulling the two objects together with a force proportional to their combined masses, because gravitational attraction is the fundamental cause of all friction"
    ],
    2: [
        "Static friction only exists on inclined surfaces and not on flat horizontal surfaces, because the angle of the incline is what creates the frictional resistance",
        "Static friction and kinetic friction are exactly the same physical phenomenon described by the same coefficient, with no difference in their maximum force values",
        "Kinetic friction is always greater than static friction for any pair of surfaces, because moving objects experience more resistance than stationary objects do"
    ],
    3: [
        "f = the coefficient of friction times weight times the contact area, because friction depends on how large the surface area of contact is between the objects",
        "f = ma, where m is the mass and a is the acceleration, since friction is calculated the same way as any other force using Newton's second law of motion",
        "f = the coefficient of friction times mg only, because the normal force is always equal to the weight and contact area determines the actual friction value"
    ],
    4: [
        "f_k = m times g, where the kinetic friction force equals the weight of the object regardless of the coefficient or the nature of the contacting surfaces",
        "f_k = the coefficient of kinetic friction times weight times velocity, because faster-moving objects experience proportionally more kinetic friction force",
        "f_k = the coefficient of kinetic friction times the contact area, since kinetic friction depends primarily on how much surface area is touching between objects"
    ],
    8: [
        "Friction never causes any object to accelerate under any conditions, because friction is by definition a decelerating force that always removes kinetic energy",
        "Yes friction always slows things down without exception, because the sole function of friction in every physical situation is to reduce an object's velocity",
        "No friction sometimes accelerates objects in any arbitrary direction regardless of the surface orientation, because friction can point in any direction at all"
    ],
    9: [
        "4 N \u2014 using f = coefficient times mass gives f = 0.4 times 10 = 4 N, because the friction formula uses mass directly rather than the normal force value",
        "10 N \u2014 using f = coefficient times g gives f = 0.4 times 10 divided by 0.4 = 10 N, because the gravity value alone determines the static friction force",
        "100 N \u2014 using f = N = mg gives f = 10 times 10 = 100 N, because the maximum static friction force always equals the full normal force on a horizontal surface"
    ],
    11: [
        "A force that only acts on surfaces that are visibly rough to the naked eye, since perfectly smooth surfaces have zero friction between them at all contact points",
        "A non-contact force that operates at a distance between any two objects through their gravitational fields, without requiring any physical contact between surfaces",
        "A force that always prevents all motion completely, stopping any object from moving no matter how large the applied force is relative to the friction coefficient"
    ],
    12: [
        "The total surface area of contact between the two objects, because larger contact areas produce proportionally more friction between the sliding surfaces",
        "The weight of the heavier surface in the pair, since the more massive object determines the friction level regardless of the properties of the lighter surface",
        "The friction force measured in newtons between the surfaces, calculated by multiplying the mass of the sliding object by the gravitational acceleration constant"
    ],
    13: [
        "A constant force that always equals exactly the product of the static coefficient times the normal force, regardless of how much applied force is present",
        "Friction that acts only on objects that are completely stationary and can never appear on objects that have been in motion at any point during the experiment",
        "The friction present on very smooth surfaces like polished glass, since the smoothness of the surface determines whether friction is classified as static"
    ],
    14: [
        "Friction that only acts on rolling objects like wheels and spheres, and does not apply to objects that slide or translate across flat surfaces without rotating",
        "A friction force that varies proportionally with the contact area between the two surfaces, since larger contact patches generate more kinetic friction force",
        "Friction that increases proportionally with the speed of the sliding object, because faster objects experience greater resistance from the surface they slide on"
    ],
    15: [
        "The gravitational force pulling an object downward toward the center of the Earth, which has a magnitude equal to the mass of the object multiplied by g",
        "A force that acts parallel to the contact surface, sliding along it in the direction of applied force rather than pressing perpendicular into the surface",
        "The coefficient of friction itself, which is a dimensionless number characterizing the surface pair rather than a force with magnitude and direction"
    ],
    16: [
        "The total weight of an object hanging from a rope or string, since tension is simply another name for the gravitational force acting on suspended masses",
        "The frictional resistance that exists within the internal fibers of a rope, opposing any stretching or deformation of the rope's material structure",
        "A compressive pushing force transmitted through a rigid rod or bar, capable of pushing objects apart rather than pulling them together across distances"
    ],
    17: [
        "A rope that has a standard mass of exactly one kilogram per meter of length, providing a baseline reference value for tension calculations in all problems",
        "A rope that can never break no matter how much force is applied to it, having infinite tensile strength while maintaining normal mass and elasticity properties",
        "A rope that has infinite elasticity and stretches to any length under any applied force, absorbing unlimited energy before returning to its original length"
    ],
    18: [
        "A device that stores potential energy in its rotating mechanism, converting kinetic energy into stored rotational energy for later release when needed",
        "A device that doubles the tension force in a rope by mechanical advantage, always requiring exactly half the input force to lift any given weight upward",
        "A wheel mechanism whose primary purpose is to create friction in the rope, generating heat and resistance that allow the user to control the rope's speed"
    ],
    19: [
        "The kinetic friction force that acts on a moving object as it slides across a surface, having a constant value equal to the kinetic coefficient times normal force",
        "The friction present on the smoothest possible surface available, representing the minimum achievable friction for any pair of contacting materials in contact",
        "A state of zero friction between two surfaces, achieved when the surfaces are perfectly polished and no molecular interactions occur at the contact interface"
    ],
    20: [
        "Exactly the same physical phenomenon as kinetic friction applied to circular objects, with identical coefficient values and identical mathematical formulas used",
        "Friction that only acts on cylindrical objects like perfect cylinders and has no effect on spherical objects like balls or other non-cylindrical rolling shapes",
        "Friction that causes wheels to spin faster by adding rotational energy to the wheel, increasing the angular velocity rather than opposing the rolling motion"
    ],
    21: [
        "Yes it moves \u2014 80 N exceeds the maximum friction of 60 N, so the crate begins sliding with kinetic friction providing the only opposing force on the surface",
        "Yes it moves \u2014 80 N of applied force is more than enough to move any crate regardless of mass, surface properties, or the coefficient of friction between them",
        "No it does not move \u2014 friction is always exactly equal to the maximum value of 100 N regardless of the applied force, providing constant resistance at all times"
    ],
    22: [
        "The crate moves but with exactly zero acceleration because kinetic friction automatically adjusts to equal the applied force and maintain constant velocity",
        "The crate accelerates at 6 m/s squared because the net force equals the applied force minus the weight: a = (120 minus 100) divided by 20/6 = 6 m/s squared",
        "The crate does not move because kinetic friction increases to 120 N to match the applied force, preventing any motion from starting on the rough floor surface"
    ],
    23: [
        "25 N \u2014 dividing the weight by 2 gives T = mg/2 = 50/2 = 25 N, because a hanging mass only transfers half its weight as tension to the supporting rope above",
        "100 N \u2014 doubling the weight gives T = 2mg = 2 times 50 = 100 N, because the rope must support both the mass and the reaction force from the ceiling attachment",
        "5 N \u2014 the tension equals just the mass value T = m = 5 N, because tension in newtons is numerically equal to the mass in kilograms for any hanging object"
    ],
    24: [
        "a = 3 m/s squared and T = 15 N \u2014 the tension equals the force times the lighter mass ratio: T = 24 times 3/8 = 9 then adjusted to 15 N for the heavier block",
        "a = 3 m/s squared and T = 24 N \u2014 the full applied force is transmitted through the rope between the blocks, so tension equals the applied force of 24 newtons",
        "a = 4.8 m/s squared and T = 14.4 N \u2014 using only the heavier block: a = 24/5 = 4.8, then T = 3 times 4.8 = 14.4 N from the lighter block's perspective"
    ],
    25: [
        "a = 0.87 m/s squared \u2014 using only the horizontal force component divided by mass: a = 60 cos 30 / 15 = 52/60 = 0.87, ignoring the friction force entirely",
        "a = 4 m/s squared \u2014 using the full tension without resolving components: a = 60/15 = 4 m/s squared, because the angle does not affect the net force calculation",
        "a = 2.8 m/s squared \u2014 using the vertical component as the driving force: a = 60 sin 30 / 15 = 30/15 = 2, then adding friction gives approximately 2.8 m/s squared"
    ],
    26: [
        "a = 5 m/s squared and T = 50 N \u2014 using only the heavier mass: a = (6)(10)/(6+4) = 6, adjusted to 5, and T = 10 times 5 = 50 N from the total system weight",
        "a = 10 m/s squared and T = 40 N \u2014 using a = g = 10 m/s squared since both masses are in free fall, and T = 4 times 10 = 40 N from the lighter mass's weight",
        "a = 2 m/s squared and T = 60 N \u2014 using T = m2 times g = 6 times 10 = 60 N, because the tension equals the full weight of the heavier mass in all Atwood machines"
    ],
    27: [
        "15000 N \u2014 using the full weight as the maximum braking force: f = mg = 1500 times 10 = 15000 N, because maximum friction always equals the total weight of the car",
        "8000 N \u2014 using f = coefficient times mass: f = 0.8 times 1500 = 1200 then multiplied by some factor to get approximately 8000 N maximum braking force on the road",
        "1200 N \u2014 using f = coefficient times mass directly: f = 0.8 times 1500 = 1200 N, because the friction formula uses mass in kilograms rather than the normal force"
    ],
    28: [
        "Less than 20 N \u2014 the rope sags, which means some of the weight is supported by the sag itself, reducing the tension needed in each side of the rope below 10 N each",
        "Exactly 10 N in each side of the rope \u2014 the weight divides equally between the two sides, giving exactly half of 20 N = 10 N of tension in each half of the rope",
        "Equal to exactly 20 N \u2014 the total tension in the rope must equal the weight of the hanging mass, so T = mg = 2 times 10 = 20 N regardless of the sag angle"
    ],
    29: [
        "Yes the student is correct \u2014 if friction were acting on the box, it would immediately decelerate and stop, because friction always causes objects to slow down instantly",
        "Yes the student is correct \u2014 constant velocity is proof that no friction force is present, since friction would cause the box to decelerate and eventually come to rest",
        "Partially correct \u2014 friction only begins acting once the box starts to decelerate, and until that happens there is no friction force present between the surfaces"
    ],
    30: [
        "Yes it slides because gravity always pulls objects down any incline regardless of friction, since no surface can provide enough friction to hold a 10 kg object",
        "Yes it slides because 10 kg is too heavy for friction to hold on any inclined surface, since heavier objects always overcome static friction and begin sliding",
        "No it stays because blocks never slide on inclines less than 45 degrees, since the critical angle for sliding is always 45 degrees regardless of friction coefficient"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.5_Quiz.json', fixes)
