
def F(n):
  if n > 0: G(n - 1)

out = []
def G(n):
  print("*")
  out.append('*')
  if n > 1: F(n - 3)


print(F(11), len(out))