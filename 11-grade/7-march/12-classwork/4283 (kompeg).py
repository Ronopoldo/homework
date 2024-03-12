a = set()
P={1,3,4,9,11,13,15,17,19,21}
Q={3,6,9,12,15,18,21,24,27,30}

def f(x):
    return ((x in P) <= (x in a)) or ((x not in a) <= (x not in Q))


for x in range(-512, 512):
    if f(x) == 0:
        a.add(x)


answer = 1

for ele in a:
    answer*=ele
print(answer)