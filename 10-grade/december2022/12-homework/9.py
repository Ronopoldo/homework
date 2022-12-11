x = 9 ** 7 + 3 ** 21 - 9
ost = 0
answer = ''
while x > 0:
    ost = x % 3
    answer = str(ost) + answer
    x //= 3

print(answer.count('2'), answer)