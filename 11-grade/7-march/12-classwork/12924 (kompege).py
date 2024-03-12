A = set([i for i in range(1,1024)])
P = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = { 3, 6, 9, 12, 15, 18, 21, 24, 27, 30 }
def f(x):
    return ((x in A) <= (x in P)) and ((x not in Q) <= (x not in A))


for x in range(1, 1024):
    if f(x) == 0:
        A.remove(x)

print(len(A), A)