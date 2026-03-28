import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    11: [
        "The energy an object possesses due to its elevated position relative to a reference point, also known as gravitational potential energy measured in joules",
        "A scalar measure of how fast an object is moving at a given instant, calculated as the distance covered per unit time in meters per second",
        "The continuous displacement of an object through space from one location to another, characterized by a trajectory path and an elapsed travel time"
    ],
    15: [
        "A state in which the object is perfectly still and has no forces acting on it at all, since the absence of motion implies the absence of all applied forces",
        "A state that can only be achieved in the microgravity environment of outer space, where gravitational forces are absent and no weight is experienced by objects",
        "A state in which all individual forces acting on the object have exactly equal magnitudes, even if they do not point in opposing directions to cancel out"
    ],
    16: [
        "A graph that plots the magnitude of force acting on an object against elapsed time, showing how the applied force changes throughout the duration of motion",
        "A detailed diagram of an object falling freely under gravity alone, showing its trajectory path, velocity at each point, and the acceleration due to gravity",
        "A complete sketch of the entire experimental setup in a physics laboratory, including all equipment, instruments, measuring devices, and surrounding furniture"
    ],
    17: [
        "Any force whose magnitude is measured in the standard SI unit of newtons, regardless of its physical origin or the type of interaction that produces it",
        "The precise amount of force needed to accelerate a one-kilogram mass by exactly one meter per second squared, which defines the SI unit called the newton",
        "A force that acts only on fundamental subatomic particles such as quarks and leptons, and has no measurable effect on larger everyday macroscopic objects"
    ],
    18: [
        "The friction force that acts along the interface between two surfaces in contact, opposing the relative sliding motion or tendency of motion between them",
        "The gravitational force that the Earth exerts on an object, pulling it downward toward the center of the Earth with a magnitude equal to mass times g",
        "A force whose magnitude is always exactly equal to the weight of the object, regardless of the surface orientation, applied forces, or acceleration present"
    ],
    19: [
        "The gravitational attraction between two objects with mass, acting at a distance through the gravitational field without any physical contact being required",
        "The restoring force produced by a spring when it is compressed below its natural equilibrium length, pushing outward on whatever compresses it at both ends",
        "A repulsive force that acts to push two objects apart from each other, operating through electromagnetic repulsion between like charges at the atomic level"
    ],
    21: [
        "Only the upward normal force from the table acts on the book, since gravity is canceled out by the table's presence and does not count as a separate force",
        "Friction and tension are the only forces acting on the book, because the book must be held in place by friction to prevent it from sliding off the table",
        "Only gravity acts on the book pulling it downward, since the table merely blocks the book's path and does not exert any actual upward force on its surface"
    ],
    22: [
        "Friction is zero because the box is currently in motion, and kinetic friction only exists when objects are stationary and about to start moving from rest",
        "Friction is greater than 50 N since the box requires extra force beyond the push to overcome the initial resistance and maintain its constant sliding speed",
        "Friction is less than 50 N because some of the applied pushing force goes into maintaining the box's velocity while only the remainder opposes friction"
    ],
    23: [
        "0 N total \u2014 the two forces completely cancel each other since both teams pull on the same rope and opposite forces on the same object always sum to zero",
        "950 N total \u2014 the net force is the sum of both pulls: 500 + 450 = 950 N, because all forces on a rope add together regardless of direction to give the total",
        "50 N toward Team B \u2014 the net force points toward the weaker team because the stronger team's force pushes the rope away from themselves toward the opposition"
    ],
    25: [
        "The elevator must be completely stationary on a floor, because the scale can only display your true weight when there is absolutely zero velocity in the system",
        "The elevator is currently in free fall, because weightlessness and normal weight are indistinguishable from each other when measured by a standard bathroom scale",
        "The elevator must be accelerating upward, because only upward acceleration can produce a scale reading that matches your actual gravitational weight value exactly"
    ],
    26: [
        "6 m/s\u00b2 \u2014 using only the lighter mass: a = F/m = 30/5 = 6 m/s\u00b2, because the force acts primarily on the smaller box which then pushes the larger one forward",
        "3 m/s\u00b2 \u2014 using only the heavier mass: a = F/m = 30/10 = 3 m/s\u00b2, because the acceleration depends on the larger box since it carries most of the system's weight",
        "0.5 m/s\u00b2 \u2014 dividing total mass by force: a = m/F = 15/30 = 0.5 m/s\u00b2, because the formula for acceleration requires mass divided by force not the reverse"
    ],
    27: [
        "0 N \u2014 since she is falling there cannot be any upward force acting on her, as falling objects by definition experience only the downward pull of gravity alone",
        "1400 N \u2014 the drag force must be double her weight to slow her descent, since the parachute needs to both support her weight and actively reduce her speed",
        "350 N \u2014 the drag force equals half her weight because the parachute only partially resists gravity, leaving the other half as a net downward force on her body"
    ],
    28: [
        "4 N \u2014 only the east-west forces matter for the resultant: 10 minus 6 = 4 N, and the northward force is perpendicular so it does not contribute to the net total",
        "8 N \u2014 only the northward component matters for the resultant: the east and west forces cancel each other out, leaving just the 8 N north as the entire net force",
        "24 N \u2014 adding all three force magnitudes together: 10 + 6 + 8 = 24 N, since the net force is the scalar sum of all individual force magnitudes acting on the object"
    ],
    29: [
        "Yes the student is correct \u2014 all moving objects eventually slow down and stop because motion naturally dissipates over time even without any external resistance present",
        "Yes the student is correct \u2014 interstellar space contains enough residual friction from gas molecules to gradually slow any spacecraft to zero velocity over time",
        "No the student is wrong \u2014 without a net force the spacecraft will actually speed up continuously, gaining velocity from the residual energy stored in its mass"
    ],
    30: [
        "Yes \u2014 the dashboard or windshield exerts a real forward force on your body, actively pushing you toward the front of the car during the rapid braking event",
        "Yes \u2014 inertia itself is a real physical force that pushes your body forward whenever the car decelerates, acting in the opposite direction of the braking force",
        "No \u2014 the only force you feel is the seatbelt pulling you back, which creates the illusion of forward motion even though no other forces are present on your body"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.1_Quiz.json', fixes)
