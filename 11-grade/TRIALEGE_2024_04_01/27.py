# k = 55

s = list(map(int, open('27a.txt').read().split('\n')))
maxi = -1

for x in range(0, len(s)-56):
    for y in range(x+55, len(s)):
        maxi = max(maxi, s[x] * s[y])

print(maxi)


#27) 9992901218 9999600004