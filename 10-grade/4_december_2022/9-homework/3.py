import turtle

t = turtle.Turtle()
scale = 25
t.speed("fastest")

for i in range(4):
  t.forward(8 * scale)
  t.right(150)
  t.forward(8 * scale)
  t.right(30)

t.penup()
for x in range(-7,10):
  for y in range(-10,2):
    t.setpos(x*scale,y*scale)
    t.dot(3, 'red')

