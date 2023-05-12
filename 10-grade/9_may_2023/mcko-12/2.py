def f(a,b,c):
    return a and not b or not c
           # 1  5   6   2 4 6  3
print('A B C F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            print(a,b,c,int(f(a,b,c)))