s = open('24.txt').read()
ALPHA = 'ABC'
NUMS = '6789'

for i in ALPHA:
    s = s.replace(i, '*')
for i in NUMS:
    s = s.replace(i, '#')

counter1 = 0
for i in range(1, len(s) // 2 - 1):
    if ('*#' * i) in s:
        counter1 += 2
    else:
        break

counter2 = 0
for i in range(1, len(s) // 2 - 1):
    if ('#*' * i) in s:
        counter2 += 2
    else:
        break

print(max(counter1, counter2))
# print(maxi)
