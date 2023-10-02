s = list(map(int, open('26.txt').readlines()))

maxSum = 0
counter = 0
print(s)
uniqueNums = set(s)

for i1 in range(len(s)-1):
    for i2 in range(i1 + 1, len(s)-1):

        x1 = int(s[i1])
        x2 = int(s[i2])
        if ((x1 % 2) != (x2 % 2)) and ((x1+x2) in uniqueNums):

            maxSum = max(maxSum, x1+x2)
            counter+=1
    print(f'{round(i1 / len(s) * 100,2)}% {counter, maxSum, x1, i1}')

print(counter, maxSum)