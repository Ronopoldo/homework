mini = 91237182903

for N in range(0, 1024):
  N2 = bin(N)[2::]
  if N % 3 == 0:
    N2+=N2[-3::]
  else:
    N2+= bin ( ( N % 3  ) * 3)[2::]
  
  if (int(N2, 2) > 151):
    mini = min(mini, int(N2, 2))


print(mini)