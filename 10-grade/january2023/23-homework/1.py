def d(n, m):
  return n % m == 0

for A in range(999, 0, -1):
  i = 0
  for x in range(1, 999):
    if ((not d(x,A)) <= (d(x,6) <= (not d(x,4)))):
      i = i + 1
  if (i == 998):
    print(A)
      # print(A,x,i)
#12