s = open('5827.txt').read()

alpha = 'ABCDEFGIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
finaleArray = []

for i in range(len(s) - 1):
    if s[i] in alpha:
        j = i+1
        temp = ''
        while s[j] in numbers:
            temp+=s[j]
            j+=1
        finaleArray.append(temp)

for i in range(len(finaleArray)):
    if len(finaleArray[i]) > 0:
        finaleArray[i] = int(finaleArray[i])
    else:
        finaleArray[i] = 0


print(max(finaleArray))