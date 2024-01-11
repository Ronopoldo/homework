s = list(map(int, open('17.txt').read().split('\n')))


maxi = -42617845
for i in s:
    if (abs(i) % 10 == 3) and (10_000 <= i < 100_000):
        maxi = max(maxi, i)

print(maxi)

correct = []

for i in range(len(s) - 2):
    if (abs(s[i]) % 10 == 3) or (abs(s[i + 1]) % 10 == 3) or (abs(s[i + 2]) % 10 == 3):
        if (s[i] + s[i + 1] + s[i + 2]) <= maxi:
            correct.append(s[i] + s[i + 1] + s[i + 2])


print(len(correct), max(correct))