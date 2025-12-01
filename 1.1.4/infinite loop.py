#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

color1 = "coral"

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 50
angle = 200
seg = int(180/angle)

# Add a loop with a zero-iteration condition
start_loop = 'y'
while start_loop == 'y':
    painter.forward(space)
    painter.left(angle)
    painter.circle(10)
    painter.left(angle)
    painter.forward(space)
    painter.circle(10)



