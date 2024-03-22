P = [i for i in range(24, 78)]
Q = [i for i in range(47, 93)]
R = [i for i in range(82, 117)]

def f(x, A):
    return ((x not in P) <= ((x in P) or (x in R))) <= ((x not in A) <= (x not in Q))


answers = []

for A1 in range(0, 256):
    for A2 in range(A1, 257):
        i = 0
        A = [i for i in range(A1, A2)]
        for x in range(256):
            if f(x, A):
                i += 1
        if i == 256:
            answers.append(A2 - A1)
            break

print(min(answers))