
f = open("27-A_2.txt")
s = f.readlines()
# print(s)
arr = []
i1 = 0
for i in range(len(s)):
    s[i] = int(s[i].replace('\n', ''))

# print(s)

for a in range(1000000):
    for b in s:
        for c in s:
            if (a  % 14 == 0 and a == (b*c)):
                arr.append(a)
                print('ae')
                print(a)


# # print(arr)
# mn = 1
# for l in range(len(arr)):
#     mn = arr[l] * mn
#     print(arr[l])
#
# print(mn)
