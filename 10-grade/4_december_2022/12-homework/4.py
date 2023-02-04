import turtle
t = turtle.Turtle()
scale = 15
for i in range(5):
    t.forward(9 * scale)
    t.right(120)

t.penup()
for x in range(0,15):
    for y in range(-15,1):
        t.setpos(x * scale, y * scale)
        t.dot(2)