f = open('3.txt').readline()
flist = list(f)


maxi = 0
counter = 0
oldCounter = 0
for i in range(1, len(f)):
    if flist[i] == 'A':
        tempCount = counter + oldCounter
        maxi = max(maxi, tempCount)
        oldCounter = counter
        counter = 0
    else:
        counter+=1
    tempCount = 1 + counter + oldCounter
    maxi = max(maxi, tempCount)
print(maxi)