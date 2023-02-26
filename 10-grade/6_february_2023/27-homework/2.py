print('z y x')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((x <= y) == (z <= w)) or (x and w)):
                    print(z,y,x)




# z y x w

# zyxw (ПРОВЕРЕНО)