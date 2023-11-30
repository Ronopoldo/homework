# Либы и глобальные переменные
from turtle import *
scale = 25
chet = [2, 4, 6, 8, 0]
color('black','red')

# Начало заливки
begin_fill()

# Алгоритм для построения фигуры
left(90)

for i in range(2): # ДОЛЖНА ЗАМЫКАТЬСЯ, поэтому не 4, а 2
    forward(8 * scale)
    right(90)
    forward(8 * scale)
    right(90)

# Конец заливки

end_fill()

canvas = getcanvas()
c = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        s = canvas.find_overlapping(x * scale, y * scale, x * scale, y * scale)
        if len(s) == 1 and s[0] == 5: # 4 – линия 5 – точка
            c += 1
            print(s)
print(c)
done()