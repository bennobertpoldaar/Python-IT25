import turtle
turtle.speed(0)

turtle.circle(50)

ekraan = turtle.Screen()

def muuda_punaseks():
    turtle.color("red")

def muuda_sinine():
    turtle.color("blue")

def muuda_roheliseks():
    turtle.color("green")

def vasakKlikk(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)
    

def paremKlikk(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    

def keskmineKlikk(x, y):
    turtle.undo()

ekraan.onscreenclick(vasakKlikk, 1) # Vasak klõps
ekraan.onscreenclick(paremKlikk, 3) # Parem klõps
ekraan.onkey(muuda_punaseks, "r")
ekraan.onkey(muuda_roheliseks, "g")
ekraan.onkey(muuda_sinine, "b")


ekraan.listen()
turtle.done()