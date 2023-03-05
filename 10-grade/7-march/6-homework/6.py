from turtle import Turtle

t = Turtle()

scale = 20

for i in range(4):
    t.forward(10 * scale)
    t.right(60)
    t.forward(10 * scale)
    t.right(120)


t.penup()
for x in range(0,18):
    for y in range(-12,2):
        t.setpos(x * scale,y * scale)
        t.dot(7)

while True:
    a = 1

# 80 (ПРОВЕРЕНО)