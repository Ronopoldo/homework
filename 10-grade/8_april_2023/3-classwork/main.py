f = open('26_6056.txt')
data = f.readlines()

result = list(reversed(sorted(list(map(int, data)))))
print(result)
current = 9998
i1 = 1
blox = 0

while len(result) > 0:
    indexesArr = []
    for i in range(len(result)):
        if (current - result[i]) >= 7:
            current = result[i]
            i1+=1
            indexesArr.append(i)
    print('123')
    print(len(indexesArr))
    print(len(result))
    for i in range(len(indexesArr)):
        a = result.pop(indexesArr[i])
    blox+=1
    #print('1')
    print(result)
    print('1GOTCHA')

print(i1)
print(blox)
print(current)