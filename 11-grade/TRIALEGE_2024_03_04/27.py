# 55

s = list(map(int, open('27B_59826.txt').read().split('\n')))

outArray = []

sortedS = sorted(s, reverse=True)


# print(sorted(s[0:len(s)])[-1])

for x1 in range(len(s) - 245):
  x = s.index(sortedS[x1])
  y = sorted(s[x+245:len(s)] + s[x-245:len(s)])[-1]
  # if abs(x - s.index(y)) >= 245:
  outArray.append(s[x] * y)
  print(max(outArray))




# 9 992 901 218