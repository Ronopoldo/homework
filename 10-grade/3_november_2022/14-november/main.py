# for n in range(4,30000):
#     n2 = bin(n)[2:]
#     n2 = n2[::-1][1::][::-1]
#     n2 = n2 + n2[1] + n2[1]
#     if (int(n2, 2) > 92):
#         print(n, bin(n), n2)
#         break

# a = 'abcde'
# a = a[::-1][1::][::-1]
# print(a)







# for n in range(100,1000):
#     nstr = str(n)
#     s1 = int(nstr[0]) + int(nstr[1])
#     s2 = int(nstr[1]) + int(nstr[2])
#     if (s1 > s2):
#         output = str(s1) + str(s2)
#     else:
#         output = str(s2) + str(s1)
#     if (output == '157'):
#         print(output, s1, s2 ,n)










# for n in range(30000, 0,-1):
#     n2 = str(bin(n)[2:])
#     if (n % 2 == 0):
#         n2 = n2 + '10'
#     else:
#         n2 = n2 + '01'
#     if (int(n2, 2) <= 102):
#         print(int(n2, 2), n2, n)





# for n in range(100,1000):
#





for n in range(100,1000):
    nstr = str(n)
    s1 = int(nstr[0]) + int(nstr[1])
    s2 = int(nstr[1]) + int(nstr[2])
    if (s1 > s2):
        output = str(s1) + str(s2)
    else:
        output = str(s2) + str(s1)
    if (output == '1711'):
        print(output, s1, s2 ,n)





# Метод	Что делает
# list.append(x)	Добавляет элемент в конец списка
# list.extend(L)	Расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x)	Вставляет на i-ый элемент значение x
# list.remove(x)	Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# list.pop([i])	Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]])	Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# list.count(x)	Возвращает количество элементов со значением x
# list.sort([key=функция])	Сортирует список на основе функции
# list.reverse()	Разворачивает список
# list.copy()	Поверхностная копия списка
# list.clear()	Очищает список
