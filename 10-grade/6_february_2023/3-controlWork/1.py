print('x y z w')
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((y <= z) or ((not x) and (not w)) == (w == z)) == 1:
                    print(x,y,z,w)

                    # zwyx