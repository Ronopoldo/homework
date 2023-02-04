alpha2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
alpha1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
for x in range(0, 11):
    for y in range(0, 11):
        num = (int(alpha1[x] + '341' + alpha1[y], 11) + int('56' + alpha2[x] + '1' + alpha2[y], 19))
        if (num % 305 == 0):
            print(num)
            print(num / 305)
            print(x, y)
            print()
            break

# 2778 ( ПРОВЕРИТЬ)
# x 10     y 2
# ПРОВЕРЕНО