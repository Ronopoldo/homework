A = set([i for i in range(1,1024)])
P = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
Q = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31}
def f(x):
    return ((x in A) <= (x in P)) and ((x in Q) <= (x not in A))


for x in range(1, 1024):
    if f(x) == 0:
        A.remove(x)

print(len(A), A)