import json, sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    3: [
        "0 N \u2014 walls are rigid structures that cannot push, so no reaction force is generated",
        "100 N \u2014 the wall pushes back twice as hard to compensate for its rigidity",
        "25 N \u2014 only half the force is returned because the wall absorbs the other half"
    ]
}

fix_file('content_data/PhysicsLessons/Unit3/Lesson3.4_Quiz.json', fixes)
