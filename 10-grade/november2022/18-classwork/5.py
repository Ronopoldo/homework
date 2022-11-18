#5 задача
array = []
length = int(input('Введите длину списка: '))
for i in range(length):
    input1 = str(input('Введите элемент ' + str(i + 1) + ': '))
    array.append(input1)

etalon = len(max(array))
print(etalon)

for i in range(len(array)):
    while len(array[i]) < etalon:
        array[i] = array[i] + '_'

print(array)