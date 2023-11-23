from turtle import *
scale = 45
for i in range(8):
    forward(6 * scale)
    right(120)

penup()
for x in range (-1, 7):
    for y in range(-9, 1):
        setpos(x * scale, y * scale)
        dot(4)
while True:
    print()

# 13