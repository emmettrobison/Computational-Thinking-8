# Setup
import turtle
import random
turtle.colormode(255)
t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.pendown()
t.speed(0)

# Set the turtle color to a light blue
t.pencolor((135, 206, 235))

# Change background color
turtle.Screen().bgcolor("black")

# Repeat the following code 250 times
for i in range(250):
    # Move
    t.forward(30 + i)
    t.left(71)

    # Change the color of the turtle randomly
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)

t.penup()
t.goto(0, 0)
t.pendown()
t.color("black")
t.begin_fill()
for i in range(250):
    t.forward(30 + i)
    t.left(71)

# Finish
turtle.exitonclick()