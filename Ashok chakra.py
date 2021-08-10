import turtle

turtle.bgcolor("black")
turtle.speed(10)

for i in range(35):
    for colours in ("blue"):
        turtle.color(colours)
        turtle.pensize(3)
        turtle.lt(12)
        for i in range(4):
            turtle.fd(200)
            turtle.lt(90)
turtle.done()


