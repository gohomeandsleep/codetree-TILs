n, h, t = map(int, input().split())
lst = list(map(int, input().split()))

res = float('inf')
for i in range(n - t + 1):
    tmp = lst[i:i+t+1]
    cnt = 0
    for j in range(i, i+t):
        cnt += abs(h - lst[j])
    res = min(res, cnt)
print(res)