glass = 'АУОИЭЫЯЮЕЁауоиэыяюеё'

inp = str(input())

flag = False

for letterID in range(1, len(inp)):
    if inp[letterID] in glass:
        if inp[letterID - 1] != ' ':
            if flag:
                inpl = list(inp)
                tmp = inpl[letterID ]
                inpl[letterID] = inp[letterID - 1]
                inpl[letterID - 1] = tmp
                inp = ''.join(inpl)

        flag = not flag
print(inp)