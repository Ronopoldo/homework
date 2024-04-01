def dels(num):
    delits = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            delits.append(i)
            delits.append(num // i)
    return sorted(list(set(delits)))

def M(n):
    if len(dels(n)) < 3: return 0
    return dels(n)[-2] + dels(n)[-3]

i = 0

for n in range(10_000_000, 421564271890):
    if 0 < M(n) < 10000:
        i+=1
        if i <= 5: print(M(n))
