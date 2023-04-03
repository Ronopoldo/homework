# from itertools import permutations
#
#
# for m in range(1000):
#     arrange = permutations('1' * 15 + '2'* 35 + '3' * m)
#
#     for num in arrange:
#         s = '>' + ''.join(num)
#         #print(s)
#
#         while '>1' in s or '>2' in s or '>3' in s:
#             s = s.replace('>1', '2>',1)
#             s = s.replace('>2', '3>',1)
#             s = s.replace('>3', '11>', 1)
#         s = s.replace('>', '')
#         #print(int(s))
#
#         k = 0
#         for elem in s:
#             if elem.isdigit():
#                 k += int(elem)
#         print(k, m)
#         i = 0
#         for delit in range(1, k):
#             if i % delit == 0:
#                 i+=1
#
#         if i == 4:
#             print(m)


for x in range(35):

    for y in range(35):

        for z in range(35):
            s = ">" + '1' * 15 + '2' * 35 + '3' * z

        while '>1' in s or '>2' in s or '>3' in s:
            s = s.replace('>1', '2>',1)
            s = s.replace('>2', '3>',1)
            s = s.replace('>3', '11>', 1)



        k = 0
        for elem in s:
            if elem.isdigit():
                k += int(elem)

        print(s, k, z)
        i = 0
        #print(k)
        for delit in range(2, k):
            if k % delit == 0:
                k+=1

        if  i == 3:
            print(k, i)