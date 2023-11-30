# Либы и глобальные переменные
from turtle import *
scale = 100
chet = [2, 4, 6, 8, 0]
color('black', 'red')
speed(1000)
# Начало заливки
begin_fill()
# Алгоритм для построения фигуры
forward(200 * scale)

for i in range(3): # ДОЛЖНА ЗАМЫКАТЬСЯ, поэтому не 4, а 2
    right(90)
    forward(100 * scale)


# Конец заливки

end_fill()

canvas = getcanvas()
c = 0
for x in range(-1000 * scale, 1000 * scale, scale): # ВАЖНО ПОВЫСИТЬ ЗНАЧЕНИЯ
    for y in range(-1000 * scale, 1000 * scale, scale): # ВАЖНО ПОВЫСИТЬ ЗНАЧЕНИЯ
        s = canvas.find_overlapping(x, y, x, y)
        if len(s) >= 1: # 4 – линия 5 – точка
            c += 1
            print(s)
print(c)
done()