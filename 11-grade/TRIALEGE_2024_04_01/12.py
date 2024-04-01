for x in range(256):
    for y in range(256):
        for z in range(256):
            origin = '0' + x*'1' + y*'2' + z*'3' + '0'
            origin2 = origin
            while '00' not in origin:
                origin = origin.replace('01','210', 1)
                origin = origin.replace('02','3101', 1)
                origin = origin.replace('03','2012', 1)

                # print(origin, origin2)
                if (origin.count('1') == 70) and (origin.count('2') == 56) and (origin.count('3') == 23):
                    print(len(origin2))



                    # 40




















            #26) 15 976339247
            #27) 9992901218 9999600004