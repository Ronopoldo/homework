from turtle import *

speed(127389)
scale = 15

for i in range(2):
    forward(13 * scale)
    right(90)
    forward(18 * scale)
    right(90)

penup()


forward(5 * scale)
right(90)
forward(9 * scale)
left(90)
pendown()
for i in range(2):
    forward(11 * scale)
    right(90)
    forward(7 * scale)
    right(90)


penup()

for x in range(0, 20):
    for y in range(-20, -8):
        setpos(x * scale, y * scale)
        dot(5)


done()