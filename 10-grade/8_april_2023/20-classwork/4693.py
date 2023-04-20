f = open('17-243.txt').readlines()
i = 0
while i < len(f):
    f[i] = int(f[i].replace('\n',''))
    i += 1
print(f)
finalArray = []
x6 = []

for y in range(len(f)):
    if f[y] % 119 == 0:
        x6.append(f[y])

print(min(x6), max(x6) ** 2)


for x in range(len(f) - 1):

    if (f[x] > max(x6) or f[x+1] > max(x6)) and (f[x] % 100 == 21 or f[x+1] % 100 == 21):
        finalArray.append(f[x] + f[x+1])

print(len(finalArray), min(finalArray))