from itertools import product

P = set()
Q = set()
A = set()

for i in product('01',repeat=8):
    if i[0:2] == ('1', '1'):
        P.add(''.join(i))
    if i[7] == '0':
        Q.add(''.join(i))

def f(x):
    return (x not in A) <= ((x in P) or (x not in Q))

for xo in product('01', repeat=8):
    x = ''.join(xo)
    if f(x) == 0:
        A.add(x)

print(len(A), A)