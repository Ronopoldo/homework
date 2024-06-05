# alpha = '0123456789ABCDEFGHI'
#
# for x in alpha:
#     if (int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)) % 18 == 0:
#         print(x)
#         print(alpha.index(x))
#         print((int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)) / 18)
#         print()

i = 0

num = 2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27 ** 2020 - 2 * 9 ** 2022 - 2024

while num > 0:
    if num % 27 > 9:
        i+=1
    num//=27

print(i)