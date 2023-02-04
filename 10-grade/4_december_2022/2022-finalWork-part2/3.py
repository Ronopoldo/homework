import turtle

t = turtle.Turtle()
scale = 40
t.speed("fastest")

# t.color('purple', 'yellow') #цвет(линии, заливки)
# t.begin_fill() # - ЗАЛИВКА

for i in range(14):
  t.right(60)
  t.forward(2 * scale)
  t.right(60)
  t.forward(2 * scale)
  t.right(270)

# t.end_fill()

t.penup()
for x in range(-15,10):
  for y in range(-15,20):
    t.setpos(x*scale,y*scale)
    t.dot(2, 'red')


# ПОЛОВИНЫ НЕ СИММЕТРИЧНЫ!!

#149