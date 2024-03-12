a = set()
P = {1, 12}
Q = { 12, 13, 14, 15, 16 }

def f(x):
    return (not (x in a)) <= (not(x in P)) and (not (x in Q))


for x in range(-512, 512):
    if f(x) == 0:
        a.add(x)

print(len(a), a)