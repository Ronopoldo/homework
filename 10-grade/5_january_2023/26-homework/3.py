# №3
# Ответ 2
for A in range(0,1024):
  i = 0
  for x in range(1,4096):
    if (x & 53 == 0) <= ( (x& 19 != 0) <= (x & A != 0) ):
      i = i + 1
  if i == 4095:
    print(A, i)