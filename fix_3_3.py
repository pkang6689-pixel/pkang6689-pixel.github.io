import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    1: [
        "For every action force there exists an equal and opposite reaction force, acting on a different object as described by Newton's third law of motion",
        "An object at rest stays at rest and an object in motion stays in motion at constant velocity unless acted on by an unbalanced external net force",
        "The net force on an object equals the product of its mass and its velocity, directed along the line of motion of the object at every instant in time"
    ],
    9: [
        "Both objects have the same net force acting on them, because identical accelerations always require identical forces regardless of the masses involved",
        "Neither object has a net force because only velocity matters for determining force, and acceleration is irrelevant to the relationship between force and mass",
        "The 1 kg object has the greater net force because lighter objects always need more force to achieve any acceleration, as their low inertia demands more input"
    ],
    11: [
        "The law describing action-reaction pairs, which states that every force is accompanied by an equal and opposite force acting on a different object in the system",
        "The law stating that objects resist changes in their state of motion due to inertia, remaining at rest or moving at constant velocity when no net force acts",
        "The law of universal gravitation, which states that every mass attracts every other mass with a force proportional to the product of their masses over distance squared"
    ],
    12: [
        "Exactly the same as mass in all situations and locations, since weight and mass are interchangeable terms that always refer to the same physical quantity",
        "The measure of how tightly packed matter is within an object, calculated by dividing the total mass of the object by its volume in cubic meters",
        "The perpendicular support force that a surface exerts on any object resting on it, acting upward to prevent the object from passing through the surface"
    ],
    13: [
        "The total volume of space that an object occupies, measured in cubic meters and determined by the physical dimensions and shape of the object in question",
        "A type of force that is measured in kilograms, representing the downward gravitational pull that the Earth exerts on any object near its surface",
        "The total amount of gravitational attraction acting on an object, which varies with location and depends on the strength of the local gravitational field"
    ],
    14: [
        "They are completely unrelated quantities that have no mathematical connection to each other and cannot be expressed through any formula or equation",
        "They are equal in magnitude at all times, meaning the numerical value of force in newtons always matches the numerical value of acceleration in m/s squared",
        "They are inversely proportional for a fixed mass \u2014 increasing the applied force causes the resulting acceleration to decrease by the same proportional factor"
    ],
    15: [
        "The electrostatic force that exists between any two protons in a nucleus, holding nuclear particles together through the fundamental electromagnetic interaction",
        "The total combined gravitational pull of all objects in the entire universe acting simultaneously on a single test mass placed at a specific location in space",
        "The total mass of the Earth in kilograms, which determines how strong the gravitational pull is for all objects located on or near the planet's surface"
    ],
    17: [
        "The reaction force in Newton's third law, which acts on the original force-applying object in the equal and opposite direction of the initial action force",
        "Any force that acts at a distance through a field without requiring physical contact, such as gravitational, electric, or magnetic forces between objects",
        "The gravitational force that the Earth exerts on an object, pulling it downward toward the center of the planet with a magnitude equal to mass times g"
    ],
    18: [
        "A condition that occurs when two forces happen to point in the same direction, reinforcing each other and producing a larger combined net effect",
        "A relationship that only exists within abstract mathematical equations and has no observable or measurable consequences in real physical experiments",
        "A condition where two quantities always have identical numerical values at every instant, regardless of the units used to measure each quantity"
    ],
    20: [
        "Always identical to the true gravitational weight of the object, since scales always display the exact value of mg regardless of any acceleration present",
        "The quotient obtained by dividing the gravitational weight by the local gravitational acceleration, yielding the mass of the object in kilograms",
        "The weight of an object specifically when measured on the surface of the Moon, where the gravitational field strength is approximately one-sixth of Earth's"
    ],
    21: [
        "480 N \u2014 the scale reads N = m times (g minus a) = 60 times (10 minus 2) = 480 N, because upward acceleration reduces the apparent weight on the scale",
        "120 N \u2014 the scale reads N = m times a = 60 times 2 = 120 N, because only the acceleration component matters when the elevator is moving upward",
        "600 N \u2014 the scale reads N = mg = 60 times 10 = 600 N, because the elevator's acceleration does not affect the reading shown on a bathroom scale"
    ],
    22: [
        "20000 N \u2014 using F = m times v = 2000 times 20/2 = 20000 N, because force equals the product of mass and average velocity during the acceleration interval",
        "40000 N \u2014 using F = m times v = 2000 times 20 = 40000 N, because force equals the product of mass and the final velocity the car reaches after ten seconds",
        "200 N \u2014 using F = m divided by t = 2000 divided by 10 = 200 N, because force equals the total mass divided by the time over which the acceleration occurs"
    ],
    23: [
        "2 m/s\u00b2 west \u2014 net force = 10 minus 30 = negative 20 N pointing west; a = 20/5 = 4, then halved because opposing forces reduce the effective acceleration",
        "8 m/s\u00b2 east \u2014 adding both forces: 30 + 10 = 40 N total; a = 40/5 = 8 m/s\u00b2 east, because forces on the same object always add regardless of direction",
        "40 m/s\u00b2 east \u2014 multiplying the forces: 30 times 10 = 300 then dividing by 5 = 60, approximately 40 m/s\u00b2, because net force is the product of individual forces"
    ],
    24: [
        "9.8 m/s\u00b2 downward \u2014 the acceleration is simply g because all falling objects accelerate at the same rate regardless of any air resistance forces acting on them",
        "15.5 m/s\u00b2 downward \u2014 adding the forces: (686 + 400)/70 = 1086/70 = 15.5 m/s\u00b2, because both weight and air resistance contribute to the downward acceleration",
        "0 m/s\u00b2 because she has reached terminal velocity \u2014 since she is falling and experiencing air resistance, the net force must already be zero at this point"
    ],
    25: [
        "80 N \u2014 the scale reads the person's mass in newtons because in free fall the gravitational acceleration cancels leaving only the raw mass value on the display",
        "784 N \u2014 the scale reads the full weight mg = 80 times 9.8 = 784 N, because weight does not change during free fall and the scale always shows true weight",
        "392 N \u2014 the scale reads half the normal weight because free fall reduces the apparent weight by exactly fifty percent compared to the stationary weight value"
    ],
    26: [
        "2 N \u2014 dividing the original force by the new acceleration: F = 12/6 = 2 N, because force and acceleration have an inverse relationship for the same mass",
        "8 N \u2014 adding the acceleration values and dividing by mass: F = (4 + 6)/3 = 3.33, rounded to approximately 8 N for the force needed to produce 6 m/s squared",
        "24 N \u2014 multiplying the original force by the acceleration ratio: F = 12 times (6/4) = 18, then adding the original to get 24 N total required force"
    ],
    27: [
        "4 m/s\u00b2 \u2014 using the full engine force: a = F divided by m = 6000/1500 = 4 m/s\u00b2, because friction does not reduce the forward force when the engine is running",
        "9 m/s\u00b2 \u2014 adding the forces: a = (6000 + 1500)/1500 = 5, approximately 9 m/s\u00b2 because friction adds to the engine force when both act on the same car",
        "5 m/s\u00b2 \u2014 dividing engine force by total resistance: a = 6000/(1500 + friction) but using only mass: a = 6000/1200 = 5 m/s\u00b2 as the net forward acceleration"
    ],
    28: [
        "10 N \u2014 using F = m times g_earth = 10 times 1 = 10 N, because on the Moon the effective gravity constant equals exactly 1 newton per kilogram of mass",
        "1.6 N \u2014 using F = g = 1.6 N, because the gravitational force is simply equal to the gravity constant value regardless of the object's mass on any surface",
        "98 N \u2014 using F = mg_earth = 10 times 9.8 = 98 N, because an object's weight depends only on Earth's gravity even when the object is located on the Moon"
    ],
    29: [
        "5 m/s\u00b2 \u2014 using the applied force only: a = F/m = 100/20 = 5 m/s\u00b2, because friction does not affect the acceleration when the box is already in motion on a level surface",
        "2 m/s\u00b2 \u2014 using the friction force only: a = f/m = 40/20 = 2 m/s\u00b2, because the friction force alone determines the acceleration rather than the net force on the box",
        "7 m/s\u00b2 \u2014 adding both forces: a = (100 + 40)/20 = 140/20 = 7 m/s\u00b2, because all forces on the object add their magnitudes regardless of their opposing directions"
    ],
    30: [
        "1 N \u2014 friction equals mass times the original acceleration: f = 0.5 times 2 = 1 N, because friction must match the driving force that was present on the smooth track",
        "0.25 N \u2014 friction equals mass times deceleration divided by 2: f = 0.5 times 1 / 2 = 0.25 N, because only half the deceleration comes from the friction force",
        "2 N \u2014 friction equals mass times the sum of both accelerations: f = 0.5 times (2 + 1) = 1.5, rounded to about 2 N since both phases contribute to friction"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.3_Quiz.json', fixes)
