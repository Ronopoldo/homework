from math import *

def dels(num):
    delit = []

    for i in range(1, floor(num ** 0.5) + 1):
        if num % i == 0:
            delit.append(i)
            delit.append(int(num / i))

    return sorted(set(delit))

def m(n):
    delits = dels(n)
    temp = 1
    if len(delits) < 6:
        return 0
    else:
        for i in range(1,6):
            temp=temp*delits[i]
    return temp

for n in range(500_000_001, 999999999999):
    if 0 < m(n) < n:
        print(m(n))






# 1008
# 1797092
# 48408867
# 1800
# 1156923

