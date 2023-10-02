s = list(map(int, open('27-A.txt').readlines()))

counter = 0
for i1 in range(len(s)-1):
    for i2 in range(i1 + 14, len(s)):
        x1 = int(s[i1])
        x2 = int(s[i2])
        if ((x1 + x2) % 8 == 0) and ((x1 * x2) % 19683 == 0):
            counter+=1

print(counter)