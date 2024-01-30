s = open('35482.txt').read().split('\n')

def f(s):

    s = sorted(s)[::-1]
    finalArray = []
    finalObj = {}

    # for i in range(len(s)):
    #     finalArray.append(s[i])
    #

    for letter in finalArray:
        finalObj[letter] = s.count(letter)
        s = s.replace(letter, '')

    print(finalObj)
    maxi = max(finalObj.values())
    finalObjReverse = dict(zip(finalObj.values(), finalObj.keys()))
    return finalObjReverse[maxi]


mini = 32768

for i in s:
    mini = min(s.count('G'), mini)

for i in s:
    if s.count('G') == mini:
        print(f(i))
        break
