from turtle import Turtle

t = Turtle()
scale = 25

for i in range(6):
    t.right(36)
    t.forward(10 * scale)
    t.right(36)

t.penup()

for x in range(-10,10):
    for y in range(-16,3):
        t.setpos(x * scale, y * scale)
        t.dot(4)