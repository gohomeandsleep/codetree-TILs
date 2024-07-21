n, m = map(int, input().split())
lst = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y, d = 0, 0, 0
cnt = 0
written = 0
if n == 1 or m == 1:
        if n == 1:
            for i in range(m):
                lst[0][i] = chr((cnt + i) % 26 + 65)
        else:
            for i in range(n):
                lst[i][0] = chr((cnt + i) % 26 + 65)
else:
    while written < n * m:
        lst[y][x] = chr(cnt + 65)
        cnt = (cnt + 1) % 26
        x += dx[d]
        y += dy[d]
        written += 1
        if x+dx[d] == m or y+dy[d] == n or lst[y+dy[d]][x+dx[d]] != 0:
            d = (d + 1) % 4

for row in lst:
    print(*row, sep=' ')