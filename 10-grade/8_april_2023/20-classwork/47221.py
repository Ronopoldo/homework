f = open('1.txt').readlines()
i = 0
while i < len(f):
    f[i] = int(f[i].replace('\n',''))
    i += 1
print(f)
finalArray = []
x6 = []

for y in range(len(f)):
    if abs(f[y])%10 == 3:
        x6.append(f[y])

print(min(x6), max(x6) ** 2)


for x in range(len(f) - 1):
    lol = 0
    if abs(f[x])%10 == 3:
        lol+=1
    if abs(f[x+1])%10 == 3:
        lol+=1
    if (lol == 1) and ((f[x] ** 2 + f[x+1] ** 2) >= max(x6) ** 2):
        finalArray.append(f[x] ** 2 + f[x+1] ** 2)

print(len(finalArray), max(finalArray))