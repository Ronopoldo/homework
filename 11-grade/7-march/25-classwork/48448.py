# s = list(map(int, open('4844b.txt').read().split('\n')))
#
# ostArr = [0] * 1024
#
# print(ostArr)
#
# for ele in s:
#     ostArr[ele % 1]



f = open("4844b.txt")
n=int(f.readline())
a = [[0]*11 for i in range(3)]
for i in range(n):
    x=int(f.readline())
    j=x%3
    k=0
    while x%2 == 0:
        k += 1
        x //= 2
        if k == 10: break
    a[j][k] += 1
k=sum(a[0][i]*(a[0][i]-1)//2 for i in range(5,11))
k+=sum(a[0][i]*a[0][j] for i in range(11) for j in range(max(i+1,10-i),11))
k+=sum(a[1][i]*a[2][j] for i in range(11) for j in range(10-i,11))
print(k)