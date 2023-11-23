from sys import *
set_int_max_str_digits(10000000)

origin = 7 * 512 ** 1912 + 6 * 64 ** 1954 - 5 * 8 ** 1991 - 4 * 8 ** 1980 - 2022

origin2 = 7 * (512 ** 1912) + 6 * (64 ** 1954) - 5 * (8 ** 1991) - 4 * (8 ** 1980) - 2022

print(str(oct(origin)[2::]).count('7'), oct(origin)[2::])


print(str(oct(origin2)[2::]).count('7'), oct(origin2)[2::])