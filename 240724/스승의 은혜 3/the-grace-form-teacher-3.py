n, b = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

mxm = 0
for i in range(n):
    tmp = lst[:]
    tmp[i][0] = tmp[i][0] // 2
    cost = []
    for j in range(n):
        cost.append(tmp[j][0] + tmp[j][1])
    #print(cost)
    cost.sort()
    budget = b
    j = 0
    cnt = 0
    while budget >= 0 and j < n:
        budget -= cost[j]
        j += 1
        cnt += 1
    tmp[i][0] = tmp[i][0] * 2
    if j == n and budget >= 0:
        mxm = cnt
        break
    else:
        mxm = max(mxm, cnt - 1)
print(mxm)