n, m = map(int, input().split())
lst = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, d = 0, 0, 0
cnt = 1

if n == 1 or m == 1:
        if n == 1:
            for i in range(m):
                lst[0][i] = i + 1
        else:
            for i in range(n):
                lst[i][0] = i + 1
else:
    while cnt <= n * m:
        lst[y][x] = cnt
        cnt += 1
        x += dx[d]
        y += dy[d]
        if x+dx[d] == m or y+dy[d] == n or lst[y+dy[d]][x+dx[d]] != 0:
            d = (d + 1) % 4

for row in lst:
    print(*row, sep=' ')