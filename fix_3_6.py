import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    1: [
        "The color and visual appearance of the surface, because darker or painted surfaces generate more friction than lighter-colored surfaces at the molecular level",
        "Air molecules pushing against the surfaces and creating a thin layer of resistance between them, since atmospheric pressure is the primary cause of surface friction",
        "Gravity pulling the two objects together with a force proportional to their combined masses, since gravitational attraction is the fundamental source of all friction"
    ],
    2: [
        "Static friction only exists on inclined surfaces and not on flat horizontal surfaces, because only the angle of an incline can create enough frictional resistance force",
        "Static friction and kinetic friction are exactly the same physical phenomenon described by identical coefficients, with no measurable difference in their force values",
        "Kinetic friction is always greater than static friction for any pair of surfaces in contact, because objects already in motion experience stronger resistance forces"
    ],
    6: [
        "The object weighs more on steeper inclines because gravity is compressed into a smaller surface area, increasing the effective force per unit area on the object",
        "The gravitational acceleration is stronger on steeper inclines because the angle amplifies the gravitational field strength acting on objects placed on the surface",
        "Steeper inclines have more friction between the surfaces, because the increased slope causes greater surface deformation that produces more resistance to sliding"
    ],
    7: [
        "86.6 N \u2014 N = mg sin theta = 50 times sin30 degrees = 50 times 0.5 = 25, then doubled to account for the incline factor giving approximately 86.6 N normal force",
        "50 N \u2014 N = mg = 50 N, because the normal force always equals the full weight of the object regardless of the angle of inclination of the surface",
        "25 N \u2014 N = mg sin theta = 50 times sin30 degrees = 50 times 0.5 = 25 N, using the sine component instead of the cosine for the perpendicular direction"
    ],
    8: [
        "Only in zero gravity environments can the normal force exceed the weight, since without gravity the surface has no baseline force to compare against for the object",
        "No the normal force is always strictly less than the weight of the object, because surfaces can only partially support the gravitational force pressing the object down",
        "No the normal force always exactly equals the weight of the object in every situation, because the surface must precisely balance gravity and nothing more at all times"
    ],
    11: [
        "A force that is always exactly equal to the object's weight in all situations, regardless of the surface orientation, applied forces, or any vertical acceleration present",
        "A component of the gravitational force itself, since the normal force is simply the portion of gravity that acts perpendicular to the surface of contact between objects",
        "A friction force that acts perpendicular to the direction of motion, resisting any tendency for the object to move sideways along the surface during sliding motion"
    ],
    12: [
        "A perfectly vertical wall surface that has an inclination angle of exactly 90 degrees, forming a right angle with the horizontal ground surface beneath the object",
        "A perfectly horizontal floor surface with zero inclination angle, where the normal force equals the full weight of any object resting on its flat level surface",
        "Any curved surface such as a sphere, cylinder, or parabola, where the inclination angle varies continuously from one point to another along the curvature path"
    ],
    13: [
        "The angle of friction between the surfaces, defined as the arctangent of the coefficient of kinetic friction for the materials in contact on the inclined surface",
        "The angle between the applied pushing force and the surface of the incline, which determines how much of the applied force contributes to motion along the slope",
        "The angle between the object and the vertical direction, which is the complement of the inclination angle and determines the perpendicular component of gravity"
    ],
    14: [
        "mg costheta, which is the component of gravitational force directed perpendicular to the incline surface and balanced by the normal force at the contact point",
        "The normal force that the surface exerts on the object, which acts perpendicular to the incline surface and prevents the object from falling through the material",
        "The total weight of the object (mg), directed straight downward, which acts on the object regardless of the surface angle or any other forces applied to it"
    ],
    15: [
        "mg sintheta, which is the component directed along the surface of the incline that tends to accelerate the object down the slope against any friction force present",
        "The force that pulls the object down the slope parallel to the surface, equal to mg sintheta, which is the driving force responsible for making objects slide down",
        "The friction force acting on the incline surface, directed opposite to the motion or tendency of motion, with magnitude equal to the friction coefficient times normal force"
    ],
    16: [
        "Always exactly 45 degrees for any combination of materials and surfaces, since the critical angle is a universal constant that does not depend on surface properties",
        "The angle at which the object launches off the incline surface and becomes airborne, losing contact with the ramp and entering projectile motion through the air",
        "The angle at which the normal force becomes exactly zero, which only occurs at 90 degrees when the surface is perfectly vertical and provides no perpendicular support"
    ],
    17: [
        "The gradual physical breakdown and deterioration of an object over extended time due to environmental exposure, corrosion, fatigue, and other degradation processes",
        "The physical process of dividing an object's mass into separate smaller parts, distributing the material evenly among multiple pieces for easier handling and transport",
        "The procedure of measuring an object's weight on different planets to determine how gravitational field strength varies across different locations in the solar system"
    ],
    18: [
        "A velocity-time graph that shows how the speed of the object changes as it moves along the incline surface, with slope representing the acceleration due to gravity",
        "A bird's-eye photograph of the incline taken from directly above, showing the spatial layout of the ramp and the positions of all objects on its surface from overhead",
        "A diagram that shows all objects present on the incline simultaneously, including the ramp structure itself, any pulleys, ropes, and the surrounding environment"
    ],
    19: [
        "The angle of the incline measured in degrees or radians, which determines how steeply the surface is tilted relative to the horizontal ground reference plane",
        "The normal force divided by the total weight of the object, giving a dimensionless ratio that characterizes the perpendicular force balance on the incline surface",
        "The coefficient of friction of the incline surface material, which characterizes how rough or smooth the surface is and determines the maximum friction force available"
    ],
    20: [
        "An object that has reached the bottom of the incline after sliding the entire length, completing its journey from the top starting position to the ground level below",
        "An object that is sliding down the incline at constant velocity, experiencing equal gravitational pull and friction force while maintaining a steady nonzero speed",
        "Any object placed anywhere on an incline regardless of the forces acting on it, since merely being on a tilted surface qualifies the object as being in equilibrium"
    ],
    21: [
        "10 m/s squared \u2014 a = g = 10 m/s squared, because on any frictionless incline the full gravitational acceleration acts on the object regardless of the incline angle",
        "8.66 m/s squared \u2014 a = g costheta = 10 times cos30 = 10 times 0.866 = 8.66 m/s squared, using the cosine rather than the sine for the parallel component",
        "0 m/s squared \u2014 without friction the block remains stationary because there is no friction force available to push the block down the slope surface"
    ],
    22: [
        "7.07 m/s squared \u2014 using a = g sintheta only: a = 10 times sin45 = 10 times 0.707 = 7.07 m/s squared, ignoring the friction contribution to the net force",
        "10 m/s squared \u2014 the acceleration equals g = 10 m/s squared because on a 45 degree incline the full gravitational acceleration acts along the slope surface",
        "2.12 m/s squared \u2014 using a = g times mu costheta: a = 10 times 0.3 times 0.707 = 2.12 m/s squared, using only the friction component of the total force"
    ],
    23: [
        "141 N \u2014 using F = mg costheta: F = 150 times cos20 = 150 times 0.94 = 141 N, because the perpendicular component determines the force needed to push up the slope",
        "150 N \u2014 using F = mg = 150 N, because the full weight must be overcome to push the box up any incline regardless of the angle of the ramp surface",
        "25 N \u2014 using F = mg/number of incline degrees: F = 150/20 = 7.5 then adjusted to approximately 25 N based on the trigonometric correction factor"
    ],
    24: [
        "0.57 \u2014 using mu = sintheta = sin35 = 0.574, because the friction coefficient equals the sine of the incline angle for objects sliding at constant velocity",
        "0.35 \u2014 using mu = theta/100 = 35/100 = 0.35, because the coefficient of kinetic friction is found by dividing the angle in degrees by one hundred",
        "1.00 \u2014 using mu = sintheta + costheta = 0.574 + 0.819 = 1.39 rounded to 1.00, because both trigonometric components contribute to the friction coefficient"
    ],
    25: [
        "0.22 \u2014 using mu = theta/100 = 22/100 = 0.22, because the coefficient of static friction is found by dividing the critical angle in degrees by one hundred",
        "0.50 \u2014 using mu = sin(22) + cos(22)/2 = 0.375 + 0.463/2 = 0.5, because both sine and cosine contribute equally to the coefficient of static friction",
        "0.38 \u2014 using mu = sin(22 degrees) = 0.375 rounded to 0.38, because the coefficient equals the sine rather than the tangent of the critical sliding angle"
    ],
    26: [
        "1000 N total force applied at one end only, because gravity pulls the person toward the nearest support and all weight is transferred to that single support point",
        "500 N at each support \u2014 the full weight of 500 N is borne by each support independently, because each support must be capable of holding the person's entire weight",
        "125 N at each support \u2014 the weight is divided by four since there are two supports and the plank is four meters long, giving one quarter of the weight per support"
    ],
    27: [
        "Cannot determine without knowing the friction coefficients, because without friction information it is impossible to predict the direction of motion on any incline",
        "The system is in perfect equilibrium and neither block moves, because the forces from the incline and the hanging block always balance each other on frictionless surfaces",
        "The 5 kg block slides down the incline pulling the 3 kg block upward, because the heavier block on the incline always dominates the motion of the connected system"
    ],
    28: [
        "100 percent of the weight acts along the slope, because on any incline steeper than 45 degrees the entire gravitational force is redirected parallel to the surface",
        "cos60 = 0.5 so 50 percent of the weight acts along the slope, because the cosine component rather than the sine component determines the parallel gravity force",
        "tan60 approximately 1.73 so 173 percent of the weight acts along the slope, because the tangent function determines the effective gravity along any inclined surface"
    ],
    29: [
        "400 N \u2014 the force equals the full weight: F = mg = 40 times 10 = 400 N, because pushing up any incline requires overcoming the object's complete weight value",
        "103 N \u2014 the force equals mg sintheta alone: F = 400 times 0.259 = 103 N, because friction acts in the same direction as the push and helps move the box upward",
        "97 N \u2014 the force equals mg times (sintheta minus mu costheta) = 400 times (0.259 minus 0.242) = 6.6 rounded up to approximately 97 N for the upward push"
    ],
    30: [
        "Both blocks slide down their respective sides simultaneously, because on frictionless surfaces all objects always accelerate downward regardless of any connecting ropes",
        "The 2 kg block on the 30 degree side slides down because the lighter block always descends first, since less mass means less inertia and faster downward acceleration",
        "The system is in perfect equilibrium and neither block moves, because the rope connecting them ensures equal tension that balances all forces on both sides of the peak"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.6_Quiz.json', fixes)
