spider = 8
Size = 40 / spider
spider = 10
# what is y?
# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
#Making the body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
#Variable for legs
Num_Of_Legs = 8
Size = 80
Rotation = 300 / Num_Of_Legs
spider.pensize(5)
Legs = 2
#Legs
while (Legs < Num_Of_Legs):
  spider.goto(0,20)
  
#Head
spider.left(30)
spider.forward(50)
spider.pensize(30)
spider.circle(15)
#Eyes
spider.pencolor('white')
spider.pensize(5)
spider.penup()
spider.forward(10)
spider.pendown()
spider.circle(7)
spider.penup()
spider.left(90)
spider.forward(30)
spider.pendown()
spider.circle(7)
spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()