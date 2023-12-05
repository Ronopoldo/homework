s = list(map(int, open('27-B.txt')))

def f(arr, b, e):
    out = 0
    for i in range(b, e + 1):
        out += arr[i]

    return(out)


count = 0
for x in range(len(s) - 1):
    for y in range(x, len(s)):
        if f(s, x, y) % 999 == 0:
            count+=1



print(count)


# 403