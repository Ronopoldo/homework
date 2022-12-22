for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    for x6 in range(2):
                        for x7 in range(2):
                            # F = int(x1 and (x2 <= x3) and x4 and x5 and x6 and (not x7))
                            # F = int((not x1) or ((not x2) <= x3) or (not x4) or (not x5) or x6 or (not x7))
                            F = int((not x1) and (x2 <= (not x3)) and x4 and x5 and (not x6) and x7)
                            if (x4 == 1 and x6 == 0 and F == 1):
                                print('1/3')
                            if (x4 == 0 and x7 == 0 and F == 0):
                                print('2/3')
                            if (x1 == 0 and x4 == 1 and F == 0):
                                print('3/3')
