# number = int(input('Введите число в десятичной СС: '))
# system = int(input('Введите СС: '))
# output = ''
# alphabet = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# while number > 0:
#     remain = number % system
#     output = alphabet[remain] + output
#     number //= system
# print(output)

for x in range(1, 1000):
  number = 5**2026 + 7 * 5**1013 + 107 - x
  output = ''
  # print(number)
  alphabet = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  while number > 0:
    output = alphabet[number % 6] + output
    number //= 6
  if (output.count('5') - output.count('0') == 28):
    print(x)
    break
