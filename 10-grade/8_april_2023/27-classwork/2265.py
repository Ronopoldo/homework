def f(n):
    if n<=3: return n
    if 3<n<=32: return n // 4 + f(n-3)
    if n > 32: return 2 * f(n-5)

print(f(100))