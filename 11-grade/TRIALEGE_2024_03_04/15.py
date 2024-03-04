def f(x, A):
  return (120 % A == 0) and (not (x % A == 0)) <= ((x % 18 == 0) <= (not (x % 24 == 0)))

for A in range(1, 256):
  i = 0
  for x in range(1, 256):
    if f(x,A): i+=1
  if i == 255:
    print(A)