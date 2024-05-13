from turtle import *

scale = 15

speed(9999)
penup()
for x in range(-5, 15):
    for y in range(-15, 4):
        setpos(x * scale, y * scale)
        dot(3)
speed(1)
setpos(0,0)
pendown()
for i in range(4):
    for i1 in range(4):
        forward(6 * scale)
        right(90)
    forward(10 * scale)
    right(90)
    forward(3 * scale)

done()