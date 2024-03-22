# https://inf-ege.sdamgia.ru/test?id=15455326&nt=True&pub=False


def f(x, y, A):
    return ((x + 2 * y) < A) or (y > x) or (x > 30)

for A in range(128):
    i = 0
    for x in range(256):
        for y in range(256):
            if f(x, y, A):
                i+=1
    if i == 256**2:
        print(A)