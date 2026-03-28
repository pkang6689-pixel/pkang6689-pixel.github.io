import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    3: [
        "Air resistance pushing inward on the car body as it moves through the turn",
        "The engine force propelling the car forward along its direction of travel",
        "Gravity pulling the car downward toward the center of the Earth's surface"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.7_Quiz.json', fixes)
