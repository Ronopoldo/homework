# num = 9**8 + 3 ** 5 - 2
#
# print(num)
# ost = ''
# while num > 0:
#     ost = str(num % 3) + ost
#     num//=3
# print(ost.count('2'), ost)






# for x in range(1,4096):
#     if (int('34', 5) + x == int('34', 7)):
#         print(oct(x))
#         print('ae')
#
# print(int('34', 5), int('34', 7) )
#


#
# print(int('34', 8), int('3400',8))
#




# num = 86
# ost = ''
# while num > 0:
#     ost = str(num % 5) + ost
#     num //= 5
# print(ost)
# print(int(ost, 5))



#
# for n in range(2,8192):
#     num = 180
#     ost = ''
#     while num > 0:
#         ost = str(num % n) + ost
#         num //= n
#
#     if (len(ost) == 3 and 180 % n == 0):
#         print(n, ost, ost.count(''))
#






# num = 4**255 + 2 ** 255 - 255
# print(bin(num))
# print(bin(num).count('1'))




# num = 49 ** 7 * 7 ** 20 - 7 ** 8 - 28
# ost = ''
# while num > 0:
#     ost = str(num % 7) + ost
#     num //= 7
# print(ost.count('6'))
# print(ost)
# print(int(ost, 7))
# print(49 ** 7 * 7 ** 20 - 7 ** 8 - 28 == int(ost, 7))




# for x in range(2,8192):
#     num = 21
#     ost = ''
#     while num > 0:
#         ost = str(num % x) + ost
#         num //= x
#     if (ost == '30'):
#         print(x)
#         print(int(ost, x))
#
# print(int('30', 7))










# for x in range(2,16384):
#     if (75 % x == 3 and 75 // x % x == 1):
#         print(x, 75 % x , 75 // x % x )









# for x in range(2, 16384):
#     num = 12
#     ost = ''
#     while num > 0:
#         ost = str(num % x) + ost
#         num //= x
#     if (ost == '110'):
#         print(x, ost)
# print(int('110', 3))