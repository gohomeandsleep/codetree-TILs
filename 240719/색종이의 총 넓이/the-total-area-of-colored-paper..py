lst = [[0] * 200 for _ in range(200)]
n = int(input())
for _ in range(n):
    x, y = map(int,input().split())
    for i in range(100+y, 108+y):
        for j in range(100+x, 108+x):
            lst[i][j] = 1

res = 0
for i in range(200):
    for j in range(200):
        if lst[i][j] == 1:
            res += 1
print(res)