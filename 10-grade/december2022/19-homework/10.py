import turtle

t = turtle.Turtle()
scale = 30

for i in range(4):
    t.forward(8 * scale)
    t.right(90)

t.pencolor('red')
for i2 in range(3):
    t.forward(12 * scale)
    t.right(120)

t.penup()
for x in range(0,10):
    for y in range(-8,1):
        t.setpos(x * scale, y * scale)
        t.dot(5)

# 13