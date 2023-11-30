# Либы и глобальные переменные
from turtle import *
scale = 15 # Важно выбрать достаточно большой (>=15)
color('black','red') # Цвет (линии, заливки)

speed(1000) # Опционально

# Начало заливки
begin_fill()

# Алгоритм для построения фигуры
right(90)

for i in range(3): # Важно чтобы точка начала и точка конца была в одном месте (начиная с номера 3)
    right(45)
    forward(10 * scale)
    right(45)

right(315)
forward(10 * scale)

for i in range(2):
    right(90)
    forward(10 * scale)

# Конец заливки
end_fill()

# Создание фигуры в системе
canvas = getcanvas()
c = 0

# Проверка пересечений
for x in range(-100, 100): # ЗНАЧЕНИЯ ПО Х И Y ДОЛЖНЫ ОХВАТЫВАТЬ ФИГУРУ!!!!! (с номера 4)
    for y in range(-100, 100):
        s = canvas.find_overlapping(x * scale, y * scale, x * scale, y * scale)
        if len(s) == 1 and s[0] == 5: # 4 – линия 5 – точка; len(s) == 1 если ТОЛЬКО внутри контура; len(s) >= 1 если ВНУТРИ ИЛИ НА КОНТУРЕ
            c += 1
            # print(s)
print(c)

# # Прорисовка точек
# penup()
# color('black')
# for x in range(-15, 10):
#     for y in range(-8, 15):
#         setpos(x * scale, y * scale)
#         dot(3)



done()