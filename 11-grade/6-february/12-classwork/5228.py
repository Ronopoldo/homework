s = list(map(int, open('26_5228.txt').read().split('\n')))



sortedS = sorted(s)

def calculate(startPos, sortedArray):
    answer1 = 1
    tempVar = list(set(sortedArray))[startPos]
    for i in range(len(sortedArray) - 1):
        if ((sortedArray[i + 1] - tempVar) >= 8):
            answer1+=1
            tempVar = sortedArray[i + 1]
    return answer1

temp = 0

while calculate(temp+1, sortedS) == calculate(0, sortedS):
    temp += 1
print(calculate(0, sortedS))
print(list(set(sortedS))[temp])