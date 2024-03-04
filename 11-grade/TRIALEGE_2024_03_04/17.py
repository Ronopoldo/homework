s = list(map(int, open('17.txt').read().split('\n')))

maxi = -1

for ele in s:
  if ele % 10 == 3:
    maxi = max(maxi, ele)


print(maxi)

outArray = []

for i in range(len(s)-1):
  act1=(abs(s[i]) % 10 == 3)
  act2=(abs(s[i + 1]) % 10 == 3)

  # print(act1, act2)
  if act1 != act2:
    if ((s[i] ** 2) + (s[i+1] ** 2)) >= (maxi ** 2):
      outArray.append(s[i] ** 2 + s[i+1] ** 2)

# print(outArray)
print(len(outArray), max(outArray))



'''
Определите количество пар последовательности, в которых только одно число оканчивается на 3, а сумма квадратов элементов пары не меньше квадрата максимального элемента последовательности, оканчивающегося на 3. В ответе запишите два числа: сначала количество найденных пар, затем максимальную из сумм квадратов элементов таких пар. 
'''
