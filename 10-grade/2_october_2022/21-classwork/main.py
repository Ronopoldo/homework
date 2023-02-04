# answer = ''
# for x in range(3, 32):
#     if (int('121', x) + 1 == int('101', 7)):
#         while x > 0:
#             ost = x % 3
#             answer = str(ost) + answer
#             x //= 3
#         print(answer)


# for i in range(1, 2048):
#     if ((56 % i == 1) and (45 % i == 1)):
#         print(i)





# x = 338
# amount = 0
# for i in range(2,10):
#
#     while x > 0:
#         x = x // i
#         amount = amount + 1
#
#     if (amount == 3 and 338 % i == 2):
#         print(i)
#     # print(amount, x)
#
#     amount = 0
#     x = 338
#






# for x in range(6,36):
#     for y in range(6, 36):
#         if (int('225', x) == int('405',  y)):
#             print(x, y)





#
# number = ''
# for i in range(0, 51):
#     # if ((str(bin(i))[len(str(bin(i)))-1] == 1) and (str(bin(i))[len(str(bin(i)))-2] == 1) and (str(bin(i))[len(str(bin(i)))-3] == 0)):
#     #     print('aeeee')
#     # print(str(bin(i))[len(str(bin(i)))-1], str(bin(i))[len(str(bin(i)))-2], str(bin(i))[len(str(bin(i)))-3])
#     # print(bin(i))
#     # print()
#
#     while i > 0:
#         number = str(i % 2) + number
#         i//=2
#     if (number[-3::] == '011'):
#         print(number)
#
#     # if (number == '1'):
#     #     print(number)
#     number = ''










# for i in range(0, 51):
#     if (hex(i)[-1::] == 'c'):
#         print(i)
#

#
#
# for i in range(10, 100):
#     if (hex(i)[-1::] == 'a' and i % 5 == 3):
#         print(i)
































# РЕШУЕГЭ

# x = 125 + 25 ** 3 + 5 ** 9
# answer = ''
# while x > 0:
#     answer = str(x % 5) + answer
#     x //= 5
#
# print(answer.count('0'))


    #15









# x = 2 * 216 ** 8 + 4 * 36 ** 12 + 6 ** 15 - 1296
# answer = ''
# while x > 0:
#     answer = str(x % 6) + answer
#     x //= 6
#
# print(answer.count('0'))




# answer = ''
# for N in range(3, 36):
#     i = N
#     while i > 0:
#         answer = str(i % N) + answer
#         i //= N
#     if (len(answer) >= 3 and 87 % N == 2):
#         print(N, answer, i)
#     # answer = ''
#
# #5


#
# answer = ''
# for x in range(10, 18):
#     i = x
#     while i > 0:
#         answer = str(i % 5) + answer
#         i //= 5
#
#     print(answer.count('2'))
#     answer = ''



# answer = ''
# for x in range(2,2048):
#     n = 343 ** 5 + 7 ** 3 - 1 - x
#     while n > 0:
#         answer = str(n % 7) + answer
#         n //= 7
#     if (answer.count('6') == 12):
#         print(x)
#     # print(n, answer)
#     answer = ''
