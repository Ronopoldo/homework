file = '2660_B.txt'
splitter = ' '

s = open(file).read().split('\n')

inp = []


for ele in s:
    print(ele)
    inp.append([int(ele.split(splitter)[0]), int(ele.split(splitter)[1])])

print(inp)
for ele in range(len(inp)):
    maxi = max(inp[ele][1], inp[ele][0])
    mini = min(inp[ele][1], inp[ele][0])
    inp[ele] = [maxi - mini, mini, maxi]

inp.sort()
predicted = 0
for ele in inp:
    predicted+=ele[2]

print(inp)
print(predicted)

predictedOrigin = predicted
i = 0

while predicted % 3 == 0:
    predicted = predictedOrigin - inp[i][2] + inp[i][1]
    i+=1

# 127127
# 399762080
print('ANSWER:')
print(predicted)