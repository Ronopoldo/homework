from turtle import *
scale = 30

color('black', 'red')

begin_fill()
right(90)
for i in range(3):
    right(45)
    forward(10 * scale)
    right(45)

right(315)
forward(10 * scale)

for i in range(2):
    right(90)
    forward(10 * scale)

end_fill()
canvas = getcanvas()
c = 0

for x in range(-100, 100):
    for y in range(-100, 100):
        s = canvas.find_overlapping(x * scale, y * scale, x * scale, y * scale)
        if len(s) == 1 and s[0] == 5:
            c+=1

print(c)
done()