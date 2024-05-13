s = list(map(int, open('17.txt').read().split('\n')))

cou = 0
maxi = []

for x in range(len(s) - 1):
    for y in range(x + 1, len(s)):
        if ((s[x] - s[y])) % 80 == 0:
            maxi.append(s[x] - s[y])
print(maxi)
print(len(maxi), max(maxi))


