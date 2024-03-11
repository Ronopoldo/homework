def DEL(m, n):
    return m % n == 0


def f(x,y,z,A):
    return ((DEL(z, 115) or DEL(y, 78) or DEL(x, 51))) <= DEL(x*y*z, A)


ae = [-1]
for A in range(1, 1024):
    tmp = 0
    for x in range(500):
        for y in range(500):
            for z in range(500):
                if f(x,y,z,A):
                    tmp+=1
                else:
                    ae.append(x)
                    ae.append(y)
                    ae.append(z)


    if tmp == 500**3:
        print(A)
        print(max(ae), x, y, z, ae)

print(max(ae))