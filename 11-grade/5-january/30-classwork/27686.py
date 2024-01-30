s = open('27686.txt').read()
maxi = -1
for i in range(90):
    check = 'X' * i
    if check in s:
        maxi = max(maxi, i)

print(maxi)