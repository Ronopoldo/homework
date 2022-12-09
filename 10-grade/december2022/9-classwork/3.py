# x z w y
# xzwy
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) == (y <= z)) and (y or w)) == 1:
                    print(x,y,z,w)

'''
x y z w
0 0 1 1
0 1 1 1
'''