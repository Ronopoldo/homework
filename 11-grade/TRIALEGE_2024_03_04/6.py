for N in range(2048):
  
  N2 = bin(N)[2::]
  
  
  if N % 3 == 0:
    N2+=N2[-3::]
  else:
    N2+=bin((N % 3) * 3)[2::]
  
  if ( int(N2, 2) > 151):
    print(int(N2, 2), N, N2)
    break
