P = [i for i in range(130, 172)]
Q = [i for i in range(150, 186)]

def f(A, x):
    return (x in P) <= (((x in Q) and not(x in A)) <= (not(x in P)))


mini = 1024

for a1 in range(1, 255):
    for a2 in range(a1, 256):
        temp = 0
        for x in range(512):
            A = [i for i in range(a1, a2 + 1)]
            if f(A, x) == True:
                temp+=1
            if len(A) > mini:
                break

        if temp == 512:
            mini = min(mini, len(A))
            print(mini)