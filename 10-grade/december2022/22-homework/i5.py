while True:
    x = int(input())
    y = int(input())
    z = int(input())
    print(int((x == z) and ((not x) <= y)))
    print(int((not(x) == z) and ((not x) <= y)))
    print(int(((not x) == z) and ((not x) <= y)))
    print(int((x == z) and (not(y <= z))))