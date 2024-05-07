s = open('24_59849.txt').read()

alpha = '0123456789ABCDEFGHIJKLMNOP'
# MAXI = -1
# isPrev = False
# tmp = 0
# for i in s:
#     if i in alpha:
#         if isPrev:
#             tmp+=1
#         else:
#             MAXI = max(MAXI, tmp)
#         isPrev = True
#     else:
#         isPrev = False

for i in alpha:
    s = s.replace(i, '*')

maxComb = 0
while (maxComb * '*') + '*' in s:
    maxComb+=1

print(maxComb)
