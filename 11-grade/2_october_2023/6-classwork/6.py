from turtle import *
scale = 30

# color('red')
begin_fill()


right(90)
for i in range(3):
    right(45)
    forward(10 * scale)
    right(45)

right(315)
forward(10 * scale)

for o in range(2):
    right(90)
    forward(10 * scale)

end_fill()
penup()

canvas = getcanvas()
c = 0
for x in range(-100*scale, 100*scale, scale):
    for y in range(-100*scale, 100*scale, scale):
        s = canvas.find_overlapping(x, y, x, y)
        if len(s) == 1 and s[0] == 5:
            c += 1


print(c)

done()