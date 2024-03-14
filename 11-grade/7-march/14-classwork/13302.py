def f(s, e):
    if s > e: return 0
    if s == e: return 1
    if s < e: return f(int(bin(int(int(str(s), 2) + 1))[2::]), e) + f(int(str(s) + bin(int(str(s), 2) % 5)[2::]), e)

print(f(1, 101000101))

# 1. Прибавить 1
# 2. Приписать справа двоичную запись остатка от деления на 5