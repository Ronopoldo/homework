from turtle import *

color('red','black')
begin_fill()

scale = 30

for i in range(5):
    forward(7 * scale)
    right(120)

penup()

for x in range(-2, 8):

    for y in range(-8, 2):
        setpos(x * scale, y * scale)
        dot(5)
done()

