import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    4: [
        "0 km/h \u2014 the two velocities cancel each other out since one is positive and the other is negative, giving a net relative velocity of zero",
        "50 km/h \u2014 the relative velocity equals just one car's speed, because the other car's contribution is irrelevant when they move in opposite directions",
        "25 km/h \u2014 the relative velocity is the average of the two speeds: (50 + 50) / 2 = 25 km/h, since averaging accounts for opposite directions"
    ],
    7: [
        "2 m/s \u2014 subtracting the river's speed from the boat's speed gives the net velocity: 5 minus 3 = 2 m/s relative to the ground observer on shore",
        "8 m/s \u2014 adding the two speeds directly gives the boat's total ground speed: 5 plus 3 = 8 m/s, since all velocities in the same system simply add",
        "5 m/s \u2014 the river current has no effect on the boat's ground speed because the boat's engine power alone determines its velocity relative to the bank"
    ],
    8: [
        "15 m/s \u2014 only half the ball's speed adds to the car's speed, since the ball is inside the car and is partially shielded from the full velocity effect",
        "10 m/s \u2014 the ball's speed relative to the ground equals just its throwing speed, because the car's velocity has no effect on a thrown object once released",
        "20 m/s \u2014 the ball's ground speed equals only the car's speed, since the throwing velocity is measured relative to the car and cancels out in the ground frame"
    ],
    10: [
        "The ball moves backward relative to the car, because the wind resistance pushes it behind the passenger's release point as the car drives forward",
        "The ball goes straight up and comes straight down, because the vertical throw direction does not change regardless of which reference frame is used",
        "The ball moves only in the horizontal direction with the car, never rising or falling, because the car's forward velocity overwhelms the vertical throw"
    ],
    11: [
        "The outermost physical boundary of an experimental setup, defining the region within which measurements can be reliably taken by laboratory instruments",
        "A standardized unit of measurement agreed upon by international scientific bodies for expressing the magnitude of displacement, velocity, and other quantities",
        "A rigid wooden or metal frame used in physics laboratories to hold measuring instruments, sensors, and other experimental equipment securely in place"
    ],
    12: [
        "The velocity of an object measured exclusively relative to the ground, since the ground is the only valid reference for reporting any velocity measurement",
        "The maximum speed an object can reach under the given conditions, representing the upper limit of its velocity regardless of the observer's reference frame",
        "The arithmetic mean of two objects' velocities divided by two, giving a single representative velocity for the pair of objects moving through the same region"
    ],
    13: [
        "Any reference frame that happens to be at rest at a given instant, regardless of whether it is accelerating, rotating, or experiencing other forms of motion",
        "A reference frame whose origin is centered at the Sun, since the Sun is the only truly stationary object in the solar system from a gravitational perspective",
        "A reference frame in which all objects always accelerate, because the frame itself provides a constant background acceleration to everything within its boundaries"
    ],
    14: [
        "A reference frame designed exclusively for analyzing motion in outer space, where gravitational effects are negligible and objects float without external forces",
        "A reference frame that is permanently at rest relative to the fixed stars and cannot translate or move under any circumstances within the physical universe",
        "A reference frame in which no objects are ever observed to be moving, because the frame definition requires that all motion within it equals exactly zero"
    ],
    15: [
        "A mathematical method of rotating coordinate axes to align them with the direction of an object's velocity, simplifying the equations of motion in that frame",
        "A transformation technique used exclusively by Galileo during his 17th-century experiments and no longer applicable to any modern physics calculations today",
        "The standard conversion formulas used to translate between Celsius and Fahrenheit temperature scales, named after Galileo for his early thermometer innovations"
    ],
    16: [
        "A force that was measured incorrectly by a scientist due to equipment calibration errors, leading to a reported value that does not match the actual force present",
        "A force that is completely imaginary and produces absolutely no observable effects whatsoever on any object, existing only as a theoretical concept in textbooks",
        "Any force that has a very small magnitude compared to the dominant forces in a system, making it negligible for practical calculations but still physically real"
    ],
    17: [
        "A formula that is valid only for rotating reference frames, relating the angular velocities of objects spinning at different rates around a common central axis",
        "The equation used to calculate the velocity an object gains due to gravitational acceleration, relating drop height to the final speed upon reaching the ground",
        "An equation specifically for adding position vectors rather than velocities, connecting the displacement of one object to the position of another in the same frame"
    ],
    18: [
        "A camera pointed at a moving object that records visual data, but whose measurements do not constitute valid physical observations from any reference frame",
        "Only a human being physically watching an experiment in person, since instruments and automated sensors cannot qualify as observers in the physics definition",
        "A scientist who remains entirely passive and does not participate in or interact with any experiments, simply recording outcomes from outside the laboratory space"
    ],
    19: [
        "A principle that applies only to the behavior of light and electromagnetic waves, having no relevance to the mechanics of material objects or their interactions",
        "The idea that only measurements made from Earth's surface reference frame are physically valid, and all other reference frames produce incorrect or distorted results",
        "The general philosophical statement that everything in physics is relative, meaning no measurement of any kind has an absolute value under any possible conditions"
    ],
    20: [
        "Simply adding the scalar speeds of two objects together without considering direction, giving the total combined speed regardless of which frame is being used",
        "Breaking a single velocity vector into its horizontal and vertical components using trigonometry, which is also called vector decomposition or resolution of vectors",
        "Calculating the arithmetic average velocity of a group of objects by summing their individual velocities and dividing by the total number of objects in the group"
    ],
    21: [
        "200 km/h \u2014 the plane's airspeed alone determines its ground speed, since wind only affects direction and cannot change the actual magnitude of the velocity",
        "250 km/h \u2014 adding the two speeds directly: 200 + 50 = 250 km/h, because the wind and the plane both contribute their full speeds to the resultant velocity",
        "150 km/h \u2014 subtracting the wind speed from the airspeed: 200 minus 50 = 150 km/h, because the crosswind partially slows the plane's forward ground progress"
    ],
    22: [
        "arctan(2/1.5) is approximately 53.1 degrees downstream \u2014 dividing the swimmer's speed by the river speed gives the correct angle from the intended crossing path",
        "0 degrees \u2014 the swimmer goes straight across the river exactly as intended, because her swimming speed is greater than the current speed and she can overpower it",
        "90 degrees \u2014 the swimmer goes entirely downstream with no crossward progress, because the river current completely overwhelms her ability to swim perpendicular to it"
    ],
    23: [
        "140 km/h west \u2014 the relative velocity points in the direction of Train B, since the observer is on Train B and perceives Train A as approaching from the opposite side",
        "20 km/h east \u2014 subtracting the speeds gives 80 minus 60 = 20 km/h, since when objects move in opposite directions you subtract rather than add their velocities",
        "80 km/h east \u2014 the relative velocity equals just Train A's ground speed, because the observer's own motion does not affect how they perceive another object's velocity"
    ],
    24: [
        "Going with: your ground speed is 5 m/s forward; running back: your ground speed is 1 m/s backward, calculated as negative 3 plus 2 = negative 1 m/s in the walkway direction",
        "3 m/s forward in both cases \u2014 the walkway has no effect on your ground speed because your running speed alone determines how fast you move relative to the stationary ground",
        "5 m/s forward in both cases \u2014 the walkway adds 2 m/s in both directions since it always pushes you forward regardless of which way you are running on its surface"
    ],
    25: [
        "7 m/s directly north \u2014 adding the speeds gives 4 + 3 = 7 m/s, and since Boat A moves north the relative velocity must also point in the northward direction only",
        "5 m/s in the northeast direction \u2014 combining the perpendicular velocities gives magnitude 5 m/s, but the direction should be northeast since both boats head that way",
        "1 m/s in the northeast direction \u2014 subtracting the speeds gives 4 minus 3 = 1 m/s, since relative velocity always involves simple subtraction of the speed magnitudes"
    ],
    26: [
        "45 degrees from vertical \u2014 the tilt angle is always 45 degrees for any combination of rain speed and running speed, since the rain always appears to fall diagonally at this angle",
        "Straight up with no tilt needed \u2014 rain falls vertically regardless of your motion, so the umbrella should be held perfectly upright to provide maximum overhead coverage",
        "arctan(8/6) is approximately 53.1 degrees from vertical \u2014 dividing the rain speed by your running speed gives the correct angle between the vertical and the apparent path"
    ],
    27: [
        "The ball falls straight down in the platform observer's view as well, because gravity pulls objects vertically regardless of which reference frame is used to observe them",
        "The ball curves backward relative to the train's direction, since the platform observer sees air resistance push the ball behind the point where it was released from rest",
        "The ball moves only in the horizontal direction with no vertical drop, since the train's forward velocity transfers entirely to the ball and overwhelms gravitational pull"
    ],
    28: [
        "40 m/s west \u2014 the package immediately reverses direction upon release, moving opposite to the helicopter because being dropped means all forward velocity is lost instantly",
        "0 m/s \u2014 the package starts from rest relative to the ground, because dropping it means no velocity was added and objects at rest in a moving vehicle have zero ground speed",
        "40 m/s downward \u2014 the package immediately acquires a downward velocity equal to the helicopter's horizontal speed, since the velocity direction shifts by 90 degrees upon drop"
    ],
    29: [
        "C measures 30 m/s and B measures 10 m/s \u2014 subtracting B's speed from A's speed: 30 minus 20 = 10 m/s, since same-direction subtraction applies for opposite travel",
        "Both C and B measure exactly 30 m/s \u2014 the speed of Car A is an absolute quantity that does not depend on the reference frame of the person making the measurement",
        "C measures 50 m/s and B measures 30 m/s \u2014 the parked observer sees the higher relative speed while the moving observer sees the basic ground speed of Car A only"
    ],
    30: [
        "80 m/s \u2014 adding the projectile's thrown speed to the villain's car speed: 30 + 50 = 80 m/s approach speed as seen from the villain's reference frame",
        "30 m/s \u2014 the projectile's approach speed equals its throwing speed, since the hero's car velocity cancels out from the villain's perspective in this reference frame",
        "5 m/s \u2014 subtracting the two car speeds gives the approach rate: 50 minus 45 = 5 m/s, since the projectile moves with the relative gap between the two vehicles"
    ]
}

fix_file('content_data/PhysicsLessons/Unit2/Lesson2.6_Quiz.json', fixes)
