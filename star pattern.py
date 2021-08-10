import turtle
col=('red','yellow','green','cyan','pink','white')
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(25)
for i in range(150):

    t.color(col[i%6])
    t.forward(i*5)
    t.left(150)
    t.width(3)