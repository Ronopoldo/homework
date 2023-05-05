arr = []
for i in range(193136, 193224):
    arr.append(i)


def div(x):
    dels = []
    for m in range(1, x+1):
        if not x % m:
            dels.append(m)
    return(dels)


for l in arr:
    if len(div(l)) == 6:
        print(div(l)[4], div(l)[5])