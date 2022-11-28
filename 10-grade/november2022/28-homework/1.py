from itertools import product

arrange = product('ABCX', repeat = 5)
counter = 0
for word in arrange:
  if word[1] != 'X' and word[2] != 'X' and word[3] != 'X' and word[4] != 'X':
      counter += 1


print(counter)