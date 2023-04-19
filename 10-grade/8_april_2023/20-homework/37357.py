f = open('1.txt').readlines()
i = 0
while i < len(f):
    f[i] = int(f[i].replace('\n',''))
    i += 1
print(f)

finalArray = []

for x in range(len(f)):
    for y in range(x + 1, len(f)):
        if (f[x] + f[y]) % 8 == 0:
            finalArray.append(f[x] + f[y])

print(len(finalArray), max(finalArray))