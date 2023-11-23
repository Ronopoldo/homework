

for x in range(32):
    for y in range(32):
        for z in range(32):
            input = '0' + '1' * x + '2' * y + '3' * z + '0'
            origin = input
            while '00' not in input:
                input = input.replace('01', '210', 1)
                input = input.replace('02', '3101', 1)
                input = input.replace('03', '2012', 1)
            if (input.count('1') == 61) and (input.count('2') == 50) and (input.count('3') == 18):
                print(len(origin), origin)