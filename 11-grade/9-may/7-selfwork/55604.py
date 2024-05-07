s = list(map(int, open('55604.txt').read().split('\n')))

mini = 10001

for i in range(len(s)):
    if str(s[i])[-2::2] == str(s[i])[-1::1]:
        mini = min(mini, s[i])

print(mini)

out = []

for x in range(len(s) - 1):
    if (str(s[x])[-1::] == str(s[x + 1])[-2::2]) or (str(s[x + 1])[-1::] == str(s[x])[-2::2]):
        is1 = (abs(s[x]) % 7) == 0
        is2 = (abs(s[x + 1]) % 7) == 0
        if is1 ^ is2:
            if ((s[x] ** 2) + (s[x + 1] ** 2)) <= mini ** 2:
                out.append((s[x] ** 2) + (s[x + 1] ** 2))

print(len(out), max(out))