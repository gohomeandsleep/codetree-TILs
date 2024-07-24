n, b = map(int, input().split())
lst = [int(input()) for _ in range(n)]

mxm = 0
for i in range(n):
    tmp = lst[:]
    tmp[i] = tmp[i] // 2
    tmp.sort()
    budget = b
    j = 0
    cnt = 0
    while budget >= 0 and j < n:
        budget -= tmp[j]
        j += 1
        cnt += 1
    if j == n:
        mxm = cnt
        break
    else:
        mxm = max(mxm, cnt - 1)
print(mxm)