f = open('1.txt').readline()
flist = list(f)


maxi = 0
counter = 0

for i in range(1, len(f)):
    if flist[i] != flist[i-1]:
        counter+=1
    else:
        counter = 1

    maxi = max(maxi, counter)

print(maxi)