import turtle

t = turtle.Turtle()
scale = 15
t.speed("fastest")

for i in range(4):
  t.forward(5 * scale)
  t.right(90)
  t.forward(10 * scale)
  t.right(90)

t.penup()
for x in range(0,10):
  for y in range(-10,15):
    t.setpos(x*scale,y*scale)
    t.dot(3, 'red')

