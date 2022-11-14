for n in range(30000,1,-1):
  n2 = bin(n)[2:]
  if n % 2 == 0:
    n2 = str(n2) + '10'
  else:
    n2 = str(n2) + '01'

  if (int(n2, 2) <= 102):
    print(int(n2, 2), n2)
    break