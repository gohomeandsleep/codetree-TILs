n = int(input())
lst = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

x, y, d = n-1, n-1, 0
cnt = n * n

if n == 1:
    lst[0][0] = 1
else:
    while cnt > 0:
        lst[y][x] = cnt
        cnt -= 1
        x += dx[d]
        y += dy[d]
        if x+dx[d] == n or y+dy[d] == n or lst[y+dy[d]][x+dx[d]] != 0:
            d = (d + 1) % 4

for row in lst:
    print(*row, sep=' ')