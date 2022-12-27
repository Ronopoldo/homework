print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x == (not y)) <= ((x and w) == (x and (not w)))):
                    print(x,y,z,w)


#wzyx

# w z y x