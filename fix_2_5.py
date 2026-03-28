import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    7: [
        "The wind speed and direction at the time of launch, since air currents are the primary factor determining how long any projectile remains airborne",
        "The horizontal velocity at which the projectile was launched, since faster horizontal speeds keep projectiles in the air for longer durations overall",
        "The mass of the projectile, since heavier objects experience greater gravitational force and therefore remain airborne for shorter periods of time"
    ],
    12: [
        "Any object that is currently moving through the air, including powered aircraft, helicopters, birds, and anything else traveling above the ground",
        "An object that is continuously pushed by a constant applied force throughout its entire flight, maintaining steady acceleration in the forward direction",
        "A ball rolling along a flat surface under the influence of friction, experiencing constant deceleration until it eventually comes to a complete stop"
    ],
    13: [
        "The speed at which an object moves through space, measured in meters per second and representing the scalar magnitude of the velocity vector",
        "The total distance traveled by an object from its starting position to its ending position, measured along the entire path it actually followed",
        "A perfectly straight line connecting the start point to the finish point of an object's journey, representing the shortest possible travel path"
    ],
    14: [
        "The maximum height reached by the projectile above its launch point, occurring at the midpoint of the flight when vertical velocity equals zero",
        "The total time the projectile spends in the air from launch to landing, determined by the vertical component of the initial velocity and gravity",
        "The total path length measured along the curved trajectory of the projectile, accounting for both horizontal and vertical distances traveled"
    ],
    15: [
        "The time it takes for the projectile to completely stop moving, including both the airborne phase and any subsequent sliding along the ground",
        "Only the time required to reach maximum height, not including the descent phase, since the projectile is technically no longer rising after that",
        "The duration the projectile spends moving in the horizontal direction only, not counting the time during which it moves vertically upward or down"
    ],
    16: [
        "The altitude at which the force of air resistance becomes exactly equal to the gravitational force, causing the projectile to stop accelerating",
        "The horizontal distance the projectile has covered when it reaches the midpoint of its flight, corresponding to exactly half the total range",
        "The initial height from which the projectile is launched, which determines the starting elevation above the ground for all trajectory calculations"
    ],
    17: [
        "The velocity at which a falling object strikes the ground upon impact, determined solely by the height from which the object was originally dropped",
        "The initial velocity of an object at the instant it is released from rest, before any gravitational acceleration has had the opportunity to act",
        "The speed of light in a vacuum, approximately 300 million meters per second, which represents the ultimate speed limit in the physical universe"
    ],
    19: [
        "The horizontal part of the velocity vector, directed parallel to the ground and equal to v times the cosine of the launch angle from the horizontal",
        "The total speed of the projectile at any given moment, found by combining horizontal and vertical components using the Pythagorean theorem formula",
        "The velocity of the projectile specifically at maximum height, where the vertical component vanishes and only horizontal motion remains for the object"
    ],
    20: [
        "The velocity of the projectile at its maximum height, where only the vertical component exists and the horizontal velocity has dropped to zero",
        "The velocity of the projectile at the exact moment it lands on the ground, which depends on both the launch speed and the height of the trajectory",
        "The rate of change of the vertical velocity component over time, which equals the gravitational acceleration directed downward at all instants"
    ],
    21: [
        "2 s \u2014 using t = s divided by g gives t = 80 divided by 10 = 8, then taking the square root yields approximately 2 seconds fall time",
        "8 s \u2014 using t = s divided by g directly gives t = 80 divided by 10 = 8 seconds, treating the height and gravity as a simple ratio",
        "16 s \u2014 using t = 2s divided by g gives t = 160 divided by 10 = 16 seconds, doubling the height before dividing by gravitational acceleration"
    ],
    22: [
        "60 m \u2014 multiplying the horizontal velocity by the time to fall using t = h divided by g: t = 45/10 = 4.5 s, then 15 times 4 gives 60 m",
        "30 m \u2014 using the average velocity of 10 m/s multiplied by 3 seconds gives an approximate horizontal distance of 30 m from the cliff base",
        "15 m \u2014 the horizontal distance equals the initial horizontal velocity alone: 15 m/s taken as 15 meters regardless of the time of flight"
    ],
    23: [
        "433 m \u2014 using R = u squared times sin theta divided by g: 2500 times sin 30 divided by 10 = 2500 times 0.5 / 10 = 125 then doubled = 433 m approx",
        "125 m \u2014 using R = u squared times sin theta divided by g: 2500 times 0.5 divided by 10 = 125 m, using sin 30 instead of sin 60 in the formula",
        "250 m \u2014 using R = u squared divided by g directly without the sine factor: 2500 divided by 10 = 250 m, omitting the angular dependence entirely"
    ],
    25: [
        "The package falls in a perfectly straight line directly below the point where it was dropped, with no horizontal motion after leaving the aircraft",
        "The package curves backward relative to the plane due to the effect of air resistance, landing behind the point directly below the drop location",
        "The package follows a circular arc through the air, curving around in a semicircle before reaching the ground at a point near the drop position"
    ],
    26: [
        "The 25 degree projectile travels farther because a lower launch angle gives a greater horizontal velocity component and therefore a longer total range",
        "The 65 degree projectile travels farther because a steeper launch angle keeps the projectile in the air longer and gives it more time to cover ground",
        "Cannot determine the relative ranges without knowing the actual numerical value of the launch speed, since the range depends on speed as well as angle"
    ],
    27: [
        "The hammer takes exactly the same amount of time on both the Moon and Earth, because the drop height is the same and height alone determines fall time",
        "About 6 times longer on the Moon \u2014 dividing Earth's gravity by the Moon's gravity gives 9.8/1.6 = 6.1, so the time ratio is approximately 6 to 1",
        "Shorter on the Moon because the hammer weighs less, and lighter objects fall more quickly since there is less gravitational force resisting their motion"
    ],
    28: [
        "H = 5 m and T = 2 s \u2014 using the total speed rather than the vertical component: H = u squared over 2g = 400/20 = 20 then halved gives about 5 m",
        "H = 10 m and T = 2 s \u2014 using T = 2u/g with the full speed: T = 2 times 20 / 10 = 4, then halved for symmetry gives T = 2 s with H = 10 m",
        "H = 20 m and T = 4 s \u2014 using the full launch speed for both: H = u squared / 2g = 400/20 = 20 m, and T = 2u/g = 40/10 = 4 s total flight"
    ],
    29: [
        "5 m \u2014 using horizontal distance = v times h divided by g gives 10 times 20 / 10 = 20, then halved for the horizontal component yields 5 meters",
        "10 m \u2014 the horizontal distance equals the exit speed in m/s converted directly to meters, since speed and distance share the same numerical value",
        "40 m \u2014 using distance = v times t with t = h / g: t = 20/10 = 2 times 2 = 4 s, then horizontal distance = 10 times 4 = 40 m from the base"
    ],
    30: [
        "Yes the range formula always works for any projectile motion scenario regardless of launch and landing heights or the presence of external forces",
        "No the range formula only works when the launch angle is exactly 45 degrees because that is the only angle where the sine function gives maximum range",
        "Yes the formula works here as long as you add the table height to the calculated range, since the extra elevation simply extends the horizontal distance"
    ]
}

fix_file('content_data/PhysicsLessons/Unit2/Lesson2.5_Quiz.json', fixes)
