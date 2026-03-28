import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    16: [
        "The gravitational force that the Earth exerts on exactly one gram of matter, measured under standard conditions at sea level on the surface",
        "The gravitational weight of a one kilogram mass on Earth's surface, equaling approximately 9.8 newtons when measured with a calibrated spring scale",
        "The product of exactly 100 grams and 10 m/s squared of acceleration, which gives the approximate force of gravity acting on a small laboratory mass"
    ],
    19: [
        "The result of subtracting just the gravitational force and friction force from one another, excluding all other forces that may act on the object",
        "Any single individual force acting on an object by itself, without considering any of the other forces that may also be acting on the same object",
        "The largest individual force among all the forces present on the object, since the dominant force alone controls the direction and magnitude of acceleration"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.3_Quiz.json', fixes)
