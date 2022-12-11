import turtle

t = turtle.Turtle()

for i in range(4):
  t.forward(10 * 10) # Масштаб увеличен в 10 раз
  t.left(90)

t.penup() #Перестать рисовать линию за черепахой
for x in range(20):
  for y in range(20):
    t.setpos(x*10,y*10) #Перемещение в (x,y) с масштабом x10
    t.dot(3, 'red')


# В ОТВЕТЕ - КОЛИЧЕСТВО ТОЧЕК __ВНУТРИ__ ФИГУРЫ