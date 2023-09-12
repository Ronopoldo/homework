# al = '0123456789ABCDEFGHIJKL'
#
# for n in range(18, 0, -1):
#     lol = int('98897' + al[n] + '21', 19) + int('2' + al[n] + '923', 19)
#     if lol % 18 == 0:
#         print(lol // 18)
#         break


num = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125**5 - 2 * 25**4 - 2024
ost = ''
while num > 0:
    ost = str(num % 25) + ost
    num //= 25

print(ost.count('0'))