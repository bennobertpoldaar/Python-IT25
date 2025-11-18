#Benno Bert Põldäär
#10.11.25

import turtle
t = turtle.Turtle()
aken = turtle.Screen()
aken.setup(width=500, height=400)

t.speed(0)
t.pensize(6)
#sinine
t.penup()
t.goto(-110,0)
t.pendown()
t.pencolor("blue")
t.circle(50)
#must
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("black")
t.circle(50)
#punane
t.penup()
t.goto(110,0)
t.pendown()
t.pencolor("red")
t.circle(50)
#kollane
t.penup()
t.goto(-55,-55)
t.pendown()
t.pencolor("yellow")
t.circle(50)
#roheline
t.penup()
t.goto(55,-55)
t.pendown()
t.pencolor("green")
t.circle(50)
turtle.done()


