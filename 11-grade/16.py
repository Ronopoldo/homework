from sys import *

setrecursionlimit(65_536)

def F(n):
    if n<=7: return 1
    if n>7: return n + 2 + F(n-1)

print(F(2024)-F(2020))