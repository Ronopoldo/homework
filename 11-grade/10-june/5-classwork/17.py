s = list(map(int, open('331_17.txt').read().split('\n')))

max121 = -99999

for ele in s:
    if abs(ele) % 1000 == 121:
        max121 = max(max121, ele)

ans = []

for id in range(len(s) - 2):
    act = 0
    act += ((len(str(abs(s[id]))) == 4) and (abs(s[id]) % 2 == 0))
    act += ((len(str(abs(s[id + 1]))) == 4) and (abs(s[id + 1]) % 2 == 0))
    act += ((len(str(abs(s[id + 2]))) == 4) and (abs(s[id + 2]) % 2 == 0))
    if act <= 1:
        if (s[id] + s[id + 1] + s[id + 2]) <= max121:
            ans.append(s[id] + s[id + 1] + s[id + 2])

print(len(ans), max(ans))