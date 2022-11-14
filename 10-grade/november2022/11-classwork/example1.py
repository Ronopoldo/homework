for n in range(1,30000):
  n2 = bin(n)[2:]
  n2 = str(n2) + str(n2.count('1') % 2)
  n2 = str(n2) + str(n2.count('1') % 2)
  if int(n2, 2) > 43:
    print(int(n2, 2), n2)
    break