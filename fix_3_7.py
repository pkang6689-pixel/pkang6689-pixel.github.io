import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    1: [
        "Acceleration that acts in the direction of motion along the tangent, causing the object to speed up or slow down as it travels along a curved path",
        "Zero acceleration during circular motion, since objects moving at constant speed in a circle have no change in velocity and therefore no net acceleration",
        "Acceleration directed away from the center of a circular path, pushing the object outward and increasing the radius of the curved trajectory over time"
    ],
    2: [
        "a_c = r divided by v squared, where r is the radius of the circular path and v is the linear speed of the object moving along the circumference",
        "a_c = v times r, where the centripetal acceleration equals the product of the linear speed and the radius of the circular path being followed",
        "a_c = v divided by r, where the centripetal acceleration equals the linear speed divided by the radius of the circular path without squaring velocity"
    ],
    5: [
        "It stops immediately at the point of release, because without a centripetal force the object has no mechanism to continue any form of motion at all",
        "It continues moving in the same circular path, because the inertia of circular motion maintains the curved trajectory even after the centripetal force vanishes",
        "It moves radially outward from the center of the circle, accelerating away from the center point due to the residual centrifugal effect from the prior rotation"
    ],
    6: [
        "No, constant speed means there is no acceleration present, because acceleration requires a change in the numerical value of speed not just a direction change",
        "Only if the radius of the circular path changes during the motion, since constant radius combined with constant speed means zero acceleration at all times",
        "Only if there is friction acting on the object, because without a friction force there is no mechanism to produce acceleration during uniform circular motion"
    ],
    8: [
        "Yes it is a completely new type of force that exists only during circular motion and does not correspond to any known fundamental physical interaction between objects",
        "No it is the same as centrifugal force, since centripetal and centrifugal are just two different names for the identical outward-pointing force in circular motion",
        "Yes it is a fundamental force of nature alongside gravity, electromagnetism, and the nuclear forces, acting specifically on objects that follow curved trajectories"
    ],
    10: [
        "It doubles, since the centripetal force is directly proportional to speed and doubling the speed doubles the required inward force by the same factor",
        "It halves, because increasing the speed allows the object to maintain the circle with less centripetal force due to the greater momentum carrying it around",
        "It stays the same, because the radius has not changed and centripetal force depends only on the radius and mass, not on the speed of the circular motion"
    ],
    11: [
        "Motion in a straight line at constant speed, where the velocity remains entirely unchanged in both magnitude and direction throughout the entire duration",
        "Any curved motion of any kind, including elliptical, parabolic, and hyperbolic paths, since all curved trajectories qualify as uniform circular motion in physics",
        "Motion in a circle with continuously increasing speed, where the object accelerates tangentially while also experiencing a radially inward centripetal acceleration"
    ],
    12: [
        "Acceleration directed tangent to the circular path at the point of interest, which causes the object to change its speed as it moves along the curved trajectory",
        "Acceleration that increases the speed of an object moving in a circle, acting along the direction of motion to continuously add kinetic energy to the system",
        "Acceleration directed radially outward from the center of the circle, pushing the object farther away from the center and increasing the radius of the path"
    ],
    13: [
        "The force that speeds up objects moving in a circle, acting along the direction of motion tangentially and increasing the kinetic energy of the rotating object",
        "A new fundamental force unique to circular motion that does not correspond to any other known force, existing as its own independent category in the force classification",
        "A force that acts outward from the center of the circular path, pushing the object away from the center and opposing the inward centripetal acceleration at all times"
    ],
    14: [
        "A real physical force that pushes objects outward during circular motion, produced by the rotation itself and acting through direct physical contact with the object",
        "Exactly the same force as centripetal force described using a different name, since both terms refer to the identical inward-directed force in circular motion problems",
        "The Newton's third law reaction partner to the centripetal force, acting on the same object in the opposite direction and partially canceling the inward acceleration"
    ],
    15: [
        "The rate of change of angular acceleration with respect to time, representing how quickly the angular acceleration itself is changing during rotational motion",
        "The linear speed of an object moving in a circle, measured in meters per second along the tangent to the circular path at the point of interest on the circumference",
        "The centripetal acceleration expressed in angular units, which gives the same information as a_c = v squared over r but measured using radians instead of meters"
    ],
    17: [
        "The linear speed of the object measured in meters per second as it travels along the circumference of the circular path at any given instant during the motion",
        "The radius of the circular path measured in meters, representing the perpendicular distance from the center of the circle to the object moving along the circumference",
        "Exactly the same quantity as angular velocity, since frequency and angular velocity are two interchangeable names for the identical rotational measurement in physics"
    ],
    18: [
        "Velocity directed toward the center of the circular path, pointing radially inward and responsible for maintaining the constant radius of the circular trajectory",
        "The rate at which the speed of the object changes over time, representing the tangential acceleration that speeds up or slows down the object along its curved path",
        "Velocity directed away from the center of the circular path, pointing radially outward and responsible for the apparent centrifugal effect observed in rotating frames"
    ],
    19: [
        "A curve on a perfectly flat and level road surface, where all centripetal force must be supplied entirely by friction between the tires and the road surface",
        "A curve with a special extra-grip friction coating applied to the road surface, designed to increase the maximum centripetal force available for turning vehicles",
        "A curve designed to be safe only at very slow speeds below 20 km/h, because the banking angle becomes dangerous and destabilizing at higher velocities"
    ],
    20: [
        "Circular motion at constant speed where only centripetal acceleration exists, and no tangential acceleration component is present at any point along the path",
        "Motion that follows a straight line rather than a circular arc, because the net force is zero and there is no centripetal acceleration to curve the trajectory",
        "Motion that follows an elliptical orbit rather than a perfect circle, because real orbits always have some eccentricity due to perturbations from nearby objects"
    ],
    21: [
        "1000 m/s squared \u2014 using a_c = v times r = 20 times 50 = 1000 m/s squared, because centripetal acceleration equals the product of velocity and radius",
        "0.4 m/s squared \u2014 using a_c = v divided by r = 20/50 = 0.4 m/s squared, because centripetal acceleration equals velocity divided by radius without squaring",
        "2.5 m/s squared \u2014 using a_c = r divided by v squared = 50/400 = 0.125 rounded to approximately 2.5 m/s squared by applying a correction factor for the radius"
    ],
    22: [
        "2 N \u2014 using T = mv/r = 0.5 times 4 / 1 = 2 N, because tension equals mass times velocity divided by the radius of the circular path without squaring speed",
        "32 N \u2014 using T = mv squared times r = 0.5 times 16 times 2 = 16 then doubled to 32 N, because the formula multiplies by radius rather than dividing by it",
        "4 N \u2014 using T = mv = 0.5 times 4 = 2 then doubled for the circular motion factor giving approximately 4 N, because centripetal force equals momentum divided by time"
    ],
    23: [
        "It doubles, because centripetal acceleration is directly proportional to the orbital radius, so doubling the radius doubles the required centripetal acceleration",
        "It halves, because centripetal acceleration equals v squared over r, and doubling the radius alone divides the acceleration by two for the same orbital speed value",
        "It stays the same, because the centripetal acceleration of a satellite depends only on the mass of the planet and is independent of the orbital radius or speed"
    ],
    24: [
        "The bucket creates a partial vacuum above the water surface that holds the water in place, preventing it from falling due to the suction effect of the low pressure",
        "Surface tension of the water molecules creates a strong cohesive film across the bucket opening that prevents any water from spilling even when the bucket inverts",
        "Centrifugal force pushes the water into the bucket from the inside, because centrifugal force is a real outward force that acts on objects during circular motion"
    ],
    25: [
        "10 m/s \u2014 using v = mu_s times g = 0.6 times 10 = 6, adjusted to approximately 10 m/s by including a radius correction factor for the flat curve geometry",
        "6 m/s \u2014 using v = mu_s times r = 0.6 times 100/10 = 6 m/s, because maximum speed equals the friction coefficient multiplied by the radius over gravity",
        "60 m/s \u2014 using v = mu_s times g times r = 0.6 times 10 times 100 = 600 then taking the square root and adding a factor to get approximately 60 m/s"
    ],
    26: [
        "12 m/s squared \u2014 using a_c = RPM times r = 120 times 0.3 divided by 3 = 12 m/s squared, because centripetal acceleration equals RPM times the radius scaled down",
        "360 m/s squared \u2014 using a_c = RPM times 2pi times r = 120 times 6.28 times 0.3 divided by some factor giving approximately 360 m/s squared centripetal acceleration",
        "0.3 m/s squared \u2014 using a_c = r = 0.3 m/s squared directly, because the centripetal acceleration numerically equals the radius when angular velocity is 1 radian per second"
    ],
    27: [
        "9.8 m/s \u2014 using v = g = 9.8 m/s, because the minimum speed at the top of a vertical circle always equals the gravitational acceleration expressed in speed units",
        "0 m/s \u2014 the minimum speed at the top is zero because the string can remain taut as long as gravity continues to act downward on the stone at every point in the circle",
        "4.4 m/s \u2014 using v = 2 times g times r = 2 times 9.8 times 0.8 = 15.68, then taking the square root to get approximately 4.0 which rounds up to 4.4 m/s"
    ],
    28: [
        "30 degrees \u2014 using theta = v divided by r = 25/200 = 0.125 then converted to degrees by multiplying by 240 to give approximately 30 degrees banking angle",
        "45 degrees \u2014 the optimal banking angle is always 45 degrees for any speed and radius combination, since 45 degrees maximizes the centripetal force component",
        "12.5 degrees \u2014 using theta = v divided by (r times g) = 25 / (200 times 10) = 0.0125 then converted to degrees by multiplying by 1000 to give 12.5 degrees"
    ],
    29: [
        "15 N \u2014 using F = m times r divided by T = 30 times 2 / 4 = 15 N, because centripetal force equals mass times radius divided by the period of revolution",
        "30 N \u2014 using F = m times g divided by 10 = 30 times 10 / 10 = 30 N, because centripetal force on a merry-go-round equals the gravitational weight of the child",
        "60 N \u2014 using F = m times v = 30 times 2 = 60 N, because the centripetal force equals the product of mass and the linear velocity at the child's position"
    ],
    30: [
        "About 1g \u2014 the centripetal acceleration in a washing machine drum is roughly equal to gravitational acceleration, producing a gentle force similar to normal weight",
        "About 40g \u2014 the centripetal acceleration is approximately 40 times gravitational acceleration, which is typical for household appliances with fast spinning motors",
        "About 10g \u2014 the centripetal acceleration is approximately 10 times gravitational acceleration, since most spinning drums produce a moderate centripetal force level"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.7_Quiz.json', fixes)
