for A in range(1000,-1,-1):
  i = 0
  for x in range(0, 100):
    for y in range(0, 100):
      if ((2*x+y)!=70) or (x < y) or (A < x):
        i+=1
  if i == 10000:
    print(A, i)
  # print(A, '/ 128')
#23

# i = 0
# for x in range(0, 100):
#   for y in range(0, 100):
#     i= i + 1
    
# print(i)