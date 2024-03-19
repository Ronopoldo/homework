P = [i for i in range(2, 20)]
Q = [i for i in range(15, 25)]

def func(x, A):
    return (((x not in A) <= (x not in P))) or (x in Q)

answers = []
for A1 in range(0, 256):
    for A2 in range(A1, 257):
        A = [i / 4 for i in range(A1 * 4, (A2 * 4) + 4)]
        i = 0
        for x in range(100):
            if func(x, A):
                i += 1

        if i == 100:
            answers.append(max(A) - min(A))

print(min(answers))
