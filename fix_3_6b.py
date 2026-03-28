import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    3: [
        "mg costheta, which is the weight component directed perpendicular to the incline surface",
        "mg, the full weight of the object acting straight downward toward the center of the Earth",
        "mg tantheta, which is the ratio of the parallel and perpendicular gravity components"
    ],
    4: [
        "mg tantheta, which gives the ratio of parallel to perpendicular weight components on the slope",
        "mg, the full weight of the object since the normal force always equals the total gravitational force",
        "mg sintheta, which is the component of gravity directed parallel along the surface of the incline"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.6_Quiz.json', fixes)
