f = open('1.txt').read()
f = f.split('\n')
for tem in range(len(f)):
    f[tem] = int(f[tem])
f = sorted(f)[::-1]
i = 0

print(f)
tmp = 65536
for k in range(len(f) - 1):
    if (int(tmp) - int(f[k + 1])) >= 3:
        tmp = int(f[k + 1])
        print(tmp)
        i += 1
print(i)


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