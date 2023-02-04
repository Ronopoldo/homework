from itertools import product

arrange = product('УЧЕНИК', repeat = 5)
counter = 0

for word in arrange:
  if word[0] == 'У' and word[4] == 'К':
    counter += 1

print(counter)