from itertools import combinations

k = 0
q = {2, 4, 8, 10}
p= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
def f(x):
    return ((x in q) <= (x in a)) and ((x in a) <= (x in p))

for i in range(1, 11):
    for a in combinations(p, i):
        if all(f(x) for x in p):
            k += 1
print(k)