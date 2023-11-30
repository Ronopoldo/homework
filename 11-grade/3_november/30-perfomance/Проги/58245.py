# Либы и глобальные переменные
from turtle import *
scale = 15
color('black', 'red')

# Начало заливки
begin_fill()

# Алгоритм для построения фигуры

right(60)
for i in range(2):
    forward(10 * scale)
    right(120)
    forward(5 * scale)
    right(240)

right(120)
forward(3 * scale)
right(90)
forward(20 * 3 ** 0.5 * scale)
right(90)
forward(8 * scale)
right(120)

for i in range(2):
    forward(10 * scale)
    left(120)
    forward(5 * scale)
    left(240)
# Конец заливки

end_fill()

canvas = getcanvas()
c = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        s = canvas.find_overlapping(x * scale, y * scale, x * scale, y * scale)
        if len(s) == 1 and s[0] == 5: # 4 – линия 5 – точка; len(s) == 1 если ТОЛЬКО внутри контура; len(s) >= 1 если ВНУТРИ ИЛИ НА КОНТУРЕ
            c += 1
            print(s)
print(c)
done()