'''
Инверсия - not ! - (отрицание)
Конъюкция - and * ^
Дизъюнкция - or + v
Импликация - <= ->
Эквивалентность - == ===
'''

print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (x or y) <= (z == x)
            print(x, y, z, int(F))