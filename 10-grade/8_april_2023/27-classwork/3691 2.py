from sys import *

setrecursionlimit(8192)



def f(n, lim):
    if n == -1:
        return(-1)
    if n <= 1: return 1
    if n > 1 and n % 2 == 0: return 3 + f(n/2-1, lim)
    if n > 1 and n % 2 != 0: return n + f(n+2, lim)
    if lim > 16:
        return -1



#print(f(126, 0))
counter = 0
e = 0
while e != 19:
    e = f(counter, 0)
    counter+=1

    print(counter)
