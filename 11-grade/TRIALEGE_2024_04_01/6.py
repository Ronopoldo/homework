from turtle import *

fillcolor('yellow')
speed(1000)
scale = 40
begin_fill()
for i in range(4):
    forward(8 * scale)
    right(90)
end_fill()
fillcolor('magenta')
begin_fill()
for i in range(3):
    forward(12 * scale)
    right(120)
end_fill()

penup()
for x in range(-2, 30):

    for y in range(-14, 1):
        setpos(x * scale, y * scale)
        dot(5)


# Внцутри жёлтой; вне мадженты (БЕЗ ЛИНИИ)
done()