import turtle
from turtle import Turtle

t = turtle.Turtle()
scale = 40

for tmp in range(5):
    t.forward(8 * scale)
    t.right(60)
    t.forward(8 * scale)
    t.right(120)

t.penup()


for x in range(-1, 15):
    for y in range(-7, 1):
        t.setpos(x * scale, y * scale)
        t.dot(3)

