n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
res = float('inf')
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        res = min(res, (lst[i][0] - lst[j][0]) ** 2 + (lst[i][1] - lst[j][1]) ** 2)
print(res)