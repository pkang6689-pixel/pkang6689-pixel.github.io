import json
import sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    4: [
        "Only if the object has zero mass, because massless particles are the sole exception to the rule that speed must change for acceleration",
        "Only in outer space where there is no gravity, since gravitational fields prevent acceleration at constant speed under normal conditions",
        "No \u2014 maintaining a constant speed always guarantees the velocity is also constant, so no acceleration can occur in that situation"
    ],
    5: [
        "Any acceleration that carries a negative sign in the chosen coordinate system, regardless of whether the object speeds up or slows down",
        "A state of zero acceleration where the object maintains a perfectly constant velocity with no change in speed or direction at all",
        "Acceleration that always equals exactly negative 9.8 m/s squared, since that is the only value at which objects can decelerate on Earth"
    ],
    10: [
        "Only if the object has infinite mass, because extremely massive objects can maintain zero velocity while forces still produce acceleration",
        "No \u2014 whenever an object has zero velocity it must also have zero acceleration, since both quantities always equal zero simultaneously",
        "Only in a perfect vacuum where air resistance is absent, since air molecules prevent acceleration from existing without velocity present"
    ],
    12: [
        "Any acceleration value that is positive in sign, since only positive accelerations can remain constant while negative ones always fluctuate",
        "Acceleration whose magnitude steadily increases over time, growing larger and larger with each passing second as the object gains speed",
        "Acceleration that is always equal to exactly 9.8 m/s squared, because gravitational acceleration is the only type that remains constant"
    ],
    14: [
        "The descent of an object from a very high altitude through the atmosphere, where air resistance plays a significant role in its motion",
        "Motion of an object through space with absolutely no forces acting on it at all, including the complete absence of gravitational attraction",
        "Any motion in which an object moves in the downward direction, whether it is powered, thrown, dropped, or sliding along an inclined plane"
    ],
    15: [
        "A graph that only applies to situations with constant velocity, since changing velocities cannot be accurately represented on such a plot",
        "A diagram showing the direct mathematical relationship between the distance an object covers and its instantaneous speed at every point",
        "A graph that plots an object's position on the vertical axis against time on the horizontal axis, showing how location changes with time"
    ],
    17: [
        "Acceleration whose value is always negative throughout the entire motion, never reaching zero or becoming positive at any point in time",
        "An extremely large but constant acceleration that stays the same at every instant but simply has a very high numerical magnitude value",
        "Acceleration that can only exist during curved motion along a circular or elliptical path, and never occurs during straight-line travel"
    ],
    18: [
        "The maximum speed limit that any falling object can reach, beyond which no further increase in downward velocity is physically possible",
        "The gravitational force that Earth exerts on an object, measured in newtons and directly dependent on the mass of the object in question",
        "The weight of an object divided by its total volume, giving a density-like quantity that determines how quickly the object accelerates"
    ],
    19: [
        "The maximum acceleration that any mechanical system can achieve, representing the upper bound on how quickly velocity can ever change",
        "A sudden and complete stop in an object's motion, where velocity drops instantly to zero without any intermediate deceleration phase",
        "An error or uncertainty introduced during the measurement of acceleration, caused by imprecise instruments or incorrect timing methods"
    ],
    20: [
        "The fastest speed theoretically possible in the universe, representing an absolute upper limit that no material object can ever exceed",
        "The final velocity an object has at the exact moment of impact with the ground, determined solely by the height from which it was dropped",
        "The minimum launch velocity required for an object to escape Earth's atmosphere and enter outer space by overcoming gravitational pull"
    ],
    22: [
        "Approximately 40 m \u2014 using the simplified formula s = v times t with an estimated flight time of about 2 seconds gives 40 meters",
        "Approximately 200 m \u2014 using s = u squared divided by g without the factor of two gives 400 divided by 2 equals 200 meters height",
        "Approximately 10 m \u2014 using the formula s = u times t squared with t = 1 second gives half the initial velocity as the peak height"
    ],
    23: [
        "Cannot determine without knowing the position data, because calculating acceleration requires distance measurements not velocity and time",
        "Yes the acceleration is constant \u2014 the cyclist is always speeding up throughout both intervals, which by definition means uniform acceleration",
        "Yes the acceleration is constant \u2014 since both time intervals are exactly 4 seconds long, the rate of velocity change must be identical"
    ],
    25: [
        "150 m \u2014 using the formula s = u times t with stopping time t = 30/5 = 6 seconds: s = 30 times 6 = 180, adjusted for braking gives 150 m",
        "6 m \u2014 dividing the initial velocity by the deceleration gives the stopping time of 6 seconds, which also equals the stopping distance in meters",
        "45 m \u2014 using the formula s = half times u times t with t = 3 seconds: s = 0.5 times 30 times 3 = 45 m of total braking distance traveled"
    ],
    26: [
        "4 m/s upward \u2014 dividing the acceleration by the elapsed time gives 20 divided by 5 = 4 m/s as the final upward velocity of the rocket",
        "100 m/s downward \u2014 the magnitude is 100 m/s but directed downward because gravity opposes the upward thrust during the launch phase",
        "25 m/s upward \u2014 adding the acceleration and the time together gives 20 + 5 = 25 m/s as the approximate final velocity of the rocket"
    ],
    27: [
        "She experienced negative acceleration throughout the entire fall, decelerating from the moment she left the plane all the way until reaching the ground below",
        "Her acceleration remained constant at exactly 9.8 m/s squared the entire time she fell, since gravitational acceleration does not change with speed or altitude",
        "Her acceleration actually increased well beyond 9.8 m/s squared as she continued to fall, because falling objects always accelerate faster the longer they fall"
    ],
    29: [
        "Total displacement is 30 m \u2014 only the constant velocity phase contributes to displacement since the acceleration and deceleration phases cancel each other out completely",
        "Total displacement is 48 m \u2014 calculated as 9 m during acceleration using half times 2 times 9, plus 30 m at constant velocity, plus 9 m during deceleration phase",
        "Total displacement is 9 m \u2014 only the initial acceleration phase contributes any displacement since the constant velocity and deceleration phases produce no net motion"
    ]
}

fix_file('content_data/PhysicsLessons/Unit2/Lesson2.2_Quiz.json', fixes)
