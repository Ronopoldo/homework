a = set()
P={2,4,6,8,10,12,14,16,18,20}
Q={3,6,9,12,15,18,21,24,27,30}
R={12,24,36,48,60}

def f(x):
    return (x not in a) <= (((x in P) and (x in Q)) <= (x in R))


for x in range(-512, 512):
    if f(x) == 0:
        a.add(x)


answer = 1

for ele in a:
    answer*=ele
print(answer)