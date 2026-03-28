import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    1: [
        "The equation F = ma, which relates the net force acting on an object to the product of its mass and the resulting acceleration it experiences",
        "The principle that energy can never be created or destroyed in any process, but can only be converted from one form to another within a closed system",
        "The principle that objects at rest will remain at rest and objects in motion stay in motion at constant velocity unless acted on by an external net force"
    ],
    5: [
        "Buoyancy created by the water's displaced volume lifts her body upward and forward, providing the propulsion needed for horizontal movement through the pool",
        "Her muscles directly push her body forward through the water by internal force generation, without any interaction between her limbs and the surrounding fluid",
        "The natural current and wave motion of the water carries her forward in the desired direction, independent of any forces her arms apply to the surrounding water"
    ],
    7: [
        "Newton's third law does not apply to this particular situation, because biological systems like horses and carts are too complex for the simple interaction law",
        "The cart does not actually pull back on the horse at all, because inanimate objects like carts cannot generate forces of their own against a living animal",
        "The horse's pull on the cart is actually larger in magnitude than the cart's pull back on the horse, which creates the net forward force for the system"
    ],
    9: [
        "Yes they are a third law pair because all balanced forces acting in opposite directions on a single object are automatically classified as Newton's third law pairs",
        "Yes they are a third law pair since the two forces are equal in magnitude and opposite in direction, which is the only requirement for being a third law pair",
        "No they are not a third law pair because they are different types of forces \u2014 gravity is a field force while the normal force is a contact force between surfaces"
    ],
    10: [
        "It pushes against the vacuum of space, because even empty space has enough substance for Newton's third law to produce a forward reaction force on the vehicle",
        "It cannot work in space at all, because rocket engines fundamentally require an atmosphere or solid ground to push against in order to generate forward thrust",
        "The solar wind provides a steady forward push that propels the spacecraft through the solar system, similar to how wind pushes a sailboat across the ocean"
    ],
    11: [
        "The principle that objects at rest stay at rest and objects in motion stay in motion unless acted on by an external net force, also called the law of inertia",
        "The principle that energy is conserved in all collisions and interactions, meaning the total energy before an event always equals the total energy after the event",
        "The principle that the net force on an object equals the product of its mass and acceleration, expressed by the mathematical equation F equals m times a"
    ],
    12: [
        "Two forces that are always gravitational in nature, because Newton's third law was originally formulated exclusively for the gravitational attraction between masses",
        "Two forces that cancel each other out when acting on the same object, resulting in zero net force and zero acceleration for that particular single object",
        "Two forces that combine additively to create motion, adding their magnitudes together to produce a larger resultant force that drives the object forward"
    ],
    13: [
        "The larger of the two forces in a Newton's third law interaction pair, since the action force is defined as whichever force has the greater numerical magnitude",
        "A force that can only be exerted by a living being such as a person or animal, since only biological organisms are capable of initiating an action force",
        "The force that always comes first in time before the corresponding reaction force follows, since there is always a measurable delay between the action and reaction"
    ],
    14: [
        "The gravitational force that the Earth exerts on a firearm, pulling it downward with a force equal to the weapon's mass multiplied by the gravitational acceleration",
        "The elastic restoring force produced by a spring when it returns to its natural equilibrium length after being stretched or compressed by an external applied force",
        "The forward motion of a projectile through the air after being launched, which is the initial kinematic effect of the launching force applied to the projectile"
    ],
    15: [
        "The gravitational pull of the Moon on a spacecraft passing through cislunar space, which varies inversely with the square of the distance between the two objects",
        "The drag force experienced by an airplane as it moves through the atmosphere, created by the friction and pressure of air molecules impacting the aircraft surfaces",
        "The total weight of a rocket sitting on the launch pad before ignition, equal to the entire mass of the rocket and fuel multiplied by the gravitational acceleration"
    ],
    16: [
        "A high-speed collision between two or more objects, where significant forces are exchanged during a brief contact period that alters each object's velocity",
        "A force that acts on only one object in complete isolation, without any corresponding force being exerted on any other object anywhere in the physical system",
        "Any event that involves motion of any kind, including rotation, translation, vibration, or oscillation of one or more objects within a defined spatial region"
    ],
    17: [
        "A force applied from outside the defined system boundary by an external agent, capable of changing the total momentum and kinetic energy of the entire system",
        "Any force whose magnitude is smaller than 10 newtons, since forces below this threshold are classified differently from larger forces in standard physics notation",
        "A gravitational force acting within the interior of a planet, directed toward the center of mass and responsible for compressing the planet's internal material"
    ],
    18: [
        "A force acting between two objects that are both contained within the defined system boundary, forming a Newton's third law pair that sums to zero internally",
        "Only the gravitational force, because gravity is the sole example of a force that originates from outside a system and can influence the system's total momentum",
        "A force that performs no work on the system regardless of the displacement, because its direction is always perpendicular to the motion of the system at every point"
    ],
    19: [
        "The direct reaction to gravity pulling the object downward, since the normal force is simply gravity's Newton's third law partner acting in the opposite direction",
        "A force that is always exactly equal to the weight of the object in every situation, regardless of whether the object is on a flat surface, incline, or accelerating",
        "A force that only acts in the horizontal direction along a surface, providing the friction needed to prevent objects from sliding sideways across the contact area"
    ],
    20: [
        "Forces that exist only after the collision has ended, arising from the deformation and rebound of the objects once they have separated from their initial contact",
        "The stronger or more massive object always exerts a greater force on the weaker object, because force depends on the mass and strength of the object producing it",
        "The lighter object always experiences a greater force during the collision, because less massive objects absorb more impact energy and therefore feel stronger forces"
    ],
    21: [
        "The truck exerts a much greater force on the car than the car exerts on the truck, because the truck has significantly more mass and is therefore much more powerful",
        "The heavier vehicle always experiences the greater impact force in any collision, because a larger mass means a larger force is required to change its velocity",
        "The car exerts a greater force on the truck than the truck exerts on the car, because the smaller object concentrates its force into a smaller area upon impact"
    ],
    22: [
        "Gravity reverses direction momentarily during the jump, pulling upward instead of downward for a brief instant that allows your body to leave the ground surface",
        "The surrounding air pushes you upward when you crouch and spring up, because compressing air beneath your body creates enough upward pressure to lift your weight",
        "Your muscles directly lift your body mass upward by generating internal forces, without any interaction between your feet and the ground being necessary at all"
    ],
    23: [
        "Both skaters move at the same speed because they push with equal force, and equal forces always produce equal speeds regardless of the masses of the objects involved",
        "Neither skater moves at all because the equal and opposite forces cancel each other out, resulting in zero net force on the system and zero motion for both skaters",
        "Skater A moves faster because A has more mass and therefore more momentum, which translates directly into a higher velocity when the two skaters push apart from each other"
    ],
    24: [
        "Reaction forces are always slightly smaller in magnitude than the corresponding action forces, which creates a small net force that allows objects to accelerate forward",
        "Reaction forces are slightly delayed in time after the action forces, and this brief temporal gap creates a window during which the object can accelerate before the reaction arrives",
        "The student is completely correct in their reasoning \u2014 since all forces truly do cancel in pairs, no object should ever be able to accelerate under any circumstances whatsoever"
    ],
    25: [
        "Nothing happens to the astronaut because the wrench is too light relative to her mass to produce any noticeable reaction force or resulting change in her velocity",
        "She also moves to the right in the same direction as the wrench, because both objects must travel in the same direction after the throwing interaction takes place",
        "She spins in place around her center of mass without translating in any direction, because throwing an object in space only produces rotational motion not linear motion"
    ],
    26: [
        "There are no third law pairs in this situation because the person is in static equilibrium, and Newton's third law only applies when objects are accelerating or moving",
        "There is only one third law pair involved: the person's weight pulling downward and the normal force from the scale pushing upward are the single action-reaction pair",
        "The scale pushing up and gravity pulling down is the only pair present, because contact forces and gravitational forces always form a third law pair when they are equal"
    ],
    27: [
        "The external air pressure from outside the balloon pushes it forward through the room, since atmospheric pressure is higher in front of the balloon than behind it",
        "Gravity pulls the air out of the balloon opening, and the downward stream of escaping air creates a horizontal deflection that propels the balloon through the room",
        "The balloon is filled with lighter-than-air helium gas, which creates buoyancy that lifts it upward and causes the erratic flying motion observed when released untied"
    ],
    28: [
        "Yes they are a third law pair \u2014 since the two forces are equal in magnitude and opposite in direction, they satisfy all the requirements for being a Newton's third law pair",
        "No they are not a third law pair \u2014 Newton's third law pairs only exist between objects that are in motion relative to each other, and the rope is currently stationary",
        "Yes \u2014 any two equal forces acting in opposite directions on any object or set of objects automatically qualify as a Newton's third law action-reaction pair by definition"
    ],
    29: [
        "No \u2014 Newton's third law does not apply to gravitational forces, since gravity is a field force that operates through empty space rather than through direct physical contact",
        "No \u2014 only large massive objects like planets and stars can exert gravitational forces, because small objects like apples do not have enough mass to generate any measurable pull",
        "Yes \u2014 but the apple pulls Earth upward with a much smaller force than 9.8 N, because the reaction force is proportional to the mass of the smaller object in the pair"
    ],
    30: [
        "The water does not really push back on the swimmer at all, because fluids cannot exert reaction forces the way solid surfaces can when pushed against by an object",
        "The swimmer pushes harder on the water than the water pushes back, creating an imbalance that allows the swimmer to accelerate forward through the pool during each stroke",
        "Newton's third law does not apply to fluid interactions like swimming, because the law was formulated only for solid objects in direct contact with other solid surfaces"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.4_Quiz.json', fixes)
