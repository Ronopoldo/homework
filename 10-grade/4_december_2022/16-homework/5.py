print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x and (not y)) == (z or not w)) <= (x and z):
                    print(x, y, z, w)


                    # y/x (z) (w) y/x
                    # y (z) (w) x