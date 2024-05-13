def F(n):
    if n <= 2: return n
    if n > 2: return F(n-1) + 3*F(n-2)
print(F(6))