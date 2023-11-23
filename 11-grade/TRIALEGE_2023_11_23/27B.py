s = open('27B.txt').read().split('\n')


newArray = []
newArray2 = []
for element in s:
    newArray.append([min(map(int,[element.split(' ')[0], element.split(' ')[1]])), max(map(int,[element.split(' ')[0], element.split(' ')[1]]))])
    newArray2.append([max(map(int, [element.split(' ')[0], element.split(' ')[1]])), min(map(int, [element.split(' ')[0], element.split(' ')[1]]))])

answerArray = []

newArray.sort(reverse = True)
newArray2.sort()

final = -1
currentSum = 0


# print(newArray)
print(newArray2)

for ele in newArray:
    currentSum+=ele[1]


print(currentSum)
c = 0
while final % 3 != 0:
    final = currentSum
    final-=newArray[c][1]
    final+=newArray[c][0]
    c+=1

print('DONED', final)


# 399759471
# 399759456
