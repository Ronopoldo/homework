from itertools import *



days = product('234', repeat = 3)

iglobal = 0
for day in days:
    i = 0
    for tea in combinations('A147', int(day[0])):
        active = 0
        if '1' in tea:
            active+=1
        i+=1
        active1 = active
        for tea1 in combinations('A147', int(day[1])):
            if '1' in tea1:
                active+=1
            print(tea1)
            i+=1
            active2 = active1


            for tea2 in combinations('A147', int(day[2])):
                if '1' in tea2:
                    active+=1
                i+=1

                if active > 1:
                    iglobal+=i
                    active = active2
    print(day)



print(iglobal)