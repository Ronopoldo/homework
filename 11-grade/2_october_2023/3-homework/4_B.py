s = list(map(int, open('27-B.txt').readlines()))


def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10

    return sum


counter = 0
for i1 in range(len(s)-1):
    for i2 in range(i1 + 14, len(s)):
        x1 = int(s[i1])
        x2 = int(s[i2])
        if  (int(str(x2)[-1::]) * int(str(x1)[-1::]) % 3 == 0):
            if (int(str(x1 + x2)[-3::]) % 8 == 0):
                counter+=1
    print(f'{round(i1 / len(s) * 100,2)}% {counter, x1, i1}')

print(counter)