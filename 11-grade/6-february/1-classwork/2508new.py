s = open('k8.txt').read()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
out = []

for i in alpha:
    tmp = 1
    while (i * tmp) in s:
        tmp+=1
    out.append((i * (tmp-1)))

final = []
for s in range(256, 0, -1):
    for e in out:
        if len(e) == s:
            final.append([out.index(e), [f'{e[0]} {len(e)}']])

print(list(map(sorted, final)))
