# make turtle
import turtle as trtl
# Print statements
print("Create your star constellations!! Lets check if your sizing is right.")
# Elif
bigdip = 8
hydrus = 3
leo = 6
apus = 10
if apus < bigdip:
    print("Program running smooth lets start up!")
    start_concept = input("Are you ready?")
    print("Thank you for your response!! Let's get to drawing! :3")
elif bigdip < apus:
    print("Hold on to changing your sizing....")
    print("........")
    start_concept2 = input("Are we ready now?")
    print("Alright!! Sorry for the minor inconvenience lets get printing! :3")

# Make the radius for circles
bigdipradius = 4
hydrusradius = 2
leoradius =  3
apusradius = 2.5

# Make individuals
bigdip = trtl.Turtle()
hydrus = trtl.Turtle()
leo = trtl.Turtle()
apus = trtl.Turtle()

# Make colors
bigdip.pencolor('purple')
hydrus.pencolor('dark blue')
leo.pencolor('black')
apus.pencolor('gold')

# Start code for Big dip
bigdip.pensize(8)
bigdip.right(30)
bigdip.pendown()
bigdip.circle(bigdipradius)
bigdip.forward(70)
bigdip.right(40)
bigdip.circle(bigdipradius)
bigdip.forward(40)
bigdip.left(10)
bigdip.circle(bigdipradius)
bigdip.forward(40)
bigdip.left(40)
for line in range(2):
    bigdip.circle(bigdipradius)
    bigdip.forward(120)
    bigdip.right(90)
    bigdip.circle(bigdipradius)
    bigdip.forward(50)
    bigdip.right(90)
bigdip.penup()
bigdip.hideturtle()

# Start code for Hydrus
hydrus.pensize(3)
hydrus.penup()
startx = 70
starty = 130
hydrus.goto(startx,starty)
hydrus.pendown()
hydrus.circle(hydrusradius)
hydrus.forward(90)
hydrus.right(50)
hydrus.circle(hydrusradius)
hydrus.forward(30)
hydrus.right(30)
hydrus.circle(hydrusradius)
hydrus.forward(60)
hydrus.left(120)
hydrus.circle(hydrusradius)
hydrus.forward(120)
hydrus.right(140)
hydrus.circle(hydrusradius)
hydrus.forward(150)
hydrus.circle(hydrusradius)
hydrus.penup()
hydrus.hideturtle()

# Start code for Leo
leo.pensize(6)
leo.penup()
startx = -60
starty = 150
leo.goto(startx, starty)
leo.right(220)
leo.pendown()
for line in range(2):
    leo.circle(leoradius)
    leo.forward(40)
    leo.left(75)
    leo.circle(leoradius)
    leo.forward(50)
    leo.left(30)
leo.right(60)
leo.circle(leoradius)
leo.forward(45)
leo.right(90)
leo.circle(leoradius)
leo.forward(110)
leo.left(40)
leo.circle(leoradius)
leo.forward(95)
leo.right(145)
leo.circle(leoradius)
leo.forward(110)
leo.right(57)
leo.circle(leoradius)
leo.forward(140)
leo.penup()
leo.hideturtle()

# Start code for apus
apus.pensize(4)
apus.penup()
startx = -160
starty = -160
apus.goto(startx, starty)
apus.pendown()
apus.left(90)
apus.circle(apusradius)
apus.forward(90)
apus.right(130)
for lines in range(2):
    apus.circle(apusradius)
    apus.forward(120)
    apus.left(10)
apus.circle(apusradius)
apus.hideturtle()

# End statement
print("Enjoy and come back later <3")




wn = trtl.Screen()
wn.mainloop()