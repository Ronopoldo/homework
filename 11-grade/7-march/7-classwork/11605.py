length = 10000

s = open('12478.txt').read().split('\n')

origin = []

for ele in s:
    origin.append([int(ele.split(' ')[0]), int(ele.split(' ')[1])])

print(sorted(origin,reverse=True))

origin = []
