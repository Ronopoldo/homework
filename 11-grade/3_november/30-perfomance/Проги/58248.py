# Либы и глобальные переменные
from turtle import *
scale = 15
seth(90)
color('black', 'red')

# Начало заливки
begin_fill()

# Алгоритм для построения фигуры

right(180)
forward(5 * scale)
right(90)
forward(50 * scale)
right(90)
forward(5 * scale)
for i in range(5):
    seth(90)
    circle(-5 * scale, 180)
# Конец заливки

end_fill()

canvas = getcanvas()
c = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        s = canvas.find_overlapping(x * scale, y * scale, x * scale, y * scale)
        if len(s) == 1 and s[0] == 5: # 4 – линия 5 – точка; len(s) == 1 если ТОЛЬКО внутри контура; len(s) >= 1 если ВНУТРИ ИЛИ НА КОНТУРЕ
            c += 1
            print(s)
print(c)
done()