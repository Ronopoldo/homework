origin = '8' * 1000
while '999' in origin or '888' in origin:
    if '888' in origin:
        origin = origin.replace('888', '9',1)
    else:
        origin = origin.replace('999','8',1)

print(origin)


a = 1000 * '8'
while '999' in a or '888' in a:
    if '888' in a: a = a.replace('888','9',1)
    else: a = a.replace('999', '8', 1)

print(a)