
s = list(map(int, open('17.txt').read().split('\n')))
i = 0

print(s)
answerArray = []
tempArray = []
for item in s:
    if abs(item) % 10 == 6:
        tempArray.append(item)

print(min(tempArray))
print(2086 % 10)
counter= 0
for i in range(len(s) - 1):
    # if (str(s[i + 1])[len(str(s[i])) - 1] == '6' and str(s[i])[len(str(s[i])) - 1] != '6') or (str(s[i])[len(str(s[i])) - 1] == '6' and str(s[i + 1])[len(str(s[i])) - 1] != '6'):# XOR
    if ((abs(s[i]) % 10 == 6) and (abs(s[i + 1]) % 10 != 6)) or ((abs(s[i]) % 10 != 6) and (abs(s[i + 1]) % 10 == 6)):
        if ((s[i] ** 2) + (s[i+1] ** 2)) < (min(tempArray) ** 2):
            print(s[i], s[i+1])
            answerArray.append(((s[i] ** 2) + (s[i+1] ** 2)))
            counter+=1

print(counter, max(answerArray))