s = open('17_2024.txt').read().split('\n')

max13 = 0
for i in range(len(s)-3):
    if int(s[i]) % 100 == 13:
        max13 = max(max13, int(s[i]))

counter = 0
for i in range(len(s)-3):
    ae = 0
    if len(str(s[i])) == 3: ae +=1
    if len(str(s[i + 1])) == 3: ae +=1
    if len(str(s[i + 2])) == 3: ae +=1

    if ae == 2 and (s[i] + s[i + 1] + s[i + 2]):
        counter+=1


print(counter)