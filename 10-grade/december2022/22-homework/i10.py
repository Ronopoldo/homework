i = 0
for j in range(2):
    for k in range(2):
        for l in range(2):
            for m in range(2):
                for n in range(2):
                    if int( ((j <= k) <= (m and n and l)) and ((j and (not k)) <= (not(m and n and l))) and (m <= j) ) == 1:
                        i += 1

print(i)