import turtle

t = turtle.Turtle()
scale = 30
t.speed("fastest")

for i in range(4):
  t.forward(8 * scale)
  t.right(90)
  
for i1 in range(3):
  t.forward(12 * scale)
  t.right(120)

t.color("red")

for i2 in range(4):
  t.forward(8 * scale)
  t.right(90)

t.color("purple")

for i3 in range(4):
  t.forward(12 * scale)
  t.right(120)

t.penup()
for x in range(-7,10):
  for y in range(-10,2):
    t.setpos(x*scale,y*scale)
    t.dot(3, 'red')

