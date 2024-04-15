B = [i for i in range(24, 91)]
C = [i for i in range(47, 116)]

def f(A, x):
    return (x in C) <= ((not(x in A) and (x in B)) <= (not(x in C)))


answers = []


for s in range(1, 255):

    for e in range(s, 256):
        i = 0
        A = [i for i in range(s, e)]
        for x in range(256):

            # print(A)
            if f(A,x):
                i+=1

        if i == 256:
            answers.append(len(A))
            print(max(answers))

print(max(answers))