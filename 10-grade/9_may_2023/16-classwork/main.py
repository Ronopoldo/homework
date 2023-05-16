f = open("26_2686.txt").read()

f = f.split('\n')
fin = []
for i in range(len(f)):
    fin.append(f[i].split(' '))
print(fin)

dict = {}

for e1 in range(len(fin) - 1):
    dict[fin[e1][0]] = list()

print(fin)

for e in range(len(fin) - 1):
    # print(dict[fin[e][0]])
    if dict[fin[e][0]] == None:
        dict[fin[e][0]] = [].append("".join([fin[e][1]]))
    else:
        dict[fin[e][0]] = dict[fin[e][0]].append("".join([fin[e][1]]))


print(dict)
