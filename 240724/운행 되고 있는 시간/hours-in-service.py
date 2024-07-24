n = int(input())
lst = []
mxm = 0
for _ in range(n):
    a, b = map(int, input().split())
    mxm = max(mxm, b)
    lst.append([a,b])

res = 0
for i in range(n):
    tmp = lst.pop(0)
    line = [0 for _ in range(mxm + 1)]
    for j in range(n - 1):
        for k in range(lst[j][0], lst[j][1]):
            line[k] = 1
    res = max(res, sum(line))
    lst.append(tmp)

print(res)