f = open('17-205.txt').readlines()
i = 0
while i < len(f):
    f[i] = int(f[i].replace('\n',''))
    i += 1
print(f)

finalArray = []

for x in range(len(f)-1):
        if (abs(f[x] - f[x+1]) % 2 == 0 and abs(f[x] - f[x+1]) % 37 == 0):
            finalArray.append(f[x] + f[x+1])


print(finalArray)

print(len(finalArray), max(finalArray))