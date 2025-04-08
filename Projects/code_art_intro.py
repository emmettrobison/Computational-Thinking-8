# Setup
import turtle
t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("purple")
t.pendown()
t.speed(10000000000000)

for i in range(20):
    for i in range(15):
        for i in range(50):
            t.forward(40)
            t.right(61)
        t.penup()
        t.left(10)
        t.forward(30)
        t.pendown()
    t.left(18)
    t.penup()
    t.forward(50)
    t.pendown()

turtle.exitonclick()