file = '2669_B.txt'

s = list(map(int, open(file).read().split('\n')))
mini = 65536
for i in range(len(s) - 6):
    for l in range(i + 6, len(s)):
        if (s[i] * s[l]) % 2:
            mini = min(mini, s[i] * s[l])
    print(i)
print(mini)