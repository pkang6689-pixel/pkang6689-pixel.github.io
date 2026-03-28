import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    2: [
        "A real force that is very weak compared to other forces in the system, but still originates from a physical interaction between two real objects in contact",
        "A force that only acts on objects lighter than one kilogram, since heavier objects have too much inertia to be affected by fictitious force interactions",
        "A force that only appears in theoretical physics textbooks but never manifests during actual real-world experiments or practical engineering applications"
    ],
    3: [
        "Air pressure building up inside the car cabin as it accelerates forward, creating a backward-directed pressure gradient that pushes occupants toward the rear",
        "A real backward force transmitted from the engine through the car frame, pushing the passengers in the opposite direction of the vehicle's forward acceleration",
        "Gravity shifting direction temporarily during the acceleration event, tilting slightly backward relative to the car's floor and pulling passengers toward the rear"
    ],
    4: [
        "The Newton's third law reaction partner to the centripetal force, acting on the same object but in the opposite radially outward direction from the center",
        "A fundamental force of nature alongside gravity and electromagnetism, classified as one of the four basic physical interactions governing all matter and energy",
        "A real physical contact force that pushes objects outward through direct molecular interaction between the spinning surface and the object placed upon it"
    ],
    6: [
        "Yes all forces without exception obey Newton's third law, including pseudo-forces, because the third law is a universal principle that applies in every reference frame",
        "Yes the reaction partner exists in the inertial reference frame, because every pseudo-force has a corresponding real reaction force acting on the accelerating frame itself",
        "Only in some special cases where the non-inertial frame has constant acceleration, because the third law applies partially during uniform non-inertial acceleration only"
    ],
    7: [
        "Double your normal weight, because the downward acceleration adds to the gravitational pull and creates a stronger net force pressing you into the elevator floor",
        "Half your normal weight, because the downward acceleration partially cancels the gravitational force, reducing the normal force to approximately half of your true weight",
        "Your normal weight unchanged, because the elevator's acceleration has no effect on the reading of a properly calibrated scale regardless of the direction of motion"
    ],
    9: [
        "Because they are very small in magnitude compared to real forces and therefore negligible in most practical calculations and engineering design applications",
        "Because they cannot be measured by any instrument or detected by any sensor, existing purely as conceptual tools that produce no observable physical effects",
        "Because they only exist in theoretical models and never manifest in actual reality, having been disproven by modern experiments that show they do not occur"
    ],
    11: [
        "A frame that is attached to a very large massive object like a planet or star, since only large objects can serve as valid non-inertial reference frame anchors",
        "A frame inside which no experiments of any kind can be validly performed, because the frame's motion corrupts all measurements taken within its boundaries",
        "A frame that moves at perfectly constant velocity relative to all other frames, experiencing no acceleration and fully obeying Newton's laws in their standard form"
    ],
    12: [
        "A very weak but real force that originates from an actual physical interaction between two objects, having a definite third law partner and a clear physical source",
        "Any force that proves difficult to measure accurately in a laboratory setting, regardless of whether it has a real physical source or obeys Newton's third law",
        "A force that acts exclusively on imaginary or hypothetical objects that do not physically exist, and therefore has no relevance to any real experimental situation"
    ],
    13: [
        "A force that operates exclusively in outer space environments where there is no atmosphere, since centrifugal effects cannot occur in the presence of air molecules",
        "A real physical force that genuinely pushes objects outward during circular motion through direct contact, originating from the spinning surface beneath the object",
        "Exactly the same force as centripetal force described using a different name, since both terms refer to the identical center-directed inward force in every situation"
    ],
    14: [
        "A force that only exists at the equator of a rotating body and has zero magnitude at every other latitude, including the poles and all intermediate positions",
        "The gravitational force acting on objects that are spinning about their own internal axis, which increases proportionally with the rate of the object's self-rotation",
        "A force that causes objects to rotate faster and faster over time by adding angular momentum through direct energy transfer from the rotating reference frame itself"
    ],
    15: [
        "The principle that all pseudo-forces are always equal in magnitude to each other regardless of the reference frame, mass of the object, or acceleration involved",
        "The principle that mass always equals weight in every reference frame, making the two quantities perfectly interchangeable under all physical conditions and locations",
        "The principle that all reference frames are equivalent for all experiments, meaning every measurement yields identical results no matter which frame the observer uses"
    ],
    16: [
        "Always exactly equal to the true gravitational weight mg regardless of any acceleration, since scales always display the correct gravitational force at all times",
        "The weight of an object measured on a different planet, which differs from the Earth value solely because of the different gravitational field strength at the surface",
        "The total mass of an object measured in kilograms, which is an intrinsic property of matter that does not change with location, acceleration, or reference frame"
    ],
    17: [
        "The stretching and compressing of extended objects by tidal forces from a nearby gravitational source, also known as spaghettification in extreme gravitational fields",
        "The bending of light rays as they pass through a strong gravitational field near a massive object, predicted by Einstein's general theory of relativity in 1915",
        "The slow wobble of Earth's rotational axis over a 26000-year cycle, caused by the gravitational torques exerted by the Sun and Moon on Earth's equatorial bulge"
    ],
    18: [
        "Quantities that can only be measured by a single specific observer in one particular reference frame, and are completely inaccessible to all other observers",
        "Quantities whose measured values remain exactly the same regardless of which reference frame the observer uses, such as mass, electric charge, and temperature",
        "Quantities that have no units of measurement and are expressed as pure dimensionless numbers, making them independent of any particular measurement system"
    ],
    19: [
        "The centrifugal force experienced by the Moon as it orbits the Earth, pushing it outward and balancing the gravitational attraction to maintain a stable orbit",
        "A pseudo-force that exists only in rotating reference frames and has no connection to gravitational fields, gradients, or variations in field strength across objects",
        "The force that ocean tides exert on a ship floating on the water surface, pushing the vessel up and down as the water level changes with the tidal cycle"
    ],
    20: [
        "F = ma applied in a standard inertial reference frame, where no pseudo-forces are needed and Newton's second law works in its simplest and most familiar form",
        "F = negative k times x for springs undergoing simple harmonic oscillation, describing the restoring force that pulls a compressed or stretched spring back to equilibrium",
        "F = mv squared divided by r for circular motion, giving the centripetal force needed to keep an object moving along a circular path of constant radius at constant speed"
    ],
    21: [
        "1400 N \u2014 the scale reads N = 2mg = 2 times 70 times 10 = 1400 N, because upward acceleration always doubles the apparent weight shown on the scale reading",
        "490 N \u2014 the scale reads N = m(g minus a) = 70 times (10 minus 3) = 490 N, because the upward acceleration subtracts from gravity rather than adding to it",
        "700 N \u2014 the scale reads N = mg = 70 times 10 = 700 N, because the elevator's acceleration has no effect on the weight displayed by a properly calibrated scale"
    ],
    22: [
        "Only the inertial frame perspective is physically correct and valid, because non-inertial frame descriptions are inherently wrong and always give incorrect predictions",
        "Both frames observe the same thing: the ball is pushed forward by the braking force transmitted through the dashboard surface, which acts identically in both frames",
        "The ball rolls forward due to gravity alone in both frames, because the braking event tilts the effective gravitational field forward inside the decelerating vehicle"
    ],
    23: [
        "5 degrees from vertical \u2014 using theta = a in degrees gives theta = 5 degrees backward, because the angle in degrees always equals the numerical acceleration value",
        "45 degrees from vertical \u2014 using theta = a divided by g times 90 gives 5/10 times 90 = 45 degrees, because the angle scales linearly up to a maximum of 90 degrees",
        "90 degrees from vertical \u2014 the plumb bob hangs horizontally whenever the train accelerates, because any forward acceleration causes the bob to point straight backward"
    ],
    24: [
        "0.1 rad/s \u2014 using omega = g divided by r = 9.8/100 = 0.098 rounded to 0.1 rad/s, because the rotation rate equals gravity divided by the station radius directly",
        "1 RPM \u2014 using RPM = g times r = 9.8 times 100 / 1000 = 0.98 rounded to 1 RPM, because the rotation rate is found from the product of gravity and radius",
        "10 RPM \u2014 using RPM = g = 9.8 rounded to 10, because the required rotation rate in RPM always numerically equals the gravitational acceleration being simulated"
    ],
    25: [
        "A real physical force from the seat cushion pushes the person to the right through direct contact, since the seat material actively generates a sideways pushing force",
        "The car door pushes the person inward toward the center of the turn, because the door's contact force acts centripetally on the passenger during every turning maneuver",
        "Gravity shifts its direction during turns to point sideways instead of downward, temporarily pulling the person to the right until the car completes its left turn"
    ],
    26: [
        "The ball does not deflect at all in any direction, because the Coriolis force is too small to produce any observable effect on objects moving on a turntable surface",
        "To the left or west \u2014 in a counterclockwise rotating frame the Coriolis force deflects all northward-moving objects to the left of their initial direction of travel",
        "Straight up off the surface of the turntable, because the Coriolis force acts perpendicular to both the velocity and the rotation axis in the vertical direction only"
    ],
    27: [
        "The ball is held in place by the air pressure inside the sealed spacecraft cabin, which creates an equilibrium zone that prevents any object from drifting in any direction",
        "There is no gravity present in outer space at the spacecraft's altitude, so the ball simply has no force acting on it and naturally remains stationary beside the astronaut",
        "The ball has no mass while inside the spacecraft because objects lose their mass in microgravity environments, making them immune to all forces including gravity"
    ],
    28: [
        "There is no difference between the equator and poles, because Earth's rotation has no measurable effect on the apparent weight of objects at any latitude on the surface",
        "Apparent weight drops to exactly zero at the equator because the centrifugal pseudo-force completely cancels gravity, making all objects weightless at equatorial latitudes",
        "Apparent weight is actually greater at the equator than at the poles, because the centrifugal pseudo-force adds to gravity rather than opposing it at lower latitudes"
    ],
    29: [
        "The supplies deflect to the north, because the Coriolis force always pushes falling objects toward the nearest geographic pole in both hemispheres of the rotating Earth",
        "There is no measurable deflection of the falling supplies, because the Coriolis effect only acts on objects moving horizontally and has zero effect on vertically falling items",
        "The supplies deflect to the west, because falling objects in the Northern Hemisphere always drift westward due to the Coriolis force acting opposite to Earth's rotation"
    ],
    30: [
        "Gravity is stronger at greater heights above the road surface, pulling upper-deck passengers outward with more force during the turn than passengers closer to the ground",
        "The upper deck has less friction between the seats and passengers, allowing passengers to slide more easily and therefore feel a stronger sensation of being pushed outward",
        "The upper deck passengers experience greater centrifugal pseudo-force because they are farther from the center of the curve, since F = m times omega squared times r increases with larger r and greater height amplifies the tipping"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.8_Quiz.json', fixes)
