# for n in range (100,200):
#   n2 = bin(n)[2:]
  
#   npos = n2[n2.find('1') + 1:]
#   n2 = del n2[npos, n2.find('1')]
#   if n2 != '':
#     print(n - int(n2, '2'))

answerlist = []
bufferamount = 0
for num in range(100, 3001):
  n2 = bin(num)[3:]
  opos = n2.find('1')
  n2 = n2[opos:len(n2)]
  n10 = int(n2, 2)
  if (num - n10 > 0):
    if (bufferamount != num - n10):
      answerlist.append(num - n10)
      bufferamount = num - n10


print(answerlist)


# n = [0,1,2,3,4,5,6,7]
# print(n[2])
