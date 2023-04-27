from sys import *

setrecursionlimit(8192)



def f(n):
    if n <= 1: return 1
    if n > 1 and n % 2 == 0: return 3 + f(n/2-1)
    if n > 1 and n % 2 != 0: return n + f(n+2)



print(f(126))
counter = 0
e = 0
while e != 19:
    try:
        e = f(counter)
    except:
        print('ae')

    print(e)
    counter+=1

print(counter)
