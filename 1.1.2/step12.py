# import the turtle module
import turtle as trtl


# create the turtle object
painter = trtl.Turtle()
painter.turtlesize(5)
painter.pendown()

print("making a circle...")
# ask user for a color (such as red, green, blue, pink, purple)
#color = input("please enter the color")
color = "pink"
# ask user for the radius of a circle
#radius = input("please enter a radius:")
radius = 110
# draw a circle with the radius and line color entered by the user
painter.color(color)
# Circle
painter.circle(int(radius))
#Reposition for first eye
painter.penup()
painter.left(130)
painter.forward(int(50))
painter.right(int(30))
painter.forward(int(50))
painter.pendown()
# Draw First Eye
painter.forward(int(70))
painter.right(int(90))
painter.forward(int(10))
painter.right(int(90))
painter.forward(int(70))
painter.right(int(90))
painter.forward(int(10))
painter.penup()
#Reposition for eye #2
painter.backward(int(100))
painter.right(90)
#draw second eye
painter.pendown()
painter.forward(int(70))
painter.left(90)
painter.forward(int(10))
painter.left(90)
painter.forward(int(70))
painter.left(90)
painter.forward(int(10))
#reposition for nose
painter.penup()
painter.right(90)
painter.forward(int(20))
painter.right(90)
painter.forward(int(40))
#drawing the nose
painter.pendown()
painter.forward(int(10))
painter.right(90)
painter.forward(int(10))
painter.right(90)
painter.forward(int(10))
painter.right(90)
painter.forward(int(10))
#reposition for mouth
painter.penup()
(painter.forward (int(20)))
painter.left(90)
painter.forward(int(50))
painter.right(180)
painter.pendown()
painter.forward(int(120))
painter.left(90)
painter.circle(60,180)
painter.left(100)
painter.circle(20,180)


# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()