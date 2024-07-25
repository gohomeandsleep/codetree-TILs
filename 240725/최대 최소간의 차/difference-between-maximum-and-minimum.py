n, k = map(int, input().split())
lst = list(map(int, input().split()))

res = float('inf')
for i in range(1, 10001):
    stp = i
    endp = i + k
    cost = 0
    for j in range(n):
        if lst[j] < stp:
            cost += stp - lst[j]
        elif lst[j] > endp:
            cost += lst[j] - endp
    res = min(res, cost)
print(res)