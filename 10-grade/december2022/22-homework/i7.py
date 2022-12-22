while True:
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())
    x4 = int(input())
    x5 = int(input())
    x6 = int(input())

    print(int((x1 and x2) or (x3 and x4) or (x5 and x6)))
    print()
    print(int((x2 and x4) or (x4 and x6) or (x6 and x2)))