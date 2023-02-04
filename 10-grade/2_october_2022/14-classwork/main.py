# amount = int(input('Введите кол-во чисел'))
# max = -30000
# for i in range (amount):
#     num = int(input('Число номер ' + str(i+1)))
#     if (num % 5 == 0 and num > max):
#         max = num
#     i=i+1
#
# print(max)
#
#
# amount = int(input('Введите кол-во чисел'))
# array = []
# for i in range (amount):
#     num = int(input('Число номер ' + str(i+1)))
#     if (num % 5 == 0):
#         array.append(num)
#     i=i+1
#
# print(max(array))


# amount = int(input('Введите кол-во чисел\n'))
# max = -30000
# i = 0
# while i < amount:
#     num = int(input('Число номер ' + str(i+1) + '\n'))
#     if (num % 5 == 0 and num > max):
#         max = num
#     i=i+1
#
# print(max)



num = int(input('Десятичное число: '))
sys = int(input('Перевести в систему счисления с основанием: '))
symbolArray = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']
remain = 0
output = []
while num >= sys:
    remain = num % sys
    num = num // sys
    output.append(str(symbolArray[remain]))
remain = num % sys
output.append(str(symbolArray[remain]))
print(''.join(output[::-1]))



# num = str(input('Исходное число: '))
# sys = int(input('Основание: '))
# symbolArray = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']
# print(list(num))
# indexArray = []
# i = 0
# while i < len(list(num)):
#     index = symbolArray.index(num[i])
#     indexArray.append(index)
#     i= i + 1
#     print(index)

# outArray = indexArray[::-1]
# answer = 0
# i = 0
# print()
# print()
# while i < len(outArray):
#     answer = answer + indexArray[i] * (sys ** i)

#     print(indexArray[i])
#     print(i)
#     print(sys ** i)
#     print(indexArray[i] * sys ** i)
#     print()
#     i = i + 1

# print('aeee')
# print(outArray)
# print(answer)