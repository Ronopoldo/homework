def isDel(n):
    return n % 11 == 0

def f(n):
    if n > 25: return 2 * n * n * n + 1
    if n <= 25: return f(n+2) + 2 * f(n+3)


out = 0
for i in range(1,1001):
    if (isDel(f(i))):
        out+=1

print(out)