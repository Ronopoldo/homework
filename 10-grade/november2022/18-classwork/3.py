#3 задача
liste = []
length = int(input('Введите длину списка: '))
for i in range(length):
    input1 = int(input('Введите элемент ' + str(i + 1) + ': '))
    liste.append(input1)

print(int(max(liste)) / length)

print(max(liste))