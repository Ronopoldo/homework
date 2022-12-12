print('y x z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((x <= y) and (z or w)) <= ((x == w) or (y and not z))):
                    print(y,x,z,w)


                    # Y X W Z