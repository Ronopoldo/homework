def cinema(n):
    obj = {}

    for i in range(0, n):
        row, seat, price = input().split()
        key = row, seat

        if key in obj:
            obj[key].add(price)
        else:
            obj[key] = {price}

    for key in obj:
        row, seat = key
        print(f'{row} {seat} – {len(obj[key])}')


n = int(input('n: '))

cinema(n)

'''
1 1 1000
1 1 1000
1 2 2000
1 2 3000
'''
