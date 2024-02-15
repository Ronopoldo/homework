s = open('26_13101.txt').read().split('\n')[1:]

separated = []

# print(s)

for i in range(len(s) - 1):
  sSpl = s[i].split(' ')
  separated.append([int(sSpl[0]), int(sSpl[1]), int(sSpl[2])])
  # print(sSpl)


separated = sorted(separated)
# print(separated)


def timeCalc(inputArray):
  if len(inputArray) >= 1:
    inputArray[0] = inputArray[0] - 1
    if inputArray[0] == 0:
      inputArray = inputArray[::-1][:-1:][::-1]
    return inputArray
  return []

    

w1 = []
w2 = []

cou = 1
uncou = 1
curr = 0
print(separated)

for i in range(1000):
  obj = separated[curr]
  print(obj)

  if i == obj[0]:
    if curr < len(separated) - 1:
      curr+=1
    if obj[2] == 0:
      if len(w1) <= len(w2):
        if len(w1) < 14:
          w1.append(obj[1])
        else:
          uncou+=1
      else:
        if len(w2) < 14:
          w2.append(obj[1])
          cou+=1
        else:
          uncou+=1
      print('ae')
    else:
      if obj[2] == 1:
        if len(w1) < 14:
          w1.append(obj[1])
        else:
          uncou+=1
        
      else:
        if len(w2) < 14:
          w2.append(obj[1])
          cou+=1
        else:
          uncou+=1
  w1 = timeCalc(w1)
  w2 = timeCalc(w2)

print(cou, uncou)

#126 469
# 252