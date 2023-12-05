def exchange(num):
    outSum = 0
    for n in num:
        if n == '1':
            outSum+=1

    return str(int(outSum % 2))

for n in range(1024):
    n2 = bin(n)[2::]
    n2 = n2 + exchange(n2)
    n2 = n2 + exchange(n2)

    if int(n2, 2) >= 83:
        print(n)
