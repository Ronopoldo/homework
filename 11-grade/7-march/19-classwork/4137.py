Q = [i for i in range(29, 48)]


def deli(n, m):
    return n % m == 0
def func(x, A):
    return ((not deli(x, 3)) and (x not in [48, 52, 56])) <= ((abs(x - 50) <= 7) <= (x in Q)) or (x & A == 0)
answers = []
for A in range(1, 1024):
    i = 0
    for x in range(1,101):
        if func(x, A):
            i+=1

    if i == 100:
        answers.append(A)

print(min(answers))
