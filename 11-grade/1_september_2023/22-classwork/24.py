s = open('../../Desktop/24_2024.txt').readline()

counter = 0
tempvar = 0
countermax = 0


for t in range(len(s) - 100):
    t_counter = 0
    counter = 0
    active = False
    while active == False:
        for i in range(tempvar, len(s) - 100):
            if s[i] == 'T' and t_counter == 0:
                tempvar = t
            if s[i] == 'T':
                t_counter += 1
            if t_counter != 0:
                counter = counter + 1
            if t_counter == 101:
                active = True
                break
    counter -= 1
    countermax = max(countermax, counter)
    print(f'Максимально найденная длина: {countermax}; Номер текущей буквы: {tempvar}; Текущая найденная длина 100 Т: {counter}')

# 133


# tempCounterFinal = 0
# for i in range(0, len(s)):
#     if s[i] == 'T':
#         tempCounterFinal +=1
