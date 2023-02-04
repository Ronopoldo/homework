# Предпоследний
num = 4 ** 12 + 2 ** 32 - 16

#
# print(bin(num).count('1'))
# print(bin(num))
#

# print(int('b', 16))
#




# print(57 % 56)
alphabet = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

for x in range(0,14):
    for y in range(0,15):
        if ((int('90' + alphabet[x] + '4' + alphabet[y], 15) + int('91' + alphabet[x] + alphabet[y] + '2', 16)) % 56 == 0):
            print(x,y,(int('90' + alphabet[x] + '4' + alphabet[y], 15) + int('91' + alphabet[x] + alphabet[y] + '2', 16)) / 56)
            print("pabeda")
        # print(x,y)
        # print(alphabet[x], alphabet[y])
        # print(int('90' + alphabet[x] + '4' + alphabet[y], 15) + int('91' + alphabet[x] + alphabet[y] + '2', 16) % 56)
        # print('90' + alphabet[x] + '4' + alphabet[y], '91' + alphabet[x] + alphabet[y] + '2')
        # print()