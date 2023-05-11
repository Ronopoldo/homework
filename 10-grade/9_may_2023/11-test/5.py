def counter(n):
    n = str(n)
    tmp = 0
    for i in n:
        tmp+=int(i)
    return tmp

for n in range(8192):
    N2 = bin(n)[2::]
    Nstr = str(N2) + str(counter(N2) % 2)
    Nstr1 = str(Nstr) + str(counter(int(Nstr)) % 2)
    if int(Nstr1,2) > 85:
        print(n, Nstr1)