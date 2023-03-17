for x in range(47):
    for y in range(47):
        for z in range(47):
            s = "0" + "1" * x + "2" * y + "3" * z
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '3103', 1)
                s = s.replace('03', '1201' , 1)
            if (s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46):
                print(x,y,z)
