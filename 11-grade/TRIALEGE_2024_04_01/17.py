s = list(map(int, open('17.txt').read().split('\n')))


mini = 65536

for ele in s:
    if ele % 21 == 0:
        mini = min(mini, ele)

out = []

for i in range(len(s) - 1):
    a1 = s[i] % mini == 0
    a2 = s[i+1] % mini == 0

    if (a1 + a2) > 0:
        out.append(s[i] + s[i+1])


print(len(out), max(out))