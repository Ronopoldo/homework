num = 343**5-7**9+48

ost = ''

while num > 0:
    ost = str(num % 7) + ost
    num//=7

print(ost.count('6'))