num = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
ost = ''
# while num > 0:
#     ost = str(num % 9) + ost
#     num//=9
#
# print(len(ost) - ost.count('0'))

i = 0
while num > 0:
    if num % 9 > 0:
        i+=1
    num //= 9

print(i)