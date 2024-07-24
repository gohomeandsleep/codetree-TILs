n, m = map(int, input().split())
lst = list(map(int, input().split()))

mxm = 0
for i in range(n): #start point
    tmp = lst[i]
    k = lst[i]
    for j in range(m - 1):
        tmp += lst[k - 1]
        k = lst[k - 1]
    #print(tmp)
    mxm = max(mxm, tmp)

print(mxm)