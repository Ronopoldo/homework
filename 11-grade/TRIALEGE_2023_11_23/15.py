P = list(range(130, 172))
Q = list(range(150, 186))

def f(P, Q, x, A):
    return (x in P) <= (((x in Q) and (not(x in A))) <= (not (x in P)))


for APos in range(128):
    i = 0
    for ALen in range(128):
        for x in range(128):
            A = list(range(APos, ALen + 1))
            if f(P, Q, x, A) == 1:
                i+=1
    if i == 128**2:
        print(ALen)