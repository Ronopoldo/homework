f = open('2.txt').readlines()
i = 0
while i < len(f):
    f[i] = int(f[i].replace('\n',''))
    i += 1
print(f)

finalArray = []

for x in range(len(f)-1):
        if (f[x] % 3 == 0) or (f[x+1] % 3 == 0):
            finalArray.append(f[x] + f[x+1])

print(len(finalArray), max(finalArray))