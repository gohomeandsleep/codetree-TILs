n, m = map(int, input().split()) #n:세로, m:가로
lst = [list(map(int, input().split())) for _ in range(n)]

res = 0

#1x3
for i in range(n):
    for j in range(m-2):
        res = max(res, lst[i][j] + lst[i][j+1] + lst[i][j+2])

#3x1
for i in range(n-2):
    for j in range(m):
        res = max(res, lst[i][j] + lst[i+1][j] + lst[i+2][j])

for i in range(n-1):
    for j in range(m-1):
        res = max(res, lst[i][j] + lst[i+1][j] + lst[i+1][j+1])

for i in range(n-1):
    for j in range(m-1):
        res = max(res, lst[i][j] + lst[i+1][j] + lst[i][j+1])

for i in range(n-1):
    for j in range(m-1):
        res = max(res, lst[i][j] + lst[i][j+1] + lst[i+1][j+1])

for i in range(n-1):
    for j in range(m-1):
        res = max(res, lst[i+1][j] + lst[i][j+1] + lst[i+1][j+1])

print(res)