i = 0
for j in range(2):
    for k in range(2):
        for l in range(2):
            for m in range(2):
                for n in range(2):
                    if int(j and (not k) and l and (not m) and (n or (not n))) == 0:
                        i += 1

print(i)