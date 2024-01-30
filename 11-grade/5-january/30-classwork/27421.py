s = open('27421.txt').read()

counter = 0
maxi = -1

for i in range(len(s) - 1):
    counter += 1
    maxi = max(maxi, counter)
    if s[i] == s[i + 1]:
        counter = 0

print(maxi)
