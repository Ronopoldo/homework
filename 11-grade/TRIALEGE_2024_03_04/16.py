import sys 
sys.setrecursionlimit(2048)


def F(n):
  if n < 11: return 10
  if n >= 11: return n + F(n-1)


print(F(2021)-F(2019))