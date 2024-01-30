s = open('33494.txt').read()

finalArray = []
finalObj = {}

for i in range(s.count('E')):
    finalArray.append(s[s.index('E') + 1])
    s = s.replace('E', '', 1)

for letter in finalArray:
    finalObj[letter] = finalArray.count(letter)

maxi = max(finalObj.values())
finalObjReverse = dict(zip(finalObj.values(), finalObj.keys()))
print(finalObjReverse[maxi])