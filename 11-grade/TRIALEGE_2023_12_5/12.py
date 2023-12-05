s = '1' * 85

while '11111' in s:
    s = s.replace('111', '2', 1)
    s = s.replace('222', '1', 1)


print(s)