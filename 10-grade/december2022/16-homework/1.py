print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x == (y <= z)) and ((not w) <= (x == y)):
                    print(x, y, z, w)


                    # y/w y/w z/x z/x
                    # y y/w z z/x
                    # y w z x