s = list(map(int, open('26.txt').read().split('\n')))

out = []

for x in range(len(s)-1):
    for y in range(x + 1, len(s)):
        if ((s[x] % 2) == 0) and ((s[y] % 2) == 0):
            if (int((s[x] + s[y]) / 2)) in s:
                out.append(((s[x] + s[y]) / 2))
                print(s[x], s[y])
    print(x)

print(len(out), max(out))

# 15 976339247.0
# 15 976339247