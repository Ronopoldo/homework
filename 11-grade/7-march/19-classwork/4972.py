P = [i for i in range(25, 51)]
Q = [i for i in range(54, 76)]
def func(x, A):
    return (x in Q) <= (((x in P) == (x in Q)) or ((x not in P) <= (x in A)))

answers = []
for A1 in range(0, 256):
    for A2 in range(A1, 257):
        A = [i / 4 for i in range(A1 * 4, (A2 * 4))]
        i = 0
        for x in range(100):
            if func(x, A):
                i += 1

        if i == 100:
            # print(max(A), min(A))
            answers.append(max(A) - min(A))

print(min(answers))
