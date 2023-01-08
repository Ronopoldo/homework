from turtle import Turtle

t = Turtle()
scale = 25

for i in range(14):
    t.right(60)
    t.forward(2*scale)
    t.right(60)
    t.forward(2*scale)
    t.right(270)

t.speed(1)
t.penup()
for x in range(-19,19):
    for y in range(-10,10):
        t.setpos(x*scale,y*scale)
        t.dot(5)

#149