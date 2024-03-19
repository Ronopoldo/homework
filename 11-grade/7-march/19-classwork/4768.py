P = [i for i in range(1, 99)]
Q = [i for i in range(25, 43)]
def func(x, A):
    return (x in Q) <= (((x not in P) and (x in Q)) <= (x in A))

answers = []
for A1 in range(0, 256):
    for A2 in range(A1, 257):
        A = [i / 4 for i in range(A1 * 4, (A2 * 4) + 1)]
        i = 0
        for x in range(100):
            if func(x, A):
                i += 1

        if i == 100:
            answers.append(max(A) - min(A))

print(min(answers))
