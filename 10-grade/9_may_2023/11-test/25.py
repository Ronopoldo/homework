a = [i for i in range(174457, 174506)]

print(a)


def dels(n):
    delss = []
    for i in range(1, n+1):
        if n % i == 0:
            delss.append(i)

    return delss

for a in range(174457, 174506):
    if len(dels(a)) == 4:
        print(dels(a))