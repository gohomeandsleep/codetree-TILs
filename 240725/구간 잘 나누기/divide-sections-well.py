import itertools

n, k = map(int, input().split())
lst = list(map(int, input().split()))
lstk = [i+1 for i in range(n-1)]
partition = itertools.combinations(lstk, k-1)

res = float('inf')
for p in partition:
    tmp_p = list(p)
    tmp = 0
    maxp = 0
    for i in range(k-1):
        maxp = max(maxp, sum(lst[tmp:tmp_p[i]]))
        tmp = tmp_p[i]
    maxp = max(maxp, sum(lst[tmp:]))
    res = min(res, maxp)
print(res)