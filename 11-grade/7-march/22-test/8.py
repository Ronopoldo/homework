P = [i for i in range(69, 91)]
Q = [i for i in range(77, 115)]

def f(x, A):
    return (x in P) <= (not ((x in P) == (x in Q)) or ((x in Q) <= (x in A)))

answers = []

for A1 in range(0, 256):
    for A2 in range(A1, 257):
        i = 0
        A = [i for i in range(A1,A2)]
        for x in range(256):
            if f(x, A):
                i+=1
        if i == 256:
            answers.append(A2 - A1)
            break
            
print(min(answers))