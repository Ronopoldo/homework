min = 30000

for num in range(30000):
    num2 = bin(num)[2::]
    if num % 2 == 0:
        num2 = '1' + num2 + '0'
    else:
        num2 = '11' + num2 + '11'

    num10 = int(num2, 2)

    if num10 > 52:
        if num10 < min:
            min = num10


print(min)


#56