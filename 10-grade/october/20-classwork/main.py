#  Задача 4
#  При каком наименьшем натуральном значении переменной х в выражении 81^20 – 9^х + 50 сумма цифр в девятеричной записи числа равна 138? (24)

# for x in range(1,100):
#   a = 81 ** 20 - 9 ** x + 50
#   a9 = ''
#   sum = 0
#   while a > 0:
#     sum += a % 9
#     a //= 9
#   if (sum == 138):
#     print(x)




# for x in range(1000):
#   a = 64 ** 12 - 8 ** 14 + x
#   a8 = oct(a)[2:]
#   # print(a8)
#   if (a8.count('7') == 12 and a8.count('1') == 1):
#     print(x, a8)


# for x in range(14):
#   a1 = (((1 * 15  + 2) * 15 + 3) * 15 + x) * 15 + 5
#   a2 = (((1 * 15  + x) * 15 + 2) * 15 + 3) * 15 + 3
#   if ((a1 + a2) % 14 == 0):
#     print(x, ' - chislo')
#     print ((a1+a2)/14)
#   print(a1,a2)



# for x in range(0,11):
#   for y in range(0,11):
#     a1 = 5 * 25 ** 5 + y * 25 ** 4 + 2 * 25 ** 3 + 3 * 25 ** 2 + x * 25 ** 1 + 5 * 25 ** 0
#     a2 = 6 * 11 ** 4 + 7 * 11 ** 3 + x * 11 ** 2 + 9 * 11 ** 1 + y * 25 ** 0
#     if ((a1 + a2) % 131 == 0):
#       print(x, y, (a1+a2)/ 131)
#     #67x9y

