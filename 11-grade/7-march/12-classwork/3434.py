A = set([i for i in range(1,1024)])
P={2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q={5, 10, 15, 20, 25, 30, 35, 40, 45, 50}

def f(x):
    return ((x in A) <= (x in P)) or ( (x not in Q) <= (x not in A) )


for x in range(1, 1024):
    if f(x) == 0:
        A.remove(x)

print(len(A), A)