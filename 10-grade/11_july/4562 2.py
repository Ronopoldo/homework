def find_s(list_to_check, item_to_find):
    indecces = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indecces.append(idx)
    return indecces
a = set()

from itertools import *

for i in product('CNOST', repeat = 5):
    i = ''.join(i)
    a_list = [p for p in i]
    count=0

    if ((i[0] != 'S') and (i[4] != 'S' )):
        temp = False
        for j in range(0,4):
            if (i[j] == i[j+1]):
                temp = True
        if temp == False:
            for k in (find_s(a_list, 'S')):
                if i[k-1] != i[k+1]:
                    a.add(i)

print(len(a))