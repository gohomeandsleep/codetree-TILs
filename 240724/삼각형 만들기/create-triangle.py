n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
 
res = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
                continue
            if lst[i][0] == lst[j][0] or lst[j][0] == lst[k][0] or lst[k][0] == lst[i][0]:
                if lst[i][1] == lst[j][1] or lst[j][1] == lst[k][1] or lst[k][1] == lst[i][1]:
                    res = max(res, abs(lst[i][0] * (lst[j][1] - lst[j][1]) + lst[j][0] * (lst[k][1] - lst[i][1]) + lst[k][0] * (lst[i][1] - lst[j][1])) / 2)

print(int(res * 2))