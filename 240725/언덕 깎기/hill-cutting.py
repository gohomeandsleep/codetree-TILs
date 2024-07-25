n = int(input())
lst = [int(input()) for _ in range(n)]

res = float('inf')
for i in range(101): #stp
    for j in range(i, 101): #endp
        if j - i > 17:
            continue
        tmp = 0
        for k in range(n):
            if lst[k] < i:
                tmp += (lst[k] - i) ** 2
            elif lst[k] > j:
                tmp += (lst[k] - j) ** 2
        res = min(tmp, res)
print(res)