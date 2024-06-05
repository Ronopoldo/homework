for N in range(1000, 100, -1):
    Nstr = str(N)
    arr = [(int(Nstr[0]) * int(Nstr[1])), int(Nstr[1]) * int(Nstr[2])]
    if ''.join([str(min(arr)), str(max(arr))]) == '621':
        print(N)