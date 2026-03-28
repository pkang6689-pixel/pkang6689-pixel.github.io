import json
import sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    9: [
        "52 m \u2014 using the formula s = u + at squared gives s = 10 + 3 times 16 = 10 + 48 = 52 m of total displacement traveled",
        "124 m \u2014 multiplying all three values together gives s = u times a times t = 10 times 3 times 4 = 120 plus 4 = 124 m displacement",
        "40 m \u2014 using only the first term of the equation gives s = ut = 10 times 4 = 40 m, ignoring the acceleration contribution"
    ],
    10: [
        "Two \u2014 there are only two fundamental kinematic equations, and any others are simply restatements using different variable arrangements",
        "Ten \u2014 there are ten independent kinematic equations because each combination of the five variables produces a unique relationship",
        "One \u2014 there is only one master kinematic equation from which all motion relationships can be directly read without rearrangement"
    ],
    11: [
        "Equations that describe the forces acting on an object, including gravity, friction, and normal force, to predict the net force and resulting motion",
        "Any equation used in any branch of physics, including thermodynamics, electromagnetism, optics, and quantum mechanics, not just kinematics",
        "Formulas that only apply to objects in free fall under gravity, and cannot be used for objects that are launched, braking, or moving horizontally"
    ],
    16: [
        "A special equation developed specifically for circular motion, relating centripetal acceleration to the radius and angular velocity of a revolving object",
        "An acronym for a particular type of force equation that connects applied force, mass, friction coefficient, and the resulting net acceleration",
        "Equations used exclusively in the United Kingdom physics curriculum and not recognized or applicable in other international education systems"
    ],
    17: [
        "Acceleration that always points in the downward direction, since deceleration can only occur when an object is moving vertically against gravity",
        "Any negative number that appears in a physics equation, regardless of whether it represents velocity, displacement, force, or some other quantity",
        "The complete absence of acceleration, meaning the object maintains a perfectly constant velocity with no change in speed or direction at all"
    ],
    18: [
        "Motion in which the object has zero velocity at all times, remaining perfectly stationary at a fixed location throughout the entire observation period",
        "Falling at a speed that is always exactly equal to the gravitational constant g, never accelerating beyond or decelerating below that fixed speed value",
        "Any motion in which an object moves in a downward direction, regardless of whether engines, air resistance, or other forces are also acting on it"
    ],
    19: [
        "The time an object spends at its highest point in the trajectory, where velocity momentarily equals zero before the object begins falling back down",
        "The time required for an object to reach its maximum speed during the acceleration phase, after which the object coasts at constant velocity",
        "The time required for one complete revolution of an object moving in a circular path, also known as the orbital period of the circular motion"
    ],
    21: [
        "48 m \u2014 using s = at squared without the one-half factor gives s = 3 times 16 = 48 m, which represents the distance at full acceleration rate",
        "12 m \u2014 using s = at gives s = 3 times 4 = 12 m, since distance equals the product of acceleration and time in uniformly accelerated motion",
        "6 m \u2014 using s = half times a times t gives s = 0.5 times 3 times 4 = 6 m, forgetting to square the time value in the displacement formula"
    ],
    22: [
        "\u221225 m/s\u00b2 \u2014 using a = v minus u divided by s gives a = (0 minus 25) divided by 1 = \u221225 m/s\u00b2, confusing distance with time in the formula",
        "\u221210 m/s\u00b2 \u2014 using a = u divided by s gives a = 25 divided by 2.5 = 10 m/s\u00b2 with a negative sign added, yielding \u221210 m/s\u00b2 deceleration",
        "\u22122.5 m/s\u00b2 \u2014 using a = u divided by 2s gives a = 25 divided by 125 = 0.2 then inverted to 2.5 m/s\u00b2 with a negative sign for braking"
    ],
    23: [
        "0.75 s \u2014 using t = u divided by 2g gives t = 15 divided by 20 = 0.75 s, which accounts for both the upward and downward phases",
        "3.0 s \u2014 this is the total flight time (up and back down), obtained by doubling the time to the highest point using t = 2u divided by g",
        "15 s \u2014 using t = u divided by 1 gives t = 15 s, mistakenly treating the initial velocity value as the time to reach the highest point"
    ],
    24: [
        "0.1 m/s\u00b2 \u2014 using a = (v minus u) divided by s gives a = 20 divided by 200 = 0.1 m/s\u00b2, confusing displacement with time in the calculation",
        "1 m/s\u00b2 \u2014 using a = (v minus u) divided by 2s gives a = 20 divided by 400 = 0.05, then rounding up to approximately 1 m/s\u00b2 acceleration",
        "4 m/s\u00b2 \u2014 using a = (v squared minus u squared) divided by s gives a = 800 divided by 200 = 4 m/s\u00b2, forgetting the factor of 2 in the formula"
    ],
    25: [
        "No \u2014 different kinematic equations always give different numerical answers because each equation models a different aspect of the physical situation",
        "Only if the initial velocity is exactly zero, because the kinematic equations are only consistent with each other when the object starts from rest",
        "Only if the acceleration is exactly zero, since the equations diverge and give conflicting results whenever there is any nonzero acceleration present"
    ],
    27: [
        "1500 m \u2014 using only the first phase: s = half times 15 times 100 = 750 m then doubling for the deceleration phase gives a total of 1500 m distance",
        "2250 m \u2014 using s = v times t for both phases: 150 times 10 = 1500 m plus 150 times 15 divided by 2 = 1125, total is roughly 2250 m distance",
        "750 m \u2014 calculating only the acceleration phase distance: s = half times 15 times 100 = 750 m and ignoring the coasting and deceleration phases"
    ],
    28: [
        "72 m \u2014 Phase 1: s = half times 1.5 times 16 = 12 m; Phase 2: s = 6 times 8 = 48 m; Phase 3: s = 12 m; Total = 12 + 48 + 12 = 72 m traveled",
        "36 m \u2014 using only the constant velocity phase and halving it: s = 6 times 8 divided by 2 = 24 m, plus 12 m from the other phases = 36 m total",
        "48 m \u2014 counting only the constant velocity middle phase: s = 6 times 8 = 48 m and treating the acceleration and deceleration as contributing zero"
    ],
    29: [
        "20 s \u2014 dividing the speeder's velocity by the police acceleration gives t = v divided by a = 20 divided by 4 = 5, then doubling yields 20 seconds",
        "4 s \u2014 dividing the police acceleration by the speeder's velocity gives t = a divided by v = 4 divided by 20 = 0.2, then inverting yields about 4 s",
        "5 s \u2014 using the average velocity method: the police car's average speed equals half the speeder's speed at t = 5 s, so they meet at t = 5 seconds"
    ],
    30: [
        "The student is always correct \u2014 distance can never be negative under any circumstances, so using a positive value of g is the only valid approach in physics",
        "The friend is always correct \u2014 the acceleration due to gravity must always carry a negative sign regardless of coordinate system or direction conventions",
        "Neither student is correct \u2014 the entire calculation itself contains a mathematical error because the formula s = ut + half at squared does not apply here"
    ]
}

fix_file('content_data/PhysicsLessons/Unit2/Lesson2.4_Quiz.json', fixes)
