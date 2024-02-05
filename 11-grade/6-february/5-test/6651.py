s = open('6651.txt').read()

s = s.replace('BAD', '*')
s = s.replace('FAT', '*')

outList = [65536]

for i in range(len(s) - 1):
    if s[i] == '*':
        j = i + 1
        tempaCount = 0
        remaining = 2
        while remaining > 0:
            if s[j] == '*':
                remaining-=1
            else:
                tempaCount+=1
            j+=1
            if j == len(s) - 1:
                remaining = 0
        outList.append(tempaCount + 9)
    # print(i / len(s) * 100)
print(min(outList))

