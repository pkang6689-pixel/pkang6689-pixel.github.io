import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    1: [
        "The net force on an object equals its mass multiplied by its acceleration, describing how force produces proportional changes in an object's velocity over time",
        "For every action force there is an equal and opposite reaction force acting on a different object, as formalized in Newton's third law of interaction pairs",
        "Energy cannot be created or destroyed in an isolated system but can only be transformed from one form to another, conserving the total energy at all times"
    ],
    5: [
        "It speeds up over time due to the momentum stored inside it, because an object in motion naturally gains additional velocity even without an applied force",
        "It eventually comes to a complete stop after a certain time, because all moving objects naturally lose their velocity and return to a state of rest on any surface",
        "It gradually slows down over time, because objects naturally lose velocity even in the absence of friction due to the inherent dissipation of motion energy"
    ],
    12: [
        "The kinetic energy stored in a moving object due to its speed and mass, calculated as one-half times mass times velocity squared in the standard formula",
        "The frictional resistance between two surfaces in contact, which depends on the coefficient of friction and the normal force pressing the surfaces together",
        "A force that actively opposes an object's motion, pushing back against the direction of travel and gradually reducing the object's speed until it comes to rest"
    ],
    15: [
        "Forces that are all oriented perpendicular to each other, forming right angles at the point of application and creating a complex multi-directional force pattern",
        "A system containing exactly two forces of any magnitude and direction, since having precisely two forces is the defining characteristic of an unbalanced arrangement",
        "Forces in which one individual force is stronger in magnitude than the others, which always guarantees the presence of a nonzero net force on the object in question"
    ],
    16: [
        "Objects naturally accelerate on their own over time, building up speed spontaneously without requiring any external force to drive the increase in velocity",
        "Objects naturally move in circular paths unless straightened out by an applied force, since circular motion is the default state of all matter in the universe",
        "Everything in the universe naturally comes to rest eventually, because all motion gradually dies out on its own even when no retarding forces are present"
    ],
    19: [
        "A state where the forces acting on an object fluctuate rapidly in magnitude and direction, causing the object to vibrate or oscillate around a central position",
        "A state where an object accelerates uniformly under a constant net force, gaining equal amounts of velocity during each equal time interval of the motion period",
        "A state that can only be achieved in a perfect vacuum, since air molecules always prevent any real object from maintaining truly constant velocity in practice"
    ],
    20: [
        "A law stating that heavier objects always move slower than lighter ones under the same conditions, because mass and speed are inversely proportional at all times",
        "A law discovered by Albert Einstein as part of his theory of general relativity, describing how mass curves spacetime and affects the motion of nearby objects",
        "A principle that only applies to objects drifting in outer space far from gravitational fields, and has no relevance to the motion of objects on planetary surfaces"
    ],
    21: [
        "Newton's third law explains this trick \u2014 the cloth pushes the dishes upward with a reaction force that holds them in place while the cloth slides out horizontally",
        "The law of conservation of energy explains this \u2014 the kinetic energy of the cloth is fully absorbed by the dishes, leaving them with no energy to move sideways",
        "The law of gravity explains this \u2014 the gravitational force pressing the dishes against the table is much stronger than any horizontal pull from the sliding cloth"
    ],
    22: [
        "It accelerates away from the astronaut due to the residual air pressure inside the station, which pushes any unsupported objects toward the nearest wall or panel",
        "It immediately stops moving and remains frozen in the exact position where it was released, because objects in space have no momentum without active propulsion",
        "It falls to the floor of the station just like on Earth, because the station's artificial gravity generator pulls all objects downward toward the lower deck surface"
    ],
    23: [
        "Gravity shifts direction during the turn, pulling the book toward the right side of the car as the vehicle's orientation changes relative to the gravitational field",
        "The dashboard has too much friction in that direction, which grabs the book's surface and drags it sideways toward the right as the car executes its left turn",
        "A real rightward force pushes the book sideways across the dashboard, generated by the centripetal acceleration of the turning car acting directly on the object"
    ],
    25: [
        "Yes the first law is violated \u2014 since the satellite moves at constant speed it should continue in a perfectly straight line, but instead it curves around Earth",
        "Yes the first law is violated \u2014 constant speed always means zero net force, so the satellite should travel in a straight line rather than following a curved orbit",
        "No the first law is not violated \u2014 but only because objects in outer space do not follow Newton's laws at all, since those laws apply exclusively to terrestrial motion"
    ],
    26: [
        "It shows that ice surfaces have less gravitational pull than carpet surfaces, which is why objects appear to be lighter and move more freely when skating on ice",
        "It proves that Newton's first law only works on ice surfaces, since objects on other surfaces like carpet naturally come to rest without requiring any external force",
        "It demonstrates that heavier people always stop faster on any surface, because mass is the primary factor determining how quickly a person decelerates to rest"
    ],
    27: [
        "The penny is simply too heavy for the card to move it, since the gravitational force pressing the penny downward exceeds any horizontal force the card could exert",
        "The card actively pulls the penny downward into the glass as it slides away, using a lever-like mechanism to redirect the horizontal flicking force into a vertical drop",
        "Air pressure above the penny holds it firmly in place while the card is removed, because atmospheric pressure is strong enough to prevent any horizontal displacement"
    ],
    28: [
        "The spacecraft immediately comes to a complete stop as soon as the engine shuts off, because without active propulsion there is nothing to sustain the forward motion",
        "The spacecraft gradually slows down over time after the engine stops, because all moving objects naturally lose velocity and eventually return to a state of rest",
        "The spacecraft continues to accelerate even after the engine shuts off, because the momentum stored during the engine burn continues to push it forward indefinitely"
    ],
    29: [
        "The water evaporates due to the sudden acceleration of the train, because rapid velocity changes generate heat energy that raises the water temperature above boiling",
        "The water surface remains perfectly level throughout the entire acceleration event, because water molecules are too heavy to be displaced by the train's forward motion",
        "The water sloshes forward toward the front of the container, because the train's forward acceleration pulls the water along with it in the same direction of travel"
    ],
    30: [
        "Car B has more friction between its tires and the road due to its greater weight, and this additional friction is the sole reason it is harder to push and accelerate",
        "Car A has better quality tires that grip the road more effectively, allowing the pushing force to be transmitted to the ground more efficiently for greater acceleration",
        "Car A has a stronger engine under its hood that supplements the pushing force, giving it an unfair advantage in acceleration despite receiving the same external push"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.2_Quiz.json', fixes)
