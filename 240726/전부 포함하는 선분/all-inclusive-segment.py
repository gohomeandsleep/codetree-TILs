n = int(input())
lst = [list((map(int, input().split()))) for _ in range(n)]

res = float('inf')
for i in range(n):
    tmp = lst.pop(0)
    stp = 100
    endp = 0
    for j in range(n - 1):
        stp = min(stp, lst[j][0])
        endp = max(endp, lst[j][1])

    res = min(res, endp - stp)
    lst.append(tmp)
print(res)