for k in range(2):
    for l in range(2):
        for m in range(2):
            for n in range(2):
                if (int((k <= m) or (l and k) or (not n))) == 0:
                    print(k,l,m,n)
