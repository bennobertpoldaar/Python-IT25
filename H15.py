import turtle
import random

aken = turtle.Screen()
aken.bgcolor("red")
aken.setup(width=600, height=600)
aken.tracer(0)

# ristkülik
ristkylik = turtle.Turtle()
ristkylik.shape("square")
ristkylik.shapesize(stretch_wid=1, stretch_len=5)
ristkylik.penup()
ristkylik.color("black")
ristkylik.goto(ristkylik.xcor(), -250)

# ring
ring = turtle.Turtle()
ring.shape("circle")
ring.penup()
ring.speed('fastest')
ring.setheading(random.randint(0, 360))

# kiirused
ristkyliku_kiirus = 20
kiirus = 10


# ristküliku funktsioonid
def liigu_vasakule():
    x = ristkylik.xcor()
    if x > -280:
        ristkylik.setx(x - ristkyliku_kiirus)
        

def liigu_paremale():
    nurk = ring.heading()
    x = ristkylik.xcor()
    if x < 280:
        ristkylik.setx(x + ristkyliku_kiirus)

# ringi funktsioonid
def peegelda_porkumisel():
    nurk = ring.heading()
    if ring.xcor() >= 290 or ring.xcor() <= -290:
        ring.setheading(180 - nurk)
    if ring.ycor() >= 290:
        ring.setheading(360 - nurk)
    if (-260 <= ring.ycor() <= -230) and \
       (ristkylik.xcor() - 50 <= ring.xcor() <= ristkylik.xcor() + 50):
            ring.setheading(360 - nurk)

    if ring.ycor() <= -290:
        print("idioot oled?")
        ring.hideturtle()
        return

punktid = 0

skoor = turtle.Turtle()
skoor.hideturtle()
skoor.penup()
skoor.color("white")
skoor.goto(0, 260)
skoor.write("Punktid: 0", align="center", font=("Arial", 20, "normal"))


def ring_liigu():
    ring.forward(kiirus)
    peegelda_porkumisel()
    aken.update()
    aken.ontimer(ring_liigu, 20)

# klaviatuurile reageerimine
aken.listen()
aken.onkeypress(liigu_vasakule, "Left")
aken.onkeypress(liigu_paremale, "Right")

ring_liigu()

aken.mainloop()