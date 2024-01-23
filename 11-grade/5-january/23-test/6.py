s = list(map(int, open('17.txt').read().split('\n')))

mini = 20000

for ele in s:
    if ((99<ele<1000) and (ele % 10 == 5)):
        mini = min(mini, ele)

print(mini)



out = []

for cur in range(len(s) - 1):
    if ((999 < s[cur] < 10000) and not(999 < s[cur + 1] < 10000)) or (not (999 < s[cur] < 10000) and (999 < s[cur + 1] < 10000)):
        if ((s[cur]) ** 2 + (s[cur+1])**2) % mini == 0:
            out.append(((s[cur]) ** 2 + (s[cur+1])**2))

print(len(out), max(out))
print(out)