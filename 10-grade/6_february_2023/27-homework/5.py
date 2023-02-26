out = set()

for N in range(100,3000):
    N2 = bin(N)[2::]
    print(N2)
    Nmod = list(str(N2))
    Nmod[Nmod.index('1')] = '0'
    N2 = "".join(Nmod)
    print(N2)
    print()
    Nnew = int(N2, 2)
    print(N, Nnew, N2, bin(N))

    out.add(N - Nnew)

print(out)

print(int('00101', 2))
print(int('101', 2))

# 6 (ПРОВЕРЕНО)