from turtle import *

scale = 30
speed(2024)

for i in range(2):
    forward(7 * scale)
    right(90)
    forward(18 * scale)
    right(90)

penup()

backward(-2 * scale)
right(90)
forward(9 * scale)
left(90)

pendown()

for i in range(2):
    forward(8 * scale)
    right(90)
    forward(5 * scale)
    right(90)

penup()
for x in range(0, 15):
    for y in range(-18, -6):
        setpos(x * scale, y * scale)
        dot(3)

done()