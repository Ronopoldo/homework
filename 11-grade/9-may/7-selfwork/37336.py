s = list(map(int, open('37336.txt').read().split('\n')))

out = []

for x in range(len(s) - 1):
    is1 = s[x] % 3 == 0
    is2 = s[x + 1] % 3 == 0

    if is1 or is2:
        out.append(s[x] + s[x + 1])

print(len(out), max(out))