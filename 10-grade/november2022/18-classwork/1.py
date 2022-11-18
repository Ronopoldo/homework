# 1 ЗАДАЧА
liste = []
length = int(input('Введите длину списка: '))
for i in range(length):
    input1 = input('Введите элемент ' + str(i + 1) + ': ')
    liste.append(input1)
print(liste[::-1])
