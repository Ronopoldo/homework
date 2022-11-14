for n in range(0,256):
  n2 = bin(n)[2:]
  n2 = '0' * (8-len(n2)) + n2
  n2 = n2.replace('1', '🍅').replace('0', '1').replace('🍅', '0')
  if int(n2, 2) - n == 133:
    print(n)
    break
    