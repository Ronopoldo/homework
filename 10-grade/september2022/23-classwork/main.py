a = int(input('Введите A'))
b = int(input('Введите B'))
c = int(input('Введите C'))

if (b ** 2 - 4 * a * c < 0):
    print('Нет корней')
elif (b ** 2 - 4 * a * c == 0):
    print((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
else:
    print('Корень один: ' + str((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)))
    print('Корень два: ' + str((-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)))







# year = int(input('Введите любой год нашей эры:'))
# # match :
#
#
match (year - year//12*12):
    case 8:
        print("Дракона")
    case 9:
        print("Змея")
    case 10:
        print("Лошадь")
    case 11:
        print("Коза")
    case 0:
        print("Обезьяна")
    case 1:
        print("Петух")
    case 2:
        print("Собака")
    case 3:
        print("Свинья")
    case 4:
        print("Крыса")
    case 5:
        print("Бык")
    case 6:
        print("Тигр")
    case 7:
        print("Кролик")

print(year - year//12*12)



import random
num = random.randint(1,38)
win = num
redArray = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

if (win == 37):
    print("Выигравшая ставка: 0")
elif (win == 38):
    print("Выигравшая ставка: 00")
else:
    print("Выпавший номер: " + str(num))

if (win == 37):
    print("Выигравшая ставка: 0")
elif (win == 38):
    print("Выигравшая ставка: 00")
else:
    print("Выигравшая ставка: " + str(win))

if (win <= 36):
    if (win % 2 == 0):
        type = 'чётное'
    else:
        type = 'нечётное'

    if (str(num) in redArray == true):
      color = 'красное'
    else:
      color = 'чёрное'

    if (win <= 18):
        range = ('От 1 до 18')
    else:
        range = ('От 19 до 36')

    print('Выигравшая ставка: ' + color)
    print('Выигравшая ставка: ' + type)
    print('Выигравшая ставка: ' + range)









pos = str(input("Введите координату: "))

num = int(pos[1])
letter = pos[0]

match  letter:
    case "a":
        letterNumber = 1
    case "b":
        letterNumber = 2
    case "c":
        letterNumber = 3
    case "d":
        letterNumber = 4
    case "e":
        letterNumber = 5
    case "f":
        letterNumber = 6
    case "g":
        letterNumber = 7
    case "h":
        letterNumber = 8

if letterNumber%2 == 0:
    added = 1
else:
    added = 0

if ((num + added) % 2 == 0):
    print('белая')
else:
    print('чёрная')




