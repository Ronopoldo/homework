# Либы и глобальные переменные
from turtle import *
scale = 100
chet = [2, 4, 6, 8, 0]
color('black', 'red')

# Начало заливки
begin_fill()
speed(1000)
# Алгоритм для построения фигуры
forward(200)

for i in range(3): # ДОЛЖНА ЗАМЫКАТЬСЯ, поэтому не 4, а 2
    right(90)
    forward(50 * scale)


# Конец заливки

end_fill()

canvas = getcanvas()
c = 0
for x in range(-100 * scale, 100 * scale, scale):
    for y in range(-100 * scale, 100 * scale, scale):
        s = canvas.find_overlapping(x, y, x, y)
        if len(s) == 1 and s[0] == 5: # 4 – линия 5 – точка
            c += 1
            print(s)
print(c)
done()