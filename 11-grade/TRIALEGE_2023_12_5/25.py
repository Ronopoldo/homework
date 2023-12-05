def find5Dels(num):
    out = []
    for i in range(2, round(num ** 0.5)):
        if num % i == 0:
            out.append(i)
            out.append(num // i)
            # print(i)
        # if len(out) == 5:
        #     i = 42674824827842742
        #     break
    out = sorted(out)
    # print(out, len(out))
    if len(out)  >= 5:
        return out[-5]
    else:
        return 0
#

# print(sorted([2,1,3,4]))
# print(find5Dels(1000))
#
#
c = 0
for i in range(460000001, 9999999999):
    if find5Dels(i) > 0:
        print(find5Dels(i))
        c+=1
    if c == 5:
        break

#
















#
#
# 41818182
#
# 261959
#
# 5
#
# 271
#
# 57500001
