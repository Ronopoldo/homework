# №1
# Ответ 9
for A in range(1024, 0, -1):
  i = 0
  for x in range(0,256):
    for y in range(0,256):
      if (x + y <= 22) or (y <= x - 6) or (y >= A):
        i = i + 1

  if i == 65536:
      print(A)