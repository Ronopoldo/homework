a = 45
c = 43
for b in range(0,9999):
    if (not (a == b) and ((a > b) <= (b > c)) and ((b > a) <= (c > b))):
        print(b)
        break