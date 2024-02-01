s = open('24-274.txt').read().replace('CSGO', '****').replace('PC', '**')
maxi = -1
for i in range(len(s)):
    if ('*' * i) in s:
        maxi = max(maxi, i)
print(maxi)





# s = open('24-274.txt').read()
#
# s = s.replace('CSGO', '****')
# s = s.replace('PC', '**')
#
# out = []
#
# for i in range(len(s)):
#     if ('*' * i) in s:
#         out.append(i)
#     else:
#         break
#
# print(max(out))