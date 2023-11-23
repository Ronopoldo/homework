s = open('24.txt').readline()

i = 0
maxi = 0
for letter in s:
    if letter == 'C':
        i+=1
        maxi = max(i, maxi)
    else:
        i = 0
print(maxi)