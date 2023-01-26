# №2
# Ответ 90
def d(n, m):
  return n % m == 0

for A in range(1, 1024):
  i = 0
  for x in range(1,512):
    if d(A, 9) and (d(280,x) <= ((not d(A,x)) <= (not d(730, x)))):
      i = i + 1
  if i == 511 or i == 512 or i == 510:
    print('Ответ ', A, i)
    
  
