n = int(input())
lst = list(map(int, input().split()))

res = float('inf')
for i in range(n):
    tmp = lst[:]
    tmp[i] *= 2
    for j in range(n):
        tmpp = tmp[:]
        tmpp.pop(j)
        cnt = 0
        for k in range(n-2):
            cnt += abs(tmpp[k+1] - tmpp[k])
        #print(tmpp)
        res = min(res, cnt)
print(res)