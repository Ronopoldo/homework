from turtle import Turtle

t = Turtle()

scale = 40

for i in range(10):
    t.forward(5 * scale)
    t.right(60)

t.penup()

for x in range(-5,16):
    for y in range(-10, 2):
        t.setpos(x * scale,y * scale)
        t.dot(7)

while True:
    print(123)


# 62 (ПРОВЕРЕНО)