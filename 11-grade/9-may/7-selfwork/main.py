# arr = list(map(int, open('2_27_B.txt').read().split('\n')))
# def longest_subarray(arr, k):
#     prefix_sum = {0: -1}
#     curr_sum = 0
#     max_len = 0
#
#     for i, num in enumerate(arr): # enumerate([a,b,c,d]) => [(0, a),(1, b),(2, c),(3, d)] - нумерует элементы
#         curr_sum += num
#         mod = curr_sum % k
#
#         if mod in prefix_sum:
#             max_len = max(max_len, i - prefix_sum[mod])
#
#         if mod not in prefix_sum:
#             prefix_sum[mod] = i
#             print('AE' + prefix_sum)
#
#     print(prefix_sum)
#     return max_len
#
# k = 263
# result = longest_subarray(arr, k)
# print(result)


print('abcde'[-1::1])

i = 'abcdef'

i[2] = 'G'
print(i)