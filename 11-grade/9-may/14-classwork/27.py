s = list(map(int, open('27-B.txt').read().split('\n')))

i = 0
obj = {}

for i in range(-100_000,100_001):
    obj[i] = 0

for ele in s:
    obj[ele]+=1

temp = []
for i in range(-100_000,100_001):
    temp.append(i)



for x in range(0, len(temp) - 1):
    for y in range(x, len(temp)):
        print(x)

# for x in range(len(s) - 19):
#     for y in range(x+18, len(s)):
#         tmp.append(s[x] * s[y])
#     print(x / len(s))
# print(tmp)

# 350