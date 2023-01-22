for A in range(0,100,1):
  i = 0
  for x in range(0, 100):
    if ((x&25!=0) <= ((x&19 == 0) <= (x & A !=0))):
      i=  i  + 1
  if i == 100:
    print(A)

#8



# i = 0
# for x in range(0, 100):
#     i = i + 1
# print(i)