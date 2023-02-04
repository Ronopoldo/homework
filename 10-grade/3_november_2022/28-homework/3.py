from itertools import product

arrange = product('ABCDXYZ', repeat = 4)
counter = 0
mustHave = ['X', 'Y', 'Z']

for word in arrange:
  if (word[0] in mustHave) and (word[1] not in mustHave) and (word[2] not in mustHave) and (word[3] not in mustHave):
    counter += 1

print(counter)