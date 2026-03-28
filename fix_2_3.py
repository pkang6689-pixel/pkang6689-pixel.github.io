import json
import sys
sys.path.insert(0, '.')
from fix_quiz import fix_file

fixes = {
    11: [
        "A graph that only applies to objects at rest, since moving objects produce values too dynamic to be plotted on a standard coordinate system",
        "A graph showing the speed of an object plotted over the distance it has traveled, giving a visual representation of how speed changes with position",
        "A chart that compares an object's position directly to its acceleration, showing how the rate of velocity change relates to location over time"
    ],
    12: [
        "A graph where the y-axis represents position and the x-axis represents time, allowing one to read off the location of the object at each moment",
        "A graph that shows only the magnitude of speed and not the direction of travel, omitting the vector nature of the quantity being plotted over time",
        "A graph that can only accurately show constant motion, since varying velocities produce curves that cannot be interpreted using standard methods"
    ],
    13: [
        "The velocity of the object only at the very start of the motion, since initial conditions are the only ones that can be measured precisely from a graph",
        "The total distance an object has traveled divided by the total time elapsed, giving a single averaged value across the entire duration of motion",
        "The fastest speed an object reaches at any point during its motion, corresponding to the peak value visible anywhere on the position-time graph"
    ],
    14: [
        "The total area enclosed under a velocity-time graph curve, which represents the net work done on the object rather than any velocity-related quantity",
        "The speed of the object measured exactly at the midpoint of its journey, assumed to represent the most typical value of motion throughout the trip",
        "The highest velocity the object reaches at any point during the trip, determined by finding the maximum slope on the corresponding position-time graph"
    ],
    16: [
        "A line drawn parallel to the horizontal x-axis at any point on the graph, representing a constant value of whatever quantity is plotted on the y-axis",
        "A line tangent to the curve at exactly one point, touching the curve locally and matching its instantaneous slope at that specific location on the graph",
        "A perfectly vertical line drawn on the graph, representing an undefined or infinite rate of change in the plotted quantity at that particular moment"
    ],
    17: [
        "The maximum peak value displayed anywhere on the vertical axis of the graph, representing the largest magnitude of the quantity plotted over time",
        "The total energy stored in the system being analyzed, since in kinematics the area always relates to an energy quantity rather than to velocity or position",
        "A direct measure of how curved or bent the plotted line is at a given point, with more curvature indicating a stronger change in the graphed variable"
    ],
    18: [
        "Motion in which the object always eventually returns to its starting point, forming a closed loop on the position-time graph regardless of speed changes",
        "Motion that produces a curved line on the position-time graph, indicating that the velocity of the object is continuously changing over the time interval",
        "Any type of motion that can be shown on any kind of graph, since all motion qualifies as uniform whenever it is represented visually on coordinate axes"
    ],
    19: [
        "Motion in a perfectly straight line at a constant speed with no direction changes, producing a straight line of constant slope on the position-time graph",
        "Motion where the acceleration always remains constant throughout, producing equal velocity changes in every equal time interval during the entire trip",
        "Motion that is fundamentally impossible to represent on any graph, since constantly changing velocities cannot be captured by standard plotting techniques"
    ],
    20: [
        "A graph that is identical to a velocity-time graph, since acceleration and velocity always display the same data when plotted against elapsed time",
        "A graph that can only display constant acceleration values, since varying accelerations produce shapes that are not physically meaningful when graphed",
        "A graph where the slope at any point gives the object's position, connecting the rate of change in acceleration directly to the location of the object"
    ],
    21: [
        "100 m/s \u2014 multiplying position by time: 20 times 5 gives 100 m/s as the velocity, since velocity is the product of final position and elapsed time",
        "20 m/s \u2014 the velocity equals the final position value of 20 m read directly from the y-axis of the graph, since position and velocity are interchangeable",
        "5 m/s \u2014 the velocity equals the time value of 5 seconds read from the x-axis of the graph, because time and velocity share the same numerical value"
    ],
    22: [
        "8 m \u2014 the displacement equals the velocity value of 8 m/s read directly from the graph, because velocity and displacement share the same numerical value",
        "6 m \u2014 the displacement equals the time value of 6 seconds taken from the horizontal axis, since displacement is always numerically equal to elapsed time",
        "14 m \u2014 the displacement is found by adding the velocity and time values together: 8 + 6 = 14 m, since displacement is the sum of speed and duration"
    ],
    24: [
        "The average velocity over the entire trip equals exactly 6 m/s, since a tangent slope at any single point always represents the overall average velocity",
        "The acceleration at t = 3 s is exactly 6 m/s squared, because the slope of the tangent line on a position-time graph directly gives the acceleration value",
        "The object is decelerating at t = 3 s, because an upward-opening parabolic curve always indicates that the object is slowing down at every instant"
    ],
    25: [
        "150 m \u2014 multiplying the maximum velocity by total time: 25 times 8 = 200, adjusted by subtracting 50 for the initial phase, gives 150 m displacement",
        "75 m \u2014 taking the average of initial and final velocities multiplied by total time: (10 + 25)/2 times some duration factor yields about 75 m displacement",
        "105 m \u2014 multiplying the average velocity of approximately 13 m/s by the total elapsed time of 8 seconds yields an approximate displacement of 105 meters"
    ],
    26: [
        "Car A has greater acceleration than Car B, since a steeper slope on a position-time graph means the object is accelerating more rapidly over time",
        "Car A is accelerating much more than Car B, because the steepness of a straight line on a position-time graph directly measures the acceleration value",
        "Car B will eventually pass Car A, because objects with lower slopes on position-time graphs always build up speed and overtake faster objects later on"
    ],
    27: [
        "The object moves at a constant velocity of 20 m/s for the entire 5 seconds, and the straight line on the velocity-time graph confirms zero acceleration throughout",
        "The object reverses direction precisely at t = 5 seconds, meaning it was traveling forward and then instantly begins moving backward at the same speed",
        "The object accelerates uniformly from rest to 20 m/s over the 5-second interval, with velocity increasing at a constant rate of 4 m/s every second"
    ],
    28: [
        "It never stops during the interval; the total displacement is 20 m because the entire area under the velocity-time graph is positive from start to finish",
        "It stops at t = 2 s when velocity reaches zero; displacement is 20 m from the total area under the velocity-time graph being entirely in the positive region",
        "It stops at t = 4 s at the end of the interval; displacement is 40 m because the total area is calculated as base times height equaling 4 times 10 = 40 m"
    ],
    29: [
        "18 m/s \u2014 the final velocity equals the area under the acceleration-time graph alone: 3 times 6 = 18 m/s, without adding the initial velocity component",
        "3 m/s \u2014 the final velocity equals the value of the acceleration since velocity and acceleration are the same quantity when the motion has a constant rate",
        "6 m/s \u2014 the final velocity equals the elapsed time of 6 seconds, because the numerical value of elapsed time always matches the final velocity of the object"
    ],
    30: [
        "Both students are wrong \u2014 curved lines on position-time graphs only show constant velocity, and neither acceleration nor deceleration can produce a curved shape",
        "The classmate is correct \u2014 any curve that flattens on a position-time graph always represents deceleration, because all curving lines indicate the object is slowing down",
        "Neither student can be correct \u2014 you would need a separate velocity-time graph to determine anything about the acceleration, since position-time graphs cannot show it"
    ]
}

fix_file('content_data/PhysicsLessons/Unit2/Lesson2.3_Quiz.json', fixes)
