n = int(input())

lst = [[0] * 200 for _ in range(200)]
for i in range(n):
    stpx, stpy, endpx, endpy = map(int, input().split())
    if i % 2 == 0:
        marker = 1
    else:
        marker = 2
    for i in range(100+stpy, 100+endpy):
        for j in range(100+stpx, 100+endpx):
            lst[i][j] = marker

res = 0
for i in range(200):
    for j in range(200):
        if lst[i][j] == 2:
            res += 1

print(res)