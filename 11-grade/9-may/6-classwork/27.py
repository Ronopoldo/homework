# s = list(map(int, open('27_A_2.txt').read().split('\n')))
# # s = [
# #     100, 300, 400, 9300, 800, 500, 9500
# # ]
# out = []
#
#
# def sumOfEl(inp):
#     ret = 0
#     for ele in inp:
#         ret += ele
#     return ret
#
#
# for x in range(len(s) - 1):
#     for y in range(x, len(s)):
#         tmp = s[x:y + 1]
#         if ((sumOfEl(tmp) % 263) == 0):
#             out.append(len(tmp))
#             if len(tmp) == 579:
#                 print(tmp)
#
# print(max(out))
#
# # 390










# s = list(map(int, open('2_27_B.txt').read().split('\n')))
# # s = [
# #     100, 300, 400, 9300, 800, 500, 9500
# # ]
# out = [1746300]
#
#
# def sumOfEl(inp):
#     ret = 0
#     for ele in inp:
#         ret += ele
#     return ret
#
#
#
#
# for x in range(len(s) - 1):
#     for y in range(len(s), x + max(out), -1):
#         tmp = s[x:y]
#         if ((sumOfEl(tmp) % 263) == 0):
#             out.append(len(tmp))
#             # y = x + max(out)
#             break
#         # print(y)
#
#     print(x/len(s) * 100)
# print(max(out), len(out))

# 390


arr = list(map(int, open('2_27_B.txt').read().split('\n')))
def longest_subarray(arr, k):
    prefix_sum = {0: -1}
    curr_sum = 0
    max_len = 0

    for i, num in enumerate(arr):
        curr_sum += num
        mod = curr_sum % k

        if mod in prefix_sum:
            max_len = max(max_len, i - prefix_sum[mod])

        if mod not in prefix_sum:
            prefix_sum[mod] = i

    print(prefix_sum)
    return max_len

k = 263
result = longest_subarray(arr, k)
print(result)
