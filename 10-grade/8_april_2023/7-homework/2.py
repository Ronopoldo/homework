f = open('2.txt').readline()
flist = list(f)


maxi = 0
counter = 0

for i in range(1, len(f)):
    if flist[i] == 'C':
        counter+=1
    else:
        counter = 0

    maxi = max(maxi, counter)

print(maxi)