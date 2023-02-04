print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x <= y) == (w <= x)) and (z <= w):
                    print(x, y, z, w)


                    # x/y z/w z/w x/y
                    # y z w x