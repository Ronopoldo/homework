import turtle
from turtle import Turtle


scale = 30

turtle.right(45)
for i in range(7):
    turtle.forward(5 * scale)
    turtle.right(45)
    turtle.forward(10 * scale)
    turtle.right(135)

turtle.penup()
for x in range(-1, 7):
    for y in range(-15, 1):
        turtle.setpos(x * scale, y * scale)
        turtle.dot(3)

temp = input()


# 27