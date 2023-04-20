f = open('17-288.txt').readlines()
i = 0
while i < len(f):
    f[i] = int(f[i].replace('\n',''))
    i += 1
#print(f)

def tox7(num):
    ost = ''
    res = ''
    while num > 0:
        ost = num % 7
        num = num // 7
        res = str(ost) + res
    return(int(res))


finalArray = []

for x in range(len(f)-2):
        tempArray = []
        tempArray.append(tox7(abs(f[x])) % 10)
        tempArray.append(tox7(abs(f[x+1])) % 10)
        tempArray.append(tox7(abs(f[x+2])) % 10)

        if (len(set(tempArray)) == 3) and (((f[x]) < 0) or ((f[x+1]) < 0) or ((f[x+2]) < 0)):
            finalArray.append(max(f[x],f[x+1],f[x+2]) - min(f[x],f[x+1],f[x+2]))

print(len(finalArray), min(finalArray))

#Запишите в ответе количество троек элементов последовательности, в которых семеричные
# записи всех чисел оканчиваются на разные цифры и хотя бы одно число отрицательно.
