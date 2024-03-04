def sumOfDigits(number):
  return sum(int(digit) for digit in str(number))

for nOrigin in range(3,256):
n = '3' + '5' * nOrigin
while ('25' in n) or ('355' in n) or ('555' in n):
  if '25' in n:
    n = n.replace('25','3',1)
  if '355' in n:
    n = n.replace('355', '52', 1)
  if '555' in n:
    n = n.replace('555','23', 1)

if sumOfDigits(n) == 27:
  print(nOrigin, n)