for A in range(1024):
    count = 0
    for x in range(256):
        for y in range(256):
            if (x + 2*y < A) or (y > x) or (x > 60):
                count+=1

    if count == 65536:
        print(A)
        break
        A = 427894