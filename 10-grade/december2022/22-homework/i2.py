for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    for x6 in range(2):
                        F = int(x1 and x2 and x3 and (not x4) and x5 and (not x6))
                        # F = int((not x1) or x2 or x3 or x4 or x5 or (not x6))
                        if (x1 == 0 and x2 == 1 and F == 0):
                            print('1/3')
                        if (x3 == 1 and x4 == 1 and F == 0):
                            print('2/3')
                        if (x5 == 1 and x6 == 0 and F == 1):
                            print('3/3')