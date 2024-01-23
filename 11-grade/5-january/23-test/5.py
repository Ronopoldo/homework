# def f(n):
#     if (n == 0): return 0
#     if (n > 0) and ((n % 3) == 2): return f(n-1) + 1
#     if (n > 0) and ((n % 3) < 2): return f((n - n % 3) / 3)
#
# mini = 8192
#
# for n in range(8192):
#     if f(n) == 5:
#         mini = min(mini, n)
#
#
# print(mini)
#






def f(n):
    if n == 0: return 0
    if (n > 0) and ((n % 3) == 2): return f(n-1) + 1
    if (n > 0) and ((n % 3) < 2): return f((n - n % 3) / 3)
mini = 8192
for n in range(8192):
    if f(n) == 5:
        mini = min(mini, n)


print(mini)
