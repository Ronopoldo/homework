s = list(map(int, open('17.txt')))

outArray = []

for i in range(len(s) - 1):
    if (s[i]  % 3 == 0) or (s[i + 1] % 3 == 0):
        outArray.append(s[i] + s[i + 1])
        print(s[i], s[i+1])


print(outArray)

print(len(outArray), max(outArray))