from itertools import permutations

print(sorted(list('РУСЛАН')))

i = 0

for word in permutations('АЛНРСУ'):
    i+=1
    if i == 442:
        print(word)

       #РСЛНУА



#
#
#
# print(sorted(list('ЫЛВЫ')))