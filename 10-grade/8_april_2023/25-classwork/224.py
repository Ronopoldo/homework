def f(n):
    if n == 1: return 1
    if n % 2 == 0: return n*n+f(n-1)
    if n % 2 != 0: return f(n-1) + 2 *  f(n-2)

print(f(23))