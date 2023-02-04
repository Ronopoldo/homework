for N in range(1, 8192):
    N2 = bin(N)[2::]
    i = 0
    temp = 0
    while i < len(N2):
        temp = temp + int(N2[i])
        i = i + 1
    N2 = str(N2) + str(temp % 2)
    i = 0
    temp = 0
    while i < len(N2):
        temp = temp + int(N2[i])
        i = i + 1
    N2 = str(N2) + str(temp % 2)
    if int(N2, 2) > 77:
        print(N, N2, bin(N))
        break

# 19



    # N2 = str(N2) + str(sum(N2))





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