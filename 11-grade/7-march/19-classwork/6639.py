P = [i for i in range(5, 54)]
Q = [i for i in range(50, 93)]

def func(x, A):
    return (x not in P) and (x in Q) <= (x > A)

answers = []
for A in range(0, 512):
    i = 0
    for x in range(256):
        if func(x, A) == 0:
            i += 1
    if i == 20:
        answers.append(A)

print(min(answers))
