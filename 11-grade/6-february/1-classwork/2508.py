s = open('k8.txt').read()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
out = []

for i in alpha:
    tmp = 1
    while (i * tmp) in s:
        tmp+=1
    out.append((i * (tmp-1)))

activate = 2
for s in range(256, 0, -1):
    for e in out:
        if len(e) == s:
            print(f'{out.index(e)}: {e[0]} {len(e)}')
            activate-=1
    if activate == 0:
        s = -2323
        break
